# Core Truth Validation System (CVS) — Scope & Application

**Effective Date:** 2026-06-28  
**Authority:** DAF  
**Primary Scope:** DUN Profiling Workflow (Johor PRN 2026)  
**Status:** ✅ MANDATORY for DUN Profiling outputs

---

## 🎯 Primary Purpose

**CVS is a focused workstream validation system** designed specifically for the **DUN Profiling V1 Workflow** — ensuring all constituency intelligence briefs meet rigorous truth standards before delivery to war room teams.

**Not a general-purpose AI safety system.** CVS is engineered for one mission: **prevent hallucination, factual drift, and conflation of inference with fact in DUN profiling outputs.**

---

## 🗳️ DUN Profiling Workflow Integration

### Workflow Steps (5 Total)

```
Step 1: Demographics → PD-level voter composition (SPR XLSX)
   └─ CVS Check: Voter counts, PD names, demographic percentages
  
Step 2: Candidates   → Candidate profiles + demographic alignment
   └─ CVS Check: Candidate names, parties, positions, ages
  
Step 3: Historical   → Voting patterns + swing analysis
   └─ CVS Check: Past results, margins, turnout figures
  
Step 4: Synthesis    → Master operational brief
   └─ CVS Check: All Tier 1/2/3 claims validated
  
Step 5: GitHub Upload → Public repository with structured workspace
   └─ CVS Check: Final validation before upload
```

**Validation Gate:** Each step must pass `validate.sh` before proceeding to next step.

---

## 📊 Claim Tier Framework (DUN-Specific)

### Tier 1: Factual Claims (Must Verify Before Output)

**Numbers:**
- Voter counts (total, by PD, by ethnicity)
- Turnout percentages (2018, 2022, historical)
- Vote margins (majority, percentage)
- Electorate sizes (registered voters, youth 18–29)
- Age demographics (candidate ages, voter age distribution)

**Names:**
- Candidate names (spelling, full name)
- Party affiliations (BN, PH, PN, MUDA, etc.)
- Positions (incumbent, former ADUN, EXCO portfolio)
- Polling district names (official SPR names)

**Locations:**
- Constituency codes (N16, N17, N27, etc.)
- Parliament alignment (P146, P147, P149, etc.)
- Polling district boundaries
- Geographic references (kampung, town, mukim)

**Historical Results:**
- Past election winners (2018, 2022, etc.)
- Vote counts per candidate/part
- Majority/margin per election
- Turnout per election

**Validation Method:** Cross-reference against ≥2 independent sources:
- SPR Electoral Roll XLSX (primary source for voter counts)
- ElectionData.MY API (primary source for historical results)
- News sources (candidate names, party announcements)
- Wikipedia (cross-reference for results)

**Output Requirement:** Every Tier 1 claim must include:
- `Source: SPR Electoral Roll 2026` (for voter counts)
- `Source: ElectionData.MY + Wikipedia` (for historical results)
- `Source: <URL>` (for candidate info from news)

---

### Tier 2: Analytical Claims (Must Tag Confidence)

**Examples:**
- Vote split calculations (e.g., "Combined opposition vote exceeded BN total")
- Turnout sensitivity analysis (e.g., "High turnout favors PH")
- Demographic inferences (e.g., "Youth concentration in urban PDs")
- Strategic assessments (e.g., "BN retention probability high")
- Mathematical derivations (e.g., "Swing of 5% needed for PH to win")

**Confidence Tags:**
- `[HIGH]` — Derived from verified Tier 1 data, straightforward calculation
- `[MEDIUM]` — Reasonable inference from multiple data points
- `[LOW]` — Speculative, depends on unverified assumptions

**Output Requirement:** Confidence tag + brief justification

**Example:**
```markdown
**BN Retention Probability:** 60–65% [MEDIUM]
- Justification: Based on incumbent advantage + 2022 margin (4,041 votes),
  but vulnerable if PN exceeds 8,501-vote base (split math: opposition
  combined 14,766 > BN 12,542) [HIGH]
```

---

### Tier 3: Predictive/Speculative Claims (Must Flag)

**Examples:**
- Victory probability models (e.g., "BN 70% chance if turnout <65%")
- Turnout scenarios (e.g., "If turnout >80%, PH could win")
- Swing projections (e.g., "Malay vote shift could compress margin to 2%")
- Risk assessments (e.g., "PN spoiler role likely")

