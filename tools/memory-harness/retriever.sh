#!/bin/bash
#
# Memory Harness — Retriever
# Purpose: Retrieve relevant memory files via keyword search
# Works without embedding API (uses QMD keyword search)
#

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE="/home/p62operator/.openclaw/workspace"
MEMORY_DIR="$WORKSPACE/memory"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

usage() {
    cat << EOF
Usage: $(basename "$0") <query> [options]

Search memory files for relevant content.

Options:
  -n, --limit N       Max results (default: 10)
  -f, --file FILE     Search specific file
  -d, --date DATE     Search files from date (YYYY-MM-DD)
  -t, --tag TAG       Filter by tag (e.g., "war-room", "brief")
  -j, --json          Output as JSON
  -h, --help          Show this help

Examples:
  $(basename "$0") "N17 Semerah"
  $(basename "$0") "turnout analysis" -n 5
  $(basename "$0") "BN candidate" -d 2026-06-27
  $(basename "$0") "validation" -t brief -j

EOF
    exit 1
}

# Search memory files
search_memory() {
    local query="$1"
    local limit="${2:-10}"
    local file_filter="${3:-}"
    local date_filter="${4:-}"
    local tag_filter="${5:-}"
    local json_output="${6:-false}"
    
    local results=()
    local count=0
    
    # Build file list
    local files=()
    
    if [[ -n "$file_filter" ]]; then
        files=("$MEMORY_DIR/$file_filter")
    elif [[ -n "$date_filter" ]]; then
        files=("$MEMORY_DIR/${date_filter}.md")
    else
        # Get all .md files, sorted by date (newest first)
        while IFS= read -r -d '' file; do
            files+=("$file")
        done < <(find "$MEMORY_DIR" -maxdepth 1 -name "*.md" -print0 | sort -rz)
    fi
    
    # Search files
    for file in "${files[@]}"; do
        if [[ ! -f "$file" ]]; then
            continue
        fi
        
        # Apply tag filter if specified
        if [[ -n "$tag_filter" ]]; then
            if ! grep -q "tags:.*$tag_filter" "$file" 2>/dev/null; then
                continue
            fi
        fi
        
        # Search for query
        local matches=$(grep -n -i -C 2 "$query" "$file" 2>/dev/null || true)
        
        if [[ -n "$matches" ]]; then
            results+=("$file|$matches")
            ((count++)) || true
            
            if [[ $count -ge $limit ]]; then
                break
            fi
        fi
    done
    
    # Output results
    if [[ "$json_output" == "true" ]]; then
        echo "{"
        echo "  \"query\": \"$query\","
        echo "  \"results\": ["
        
        local first=true
        for result in "${results[@]}"; do
            local file="${result%%|*}"
            local content="${result#*|}"
            
            if [[ "$first" != "true" ]]; then
                echo ","
            fi
            first=false
            
            echo -n "    {\"file\": \"$file\", \"matches\": $(echo "$content" | jq -R -s -c 'split("\n") | map(select(length > 0))')}"
        done
        
        echo ""
        echo "  ],"
        echo "  \"count\": $count"
        echo "}"
    else
        echo -e "${BLUE}Search: $query${NC}"
        echo -e "${GREEN}Found $count results${NC}"
        echo ""
        
        for result in "${results[@]}"; do
            local file="${result%%|*}"
            local content="${result#*|}"
            
            echo -e "${YELLOW}$(basename "$file")${NC}"
            echo "$content"
            echo "---"
        done
    fi
    
    return $count
}

# Main
main() {
    local query=""
    local limit=10
    local file_filter=""
    local date_filter=""
    local tag_filter=""
    local json_output=false
    
    while [[ $# -gt 0 ]]; do
        case $1 in
            -n|--limit)
                limit="$2"
                shift 2
                ;;
            -f|--file)
                file_filter="$2"
                shift 2
                ;;
            -d|--date)
                date_filter="$2"
                shift 2
                ;;
            -t|--tag)
                tag_filter="$2"
                shift 2
                ;;
            -j|--json)
                json_output=true
                shift
                ;;
            -h|--help)
                usage
                ;;
            -*)
                echo "Unknown option: $1"
                usage
                ;;
            *)
                if [[ -z "$query" ]]; then
                    query="$1"
                fi
                shift
                ;;
        esac
    done
    
    if [[ -z "$query" ]]; then
        echo "Error: Query required"
        usage
    fi
    
    search_memory "$query" "$limit" "$file_filter" "$date_filter" "$tag_filter" "$json_output"
}

main "$@"
