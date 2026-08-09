# Core Truth Validation System (CVS) — System-Wide Mandate

**Effective Date:** 2026-06-28  
**Authority:** DAF  
**Scope:** All sessions, all outputs, all agents  
**Status:** ✅ **MANDATORY**

---

## 🎯 Purpose

**Prevent hallucination, factual drift, and conflation of inference with fact in ALL AI-generated output.**

This is not optional. This is not a suggestion. This is the **engineered trust infrastructure** that makes AI output reliable without manual verification.

---

## 🔒 Mandatory Requirements

### 1. Multi-Source Verification

**Rule:** All Tier 1 factual claims must be cross-referenced from ≥2 independent sources before output.

**Tier 1 Claims (Must Verify):**
- Numbers: vote counts, percentages, dates, margins, electorate sizes
- Names: candidates, positions, titles, party affiliations
- Locations: constituencies, polling districts, geographic references
- Historical results: past election outcomes, majorities, turnout figures

**Validation Method:** Cross-reference against source file + line number. If source is external (news, official data), fetch and cite URL.

**Output Requirement:** Every Tier 1 claim must include `Source: <file#line>` or `Source: <URL>`

---

### 2. Confidence Assertion Tags

**Rule:** All analytical claims must be tagged with confidence level.

| Tag | Meaning | When to Use |
|-----|---------|-------------|
| `[HIGH]` | Derived from verified Tier 1 data, straightforward calculation | Multi-source agreement, simple math |
| `[MEDIUM]` | Reasonable inference from multiple data points | Pattern recognition, historical comparison |
| `[LOW]` | Speculative, depends on unverified assumptions | Emerging trends, uncertain dynamics |

**Output Requirement:** Confidence tag + brief justification for every analytical claim

---

### 3. Speculation Demarcation

**Rule:** All predictive/speculative claims must be explicitly flagged.

**Tags:**
- `SPECULATION:` — Forward-looking claim without verified basis
- `SCENARIO:` — What-if modelling with stated assumptions

**Output Requirement:** Clear demarcation + underlying assumptions stated

**Never:** Present speculation as fact.

---

### 4. Conflict Resolution

**Rule:** When sources disagree, flag and show both values.

**Tag:** `[CONFLICTING]`

**Output Requirement:**
- Show both values
- Cite both sources
- Request human review if unresolved

---

## 🛠️ Validation Gate

**All output must pass validation before delivery:**

```bash
./tools/truth-validator/validate.sh <output-file>.md || exit 1
```

**Exit codes:**
- `0` = Passed (safe to deliver)
- `1` = Failed (blocks delivery, must fix)

**Pre-Output Checklist:**

```
[ ] All Tier 1 numbers verified against source?
[ ] All names double-checked (spelling, position, party)?
[ ] All citations include file#line or URL?
[ ] Confidence tags applied to Tier 2 claims?
[ ] Tier 3 speculation clearly demarcated?
[ ] Any contradictory evidence considered?
[ ] Math shown explicitly for analytical claims?
```

---

## 📊 Claim Tiers

| Tier | Type | Verification Required | Confidence Tag |
|------|------|----------------------|----------------|
| **Tier 1** | Factual (numbers, names, dates, locations) | ≥2 independent sources | `[VERIFIED]` or `[CORROBORATED]` |
| **Tier 2** | Analytical (calculations, inferences, assessments) | Show the math | `[HIGH]` / `[MEDIUM]` / `[LOW]` |
| **Tier 3** | Predictive (scenarios, forecasts, risk assessments) | Flag as speculation | `SPECULATION:` or `SCENARIO:` |

---

## 🔄 Feedback Loop (Loop Engineering)

**All corrections must be captured:**

```bash
./tools/memory-harness/feedback-capture.sh add \
  -f <file>.md \
  -c "<claim text>" \
  -t factual|confidence|source|citation \
  -o "<original value>" \
  -n "<corrected value>" \
  -s "<correct source>"
```

**Monthly Review:**

```bash
./tools/memory-harness/calibration-check.sh analyze
./tools/truth-validator/monthly-review.sh
```

---

## ⚠️ Non-Compliance Consequences

**If CVS is bypassed:**

1. **Immediate:** Output blocked by validation gate
2. **Repeated:** Feedback captured, calibration degraded
3. **Systemic:** Monthly review triggers rule updates, tighter gates

**No output is worth delivering false information.**

---

## 📁 Reference Documents

| Document | Purpose |
|----------|---------|
| `TOOLS.md` | Truth Validation Protocol (claim tiers, checklist, output format) |
| `tools/truth-validator/README.md` | Validator script documentation |
| `tools/truth-validator/QUICKSTART.md` | Quick start guide |
| `tools/memory-harness/README.md` | Feedback loop infrastructure |
| `memory/confidence-calibration.json` | Tag accuracy tracking |
| `memory/validation-feedback.jsonl` | Human corrections log |

## 🔗 External Verification Sources

| Source | Coverage | API Access | Use Case |
|--------|----------|------------|----------|
| **ElectionData.MY** | Malaysia 1954–present | Free API key required | Historical results, candidate data, constituency boundaries |
| **SPR (Suruhanjaya Pilihan Raya)** | Official election results | Manual fetch | Primary source for certified results |
| **MEMORY.md** | Internal war-room briefs | Local file | Cross-reference for ongoing monitoring |

---

## 🎯 Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Tier 1 claims with ≥2 sources | 100% | `validate.sh` enforcement |
| Confidence tags on analytical claims | 100% | `validate.sh` enforcement |
| Speculation demarcation | 100% | `validate.sh` enforcement |
| Feedback capture rate | >90% of corrections | `feedback-capture.sh stats` |
| HIGH tag accuracy | >90% | `calibration-check.sh report` |

---

## 🔐 Authority & Governance

**System Owner:** DAF  
**Enforcement:** Automated (`validate.sh` gate)  
**Review:** Monthly (Loop 4 synthesis)  
**Updates:** Based on feedback patterns + calibration data

**This mandate applies to:**
- All war-room briefs
- All analytical output
- All session responses
- All agent-generated content

**No exceptions.**

---

## 📜 Version History

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-06-28 | Initial mandate, system-wide enforcement |

---

**Approved by:** DAF  
**Effective:** 2026-06-28  
**Next Review:** 2026-07-28 (or after 100 feedback entries)
