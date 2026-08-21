---
id: DOC-20260821-002
record_type: document
title: "Actionable Intelligence Protocol — Wan Roshaimi Stakeholder Engagement"
created_at: 2026-08-21T06:48:00+00:00
updated_at: 2026-08-21T06:48:00+00:00
owner: faurani-jaafar
status: active
priority: critical
sensitivity: confidential
lifecycle_state: canonical
confidence: high
tags:
  - domain/stakeholder-engagement
  - domain/csm-partnership
  - domain/cyberdsa-2026
  - type/actionable-protocol
  - type/execution-protocol
  - domain/execution-management
source:
  type: synthesis
  reference: "Synthesis of DOC-20260821-001, INT-20260821-001, STK-20260812-001, DEC-20260821-006, ACT-20260819-006, DOC-20260819-001"
summary: "Execution protocol converting the Wan Roshaimi engagement strategy into actionable steps with owners, timelines, triggers, decision points, and escalation paths. Covers pre-engagement preparation, Gate 4 execution, post-meeting closure, Layer 3-5 activation triggers, and monitoring cadence."
strategic_significance: "Converts strategic one-pager into executable protocol. Every step has an owner, deadline, required input, required output, and escalation path. Eliminates ambiguity about who does what when."
mission_alignment:
  - sovereign-capability
  - csm-aras-partnership
  - cyberdsa-2026
related_records:
  - DOC-20260821-001
  - INT-20260821-001
  - STK-20260812-001
  - DEC-20260821-006
  - DEC-20260819-004
  - DOC-20260819-001
  - ACT-20260819-006
  - ACT-20260821-006
---

# Actionable Intelligence Protocol — Wan Roshaimi Stakeholder Engagement

**TLP:AMBER | Aras Integrasi × CSM | CyberDSA 2026 Activation**
**Reference:** DOC-20260821-001 (one-pager), INT-20260821-001 (5-layer objective)
**Protocol owner:** DAF
**Technical lead:** Hadri
**Protocol status:** ACTIVE — pending Gate 0 + Gates 1-2 closure

---

## Phase 0 — Pre-Engagement Preparation (Aug 21–30)

**Trigger:** Gate 0 (Roshdi) OR Gate 1 (Azrul) closes — whichever comes first
**Owner:** DAF

| Step | Action | Owner | Required Input | Required Output | Deadline |
|------|--------|-------|----------------|-----------------|----------|
| 0.1 | Prepare technical validation brief — architecture posture, integration boundaries, CyberDSA technical representation | Hadri + Fuad | Product architecture docs, GovSec TIP v3.0 specs, VoronDRQ/VoronCitadel specs, ChainSentry specs | Technical brief document (2-3 pages) | Aug 27 |
| 0.2 | Prepare co-branding proposition document — 3 products, CSM × Aras framing, what co-branding means technically | DAF | DEC-20260821-006, product naming convention, media narrative v1.1 draft | Co-branding proposition (1 page) | Aug 28 |
| 0.3 | Map existing CSM ecosystem assets — SiberSUITE architecture, CMERP, existing integrations | Hadri | INIT-20260804-003, CONV-20260810-001, DEC-20260810-001 | Ecosystem context map (1 page) | Aug 28 |
| 0.4 | Define POC success criteria for each product — what "validated" looks like technically | Fuad | Product specs, deployment model | POC success criteria sheet (1 page per product) | Aug 29 |
| 0.5 | Prepare meeting request — framing, proposed dates, agenda outline | DAF | Stakeholder brief, engagement strategy | Meeting request email/message | Aug 30 |

**Gate check before proceeding to Phase 1:**
- [ ] Gate 0 (Roshdi) closed — executive authorization confirmed
- [ ] Gate 1 (Azrul) closed — partnership narrative locked
- [ ] Gate 2 (Zulfeka) closed — commercial model agreed
- [ ] Technical brief prepared
- [ ] Co-branding proposition prepared
- [ ] POC success criteria defined

