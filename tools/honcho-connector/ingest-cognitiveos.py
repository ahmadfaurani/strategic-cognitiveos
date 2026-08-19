#!/usr/bin/env python3
"""
Batch ingest CognitiveOS records from strategic-cognitiveos repo into Honcho.
Parses markdown files with YAML frontmatter, maps to sessions, batch-uploads.
"""
import os, sys, re, json, time, requests
from pathlib import Path
from datetime import datetime

HONCHO_URL = "http://localhost:8000"
WORKSPACE = "cognitiveos"
BATCH_SIZE = 50
REPO_PATH = os.environ.get(
    "COGNITIVEOS_REPO",
    "/home/p62operator/.openclaw/workspace/strategic-cognitiveos",
)

# Directories to ingest (excluding cron-output, projects, schemas, etc.)
RECORD_DIRS = [
    "initiatives",    # INIT
    "decisions",      # DEC
    "actions",        # ACT
    "risks",          # RSK
    "stakeholders",   # STK
    "intelligence",   # INT
    "outcomes",       # OUT
    "commitments",    # COM
    "conversations",  # CONV (created Aug 19)
    "engagements",    # ENG
    "assessments",    # ASS
    "briefings",      # BRF
    "documents",      # DOC
]

# Record type prefix mapping
PREFIX_MAP = {
    "INIT": "initiative",
    "DEC": "decision",
    "ACT": "action",
    "RSK": "risk",
    "STK": "stakeholder",
    "INT": "intelligence",
    "OUT": "outcome",
    "COM": "commitment",
    "CONV": "conversation",
    "ASS": "assessment",
    "BRF": "briefing",
    "DOC": "document",
}

# Session routing rules (keyword → session_id)
SESSION_MAP = [
    (["PERJASA", "perjasa"], "sovereign-ai-perjasa"),
    (["R.I.S.I.K", "RISIK", "risik", "UiTM", "uitm"], "risk-uitm"),
    (["CyberDSA", "cyberdsa", "CYBERDSA"], "cyberdsa-2026"),
    (["CSM", "csm", "NACSA", "nacsa"], "csm-partnership"),
    (["GovSec", "govsec", "Voron", "voron", "ChainSentry", "chainsentry",
      "VoronDRQ", "VoronCitadel", "productisation", "dev freeze"], "productisation"),
    (["TH-RCI", "Tabung Haji", "tabung haji", "TH RCI", "parliamentary watch"], "th-rci-watch"),
]


def route_to_session(content, record_id, tags=None):
    """Route a record to the correct session based on content and metadata."""
    text = content.lower()
    if tags:
        text += " " + " ".join(tags).lower()

    # Check for specific record IDs first
    if record_id:
        for prefixes, session in SESSION_MAP:
            for p in prefixes:
                if p.lower() in record_id.lower() or p.lower() in text:
                    return session

    # Default
    return "cognitiveos-ops"


def parse_frontmatter(content):
    """Parse YAML frontmatter from markdown. Returns (metadata_dict, body_text)."""
    if not content.startswith("---"):
        return {}, content

    parts = content.split("---", 2)
    if len(parts) < 3:
        return {}, content

    fm_text = parts[1].strip()
    body = parts[2].strip()

    # Simple YAML parsing (handle common cases)
    metadata = {}
    current_key = None
    current_list = None
    current_dict = None

    for line in fm_text.split("\n"):
        line = line.rstrip()
        if not line:
            continue

        # List item
        if line.startswith("  - ") or line.startswith("- "):
            item = line.lstrip("- ").strip()
            if current_key and isinstance(metadata.get(current_key), list):
                metadata[current_key].append(item)
            continue

        # Nested dict (e.g. source:)
        if line.startswith("  ") and current_key:
            # Skip nested for now
            continue

        # Key-value
        if ":" in line:
            key, _, value = line.partition(":")
            key = key.strip()
            value = value.strip().strip("'\"")

            if value:
                # Try to parse as different types
                if value.lower() in ("true", "false"):
                    metadata[key] = value.lower() == "true"
                elif value.isdigit():
                    metadata[key] = int(value)
                else:
                    metadata[key] = value
            else:
                # Could be a list or dict
                metadata[key] = []
                current_key = key

    return metadata, body


