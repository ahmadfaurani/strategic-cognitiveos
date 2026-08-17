---
id: INT-20260815-003
record_type: intelligence
title: CyberDSA 2026 — Execution Stakeholder Matrix & RACI
created_at: 2026-08-15 16:55:00+00:00
updated_at: 2026-08-15 16:55:00+00:00
owner: faurani-jaafar
intelligence_type: operational
status: active
priority: critical
sensitivity: confidential
lifecycle_state: canonical
confidence: high
summary: Execution stakeholder assignments for CyberDSA 2026 success criteria — RACI matrix, capacity assessment, and critical gaps.
strategic_significance: Identifies single points of failure, critical gaps, and overload risks across 6 dimensions of CyberDSA execution.
mission_alignment:
- productisation
- commercial-growth
- organisational-capability
evidence:
- DEC-20260815-004 War-Room activation
- INT-20260815-002 Success Criteria Definition
- CONV-20260815-003 DAF strategic directives
related_initiatives:
- INIT-20260811-001
- INIT-20260810-003
- INIT-20260804-001
related_stakeholders:
- STK-20260815-004
- STK-20260815-005
- STK-20260815-006
recommended_actions:
- Appoint Programme Coordinator (highest leverage)
- Schedule demo scope lock meeting (Hadri + Fuad)
- Confirm Hadi onboarding date with Kenny
implications:
- DAF carries 21 of 47 criteria (45%) — single point of failure
- Shuhada solo on 8 commercial pipeline criteria — concentration risk
open_questions:
- DevSecOps intern availability for documentation support?
- CRM backup for Shuhada?
tags:
- domain/cybersecurity
- domain/commercial-development
- domain/product-management
- milestone/cyberdsa-2026
- workstream/cybersec-products
- lifecycle/canonical
- priority/critical
source:
  type: internal-analysis
  reference: INT-20260815-002
related_records:
- INT-20260815-002
- DEC-20260815-004
- INIT-20260811-001
- INIT-20260810-003
- INIT-20260804-001
---

# CyberDSA 2026 — Execution Stakeholder Matrix & RACI

**Reference:** INT-20260815-002 (Success Criteria)
**War-Room:** DEC-20260815-004

---

## Stakeholder Summary

| Stakeholder | Role | Status | Criteria Owned | Dimensions Touched |
|-------------|------|--------|----------------|-------------------|
| DAF | Strategic Owner / Director | ✅ Active | 14 | All 6 |
| Hadri | Lead Architect | ✅ Active | 5 | 1, 3, 5 |
| Ahmad Fuad | Product Owner (VoronCitadel) / Tech Owner | ✅ Active | 7 | 1, 4 |
| Shuhada M. Halimi | Sales / Account Coordination | ✅ Active | 8 | 2, 5, 6 |
| Azzatullina Pawanchik | Marketing / WIG | ✅ Active | 5 | 3, 4 |
| Hadi | Incoming Product Manager | ⏳ Pending onboarding | 0 (future) | 1 (planned) |
| Aisha | CSM-Aras PIC (proposed) | ⏳ Pending CSM confirmation | 0 (coordination) | 3 (supporting) |
| Amelia Nadia | Event Lead — CyberDSA | ✅ Active | 1 | 5 (Execution) |
| Kenny Kok | COO, MTAI | ✅ Active (authority) | 0 | — |
| Programme Coordinator | UNFILLED | ❌ CRITICAL GAP | 0 | All (coordination) |

---

## RACI Matrix

**R** = Responsible (does the work) · **A** = Accountable (owns the outcome) · **C** = Consulted · **I** = Informed

### Dimension 1: Product Readiness

| # | Criterion | DAF | Hadri | Fuad | Hadi | Shuhada | Azza |
|---|-----------|-----|-------|------|------|---------|------|
| 1.1 | Demo scope locked | A | R | R | I | — | — |
| 1.2 | VoronCitadel stable | I | A | R | — | — | — |
| 1.3 | GovSec TIP stable | I | R | A | — | — | — |
| 1.4 | ChainSentry go/no-go | A | R | R | — | — | — |
| 1.5 | Demo rehearsal | A | C | C | — | — | C |
| 1.6 | VoronCitadel docs | I | C | R/A | — | — | — |
| 1.7 | GovSec TIP docs | I | C | R/A | — | — | — |
| 1.8 | Hadri handover | A | A | R | — | — | — |
| 1.9 | ChainSentry docs | I | C | R/A | — | — | — |
| 1.10 | Live demo at event | A | R | R | — | — | — |

### Dimension 2: Commercial Pipeline

