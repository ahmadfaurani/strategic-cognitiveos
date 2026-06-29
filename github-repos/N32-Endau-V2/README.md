# N.32 Endau (P.154 Mersing) — Political Intelligence Repository

**Johor State Election 2026** | **Four-Cornered Fight** | **BN-Favoring Contestable Seat**

**⚠️ CORRECTIONS APPLIED (2026-06-29):** Historical results updated per DAF feedback. PH ceiling revised from 25% to 12–15%. Strategy shifted to long-game positioning for 2030.

---

## 📊 Executive Summary

**N.32 Endau** is a Malay super-majority rural seat (79.6% Malay, 28,767 voters) within P.154 Mersing, Johor. The 2026 contest features a four-cornered fight with significant strategic complexity:

| Party | Candidate | Status | Vote Projection (CORRECTED) |
|-------|-----------|--------|-----------------------------|
| **BN-UMNO** | Alwiyah Talib | Incumbent (won 2018 BN, 2022 PN) | 48% (8,975 votes) |
| **PH-PKR** | Saiful Nizam Samat | Unity Government candidate | **13% (2,431 votes)** — CORRECTED from 23% |
| **PN** | Hasnul Hakimi Hussien | New candidate (no incumbent) | 24% (4,488 votes) |
| **ASLI** | Jati Awang | OA representation (electoral debut) | 5% (935 votes) |

**Bottom Line:** BN enters as **strong favorite** (70–75% retention probability). Alwiyah's incumbency + name recognition + return to UMNO consolidates position. PN weakened without incumbent. **PH faces structural ceiling of 12–15%** (Chinese + OA insufficient without Malay vote). ASLI could be spoiler in tight race.

---

## 📜 Historical Results (CORRECTED 2026-06-29)

### 2022 State Election (Standalone, Low Turnout)

| Party | Candidate | Votes | Share | Note |
|-------|-----------|-------|-------|------|
| **PN (BERSATU)** | Alwiyah Talib | **8,433** | **50.2%** | **WINNER** |
| **BN (UMNO)** | Mohd Youzaimi Yusof | 5,392 | 32.1% | Runner-up |
| **PH (AMANAH)** | (Candidate) | **1,154** | **6.9%** | Distant third |
| **Other 1** | — | ~600 | ~3.6% | |
| **Other 2** | — | ~600 | ~3.6% | |
| **Total Valid Votes** | | ~16,800 | | |
| **Turnout** | | **55%** | | Low (standalone state election) |
| **Majority** | | **3,041 votes** | | Alwiyah (PN) over BN |

**Corrections Applied:**
- ✅ PH got **6.9% (1,154 votes)**, not 12.4% — AMANAH candidate, not PKR
- ✅ BN candidate was **Mohd Youzaimi Yusof**, not "Mohd Fared Mohd Khalid"
- ✅ Five-cornered fight, not four
- ✅ Turnout was **55%**, majority was **3,041 votes**

### 2018 State Election (GE14 Coattails, High Turnout)

| Party | Candidate | Result | Note |
|-------|-----------|--------|------|
| **BN (UMNO)** | Alwiyah Talib | **Won** | First term |
| **Turnout** | | **78%** | High (GE year) — not 82% |
| **Majority** | | **Larger than 2022** | Alwiyah won comfortably |

---

## ⚠️ Strategic Corrections (DAF Feedback 2026-06-29)

### Problem 1: PH's 25% Target Is Structurally Impossible

**Original Assumption (WRONG):**
- PH targets 25% (~4,500–5,000 votes)
- Plan focuses heavily on Chinese vote maximization
- Malay heartland treated as "barely worth showing up to"

**Reality (CORRECTED):**
- Chinese (13.4%) + OA (4.9%) = **18.3% of seat maximum** even at 100% turnout + 100% support
- PH got **6.9% in 2022** (1,154 votes)
- Targeting 25% requires **3x growth** in one election cycle — structurally impossible
- **Seat is 79.6% Malay** — won/lost on Malay vote split
- **Corrected PH ceiling:** 12–15% (2,500–3,500 votes) — already ambitious 2x growth