**Escalation:** If Gates 0-2 not closed by Aug 30 → DAF assesses whether to proceed with preparation only or hold engagement. Do NOT approach Wan Roshaimi without co-branding authorization (Gate 0).

---

## Phase 1 — Gate 4 Engagement (Aug 31–Sep 10)

**Trigger:** Phase 0 gate check complete
**Owner:** DAF (strategic) + Hadri (technical)
**Stakeholder:** Wan Roshaimi (STK-20260812-001)

### 1A — Meeting Setup (Aug 31–Sep 3)

| Step | Action | Owner | Output | Deadline |
|------|--------|-------|--------|----------|
| 1A.1 | Send meeting request to Wan Roshaimi — frame as technical alignment session for CSM × Aras CyberDSA collaboration | DAF | Meeting request sent | Aug 31 |
| 1A.2 | Proposed framing: "Technical alignment session to validate the CSM × Aras co-branded stack architecture and CyberDSA technical representation" | DAF | Agenda confirmed | Sep 3 |
| 1A.3 | Confirm attendees — Aras side: DAF + Hadri (mandatory), Fuad (if technical depth needed) | DAF | Attendee list confirmed | Sep 3 |
| 1A.4 | Pre-read package sent to Wan Roshaimi 48h before meeting — technical brief + co-branding proposition (not product brochures) | Hadri | Pre-read delivered | T-48h |

**Framing rule:** This is a technical alignment session, not a product pitch. The pre-read contains architecture and governance — not marketing materials.

### 1B — The Meeting (Sep 4–10, target Sep 5–7)

**Duration:** 60–90 minutes
**Aras attendees:** DAF (strategic framing + close), Hadri (technical lead)
**CSM attendee:** Wan Roshaimi (possibly with technical team members he invites)

**Agenda structure (90 min):**

| Time | Segment | Lead | Content |
|------|---------|------|---------|
| 0–10 | Opening & context | DAF | National outcome framing. Why CSM × Aras. Why now. What we're asking. |
| 10–25 | Co-branding proposition | DAF | Three products, CSM × Aras co-branding rationale, what it means, what we need from him |
| 25–55 | Technical architecture review | Hadri | GovSec TIP architecture, VoronDRQ/VoronCitadel architecture, ChainSentry architecture. Integration posture with SiberSUITE. POC success criteria. Deployment model. |
| 55–70 | Integration & governance discussion | Hadri | How capabilities fit existing CSM ecosystem. Integration boundaries. Data handling. Assurance model. Ownership. |
| 70–80 | Operationalisation pathway | DAF | Sustainable Malaysian capability. Local support. Skills transfer. Sovereign infrastructure. Scale pathway. |
| 80–90 | Close — next decision | DAF | Named next step. Owner. Due date. Written recap commitment. |

**Required outputs from meeting:**
- [ ] Technical narrative validated (or objections captured)
- [ ] Integration considerations identified (or deferred)
- [ ] Red lines / constraints surfaced
- [ ] CyberDSA technical representation agreed (or flagged for resolution)
- [ ] Named next step with owner and due date
- [ ] Meeting recap committed to writing within 24h

**Decision tree for meeting outcomes:**

| Wan Roshaimi's Response | Action | Owner |
|--------------------------|--------|-------|
| Validates fully — no objections | Proceed to Phase 2. Capture technical alignment note. Schedule Layer 3 meeting. | Hadri |
| Validates with conditions — specific concerns raised | Document conditions. Hadri addresses within 5 days. Re-confirm with Wan Roshaimi. | Hadri |
| Defers — wants more information or internal consultation | Provide requested materials within 3 days. Follow up within 7 days. | Hadri + DAF |
| Declines — does not support co-branding | ESCALATE to DAF immediately. DAF assesses with Roshdi/Azrul. Do NOT proceed with co-branding claims. | DAF |
| No response / meeting not secured | DAF escalates via Azrul (partnership pathway) or Roshdi (executive authority). | DAF |

