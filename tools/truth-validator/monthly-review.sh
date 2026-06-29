#!/bin/bash
# Monthly Review — Loop 4 (System Improvement)
# Aggregates feedback, identifies patterns, updates validation rules

set -e

FEEDBACK_FILE="/home/p62operator/.openclaw/workspace/memory/validation-feedback.jsonl"
REPORT_FILE="/home/p62operator/.openclaw/workspace/memory/validation-monthly-review-$(date -u +%Y-%m).md"

echo "=== Monthly Validation Review ==="
echo "Month: $(date -u +%Y-%m)"
echo ""

# Check if feedback file exists
if [ ! -f "$FEEDBACK_FILE" ]; then
    echo "No feedback data found. Run feedback-log.sh to record issues."
    exit 0
fi

# Count feedback by type
echo "[1] Feedback Summary"
echo "-----------------------------------"

TOTAL=$(wc -l < "$FEEDBACK_FILE")
FALSE_POS=$(grep -c '"type":"false-positive"' "$FEEDBACK_FILE" 2>/dev/null || echo 0)
FALSE_NEG=$(grep -c '"type":"false-negative"' "$FEEDBACK_FILE" 2>/dev/null || echo 0)
WRONG_CONF=$(grep -c '"type":"wrong-confidence"' "$FEEDBACK_FILE" 2>/dev/null || echo 0)
SOURCE_ERR=$(grep -c '"type":"source-error"' "$FEEDBACK_FILE" 2>/dev/null || echo 0)
CORRECTIONS=$(grep -c '"type":"correction"' "$FEEDBACK_FILE" 2>/dev/null || echo 0)

echo "  Total feedback: $TOTAL"
echo "  False positives: $FALSE_POS"
echo "  False negatives: $FALSE_NEG"
echo "  Wrong confidence: $WRONG_CONF"
echo "  Source errors: $SOURCE_ERR"
echo "  Corrections: $CORRECTIONS"
echo ""

# Count by severity
echo "[2] Severity Breakdown"
echo "-----------------------------------"

CRITICAL=$(grep -c '"severity":"CRITICAL"' "$FEEDBACK_FILE" 2>/dev/null || echo 0)
HIGH=$(grep -c '"severity":"HIGH"' "$FEEDBACK_FILE" 2>/dev/null || echo 0)
MEDIUM=$(grep -c '"severity":"MEDIUM"' "$FEEDBACK_FILE" 2>/dev/null || echo 0)
LOW=$(grep -c '"severity":"LOW"' "$FEEDBACK_FILE" 2>/dev/null || echo 0)

echo "  Critical: $CRITICAL"
echo "  High: $HIGH"
echo "  Medium: $MEDIUM"
echo "  Low: $LOW"
echo ""

# Identify patterns (most common issues)
echo "[3] Common Issues"
echo "-----------------------------------"

# Extract issue field and count
grep -oE '"issue":"[^"]*"' "$FEEDBACK_FILE" | sort | uniq -c | sort -rn | head -10 | while read -r count issue; do
    echo "  $count × $issue"
done
echo ""

# Unresolved issues
echo "[4] Unresolved Issues"
echo "-----------------------------------"

UNRESOLVED=$(grep -c '"resolved":false' "$FEEDBACK_FILE" 2>/dev/null || echo 0)
echo "  Unresolved: $UNRESOLVED"

if [ $UNRESOLVED -gt 0 ]; then
    echo ""
    echo "  Unresolved items requiring attention:"
    grep '"resolved":false' "$FEEDBACK_FILE" | while read -r line; do
        FILE=$(echo "$line" | grep -oE '"file":"[^"]*"' | cut -d'"' -f4)
        ISSUE=$(echo "$line" | grep -oE '"issue":"[^"]*"' | cut -d'"' -f4)
        SEV=$(echo "$line" | grep -oE '"severity":"[^"]*"' | cut -d'"' -f4)
        echo "    - [$SEV] $FILE: $ISSUE"
    done
fi
echo ""

# Generate report
echo "[5] Generating Monthly Report"
echo "-----------------------------------"

cat > "$REPORT_FILE" << EOF
# Validation Monthly Review — $(date -u +%Y-%m)

**Generated:** $(date -u +%Y-%m-%d)

## Summary

| Metric | Value |
|--------|-------|
| Total Feedback | $TOTAL |
| False Positives | $FALSE_POS |
| False Negatives | $FALSE_NEG |
| Wrong Confidence | $WRONG_CONF |
| Source Errors | $SOURCE_ERR |
| Corrections | $CORRECTIONS |

## Severity Distribution

| Severity | Count |
|----------|-------|
| Critical | $CRITICAL |
| High | $HIGH |
| Medium | $MEDIUM |
| Low | $LOW |

## Top Issues

$(grep -oE '"issue":"[^"]*"' "$FEEDBACK_FILE" | sort | uniq -c | sort -rn | head -10 | awk '{print "- " $0}')

## Action Items

$(if [ $CRITICAL -gt 0 ] || [ $HIGH -gt 0 ]; then echo "### Urgent (Critical/High)"; grep -E '"severity":"(CRITICAL|HIGH)"' "$FEEDBACK_FILE" | while read -r line; do FILE=$(echo "$line" | grep -oE '"file":"[^"]*"' | cut -d'"' -f4); ISSUE=$(echo "$line" | grep -oE '"issue":"[^"]*"' | cut -d'"' -f4); echo "- [ ] Fix: $ISSUE (in $FILE)"; done; echo ""; fi)

## Recommendations for Loop 4

$(if [ $FALSE_POS -gt $FALSE_NEG ]; then echo "- Validator is too strict — consider relaxing rules for: (see top issues)"; elif [ $FALSE_NEG -gt $FALSE_POS ]; then echo "- Validator is missing errors — add rules for: (see top issues)"; else echo "- Balance is good — continue monitoring"; fi)

---

*Review completed. Update validation rules based on findings.*
EOF

echo "  Report generated: $REPORT_FILE"
echo ""

# Summary
echo "=== Review Complete ==="
echo ""
echo "Key Findings:"
[ $CRITICAL -gt 0 ] && echo "  ⚠ $CRITICAL critical issues need immediate attention"
[ $FALSE_NEG -gt $FALSE_POS ] && echo "  ⚠ More false negatives than positives — validator missing real errors"
[ $FALSE_POS -gt $FALSE_NEG ] && echo "  ℹ More false positives — validator may be too strict"
[ $UNRESOLVED -gt 0 ] && echo "  ⚠ $UNRESOLVED unresolved issues in feedback log"

echo ""
echo "Next Steps:"
echo "  1. Review $REPORT_FILE"
echo "  2. Update validation rules in validate.sh"
echo "  3. Mark resolved items: grep -l 'issue' $FEEDBACK_FILE | sed -i 's/\"resolved\":false/\"resolved\":true/'"
echo ""
