#!/usr/bin/env python3
"""
Retroactive Framework Tagging Script
Scans all CognitiveOS records and adds framework/domain/outcome/deadline tags
based on content analysis. Achieves universal queryability.

Usage: python3 retroactive-tagging.py [--dry-run]
"""

import os
import re
import sys
import glob
from pathlib import Path

REPO_DIR = "/home/p62operator/.openclaw/workspace/strategic-cognitiveos"
DRY_RUN = "--dry-run" in sys.argv

# Record directories to scan
RECORD_DIRS = [
    "actions", "decisions", "documents", "commitments", "outcomes",
    "risks", "initiatives", "intelligence", "stakeholders", "organizations",
    "engagements", "assessments", "briefings", "drafts", "artifacts",
    "opportunities", "lessons", "governance"
]

# --- Tagging Rules ---

def get_domain_tags(content_lower, fm):
    """Add domain tags based on content."""
    tags = set()
    if "cyberdsa" in content_lower:
        tags.add("domain/cyberdsa-2026")
    if "govsec" in content_lower and "tip" in content_lower:
        tags.add("domain/cybersecurity-productisation")
    if "voroncitadel" in content_lower or "voron-citadel" in content_lower:
        tags.add("domain/cybersecurity-productisation")
    if "chainsentry" in content_lower or "chain-sentry" in content_lower:
        tags.add("domain/cybersecurity-productisation")
    if "vorondrq" in content_lower or "voron-drq" in content_lower:
        tags.add("domain/cybersecurity-productisation")
    if "engineered success" in content_lower or "§9" in content_lower:
        tags.add("domain/governance")
    if "cognitive loop" in content_lower or "sop-cl-001" in content_lower:
        tags.add("domain/cognitiveos-operations")
    if "adep-001" in content_lower or "agentic diligence" in content_lower:
        tags.add("domain/development-governance")
    if "cvs" in content_lower and ("master framework" in content_lower or "evidence register" in content_lower or "claim" in content_lower):
        tags.add("domain/governance")
    if "intake" in content_lower and "sop" in content_lower:
        tags.add("domain/cognitiveos-operations")
    if "template discipline" in content_lower:
        tags.add("domain/cognitiveos-operations")
    if "sovereign ai" in content_lower or "perjasa" in content_lower:
        tags.add("domain/sovereign-ai")
    if "csm" in content_lower and ("cybersecurity malaysia" in content_lower or "partnership" in content_lower or "mou" in content_lower):
        tags.add("domain/csm-partnership")
    if "political" in content_lower and ("intelligence" in content_lower or "election" in content_lower):
        tags.add("domain/political-intelligence")
    if "stakeholder engagement" in content_lower or "sse lead" in content_lower or "amelia" in content_lower:
        if "stakeholder" in content_lower:
            tags.add("domain/stakeholder-engagement")
    if "tbh" in content_lower or "hiring" in content_lower or "project manager" in content_lower:
        tags.add("domain/organisational-capability")
    if "memory infrastructure" in content_lower or "honcho" in content_lower or "tei" in content_lower or "pgvector" in content_lower or "deriver" in content_lower or "embedding" in content_lower:
        tags.add("domain/data-infrastructure")
    if "productization" in content_lower or "productisation" in content_lower:
        tags.add("domain/cybersecurity-productisation")
    if "commercial" in content_lower and ("pipeline" in content_lower or "gtm" in content_lower or "revenue" in content_lower):
        tags.add("domain/commercial-development")
    return tags


