# DUN Profiling V1 — Workflow Schema

**Version:** 1.0  
**Status:** ✅ Production  
**Last Updated:** 2026-07-01  
**Maintainer:** Political Intelligence Team

---

## 📋 Overview

This document defines the input/output schemas, data structures, and validation rules for the DUN Profiling V1 workflow.

---

## 🗳️ Workflow Pipeline

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        DUN PROFILING V1 PIPELINE                            │
└─────────────────────────────────────────────────────────────────────────────┘

  ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
  │   Step 1     │     │   Step 2     │     │   Step 3     │
  │ Demographics │     │  Candidates  │     │  Historical  │
  │              │     │              │     │              │
  │ Input:       │     │ Input:       │     │ Input:       │
  │ SPR XLSX     │     │ News +       │     │ ElectionData │
  │              │     │ Nominations  │     │ + SPR        │
  └──────┬───────┘     └──────┬───────┘     └──────┬───────┘
         │                   │                     │
         ▼                   ▼                     ▼
  ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
  │ {code}-      │     │ {code}-      │     │ {code}-      │
  │ demographic- │     │ candidate-   │     │ historical-  │
  │ brief.md     │     │ brief.md     │     │ brief.md     │
  └──────┬───────┘     └──────┬───────┘     └──────┬───────┘
         │                   │                     │
         └───────────────────┼─────────────────────┘
                             │
                             ▼
                    ┌────────────────┐
                    │    Step 4      │
                    │   Synthesis    │
                    │                │
                    │ Input: Steps   │
                    │ 1-3 briefs     │
                    └───────┬────────┘
                            │
                            ▼
                    ┌────────────────┐
                    │ {code}-master- │
                    │ operational-   │
                    │ brief.md       │
                    └───────┬────────┘
                            │
                            ▼
                    ┌────────────────┐
                    │    Step 5      │
                    │  GitHub Upload │
                    │                │
                    │ Input: All 4   │
                    │ briefs         │
                    └───────┬────────┘
                            │
                            ▼
                    ┌────────────────┐
                    │ GitHub Repo:   │
                    │ analytical-dun │
                    │ -profiling-nXX │
                    └────────────────┘
```

---

## 📥 Step 1: Demographics — Input/Output Schema

### Input Schema

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `spr_xlsx_file` | string | ✅ | Path to SPR Electoral Roll XLSX file |
| `constituency_code` | string | ✅ | DUN code (e.g., `N16`, `N27`) |
| `constituency_name` | string | ✅ | Full constituency name (e.g., `Sungai Balang`) |
| `state` | string | ✅ | State name (e.g., `Johor`) |
| `parliament_code` | string | ✅ | Linked parliament code (e.g., `P146`) |

**Example Input:**
```yaml
spr_xlsx_file: /home/p62operator/data/spr/8_SUNGAI_BALANG_as_of_190626.xlsx
constituency_code: N16
constituency_name: Sungai Balang
state: Johor
parliament_code: P146
```

### Output Schema (`{code}-demographic-brief-{YYYYMMDD}.md`)

```markdown
# N{code} {Constituency Name} — Demographic Brief

**Generated:** {YYYY-MM-DD HH:MM UTC}  
**Source:** SPR Electoral Roll 2026  
**CVS Status:** ✅ Primary source verified

---

## 1. Constituency Overview

| Metric | Value |
|--------|-------|
| Total Voters | {integer} |
| Male Voters | {integer} ({percentage}%) |
| Female Voters | {integer} ({percentage}%) |
| Malay Voters | {integer} ({percentage}%) |
| Chinese Voters | {integer} ({percentage}%) |
| Indian Voters | {integer} ({percentage}%) |
| Other Voters | {integer} ({percentage}%) |
| Youth (18-29) | {integer} ({percentage}%) |
| OKU Voters | {integer} |

---

## 2. PD Tier Classification

### Tier 1: Malay Super Safe (≥80% Malay)
| PD Code | PD Name | Malay % | Chinese % | Indian % | Total Voters |
|---------|---------|---------|-----------|----------|--------------|
| {code}  | {name}  | {pct}   | {pct}     | {pct}    | {count}      |

### Tier 2: Malay Safe (60-79% Malay)
...

### Tier 3: Mixed (40-59% Malay)
...

### Tier 4: Chinese Safe (≥60% Chinese)
...

