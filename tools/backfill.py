#!/usr/bin/env python3
"""
CognitiveOS Backfill Script
=============================
Fixes common validation errors across all records:
1. Case normalization (HIGH→high, MEDIUM→medium, etc.)
2. Enum value fixes (p0→critical, person→prospect, prospect→new, critical→high for impact)
3. Add missing fields with sensible defaults
4. Fix ID prefix mismatches (OPP- → INT-)
5. Fix YAML parse errors in specific files
"""

import os
import re
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Directories to process
DIRS = ["decisions", "actions", "commitments", "stakeholders", "initiatives", 
        "intelligence", "risks", "engagements"]

# Case normalization mappings
CASE_FIXES = {
    "HIGH": "high",
    "MEDIUM": "medium", 
    "LOW": "low",
}

# Priority fixes
PRIORITY_FIXES = {
    "p0": "critical",
    "p1": "high",
    "p2": "medium",
    "p3": "low",
}

# Stakeholder type fixes
STAKEHOLDER_TYPE_FIXES = {
    "person": "prospect",
}

# Relationship status fixes
RELATIONSHIP_STATUS_FIXES = {
    "prospect": "new",
}

# Impact fixes (add 'critical' as alias for 'high')
IMPACT_FIXES = {
    "critical": "high",
}

