#!/usr/bin/env python3
"""
CognitiveOS Validator — CVS Error Rate (CVS ER) Gate
=====================================================
Validates records against schemas using CVS 5-criteria scoring methodology.
Produces an Error Rate (ER) metric for conformance measurement.

CVS ER Mapping (5 criteria → 5 validation dimensions):
  Authority     → Schema conformance: record_type valid, matches known schema
  Traceability → Required field presence: all required fields present and non-null
  Recency      → Timestamp validity: created_at/updated_at present, valid ISO format
  Consistency  → Enum consistency: field values match schema enum definitions
  Completeness → Content quality: summary/strategic_significance are meaningful (not placeholder)

Error Rate = (failed checks / total checks) × 100

Per-record CVS tier:
  T1 (Verified)      — 0 errors, all 5 criteria pass
  T2 (Partially OK) — 1-2 P1 warnings, no P0 errors
  T3 (Interpretation)— Content quality issues only, structurally sound
  T6 (Rejected)     — 3+ errors or any P0 (missing required, invalid type)

Severity:
  P0 (blocking)  — Missing required field, invalid record_type, malformed YAML
  P1 (warning)   — Null optional field, enum mismatch, short content
  P2 (advisory)  — Heuristic content detected, quality suggestions

Usage:
  python3 tools/validate.py --file <path> --quiet    # Single file, minimal output (pre-commit hook)
  python3 tools/validate.py --file <path>            # Single file, full output
  python3 tools/validate.py                          # Full workspace ER report
  python3 tools/validate.py --full                    # Full workspace ER report (explicit)
"""

import argparse, sys, os, re, yaml, json
from pathlib import Path
from datetime import datetime
from collections import Counter, defaultdict

WS = Path(__file__).resolve().parent.parent
SCHEMAS_DIR = WS / "schemas"
SKIP_DIRS = {'.git', 'schemas', 'templates', 'tools', 'references', 'cron-output', 'osint-stack', 'indexes'}

# ─── Schema loading ───

_schema_cache = {}

def load_schema(record_type):
    """Load type-specific schema, fall back to master schema."""
    if record_type in _schema_cache:
        return _schema_cache[record_type]
    
    # Try type-specific schema first
    schema_path = SCHEMAS_DIR / f"{record_type}.schema.json"
    if schema_path.exists():
        with open(schema_path) as f:
            schema = json.load(f)
        _schema_cache[record_type] = schema
        return schema
    
    # Fall back to master schema
    master_path = SCHEMAS_DIR / "strategic-memory.schema.json"
    if master_path.exists():
        with open(master_path) as f:
            schema = json.load(f)
        _schema_cache[record_type] = schema
        return schema
    
    return None

def load_master_schema():
    """Load the master schema for record_type validation."""
    master_path = SCHEMAS_DIR / "strategic-memory.schema.json"
    if master_path.exists():
        with open(master_path) as f:
            return json.load(f)
    return None

# ─── CVS ER Validation ───