| # | Criterion | DAF | Hadri | Fuad | Hadi | Shuhada | Azza | Kenny |
|---|-----------|-----|-------|------|------|---------|------|-------|
| 2.1 | 193-org segmented | A | — | — | — | R | — | I |
| 2.2 | 10–15 priority accounts | A | — | — | — | R | — | I |
| 2.3 | Pre-event outreach | A | — | — | — | R | C | I |
| 2.4 | 5 pre-scheduled meetings | A | — | — | — | R | — | I |
| 2.5 | 10 pre-scheduled meetings | A | — | — | — | R | — | I |
| 2.6 | Discovery sessions at event | A | — | — | — | R | — | — |
| 2.7 | 24hr post-event follow-up | A | — | — | — | R | — | — |
| 2.8 | HubSpot CRM updated | A | — | — | — | R | — | I |
| 2.9 | 2–3 POC candidates | A/R | — | — | — | C | — | I |
| 2.10 | 1 signed POC (T+30) | A/R | — | — | — | C | — | I |

### Dimension 3: CSM Partnership

| # | Criterion | DAF | Hadri | Fuad | Aisha | Kenny | CSM (Fahdzli/Zulfeka) |
|---|-----------|-----|-------|------|-------|-------|----------------------|
| 3.1 | CSM participation confirmed | A/R | — | — | — | C | R |
| 3.2 | Aisha PIC resolved | A/R | — | — | R | — | A |
| 3.3 | Joint visible presence | A/R | C | — | C | I | C |
| 3.4 | Integration tracks status | I | R/A | C | — | — | C |
| 3.5 | CSM VIP engagement | A/R | — | — | C | — | C |
| 3.6 | Joint post-event review | A/R | — | — | C | I | C |

### Dimension 4: Marketing & Positioning

| # | Criterion | DAF | Fuad | Azza | Kenny |
|---|-----------|-----|------|------|-------|
| 4.1 | Positioning defined | A/R | — | C | I |
| 4.2 | Product one-pagers | A | C | R | I |
| 4.3 | Booth design confirmed | A | — | R | I |
| 4.4 | Demo walkthrough materials | A | R | R | — |
| 4.5 | Sovereign tech narrative | A/R | — | R | I |
| 4.6 | Marketing campaign to 193 | I | — | R/A | I |

### Dimension 5: Execution

| # | Criterion | DAF | Hadri | Fuad | Shuhada | Azza |
|---|-----------|-----|-------|------|---------|------|
| 5.1 | Staffing roster | A/R | C | C | C | C |
| 5.2 | Booth operational | A | R/A | R | — | — |
| 5.3 | Standalone demo infra | I | R/A | R | — | — |
| 5.4 | Pre-scheduled meetings executed | A | — | — | R | — |
| 5.5 | VIP briefings | A/R | — | — | C | — |
| 5.6 | Lead capture system | A | — | — | R/A | — |
| 5.7 | Daily debriefs | A/R | C | C | C | C |

### Dimension 6: Post-Event Conversion

| # | Criterion | DAF | Shuhada | Kenny |
|---|-----------|-----|---------|-------|
| 6.1 | Post-event review (1 week) | A/R | C | I |
| 6.2 | CRM tagged "CyberDSA 2026" | A | R | I |
| 6.3 | 24hr follow-up sent | A | R | — |
| 6.4 | Pipeline value updated | A/R | C | I |
| 6.5 | 5 discovery calls scheduled | A | R | I |
| 6.6 | 1 POC signed (T+30) | A/R | C | I |
| 6.7 | War-Room deactivated, AAR filed | A/R | — | — |

---

## Stakeholder Load Analysis

| Stakeholder | Criteria as R (Responsible) | Criteria as A (Accountable) | Total Load | Risk |
|-------------|---------------------------|---------------------------|------------|------|
| DAF | 7 | 14 | **21** | 🔴 OVERLOADED — single point of failure |
| Shuhada | 8 | 1 | 9 | 🟡 HIGH — entire commercial pipeline rests on one person |
| Fuad | 7 | 5 | **12** | 🟡 HIGH — product readiness + documentation + demo environments |
| Hadri | 5 | 4 | 9 | 🟡 MODERATE — technical delivery + event infrastructure |
| Azza | 5 | 1 | 6 | 🟢 MANAGEABLE |
| Hadi | 0 | 0 | 0 | ⚪ NOT ONBOARDED — capacity unavailable |
| Aisha | 0 | 0 | 0 | ⚪ PENDING — coordination role only |
| Kenny | 0 | 0 | 0 | ⚪ AUTHORITY ONLY — no execution load |

