---
id: ART-20260904-001
record_type: artifact
title: "Activation Meeting Agenda — Sep 4 2026"
created_at: 2026-09-04T05:05:00+00:00
updated_at: 2026-09-04T05:05:00+00:00
owner: faurani-jaafar
status: active
sensitivity: internal
lifecycle_state: canonical
tags:
  - domain/governance
  - domain/organisational-capability
  - domain/strategic
  - artifact/brief
  - lifecycle/canonical
source:
  type: cognitive-loop
  reference: "INT-20260904-006, INT-20260904-002 through 005"
related_records:
  - INT-20260904-002
  - INT-20260904-003
  - INT-20260904-004
  - INT-20260904-005
  - INT-20260904-006
---

# Activation Meeting Agenda — Sep 4, 2026

**Prepared from:** INT-20260904-002 through 006 (Four-Directive Discovery + Cognitive Loop)
**Meeting purpose:** Convert discovery findings into assigned, deadline-gated actions
**Time constraint:** CyberDSA Oct 10 (T-36). QC deadline Sep 28. C1 credential rotation 16 days overdue.

---

## 1. Syahir — Priority Sequencing & C1 Execution

**Context:** Syahir is triple-hatted (QC Engineer + POC Engineer + chain:SENTRY Engineering Owner). Four decisions assign work. Zero are in execution. C1 credential rotation is 16+ days overdue.

**Discussion points:**
- C1 credential rotation — who drives this TODAY? Syahir executes, Fuad supports (2-3h). This is 16 days of exposed supplier credentials. Blocks C2 (Deployment Parity, Sep 10) and entire Track C.
- Priority sequencing: QC preparation (Sep 28) is hard-gated. chain:SENTRY Phase 0 work happens AFTER QC is on track (no later than Sep 14). If Syahir can't do both by Sep 28 → chain:SENTRY de-scoped from CyberDSA demo. Formal decision needed.
- Hadri → Syahir chain:SENTRY knowledge transfer — schedule this week. 2-hour briefing + 1-page handover doc. 43 uncommitted mods, no migration ledger. Without this, Syahir loses 1-2 weeks reverse-engineering.

**Decision needed today:**
- [ ] C1 execution owner confirms rotation will happen today/tomorrow
- [ ] Priority sequence confirmed: QC first, chain:SENTRY after
- [ ] Knowledge transfer session scheduled (date + time)

---

## 2. Product Costing — Owner Assignment & Input Chain

**Context:** Every revenue projection is top-line only. No product has costing methodology, licensing terms, SKU structure, or margin calculation. VoronCitadel has 3 price points (RM 138K/168K/368K) with no documented rationale for 2.7× spread. ACT-20260811-004 (Commercialisation Readiness) is 18 days overdue.

**Discussion points:**
- Who owns the costing framework? Recommendation: Fuud owns costing methodology (engineering effort, infrastructure cost), DAF owns commercial pricing (licence terms, margin, SKU structure, packaging).
- Input owners needed:
  - Fuud: engineering effort per module, Teras cost allocation per product
  - Hadri: operational cost per deployment, service delivery model
  - DAF: pricing model, licensing terms, margin methodology, SKU structure
- First deliverable: VoronCitadel Costing Sheet (1 page) — module-level cost breakdown for GRC, DRM, ASM, TPRM. Due Sep 14.
- Licensing terms: what does a "licence" cover? Per org? Per user? Per module? Per deployment? This needs definition before CyberDSA.
- VoronCitadel price points: confirm relationship between RM 138K (existing), RM 168K (early adopter), RM 368K (retail). Is RM 138K grandfathered? Is RM 168K time-limited?

**Decision needed today:**
- [ ] Costing owner assigned (Fuud confirmed?)
- [ ] VoronCitadel Costing Sheet deadline set (Sep 14?)
- [ ] Licensing model scope defined (what needs to be answered before CyberDSA)

---

## 3. Portfolio Register — Kill Date Enforcement & Shadow Programme

**Context:** 3 of 5 programmes have passed kill dates with zero enforcement. 1 active programme is not in the register. Kill dates have never been exercised — they are currently advisory, not binding.

**Discussion points:**
- **PRG-003 (PMO AI Cohort):** Kill date Aug 25 (10 days ago). Kill criteria: "If no response by Aug 25, formally park." This is the first kill-date enforcement test. If not enforced, every future kill date is advisory.
  - Action: Update to ⛔ Parked. Log decision. Free the cognitive slot.
- **PRG-002 (CSM GTM):** Kill date Aug 22 (13 days ago). Gate: Aisha PIC + POC scope. No evidence of completion. But CSM partnership continues through other channels (Co-Design Lab, stakeholder engagement).
  - Decision: Kill or merge into CSM Joint Operating Model (INIT-20260813-005)? Either way, update register. No zombie.
- **PRG-004 (RISIK × UiTM):** Kill date Sep 3 (1 day ago). Contingency: push UiTM session to Sep 20. Not a kill — a slip. DeerFlow collection is operational; claim register and sample brief need verification.
  - Action: Update next action to "Complete Phase 0 deliverables by Sep 20 — UiTM session rescheduled."
- **PRG-001 (PERJASA Workshop):** Kill date Sep 2 (2 days ago). Workshop dates Sep 2-3. DAF was there. No execution evidence ingested.
  - Action: DAF confirms workshop status. If executed → trigger intake + 90-day continuation (COM-20260813-003). If not → update status.
- **Shadow programme:** CSM Co-Design Lab Cohort 01 (INIT-20260804-004) — 23 MyCERT personnel in active cohort. Not in Portfolio Register. Add as PRG-006.

