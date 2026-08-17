#!/usr/bin/env bash
# DeerFlow PIR Dispatch Script
# Called by Hermes cronjobs to outsource PIR execution to DeerFlow.
#
# Usage: bash deerflow-dispatch.sh <prompt_file> <output_file> [mode]
#   prompt_file: Path to file containing the DeerFlow research prompt
#   output_file: Path to save the intelligence product
#   mode: ultra (default) | pro | standard | flash
#
# Returns: 0 on success, 1 on failure
# Output: Intelligence product written to output_file

set -euo pipefail

PROMPT_FILE="${1:?Usage: deerflow-dispatch.sh <prompt_file> <output_file> [mode]}"
OUTPUT_FILE="${2:?Output file required}"
MODE="${3:-ultra}"

# Resolve DeerFlow URLs
DEERFLOW_URL="${DEERFLOW_URL:-http://localhost:2026}"
DEERFLOW_GATEWAY_URL="${DEERFLOW_GATEWAY_URL:-$DEERFLOW_URL}"
DEERFLOW_LANGGRAPH_URL="${DEERFLOW_LANGGRAPH_URL:-$DEERFLOW_URL/api/langgraph}"

echo "[deerflow-dispatch] Mode: $MODE"
echo "[deerflow-dispatch] Prompt: $PROMPT_FILE"
echo "[deerflow-dispatch] Output: $OUTPUT_FILE"

# Step 1: Health check
HEALTH=$(curl -s -m 10 "$DEERFLOW_GATEWAY_URL/health" 2>/dev/null || echo "")
if [ -z "$HEALTH" ]; then
  echo "[deerflow-dispatch] ERROR: DeerFlow not reachable at $DEERFLOW_GATEWAY_URL"
  echo "[deerflow-dispatch] Falling back to inline collection mode"
  exit 1
fi
echo "[deerflow-dispatch] DeerFlow healthy: $HEALTH"

# Step 2: Read prompt
PROMPT=$(cat "$PROMPT_FILE")
if [ -z "$PROMPT" ]; then
  echo "[deerflow-dispatch] ERROR: Prompt file is empty"
  exit 1
fi

# Step 3: Create thread
THREAD_RESPONSE=$(curl -s -m 10 -X POST "$DEERFLOW_LANGGRAPH_URL/threads" \
  -H "Content-Type: application/json" \
  -d '{}' 2>/dev/null || echo "")

THREAD_ID=$(echo "$THREAD_RESPONSE" | python3 -c "
import sys, json
try:
    d = json.load(sys.stdin)
    print(d.get('thread_id', ''))
except:
    print('')
" 2>/dev/null || echo "")

if [ -z "$THREAD_ID" ]; then
  echo "[deerflow-dispatch] ERROR: Failed to create DeerFlow thread"
  exit 1
fi
echo "[deerflow-dispatch] Thread created: $THREAD_ID"

# Step 4: Set mode flags
case "$MODE" in
  ultra)
    THINKING="true"; PLANNING="true"; SUBAGENT="true"
    ;;
  pro)
    THINKING="true"; PLANNING="true"; SUBAGENT="false"
    ;;
  standard)
    THINKING="true"; PLANNING="false"; SUBAGENT="false"
    ;;
  flash)
    THINKING="false"; PLANNING="false"; SUBAGENT="false"
    ;;
  *)
    THINKING="true"; PLANNING="true"; SUBAGENT="true"
    ;;
esac

# Step 5: Stream run and collect response
# Escape prompt for JSON
PROMPT_JSON=$(python3 -c "
import json, sys
print(json.dumps(open('$PROMPT_FILE').read()))
" 2>/dev/null || echo '""')

echo "[deerflow-dispatch] Dispatching research run ($MODE)..."

# Build request body
REQUEST_BODY=$(cat <<ENDJSON
{
  "assistant_id": "lead_agent",
  "input": {
    "messages": [
      {
        "type": "human",
        "content": [{"type": "text", "text": $PROMPT_JSON}]
      }
    ]
  },
  "stream_mode": ["values"],
  "config": {"recursion_limit": 1000},
  "context": {
    "thinking_enabled": $THINKING,
    "is_plan_mode": $PLANNING,
    "subagent_enabled": $SUBAGENT,
    "thread_id": "$THREAD_ID"
  }
}
ENDJSON
)

# Stream and extract final response
curl -s -N -m 900 -X POST "$DEERFLOW_LANGGRAPH_URL/threads/$THREAD_ID/runs/stream" \
  -H "Content-Type: application/json" \
  -d "$REQUEST_BODY" 2>/dev/null | python3 -c "
import sys, json, re

final_content = ''
current_event = None
buffer = ''

for line in sys.stdin:
    line = line.rstrip()
    if line.startswith('event: '):
        current_event = line[7:]
        continue
    if line.startswith('data: '):
        buffer = line[6:]
        # Try to parse as JSON
        try:
            data = json.loads(buffer)
        except:
            continue
        
        if current_event == 'values':
            messages = data.get('messages', [])
            for msg in messages:
                if msg.get('type') == 'ai':
                    content = msg.get('content', '')
                    if isinstance(content, list):
                        for item in content:
                            if isinstance(item, dict) and item.get('type') == 'text':
                                final_content = item.get('text', '')
                    elif isinstance(content, str):
                        final_content = content
        elif current_event == 'end':
            break

if final_content:
    print(final_content)
else:
    print('[deerflow-dispatch] WARNING: No AI response found in stream')
    sys.exit(1)
" > "$OUTPUT_FILE" 2>/dev/null

EXIT_CODE=$?

if [ $EXIT_CODE -ne 0 ] || [ ! -s "$OUTPUT_FILE" ]; then
  echo "[deerflow-dispatch] ERROR: Failed to collect DeerFlow response"
  exit 1
fi

echo "[deerflow-dispatch] Success: $(wc -c < "$OUTPUT_FILE") bytes written to $OUTPUT_FILE"
exit 0
