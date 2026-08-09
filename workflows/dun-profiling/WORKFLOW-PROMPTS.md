# DUN Profiling V1 — Three-Dimensional Analysis + GitHub Upload

**Workflow Name:** DUN Profiling V1  
**Purpose:** Complete constituency intelligence package for Johor PRN 2026 war room operations. This three-dimensional methodology transforms raw electoral data into actionable operational guidance with automated GitHub repository creation.

**Workflow Type:** Three-dimensional analysis + synthesis + GitHub upload (one-time per constituency)  
**Output:** Four brief documents + GitHub repository

**Status:** ✅ VALIDATED (N.27 Layang-Layang test run complete)  
**Version:** V1 (Production)

---

## 📋 Workflow Overview

```
                    ┌─────────────────────────────────────┐
                    │  Input Data Sources                 │
                    │  - SPR Electoral Roll (XLSX)        │
                    │  - News sources + nominations       │
                    │  - ElectionData.MY + SPR historical │
                    └─────────────────────────────────────┘
                                    │
        ┌───────────────────────────┼───────────────────────────┐
        │                           │                           │
        ▼                           ▼                           ▼
┌───────────────────┐   ┌───────────────────┐   ┌───────────────────┐
│ Step 1:           │   │ Step 2:           │   │ Step 3:           │
│ Demographics      │   │ Candidates        │   │ Historical        │
│                   │   │                   │   │                   │
│ PD-level voter    │   │ Candidate profiles│   │ Voting patterns   │
│ composition       │   │ + demographic     │   │ + swing analysis  │
│                   │   │   alignment       │   │                   │
│ Input: SPR XLSX   │   │ Input: News       │   │ Input:            │
│ (CVS: ✅)         │   │       nominations │   │       ElectionData│
│                   │   │ (CVS: ✅)         │   │ (CVS: ✅)         │
│ Output:           │   │ Output:           │   │ Output:           │
│ {code}-demographic│   │ {code}-candidate  │   │ {code}-historical │
│ -brief.md         │   │ -demographic-     │   │ -performance-     │
│                   │   │   brief.md        │   │   brief.md        │
└───────────────────┘   └───────────────────┘   └───────────────────┘
        │                           │                           │
        └───────────────────────────┼───────────────────────────┘
                                    │
                                    ▼
                    ┌─────────────────────────────────────┐
                    │  Step 4: Synthesis                  │
                    │  Master Operational Brief           │
                    │                                     │
                    │  Input: All three dimensional       │
                    │         briefs                      │
                    │  (CVS: ✅)                          │
                    │                                     │
                    │  Output: {code}-master-operational  │
                    │          -brief.md                  │
                    └─────────────────────────────────────┘
                                    │
                                    ▼
                    ┌─────────────────────────────────────┐
                    │  Step 5: GitHub Upload              │
                    │  Private Repository Creation        │
                    │                                     │
                    │  Input: All 4 brief documents       │
                    │  (CVS: ✅)                          │
                    │                                     │
                    │  Output: GitHub repo with           │
                    │          structured workspace       │
                    └─────────────────────────────────────┘
                                    │
                                    ▼
                    DELIVERY (memory/ + Telegram + GitHub)
```

---

## 🗳️ Complete DUN Profiling Workflow — Three-Dimensional Analysis

### Overview

This is the established, repeatedly-leveraged methodology for Johor PRN 2026 war room intelligence:

| Step | Dimension | Focus | Input Data | Output Document | CVS Status |
|------|-----------|-------|------------|-----------------|------------|
| **Step 1** | **Demographics** | PD-level voter composition | SPR Electoral Roll (XLSX) | `{code}-demographic-brief.md` | ✅ Primary source |
| **Step 2** | **Candidates** | Candidate profiles + alignment | News + nominations | `{code}-candidate-demographic-brief.md` | ✅ Multi-source |
| **Step 3** | **Historical** | Voting patterns + swing | ElectionData.MY + SPR | `{code}-historical-performance-brief.md` | ✅ Cross-ref |
| **Step 4** | **Synthesis** | Integrated operational guidance | Steps 1-3 briefs | `{code}-master-operational-brief.md` | ✅ Model tags |
| **Step 5** | **GitHub Upload** | Private repo creation | All 4 briefs | GitHub repository | ✅ Structured |

**File Naming Convention:** `n{code}-{constituency-name}-{brief-type}-{YYYYMMDD}.md`  
**Storage:** `/home/p62operator/memory/`  
**GitHub Naming:** `analytical-dun-profiling-n{code}-{constituency-name}`