---

## Critical Gaps

### Gap 1: Programme Coordinator — UNFILLED

**Impact:** DAF carries 21 of 47 criteria (45%). No coordination layer exists between strategic direction and execution owners. Every criterion currently routes through DAF for accountability.

**Risk:** If DAF is unavailable for >48 hours during any checkpoint window, multiple criteria stall. War-room protocol requires 24-hour escalation — but escalation routes to DAF.

**Checkpoint 1 impact:** 5 criteria due Aug 22. DAF owns 3 of them (1.1, 3.2, 4.1). Programme Coordinator could absorb accountability for 1.1 and 4.1, reducing DAF load to 2.

**Recommendation:** Programme Coordinator appointment is the single highest-leverage action. This person absorbs coordination accountability across dimensions, freeing DAF for strategic decisions only.

### Gap 2: Hadi Onboarding — PENDING

**Impact:** Product Manager role for GovSec TIP unoccupied. Criteria 1.3, 1.7, 1.8, 1.10 currently fall to Hadri/Fuad with no PM layer. Once onboarded, Hadi should absorb accountability for GovSec TIP product readiness criteria.

**Risk:** If Hadi onboards after CP2 (Sep 5), his contribution window is compressed to 3 weeks before CP3.

**Recommendation:** Confirm onboarding date with Kenny before CP1 (Aug 22).

### Gap 3: Aisha PIC — PENDING

**Impact:** CSM-Aras coordination channel lacks a dedicated PIC. All CSM communication currently routes through DAF. Criteria 3.1, 3.2, 3.3, 3.5, 3.6 carry coordination overhead that Aisha would absorb.

**Risk:** If CSM higher management meeting slips beyond week of Aug 18, PIC gap persists into CP2.

**Recommendation:** Confirm CSM meeting date before CP1 (Aug 22).

### Gap 4: Shuhada Solo on Commercial Pipeline

**Impact:** 8 of 10 commercial pipeline criteria have Shuhada as sole Responsible. No backup identified. If Shuhada unavailable, entire pipeline track stalls.

**Risk:** 193-org segmentation (2.1) and priority account selection (2.2) are CP1 deliverables — 7 days out.

**Recommendation:** Ember to prepare segmentation analysis framework to support Shuhada's execution. Identify backup for CRM management.

### Gap 5: Fuad Concentration on Product Readiness

**Impact:** Fuad owns 7 of 11 product readiness criteria — demo environments, documentation, handover package. Concurrent with development freeze execution and DevSecOps intern oversight.

**Risk:** Documentation scope is 3 products × 6 categories = 18 deliverables. CP2 (Sep 5) deadline for VoronCitadel docs + handover package is aggressive.

**Recommendation:** Confirm whether DevSecOps intern is available to support documentation compilation under Fuad's direction.

---

## Stakeholder Detail

### DAF — Strategic Owner
- **Role:** Director, Cyber Security Practice, Aras Integrasi
- **Authority:** Final decision on all criteria
- **Owned criteria:** 1.1, 1.4, 1.5, 2.6, 2.9, 2.10, 3.1, 3.2, 3.3, 3.5, 3.6, 4.1, 4.5, 5.1, 5.4, 5.5, 5.7, 6.1, 6.4, 6.6, 6.7
- **Dimensions:** All 6
- **Load risk:** 🔴 OVERLOADED (21 criteria)
- **Mitigation:** Appoint Programme Coordinator to absorb coordination accountability

### Hadri — Lead Architect
- **Role:** Technical architecture, delivery ownership for GovSec TIP
- **Authority:** Technical decisions on demo scope, infrastructure, integration
- **Owned criteria:** 1.3, 1.10, 3.4, 5.2, 5.3
- **Dimensions:** 1 (Product Readiness), 3 (CSM Partnership), 5 (Execution)
- **Load risk:** 🟡 MODERATE (9 criteria) — but SPOF for all technical infrastructure
- **Mitigation:** Hadi onboarding absorbs GovSec TIP PM responsibilities; Fuad supports demo environment setup

### Ahmad Fuad — Product Owner / Technical Owner
- **Role:** VoronCitadel Product Owner, current technical owner for GovSec TIP (pre-handover)
- **Authority:** Product documentation, demo environment build, handover package compilation
- **Owned criteria:** 1.2, 1.6, 1.7, 1.8, 1.9, 4.4 (shared)
- **Dimensions:** 1 (Product Readiness), 4 (Marketing — materials support)
- **Load risk:** 🟡 HIGH (12 criteria) — documentation scope is 18 deliverables across 3 products
- **Mitigation:** DevSecOps intern support for documentation; Hadi absorbs GovSec TIP post-handover

