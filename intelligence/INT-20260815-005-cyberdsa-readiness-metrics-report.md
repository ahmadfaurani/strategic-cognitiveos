---
id: INT-20260815-005
record_type: intelligence
title: CyberDSA 2026 — Readiness Metrics Analytical Report
created_at: 2026-08-15 18:15:00+00:00
updated_at: 2026-08-15 18:15:00+00:00
owner: faurani-jaafar
intelligence_type: operational
status: active
priority: critical
sensitivity: confidential
lifecycle_state: canonical
confidence: high
summary: Detailed analytical assessment of the 8 readiness metrics from the CSM-Aras Stakeholder Coverage & Communication Ownership Plan against current operational state, with gap analysis, risk assessment, and remediation recommendations.
strategic_significance: Readiness metrics define the operational threshold for CyberDSA stakeholder coverage. 3 of 8 metrics currently unmet. Report identifies specific blockers, owners, and remediation paths for each metric.
mission_alignment:
- cybersecurity
- stakeholder-engagement
- organisational-capability
- commercial-development
evidence:
- 'INT-20260815-004: CSM-Aras Stakeholder Coverage & Communication Ownership Plan'
- 'INT-20260815-003: Execution Stakeholder Matrix & RACI'
- 'INT-20260815-002: CyberDSA Success Criteria Definition'
- 'CONV-20260815-005: Document intake record'
- 'DEC-20260815-004: War-room activation'
recommended_actions:
- Create stakeholder coverage tracker (Metric 7 blocker)
- Implement pre/during/post meeting protocol (Metric 6 blocker)
- Appoint Programme Coordinator (Metric 8 — SPOF elimination)
- Begin specialist relationship activation (Metric 3 reinforcement)
related_records:
- INT-20260815-004
- INT-20260815-003
- INT-20260815-002
- CONV-20260815-005
- DEC-20260815-004
- INIT-20260810-003
implications:
- 3 of 8 readiness metrics at 0% — all require execution, not planning
- 5 of 8 metrics met by plan design — but require operational enforcement
- 'Weekly review cadence (Action #7) is the enforcement mechanism for all metrics'
- Programme Coordinator appointment remains highest-leverage SPOF intervention
open_questions:
- Who creates and maintains the stakeholder coverage tracker?
- What is the format for pre/during/post meeting owner assignment?
- Can Hadri absorb tracker ownership on top of 9 existing criteria?
tags:
- domain/cybersecurity
- domain/stakeholder-engagement
- domain/organisational-capability
- milestone/cyberdsa-2026
- workstream/cybersec-products
- lifecycle/canonical
- priority/critical
source:
  type: internal-analysis
  reference: INT-20260815-004
---

# CyberDSA 2026 — Readiness Metrics Analytical Report

**Reference:** CSM-Aras Stakeholder Coverage & Communication Ownership Plan (13 Aug 2026)
**Intake:** CONV-20260815-005, INT-20260815-004
**Cross-Reference:** INT-20260815-002 (Success Criteria), INT-20260815-003 (RACI Matrix)
**Date:** 15 August 2026
**CP1 Deadline:** 22 August 2026 (7 days)

---

## Executive Summary

The Stakeholder Coverage Plan defines 8 binary readiness metrics — each targeting 100% coverage or 0 single-points-of-failure. This report assesses each metric against current operational state using evidence from CognitiveOS records.

**Current state: 5 of 8 metrics MET (by plan design), 3 of 8 at 0%.**

The 3 unmet metrics share a common characteristic: they require **execution and enforcement**, not planning. The plan defines the target state; operationalising it requires tracker creation, meeting protocol implementation, and SPOF elimination through Programme Coordinator appointment.

---

## Metric 1: Priority CSM Stakeholders with Named Primary Owner

| Field | Value |
|---|---|
| **Target** | 100% |
| **Current Status** | ✅ MET — 10/10 |
| **Confidence** | [HIGH] |
| **Evidence Source** | INT-20260815-004, Table 2 (Coverage Matrix) |

### Assessment

All 10 priority CSM stakeholders have a named primary Aras owner in the coverage plan:

| CSM Stakeholder | Primary Aras Owner | STK Record |
|---|---|---|
| Mohammad Fahdzli bin Abdul Rauf | DAF | STK-20260804-001 |
| Azrul Nazim Abdul Aziz | DAF | STK-20260813-008 |
| Mohammad Zaharudin Ahmad Darus | Hadri | STK-20260804-011 |
| Mohamad Hafiz Rahman | Hadri | STK-20260804-010 |
| Mohamed Iqbal Tajol Azmi | Fuad | STK-20260813-009 |
| Muhammad Amirul Bukhari Razak | Fuad | STK-20260813-010 |
| Nurshahira Mohd | Hadri | STK-20260813-011 |
| Nazri Ahmad Zamani | Hadri | STK-20260804-012 |
| Suraya Hani Ahmad Zaki | DAF / Hadri | STK-20260813-012 |
| Siti Aishah Omar (Aisha) | DAF | STK-20260815-001 |

### Risk

**LOW.** All 10 stakeholders are mapped to existing STK records. DAF remains primary on 4 of 10 — concentrated but not a SPOF since each has 2–4 additional coverage paths.

### Gap

None. Metric is met by plan design.

---

## Metric 2: Priority CSM Stakeholders with at Least One Secondary Owner

| Field | Value |
|---|---|
| **Target** | 100% |
| **Current Status** | ✅ MET — 10/10 |
| **Confidence** | [HIGH] |
| **Evidence Source** | INT-20260815-004, Table 2 (Additional Coverage column) |

### Assessment

All 10 stakeholders have at least 2 additional Aras coverage paths beyond the primary owner:

| CSM Stakeholder | Primary | Additional Coverage | Paths |
|---|---|---|---|
| Fahdzli | DAF | Kenny; Farul; Hadri | 4 |
| Azrul | DAF | Hadri; Kenny; Shuhada; Zulfelka | 5 |
| Zaharudin | Hadri | Fuad; Farul; DAF | 4 |
| Hafiz Rahman | Hadri | Fuad; Farul | 3 |
| Iqbal | Fuad | Hadri; Farul | 3 |
| Amirul | Fuad | Hadri; Farul | 3 |
| Nurshahira | Hadri | Fuad; Shuhada | 3 |
| Nazri | Hadri | Fuad; Farul; DAF | 4 |
| Suraya | DAF / Hadri | Fuad; Shuhada | 4 |
| Siti Aishah | DAF | Azza; Shuhada; Hadri | 4 |

**Average coverage paths per stakeholder: 3.7** (target was ~3, achieved).

### Risk

**LOW.** No stakeholder has fewer than 3 total Aras contacts. The plan's governance principle ("No priority CSM stakeholder should depend on a single Aras contact for all matters") is satisfied.

### Gap

None operational. However, **secondary owners have not yet been formally notified or have accepted their coverage responsibilities.** The plan is a working document — Action #3 (activate specialist relationships) is the mechanism for operationalising this metric. Until specialists begin direct working engagement with CSM counterparts, this metric is met on paper but not in practice.

**Adjusted confidence if measuring operational activation (not plan assignment): [MEDIUM]**

---

## Metric 3: Priority Technical Stakeholders with Direct Fuad/Hadri/Farul Coverage

| Field | Value |
|---|---|
| **Target** | 100% |
| **Current Status** | ✅ MET (by design) — 5/5 |
| **Confidence** | [MEDIUM] |
| **Evidence Source** | INT-20260815-004, Coverage Matrix filtered for technical stakeholders |

### Assessment

The 5 CSM technical stakeholders are:

| CSM Technical Stakeholder | Direct Aras Technical Coverage | Primary | Secondary |
|---|---|---|---|
| Zaharudin (AI platform, intelligence platform) | Hadri (primary), Fuad (secondary), Farul (secondary) | ✅ | ✅ |
| Hafiz Rahman (GovSec/TI, telemetry, architecture) | Hadri (primary), Fuad (secondary), Farul (secondary) | ✅ | ✅ |
| Iqbal (intelligence platform, AI technical) | Fuad (primary), Hadri (secondary), Farul (secondary) | ✅ | ✅ |
| Amirul (development, AI integration) | Fuad (primary), Hadri (secondary), Farul (secondary) | ✅ | ✅ |
| Nazri (R&D, UPM/Purple Teaming, AI infra) | Hadri (primary), Fuad (secondary), Farul (secondary), DAF (escalation) | ✅ | ✅ |