---

## 🔍 CVS (Core Truth Validation System) — Mandatory at Each Step

### CVS Requirements Applied Throughout Workflow

| Requirement | Application |
|-------------|-------------|
| **Multi-Source Verification** | Tier 1 claims (numbers, names, dates) require ≥2 independent sources (except SPR XLSX = primary) |
| **Confidence Assertion Tags** | All analytical claims tagged: [HIGH] / [MEDIUM] / [LOW] with justification |
| **Speculation Demarcation** | All predictive claims flagged: `SPECULATION:` or `SCENARIO:` |
| **Conflict Resolution** | When sources disagree, tag [CONFLICTING], show both values, request human review |
| **Validation Gate** | All output must pass: `./tools/truth-validator/validate.sh <output>.md || exit 1` |

### Step-Specific CVS Application

#### **Step 1 (Demographics) — CVS Compliance ✅**
- **SPR XLSX = Official Primary Source** (no cross-reference needed for voter counts)
- All numerical claims cite "SPR Electoral Roll 2026"
- Confidence tags: [HIGH] for SPR data, [MEDIUM] for derived analysis
- No speculation (factual data only)

#### **Step 2 (Candidates) — CVS Compliance ✅**
- Names/parties verified via ≥2 sources (WakilKu + news + Wikipedia)
- Single-source claims tagged [MEDIUM] or [LOW]
- All sources cited with URLs
- Strategic assessments tagged [MEDIUM/LOW]

#### **Step 3 (Historical) — CVS Compliance ✅**
- Election results cross-referenced (Wikipedia + ElectionData.MY + SPR)
- Turnout figures verified across multiple sources
- Projections marked [LOW] with assumptions stated
- `SPECULATION:` prefix on scenario modelling

#### **Step 4 (Synthesis) — CVS Compliance ✅**
- Victory probability models prefixed with `SPECULATION:`
- Model assumptions explicitly listed (5 points)
- Strategic assessments tagged [MEDIUM/LOW]
- Battleground PD analysis tagged [MEDIUM]
- Sources reference all 3 input briefs

#### **Step 5 (GitHub Upload) — CVS Compliance ✅**
- All uploaded files pre-validated via truth validator
- Repository README includes CVS compliance statement
- Source citations preserved in all documents
- Confidence tags visible in all markdown files

---

## 🗳️ Step 1: PD-Level Demographic Structuring ✅

**Input:** SPR Electoral Roll XLSX (e.g., `8_LAYANG_LAYANG_as_of_190626.xlsx`)

**Output:** `n27-layang-layang-demographic-brief-20260701.md`

**CVS Compliance:** ✅ SPR XLSX = official primary source

### 📝 Prompt

```
You are a political data analyst specializing in electoral demographics and PD-level voter composition.

Review the attached SPR Electoral Roll data and generate a detailed and structured analytical report optimized for political intelligence operational applied use case.

**CVS Requirement:** SPR XLSX is the official primary source. All numerical claims must cite "SPR Electoral Roll 2026". Tag confidence: [HIGH] for SPR data, [MEDIUM] for derived analysis.

Required sections:
1. Constituency overview (total voters, ethnicity, gender, youth, OKU)
2. PD tier classification (Malay Super Safe ≥80% → Chinese Super Safe ≥60%)
3. PD-level breakdown table (all PDs with demographics)
4. Youth concentration analysis (top 5 PDs)
5. Strategic assessment (advantages per party, decisive segments)

All claims must cite SPR Electoral Roll 2026. Tag confidence: [HIGH/MEDIUM/LOW].
```

---

## 🗳️ Step 2: Candidate Profiling + Demographic Alignment ✅

**Input:**
- Candidate nomination announcements (Sinar Harian, BERNAMA)
- Party press releases (UMNO Online, PKR, PAS)
- Historical candidate performance (ElectionData.MY)

**Output:** `n27-layang-layang-candidate-brief-20260701.md`

**CVS Compliance:** ✅ Multi-source verification on key claims

### 📝 Prompt

