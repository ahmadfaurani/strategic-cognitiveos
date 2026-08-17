#!/usr/bin/env python3
"""
Phase 3: PIR Status Sync + Analytical Backfill
Synchronises intelligence layer (Aug 3 PIR Status Report) to record layer.

Usage:
  python3 tools/phase3-pir-sync.py --dry-run    # Show what will change
  python3 tools/phase3-pir-sync.py --execute     # Apply changes
"""

import os
import re
import sys
import yaml
import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

WS_ROOT = Path(__file__).resolve().parent.parent

# === PIR STATUS MAPPING (extracted from Aug 3 PIR Status Report) ===
# Source: indexes/pir-status-report-2026-08-03.md
# Intelligence cutoff: 2026-08-03 20:09 MYT

# 12 parent records and their file paths (CORRECTED)
PARENT_RECORDS = {
    "STK-20260725-001": {
        "file": "stakeholders/STK-20260725-001-cscdc.md",
        "record_type": "stakeholder",
        "critical_pirs": 2,
        "total_pirs": 10,
        "cronjob": "CJ-1",
        "collection_cycle": "6h",
    },
    "INIT-20260725-007": {
        "file": "initiatives/INIT-20260725-007.md",
        "record_type": "initiative",
        "critical_pirs": 3,
        "total_pirs": 10,
        "cronjob": "CJ-1",
        "collection_cycle": "6h",
    },
    "OPP-20260725-001": {
        "file": "intelligence/OPP-20260725-001-social-listening-infrastructure.md",
        "record_type": "intelligence",
        "critical_pirs": 0,
        "total_pirs": 10,
        "cronjob": "CJ-3",
        "collection_cycle": "daily",
    },
    "OPP-20260725-002": {
        "file": "intelligence/OPP-20260725-002-war-room-methodology.md",
        "record_type": "intelligence",
        "critical_pirs": 1,
        "total_pirs": 10,
        "cronjob": "CJ-5",
        "collection_cycle": "daily",
    },
    "OPP-20260725-003": {
        "file": "intelligence/OPP-20260725-003-encrypted-alert-portal.md",
        "record_type": "intelligence",
        "critical_pirs": 1,
        "total_pirs": 10,
        "cronjob": "CJ-3",
        "collection_cycle": "daily",
    },
    "OPP-20260725-004": {
        "file": "intelligence/OPP-20260725-004-content-studio.md",
        "record_type": "intelligence",
        "critical_pirs": 1,
        "total_pirs": 10,
        "cronjob": "CJ-4",
        "collection_cycle": "12h",
    },
    "OPP-20260725-005": {
        "file": "intelligence/OPP-20260725-005-pqc-sovereign-ai.md",
        "record_type": "intelligence",
        "critical_pirs": 3,
        "total_pirs": 10,
        "cronjob": "CJ-2",
        "collection_cycle": "12h",
    },
    "OPP-20260725-006": {
        "file": "intelligence/OPP-20260725-006-community-champions.md",
        "record_type": "intelligence",
        "critical_pirs": 1,
        "total_pirs": 10,
        "cronjob": "CJ-6",
        "collection_cycle": "12h",
    },
    "OPP-20260725-007": {
        "file": "intelligence/OPP-20260725-007-cyber-drill.md",
        "record_type": "intelligence",
        "critical_pirs": 2,
        "total_pirs": 10,
        "cronjob": "CJ-5",
        "collection_cycle": "daily",
    },
    "OPP-20260725-008": {
        "file": "intelligence/OPP-20260725-008-anti-deepfake-campaign.md",
        "record_type": "intelligence",
        "critical_pirs": 2,
        "total_pirs": 10,
        "cronjob": "CJ-4",
        "collection_cycle": "12h",
    },
    "OPP-20260725-009": {
        "file": "intelligence/OPP-20260725-009-g2g-briefing-support.md",
        "record_type": "intelligence",
        "critical_pirs": 0,
        "total_pirs": 10,
        "cronjob": "CJ-6",
        "collection_cycle": "12h",
    },
    "OPP-20260725-010": {
        "file": "intelligence/OPP-20260725-010-post-merger-integration.md",
        "record_type": "intelligence",
        "critical_pirs": 1,
        "total_pirs": 10,
        "cronjob": "CJ-6",
        "collection_cycle": "12h",
    },
}

