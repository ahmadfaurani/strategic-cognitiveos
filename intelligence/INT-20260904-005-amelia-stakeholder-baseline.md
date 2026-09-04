---
id: INT-20260904-005
record_type: intelligence
title: "Amelia 77-Person High-Touch Stakeholder Activation — Baseline & Gap Analysis"
created_at: 2026-09-04T03:55:00+00:00
updated_at: 2026-09-04T03:55:00+00:00
owner: faurani-jaafar
intelligence_type: operational
status: active
priority: critical
sensitivity: confidential
lifecycle_state: canonical
confidence: high
summary: "Complete baseline of existing stakeholder and organisation records in the Strategic CognitiveOS repository, mapped against the 77-person high-touch stakeholder activation target. Identifies 108 existing STK records (40 CSM, 20 internal, 14 partner/academic, 5 intelligence subjects, 29 other government), 24 ORG records, and the 193-organisation segmentation framework as the primary source for target identification. Gap: 77 high-touch targets minus ~40 named CSM stakeholders = ~37 stakeholders to identify from the 193-org database, likely from A-Target (93) and B-Engage (35) tiers."
strategic_significance: "Establishes the data foundation for Amelia's high-touch activation programme. Without this baseline, the 77-person target cannot be scoped, prioritised, or executed."
mission_alignment:
  - stakeholder-engagement
  - cybersecurity-productisation
  - commercial-development
  - cyberdsa-2026
tags:
  - domain/stakeholder-engagement
  - domain/commercial-development
  - domain/csm-partnership
  - domain/cyberdsa-2026
  - framework/actionable-intelligence-protocol
  - lifecycle/canonical
  - priority/critical
source:
  type: internal-analysis
  reference: CognitiveOS Discovery Directive D (2026-09-04)
related_records:
  - STK-20260813-014
  - SEG-20260818-001
  - INT-20260815-003
  - INT-20260815-004
  - TRK-20260818-001
  - ART-20260823-001
  - AIP-20260823-001
---

# Amelia 77-Person High-Touch Stakeholder Activation — Baseline & Gap Analysis

**Directive:** CognitiveOS Discovery — Directive D
**Date:** 4 September 2026
**Analyst:** Ember (subagent)
**Scope:** Full audit of Strategic CognitiveOS stakeholder and organisation records

---

## A. Total Existing Stakeholder Records

**Count: 108 STK records** (files in `stakeholders/` directory)

### Breakdown by Category

| Category | Count | Notes |
|----------|-------|-------|
| **CyberSecurity Malaysia (CSM)** | ~40 | Named individuals at CSM — including leadership, technical, Co-Design Lab participants, and gate stakeholders |
| **Internal (Aras / WIG / MTAI)** | ~20 | DAF, Hadri, Fuad, Shuhada, Amelia, Kenny, Azza, Hadi, Syahir, others |
| **Government (non-CSM)** | ~18 | JDN (5), PMO (2), NACSA (1), MCMC (2), MOH (1), SUK Negeri Sembilan (1), PERJASA (1), MAPO (1), PDRM (1), others |
| **Partner / Academic** | ~14 | ELSA (4), UiTM (6), UPM (1), Plymouth/CRC (1), Aerosea (1), NanoSec (1) |
| **Intelligence Subjects** | ~5 | MACC trial defendants, PDRM CID Director (no direct engagement) |
| **Misc/Dormant** | ~11 | Reclassified, superseded, dormant records |

### Detailed CSM Stakeholder Breakdown (40 records)

