#!/bin/bash
# Extract all numerical claims from input for verification
# Output: Claim | Context | Line Number | Verification Status

set -e

INPUT_FILE="${1:-/dev/stdin}"

if [ ! -f "$INPUT_FILE" ] && [ "$INPUT_FILE" != "/dev/stdin" ]; then
    echo "Error: File not found: $INPUT_FILE" >&2
    exit 1
fi

echo "=== Numerical Claims Extraction ==="
echo "Source: $INPUT_FILE"
echo ""
echo "Line | Claim | Context"
echo "-----|-------|--------"

# Extract numbers with surrounding context
grep -nE '[0-9]+[,0-9]*' "$INPUT_FILE" 2>/dev/null | while IFS=: read -r line_num content; do
    # Extract the number and ~50 chars of context
    numbers=$(echo "$content" | grep -oE '[0-9]+[,0-9]*' | head -3 | tr '\n' ' ')
    context=$(echo "$content" | sed 's/^[[:space:]]*//' | cut -c1-60)
    
    if [ -n "$numbers" ]; then
        printf "%4s | %-20s | %s\n" "$line_num" "$numbers" "$context"
    fi
done

echo ""
echo "=== End of Extraction ==="