### Problem 2: Anti-Defection Sentiment Benefits PN, Not PH

**Original Assumption (WRONG):**
- Alwiyah's party-switching hurts BN
- Anti-defection voters will support PH

**Reality (CORRECTED):**
- Alwiyah's switching hurts **PN** (she left them), not PH
- Malay voters fed up with her switching will go to **PAS/PN**, not PH
- PH has **no Malay base** to absorb anti-defection sentiment
- PAS is the natural recipient of Malay protest vote

### Problem 3: Plan Is Too Heavy for a Lost Cause

**Original Approach (WRONG):**
- Resource-intensive campaign
- Chinese-focused strategy
- Assumes 25% ceiling
- Implicitly treats seat as "winnable with perfect conditions"

**Corrected Approach:**
- **Acknowledge reality:** BN has 70–75% retention probability
- **Lighter presence:** Lock in Chinese + mixed votes quietly
- **Long-game strategy:**
  - Run decent candidate for name recognition **next time**
  - Use campaign to **learn Malay areas properly** for future run
  - "Keep a presence," "build for next time"
  - **2026 is about positioning for 2030**, not winning 2026

---

## 🗺️ Seat Classification

**Tier:** Tier-2 Contestable (BN-leaning)  
**Ethnic Structure:** Malay super-majority (79.6%)  
**Decisive Variables:**
1. Malay vote split (BN vs PN)
2. Alwiyah personal vote retention (60–70% of 2022 PN voters?)
3. Chinese turnout (PH needs 75%+ in concentrated PDs)
4. OA consolidation (ASLI could take 60–70% of 4.9% OA vote)

---

## 📁 Repository Structure

```
N32-Endau-V2/
├── README.md                          # This file (CORRECTED 2026-06-29)
├── data/
│   ├── demographics.json              # Ethnic, age, gender breakdown
│   ├── polling-districts.json         # 20 PD detailed data
│   ├── candidates.json                # Candidate profiles
│   └── historical-results.json        # 2018, 2022 election results (CORRECTED)
├── analysis/
│   ├── tier-strategy.md               # PD tier classification + strategy
│   ├── vote-projections.md            # 5 scenarios with math (CORRECTED PH ceilings)
│   ├── party-playbooks.md             # BN/PH/PN/ASLI strategic playbooks (PH corrected)
│   └── critical-dynamics.md           # Malay split, OA swing, FELDA factor
├── monitoring/
│   ├── watch-metrics.md               # Pre-nomination to post-election tracking
│   ├── signal-registry.md             # DeerFlow signal integration
│   └── pd-targets.md                  # PD-level vote targets
├── docs/
│   ├── methodology.md                 # Data sources, validation, confidence levels
│   └── truth-validation.md            # CVS compliance checklist
└── assets/
    └── maps/                          # (Future: PD maps, demographic visualizations)
```

---

## 🔑 Key Findings

### Demographics (Source: SPR Electoral Roll, 2026-06-19)

- **Total Voters:** 28,767 (20 polling districts)
- **Malay:** 22,911 (79.6%) — Seat won/lost on Malay vote
- **Chinese:** 3,858 (13.4%) — Hyper-concentrated in 3 PDs (62.2% in top 3)
- **Orang Asli:** 1,411 (4.9%) — 96% in 4 PDs (swing kingmaker)
- **Youth (18–30):** 8,084 (28.1%) — Exceeds typical victory margin
- **Under-45:** 17,638 (61.3%) — Generational politics matters

### Polling District Tiers