class ValidationResult:
    """Holds validation results for a single record with CVS ER scoring."""
    
    def __init__(self, filepath, record_id, record_type):
        self.filepath = filepath
        self.record_id = record_id
        self.record_type = record_type
        self.errors = []      # P0 — blocking
        self.warnings = []    # P1 — warning
        self.advisories = []  # P2 — advisory
        
        # CVS 5-criteria scores (0 = fail, 1 = partial, 2 = pass)
        self.authority = 0       # Schema conformance
        self.traceability = 0    # Required field presence
        self.recency = 0         # Timestamp validity
        self.consistency = 0     # Enum consistency
        self.completeness = 0    # Content quality
        
    @property
    def cvs_score(self):
        """Total CVS score (0-10)."""
        return self.authority + self.traceability + self.recency + self.consistency + self.completeness
    
    @property
    def error_count(self):
        return len(self.errors)
    
    @property
    def warning_count(self):
        return len(self.warnings)
    
    @property
    def advisory_count(self):
        return len(self.advisories)
    
    @property
    def total_checks(self):
        """Total validation checks performed (5 criteria × sub-checks)."""
        return 5
    
    @property
    def failed_checks(self):
        """Number of criteria that failed (score = 0)."""
        return sum(1 for s in [self.authority, self.traceability, self.recency, 
                               self.consistency, self.completeness] if s == 0)
    
    @property
    def error_rate(self):
        """CVS ER = (failed checks / total checks) × 100."""
        if self.total_checks == 0:
            return 0.0
        return (self.failed_checks / self.total_checks) * 100
    
    @property
    def tier(self):
        """CVS tier assignment based on error count and severity."""
        if self.error_count > 0:
            return "T6"
        if self.failed_checks == 0 and self.warning_count == 0:
            return "T1"
        if self.failed_checks <= 2:
            return "T2"
        if self.failed_checks <= 3 and self.error_count == 0:
            return "T3"
        return "T6"
    
    @property
    def passed(self):
        """True if no P0 errors (commit can proceed)."""
        return self.error_count == 0


