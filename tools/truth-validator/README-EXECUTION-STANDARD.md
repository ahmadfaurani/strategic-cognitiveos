# Execution Standard Validation Tool

**Location:** `tools/truth-validator/execution-standard-check.sh`  
**Effective:** 2026-07-09  
**Authority:** DOCTRINE.md — Execution Standard

---

## Purpose

Automated validation script that enforces the **Execution Standard** from DOCTRINE.md:

- **Zero shortcuts** — No skipped or compressed workflow stages
- **Zero placeholders** — No TBD, dummy data, empty sections, unresolved variables
- **Deliverable readiness** — Outputs must be complete and operationally usable

---

## Quick Usage

```bash
# Validate a document before delivery
./tools/truth-validator/execution-standard-check.sh memory/my-brief.md

# Integrate into validation pipeline
./tools/truth-validator/execution-standard-check.sh <input.md> || exit 1
```

---

## What It Checks

### ❌ Violations (Exit Code 1)

| Pattern | Examples |
|---------|----------|
| **Placeholder text** | TBD, TODO, FIXME, XXX, "to be added", "insert here" |
| **Dummy/mock data** | "example content", "sample data", "placeholder", "dummy value" |
| **Template variables** | `{{variable}}`, `[...]`, `__placeholder__` |
| **Empty sections** | Headers with no substantive content in next 3 lines |
| **Unavailable markers** | "N/A", "not available", "will be provided" |

### ⚠️ Warnings (Exit Code 0, but flagged)

| Pattern | Examples |
|---------|----------|
| **Draft-state markers** | "draft", "preliminary", "initial version", "first pass", "rough draft" |
| **Incomplete indicators** | "step pending", "awaiting input", "waiting for", "incomplete" |

---

## Exit Codes

| Code | Meaning | Action |
|------|---------|--------|
| `0` | PASS (no violations) | Deliverable is ready |
| `0` (with warnings) | PASS with warnings | Review flagged content before delivery |
| `1` | FAIL (violations found) | **DO NOT DELIVER** — Fix all violations first |
| `2` | ERROR (script failure) | Check file path, permissions, syntax |

---

## Integration Points

### With CVS Validation Pipeline

```bash
# Full validation gate (CVS + Execution Standard)
./tools/truth-validator/validate.sh <input.md> || exit 1
./tools/truth-validator/execution-standard-check.sh <input.md> || exit 1
```

### With Heartbeat Daily Brief

```bash
# In daily-brief-generator workflow
./tools/truth-validator/execution-standard-check.sh memory/daily-brief-YYYY-MM-DD.md
if [[ $? -eq 1 ]]; then
    echo "Execution Standard violations — correcting before delivery"
    # Trigger correction workflow
    exit 1
fi
```

### With Dreaming CVS

```bash
# In dreaming-cvs-integration.sh
./tools/truth-validator/execution-standard-check.sh memory/dreaming/rem/YYYY-MM-DD.md
```

---

## Example Output

### ✅ PASS
```
=== Execution Standard Validation ===
Input: memory/my-brief.md
Date: 2026-07-09_10:45:00_UTC

--- Checking for Placeholders ---
--- Checking for Empty Sections ---
--- Checking for Draft-State Markers ---
--- Checking for Incomplete Workflow Indicators ---

=== Validation Summary ===
Violations: 0
Warnings: 0

✅ PASSED: No Execution Standard violations detected
```

### ❌ FAIL
```
=== Execution Standard Validation ===
Input: memory/draft-brief.md
Date: 2026-07-09_10:45:00_UTC

--- Checking for Placeholders ---
❌ VIOLATION: Placeholder pattern found: 'TBD'
15: Voter turnout projection: TBD (awaiting SPR data)
❌ VIOLATION: Placeholder pattern found: 'to be added'
23: Candidate list to be added

--- Checking for Empty Sections ---
  Empty section: Strategic Assessment (line 18)

=== Validation Summary ===
Violations: 3
Warnings: 0

❌ FAILED: Execution Standard violations detected
Action required: Remove all placeholders and empty sections before delivery
```

---

## Enforcement Policy

**Per DOCTRINE.md:**
- All outputs must pass this check before delivery
- Violations trigger immediate correction cycle
- Repeated violations escalate to doctrine compliance review

**Integration with OPERATIONAL-INTEGRATION.md:**
- Added to Pre-Output Checklist (Section 4.3)
- Violations logged to `memory/YYYY-MM-DD.md` with root cause
- Monthly review tracks violation frequency and patterns

---

## Limitations

- Does not verify factual accuracy (use `validate.sh` for CVS Tier 1/2/3 checks)
- Does not check for logical consistency or completeness of analysis
- Pattern-based detection may miss contextual placeholders
- Empty section detection uses heuristic (3-line lookahead)

**Recommendation:** Use as part of full validation pipeline, not standalone.

---

## Related Documents

- `DOCTRINE.md` — Execution Standard section
- `CVS-MANDATE.md` — Core Truth Validation requirements
- `validate.sh` — Main CVS validation script
- `workflows/OPERATIONAL-INTEGRATION.md` — Pre-output checklist integration

---

*This tool enforces doctrine — not guidance. Compliance is mandatory.*
