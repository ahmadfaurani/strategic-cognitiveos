#!/usr/bin/env python3
"""
CognitiveOS JSON Schema Conformance Validator (Phase A, P0-TAX-03)
==================================================================
Full JSON Schema enforcement (Draft 2020-12) with datetime normalization,
complementing tools/validate.py (governance/quality validator).

Phased enforcement policy (approved 2026-09-08, ASSESS-20260908-001):
  Phase A — new records STRICT · touched records NO-REGRESSION vs baseline ·
            full corpus ADVISORY (rides weekly audit_taxonomy_v2.py run)
  Phase B — touched records STRICT
  Phase C — entire corpus STRICT

Modes:
  --file FILE [FILE ...]      Strict validation of specific records (exit 1 on any violation)
  --staged [--baseline PATH]  Pre-commit mode: strict for files absent from baseline,
                              no-regression (current count <= baseline count) for touched files
  --report [--baseline PATH]  Full-corpus advisory summary (always exit 0 unless --enforce)

Methodology note: YAML parses ISO-8601 timestamp strings into datetime objects;
schemas declare these fields type:string. Datetime values are normalized via
.isoformat() before validation. This is frozen methodology (matches
audit_taxonomy_v2.py), not leniency — null/empty timestamps still fail.
"""
import argparse
import glob
import json
import os
import sys
from datetime import date, datetime

import yaml
from jsonschema import Draft202012Validator

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_BASELINE = os.path.join(REPO, "reports", "taxonomy-audit-2026-09-08.json")
# Canonical record directories (SOP §3 v1.1 — mirrors audit_taxonomy_v2.py v1.1)
RECORD_DIRS = (
    "actions", "assessments", "briefings", "commitments", "decisions",
    "documents", "drafts", "engagements", "initiatives", "intelligence",
    "lessons", "opportunities", "organizations", "outcomes", "risks",
    "stakeholders", "artifacts",
)


def extract_frontmatter(text):
    """Line-based YAML frontmatter extraction (handles '---' inside quoted scalars)."""
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


def load_schemas():
    schemas = {}
    for f in glob.glob(os.path.join(REPO, "schemas", "*.schema.json")):
        s = json.load(open(f))
        decl = s.get("properties", {}).get("record_type", {})
        vals = [decl["const"]] if "const" in decl else (decl.get("enum") or [])
        if len(vals) == 1:
            schemas[vals[0]] = s
    return schemas


def validate_file(path, schemas):
    """Return (violations, structural_reason). violations=[] if clean."""
    rel = os.path.relpath(path, REPO).replace(os.sep, "/")
    if rel.split("/")[0] not in RECORD_DIRS:
        return [], None
    try:
        text = open(path, encoding="utf-8").read()
    except OSError as e:
        return [], f"unreadable: {e}"
    if not text.startswith("---"):
        return [], "no-frontmatter"
    fm_text = extract_frontmatter(text)
    if fm_text is None:
        return [], "malformed-frontmatter"
    try:
        fm = yaml.safe_load(fm_text)
    except Exception as e:
        return [], f"yaml-parse: {str(e).splitlines()[0][:100]}"
    if not isinstance(fm, dict):
        return [], "frontmatter-not-mapping"
    rt = fm.get("record_type")
    if rt not in schemas:
        return [], f"unknown-or-retired-record_type: {rt}"
    return [
        {"path": "/".join(map(str, e.absolute_path)) or "<root>",
         "validator": e.validator,
         "message": e.message[:160]}
        for e in Draft202012Validator(schemas[rt]).iter_errors(norm(fm))
    ], None


def load_baseline(path):
    """file -> violation count (schema + structural)."""
    if not os.path.exists(path):
        return {}
    b = json.load(open(path))
    counts = {f["file"]: len(f.get("violations", [])) for f in b.get("violations", {}).get("files", [])}
    for s in b.get("violations", {}).get("structural", []):
        counts[s["file"]] = counts.get(s["file"], 0) + 1
    return counts


def cmd_files(paths, schemas):
    failed = False
    for p in paths:
        rel = os.path.relpath(p, REPO).replace(os.sep, "/")
        v, structural = validate_file(p, schemas)
        if structural:
            print(f"  ❌ SCHEMA-V2: {rel} — {structural}")
            failed = True
        elif v:
            print(f"  ❌ SCHEMA-V2: {rel} — {len(v)} violation(s)")
            for x in v[:8]:
                print(f"     [{x['validator']}] {x['path']}: {x['message']}")
            failed = True
        else:
            print(f"  ✅ SCHEMA-V2: {rel}")
    return 1 if failed else 0


