#!/usr/bin/env python3
"""
CognitiveOS Registry Generator (P0-TAX-01) — canonical vocabulary propagation
=============================================================================
Single canonical vocabulary source: taxonomy/registry.yaml.

Generates the two CONSUMED target classes:
  1. taxonomy/tags.yaml            — consumed by tools/validate_taxonomy.py + pre-commit
  2. schemas/*.schema.json enums   — consumed by tools/validate.py + validate_schema_v2.py
       status        ← registry.vocab.status_by_type[record_type]
       priority      ← registry.vocab.priority.emitted
       sensitivity   ← registry.vocab.sensitivity.sets[0]
       readiness_level, portfolio_tier (initiative only) ← registry.vocab.*

Rule (ASSESS-20260908-001, Athena deliberation round 2):
  Vocabulary changes are made in registry.yaml, never in generated targets.
  Pre-commit runs --check and blocks on drift.

Method notes:
  - Schema edits are in-memory on the parsed object, then dumped in the
    canonical form (json.dumps indent=2, ensure_ascii=False, trailing newline)
    which ALL schemas already match (round-trip identity verified 2026-09-08),
    so writes are formatting-stable and diff-minimal.
  - tags.yaml is regenerated from the registry namespaces block; the header
    declares it generated. Semantic (parsed) equality is the sync criterion.

Usage:
  python3 tools/generate_from_registry.py --check   # exit 1 if targets out of sync
  python3 tools/generate_from_registry.py --write   # regenerate targets from registry
"""
import glob
import json
import os
import sys

import yaml

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REGISTRY_PATH = os.path.join(REPO, "taxonomy", "registry.yaml")
TAGS_PATH = os.path.join(REPO, "taxonomy", "tags.yaml")
SCHEMAS_DIR = os.path.join(REPO, "schemas")

TAGS_HEADER = """# GENERATED FILE — do not edit directly.
# Canonical source: taxonomy/registry.yaml (P0-TAX-01, 2026-09-08).
# Regenerate: python3 tools/generate_from_registry.py --write
# Historical changelog (v2.0 merge-debt cleanup, Aug 21 2026): see git history of this file.
"""


def load_registry():
    return yaml.safe_load(open(REGISTRY_PATH, encoding="utf-8"))


def schema_record_type(s):
    decl = s.get("properties", {}).get("record_type", {})
    vals = [decl["const"]] if "const" in decl else (decl.get("enum") or [])
    return vals[0] if len(vals) == 1 else None


def _bound_enums_impl(reg, rt):
    """Return {field: enum_values} the registry binds for a record type."""
    vocab = reg.get("vocab", {})
    want = {}
    sbt = vocab.get("status_by_type") or {}
    if rt in sbt:
        want["status"] = list(sbt[rt])
    priority = (vocab.get("priority") or {}).get("emitted")
    if isinstance(priority, list):
        want["priority"] = list(priority)
    sen_sets = (vocab.get("sensitivity") or {}).get("sets") or []
    if sen_sets:
        want["sensitivity"] = list(sen_sets[0])
    if rt == "initiative":
        readiness = (vocab.get("readiness") or {}).get("emitted")
        if isinstance(readiness, list):
            want["readiness_level"] = list(readiness)
        pt = vocab.get("portfolio_tier") or {}
        pe = list(pt.get("canonical") or []) + list(pt.get("deprecated_emitted") or [])
        if pe:
            want["portfolio_tier"] = pe
    return want


def gen_tags(reg):
    out_ns = {}
    for name, ns in reg["namespaces"].items():
        entry = {"description": ns.get("description", "")}
        if ns.get("mode") == "extensible":
            entry["pattern"] = ns.get("pattern", f"{name}/<slug>")
            entry["known_values"] = list(ns.get("known_values") or [])
        else:
            entry["values"] = list(ns.get("values", []))
        out_ns[name] = entry
    return TAGS_HEADER + yaml.safe_dump({"namespaces": out_ns}, sort_keys=False, allow_unicode=True, width=100)


def gen_aliases_property(reg):
    """JSON-schema property for registry-gated alias identifiers (D8, DEC-20260909-005).

    Declared once in taxonomy/registry.yaml (aliasing block); propagated by this
    generator into every schema whose record_type is listed in
    aliasing.schema_types. Canonical id remains the sole primary key.
    """
    al = reg.get("aliasing") or {}
    if not al.get("schema_types"):
        return None
    return {
        "type": "array",
        "items": {
            "type": "string",
            "pattern": "^[A-Z][A-Z0-9]*(?:-[A-Z0-9]+)*-[0-9]{2,8}(?:-[0-9]{3})?$",
            "maxLength": 64,
        },
        "uniqueItems": True,
        "maxItems": 16,
        "description": (
            "Secondary identifier handles (former ids) for D8 rename-with-alias. "
            "Canonical id is the sole primary key; aliases are resolution handles only. "
            "Registry-gated per taxonomy/registry.yaml aliasing block (DEC-20260909-005); "
            "validated repo-wide by tools/validate_aliases.py."
        ),
    }


