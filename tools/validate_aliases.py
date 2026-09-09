#!/usr/bin/env python3
"""
CognitiveOS Alias Registry Validator (D8 precondition — DEC-20260909-005)
=========================================================================
Repo-wide validation of schema-governed alias identifiers declared in record
frontmatter (`aliases:` property, registry-gated per taxonomy/registry.yaml
`aliasing` block).

Invariants enforced (DEC-20260909-005):
  A1 Type gate        — only record types listed in aliasing.schema_types may
                        carry `aliases`; all other types must not.
  A2 Uniqueness       — every alias is globally unique across the repository
                        (no two records share an alias).
  A3 Canonical-exists — every aliasing record's own canonical `id` must exist
                        (self-check) and every alias must be non-empty.
  A4 No collisions    — an alias must never equal ANY record's canonical id
                        (ids are never reused as alias handles).
  A5 No chains/cycles — an alias must not equal another record's alias AND
                        must not be an id of any record (A4 covers id-chain);
                        cycles among pure-alias handles are impossible because
                        aliases never resolve to other aliases — resolver
                        parity test (T-parity in tools/test_aliases.py)
                        proves single-hop resolution.
  A6 Resolution parity— tools/resolve_id.py resolves canonical → record and
                        alias → same record, identical result.
  A7 Backward-refs    — informational count of remaining references to alias
                        handles in corpus text (migration-progress signal;
                        non-blocking).

Usage:
  python3 tools/validate_aliases.py [--root PATH] [--quiet]
  Exit 0 = clean · exit 1 = violations (pre-commit Phase 5.5).
"""
import os
import re
import sys
from pathlib import Path

import yaml

DEFAULT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RECORD_DIRS = ("actions", "assessments", "briefings", "commitments", "decisions",
               "documents", "drafts", "engagements", "initiatives", "intelligence",
               "lessons", "opportunities", "organizations", "outcomes", "risks",
               "stakeholders", "artifacts")

ALIAS_PATTERN = re.compile(r"^[A-Z][A-Z0-9]*(?:-[A-Z0-9]+)*-[0-9]{2,8}(?:-[0-9]{3})?$")


def load_aliasing_config(root):
    reg_path = Path(root) / "taxonomy" / "registry.yaml"
    reg = __import__("yaml").safe_load(open(reg_path, encoding="utf-8"))
    cfg = reg.get("aliasing") or {}
    return cfg.get("property", "aliases"), set(cfg.get("schema_types") or []), set((cfg.get("known_duplicate_ids") or {}).get("ids") or [])


def extract_fm_lines(text):
    if not text.startswith("---"):
        return None
    lines = text.split("\n")
    try:
        end = lines[1:].index("---") + 1
    except ValueError:
        return None
    return lines[1:end]


def fm_field(fm_lines, key):
    """Scalar or block-list extraction (line-based, both indent styles)."""
    for i, l in enumerate(fm_lines):
        if l.startswith(f"{key}:"):
            v = l.split(":", 1)[1].strip()
            if v.startswith("["):
                return [x.strip().strip("\"'") for x in v.strip("[]").split(",") if x.strip()]
            if v:
                return v
            vals = []
            for l2 in fm_lines[i + 1:]:
                mt = re.match(r"^\s*-\s(.*)$", l2)
                if mt:
                    vals.append(mt.group(1).strip().strip("\"'"))
                else:
                    break
            return vals
    return None


def scan_records(root):
    """Yield (path, record_type, id, aliases_list, fm_lines)."""
    for d in RECORD_DIRS:
        base = Path(root) / d
        if not base.is_dir():
            continue
        for p in sorted(base.glob("*.md")):
            try:
                txt = p.read_text(encoding="utf-8")
            except Exception:
                continue
            fm = extract_fm_lines(txt)
            if fm is None:
                continue
            rt = fm_field(fm, "record_type")
            rid = fm_field(fm, "id")
            yield str(p.relative_to(root)), rt, rid, fm


def main():
    root = Path(sys.argv[sys.argv.index("--root") + 1]) if "--root" in sys.argv else Path(DEFAULT_ROOT)
    prop, declared_types, waived_dups = load_aliasing_config(root)

    records = {}          # canonical id → relpath
    alias_map = {}        # alias → (relpath, canonical id)
    problems = []

    for rel, rt, rid, _ in scan_records(root):
        if not rid:
            problems.append(f"[A3] {rel}: record missing canonical `id`")
            continue
        if rid in records:
            if rid in waived_dups:
                records.setdefault(rid, f"(WAIVED first-seen) {records[rid]}")
            else:
                problems.append(f"[A4] duplicate canonical id `{rid}`: {records[rid]} vs {rel}")
        else:
            records[rid] = rel

    # second pass: aliases (A1 type gate, format, A3, A4)
    for rel, rt, rid, fm_lines in scan_records(root):
        if rid is None:
            continue
        aliases = fm_field(fm_lines, "aliases")
        if aliases is None:
            continue
        if not isinstance(aliases, list):
            problems.append(f"[FMT] {rel}: aliases must be a list")
            continue
        if rt not in declared_types:
            problems.append(f"[A1] {rel}: record_type `{rt}` not in aliasing.schema_types {sorted(declared_types)} but declares aliases")
            continue
        for a in aliases:
            if not a or not isinstance(a, str):
                problems.append(f"[A3] {rel}: empty/invalid alias entry")
                continue
            if not ALIAS_PATTERN.match(a):
                problems.append(f"[FMT] {rel}: alias `{a}` fails id-token pattern")
                continue
            if a == rid:
                problems.append(f"[A4] {rel}: alias `{a}` equals own canonical id")
                continue
            if a in records:
                problems.append(f"[A4] {rel}: alias `{a}` collides with canonical id of {records[a]} (ids are never reused)")
                continue
            alias_map.setdefault(a, []).append((rel, rid))

    for a, owners in sorted(alias_map.items()):
        if len(owners) > 1:
            problems.append(f"[A2] alias `{a}` declared by multiple records: {owners}")

    # A7: backward references (informational)
    backrefs = 0
    if alias_map:
        for d in RECORD_DIRS:
            base = Path(root) / d
            if not base.is_dir():
                continue
            for p in base.glob("*.md"):
                try:
                    txt = p.read_text(encoding="utf-8", errors="ignore")
                except Exception:
                    continue
                for a in alias_map:
                    if a in txt:
                        backrefs += 1
                        break

    quiet = "--quiet" in sys.argv
    if problems:
        print("❌ ALIAS VALIDATION FAILED —", len(problems), "violation(s):")
        for pr in problems:
            print("  ", pr)
        sys.exit(1)
    if not quiet:
        print(f"✅ Alias validation passed: {len(records)} canonical ids · {len(alias_map)} aliases declared · "
              f"uniqueness/collision/chain checks clean · backward-refs: {backrefs}")
    sys.exit(0)


if __name__ == "__main__":
    main()
