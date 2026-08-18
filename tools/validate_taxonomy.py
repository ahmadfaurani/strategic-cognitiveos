#!/usr/bin/env python3
"""
Taxonomy Validator — Pre-commit hook for CognitiveOS tag compliance.
Validates that all tag namespace prefixes and values in record frontmatter
match the controlled vocabulary defined in taxonomy/tags.yaml.

Usage:
    python3 tools/validate_taxonomy.py [file1] [file2] ...
    
If no files provided, scans all .md files in record directories.

Exit codes:
    0 — all tags valid
    1 — one or more tags invalid
    2 — taxonomy file error
"""

import os
import re
import sys
import yaml
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
TAGS_FILE = REPO_ROOT / "taxonomy" / "tags.yaml"

# Directories that contain CognitiveOS records with frontmatter
RECORD_DIRS = [
    "actions", "decisions", "initiatives", "risks", "intelligence",
    "engagements", "commitments", "outcomes", "stakeholders",
    "organizations", "artifacts", "assessments", "briefings",
    "documents", "drafts", "lessons", "opportunities",
]

# Directories to skip (not record directories)
SKIP_DIRS = {".git", "taxonomy", "schemas", "tools", "templates", "osint-stack", "memory", "logs", "archive", "portfolio", "products", "projects", "profiles", "strategies", "strategy", "03-VERIFICATION", "05-TOOLS-AND-AUTOMATION", "governance", "indexes", "cognitiveos-development-plan-v2.md"}


def load_taxonomy():
    """Load and parse tags.yaml into namespace → set of values mapping."""
    with open(TAGS_FILE) as f:
        data = yaml.safe_load(f)
    
    namespaces = {}
    for ns_name, ns_def in data.get("namespaces", {}).items():
        values = set()
        for v in ns_def.get("values", []) or ns_def.get("known_values", []):
            values.add(v)
        # Store the pattern if defined (for slug-based namespaces)
        pattern = ns_def.get("pattern")
        namespaces[ns_name] = {
            "values": values,
            "pattern": pattern,
            "description": ns_def.get("description", "")
        }
    return namespaces


def extract_tags_from_file(filepath):
    """Extract tags from YAML frontmatter of a markdown file."""
    with open(filepath, encoding="utf-8") as f:
        content = f.read()
    
    # Check for frontmatter
    if not content.startswith("---"):
        return []
    
    # Find the closing ---
    parts = content.split("---", 2)
    if len(parts) < 3:
        return []
    
    frontmatter = parts[1]
    
    try:
        fm_data = yaml.safe_load(frontmatter)
    except yaml.YAMLError:
        return []
    
    if not fm_data or "tags" not in fm_data:
        return []
    
    tags = fm_data["tags"]
    if not isinstance(tags, list):
        return []
    
    return tags


def validate_tag(tag, namespaces):
    """Validate a single tag against the taxonomy. Returns (is_valid, error_msg)."""
    if "/" not in tag:
        return False, f"tag '{tag}' has no namespace prefix (expected 'namespace/value' format)"
    
    prefix, value = tag.split("/", 1)
    
    if prefix not in namespaces:
        return False, f"tag '{tag}' uses unknown namespace '{prefix}'"
    
    ns = namespaces[prefix]
    
    # If namespace has a pattern (slug-based), accept any slug value
    if ns["pattern"]:
        # For pattern-based namespaces, we accept known_values but also
        # accept any kebab-case slug (since pattern says <slug>)
        if re.match(r"^[a-z0-9][a-z0-9_-]*$", value):
            return True, None
        else:
            return False, f"tag '{tag}' value '{value}' is not a valid kebab-case slug"
    
    # For value-list namespaces, check against known values
    if value in ns["values"]:
        return True, None
    
    return False, f"tag '{tag}' value '{value}' not in namespace '{prefix}' (valid: {sorted(ns['values'])})"


def validate_file(filepath, namespaces):
    """Validate all tags in a single file. Returns list of (file, tag, error)."""
    errors = []
    tags = extract_tags_from_file(filepath)
    for tag in tags:
        if not isinstance(tag, str):
            continue
        is_valid, err = validate_tag(tag, namespaces)
        if not is_valid:
            errors.append((str(filepath), tag, err))
    return errors


def main():
    # Load taxonomy
    try:
        namespaces = load_taxonomy()
    except Exception as e:
        print(f"❌ Failed to load taxonomy: {e}", file=sys.stderr)
        sys.exit(2)
    
    # Determine files to check
    if len(sys.argv) > 1:
        # Files passed as arguments (from pre-commit hook)
        files = [Path(f) for f in sys.argv[1:] if f.endswith(".md")]
    else:
        # Scan all record directories
        files = []
        for d in RECORD_DIRS:
            dirpath = REPO_ROOT / d
            if dirpath.exists():
                files.extend(dirpath.rglob("*.md"))
    
    if not files:
        print("No .md files to validate.")
        sys.exit(0)
    
    all_errors = []
    files_checked = 0
    
    for filepath in files:
        # Skip files in skip directories
        rel = filepath.relative_to(REPO_ROOT) if filepath.is_absolute() else filepath
        if any(str(rel).startswith(s + "/") or str(rel).startswith(s + "\\") for s in SKIP_DIRS):
            continue
        if not filepath.exists():
            continue
        
        files_checked += 1
        errors = validate_file(filepath, namespaces)
        all_errors.extend(errors)
    
    if all_errors:
        print(f"❌ Taxonomy validation failed: {len(all_errors)} violation(s) in {files_checked} files checked\n")
        for filepath, tag, err in all_errors:
            print(f"  {filepath}")
            print(f"    tag: {tag}")
            print(f"    error: {err}")
            print()
        sys.exit(1)
    else:
        print(f"✅ Taxonomy validation passed: {files_checked} files checked, 0 violations")
        sys.exit(0)


if __name__ == "__main__":
    main()
