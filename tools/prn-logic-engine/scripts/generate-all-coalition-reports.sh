#!/usr/bin/env bash
# PRN Johor 2026 - Multi-Coalition Daily Report Generator
# Classification: TLP:AMBER
# Usage: ./generate-all-coalition-reports.sh 2026-06-27

set -e

REPORT_DATE="${1:-$(date +%Y-%m-%d)}"
CAMPAIGN_DAY="D-14"  # Will be calculated based on nomination date
WORKSPACE="/home/p62operator/.openclaw/workspace-hoi/intelligence/prn-johor-2026"
OUTPUT_DIR="$WORKSPACE/coalition-analysis"

echo "🔵 PRN Johor 2026 - Multi-Coalition Daily Report Generator"
echo "Report Date: $REPORT_DATE"
echo "Output Directory: $OUTPUT_DIR"
echo ""

# Calculate campaign day (Nomination: 2026-06-26, Polling: 2026-07-12)
NOMINATION_DATE="2026-06-26"
DAYS_SINCE_NOMINATION=$(( ($(date -d "$REPORT_DATE" +%s) - $(date -d "$NOMINATION_DATE" +%s)) / 86400 ))
CAMPAIGN_DAY="D+$DAYS_SINCE_NOMINATION"

echo "Campaign Day: $CAMPAIGN_DAY"
echo ""

# Function to generate report for a coalition
generate_report() {
    local COALITION="$1"
    local TEMPLATE="$OUTPUT_DIR/${COALITION}-daily-template.md"
    local OUTPUT="$OUTPUT_DIR/${COALITION}-daily-${REPORT_DATE}.md"
    
    echo "📊 Generating $COALITION report..."
    
    if [ ! -f "$TEMPLATE" ]; then
        echo "❌ Template not found: $TEMPLATE"
        return 1
    fi
    
    # Replace placeholders with actual date info
    sed -e "s/{{REPORT_DATE}}/$REPORT_DATE/g" \
        -e "s/{{CAMPAIGN_DAY}}/$CAMPAIGN_DAY/g" \
        -e "s/{{TIMESTAMP}}/$(date '+%Y-%m-%d %H:%M:%S')/g" \
        -e "s/{{NEXT_REPORT}}/$(date -d "$REPORT_DATE + 1 day" '+%Y-%m-%d')/g" \
        "$TEMPLATE" > "$OUTPUT"
    
    echo "✅ $COALITION report generated: $OUTPUT"
}

# Generate reports for all coalitions
generate_report "pn"
generate_report "bn"
generate_report "ph"
generate_report "independent"

echo ""
echo "📈 All coalition reports generated successfully!"
echo ""
echo "Generated files:"
ls -lh "$OUTPUT_DIR"/*-daily-${REPORT_DATE}.md 2>/dev/null || echo "No reports found"
echo ""
echo "Next steps:"
echo "1. Review and populate reports with intelligence data"
echo "2. Commit to Git: cd $WORKSPACE && git add . && git commit -m 'Daily reports: $REPORT_DATE'"
echo "3. Push to GitHub: git push origin main"
