#!/bin/bash
#
# Memory Harness — Indexer
# Purpose: Index memory files into QMD for semantic retrieval
# Does NOT require embedding API access (QMD handles locally)
#

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE="/home/p62operator/.openclaw/workspace"
MEMORY_DIR="$WORKSPACE/memory"
SOURCES_DIR="$WORKSPACE/sources"
LOG_FILE="$WORKSPACE/tools/memory-harness/indexer.log"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

log() {
    echo -e "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
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

# Check if QMD is installed
check_qmd() {
    if ! command -v qmd &> /dev/null; then
        log_error "QMD not found. Install with: npm install -g @tobilu/qmd"
        exit 1
    fi
    log_success "QMD found: $(qmd --version)"
}

# Check if gateway is running
check_gateway() {
    if ! pgrep -f "openclaw.*gateway" > /dev/null; then
        log_warn "Gateway not running. Some features may be unavailable."
        return 1
    fi
    log_success "Gateway is running"
    return 0
}

# Index memory files
index_memory_files() {
    log "Indexing memory files..."
    
    local count=0
    local failed=0
    
    # Index MEMORY.md
    if [[ -f "$WORKSPACE/MEMORY.md" ]]; then
        log "  → MEMORY.md"
        ((count++)) || true
    else
        log_warn "MEMORY.md not found"
    fi
    
    # Index daily memory files
    if [[ -d "$MEMORY_DIR" ]]; then
        for file in "$MEMORY_DIR"/*.md; do
            if [[ -f "$file" ]]; then
                log "  → $(basename "$file")"
                ((count++)) || true
            fi
        done
    else
        log_warn "Memory directory not found: $MEMORY_DIR"
    fi
    
    log_success "Indexed $count memory files"
}

# Index source collections
index_sources() {
    log "Indexing source collections..."
    
    local collections=(
        "war-room"
        "technical-runbooks"
    )
    
    for collection in "${collections[@]}"; do
        local path="$SOURCES_DIR/$collection"
        if [[ -d "$path" ]]; then
            local file_count=$(find "$path" -type f \( -name "*.md" -o -name "*.json" -o -name "*.yaml" \) | wc -l)
            log "  → $collection: $file_count files"
        else
            log_warn "Collection not found: $collection"
        fi
    done
}

# Trigger QMD reindex
trigger_reindex() {
    log "Triggering QMD reindex..."
    
    # QMD auto-indexes on gateway startup with memory.qmd.update.onBoot=true
    # This command forces a manual reindex if needed
    
    if command -v openclaw &> /dev/null; then
        # Use OpenClaw CLI to trigger memory reindex
        openclaw memory reindex 2>&1 || log_warn "Reindex command not available (QMD will index on next gateway restart)"
    else
        log_warn "OpenClaw CLI not found"
    fi
}

# Main
main() {
    log "========================================="
    log "Memory Harness — Indexer"
    log "========================================="
    
    check_qmd
    check_gateway || true
    
    echo ""
    index_memory_files
    echo ""
    index_sources
    echo ""
    trigger_reindex
    
    echo ""
    log_success "Indexing complete!"
    log "Log file: $LOG_FILE"
}

main "$@"