| Sub-category | Count | Key Individuals |
|--------------|-------|-----------------|
| CSM Leadership/Strategic | 6 | Fahdzli (STK-004-001), Zulfeka (STK-004-002), Roshdi (STK-015-010), Azrul (STK-013-008), Bala (STK-017-001), Amirudin (STK-015-013, retired) |
| CSM Technical/Gate Owners | 5 | Zaharudin (STK-004-011), Wan Roshaimi (STK-012-001), Hafiz Rahman (STK-004-010/027-001), Iqbal (STK-013-009), Amirul (STK-013-010) |
| CSM Co-Design Lab (MyCERT) | 17 | Fathi Kamil (STK-004-004), Izzatul (005), Imran (006), Qurratu (007), Lukman (008), Syahidah (009), Kamarul (012-002), Ahmad Osman (012-003), Mohd Hafiz Tabrani (012-004), Imran Hasnan (012-005), Wan Lukman (012-006), Norlinda (012-007), Sarah (012-008), Kamil (012-009), Afiqah (012-010), Aizuddin (012-011), Nurshuhada (012-012) |
| CSM Other | 6 | Nurshahira (STK-013-011), Suraya Hani (STK-013-012), Zulfelka (STK-013-013), Fazlan (STK-018-002), Tuan Fatah (STK-026-001), Shamsul Azri (STK-015-007) |
| CSM-Adjacent (Aisha, Megat, etc.) | 6 | Aisha (STK-015-001), Dr. Megat/NACSA (STK-019-001), Nushirwan/MKN (STK-015-009), Mohamad Salim/MCMC (STK-015-014), Fabian Bigar/KKD (STK-015-015), Fahmi Fadzil (STK-015-018) |

---

## B. Total Existing Organisation Records

**Count: 24 ORG records** (files in `organizations/` directory)

### Breakdown by Type

| Type | Count | Organisations |
|------|-------|---------------|
| Government Agency | 7 | CSM, NACSA, JDN, PMO, PERJASA, MKN, MAPO |
| Private Company | 2 | Nexuscorpgroup, Al Khairi Group (both intelligence subjects) |
| Internal Division | 1 | RADAR (Data Research Acquisition & Development) |
| Community Team | 1 | NanoSec Community Team |
| Other (backfilled) | 13 | Includes CSCDC (×2), LHDN, WIG, MTAI, ELSA, MOH, UiTM, SUK Negeri Sembilan, Aerosea Exhibitions, + 4 ORG-20260820-001–004 |

### Organisation Index (6 formally indexed)

The organisation index (`indexes/organization-index.md`) only tracks 6 organisations formally:
- ORG-20260820-001: CyberSecurity Malaysia (government-agency, cybersecurity)
- ORG-20260820-002: Nexuscorpgroup Sdn Bhd (private-company, law-enforcement intelligence)
- ORG-20260820-003: Al Khairi Group Berhad (private-company, intelligence subject)
- ORG-20260820-004: RADAR (internal-division, government)
- ORG-20260903-001: MAPO (government-agency, intelligence subject)
- ORG-20260904-001: NanoSec Community Team (community-team, cybersecurity)

**Gap:** 18 of 24 organisation files exist in the directory but are not yet reflected in the index. The index is stale and needs updating.

---

## C. Stakeholder Records Grouped by Type

### Government (Non-CSM)
| ID | Name | Organisation | Status |
|----|------|--------------|--------|
| STK-20260725-001 | CSCDC | CSCDC / JPM-MKN-NACSA | Prospect |
| STK-20260725-009 | NACSA | NACSA / JPM | Active |
| STK-20260725-010 | JDN | JDN / Government | Active |
| STK-20260725-011 | PMO Strategic Data | PMO | Active |
| STK-20260725-012 | LHDN | LHDN / Ministry of Finance | Active |
| STK-20260803-010 | Khairil Hilmi | PMO | New |
| STK-20260803-011 | Dr. Noor Dasrafeezal | PMO | New |
| STK-20260813-001 | PERJASA | PERJASA | Developing |
| STK-20260813-002 | Mohamed Kheirulnaim | JDN | Active |
| STK-20260813-003 | Razale bin Ibrahim | JDN | Active |
| STK-20260813-004 | Azwan bin Azmi | JDN | Active |
| STK-20260813-005 | Meor Mohd Shahrulnizam | JDN | Active |
| STK-20260813-006 | Raja Mohammad Hafiz | MOH | Active |
| STK-20260813-007 | Hussein bin Mohamed | SUK Negeri Sembilan | Active |
| STK-20260815-002 | MCMC | MCMC | Identified |
| STK-20260815-007 | Shamsul Azri | JPM | New |
| STK-20260815-008 | Megat Zuhairy | NACSA | New |
| STK-20260815-009 | Nushirwan | MKN | New |
| STK-20260815-011 | Muhammad Rezal | PTPKM | New |
| STK-20260815-014 | Mohamad Salim | MCMC | New |
| STK-20260815-015 | Fabian Bigar | KKD | New |
| STK-20260815-018 | Fahmi Fadzil | KKD | New |
| STK-20260903-001 | CP Datuk M. Kumar | PDRM — CID | Intelligence subject |

