#!/bin/bash
# recall.sh — Bootstrap Recall Script
# Queries Honcho for relevant context at session start
# Usage: recall.sh "<query>" [--session <session_id>] [--timeout <seconds>]
# Fail-open: returns "UNAVAILABLE" if Honcho is down, session continues with file injection only

set -euo pipefail
SCRIPT_DIR="$(dirname "$(readlink -f "$0")")"
source "$SCRIPT_DIR/config.sh"
source "$SCRIPT_DIR/lib/honcho-client.sh"

# Parse arguments
QUERY=""
SESSION=""
TIMEOUT="$DEFAULT_TIMEOUT"

while [[ $# -gt 0 ]]; do
    case "$1" in
        --session)
            SESSION="$2"; shift 2 ;;
        --timeout)
            TIMEOUT="$2"; shift 2 ;;
        *)
            if [ -z "$QUERY" ]; then
                QUERY="$1"
            fi
            shift ;;
    esac
done

if [ -z "$QUERY" ]; then
    echo "=== HONCHO RECALL ==="
    echo "ERROR: No query provided"
    echo "Usage: recall.sh \"<query>\" [--session <session_id>] [--timeout <seconds>]"
    exit 1
fi

# Escape query for JSON
QUERY_ESCAPED=$(echo "$QUERY" | python3 -c "import sys,json; print(json.dumps(sys.stdin.read().strip()))" 2>/dev/null || echo "\"$QUERY\"")

echo "=== HONCHO RECALL ==="
echo "Query: $QUERY"
echo "Timestamp: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo ""

# 1. Semantic search (workspace or session-scoped)
if [ -n "$SESSION" ]; then
    SEARCH_RESULT=$(honcho_search_session "$SESSION" "$QUERY" 10 2>/dev/null || echo "{\"error\":\"failed\"}")
else
    SEARCH_RESULT=$(honcho_search "$QUERY" 10 2>/dev/null || echo "{\"error\":\"failed\"}")
fi

if echo "$SEARCH_RESULT" | grep -q '"error"'; then
    echo "--- MESSAGES: UNAVAILABLE ---"
    log recall "ERROR" "search failed"
else
    format_search_results "$SEARCH_RESULT" "MESSAGES (10)"
fi

echo ""

# 2. Conclusions
CONCLUSIONS_RESULT=$(honcho_conclusions "$QUERY" 5 2>/dev/null || echo "{\"error\":\"failed\"}")

if echo "$CONCLUSIONS_RESULT" | grep -q '"error"'; then
    echo "--- CONCLUSIONS: UNAVAILABLE ---"
    log recall "ERROR" "conclusions query failed"
else
    format_search_results "$CONCLUSIONS_RESULT" "CONCLUSIONS (5)"
fi

echo ""

# 3. DAF Peer Context (ember observing daf = what ember knows about daf)
CONTEXT_RESULT=$(honcho_peer_context "ember" "daf" 2>/dev/null || echo "{\"error\":\"failed\"}")

if echo "$CONTEXT_RESULT" | grep -q '"error"'; then
    echo "--- DAF PEER CONTEXT: UNAVAILABLE ---"
    log recall "ERROR" "peer context failed"
else
    format_peer_context "$CONTEXT_RESULT"
fi

echo ""
echo "=== END RECALL ==="