---

## 3. PD-Level Breakdown (All PDs)

| PD Code | PD Name | Total | Malay | Chinese | Indian | Youth | Turnout 2022 |
|---------|---------|-------|-------|---------|--------|-------|--------------|
| {code}  | {name}  | {n}   | {pct} | {pct}   | {pct}  | {pct} | {pct}        |

---

## 4. Youth Concentration Analysis

**Top 5 PDs by Youth Voters (18-29):**

| Rank | PD Code | PD Name | Youth Count | Youth % |
|------|---------|---------|-------------|---------|
| 1    | {code}  | {name}  | {count}     | {pct}   |

---

## 5. Strategic Assessment

**BN Advantages:** [HIGH/MEDIUM/LOW confidence]
- ...

**PH Advantages:** [HIGH/MEDIUM/LOW confidence]
- ...

**PN Advantages:** [HIGH/MEDIUM/LOW confidence]
- ...

**Decisive Segments:**
- ...
```

### Validation Rules

- ✅ All voter counts must sum to total electorate
- ✅ All ethnicity percentages must sum to ~100% (±0.5% tolerance)
- ✅ All PD codes must match SPR XLSX exactly
- ✅ Youth percentage must be calculated from age distribution
- ✅ CVS citation required: "SPR Electoral Roll 2026"

---

## 📥 Step 2: Candidates — Input/Output Schema

### Input Schema

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `constituency_code` | string | ✅ | DUN code |
| `constituency_name` | string | ✅ | Full name |
| `nomination_date` | date | ✅ | Nomination day date |
| `nomination_centre` | string | ✅ | Nomination centre location |
| `news_sources` | array | ✅ | List of news URLs for candidate announcements |
| `party_sources` | array | ✅ | List of party announcement URLs |

**Example Input:**
```yaml
constituency_code: N16
constituency_name: Sungai Balang
nomination_date: 2026-06-27
nomination_centre: Dewan Serbaguna, Sungai Balang
news_sources:
  - https://www.sinarharian.com.my/article/...
  - https://www.bernama.com/bm/...
party_sources:
  - https://umno-online.my/...
  - https://pkrr.com.my/...
```

### Output Schema (`{code}-candidate-brief-{YYYYMMDD}.md`)

```markdown
# N{code} {Constituency Name} — Candidate Brief

**Generated:** {YYYY-MM-DD HH:MM UTC}  
**Nomination Date:** {YYYY-MM-DD}  
**Nomination Centre:** {location}  
**CVS Status:** ✅ Multi-source verified

---

## 1. Candidate Roll Confirmation

| Party | Candidate | Age | Incumbent | Nomination Status |
|-------|-----------|-----|-----------|-------------------|
| BN    | {name}    | {n} | Yes/No    | ✅ Confirmed      |
| PH    | {name}    | {n} | Yes/No    | ✅ Confirmed      |
| PN    | {name}    | {n} | Yes/No    | ✅ Confirmed      |

**Contest Type:** {Three/Four/Five}-cornered fight

---

## 2. Candidate Profile Cards

### {Candidate Name} ({Party})

| Attribute | Value |
|-----------|-------|
| Full Name | {name} |
| Age | {n} |
| Party | {party} |
| Position | {position} |
| Incumbent | Yes/No |
| 2022 Performance | {votes} ({pct}%) |
| Education | {degree/diploma} |
| Professional Background | {career} |
| Political Experience | {roles} |
| Family Connections | {dynasty/alliances} |
| Social Media | {platforms} |

**Core Advantages:**
- ...

**Key Vulnerabilities:**
- ...

---

## 3. Demographic Alignment Matrix

| Candidate | Rural Malay | Urban Malay | Chinese | Indian | Youth | Women |
|-----------|-------------|-------------|---------|--------|-------|-------|
| {Name}    | Strong/Mod/Weak | ... | ... | ... | ... | ... |

---

## 4. Vote Projections (Baseline Scenario)

| Candidate | Projected Vote % | Projected Votes | Path to Victory |
|-----------|------------------|-----------------|-----------------|
| {Name}    | {pct}%           | {votes}         | {description}   |

---

## 5. Vote Split Dynamics

**Opposition Fragmentation Math:**
- Combined opposition vote: {votes} ({pct}%)
- Incumbent vote: {votes} ({pct}%)
- Spoiler impact: {description}