# === PIR STATUS DATA (from Aug 3 report, per-PIR) ===
# Format: pir_id -> {status, parent_record, note, cj_source, osint_unresolvable}
PIR_STATUS = {
    # === CRITICAL PIRs (16) ===
    "PIR-CSCDC-001": {"status": "partial", "parent": "STK-20260725-001", "note": "Leadership Mapping — NACSA CE primary-source confirmed, MKN DG + PTPKM Director + CSM CTO mapped. Dedicated CSCDC CEO + acting CCO still not found.", "cj": "CJ-1", "priority": "critical"},
    "PIR-CSCDC-002": {"status": "open", "parent": "STK-20260725-001", "note": "Approval Timeline (Framework v2.0) — specific v2.0 approval date & 90-day clock NOT found. OSINT-unresolvable — internal instrument.", "cj": "CJ-1", "priority": "critical", "osint_unresolvable": True},
    "PIR-INIT-CSCDC-001": {"status": "open", "parent": "INIT-20260725-007", "note": "Decision Authority — KSN-as-Board-Chairman implies board-level authority; specific delegated authority NOT documented. OSINT-unresolvable.", "cj": "CJ-1", "priority": "critical", "osint_unresolvable": True},
    "PIR-INIT-CSCDC-002": {"status": "resolved", "parent": "INIT-20260725-007", "note": "Warm Introduction Path — RESOLVED. NACSA CE primary-source confirmed; CSCDC = NACSA operational arm; JPM/KSN path most evidenced. AISE26 keynote bridge verified.", "cj": "CJ-1", "priority": "critical"},
    "PIR-INIT-CSCDC-003": {"status": "open", "parent": "INIT-20260725-007", "note": "Mobilisation Timeline (weekly milestones) — internal/non-public planning document. OSINT-unresolvable.", "cj": "CJ-1", "priority": "critical", "osint_unresolvable": True},
    "PIR-OPP002-001": {"status": "partial", "parent": "OPP-20260725-002", "note": "Playbook Budget (RM 150K) — no public disclosure; inferred inter-agency-led (NACSA) + external consultancy.", "cj": "CJ-5", "priority": "critical"},
    "PIR-OPP003-003": {"status": "resolved", "parent": "OPP-20260725-003", "note": "Classification (SULUT/Rahsia) — RESOLVED. OSA 1972 four levels; MyKriptografi governs crypto product classes; MyGovCloud@PDSA for classified hosting.", "cj": "CJ-3", "priority": "critical"},
    "PIR-OPP004-002": {"status": "partial", "parent": "OPP-20260725-004", "note": "In-House vs Outsourced — LEAN IN-HOUSE signal strengthened. Walk Production (KL agency) identified as first candidate for outsourced-peak layer.", "cj": "CJ-4", "priority": "critical"},
    "PIR-OPP005-001": {"status": "partial", "parent": "OPP-20260725-005", "note": "PQC Sandbox Scope — international benchmark deeply expanded (FIPS 203/204/205, HQC, FALCON→FN-DSA). Malaysia Sandbox scope NOT public.", "cj": "CJ-2", "priority": "critical"},
    "PIR-OPP005-002": {"status": "partial", "parent": "OPP-20260725-005", "note": "PQC Timeline — international timeline resolved (U.S.: 2030/2031/2035). Malaysia Sandbox timeline NOT public.", "cj": "CJ-2", "priority": "critical"},
    "PIR-OPP005-003": {"status": "resolved", "parent": "OPP-20260725-005", "note": "Industry Engagement Model — RESOLVED. Grant-based POC cohort; templates expanded (PQCC, CISA, DHS, G7 coordinated approach).", "cj": "CJ-2", "priority": "critical"},
    "PIR-OPP006-001": {"status": "partial", "parent": "OPP-20260725-006", "note": "Curriculum Status — no public curriculum draft located (exhaustive search). Greenfield confirmed with HIGH confidence. Building blocks mapped.", "cj": "CJ-6", "priority": "critical"},
    "PIR-OPP007-001": {"status": "resolved", "parent": "OPP-20260725-007", "note": "Drill Scope & Objectives — RESOLVED. X-MAYA (since 2008) is integrated; Locked Shields 2026 integrates comms+legal+decision-making.", "cj": "CJ-5", "priority": "critical"},
    "PIR-OPP007-002": {"status": "resolved", "parent": "OPP-20260725-007", "note": "MKN Drill Protocols — RESOLVED. Arahan MKN No.24 governs X-MAYA; Act 854 Sec.24 makes drill participation mandatory.", "cj": "CJ-5", "priority": "critical"},
    "PIR-OPP008-001": {"status": "partial", "parent": "OPP-20260725-008", "note": "Campaign Strategy — national legislative architecture crystallised (Cybercrimes Bill 2026, AI Governance Bill, ASEAN guidelines). No CSCDC-specific branded campaign exists.", "cj": "CJ-4", "priority": "critical"},
    "PIR-OPP008-002": {"status": "partial", "parent": "OPP-20260725-008", "note": "Agency Selection — LEAN IN-HOUSE signal + Walk Production identified as first concrete agency candidate. Panel status UNVERIFIED.", "cj": "CJ-4", "priority": "critical"},

    # === HIGH PIRs (key resolved ones from report) ===
    "PIR-OPP002-002": {"status": "resolved", "parent": "OPP-20260725-002", "note": "Existing MKN crisis protocols — RESOLVED. NCCMP covers detection/response/communication/coordination.", "cj": "CJ-5", "priority": "high"},
    "PIR-OPP002-007": {"status": "resolved", "parent": "OPP-20260725-002", "note": "Inter-agency crisis coordination — RESOLVED. NC4-led 4-pillar CERT ecosystem.", "cj": "CJ-5", "priority": "high"},
    "PIR-OPP003-007": {"status": "resolved", "parent": "OPP-20260725-003", "note": "Hosting & data sovereignty — RESOLVED. MyGovCloud@PDSA for classified; 4 Panel CSPs for less-sensitive.", "cj": "CJ-3", "priority": "high"},
    "PIR-OPP003-009": {"status": "resolved", "parent": "OPP-20260725-003", "note": "Authentication model — RESOLVED. MyGPKI mandated (Digital Signature Act 1997).", "cj": "CJ-3", "priority": "high"},
    "PIR-OPP005-006": {"status": "resolved", "parent": "OPP-20260725-005", "note": "International partners — RESOLVED. NIST, CISA, G7 PQC guidance. Singapore/BSI have NO PQC pages = first-mover window.", "cj": "CJ-2", "priority": "high"},
    "PIR-OPP006-005": {"status": "resolved", "parent": "OPP-20260725-006", "note": "NGO/education partners — RESOLVED. KPM/MOE, MDEC, MCCO, SherpaSec, USM confirmed as ecosystem partners.", "cj": "CJ-6", "priority": "high"},
    "PIR-OPP007-003": {"status": "resolved", "parent": "OPP-20260725-007", "note": "Drill designer/facilitator — RESOLVED. X-MAYA joint MKN/CSM; CSM CyberDrill service is methodology provider.", "cj": "CJ-5", "priority": "high"},
    "PIR-OPP007-004": {"status": "resolved", "parent": "OPP-20260725-007", "note": "Participant agencies — RESOLVED. X-MAYA ≥100 CNII agencies; Act 854 NCII sector leads.", "cj": "CJ-5", "priority": "high"},
    "PIR-OPP007-005": {"status": "resolved", "parent": "OPP-20260725-007", "note": "External facilitation — RESOLVED. CSM CyberDrill service confirmed as EXCON.", "cj": "CJ-5", "priority": "high"},
    "PIR-OPP008-004": {"status": "resolved", "parent": "OPP-20260725-008", "note": "Existing MCMC campaigns — RESOLVED. Enforcement cadence quantified (42→54→65 investigations Apr 2026).", "cj": "CJ-4", "priority": "high"},
    "PIR-OPP009-001": {"status": "resolved", "parent": "OPP-20260725-009", "note": "G2G briefing capability — RESOLVED. CSCDC under PM's Dept; NCSS 2026 + CYDES platforms (27 countries, 70 delegations).", "cj": "CJ-6", "priority": "high"},
    "PIR-OPP009-002": {"status": "resolved", "parent": "OPP-20260725-009", "note": "ASEAN positioning — RESOLVED. Malaysia leads ASEAN Cybersecurity Cooperation Strategy 2026-2030.", "cj": "CJ-6", "priority": "high"},

    # === MEDIUM resolved PIRs ===
    "PIR-OPP002-005": {"status": "resolved", "parent": "OPP-20260725-002", "note": "Historical cyber incidents — RESOLVED. 2024 breaches: MyKad 17M, ATM/Wisma Putra/KDN, Prasarana RansomHub.", "cj": "CJ-5", "priority": "medium"},
    "PIR-OPP005-008": {"status": "resolved", "parent": "OPP-20260725-005", "note": "CNII migration timeline — RESOLVED. U.S. benchmark 2030/2031/2035 + DHS 7-step roadmap + G7 Financial Sector PQC Roadmap.", "cj": "CJ-2", "priority": "medium"},
    "PIR-OPP009-003": {"status": "resolved", "parent": "OPP-20260725-009", "note": "ASEAN strategy — RESOLVED. Published Jul 2026.", "cj": "CJ-6", "priority": "medium"},
    "PIR-OPP009-010": {"status": "resolved", "parent": "OPP-20260725-009", "note": "Foreign delegation engagement — RESOLVED. CYDES 2025: 70 delegations/27 countries.", "cj": "CJ-6", "priority": "medium"},

    # === LOW resolved PIRs ===
    "PIR-OPP006-010": {"status": "resolved", "parent": "OPP-20260725-006", "note": "International community-champion models — RESOLVED. UK Cyber Champions, Singapore SG Cyber Youth/Div0, Australia Cyber Centa.", "cj": "CJ-6", "priority": "low"},
    "PIR-OPP009-009": {"status": "resolved", "parent": "OPP-20260725-009", "note": "NCSS/CYDES engagement platform — RESOLVED. Confirmed.", "cj": "CJ-6", "priority": "low"},
}

