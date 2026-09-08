#!/usr/bin/env python3
"""
CognitiveOS Taxonomy Integrity Audit V2 (audit_taxonomy_v2.py) — v1.1
=====================================================================
Reproducible, full-corpus taxonomy integrity audit.

v1.1 (2026-09-08): two methodology corrections to the first baseline —
  (1) scan scope tightened to the 17 canonical record directories
      (SOP §3 v1.1, mirrors tools/validate_taxonomy.py + pre-commit).
      v1.0 accidentally swept memory/, profiles/, logs/, osint-stack/,
      03-VERIFICATION/ etc. as "structural" — scope contamination.
  (2) schema→record_type mapping now accepts const OR single-value enum
      (outcome.schema.json declares enum — v1.0 misclassified all OUT
      records as unknown-type).

Produces reports/taxonomy-audit-YYYY-MM-DD.{json,md}:
  - repository_commit, audit_timestamp, tool sha256, methodology_version
  - records_scanned, violations (schema + structural)
  - SECTION C open-namespace census, SECTION D mission_alignment census (informational)

Usage:
  python3 tools/audit_taxonomy_v2.py                # write .json + .md
  python3 tools/audit_taxonomy_v2.py --stdout       # print MD only
"""
import glob
import hashlib
import importlib.metadata
import json
import os
import re
import subprocess
import sys
from collections import Counter, defaultdict
from datetime import date, datetime, timezone

import yaml
from jsonschema import Draft202012Validator

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Canonical record directories (SOP §3 v1.1 — 17 dirs; mirrors validate_taxonomy.py + pre-commit)
RECORD_DIRS = (
    "actions", "assessments", "briefings", "commitments", "decisions",
    "documents", "drafts", "engagements", "initiatives", "intelligence",
    "lessons", "opportunities", "organizations", "outcomes", "risks",
    "stakeholders", "artifacts",
)

METHODOLOGY_VERSION = "v1.2-20260908"
METHODOLOGY = {
    "scope": "all *.md in the 17 canonical record directories (SOP §3 v1.1); any frontmatter state",
    "normalization": "datetime/date instances (YAML ISO-8601 auto-parsing) serialized via .isoformat() before validation; frozen methodology, not leniency — schemas declare date/time fields type:string",
    "schema_validation": "jsonschema Draft202012Validator, per-type schema (record_type via const or single-value enum), additionalProperties honored as declared",
    "violation_unit": "one violation = (file, json_path, validator) instance; records_with_violations counted separately",
    "excluded_from_violations": "taxonomy tag validation (separate validator: tools/validate_taxonomy.py) — reported informationally in SECTION C",
    "v1.2_changes": "frontmatter extraction corrected to line-based parsing — v1.0/v1.1 split('---',2) truncated frontmatter when quoted scalars contained '---' (staged media filenames), misclassifying 10 valid records as yaml-parse structural",
    "v1.1_changes": "scope narrowed to canonical record dirs (v1.0 swept non-record dirs as structural); record_type mapping extended to enum-form schemas (outcome)",
}


def extract_frontmatter(text):
    """Line-based YAML frontmatter extraction.

    Handles quoted scalar values that legitimately contain '---'
    (e.g. staged media filenames like 'POs_ITSS---2a80fadd.pdf').
    A naive split('---', 2) truncates frontmatter mid-scalar and
    produces false yaml-parse structural failures (methodology v1.2 fix).
    """
    if not text.startswith("---"):
        return None
    lines = text.split("\n")
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return "\n".join(lines[1:i])
    return None


def norm(o):
    if isinstance(o, (datetime, date)):
        return o.isoformat()
    if isinstance(o, list):
        return [norm(x) for x in o]
    if isinstance(o, dict):
        return {k: norm(v) for k, v in o.items()}
    return o


def git_commit():
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=REPO, text=True).strip()
    except Exception:
        return "unknown"


def load_schemas():
    schemas = {}
    for f in glob.glob(os.path.join(REPO, "schemas", "*.schema.json")):
        s = json.load(open(f))
        decl = s.get("properties", {}).get("record_type", {})
        vals = [decl["const"]] if "const" in decl else (decl.get("enum") or [])
        if len(vals) == 1:
            schemas[vals[0]] = s
    return schemas


def record_files():
    for d in RECORD_DIRS:
        for f in sorted(glob.glob(os.path.join(REPO, d, "*.md"))):
            yield f