**Turnout Sensitivity:**
- Low turnout (60%): Favors {party}
- High turnout (75%): Favors {party}
```

### Validation Rules

- ✅ All candidate names verified via ≥2 sources
- ✅ All party affiliations confirmed via official party announcements
- ✅ Single-source claims tagged [MEDIUM] or [LOW]
- ✅ All sources cited with URLs
- ✅ Speculative assessments tagged with confidence level

---

## 📥 Step 3: Historical — Input/Output Schema

### Input Schema

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `constituency_code` | string | ✅ | DUN code |
| `electiondata_api_key` | string | ✅ | ElectionData.MY API key |
| `include_2018` | boolean | ✅ | Include 2018 results |
| `include_2022` | boolean | ✅ | Include 2022 results |
| `include_byelections` | boolean | ❌ | Include byelection history |

**Example Input:**
```yaml
constituency_code: N16
electiondata_api_key: ${ELECTIONDATA_API_KEY}
include_2018: true
include_2022: true
include_byelections: false
```

### Output Schema (`{code}-historical-brief-{YYYYMMDD}.md`)

```markdown
# N{code} {Constituency Name} — Historical Performance Brief

**Generated:** {YYYY-MM-DD HH:MM UTC}  
**Sources:** ElectionData.MY, SPR, Wikipedia  
**CVS Status:** ✅ Cross-referenced

---

## 1. Election Results Summary

### GE15 / PRN 2022 Results

| Candidate | Party | Votes | % | +/- from 2018 |
|-----------|-------|-------|---|---------------|
| {Name}    | {Party} | {n} | {pct}% | {delta}% |

**Winner:** {Name} ({Party})  
**Majority:** {votes} votes ({pct}% margin)  
**Turnout:** {pct}% ({n} voters)

### GE14 / PRN 2018 Results

...

---

## 2. Turnout Analysis & Swing Modelling

| Election | Registered Voters | Turnout % | Votes Cast |
|----------|-------------------|-----------|------------|
| 2018     | {n}               | {pct}%    | {n}        |
| 2022     | {n}               | {pct}%    | {n}        |
| 2026 (Proj.) | {n}           | {pct}%    | {n}        |

**Swing Analysis:**
- BN swing: {+/-pct}%
- PH swing: {+/-pct}%
- PN swing: {+/-pct}%

---

## 3. Turnout Sensitivity Modelling

SPECULATION: Turnout scenarios based on 2018-2022 patterns

| Turnout | Projected Winner | Margin | Key Assumptions |
|---------|------------------|--------|-----------------|
| 60% (Low) | {Party} | {votes} | Rural base mobilized |
| 68% (Med) | {Party} | {votes} | Mixed turnout |
| 75% (High) | {Party} | {votes} | Youth surge |
| 80% (V.High) | {Party} | {votes} | Anti-incumbent wave |

---

## 4. Opposition Fragmentation Analysis

**Counterfactual Scenario:**
- If opposition consolidated: {Party} would win/lose
- BN dependency on split: {votes} vote cushion
- Spoiler impact: {Party} spoils {Party} by {votes}

---

## 5. Demographic Shift Analysis

**Electorate Changes (2018 → 2026):**
- Total growth: +{n} voters (+{pct}%)
- Malay share: {pct}% → {pct}%
- Chinese share: {pct}% → {pct}%
- Youth share (Undi18): {pct}% → {pct}%
```

### Validation Rules

- ✅ All election results cross-referenced (≥2 sources)
- ✅ Turnout figures verified across sources
- ✅ Projections marked [LOW] confidence with assumptions stated
- ✅ All scenario modelling prefixed with `SPECULATION:`

---

## 📥 Step 4: Synthesis — Input/Output Schema

### Input Schema

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `demographic_brief` | string | ✅ | Path to Step 1 output |
| `candidate_brief` | string | ✅ | Path to Step 2 output |
| `historical_brief` | string | ✅ | Path to Step 3 output |
| `war_room_team` | array | ❌ | List of team members for TLP marking |

**Example Input:**
```yaml
demographic_brief: /home/p62operator/memory/n16-sungai-balang-demographic-brief-20260627.md
candidate_brief: /home/p62operator/memory/n16-sungai-balang-candidate-brief-20260627.md
historical_brief: /home/p62operator/memory/n16-sungai-balang-historical-brief-20260627.md
war_room_team:
  - @user1
  - @user2