All 5 have direct coverage from at least 2 of the 3 technical Aras stakeholders (Fuad, Hadri, Farul).

### Risk

**MEDIUM.** Coverage is assigned but not yet activated. Action #3 specifies "begin direct working engagement with relevant CSM counterparts before CyberDSA" — no date specified. If specialist activation doesn't begin before CP2 (Sep 5), technical relationships will be paper-only entering the final 4-week sprint.

### Secondary Risk: Fuad Overload

Fuad is primary on 2 and secondary on 3 of the 5 technical stakeholders. He simultaneously owns 12 CyberDSA execution criteria including 18 documentation deliverables. Adding 5 direct CSM technical relationships creates a **new SPOF vector on Fuad**.

**[MEDIUM] Confidence** — metric is met by assignment but activation and capacity risk are unresolved.

### Gap

- **Activation timing:** No date for specialist relationship kickoff
- **Fuad capacity:** 5 CSM relationships + 12 criteria + 18 docs = overload risk
- **Farul scope:** Farul is secondary on 4 of 5 but his current engagement level with CSM technical stakeholders is unconfirmed

---

## Metric 4: Priority Market/Commercial Stakeholders with Direct Azza/Shuhada/Zulfelka Coverage

| Field | Value |
|---|---|
| **Target** | 100% |
| **Current Status** | ✅ MET (by design) — 3/3 |
| **Confidence** | [MEDIUM] |
| **Evidence Source** | INT-20260815-004, Coverage Matrix filtered for market/commercial stakeholders |

### Assessment

The 3 CSM market/commercial stakeholders are:

| CSM Stakeholder | Aras Coverage | Primary | Specialists |
|---|---|---|---|
| Fahdzli (strategic partnership) | DAF (primary), Kenny; Farul; Hadri | ✅ | Zulfelka for commercial |
| Azrul (programme mobilisation, account activation) | DAF (primary), Hadri; Kenny; Shuhada; Zulfelka | ✅ | Shuhada + Zulfelka |
| Siti Aishah / Aisha (market activation) | DAF (primary), Azza; Shuhada; Hadri | ✅ | Azza + Shuhada |

All 3 have direct coverage from at least 2 of the 4 market/commercial Aras stakeholders (Azza, Shuhada, Zulfelka, DAF).

### Risk

**MEDIUM.** Two sub-risks identified:

1. **Zulfelka identity/role clarification:** The document refers to "Zulfelka" as a CSM stakeholder with commercial coverage scope. STK-20260804-002 records "Zulfeka Zainal Abidin" with a noted spelling discrepancy. MWR-20260813-001 flagged: *"Zulfelka (CSM Head of Commercial) — GAP: no Aras-side owner."* The coverage plan assigns Aras coverage TO CSM's Zulfelka, but the MWR flagged that Zulfelka himself lacks an Aras-side primary counterpart. The plan partially addresses this by assigning Kenny as executive cover, but no dedicated Aras commercial specialist is named as primary.

2. **Azza activation dependency:** Azza is assigned market activation ownership (campaign, collateral, invitations, lead capture) but depends on DAF's positioning statement (Criterion 4.1, CP1 Aug 22) before one-pagers (4.2) can be finalised. If 4.1 slips, Azza's entire workstream is blocked.

**[MEDIUM] Confidence** — coverage assigned but Zulfelka gap and Azza dependency chain create execution risk.

### Gap

- **Zulfelka Aras counterpart:** Plan assigns DAF/Kenny as cover but no dedicated commercial specialist
- **Azza blocking dependency:** Positioning statement (4.1) must be signed off before market activation workstream can proceed
- **Shuhada solo risk persists:** Formalised in role but still sole Responsible on 8 commercial pipeline criteria

---

## Metric 5: Strategic Stakeholders with Defined Executive Escalation Path

| Field | Value |
|---|---|
| **Target** | 100% |
| **Current Status** | ✅ MET — 10/10 |
| **Confidence** | [HIGH] |
| **Evidence Source** | INT-20260815-004, Coverage Matrix + Communication Ownership Model |

### Assessment

The plan defines executive escalation paths through two mechanisms:

**Mechanism 1: Coverage Matrix** — Every stakeholder has at least one executive-level Aras contact (Kenny, Farul, or DAF) in their additional coverage:

| Stakeholder | Executive Escalation |
|---|---|
| Fahdzli | Kenny; DAF |
| Azrul | Kenny; DAF |
| Zaharudin | DAF |
| Hafiz Rahman | Farul |
| Iqbal | Farul |
| Amirul | Farul |
| Nurshahira | (Hadri → DAF escalation) |
| Nazri | DAF |
| Suraya | DAF |
| Siti Aishah | DAF |

**Mechanism 2: Communication Ownership Model** — Table 4 defines escalation by topic:
- Strategic direction → DAF (primary), Kenny/Farul (cover)
- Commercial opportunity → Zulfelka/DAF (primary), Kenny (cover)
- AI platform → Farul (primary), DAF (escalation)

### Risk

**LOW.** Escalation paths are well-defined. However, two nuances:

1. **Nurshahira** has the thinnest executive path — her coverage is Hadri (primary), Fuad, Shuhada. No named executive in her additional coverage. Escalation would route through Hadri → DAF, which is a 2-hop path. Every other stakeholder has a direct executive name.

2. **Escalation protocol undefined:** The plan names WHO to escalate to but not HOW or WHEN. No defined response SLA, no escalation trigger criteria, no escalation format.

### Gap

- **Nurshahira executive path:** Add explicit executive escalation (DAF or Kenny)
- **Escalation protocol:** Define trigger criteria, response SLA, and format for executive escalation

---

## Metric 6: Priority CyberDSA Meetings with Named Pre/During/Post Owners

| Field | Value |
|---|---|
| **Target** | 100% |
| **Current Status** | ❌ NOT MET — 0% |
| **Confidence** | [HIGH] |
| **Evidence Source** | INT-20260815-004, Section 8 (Strategic Engagement Flow) + Section 10 (Governance) |

### Assessment

The plan defines a clear meeting lifecycle protocol:

| Stage | Owner | Activities |
|---|---|---|
| **Before** | Shuhada | Account intelligence; attendee verification; meeting schedule; CRM context |
| **Before** | Azza | Messaging; collateral; approved customer-facing communication |
| **Before** | Hadri | Solution alignment; technical context; CSM coordination |
| **Before** | Fuad | Demo readiness; product technical preparation; likely technical Q&A |
| **During** | DAF | Strategic framing; customer/business problem; partnership direction |
| **During** | CSM rep | CSM context; credibility; domain contribution |
| **During** | Fuad / Hadri | Product demonstration; architecture; technical response |
| **During** | Zulfelka | Commercial follow-through where appropriate |
| **After** | Shuhada | CRM capture; actions; meeting record; assignment |
| **After** | Hadri / Fuad | Technical discovery; POC scoping; technical actions |
| **After** | DAF / Zulfelka | Opportunity progression; commercial next step; escalation |

**The protocol is defined but NOT implemented.** No priority CyberDSA meeting has been scheduled with named pre/during/post owners because:

1. No priority customer meetings have been scheduled yet (Criterion 2.4, CP4 Sep 28)
2. No meeting template or tracker exists for assigning pre/during/post owners
3. The 193-org database hasn't been segmented (Criterion 2.1, CP1 Aug 22) — so no priority accounts are identified to schedule meetings with

### Dependency Chain

```
2.1 (193-org segmentation) → 2.2 (priority accounts) → 2.4 (pre-scheduled meetings) → Metric 6 (meeting owners)
```

Metric 6 cannot be operationalised until 2.1 and 2.2 are complete. Both are CP1 criteria (Aug 22) currently at 0%.

### Risk

**HIGH.** This metric has a 3-step dependency chain, all currently at 0%. The earliest this metric can be operationalised is after CP1 (Aug 22), assuming 2.1 and 2.2 are completed on time. If CP1 slips, Metric 6 slips to after CP2 (Sep 5), compressing meeting preparation to 3 weeks before the event.

### Gap

