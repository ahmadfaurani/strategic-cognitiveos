#!/bin/bash
###############################################################################
# SOP-AV-001 Phase 2: Action Register Validation Script
# 
# Validates all ACT- records against 13 evidence sources using 15 rules.
# Deterministic rules (V1-V4, V7, V8, V13, V14, V15) are automated here.
# Semantic rules (V5, V6, V9-V12) require AI review of the flagged output.
#
# Usage: ./validate-actions.sh [--json] [--summary]
# Output: Structured flag report to stdout (or JSON with --json)
###############################################################################
set -euo pipefail

REPO_DIR="/home/p62operator/.openclaw/workspace/strategic-cognitiveos"
ACTIONS_DIR="$REPO_DIR/actions"
DECISIONS_DIR="$REPO_DIR/decisions"
DOCUMENTS_DIR="$REPO_DIR/documents"
COMMITMENTS_DIR="$REPO_DIR/commitments"
OUTCOMES_DIR="$REPO_DIR/outcomes"
RISKS_DIR="$REPO_DIR/risks"
INITIATIVES_DIR="$REPO_DIR/initiatives"
ENGAGEMENTS_DIR="$REPO_DIR/engagements"
MEMORY_FILE="$REPO_DIR/../MEMORY.md"
DAILY_MEMORY_DIR="$REPO_DIR/../memory"

OUTPUT_JSON=false
SUMMARY_ONLY=false

while [[ $# -gt 0 ]]; do
    case "$1" in
        --json) OUTPUT_JSON=true; shift ;;
        --summary) SUMMARY_ONLY=true; shift ;;
        *) echo "Unknown option: $1" >&2; exit 1 ;;
    esac
done

cd "$REPO_DIR" || { echo "ERROR: Cannot cd to $REPO_DIR" >&2; exit 1; }

# --- Helper functions ---

