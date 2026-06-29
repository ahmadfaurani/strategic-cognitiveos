#!/bin/bash
#
# Memory Harness — Calibration Check (Loop 4)
# Purpose: Validate confidence tag accuracy over time
# Tracks which sources/tags are reliable
#

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE="/home/p62operator/.openclaw/workspace"
FEEDBACK_FILE="$WORKSPACE/memory/validation-feedback.jsonl"
CALIBRATION_FILE="$WORKSPACE/memory/confidence-calibration.json"
SOURCE_ACCURACY_FILE="$WORKSPACE/memory/source-accuracy.json"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

usage() {
    cat << EOF
Usage: $(basename "$0") <command> [options]

Validate and track confidence calibration over time.

Commands:
  analyze     Analyze feedback to update calibration data
  report      Generate calibration report
  source      Show source accuracy statistics
  reset       Reset calibration data (use with caution)
  help        Show this help

Examples:
  $(basename "$0") analyze
  $(basename "$0") report
  $(basename "$0") source --tier 0
  $(basename "$0") reset --confirm

EOF
    exit 1
}

log() {
    echo -e "$1"
}

log_success() {
    log "${GREEN}✓${NC} $1"
}

log_error() {
    log "${RED}✗${NC} $1"
}

log_info() {
    log "${BLUE}ℹ${NC} $1"
}

# Initialize calibration files
init_files() {
    if [[ ! -f "$CALIBRATION_FILE" ]]; then
        cat > "$CALIBRATION_FILE" << 'EOF'
{
  "lastUpdated": null,
  "confidenceAccuracy": {
    "HIGH": {"total": 0, "correct": 0, "accuracy": 0},
    "MEDIUM": {"total": 0, "correct": 0, "accuracy": 0},
    "LOW": {"total": 0, "correct": 0, "accuracy": 0}
  },
  "typeAccuracy": {
    "factual": {"total": 0, "correct": 0},
    "confidence": {"total": 0, "correct": 0},
    "source": {"total": 0, "correct": 0},
    "citation": {"total": 0, "correct": 0}
  }
}
EOF
        log_info "Created calibration file: $CALIBRATION_FILE"
    fi
    
    if [[ ! -f "$SOURCE_ACCURACY_FILE" ]]; then
        cat > "$SOURCE_ACCURACY_FILE" << 'EOF'
{
  "lastUpdated": null,
  "sources": {}
}
EOF
        log_info "Created source accuracy file: $SOURCE_ACCURACY_FILE"
    fi
}

# Analyze feedback and update calibration
analyze_feedback() {
    log "========================================="
    log "Calibration Analysis (Loop 4)"
    log "========================================="
    
    init_files
    
    if [[ ! -f "$FEEDBACK_FILE" || ! -s "$FEEDBACK_FILE" ]]; then
        log_info "No feedback data to analyze"
        return 0
    fi
    
    local total_feedback=$(wc -l < "$FEEDBACK_FILE")
    log_info "Analyzing $total_feedback feedback entries..."
    echo ""
    
    # Count by confidence type (simplified analysis)
    local high_count=$(grep -c '"original": "HIGH"' "$FEEDBACK_FILE" 2>/dev/null || echo 0)
    local medium_count=$(grep -c '"original": "MEDIUM"' "$FEEDBACK_FILE" 2>/dev/null || echo 0)
    local low_count=$(grep -c '"original": "LOW"' "$FEEDBACK_FILE" 2>/dev/null || echo 0)
    
    # Count corrections (where original != corrected)
    local high_corrected=$(grep '"original": "HIGH"' "$FEEDBACK_FILE" 2>/dev/null | grep -cv '"corrected": "HIGH"' 2>/dev/null || echo 0)
    local medium_corrected=$(grep '"original": "MEDIUM"' "$FEEDBACK_FILE" 2>/dev/null | grep -cv '"corrected": "MEDIUM"' 2>/dev/null || echo 0)
    local low_corrected=$(grep '"original": "LOW"' "$FEEDBACK_FILE" 2>/dev/null | grep -cv '"corrected": "LOW"' 2>/dev/null || echo 0)
    
    # Calculate accuracy
    local high_total=$((high_count))
    local high_correct=$((high_total - high_corrected))
    local high_accuracy=0
    if [[ $high_total -gt 0 ]]; then
        high_accuracy=$(echo "scale=2; $high_correct * 100 / $high_total" | bc 2>/dev/null || echo "N/A")
    fi
    
    local medium_total=$((medium_count))
    local medium_correct=$((medium_total - medium_corrected))
    local medium_accuracy=0
    if [[ $medium_total -gt 0 ]]; then
        medium_accuracy=$(echo "scale=2; $medium_correct * 100 / $medium_total" | bc 2>/dev/null || echo "N/A")
    fi
    
    local low_total=$((low_count))
    local low_correct=$((low_total - low_corrected))
    local low_accuracy=0
    if [[ $low_total -gt 0 ]]; then
        low_accuracy=$(echo "scale=2; $low_correct * 100 / $low_total" | bc 2>/dev/null || echo "N/A")
    fi
    
    # Update calibration file
    local timestamp=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
    
    cat > "$CALIBRATION_FILE" << EOF
{
  "lastUpdated": "$timestamp",
  "confidenceAccuracy": {
    "HIGH": {"total": $high_total, "correct": $high_correct, "accuracy": $high_accuracy},
    "MEDIUM": {"total": $medium_total, "correct": $medium_correct, "accuracy": $medium_accuracy},
    "LOW": {"total": $low_total, "correct": $low_correct, "accuracy": $low_accuracy}
  },
  "typeAccuracy": {
    "factual": {"total": $(grep -c '"type": "factual"' "$FEEDBACK_FILE" 2>/dev/null || echo 0), "correct": 0},
    "confidence": {"total": $(grep -c '"type": "confidence"' "$FEEDBACK_FILE" 2>/dev/null || echo 0), "correct": 0},
    "source": {"total": $(grep -c '"type": "source"' "$FEEDBACK_FILE" 2>/dev/null || echo 0), "correct": 0},
    "citation": {"total": $(grep -c '"type": "citation"' "$FEEDBACK_FILE" 2>/dev/null || echo 0), "correct": 0}
  }
}
EOF
    
    log_success "Calibration updated"
    echo ""
    log "Confidence Accuracy:"
    log "  HIGH:   $high_correct/$high_total ($high_accuracy%)"
    log "  MEDIUM: $medium_correct/$medium_total ($medium_accuracy%)"
    log "  LOW:    $low_correct/$low_total ($low_accuracy%)"
}

