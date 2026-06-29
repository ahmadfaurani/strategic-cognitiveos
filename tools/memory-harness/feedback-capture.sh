#!/bin/bash
#
# Memory Harness — Feedback Capture (Loop 3)
# Purpose: Capture human corrections to validation output
# Stores feedback in JSONL format for monthly review
#

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE="/home/p62operator/.openclaw/workspace"
FEEDBACK_FILE="$WORKSPACE/memory/validation-feedback.jsonl"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

usage() {
    cat << EOF
Usage: $(basename "$0") <command> [options]

Capture and manage human feedback on validation output.

Commands:
  add       Add a new feedback entry
  list      List recent feedback entries
  stats     Show feedback statistics
  export    Export feedback to JSON

Options for 'add':
  -f, --file FILE       Source file that was validated
  -c, --claim CLAIM     The claim that was corrected
  -t, --type TYPE       Feedback type: factual|confidence|source|citation
  -o, --old VALUE       Original (incorrect) value
  -n, --new VALUE       Corrected value
  -s, --source SOURCE   Correct source reference
  -m, --note NOTE       Additional notes
  -h, --help            Show this help

Examples:
  $(basename "$0") add -f brief.md -c "BN won by 4,041 votes" -t factual -o "4,041" -n "4,042" -s "SPR data"
  $(basename "$0") add -f brief.md -c "Turnout >80% favors PH" -t confidence -o "HIGH" -n "MEDIUM"
  $(basename "$0") list -n 10
  $(basename "$0") stats

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

# Initialize feedback file
init_feedback_file() {
    if [[ ! -f "$FEEDBACK_FILE" ]]; then
        touch "$FEEDBACK_FILE"
        log_info "Created feedback file: $FEEDBACK_FILE"
    fi
}

# Add feedback entry
add_feedback() {
    local file="${1:-}"
    local claim="${2:-}"
    local type="${3:-factual}"
    local old_value="${4:-}"
    local new_value="${5:-}"
    local source="${6:-}"
    local note="${7:-}"
    
    if [[ -z "$file" || -z "$claim" ]]; then
        log_error "File and claim are required"
        usage
    fi
    
    init_feedback_file
    
    local timestamp=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
    local id=$(uuidgen 2>/dev/null || echo "$(date +%s)-$$")
    
    # Build JSON entry
    local json=$(cat << EOF
{
  "id": "$id",
  "timestamp": "$timestamp",
  "file": "$file",
  "claim": "$claim",
  "type": "$type",
  "original": "$old_value",
  "corrected": "$new_value",
  "source": "$source",
  "note": "$note"
}
EOF
)
    
    # Append to feedback file
    echo "$json" >> "$FEEDBACK_FILE"
    
    log_success "Feedback captured"
    log_info "ID: $id"
    log_info "Type: $type"
    log_info "File: $file"
}

# List feedback entries
list_feedback() {
    local limit="${1:-10}"
    
    if [[ ! -f "$FEEDBACK_FILE" ]]; then
        log_info "No feedback entries yet"
        return 0
    fi
    
    log_info "Recent feedback (last $limit entries):"
    echo ""
    
    tail -n "$limit" "$FEEDBACK_FILE" | while IFS= read -r line; do
        local id=$(echo "$line" | jq -r '.id' 2>/dev/null || echo "unknown")
        local timestamp=$(echo "$line" | jq -r '.timestamp' 2>/dev/null || echo "unknown")
        local type=$(echo "$line" | jq -r '.type' 2>/dev/null || echo "unknown")
        local claim=$(echo "$line" | jq -r '.claim' 2>/dev/null | head -c 60)
        
        echo -e "${YELLOW}$timestamp${NC} [$type] $claim..."
        echo "  ID: $id"
        echo ""
    done
}

# Show feedback statistics
show_stats() {
    if [[ ! -f "$FEEDBACK_FILE" ]]; then
        log_info "No feedback entries yet"
        return 0
    fi
    
    local total=$(wc -l < "$FEEDBACK_FILE")
    local factual=$(grep -c '"type": "factual"' "$FEEDBACK_FILE" 2>/dev/null || echo 0)
    local confidence=$(grep -c '"type": "confidence"' "$FEEDBACK_FILE" 2>/dev/null || echo 0)
    local source=$(grep -c '"type": "source"' "$FEEDBACK_FILE" 2>/dev/null || echo 0)
    local citation=$(grep -c '"type": "citation"' "$FEEDBACK_FILE" 2>/dev/null || echo 0)
    
    log "========================================="
    log "Feedback Statistics"
    log "========================================="
    log_info "Total entries: $total"
    echo ""
    log "By type:"
    log "  Factual:    $factual"
    log "  Confidence: $confidence"
    log "  Source:     $source"
    log "  Citation:   $citation"
    echo ""
    
    # Show recent trend (last 7 days)
    local week_ago=$(date -u -d "7 days ago" +%Y-%m-%dT%H:%M:%SZ 2>/dev/null || date -u +%Y-%m-%dT%H:%M:%SZ)
    local recent=$(tail -n 100 "$FEEDBACK_FILE" | grep -c "\"timestamp\": \"$week_ago" 2>/dev/null || echo "N/A")
    
    log_info "Recent activity (last 7 days): ~$recent entries"
}

# Export feedback to JSON
export_feedback() {
    local output="${1:-$WORKSPACE/tools/memory-harness/feedback-export.json}"
    
    if [[ ! -f "$FEEDBACK_FILE" ]]; then
        log_error "No feedback file found"
        exit 1
    fi
    
    # Convert JSONL to JSON array
    echo "[" > "$output"
    local first=true
    while IFS= read -r line; do
        if [[ "$first" != "true" ]]; then
            echo "," >> "$output"
        fi
        first=false
        echo "  $line" >> "$output"
    done < "$FEEDBACK_FILE"
    echo "]" >> "$output"
    
    log_success "Exported to: $output"
}

# Main
main() {
    if [[ $# -lt 1 ]]; then
        usage
    fi
    
    local command="$1"
    shift
    
    case $command in
        add)
            local file=""
            local claim=""
            local type="factual"
            local old_value=""
            local new_value=""
            local source=""
            local note=""
            
            while [[ $# -gt 0 ]]; do
                case $1 in
                    -f|--file)
                        file="$2"
                        shift 2
                        ;;
                    -c|--claim)
                        claim="$2"
                        shift 2
                        ;;
                    -t|--type)
                        type="$2"
                        shift 2
                        ;;
                    -o|--old)
                        old_value="$2"
                        shift 2
                        ;;
                    -n|--new)
                        new_value="$2"
                        shift 2
                        ;;
                    -s|--source)
                        source="$2"
                        shift 2
                        ;;
                    -m|--note)
                        note="$2"
                        shift 2
                        ;;
                    -h|--help)
                        usage
                        ;;
                    *)
                        shift
                        ;;
                esac
            done
            
            add_feedback "$file" "$claim" "$type" "$old_value" "$new_value" "$source" "$note"
            ;;
        list)
            local limit=10
            while [[ $# -gt 0 ]]; do
                case $1 in
                    -n|--limit)
                        limit="$2"
                        shift 2
                        ;;
                    *)
                        shift
                        ;;
                esac
            done
            list_feedback "$limit"
            ;;
        stats)
            show_stats
            ;;
        export)
            local output="$1"
            export_feedback "$output"
            ;;
        *)
            log_error "Unknown command: $command"
            usage
            ;;
    esac
}

main "$@"