def validate_record(filepath):
    """Validate a single record file against its schema. Returns ValidationResult."""
    filepath = Path(filepath)
    
    # Parse YAML frontmatter
    try:
        content = filepath.read_text(encoding='utf-8')
    except Exception as e:
        result = ValidationResult(str(filepath), "?", "?")
        result.errors.append(f"P0: Cannot read file: {e}")
        result.authority = 0
        return result
    
    if not content.strip().startswith('---'):
        result = ValidationResult(str(filepath), "?", "?")
        result.errors.append("P0: No YAML frontmatter found (must start with ---)")
        result.authority = 0
        return result
    
    m = re.match(r'^---\n(.*?)\n---\n?(.*)$', content, re.DOTALL)
    if not m:
        result = ValidationResult(str(filepath), "?", "?")
        result.errors.append("P0: Malformed YAML frontmatter (missing closing ---)")
        result.authority = 0
        return result
    
    try:
        fm = yaml.safe_load(m.group(1))
        if not isinstance(fm, dict):
            raise ValueError("Frontmatter is not a dictionary")
    except yaml.YAMLError as e:
        result = ValidationResult(str(filepath), "?", "?")
        result.errors.append(f"P0: YAML parse error: {e}")
        result.authority = 0
        return result
    except ValueError as e:
        result = ValidationResult(str(filepath), "?", "?")
        result.errors.append(f"P0: {e}")
        result.authority = 0
        return result
    
    record_id = fm.get('id', '?')
    record_type = fm.get('record_type', '?')
    
    result = ValidationResult(str(filepath), record_id, record_type)
    
    # ─── Criterion 1: Authority (Schema conformance) ───
    master_schema = load_master_schema()
    valid_types = master_schema["properties"]["record_type"]["enum"] if master_schema else []
    
    if record_type == '?':
        result.errors.append("P0: Missing 'record_type' field")
        result.authority = 0
    elif valid_types and record_type not in valid_types:
        result.errors.append(f"P0: Invalid record_type '{record_type}' — must be one of {valid_types}")
        result.authority = 0
    else:
        type_schema = load_schema(record_type)
        if type_schema is None:
            result.warnings.append(f"P1: No schema found for type '{record_type}' — using master only")
            result.authority = 1
        else:
            result.authority = 2
    
    # ─── Criterion 2: Traceability (Required field presence) ───
    type_schema = load_schema(record_type) if record_type != '?' else None
    if type_schema:
        required_fields = type_schema.get("required", [])
    elif master_schema:
        required_fields = master_schema.get("required", [])
    else:
        required_fields = []
    
    missing_required = []
    null_required = []
    
    for field in required_fields:
        if field not in fm:
            missing_required.append(field)
        elif fm[field] is None:
            null_required.append(field)
    
    if missing_required:
        result.errors.append(f"P0: Missing required fields: {', '.join(missing_required)}")
        result.traceability = 0
    elif null_required:
        result.errors.append(f"P0: Required fields are null: {', '.join(null_required)}")
        result.traceability = 0
    else:
        # Check universal base fields presence (17 fields)
        universal = ['id', 'record_type', 'title', 'created_at', 'updated_at', 'owner',
                     'status', 'priority', 'sensitivity', 'lifecycle_state', 'confidence',
                     'tags', 'source', 'summary', 'strategic_significance', 
                     'mission_alignment', 'related_records']
        null_universal = [f for f in universal if f in fm and fm[f] is None]
        if null_universal:
            result.warnings.append(f"P1: Universal fields are null: {', '.join(null_universal)}")
            result.traceability = 1
        else:
            result.traceability = 2
    
    # ─── Criterion 3: Recency (Timestamp validity) ───
    created_at = fm.get('created_at')
    updated_at = fm.get('updated_at')
    ts_issues = []
    
    for ts_field, ts_val in [('created_at', created_at), ('updated_at', updated_at)]:
        if ts_val is None:
            ts_issues.append(f"{ts_field} is null")
        elif isinstance(ts_val, datetime):
            pass  # YAML auto-parsed ISO datetime — valid
        elif not isinstance(ts_val, str):
            ts_issues.append(f"{ts_field} is not a string (got {type(ts_val).__name__})")
        elif not re.match(r'\d{4}-\d{2}-\d{2}', str(ts_val)):
            ts_issues.append(f"{ts_field} has invalid format: '{ts_val}'")
    
    if ts_issues:
        result.warnings.append(f"P1: Timestamp issues: {'; '.join(ts_issues)}")
        result.recency = 1
    else:
        result.recency = 2
    
    # ─── Criterion 4: Consistency (Enum validation) ───
    if type_schema:
        props = type_schema.get("properties", {})
        enum_mismatches = []
        
        for field, prop in props.items():
            if field not in fm or fm[field] is None:
                continue
            if "enum" in prop:
                value = fm[field]
                if value not in prop["enum"]:
                    enum_mismatches.append(f"{field}='{value}' (valid: {prop['enum'][:5]}...)")
        
        if enum_mismatches:
            result.warnings.append(f"P1: Enum mismatches: {'; '.join(enum_mismatches)}")
            result.consistency = 1
        else:
            result.consistency = 2
    else:
        # No type schema — can't validate enums
        result.consistency = 1
    
    # ─── Criterion 5: Completeness (Content quality) ───
    quality_issues = []
    
    summary = fm.get('summary')
    if summary is not None:
        summary_str = str(summary).strip()
        if len(summary_str) < 20:
            quality_issues.append(f"summary too short ({len(summary_str)} chars)")
        elif summary_str.startswith("See record body"):
            quality_issues.append("summary is placeholder ('See record body')")
    
    sig = fm.get('strategic_significance')
    if sig is not None:
        sig_str = str(sig).strip()
        if len(sig_str) < 15:
            quality_issues.append(f"strategic_significance too short ({len(sig_str)} chars)")
    
    confidence = fm.get('confidence')
    if confidence is not None and str(confidence).lower() not in ('high', 'medium', 'low'):
        quality_issues.append(f"confidence value unusual: '{confidence}'")
    
    # Check for heuristic-derived content markers
    body = m.group(2) if m else ""
    
    if quality_issues:
        result.advisories.append(f"P2: Content quality: {'; '.join(quality_issues)}")
        result.completeness = 1
    else:
        result.completeness = 2
    
    return result


# ─── Workspace-wide ER report ───

def workspace_er_report():
    """Run validation across all records and produce CVS ER report."""
    results = []
    
    for root, dirs, files in os.walk(WS):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for f in files:
            if not f.endswith('.md'):
                continue
            fp = Path(root) / f
            # Quick check: only validate files with frontmatter
            try:
                content = fp.read_text(encoding='utf-8')
                if not content.strip().startswith('---'):
                    continue
            except:
                continue
            result = validate_record(fp)
            results.append(result)
    
    return results


