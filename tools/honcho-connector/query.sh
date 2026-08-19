#!/bin/bash
# query.sh — Mid-Session Semantic Search
# Queries Honcho for relevant context during session processing
# Usage: query.sh "<query>" [--session <session_id>] [--limit <n>] [--conclusions] [--timeout <seconds>]
# Fail-open: returns empty results if Honcho is down, session continues

set -euo pipefail
SCRIPT_DIR="$(dirname "$(readlink -f "$0")")"
source "$SCRIPT_DIR/config.sh"
source "$SCRIPT_DIR/lib/honcho-client.sh"

# Parse arguments
QUERY=""
SESSION=""
LIMIT=10
SEARCH_CONCLUSIONS=false
TIMEOUT="$DEFAULT_TIMEOUT"

while [[ $# -gt 0 ]]; do
    case "$1" in
        --session)
            SESSION="$2"; shift 2 ;;
        --limit)
            LIMIT="$2"; shift 2 ;;
        --conclusions)
            SEARCH_CONCLUSIONS=true; shift ;;
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
    echo "=== HONCHO QUERY ==="
    echo "ERROR: No query provided"
    echo "Usage: query.sh \"<query>\" [--session <session_id>] [--limit <n>] [--conclusions]"
    exit 1
fi

echo "=== HONCHO QUERY ==="
echo "Query: $QUERY"
echo ""

# 1. Message search
if [ -n "$SESSION" ]; then
    SEARCH_RESULT=$(honcho_search_session "$SESSION" "$QUERY" "$LIMIT" 2>/dev/null || echo "{\"error\":\"failed\"}")
else
    SEARCH_RESULT=$(honcho_search "$QUERY" "$LIMIT" 2>/dev/null || echo "{\"error\":\"failed\"}")
fi

if echo "$SEARCH_RESULT" | grep -q '"error"'; then
    echo "--- MESSAGES: UNAVAILABLE ---"
    log query "ERROR" "search failed: $QUERY"
else
    format_search_results "$SEARCH_RESULT" "MESSAGES ($LIMIT)"
fi

echo ""

# 2. Conclusions (if --conclusions flag)
if [ "$SEARCH_CONCLUSIONS" = true ]; then
    CONCLUSIONS_RESULT=$(honcho_conclusions "$QUERY" 5 "ember" "daf" 2>/dev/null || echo "{\"error\":\"failed\"}")

    if echo "$CONCLUSIONS_RESULT" | grep -q '"error"'; then
        echo "--- CONCLUSIONS: UNAVAILABLE ---"
        log query "ERROR" "conclusions failed: $QUERY"
    else
        format_search_results "$CONCLUSIONS_RESULT" "CONCLUSIONS (5)"
    fi
    echo ""
fi

echo "=== END QUERY ==="