| Tier | PDs | Voters | Malay % | Strategic Role |
|------|-----|--------|---------|----------------|
| **TIER-1A** (Chinese-Majority) | 1 | 3,048 | 43.2% | PH ceiling foundation |
| **TIER-1B** (Mixed 20–40% Chinese) | 2 | 2,491 | 66.4% | Battleground |
| **TIER-2** (Mixed/OA Swing) | 5 | 7,113 | 69.5% | True battleground (19% OA) |
| **TIER-3A** (Deep Rural Malay >95%) | 8 | 6,558 | 98.2% | BN firewall |
| **TIER-3B** (Rural Malay 85–95%) | 6 | 9,557 | 88.9% | BN base, competitive |

### Critical Dynamics

1. **Alwiyah Personal Vote:** Won 2018 (BN) + 2022 (PN). How many 2022 voters follow her back to BN?
   - 60–70% retention = BN comfortable win (4,000+ margin)
   - 30–40% retention = PN spoiler, BN margin compressed

2. **OA Consolidation:** Jati Awang (ASLI) could take 60–70% of OA vote (800–950 votes)
   - In tight race (<1,500 margin), this is decisive
   - Most likely impacts BN (traditional patron) + PN

3. **Chinese Turnout:** PH needs 75–80% in Bandar Endau Utara (53.9% Chinese)
   - Target: 1,300–1,400 votes from this PD alone
   - **Without Malay penetration, PH ceiling is ~12–15%, not 25%**

4. **FELDA Factor:** Rancangan FELDA Endau (1,137 voters, 98.9% Malay)
   - Economically sensitive (commodity prices, land rights)
   - Protest vote risk for BN if federal policy unpopular

---

## 🎯 Vote Projection Scenarios (CORRECTED)

### Base Case (50–55% Probability) — CORRECTED

**Turnout:** 65% (18,699 votes)

| Party | Votes | Share | Margin | Note |
|-------|-------|-------|--------|------|
| BN | 8,975 | 48% | — | Alwiyah personal vote + UMNO base |
| PN | 4,488 | 24% | -4,487 | Retains core without incumbent |
| **PH** | **2,431** | **13%** | -6,544 | **CORRECTED from 23%** — Chinese 75%+, minimal Malay |
| ASLI | 935 | 5% | -8,040 | OA consolidation |
| **Others/Residual** | **1,870** | **10%** | — | Low-turnout PDs, split votes |

**Outcome:** BN wins comfortably (4,487 margin over PN). **PH is not a contender** — race is BN vs PN.

---

### Contestable Scenario (15–20% Probability) — CORRECTED

**Turnout:** 70% (20,137 votes)

| Party | Votes | Share | Margin | Note |
|-------|-------|-------|--------|------|
| BN | 8,860 | 44% | — | Alwiyah underperforms |
| PN | 5,236 | 26% | -3,624 | Anti-defection narrative resonates |
| **PH** | **3,021** | **15%** | -5,839 | **CORRECTED from 25%** — Optimistic but achievable |
| ASLI | 1,007 | 5% | -7,853 | OA consolidation |
| **Others/Residual** | **2,013** | **10%** | — | |

**Outcome:** BN wins but margin compressed (3,624 over PN). **PH still third place** — ceiling is 15% even in optimistic scenario.

---

### Tight Race / ASLI Spoiler (10–15% Probability) — CORRECTED

**Turnout:** 70% (20,137 votes)

| Party | Votes | Share | Margin | Note |
|-------|-------|-------|--------|------|
| BN | 8,458 | 42% | — | Significant Malay leakage |
| PN | 5,638 | 28% | -2,820 | Exceeds 2022 base |
| **PH** | **2,819** | **14%** | -5,639 | **CORRECTED from 24%** — Strong Chinese turnout |
| ASLI | 1,208 | 6% | -7,250 | Spoiler threshold exceeded |
| **Others/Residual** | **2,014** | **10%** | — | |

**Outcome:** BN wins narrowly (2,820 margin over PN). **ASLI >5% acts as spoiler**. **PH is irrelevant to outcome** — race is BN vs PN with ASLI spoiler.