# OSINT-unresolvable PIRs (require HUMINT/internal enquiry)
OSINT_UNRESOLVABLE = {
    "PIR-CSCDC-002": "Internal instrument, not publicly disclosed",
    "PIR-INIT-CSCDC-001": "Internal delegated-authority question",
    "PIR-INIT-CSCDC-003": "Internal planning document",
    "PIR-CSCDC-003": "Requires Treasury/OBB confirmation",
    "PIR-CSCDC-005": "Internal procurement decision",
    "PIR-OPP002-003": "CSCDC-specific facility (NACSA/MKN footprint exists; CSCDC space unknown)",
    "PIR-OPP003-006": "Requires CSCDC programme-office confirmation",
    "PIR-OPP004-004": "Internal HR/position-design detail",
}

# Intelligence cutoff date
INTEL_CUTOFF = "2026-08-03T20:09:00+08:00"

# Status emoji mapping
STATUS_EMOJI = {
    "resolved": "🟢",
    "partial": "🟡",
    "open": "🔴",
}

# === PARSING ===

def parse_record(filepath):
    """Parse MD with YAML frontmatter. Returns (fm_dict, body_str) or None."""
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
    return fm, fm_match.group(2)

def serialize_record(fm_dict, body_str):
    """Serialize back to MD with YAML frontmatter."""
    fm_yaml = yaml.dump(fm_dict, sort_keys=False, default_flow_style=False,
                        allow_unicode=True, width=1000)
    return f"---\n{fm_yaml}---\n{body_str}"

