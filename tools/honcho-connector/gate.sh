#!/bin/bash
# gate.sh — ADEP-001 Operational Gate Checker
# Pre-task readiness and closure gate enforcement for D2-D4 tasks
# Usage:
#   gate.sh pre --level D2 --task "description" [--assumptions "..."] [--failure-modes "..."]
#   gate.sh close --level D2 --task "description" --result PASS|BLOCK [--exceptions "..."]
# D1 tasks: no gate required, log only
# Fail-open: if Honcho down, gate still returns PASS (session continues)

set -euo pipefail
SCRIPT_DIR="$(dirname "$(readlink -f "$0")")"
source "$SCRIPT_DIR/config.sh"
source "$SCRIPT_DIR/lib/honcho-client.sh"

# Parse arguments
GATE_TYPE=""
LEVEL=""
TASK=""
ASSUMPTIONS=""
FAILURE_MODES=""
RESULT=""
EXCEPTIONS=""
OWNER=""
DEPENDENCIES=""

while [[ $# -gt 0 ]]; do
    case "$1" in
        pre|close)
            GATE_TYPE="$1"; shift ;;
        --level)
            LEVEL="$2"; shift 2 ;;
        --task)
            TASK="$2"; shift 2 ;;
        --assumptions)
            ASSUMPTIONS="$2"; shift 2 ;;
        --failure-modes)
            FAILURE_MODES="$2"; shift 2 ;;
        --result)
            RESULT="$2"; shift 2 ;;
        --exceptions)
            EXCEPTIONS="$2"; shift 2 ;;
        --owner)
            OWNER="$2"; shift 2 ;;
        --dependencies)
            DEPENDENCIES="$2"; shift 2 ;;
        *)
            shift ;;
    esac
done

if [ -z "$GATE_TYPE" ] || [ -z "$LEVEL" ] || [ -z "$TASK" ]; then
    echo "Usage: gate.sh <pre|close> --level <D1-D4> --task \"description\" [options]"
    exit 1
fi

# D1: no gate, log only
if [ "$LEVEL" = "D1" ]; then
    log gate "D1" "$GATE_TYPE task=$TASK"
    echo "GATE: D1 — no enforcement, logged"
    exit 0
fi

TIMESTAMP=$(date -u +%Y-%m-%dT%H:%M:%SZ)
GATE_STATUS="PASS"
GATE_CHECKS=""

if [ "$GATE_TYPE" = "pre" ]; then
    # === PRE-TASK READINESS GATE ===
    echo "=== PRE-TASK GATE ($LEVEL) ==="
    echo "Task: $TASK"
    echo "Timestamp: $TIMESTAMP"
    echo ""

    case "$LEVEL" in
        D2)
            # Objective + success check + owner + dependencies
            if [ -z "$OWNER" ]; then
                GATE_STATUS="BLOCK"
                GATE_CHECKS="owner: missing"
                echo "❌ BLOCK: No owner specified"
            else
                echo "✅ Owner: $OWNER"
            fi
            if [ -z "$DEPENDENCIES" ]; then
                echo "⚠️  WARN: Dependencies not explicitly stated (D2 minimum)"
            else
                echo "✅ Dependencies: $DEPENDENCIES"
            fi
            ;;
        D3)
            # Above + assumptions + failure modes
            if [ -z "$OWNER" ]; then
                GATE_STATUS="BLOCK"
                GATE_CHECKS="$GATE_CHECKS owner: missing"
                echo "❌ BLOCK: No owner specified"
            else
                echo "✅ Owner: $OWNER"
            fi
            if [ -z "$ASSUMPTIONS" ]; then
                GATE_STATUS="BLOCK"
                GATE_CHECKS="$GATE_CHECKS assumptions: missing"
                echo "❌ BLOCK: No assumptions stated (D3 requires assumption list)"
            else
                echo "✅ Assumptions: $ASSUMPTIONS"
            fi
            if [ -z "$FAILURE_MODES" ]; then
                GATE_STATUS="BLOCK"
                GATE_CHECKS="$GATE_CHECKS failure-modes: missing"
                echo "❌ BLOCK: No failure modes identified (D3 requires pre-mortem)"
            else
                echo "✅ Failure modes: $FAILURE_MODES"
            fi
            ;;
        D4)
            # Above + human decision authority + rollback plan
            if [ -z "$OWNER" ]; then
                GATE_STATUS="BLOCK"
                echo "❌ BLOCK: No owner specified"
            else
                echo "✅ Owner: $OWNER"
            fi
            if [ -z "$ASSUMPTIONS" ]; then
                GATE_STATUS="BLOCK"
                echo "❌ BLOCK: No assumptions stated (D4 requires full assumption register)"
            else
                echo "✅ Assumptions: $ASSUMPTIONS"
            fi
            if [ -z "$FAILURE_MODES" ]; then
                GATE_STATUS="BLOCK"
                echo "❌ BLOCK: No failure modes identified (D4 requires full pre-mortem)"
            else
                echo "✅ Failure modes: $FAILURE_MODES"
            fi
            # D4 requires explicit human authority
            echo "⚠️  D4: Human decision authority required before execution"
            echo "⚠️  D4: Rollback/containment plan required before execution"
            ;;
    esac

    echo ""
    if [ "$GATE_STATUS" = "PASS" ]; then
        echo "GATE: PASS — proceed with execution"
    else
        echo "GATE: BLOCK — resolve missing items before proceeding"
    fi

