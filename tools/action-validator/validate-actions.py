#!/usr/bin/env python3
"""
SOP-AV-001 Phase 2: Action Register Validation Script

Validates all ACT- records against evidence sources using 15 rules.
Deterministic rules (V1-V4, V7, V8, V13, V14, V15) are automated here.
Semantic rules (V5, V6, V9-V12) require AI review of the flagged output.

Usage: python3 validate-actions.py [--json] [--summary]
"""

import os
import re
import sys
import json
import glob
from datetime import datetime, date

REPO_DIR = "/home/p62operator/.openclaw/workspace/strategic-cognitiveos"
ACTIONS_DIR = os.path.join(REPO_DIR, "actions")
DECISIONS_DIR = os.path.join(REPO_DIR, "decisions")
DOCUMENTS_DIR = os.path.join(REPO_DIR, "documents")
COMMITMENTS_DIR = os.path.join(REPO_DIR, "commitments")
OUTCOMES_DIR = os.path.join(REPO_DIR, "outcomes")
RISKS_DIR = os.path.join(REPO_DIR, "risks")
INITIATIVES_DIR = os.path.join(REPO_DIR, "initiatives")
ENGAGEMENTS_DIR = os.path.join(REPO_DIR, "engagements")

OUTPUT_JSON = False
SUMMARY_ONLY = False

for arg in sys.argv[1:]:
    if arg == "--json":
        OUTPUT_JSON = True
    elif arg == "--summary":
        SUMMARY_ONLY = True
    else:
        print(f"Unknown option: {arg}", file=sys.stderr)
        sys.exit(1)

STOP_WORDS = {
    'the', 'a', 'an', 'for', 'of', 'to', 'and', 'in', 'on', 'at', 'by', 'with',
    'from', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has',
    'had', 'do', 'does', 'did', 'will', 'would', 'could', 'should', 'may',
    'might', 'must', 'shall', 'can', 'this', 'that', 'these', 'those', 'it',
    'its', 'as', 'or', 'if', 'then', 'else', 'when', 'where', 'why', 'how',
    'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some',
    'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too',
    'very', 's', 't', 'just', 'don', 'now', 'up', 'down', 'out', 'off',
    'over', 'under', 'again', 'further', 'once', 'here', 'there',
}