# === STEP 3: PIR STATUS SYNC IN BODY ===

def update_pir_status_in_body(body, record_id):
    """Find PIR sections in body (## PIR-XXXX-NNN: ... \\n **Status:** ...) and update status."""
    changes = []
    lines = body.split('\n')
    new_lines = []
    current_pir_id = None

    for i, line in enumerate(lines):
        # Track current PIR section header (handles multi-segment IDs like PIR-INIT-CSCDC-002)
        pir_header = re.match(r'^## (PIR-[A-Z0-9-]+-\d+):', line)
        if pir_header:
            current_pir_id = pir_header.group(1)
            new_lines.append(line)
            continue

        # Match Status line: **Status:** Open  or  **Status:** Partially Resolved (as of ...)
        status_match = re.match(r'^(\*\*Status:\*\*\s*)(.+)$', line)
        if status_match and current_pir_id and current_pir_id in PIR_STATUS:
            current_status_raw = status_match.group(2).strip()
            # Normalize: "Open" -> open, "Partially Resolved (as of ...)" -> partial, "Resolved" -> resolved
            if 'resolved' in current_status_raw.lower() and 'partial' not in current_status_raw.lower():
                current_status = 'resolved'
            elif 'partial' in current_status_raw.lower():
                current_status = 'partial'
            elif 'open' in current_status_raw.lower():
                current_status = 'open'
            else:
                current_status = current_status_raw.lower()

            new_status = PIR_STATUS[current_pir_id]["status"]
            priority = PIR_STATUS[current_pir_id].get("priority", "")
            emoji = STATUS_EMOJI.get(new_status, "")

            if current_status != new_status:
                # Build new status line with emoji + date
                new_status_text = f"{emoji} {new_status.title()} (synced 2026-08-18, intel cutoff 2026-08-03)"
                new_lines.append(f"**Status:** {new_status_text}")
                changes.append({
                    'pir_id': current_pir_id,
                    'old_status': current_status,
                    'new_status': new_status,
                    'priority': priority,
                })
            else:
                new_lines.append(line)

            # Add intelligence note line after Status (if not already present)
            note = PIR_STATUS[current_pir_id].get("note", "")
            if note and i + 1 < len(lines):
                next_line = lines[i + 1] if i + 1 < len(lines) else ""
                if not next_line.strip().startswith('**Intelligence:**'):
                    intel_line = f"**Intelligence:** {note} (Source: {PIR_STATUS[current_pir_id].get('cj', '?')}, Aug 3 report)"
                    new_lines.append(intel_line)
        else:
            new_lines.append(line)

    return '\n'.join(new_lines), changes