```
You are a political intelligence analyst specializing in candidate profiling and demographic alignment.

Research all candidates contesting this constituency and generate a detailed and structured analytical report optimized for political intelligence operational applied use case.

**CVS Requirement:** All Tier 1 claims (names, parties, ages) must be verified via ≥2 independent sources. Single-source claims tagged [MEDIUM] or [LOW]. All sources cited with URLs.

Conduct open-source research: news articles (Sinar Harian, BERNAMA, The Star, NST), party announcements (UMNO Online, PKR, PAS official channels), candidate social media, and historical election data (ElectionData.MY).

Required sections:

1. **Candidate Roll Confirmation**
   - Names, parties, nomination details
   - Contest type (3/4/5-cornered fight)
   - Nomination date + centre

2. **Candidate Profile Cards** (One per candidate)
   - Full name + age
   - Party + position (if any)
   - Incumbent status (Yes/No, 2022 performance if applicable)
   - Professional background (education, career, business)
   - Political experience (previous contests, party roles, public office)
   - Family/political connections (dynasty, alliances)
   - Public profile (social media presence, media coverage)
   - Core advantages (incumbency, name recognition, machinery, personal brand)
   - Key vulnerabilities (weak record, controversies, limited appeal, inexperience)

3. **Demographic Alignment Matrix**
   - Assess each candidate's alignment per segment (Strong/Moderate/Weak):
     - Rural Malay (kampung)
     - Urban Malay
     - Chinese voters
     - Indian voters
     - Youth (18-29)
     - Women voters
   - Justify each assessment with evidence

4. **Vote Projections (Baseline Scenario)**
   - Projected vote share per candidate (%)
   - Projected vote count (absolute votes)
   - Path to victory (what each candidate needs)
   - Key risk factors per candidate

5. **Vote Split Dynamics**
   - Opposition fragmentation math (combined opposition vs incumbent)
   - Spoiler potential (which candidate spoils for whom)
   - Turnout sensitivity (how turnout changes affect each candidate)

All candidate claims must cite news sources or official announcements with URL. Tag confidence: [HIGH/MEDIUM/LOW].
```

---

## 🗳️ Step 3: Historical Performance + Voter Behaviour Signals ✅

**Input:**
- ElectionData.MY (2018, 2022 official results)
- SPR electoral roll historical data
- Turnout statistics by election cycle

**Output:** `n27-layang-layang-historical-brief-20260701.md`

**CVS Compliance:** ✅ Cross-referenced election results

### 📝 Prompt

```
You are a political data analyst specializing in historical election performance and voter behaviour modelling.

Research historical election data for this constituency and generate a detailed and structured analytical report optimized for political intelligence operational applied use case.

**CVS Requirement:** All election results must be cross-referenced (≥2 sources: Wikipedia + ElectionData.MY + SPR). Projections marked [LOW] with assumptions stated. Use `SPECULATION:` prefix for scenario modelling.

Use ElectionData.MY API, SPR historical data, and official election results.

Required sections:

1. **Election Results Summary**
   - 2018 results (votes, %, candidates)
   - 2022 results (votes, %, candidates)
   - Turnout comparison (2018 vs 2022)

2. **Turnout Analysis & Swing Modelling**
   - Electorate growth (2018 → 2022 → 2026)
   - Turnout volatility (2018 vs 2022 → 2026 projection)
   - Vote share swing per party

3. **Turnout Sensitivity Modelling**
   - Low turnout (60%): Projected winner + margin
   - Medium turnout (68%): Competitive scenario
   - High turnout (75%): Projected winner + margin
   - Very high turnout (80%): Surge scenario

4. **Opposition Fragmentation Analysis**
   - Counterfactual: What if opposition consolidated?
   - BN's dependency on split math
   - Spoiler impact (which party, how much vote share)

5. **Demographic Shift Analysis**
   - Ethnic composition changes (2018 → 2026)
   - Youth vote share (Undi18 impact)
   - Incumbency factor analysis

All numerical claims must cite ElectionData.MY or SPR. Tag confidence: [HIGH/MEDIUM/LOW].
```

---

## 🗳️ Step 4: Master Operational Brief Synthesis ✅

**Input:** All three dimensional briefs (Steps 1-3)

**Output:** `n27-layang-layang-master-operational-brief-20260701.md`

**CVS Compliance:** ✅ Model assumptions explicit + `SPECULATION:` tags

### 📝 Prompt

