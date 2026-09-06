#!/bin/bash
# SOP-AV-001: Apply overdue status to non-terminal actions with passed deadlines
# Generated: 2026-09-06T17:00:00+00:00

cd /home/p62operator/.openclaw/workspace/strategic-cognitiveos

# Terminal states that should NOT be changed to overdue
# (completed, closed, de-scoped, archived, resolved)

# List of ACT-IDs with passed deadlines in non-terminal states
# Format: ACT-ID|filename
ACTIONS=(
  "ACT-20260807-002|ACT-20260807-002.md"
  "ACT-20260808-008|ACT-20260808-008.md"
  "ACT-20260810-002|ACT-20260810-002.md"
  "ACT-20260810-003|ACT-20260810-003.md"
  "ACT-20260810-004|ACT-20260810-004.md"
  "ACT-20260810-005|ACT-20260810-005.md"
  "ACT-20260810-006|ACT-20260810-006.md"
  "ACT-20260811-002|ACT-20260811-002.md"
  "ACT-20260811-003|ACT-20260811-003.md"
  "ACT-20260811-006|ACT-20260811-006.md"
  "ACT-20260811-008|ACT-20260811-008.md"
  "ACT-20260811-009|ACT-20260811-009.md"
  "ACT-20260811-010|ACT-20260811-010.md"
  "ACT-20260811-011|ACT-20260811-011.md"
  "ACT-20260811-012|ACT-20260811-012.md"
  "ACT-20260811-013|ACT-20260811-013.md"
  "ACT-20260813-005|ACT-20260813-005.md"
  "ACT-20260813-007|ACT-20260813-007.md"
  "ACT-20260813-009|ACT-20260813-009.md"
  "ACT-20260813-011|ACT-20260813-011.md"
  "ACT-20260815-002|ACT-20260815-002.md"
  "ACT-20260815-008|ACT-20260815-008.md"
  "ACT-20260815-013|ACT-20260815-013.md"
  "ACT-20260817-002|ACT-20260817-002.md"
  "ACT-20260817-003|ACT-20260817-003.md"
  "ACT-20260817-004|ACT-20260817-004.md"
  "ACT-20260818-003|ACT-20260818-003.md"
  "ACT-20260818-007|ACT-20260818-007.md"
  "ACT-20260819-010|ACT-20260819-010.md"
  "ACT-20260820-001|ACT-20260820-001.md"
  "ACT-20260821-001|ACT-20260821-001.md"
  "ACT-20260821-002|ACT-20260821-002.md"
  "ACT-20260821-003|ACT-20260821-003.md"
  "ACT-20260821-004|ACT-20260821-004.md"
  "ACT-20260821-006|ACT-20260821-006.md"
  "ACT-20260821-007|ACT-20260821-007.md"
  "ACT-20260821-008|ACT-20260821-008.md"
  "ACT-20260822-001|ACT-20260822-001.md"
  "ACT-20260822-002|ACT-20260822-002.md"
  "ACT-20260823-001|ACT-20260823-001.md"
  "ACT-20260823-002|ACT-20260823-002.md"
  "ACT-20260823-003|ACT-20260823-003.md"
  "ACT-20260823-004|ACT-20260823-004.md"
  "ACT-20260823-005|ACT-20260823-005.md"
  "ACT-20260824-006|ACT-20260824-006.md"
  "ACT-20260824-007|ACT-20260824-007.md"
  "ACT-20260825-003|ACT-20260825-003.md"
  "ACT-20260825-004|ACT-20260825-004.md"
  "ACT-20260825-005|ACT-20260825-005.md"
  "ACT-20260825-007|ACT-20260825-007.md"
  "ACT-20260825-009|ACT-20260825-009.md"
  "ACT-20260826-001|ACT-20260826-001.md"
  "ACT-20260826-002|ACT-20260826-002.md"
  "ACT-20260827-001|ACT-20260827-001.md"
  "ACT-20260827-002|ACT-20260827-002.md"
  "ACT-20260827-003|ACT-20260827-003.md"
  "ACT-20260827-004|ACT-20260827-004.md"
  "ACT-20260827-005|ACT-20260827-005.md"
  "ACT-20260827-006|ACT-20260827-006.md"
  "ACT-20260827-007|ACT-20260827-007.md"
  "ACT-20260827-008|ACT-20260827-008.md"
)

COUNT=0
for entry in "${ACTIONS[@]}"; do
  IFS='|' read -r act_id filename <<< "$entry"
  filepath="actions/$filename"
  
  # Find file if not exact name match
  if [ ! -f "$filepath" ]; then
    filepath=$(find actions/ -name "${act_id}*.md" 2>/dev/null | head -1)
    if [ -z "$filepath" ]; then
      echo "SKIP: $act_id — file not found"
      continue
    fi
  fi
  
  # Get current status
  current_status=$(grep -m1 "^status:" "$filepath" | awk '{print $2}')
  
  # Skip terminal states
  case "$current_status" in
    completed|closed|de-scoped|archived|resolved)
      echo "SKIP: $act_id — terminal state ($current_status)"
      continue
      ;;
  esac
  
  # Update status to overdue
  sed -i "s/^status: ${current_status}/status: overdue/" "$filepath"
  
  # Add validation note if field exists and is empty
  sed -i 's/^validation_note: ""/validation_note: "SOP-AV-001 2026-09-06: Status updated from '"${current_status}"' to overdue (deadline passed)"/' "$filepath"
  
  echo "UPDATED: $act_id — $current_status → overdue"
  ((COUNT++))
done

echo ""
echo "Total updated: $COUNT"