- **2.1 193-org segmentation:** Not started — Shuhada awaiting input framework
- **2.2 Priority accounts:** Not started — depends on 2.1
- **Meeting template:** No standardised template for pre/during/post owner assignment
- **Meeting tracker:** Not created (Action #4 from plan)

### Remediation

1. **Ember:** Deliver 193-org segmentation framework to Shuhada this week
2. **Shuhada:** Execute 2.1 and 2.2 by CP1 (Aug 22)
3. **Hadri/Shuhada:** Create stakeholder coverage tracker (Action #4) with meeting protocol section
4. **DAF:** Once priority accounts identified, map meetings with named pre/during/post owners

---

## Metric 7: Priority Stakeholders with Current Communication/Action Status Captured in Tracker

| Field | Value |
|---|---|
| **Target** | 100% |
| **Current Status** | ❌ NOT MET — 0% |
| **Confidence** | [HIGH] |
| **Evidence Source** | INT-20260815-004, Action #4 (Create stakeholder coverage tracker) |

### Assessment

**The tracker does not exist.** Action #4 from the plan's Immediate Action Plan assigns:

> **Action:** Create stakeholder coverage tracker
> **Owner:** Hadri / Shuhada
> **Required output:** Capture CSM stakeholder, primary owner, cover, purpose, last engagement, next action, and escalation path.

No tracker has been created. No format has been defined. No owner has been formally assigned the task.

### Current Tracking State

CognitiveOS records contain the data that WOULD populate the tracker:

| Data Point | Source | Current State |
|---|---|---|
| CSM stakeholder details | STK records (10 stakeholders) | ✅ Exists |
| Primary/secondary owners | INT-20260815-004 coverage matrix | ✅ Exists |
| Coverage purpose | INT-20260815-004 coverage matrix | ✅ Exists |
| Last engagement | Individual STK records | ⚠️ Partial — some have dates, some say "Not yet directly engaged" |
| Next engagement | Individual STK records | ⚠️ Partial — some have dates, some say "Pending" |
| Escalation path | INT-20260815-004 communication model | ✅ Exists |
| Action status | Individual STK records + ACT records | ⚠️ Scattered across records, not consolidated |

**The data exists in CognitiveOS but is not consolidated into a single operational tracker.**

### Risk

**HIGH.** Without a tracker, the weekly coverage review (Action #7) has no input. The review becomes a verbal discussion rather than a data-driven assessment. Coverage gaps and SPOFs cannot be identified systematically.

Additionally, Hadri is assigned as co-owner of the tracker (Action #4) but already carries 9 CyberDSA execution criteria. Adding tracker maintenance to his load is a capacity risk.

### Gap

- **Tracker format:** Not defined (spreadsheet? CognitiveOS record? Dashboard?)
- **Tracker owner:** Assigned to Hadri/Shuhada but neither has been formally tasked
- **Tracker population:** Data exists in CognitiveOS but requires consolidation
- **Tracker maintenance cadence:** Not defined (weekly update implied by Action #7 but not explicit)

### Remediation

1. **Define tracker format:** Recommend a CognitiveOS record (live document) or a structured spreadsheet synced to CognitiveOS
2. **Assign single owner:** Hadri is co-owner but already at 9 criteria. Recommend Shuhada as primary owner with Hadri as reviewer
3. **Populate from CognitiveOS:** Extract data from STK records and INT-20260815-004 into tracker
4. **Set update cadence:** Weekly, aligned with Action #7 (coverage review)
5. **Define fields:** Stakeholder | Primary Owner | Secondary | Specialist | Escalation | Last Engagement | Next Action | Status | SPOF Flag

---

## Metric 8: Single-Person Dependency for Critical CSM Workstream

| Field | Value |
|---|---|
| **Target** | 0 |
| **Current Status** | ❌ NOT MET — ≥3 SPOFs identified |
| **Confidence** | [HIGH] |
| **Evidence Source** | INT-20260815-003 (RACI Matrix), INT-20260815-004 (Coverage Plan) |

### Assessment

The plan's governance principle states: *"Any single point of failure identified in the coverage map should be corrected before the final CyberDSA readiness review."*

**Current SPOFs identified from cross-referencing Coverage Plan (INT-004) with RACI Matrix (INT-003):**

| # | SPOF | Evidence | Impact | Status |
|---|---|---|---|---|
| 1 | **DAF — 21 of 47 criteria (45%)** | INT-003, RACI Matrix | If DAF unavailable >48hrs, multiple criteria stall across all 6 dimensions | ❌ Unresolved |
| 2 | **Shuhada — solo on 8 commercial pipeline criteria** | INT-003, Dimension 2 RACI | If Shuhada unavailable, entire commercial pipeline track stalls | ❌ Unresolved |
| 3 | **Fuad — 12 criteria + 5 CSM technical relationships** | INT-003 + INT-004 | If Fuad unavailable, product readiness + documentation + CSM technical engagement all stall | ❌ Unresolved |
| 4 | **Programme Coordinator — UNFILLED** | INT-003, Gap 1 | No coordination layer between strategy and execution; all accountability routes through DAF | ❌ Unresolved |
| 5 | **Hadi — NOT ONBOARDED** | INT-003, Gap 2 | GovSec TIP product management unoccupied; PM layer missing | ❌ Unresolved |
| 6 | **Aisha PIC — PENDING** | INT-003, Gap 3 | CSM-Aras coordination channel has no dedicated PIC | ❌ Unresolved |

### What the Coverage Plan Addresses

The coverage plan reduces **relationship SPOFs** (Metric 1–5) by distributing CSM contact paths. However, it does NOT address **execution SPOFs**:

| SPOF Type | Coverage Plan Impact | Execution Impact |
|---|---|---|
| DAF relationship dependency | ✅ Reduced — 4 stakeholders now have 2–4 alternate paths | ❌ Unchanged — DAF still owns 21 execution criteria |
| Shuhada relationship dependency | ✅ Reduced — Zulfelka added as commercial cover | ❌ Unchanged — still sole R on 8 criteria |
| Fuad relationship dependency | ✅ Reduced — Hadri/Farul as secondary on technical stakeholders | ❌ Worsened — now primary on 2 + secondary on 3 CSM relationships, adding to 12 criteria load |
| Programme Coordinator | ❌ Not addressed — plan distributes but doesn't centralise coordination | ❌ Unchanged |
| Hadi onboarding | ❌ Not addressed | ❌ Unchanged |
| Aisha PIC | ✅ Partially addressed — plan defines coverage model for CSM communication | ❌ Unchanged — still pending CSM confirmation |

### Risk

**CRITICAL.** The plan's target of 0 SPOFs is the most ambitious metric. It requires not just relationship coverage (which the plan provides) but execution coverage (which requires structural changes beyond the plan's scope):

1. **Programme Coordinator** — absorbs coordination accountability from DAF
2. **Hadi onboarding** — absorbs GovSec TIP PM from Hadri/Fuad
3. **Aisha confirmation** — absorbs CSM coordination from DAF
4. **CRM backup for Shuhada** — absorbs commercial pipeline continuity
5. **Documentation support for Fuad** — absorbs doc load (DevSecOps intern?)

Until these 5 structural gaps are closed, Metric 8 cannot reach 0.

### Gap

- **5 structural SPOFs** identified, all requiring personnel decisions (not planning)
- **3 of 5** are pending external triggers (Hadi onboarding via Kenny, Aisha via CSM, Programme Coordinator via DAF appointment)
- **2 of 5** are internal (Shuhada backup, Fuad documentation support)

### Remediation

1. **DAF: Appoint Programme Coordinator** — highest leverage single action. Absorbs coordination accountability, reduces DAF from 21 to ~14 criteria.
2. **DAF/Kenny: Confirm Hadi onboarding date** — target Aug 25 start. Absorbs GovSec TIP PM, reduces Fuad/Hadri load.
3. **DAF: Confirm CSM meeting for Aisha PIC** — week of Aug 18. Absorbs CSM coordination, reduces DAF's CSM communication load.
4. **DAF: Identify CRM backup for Shuhada** — minimum 1 person trained on HubSpot intake.
5. **DAF/Kenny: Confirm DevSecOps intern availability** — supports Fuad's documentation compilation.

---

## Cross-Metric Dependency Map

```
Metric 1 (Primary owners) ──────────────────── ✅ MET (by plan)
Metric 2 (Secondary owners) ────────────────── ✅ MET (by plan, activation pending)
Metric 3 (Technical coverage) ──────────────── ✅ MET (by plan, activation + Fuad capacity risk)
Metric 4 (Market/commercial coverage) ──────── ✅ MET (by plan, Zulfelka gap + Azza dependency)
Metric 5 (Executive escalation) ────────────── ✅ MET (by plan, protocol undefined)
Metric 6 (Meeting pre/during/post owners) ──── ❌ 0% (blocked by 2.1 → 2.2 → 2.4 dependency chain)
Metric 7 (Tracker exists and current) ──────── ❌ 0% (tracker not created, Action #4 unstarted)
Metric 8 (Zero SPOFs) ──────────────────────── ❌ ≥3 SPOFs (requires 5 structural personnel decisions)
```

**Key insight:** Metrics 6, 7, and 8 share a common root — they require **execution and enforcement**, not planning. The plan defines the target state; operationalising it requires:

- Metric 6: 193-org segmentation → priority accounts → meeting scheduling
- Metric 7: Tracker creation (Action #4) + weekly maintenance (Action #7)
- Metric 8: Programme Coordinator + Hadi + Aisha + CRM backup + doc support

---

## Risk-Weighted Readiness Score

| Metric | Target | Current | Gap | Risk Level | Remediation Owner | Days to CP1 |
|---|---|---|---|---|---|---|
| 1. Primary owners | 100% | 100% | 0% | LOW | — | — |
| 2. Secondary owners | 100% | 100%* | 0%* | MEDIUM | Hadri (activation) | 7 |
| 3. Technical coverage | 100% | 100%* | 0%* | MEDIUM | Fuad (capacity) | 7 |
| 4. Market/commercial coverage | 100% | 100%* | 0%* | MEDIUM | DAF (4.1 sign-off) | 7 |
| 5. Executive escalation | 100% | 100% | 0% | LOW | — | — |
| 6. Meeting owners | 100% | 0% | 100% | HIGH | Shuhada (2.1/2.2) → DAF (meetings) | 7 |
| 7. Tracker current | 100% | 0% | 100% | HIGH | Hadri/Shuhada (Action #4) | 7 |
| 8. Zero SPOFs | 0 | ≥3 | 3+ | CRITICAL | DAF (personnel decisions) | 7 |

*Met by plan design, not yet operationally activated.

**Overall readiness: 62.5% (5/8 met)** — but only 37.5% if measuring operational activation rather than plan assignment.

---

## Recommendations (Prioritised)

### Immediate (Before CP1 — Aug 22)

1. **DAF: Sign off positioning statement (4.1)** — unblocks Azza's entire market activation workstream
2. **Ember: Deliver 193-org segmentation framework** — unblocks Shuhada for 2.1/2.2, which unblocks Metric 6
3. **Hadri/Shuhada: Create stakeholder coverage tracker** — operationalises Metric 7, enables weekly review (Action #7)
4. **DAF: Appoint Programme Coordinator** — highest-leverage SPOF intervention for Metric 8
5. **DAF/Kenny: Confirm Hadi onboarding date** — target Aug 25, unblocks Fuad/Hadri capacity

### Near-Term (Before CP2 — Sep 5)

6. **Hadri/Fuad/Farul/Azza/Shuhada/Zulfelka: Activate specialist relationships** — Action #3, converts paper coverage to operational relationships
7. **DAF: Confirm CSM meeting for Aisha PIC** — resolves Metric 8 SPOF #6
8. **DAF: Identify CRM backup for Shuhada** — resolves Metric 8 SPOF #2
9. **DAF/Kenny: Confirm DevSecOps intern** — resolves Metric 8 SPOF #3 (Fuad overload)

### Ongoing

10. **DAF/Hadri: Weekly coverage review** — Action #7, enforcement mechanism for all 8 metrics
11. **DAF: Define escalation protocol** — trigger criteria, response SLA, format for Metric 5
12. **DAF: Address Nurshahira executive path** — add explicit executive name for Metric 5 completeness

---

## Conclusion

The Stakeholder Coverage Plan is **architecturally sound** — it correctly identifies the target state and defines the right structure. Five of eight metrics are met by plan design.

However, **three metrics remain at 0%** because they require execution, not planning:

- **Metric 6 (Meeting protocol):** Blocked by a 3-step dependency chain starting with 193-org segmentation
- **Metric 7 (Tracker):** Not started — Action #4 unassigned in practice
- **Metric 8 (Zero SPOFs):** Requires 5 personnel decisions, 3 of which are pending external triggers

The highest-leverage action available is **Programme Coordinator appointment** — it directly addresses Metric 8 (SPOF #1 and #4) and indirectly supports Metric 7 (tracker ownership could shift from Hadri to the coordinator).

The plan's own governance rule is clear: *"Any single point of failure identified in the coverage map should be corrected before the final CyberDSA readiness review."* The final readiness review is CP4 (Sep 28). The clock starts now.