def extract_frontmatter(filepath):
    """Extract YAML frontmatter from a markdown file. Returns dict of fields."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read(8192)  # Only read first 8KB for frontmatter
    except Exception:
        return {}

    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return {}

    fm_text = match.group(1)
    result = {}
    for line in fm_text.split('\n'):
        if ':' in line and not line.startswith(' '):
            key, _, val = line.partition(':')
            key = key.strip()
            val = val.strip().strip('"').strip("'")
            # Skip empty values and list/array values
            if val and not val.startswith('['):
                result[key] = val
            elif val.startswith('['):
                result[key] = val  # Keep raw for related_records
    return result


def tokenize(text):
    """Extract meaningful keywords from text."""
    if not text:
        return []
    words = re.split(r'[\s;,/\-]+', text.lower())
    return [w for w in words if len(w) >= 4 and w not in STOP_WORDS]


def load_records(directory):
    """Load all .md records from a directory. Returns list of (filepath, frontmatter) tuples."""
    records = []
    for filepath in sorted(glob.glob(os.path.join(directory, "*.md"))):
        fm = extract_frontmatter(filepath)
        if fm:
            records.append((filepath, fm))
    return records


def count_actions_by_status(actions):
    """Count actions grouped by status."""
    counts = {}
    for _, fm in actions:
        status = fm.get('status', 'unknown')
        counts[status] = counts.get(status, 0) + 1
    return counts


# --- Validation Rules ---

def validate_v1(actions, decisions):
    """V1: Decision Supersession Rule"""
    flags = []
    for _, act_fm in actions:
        act_status = act_fm.get('status', '')
        if act_status not in ('draft', 'active', 'in-progress'):
            continue
        act_id = act_fm.get('id', '?')
        act_title = act_fm.get('title', '')
        act_keywords = tokenize(act_title)
        if len(act_keywords) < 2:
            continue

        for _, dec_fm in decisions:
            dec_id = dec_fm.get('id', '?')
            dec_title = dec_fm.get('title', '')
            dec_lower = dec_title.lower()

            match_count = sum(1 for kw in act_keywords if kw in dec_lower)
            if match_count >= 3:
                flags.append({
                    'rule': 'V1', 'severity': 'S1-CRITICAL',
                    'action_id': act_id, 'current_status': act_status,
                    'message': f'Potential decision supersession: {dec_id} ({dec_title}) — {match_count} keyword matches'
                })
    return flags


def validate_v2(actions, documents):
    """V2: Document Fulfilment Rule"""
    flags = []
    for _, act_fm in actions:
        act_status = act_fm.get('status', '')
        if act_status not in ('draft', 'active', 'in-progress'):
            continue
        act_id = act_fm.get('id', '?')
        act_output = act_fm.get('required_output', '')
        if not act_output:
            continue
        output_keywords = tokenize(act_output)

        for _, doc_fm in documents:
            doc_id = doc_fm.get('id', '?')
            doc_title = doc_fm.get('title', '')
            doc_keywords = tokenize(doc_title)

            match_count = sum(1 for kw in doc_keywords if kw in output_keywords or kw in act_output.lower())
            if match_count >= 3:
                flags.append({
                    'rule': 'V2', 'severity': 'S1-CRITICAL',
                    'action_id': act_id, 'current_status': act_status,
                    'message': f'Potential document fulfilment: {doc_id} ({doc_title}) — {match_count} keyword matches'
                })
    return flags


def validate_v3(actions, commitments):
    """V3: Commitment Resolution Rule"""
    flags = []
    for _, act_fm in actions:
        act_status = act_fm.get('status', '')
        if act_status not in ('draft', 'active', 'in-progress'):
            continue
        act_id = act_fm.get('id', '?')
        act_title = act_fm.get('title', '')
        act_keywords = tokenize(act_title)

        for _, com_fm in commitments:
            com_id = com_fm.get('id', '?')
            com_title = com_fm.get('title', '')
            com_lower = com_title.lower()

            match_count = sum(1 for kw in act_keywords if kw in com_lower)
            if match_count >= 3:
                flags.append({
                    'rule': 'V3', 'severity': 'S1-CRITICAL',
                    'action_id': act_id, 'current_status': act_status,
                    'message': f'Potential commitment resolution: {com_id} ({com_title}) — {match_count} keyword matches'
                })
    return flags


def validate_v4(actions, outcomes):
    """V4: Outcome Achievement Rule"""
    flags = []
    for _, act_fm in actions:
        act_status = act_fm.get('status', '')
        if act_status not in ('draft', 'active', 'in-progress'):
            continue
        act_id = act_fm.get('id', '?')
        act_title = act_fm.get('title', '')
        act_keywords = tokenize(act_title)

        for _, out_fm in outcomes:
            out_id = out_fm.get('id', '?')
            out_title = out_fm.get('title', '')
            out_lower = out_title.lower()

            match_count = sum(1 for kw in act_keywords if kw in out_lower)
            if match_count >= 3:
                flags.append({
                    'rule': 'V4', 'severity': 'S1-CRITICAL',
                    'action_id': act_id, 'current_status': act_status,
                    'message': f'Potential outcome achievement: {out_id} ({out_title}) — {match_count} keyword matches'
                })
    return flags


def validate_v7(actions, risks):
    """V7: Risk Mitigation Rule"""
    flags = []
    for _, act_fm in actions:
        act_status = act_fm.get('status', '')
        if act_status not in ('draft', 'active', 'in-progress'):
            continue
        act_id = act_fm.get('id', '?')
        act_related = act_fm.get('related_records', '')

        if 'RSK-' not in act_related:
            continue

        for _, rsk_fm in risks:
            rsk_id = rsk_fm.get('id', '?')
            rsk_status = rsk_fm.get('status', '')

            if rsk_id in act_related:
                if rsk_status in ('closed', 'mitigating'):
                    flags.append({
                        'rule': 'V7', 'severity': 'S2-HIGH',
                        'action_id': act_id, 'current_status': act_status,
                        'message': f'Linked risk {rsk_id} is {rsk_status} but action still {act_status}'
                    })
    return flags


def validate_v8(actions, initiatives):
    """V8: Initiative Status Implied Rule"""
    flags = []
    init_status_map = {}
    for _, init_fm in initiatives:
        init_id = init_fm.get('id', '')
        init_status = init_fm.get('status', '')
        if init_id and init_status:
            init_status_map[init_id] = init_status

    for _, act_fm in actions:
        act_id = act_fm.get('id', '?')
        act_status = act_fm.get('status', '')
        act_init = act_fm.get('related_initiative', '')

        if not act_init:
            continue

        for iid, i_status in init_status_map.items():
            if iid in act_init:
                if i_status in ('completed', 'archived', 'superseded'):
                    if act_status not in ('completed', 'cancelled', 'archived'):
                        flags.append({
                            'rule': 'V8', 'severity': 'S2-HIGH',
                            'action_id': act_id, 'current_status': act_status,
                            'message': f'Parent initiative {iid} is {i_status} but action still {act_status}'
                        })
                elif i_status in ('blocked', 'deferred'):
                    if act_status in ('active', 'in-progress'):
                        flags.append({
                            'rule': 'V8', 'severity': 'S3-MEDIUM',
                            'action_id': act_id, 'current_status': act_status,
                            'message': f'Parent initiative {iid} is {i_status} — action may need review'
                        })
    return flags


def validate_v13(actions):
    """V13: Deadline Staleness Rule"""
    flags = []
    today_str = date.today().isoformat()

    for _, act_fm in actions:
        act_id = act_fm.get('id', '?')
        act_status = act_fm.get('status', '')
        act_deadline = act_fm.get('deadline', '')

        if not act_deadline:
            continue
        if act_status in ('completed', 'cancelled', 'overdue', 'archived'):
            continue

        try:
            # YYYY-MM-DD comparison works lexicographically
            if act_deadline < today_str:
                flags.append({
                    'rule': 'V13', 'severity': 'S2-HIGH',
                    'action_id': act_id, 'current_status': act_status,
                    'message': f'Deadline {act_deadline} has passed — status should be overdue or blocked'
                })
        except Exception:
            pass
    return flags


def validate_v14(actions):
    """V14: Orphan Action Rule"""
    flags = []
    for _, act_fm in actions:
        act_id = act_fm.get('id', '?')
        act_status = act_fm.get('status', '')
        act_related = act_fm.get('related_records', '')
        act_init = act_fm.get('related_initiative', '')

        if act_status in ('completed', 'cancelled', 'archived'):
            continue

        has_related = act_related and act_related not in ('[]', "''", '""', '')
        has_init = act_init and act_init not in ('[]', "''", '""', '')

        if not has_related and not has_init:
            flags.append({
                'rule': 'V14', 'severity': 'S3-MEDIUM',
                'action_id': act_id, 'current_status': act_status,
                'message': 'Orphan action — no related_records and no related_initiative'
            })
    return flags


def validate_v15(actions):
    """V15: Duplicate/Superseded Action Rule"""
    flags = []
    seen = set()
    act_list = [(fm.get('id', '?'), fm.get('title', ''), fm.get('status', '')) for _, fm in actions]

    for i, (id1, title1, status1) in enumerate(act_list):
        if not title1 or status1 in ('superseded', 'cancelled', 'completed'):
            continue
        kw1 = set(tokenize(title1))
        if len(kw1) < 2:
            continue

        for j in range(i + 1, len(act_list)):
            id2, title2, status2 = act_list[j]
            if not title2 or status2 in ('superseded', 'cancelled', 'completed'):
                continue

            kw2 = set(tokenize(title2))
            if len(kw2) < 2:
                continue

            common = kw1 & kw2
            union = kw1 | kw2
            if not union:
                continue

            overlap_pct = len(common) * 100 // len(union)
            if overlap_pct >= 60:
                pair_key = tuple(sorted([id1, id2]))
                if pair_key not in seen:
                    seen.add(pair_key)
                    flags.append({
                        'rule': 'V15', 'severity': 'S3-MEDIUM',
                        'action_id': id1, 'current_status': status1,
                        'message': f'Potential duplicate: {id2} ({title2}) — {overlap_pct}% keyword overlap'
                    })
    return flags


# --- Main ---

def main():
    # Load all records
    actions = load_records(ACTIONS_DIR)
    decisions = load_records(DECISIONS_DIR)
    documents = load_records(DOCUMENTS_DIR)
    commitments = load_records(COMMITMENTS_DIR)
    outcomes = load_records(OUTCOMES_DIR)
    risks = load_records(RISKS_DIR)
    initiatives = load_records(INITIATIVES_DIR)
    engagements = load_records(ENGAGEMENTS_DIR)

    total_actions = len(actions)

    # Run all validations
    all_flags = []
    all_flags.extend(validate_v1(actions, decisions))
    all_flags.extend(validate_v2(actions, documents))
    all_flags.extend(validate_v3(actions, commitments))
    all_flags.extend(validate_v4(actions, outcomes))
    all_flags.extend(validate_v7(actions, risks))
    all_flags.extend(validate_v8(actions, initiatives))
    all_flags.extend(validate_v13(actions))
    all_flags.extend(validate_v14(actions))
    all_flags.extend(validate_v15(actions))

    # Count by severity
    s1 = sum(1 for f in all_flags if 'S1-CRITICAL' in f['severity'])
    s2 = sum(1 for f in all_flags if 'S2-HIGH' in f['severity'])
    s3 = sum(1 for f in all_flags if 'S3-MEDIUM' in f['severity'])
    total_flags = len(all_flags)

    # Status counts
    status_counts = count_actions_by_status(actions)

    if SUMMARY_ONLY:
        print(f"Actions: {total_actions} | Flags: {total_flags} (S1:{s1} S2:{s2} S3:{s3})")
        return

    if OUTPUT_JSON:
        output = {
            "report_date": datetime.utcnow().isoformat(),
            "actions_scanned": total_actions,
            "evidence_sources": {
                "decisions": len(decisions),
                "documents": len(documents),
                "commitments": len(commitments),
                "outcomes": len(outcomes),
                "risks": len(risks),
                "initiatives": len(initiatives),
                "engagements": len(engagements)
            },
            "flags": {
                "total": total_flags,
                "s1_critical": s1,
                "s2_high": s2,
                "s3_medium": s3,
                "s4_low": 0
            },
            "flag_details": all_flags,
            "status_summary": status_counts
        }
        print(json.dumps(output, indent=2))
    else:
        # Human-readable
        print(f"SOP-AV-001 VALIDATION REPORT — {datetime.utcnow().strftime('%Y-%m-%d')}")
        print("=" * 50)
        print(f"Actions scanned: {total_actions}")
        print(f"Evidence sources: DEC-({len(decisions)}), DOC-({len(documents)}), COM-({len(commitments)}), "
              f"OUT-({len(outcomes)}), RSK-({len(risks)}), INIT-({len(initiatives)}), ENG-({len(engagements)})")
        print()
        print(f"Flags raised: {total_flags}")
        print(f"  S1 CRITICAL:  {s1}")
        print(f"  S2 HIGH:      {s2}")
        print(f"  S3 MEDIUM:    {s3}")
        print()

        if total_flags == 0:
            print("No flags raised. Action register appears consistent with evidence sources.")
        else:
            print("FLAGS:")
            print("-" * 6)
            for f in all_flags:
                print(f"[{f['rule']}] [{f['severity']}] {f['action_id']} (status: {f['current_status']})")
                print(f"  → {f['message']}")
                print()

        print()
        print("STATUS SUMMARY:")
        for status in ['draft', 'in-progress', 'active', 'pending', 'blocked', 'completed', 'overdue', 'cancelled']:
            c = status_counts.get(status, 0)
            if c > 0:
                print(f"  {status}: {c}")


if __name__ == '__main__':
    main()