def print_er_report(results):
    """Print full CVS ER report."""
    total = len(results)
    if total == 0:
        print("No records found to validate.")
        return
    
    passed = sum(1 for r in results if r.passed)
    failed = total - passed
    
    # Tier distribution
    tier_counts = Counter(r.tier for r in results)
    
    # Per-criterion scores
    criterion_scores = {
        'Authority': [r.authority for r in results],
        'Traceability': [r.traceability for r in results],
        'Recency': [r.recency for r in results],
        'Consistency': [r.consistency for r in results],
        'Completeness': [r.completeness for r in results],
    }
    
    # Aggregate ER
    total_checks = total * 5
    total_failed = sum(r.failed_checks for r in results)
    aggregate_er = (total_failed / total_checks) * 100 if total_checks > 0 else 0
    
    # Per-record-type ER
    type_results = defaultdict(list)
    for r in results:
        type_results[r.record_type].append(r)
    
    print("=" * 80)
    print("CVS ER REPORT — CognitiveOS Validation Score & Error Rate")
    print("=" * 80)
    print(f"\nRecords validated: {total}")
    print(f"Passed (no P0): {passed} ({passed/total*100:.1f}%)")
    print(f"Failed (P0 errors): {failed} ({failed/total*100:.1f}%)")
    
    print(f"\n─── CVS Tier Distribution ───")
    for tier in ['T1', 'T2', 'T3', 'T6']:
        count = tier_counts.get(tier, 0)
        pct = count / total * 100
        bar = '█' * int(pct / 2)
        print(f"  {tier} ({'Verified' if tier == 'T1' else 'Partial' if tier == 'T2' else 'Interpretation' if tier == 'T3' else 'Rejected'}): {count:4d} ({pct:5.1f}%) {bar}")
    
    print(f"\n─── CVS 5-Criteria Breakdown ───")
    for name, scores in criterion_scores.items():
        avg = sum(scores) / len(scores) if scores else 0
        pass_count = sum(1 for s in scores if s == 2)
        partial_count = sum(1 for s in scores if s == 1)
        fail_count = sum(1 for s in scores if s == 0)
        print(f"  {name:15s}: avg={avg:.2f}/2 | PASS={pass_count} PARTIAL={partial_count} FAIL={fail_count}")
    
    print(f"\n─── Aggregate Error Rate ───")
    print(f"  Total checks: {total_checks}")
    print(f"  Failed checks: {total_failed}")
    print(f"  CVS ER: {aggregate_er:.2f}%")
    print(f"  Conformance: {100 - aggregate_er:.2f}%")
    
    print(f"\n─── Per Record Type ───")
    for rtype in sorted(type_results.keys()):
        type_res = type_results[rtype]
        type_total = len(type_res)
        type_passed = sum(1 for r in type_res if r.passed)
        type_failed_checks = sum(r.failed_checks for r in type_res)
        type_total_checks = type_total * 5
        type_er = (type_failed_checks / type_total_checks) * 100 if type_total_checks > 0 else 0
        avg_score = sum(r.cvs_score for r in type_res) / type_total
        print(f"  {rtype:20s}: {type_total:4d} records | ER={type_er:5.1f}% | avg CVS={avg_score:.1f}/10 | P0={type_total - type_passed}")
    
    # Show P0 errors
    p0_records = [r for r in results if not r.passed]
    if p0_records:
        print(f"\n─── P0 Errors (blocking) ───")
        for r in p0_records[:20]:
            for err in r.errors:
                print(f"  ❌ [{r.record_id}] {err}")
        if len(p0_records) > 20:
            print(f"  ... and {len(p0_records) - 20} more records with P0 errors")
    
    # Show P1 warnings summary
    p1_records = [r for r in results if r.warnings]
    if p1_records:
        print(f"\n─── P1 Warnings ({len(p1_records)} records) ───")
        warning_types = Counter()
        for r in p1_records:
            for w in r.warnings:
                # Extract warning category
                if "null" in w.lower():
                    warning_types["Null fields"] += 1
                elif "enum" in w.lower():
                    warning_types["Enum mismatch"] += 1
                elif "timestamp" in w.lower():
                    warning_types["Timestamp issue"] += 1
                elif "schema" in w.lower():
                    warning_types["Schema missing"] += 1
                else:
                    warning_types["Other"] += 1
        for wtype, count in warning_types.most_common():
            print(f"  {wtype:20s}: {count}")
    
    # Show P2 advisories summary
    p2_records = [r for r in results if r.advisories]
    if p2_records:
        print(f"\n─── P2 Advisories ({len(p2_records)} records) ───")
        adv_types = Counter()
        for r in p2_records:
            for a in r.advisories:
                if "too short" in a:
                    adv_types["Short content"] += 1
                elif "placeholder" in a:
                    adv_types["Placeholder content"] += 1
                elif "unusual" in a:
                    adv_types["Unusual value"] += 1
                else:
                    adv_types["Other"] += 1
        for atype, count in adv_types.most_common():
            print(f"  {atype:20s}: {count}")
    
    print(f"\n{'='*80}")
    if failed > 0:
        print(f"🚫 {failed} record(s) with P0 errors — commit would be BLOCKED")
    else:
        print(f"✅ All {total} records pass P0 validation")
    print(f"   CVS ER: {aggregate_er:.2f}% | Conformance: {100 - aggregate_er:.2f}%")
    print(f"{'='*80}")


