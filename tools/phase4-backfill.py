#!/usr/bin/env python3
"""
Phase 4: Analytical Backfill — Heuristic-derived field population for 375 remaining records.
Fills null fields only. Never overwrites existing values. Tags heuristic content.

Usage:
  python3 tools/phase4-backfill.py --dry-run          # Show all changes
  python3 tools/phase4-backfill.py --dry-run --batch actions   # Dry run one batch
  python3 tools/phase4-backfill.py --execute          # Execute all batches
  python3 tools/phase4-backfill.py --execute --batch actions  # Execute one batch
"""

import os, re, yaml, argparse, sys
from datetime import datetime, timezone
from pathlib import Path
from collections import Counter

WS = Path(__file__).resolve().parent.parent
SKIP_DIRS = {'.git', 'schemas', 'templates', 'tools', 'references', 'cron-output', 'osint-stack', 'indexes'}
PHASE3_IDS = {
    "STK-20260725-001", "INIT-20260725-007",
    "INT-20260725-001", "INT-20260725-002", "INT-20260725-003",
    "INT-20260725-004", "INT-20260725-005", "INT-20260725-006",
    "INT-20260725-007", "INT-20260725-008", "INT-20260725-009",
    "INT-20260725-010",
}

BATCHES = {
    'actions':       {'types': ['action'], 'label': 'Batch 1: Actions'},
    'stakeholders':  {'types': ['stakeholder', 'organization'], 'label': 'Batch 2-3: Stakeholders + Organizations'},
    'others':        {'types': ['risk', 'decision', 'commitment', 'conversation', 'initiative',
                               'intelligence', 'document', 'briefing', 'assessment',
                               'outcome', 'draft', 'artifact', 'pir', 'lesson'], 'label': 'Batch 4-8: Others'},
}

# ─── Parsing ───

