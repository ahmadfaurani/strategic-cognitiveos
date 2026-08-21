#!/usr/bin/env python3
"""
CognitiveOS Pair-Lock Invariant Validator
==========================================
Validates paired_sops reciprocity and mandatory pair integrity.

Checks:
  1. Every paired_sops reference points to a record that exists
  2. Every paired_sops reference is reciprocated
  3. Mandatory pairs (declared in pair-registry.yaml) are present and intact
  4. Mandatory pair metadata cannot be silently removed from both sides

Usage:
  python3 tools/validate_pair_lock.py            # Full workspace check
  python3 tools/validate_pair_lock.py --quiet     # Minimal output (pre-commit hook)
  python3 tools/validate_pair_lock.py --staged   # Only check staged files
"""

import argparse
import sys
import re
import yaml
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PAIR_REGISTRY = REPO_ROOT / "governance" / "pair-registry.yaml"

# Directories to scan for paired_sops fields
SCAN_DIRS = ["governance"]


def extract_frontmatter(filepath):
    """Extract YAML frontmatter from a markdown file."""
    try:
        with open(filepath, encoding="utf-8") as f:
            content = f.read()
    except (IOError, OSError):
        return {}
    m = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if m:
        try:
            return yaml.safe_load(m.group(1)) or {}
        except yaml.YAMLError:
            return {}
    return {}


def build_pair_index():
    """Build index of all records that have paired_sops fields.
    Returns: {record_id: {filepath, paired_sops: [ids]}}
    """
    index = {}
    for scan_dir in SCAN_DIRS:
        dirpath = REPO_ROOT / scan_dir
        if not dirpath.exists():
            continue
        for f in dirpath.glob("*.md"):
            data = extract_frontmatter(f)
            record_id = data.get("id", "")
            paired_sops = data.get("paired_sops", [])
            if record_id and paired_sops:
                if not isinstance(paired_sops, list):
                    paired_sops = [paired_sops]
                index[record_id] = {
                    "filepath": str(f.relative_to(REPO_ROOT)),
                    "paired_sops": paired_sops,
                }
    return index


def load_pair_registry():
    """Load mandatory pairs from governance/pair-registry.yaml.
    Returns: list of {pair: [id_a, id_b], type, authority} or empty list if no registry.
    """
    if not PAIR_REGISTRY.exists():
        return []
    try:
        data = yaml.safe_load(PAIR_REGISTRY.read_text(encoding="utf-8"))
        if not data:
            return []
        return data.get("mandatory_pairs", [])
    except (yaml.YAMLError, IOError):
        return []


def validate_reciprocity(index):
    """Check that every paired_sops reference is reciprocated.
    Returns: list of error strings.
    """
    errors = []
    for record_id, info in sorted(index.items()):
        for paired_id in info["paired_sops"]:
            # Check 1: Referenced record exists
            if paired_id not in index:
                errors.append(
                    f"  ❌ {record_id} ({info['filepath']}) references "
                    f"{paired_id} but no record with that ID has paired_sops"
                )
                continue

            # Check 2: Reciprocal reference exists
            paired_info = index[paired_id]
            if record_id not in paired_info["paired_sops"]:
                errors.append(
                    f"  ❌ Asymmetric pairing: {record_id} references {paired_id} "
                    f"but {paired_id} does not reference back"
                )
    return errors


def validate_mandatory_pairs(index, registry):
    """Check that mandatory pairs declared in pair-registry.yaml are intact.
    Returns: list of error strings.
    """
    errors = []
    for entry in registry:
        pair = entry.get("pair", [])
        if len(pair) != 2:
            continue

        id_a, id_b = pair

        # Check: both records exist in the index (have paired_sops)
        if id_a not in index:
            errors.append(
                f"  ❌ Mandatory pair violation: {id_a} is declared in pair-registry.yaml "
                f"but has no paired_sops field (metadata may have been removed)"
            )
        elif id_b not in index[id_a]["paired_sops"]:
            errors.append(
                f"  ❌ Mandatory pair violation: {id_a} must declare {id_b} "
                f"in paired_sops (per pair-registry.yaml)"
            )

        if id_b not in index:
            errors.append(
                f"  ❌ Mandatory pair violation: {id_b} is declared in pair-registry.yaml "
                f"but has no paired_sops field (metadata may have been removed)"
            )
        elif id_a not in index[id_b]["paired_sops"]:
            errors.append(
                f"  ❌ Mandatory pair violation: {id_b} must declare {id_a} "
                f"in paired_sops (per pair-registry.yaml)"
            )

    return errors


def main():
    parser = argparse.ArgumentParser(description="Pair-Lock Invariant Validator")
    parser.add_argument("--quiet", action="store_true", help="Minimal output")
    args = parser.parse_args()

    index = build_pair_index()
    registry = load_pair_registry()

    # If no pairs exist and no registry, nothing to validate
    if not index and not registry:
        if not args.quiet:
            print("ℹ️  No paired_sops relationships found. Nothing to validate.")
        sys.exit(0)

    errors = []

    # Check reciprocity
    reciprocity_errors = validate_reciprocity(index)
    errors.extend(reciprocity_errors)

    # Check mandatory pairs from registry
    registry_errors = validate_mandatory_pairs(index, registry)
    errors.extend(registry_errors)

    if errors:
        print(f"❌ Pair-lock validation failed: {len(errors)} violation(s)")
        for e in errors:
            print(e)
        sys.exit(1)
    else:
        pair_count = sum(len(info["paired_sops"]) for info in index.values())
        mandatory_count = len(registry)
        if args.quiet:
            # Brief output for pre-commit hook
            print(f"✅ Pair-lock: {len(index)} record(s), {pair_count} pairing(s), {mandatory_count} mandatory pair(s)")
        else:
            print(
                f"✅ Pair-lock validation passed: {len(index)} record(s), "
                f"{pair_count} pairing(s), {mandatory_count} mandatory pair(s)"
            )
        sys.exit(0)


if __name__ == "__main__":
    main()
