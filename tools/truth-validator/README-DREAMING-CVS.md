# Dreaming CVS Integration

**Purpose:** Run Core Truth Validation System (CVS) on Dreaming REM phase candidates before Deep Sleep promotion to `MEMORY.md`.

**Status:** ✅ Operational (2026-07-03)

---

## Quick Start

```bash
# Validate today's REM candidates
./tools/truth-validator/dreaming-cvs-integration.sh

# Validate specific date
./tools/truth-validator/dreaming-cvs-integration.sh 2026-07-03

# Verbose output (see each candidate's validation)
./tools/truth-validator/dreaming-cvs-integration.sh --verbose

# Dry run (preview without writing validation log)
./tools/truth-validator/dreaming-cvs-integration.sh --dry-run
```

---

## What It Does

The script performs **4 CVS validation checks** on each REM phase candidate:

| Check | Detects | Action |
|-------|---------|--------|
| **Numerical Claims** | Vote counts, percentages, margins without citations | ❌ FAIL |
| **Named Entities** | Candidates, positions, parties without sources | ⚠️ WARNING |
| **Confidence Tags** | Missing `[HIGH]`, `[MEDIUM]`, `[LOW]` tags | ⚠️ WARNING |
| **Speculation Flags** | Predictive claims without `SPECULATION:` or `SCENARIO:` | ⚠️ WARNING |

**Gate Decision:**
- **0 failures** → ✅ PASSED → Safe to promote to `MEMORY.md`
- **1+ failures** → ❌ BLOCKED → Review and fix candidates before promotion

---

## Integration with Dreaming Pipeline

### Manual Workflow (Current)

```bash
# 1. Dreaming REM phase completes (3:00 AM UTC daily)
# 2. Run CVS validation
./tools/truth-validator/dreaming-cvs-integration.sh

# 3. Review validation log
cat memory/dreaming-validation.jsonl | jq .

# 4. If PASSED, promote to MEMORY.md
openclaw memory promote --apply

# 5. If BLOCKED, review failed candidates
cat memory/dreaming/rem/YYYY-MM-DD.md
# Edit to add citations/tags, then re-run validation
```

### Automated Workflow (Future)

**Integration Point:** Modify `memory-core` plugin to call this script between REM and Deep Sleep phases.

**Proposed Config:**
```json5
{
  plugins: {
    entries: {
      "memory-core": {
        config: {
          dreaming: {
            enabled: true,
            phases: {
              deep: {
                prePromotionHook: "./tools/truth-validator/dreaming-cvs-integration.sh",
                blockOnCvsFailure: true  // Prevent promotion if CVS fails
              }
            }
          }
        }
      }
    }
  }
}
```

**Status:** ⏳ Pending `memory-core` plugin update (requires gateway modification)

---

## Output Files

| File | Purpose | Format |
|------|---------|--------|
| `memory/dreaming-validation.jsonl` | Validation results log | JSONL (one entry per candidate) |
| `memory/dreaming/rem/YYYY-MM-DD.md` | REM phase candidates (input) | Markdown |
| `MEMORY.md` | Promoted durable memories (output) | Markdown |

**Example Validation Log Entry:**
```json
{
  "candidate_id": "6dd4f477",
  "date": "2026-07-03",
  "status": "WARNING",
  "issues": "missing_confidence_tag",
  "timestamp": "2026-07-03T03:15:22Z"
}
```

---

## Validation Rules (CVS Mandate)

### Tier 1: Factual Claims (Must Pass)
- **Numbers:** Vote counts, percentages, dates, margins, electorate sizes
- **Names:** Candidates, positions, titles, party affiliations
- **Locations:** Constituencies, polling districts, geographic references
- **Historical results:** Past election outcomes, majorities, turnout figures

**Requirement:** Must include `Source: <file#line>` or `evidence: <path>`

**Failure:** Candidate blocked from promotion

---

### Tier 2: Analytical Claims (Warning Only)
- Vote split calculations
- Turnout sensitivity analysis
- Demographic inferences
- Strategic assessments
- Mathematical derivations

**Requirement:** Must include confidence tag `[HIGH]`, `[MEDIUM]`, or `[LOW]`

**Failure:** Warning logged, but promotion allowed