# Generate calibration report
generate_report() {
    if [[ ! -f "$CALIBRATION_FILE" ]]; then
        log_info "No calibration data. Run 'analyze' first."
        return 0
    fi
    
    log "========================================="
    log "Calibration Report"
    log "========================================="
    
    local last_updated=$(jq -r '.lastUpdated' "$CALIBRATION_FILE" 2>/dev/null || echo "Never")
    log_info "Last updated: $last_updated"
    echo ""
    
    log "Confidence Tag Accuracy:"
    echo ""
    
    for tag in HIGH MEDIUM LOW; do
        local total=$(jq -r ".confidenceAccuracy.$tag.total" "$CALIBRATION_FILE" 2>/dev/null || echo 0)
        local correct=$(jq -r ".confidenceAccuracy.$tag.correct" "$CALIBRATION_FILE" 2>/dev/null || echo 0)
        local accuracy=$(jq -r ".confidenceAccuracy.$tag.accuracy" "$CALIBRATION_FILE" 2>/dev/null || echo 0)
        
        local bar=""
        if [[ "$accuracy" != "N/A" && "$accuracy" != "0" ]]; then
            local filled=$(echo "$accuracy / 10" | bc 2>/dev/null || echo 0)
            bar=$(printf '%*s' "$filled" | tr ' ' '█')
            bar=$(printf '%*s' 10 | tr ' ' '░' | sed "s/░/$bar/g" | head -c 10)
        else
            bar="N/A       "
        fi
        
        printf "  %-8s [%s] %3s%% (%s/%s)\n" "$tag:" "$bar" "$accuracy" "$correct" "$total"
    done
    
    echo ""
    log_info "Recommendation: If HIGH accuracy <90%, consider tightening validation criteria."
}

# Show source accuracy
show_source_accuracy() {
    local tier_filter="${1:-}"
    
    if [[ ! -f "$SOURCE_ACCURACY_FILE" ]]; then
        log_info "No source accuracy data yet"
        return 0
    fi
    
    log "========================================="
    log "Source Accuracy by Tier"
    log "========================================="
    
    # Placeholder - would need to integrate with source registry
    log_info "Source accuracy tracking not yet implemented"
    log_info "This will track Tier 0-4 source reliability over time"
}

# Reset calibration data
reset_calibration() {
    local confirm="${1:-false}"
    
    if [[ "$confirm" != "true" ]]; then
        log_error "Reset requires --confirm flag"
        log_error "This will delete all calibration data!"
        echo ""
        echo "Usage: $(basename "$0") reset --confirm"
        exit 1
    fi
    
    rm -f "$CALIBRATION_FILE" "$SOURCE_ACCURACY_FILE"
    init_files
    
    log_success "Calibration data reset"
}

# Main
main() {
    if [[ $# -lt 1 ]]; then
        usage
    fi
    
    local command="$1"
    shift
    
    case $command in
        analyze)
            analyze_feedback
            ;;
        report)
            generate_report
            ;;
        source)
            local tier=""
            while [[ $# -gt 0 ]]; do
                case $1 in
                    -t|--tier)
                        tier="$2"
                        shift 2
                        ;;
                    *)
                        shift
                        ;;
                esac
            done
            show_source_accuracy "$tier"
            ;;
        reset)
            local confirm=false
            while [[ $# -gt 0 ]]; do
                case $1 in
                    --confirm)
                        confirm=true
                        shift
                        ;;
                    *)
                        shift
                        ;;
                esac
            done
            reset_calibration "$confirm"
            ;;
        help|--help|-h)
            usage
            ;;
        *)
            log_error "Unknown command: $command"
            usage
            ;;
    esac
}

main "$@"