def get_framework_tags(content_lower, fm, filepath):
    """Add framework tags based on content."""
    tags = set()
    
    # Cognitive Loop
    if any(kw in content_lower for kw in [
        "cognitive loop", "sop-cl-001", "stage mapping", "gap identification",
        "kill date", "week-over-week", "cognitive loop review",
        "strategic pathway", "programme review"
    ]):
        tags.add("framework/cognitive-loop")
    
    # AIP
    if any(kw in content_lower for kw in [
        "actionable intelligence protocol", "aip-productization", "aip productization",
        "productization track", "productisation track", "gate tracker",
        "track a", "track b", "track c", "voroncitadel gtm",
        "govsec tip", "cyberdsa demo", "chainsentry pilot",
        "poc document", "commercial packaging", "white-label",
        "security remediation", "core build", "ai analyst workbench",
        "demo environment", "credential closure", "deployment parity",
        "pilot scope definition", "aip gate"
    ]):
        tags.add("framework/actionable-intelligence-protocol")
    
    # WIP
    if any(kw in content_lower for kw in [
        "workflow identification", "wip protocol", "turnaround time",
        "tat ", "7-working-day", "creation owner", "qc reviewer",
        "approval owner", "execution owner", "compression flag",
        "orphan role", "compression risk"
    ]):
        tags.add("framework/workflow-identification-protocol")
    
    # Engineered Success
    if any(kw in content_lower for kw in [
        "engineered success", "§9", "definition of done", "dod item",
        "success conditions", "failure conditions", "critical path",
        "leading indicator", "lagging indicator", "verification criteria",
        "engineered-success-register", "es-001", "es-002", "es-003",
        "es-004", "es-005", "es-006", "es-007"
    ]):
        tags.add("framework/engineered-success")
    
    # Action Validation
    if any(kw in content_lower for kw in [
        "sop-av-001", "action validation", "validate-actions",
        "action register validation", "cross-evidence reconciliation",
        "v1:", "v2:", "v3:", "v7:", "v8:", "v13:", "v14:", "v15:"
    ]):
        tags.add("framework/action-validation")
    
    return tags


def get_cognitive_loop_tags(content_lower, fm):
    """Add cognitive-loop phase tags."""
    tags = set()
    if "stage mapping" in content_lower or "stage-level progression" in content_lower or "progression matrix" in content_lower:
        tags.add("cognitive-loop/stage-mapping")
    if "largest gap" in content_lower or "single largest gap" in content_lower or "gap identification" in content_lower:
        tags.add("cognitive-loop/gap-identification")
    if "secondary pattern" in content_lower:
        tags.add("cognitive-loop/secondary-pattern")
    if "kill date" in content_lower:
        tags.add("cognitive-loop/kill-date-enforcement")
    if "self-assessment" in content_lower:
        tags.add("cognitive-loop/self-assessment")
    if "week-over-week" in content_lower or "week over week" in content_lower:
        tags.add("cognitive-loop/week-over-week-delta")
    if "sense" in content_lower and "classify" in content_lower:
        tags.add("cognitive-loop/full-cycle")
    return tags


def get_outcome_tags(content_lower, fm):
    """Add outcome tags based on §9 DoD status."""
    tags = set()
    status = fm.get("status", "").lower()
    
    if "dod" in content_lower:
        if "dod-pending" in content_lower or "dod pending" in content_lower or "DoD Items" in content_lower:
            if "complete" not in status and "completed" not in status:
                tags.add("outcome/dod-pending")
        if "dod-completed" in content_lower or "dod completed" in content_lower:
            tags.add("outcome/dod-completed")
        if "dod-failed" in content_lower or "dod failed" in content_lower:
            tags.add("outcome/dod-failed")
        if "dod-blocked" in content_lower or "dod blocked" in content_lower:
            tags.add("outcome/dod-blocked")
    
    if "checkpoint" in content_lower:
        if "checkpoint passed" in content_lower or "checkpoint-passed" in content_lower:
            tags.add("outcome/checkpoint-passed")
        if "checkpoint missed" in content_lower or "checkpoint-missed" in content_lower or "overdue checkpoint" in content_lower:
            tags.add("outcome/checkpoint-missed")
    
    if "evidence" in content_lower:
        if "evidence confirmed" in content_lower or "evidence-confirmed" in content_lower or ("evidence" in content_lower and "verified" in content_lower):
            tags.add("outcome/evidence-confirmed")
        if "evidence missing" in content_lower or "evidence-missing" in content_lower or "no evidence" in content_lower:
            tags.add("outcome/evidence-missing")
    
    return tags