### 1C — Post-Meeting Closure (within 24h of meeting)

| Step | Action | Owner | Output | Deadline |
|------|--------|-------|--------|----------|
| 1C.1 | Write meeting recap — decisions, action items, next steps | Hadri | Meeting recap document | 24h post-meeting |
| 1C.2 | Send recap to Wan Roshaimi for confirmation | DAF | Recap sent | 24h post-meeting |
| 1C.3 | Capture technical alignment note — architecture validated, integration boundaries, constraints | Hadri | Technical alignment note (filed in CognitiveOS) | 48h post-meeting |
| 1C.4 | Update Gate 4 status in success metrics dashboard | DAF | Dashboard updated | 48h post-meeting |
| 1C.5 | Update ACT-20260819-006 status | DAF | Action record updated | 48h post-meeting |

**Gate 4 closure criteria:**
- Technical alignment note filed
- Wan Roshaimi has confirmed recap (or 72h silent acceptance)
- No unresolved P0 technical objections
- CyberDSA technical representation agreed

---

## Phase 2 — Layer 3 Activation: Technical Partnership Architecture (Oct–Dec)

**Trigger:** Gate 4 closed + CyberDSA 2026 completed (Oct 7)
**Owner:** Hadri (technical) + DAF (strategic)
**Objective:** Position Aras as CSM's natural technical integration partner

| Step | Action | Owner | Trigger | Output |
|------|--------|-------|---------|--------|
| 2.1 | Schedule post-CyberDSA integration architecture discussion with Wan Roshaimi | DAF | Oct 7 (post-CyberDSA) | Meeting scheduled within 2 weeks |
| 2.2 | Prepare integration architecture proposal — GovSec × SiberSUITE, Score Card, CBOM — how they fit CSM's tech roadmap and CSCDC transition | Hadri + Fuad | Before meeting | Integration architecture proposal (3-5 pages) |
| 2.3 | Conduct integration architecture discussion | DAF + Hadri | Meeting date | Decisions on which tracks to activate |
| 2.4 | Activate agreed joint tracks — assign technical owners, define milestones | Hadri | Post-meeting | Track activation records (ACT records for each) |
| 2.5 | Establish quarterly architecture review cadence | DAF | Post-meeting | Recurring calendar invite + cadence SOP |

**Activation triggers for each joint track:**

| Track | Activation Condition | Owner | First Milestone |
|-------|---------------------|-------|----------------|
| GovSec × SiberSUITE | Wan Roshaimi validates integration architecture | Hadri | Consolidated requirements document (currently overdue — ACT-20260810-001) |
| Cybersecurity Score Card | Wan Roshaimi confirms CNII sector scoring priority | Joint | Scoring model design session |
| CBOM Agent | Wan Roshaimi confirms feasibility assessment direction | Joint | Feasibility report + architecture sketch |
| AI Co-Design Lab | Cohort 01 completion + Wan Roshaimi interest in deeper collaboration | Hadri | Cohort 02 scoping |

---

## Phase 3 — Layer 4 Activation: CSCDC Transition Positioning (2026–2027)

**Trigger:** CSCDC transition timeline clarifies OR Wan Roshaimi indicates readiness for infrastructure-level discussion
**Owner:** DAF (strategic) + Hadri (technical)
**Condition:** Do NOT activate until Gate 4 closed AND at least one Layer 3 track is operational

| Step | Action | Owner | Trigger | Output |
|------|--------|-------|---------|--------|
| 3.1 | Map CSCDC infrastructure procurement opportunities — RM 485K social listening, content studio, encrypted portal | DAF | CSCDC procurement timeline published | Opportunity assessment |
| 3.2 | Position Aras integration architecture as reference for CSCDC tech stack | DAF + Hadri | Post-Layer 3 activation | Reference architecture document |
| 3.3 | Engage Wan Roshaimi on CSCDC transition technology roadmap | DAF | CSCDC timeline confirmed | Strategic alignment confirmed |
| 3.4 | Identify Aras capabilities that map to CSCDC infrastructure gaps | Hadri | CSCDC gap analysis | Capability mapping document |

