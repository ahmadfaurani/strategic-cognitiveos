#!/bin/bash
# Extract and verify named entities (candidates, positions, parties)
# Cross-references against known registry if available

set -e

INPUT_FILE="${1:-/dev/stdin}"
REGISTRY_FILE="/home/p62operator/.openclaw/workspace/memory/candidate-registry.md"

if [ ! -f "$INPUT_FILE" ] && [ "$INPUT_FILE" != "/dev/stdin" ]; then
    echo "Error: File not found: $INPUT_FILE" >&2
    exit 1
fi

echo "=== Named Entity Extraction ==="
echo "Source: $INPUT_FILE"
[ -f "$REGISTRY_FILE" ] && echo "Registry: $REGISTRY_FILE (available for cross-reference)"
echo ""

# Extract potential candidate names (capitalized words, often with titles)
echo "## Potential Candidate Names"
echo "----------------------------"
grep -oE '\b(Dato'|'Datuk|Dr|Ir|Hj|Hjh|Mr|Ms|Mrs)\.?[[:space:]]+[A-Z][a-z]+([[:space:]]+[A-Z][a-z]+)*' "$INPUT_FILE" 2>/dev/null | sort -u || echo "  No titled names found"

grep -oE '\b[A-Z][a-z]+[[:space:]]+[A-Z][a-z]+[[:space:]]+[A-Z][a-z]+\b' "$INPUT_FILE" 2>/dev/null | sort -u || echo "  No three-part names found"

echo ""
echo "## Party/Position References"
echo "----------------------------"
grep -oE '\b(PH|BN|PN|MUDA|BERSATU|UMNO|PAS|PKR|DAP|AMANAH|MCA|MIC|Gerakan|PEJUANG|Bersama)\b' "$INPUT_FILE" 2>/dev/null | sort | uniq -c | sort -rn || echo "  No party references found"

echo ""
echo "## Constituency References"
echo "----------------------------"
grep -oE '\b(N[0-9]+[[:space:]]+[A-Za-z]+|[A-Za-z]+[[:space:]]+\(P[0-9]+\))\b' "$INPUT_FILE" 2>/dev/null | sort -u || echo "  No constituency references found"

echo ""

# Cross-reference with registry if available
if [ -f "$REGISTRY_FILE" ]; then
    echo "## Registry Cross-Reference"
    echo "----------------------------"
    echo "  (Manual verification recommended against official SPR list)"
fi

echo ""
echo "=== End of Extraction ==="