---

## 📋 Party Strategic Playbooks (CORRECTED)

### BN (Alwiyah) — Incumbency + Personal Vote

**Objective:** Win with 4,000+ margin (48–52% share)

**Priorities:**
1. Hold rural Malay base (TIER-3A/B) — 60–65% vote share
2. Retain 60–70% of 2022 personal voters
3. Limit OA defection to ASLI — 25–35% OA vote
4. Damage limitation in Chinese PDs — 30–35% share

**Risk Factors:** PN >30% Malay vote, ASLI >5%, PH Chinese turnout >75%

**Retention Probability:** 70–75% `[HIGH]`

---

### PH (Saiful) — Realistic Ceiling + Long Game (CORRECTED)

**Objective:** Achieve 12–15% (2,500–3,500 votes), build for 2030

**⚠️ Strategic Reality Check:**
- **2022 Result:** PH got **6.9% (1,154 votes)**, not 12.4%
- **25% target is structurally impossible:** Chinese + OA = 18.3% of seat even at 100% turnout
- **Malay vote is decisive (79.6%):** PH cannot reach 25% without 15–20% Malay support
- **Anti-defection sentiment benefits PN, not PH:** Malay voters fed up with Alwiyah switching go to PAS, not PH
- **Appropriate strategy:** Lighter presence, lock in Chinese + mixed votes, build Malay relationships for **next cycle**

**Priorities:**
1. **Lock In Chinese Vote (TIER-1A — Bandar Endau Utara, 3,048 voters):**
   - Target: 80%+ turnout (2,440 votes cast)
   - Target: 80–85% partisan support (1,950–2,075 votes)
   - **This is PH's ceiling foundation**

2. **Competitive Presence in Mixed PDs (TIER-1B + TIER-2 — 9,604 voters):**
   - Target: 15–20% vote share (1,440–1,920 votes)
   - **Purpose:** Relationship-building for 2030, not 2026 win play

3. **Show Up in Malay Heartland (TIER-3A/B — 16,115 voters):**
   - Target: 8–12% vote share (1,290–1,935 votes)
   - **Purpose:** Name recognition, future groundwork
   - **Critical:** "Show up" mentality — don't write off 79.6% of seat

4. **OA Engagement (4 OA PDs — 1,411 voters):**
   - Target: 20–25% OA vote (280–350 votes)
   - **Note:** ASLI is main competitor here, not BN/PN

**Revised Vote Target:** 12–15% (2,500–3,500 votes) `[MEDIUM]`
- Chinese vote (80% turnout, 80% partisan): ~2,200–2,600 votes
- Malay vote (mixed PDs, 10–15% penetration): ~300–600 votes
- OA vote (20–25% consolidation): ~280–350 votes

**Long-Game Strategy:**
- **2026:** Establish presence, exceed 2022's 6.9%, build name recognition
- **2026–2030:** Maintain constituency office, continuous engagement in Malay PDs
- **2030:** Position for competitive run if demographic/political shifts favor PH

**Upset Probability:** <5% `[HIGH]` — Structurally impossible without Malay wave

---

### PN (Hasnul) — Rebuild Without Incumbent

**Objective:** Retain core base, exceed 20% (spoiler role)

**Priorities:**
1. Hold core PN supporters (25–30% in TIER-3A/B)
2. Retain 30–40% of 2022 Alwiyah-PN voters
3. Compete in mixed PDs (20–25%)
4. Anti-defection narrative ("Principles over personalities")

**Realistic:** 22–26% (4,900–5,900 votes) — compresses BN margin

**Spoiler Probability:** 60–70% `[MEDIUM]` — Can compress BN margin, cannot win

---

### ASLI (Jati) — Representation + Spoiler

**Objective:** Achieve 5%+ (symbolic + spoiler threshold)

**Priorities:**
1. Consolidate OA vote (60–70% in 4 OA PDs) — 815–950 votes
2. Expand to mixed OA PDs (Kampung Hubong)
3. Sympathy votes from non-OA progressives (200–300)