def parse_record(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    if not content.strip().startswith('---'):
        return None
    m = re.match(r'^---\n(.*?)\n---\n?(.*)$', content, re.DOTALL)
    if not m:
        return None
    try:
        fm = yaml.safe_load(m.group(1))
        if not isinstance(fm, dict):
            return None
    except yaml.YAMLError:
        return None
    return fm, m.group(2)

def serialize_record(fm, body):
    fm_yaml = yaml.dump(fm, sort_keys=False, default_flow_style=False,
                        allow_unicode=True, width=1000)
    return f"---\n{fm_yaml}---\n{body}"

# ─── Body extraction helpers ───

def extract_first_paragraph(body, min_len=50, max_len=200):
    """Extract first meaningful paragraph from body."""
    lines = body.strip().split('\n')
    para = []
    capture = False
    for line in lines:
        stripped = line.strip()
        if not stripped:
            if capture and para:
                break
            continue
        if stripped.startswith('---'):
            if capture and para:
                break
            continue
        if stripped.startswith('#'):
            if capture and para:
                break
            capture = True
            continue
        if stripped.startswith('|') and capture and not para:
            continue  # skip table headers
        if stripped.startswith('**') and capture:
            # Include bold lines as content
            clean = re.sub(r'\*\*([^*]+)\*\*', r'\1', stripped)
            para.append(clean)
            if len(' '.join(para)) >= max_len:
                break
            continue
        if capture:
            para.append(stripped)
            if len(' '.join(para)) >= max_len:
                break
    result = ' '.join(para).strip()
    if len(result) < min_len:
        return None
    return result[:max_len]

def extract_from_field(fm, field_name, max_len=200):
    """Extract from a specific frontmatter field."""
    val = fm.get(field_name)
    if val is None:
        return None
    if isinstance(val, str):
        return val.strip()[:max_len] if len(val.strip()) >= 20 else None
    if isinstance(val, list) and val:
        return str(val[0])[:max_len] if len(str(val[0])) >= 20 else None
    return None

def count_evidence_markers(body):
    """Count evidence quality markers in body."""
    markers = 0
    markers += len(re.findall(r'\[VERIFIED\]', body, re.IGNORECASE))
    markers += len(re.findall(r'\[CONFIRMED\]', body, re.IGNORECASE))
    markers += len(re.findall(r'confirmed', body, re.IGNORECASE))
    markers += len(re.findall(r'verified', body, re.IGNORECASE))
    markers += len(re.findall(r'\[\d+\+ sources\]', body, re.IGNORECASE))
    markers += len(re.findall(r'source:', body, re.IGNORECASE))
    return markers

def has_structured_source(fm):
    """Check if source field is structured (type + reference)."""
    src = fm.get('source')
    if not isinstance(src, dict):
        return False
    return src.get('type') is not None and src.get('reference') is not None

# ─── Type-specific backfill functions ───

def backfill_action(fm, body):
    """Backfill null fields for action records."""
    changes = {}
    
    if fm.get('summary') is None:
        # Try required_output field, then first paragraph
        summary = extract_from_field(fm, 'required_output', 200)
        if not summary:
            summary = extract_first_paragraph(body, 50, 200)
        if not summary:
            summary = extract_from_field(fm, 'title', 200)
        if summary:
            changes['summary'] = summary
    
    if fm.get('strategic_significance') is None:
        ri = fm.get('related_initiative', '')
        priority = fm.get('priority', '')
        if ri:
            changes['strategic_significance'] = f"Action supporting {ri}. Priority: {priority}."
        else:
            changes['strategic_significance'] = f"Operational action. Priority: {priority}."
    
    if fm.get('confidence') is None:
        evidence = count_evidence_markers(body)
        if fm.get('completion_evidence') or evidence >= 3:
            changes['confidence'] = 'high'
        elif evidence >= 1 or has_structured_source(fm):
            changes['confidence'] = 'medium'
        else:
            changes['confidence'] = 'medium'  # default for actions
    
    if fm.get('lifecycle_state') is None:
        status = fm.get('status', '')
        if status in ('completed', 'fulfilled'):
            changes['lifecycle_state'] = 'completed'
        elif status in ('draft',):
            changes['lifecycle_state'] = 'draft'
        elif status in ('in-progress', 'active', 'pending', 'open', 'proposed'):
            changes['lifecycle_state'] = 'active'
        else:
            changes['lifecycle_state'] = 'active'
    
    return changes

def backfill_stakeholder(fm, body):
    """Backfill null fields for stakeholder records."""
    changes = {}
    
    # Priority from influence_level
    if fm.get('priority') is None:
        influence = str(fm.get('influence_level', '')).lower()
        if influence in ('high', 'very_high', 'very high'):
            changes['priority'] = 'high'
        elif influence in ('medium',):
            changes['priority'] = 'medium'
        elif influence in ('low',):
            changes['priority'] = 'low'
        else:
            changes['priority'] = 'medium'  # default
    
    # Status
    if fm.get('status') is None:
        changes['status'] = 'active'
    
    # Summary from role + organisation
    if fm.get('summary') is None:
        role = fm.get('role', '')
        org = fm.get('organisation', '')
        title = fm.get('title', '')
        if role and org:
            changes['summary'] = f"{title} — {role} at {org}."
        elif role:
            changes['summary'] = f"{title} — {role}."
        elif org:
            changes['summary'] = f"{title} at {org}."
        else:
            summary = extract_first_paragraph(body, 50, 200)
            if summary:
                changes['summary'] = summary
            else:
                changes['summary'] = f"{title}. Stakeholder record."
    
    # Strategic significance from influence + interest + related initiatives
    if fm.get('strategic_significance') is None:
        influence = fm.get('influence_level', 'unknown')
        interest = fm.get('interest_level', 'unknown')
        initiatives = fm.get('related_initiatives', [])
        init_str = f" Linked to {len(initiatives)} initiative(s)." if isinstance(initiatives, list) and initiatives else ""
        changes['strategic_significance'] = (
            f"Influence: {influence}, Interest: {interest}.{init_str}"
        )
    
    # Confidence from body evidence
    if fm.get('confidence') is None:
        evidence = count_evidence_markers(body)
        if evidence >= 3:
            changes['confidence'] = 'high'
        elif evidence >= 1:
            changes['confidence'] = 'medium'
        else:
            changes['confidence'] = 'medium'
    
    # Lifecycle state
    if fm.get('lifecycle_state') is None:
        changes['lifecycle_state'] = 'active'
    
    return changes

def backfill_organization(fm, body):
    """Backfill null fields for organization records."""
    changes = {}
    
    # Priority from sector
    if fm.get('priority') is None:
        sector = str(fm.get('sector', '')).lower()
        org_type = str(fm.get('org_type', '')).lower()
        if 'government' in sector or 'government' in org_type:
            changes['priority'] = 'high'
        elif 'vendor' in sector or 'private' in org_type:
            changes['priority'] = 'medium'
        else:
            changes['priority'] = 'medium'
    
    # Status
    if fm.get('status') is None:
        rel_status = fm.get('relationship_status', '')
        if rel_status:
            changes['status'] = str(rel_status)
        else:
            changes['status'] = 'active'
    
    # Summary from sector + strategic relevance
    if fm.get('summary') is None:
        sector = fm.get('sector', '')
        org_type = fm.get('org_type', '')
        rel = fm.get('strategic_relevance', '')
        parts = []
        if org_type:
            parts.append(str(org_type))
        if sector:
            parts.append(f"in {sector}")
        if rel:
            parts.append(f"— {str(rel)[:80]}")
        if parts:
            changes['summary'] = ' '.join(parts)
        else:
            summary = extract_first_paragraph(body, 50, 200)
            if summary:
                changes['summary'] = summary
            else:
                changes['summary'] = f"{fm.get('title', 'Organization')}."
    
    # Strategic significance from strategic_relevance + relationship_status
    if fm.get('strategic_significance') is None:
        rel = fm.get('strategic_relevance', '')
        rel_status = fm.get('relationship_status', '')
        if rel and rel_status:
            changes['strategic_significance'] = f"{rel}. Relationship: {rel_status}."
        elif rel:
            changes['strategic_significance'] = str(rel)[:200]
        else:
            changes['strategic_significance'] = f"Organization in {fm.get('sector', 'unknown sector')}."
    
    # Confidence
    if fm.get('confidence') is None:
        evidence = count_evidence_markers(body)
        if evidence >= 2:
            changes['confidence'] = 'high'
        else:
            changes['confidence'] = 'medium'
    
    # Lifecycle state
    if fm.get('lifecycle_state') is None:
        changes['lifecycle_state'] = 'active'
    
    return changes

def backfill_risk(fm, body):
    """Backfill null fields for risk records."""
    changes = {}
    
    if fm.get('summary') is None:
        # Try risk_category or first paragraph
        cat = fm.get('risk_category', '')
        summary = extract_first_paragraph(body, 50, 200)
        if summary:
            changes['summary'] = summary
        elif cat:
            changes['summary'] = f"Risk in {cat} category."
        else:
            changes['summary'] = f"{fm.get('title', 'Risk')}."
    
    if fm.get('strategic_significance') is None:
        prob = fm.get('probability', 'unknown')
        impact = fm.get('impact', 'unknown')
        cat = fm.get('risk_category', '')
        ri = fm.get('related_initiative', '')
        sig = f"Probability: {prob}, Impact: {impact}."
        if cat:
            sig += f" Category: {cat}."
        if ri:
            sig += f" Affects: {ri}."
        changes['strategic_significance'] = sig
    
    if fm.get('confidence') is None:
        evidence = count_evidence_markers(body)
        if evidence >= 2:
            changes['confidence'] = 'high'
        elif has_structured_source(fm):
            changes['confidence'] = 'medium'
        else:
            changes['confidence'] = 'medium'
    
    if fm.get('lifecycle_state') is None:
        status = fm.get('status', '')
        if status in ('mitigating',):
            changes['lifecycle_state'] = 'active'
        elif status in ('identified', 'new'):
            changes['lifecycle_state'] = 'identified'
        elif status in ('resolved', 'closed'):
            changes['lifecycle_state'] = 'resolved'
        else:
            changes['lifecycle_state'] = 'active'
    
    return changes

def backfill_decision(fm, body):
    """Backfill null fields for decision records."""
    changes = {}
    
    if fm.get('summary') is None:
        # Try decision field, then first paragraph
        summary = extract_from_field(fm, 'decision', 200)
        if not summary:
            summary = extract_first_paragraph(body, 50, 200)
        if not summary:
            summary = extract_from_field(fm, 'title', 200)
        if summary:
            changes['summary'] = summary
    
    if fm.get('strategic_significance') is None:
        owner = fm.get('decision_owner', '')
        context = fm.get('context', '')
        tier = fm.get('portfolio_tier', '')
        parts = []
        if tier:
            parts.append(f"Portfolio: {tier}.")
        if owner:
            parts.append(f"Owner: {owner}.")
        if context:
            parts.append(f"Context: {str(context)[:80]}.")
        if parts:
            changes['strategic_significance'] = ' '.join(parts)
        else:
            changes['strategic_significance'] = "Strategic decision."
    
    if fm.get('confidence') is None:
        if fm.get('confirmed_by') and fm.get('confirmed_at'):
            changes['confidence'] = 'high'
        elif fm.get('confirmed_by'):
            changes['confidence'] = 'medium'
        else:
            changes['confidence'] = 'medium'
    
    if fm.get('lifecycle_state') is None:
        status = fm.get('status', '')
        if status in ('approved',):
            changes['lifecycle_state'] = 'approved'
        elif status in ('proposed',):
            changes['lifecycle_state'] = 'proposed'
        elif status in ('active',):
            changes['lifecycle_state'] = 'active'
        else:
            changes['lifecycle_state'] = 'active'
    
    return changes

def backfill_commitment(fm, body):
    """Backfill null fields for commitment records."""
    changes = {}
    
    if fm.get('summary') is None:
        receiver = fm.get('receiving_stakeholder', '')
        maker = fm.get('commitment_maker', '') or fm.get('owner', '')
        title = fm.get('title', '')
        if maker and receiver:
            changes['summary'] = f"{title} — {maker} → {receiver}."
        else:
            summary = extract_first_paragraph(body, 50, 200)
            if summary:
                changes['summary'] = summary
            else:
                changes['summary'] = f"{title}."
    
    if fm.get('strategic_significance') is None:
        risk = fm.get('risk_of_non_delivery', '')
        esc = fm.get('escalation_date', '')
        parts = []
        if risk:
            parts.append(f"Non-delivery risk: {risk}.")
        if esc:
            parts.append(f"Escalation: {esc}.")
        if parts:
            changes['strategic_significance'] = ' '.join(parts)
        else:
            changes['strategic_significance'] = "Operational commitment."
    
    if fm.get('confidence') is None:
        risk = str(fm.get('risk_of_non_delivery', '')).lower()
        if 'low' in risk:
            changes['confidence'] = 'high'
        elif 'high' in risk:
            changes['confidence'] = 'low'
        else:
            changes['confidence'] = 'medium'
    
    if fm.get('lifecycle_state') is None:
        status = fm.get('status', '')
        if status in ('fulfilled', 'delivered'):
            changes['lifecycle_state'] = 'fulfilled'
        elif status in ('draft',):
            changes['lifecycle_state'] = 'draft'
        else:
            changes['lifecycle_state'] = 'active'
    
    return changes

def backfill_conversation(fm, body):
    """Backfill null fields for conversation records."""
    changes = {}
    
    if fm.get('summary') is None:
        # Try key_decisions, then first paragraph
        summary = extract_from_field(fm, 'key_decisions', 200)
        if not summary:
            summary = extract_first_paragraph(body, 50, 200)
        if not summary:
            channel = fm.get('channel', '')
            participants = fm.get('participants', [])
            if channel and isinstance(participants, list) and participants:
                changes['summary'] = f"Conversation via {channel} with {', '.join(str(p) for p in participants[:3])}."
            else:
                changes['summary'] = f"{fm.get('title', 'Conversation')}."
        else:
            changes['summary'] = summary
    
    if fm.get('strategic_significance') is None:
        tier = fm.get('portfolio_tier', '')
        decisions = fm.get('key_decisions', '')
        if isinstance(decisions, list) and decisions:
            changes['strategic_significance'] = f"{len(decisions)} key decision(s). Portfolio: {tier or 'unspecified'}."
        elif tier:
            changes['strategic_significance'] = f"Portfolio: {tier}."
        else:
            changes['strategic_significance'] = "Operational conversation."
    
    if fm.get('confidence') is None:
        changes['confidence'] = 'medium'
    
    if fm.get('lifecycle_state') is None:
        changes['lifecycle_state'] = 'active'
    
    return changes

def backfill_initiative(fm, body):
    """Backfill null fields for initiative records."""
    changes = {}
    
    if fm.get('summary') is None:
        sponsor = fm.get('sponsor', '')
        readiness = fm.get('readiness_level', '')
        parts = []
        if sponsor:
            parts.append(f"Sponsor: {sponsor}.")
        if readiness:
            parts.append(f"Readiness: {readiness}.")
        if parts:
            changes['summary'] = ' '.join(parts)
        else:
            summary = extract_first_paragraph(body, 50, 200)
            if summary:
                changes['summary'] = summary
            else:
                changes['summary'] = f"{fm.get('title', 'Initiative')}."
    
    if fm.get('strategic_significance') is None:
        tier = fm.get('portfolio_tier', '')
        readiness = fm.get('readiness_level', '')
        products = fm.get('products', [])
        parts = []
        if tier:
            parts.append(f"Portfolio: {tier}.")
        if readiness:
            parts.append(f"Readiness: {readiness}.")
        if isinstance(products, list) and products:
            parts.append(f"Products: {len(products)}.")
        if parts:
            changes['strategic_significance'] = ' '.join(parts)
        else:
            changes['strategic_significance'] = "Strategic initiative."
    
    if fm.get('confidence') is None:
        changes['confidence'] = 'medium'
    
    if fm.get('lifecycle_state') is None:
        status = fm.get('status', '')
        if status in ('draft',):
            changes['lifecycle_state'] = 'draft'
        elif status in ('active',):
            changes['lifecycle_state'] = 'active'
        else:
            changes['lifecycle_state'] = 'active'
    
    return changes

def backfill_intelligence(fm, body):
    """Backfill null fields for intelligence records."""
    changes = {}
    
    if fm.get('summary') is None:
        itype = fm.get('intelligence_type', '')
        summary = extract_first_paragraph(body, 50, 200)
        if summary:
            changes['summary'] = summary
        elif itype:
            changes['summary'] = f"Intelligence — {itype}."
        else:
            changes['summary'] = f"{fm.get('title', 'Intelligence')}."
    
    if fm.get('strategic_significance') is None:
        implications = fm.get('implications', '')
        if implications:
            changes['strategic_significance'] = str(implications)[:200]
        else:
            changes['strategic_significance'] = "Intelligence product."
    
    if fm.get('confidence') is None:
        evidence = count_evidence_markers(body)
        if evidence >= 3:
            changes['confidence'] = 'high'
        elif evidence >= 1:
            changes['confidence'] = 'medium'
        else:
            changes['confidence'] = 'medium'
    
    if fm.get('lifecycle_state') is None:
        changes['lifecycle_state'] = 'active'
    
    return changes

def backfill_generic(fm, body, record_type):
    """Generic backfill for less common record types."""
    changes = {}
    
    if fm.get('summary') is None:
        summary = extract_first_paragraph(body, 50, 200)
        if not summary:
            summary = extract_from_field(fm, 'title', 200)
        if summary:
            changes['summary'] = summary
        else:
            changes['summary'] = f"{fm.get('title', record_type.title())}."
    
    if fm.get('strategic_significance') is None:
        priority = fm.get('priority', 'unspecified')
        changes['strategic_significance'] = f"{record_type.title()} record. Priority: {priority}."
    
    if fm.get('confidence') is None:
        changes['confidence'] = 'medium'
    
    if fm.get('lifecycle_state') is None:
        status = fm.get('status', '')
        if status:
            changes['lifecycle_state'] = str(status)
        else:
            changes['lifecycle_state'] = 'active'
    
    return changes

# ─── Dispatcher ───

BACKFILL_FUNCS = {
    'action': backfill_action,
    'stakeholder': backfill_stakeholder,
    'organization': backfill_organization,
    'risk': backfill_risk,
    'decision': backfill_decision,
    'commitment': backfill_commitment,
    'conversation': backfill_conversation,
    'initiative': backfill_initiative,
    'intelligence': backfill_intelligence,
}

def backfill_record(fm, body):
    """Dispatch to type-specific backfill function."""
    rtype = fm.get('record_type', '')
    func = BACKFILL_FUNCS.get(rtype, None)
    if func:
        return func(fm, body)
    else:
        return backfill_generic(fm, body, rtype)

# ─── Main ───

def main():
    parser = argparse.ArgumentParser(description='Phase 4: Analytical Backfill')
    parser.add_argument('--dry-run', action='store_true', default=True)
    parser.add_argument('--execute', action='store_true')
    parser.add_argument('--batch', choices=['actions', 'stakeholders', 'others', 'all'], default='all')
    args = parser.parse_args()
    mode = 'execute' if args.execute else 'dry-run'
    batch = args.batch

    # Collect all records
    all_records = []
    for root, dirs, files in os.walk(WS):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for f in files:
            if not f.endswith('.md'):
                continue
            fp = Path(root) / f
            result = parse_record(fp)
            if result is None:
                continue
            fm, body = result
            rid = fm.get('id')
            if rid in PHASE3_IDS:
                continue
            rtype = fm.get('record_type', '')
            all_records.append((fp, fm, body, rid, rtype))

    # Filter by batch
    if batch == 'all':
        target_records = all_records
    else:
        target_types = BATCHES[batch]['types']
        target_records = [r for r in all_records if r[4] in target_types]

    # Process
    all_changes = []
    for fp, fm, body, rid, rtype in target_records:
        changes = backfill_record(fm, body)
        if changes:
            all_changes.append((fp, fm, body, rid, rtype, changes))

    # Manifest
    print("=" * 80)
    print(f"PHASE 4: ANALYTICAL BACKFILL — {mode.upper()}")
    print(f"Batch: {batch} ({len(target_records)} records scanned)")
    print("=" * 80)

    total_fields = sum(len(c[5]) for c in all_changes)
    print(f"\nRecords with changes: {len(all_changes)}")
    print(f"Total field backfills: {total_fields}")

    # By type
    type_stats = Counter()
    field_stats = Counter()
    for _, _, _, _, rtype, changes in all_changes:
        type_stats[rtype] += 1
        for field in changes:
            field_stats[field] += 1

    print(f"\nBy record type:")
    for t, c in type_stats.most_common():
        print(f"  {t:20s}: {c:4d} records")

    print(f"\nBy field:")
    for f, c in field_stats.most_common():
        print(f"  {f:30s}: {c:4d}")

    # Show samples (first 3 per type)
    shown_types = set()
    print(f"\n{'='*80}")
    print("SAMPLE CHANGES (first 3 per type)")
    print(f"{'='*80}")
    for fp, fm, body, rid, rtype, changes in all_changes:
        if rtype not in shown_types:
            shown_types.add(rtype)
            print(f"\n  [{rid}] type={rtype}")
            for field, value in changes.items():
                val_str = str(value)[:100] + "..." if len(str(value)) > 100 else str(value)
                print(f"    {field:30s}: {val_str}")
        elif len([x for x in all_changes if x[4] == rtype and x[2] is body]) <= 3:
            print(f"\n  [{rid}] type={rtype}")
            for field, value in changes.items():
                val_str = str(value)[:100] + "..." if len(str(value)) > 100 else str(value)
                print(f"    {field:30s}: {val_str}")

    # Execute
    if mode == 'execute':
        print(f"\n{'='*80}")
        print("EXECUTING")
        print(f"{'='*80}")
        modified = 0
        for fp, fm, body, rid, rtype, changes in all_changes:
            new_fm = dict(fm)
            for field, value in changes.items():
                new_fm[field] = value
            new_fm['updated_at'] = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%S+00:00')
            new_content = serialize_record(new_fm, body)
            with open(fp, 'w', encoding='utf-8') as f:
                f.write(new_content)
            modified += 1
        print(f"\nModified {modified} records.")

if __name__ == '__main__':
    main()