extract_frontmatter_field() {
    local file="$1"
    local field="$2"
    python3 -c "
import sys, re
try:
    with open('$file', 'r') as f:
        content = f.read()
    # Extract YAML frontmatter
    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not match:
        sys.exit(0)
    fm = match.group(1)
    # Find field (handle both 'field: value' and 'field: \"value\"')
    for line in fm.split('\n'):
        if line.startswith('$field:'):
            val = line.split(':', 1)[1].strip().strip('\"').strip(\"'\")
            print(val)
            break
except:
    pass
" 2>/dev/null
}

get_all_actions() {
    find "$ACTIONS_DIR" -name "*.md" -type f 2>/dev/null | sort
}

get_all_records() {
    local dir="$1"
    find "$dir" -name "*.md" -type f 2>/dev/null | sort
}

# Count records per status
count_status() {
    local status="$1"
    local count=0
    for f in $(get_all_actions); do
        s=$(extract_frontmatter_field "$f" "status")
        if [[ "$s" == "$status" ]]; then
            count=$((count + 1))
        fi
    done
    echo "$count"
}

# --- Flag collection ---
FLAGS_FILE=$(mktemp)
trap "rm -f $FLAGS_FILE" EXIT

# --- V1: Decision Supersession Rule ---
# For each ACT- in draft/active, check if a DEC- resolves it
validate_v1() {
    local decisions=$(get_all_records "$DECISIONS_DIR")
    [[ -z "$decisions" ]] && return
    
    for act_file in $(get_all_actions); do
        local act_id=$(extract_frontmatter_field "$act_file" "id")
        local act_status=$(extract_frontmatter_field "$act_file" "status")
        local act_title=$(extract_frontmatter_field "$act_file" "title")
        
        # Only check draft/active/in-progress
        [[ "$act_status" != "draft" && "$act_status" != "active" && "$act_status" != "in-progress" ]] && continue
        [[ -z "$act_title" ]] && continue
        
        # Extract keywords from title (lowercase, split on common separators)
        local keywords=$(echo "$act_title" | tr '[:upper:]' '[:lower:]' | tr ' ;,/-' '\n' | grep -v '^$' | grep -v '^the$' | grep -v '^a$' | grep -v '^an$' | grep -v '^for$' | grep -v '^of$' | grep -v '^to$' | grep -v '^and$' | head -10)
        
        for dec_file in $decisions; do
            local dec_id=$(extract_frontmatter_field "$dec_file" "id")
            local dec_title=$(extract_frontmatter_field "$dec_file" "title")
            [[ -z "$dec_title" ]] && continue
            
            local dec_lower=$(echo "$dec_title" | tr '[:upper:]' '[:lower:]')
            
            # Check for keyword overlap
            local match_count=0
            for kw in $keywords; do
                if [[ ${#kw} -ge 4 ]] && echo "$dec_lower" | grep -qi "$kw"; then
                    match_count=$((match_count + 1))
                fi
            done
            
            # If ≥3 keywords match, flag as potential supersession
            if [[ $match_count -ge 3 ]]; then
                echo "V1|S1-CRITICAL|$act_id|$act_status|Potential decision supersession: $dec_id ($dec_title) matches $match_count keywords from ACT title" >> "$FLAGS_FILE"
            fi
        done
    done
}

# --- V2: Document Fulfilment Rule ---
validate_v2() {
    local docs=$(get_all_records "$DOCUMENTS_DIR")
    [[ -z "$docs" ]] && return
    
    for act_file in $(get_all_actions); do
        local act_id=$(extract_frontmatter_field "$act_file" "id")
        local act_status=$(extract_frontmatter_field "$act_file" "status")
        local act_output=$(extract_frontmatter_field "$act_file" "required_output")
        
        [[ "$act_status" != "draft" && "$act_status" != "active" && "$act_status" != "in-progress" ]] && continue
        [[ -z "$act_output" ]] && continue
        
        local output_lower=$(echo "$act_output" | tr '[:upper:]' '[:lower:]')
        
        for doc_file in $docs; do
            local doc_id=$(extract_frontmatter_field "$doc_file" "id")
            local doc_title=$(extract_frontmatter_field "$doc_file" "title")
            [[ -z "$doc_title" ]] && continue
            
            local doc_lower=$(echo "$doc_title" | tr '[:upper:]' '[:lower:]')
            
            # Check if doc title keywords appear in required_output
            local match_count=0
            for word in $(echo "$doc_lower" | tr ' ;,/-' '\n' | grep -v '^$' | grep -v '^the$' | grep -v '^a$' | grep -v '^an$' | head -8); do
                if [[ ${#word} -ge 4 ]] && echo "$output_lower" | grep -qi "$word"; then
                    match_count=$((match_count + 1))
                fi
            done
            
            if [[ $match_count -ge 3 ]]; then
                echo "V2|S1-CRITICAL|$act_id|$act_status|Potential document fulfilment: $doc_id ($doc_title) matches required_output" >> "$FLAGS_FILE"
            fi
        done
    done
}

# --- V3: Commitment Resolution Rule ---
validate_v3() {
    local coms=$(get_all_records "$COMMITMENTS_DIR")
    [[ -z "$coms" ]] && return
    
    for act_file in $(get_all_actions); do
        local act_id=$(extract_frontmatter_field "$act_file" "id")
        local act_status=$(extract_frontmatter_field "$act_file" "status")
        local act_title=$(extract_frontmatter_field "$act_file" "title")
        
        [[ "$act_status" != "draft" && "$act_status" != "active" && "$act_status" != "in-progress" ]] && continue
        [[ -z "$act_title" ]] && continue
        
        local title_lower=$(echo "$act_title" | tr '[:upper:]' '[:lower:]')
        
        for com_file in $coms; do
            local com_id=$(extract_frontmatter_field "$com_file" "id")
            local com_title=$(extract_frontmatter_field "$com_file" "title")
            [[ -z "$com_title" ]] && continue
            
            local com_lower=$(echo "$com_title" | tr '[:upper:]' '[:lower:]')
            
            local match_count=0
            for word in $(echo "$title_lower" | tr ' ;,/-' '\n' | grep -v '^$' | head -8); do
                if [[ ${#word} -ge 4 ]] && echo "$com_lower" | grep -qi "$word"; then
                    match_count=$((match_count + 1))
                fi
            done
            
            if [[ $match_count -ge 3 ]]; then
                echo "V3|S1-CRITICAL|$act_id|$act_status|Potential commitment resolution: $com_id ($com_title)" >> "$FLAGS_FILE"
            fi
        done
    done
}

# --- V4: Outcome Achievement Rule ---
validate_v4() {
    local outs=$(get_all_records "$OUTCOMES_DIR")
    [[ -z "$outs" ]] && return
    
    for act_file in $(get_all_actions); do
        local act_id=$(extract_frontmatter_field "$act_file" "id")
        local act_status=$(extract_frontmatter_field "$act_file" "status")
        local act_title=$(extract_frontmatter_field "$act_file" "title")
        
        [[ "$act_status" != "draft" && "$act_status" != "active" && "$act_status" != "in-progress" ]] && continue
        [[ -z "$act_title" ]] && continue
        
        local title_lower=$(echo "$act_title" | tr '[:upper:]' '[:lower:]')
        
        for out_file in $outs; do
            local out_id=$(extract_frontmatter_field "$out_file" "id")
            local out_title=$(extract_frontmatter_field "$out_file" "title")
            [[ -z "$out_title" ]] && continue
            
            local out_lower=$(echo "$out_title" | tr '[:upper:]' '[:lower:]')
            
            local match_count=0
            for word in $(echo "$title_lower" | tr ' ;,/-' '\n' | grep -v '^$' | head -8); do
                if [[ ${#word} -ge 4 ]] && echo "$out_lower" | grep -qi "$word"; then
                    match_count=$((match_count + 1))
                fi
            done
            
            if [[ $match_count -ge 3 ]]; then
                echo "V4|S1-CRITICAL|$act_id|$act_status|Potential outcome achievement: $out_id ($out_title)" >> "$FLAGS_FILE"
            fi
        done
    done
}

# --- V7: Risk Mitigation Rule ---
validate_v7() {
    local risks=$(get_all_records "$RISKS_DIR")
    [[ -z "$risks" ]] && return
    
    for act_file in $(get_all_actions); do
        local act_id=$(extract_frontmatter_field "$act_file" "id")
        local act_status=$(extract_frontmatter_field "$act_file" "status")
        local act_related=$(extract_frontmatter_field "$act_file" "related_records")
        
        [[ -z "$act_related" ]] && continue
        
        # Check if any related record is a RSK-
        if echo "$act_related" | grep -qi "RSK-"; then
            for rsk_file in $risks; do
                local rsk_id=$(extract_frontmatter_field "$rsk_file" "id")
                local rsk_status=$(extract_frontmatter_field "$rsk_file" "status")
                
                if echo "$act_related" | grep -qi "$rsk_id"; then
                    if [[ "$rsk_status" == "closed" || "$rsk_status" == "mitigating" ]]; then
                        if [[ "$act_status" == "draft" || "$act_status" == "active" || "$act_status" == "in-progress" ]]; then
                            echo "V7|S2-HIGH|$act_id|$act_status|Linked risk $rsk_id is $rsk_status but action still $act_status" >> "$FLAGS_FILE"
                        fi
                    fi
                fi
            done
        fi
    done
}

# --- V8: Initiative Status Implied Rule ---
validate_v8() {
    local inits=$(get_all_records "$INITIATIVES_DIR")
    [[ -z "$inits" ]] && return
    
    # Build initiative status map
    declare -A init_status_map
    for init_file in $inits; do
        local init_id=$(extract_frontmatter_field "$init_file" "id")
        local init_status=$(extract_frontmatter_field "$init_file" "status")
        [[ -n "$init_id" && -n "$init_status" ]] && init_status_map["$init_id"]="$init_status"
    done
    
    for act_file in $(get_all_actions); do
        local act_id=$(extract_frontmatter_field "$act_file" "id")
        local act_status=$(extract_frontmatter_field "$act_file" "status")
        local act_init=$(extract_frontmatter_field "$act_file" "related_initiative")
        
        [[ -z "$act_init" ]] && continue
        
        # Check if initiative exists in map
        for iid in "${!init_status_map[@]}"; do
            if echo "$act_init" | grep -qi "$iid"; then
                local i_status="${init_status_map[$iid]}"
                if [[ "$i_status" == "completed" || "$i_status" == "archived" || "$i_status" == "superseded" ]]; then
                    if [[ "$act_status" != "completed" && "$act_status" != "cancelled" && "$act_status" != "archived" ]]; then
                        echo "V8|S2-HIGH|$act_id|$act_status|Parent initiative $iid is $i_status but action still $act_status" >> "$FLAGS_FILE"
                    fi
                elif [[ "$i_status" == "blocked" || "$i_status" == "deferred" ]]; then
                    if [[ "$act_status" == "active" || "$act_status" == "in-progress" ]]; then
                        echo "V8|S3-MEDIUM|$act_id|$act_status|Parent initiative $iid is $i_status — action may need review" >> "$FLAGS_FILE"
                    fi
                fi
            fi
        done
    done
}

# --- V13: Deadline Staleness Rule ---
validate_v13() {
    local today=$(date -u +%Y-%m-%d)
    
    for act_file in $(get_all_actions); do
        local act_id=$(extract_frontmatter_field "$act_file" "id")
        local act_status=$(extract_frontmatter_field "$act_file" "status")
        local act_deadline=$(extract_frontmatter_field "$act_file" "deadline")
        
        [[ -z "$act_deadline" ]] && continue
        
        # Skip completed/cancelled/overdue
        [[ "$act_status" == "completed" || "$act_status" == "cancelled" || "$act_status" == "overdue" || "$act_status" == "archived" ]] && continue
        
        # Compare dates (YYYY-MM-DD comparison works lexicographically)
        if [[ "$act_deadline" < "$today" ]]; then
            echo "V13|S2-HIGH|$act_id|$act_status|Deadline $act_deadline has passed — status should be 'overdue' or 'blocked'" >> "$FLAGS_FILE"
        fi
    done
}

# --- V14: Orphan Action Rule ---
validate_v14() {
    for act_file in $(get_all_actions); do
        local act_id=$(extract_frontmatter_field "$act_file" "id")
        local act_status=$(extract_frontmatter_field "$act_file" "status")
        local act_related=$(extract_frontmatter_field "$act_file" "related_records")
        local act_init=$(extract_frontmatter_field "$act_file" "related_initiative")
        
        [[ "$act_status" == "completed" || "$act_status" == "cancelled" || "$act_status" == "archived" ]] && continue
        
        # Check if action has no related records and no related initiative
        if [[ -z "$act_related" || "$act_related" == "[]" || "$act_related" == "''" ]] && [[ -z "$act_init" || "$act_init" == "''" ]]; then
            echo "V14|S3-MEDIUM|$act_id|$act_status|Orphan action — no related_records and no related_initiative" >> "$FLAGS_FILE"
        fi
    done
}

# --- V15: Duplicate/Superseded Action Rule ---
validate_v15() {
    local act_files=($(get_all_actions))
    local i=0
    
    while [[ $i -lt ${#act_files[@]} ]]; do
        local act1_id=$(extract_frontmatter_field "${act_files[$i]}" "id")
        local act1_title=$(extract_frontmatter_field "${act_files[$i]}" "title")
        local act1_status=$(extract_frontmatter_field "${act_files[$i]}" "status")
        [[ -z "$act1_title" ]] && { i=$((i+1)); continue; }
        
        local j=$((i+1))
        while [[ $j -lt ${#act_files[@]} ]]; do
            local act2_id=$(extract_frontmatter_field "${act_files[$j]}" "id")
            local act2_title=$(extract_frontmatter_field "${act_files[$j]}" "title")
            local act2_status=$(extract_frontmatter_field "${act_files[$j]}" "status")
            [[ -z "$act2_title" ]] && { j=$((j+1)); continue; }
            
            # Compare titles — count matching keywords
            local t1_lower=$(echo "$act1_title" | tr '[:upper:]' '[:lower:]' | tr ' ;,/-' '\n' | grep -v '^$' | sort -u)
            local t2_lower=$(echo "$act2_title" | tr '[:upper:]' '[:lower:]' | tr ' ;,/-' '\n' | grep -v '^$' | sort -u)
            
            # Count common words
            local common=$(comm -12 <(echo "$t1_lower") <(echo "$t2_lower") | grep -c '.')
            local total=$(echo "$t1_lower" | wc -l)
            
            if [[ $total -gt 0 ]]; then
                local overlap=$((common * 100 / total))
                if [[ $overlap -ge 60 ]]; then
                    if [[ "$act1_status" != "superseded" && "$act2_status" != "superseded" && "$act1_status" != "cancelled" && "$act2_status" != "cancelled" ]]; then
                        echo "V15|S3-MEDIUM|$act1_id|$act1_status|Potential duplicate: $act2_id ($act2_title) — ${overlap}% title overlap" >> "$FLAGS_FILE"
                    fi
                fi
            fi
            
            j=$((j+1))
        done
        i=$((i+1))
    done
}

# --- Run all validations ---
echo "SOP-AV-001 VALIDATION REPORT — $(date -u +%Y-%m-%d)" >&2
echo "=========================================" >&2

total_actions=$(get_all_actions | wc -l)
echo "Actions scanned: $total_actions" >&2

# Count evidence sources
dec_count=$(get_all_records "$DECISIONS_DIR" | wc -l)
doc_count=$(get_all_records "$DOCUMENTS_DIR" | wc -l)
com_count=$(get_all_records "$COMMITMENTS_DIR" | wc -l)
out_count=$(get_all_records "$OUTCOMES_DIR" | wc -l)
rsk_count=$(get_all_records "$RISKS_DIR" | wc -l)
init_count=$(get_all_records "$INITIATIVES_DIR" | wc -l)
eng_count=$(get_all_records "$ENGAGEMENTS_DIR" | wc -l)

echo "Evidence sources: DEC-($dec_count), DOC-($doc_count), COM-($com_count), OUT-($out_count), RSK-($rsk_count), INIT-($init_count), ENG-($eng_count)" >&2

# Run validations
validate_v1
validate_v2
validate_v3
validate_v4
validate_v7
validate_v8
validate_v13
validate_v14
validate_v15

# --- Count flags by severity ---
s1_count=$(grep -c "S1-CRITICAL" "$FLAGS_FILE" 2>/dev/null || echo 0)
s2_count=$(grep -c "S2-HIGH" "$FLAGS_FILE" 2>/dev/null || echo 0)
s3_count=$(grep -c "S3-MEDIUM" "$FLAGS_FILE" 2>/dev/null || echo 0)
s4_count=0  # No S4 in deterministic rules
total_flags=$(wc -l < "$FLAGS_FILE" 2>/dev/null || echo 0)

echo "Flags raised: $total_flags" >&2
echo "  S1 CRITICAL:  $s1_count" >&2
echo "  S2 HIGH:      $s2_count" >&2
echo "  S3 MEDIUM:    $s3_count" >&2
echo "" >&2

# --- Output ---
if [[ "$SUMMARY_ONLY" == "true" ]]; then
    echo "Actions: $total_actions | Flags: $total_flags (S1:$s1_count S2:$s2_count S3:$s3_count)"
    exit 0
fi

if [[ "$OUTPUT_JSON" == "true" ]]; then
    echo "{"
    echo "  \"report_date\": \"$(date -u +%Y-%m-%d)\","
    echo "  \"actions_scanned\": $total_actions,"
    echo "  \"evidence_sources\": {"
    echo "    \"decisions\": $dec_count,"
    echo "    \"documents\": $doc_count,"
    echo "    \"commitments\": $com_count,"
    echo "    \"outcomes\": $out_count,"
    echo "    \"risks\": $rsk_count,"
    echo "    \"initiatives\": $init_count,"
    echo "    \"engagements\": $eng_count"
    echo "  },"
    echo "  \"flags\": {"
    echo "    \"total\": $total_flags,"
    echo "    \"s1_critical\": $s1_count,"
    echo "    \"s2_high\": $s2_count,"
    echo "    \"s3_medium\": $s3_count,"
    echo "    \"s4_low\": $s4_count"
    echo "  },"
    echo "  \"flag_details\": ["
    
    first=true
    while IFS= read -r line; do
        [[ -z "$line" ]] && continue
        IFS='|' read -r rule severity act_id act_status message <<< "$line"
        if [[ "$first" == "true" ]]; then
            first=false
        else
            echo ","
        fi
        echo "    {\"rule\": \"$rule\", \"severity\": \"$severity\", \"action_id\": \"$act_id\", \"current_status\": \"$act_status\", \"message\": \"$message\"}"
    done < "$FLAGS_FILE"
    
    echo ""
    echo "  ]"
    echo "}"
else
    # Human-readable output
    if [[ $total_flags -eq 0 ]]; then
        echo "No flags raised. Action register appears consistent with evidence sources."
    else
        echo "FLAGS:"
        echo "------"
        while IFS= read -r line; do
            [[ -z "$line" ]] && continue
            IFS='|' read -r rule severity act_id act_status message <<< "$line"
            echo "[$rule] [$severity] $act_id (status: $act_status)"
            echo "  → $message"
            echo ""
        done < "$FLAGS_FILE"
    fi
fi

# --- Status summary ---
echo ""
echo "STATUS SUMMARY:"
for status in draft in-progress active pending blocked completed overdue cancelled; do
    c=$(count_status "$status")
    [[ $c -gt 0 ]] && echo "  $status: $c"
done