**Flags:**
- `SPECULATION:` — Forward-looking claim without verified basis
- `SCENARIO:` — What-if modelling with stated assumptions

**Output Requirement:** Clear demarcation + underlying assumptions stated

**Example:**
```markdown
SPECULATION: Turnout scenarios based on 2018-2022 patterns

| Turnout | Projected Winner | Margin | Key Assumptions |
|---------|------------------|--------|-----------------|
| 60% (Low) | BN | 6,000+ votes | Rural base mobilized, Chinese stay home |
| 75% (High) | Toss-up | <1,000 votes | Youth surge, Chinese turnout 80%+ |
| 85% (Very High) | PH | 500–1,500 votes | 2018 patterns repeat, Malay swing 5% |

Assumptions:
1. Chinese turnout correlates with PH performance (r=0.85, 2018-2022)
2. Malay vote split remains stable (BN 55%, PN 30%, PH 15%)
3. Youth turnout favors PH by 10–15% margin
```

---

## 🛡️ Validation Gate (DUN Profiling)

**Mandatory Pre-Output Check:**

```bash
./tools/truth-validator/validate.sh <brief-file>.md || exit 1
```

**Exit Codes:**
- `0` → PASSED (safe to deliver to war room)
- `1` → FAILED (blocks delivery, must fix before proceeding)

**7 Validation Checks:**