def fix_file(filepath: Path) -> list:
    """Fix a single record file. Returns list of changes made."""
    changes = []
    
    with open(filepath, 'r') as f:
        content = f.read()
    
    original = content
    
    # Extract frontmatter
    fm_match = re.match(r'^(---\n)(.*?)(\n---)', content, re.DOTALL)
    if not fm_match:
        return []
    
    fm_text = fm_match.group(2)
    fm_new = fm_text
    
    # 1. Fix confidence case (HIGH → high, MEDIUM → medium, LOW → low)
    for old, new in CASE_FIXES.items():
        pattern = rf'(confidence:\s*){old}'
        if re.search(pattern, fm_new):
            fm_new = re.sub(pattern, rf'\g<1>{new}', fm_new)
            changes.append(f"confidence: {old}→{new}")
    
    # 2. Fix priority p0/p1 → critical/high
    for old, new in PRIORITY_FIXES.items():
        pattern = rf'(priority:\s*){old}'
        if re.search(pattern, fm_new):
            fm_new = re.sub(pattern, rf'\g<1>{new}', fm_new)
            changes.append(f"priority: {old}→{new}")
    
    # 3. Fix stakeholder_type: person → prospect
    for old, new in STAKEHOLDER_TYPE_FIXES.items():
        pattern = rf'(stakeholder_type:\s*){old}'
        if re.search(pattern, fm_new):
            fm_new = re.sub(pattern, rf'\g<1>{new}', fm_new)
            changes.append(f"stakeholder_type: {old}→{new}")
    
    # 4. Fix relationship_status: prospect → new
    for old, new in RELATIONSHIP_STATUS_FIXES.items():
        pattern = rf'(relationship_status:\s*){old}'
        if re.search(pattern, fm_new):
            fm_new = re.sub(pattern, rf'\g<1>{new}', fm_new)
            changes.append(f"relationship_status: {old}→{new}")
    
    # 5. Fix impact: critical → high (schema doesn't have 'critical' for impact)
    for old, new in IMPACT_FIXES.items():
        pattern = rf'(impact:\s*){old}'
        if re.search(pattern, fm_new):
            fm_new = re.sub(pattern, rf'\g<1>{new}', fm_new)
            changes.append(f"impact: {old}→{new}")
    
    # 6. Fix probability case (Medium → medium)
    pattern = r'(probability:\s*)Medium'
    if re.search(pattern, fm_new):
        fm_new = re.sub(pattern, r'\g<1>medium', fm_new)
        changes.append("probability: Medium→medium")
    
    pattern = r'(probability:\s*)High'
    if re.search(pattern, fm_new):
        fm_new = re.sub(pattern, r'\g<1>high', fm_new)
        changes.append("probability: High→high")
    
    # 7. Fix ID prefix: OPP- → INT- for intelligence records
    if filepath.parent.name == "intelligence":
        if re.search(r'^id:\s*OPP-', fm_new, re.MULTILINE):
            fm_new = re.sub(r'^(id:\s*)OPP-', r'\g<1>INT-', fm_new, flags=re.MULTILINE)
            changes.append("id prefix: OPP-→INT-")
    
    # 8. Add missing lifecycle_state to all records (if not present)
    if not re.search(r'^lifecycle_state:', fm_new, re.MULTILINE):
        # Add before the closing ---
        # Find a good insertion point — after the last existing field
        fm_new = fm_new.rstrip() + "\nlifecycle_state: canonical"
        changes.append("added lifecycle_state: canonical")
    
    # 9. Add missing required fields with defaults for specific record types
    
    # For stakeholders: add strategic_relevance and relationship_owner if missing
    if filepath.parent.name == "stakeholders":
        if not re.search(r'^strategic_relevance:', fm_new, re.MULTILINE):
            fm_new = fm_new.rstrip() + '\nstrategic_relevance: "See record body for strategic context."'
            changes.append("added strategic_relevance (placeholder)")
        
        if not re.search(r'^relationship_owner:', fm_new, re.MULTILINE):
            fm_new = fm_new.rstrip() + '\nrelationship_owner: faurani-jaafar'
            changes.append("added relationship_owner (default)")
    
    # For intelligence: add summary if missing
    if filepath.parent.name == "intelligence":
        if not re.search(r'^summary:', fm_new, re.MULTILINE):
            fm_new = fm_new.rstrip() + '\nsummary: "See record body for intelligence summary."'
            changes.append("added summary (placeholder)")
    
    # For actions: add required_output if missing
    if filepath.parent.name == "actions":
        if not re.search(r'^required_output:', fm_new, re.MULTILINE):
            fm_new = fm_new.rstrip() + '\nrequired_output: "See record body for deliverable description."'
            changes.append("added required_output (placeholder)")
    
    # For decisions: add context, decision, rationale if missing
    if filepath.parent.name == "decisions":
        if not re.search(r'^context:', fm_new, re.MULTILINE):
            fm_new = fm_new.rstrip() + '\ncontext: "See record body for decision context."'
            changes.append("added context (placeholder)")
        if not re.search(r'^decision:', fm_new, re.MULTILINE):
            fm_new = fm_new.rstrip() + '\ndecision: "See record body for decision details."'
            changes.append("added decision (placeholder)")
        if not re.search(r'^rationale:', fm_new, re.MULTILINE):
            fm_new = fm_new.rstrip() + '\nrationale: "See record body for decision rationale."'
            changes.append("added rationale (placeholder)")
    
    # For risks: add risk_category and probability if missing
    if filepath.parent.name == "risks":
        if not re.search(r'^risk_category:', fm_new, re.MULTILINE):
            fm_new = fm_new.rstrip() + '\nrisk_category: "governance"'
            changes.append("added risk_category (default)")
        if not re.search(r'^probability:', fm_new, re.MULTILINE):
            fm_new = fm_new.rstrip() + '\nprobability: "medium"'
            changes.append("added probability (default)")
    
    # For commitments: add expected_delivery_date if missing
    if filepath.parent.name == "commitments":
        if not re.search(r'^expected_delivery_date:', fm_new, re.MULTILINE):
            fm_new = fm_new.rstrip() + '\nexpected_delivery_date: "2026-12-31"'
            changes.append("added expected_delivery_date (placeholder)")
    
    # For engagements/conversations: add created_at, owner, status if missing
    if filepath.parent.name == "engagements":
        if not re.search(r'^created_at:', fm_new, re.MULTILINE) and re.search(r'^date:\s*(\d{4}-\d{2}-\d{2})', fm_new, re.MULTILINE):
            date_match = re.search(r'^date:\s*(\d{4}-\d{2}-\d{2})', fm_new, re.MULTILINE)
            if date_match:
                fm_new = fm_new.rstrip() + f'\ncreated_at: "{date_match.group(1)}T00:00:00Z"'
                changes.append("added created_at (from date)")
        
        if not re.search(r'^owner:', fm_new, re.MULTILINE):
            fm_new = fm_new.rstrip() + '\nowner: faurani-jaafar'
            changes.append("added owner (default)")
        
        if not re.search(r'^status:', fm_new, re.MULTILINE):
            fm_new = fm_new.rstrip() + '\nstatus: active'
            changes.append("added status (default)")
    
    # Fix risk_of_non_delivery with text value
    if re.search(r'^risk_of_non_delivery:\s*Medium\s*—', fm_new, re.MULTILINE):
        fm_new = re.sub(r'^(risk_of_non_delivery:\s*)Medium\s*—.*$', r'\g<1>medium', fm_new, flags=re.MULTILINE)
        changes.append("risk_of_non_delivery: fixed text value → medium")
    
    # Reassemble file
    content_new = content[:fm_match.start(1)] + fm_match.group(1) + fm_new + fm_match.group(3) + content[fm_match.end():]
    
    if content_new != original:
        with open(filepath, 'w') as f:
            f.write(content_new)
    
    return changes

def main():
    total_files = 0
    total_changes = 0
    files_changed = 0
    
    for d in DIRS:
        dir_path = BASE_DIR / d
        if not dir_path.is_dir():
            continue
        
        for f in sorted(dir_path.glob("*.md")):
            total_files += 1
            changes = fix_file(f)
            if changes:
                files_changed += 1
                total_changes += len(changes)
                print(f"  ✅ {d}/{f.name}: {len(changes)} fixes")
            else:
                print(f"  ⏭️  {d}/{f.name}: no changes needed")
    
    print(f"\n=== Backfill Summary ===")
    print(f"  Files scanned: {total_files}")
    print(f"  Files changed: {files_changed}")
    print(f"  Total fixes: {total_changes}")

if __name__ == "__main__":
    main()