# === STEP 4: FRONTMATTER BACKFILL ===

def compute_frontmatter_backfill(fm, record_id):
    """Compute analytical frontmatter field values for a record."""
    changes = {}
    meta = PARENT_RECORDS.get(record_id, {})
    pirs_in_record = {pid: data for pid, data in PIR_STATUS.items()
                      if data.get("parent") == record_id}

    # Count statuses
    resolved_count = sum(1 for p in pirs_in_record.values() if p["status"] == "resolved")
    partial_count = sum(1 for p in pirs_in_record.values() if p["status"] == "partial")
    open_count = sum(1 for p in pirs_in_record.values() if p["status"] == "open")
    total_known = resolved_count + partial_count + open_count

    # summary — analytical, per-record
    if fm.get('summary') is None:
        if total_known > 0:
            changes['summary'] = (
                f"{total_known} PIRs tracked ({resolved_count} resolved, "
                f"{partial_count} partial, {open_count} open). "
                f"Intelligence as of {INTEL_CUTOFF[:10]}. "
                f"Collection: {meta.get('cronjob', '?')} ({meta.get('collection_cycle', '?')})."
            )
        else:
            changes['summary'] = f"10 PIRs tracked. Intelligence as of {INTEL_CUTOFF[:10]}."

    # strategic_significance — derive from PIR resolution + critical count
    if fm.get('strategic_significance') is None:
        crit = meta.get('critical_pirs', 0)
        if crit > 0:
            crit_resolved = sum(1 for p in pirs_in_record.values()
                               if p["status"] == "resolved" and p.get("priority") == "critical")
            changes['strategic_significance'] = (
                f"{crit} Critical PIRs ({crit_resolved} resolved). "
                f"CSCDC partnership workstream — {'gate prerequisites met' if crit_resolved >= crit // 2 else 'gate prerequisites pending'}."
            )
        else:
            changes['strategic_significance'] = (
                f"No Critical PIRs. Supporting workstream for CSCDC partnership."
            )

    # confidence — map from best PIR collection confidence
    if fm.get('confidence') is None:
        if resolved_count >= 3:
            changes['confidence'] = 'high'
        elif resolved_count >= 1 or partial_count >= 3:
            changes['confidence'] = 'medium'
        else:
            changes['confidence'] = 'low'

    # status — for STK record (missing)
    if fm.get('status') is None and record_id == "STK-20260725-001":
        changes['status'] = 'active'

    # priority — for STK record (missing)
    if fm.get('priority') is None and record_id == "STK-20260725-001":
        changes['priority'] = 'critical'

    return changes

# === STEP 5: PIR-SPECIFIC FRONTMATTER FIELDS ===

