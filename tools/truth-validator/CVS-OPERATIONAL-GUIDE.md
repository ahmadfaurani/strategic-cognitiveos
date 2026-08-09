# CVS Operational Guide — ElectionData.MY Integration

**Status:** ✅ **OPERATIONAL** (2026-07-01)  
**API Key:** Configured and active  
**Key Location:** `tools/truth-validator/.electiondata-key` (chmod 600)

---

## 🔑 API Key Configuration

**Automatic Loading:** The validation script now auto-loads the API key from three sources (priority order):

1. **Environment variable** (`$ELECTIONDATA_API_KEY`)
2. **Workspace config** (`~/.openclaw/workspace/.electiondata-config`)
3. **Key file** (`tools/truth-validator/.electiondata-key`) ← **ACTIVE**

**No manual setup required** — the key is loaded automatically when running `validate.sh`.

---

## 🚀 Quick Start

### Validate a Brief

```bash
cd /home/p62operator/.openclaw/workspace
./tools/truth-validator/validate.sh memory/n17-semerah-war-room-brief-20260627.md
```

### Manual API Key Load (if needed)

```bash
source tools/truth-validator/.electiondata-key
export ELECTIONDATA_API_KEY
```

---

## 📋 CVS Enforcement Workflow

### Pre-Output (Mandatory)

**Every war-room brief MUST pass validation before delivery:**

```bash
# Step 1: Run validation
./tools/truth-validator/validate.sh memory/<brief-file>.md

# Step 2: Check result
# - Exit 0 = Passed (safe to deliver)
# - Exit 1 = Failed (must fix before delivery)

# Step 3: Address warnings
# - Add confidence tags [HIGH/MEDIUM/LOW] to analytical claims
# - Add SPECULATION: or SCENARIO: to predictive claims
# - Add Source: citations to Tier 1 claims
```

### Validation Checks

| Check | Status | Enforcement |
|-------|--------|-------------|
| Numerical claims extraction | ✅ Active | Flags all Tier 1 numbers |
| Multi-source verification | ✅ Active | Requires ≥2 sources |
| Confidence assertion tags | ✅ Active | Flags missing tags |
| Speculation demarcation | ✅ Active | Flags unmarked predictions |
| Citation verification | ✅ Active | Checks internal citations |
| Cross-reference engine | ✅ Active | Queries external sources |
| **ElectionData.MY API** | ✅ **ACTIVE** | **Auto-verifies all constituencies** |

---

## 🔍 ElectionData.MY Integration

### What Gets Verified

The validator automatically extracts constituency names and queries ElectionData.MY for:

- Historical election results (2018, 2022, etc.)
- Candidate names and party affiliations
- Vote counts and margins
- Electorate size and turnout
- Demographic breakdowns

### API Response Handling

| Response | Action |
|----------|--------|
| ✅ Data matches | Logged as verified |
| ⚠️ Data differs | Flagged as `[CONFLICTING]` |
| ❌ Not found | Warning logged, continues validation |
| 🔌 API unavailable | Warning logged, relies on other sources |

### Citation Format

When citing ElectionData.MY in briefs:

```markdown
Source: ElectionData.MY API (2026-07-01 query)
Source: https://electiondata.my/constituency/N17-semerah
```

---

## ⚠️ Error Handling

### Missing API Key (CRITICAL)

```
❌ ERROR: ElectionData.MY API key not configured
   This is MANDATORY per CVS-MANDATE.md
   Configure: export ELECTIONDATA_API_KEY=***
   Or run: source tools/truth-validator/.electiondata-key
```

**Action:** Validation **FAILS** (exit 1) — no output allowed without API key.

### API Unavailable (WARNING)

```
⚠ API verification skipped (API unavailable)
```

**Action:** Validation continues with warnings — relies on other sources.

### Data Conflict (WARNING)

```
[CONFLICTING]: 1
  - Claim A: 75.1% (MEMORY.md#L142)
  - Claim B: 73.9% (ElectionData.MY)
```

**Action:** Flag in brief, request human review if unresolved.

---

## 📊 Validation Output Examples

### Clean Pass (No Warnings)

```
=== Validation Summary ===
Errors: 0
Warnings: 0

✅ VALIDATION PASSED - Safe to output
```

### Pass with Warnings (Review Required)

```
=== Validation Summary ===
Errors: 0
Warnings: 2

⚠️  VALIDATION PASSED WITH WARNINGS - Review before output
```

### Fail (Blocks Delivery)

```
=== Validation Summary ===
Errors: 1
Warnings: 0

❌ VALIDATION FAILED - Fix errors before output
```

---

## 🔄 Feedback Loop

### Capture Corrections

When validation reveals errors:

```bash
./tools/memory-harness/feedback-capture.sh add \
  -f memory/n17-semerah-war-room-brief-20260627.md \
  -c "2022 turnout: 61.8%" \
  -t source \
  -o "61.8% (MEMORY.md)" \
  -n "60.5% (ElectionData.MY)" \
  -s "ElectionData.MY API (2026-07-01)"
```

### Monthly Review

```bash
./tools/truth-validator/monthly-review.sh
```

Generates:
- Tag accuracy report (HIGH/MEDIUM/LOW calibration)
- False positive/negative analysis
- PIR keyword refinement recommendations
- API performance metrics

---

## 🛡️ Security Notes

- **API key file:** `chmod 600` (owner read/write only)
- **Never commit** `.electiondata-key` to version control
- **Rotate key** if compromised (get new key from https://electiondata.my/console)

---

## 📚 Related Documents

| Document | Purpose |
|----------|---------|
| `CVS-MANDATE.md` | System-wide mandate (authority, scope, requirements) |
| `CVS-SYSTEM-PROMPT.md` | Technical implementation details |
| `CVS-QUICK-REFERENCE.md` | Quick reference for claim tiers and tags |
| `ELECTIONDATA-INTEGRATION.md` | API integration guide |
| `validate.sh` | Main validation script |
| `electiondata-verify.sh` | API verification script |

---

## 🎯 Success Metrics

| Metric | Target | Status |
|--------|--------|--------|
| Tier 1 claims with ≥2 sources | 100% | ✅ Enforced |
| Confidence tags on analytical claims | 100% | ✅ Enforced |
| Speculation demarcation | 100% | ✅ Enforced |
| ElectionData.MY API active | 100% | ✅ **ACTIVE** |
| Validation gate before delivery | 100% | ✅ Enforced |

---

**Last Updated:** 2026-07-01  
**Maintained By:** DAF  
**Next Review:** 2026-08-01 (or after 100 validation runs)