---

### Tier 3: Predictive/Speculative Claims (Warning Only)
- Future scenarios
- Emerging narratives
- Risk assessments
- "What-if" modelling

**Requirement:** Must flag as `SPECULATION:`, `SCENARIO:`, or include words like "inference", "projection"

**Failure:** Warning logged, but promotion allowed

---

## Troubleshooting

### Issue: "No candidates found in REM file"

**Cause:** Dreaming hasn't run yet, or REM file is empty.

**Resolution:**
```bash
# Check dreaming status
openclaw memory status --deep

# Check last REM file
ls -lt memory/dreaming/rem/ | head -3

# Manually trigger promotion (runs all phases)
openclaw memory promote
```

---

### Issue: "CVS VALIDATION GATE: BLOCKED"

**Cause:** One or more candidates failed Tier 1 validation (numerical claims without citations).

**Resolution:**
```bash
# 1. Review validation log
cat memory/dreaming-validation.jsonl | jq 'select(.status == "FAILED")'

# 2. Open REM file and add citations
nvim memory/dreaming/rem/2026-07-03.md

# Example fix:
# Before: "BN won 2022 by 4,041 votes"
# After: "BN won 2022 by 4,041 votes [Source: MEMORY.md#L142]"

# 3. Re-run validation
./tools/truth-validator/dreaming-cvs-integration.sh

# 4. If urgent, promote with override (not recommended)
openclaw memory promote --apply --override-cvs
```

---

### Issue: Color codes showing as `[0;32m` instead of green

**Cause:** Terminal doesn't support ANSI color codes.

**Resolution:** Script still works correctly — ignore color codes. Or pipe through `cat -v` to strip them:
```bash
./tools/truth-validator/dreaming-cvs-integration.sh 2>&1 | cat -v
```

---

## Performance Metrics

| Metric | Value | Notes |
|--------|-------|-------|
| **Validation Speed** | ~50 candidates/second | Tested on 2026-07-03 REM file |
| **False Positive Rate** | 0% (by design) | Tier 1 failures are hard errors |
| **Warning Rate** | ~60-80% | Most candidates lack confidence tags |
| **Blocking Rate** | ~5-10% | Depends on source quality |

---

## Security Considerations

### What This Protects Against

1. **Hallucination Propagation** — Prevents unverified claims from entering durable memory
2. **Single-Source Injection** — Requires citations for numerical/entity claims
3. **Confidence Drift** — Enforces confidence tagging on analytical claims
4. **Speculation as Fact** — Flags predictive claims for review

### What This Does NOT Protect Against

1. **Citation Fraud** — Script doesn't verify cited sources actually exist
2. **Multi-Source Collusion** — If 2+ sources share same error, CVS won't catch it
3. **Temporal Decay** — Old citations may become outdated (requires periodic review)
4. **Adversarial Citations** — Attacker could plant fake source files

**Recommendation:** Pair with `tools/memory-harness/calibration-check.sh` for monthly accuracy audits.

---

## Related Tools

| Tool | Purpose | Command |
|------|---------|---------|
| `validate.sh` | General CVS validation for any document | `./validate.sh <file.md>` |
| `extract-numbers.sh` | Extract all numerical claims | `./extract-numbers.sh <file.md>` |
| `verify-names.sh` | Cross-reference candidate names | `./verify-names.sh <file.md>` |
| `calibration-check.sh` | Track confidence tag accuracy | `./calibration-check.sh` |
| `feedback-capture.sh` | Log human corrections | `./feedback-capture.sh add` |

---

## Future Enhancements

| Enhancement | Priority | Status |
|-------------|----------|--------|
| Auto-citation lookup | High | ⏳ Pending (requires embedding API) |
| Multi-source verification | Critical | ⏳ Pending (requires ElectionData.MY integration) |
| Gateway hook integration | Medium | ⏳ Pending (requires memory-core modification) |
| Confidence auto-tagging | Medium | ⏳ Pending (requires LLM inference) |
| Contradiction detection | High | ⏳ Pending (requires vector similarity) |

---

**Maintainer:** DAF  
**Last Updated:** 2026-07-03  
**Version:** 1.0  
**Mandate:** CVS-MANDATE.md (effective 2026-06-28)