**Realistic:** 4–6% (900–1,350 votes) — spoiler in tight race

**Spoiler Probability:** 40–50% `[LOW]` — Depends on OA turnout + consolidation

---

## ⚠️ Critical Watch Metrics

### Pre-Nomination to Campaign

- [ ] Rally sizes (Alwiyah vs. Hasnul comparison)
- [ ] Social media sentiment (anti-defection narrative?)
- [ ] OA community response to ASLI
- [ ] 2022 Alwiyah voter retention indicators

### Election Day

- [ ] Turnout by PD (Chinese PDs, OA PDs, FELDA critical)
- [ ] Postal vote patterns (BN-leaning typically)
- [ ] OA PD vote share (ASLI performance)

### Post-Election Analysis

- [ ] Vote share by PD
- [ ] Alwiyah personal vote estimation
- [ ] OA vote pattern (ASLI consolidation?)
- [ ] Chinese turnout estimation
- [ ] Malay vote split (BN vs. PN vs. PH)

---

## 📊 Data Sources

| Source | File | Confidence |
|--------|------|------------|
| SPR Electoral Roll (2026-06-19) | `data/demographics.json` | `[HIGH]` |
| Candidate Announcements (2026-06-29) | `data/candidates.json` | `[HIGH]` |
| Historical Results (2018, 2022) | `data/historical-results.json` | `[HIGH]` — **CORRECTED 2026-06-29** |
| Tier Classification | `analysis/tier-strategy.md` | `[HIGH]` |
| Vote Projections | `analysis/vote-projections.md` | `[MEDIUM/LOW]` — **CORRECTED PH ceilings** |
| Strategic Assessments | `analysis/party-playbooks.md` | `[MEDIUM]` — **PH strategy corrected** |

---

## ✅ Truth Validation (CVS Compliance)

This repository follows the **Core Truth Validation System (CVS)**:

- **Tier 1 Claims** (numbers, names, dates): Sourced to SPR data or official announcements
- **Tier 2 Claims** (analytical): Tagged with confidence [HIGH/MEDIUM/LOW]
- **Tier 3 Claims** (predictive): Flagged as SPECULATION: or SCENARIO:
- **Pre-Output Checklist:** All numerical claims verified, math shown explicitly

**Validation Command:**
```bash
./tools/truth-validator/validate.sh analysis/vote-projections.md
```

**Corrections Log:**
- 2026-06-29: Historical results corrected (2022: PH 6.9% not 12.4%, BN candidate Youzaimi not Fared, turnout 55% not unspecified)
- 2026-06-29: PH ceiling revised from 25% to 12–15% (structurally impossible without Malay vote)
- 2026-06-29: PH strategy shifted from "win play" to "build for 2030" (BN 70–75% retention probability)
- 2026-06-29: Anti-defection flow corrected (benefits PN, not PH)

---

## 🔗 Related Repositories

- **N.17 Semerah:** [github.com/DAF2727/N17-Semerah-War-Room](https://github.com/DAF2727/N17-Semerah-War-Room)
- **N.33 Tenggaroh:** [github.com/DAF2727/N33-Tenggaroh-Brief](https://github.com/DAF2727/N33-Tenggaroh-Brief)
- **Johor PRN 2026 Master Dashboard:** [github.com/DAF2727/Johor-PRN-2026](https://github.com/DAF2727/Johor-PRN-2026)
- **N32 Endau Corrections Log:** [memory/n32-endau-corrections-20260629.md](https://github.com/DAF2727/N32-Endau-V2/blob/main/memory/n32-endau-corrections-20260629.md)

---

## 📄 License

**Internal Use Only** — Political intelligence for campaign planning and analysis.

**Contact:** DAF (@DAF2727)

**Last Updated:** 2026-06-29 (CORRECTIONS APPLIED)