```

### Output Schema (`{code}-master-operational-brief-{YYYYMMDD}.md`)

```markdown
# N{code} {Constituency Name} — Master Operational Brief

**Generated:** {YYYY-MM-DD HH:MM UTC}  
**Classification:** TLP:AMBER  
**CVS Status:** ✅ Model assumptions explicit

---

## 1. BLUF (Bottom Line Up Front)

**Seat Status:** {BN-leaning/PH-upset/PN-spoiler}  
**Decisive Variable:** {turnout/Malay split/Chinese consolidation}  
**2026 Projections:**
- BN retention probability: {pct}%
- PH upset probability: {pct}%
- PN spoiler probability: {pct}%

---

## 2. Strategic Guidance by Party

### PN Strategy
- **Core Strategy:** {description}
- **Priority Actions:** {list}
- **Key Vulnerability:** {description}
- **Win Condition:** {description}

### PH Strategy
...

### BN Strategy
...

---

## 3. Risk Assessment

### High-Risk Scenarios

| Scenario | Trigger | Impact | Indicator | Mitigation |
|----------|---------|--------|-----------|------------|
| {name}   | {event} | {level} | {metric}  | {action}   |

### Key Battleground Indicators
1. {indicator}
2. {indicator}
3. {indicator}
4. {indicator}
5. {indicator}

---

## 4. Actionable Intelligence

### Battleground PD Tier Classification

**Tier 1 (Critical):**
| PD Code | PD Name | Total Voters | Key Demographic | Priority |
|---------|---------|--------------|-----------------|----------|

**Tier 2 (Important):**
...

### GOTV Priority Matrix

| Party | P1 | P2 | P3 | P4 | P5 |
|-------|----|----|----|----|----|
| BN    | {action} | {action} | {action} | {action} | {action} |
| PH    | {action} | {action} | {action} | {action} | {action} |
| PN    | {action} | {action} | {action} | {action} | {action} |

### Messaging Framework

| Party | Core Narrative | Key Messages | Attack Lines | Endorsements |
|-------|----------------|--------------|--------------|--------------|
| BN    | {narrative}    | {messages}   | {attacks}    | {endorsers}  |
| PH    | {narrative}    | {messages}   | {attacks}    | {endorsers}  |
| PN    | {narrative}    | {messages}   | {attacks}    | {endorsers}  |

### Victory Probability Model

SPECULATION: Model based on demographic alignment + historical patterns + candidate strength

**Assumptions:**
1. {assumption}
2. {assumption}
3. {assumption}
4. {assumption}
5. {assumption}

**Sensitivity Table:**

| Variable | Change | BN Win % | PH Win % | PN Win % |
|----------|--------|----------|----------|----------|
| Turnout | +5% | {pct}% | {pct}% | {pct}% |
| Malay Split | PN +5% | {pct}% | {pct}% | {pct}% |
| Chinese Turnout | +10% | {pct}% | {pct}% | {pct}% |

### Early Warning Indicators (7 Days Before Polling)
- {indicator}
- {indicator}
- {indicator}

### Operational Checklist

**All Parties:**
- [ ] {task}
- [ ] {task}

**BN-Specific:**
- [ ] {task}

**PH-Specific:**
- [ ] {task}

**PN-Specific:**
- [ ] {task}
```

### Validation Rules

- ✅ All strategic claims backed by data from Steps 1-3
- ✅ Victory probability models prefixed with `SPECULATION:`
- ✅ Model assumptions explicitly listed (≥5 points)
- ✅ All confidence tags applied [HIGH/MEDIUM/LOW]
- ✅ Sources reference all 3 input briefs

---

## 📥 Step 5: GitHub Upload — Input/Output Schema

### Input Schema

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `brief_files` | array | ✅ | List of 4 brief file paths |
| `github_token` | string | ✅ | GitHub PAT with repo scope |
| `repo_visibility` | string | ✅ | `private` or `public` |
| `war_room_team` | array | ❌ | GitHub usernames for collaborator access |
| `tlp_marking` | string | ✅ | TLP classification (AMBER/RED/GREEN) |

**Example Input:**
```yaml
brief_files:
  - /home/p62operator/memory/n16-demographic-brief-20260627.md
  - /home/p62operator/memory/n16-candidate-brief-20260627.md
  - /home/p62operator/memory/n16-historical-brief-20260627.md
  - /home/p62operator/memory/n16-master-operational-brief-20260627.md
