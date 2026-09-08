#!/usr/bin/env python3
"""
gai_to_openstinger.py — CJ-GAI collection → OpenStinger "simple" JSONL exporter.

Converts the latest N daily/weekly collection markdown files from the gov-ai
workspace into JSONL episodes OpenStinger's SessionReader can ingest
({"content": str, "source": str, "valid_at": unix_seconds} per line).

One section = one episode (Signal Register tiers), falling back to the whole
file as a single episode when no sections parse. Idempotent via a state file
tracking processed (path, mtime) pairs.

Usage: gai_to_openstinger.py [--days N]
"""
import argparse
import json
import re
import sys
import time
from pathlib import Path

GAI_COLLECTION = Path("/home/p62operator/.openclaw/workspace-gov-ai/collection")
OUT_DIR = Path("/home/p62operator/.openclaw/workspace/research-stack/sessions")
OUT_FILE = OUT_DIR / "gai-collection.jsonl"
STATE_FILE = Path("/home/p62operator/.openclaw/workspace/research-stack/.gai_export_state.json")
TLP_RE = re.compile(r"Classification:\s*(TLP:[A-Z]+)", re.IGNORECASE)
SECTION_RE = re.compile(r"^###\s+.*", re.MULTILINE)


def load_state() -> dict:
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text())
    return {}


def content_fingerprint(ep: dict) -> str:
    """Stable hash of episode content (excluding valid_at/mtime)."""
    import hashlib
    return hashlib.sha256(ep["content"].encode("utf-8")).hexdigest()[:16]


def save_state(state: dict) -> None:
    STATE_FILE.write_text(json.dumps(state, indent=1))


def extract_tlp(text: str) -> str:
    m = TLP_RE.search(text[:600])
    return m.group(1).upper() if m else "TLP:AMBER"


def file_to_episodes(path: Path) -> list[dict]:
    """Split one collection markdown file into episode dicts."""
    text = path.read_text(encoding="utf-8", errors="replace")
    tlp = extract_tlp(text)
    valid_at = int(path.stat().st_mtime)

    # Section split: ### headings inside the Signal Register
    sections = re.split(r"(?=^###\s+)", text, flags=re.MULTILINE)
    episodes: list[dict] = []
    for sec in sections:
        sec = sec.strip()
        if len(sec) < 80:  # skip headers/fragments
            continue
        # Episode content = section heading + body; prefix file context
        header = sec.splitlines()[0][:120]
        body = sec[:4000]
        episodes.append({
            "content": f"[{path.name} | {tlp}] {header}\n{body}",
            "source": "cj-gai-collection",
            "valid_at": valid_at,
        })
    if not episodes:  # fallback: whole file as one episode
        episodes.append({
            "content": f"[{path.name} | {tlp}]\n{text[:6000]}",
            "source": "cj-gai-collection",
            "valid_at": valid_at,
        })
    return episodes


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=7, help="lookback window")
    args = ap.parse_args()

    cutoff = time.time() - args.days * 86400
    candidates = sorted(
        p for p in GAI_COLLECTION.rglob("*.md")
        if p.stat().st_mtime >= cutoff
    )
    if not candidates:
        print("NO NEW FILES")
        return 0

    state = load_state()
    seen_hashes = set(state.get("content_hashes", []))
    new_eps: list[dict] = []
    new_hashes: list[str] = []
    for p in candidates:
        key = f"{p}:{p.stat().st_mtime}"
        if state.get("processed", {}).get(key):
            continue
        for ep in file_to_episodes(p):
            fp = content_fingerprint(ep)
            if fp in seen_hashes:
                continue  # same content re-exported under new mtime — skip
            new_eps.append(ep)
            new_hashes.append(fp)
        state.setdefault("processed", {})[key] = int(time.time())

    if not new_eps:
        print("NO NEW EPISODES (all processed)")
        return 0

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    with OUT_FILE.open("a", encoding="utf-8") as f:
        for ep in new_eps:
            f.write(json.dumps(ep, ensure_ascii=False) + "\n")
    state.setdefault("content_hashes", []).extend(new_hashes)
    state["content_hashes"] = state["content_hashes"][-5000:]  # bound growth
    save_state(state)
    print(f"EXPORTED {len(new_eps)} episodes from {len(candidates)} files -> {OUT_FILE.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