**Decision needed today:**
- [ ] PRG-003 parked (formal kill)
- [ ] PRG-002 kill or merge decision
- [ ] PRG-004 UiTM session pushed to Sep 20
- [ ] PRG-001 workshop status confirmed
- [ ] CSM Co-Design Lab Cohort 01 added to register

---

## 4. Amelia — 77-Person High-Touch Activation

**Context:** Amelia is assigned as Strategic Stakeholder Engagement Lead. 108 stakeholder records exist. 193-org segmentation framework exists (93 A-Target, 35 B-Engage). But: no 77-person target list, no activation tracker, no evidence of outbound engagement.

**Discussion points:**
- The 77 need to be identified. Selection criteria: likely from A-Target (93 orgs) and B-Engage (35 orgs) tiers. 7 stakeholder functions per org in the CSV (CISO, Head of GRC, CFO, CRO, Head of Compliance, CIO, Head of Internal Audit).
- Existing STK records: 40 CSM stakeholders already named. But the 77 are for CyberDSA pre-engagement — primarily the 193-org RMiT financial services market, not CSM.
- Tracker needed: who's contacted, who's responded, who's confirmed, meeting status. Should live in CognitiveOS, not a separate sheet.
- CyberDSA timeline: pre-schedule meetings with A-Target orgs before Oct 10. That's 93 orgs, 5 weeks out. At ~4 meetings/week = 20 meetings in 5 weeks. Is that the target?
- Amelia's scope: outbound engagement + tracker + coordination. Does she have the authority to initiate contact directly, or does she need DAF approval per contact?

**Decision needed today:**
- [ ] 77-person target list: how selected, from which tier, by when
- [ ] Activation tracker: format, location, update cadence
- [ ] Amelia's authority scope: direct contact or DAF-approved
- [ ] Weekly meeting target for CyberDSA pre-engagement

---

## 5. MEISAC × NanoSec × Aras — Status Clarification

**Context:** MEISAC does not exist anywhere in CognitiveOS. Zero occurrences. No initiative, no stakeholder, no organisation record. NanoSec is a pentesting resource (ORG-20260904-001), not a cohort partner. No "trifecta" or "third cohort" references found.

**Discussion points:**
- What is MEISAC? If it's a real entity DAF intends to partner with, it needs a full intake event (stakeholder record, organisation record, initiative record, portfolio register entry).
- If the "third cohort" is a concept DAF is exploring but hasn't committed to, it should be tracked as a Watch List item, not left as an undefined reference.
- NanoSec is correctly scoped to pentesting (GovSec TIP B1 Security Remediation, Sep 15). Confirm this remains separate from any cohort programme.

**Decision needed today:**
- [ ] MEISAC: does it exist? If yes → intake. If no → drop from discussion.
- [ ] Third cohort: is this a real initiative or a concept? If concept → Watch List.

---

## 6. PERJASA Workshop Outcomes — Intake

**Context:** DAF was at the PERJASA AI Cohort Workshop Sep 2-3. No outcomes have been ingested into CognitiveOS. PRG-001 kill date (Sep 2) has passed with no execution evidence.

**Discussion points:**
- What happened at the workshop? Attendance, outcomes, commitments, next steps.
- Any new stakeholders to ingest? New initiatives? Follow-up commitments?
- COM-20260813-001 (expected delivery Sep 3) needs status update.
- If workshop was executed → trigger 90-day post-workshop continuation (COM-20260813-003).

**Decision needed today:**
- [ ] Workshop execution confirmed
- [ ] Intake scheduled (today? tomorrow?)
- [ ] COM-20260813-001 status updated

---

## Pre-Meeting Summary: Decisions Queue

| # | Decision | Owner | Urgency |
|---|----------|-------|---------|
| 1 | C1 credential rotation — execute today | Syahir (Hadri directs, Fuud supports) | 🔴 16 days overdue |
| 2 | Syahir priority sequence — QC first, chain:SENTRY after | DAF confirms | 🔴 This week |
| 3 | chain:SENTRY knowledge transfer — schedule date | Hadri | 🟡 This week |
| 4 | Product costing owner assigned | DAF | 🟡 By Sep 7 |
| 5 | VoronCitadel Costing Sheet deadline | Fuud (if assigned) | 🟡 Sep 14 |
| 6 | Licensing model scope for CyberDSA | DAF | 🟡 Before Oct 10 |
| 7 | PRG-003 parked | DAF | 🔴 10 days overdue |
| 8 | PRG-002 kill or merge | DAF | 🔴 13 days overdue |
| 9 | PRG-004 UiTM session pushed to Sep 20 | DAF | 🟡 1 day overdue |
| 10 | PRG-001 workshop status confirmed | DAF | 🟡 2 days overdue |
| 11 | CSM Co-Design Lab added to register | Ember (after approval) | 🟡 This week |
| 12 | 77-person target list defined | Amelia / DAF | 🟡 By Sep 14 |
| 13 | Activation tracker format decided | DAF | 🟡 By Sep 14 |
| 14 | Amelia's contact authority scope | DAF | 🟡 This week |
| 15 | MEISAC: exists or not? | DAF | 🟢 Clarify today |
| 16 | Third cohort: concept or initiative? | DAF | 🟢 Clarify today |
| 17 | PERJASA workshop intake scheduled | DAF | 🟡 Within 48h |

---

*Agenda prepared from CognitiveOS Discovery Directives A-D and Cognitive Loop INT-20260904-006. All claims T3 [ASSESSMENT], L2 evidence, confidence 7/10 (Rule 6 cap). DAF retains all decision authority.*
