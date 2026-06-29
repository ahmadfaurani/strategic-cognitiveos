# CVS Quick Reference Card

**Print this. Pin it. Use it.**

---

## 🛡️ 5 Non-Negotiable Rules

1. **≥2 sources** for Tier 1 claims (numbers, names, dates, locations)
2. **Confidence tags** on all analytical claims: `[HIGH]` / `[MEDIUM]` / `[LOW]`
3. **Speculation flags** on all predictions: `SPECULATION:` or `SCENARIO:`
4. **Citations** on every claim: `Source: <file#line>` or `Source: <URL>`
5. **Validation gate** before delivery: `./tools/truth-validator/validate.sh <file>.md || exit 1`

---

## ✅ Pre-Output Checklist (30 seconds)

```
[ ] Tier 1 numbers verified (≥2 sources)?
[ ] Names checked (spelling, position, party)?
[ ] Citations present (file#line or URL)?
[ ] Confidence tags on analytical claims?
[ ] Speculation flagged (SPECULATION:/SCENARIO:)?
[ ] Math shown for derivations?
```

**If any box is unchecked → DO NOT SEND**

---

## 📊 Claim Tiers

| Tier | What | Requirement | Example |
|------|------|-------------|---------|
| **1** | Numbers, names, dates, locations | ≥2 sources + citation | "4,041 votes [VERIFIED] Source: MEMORY.md#L142" |
| **2** | Analysis, inferences, assessments | Confidence tag + math | "High retention [MEDIUM] — 60–65% based on margin" |
| **3** | Predictions, scenarios, risks | Speculation flag | "SPECULATION: If turnout >80%, PH could win" |

---

## 🏷️ Confidence Tags

| Tag | When | Formula |
|-----|------|---------|
| `[HIGH]` | ≥2 sources agree, simple math | Confidence ≥0.8 |
| `[MEDIUM]` | Reasonable inference, multiple data points | Confidence 0.5–0.79 |
| `[LOW]` | Speculative, unverified assumptions | Confidence <0.5 |

**Confidence = Source Quality × Convergence × Recency**

---

## 🔧 Essential Commands

### Validate Output
```bash
./tools/truth-validator/validate.sh memory/draft.md || exit 1
```

### Capture Feedback (Loop 3)
```bash
./tools/memory-harness/feedback-capture.sh add \
  -f memory/brief.md \
  -c "Claim text" \
  -t factual \
  -o "wrong value" \
  -n "correct value" \
  -s "correct source"
```

### Check Calibration (Loop 4)
```bash
./tools/memory-harness/calibration-check.sh report
```

### Search Memory
```bash
./tools/memory-harness/retriever.sh "N17 Semerah" -n 5
```

### Archive Old Files
```bash
./tools/memory-harness/archiver.sh -d 30 -k 10
```

---

## 📁 Key Files

| File | Purpose |
|------|---------|
| `tools/truth-validator/CVS-MANDATE.md` | System-wide mandate |
| `tools/truth-validator/CVS-SYSTEM-PROMPT.md` | System prompt (this is you) |
| `tools/truth-validator/validate.sh` | Validation gate |
| `memory/validation-feedback.jsonl` | Corrections log |
| `memory/confidence-calibration.json` | Tag accuracy tracking |

---

## 🚨 Common Validation Failures

| Error | Fix |
|-------|-----|
| No Confidence Assertion tags | Add `[HIGH]` / `[MEDIUM]` / `[LOW]` to analytical claims |
| No multi-source verification | Cross-reference ≥2 independent sources |
| Missing citations | Add `Source: <file#line>` or `Source: <URL>` |
| Speculation without flag | Prefix with `SPECULATION:` or `SCENARIO:` |
| Math not shown | Explicitly show derivation (e.g., "PN 8,501 + PH 6,265 = 14,766") |

---

## 💡 Examples

### ✅ Good
```markdown
**BN majority:** 4,041 votes [VERIFIED] Source: MEMORY.md#L142  
**Turnout:** 60–61% [CORROBORATED] Source: MEMORY.md#L145, Malaysiakini 2022-11-20  
**Retention probability:** 60–65% [MEDIUM] — Based on incumbent advantage + 2022 margin

SPECULATION: If turnout exceeds 80%, PH could regain the seat — assumes 2018 patterns repeat
```

### ❌ Bad (Fails Validation)
```markdown
BN won by 4,041 votes. Turnout was about 60%. BN is likely to retain.
PH might win if turnout is high.
```

---

## 🔄 Feedback Loop

1. **Generate** output → `validate.sh` gate
2. **Deliver** if passed
3. **Human corrects** → `feedback-capture.sh add`
4. **Monthly review** → `calibration-check.sh analyze`
5. **System improves** → Update source weights, refine rules

---

## 🎯 Success Metrics

| Metric | Target |
|--------|--------|
| Tier 1 claims with ≥2 sources | 100% |
| Confidence tags on analytical claims | 100% |
| Speculation demarcation | 100% |
| HIGH tag accuracy | >90% |
| Feedback capture rate | >90% |

---

## 🔐 Authority

**Mandatory per:** DAF, 2026-06-28  
**Applies to:** ALL sessions, ALL outputs, ALL agents  
**No exceptions**

**Questions?** → `tools/truth-validator/CVS-MANDATE.md`

---

**Remember:** Trust is the product. Validation is the process. Truth is the output.

🔥
