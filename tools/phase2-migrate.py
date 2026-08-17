#!/usr/bin/env python3
"""
Phase 2 Migration Script — CognitiveOS Canonical Template Conformance
Dry-run mode generates manifest. Execute mode applies changes.

Usage:
  python3 phase2-migrate.py --dry-run    # Generate manifest only (no writes)
  python3 phase2-migrate.py --execute    # Apply all changes
  python3 phase2-migrate.py --execute --type stakeholder  # Single record type
"""

import os
import re
import sys
import yaml
import json
import argparse
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

# === CONSTANTS ===

WS_ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {'.git', 'schemas', 'templates', 'tools', 'references', 'node_modules',
             'cron-output', 'osint-stack'}

UNIVERSAL_FIELDS = [
    'id', 'record_type', 'title', 'created_at', 'updated_at', 'owner', 'status',
    'priority', 'sensitivity', 'lifecycle_state', 'confidence', 'tags', 'source',
    'summary', 'strategic_significance', 'mission_alignment', 'related_records'
]

CANONICAL_TYPES = {
    'stakeholder', 'action', 'initiative', 'risk', 'decision', 'conversation',
    'commitment', 'organization', 'intelligence', 'opportunity', 'outcome',
    'lesson', 'assessment', 'pir', 'briefing', 'draft', 'document', 'artifact'
}

# Field renames: old → new
# NOTE: assignee/assigned_to REMOVED — preserved as non-canonical (delegation ≠ ownership)
# NOTE: commitment_maker REMOVED — preserved as non-canonical (commitment maker ≠ record owner)
RENAME_MAP = {
    'influence': 'influence_level',
    'interest': 'interest_level',
    'engagement_level': 'engagement_objective',
    'likelihood': 'probability',
    'decision_maker': 'decision_owner',
    'commitment_receiver': 'receiving_stakeholder',
}

# Special swap: stakeholder records where `name` (person name) should become `title`
# and existing `title` (role/placeholder) should be preserved as a non-canonical field
STAKEHOLDER_NAME_SWAP = {
    'record_type': 'stakeholder',
    'old_field': 'name',
    'target_field': 'title',
    'displaced_field': '_displaced_title',  # preserve old title value
}

# Flat source fields that need nesting into source object
FLAT_SOURCE_FIELDS = {
    'source_type': 'type',
    'source_reference': 'reference',
    'source_platform': 'platform',
}

# Non-canonical record type reclassification
TYPE_RECLASSIFY = {
    'index': 'artifact',
    'strategy': 'initiative',
    'governance': 'document',
}

# Empty field defaults by type
def empty_value(field):
    """Return the appropriate empty value for a field."""
    if field in ('tags', 'mission_alignment', 'related_records'):
        return []
    elif field == 'source':
        return {'type': None, 'reference': None}
    else:
        return None

# === PARSING ===

