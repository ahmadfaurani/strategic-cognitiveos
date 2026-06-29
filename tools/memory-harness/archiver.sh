#!/bin/bash
#
# Memory Harness — Archiver
# Purpose: Archive old memory files to reduce bootstrap load
# Moves files to memory/archive/ with date-based organization
#

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE="/home/p62operator/.openclaw/workspace"
MEMORY_DIR="$WORKSPACE/memory"
ARCHIVE_DIR="$MEMORY_DIR/archive"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

usage() {
    cat << EOF
Usage: $(basename "$0") [options]

Archive old memory files to reduce bootstrap load.

Options:
  -d, --days N          Archive files older than N days (default: 30)
  -n, --dry-run         Show what would be archived (don't move)
  -l, --list            List files that would be archived
  -k, --keep N          Keep at least N most recent files (default: 10)
  -h, --help            Show this help

Examples:
  $(basename "$0") -d 30              # Archive files >30 days old
  $(basename "$0") -d 7 -n            # Dry-run: show files >7 days old
  $(basename "$0") -l                 # List archivable files
  $(basename "$0") -d 30 -k 15        # Archive >30 days, keep 15 recent

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

log_warn() {
    log "${YELLOW}!${NC} $1"
}

log_info() {
    log "${BLUE}ℹ${NC} $1"
}

# Get files older than N days
get_old_files() {
    local days="$1"
    local keep="$2"
    
    # Get all .md files except MEMORY.md, sorted by date (newest first)
    local all_files=()
    while IFS= read -r -d '' file; do
        all_files+=("$file")
    done < <(find "$MEMORY_DIR" -maxdepth 1 -name "*.md" ! -name "MEMORY.md" -print0 | sort -rz)
    
    # Skip the N most recent files
    local skip_count=0
    local old_files=()
    
    for file in "${all_files[@]}"; do
        if [[ $skip_count -lt $keep ]]; then
            ((skip_count++)) || true
            continue
        fi
        
        # Check file age
        local file_date=$(basename "$file" .md)
        local file_ts=$(date -d "$file_date" +%s 2>/dev/null || echo 0)
        local now_ts=$(date +%s)
        local age_days=$(( (now_ts - file_ts) / 86400 ))
        
        if [[ $age_days -gt $days ]]; then
            old_files+=("$file")
        fi
    done
    
    echo "${old_files[@]}"
}

# Archive files
archive_files() {
    local days="${1:-30}"
    local keep="${2:-10}"
    local dry_run="${3:-false}"
    
    log "========================================="
    log "Memory Harness — Archiver"
    log "========================================="
    log_info "Archiving files older than $days days (keeping $keep most recent)"
    
    if [[ "$dry_run" == "true" ]]; then
        log_info "DRY RUN — No files will be moved"
    fi
    
    echo ""
    
    # Create archive directory
    if [[ "$dry_run" != "true" ]]; then
        mkdir -p "$ARCHIVE_DIR"
    fi
    
    # Get old files
    local old_files=($(get_old_files "$days" "$keep"))
    local count=${#old_files[@]}
    
    if [[ $count -eq 0 ]]; then
        log_success "No files to archive"
        return 0
    fi
    
    log_info "Found $count files to archive:"
    echo ""
    
    local archived=0
    local failed=0
    
    for file in "${old_files[@]}"; do
        local filename=$(basename "$file")
        local file_date="${filename%.md}"
        local year_month=$(echo "$file_date" | cut -d'-' -f1,2)
        local target_dir="$ARCHIVE_DIR/$year_month"
        local target_path="$target_dir/$filename"
        
        if [[ "$dry_run" == "true" ]]; then
            log_info "  Would archive: $filename → $target_path"
            ((archived++)) || true
        else
            mkdir -p "$target_dir"
            if mv "$file" "$target_path" 2>/dev/null; then
                log_success "Archived: $filename → $target_path"
                ((archived++)) || true
            else
                log_error "Failed: $filename"
                ((failed++)) || true
            fi
        fi
    done
    
    echo ""
    log_success "Archived $archived files"
    
    if [[ $failed -gt 0 ]]; then
        log_warn "$failed files failed to archive"
    fi
    
    if [[ "$dry_run" != "true" ]]; then
        log_info "Archive location: $ARCHIVE_DIR"
    fi
}

# List files that would be archived
list_archivable() {
    local days="${1:-30}"
    local keep="${2:-10}"
    
    log_info "Files that would be archived (older than $days days, keeping $keep):"
    echo ""
    
    local old_files=($(get_old_files "$days" "$keep"))
    
    if [[ ${#old_files[@]} -eq 0 ]]; then
        log_success "No files to archive"
    else
        for file in "${old_files[@]}"; do
            echo "  $(basename "$file")"
        done
        echo ""
        log_info "Total: ${#old_files[@]} files"
    fi
}

# Main
main() {
    local days=30
    local keep=10
    local dry_run=false
    local list_only=false
    
    while [[ $# -gt 0 ]]; do
        case $1 in
            -d|--days)
                days="$2"
                shift 2
                ;;
            -n|--dry-run)
                dry_run=true
                shift
                ;;
            -l|--list)
                list_only=true
                shift
                ;;
            -k|--keep)
                keep="$2"
                shift 2
                ;;
            -h|--help)
                usage
                ;;
            *)
                echo "Unknown option: $1"
                usage
                ;;
        esac
    done
    
    if [[ "$list_only" == "true" ]]; then
        list_archivable "$days" "$keep"
    else
        archive_files "$days" "$keep" "$dry_run"
    fi
}

main "$@"
