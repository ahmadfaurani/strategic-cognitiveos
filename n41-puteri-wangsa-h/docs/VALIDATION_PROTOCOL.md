# 🔒 SOURCE OF TRUTH PROTOCOL
**Effective:** 2026-06-28 08:20 UTC  
**Trigger:** N11/N41 confusion incident  
**Mandate:** NO output without grounded truth citation

---

## 🎯 CORE PRINCIPLE

**"If it's not in SOURCE_OF_TRUTH, it doesn't exist."**

Every factual claim must be traceable to:
1. ✅ `memory/SOURCE_OF_TRUTH_N41_PUTERI_WANGSA.md` (golden records), OR
2. ✅ Primary source document (SPR Excel, official news report, manifesto extract)

---

## 📋 VALIDATION WORKFLOW

### Step 1: Check SOURCE_OF_TRUTH
Before outputting ANY fact:
```bash
# Mental check
- Is this claim in SOURCE_OF_TRUTH_N41_PUTERI_WANGSA.md?
- If YES → proceed with citation
- If NO → go to Step 2
```

### Step 2: Verify Against Primary Source
```bash
# Primary sources (in priority order)
1. SPR Excel file (`11_PUTERI_WANGSA_as_of_190626---*.xlsx`)
2. Official news reports (Bernama, Astro Awani, The Star, NST)
3. PH Johor Manifesto extract (`ph-johor-manifesto-20260624-extracted.txt`)
4. electiondata.my
5. Jacknjillscute.com (for 2022 results)
```

### Step 3: Add to SOURCE_OF_TRUTH
Before using the claim:
```markdown
## [New Section]
| Field | Value | Source | Verified Date |
|-------|-------|--------|---------------|
| [claim] | [value] | [source file/url] | [date] |
```

### Step 4: Output with Citation
```markdown
**Claim:** [statement]  
**Source:** `SOURCE_OF_TRUTH_N41_PUTERI_WANGSA.md` → [section]  
**Confidence:** HIGH (verified against primary source)
```

---

## 🚨 RED LINES (NEVER OUTPUT WITHOUT VERIFICATION)

| Category | Examples | Action Required |
|----------|----------|-----------------|
| **Seat Identification** | N11 vs N41, P158 vs P156, seat names | ✅ Must match SOURCE_OF_TRUTH exactly |
| **Voter Counts** | Total electorate, PD-level counts | ✅ Must match SPR Excel |
| **Demographics** | Ethnic %, age %, gender % | ✅ Must match SPR Excel sums |
| **Candidate Names** | Maszlee, Rashifa, Teow, etc. | ✅ Must match BusinessToday/MalaysiaGazette |
| **Election Results** | 2022 votes, percentages, majorities | ✅ Must match jacknjillscute.com/Bernama |
| **Polling Districts** | PD names, codes, tier classification | ✅ Must match SPR Excel KOD DM column |

---

## 📝 CITATION FORMAT (MANDATORY)

### For Tables:
```markdown
| Metric | Value | Source | Verified Date |
|--------|-------|--------|---------------|
| Total Voters | 128,723 | SOURCE_OF_TRUTH → Section 2 | 2026-06-28 |
```

### For Text Claims:
```markdown
Dr Maszlee Malik is contesting N41 Puteri Wangsa (SOURCE_OF_TRUTH → Section 5, verified 2026-06-28 against BusinessToday).
```

### For Analysis:
```markdown
**Assumption:** 60% turnout scenario  
**Basis:** SOURCE_OF_TRUTH → Section 2 (2022 turnout was 47.9%)  
**Confidence:** MEDIUM (projection, not verified fact)
```

---

## ⚠️ INCIDENT RESPONSE

### If Wrong Information is Output:
1. **Immediate:** Acknowledge error publicly
2. **Correction:** Issue corrected statement with proper citation
3. **Update:** Add correct data to SOURCE_OF_TRUTH
4. **Audit:** Check all downstream documents for same error
5. **Document:** Log incident in CHANGE_LOG below

### Example (N11/N41 Incident):
```
INCIDENT: Repository named N11---Puteri-Wangsa-H (wrong)
CORRECT: N41---Puteri-Wangsa-H
ROOT CAUSE: No SOURCE_OF_TRUTH check before repo creation
FIX: Created SOURCE_OF_TRUTH_N41_PUTERI_WANGSA.md
PREVENTION: Mandatory citation check before all outputs
```

---

## 🔄 MAINTENANCE

### Daily Checks:
- [ ] Review all outputs from previous day
- [ ] Verify any new claims against primary sources
- [ ] Update SOURCE_OF_TRUTH with newly verified data

### Weekly Reviews:
- [ ] Audit all documents for citation compliance
- [ ] Remove any unverified assumptions that were used as facts
- [ ] Add new primary sources if discovered

### Before Major Deliverables:
- [ ] Full SOURCE_OF_TRUTH review
- [ ] Cross-check all tables/numbers against golden records
- [ ] Flag any assumptions vs verified facts

---

## 📁 FILE LOCATIONS

| File | Purpose | Path |
|------|---------|------|
| **SOURCE_OF_TRUTH** | Golden records | `memory/SOURCE_OF_TRUTH_N41_PUTERI_WANGSA.md` |
| **SPR Excel** | Raw demographic data | `/home/p62operator/.openclaw/media/inbound/11_PUTERI_WANGSA_as_of_190626---*.xlsx` |
| **Manifesto** | PH Johor Manifesto 2026 | `memory/ph-johor-manifesto-20260624-extracted.txt` |
| **Fact-Check** | All outputs validated | `memory/puteri-wangsa-comprehensive-fact-check-20260628.md` |

---

## 📊 CHANGE LOG

| Date | Incident | Fix | Prevention |
|------|----------|-----|------------|
| 2026-06-28 08:03 | Repo named N11 instead of N41 | Renamed to N41---Puteri-Wangsa-H | Created SOURCE_OF_TRUTH protocol |

---

## ✅ COMPLIANCE CHECKLIST

Before sending ANY output:

- [ ] Does this contain factual claims?
- [ ] Are all claims in SOURCE_OF_TRUTH or primary sources?
- [ ] Are citations included (file + section/date)?
- [ ] Are assumptions clearly labeled as assumptions?
- [ ] Would another team member be able to verify this independently?

**If any answer is NO → STOP and verify before outputting.**

---

**Protocol Owner:** PKR War Room Data Team  
**Last Updated:** 2026-06-28 08:20 UTC  
**Next Review:** 2026-06-29 08:00 UTC (daily)
