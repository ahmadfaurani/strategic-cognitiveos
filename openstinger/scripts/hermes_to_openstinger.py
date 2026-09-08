#!/usr/bin/env python3
"""
hermes_to_openstinger.py — Hermes state.db → OpenStinger "hermes-sessions" namespace.

Reads role=user|assistant messages from Hermes' SQLite message store (READ-ONLY,
mode=ro URI) and emits flat JSONL episodes for OpenStinger's SessionReader.

Modes:
  --drain N     Staggered historical backfill: export up to N messages per run,
                oldest-first, resumable via state file (last exported message id).
  --follow      Live tail: export everything newer than the drain watermark.
                Used by the recurring cron job after backfill completes.

Output: {sessions_dir}/hermes-sessions.jsonl   (one JSON object per line)
State:  .hermes_export_state.json next to this script.

Episode shape (SessionReader "simple" format):
  {"content": "...", "source": "hermes:<session_id>:<role>", "valid_at": <unix>}

Safety:
  - SQLite opened with ?mode=ro (cannot write, cannot lock writer)
  - Skips empty/compacted/system messages; truncates >8k chars (extraction sanity)
  - Fingerprint guard: sha256 content hash per message, never re-exported
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sqlite3
import sys
import time
from pathlib import Path

STATE_DB = Path("/home/p62operator/.hermes/state.db")
SESSIONS_DIR = Path("/home/p62operator/.openclaw/workspace/research-stack/sessions")
OUT_FILE = SESSIONS_DIR / "hermes-sessions.jsonl"
STATE_FILE = Path(__file__).resolve().parent / ".hermes_export_state.json"
MAX_CHARS = 8000


def load_state() -> dict:
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text())
    return {"last_id": 0, "content_hashes": [], "done": False}


def save_state(st: dict) -> None:
    STATE_FILE.write_text(json.dumps(st))


def fingerprint(content: str) -> str:
    return hashlib.sha256(content.encode("utf-8")).hexdigest()[:16]


def fetch_batch(last_id: int, limit: int) -> list[dict]:
    con = sqlite3.connect(f"file:{STATE_DB}?mode=ro", uri=True)
    con.row_factory = sqlite3.Row
    try:
        rows = con.execute(
            """
            SELECT id, session_id, role, content, timestamp
            FROM messages
            WHERE id > ? AND role IN ('user','assistant')
              AND (compacted IS NULL OR compacted = 0)
              AND (active IS NULL OR active = 1)
            ORDER BY id ASC
            LIMIT ?
            """,
            (last_id, limit),
        ).fetchall()
        return [dict(r) for r in rows]
    finally:
        con.close()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--drain", type=int, default=0,
                    help="max messages to export this run (staggered backfill)")
    ap.add_argument("--follow", action="store_true",
                    help="export all messages newer than watermark (live tail)")
    args = ap.parse_args()

    if not STATE_DB.exists():
        print(f"ALERT — state.db not found at {STATE_DB}")
        return 1

    st = load_state()
    seen = set(st.get("content_hashes", []))

    if args.drain and st.get("done"):
        print("DRAIN COMPLETE (state says finished)")
        return 0

    if args.follow and not st.get("done"):
        # Safety interlock: follow mode bypasses staggered pacing (unbounded export).
        # Only allowed once the historical backfill drain has completed.
        print("FOLLOW BLOCKED — backfill drain incomplete; run with --drain (cron owns pacing)")
        return 1

    limit = args.drain if args.drain else 10_000_000  # follow = unbounded
    rows = fetch_batch(st["last_id"], limit)

    SESSIONS_DIR.mkdir(parents=True, exist_ok=True)
    exported = 0
    new_hashes: list[str] = []
    last_id = st["last_id"]
    skipped_dup = 0
    skipped_empty = 0

    with OUT_FILE.open("a", encoding="utf-8") as f:
        for r in rows:
            last_id = r["id"]
            content = (r["content"] or "").strip()
            if not content:
                skipped_empty += 1
                continue
            if len(content) > MAX_CHARS:
                content = content[:MAX_CHARS] + " …[truncated]"
            fp = fingerprint(content)
            if fp in seen:
                skipped_dup += 1
                continue
            seen.add(fp)
            new_hashes.append(fp)
            f.write(json.dumps({
                "content": content,
                "source": f"hermes:{r['session_id']}:{r['role']}",
                "valid_at": int(r["timestamp"] or time.time()),
            }, ensure_ascii=False) + "\n")
            exported += 1

    st["last_id"] = last_id
    st["content_hashes"] = (st.get("content_hashes", []) + new_hashes)[-20000:]
    if args.drain and not rows:
        st["done"] = True
    save_state(st)

    # Drain progress report
    total_remaining = None
    try:
        con = sqlite3.connect(f"file:{STATE_DB}?mode=ro", uri=True)
        total_remaining = con.execute(
            "SELECT COUNT(*) FROM messages WHERE id > ? AND role IN ('user','assistant')",
            (last_id,),
        ).fetchone()[0]
        con.close()
    except Exception:
        pass

    if args.drain:
        print(f"DRAINED {exported} msgs (dup={skipped_dup} empty={skipped_empty}) "
              f"watermark={last_id} remaining={total_remaining}")
    else:
        print(f"FOLLOW {exported} msgs (dup={skipped_dup}) watermark={last_id} remaining={total_remaining}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