def compute_pir_fields(fm, record_id):
    """Add PIR-specific frontmatter fields."""
    changes = {}
    meta = PARENT_RECORDS.get(record_id, {})
    pirs_in_record = {pid: data for pid, data in PIR_STATUS.items()
                      if data.get("parent") == record_id}

    # pir_priority — highest PIR priority in record
    if fm.get('pir_priority') is None:
        priorities = [p.get("priority") for p in pirs_in_record.values()]
        if 'critical' in priorities:
            changes['pir_priority'] = 'critical'
        elif 'high' in priorities:
            changes['pir_priority'] = 'high'
        elif 'medium' in priorities:
            changes['pir_priority'] = 'medium'
        elif 'low' in priorities:
            changes['pir_priority'] = 'low'

    # pir_tier — collection tier from cronjob
    if fm.get('pir_tier') is None:
        changes['pir_tier'] = meta.get('cronjob', 'unassigned')

    # collection_cycle
    if fm.get('collection_cycle') is None:
        changes['collection_cycle'] = meta.get('collection_cycle', 'unassigned')

    # last_collected — Aug 3 (intelligence cutoff)
    if fm.get('last_collected') is None:
        changes['last_collected'] = '2026-08-03'

    # next_collection — would be next cronjob cycle, but cronjobs are paused
    if fm.get('next_collection') is None:
        changes['next_collection'] = 'paused — model config review'

    # related_intelligence — cronjob output references
    if fm.get('related_intelligence') is None:
        cj = meta.get('cronjob', '')
        if cj:
            # Find cronjob output files for this CJ
            cj_prefix = cj.lower().replace('cj-', 'cj') + '-'
            cron_dir = WS_ROOT / 'intelligence' / 'cron-output'
            intel_refs = []
            if cron_dir.exists():
                for f in sorted(cron_dir.iterdir()):
                    if f.name.startswith(cj_prefix) and f.name.endswith('.md'):
                        intel_refs.append(f"intelligence/cron-output/{f.name}")
            changes['related_intelligence'] = intel_refs[:5] if intel_refs else []

    return changes

# === STEP 6: HUMINT FLAG ===

def add_humint_section(body, record_id):
    """Add HUMINT-required section to body if record has OSINT-unresolvable PIRs."""
    humint_pirs = {pid: reason for pid, reason in OSINT_UNRESOLVABLE.items()
                   if PIR_STATUS.get(pid, {}).get("parent") == record_id}

    if not humint_pirs:
        return body, False

    humint_section = "\n\n## ⚠️ HUMINT Required — OSINT-Unresolvable PIRs\n\n"
    humint_section += "The following PIRs cannot be resolved via open-source intelligence collection. "
    humint_section += "They require direct internal enquiry, HUMINT, or leadership action.\n\n"
    humint_section += "| PIR ID | Priority | Reason OSINT Cannot Resolve |\n"
    humint_section += "|--------|----------|---------------------------|\n"
    for pid, reason in sorted(humint_pirs.items()):
        priority = PIR_STATUS.get(pid, {}).get("priority", "?")
        humint_section += f"| {pid} | {priority} | {reason} |\n"
    humint_section += f"\n*Flagged during Phase 3 status sync (intelligence cutoff: {INTEL_CUTOFF[:10]}).*\n"

    # Check if section already exists
    if "HUMINT Required" in body:
        return body, False

    return body + humint_section, True

# === MAIN ===

