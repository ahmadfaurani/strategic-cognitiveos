#!/bin/bash
# Dreaming CVS Integration
# Runs Core Truth Validation System on Dreaming REM phase candidates before Deep Sleep promotion
# 
# Usage: ./dreaming-cvs-integration.sh [date]
#   date: YYYY-MM-DD format (defaults to today)
#
# Integration Point: Call this script from memory-core dreaming pipeline
#   after REM phase completes, before Deep Sleep promotion

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE="/home/p62operator/.openclaw/workspace"
DREAMS_DIR="$WORKSPACE/memory/dreaming"
VALIDATION_LOG="$WORKSPACE/memory/dreaming-validation.jsonl"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

# Date handling
DATE="${1:-$(date -u +%Y-%m-%d)}"
REM_FILE="$DREAMS_DIR/rem/${DATE}.md"

usage() {
    echo "Dreaming CVS Integration - Truth Validation for REM Phase Candidates"
    echo ""
    echo "Usage: $0 [YYYY-MM-DD]"
    echo ""
    echo "Validates all REM phase candidates before Deep Sleep promotion"
    echo "Output: $VALIDATION_LOG"
    echo ""
    echo "Options:"
    echo "  --dry-run    Preview validation without writing results"
    echo "  --verbose    Show detailed validation output"
    echo "  --help       Show this help"
    exit 0
}

# Parse arguments
DRY_RUN=false
VERBOSE=false

for arg in "$@"; do
    case $arg in
        --dry-run)
            DRY_RUN=true
            shift
            ;;
        --verbose)
            VERBOSE=true
            shift
            ;;
        --help)
            usage
            ;;
        *)
            DATE="$arg"
            shift
            ;;
    esac
done

REM_FILE="$DREAMS_DIR/rem/${DATE}.md"

echo -e "${BLUE}=== Dreaming CVS Validation Gate ===${NC}"
echo "Date: $DATE"
echo "REM File: $REM_FILE"
echo "Validation Log: $VALIDATION_LOG"
echo ""

# Check if REM file exists
if [ ! -f "$REM_FILE" ]; then
    echo -e "${YELLOW}⚠ REM file not found: $REM_FILE${NC}"
    echo "Dreaming may not have run yet, or date is incorrect."
    echo "Available REM files:"
    ls -1 "$DREAMS_DIR/rem/"*.md 2>/dev/null | tail -5 || echo "  (none found)"
    exit 1
fi

echo -e "${GREEN}✓ REM file found${NC}"
echo ""

# Count candidates in REM file
CANDIDATE_COUNT=$(grep -c "^- Candidate:" "$REM_FILE" 2>/dev/null || echo "0")
echo "Candidates to validate: $CANDIDATE_COUNT"
echo ""

if [ "$CANDIDATE_COUNT" -eq 0 ]; then
    echo -e "${YELLOW}No candidates found in REM file. Skipping validation.${NC}"
    exit 0
fi

# Initialize validation log
if [ "$DRY_RUN" = false ]; then
    echo "[]" > "$VALIDATION_LOG"
fi

# Validation counters
PASSED=0
FAILED=0
WARNINGS=0

echo -e "${BLUE}Running CVS validation on each candidate...${NC}"
echo ""

