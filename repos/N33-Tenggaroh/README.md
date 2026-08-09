# N33 Tenggaroh — 16th Johor State Election (2026)

**Constituency:** N33 Tenggaroh, P154 Mersing, Johor, Malaysia  
**Election:** 16th Johor State Election (2026)  
**Contest Type:** Three-cornered fight (BN, PH, PN)  
**Total Registered Voters:** 39,001 (as of 19 June 2026)  
**Total Polling Districts:** 24

---

## Quick Navigation

| Section | Description | Location |
|---------|-------------|----------|
| 📊 Demographics | Ethnic, age, gender, geographic breakdown | `01-demographics/` |
| 👥 Candidates | 2026 candidate profiles and analysis | `02-candidates/` |
| 📜 Historical | 2018/2022 results, trends, patterns | `03-historical/` |
| 🎯 Strategy | PKR/PH strategic recommendations | `04-strategy/` |
| 📈 Analysis | Turnout scenarios, vote projections | `05-analysis/` |
| 📎 Appendix | Raw data tables, PD-level breakdowns | `06-appendix/` |
| 📚 Docs | Methodology, sources, CVS compliance | `docs/` |

---

## 2026 Candidate Slate

| Coalition | Candidate | Party | Notes |
|-----------|-----------|-------|-------|
| **BN** | Tuan Haji Mohd Youzaimi bin Haji Yusof | UMNO | Malay candidate — corrective switch from 2022 MIC candidate |
| **PH** | Md Yusof bin Dawam | PKR | PH's challenger; must rebuild from 2022 collapse |
| **PN** | Muhamad Amer bin Muhamad | PAS | Primary disruptor; benefits from Malay consolidation |

**Historical Context:** Seat held by Raven Kumar Krishnasamy (BN-MIC) — long-time ADUN and former Johor EXCO member. BN's 2026 UMNO candidate switch is a defensive correction to 2022's 83% Malay electorate reality.

---

## Key Demographics

| Metric | Value | Strategic Significance |
|--------|-------|------------------------|
| **Malay** | 83.25% (32,469) | Decisive majority — BN/PN battleground |
| **Chinese** | 12.75% (4,972) | PH's base — turnout-elastic |
| **Indian** | 1.42% (554) | Concentrated in mixed PDs — persuasion target |
| **Youth (18–29)** | 26.15% (10,198) | Structurally decisive if mobilised |
| **Under 40** | 67.04% (26,148) | Two-thirds of electorate — cost-of-living messaging |
| **FELDA/RISDA** | 49.5% (19,305) | 9 PDs, 98.98% Malay — BN's firewall, PN's opportunity |

---

## Strategic Assessment

**Tier Classification:** Tier-2 BN-defensive / contestable

**Decisive Variables:**
1. **Turnout differential** — 2022 low turnout (57.2%) produced BN's narrow 1,356-vote margin; recovery to 2018 levels (~80%) shifts dynamics dramatically
2. **FELDA second-generation sentiment** — 69.5% under-40 in FELDA; cost-of-living messaging resonance
3. **Chinese mobilisation** — 4 Chinese-concentration PDs (3,605 voters); PH needs 75–80% turnout + 80%+ support
4. **Malay vote split** — BN vs PN competition in 15 Malay-majority PDs (20,553 voters)

**BN Retention Probability by Scenario:**
- Low turnout (55–60%): 65–70% [MEDIUM]
- Moderate turnout (65–70%): 50–55% [MEDIUM]
- High turnout (75–80%): 40–45% [LOW]

**PH Strategic Role:** Contest at minimal viable level (target 5,500–6,000 votes, 14–15% share). Accept spoiler role — force BN to defend mixed PDs, stretch resources. Prioritize neighbouring seats (N32 Panti, N34 Johor Lama) where PH has higher ceiling.

---

## Repository Structure

```
N33-Tenggaroh/
├── README.md                    # This file — overview and navigation
├── 01-demographics/
│   ├── ethnic-composition.md    # Ethnic breakdown by PD
│   ├── age-gender.md            # Age structure, youth bulge analysis
│   ├── geographic-analysis.md   # FELDA vs non-FELDA, island PDs
│   └── pd-profiles/             # Individual PD profiles (24 files)
├── 02-candidates/
│   ├── bn-mohd-youzaimi.md      # BN candidate profile
│   ├── ph-md-yusof-dawam.md     # PH candidate profile
│   ├── pn-muhamad-amer.md       # PN candidate profile
│   └── historical-reps.md       # Raven Kumar, past ADUNs
├── 03-historical/
│   ├── 2022-results.md          # 2022 election results, analysis
│   ├── 2018-results.md          # 2018 election results (PH win)
│   └── trend-analysis.md        # 2018→2022→2026 trends
├── 04-strategy/
│   ├── ph-strategic-plan.md     # PKR/PH operational plan
│   ├── priority-pds.md          # Tier 1/2/3 PD targeting
│   ├── messaging-framework.md   # Ethnic-specific messaging
│   └── resource-allocation.md   # Minimal viable contest model
├── 05-analysis/
│   ├── turnout-scenarios.md     # 5-scenario vote projection model
│   ├── vote-split-dynamics.md   # BN vs PN vs PH interactions
│   └── comparative-seats.md     # vs N17 Semerah, N16 Sungai Balang
├── 06-appendix/
│   ├── full-pd-table.md         # 24 PD demographic table
│   ├── raw-data-sources.md      # SPR Excel extraction logs
│   └── gis-maps/                # (Future: polling district maps)
└── docs/
    ├── methodology.md           # Data extraction, analysis methods
    ├── cvs-compliance.md        # Core Truth Validation checklist
    └── sources.md               # SPR, MEMORY.md, external references
```

---

## Data Sources

- **Primary:** SPR Electoral Roll (as of 19 June 2026) — Excel file
- **Historical:** MEMORY.md#L280-L310 (N33 Tenggaroh 2022 results)
- **Comparative:** MEMORY.md#L230-L279 (N17 Semerah), MEMORY.md#L180-L229 (N16 Sungai Balang)

---

## CVS Compliance

All Tier-1 claims (numbers, names, dates) are sourced from SPR data or MEMORY.md with line-number citations. Analytical claims carry confidence tags ([HIGH]/[MEDIUM]/[LOW]). Speculative claims are flagged as `SPECULATION:` or `SCENARIO:`.

**Validation:** `./tools/truth-validator/validate.sh repos/N33-Tenggaroh/README.md`

---

## Last Updated

**Date:** 2026-06-29  
**Analyst:** PKR Political Intelligence (Automated)  
**Next Review:** Post-candidate nomination roadshow (verify candidate visibility, early polling)

---

## Related Repositories

- **N17 Semerah:** `repos/N17-Semerah/`
- **N16 Sungai Balang:** `repos/N16-Sungai-Balang/`
- **Johor PRN 2026 War Room:** `repos/Johor-PRN-2026/`

---

**Classification:** INTERNAL — EYES ONLY  
**Prepared for:** PKR Political Intelligence — Applied Use Case
