---
id: SEG-20260818-001
record_type: document
title: 193-Organisation Segmentation Framework — CyberDSA 2026 Pre-Engagement
created_at: 2026-08-18 15:40:00+00:00
updated_at: 2026-08-18 15:40:00+00:00
owner: faurani-jaafar
status: active
priority: critical
sensitivity: confidential
lifecycle_state: canonical
tags:
  - domain/commercial-development
  - domain/stakeholder-engagement
  - milestone/cyberdsa-2026
  - workstream/cybersec-products
  - lifecycle/canonical
  - priority/critical
related_records:
  - INT-20260815-002
  - INT-20260815-003
  - INT-20260815-004
  - INT-20260815-005
  - INT-20260815-006
  - GRP-20260813-001
---

# 193-Organisation Segmentation Framework
## CyberDSA 2026 Pre-Engagement & Account Prioritisation

**Document ID:** SEG-20260818-001
**Created:** 18 August 2026
**Owner:** DAF (strategic), Shuhada (execution)
**Source Database:** `prospect-database-enriched-v5.51.csv` (191 organisations, 7 contact roles each)
**Output File:** `SEG-193-org-segmentation-20260818.csv` (full segmentation with scores)

---

## 1. Purpose

This framework converts the 193-organisation RMiT compliance market database into a prioritised, actionable account list for CyberDSA 2026 pre-engagement. It defines:

- **Who to target** before CyberDSA (priority accounts for pre-scheduled meetings)
- **How to engage** each tier (meeting, collateral, mailing list, database only)
- **Who owns** each engagement (Aras primary + secondary)
- **What success looks like** (10-15 pre-scheduled meetings by CP1 Aug 22 → CP2 Sep 5)

This directly unblocks CyberDSA criteria 2.1 (segmentation), 2.2 (priority accounts), and indirectly 2.4 (pre-scheduled meetings), 2.6 (discovery sessions), 2.9 (POC candidates), and 2.10 (signed POC). **Six criteria from one deliverable.**

---

## 2. Scoring Methodology

Each of the 191 organisations is scored on a composite 70-point scale across four dimensions:

### 2.1 Tier Weight (30 max)

Based on the existing database tier classification:

| Tier | Weight | Rationale |
|------|--------|-----------|
| Tier 1 | 30 | Licensed banks — highest RMiT compliance budget, CISO+GRC roles established, largest cybersecurity spend |
| Tier 2 | 24 | Insurers, takaful, investment banks — strong compliance mandate, dedicated GRC functions |
| Tier 3 | 18 | MSBs, development FIs — growing compliance needs, moderate budget |
| Tier 4 | 15 | E-money, payment operators — fintech security, emerging regulation |
| Tier 5 | 9 | GLC-linked, cooperatives — strategic but slower procurement |
| Tier 6 | 6 | Fintech sandbox/registered — early stage, limited budget |

### 2.2 Segment Relevance (20 max)

Cybersecurity/GRC product relevance by segment (VoronCitadel, GovSec TIP, ChainSentry):

| Segment | Score | Rationale |
|---------|-------|-----------|
| Licensed Banks | 20 | RMiT mandatory, CISO+GRC roles, highest budget, VoronCitadel primary market |
| Insurers | 18 | RMiT mandatory, strong GRC needs, VoronCitadel + GovSec TIP relevant |
| Development FIs | 18 | Government-linked, strategic visibility, high compliance standards |
| Card Schemes | 16 | High security standards, payment security, ChainSentry relevant |
| Investment Banks | 16 | Compliance, smaller teams, faster decisions |
| Takaful | 16 | Islamic compliance overlay + RMiT, similar to insurers |
| Payment Operators | 14 | PCI-DSS, payment security, ChainSentry relevant |
| E-Money | 14 | Fintech security, growing regulation, emerging budget |
| GLC-Linked | 14 | Government visibility, strategic accounts |
| Cooperatives | 12 | Growing compliance needs, lower budget, volume play |
| MSBs | 12 | Money services, compliance emerging |
| Fintech Registered | 10 | Small, early stage, limited immediate budget |
| Fintech Sandbox | 10 | Digital banks, emerging, relationship-building phase |

### 2.3 Contact Enrichment (14 max)

Number of identified decision-makers per organisation (0-7 contacts × 2 points):

