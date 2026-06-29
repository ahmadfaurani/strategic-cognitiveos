#!/bin/bash
# Cross-Reference Engine
# Compares claims across multiple sources, computes Confidence Assertion

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REGISTRY="/home/p62operator/.openclaw/workspace/tools/source-registry/sources.yaml"
RAW_DIR="/home/p62operator/.openclaw/workspace/memory/signals/raw"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

usage() {
    echo "Usage: $0 <claim-type> [search-term]"
    echo ""
    echo "Cross-references a claim across multiple sources"
    echo ""
    echo "Claim types:"
    echo "  candidate     — Candidate name/party for constituency"
    echo "  result        — Election result (votes, majority)"
    echo "  demographic   — Voter demographics (%, electorate size)"
    echo "  turnout       — Turnout figures"
    echo ""
    echo "Examples:"
    echo "  $0 candidate \"N17 Semerah\""
    echo "  $0 result \"N17 Semerah 2022\""
    echo "  $0 demographic \"N33 Tenggaroh\""
    exit 1
}

if [ $# -lt 1 ]; then
    usage
fi

CLAIM_TYPE="$1"
SEARCH_TERM="${2:-}"

echo -e "${BLUE}=== Cross-Reference Engine ===${NC}"
echo "Claim Type: $CLAIM_TYPE"
[ -n "$SEARCH_TERM" ] && echo "Search Term: $SEARCH_TERM"
echo ""

# Find latest raw data files
SPR_FILE=$(ls -t "$RAW_DIR"/*-spr-official.jsonl 2>/dev/null | head -1)
MKINI_FILE=$(ls -t "$RAW_DIR"/*-mkini.jsonl 2>/dev/null | head -1)

# Track sources and values
declare -A SOURCE_VALUES
declare -A SOURCE_TIERS
CONVERGED=0
CONFLICTING=0

echo -e "${YELLOW}[1] Checking Tier 0 (Official)${NC}"
echo "-----------------------------------"

if [ -f "$SPR_FILE" ]; then
    echo "  Source: SPR Official"
    # Extract relevant data (simplified; production needs proper JSON parsing)
    if grep -qi "$SEARCH_TERM" "$SPR_FILE" 2>/dev/null; then
        VALUE=$(grep -i "$SEARCH_TERM" "$SPR_FILE" | head -1)
        echo "  Value: $VALUE"
        SOURCE_VALUES["SPR"]="$VALUE"
        SOURCE_TIERS["SPR"]=0
        echo -e "  ${GREEN}✓ Found${NC}"
    else
        echo -e "  ${YELLOW}⚠ Not found in latest SPR data${NC}"
    fi
else
    echo -e "  ${YELLOW}⚠ No SPR data available (offline or pre-election)${NC}"
fi

echo ""
echo -e "${YELLOW}[2] Checking Tier 1 (Established Media)${NC}"
echo "-----------------------------------"

if [ -f "$MKINI_FILE" ]; then
    echo "  Source: Malaysiakini"
    if grep -qi "$SEARCH_TERM" "$MKINI_FILE" 2>/dev/null; then
        VALUE=$(grep -i "$SEARCH_TERM" "$MKINI_FILE" | head -1)
        echo "  Value: $VALUE"
        SOURCE_VALUES["MKINI"]="$VALUE"
        SOURCE_TIERS["MKINI"]=1
        echo -e "  ${GREEN}✓ Found${NC}"
    else
        echo -e "  ${YELLOW}⚠ Not found in latest Malaysiakini feed${NC}"
    fi
else
    echo -e "  ${YELLOW}⚠ No Malaysiakini data available${NC}"
fi

# Add more Tier 1 sources as fetch scripts are implemented
# The Star, NST, FMT, Bernama

echo ""
echo -e "${YELLOW}[3] Computing Confidence Assertion${NC}"
echo "-----------------------------------"

# Count sources
SOURCE_COUNT=${#SOURCE_VALUES[@]}
echo "  Sources found: $SOURCE_COUNT"

if [ $SOURCE_COUNT -eq 0 ]; then
    echo -e "  ${RED}✗ No sources found${NC}"
    ASSERTION="[UNVERIFIED]"
elif [ $SOURCE_COUNT -eq 1 ]; then
    echo -e "  ${YELLOW}⚠ Single source${NC}"
    ASSERTION="[SINGLE-SOURCE]"
else
    # Check convergence (simplified: exact match)
    VALUES=($(printf "%s\n" "${SOURCE_VALUES[@]}" | sort -u))
    UNIQUE_COUNT=${#VALUES[@]}
    
    if [ $UNIQUE_COUNT -eq 1 ]; then
        echo -e "  ${GREEN}✓ All sources converged${NC}"
        ASSERTION="[VERIFIED]"
        CONVERGED=1
    else
        echo -e "  ${RED}✗ Sources conflict (${UNIQUE_COUNT} different values)${NC}"
        ASSERTION="[CONFLICTING]"
        CONFLICTING=1
        
        echo ""
        echo "  Conflicting values:"
        for val in "${VALUES[@]}"; do
            echo "    - $val"
        done
    fi
fi

# Determine highest tier
MAX_TIER=9
for source in "${!SOURCE_TIERS[@]}"; do
    tier=${SOURCE_TIERS[$source]}
    if [ $tier -lt $MAX_TIER ]; then
        MAX_TIER=$tier
    fi
done

echo ""
echo -e "${BLUE}=== Confidence Assertion ===${NC}"
echo "  Assertion: $ASSERTION"
echo "  Highest Tier: $MAX_TIER"
echo "  Source Count: $SOURCE_COUNT"
[ $CONVERGED -eq 1 ] && echo "  Status: Converged"
[ $CONFLICTING -eq 1 ] && echo -e "  ${RED}Status: Conflicting - Human review required${NC}"

echo ""
echo "=== End of Cross-Reference ==="

# Exit code: 0 = verified/corroborated, 1 = conflicting/unverified
if [ $CONFLICTING -eq 1 ] || [ $SOURCE_COUNT -eq 0 ]; then
    exit 1
fi
exit 0