def scan_records(schemas):
    results, structural, scanned = [], [], 0
    for f in record_files():
        rel = os.path.relpath(f, REPO).replace(os.sep, "/")
        text = open(f, encoding="utf-8").read()
        if not text.startswith("---"):
            structural.append((rel, "no-frontmatter"))
            continue
        fm_text = extract_frontmatter(text)
        if fm_text is None:
            structural.append((rel, "malformed-frontmatter"))
            continue
        try:
            fm = yaml.safe_load(fm_text)
        except Exception as e:
            structural.append((rel, f"yaml-parse: {str(e).splitlines()[0][:80]}"))
            continue
        if not isinstance(fm, dict):
            structural.append((rel, "frontmatter-not-mapping"))
            continue
        rt = fm.get("record_type")
        if rt not in schemas:
            structural.append((rel, f"unknown-or-retired-record_type: {rt}"))
            continue
        scanned += 1
        errs = [
            {"path": "/".join(map(str, e.absolute_path)) or "<root>",
             "validator": e.validator, "message": e.message[:160]}
            for e in Draft202012Validator(schemas[rt]).iter_errors(norm(fm))
        ]
        results.append((rel, rt, errs))
    return scanned, results, structural


def taxonomy_census():
    tax = yaml.safe_load(open(os.path.join(REPO, "taxonomy", "tags.yaml")))["namespaces"]
    open_ns = {k: set(v.get("known_values") or []) for k, v in tax.items() if v.get("pattern")}
    usage = defaultdict(set)
    for f in record_files():
        rel = os.path.relpath(f, REPO).replace(os.sep, "/")
        m = re.match(r"^---\n(.*?)\n---", open(f, encoding="utf-8").read(), re.S)
        if not m:
            continue
        try:
            fm = yaml.safe_load(m.group(1))
        except Exception:
            continue
        for tag in (fm.get("tags") or []) if isinstance(fm, dict) else []:
            if isinstance(tag, str) and "/" in tag:
                ns, val = tag.split("/", 1)
                if ns in open_ns:
                    usage[ns].add(val)
    census = {}
    for ns in sorted(set(usage) | set(open_ns)):
        used, reg = usage.get(ns, set()), open_ns.get(ns, set())
        census[ns] = {"used": len(used), "registered": len(reg), "unregistered": len(used - reg)}
    census["_total"] = {
        "used": sum(v["used"] for v in census.values()),
        "registered": sum(v["registered"] for v in census.values()),
        "unregistered": sum(v["unregistered"] for v in census.values()),
    }
    return census


def mission_alignment_census():
    tax = yaml.safe_load(open(os.path.join(REPO, "taxonomy", "tags.yaml")))["namespaces"]
    mission_vocab = set(tax["mission"]["values"])
    stats, offvocab = Counter(), Counter()
    for f in record_files():
        rel = os.path.relpath(f, REPO).replace(os.sep, "/")
        text = open(f, encoding="utf-8").read()
        m = re.search(r"^mission_alignment:\n((?:\s*- .*\n)+)", text, re.M)
        if not m:
            continue
        vals = [v.strip().lstrip("- ").strip() for v in m.group(1).strip().split("\n") if v.strip()]
        stats["records_with_field"] += 1
        prefixed = [v for v in vals if "/" in v]
        bare = [v for v in vals if "/" not in v]
        true_mission = [v for v in bare if v in mission_vocab]
        off = [v for v in bare if v not in mission_vocab]
        if prefixed:
            stats["has_cross_facet_prefixed"] += 1
        if true_mission and not off and not prefixed:
            stats["pure_true_mission"] += 1
        if off:
            stats["has_offvocab_value"] += 1
            offvocab.update(off)
        if not true_mission and not prefixed and bare:
            stats["zero_true_mission"] += 1
    return stats, offvocab.most_common(15)