# ─────────────────────────────────────────────────────────────────────────────
# --write application
# ─────────────────────────────────────────────────────────────────────────────

def _apply_bound_enums(s, reg, rt):
    """In-memory enum binding for --write. Returns (schema, changes:list[str])."""
    want = _bound_enums_impl(reg, rt)
    changes = []
    for field, values in want.items():
        prop = s.get("properties", {}).get(field)
        if not isinstance(prop, dict):
            continue
        if prop.get("enum") != values:
            prop["enum"] = list(values)
            changes.append(field)
    return s, changes


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "--check"
    if mode not in ("--write", "--check"):
        print(__doc__)
        sys.exit(2)

    reg = load_registry()
    aliasing_cfg = reg.get("aliasing") or {}
    aliasing_types = set(aliasing_cfg.get("schema_types") or [])
    want_aliases = gen_aliases_property(reg)

    if mode == "--check":
        drift = []

        # tags.yaml: parsed semantic comparison
        try:
            current = yaml.safe_load(open(TAGS_PATH, encoding="utf-8"))
        except Exception as e:
            print(f"🚫 REGISTRY DRIFT: taxonomy/tags.yaml unparseable: {str(e)[:80]}")
            sys.exit(1)
        want_tags = yaml.safe_load(gen_tags(reg))
        if current != want_tags:
            drift.append("taxonomy/tags.yaml")

        # schemas: enum comparison per bound field + registry-gated aliases property (D8)
        for f in sorted(glob.glob(os.path.join(SCHEMAS_DIR, "*.schema.json"))):
            try:
                s = json.load(open(f, encoding="utf-8"))
            except Exception as e:
                drift.append(f"schemas/{os.path.basename(f)} (parse: {str(e)[:50]})")
                continue
            rt = schema_record_type(s)
            if not rt:
                continue
            if rt in aliasing_types:
                if s.get("properties", {}).get("aliases") != want_aliases:
                    drift.append(f"schemas/{os.path.basename(f)}:aliases")
            want = _bound_enums_impl(reg, rt)
            for field, values in want.items():
                have = s.get("properties", {}).get(field, {}).get("enum")
                if have != values:
                    drift.append(f"schemas/{os.path.basename(f)}:{field}")
                    break

        if drift:
            print("🚫 REGISTRY DRIFT — generated targets out of sync with taxonomy/registry.yaml:")
            for d in drift:
                print(f"   {d}")
            print("   Fix: edit taxonomy/registry.yaml, then run: python3 tools/generate_from_registry.py --write")
            sys.exit(1)
        print("✅ registry check: tags.yaml + schema enums in sync with taxonomy/registry.yaml")
        sys.exit(0)

    # --write
    open(TAGS_PATH, "w", encoding="utf-8").write(gen_tags(reg))
    changed = []
    for f in sorted(glob.glob(os.path.join(SCHEMAS_DIR, "*.schema.json"))):
        s = json.load(open(f, encoding="utf-8"))
        rt = schema_record_type(s)
        if not rt:
            continue
        s2, changes = _apply_bound_enums(s, reg, rt)
        if rt in aliasing_types and want_aliases is not None and s2.get("properties", {}).get("aliases") != want_aliases:
            s2.setdefault("properties", {})["aliases"] = want_aliases
            changes.append("aliases")
        if changes:
            open(f, "w", encoding="utf-8").write(json.dumps(s2, indent=2, ensure_ascii=False) + "\n")
            changed.append(f"{os.path.basename(f)} ({', '.join(changes)})")
    print(f"generator: regenerated taxonomy/tags.yaml; schema enum changes: {len(changed)}")
    for c in changed:
        print(f"   {c}")
    # self-verify
    rc = os.system(f'cd "{REPO}" && python3 tools/generate_from_registry.py --check > /dev/null 2>&1')
    if rc != 0:
        print("🚫 generator self-verification FAILED — registry still out of sync after write")
        sys.exit(1)
    print("✅ generator self-verification: all targets in sync")
    sys.exit(0)


def _apply_bound_enums(s, reg, rt):
    """In-memory enum binding for --write. Returns (schema, changes)."""
    want = _bound_enums_impl(reg, rt)
    changes = []
    for field, values in want.items():
        prop = s.get("properties", {}).get(field)
        if not isinstance(prop, dict):
            continue
        if prop.get("enum") != values:
            prop["enum"] = list(values)
            changes.append(field)
    return s, changes


if __name__ == "__main__":
    main()
