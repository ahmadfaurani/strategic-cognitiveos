#!/bin/bash
# ingest.sh — Write-Back Script
# Writes significant exchanges to Honcho during active sessions
# Usage: ingest.sh --content "<message>" --peer <peer_id> --session <session_id> [--type <type>] [--metadata '<json>']
# Fail-open: logs error and continues if Honcho is down, daily memory file unaffected

set -euo pipefail
SCRIPT_DIR="$(dirname "$(readlink -f "$0")")"
source "$SCRIPT_DIR/config.sh"
source "$SCRIPT_DIR/lib/honcho-client.sh"

# Parse arguments
CONTENT=""
PEER=""
SESSION=""
TYPE=""
METADATA=""
TIMEOUT=10

while [[ $# -gt 0 ]]; do
    case "$1" in
        --content)
            CONTENT="$2"; shift 2 ;;
        --peer)
            PEER="$2"; shift 2 ;;
        --session)
            SESSION="$2"; shift 2 ;;
        --type)
            TYPE="$2"; shift 2 ;;
        --metadata)
            METADATA="$2"; shift 2 ;;
        --timeout)
            TIMEOUT="$2"; shift 2 ;;
        *)
            shift ;;
    esac
done

# Validate required args
if [ -z "$CONTENT" ] || [ -z "$PEER" ] || [ -z "$SESSION" ]; then
    echo "ERROR: --content, --peer, and --session are required"
    echo "Usage: ingest.sh --content \"<message>\" --peer <peer_id> --session <session_id> [--type <type>]"
    exit 1
fi

# Build metadata
TIMESTAMP=$(date -u +%Y-%m-%dT%H:%M:%SZ)
if [ -n "$TYPE" ]; then
    META_JSON="{\"type\": \"$TYPE\", \"live\": true, \"ingested_at\": \"$TIMESTAMP\""
    if [ -n "$METADATA" ]; then
        # Merge additional metadata
        META_JSON="$META_JSON, \"extra\": $METADATA}"
    else
        META_JSON="$META_JSON}"
    fi
else
    META_JSON="{\"live\": true, \"ingested_at\": \"$TIMESTAMP\"}"
fi

# Escape content for JSON
CONTENT_ESCAPED=$(echo "$CONTENT" | python3 -c "import sys,json; print(json.dumps(sys.stdin.read()))" 2>/dev/null || echo "\"$CONTENT\"")

# Build message JSON
MESSAGE_JSON="[{\"content\": $CONTENT_ESCAPED, \"peer_id\": \"$PEER\", \"metadata\": $META_JSON}]"

# Send to Honcho
RESULT=$(honcho_create_messages "$SESSION" "$MESSAGE_JSON" 2>/dev/null || echo "{\"error\":\"failed\"}")

if echo "$RESULT" | grep -q '"error"'; then
    echo "INGEST FAILED: Honcho unavailable or error"
    log ingest "ERROR" "session=$SESSION peer=$PEER type=$TYPE"
    exit 0  # Fail-open: don't crash the session
fi

# Extract message ID
MSG_ID=$(echo "$RESULT" | python3 -c "
import sys, json
try:
    d = json.load(sys.stdin)
    # API returns a bare list
    if isinstance(d, list):
        items = d
    else:
        items = d.get('items', d.get('results', []))
    if items:
        print(items[0].get('id', 'unknown'))
    else:
        print('unknown')
except:
    print('parse_error')
" 2>/dev/null)

echo "INGEST OK: session=$SESSION peer=$PEER message_id=$MSG_ID"
log ingest "OK" "session=$SESSION peer=$PEER type=$TYPE msg_id=$MSG_ID"