```
You are a senior political intelligence strategist specializing in war room operational planning.

Synthesize the three dimensional briefs (demographics, candidates, historical) and generate a detailed and structured analytical report optimized for political intelligence operational applied use case: master operational brief for war room deployment.

**CVS Requirement:** All victory probability models must be prefixed with `SPECULATION:` and include explicit model assumptions (5+ points). Strategic assessments tagged [MEDIUM/LOW]. Reference all 3 input briefs.

Required sections:

1. **BLUF (Bottom Line Up Front)**
   - Seat status (BN-leaning/PH-upset/PN-spoiler)
   - Decisive variable (turnout/Malay split/Chinese consolidation)
   - 2026 projections (BN retention %, PH upset %, PN spoiler %)

2. **Strategic Guidance by Party**
   - PN strategy (core strategy, priority actions, key vulnerability, win condition)
   - PH strategy (core strategy, priority actions, key vulnerability, win condition)
   - BN strategy (core strategy, priority actions, key vulnerability, win condition)

3. **Risk Assessment**
   - High-risk scenarios (5 scenarios with trigger, impact, indicator, mitigation)
   - Key battleground indicators (5 critical metrics to watch)

4. **Actionable Intelligence**
   - Battleground PD tier classification (Tier 1/2/3 with tables)
   - GOTV priority matrix (per party: P1-P5 priorities)
   - Messaging framework (core narrative, key messages, attack lines, endorsements)
   - Victory probability model (SPECULATION: with assumptions + sensitivity table)
   - Early warning indicators (7 days before polling)
   - Operational checklist (all parties + party-specific)

All strategic claims must be backed by data from Steps 1-3. Tag confidence: [HIGH/MEDIUM/LOW].
```

---

## 🗳️ Step 5: GitHub Upload — Private Repository Creation ✅

**Input:** All 4 brief documents (Steps 1-4)

**Output:** Private GitHub repository with structured workspace

**CVS Compliance:** ✅ Pre-validation + structured documentation

### 📝 Prompt

```
You are a political intelligence operations specialist responsible for secure knowledge management and GitHub repository structuring.

Analyze all the information generated so far (Steps 1-4 briefs) and upload into a detailed and structured analytical workspace in a new private GitHub repository.

**CVS Requirement:** All files must pass truth validation before upload. Repository must include CVS compliance statement in README.

**Repository Naming Convention:** `analytical-dun-profiling-n{code}-{constituency-name}`
- Example: `analytical-dun-profiling-n27-layang-layang`
- Example: `analytical-dun-profiling-n16-sungai-balang`

**Required Repository Structure:**

```
analytical-dun-profiling-n{code}-{constituency-name}/
├── README.md
├── CVS-COMPLIANCE.md
├── briefs/
│   ├── n{code}-demographic-brief-YYYYMMDD.md
│   ├── n{code}-candidate-brief-YYYYMMDD.md
│   ├── n{code}-historical-brief-YYYYMMDD.md
│   └── n{code}-master-operational-brief-YYYYMMDD.md
├── data-sources/
│   ├── SPR-electoral-roll-sources.md
│   ├── candidate-news-sources.md
│   └── historical-data-sources.md
├── methodology/
│   ├── PD-tier-classification.md
│   ├── turnout-sensitivity-model.md
│   └── vote-split-dynamics.md
└── archives/
    └── (previous iterations if any)
```

**README.md Requirements:**
- Constituency overview (name, code, state, parliament)
- Election date (PRN Johor 2026, polling day)
- Contest type (3/4/5-cornered fight)
- Total electorate
- Key findings summary (BLUF from master brief)
- Links to all 4 briefs
- Last updated date

**CVS-COMPLIANCE.md Requirements:**
- Statement of CVS application at each step
- Source verification summary (Step 1: SPR primary, Step 2: multi-source, etc.)
- Confidence tag legend ([HIGH]/[MEDIUM]/[LOW])
- Speculation demarcation note (`SPECULATION:` prefix usage)
- Validation gate confirmation (all files passed `validate.sh`)

**Data Sources Files:**
- List all URLs + references used in Steps 1-3
- Include access dates
- Note any conflicting sources and resolution

**Methodology Files:**
- Document PD tier classification thresholds
- Explain turnout sensitivity modelling assumptions
- Describe vote split dynamics calculation

**Upload Steps:**
1. Create private GitHub repository with naming convention
2. Initialize with .gitignore (exclude sensitive data)
3. Upload all 4 brief documents to `briefs/` folder
4. Create README.md with constituency overview
5. Create CVS-COMPLIANCE.md with validation statement
6. Create data-sources/ documentation
7. Create methodology/ documentation
8. Commit with message: "Initial upload: N.{code} {constituency} complete 4-step analysis"
9. Set repository to private
10. Share repository URL with war room team

**Security Note:** Repository must be PRIVATE. Do not make electoral intelligence public.
```

---

## 📊 Current Status: Manual Workflow

