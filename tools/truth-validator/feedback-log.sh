#!/bin/bash
# Feedback Log — Loop 3 (Human Feedback Capture)
# Records validation failures, false positives, and corrections for Loop 4 improvement

set -e

FEEDBACK_FILE="/home/p62operator/.openclaw/workspace/memory/validation-feedback.jsonl"

# Ensure directory exists
mkdir -p "$(dirname "$FEEDBACK_FILE")"

usage() {
    echo "Usage: $0 --type <TYPE> --file <FILE> --issue <ISSUE> [--severity <SEV>] [--notes <NOTES>]"
    echo ""
    echo "Log human feedback on validation accuracy"
    echo ""
    echo "Types:"
    echo "  false-positive   — Validator flagged something that was actually correct"
    echo "  false-negative   — Validator missed an actual error"
    echo "  wrong-confidence — Confidence tag didn't match actual accuracy"
    echo "  source-error     — Source itself was wrong"
    echo "  correction       — User corrected a claim post-output"
    echo ""
    echo "Severity: LOW, MEDIUM, HIGH, CRITICAL"
    echo ""
    echo "Examples:"
    echo "  $0 --type false-negative --file n17-brief.md --issue \"Wrong vote count\" --severity HIGH"
    echo "  $0 --type correction --file n33-brief.md --issue \"Candidate name misspelled\" --notes \"Should be Mohd Fared\""
    exit 1
}

# Parse arguments
TYPE=""
FILE=""
ISSUE=""
SEVERITY="MEDIUM"
NOTES=""

while [[ $# -gt 0 ]]; do
    case $1 in
        --type) TYPE="$2"; shift 2 ;;
        --file) FILE="$2"; shift 2 ;;
        --issue) ISSUE="$2"; shift 2 ;;
        --severity) SEVERITY="$2"; shift 2 ;;
        --notes) NOTES="$2"; shift 2 ;;
        *) echo "Unknown option: $1"; usage ;;
    esac
done

if [ -z "$TYPE" ] || [ -z "$FILE" ] || [ -z "$ISSUE" ]; then
    usage
fi

# Generate timestamp
TIMESTAMP=$(date -u +%Y-%m-%dT%H:%M:%SZ)
DATE=$(date -u +%Y-%m-%d)

# Create feedback entry
cat >> "$FEEDBACK_FILE" << EOF
{"timestamp":"$TIMESTAMP","date":"$DATE","type":"$TYPE","file":"$FILE","issue":"$ISSUE","severity":"$SEVERITY","notes":"$NOTES","resolved":false}
EOF

echo "✓ Feedback logged to $FEEDBACK_FILE"
echo ""
echo "Entry:"
echo "  Type: $TYPE"
echo "  File: $FILE"
echo "  Issue: $ISSUE"
echo "  Severity: $SEVERITY"
[ -n "$NOTES" ] && echo "  Notes: $NOTES"
echo ""
echo "Next: Run monthly-review.sh to aggregate feedback and update rules"