### Shuhada M. Halimi — Sales / Account Coordination
- **Role:** Sales team, account coordination, CRM management
- **Authority:** Account selection, outreach execution, lead capture
- **Owned criteria:** 2.1, 2.2, 2.3, 2.4, 2.5, 2.7, 2.8, 5.6, 6.2, 6.3, 6.5
- **Dimensions:** 2 (Commercial Pipeline), 5 (Execution), 6 (Post-Event Conversion)
- **Load risk:** 🟡 HIGH (9 criteria) — entire commercial pipeline solo
- **Mitigation:** Ember prepares 193-org segmentation analysis as input support; identify CRM backup

### Azzatullina Pawanchik — Marketing / WIG
- **Role:** Marketing campaign, collateral, booth design
- **Authority:** Marketing materials, booth logistics, campaign execution
- **Owned criteria:** 4.2, 4.3, 4.6, 4.4 (shared), 4.5 (shared)
- **Dimensions:** 4 (Marketing & Positioning), 3 (CSM — joint presence support)
- **Load risk:** 🟢 MANAGEABLE (6 criteria)
- **Dependencies:** Needs positioning statement (4.1) from DAF before one-pagers (4.2) can be finalised; needs product info from Fuad for demo walkthrough materials (4.4)

### Hadi — Incoming Product Manager
- **Role:** GovSec TIP Product Manager (incoming)
- **Status:** ⏳ Not yet onboarded
- **Planned criteria:** Should absorb accountability for 1.3, 1.7, 1.10 from Hadri/Fuad post-onboarding
- **Onboarding dependency:** Kenny Kok to confirm date
- **Risk:** If onboarding after CP2 (Sep 5), contribution window compresses to 3 weeks before CP3

### Aisha — Proposed CSM-Aras PIC
- **Role:** Communication coordination between CSM and Aras
- **Status:** ⏳ Pending CSM higher management confirmation
- **Planned criteria:** Coordination support for 3.1, 3.2, 3.3, 3.5, 3.6
- **Confirmation dependency:** CSM higher management meeting (week of Aug 18)
- **Risk:** If not confirmed by CP1 (Aug 22), criterion 3.2 flags RED

### Kenny Kok — COO, MTAI
- **Role:** Authority for sales team, onboarding decisions
- **Authority level:** Approves resource allocation, confirms Hadi onboarding
- **Owned criteria:** 0 (authority, not execution)
- **Informed on:** All commercial pipeline criteria, marketing campaign

---

## Checkpoint 1 (Aug 22) — Stakeholder Readiness

| Criterion | Owner | Status | Blocker |
|-----------|-------|--------|---------|
| 1.1 Demo scope locked | Hadri + Fuad | ⏳ Not started | Meeting not scheduled |
| 2.1 193-org segmented | Shuhada | ⏳ Not started | Awaiting input framework |
| 2.2 10–15 priority accounts | Shuhada | ⏳ Not started | Depends on 2.1 |
| 3.2 Aisha PIC resolved | DAF | ⏳ Pending | CSM meeting not scheduled |
| 4.1 Positioning defined | DAF | ✅ Draft exists | Needs formal sign-off |

**7 days to CP1. 4 of 5 criteria not started. 1 blocker is external (CSM meeting).**

---

## Recommendations

1. **Appoint Programme Coordinator this week** — single highest-leverage action. Absorbs coordination accountability from DAF across all 6 dimensions.

2. **Schedule demo scope lock meeting (Hadri + Fuad) immediately** — Criterion 1.1 is CP1, 7 days out. Hadri and Fuad need a focused session to define what is demonstrated and what is not.

3. **Confirm Hadi onboarding date with Kenny** — If onboarding slips past Sep 1, Hadi's contribution window is too compressed. Push for Aug 25 start.

4. **Confirm CSM higher management meeting for Aisha PIC** — Week of Aug 18. If this slips, 3.2 flags RED at CP1.

5. **Ember to prepare 193-org segmentation framework** — Support Shuhada's execution of 2.1 and 2.2. Segmentation criteria, tier definitions, and initial clustering ready for Shuhada to validate and execute against.

6. **Confirm DevSecOps intern availability** — Fuad's documentation load (18 deliverables) needs execution support. Intern can compile documentation under Fuad's direction.

7. **Identify CRM backup for Shuhada** — Solo ownership of 8 commercial pipeline criteria is a concentration risk. Minimum: one person trained on HubSpot CRM intake as backup.