def parse_record(filepath):
    """Parse a MD file with YAML frontmatter. Returns (frontmatter_dict, body_str) or None."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if not content.strip().startswith('---'):
        return None

    fm_match = re.match(r'^---\n(.*?)\n---\n?(.*)$', content, re.DOTALL)
    if not fm_match:
        return None

    try:
        fm = yaml.safe_load(fm_match.group(1))
        if not isinstance(fm, dict):
            return None
    except yaml.YAMLError:
        return None

    # Must have record_type to be a record
    if 'record_type' not in fm:
        return None

    body = fm_match.group(2)
    return fm, body

def serialize_record(fm_dict, body_str):
    """Serialize frontmatter back to MD with YAML frontmatter."""
    fm_yaml = yaml.dump(fm_dict, sort_keys=False, default_flow_style=False,
                        allow_unicode=True, width=1000)
    return f"---\n{fm_yaml}---\n{body_str}"

# === MIGRATION LOGIC ===

def compute_migration(fm, filepath, rel_path):
    """Compute all changes for a single record. Returns a change dict."""
    changes = {
        'file': rel_path,
        'record_type': fm.get('record_type', 'unknown'),
        'id': fm.get('id', 'MISSING'),
        'renames': [],
        'conflicts': [],
        'source_nesting': [],
        'empty_inserts': [],
        'type_reclassify': None,
        'stakeholder_name_swap': None,
        'id_reformat': None,
        'non_canonical_fields_preserved': [],
    }

    # 1. Type reclassification
    rt = fm.get('record_type', '')
    if rt in TYPE_RECLASSIFY:
        changes['type_reclassify'] = (rt, TYPE_RECLASSIFY[rt])

    # 1b. Stakeholder name→title swap (special case)
    if rt == 'stakeholder' and STAKEHOLDER_NAME_SWAP['old_field'] in fm:
        old_name = fm[STAKEHOLDER_NAME_SWAP['old_field']]
        existing_title = fm.get(STAKEHOLDER_NAME_SWAP['target_field'])
        if old_name is not None:
            if existing_title is not None and existing_title != old_name:
                # Displaced title (role/placeholder) — preserve as non-canonical
                changes['stakeholder_name_swap'] = {
                    'name_value': old_name,
                    'displaced_title': existing_title,
                    'action': 'swap_with_displacement'
                }
            else:
                # No existing title or same value — clean rename
                changes['stakeholder_name_swap'] = {
                    'name_value': old_name,
                    'displaced_title': None,
                    'action': 'swap_clean'
                }

    # 2. Field renames with conflict detection
    for old, new in RENAME_MAP.items():
        if old not in fm:
            continue

        old_val = fm[old]
        if old_val is None:
            # Legacy field is null — safe to remove without touching new field
            changes['renames'].append({
                'old': old, 'new': new, 'old_value': old_val,
                'new_value': fm.get(new), 'action': 'delete_null_legacy'
            })
            continue

        if new in fm and fm[new] is not None:
            # CONFLICT: both fields have values
            new_val = fm[new]
            if old_val == new_val:
                # Same value — safe to delete legacy
                changes['renames'].append({
                    'old': old, 'new': new, 'old_value': old_val,
                    'new_value': new_val, 'action': 'delete_duplicate'
                })
            else:
                # VALUE MISMATCH — flag for manual review
                changes['conflicts'].append({
                    'old': old, 'new': new,
                    'old_value': old_val, 'new_value': new_val,
                    'action': 'MANUAL_REVIEW_NEEDED',
                    'file': rel_path,
                    'id': fm.get('id', '?')
                })
        else:
            # Clean rename — move value
            changes['renames'].append({
                'old': old, 'new': new, 'old_value': old_val,
                'new_value': None, 'action': 'rename'
            })

    # 3. Flat source field nesting
    has_source_obj = 'source' in fm and fm['source'] is not None
    flat_fields_present = {f: fm[f] for f in FLAT_SOURCE_FIELDS if f in fm and fm[f] is not None}

    if flat_fields_present:
        if has_source_obj:
            # Both source object and flat fields — merge flat into existing object
            for flat_f, target_k in flat_fields_present.items():
                changes['source_nesting'].append({
                    'flat_field': flat_f,
                    'target': f'source.{target_k}',
                    'value': fm[flat_f],
                    'action': 'merge_into_existing'
                })
        else:
            # No source object — create one from flat fields
            for flat_f, target_k in flat_fields_present.items():
                changes['source_nesting'].append({
                    'flat_field': flat_f,
                    'target': f'source.{target_k}',
                    'value': fm[flat_f],
                    'action': 'create_source_object'
                })

    # 4. Empty field insertion (only for canonical record types)
    effective_rt = TYPE_RECLASSIFY.get(rt, rt)
    if effective_rt in CANONICAL_TYPES:
        for field in UNIVERSAL_FIELDS:
            if field not in fm or fm[field] is None:
                # Skip if this field is being created by a rename
                will_be_renamed = any(r['new'] == field and r['action'] in ('rename', 'delete_null_legacy', 'delete_duplicate') for r in changes['renames'])
                will_be_sourced = any(sn['target'].startswith('source.') for sn in changes['source_nesting']) and field == 'source'
                if will_be_renamed or will_be_sourced:
                    continue
                changes['empty_inserts'].append({
                    'field': field,
                    'current': fm.get(field),
                    'insert': empty_value(field)
                })

    # 5. Non-canonical fields (preserve — don't delete)
    type_specific_fields = {
        'stakeholder': {'stakeholder_type','organisation','role','influence_level','interest_level',
            'relationship_status','strategic_relevance','engagement_objective','current_position',
            'commitments_by_us','commitments_by_stakeholder','last_engagement','next_engagement',
            'relationship_owner','related_initiatives'},
        'action': {'required_output','deadline','dependency','attention_level',
            'completion_evidence','related_initiative','related_stakeholder'},
        'initiative': {'sponsor','delivery_owner','commercial_owner','portfolio_tier',
            'readiness_level','stakeholders','products','projects','next_review'},
        'risk': {'risk_category','probability','impact','mitigation_strategy','mitigation_owner',
            'trigger_conditions','related_initiative','mitigation_status'},
        'decision': {'decision_date','decision_owner','portfolio_tier','context','decision',
            'rationale','alternatives_considered','confirmed_by','confirmed_at','authority',
            'classification','assumptions','evidence','expected_outcome','consequences',
            'implementation_owner','implementation_actions','review_trigger',
            'supersedes','superseded_by'},
        'conversation': {'channel','participants','decision_owner','delivery_owner',
            'portfolio_tier','key_decisions'},
        'commitment': {'receiving_stakeholder','source_engagement','expected_delivery_date',
            'risk_of_non_delivery','escalation_date','dependencies'},
        'organization': {'org_type','sector','strategic_relevance','relationship_status',
            'relationship_owner','key_contacts','related_initiatives','engagement_objective',
            'current_position','decision_authority','commitments_by_us','commitments_by_org',
            'last_engagement','next_engagement'},
        'intelligence': {'intelligence_type','evidence','implications','open_questions',
            'recommended_actions','related_intelligence','related_stakeholders','related_initiatives'},
        'opportunity': {'opportunity_type','source_stakeholder','potential_value','timeline',
            'probability','related_initiative'},
        'outcome': {'related_initiative','outcome_date','success_metrics'},
        'lesson': {'lesson_source','lesson_date','lesson_category','applies_to','evidence'},
        'assessment': {'assessment_type','assessment_target','assessment_date','findings','recommendations'},
        'pir': {'pir_priority','pir_tier','collection_cycle','related_intelligence',
            'last_collected','next_collection'},
        'briefing': {'briefing_type','prepared_for','prepared_at','classification',
            'key_findings','recommendations'},
        'draft': {'draft_type','related_action','content_summary'},
        'document': {'document_type','file_path','related_initiative','version','author'},
        'artifact': {'artifact_type','file_path','related_initiative','version','created_by'},
    }

    known_fields = set(UNIVERSAL_FIELDS) | set(RENAME_MAP.keys()) | set(FLAT_SOURCE_FIELDS.keys())
    ts = type_specific_fields.get(effective_rt, set())
    known_fields |= ts

    for k, v in fm.items():
        if k not in known_fields and not k.startswith('_'):
            changes['non_canonical_fields_preserved'].append({
                'field': k, 'value_preview': str(v)[:60] if v else str(v)
            })

    return changes

# === MANIFEST GENERATION ===

def generate_manifest(all_changes):
    """Generate a human-readable manifest from computed changes."""
    lines = []
    lines.append("=" * 80)
    lines.append("PHASE 2 MIGRATION MANIFEST — DRY RUN")
    lines.append(f"Generated: {datetime.now(timezone.utc).isoformat()}")
    lines.append("=" * 80)

    # Summary stats
    total = len(all_changes)
    with_conflicts = sum(1 for c in all_changes if c['conflicts'])
    with_renames = sum(1 for c in all_changes if c['renames'])
    with_source = sum(1 for c in all_changes if c['source_nesting'])
    with_inserts = sum(1 for c in all_changes if c['empty_inserts'])
    with_reclassify = sum(1 for c in all_changes if c['type_reclassify'])

    total_renames = sum(len(c['renames']) for c in all_changes)
    total_conflicts = sum(len(c['conflicts']) for c in all_changes)
    total_inserts = sum(len(c['empty_inserts']) for c in all_changes)
    total_source = sum(len(c['source_nesting']) for c in all_changes)

    lines.append(f"\n## SUMMARY")
    lines.append(f"  Records scanned: {total}")
    lines.append(f"  Records with renames: {with_renames} ({total_renames} total rename ops)")
    lines.append(f"  Records with CONFLICTS: {with_conflicts} ({total_conflicts} conflict ops)")
    lines.append(f"  Records with source nesting: {with_source} ({total_source} ops)")
    lines.append(f"  Records with empty field inserts: {with_inserts} ({total_inserts} total inserts)")
    lines.append(f"  Records with type reclassification: {with_reclassify}")

    # Blocker section: value-mismatch conflicts
    lines.append(f"\n{'=' * 80}")
    lines.append(f"## BLOCKER: VALUE-MISMATCH CONFLICTS (require manual decision)")
    lines.append(f"{'=' * 80}")
    if total_conflicts == 0:
        lines.append("  None — all renames are safe.")
    else:
        lines.append(f"  {total_conflicts} conflicts found across {with_conflicts} records.")
        lines.append(f"  Policy: canonical field value wins, legacy field deleted.")
        lines.append(f"  BUT if values differ, DAF must review.\n")
        for c in all_changes:
            for conf in c['conflicts']:
                lines.append(f"  FILE: {conf['file']}")
                lines.append(f"    ID: {conf['id']}")
                lines.append(f"    OLD: {conf['old']} = {conf['old_value']}")
                lines.append(f"    NEW: {conf['new']} = {conf['new_value']}")
                lines.append(f"    DECISION: keep '{conf['new']}' (canonical), delete '{conf['old']}'?")
                lines.append(f"    ===> {'VALUES MATCH — safe to proceed' if conf['old_value'] == conf['new_value'] else 'VALUES DIFFER — REVIEW REQUIRED'}")
                lines.append("")

    # Safe renames
    lines.append(f"\n{'=' * 80}")
    lines.append(f"## SAFE RENAMES (no conflicts)")
    lines.append(f"{'=' * 80}")
    safe_renames = []
    for c in all_changes:
        for r in c['renames']:
            safe_renames.append((c['file'], c['id'], r))
    if not safe_renames:
        lines.append("  None.")
    else:
        lines.append(f"  {len(safe_renames)} safe rename operations:\n")
        for fpath, rid, r in safe_renames:
            lines.append(f"  {rid:40s} | {r['old']:25s} -> {r['new']:25s} | {r['action']}")

    # Source nesting
    lines.append(f"\n{'=' * 80}")
    lines.append(f"## SOURCE FIELD NESTING")
    lines.append(f"{'=' * 80}")
    source_ops = []
    for c in all_changes:
        for sn in c['source_nesting']:
            source_ops.append((c['file'], c['id'], sn))
    if not source_ops:
        lines.append("  None.")
    else:
        lines.append(f"  {len(source_ops)} source nesting operations:\n")
        for fpath, rid, sn in source_ops:
            lines.append(f"  {rid:40s} | {sn['flat_field']:25s} -> {sn['target']:25s} | {sn['action']}")

    # Empty field inserts
    lines.append(f"\n{'=' * 80}")
    lines.append(f"## EMPTY FIELD INSERTIONS")
    lines.append(f"{'=' * 80}")
    insert_by_field = defaultdict(int)
    for c in all_changes:
        for ins in c['empty_inserts']:
            insert_by_field[ins['field']] += 1
    if not insert_by_field:
        lines.append("  None.")
    else:
        lines.append(f"  Total insertions by field:")
        for field, count in sorted(insert_by_field.items(), key=lambda x: -x[1]):
            lines.append(f"    {field:30s}: {count:4d} records")
        lines.append(f"\n  Empty value types:")
        for field in sorted(insert_by_field.keys()):
            lines.append(f"    {field:30s}: {repr(empty_value(field))}")

    # Type reclassification
    lines.append(f"\n{'=' * 80}")
    lines.append(f"## TYPE RECLASSIFICATION")
    lines.append(f"{'=' * 80}")
    reclass = [(c['file'], c['id'], c['type_reclassify']) for c in all_changes if c['type_reclassify']]
    if not reclass:
        lines.append("  None.")
    else:
        for fpath, rid, (old, new) in reclass:
            lines.append(f"  {rid:40s} | {old} -> {new}")

    # Stakeholder name→title swaps
    lines.append(f"\n{'=' * 80}")
    lines.append(f"## STAKEHOLDER NAME→TITLE SWAPS")
    lines.append(f"{'=' * 80}")
    swaps = [(c['file'], c['id'], c['stakeholder_name_swap']) for c in all_changes if c.get('stakeholder_name_swap')]
    if not swaps:
        lines.append("  None.")
    else:
        lines.append(f"  {len(swaps)} stakeholder records:\n")
        for fpath, rid, swap in swaps:
            lines.append(f"  {rid}")
            lines.append(f"    name (person)      : {swap['name_value']}")
            lines.append(f"    displaced title    : {swap['displaced_title']}")
            lines.append(f"    action             : {swap['action']}")

    # Non-canonical fields preserved
    lines.append(f"\n{'=' * 80}")
    lines.append(f"## NON-CANONICAL FIELDS (preserved, not deleted)")
    lines.append(f"{'=' * 80}")
    non_canon = defaultdict(int)
    for c in all_changes:
        for f in c['non_canonical_fields_preserved']:
            non_canon[f['field']] += 1
    if not non_canon:
        lines.append("  None.")
    else:
        lines.append(f"  {len(non_canon)} distinct non-canonical fields preserved:")
        for field, count in sorted(non_canon.items(), key=lambda x: -x[1]):
            lines.append(f"    {field:40s}: {count:3d} records")

    # Per-record detail
    lines.append(f"\n{'=' * 80}")
    lines.append(f"## PER-RECORD CHANGE DETAIL")
    lines.append(f"{'=' * 80}")
    for c in sorted(all_changes, key=lambda x: (x['record_type'], x['id'])):
        ops = len(c['renames']) + len(c['conflicts']) + len(c['source_nesting']) + len(c['empty_inserts'])
        if ops == 0 and not c['type_reclassify']:
            continue
        lines.append(f"\n  [{c['record_type']}] {c['id']} — {c['file']}")
        if c['type_reclassify']:
            lines.append(f"    RECLASSIFY: {c['type_reclassify'][0]} -> {c['type_reclassify'][1]}")
        if c.get('stakeholder_name_swap'):
            sw = c['stakeholder_name_swap']
            lines.append(f"    NAME_SWAP: name='{sw['name_value']}' -> title (displaced: {sw['displaced_title']})")
        for r in c['renames']:
            lines.append(f"    RENAME: {r['old']} -> {r['new']} ({r['action']})")
        for conf in c['conflicts']:
            lines.append(f"    CONFLICT: {conf['old']}={conf['old_value']} vs {conf['new']}={conf['new_value']}")
        for sn in c['source_nesting']:
            lines.append(f"    SOURCE: {sn['flat_field']} -> {sn['target']} ({sn['action']})")
        for ins in c['empty_inserts']:
            lines.append(f"    INSERT: {ins['field']} = {repr(ins['insert'])}")

    lines.append(f"\n{'=' * 80}")
    lines.append(f"END OF MANIFEST")
    lines.append(f"{'=' * 80}")

    return '\n'.join(lines)

# === EXECUTION ===

def apply_migration(fm, body, changes, filepath):
    """Apply all computed changes to a record. Returns (new_fm, new_body)."""
    new_fm = dict(fm)

    # 1. Type reclassification
    if changes['type_reclassify']:
        new_fm['record_type'] = changes['type_reclassify'][1]

    # 1b. Stakeholder name→title swap
    if changes.get('stakeholder_name_swap'):
        swap = changes['stakeholder_name_swap']
        old_name_key = STAKEHOLDER_NAME_SWAP['old_field']  # 'name'
        displaced_key = STAKEHOLDER_NAME_SWAP['displaced_field']  # '_displaced_title'

        if swap['action'] == 'swap_with_displacement':
            # Preserve old title value as _displaced_title
            new_fm[displaced_key] = swap['displaced_title']
            # Set title to the person name
            new_fm['title'] = new_fm.pop(old_name_key)
        elif swap['action'] == 'swap_clean':
            # Clean rename: name → title
            new_fm['title'] = new_fm.pop(old_name_key)

    # 2. Handle renames
    for r in changes['renames']:
        old, new = r['old'], r['new']
        if r['action'] == 'rename':
            new_fm[new] = new_fm.pop(old)
        elif r['action'] in ('delete_null_legacy', 'delete_duplicate'):
            new_fm.pop(old, None)

    # 3. Handle conflicts — canonical wins, legacy deleted
    for conf in changes['conflicts']:
        new_fm.pop(conf['old'], None)
        # Keep existing new field value

    # 4. Source nesting
    source_obj = new_fm.get('source')
    if not isinstance(source_obj, dict):
        source_obj = {}
    for sn in changes['source_nesting']:
        target_key = sn['target'].split('.')[1]
        source_obj[target_key] = new_fm.pop(sn['flat_field'], source_obj.get(target_key))
    if source_obj:
        new_fm['source'] = source_obj

    # 5. Empty field insertion
    for ins in changes['empty_inserts']:
        if ins['field'] not in new_fm or new_fm[ins['field']] is None:
            new_fm[ins['field']] = ins['insert']

    return new_fm, body

# === MAIN ===

def main():
    parser = argparse.ArgumentParser(description='Phase 2 Migration Script')
    parser.add_argument('--dry-run', action='store_true', default=True,
                        help='Generate manifest only (default)')
    parser.add_argument('--execute', action='store_true',
                        help='Apply all changes')
    parser.add_argument('--type', type=str, default=None,
                        help='Migrate only specified record type')
    parser.add_argument('--output', type=str, default=None,
                        help='Output manifest file path (default: stdout)')
    args = parser.parse_args()

    mode = 'execute' if args.execute else 'dry-run'

    # Scan all records
    all_changes = []
    all_records_data = []

    for root, dirs, files in os.walk(WS_ROOT):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for f in files:
            if not f.endswith('.md'):
                continue
            fp = os.path.join(root, f)
            rel = os.path.relpath(fp, WS_ROOT)

            result = parse_record(fp)
            if result is None:
                continue

            fm, body = result
            rt = fm.get('record_type', '')

            if args.type and rt != args.type:
                continue

            changes = compute_migration(fm, fp, rel)
            all_changes.append(changes)
            all_records_data.append((fp, rel, fm, body, changes))

    # Generate manifest
    manifest = generate_manifest(all_changes)

    if args.output:
        out_path = Path(args.output)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        with open(out_path, 'w') as f:
            f.write(manifest)
        print(f"Manifest written to {out_path}")
    else:
        print(manifest)

    # Execute mode
    if mode == 'execute':
        print("\n\n=== EXECUTING MIGRATION ===")
        modified = 0
        for fp, rel, fm, body, changes in all_records_data:
            new_fm, new_body = apply_migration(fm, body, changes, fp)
            new_content = serialize_record(new_fm, new_body)
            with open(fp, 'w', encoding='utf-8') as f:
                f.write(new_content)
            modified += 1
        print(f"Modified {modified} files.")

if __name__ == '__main__':
    main()
