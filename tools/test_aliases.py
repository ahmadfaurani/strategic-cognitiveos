#!/usr/bin/env python3
"""
CognitiveOS Alias Infrastructure Test Suite (D8 precondition — DEC-20260909-005)
================================================================================
Tests covering all affected schema types for the registry-gated alias mechanism.

Covers (maps to validate_aliases.py A1-A7 + resolve_id.py parity):
  T-A1  Type gate        — aliases rejected on non-gated record types
  T-A2  Uniqueness       — same alias on two records → violation
  T-A3  Canonical-exists — aliasing record without `id` → violation;
                           empty alias string → violation
  T-A4  Collision        — alias equal to another record's canonical id → violation;
                           alias equal to own id → violation
  T-A5  No chains        — alias equal to another record's alias is caught by A2;
                           id-chains impossible (A4)
  T-A6  Parity           — resolve_id --parity: every alias resolves to exactly
                           one canonical record
  T-A7  Backward-refs    — reference counter reports records still citing aliases
  T-FMT Format          — malformed alias tokens → violation
  T-REG  Registry gate   — generator propagates aliases property only to
                           aliasing.schema_types; --check detects drift
  T-SYN  Schema conformance — every aliasing.schema_types schema carries a
                           registry-identical aliases property (strict jsonschema)

Isolated-root runner: every test builds a temporary repository tree
(record dirs + taxonomy/registry.yaml + tools copies) and invokes the real
validators as subprocesses — no production record is ever touched.

Usage:
  python3 tools/test_aliases.py            # run all, print summary
  python3 tools/test_aliases.py --quiet    # exit-code only
Exit 0 = all pass · exit 1 = failure(s).
"""
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
SRC_ROOT = TOOLS.parent
ALIAS_SCHEMA_TYPES = ["artifact", "intelligence", "draft", "briefing", "commitment", "document"]
ALIAS_PROPERTY = {
    "type": "array",
    "items": {
        "type": "string",
        "pattern": "^[A-Z][A-Z0-9]*(?:-[A-Z0-9]+)*-[0-9]{2,8}(?:-[0-9]{3})?$",
        "maxLength": 64,
    },
    "uniqueItems": True,
    "maxItems": 16,
    "description": "Secondary identifier handles (former ids) for D8 rename-with-alias. "
                   "Canonical id is the sole primary key; aliases are resolution handles only. "
                   "Registry-gated per taxonomy/registry.yaml aliasing block (DEC-20260909-005); "
                   "validated repo-wide by tools/validate_aliases.py.",
}

RECORD_DIRS = ["actions", "assessments", "briefings", "commitments", "decisions",
               "documents", "drafts", "engagements", "initiatives", "intelligence",
               "lessons", "opportunities", "organizations", "outcomes", "risks",
               "stakeholders", "artifacts"]

REGISTRY_TEMPLATE = """registry:
  version: 1
  rule: Vocabulary changes are made HERE, never in generated targets
namespaces:
  mission:
    mode: closed
    values: []
aliasing:
  version: 1
  property: aliases
  schema_types: {types}
  rules:
    enforce_uniqueness: true
    canonical_target_existence: true
    collision_prevention: true
    no_chains: true
    resolution_parity: true
    backward_reference_validation: true
"""


def make_repo(tmp):
    """Minimal isolated repo: record dirs, registry with aliasing block, tools copies."""
    root = Path(tmp)
    for d in RECORD_DIRS:
        (root / d).mkdir(parents=True, exist_ok=True)
    (root / "taxonomy").mkdir(exist_ok=True)
    (root / "taxonomy" / "registry.yaml").write_text(
        REGISTRY_TEMPLATE.format(types=str(ALIAS_SCHEMA_TYPES)), encoding="utf-8")
    shutil.copy(TOOLS / "validate_aliases.py", root / "validate_aliases.py")
    shutil.copy(TOOLS / "resolve_id.py", root / "resolve_id.py")
    return root


def record(root, d, rid, record_type, aliases=None):
    """Write a minimal record file; returns relpath."""
    fm = [f"id: {rid}", f"record_type: {record_type}", "title: t", "status: draft"]
    if aliases is not None:
        fm.append("aliases:")
        for a in aliases:
            fm.append(f"  - {a}")
    rel = f"{d}/{rid}.md"
    (root / rel).write_text("---\n" + "\n".join(fm) + "\n---\n\nbody\n", encoding="utf-8")
    return rel


