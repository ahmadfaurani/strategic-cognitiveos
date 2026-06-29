# Core Truth Validation System (CVS) — Operational Summary

**Date:** 2026-06-28  
**Status:** ✅ **OPERATIONAL**  
**Scope:** System-wide mandate, all sessions

---

## 🎯 What We Built

A **trust engine** — not just a validator. Every output is engineered to be verifiable, every correction feeds back into system improvement, and the user never has to fact-check manually.

---

## 📁 Documentation Structure

```
tools/truth-validator/
├── CVS-MANDATE.md                  # System-wide mandate (authority document)
├── CVS-SYSTEM-PROMPT.md            # System prompt for all sessions
├── CVS-QUICK-REFERENCE.md          # Quick reference card (print this)
├── CVS-OPERATIONAL-SUMMARY.md      # This file (executive summary)
├── validate.sh                     # Validation gate script
├── crossref.sh                     # Multi-source fetcher
├── feedback-log.sh                 # Loop 3 feedback capture
├── monthly-review.sh               # Loop 4 system improvement
├── extract-numbers.sh              # Extract numerical claims
├── verify-names.sh                 # Verify candidate names
├── README.md                       # Validator documentation
└── QUICKSTART.md                   # Quick start guide

tools/memory-harness/
├── README.md                       # Usage guide
├── indexer.sh                      # QMD file indexing
├── retriever.sh                    # Keyword search
├── archiver.sh                     # Archive old files
├── feedback-capture.sh             # Loop 3: Capture corrections
├── calibration-check.sh            # Loop 4: Track accuracy
└── CTO-Embedding-Access-Request.md # Ready to send

memory/
├── validation-feedback.jsonl       # Human corrections log (empty, ready)
├── confidence-calibration.json     # Tag accuracy tracking (baseline)
└── source-accuracy.json            # Source reliability tracking (baseline)
```

---

## 🔥 Mandatory Requirements (All Sessions)

### 1. Multi-Source Verification
- **Rule:** ≥2 independent sources for Tier 1 claims
- **Tier 1:** Numbers, names, dates, locations, historical results
- **Output:** `Source: <file#line>` or `Source: <URL>`

### 2. Confidence Assertion Tags
- **Rule:** All analytical claims tagged
- **Tags:** `[HIGH]` / `[MEDIUM]` / `[LOW]`
- **Requirement:** Brief justification

### 3. Speculation Demarcation
- **Rule:** All predictive claims flagged
- **Tags:** `SPECULATION:` or `SCENARIO:`
- **Requirement:** State underlying assumptions

### 4. Validation Gate
- **Command:** `./tools/truth-validator/validate.sh <output>.md || exit 1`
- **Exit 0:** Passed (safe to deliver)
- **Exit 1:** Failed (blocks delivery, must fix)

---

## 🔄 Loop Engineering

| Loop | Purpose | Script | Status |
|------|---------|--------|--------|
| **Loop 1** | Generate + validate | `validate.sh` | ✅ Operational |
| **Loop 2** | Auto-verify (multi-source) | `crossref.sh` | ✅ Operational |
| **Loop 3** | Human feedback capture | `feedback-capture.sh` | ✅ Ready |
| **Loop 4** | Monthly synthesis | `calibration-check.sh` + `monthly-review.sh` | ✅ Ready |

**Missing:** Embedding API for semantic search + automated dreaming (pending CTO approval)

---

## 📊 Success Metrics

| Metric | Target | Current |
|--------|--------|---------|
| Tier 1 claims with ≥2 sources | 100% | ✅ Enforced by gate |
| Confidence tags on analytical claims | 100% | ✅ Enforced by gate |
| Speculation demarcation | 100% | ✅ Enforced by gate |
| Feedback capture rate | >90% | ⏳ Awaiting production use |
| HIGH tag accuracy | >90% | ⏳ Awaiting calibration data |

---

## 🚀 How to Use (Today)

### Step 1: Generate Output

```bash
# Your normal workflow
./generate-brief.sh > memory/draft-brief.md
```

### Step 2: Validate