def get_deadline_tags(content_lower, fm):
    """Add deadline tags based on TAT/gate status."""
    tags = set()
    
    # TAT phases
    if "tat-creation" in content_lower or "creation phase" in content_lower or ("3 working days" in content_lower and "creation" in content_lower):
        tags.add("deadline/tat-creation")
    if "tat-qc" in content_lower or "qc phase" in content_lower or ("2 working days" in content_lower and "qc" in content_lower):
        tags.add("deadline/tat-qc")
    if "tat-approval" in content_lower or "approval phase" in content_lower or ("1 working day" in content_lower and "approval" in content_lower):
        tags.add("deadline/tat-approval")
    if "tat-execution" in content_lower or "execution phase" in content_lower:
        tags.add("deadline/tat-execution")
    
    # Gate status
    if "gate-approaching" in content_lower or "approaching" in content_lower and "deadline" in content_lower:
        if "72h" in content_lower or "72 hours" in content_lower or "approaching" in content_lower:
            tags.add("deadline/gate-approaching")
    if "gate-overdue" in content_lower or ("overdue" in content_lower and "gate" in content_lower):
        tags.add("deadline/gate-overdue")
    if "gate-passed" in content_lower or ("passed" in content_lower and "gate" in content_lower):
        tags.add("deadline/gate-passed")
    if "gate-failed" in content_lower or ("failed" in content_lower and "gate" in content_lower):
        tags.add("deadline/gate-failed")
    
    return tags


def get_doctrine_tags(content_lower, fm):
    """Add doctrine tags."""
    tags = set()
    if "cognitiveos prime" in content_lower or "cognitiveos-prime" in content_lower:
        tags.add("doctrine/cognitiveos-prime")
    if "adep-001" in content_lower or "agentic diligence" in content_lower:
        tags.add("doctrine/adep-001")
    if "cvs" in content_lower and ("master" in content_lower or "framework" in content_lower):
        tags.add("doctrine/cvs-master-framework")
    return tags


def get_method_tags(content_lower, fm):
    """Add method tags."""
    tags = set()
    if "triangulation" in content_lower or "cross-doctrinal" in content_lower:
        tags.add("method/triangulation")
    if "pre-mortem" in content_lower or "pre mortem" in content_lower:
        tags.add("method/pre-mortem")
    if "post-action learning" in content_lower or "post action learning" in content_lower:
        tags.add("method/post-action-learning")
    if "cross-doctrinal analysis" in content_lower:
        tags.add("method/cross-doctrinal-analysis")
    if "engineered success" in content_lower and ("framework" in content_lower or "§9" in content_lower):
        tags.add("method/engineered-success")
    return tags