# ─── CLI ───

def main():
    parser = argparse.ArgumentParser(description='CognitiveOS CVS ER Validator')
    parser.add_argument('--file', metavar='PATH', help='Validate a single file')
    parser.add_argument('--quiet', action='store_true', help='Minimal output (for pre-commit hook)')
    parser.add_argument('--full', action='store_true', help='Full workspace ER report')
    args = parser.parse_args()
    
    # Single file mode (pre-commit hook)
    if args.file:
        result = validate_record(args.file)
        
        if args.quiet:
            # Minimal output for pre-commit hook
            if not result.passed:
                for err in result.errors:
                    print(err, file=sys.stderr)
                sys.exit(1)
            else:
                sys.exit(0)
        else:
            # Full single-file output
            print(f"File: {result.filepath}")
            print(f"Record ID: {result.record_id}")
            print(f"Record Type: {result.record_type}")
            print(f"CVS Tier: {result.tier}")
            print(f"CVS Score: {result.cvs_score}/10")
            print(f"Error Rate: {result.error_rate:.0f}%")
            print(f"Passed: {'✅' if result.passed else '❌'}")
            print()
            print(f"Criteria breakdown:")
            print(f"  Authority (schema):      {result.authority}/2")
            print(f"  Traceability (required):  {result.traceability}/2")
            print(f"  Recency (timestamps):     {result.recency}/2")
            print(f"  Consistency (enums):      {result.consistency}/2")
            print(f"  Completeness (quality):   {result.completeness}/2")
            
            if result.errors:
                print(f"\nErrors (P0):")
                for e in result.errors:
                    print(f"  ❌ {e}")
            if result.warnings:
                print(f"\nWarnings (P1):")
                for w in result.warnings:
                    print(f"  ⚠️  {w}")
            if result.advisories:
                print(f"\nAdvisories (P2):")
                for a in result.advisories:
                    print(f"  ℹ️  {a}")
            
            sys.exit(0 if result.passed else 1)
    
    # Full workspace mode
    results = workspace_er_report()
    print_er_report(results)
    sys.exit(0 if all(r.passed for r in results) else 1)


if __name__ == '__main__':
    main()