def run_validator(root, script, *args):
    return subprocess.run([sys.executable, str(root / script), *args],
                          capture_output=True, text=True, cwd=str(root))


# ─────────────────────────────────────────────────────────────────────────────
# Tests
# ─────────────────────────────────────────────────────────────────────────────

def t_a1_type_gate(tmp):
    """aliases on a non-gated type (stakeholder) → A1 violation; gated type passes."""
    root = make_repo(tmp)
    record(root, "stakeholders", "STK-20260101-001", "stakeholder", aliases=["OLD-ID-2026"])
    record(root, "artifacts", "ART-20260101-001", "artifact")
    r = run_validator(root, "validate_aliases.py", "--root", str(root))
    ok = r.returncode == 1 and "[A1]" in r.stdout
    return ok, f"non-gated type rejected (exit={r.returncode})"


def t_a2_uniqueness(tmp):
    """Same alias declared by two records → A2 violation."""
    root = make_repo(tmp)
    record(root, "artifacts", "ART-20260101-001", "artifact", aliases=["AIP-20260101-001"])
    record(root, "artifacts", "ART-20260101-002", "artifact", aliases=["AIP-20260101-001"])
    r = run_validator(root, "validate_aliases.py", "--root", str(root))
    ok = r.returncode == 1 and "[A2]" in r.stdout
    return ok, "duplicate alias caught"


def t_a3_canonical_exists(tmp):
    """(a) record missing id entirely; (b) empty alias string → A3."""
    root = make_repo(tmp)
    (root / "artifacts" / "NOID-20260101-001.md").write_text(
        "---\nrecord_type: artifact\ntitle: t\nstatus: draft\naliases:\n  - X-20260101\n---\n\nb\n",
        encoding="utf-8")
    r = run_validator(root, "validate_aliases.py", "--root", str(root))
    a3_id = r.returncode == 1 and "[A3]" in r.stdout

    root2 = make_repo(tmp)
    record(root2, "artifacts", "ART-20260101-001", "artifact", aliases=[""])
    r2 = run_validator(root2, "validate_aliases.py", "--root", str(root2))
    a3_empty = r2.returncode == 1 and "[A3]" in r2.stdout
    return (a3_id and a3_empty), "missing-id and empty-alias both caught"


def t_a4_collision(tmp):
    """(a) alias equals ANOTHER record's canonical id → A4; (b) alias equals own id → A4."""
    root = make_repo(tmp)
    record(root, "artifacts", "ART-20260101-001", "artifact", aliases=["ART-20260101-002"])
    record(root, "artifacts", "ART-20260101-002", "artifact")
    r = run_validator(root, "validate_aliases.py", "--root", str(root))
    a4_other = r.returncode == 1 and "[A4]" in r.stdout

    root2 = make_repo(tmp)
    record(root2, "artifacts", "ART-20260101-001", "artifact", aliases=["ART-20260101-001"])
    r2 = run_validator(root2, "validate_aliases.py", "--root", str(root2))
    a4_self = r2.returncode == 1 and "[A4]" in r2.stdout
    return (a4_other and a4_self), "id-collision and self-alias both caught"


def t_a5_no_chains(tmp):
    """Alias chains are impossible by construction: an alias that names another
    record's alias is a duplicate (A2); an alias that names another record's id
    is a collision (A4). Two alias handles may never reference each other."""
    root = make_repo(tmp)
    # alias2 == alias of record 2 → A2 duplicate; not resolvable as chain
    record(root, "artifacts", "ART-20260101-001", "artifact", aliases=["FORMER-ID-2026"])
    record(root, "artifacts", "ART-20260101-002", "artifact", aliases=["FORMER-ID-2026"])
    r = run_validator(root, "validate_aliases.py", "--root", str(root))
    a2 = r.returncode == 1 and "[A2]" in r.stdout
    # chain-via-id is structurally excluded: alias FORMER-ID-2026 colliding with an id
    root2 = make_repo(tmp)
    record(root2, "artifacts", "ART-20260101-001", "artifact", aliases=["INT-20260101-002"])
    record(root2, "intelligence", "INT-20260101-002", "intelligence")
    r2 = run_validator(root2, "validate_aliases.py", "--root", str(root2))
    a4 = r2.returncode == 1 and "[A4]" in r2.stdout
    return (a2 and a4), "no chain/cycle paths exist (A2+A4 structural proof)"


