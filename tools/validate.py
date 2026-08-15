#!/usr/bin/env python3
"""
CognitiveOS Deterministic Validator
====================================
Validates all CognitiveOS records against their JSON schemas.

Usage:
    ./validate.py                    # Validate entire corpus
    ./validate.py --dir decisions    # Validate single directory
    ./validate.py --file decisions/DEC-20260628-001.md  # Validate single file
    ./validate.py --quiet            # Only show errors
    ./validate.py --json             # Machine-readable output

Exit codes:
    0 — All records valid
    1 — One or more records failed validation
    2 — Schema or configuration error
"""

import os
import sys
import re
import json
import argparse
import yaml
from pathlib import Path
from datetime import datetime, timezone

try:
    from jsonschema import Draft202012Validator, ValidationError
except ImportError:
    print("ERROR: jsonschema not installed. Run: pip install jsonschema pyyaml", file=sys.stderr)
    sys.exit(2)

# ─────────────────────────────────────────────────────────
# Configuration
# ─────────────────────────────────────────────────────────

BASE_DIR = Path(__file__).resolve().parent.parent
SCHEMAS_DIR = BASE_DIR / "schemas"
LOGS_DIR = BASE_DIR / "logs"

# Record type → directory mapping
TYPE_TO_DIR = {
    "decision": "decisions",
    "action": "actions",
    "commitment": "commitments",
    "stakeholder": "stakeholders",
    "initiative": "initiatives",
    "intelligence": "intelligence",
    "risk": "risks",
    "conversation": "engagements",
    "event": "engagements",
}

# Override: conversation records use CONV- prefix, events use EVT- prefix
# The engagements/ directory contains both conversation and event records
DIR_TO_TYPES = {
    "decisions": ["decision"],
    "actions": ["action"],
    "commitments": ["commitment"],
    "stakeholders": ["stakeholder"],
    "initiatives": ["initiative"],
    "intelligence": ["intelligence"],
    "risks": ["risk"],
    "engagements": ["conversation", "event"],
}


# ─────────────────────────────────────────────────────────
# Schema Loading
# ─────────────────────────────────────────────────────────

def load_schemas():
    """Load all JSON schemas from the schemas directory."""
    schemas = {}
    for f in sorted(SCHEMAS_DIR.glob("*.schema.json")):
        name = f.stem.replace(".schema", "")
        try:
            with open(f) as fh:
                schemas[name] = json.load(fh)
            # Compile validator for performance
            schemas[name + "__validator"] = Draft202012Validator(schemas[name])
        except json.JSONDecodeError as e:
            print(f"ERROR: Schema {f.name} has invalid JSON: {e}", file=sys.stderr)
            sys.exit(2)
    return schemas


# ─────────────────────────────────────────────────────────
# Record Parsing
# ─────────────────────────────────────────────────────────