### Internal (Aras / WIG / MTAI)
| ID | Name | Role | Status |
|----|------|------|--------|
| STK-20260725-007 | Aras Integrasi | Employer | Active |
| STK-20260803-007 | Hadri | Lead Architect | Active |
| STK-20260804-003 | Ahmad Fuad | VoronCitadel Product Owner | Active |
| STK-20260808-003 | Shuhada M. Halimi | Sales / Account Coordination | New |
| STK-20260810-003 | Hadi | GovSec Product Manager (incoming) | Pending |
| STK-20260811-001 | Syahir | TBD | New |
| STK-20260811-002 | Nik Sarah Naqibah | TBD | New |
| STK-20260811-003 | Jasila Jalil | TBD | New |
| STK-20260815-006 | Azirul Hazran | TBD | New |
| STK-20260815-016 | Che Nasir | Managing Director, Aras | Active |
| STK-20260815-017 | Dennis Looi | Deputy CEO, Aras | Active |
| STK-20260808-001 | Kenny Kok | COO, MTAI | Active |
| STK-20260808-002 | Azzatullina Pawanchik | CMO, WIG | New |
| STK-20260813-014 | Amelia Nadia | Strategic Stakeholder Engagement Lead | Active |
| STK-20260813-015 | Rashid Bin Ramli | Event Activation Support | New |
| STK-20260813-016 | Said Farid Zainudin | Event Activation Support | New |
| STK-20260815-004 | Norshaza Hanis | Marketing Team, WIG | New |
| STK-20260815-005 | Muhamad Danish | TBD, WIG | New |
| STK-20260820-002 | Orange Ng | WIG (Finance) | New |
| STK-20260818-003 | Shageenderan | MTAI | New |

### Partner
| ID | Name | Organisation | Status |
|----|------|--------------|--------|
| STK-20260803-001 | ELSA | ELSA Sdn Bhd | Developing |
| STK-20260803-002 | Abdul Hafeez Abdul Bari | ELSA | Developing |
| STK-20260803-003 | Daniel Ilham | ELSA | New |
| STK-20260803-004 | Azarul | ELSA Group | New |
| STK-20260803-005 | Samantha Lai | MTAI (Legal) | Active |
| STK-20260803-006 | Farul Mohd Ghazali | MTAI (CTO/Legal) | Active |
| STK-20260816-001 | Mr Hazdi | Aerosea Exhibitions | New |
| STK-20260820-001 | Dr. Ji-Jian Chin | Plymouth / CRC 2026 | New |

### Academic
| ID | Name | Institution | Status |
|----|------|-------------|--------|
| STK-20260803-008 | UiTM CMIWS | UiTM | Active |
| STK-20260803-009 | Prof. Madya Dr. Suhaimee | UiTM | Active |
| STK-20260807-001 | Dr. Mohd Firdauz | UiTM | New |
| STK-20260807-002 | En. Antashah | UiTM | New |
| STK-20260807-003 | En. Muhd Faiz | UiTM | New |
| STK-20260807-004 | En. Al Faliq | UiTM | New |
| STK-20260818-001 | Dr. Azree Shahrel | UPM | Active |

### Intelligence Subjects (OSINT — No Direct Engagement)
| ID | Name | Context | Source |
|----|------|---------|--------|
| STK-20260820-003 | Sayed Amir Muzzakkir | MACC defendant (RMPNet) | DOC-20260820-001 |
| STK-20260820-004 | Datuk Seri Mohd Khairi | 15th prosecution witness | DOC-20260820-001 |
| STK-20260820-005 | Wan Azhar Yusof | Bribe payer | DOC-20260820-001 |
| STK-20260820-006 | Datuk Seri Hamzah Zainudin | Former Home Minister | DOC-20260820-001 |
| STK-20260903-001 | CP Datuk M. Kumar | PDRM CID Director | DOC-20260903-001 |

### CSM (CyberSecurity Malaysia) — Full List