# Extract and validate each candidate (supports both formats)
# Format 1: "- Candidate: ..." (staged candidates)
# Format 2: "- - **..." (grounded reflections from DREAMS.md)
grep -E "^- (Candidate:|\- \*\*)" "$REM_FILE" | while IFS= read -r line; do
    # Extract candidate snippet (first 200 chars for validation)
    SNIPPET=$(echo "$line" | sed 's/^- Candidate: //' | sed 's/^- //' | cut -c1-200)
    
    # Generate candidate ID
    CANDIDATE_ID=$(echo "$SNIPPET" | md5sum | cut -c1-8)
    
    # Validation checks
    VALIDATION_STATUS="PASSED"
    ISSUES=""
    
    # Check 1: Does snippet contain numerical claims without citations?
    if echo "$SNIPPET" | grep -qE '[0-9]+(%|votes|majority|turnout|seats)'; then
        if ! echo "$SNIPPET" | grep -qE 'Source:|evidence:'; then
            VALIDATION_STATUS="FAILED"
            ISSUES="numerical_claim_without_citation"
        fi
    fi
    
    # Check 2: Does snippet contain named entities (candidates, positions)?
    if echo "$SNIPPET" | grep -qE '(won|defeated|candidate|ADUN|minister|party)'; then
        if ! echo "$SNIPPET" | grep -qE 'evidence:|Source:'; then
            if [ "$VALIDATION_STATUS" = "PASSED" ]; then
                VALIDATION_STATUS="WARNING"
                ISSUES="named_entity_without_source"
            fi
        fi
    fi
    
    # Check 3: Does snippet contain confidence tags?
    if echo "$SNIPPET" | grep -qE '\[HIGH\]|\[MEDIUM\]|\[LOW\]'; then
        : # Good, has confidence tag
    else
        if [ "$VALIDATION_STATUS" = "PASSED" ]; then
            VALIDATION_STATUS="WARNING"
            ISSUES="${ISSUES:+$ISSUES,}missing_confidence_tag"
        fi
    fi
    
    # Check 4: Does snippet contain speculation without flag?
    if echo "$SNIPPET" | grep -qiE '(will|could|might|likely|expected|projected)'; then
        if ! echo "$SNIPPET" | grep -qiE 'SPECULATION:|SCENARIO:|inference|projection'; then
            if [ "$VALIDATION_STATUS" = "PASSED" ]; then
                VALIDATION_STATUS="WARNING"
                ISSUES="${ISSUES:+$ISSUES,}speculation_without_flag"
            fi
        fi
    fi
    
    # Output result
    if [ "$VERBOSE" = true ]; then
        echo "Candidate: $CANDIDATE_ID"
        echo "  Status: $VALIDATION_STATUS"
        echo "  Issues: ${ISSUES:-none}"
        echo "  Snippet: $SNIPPET..."
        echo ""
    fi
    
    # Update counters
    case $VALIDATION_STATUS in
        PASSED)
            PASSED=$((PASSED + 1))
            ;;
        FAILED)
            FAILED=$((FAILED + 1))
            ;;
        WARNING)
            WARNINGS=$((WARNINGS + 1))
            PASSED=$((PASSED + 1))  # Count warnings as passed with notes
            ;;
    esac
    
    # Write to validation log (JSONL format)
    if [ "$DRY_RUN" = false ]; then
        TIMESTAMP=$(date -u +%Y-%m-%dT%H:%M:%SZ)
        echo "{\"candidate_id\":\"$CANDIDATE_ID\",\"date\":\"$DATE\",\"status\":\"$VALIDATION_STATUS\",\"issues\":\"$ISSUES\",\"timestamp\":\"$TIMESTAMP\"}" >> "$VALIDATION_LOG"
    fi
done

echo ""
echo -e "${BLUE}=== Validation Summary ===${NC}"
echo -e "Passed: ${GREEN}$PASSED${NC}"
echo -e "Failed: ${RED}$FAILED${NC}"
echo -e "Warnings: ${YELLOW}$WARNINGS${NC}"
echo ""

# Final gate decision
if [ "$FAILED" -gt 0 ]; then
    echo -e "${RED}❌ CVS VALIDATION GATE: BLOCKED${NC}"
    echo ""
    echo "$FAILED candidate(s) failed validation. Deep Sleep promotion should be blocked."
    echo "Review $VALIDATION_LOG for details."
    echo ""
    echo "Recommended action:"
    echo "  1. Review failed candidates in $REM_FILE"
    echo "  2. Add missing citations or confidence tags"
    echo "  3. Re-run validation or manually promote with --override"
    exit 1
else
    echo -e "${GREEN}✅ CVS VALIDATION GATE: PASSED${NC}"
    echo ""
    echo "All candidates passed CVS validation (with $WARNINGS warnings)."
    echo "Safe to proceed with Deep Sleep promotion."
    echo ""
    if [ "$DRY_RUN" = false ]; then
        echo "Validation log written to: $VALIDATION_LOG"
    fi
    exit 0
fi