def parse_record(filepath):
    """Parse a single record file. Returns dict with id, type, content, created_at, metadata."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            raw = f.read()
    except Exception as e:
        return {"error": str(e), "path": str(filepath)}

    fm, body = parse_frontmatter(raw)

    record_id = fm.get("id", Path(filepath).stem)
    record_type = fm.get("record_type", "")
    title = fm.get("title", "")
    created_at = fm.get("created_at", fm.get("date", ""))

    # Normalize created_at to ISO format
    if created_at:
        # Handle "2026-08-03 08:14:00+00:00" format
        created_at = str(created_at).replace(" ", "T")
        # Handle "2026-08-03 08:14:00+00:00" → already ISO
        # Handle bare date "2026-08-04"
        if len(created_at) == 10:
            created_at = created_at + "T00:00:00Z"
    else:
        # Try to extract from filename (e.g. INIT-20260803-002)
        m = re.search(r"(\d{4})(\d{2})(\d{2})", record_id)
        if m:
            created_at = f"{m.group(1)}-{m.group(2)}-{m.group(3)}T00:00:00Z"
        else:
            created_at = datetime.now().isoformat() + "Z"

    # Build content string
    content_parts = [f"[{record_id}] {title}"]
    if record_type:
        content_parts.append(f"Type: {record_type}")
    if "status" in fm:
        content_parts.append(f"Status: {fm['status']}")
    if "owner" in fm:
        content_parts.append(f"Owner: {fm['owner']}")
    if "priority" in fm:
        content_parts.append(f"Priority: {fm['priority']}")
    if "assignee" in fm:
        content_parts.append(f"Assignee: {fm['assignee']}")
    if "deadline" in fm:
        content_parts.append(f"Deadline: {fm['deadline']}")
    if "related_records" in fm:
        related = fm["related_records"]
        if isinstance(related, list):
            content_parts.append(f"Related: {', '.join(related)}")
    if "tags" in fm:
        tags = fm["tags"]
        if isinstance(tags, list):
            content_parts.append(f"Tags: {', '.join(tags)}")

    content_parts.append("")  # blank line
    content_parts.append(body[:5000])  # Cap body at 5000 chars

    content = "\n".join(content_parts)

    # Determine peer_id
    record_prefix = record_id.split("-")[0] if "-" in record_id else ""
    owner = str(fm.get("owner", "")).lower()

    if record_prefix in ("STK", "INT", "BRF", "ASS"):
        peer_id = "ember"
    elif "ember" in owner:
        peer_id = "ember"
    else:
        peer_id = "daf"

    # Determine session
    tags = fm.get("tags", [])
    if not isinstance(tags, list):
        tags = [str(tags)]
    session = route_to_session(content, record_id, tags)

    # Build Honcho metadata
    honcho_metadata = {
        "record_id": record_id,
        "record_type": record_type,
        "source": "strategic-cognitiveos",
        "ingested_at": datetime.now().isoformat() + "Z",
        "live": False,
    }
    if "status" in fm:
        honcho_metadata["status"] = str(fm["status"])
    if "priority" in fm:
        honcho_metadata["priority"] = str(fm["priority"])
    if "related_records" in fm:
        related = fm["related_records"]
        if isinstance(related, list):
            honcho_metadata["links"] = related

    return {
        "record_id": record_id,
        "content": content,
        "peer_id": peer_id,
        "session_id": session,
        "created_at": created_at,
        "metadata": honcho_metadata,
        "path": str(filepath),
    }


def batch_upload(messages, session_id):
    """Upload a batch of messages to Honcho."""
    url = f"{HONCHO_URL}/v3/workspaces/{WORKSPACE}/sessions/{session_id}/messages"
    payload = {"messages": messages}
    try:
        resp = requests.post(url, json=payload, timeout=30)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        return {"error": str(e), "status_code": getattr(e, "response", {}).status_code if hasattr(e, "response") else None}


def get_existing_record_ids(session_id):
    """Query Honcho for already-ingested record_ids in a session. Returns a set.
    Paginates through all messages (API caps at 50 per call)."""
    url = f"{HONCHO_URL}/v3/workspaces/{WORKSPACE}/sessions/{session_id}/messages/list"
    ids = set()
    offset = 0
    while True:
        try:
            resp = requests.post(url, json={"limit": 50, "offset": offset}, timeout=30)
            resp.raise_for_status()
            data = resp.json()
            items = data if isinstance(data, list) else data.get("items", [])
            if not items:
                break
            for item in items:
                meta = item.get("metadata", {})
                rid = meta.get("record_id")
                if rid:
                    ids.add(rid)
            if len(items) < 50:
                break
            offset += 50
        except Exception:
            break
    return ids


def main():
    repo = Path(REPO_PATH)
    if not repo.exists():
        print(f"ERROR: Repo not found at {REPO_PATH}")
        sys.exit(1)

    # Collect all record files
    all_records = []
    errors = []

    for dir_name in RECORD_DIRS:
        dir_path = repo / dir_name
        if not dir_path.exists():
            continue

        for filepath in sorted(dir_path.rglob("*.md")):
            # Skip cron-output
            if "cron-output" in str(filepath):
                continue
            # Skip applied-use-cases subdirectory in intelligence
            if "applied-use-cases" in str(filepath):
                continue

            record = parse_record(filepath)
            if "error" in record:
                errors.append(record)
            else:
                all_records.append(record)

    print(f"Parsed {len(all_records)} records ({len(errors)} errors)")

    # Group by session
    sessions = {}
    for r in all_records:
        sid = r["session_id"]
        sessions.setdefault(sid, []).append(r)

    print(f"\nSession distribution:")
    for sid, records in sorted(sessions.items()):
        print(f"  {sid}: {len(records)} records")

    # === DEDUP GUARD ===
    # Query each session for already-ingested record_ids before uploading
    print(f"\n=== DEDUP CHECK ===")
    total_skipped = 0
    for sid, records in sorted(sessions.items()):
        existing = get_existing_record_ids(sid)
        before = len(records)
        records = [r for r in records if r["record_id"] not in existing]
        skipped = before - len(records)
        total_skipped += skipped
        sessions[sid] = records  # update with filtered list
        if skipped > 0:
            print(f"  {sid}: {skipped} duplicates skipped ({len(records)} new to upload)")
        else:
            print(f"  {sid}: no duplicates ({len(records)} new)")
    print(f"Total duplicates skipped: {total_skipped}")

    if errors:
        print(f"\nErrors ({len(errors)}):")
        for e in errors[:5]:
            print(f"  {e['path']}: {e['error']}")

    # Batch upload
    total_uploaded = 0
    upload_errors = []
    session_stats = {}

    for session_id, records in sessions.items():
        session_uploaded = 0
        for i in range(0, len(records), BATCH_SIZE):
            batch = records[i:i + BATCH_SIZE]
            messages = []
            for r in batch:
                messages.append({
                    "content": r["content"],
                    "peer_id": r["peer_id"],
                    "created_at": r["created_at"],
                    "metadata": r["metadata"],
                })

            result = batch_upload(messages, session_id)
            if "error" in result:
                upload_errors.append({
                    "session": session_id,
                    "batch": i // BATCH_SIZE,
                    "error": result["error"],
                })
                print(f"  ❌ {session_id} batch {i//BATCH_SIZE}: {result['error']}")
            else:
                batch_count = len(messages)
                session_uploaded += batch_count
                total_uploaded += batch_count

        session_stats[session_id] = session_uploaded
        print(f"  ✅ {session_id}: {session_uploaded}/{len(records)} uploaded")

    print(f"\n=== INGESTION COMPLETE ===")
    print(f"Total records parsed: {len(all_records)}")
    print(f"Total uploaded: {total_uploaded}")
    print(f"Upload errors: {len(upload_errors)}")
    print(f"Parse errors: {len(errors)}")

    # Write report
    report = {
        "timestamp": datetime.now().isoformat() + "Z",
        "total_records_parsed": len(all_records),
        "total_messages_uploaded": total_uploaded,
        "upload_errors": len(upload_errors),
        "parse_errors": len(errors),
        "session_breakdown": session_stats,
        "errors": upload_errors[:20],
    }

    report_path = Path(__file__).parent / "logs" / "ingestion-report.json"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    with open(report_path, "w") as f:
        json.dump(report, f, indent=2)
    print(f"\nReport: {report_path}")


if __name__ == "__main__":
    main()