See Section A above. 40 named individuals spanning leadership, technical, Co-Design Lab, and gate stakeholders.

---

## D. Organisation Records Grouped by Type

| Type | Count | Organisations |
|------|-------|---------------|
| Government Agency | 7 | CSM, NACSA, JDN, PMO, PERJASA, MKN, MAPO |
| Private Company | 2 | Nexuscorpgroup, Al Khairi Group |
| Internal Division | 1 | RADAR |
| Community Team | 1 | NanoSec Community Team |
| Other / Backfilled | 13 | CSCDC (×2), LHDN, WIG, MTAI, ELSA, MOH, UiTM, SUK NS, Aerosea, + 4 ORG-20260820 |

---

## E. The 193-Organisation Segmentation Framework

**Document:** `documents/SEG-20260818-001-193-org-segmentation-framework.md`
**CSV Data:** `artifacts/SEG-193-org-segmentation-20260818.csv` (191 rows + header = 192 lines)
**Raw Mapping CSV:** `products/voroncitadel/STAKEHOLDER_MAPPING_193.csv` (193 rows + header = 194 lines)
**Summary:** `products/voroncitadel/STAKEHOLDER_MAPPING_SUMMARY.md`

### What It Is

A prioritisation framework converting the RMiT compliance market database (193 Malaysian financial services organisations) into an actionable account list for CyberDSA 2026 pre-engagement and the broader VoronCitadel GTM.

### Scale

- **191 unique organisations** in the segmentation CSV (2 duplicates merged in v5.51)
- **193 rows** in the raw stakeholder mapping CSV (original database)
- **150 unique stakeholder entries** (43 share parent organisation stakeholders)
- **7 stakeholder functions mapped per organisation:** CISO, Head of GRC, CFO, CRO, Head of Compliance, CIO, Head of Internal Audit

### Sector Breakdown

| Tier | Count | Segments |
|------|-------|---------|
| Tier 1 | 32 | Licensed Banks |
| Tier 2 | 52 | Insurers (26), Investment Banks (14), Takaful (12) |
| Tier 3 | 34 | Development FIs (13), MSBs (16), Asset Management (5) |
| Tier 4 | 35 | E-Money (17), Card Schemes (10), Payment Operators (8) |
| Tier 5 | 23 | GLC-Linked |
| Tier 6 | 17 | Fintech Registered (6), Fintech Sandbox (11) |
| **Total** | **193** | **13 market segments** |

### Priority Classification

| Class | Score Range | Count | CyberDSA Action |
|-------|------------|-------|----------------|
| **A — Target** | ≥50 | 93 | Pre-schedule meeting before CyberDSA |
| **B — Engage** | 40–49 | 35 | Send collateral + personal invitation to booth |
| **C — Monitor** | 30–39 | 44 | Include in mailing list |
| **D — Watch** | <30 | 19 | Database only, no active outreach |

### Does It Contain Named Individuals?

**Yes — extensively.** The raw CSV (`STAKEHOLDER_MAPPING_193.csv`) contains 7 columns of named decision-makers per organisation:
- Chief Information Security Officer (CISO)
- Head of Governance Risk & Compliance (GRC)
- Chief Financial Officer (CFO)
- Chief Risk Officer (CRO)
- Head of Compliance
- Chief Information Officer (CIO)
- Head of Internal Audit

**Unique named CISOs identified:** ~94 (after deduplication of shared-parent entries)

Data quality varies:
- 135 organisations (71%) have 3+ identified contacts (enriched)
- 18 organisations (9%) have 1-2 contacts (partial)
- 38 organisations (20%) have 0 contacts (bare — primarily Tier 3 MSBs and Tier 6 fintechs)
- Tier 1 and Tier 2 are **fully enriched** — 26/30 Tier 1 and 54/54 Tier 2 have 3+ contacts

### Top 15 VIP Targets (from the framework)

Maybank, CIMB, Public Bank, HSBC, AmBank, RHB, Hong Leong, Bank Islam, OCBC, Standard Chartered, Prudential, Great Eastern, Etiqa, Tokio Marine, Liberty General.

---

## F. Gap Analysis: 77 Target vs Existing Stakeholders

### Understanding the "77-Person High-Touch" Target