def build_report(stdout_only=False):
    schemas = load_schemas()
    scanned, results, structural = scan_records(schemas)
    census = taxonomy_census()
    ma_stats, ma_offvocab = mission_alignment_census()

    v_by_type = defaultdict(lambda: {"violations": 0, "records": 0})
    v_by_cat = Counter()
    files = []
    total_v = dirty = 0
    for rel, rt, errs in results:
        if errs:
            dirty += 1
            files.append({"file": rel, "record_type": rt, "violations": errs})
        v_by_type[rt]["violations"] += len(errs)
        v_by_type[rt]["records"] += 1 if errs else 0
        for e in errs:
            v_by_cat[f"{rt}:{e['validator']}:{e['path'].split('/')[0]}"] += 1
        total_v += len(errs)

    report = {
        "repository_commit": git_commit(),
        "audit_timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "methodology_version": METHODOLOGY_VERSION,
        "validator_version": {
            "tool": "tools/audit_taxonomy_v2.py",
            "tool_sha256": hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest()[:16],
            "jsonschema": importlib.metadata.version("jsonschema"),
            "pyyaml": importlib.metadata.version("PyYAML"),
        },
        "methodology": METHODOLOGY,
        "records_scanned": scanned,
        "violations": {
            "schema_total": total_v,
            "records_with_violations": dirty,
            "records_clean": scanned - dirty,
            "structural_total": len(structural),
            "structural": [{"file": f, "reason": r} for f, r in structural],
            "by_type": dict(sorted(v_by_type.items(), key=lambda x: -x[1]["violations"])),
            "by_category": dict(v_by_cat.most_common(30)),
            "files": files,
        },
        "open_namespace_census": census,
        "mission_alignment_census": {"stats": dict(ma_stats), "top_offvocab": dict(ma_offvocab)},
    }

    L = []
    L.append(f"# Taxonomy Integrity Audit — {report['audit_timestamp'][:10]} (methodology {METHODOLOGY_VERSION})")
    L.append("")
    L.append(f"- **repository_commit:** `{report['repository_commit']}`")
    L.append(f"- **audit_timestamp:** {report['audit_timestamp']}")
    L.append(f"- **tool:** audit_taxonomy_v2.py (sha256:{report['validator_version']['tool_sha256']}, jsonschema {report['validator_version']['jsonschema']})")
    L.append(f"- **records_scanned:** {scanned} typed records (17 canonical record dirs)")
    L.append(f"- **methodology:** frozen — see JSON artifact; datetime-normalized full JSON Schema enforcement, additionalProperties honored")
    L.append("")
    L.append("## A. JSON Schema violations (burndown metric — target 0)")
    L.append("")
    L.append("| Metric | Value |")
    L.append("|--------|-------|")
    L.append(f"| Total violations | {total_v} |")
    L.append(f"| Records with ≥1 violation | {dirty} / {scanned} ({(dirty / scanned * 100) if scanned else 0:.0f}%) |")
    L.append(f"| Clean records | {scanned - dirty} |")
    L.append(f"| Structural (unparseable/unknown-type/no-frontmatter) | {len(structural)} |")
    L.append("")
    L.append("### By record type")
    L.append("")
    L.append("| Type | Violations | Records affected |")
    L.append("|------|-----------|------------------|")
    for rt, d in report["violations"]["by_type"].items():
        L.append(f"| {rt} | {d['violations']} | {d['records']} |")
    L.append("")
    L.append("### Top violation categories")
    L.append("")
    L.append("| Category | Count |")
    L.append("|----------|-------|")
    for k, c in v_by_cat.most_common(15):
        L.append(f"| {k} | {c} |")
    L.append("")
    if structural:
        L.append("### Structural violations")
        L.append("")
        for f, r in structural:
            L.append(f"- `{f}` — {r}")
        L.append("")
    L.append("## C. Open-namespace tag census (informational)")
    L.append("")
    L.append("| Namespace | Used | Registered | Unregistered |")
    L.append("|-----------|------|-----------|--------------|")
    for ns, d in census.items():
        if ns == "_total":
            continue
        L.append(f"| {ns} | {d['used']} | {d['registered']} | {d['unregistered']} |")
    t = census["_total"]
    L.append(f"| **TOTAL** | **{t['used']}** | **{t['registered']}** | **{t['unregistered']}** |")
    L.append("")
    L.append("## D. mission_alignment facet-leakage census (informational)")
    L.append("")
    for k, v in ma_stats.items():
        L.append(f"- {k}: {v}")
    L.append("")
    L.append("Top off-vocabulary values: " + ", ".join(f"{k} ({v})" for k, v in ma_offvocab[:8]))
    L.append("")
    md = "\n".join(L)

    if stdout_only:
        print(md)
        return

    os.makedirs(os.path.join(REPO, "reports"), exist_ok=True)
    day = report["audit_timestamp"][:10]
    jpath = os.path.join(REPO, "reports", f"taxonomy-audit-{day}.json")
    mpath = os.path.join(REPO, "reports", f"taxonomy-audit-{day}.md")
    json.dump(report, open(jpath, "w"), indent=1)
    open(mpath, "w").write(md)
    print(f"written: {os.path.relpath(jpath, REPO)}")
    print(f"written: {os.path.relpath(mpath, REPO)}")
    print(f"schema violations: {total_v} across {dirty}/{scanned} records; structural: {len(structural)}")


if __name__ == "__main__":
    build_report(stdout_only="--stdout" in sys.argv)
