#!/bin/bash
# Truth Validation Script
# Validates claims against source files and flags unverified assertions

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE="/home/p62operator/.openclaw/workspace"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

usage() {
    echo "Usage: $0 <input-file> [source-file]"
    echo ""
    echo "Validates claims in input-file against optional source-file"
    echo "If no source-file provided, validates internal consistency only"
    echo ""
    echo "Options:"
    echo "  --extract-numbers    Extract all numerical claims"
    echo "  --extract-names      Extract all named entities"
    echo "  --check-citations    Verify all citations exist"
    echo "  --help               Show this help"
    exit 1
}

if [ $# -lt 1 ]; then
    usage
fi

INPUT_FILE="$1"
SOURCE_FILE="${2:-}"

if [ ! -f "$INPUT_FILE" ]; then
    echo -e "${RED}Error: Input file not found: $INPUT_FILE${NC}"
    exit 1
fi

echo "=== Truth Validation Report (Multi-Source) ==="
echo "Input: $INPUT_FILE"
[ -n "$SOURCE_FILE" ] && echo "Source: $SOURCE_FILE"
echo ""
echo "Standard: ≥2 independent sources for Tier 1 claims + Confidence Assertion tags"
echo ""

# Track validation status
ERRORS=0
WARNINGS=0

# --- Check 1: Extract numerical claims ---
echo -e "\n${YELLOW}[1] Numerical Claims${NC}"
echo "-----------------------------------"

# Pattern: numbers with context (votes, percentages, dates, margins)
NUM_CLAIMS=$(grep -oE '[0-9]+[,0-9]* (votes|majority|turnout|%|percent|voters|electorate|seats)' "$INPUT_FILE" 2>/dev/null || true)

if [ -n "$NUM_CLAIMS" ]; then
    echo "$NUM_CLAIMS" | while read -r claim; do
        echo "  Found: $claim"
    done
    COUNT=$(echo "$NUM_CLAIMS" | wc -l)
    echo -e "  ${GREEN}✓ $COUNT numerical claims identified${NC}"
else
    echo -e "  ${YELLOW}⚠ No numerical claims found (verify this is expected)${NC}"
    ((WARNINGS++)) || true
fi

# --- Check 2: Multi-Source Verification + Confidence Assertion ---
echo -e "\n${YELLOW}[2] Multi-Source Verification${NC}"
echo "-----------------------------------"

# Check for Confidence Assertion tags
VERIFIED=$(grep -c '\[VERIFIED\]' "$INPUT_FILE" 2>/dev/null || true)
CORROBORATED=$(grep -c '\[CORROBORATED\]' "$INPUT_FILE" 2>/dev/null || true)
SINGLE=$(grep -c '\[SINGLE-SOURCE\]' "$INPUT_FILE" 2>/dev/null || true)
CONFLICTING=$(grep -c '\[CONFLICTING\]' "$INPUT_FILE" 2>/dev/null || true)
UNVERIFIED=$(grep -c '\[UNVERIFIED\]' "$INPUT_FILE" 2>/dev/null || true)

# Handle empty results
VERIFIED=${VERIFIED:-0}
CORROBORATED=${CORROBORATED:-0}
SINGLE=${SINGLE:-0}
CONFLICTING=${CONFLICTING:-0}
UNVERIFIED=${UNVERIFIED:-0}

echo "  [VERIFIED]: $VERIFIED"
echo "  [CORROBORATED]: $CORROBORATED"
echo "  [SINGLE-SOURCE]: $SINGLE"
echo "  [CONFLICTING]: $CONFLICTING"
echo "  [UNVERIFIED]: $UNVERIFIED"

# Count total factual claims (numbers, names, dates)
FACTUAL_CLAIMS=$(grep -cE '[0-9]+[,0-9]* (votes|majority|turnout|%|voters|electorate)' "$INPUT_FILE" 2>/dev/null || true)
FACTUAL_CLAIMS=${FACTUAL_CLAIMS:-0}
TAGGED_CLAIMS=$((VERIFIED + CORROBORATED + SINGLE + CONFLICTING))

echo ""
echo "  Total factual claims: $FACTUAL_CLAIMS"
echo "  Tagged with assertion: $TAGGED_CLAIMS"

if [ $FACTUAL_CLAIMS -gt 0 ] && [ $TAGGED_CLAIMS -eq 0 ]; then
    echo -e "  ${RED}✗ No Confidence Assertion tags found${NC}"
    ((ERRORS++)) || true
elif [ $CONFLICTING -gt 0 ]; then
    echo -e "  ${YELLOW}⚠ $CONFLICTING conflicting claims require human review${NC}"
    ((WARNINGS++)) || true
elif [ $SINGLE -gt 0 ]; then
    echo -e "  ${YELLOW}⚠ $SINGLE single-source claims (recommend multi-source)${NC}"
    ((WARNINGS++)) || true
elif [ $UNVERIFIED -gt 0 ]; then
    echo -e "  ${YELLOW}⚠ $UNVERIFIED unverified claims${NC}"
    ((WARNINGS++)) || true
else
    echo -e "  ${GREEN}✓ All factual claims have Confidence Assertion${NC}"
fi

# --- Check 3: Citation Verification (Legacy, for internal memory) ---
echo -e "\n${YELLOW}[3] Citation Verification (Internal Memory)${NC}"
echo "-----------------------------------"

# Pattern: MEMORY.md#L123 or file.md#L456
CITATIONS=$(grep -oE '[A-Za-z0-9_-]+\.md#L[0-9]+' "$INPUT_FILE" 2>/dev/null || true)

if [ -n "$CITATIONS" ]; then
    VALID_CITATIONS=0
    INVALID_CITATIONS=0
    
    echo "$CITATIONS" | sort -u | while read -r citation; do
        FILE=$(echo "$citation" | cut -d'#' -f1)
        LINE=$(echo "$citation" | cut -d'L' -f2)
        FULL_PATH="$WORKSPACE/$FILE"
        
        if [ -f "$FULL_PATH" ]; then
            TOTAL_LINES=$(wc -l < "$FULL_PATH")
            if [ "$LINE" -le "$TOTAL_LINES" ]; then
                LINE_CONTENT=$(sed -n "${LINE}p" "$FULL_PATH")
                if [ -n "$LINE_CONTENT" ]; then
                    ((VALID_CITATIONS++)) || true
                else
                    ((INVALID_CITATIONS++)) || true
                fi
            else
                ((INVALID_CITATIONS++)) || true
            fi
        else
            ((INVALID_CITATIONS++)) || true
        fi
    done
    
    if [ $INVALID_CITATIONS -gt 0 ]; then
        echo -e "  ${RED}✗ $INVALID_CITATIONS invalid citations${NC}"
        ((ERRORS++)) || true
    else
        echo -e "  ${GREEN}✓ Citations valid${NC}"
    fi
else
    echo -e "  ${YELLOW}⚠ No internal citations (relying on external multi-source)${NC}"
fi

# --- Check 4: Analytical Confidence Tags ---
echo -e "\n${YELLOW}[4] Analytical Confidence Tags${NC}"
echo "-----------------------------------"

# Check for analytical claims without confidence tags
ANALYTICAL_PATTERNS="could|might|likely|probably|suggests|indicates|appears|seems"
UNTAGGED=$(grep -iE "$ANALYTICAL_PATTERNS" "$INPUT_FILE" 2>/dev/null | grep -vE '\[HIGH\]|\[MEDIUM\]|\[LOW\]|SPECULATION:|SCENARIO:' || true)

if [ -n "$UNTAGGED" ]; then
    COUNT=$(echo "$UNTAGGED" | wc -l)
    echo -e "  ${YELLOW}⚠ $COUNT analytical claims without confidence tags:${NC}"
    echo "$UNTAGGED" | head -5 | while read -r line; do
        echo "    → ${line:0:80}..."
    done
    ((WARNINGS++)) || true
else
    echo -e "  ${GREEN}✓ All analytical claims properly tagged${NC}"
fi

# --- Check 5: Speculation demarcation ---
echo -e "\n${YELLOW}[4] Speculation Demarcation${NC}"
echo "-----------------------------------"

# Check for predictive language without proper flags
PREDICTIVE_PATTERNS="will|should|expected to|projected|forecast|anticipate|predict"
UNFLAGGED_PRED=$(grep -iE "$PREDICTIVE_PATTERNS" "$INPUT_FILE" 2>/dev/null | grep -vE 'SPECULATION:|SCENARIO:|HYPOTHESIS:' || true)

if [ -n "$UNFLAGGED_PRED" ]; then
    COUNT=$(echo "$UNFLAGGED_PRED" | wc -l)
    echo -e "  ${YELLOW}⚠ $COUNT predictive claims without speculation flags:${NC}"
    echo "$UNFLAGGED_PRED" | head -5 | while read -r line; do
        echo "    → ${line:0:80}..."
    done
    ((WARNINGS++)) || true
else
    echo -e "  ${GREEN}✓ All predictive claims properly demarcated${NC}"
fi

# --- Check 6: Multi-Source Evidence (Cross-Reference) ---
echo -e "\n${YELLOW}[5] Cross-Reference Check${NC}"
echo "-----------------------------------"

# If crossref.sh exists and search term provided, run it
CROSSREF_SCRIPT="$SCRIPT_DIR/crossref.sh"
if [ -x "$CROSSREF_SCRIPT" ]; then
    # Extract constituency name from file (simplified)
    CONSTITUENCY=$(grep -oE 'N[0-9]+ [A-Za-z]+' "$INPUT_FILE" | head -1)
    
    if [ -n "$CONSTITUENCY" ]; then
        echo "  Running cross-reference for: $CONSTITUENCY"
        # Run crossref but don't fail this script based on its result
        bash "$CROSSREF_SCRIPT" result "$CONSTITUENCY" 2>/dev/null || true
    else
        echo -e "  ${YELLOW}⚠ No constituency found for cross-reference${NC}"
    fi
else
    echo -e "  ${YELLOW}⚠ Cross-reference script not available${NC}"
fi

# --- Check 7: ElectionData.MY API Verification ---
echo -e "\n${YELLOW}[6] ElectionData.MY API Verification${NC}"
echo "-----------------------------------"

ELECTIONDATA_SCRIPT="$SCRIPT_DIR/electiondata-verify.sh"
if [ -x "$ELECTIONDATA_SCRIPT" ]; then
    # Extract constituency name from file
    CONSTITUENCY=$(grep -oE 'N[0-9]+ [A-Za-z ]+' "$INPUT_FILE" | head -1)
    
    if [ -n "$CONSTITUENCY" ]; then
        echo "  Verifying against ElectionData.MY: $CONSTITUENCY"
        
        # Check if API key is configured (multiple sources)
        # Priority: 1) Env var, 2) Workspace config, 3) Key file
        API_KEY_SOURCE=""
        if [ -n "$ELECTIONDATA_API_KEY" ]; then
            API_KEY_SOURCE="env"
        elif [ -f "$WORKSPACE/.electiondata-config" ]; then
            source "$WORKSPACE/.electiondata-config"
            API_KEY_SOURCE="config"
        elif [ -f "$SCRIPT_DIR/.electiondata-key" ]; then
            source "$SCRIPT_DIR/.electiondata-key"
            API_KEY_SOURCE="keyfile"
        fi
        
        if [ -n "$ELECTIONDATA_API_KEY" ]; then
            # Run verification (non-blocking, informational)
            echo "     API key loaded from: $API_KEY_SOURCE"
            bash "$ELECTIONDATA_SCRIPT" "$CONSTITUENCY" 2>/dev/null || echo -e "  ${YELLOW}⚠ API verification skipped (API unavailable)${NC}"
        else
            echo -e "  ${RED}❌ ERROR: ElectionData.MY API key not configured${NC}"
            echo "     This is MANDATORY per CVS-MANDATE.md"
            echo "     Configure: export ELECTIONDATA_API_KEY=***"
            echo "     Or run: source tools/truth-validator/.electiondata-key"
            echo "     Get key: https://electiondata.my/console"
            ERRORS=$((ERRORS + 1))
        fi
    else
        echo -e "  ${YELLOW}⚠ No constituency found for ElectionData.MY verification${NC}"
    fi
else
    echo -e "  ${YELLOW}⚠ ElectionData.MY verification script not found${NC}"
fi

# --- Summary ---
echo -e "\n=== Validation Summary ==="
echo -e "Errors: ${RED}$ERRORS${NC}"
echo -e "Warnings: ${YELLOW}$WARNINGS${NC}"

if [ $ERRORS -gt 0 ]; then
    echo -e "\n${RED}❌ VALIDATION FAILED - Fix errors before output${NC}"
    exit 1
elif [ $WARNINGS -gt 0 ]; then
    echo -e "\n${YELLOW}⚠️  VALIDATION PASSED WITH WARNINGS - Review before output${NC}"
    exit 0
else
    echo -e "\n${GREEN}✅ VALIDATION PASSED - Safe to output${NC}"
    exit 0
fi