The 77-person high-touch stakeholder activation target is a directive to identify and engage 77 specific individuals who require personalised, relationship-based activation — not mass marketing or database-only outreach.

### Current Named Stakeholder Pool

| Pool | Count | High-Touch Eligible? |
|------|-------|---------------------|
| CSM named stakeholders | ~40 | ✅ Yes — primary engagement targets |
| Internal team (Aras/WIG/MTAI) | ~20 | ❌ No — internal team, not external stakeholders |
| Government (non-CSM) | ~18 | ✅ Partially — JDN, NACSA, MCMC leadership are high-touch |
| Partner/Academic | ~14 | ✅ Partially — ELSA, UiTM, UPM contacts |
| Intelligence subjects | ~5 | ❌ No — OSINT only, no direct engagement |
| **Total externally engaging** | **~72** | |

### Gap Calculation

If the 77-person target is comprised of **external stakeholders requiring high-touch activation**:

| Metric | Value |
|--------|-------|
| Target high-touch stakeholders | 77 |
| Existing named external stakeholders (excl. internal + OSINT) | ~62 |
| Existing named CSM stakeholders (most likely high-touch candidates) | ~40 |
| **Gap if CSM-only scope** | 77 - 40 = **37 missing** |
| **Gap if all external scope** | 77 - 62 = **15 missing** |

### Likely Source of Missing 77 Stakeholders

The 193-organisation segmentation framework contains ~94 unique named CISOs and hundreds of other decision-makers. The 77-person target is most likely drawn from:

1. **A-Target tier (93 organisations):** Named CISOs and Heads of GRC from top-tier banks and insurers
2. **Existing CSM stakeholders (40):** Already engaged through partnership activities
3. **Government stakeholders (18):** JDN, NACSA, MCMC, PMO contacts
4. **Partner/Academic (14):** ELSA, UiTM, UPM, Plymouth

**Most probable interpretation:** The 77-person target = the set of named, reachable decision-makers across the A-Target organisations who have CISO or Head of GRC roles identified (approximately 70-80 unique individuals once parent-shared duplicates are consolidated), plus key CSM and government stakeholders already in the system.

### What's Missing in the STK Records

1. **STK records for 193-org contacts:** The 193-org CSV contains hundreds of named decision-makers (CISOs, GRC heads, CROs, CIOs) but these are NOT in the stakeholder registry as STK records. They exist only in the CSV data file.
2. **Engagement status tracking:** No STK records means no engagement status, contact history, or relationship owner assigned for these individuals.
3. **STK records needed:** For a 77-person high-touch programme, each of the 77 individuals needs a STK record with:
   - Named contact (CISO/GRC Head)
   - Organisation context (from 193-org framework)
   - Engagement tier (high-touch = A-Target VIP)
   - Relationship owner (likely Amelia or DAF)
   - Contact status and history

---

## G. Existing Stakeholder Engagement Matrix / Tracker

### 1. TRK-20260818-001 — Stakeholder Coverage Tracker

**File:** `artifacts/TRK-20260818-001-stakeholder-coverage-tracker.csv`

A CSV tracker with 18 columns including:
- stakeholder_id, name, role, organisation
- relationship_status, priority, created_date, last_contact_date
- days_since_contact, staleness, engagement_depth
- last_contact_summary, next_action
- primary_owner, secondary_owner, engagement_target, next_target_date

**Status:** Partially populated. Contains ~85 rows but many are placeholder entries (reclassified, dormant, no-contact). The tracker was created Aug 18 as part of the CyberDSA preparation but appears to have been a one-time export rather than a living document. Many entries have empty owner/action fields.

### 2. INT-20260815-003 — CyberDSA Execution Stakeholder Matrix (RACI)

A RACI matrix covering 10 named stakeholders across 6 dimensions of CyberDSA execution. This is an **execution** matrix, not a relationship activation matrix. It tracks who is Responsible/Accountable/Consulted/Informed for specific success criteria.

### 3. INT-20260815-004 — CSM-Aras Stakeholder Coverage Plan

Defines a four-layer coverage model (Primary, Secondary, Specialist, Executive) for 10 CSM stakeholders. Includes:
- Priority CSM Stakeholder Coverage Matrix (10 CSM stakeholders × Aras coverage)
- Communication Ownership Model (7 topic areas)
- Strategic Engagement Flow (Before/During/After meetings)
- Coverage Readiness Metrics (8 metrics, all targeting 100%/0 SPOF)
- Immediate Action Plan (8 actions)

