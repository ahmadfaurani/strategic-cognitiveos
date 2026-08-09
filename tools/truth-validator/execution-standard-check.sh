#!/bin/bash
# execution-standard-check.sh — Validate DOCTRINE.md Execution Standard compliance
# 
# Checks for:
# - Placeholder patterns (TBD, TODO, dummy values, empty sections)
# - Incomplete workflow markers
# - Draft-state content
#
# Usage: ./execution-standard-check.sh <input.md>
# Exit codes: 0 = PASS, 1 = FAIL (violations found), 2 = ERROR

set -e

INPUT_FILE="${1:-}"

if [[ -z "$INPUT_FILE" ]]; then
    echo "ERROR: No input file specified"
    echo "Usage: $0 <input.md>"
    exit 2
fi

if [[ ! -f "$INPUT_FILE" ]]; then
    echo "ERROR: File not found: $INPUT_FILE"
    exit 2
fi

echo "=== Execution Standard Validation ==="
echo "Input: $INPUT_FILE"
echo "Date: $(date -u +%Y-%m-%d_%H:%M:%S_UTC)"
echo ""

VIOLATIONS=0
WARNINGS=0

# Placeholder patterns (strict violations)
PLACEHOLDER_PATTERNS=(
    "TBD"
    "TODO"
    "FIXME"
    "XXX"
    "to be added"
    "to be completed"
    "insert .* here"
    "example content"
    "placeholder"
    "dummy value"
    "mock data"
    "sample data"
    "\\[\\.\\.\\.\\]"
    "\\{\\{.*\\}\\}"  # Template variables like {{variable}}
    "__.*__"          # Underscore placeholders
    "N/A"
    "not available"
    "will be provided"
    "coming soon"
    "draft"
    "work in progress"
    "WIP"
)

echo "--- Checking for Placeholders ---"
for pattern in "${PLACEHOLDER_PATTERNS[@]}"; do
    MATCHES=$(grep -inE "$pattern" "$INPUT_FILE" 2>/dev/null || true)
    if [[ -n "$MATCHES" ]]; then
        echo "❌ VIOLATION: Placeholder pattern found: '$pattern'"
        echo "$MATCHES" | head -5
        VIOLATIONS=$((VIOLATIONS + 1))
    fi
done

# Empty section detection (sections with no substantive content)
echo ""
echo "--- Checking for Empty Sections ---"
EMPTY_SECTIONS=$(grep -E "^#{1,6}.*$" "$INPUT_FILE" | while read -r header; do
    section_name=$(echo "$header" | sed 's/^#\+ //')
    # Check if next non-empty line is another header or EOF within 3 lines
    line_num=$(grep -n "^${header}$" "$INPUT_FILE" | head -1 | cut -d: -f1)
    if [[ -n "$line_num" ]]; then
        next_content=$(sed -n "$((line_num + 1)),$((line_num + 4))p" "$INPUT_FILE" | grep -v "^$" | grep -v "^#" | head -1)
        if [[ -z "$next_content" ]]; then
            echo "  Empty section: $section_name (line $line_num)"
        fi
    fi
done)

if [[ -n "$EMPTY_SECTIONS" ]]; then
    echo "$EMPTY_SECTIONS"
    VIOLATIONS=$((VIOLATIONS + 1))
fi

# Draft-state markers
echo ""
echo "--- Checking for Draft-State Markers ---"
DRAFT_MARKERS=$(grep -inE "(draft|preliminary|initial version|first pass|rough draft|not final)" "$INPUT_FILE" 2>/dev/null || true)
if [[ -n "$DRAFT_MARKERS" ]]; then
    echo "⚠️  WARNING: Draft-state markers detected:"
    echo "$DRAFT_MARKERS" | head -5
    WARNINGS=$((WARNINGS + 1))
fi

# Incomplete workflow indicators
echo ""
echo "--- Checking for Incomplete Workflow Indicators ---"
INCOMPLETE=$(grep -inE "(step.*pending|awaiting.*input|waiting for|incomplete|partial implementation)" "$INPUT_FILE" 2>/dev/null || true)
if [[ -n "$INCOMPLETE" ]]; then
    echo "⚠️  WARNING: Incomplete workflow indicators detected:"
    echo "$INCOMPLETE" | head -5
    WARNINGS=$((WARNINGS + 1))
fi

# Summary
echo ""
echo "=== Validation Summary ==="
echo "Violations: $VIOLATIONS"
echo "Warnings: $WARNINGS"
echo ""

if [[ $VIOLATIONS -gt 0 ]]; then
    echo "❌ FAILED: Execution Standard violations detected"
    echo "Action required: Remove all placeholders and empty sections before delivery"
    exit 1
elif [[ $WARNINGS -gt 0 ]]; then
    echo "⚠️  PASSED WITH WARNINGS: Review draft-state markers and incomplete indicators"
    echo "Recommendation: Ensure deliverable is operationally ready"
    exit 0
else
    echo "✅ PASSED: No Execution Standard violations detected"
    exit 0
fi