**Escalation gate:** Any CSCDC engagement requires DAF approval. Do not initiate without explicit strategic direction — CSCDC is a different institutional context from CSM.

---

## Monitoring & Escalation Protocol

### Weekly Status Check (DAF, every Monday)

| Check | Green | Amber | Red |
|-------|-------|-------|-----|
| Gate 0 (Roshdi) status | Authorized | In progress >7 days | No response >14 days |
| Gate 1 (Azrul) status | Closed | In progress >7 days | No response >14 days |
| Gate 2 (Zulfeka) status | Closed | In progress >7 days | No response >14 days |
| Gate 4 (Wan Roshaimi) status | Validated | Conditions raised | Declined / no response |
| Technical brief prepared | Complete | In progress | Not started |
| POC success criteria defined | Complete | In progress | Not started |

### Escalation Paths

| Situation | Escalate To | Method | Timeline |
|-----------|-----------|--------|----------|
| Wan Roshaimi declines co-branding validation | DAF → Roshdi (executive) + Azrul (partnership) | Direct conversation | Within 48h |
| Wan Roshaimi raises technical objections Aras cannot resolve | Hadri → DAF → technical escalation review | Technical review meeting | Within 5 days |
| Meeting not secured after 2 attempts | DAF → Azrul (partnership pathway) | Via Azrul's institutional channel | Within 7 days of 2nd attempt |
| Wan Roshaimi requests scope beyond Gate 4 (CSCDC, procurement) | Hadri → DAF | DAF decision | Before responding |
| CSM internal politics blocks engagement | DAF → Roshdi | Executive intervention | Case-by-case |

### Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Gate 4 closed by Sep 10 | Yes/No | Technical alignment note filed |
| Technical validation without P0 objections | Yes/No | Meeting recap |
| CyberDSA technical representation agreed | Yes/No | Meeting recap |
| Post-CyberDSA meeting scheduled within 2 weeks | Yes/No | Calendar confirmation |
| At least 1 Layer 3 track activated by Dec 31 | Yes/No | Track activation record |
| Quarterly architecture review cadence established | Yes/No | Recurring invite + SOP |

---

## Protocol Rules

1. **One stakeholder, one primary ask** — Gate 4 ask is co-branding technical validation. Do not add CSCDC, procurement, or partnership expansion asks to the first meeting.
2. **Every meeting closes with owner, due date, written recap** — no exceptions. Verbal support is not operating behaviour.
3. **Aras owns POC delivery** — Wan Roshaimi validates, he doesn't execute. Never position him as a delivery resource (DEC-20260819-004).
4. **Do not overstate alignment** — use "designed for national-grade deployment" not "nationally deployed." Use "working in partnership with CSM" not "CSM-endorsed" until formal validation closes.
5. **Technical claims must be defensible** — architecture, integration, AI capabilities. If it can't be demonstrated, don't claim it.
6. **Layer progression is conditional** — do not skip to Layer 3 until Gate 4 closes. Do not skip to Layer 4 until at least one Layer 3 track is operational.
7. **DAF owns strategic escalation** — Hadri does not escalate to CSM executives directly. Technical issues route through DAF.

---

## Document Control

| Field | Value |
|-------|-------|
| Protocol owner | DAF |
| Technical lead | Hadri |
| Created | Aug 21, 2026 |
| Status | ACTIVE — pending Gate 0 + Gates 1-2 |
| Next review | Aug 30 (pre-engagement gate check) |
| Related one-pager | DOC-20260821-001 |
| Related intelligence | INT-20260821-001 |

---

*Author: Ember | Source: DAF directives Aug 21 2026 | Classification: TLP:AMBER*