### 4. DOC-20260827-003 — CyberDSA Stakeholder Framework v1.1

Referenced in the stakeholder index update notes. A dependency chain reorder document that reorganised gate stakeholders (Roshdi → Bala → Wan Roshaimi → Zaharudin → Dr. Megat). This is a gate-sequence framework, not a high-touch activation tracker.

---

## H. Existing "Contact Dumps" — NOT High-Touch Activation

### 1. STAKEHOLDER_MAPPING_193.csv (193 rows × 7 contact roles)

**File:** `products/voroncitadel/STAKEHOLDER_MAPPING_193.csv`

This is a **data enrichment dump** — 193 organisations × 7 stakeholder functions = ~1,351 contact cells. It contains names, titles, and source URLs but:
- No engagement status
- No relationship owner
- No contact history
- No priority classification
- No next-action tracking

**This is a DATABASE, not a high-touch activation list.** It should NOT be confused with the 77-person high-touch target. It is the source from which the 77 would be identified, not the 77 itself.

### 2. SEG-193-org-segmentation-20260818.csv (191 rows)

**File:** `artifacts/SEG-193-org-segmentation-20260818.csv`

The scored segmentation CSV with priority classification (A/B/C/D), composite scores, CISO names, and CyberDSA action assignments. Also a database, not an activation tracker.

### 3. STAKEHOLDER_MAPPING_SUMMARY.md

**File:** `products/voroncitadel/STAKEHOLDER_MAPPING_SUMMARY.md`

A summary of the 193-org mapping with tier breakdown and stakeholder function descriptions. Notes that:
- 150 unique stakeholder entries (43 share parent stakeholders)
- ~146 directional buying centres
- 65.4% directionally actionable
- Only 4.7% has explicit numeric confidence
- CRM normalisation is a pre-launch requirement

### Key Distinction

| What it is | What it is NOT |
|------------|----------------|
| A database of 193 organisations and ~1,351 contact roles | A high-touch activation list |
| A segmentation framework with scoring | An engagement tracker |
| A market intelligence asset | A relationship management tool |
| Source for identifying the 77 | The 77 itself |

---

## I. Summary Assessment

### What Exists

1. **108 STK records** — comprehensive for CSM (40) and internal team (20), thin for the 193-org market
2. **24 ORG records** — partially indexed (6 of 24 in the index)
3. **193-organisation segmentation framework** — robust, fully scored, with named CISOs and GRC heads
4. **94 unique CISOs identified** in the market database
5. **Stakeholder coverage tracker** — exists but stale and incomplete
6. **RACI execution matrix** — exists for CyberDSA operational dimensions
7. **CSM coverage plan** — exists with 4-layer model for 10 CSM stakeholders

### What's Missing

1. **STK records for the 77 high-touch targets** — most of the 77 individuals are in the CSV, not in the stakeholder registry
2. **Amelia's activation tracker** — no dedicated tracker for the 77-person high-touch programme
3. **Engagement status** for market contacts — no contact history, relationship owner, or next-action data
4. **Organisation index update** — 18 of 24 ORG files not reflected in the index
5. **Clear definition of "the 77"** — no document explicitly defines who the 77 are, what selection criteria were used, or how they map to the 193-org framework

### Recommended Next Steps

1. **Define the 77:** Clarify selection criteria — is it 77 individuals from A-Target orgs (CISO + GRC Head), or 77 across all categories (CSM + government + market)?
2. **Create STK records:** For each of the 77, create a STK record with engagement tier, relationship owner (Amelia/DAF), and activation status
3. **Build the activation tracker:** Either upgrade TRK-20260818-001 or create a new tracker specifically for the 77-person programme
4. **Update the organisation index:** 18 ORG files need to be reflected in `indexes/organization-index.md`
5. **Assign relationship owners:** Map each of the 77 to a primary Aras relationship owner per the CSM-Aras coverage model (INT-20260815-004)

---

*This baseline establishes the data foundation for Amelia's high-touch activation programme. All subsequent work should reference this document as the starting state.*