elif [ "$GATE_TYPE" = "close" ]; then
    # === CLOSURE GATE ===
    echo "=== CLOSURE GATE ($LEVEL) ==="
    echo "Task: $TASK"
    echo "Result: $RESULT"
    echo "Timestamp: $TIMESTAMP"
    echo ""

    if [ -z "$RESULT" ]; then
        RESULT="BLOCK"
        echo "❌ No result specified — defaulting to BLOCK"
    fi

    case "$LEVEL" in
        D2)
            echo "Checklist:"
            echo "  [ ] Objective met?"
            echo "  [ ] Evidence exists?"
            echo "  [ ] Dependencies addressed?"
            echo "  [ ] Owner informed?"
            ;;
        D3)
            echo "Checklist:"
            echo "  [ ] Objective met?"
            echo "  [ ] Evidence exists?"
            echo "  [ ] Dependencies addressed?"
            echo "  [ ] Assumptions validated?"
            echo "  [ ] Risks reviewed?"
            echo "  [ ] Acceptance criteria met?"
            ;;
        D4)
            echo "Checklist:"
            echo "  [ ] Objective met?"
            echo "  [ ] Evidence exists?"
            echo "  [ ] Dependencies addressed?"
            echo "  [ ] Assumptions validated?"
            echo "  [ ] Risks reviewed?"
            echo "  [ ] Acceptance criteria met?"
            echo "  [ ] Independent verification?"
            echo "  [ ] Human approval?"
            echo "  [ ] Rollback confirmed?"
            ;;
    esac

    if [ -n "$EXCEPTIONS" ]; then
        echo ""
        echo "Exceptions: $EXCEPTIONS"
    fi

    echo ""
    if [ "$RESULT" = "PASS" ]; then
        echo "GATE: PASS — task may be marked complete"
    else
        echo "GATE: BLOCK — task NOT complete. Report actual state."
    fi
    GATE_STATUS="$RESULT"
fi

# Log compliance record to Honcho
COMPLIANCE_CONTENT="[GATE] ${GATE_TYPE} | ${LEVEL} | ${TASK} | ${GATE_STATUS} | ${TIMESTAMP}"
if [ -n "$EXCEPTIONS" ]; then
    COMPLIANCE_CONTENT="${COMPLIANCE_CONTENT} | exceptions: ${EXCEPTIONS}"
fi
if [ -n "$GATE_CHECKS" ]; then
    COMPLIANCE_CONTENT="${COMPLIANCE_CONTENT} | checks: ${GATE_CHECKS}"
fi

COMPLIANCE_METADATA=$(python3 -c "
import json
meta = {
    'record_type': 'compliance',
    'gate_type': '$GATE_TYPE',
    'diligence_level': '$LEVEL',
    'gate_status': '$GATE_STATUS',
    'task': '''$(echo "$TASK" | sed "s/'/\\\\'/g")''',
    'timestamp': '$TIMESTAMP',
    'live': True
}
if '$EXCEPTIONS':
    meta['exceptions'] = '$EXCEPTIONS'
print(json.dumps(meta))
" 2>/dev/null || echo "{\"record_type\":\"compliance\",\"gate_type\":\"$GATE_TYPE\",\"level\":\"$LEVEL\",\"status\":\"$GATE_STATUS\"}")

# Escape content for JSON
CONTENT_ESCAPED=$(echo "$COMPLIANCE_CONTENT" | python3 -c "import sys,json; print(json.dumps(sys.stdin.read()))" 2>/dev/null || echo "\"$COMPLIANCE_CONTENT\"")

MESSAGE_JSON="[{\"content\": $CONTENT_ESCAPED, \"peer_id\": \"ember\", \"metadata\": $COMPLIANCE_METADATA}]"

# Send to Honcho (fail-open: don't block if Honcho is down)
INGEST_RESULT=$(honcho_create_messages "cognitiveos-ops" "$MESSAGE_JSON" 2>/dev/null || echo "{\"error\":\"failed\"}")

if echo "$INGEST_RESULT" | grep -q '"error"'; then
    log gate "ERROR" "compliance log failed: $GATE_TYPE $LEVEL $TASK"
    echo ""
    echo "(compliance log: UNAVAILABLE — Honcho down, gate still $GATE_STATUS)"
else
    log gate "$GATE_STATUS" "$GATE_TYPE $LEVEL task=$TASK"
    echo ""
    echo "(compliance log: OK — recorded to Honcho)"
fi

# Exit code: 0 = PASS, 1 = BLOCK
if [ "$GATE_STATUS" = "PASS" ]; then
    exit 0
else
    exit 1
fi