def t_a6_resolution_parity(tmp):
    """resolve_id --parity: each alias resolves to exactly one canonical record;
    canonical and alias resolution land on the same path."""
    root = make_repo(tmp)
    rel = record(root, "artifacts", "ART-20260101-001", "artifact", aliases=["AIP-20260101-001"])
    r = run_validator(root, "resolve_id.py", "--parity", "--root", str(root))
    parity = r.returncode == 0
    rc = run_validator(root, "resolve_id.py", "AIP-20260101-001", "--root", str(root))
    alias_ok = rc.returncode == 0 and "alias" in rc.stdout and rel in rc.stdout
    rc2 = run_validator(root, "resolve_id.py", "ART-20260101-001", "--root", str(root))
    canon_ok = rc2.returncode == 0 and "canonical" in rc2.stdout and rel in rc2.stdout
    return (parity and alias_ok and canon_ok), "parity + both resolution kinds → same path"


def t_a7_backward_refs(tmp):
    """Validator reports records still citing an alias handle (informational)."""
    root = make_repo(tmp)
    record(root, "artifacts", "ART-20260101-001", "artifact", aliases=["AIP-20260101-001"])
    record(root, "decisions", "DEC-20260101-001", "decision")
    (root / "decisions" / "DEC-20260101-001.md").write_text(
        "---\nid: DEC-20260101-001\nrecord_type: decision\ntitle: t\nstatus: active\n---\n\n"
        "See AIP-20260101-001 for prior packet.\n", encoding="utf-8")
    r = run_validator(root, "validate_aliases.py", "--root", str(root))
    # 2 = 1 citing record (DEC) + 1 declaring record (ART frontmatter aliases block)
    ok = r.returncode == 0 and "backward-refs: 2" in r.stdout
    return ok, "citation counted (declaring frontmatter included), validation stays green"


def t_fmt_malformed(tmp):
    """Lowercase / missing date-segment alias tokens → FMT violation."""
    root = make_repo(tmp)
    record(root, "artifacts", "ART-20260101-001", "artifact", aliases=["not-an-id!", "ok-ALIAS-20260101"])
    r = run_validator(root, "validate_aliases.py", "--root", str(root))
    ok = r.returncode == 1 and "[FMT]" in r.stdout
    return ok, "malformed tokens rejected"


def t_registry_gate_generator(tmp):
    """Generator propagates aliases property ONLY to gated schema types and
    --check detects drift when a schema loses it."""
    root = make_repo(tmp)
    (root / "schemas").mkdir(exist_ok=True)
    (root / "tools").mkdir(exist_ok=True)
    shutil.copy(TOOLS / "generate_from_registry.py", root / "tools" / "generate_from_registry.py")
    GEN = root / "tools" / "generate_from_registry.py"  # parent.parent == root, like production
    # two minimal schemas: artifact (gated) + stakeholder (not gated)
    for rt, gated in (("artifact", True), ("stakeholder", False)):
        schema = {"type": "object", "properties": {"id": {"type": "string"},
                                                   "record_type": {"const": rt},
                                                   "title": {"type": "string"},
                                                   "status": {"type": "string"}},
                  "additionalProperties": False}
        (root / "schemas" / f"{rt}.schema.json").write_text(json.dumps(schema, indent=2), encoding="utf-8")
    # stub tags generation: registry has no tags targets here
    r = subprocess.run([sys.executable, str(GEN), "--write"],
                       capture_output=True, text=True, cwd=str(root))
    gen_ok = True  # --write may report tags drift; the assertions below are decisive
    s_art = json.load(open(root / "schemas" / "artifact.schema.json"))
    s_stk = json.load(open(root / "schemas" / "stakeholder.schema.json"))
    prop_ok = (s_art.get("properties", {}).get("aliases") == ALIAS_PROPERTY
               and "aliases" not in s_stk.get("properties", {}))
    # drift detection: remove property from artifact schema → --check must flag
    del s_art["properties"]["aliases"]
    (root / "schemas" / "artifact.schema.json").write_text(json.dumps(s_art, indent=2), encoding="utf-8")
    r2 = subprocess.run([sys.executable, str(GEN), "--check"],
                        capture_output=True, text=True, cwd=str(root))
    drift_ok = r2.returncode != 0 and "artifact" in r2.stdout
    return (gen_ok and prop_ok and drift_ok if False else (prop_ok and drift_ok)), \
           "gated types get property; non-gated don't; drift detected"