def process_file(filepath, stats):
    """Process a single file — read, analyze, tag, write."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        stats['errors'] += 1
        return
    
    # Extract existing frontmatter
    fm_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not fm_match:
        stats['skipped'] += 1
        return
    
    fm_text = fm_match.group(1)
    content_body = content[fm_match.end():]
    content_lower = (fm_text + ' ' + content_body).lower()
    
    # Parse existing tags from frontmatter — handle both indented and non-indented formats
    existing_tags = set()
    in_tags = False
    fm_lines = fm_text.split('\n')
    for line in fm_lines:
        if line.strip().startswith('tags:'):
            in_tags = True
            continue
        if in_tags:
            # Match '- tag' (no indent), '  - tag' (2-space), or '    - tag' (4-space)
            stripped = line.strip()
            if stripped.startswith('- '):
                tag = stripped.lstrip('-').strip()
                existing_tags.add(tag)
            elif line and not line.startswith(' ') and not line.startswith('\t'):
                in_tags = False
    
    # Generate new tags
    new_tags = set()
    new_tags |= get_domain_tags(content_lower, {})
    new_tags |= get_framework_tags(content_lower, {}, filepath)
    new_tags |= get_cognitive_loop_tags(content_lower, {})
    new_tags |= get_outcome_tags(content_lower, {})
    new_tags |= get_deadline_tags(content_lower, {})
    new_tags |= get_doctrine_tags(content_lower, {})
    new_tags |= get_method_tags(content_lower, {})
    
    # Only add tags that don't already exist
    tags_to_add = new_tags - existing_tags
    
    if not tags_to_add:
        stats['unchanged'] += 1
        return
    
    # Build new tags list (existing + new)
    all_tags = sorted(existing_tags | tags_to_add)
    
    # Rebuild frontmatter with new tags
    new_fm_lines = []
    in_tags_section = False
    tags_replaced = False
    
    for line in fm_lines:
        if line.strip().startswith('tags:'):
            in_tags_section = True
            new_fm_lines.append('tags:')
            for tag in all_tags:
                new_fm_lines.append(f'  - {tag}')
            tags_replaced = True
            continue
        if in_tags_section:
            stripped = line.strip()
            # Skip old tag lines (any indentation: '- tag', '  - tag', '    - tag')
            if stripped.startswith('- '):
                continue
            else:
                in_tags_section = False
        
        new_fm_lines.append(line)
    
    # If no tags section existed, add one
    if not tags_replaced:
        # Find a good place to insert tags (after the first few fields)
        insert_pos = min(5, len(new_fm_lines))
        new_fm_lines.insert(insert_pos, 'tags:')
        for tag in all_tags:
            new_fm_lines.insert(insert_pos + 1 + all_tags.index(tag), f'  - {tag}')
    
    new_fm = '\n'.join(new_fm_lines)
    new_content = f'---\n{new_fm}\n---{content_body}'
    
    if DRY_RUN:
        stats['would_tag'] += 1
        stats['tags_added'] += len(tags_to_add)
        if filepath not in stats['examples']:
            stats['examples'][filepath] = list(tags_to_add)[:5]
    else:
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            stats['tagged'] += 1
            stats['tags_added'] += len(tags_to_add)
        except Exception as e:
            stats['errors'] += 1
            print(f"ERROR writing {filepath}: {e}", file=sys.stderr)


def main():
    stats = {
        'scanned': 0, 'tagged': 0, 'unchanged': 0, 'skipped': 0,
        'errors': 0, 'tags_added': 0, 'would_tag': 0,
        'examples': {}
    }
    
    print(f"Retroactive Framework Tagging {'(DRY RUN)' if DRY_RUN else '(LIVE)'}")
    print(f"Repository: {REPO_DIR}")
    print()
    
    for record_dir in RECORD_DIRS:
        dir_path = os.path.join(REPO_DIR, record_dir)
        if not os.path.isdir(dir_path):
            continue
        
        files = sorted(glob.glob(os.path.join(dir_path, "*.md")))
        if not files:
            continue
        
        dir_tagged = 0
        for filepath in files:
            stats['scanned'] += 1
            process_file(filepath, stats)
            if not DRY_RUN and stats['tagged'] > (stats.get('_last_tagged', 0)):
                dir_tagged += 1
                stats['_last_tagged'] = stats['tagged']
        
        if dir_tagged or DRY_RUN:
            action = "would tag" if DRY_RUN else "tagged"
            count = stats['would_tag'] if DRY_RUN else dir_tagged
            print(f"  {record_dir}/: {count} files {action}")
    
    print()
    print(f"SUMMARY:")
    print(f"  Scanned: {stats['scanned']}")
    if DRY_RUN:
        print(f"  Would tag: {stats['would_tag']}")
    else:
        print(f"  Tagged: {stats['tagged']}")
    print(f"  Unchanged: {stats['unchanged']}")
    print(f"  Skipped: {stats['skipped']}")
    print(f"  Errors: {stats['errors']}")
    print(f"  Total tags added: {stats['tags_added']}")
    
    if stats['examples']:
        print(f"\nSample files (first 5):")
        for fp, tags in list(stats['examples'].items())[:5]:
            print(f"  {os.path.basename(fp)}: {', '.join(tags)}")


if __name__ == '__main__':
    main()