github_token: ${GITHUB_TOKEN}
repo_visibility: private
war_room_team:
  - user1
  - user2
tlp_marking: TLP:AMBER
```

### Output Schema (GitHub Repository Structure)

```
analytical-dun-profiling-n{code}-{constituency-name}/
├── README.md
├── CVS-COMPLIANCE.md
├── data-sources/
│   └── source-registry.md
├── methodology/
│   └── three-dimensional-framework.md
├── briefs/
│   ├── 01-demographic-brief.md
│   ├── 02-candidate-brief.md
│   ├── 03-historical-brief.md
│   └── 04-master-operational-brief.md
├── raw-data/
│   └── (SPR XLSX reference, not uploaded)
└── .gitignore
```

### Repository README Template

```markdown
# N{code} {Constituency Name} — Political Intelligence Package

**Classification:** {TLP:AMBER/RED/GREEN}  
**Generated:** {YYYY-MM-DD}  
**Workflow:** DUN Profiling V1 (Three-Dimensional Analysis)  
**CVS Status:** ✅ Validated

---

## 📁 Repository Structure

| Directory | Contents |
|-----------|----------|
| `briefs/` | Four intelligence briefs (demographic, candidate, historical, master) |
| `data-sources/` | Source registry with citations |
| `methodology/` | Three-dimensional framework documentation |
| `raw-data/` | Reference to source data (not uploaded) |

---

## 📊 Brief Documents

| Brief | Description | File |
|-------|-------------|------|
| Demographic | PD-level voter composition, tier classification | `briefs/01-demographic-brief.md` |
| Candidate | Candidate profiles, demographic alignment | `briefs/02-candidate-brief.md` |
| Historical | Election results, turnout sensitivity, swing analysis | `briefs/03-historical-brief.md` |
| Master Operational | Integrated war room guidance | `briefs/04-master-operational-brief.md` |

---

## 🔒 Access Control

**Collaborators:**
- @{user1}
- @{user2}

**TLP Marking:** {TLP:AMBER} — Distribution limited to war room team only.

---

## ✅ CVS Compliance

All documents in this repository have passed the Core Truth Validation System:
- Tier 1 claims (numbers, names, dates) verified via ≥2 sources
- Confidence tags applied to all analytical claims
- Speculative claims prefixed with `SPECULATION:` or `SCENARIO:`
- Source citations included for all factual claims

See `CVS-COMPLIANCE.md` for full validation report.
```

### Validation Rules

- ✅ All files pass truth validation before upload
- ✅ Repository README includes CVS compliance statement
- ✅ TLP marking clearly displayed
- ✅ Collaborator access configured correctly
- ✅ .gitignore excludes sensitive data (API keys, credentials)

---

## 🔧 Error Handling

| Error Code | Description | Resolution |
|------------|-------------|------------|
| `ERR-SPX-001` | SPR XLSX file not found | Verify file path, check file permissions |
| `ERR-SPX-002` | XLSX parsing failed (format change) | Contact SPR, update parser for new format |
| `ERR-CVS-001` | Tier 1 claim lacks source citation | Add source citation, re-run validator |
| `ERR-CVS-002` | Confidence tag missing on analytical claim | Add [HIGH/MEDIUM/LOW] tag |
| `ERR-CVS-003` | Speculation not prefixed | Add `SPECULATION:` or `SCENARIO:` prefix |
| `ERR-GH-001` | GitHub repo creation failed | Verify token permissions, check rate limits |
| `ERR-GH-002` | Collaborator invite failed | Verify username, check team membership |

---

## 📊 Metrics & KPIs

| Metric | Target | Current |
|--------|--------|---------|
| Time per constituency (manual) | <2 hours | ~2 hours |
| Time per constituency (automated) | <25 minutes | N/A (not built) |
| CVS compliance rate | 100% | 100% (completed seats) |
| GitHub upload success rate | 100% | 100% (1/1 tested) |
| Brief document completeness | 100% | 100% (4/4 seats) |

---

**Document Control:**
- Version: 1.0
- Status: Production
- Next Review: 2026-07-15
