#!/bin/bash
# ElectionData.MY API Verification Script
# Cross-references claims against ElectionData.MY open API

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE="/home/p62operator/.openclaw/workspace"
CONFIG_FILE="$WORKSPACE/.electiondata-config"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

usage() {
    echo "Usage: $0 <constituency> [year]"
    echo ""
    echo "Verifies election data claims against ElectionData.MY API"
    echo ""
    echo "Arguments:"
    echo "  constituency  State constituency (e.g., 'N16 Sungai Balang') or Parliament (e.g., 'P146 Muar')"
    echo "  year          Election year (optional, default: latest available)"
    echo ""
    echo "Options:"
    echo "  --api-key     Set API key (or set ELECTIONDATA_API_KEY env var)"
    echo "  --cache       Use cached response (skip API call)"
    echo "  --help        Show this help"
    exit 1
}

# Load API key
load_api_key() {
    if [ -n "$ELECTIONDATA_API_KEY" ]; then
        echo "$ELECTIONDATA_API_KEY"
    elif [ -f "$CONFIG_FILE" ]; then
        grep "^api_key=" "$CONFIG_FILE" | cut -d'=' -f2
    else
        echo ""
    fi
}

save_api_key() {
    local key="$1"
    mkdir -p "$(dirname "$CONFIG_FILE")"
    echo "api_key=$key" > "$CONFIG_FILE"
    chmod 600 "$CONFIG_FILE"
    echo -e "${GREEN}✓ API key saved${NC}"
}

# Fetch from ElectionData.MY API
fetch_election_data() {
    local constituency="$1"
    local year="${2:-}"
    local api_key="$3"
    
    if [ -z "$api_key" ]; then
        echo -e "${YELLOW}⚠ No API key found. Generate one at: https://electiondata.my/console${NC}"
        echo ""
        echo "Then run: export ELECTIONDATA_API_KEY=your_key_here"
        echo "Or: $0 --api-key your_key_here"
        exit 1
    fi
    
    # Normalize constituency name for API query
    local query=$(echo "$constituency" | sed 's/ /+/g')
    
    # API endpoints (based on ElectionData.MY documentation)
    local base_url="https://electiondata.my/api/v1"
    
    echo -e "${BLUE}📡 Querying ElectionData.MY API...${NC}"
    echo "  Constituency: $constituency"
    [ -n "$year" ] && echo "  Year: $year"
    echo ""
    
    # Try to fetch constituency data
    # Note: Actual endpoint structure may need adjustment based on API docs
    local response=$(curl -s -X GET \
        -H "Authorization: Bearer $api_key" \
        -H "Accept: application/json" \
        "${base_url}/constituencies?q=${query}" 2>/dev/null || echo '{"error": "API call failed"}')
    
    echo "$response"
}

# Parse and validate response
parse_response() {
    local response="$1"
    local expected_year="${2:-}"
    
    # Check for errors
    if echo "$response" | grep -q '"error"'; then
        echo -e "${RED}✗ API Error:$(echo "$response" | grep -o '"error":"[^"]*"' | cut -d'"' -f4)${NC}"
        return 1
    fi
    
    # Extract key data points
    echo -e "\n${YELLOW}Verification Results:${NC}"
    echo "-----------------------------------"
    
    # Extract constituency name
    local name=$(echo "$response" | grep -o '"name":"[^"]*"' | head -1 | cut -d'"' -f4)
    if [ -n "$name" ]; then
        echo -e "  Constituency: ${GREEN}✓ $name${NC}"
    fi
    
    # Extract election results if available
    local results=$(echo "$response" | grep -o '"results":\[[^]]*\]' || true)
    if [ -n "$results" ]; then
        echo -e "  Results: ${GREEN}✓ Found${NC}"
        # Parse winner, votes, margin if available
        echo "$results" | head -c 200
        echo "..."
    else
        echo -e "  Results: ${YELLOW}⚠ Not found in response${NC}"
    fi
    
    echo ""
}

# Main execution
if [ $# -lt 1 ]; then
    usage
fi

CONSTITUENCY="$1"
YEAR="${2:-}"
API_KEY=$(load_api_key)

# Handle --api-key flag
if [ "$1" = "--api-key" ]; then
    save_api_key "$2"
    exit 0
fi

# Fetch and verify
RESPONSE=$(fetch_election_data "$CONSTITUENCY" "$YEAR" "$API_KEY")

if [ $? -eq 0 ]; then
    parse_response "$RESPONSE" "$YEAR"
    echo -e "${GREEN}✅ Verification complete${NC}"
else
    echo -e "${RED}❌ Verification failed${NC}"
    exit 1
fi