### What's Automated ✅
- DeerFlow news collection (`collect_political_news_25sources_OPERATIONAL.py`)
- Entity extraction (PIR tagging)
- Signal quality grading (Loop 2 verification)
- Threshold escalation (ESC-001 to ESC-006)
- Daily brief generation (from news signals)

### What's Manual (OpenClaw Agent Sessions) ❌
- XLSX parsing → PD demographic tables
- Candidate profile synthesis from news sources
- Historical data analysis + swing modelling
- Master brief integration
- GitHub repository creation + structuring

### Gap Identified
**No Python script to automate Steps 1-5 from XLSX + news sources → markdown briefs + GitHub upload**

**Automation Priority:** HIGH — would reduce manual work by 60-70% per constituency

---

## 📚 Example Outputs

### N.27 Layang-Layang (Completed 2026-07-01) ✅ CVS-COMPLIANT
- `n27-layang-layang-demographic-brief-20260701.md` ✅
- `n27-layang-layang-candidate-brief-20260701.md` ✅
- `n27-layang-layang-historical-brief-20260701.md` ✅
- `n27-layang-layang-master-operational-brief-20260701.md` ✅
- **CVS Compliance:** 100% (all steps validated)

### N16 Sungai Balang (Completed 2026-06-29)
- `n16-sungai-balang-demographic-brief-20260629.md` ✅
- `n16-sungai-balang-candidate-demographic-brief-20260629.md` ✅
- `n16-sungai-balang-historical-performance-brief-20260629.md` ✅
- `n16-sungai-balang-master-operational-brief-20260629.md` ✅

### N17 Semerah (Completed 2026-06-27)
- `n17-semerah-demographic-brief-20260627.md` ✅
- `n17-semerah-candidate-demographic-brief-20260627.md` ✅
- `n17-semerah-historical-performance-brief-20260627.md` ✅
- `n17-semerah-master-operational-brief-20260627.md` ✅

### N32 Endau (Completed 2026-06-29)
- `n32-endau-demographic-brief-20260629.md` ✅
- `n32-endau-candidate-brief-20260629.md` ✅
- `n32-endau-historical-performance-brief-20260629.md` ✅

---

## 🔧 Automation Roadmap

### Phase 1: XLSX Parser (Priority: HIGH)
```python
# spr-xlsx-parser.py
- Read SPR Electoral Roll XLSX
- Extract PD-level data (Kod DM, voters, ethnicity, age, gender)
- Classify PDs into tiers
- Generate demographic brief markdown
- CVS: Cite SPR as primary source
```

### Phase 2: Candidate Profiler (Priority: MEDIUM)
```python
# candidate-profiler.py
- Scrape news sources for candidate announcements
- Extract candidate profiles (name, party, incumbency, background)
- Multi-source verification (≥2 sources)
- Map to demographic segments
- Generate candidate demographic brief markdown
- CVS: Tag single-source claims
```

### Phase 3: Historical Analyst (Priority: MEDIUM)
```python
# historical-analyst.py
- Fetch ElectionData.MY API (2018, 2022 results)
- Cross-reference with Wikipedia + SPR
- Calculate swing, turnout volatility, margin trends
- Model turnout sensitivity scenarios
- Generate historical performance brief markdown
- CVS: Use SPECULATION: prefix for projections
```

### Phase 4: Master Brief Synthesizer (Priority: LOW)
```python
# master-brief-synthesizer.py
- Read all three dimensional briefs
- Synthesize into master operational brief
- Generate strategic guidance, risk assessment, actionable intel
- CVS: Add model assumptions + confidence tags
```

### Phase 5: GitHub Uploader (Priority: LOW)
```python
# github-repo-creator.py
- Create private GitHub repository
- Generate README.md + CVS-COMPLIANCE.md
- Upload all 4 briefs with structured folders
- Create data-sources/ and methodology/ documentation
- Set repository to private
- Share URL with war room team
```

**Target:** Automate 80% of manual work → reduce time per constituency from 2 hours to 25 minutes

---

## 🛡️ Security & Classification

**All DUN profiling outputs:**
- **Classification:** TLP:AMBER (Operational Use — Do Not Distribute Publicly)
- **GitHub Repositories:** PRIVATE only
- **Access:** War room team members only
- **Retention:** Archive post-election (retain for historical analysis)

---

**Document Version:** 2.0 (Updated with Step 5 + CVS compliance)  
**Last Updated:** 2026-07-01 06:15 UTC  
**Maintainer:** Political Intelligence Team  
**Status:** Manual workflow documented, automation roadmap defined, CVS-compliant