- CISO (Chief Information Security Officer) — primary buyer for VoronCitadel
- Head of GRC — primary buyer for VoronCitadel, secondary for GovSec TIP
- CFO — budget authority
- CRO — risk function, VoronCitadel relevance
- Head of Compliance — regulatory driver, VoronCitadel relevance
- CIO — IT authority, infrastructure decisions
- Head of Internal Audit — assurance function, GRC relevance

### 2.4 Key Decision-Maker Presence (6 max)

Weighted presence of the three most critical contacts for cybersecurity sales:

- CISO present: +3 points (primary buyer)
- Head of GRC present: +2 points (direct user/champion)
- CRO present: +1 point (budget influencer)

---

## 3. Priority Classification

| Class | Score Range | Count | CyberDSA Action |
|-------|------------|-------|-----------------|
| **A — Target** | ≥50 | 93 | Pre-schedule meeting before CyberDSA (top 10-15 for VIP meetings) |
| **B — Engage** | 40-49 | 35 | Send collateral + personal invitation to booth |
| **C — Monitor** | 30-39 | 44 | Include in mailing list, general invitation |
| **D — Watch** | <30 | 19 | Database only, no active outreach |

---

## 4. Priority Account Shortlist (Top 15 for CyberDSA VIP Meetings)

From the A-Target class, the following 15 organisations are recommended for pre-scheduled meetings at CyberDSA. Selection criteria: Tier 1-2, full contact enrichment (7/7), CISO identified, strategic significance beyond CyberDSA (CSCDC visibility, CSM partnership relevance, existing relationship potential).

| # | Institution | Tier | Segment | CISO | GRC | Why This Account |
|---|-------------|------|---------|------|-----|-----------------|
| 1 | Maybank Berhad | 1 | Licensed Banks | ✅ | ✅ | Largest Malaysian bank, biggest cybersecurity budget, RMiT flagship |
| 2 | CIMB Bank Berhad | 1 | Licensed Banks | ✅ | ✅ | 2nd largest, strong GRC function, ASEAN presence |
| 3 | Public Bank Berhad | 1 | Licensed Banks | ✅ | ✅ | Top 3 domestic bank, conservative but steady GRC spend |
| 4 | HSBC Bank Malaysia | 1 | Licensed Banks | ✅ | ✅ | International bank, high security standards, regional visibility |
| 5 | AmBank (M) Berhad | 1 | Licensed Banks | ✅ | ✅ | Active cybersecurity programme, known GRC maturity |
| 6 | RHB Bank Berhad | 1 | Licensed Banks | ✅ | ✅ | Strong institutional relationships, GLC-linked |
| 7 | Hong Leong Bank | 1 | Licensed Banks | ✅ | ✅ | Digital-first, strong CISO function, fintech-curious |
| 8 | Bank Islam Malaysia | 1 | Licensed Banks | ✅ | ✅ | Islamic banking, unique compliance overlay, sovereign-aligned |
| 9 | OCBC Bank Malaysia | 1 | Licensed Banks | ✅ | ✅ | International, strong GRC, ASEAN cybersecurity standards |
| 10 | Standard Chartered | 1 | Licensed Banks | ✅ | ✅ | International, high compliance bar, CSM partnership visibility |
| 11 | Prudential Assurance | 2 | Insurers | ✅ | ✅ | Largest insurer, GRC maturity, RMiT compliance active |
| 12 | Great Eastern Life | 2 | Insurers | ✅ | ✅ | Major insurer, strong CISO, domestic+ASEAN |
| 13 | Etiqa General Insurance | 2 | Insurers | ✅ | ✅ | GLC-linked (Maybank group), takaful + conventional |
| 14 | Tokio Marine Life | 2 | Insurers | ✅ | ✅ | Japanese standards, high security maturity |
| 15 | Liberty General Insurance | 2 | Insurers | ✅ | ✅ | International, GRC-focused, mid-size (faster decision) |

**Shuhada:** These 15 need meeting requests sent by Aug 22 (CP1). Use the CISO and Head of GRC names from the enriched database. Draft meeting request template to be prepared by Shuhada, reviewed by DAF.

---

## 5. Engagement Owner Assignment

For each priority account, an Aras primary and secondary owner is assigned for pre/during/post CyberDSA engagement:

| Priority Tier | Primary Owner | Secondary Owner | Escalation |
|---------------|---------------|-----------------|-----------|
| A — Target (VIP meetings) | DAF | Hadri / Fuad | Kenny |
| A — Target (booth meetings) | Hadri | Fuad / Farul | DAF |
| B — Engage | Shuhada | Azza | DAF |
| C — Monitor | Shuhada | — | — |
| D — Watch | — | — | — |

**DAF owns VIP meetings** (top 15) because these are strategic accounts requiring executive presence.
**Hadri owns technical booth meetings** for A-Target accounts not in the top 15.
**Shuhada owns B and C tier** — collateral distribution, invitation management, CRM capture.

---

## 6. Shuhada's Execution Framework

### 6.1 What Shuhada Receives

1. **This framework document** (methodology + scoring + priority classification)
2. **`SEG-193-org-segmentation-20260818.csv`** (full 191-org scoring with contact names)
3. **Top 15 VIP list** (above) with named CISO/GRC contacts from the database

### 6.2 What Shuhada Produces by CP1 (Aug 22)

| Deliverable | Description | Due |
|-------------|-------------|-----|
| **2.1 Segmentation complete** | Confirm or adjust priority classification | Aug 20 |
| **2.2 Priority accounts finalised** | 10-15 accounts locked, meeting owners assigned | Aug 21 |
| **Meeting request drafts** | Template for DAF (VIP) + Shuhada (booth) | Aug 21 |
| **2.4 Meeting requests sent** | First wave of meeting requests dispatched | Aug 22 |

### 6.3 What Shuhada Needs from Others

| Input | From | When |
|-------|------|------|
| DAF review of top 15 list | DAF | Aug 19-20 |
| Demo scope per product (for meeting value prop) | Hadri + Fuad | Aug 19-20 |
| Collateral (one-pagers) | Azza | Aug 22+ (positioning now signed off) |
| CRM setup (HubSpot or equivalent) | Shuhada | Aug 20 |

---

## 7. Data Hygiene Notes

The source database has 191 organisations (not 193 — 2 were duplicates merged during v5.51 enrichment).

**Enrichment status:**
- 135 organisations (71%) have 3+ identified contacts (enriched)
- 18 organisations (9%) have 1-2 contacts (partial)
- 38 organisations (20%) have 0 contacts (bare — primarily Tier 3 MSBs and Tier 6 fintechs)

**Tier 1 and Tier 2 are fully enriched** — 26/30 Tier 1 and 54/54 Tier 2 have 3+ contacts. No data gap for priority accounts.

---

## 8. Compounding Value Beyond CyberDSA

This segmentation framework serves multiple workstreams beyond CyberDSA:

| Workstream | How This Framework Is Used |
|------------|---------------------------|
| **CyberDSA 2026** | Priority account selection, meeting scheduling, booth engagement |
| **CSM × Aras GTM** | Joint account mapping with CSM coverage plan (10 CSM stakeholders mapped to 93 A-Target orgs) |
| **MCMC/R.I.S.I.K proposal** | Target identification for institutional cybersecurity intelligence platform |
| **Future events** | Reusable account database for any industry event, not CyberDSA-specific |
| **Sales pipeline** | Long-term account development beyond single event |
| **Product roadmap** | Segment-level demand signals (which segments have CISOs, which don't) |

---

## 9. Next Actions

| # | Action | Owner | Due |
|---|--------|-------|-----|
| 1 | DAF reviews and approves this framework | DAF | Aug 19 |
| 2 | DAF reviews top 15 VIP list (add/remove/swap) | DAF | Aug 19 |
| 3 | Shuhada receives framework + CSV | Shuhada | Aug 19 (on delivery) |
| 4 | Shuhada confirms segmentation (2.1) | Shuhada | Aug 20 |
| 5 | Shuhada finalises priority accounts (2.2) | Shuhada | Aug 21 |
| 6 | Shuhada drafts meeting request templates | Shuhada | Aug 21 |
| 7 | First wave meeting requests dispatched (2.4) | Shuhada + DAF | Aug 22 |
| 8 | CRM capture configured | Shuhada | Aug 20 |

---

*This framework unblocks CyberDSA criteria 2.1, 2.2, 2.4, 2.6, 2.9, 2.10 — six criteria from one deliverable. It also operationalises the stakeholder coverage tracker (Metric 7) by providing the engagement owner assignment structure.*