def _coerce_yaml_types(obj):
    """Recursively coerce YAML date/datetime objects to ISO strings for schema compatibility.
    YAML safe_load parses unquoted dates as datetime.date/datetime objects.
    JSON Schema expects strings with format: date/date-time."""
    import datetime
    if isinstance(obj, datetime.datetime):
        return obj.isoformat()
    if isinstance(obj, datetime.date):
        return obj.isoformat()
    if isinstance(obj, dict):
        return {k: _coerce_yaml_types(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_coerce_yaml_types(v) for v in obj]
    return obj


def extract_frontmatter(content: str):
    """Extract YAML frontmatter from markdown file. Returns (frontmatter_dict, body_str) or (None, content)."""
    fm_match = re.match(r'^---\n(.*?)\n---\s*\n?(.*)', content, re.DOTALL)
    if not fm_match:
        return None, content
    
    try:
        fm = yaml.safe_load(fm_match.group(1))
        if not isinstance(fm, dict):
            return None, fm_match.group(2)
        # Coerce YAML date/datetime objects to ISO strings
        fm = _coerce_yaml_types(fm)
        return fm, fm_match.group(2)
    except yaml.YAMLError as e:
        return "PARSE_ERROR", str(e)


def get_record_files(directory: str = None, single_file: str = None):
    """Yield (filepath, directory_name) for all .md records."""
    if single_file:
        fpath = Path(single_file)
        if not fpath.is_absolute():
            fpath = BASE_DIR / single_file
        yield fpath, fpath.parent.name
        return
    
    if directory:
        dirs = [directory]
    else:
        dirs = list(DIR_TO_TYPES.keys())
    
    for d in dirs:
        dir_path = BASE_DIR / d
        if not dir_path.is_dir():
            continue
        for f in sorted(dir_path.glob("*.md")):
            yield f, d


# ─────────────────────────────────────────────────────────
# Validation
# ─────────────────────────────────────────────────────────

def validate_record(fm: dict, body: str, filepath: Path, dir_name: str, schemas: dict):
    """Validate a single record's frontmatter against its schema.
    Returns list of errors (empty if valid)."""
    errors = []
    rel_path = f"{dir_name}/{filepath.name}"
    
    # Get record_type
    record_type = fm.get("record_type", "")
    if not record_type:
        errors.append(f"{rel_path}: Missing 'record_type' field")
        return errors
    
    # Find schema
    schema = schemas.get(record_type)
    if not schema:
        errors.append(f"{rel_path}: No schema for record_type='{record_type}'")
        return errors
    
    validator = schemas.get(record_type + "__validator")
    if not validator:
        errors.append(f"{rel_path}: Schema '{record_type}' not compiled")
        return errors
    
    # Run JSON Schema validation
    for error in validator.iter_errors(fm):
        # Make error path readable
        path = ".".join(str(p) for p in error.absolute_path) or "(root)"
        errors.append(f"{rel_path}: Schema violation at '{path}': {error.message}")
    
    # Additional checks beyond JSON Schema
    
    # Check: lifecycle_state should exist (warning, not error — for migration period)
    if "lifecycle_state" not in fm:
        errors.append(f"{rel_path}: WARNING — Missing 'lifecycle_state' field (add 'lifecycle_state: canonical' for existing records)")
    
    # Check: ID pattern matches directory expectation
    id_val = fm.get("id", "")
    expected_prefixes = {
        "decision": "DEC-",
        "action": "ACT-",
        "commitment": "COM-",
        "stakeholder": "STK-",
        "initiative": "INIT-",
        "intelligence": "INT-",
        "risk": "RSK-",
        "conversation": "CONV-",
        "event": "EVT-",
    }
    expected_prefix = expected_prefixes.get(record_type, "")
    if expected_prefix and id_val and not id_val.startswith(expected_prefix):
        errors.append(f"{rel_path}: ID '{id_val}' doesn't match expected prefix '{expected_prefix}' for record_type '{record_type}'")
    
    return errors


# ─────────────────────────────────────────────────────────
# Index Reconciliation
# ─────────────────────────────────────────────────────────

def check_indexes(schemas: dict):
    """Check that all record files appear in their respective indexes."""
    issues = []
    indexes_dir = BASE_DIR / "indexes"
    
    if not indexes_dir.is_dir():
        return [("INDEX: indexes/ directory not found")]
    
    # Map record types to index files
    type_to_index = {
        "decision": "decision-index.md",
        "action": None,  # No action index exists
        "commitment": "commitment-index.md",
        "stakeholder": "stakeholder-index.md",
        "initiative": "initiative-index.md",
        "risk": "risk-index.md",
        "conversation": "conversation-index.md",
        "event": None,
        "intelligence": None,
    }
    
    for record_type, index_file in type_to_index.items():
        if not index_file:
            continue
        
        index_path = indexes_dir / index_file
        if not index_path.exists():
            issues.append(f"INDEX: {index_file} not found")
            continue
        
        # Get all record IDs of this type
        expected_ids = set()
        dir_name = TYPE_TO_DIR.get(record_type, "")
        if not dir_name:
            continue
        
        dir_path = BASE_DIR / dir_name
        if not dir_path.is_dir():
            continue
        
        for f in dir_path.glob("*.md"):
            with open(f) as fh:
                content = fh.read()
            fm, _ = extract_frontmatter(content)
            if fm and isinstance(fm, dict) and fm.get("record_type") == record_type:
                rid = fm.get("id", "")
                if rid:
                    expected_ids.add(rid)
        
        # Read index file and extract IDs
        with open(index_path) as fh:
            index_content = fh.read()
        
        # Find IDs in index (look for ID patterns in table rows)
        id_pattern = re.compile(r'\b([A-Z]+-\d{8}-\d{3})\b')
        index_ids = set(id_pattern.findall(index_content))
        
        # Find mismatches
        missing_from_index = expected_ids - index_ids
        extra_in_index = index_ids - expected_ids
        
        for rid in sorted(missing_from_index):
            issues.append(f"INDEX: {rid} exists in {dir_name}/ but not in {index_file}")
        
        for rid in sorted(extra_in_index):
            issues.append(f"INDEX: {rid} in {index_file} but no file found in {dir_name}/")
    
    return issues


# ─────────────────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="CognitiveOS Deterministic Validator")
    parser.add_argument("--dir", help="Validate single directory")
    parser.add_argument("--file", help="Validate single file")
    parser.add_argument("--quiet", action="store_true", help="Only show errors")
    parser.add_argument("--json", action="store_true", help="Machine-readable JSON output")
    parser.add_argument("--no-index-check", action="store_true", help="Skip index reconciliation")
    args = parser.parse_args()
    
    schemas = load_schemas()
    
    total = 0
    passed = 0
    failed = 0
    warnings = 0
    all_errors = []
    
    for filepath, dir_name in get_record_files(args.dir, args.file):
        total += 1
        
        with open(filepath) as fh:
            content = fh.read()
        
        fm, body = extract_frontmatter(content)
        
        if fm == "PARSE_ERROR":
            failed += 1
            all_errors.append(f"{dir_name}/{filepath.name}: YAML parse error: {body}")
            continue
        
        if fm is None:
            failed += 1
            all_errors.append(f"{dir_name}/{filepath.name}: No YAML frontmatter found")
            continue
        
        errors = validate_record(fm, body, filepath, dir_name, schemas)
        
        if not errors:
            passed += 1
        else:
            has_errors = False
            for err in errors:
                if "WARNING" in err:
                    warnings += 1
                else:
                    has_errors = True
                    all_errors.append(err)
            
            if has_errors:
                failed += 1
            else:
                passed += 1  # Only warnings, no hard errors
    
    # Index reconciliation
    index_issues = []
    if not args.no_index_check and not args.file:
        index_issues = check_indexes(schemas)
    
    # Output
    if args.json:
        output = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "total": total,
            "passed": passed,
            "failed": failed,
            "warnings": warnings,
            "errors": all_errors,
            "index_issues": index_issues,
        }
        print(json.dumps(output, indent=2))
    else:
        print(f"╔══════════════════════════════════════╗")
        print(f"║  CognitiveOS Validator               ║")
        print(f"╚══════════════════════════════════════╝")
        print()
        print(f"  Records scanned: {total}")
        print(f"  ✅ Passed:       {passed}")
        print(f"  ❌ Failed:        {failed}")
        print(f"  ⚠️  Warnings:     {warnings}")
        print()
        
        if all_errors:
            print("═══ ERRORS ═══")
            for err in all_errors:
                if "WARNING" not in err:
                    print(f"  ❌ {err}")
            print()
        
        if not args.quiet:
            warning_errors = [e for e in all_errors if "WARNING" in e]
            if warning_errors:
                print("═══ WARNINGS ═══")
                for err in warning_errors[:20]:
                    print(f"  ⚠️  {err}")
                if len(warning_errors) > 20:
                    print(f"  ... and {len(warning_errors) - 20} more warnings")
                print()
        
        if index_issues:
            print("═══ INDEX RECONCILIATION ═══")
            for issue in index_issues:
                print(f"  🔍 {issue}")
            print()
        
        # Write to audit log
        LOGS_DIR.mkdir(parents=True, exist_ok=True)
        log_entry = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "total": total,
            "passed": passed,
            "failed": failed,
            "warnings": warnings,
            "index_issues": len(index_issues),
        }
        with open(LOGS_DIR / "validation.jsonl", "a") as fh:
            fh.write(json.dumps(log_entry) + "\n")
    
    # Exit code
    if failed > 0:
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