def main():
    parser = argparse.ArgumentParser(description='Phase 3 PIR Status Sync')
    parser.add_argument('--dry-run', action='store_true', default=True)
    parser.add_argument('--execute', action='store_true')
    args = parser.parse_args()
    mode = 'execute' if args.execute else 'dry-run'

    all_changes = []

    for record_id, meta in PARENT_RECORDS.items():
        filepath = WS_ROOT / meta['file']
        if not filepath.exists():
            print(f"  ✗ MISSING: {filepath}")
            continue

        result = parse_record(filepath)
        if result is None:
            print(f"  ✗ PARSE ERROR: {filepath}")
            continue

        fm, body = result
        record_changes = {
            'record_id': record_id,
            'file': meta['file'],
            'body_status_updates': [],
            'frontmatter_backfill': {},
            'pir_fields': {},
            'humint_section_added': False,
        }

        # Step 3: Body PIR status sync
        new_body, body_changes = update_pir_status_in_body(body, record_id)
        record_changes['body_status_updates'] = body_changes

        # Step 6: HUMINT section
        new_body, humint_added = add_humint_section(new_body, record_id)
        record_changes['humint_section_added'] = humint_added

        # Step 4: Frontmatter backfill
        fm_changes = compute_frontmatter_backfill(fm, record_id)
        record_changes['frontmatter_backfill'] = fm_changes

        # Step 5: PIR-specific fields
        pir_changes = compute_pir_fields(fm, record_id)
        record_changes['pir_fields'] = pir_changes

        all_changes.append((record_id, filepath, fm, body, new_body, record_changes))

    # === MANIFEST ===
    print("=" * 80)
    print("PHASE 3: PIR STATUS SYNC — DRY RUN MANIFEST")
    print(f"Intelligence cutoff: {INTEL_CUTOFF}")
    print("=" * 80)

    total_body_updates = sum(len(rc['body_status_updates']) for _, _, _, _, _, rc in all_changes)
    total_fm_backfill = sum(len(rc['frontmatter_backfill']) for _, _, _, _, _, rc in all_changes)
    total_pir_fields = sum(len(rc['pir_fields']) for _, _, _, _, _, rc in all_changes)
    total_humint = sum(1 for _, _, _, _, _, rc in all_changes if rc['humint_section_added'])

    print(f"\n## SUMMARY")
    print(f"  Records processed: {len(all_changes)}")
    print(f"  Body PIR status updates: {total_body_updates}")
    print(f"  Frontmatter analytical backfills: {total_fm_backfill}")
    print(f"  PIR-specific field additions: {total_pir_fields}")
    print(f"  HUMINT sections added: {total_humint}")

    # Body status updates detail
    print(f"\n{'='*80}")
    print(f"## BODY PIR STATUS UPDATES (Step 3)")
    print(f"{'='*80}")
    if total_body_updates == 0:
        print("  None — all PIRs already reflect current intelligence.")
    else:
        for record_id, _, _, _, _, rc in all_changes:
            if rc['body_status_updates']:
                print(f"\n  [{record_id}] {rc['file']}")
                for u in rc['body_status_updates']:
                    print(f"    {u['pir_id']:25s} | {u['old_status']:10s} -> {u['new_status']:10s} | {u['priority']}")

    # Frontmatter backfill detail
    print(f"\n{'='*80}")
    print(f"## FRONTMATTER ANALYTICAL BACKFILL (Step 4)")
    print(f"{'='*80}")
    for record_id, _, _, _, _, rc in all_changes:
        if rc['frontmatter_backfill']:
            print(f"\n  [{record_id}]")
            for field, value in rc['frontmatter_backfill'].items():
                val_str = str(value)[:80] + "..." if len(str(value)) > 80 else str(value)
                print(f"    {field:30s}: {val_str}")

    # PIR-specific fields detail
    print(f"\n{'='*80}")
    print(f"## PIR-SPECIFIC FIELD ADDITIONS (Step 5)")
    print(f"{'='*80}")
    for record_id, _, _, _, _, rc in all_changes:
        if rc['pir_fields']:
            print(f"\n  [{record_id}]")
            for field, value in rc['pir_fields'].items():
                val_str = str(value)
                if len(val_str) > 80:
                    val_str = val_str[:80] + "..."
                print(f"    {field:25s}: {val_str}")

    # HUMINT sections
    print(f"\n{'='*80}")
    print(f"## HUMINT FLAGS (Step 6)")
    print(f"{'='*80}")
    for record_id, _, _, _, _, rc in all_changes:
        if rc['humint_section_added']:
            humint_pirs = {pid: r for pid, r in OSINT_UNRESOLVABLE.items()
                          if PIR_STATUS.get(pid, {}).get("parent") == record_id}
            print(f"\n  [{record_id}] — {len(humint_pirs)} OSINT-unresolvable PIR(s):")
            for pid, reason in humint_pirs.items():
                print(f"    {pid}: {reason}")

    if total_humint == 0:
        print("  None — no OSINT-unresolvable PIRs in any record.")

    # Execute
    if mode == 'execute':
        print(f"\n{'='*80}")
        print(f"## EXECUTING")
        print(f"{'='*80}")
        modified = 0
        for record_id, filepath, fm, body, new_body, rc in all_changes:
            # Apply frontmatter changes
            new_fm = dict(fm)
            for field, value in rc['frontmatter_backfill'].items():
                new_fm[field] = value
            for field, value in rc['pir_fields'].items():
                new_fm[field] = value

            # Update timestamp
            new_fm['updated_at'] = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%S+00:00')

            # Write
            new_content = serialize_record(new_fm, new_body)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            modified += 1
            print(f"  ✓ {record_id} — {rc['file']}")

        print(f"\nModified {modified} records.")

if __name__ == '__main__':
    main()