| Check | DUN-Specific Focus |
|-------|-------------------|
| 1. Numerical Claims | Voter counts, turnout %, margins, PD-level demographics |
| 2. Multi-Source Verification | SPR + ElectionData.MY + news cross-reference |
| 3. Citation Verification | Internal citations (MEMORY.md#L###) valid |
| 4. Analytical Confidence Tags | [HIGH/MEDIUM/LOW] on strategic assessments |
| 5. Speculation Demarcation | SPECULATION:/SCENARIO: on victory projections |
| 6. Cross-Reference Check | External API queries (ElectionData.MY) |
| 7. ElectionData.MY API | Auto-verify constituency historical results |

---

## 📁 DUN Profiling Output Documents

**4 Briefs Per Constituency:**

1. **Demographic Brief** (`memory/nXX-constituency-demographic-brief-YYYYMMDD.md`)
   - PD-level voter composition
   - Ethnicity breakdown
   - Youth concentration
   - Gender distribution

2. **Candidate Brief** (`memory/nXX-constituency-candidate-brief-YYYYMMDD.md`)
   - Candidate profiles (name, party, age, background)
   - Demographic alignment analysis
   - Strengths/vulnerabilities assessment

3. **Historical Brief** (`memory/nXX-constituency-historical-brief-YYYYMMDD.md`)
   - Past election results (2018, 2022)
   - Swing analysis
   - Turnout patterns
   - Historical majorities

4. **Master Operational Brief** (`memory/nXX-constituency-master-brief-YYYYMMDD.md`)
   - Integrated synthesis of all 3 dimensions
   - Strategic assessment (BN/PH/PN paths to victory)
   - Key battleground PDs
   - Victory probability scenarios

**All 4 briefs must pass CVS validation before delivery.**

---

## ✅ Completed Constituencies (CVS-Validated)

| Constituency | Code | Parliament | Status | CVS Validated |
|--------------|------|------------|--------|---------------|
| Layang-Layang | N27 | P149 | ✅ Full (5 steps) | ✅ Yes |
| Sungai Balang | N16 | P146 | ✅ Partial (4 steps) | ✅ Yes |
| Semerah | N17 | P147 | ✅ Partial (4 steps) | ✅ Yes |
| Endau | N32 | P154 | ✅ Partial (4 steps) | ✅ Yes |

**Total CVS Validations:** 16 briefs (4 constituencies × 4 briefs each)  
**Compliance Rate:** 100%

---

## 🔍 Source Hierarchy (DUN Profiling)

| Tier | Type | Weight | Examples | Use Case |
|------|------|--------|----------|----------|
| **Tier 0** | Official Primary | 1.0 | SPR Electoral Roll XLSX, government gazettes | Voter counts, PD boundaries |
| **Tier 1** | Established Media | 0.8 | Malaysiakini, The Star, NST, FMT, BERNAMA | Candidate announcements |
| **Tier 2** | Secondary Media | 0.6 | Sinar Harian, Malaysian Insight, local news | Candidate profiles |
| **Tier 3** | Social/Unverified | 0.3 | Twitter, Facebook, WhatsApp forwards | ⚠️ Insufficient alone |
| **Tier 4** | Internal Memory | 0.5 | MEMORY.md, prior briefs (if sourced) | Cross-reference only |

**Rule:** Tier 1 claims require ≥2 Tier 0–2 sources. Tier 3 sources alone are insufficient.

---

## 🔄 Feedback Loop (Loop Engineering)

### Loop 3: Feedback Capture

**When:** Human reviewer corrects a brief

**How:**
```bash
./tools/memory-harness/feedback-capture.sh add \
  -f memory/n17-semerah-demographic-brief-20260627.md \
  -c "Total voters: 89,234" \
  -t factual \
  -o "89,234" \
  -n "89,156" \
  -s "SPR Electoral Roll XLSX (corrected file)"
```

**Tracking:** `memory/validation-feedback.jsonl`

---

### Loop 4: Monthly Review

**When:** First of each month (next: 2026-07-28)

**How:**
```bash
./tools/truth-validator/monthly-review.sh
```

**Generates:**
- Tag accuracy report (HIGH/MEDIUM/LOW calibration)
- False positive/negative analysis
- Source quality assessment
- Recommendations for workflow improvements

**Tracking:** `memory/confidence-calibration.json`

---

## 📊 Performance Metrics (DUN Profiling)

| Metric | Target | Current (as of 2026-07-03) |
|--------|--------|---------------------------|
| Tier 1 claims with ≥2 sources | 100% | 100% (16/16 briefs) |
| Confidence tags on analytical claims | 100% | 100% (16/16 briefs) |
| Speculation demarcation | 100% | 100% (16/16 briefs) |
| Validation gate before delivery | 100% | 100% (16/16 briefs) |
| Feedback capture rate | >90% | 0% (⚠️ no corrections yet) |
| HIGH tag accuracy | >90% | TBD (⏳ awaiting calibration) |

---

## 🚫 What CVS Is NOT

**CVS is NOT:**
- ❌ A general-purpose AI safety system for all outputs
- ❌ A chatbot conversation validator
- ❌ A memory curation tool (except for DUN profiling briefs)
- ❌ A political opinion validator (doesn't assess political views)
- ❌ A real-time fact-checker for live conversations

**CVS IS:**
- ✅ A focused workstream validation system for DUN profiling
- ✅ A pre-delivery gate for constituency intelligence briefs
- ✅ A structured framework for multi-source verification
- ✅ A confidence tagging system for analytical claims
- ✅ A speculation demarcation tool for predictive modelling

---

## 🔐 Authority & Governance

**System Owner:** DAF  
**Enforcement:** Automated (`validate.sh` gate in DUN profiling workflow)  
**Review:** Monthly (Loop 4 synthesis, next: 2026-07-28)  
**Updates:** Based on feedback patterns + calibration data

**This mandate applies to:**
- ✅ All DUN profiling briefs (Demographic, Candidate, Historical, Master)
- ✅ All war-room intelligence outputs
- ✅ All GitHub repository uploads from DUN profiling workflow

**Does NOT apply to:**
- ❌ General chat conversations
- ❌ Non-DUN analytical outputs (unless explicitly opted-in)
- ❌ Personal memory notes (daily files, MEMORY.md curation)

---

## 📚 Related Documents

| Document | Purpose |
|----------|---------|
| `DUN-Profiling/README.md` | Workflow overview |
| `DUN-Profiling/WORKFLOW-PROMPTS.md` | Step-by-step execution prompts |
| `DUN-Profiling/CVS-COMPLIANCE.md` | CVS compliance report for DUN profiling |
| `tools/truth-validator/CVS-MANDATE.md` | System-wide mandate (broader scope) |
| `tools/truth-validator/validate.sh` | Main validation script |

---

## 📝 Version History

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-06-28 | Initial mandate, DUN profiling focus |
| 1.1 | 2026-07-01 | ElectionData.MY API integration |
| 1.2 | 2026-07-03 | Dreaming CVS integration added |

---

**Approved by:** DAF  
**Effective:** 2026-06-28  
**Primary Scope:** DUN Profiling Workflow (Johor PRN 2026)  
**Next Review:** 2026-07-28 (or after 100 feedback entries)

---

**Remember:** CVS exists to make DUN profiling outputs **trustworthy**. Every validation check, every confidence tag, every citation serves one purpose: **ensure war room teams can act on intelligence without second-guessing accuracy.**

🔥
