#!/bin/bash
# Honcho Client — Shared API functions
# Source after config.sh

# Search workspace for messages
honcho_search() {
    local query="$1"
    local limit="${2:-10}"
    local data="{\"query\": \"$query\", \"limit\": $limit}"

    honcho_api POST "/v3/workspaces/$WORKSPACE/search" "$data"
}

# Search within a specific session
honcho_search_session() {
    local session_id="$1"
    local query="$2"
    local limit="${3:-10}"
    local data="{\"query\": \"$query\", \"limit\": $limit}"

    honcho_api POST "/v3/workspaces/$WORKSPACE/sessions/$session_id/search" "$data"
}

# Query conclusions (requires observer + observed for semantic search)
honcho_conclusions() {
    local query="$1"
    local top_k="${2:-5}"
    local observer="${3:-ember}"
    local observed="${4:-daf}"
    local data="{\"query\": \"$query\", \"top_k\": $top_k, \"observer\": \"$observer\", \"observed\": \"$observed\"}"

    honcho_api POST "/v3/workspaces/$WORKSPACE/conclusions/query" "$data"
}

# Get peer context (observer looks at observed)
# ember observing daf = what ember knows about daf
honcho_peer_context() {
    local observer="${1:-ember}"
    local observed="${2:-daf}"

    honcho_api GET "/v3/workspaces/$WORKSPACE/peers/$observer/context?target=$observed" ""
}

# Get peer card
honcho_peer_card() {
    local peer_id="$1"

    honcho_api GET "/v3/workspaces/$WORKSPACE/peers/$peer_id/card" ""
}

# Create messages in a session
honcho_create_messages() {
    local session_id="$1"
    local messages_json="$2"

    honcho_api POST "/v3/workspaces/$WORKSPACE/sessions/$session_id/messages" "{\"messages\": $messages_json}" 10
}

# Get queue status
honcho_queue_status() {
    honcho_api GET "/v3/workspaces/$WORKSPACE/queue/status" ""
}

# Schedule a dream
honcho_schedule_dream() {
    local types="${1:-[\"omni\"]}"
    honcho_api POST "/v3/workspaces/$WORKSPACE/schedule_dream" "{\"types\": $types}"
}

# Format search results for injection
format_search_results() {
    local json_data="$1"
    local section_title="$2"

    echo "--- $section_title ---"
    echo "$json_data" | python3 -c "
import sys, json
try:
    d = json.load(sys.stdin)
    if 'error' in d:
        print(f'  (error: {d[\"error\"]})')
        sys.exit(0)
    # API returns a bare list, not a dict with items/results
    if isinstance(d, list):
        items = d
    else:
        items = d.get('items', d.get('results', []))
    if not items:
        print('  (no results)')
        sys.exit(0)
    for i, item in enumerate(items[:10]):
        content = item.get('content', '')[:150].replace('\n', ' ')
        session = item.get('session_id', '?')
        score = item.get('score', item.get('distance', '?'))
        peer = item.get('peer_id', '?')
        print(f'  [{i+1}] [{peer}] {content}...')
        if session and session != '?':
            print(f'      session: {session}')
except Exception as e:
    print(f'  (parse error: {e})')
" 2>/dev/null
}

# Format peer context for injection
format_peer_context() {
    local json_data="$1"

    echo "--- DAF PEER CONTEXT ---"
    echo "$json_data" | python3 -c "
import sys, json
try:
    d = json.load(sys.stdin)
    if 'error' in d:
        print(f'  (error: {d[\"error\"]})')
        sys.exit(0)
    rep = d.get('representation')
    if rep:
        print(f'  Representation: {rep[:300]}...')
    else:
        print('  (no representation yet)')
    card = d.get('peer_card')
    if card:
        print(f'  Peer card: {', '.join(card[:10])}')
    else:
        print('  (no peer card yet)')
except Exception as e:
    print(f'  (parse error: {e})')
" 2>/dev/null
}