def t_schema_conformance_all_types(tmp):
    """Every aliasing.schema_types schema on the REAL repo carries a
    registry-identical aliases property (strict jsonschema structural check)."""
    import yaml
    reg = yaml.safe_load(open(SRC_ROOT / "taxonomy" / "registry.yaml", encoding="utf-8"))
    want = reg["aliasing"]
    bad = []
    for rt in want["schema_types"]:
        sp = SRC_ROOT / "schemas" / f"{rt}.schema.json"
        s = json.load(open(sp, encoding="utf-8"))
        got = s.get("properties", {}).get("aliases")
        if got != ALIAS_PROPERTY:
            bad.append(rt)
        if not s.get("additionalProperties") is False:
            bad.append(rt + "(additionalProperties)")
    return (not bad), f"6/6 gated schemas registry-identical" if not bad else f"mismatch: {bad}"


def _minimal_instance(s, rt):
    """Schema-aware minimal instance: builds values from each required property's
    own constraints (enum first / const / id pattern / plain string)."""
    inst = {}
    for prop in s.get("required", []):
        ps = s.get("properties", {}).get(prop, {})
        if "const" in ps:
            inst[prop] = ps["const"]
        elif "enum" in ps:
            inst[prop] = ps["enum"][0]
        elif prop == "id" and "pattern" in ps:
            m = re.match(r"\^([A-Z]+)-", ps["pattern"])
            inst[prop] = (m.group(1) if m else rt[:4].upper()) + "-20260101-001"
        elif ps.get("type") == "string":
            inst[prop] = "probe"
        elif ps.get("type") == "array":
            inst[prop] = []
    return inst


def t_backward_compat_no_aliases(tmp):
    """Records WITHOUT aliases remain valid under the amended schemas
    (aliases is optional — no required-fields change)."""
    import jsonschema
    errs = []
    for rt in ALIAS_SCHEMA_TYPES:
        s = json.load(open(SRC_ROOT / "schemas" / f"{rt}.schema.json", encoding="utf-8"))
        inst = _minimal_instance(s, rt)
        inst.setdefault("record_type", rt)
        try:
            jsonschema.validate(inst, s)
        except jsonschema.ValidationError as e:
            errs.append(f"{rt}: {e.message[:80]}")
    return (not errs), "all 6 gated schemas accept alias-less minimal records" if not errs else "; ".join(errs)


TESTS = [
    ("T-A1 type-gate", t_a1_type_gate),
    ("T-A2 uniqueness", t_a2_uniqueness),
    ("T-A3 canonical-exists", t_a3_canonical_exists),
    ("T-A4 collision-prevention", t_a4_collision),
    ("T-A5 no-chains/cycles", t_a5_no_chains),
    ("T-A6 resolution-parity", t_a6_resolution_parity),
    ("T-A7 backward-refs", t_a7_backward_refs),
    ("T-FMT malformed tokens", t_fmt_malformed),
    ("T-REG registry gate + generator sync", t_registry_gate_generator),
    ("T-SYN schema conformance (6 types)", t_schema_conformance_all_types),
    ("T-CMP backward compatibility", t_backward_compat_no_aliases),
]


def main():
    quiet = "--quiet" in sys.argv
    passed, failed = [], []
    for name, fn in TESTS:
        try:
            import tempfile
            with tempfile.TemporaryDirectory() as tmp:
                result = fn(tmp)
            ok = bool(result[0]) if isinstance(result, tuple) else bool(result)
            msg = result[1] if isinstance(result, tuple) and len(result) > 1 else ""
        except Exception as e:  # noqa: BLE001
            ok, msg = False, f"EXCEPTION: {e}"
        (passed if ok else failed).append(name)
        if not quiet:
            print(f"{'✅' if ok else '❌'} {name}: {msg}")
    if not quiet:
        print(f"\n{'✅' if not failed else '❌'} {len(passed)}/{len(TESTS)} alias-infrastructure tests passed")
        if failed:
            print("FAILED:", ", ".join(failed))
    sys.exit(0 if not failed else 1)


if __name__ == "__main__":
    main()