```bash
./tools/truth-validator/validate.sh memory/draft-brief.md || exit 1
```

**If validation fails:**
- Read error messages
- Fix missing citations, tags, or verification
- Re-validate until exit code = 0

### Step 3: Deliver

```bash
# If validation passed (exit 0)
# Deliver output to user/channel
```

### Step 4: Capture Feedback (If Corrected)

```bash
./tools/memory-harness/feedback-capture.sh add \
  -f memory/draft-brief.md \
  -c "Claim that was corrected" \
  -t factual \
  -o "Your original value" \
  -n "Corrected value" \
  -s "Correct source"
```

### Step 5: Monthly Review

```bash
./tools/memory-harness/calibration-check.sh analyze
./tools/truth-validator/monthly-review.sh
```

---

## 📝 System Prompt Integration

**CVS is now embedded in:**
- `AGENTS.md` — Mandatory section added (Red Lines)
- `tools/truth-validator/CVS-SYSTEM-PROMPT.md` — Full system prompt
- `memory/2026-06-28.md` — Decision recorded

**All future sessions will inherit CVS requirements automatically.**

---

## ⏳ Pending Items

| Item | Status | Owner | Blocker |
|------|--------|-------|---------|
| Embedding API access | ⏳ Pending | CTO | Awaiting approval |
| First production test | ⏳ Pending | DAF | Next brief |
| First feedback entry | ⏳ Pending | DAF | First correction |
| First dreaming cycle | ⏳ Pending | System | Embedding API |
| First monthly review | ⏳ Pending | System | 30 days of data |

---

## 🎯 Next Actions

**Immediate (today):**
- [x] CVS mandate documented
- [x] System prompt created
- [x] Memory harness built
- [x] AGENTS.md updated
- [ ] Send CTO embedding request
- [ ] Use CVS on next brief (production test)

**This week:**
- [ ] Capture first feedback entry
- [ ] Test archiver script (if MEMORY.md grows)
- [ ] Run calibration check (even with 0 data, establishes baseline)

**This month:**
- [ ] Accumulate 10+ feedback entries
- [ ] Run first monthly review
- [ ] Refine validation rules based on patterns

---

## 🔐 Governance

**System Owner:** DAF  
**Enforcement:** Automated (`validate.sh` gate)  
**Review:** Monthly (Loop 4 synthesis)  
**Updates:** Based on feedback patterns + calibration data  
**Authority:** `tools/truth-validator/CVS-MANDATE.md`

**Non-compliance consequences:**
1. Immediate: Output blocked by validation gate
2. Repeated: Feedback captured, calibration degraded
3. Systemic: Monthly review triggers tighter gates

---

## 📞 Quick Help

| Need | Command | File |
|------|---------|------|
| Validate output | `./tools/truth-validator/validate.sh <file>.md` | `README.md` |
| Capture feedback | `./tools/memory-harness/feedback-capture.sh add` | `tools/memory-harness/README.md` |
| Check calibration | `./tools/memory-harness/calibration-check.sh report` | N/A |
| Search memory | `./tools/memory-harness/retriever.sh "query"` | `tools/memory-harness/README.md` |
| Archive files | `./tools/memory-harness/archiver.sh -d 30 -k 10` | `tools/memory-harness/README.md` |
| Quick reference | — | `CVS-QUICK-REFERENCE.md` |
| Full mandate | — | `CVS-MANDATE.md` |
| System prompt | — | `CVS-SYSTEM-PROMPT.md` |

---

## 💭 Philosophy

**Trust is the product.** Not speed. Not verbosity. Not cleverness.

**Validation is the process.** Not an afterthought. Not optional. Not "when I remember."

**Truth is the output.** Not plausible. Not "probably right." Not "close enough."

**Engineered for success.** Prevention over detection. Make errors harder to make than to avoid.

**Feedback loop required.** Every correction makes the system smarter. Every mistake is a lesson.

**No exceptions.**

---

**Approved by:** DAF  
**Effective:** 2026-06-28  
**Next Review:** 2026-07-28 (or after 100 feedback entries)

🔥
