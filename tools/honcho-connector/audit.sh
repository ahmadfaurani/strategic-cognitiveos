#!/bin/bash
# audit.sh — Daily ADEP-001 Compliance Audit
# Queries Honcho for compliance records from the past 24 hours
# Produces a compliance score and flags exceptions
# Usage: audit.sh [--hours <n>] [--threshold <percent>]
# Fail-open: returns "UNAVAILABLE" if Honcho down

set -euo pipefail
SCRIPT_DIR="$(dirname "$(readlink -f "$0")")"
source "$SCRIPT_DIR/config.sh"
source "$SCRIPT_DIR/lib/honcho-client.sh"

HOURS=24
THRESHOLD=80

while [[ $# -gt 0 ]]; do
    case "$1" in
        --hours) HOURS="$2"; shift 2 ;;
        --threshold) THRESHOLD="$2"; shift 2 ;;
        *) shift ;;
    esac
done

echo "=== ADEP-001 COMPLIANCE AUDIT ==="
echo "Period: last ${HOURS}h"
echo "Threshold: ${THRESHOLD}%"
echo "Timestamp: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo ""

# Search Honcho for compliance records in cognitiveos-ops session
SEARCH_RESULT=$(honcho_search_session "cognitiveos-ops" "GATE compliance diligence" 50 2>/dev/null || echo "{\"error\":\"failed\"}")

if echo "$SEARCH_RESULT" | grep -q '"error"'; then
    echo "--- AUDIT: UNAVAILABLE (Honcho down) ---"
    log audit "ERROR" "search failed"
    exit 0
fi

echo "$SEARCH_RESULT" | python3 -c "
import sys, json
data = json.load(sys.stdin)
items = data if isinstance(data, list) else data.get('items', data.get('results', []))

# Filter to compliance records only
compliance = []
for item in items:
    meta = item.get('metadata', {})
    if meta.get('record_type') == 'compliance':
        compliance.append(item)

total = len(compliance)
if total == 0:
    print('No compliance records found in period.')
    print()
    print('AUDIT: INSUFFICIENT DATA — no D2+ tasks logged')
    sys.exit(0)

# Count by status
pass_count = 0
block_count = 0
exceptions = []
by_level = {}

for item in compliance:
    meta = item.get('metadata', {})
    status = meta.get('gate_status', 'unknown')
    level = meta.get('diligence_level', '?')
    gate_type = meta.get('gate_type', '?')
    task = meta.get('task', '?')

    by_level.setdefault(level, {'pass': 0, 'block': 0})
    if status == 'PASS':
        pass_count += 1
        by_level[level]['pass'] += 1
    else:
        block_count += 1
        by_level[level]['block'] += 1
        if meta.get('exceptions'):
            exceptions.append(f'  [{level}] {task}: {meta[\"exceptions\"]}')

score = round((pass_count / total) * 100) if total else 0

print(f'Total compliance records: {total}')
print(f'  PASS: {pass_count}')
print(f'  BLOCK: {block_count}')
print(f'  Score: {score}%')
print()

print('By diligence level:')
for level in sorted(by_level.keys()):
    d = by_level[level]
    print(f'  {level}: {d[\"pass\"]} pass, {d[\"block\"]} block')

if exceptions:
    print()
    print(f'Exceptions ({len(exceptions)}):')
    for e in exceptions[:10]:
        print(e)

print()
if score >= $THRESHOLD:
    print(f'AUDIT: PASS ({score}% >= ${THRESHOLD}% threshold)')
else:
    print(f'AUDIT: BELOW THRESHOLD ({score}% < ${THRESHOLD}% threshold)')
    print('  → Review skipped gates and common failure patterns')
" 2>/dev/null

echo ""
echo "=== END AUDIT ==="