def cmd_staged(paths, schemas, baseline_path):
    baseline = load_baseline(baseline_path)
    failed = False
    new_strict, touched_ok, touched_regressed = 0, 0, 0
    for p in paths:
        rel = os.path.relpath(p, REPO).replace(os.sep, "/")
        v, structural = validate_file(p, schemas)
        cur = len(v) + (1 if structural else 0)
        if structural:
            print(f"  ❌ SCHEMA-V2: {rel} — {structural}")
            failed = True
            continue
        if rel not in baseline:
            # NEW record → Phase A STRICT
            if v:
                print(f"  ❌ SCHEMA-V2 (new-record strict): {rel} — {len(v)} violation(s)")
                for x in v[:8]:
                    print(f"     [{x['validator']}] {x['path']}: {x['message']}")
                failed = True
            else:
                new_strict += 1
                print(f"  ✅ SCHEMA-V2 (new, strict): {rel}")
        else:
            # TOUCHED record → Phase A no-regression
            allowed = baseline[rel]
            if cur > allowed:
                print(f"  ❌ SCHEMA-V2 (regression): {rel} — {cur} violations (baseline allows {allowed})")
                for x in v[:8]:
                    print(f"     [{x['validator']}] {x['path']}: {x['message']}")
                failed = True
                touched_regressed += 1
            else:
                touched_ok += 1
                note = f" ({allowed - cur} improved)" if cur < allowed else ""
                print(f"  ✅ SCHEMA-V2 (touched, no-regression): {rel} — {cur}/{allowed}{note}")
    print(f"  — schema-v2 Phase A: {new_strict} new strict · {touched_ok} no-regression · "
          f"{touched_regressed} regressed —")
    return 1 if failed else 0


def cmd_report(schemas, baseline_path, enforce):
    baseline = load_baseline(baseline_path)
    total = clean = structural_n = 0
    per_type = {}
    for d in RECORD_DIRS:
      for f in glob.glob(os.path.join(REPO, d, "*.md")):
        rel = os.path.relpath(f, REPO).replace(os.sep, "/")
        v, structural = validate_file(f, schemas)
        total += 1
        if structural:
            structural_n += 1
            continue
        if v:
            rt = "unknown"
            parts = open(f, encoding="utf-8").read().split("---", 2)
            try:
                fm = yaml.safe_load(parts[1]) if len(parts) >= 3 else {}
                rt = fm.get("record_type", rt) if isinstance(fm, dict) else rt
            except Exception:
                pass
            d = per_type.setdefault(rt, {"records": 0, "violations": 0})
            d["records"] += 1
            d["violations"] += len(v)
        else:
            clean += 1
    nviol = sum(d["violations"] for d in per_type.values())
    print("📊 JSON Schema conformance (advisory)")
    print(f"   typed records: {total - structural_n} · clean: {clean} · dirty: {(total - structural_n) - clean} · structural: {structural_n}")
    for rt, d in sorted(per_type.items(), key=lambda x: -x[1]["violations"])[:8]:
        print(f"   {rt:14} {d['violations']:5} violations in {d['records']} records")
    if baseline:
        b_total = sum(baseline.values())
        cur_total = sum(d["violations"] for d in per_type.values()) + structural_n
        print(f"   baseline ({os.path.basename(baseline_path)}): {b_total} → current: {cur_total} → delta: {cur_total - b_total:+d}")
    if enforce and (n_v := sum(d["violations"] for d in per_type.values())):
        print(f"🚫 enforce mode: {n_v} violations > 0")
        return 1
    return 0


def main():
    ap = argparse.ArgumentParser(description="CognitiveOS JSON Schema conformance (Phase A)")
    ap.add_argument("--file", nargs="+", help="strict-validate specific record files")
    ap.add_argument("--staged", action="store_true", help="pre-commit mode: strict new / no-regression touched")
    ap.add_argument("--report", action="store_true", help="full-corpus advisory summary")
    ap.add_argument("--baseline", default=DEFAULT_BASELINE)
    ap.add_argument("--enforce", action="store_true", help="with --report: exit 1 if corpus not clean")
    args = ap.parse_args()

    schemas = load_schemas()
    if not schemas:
        print("❌ no schemas loaded from schemas/*.schema.json")
        sys.exit(2)

    if args.staged:
        sys.exit(cmd_staged(args.file or [], schemas, args.baseline))
    if args.file:
        sys.exit(cmd_files(args.file, schemas))
    if args.report:
        sys.exit(cmd_report(schemas, args.baseline, args.enforce))

    ap.print_help()
    sys.exit(2)


if __name__ == "__main__":
    main()
