# CSM–Aras Master Workstream Register

**Document ID:** MWR-20260813-001
**Initiative:** INIT-20260813-005
**Decision Authority:** DEC-20260813-001
**Programme Coordinator:** DAF
**Date:** 13 August 2026
**Status:** First Issue (v1.0)
**Next Review:** 17 August 2026 (weekly cadence)

---

## Governance Structure

| Role | Holder | Scope |
|------|--------|------|
| Programme Coordinator (Aras) | DAF | Strategic ownership, P2, P4, P5 |
| Technical Coordinator P1 & P3 | Hadri | Cyber Intelligence, AI Cyber R&D |
| CSM Programme Coordinator | Not yet requested | Deferred by DAF |
| Review Cadence | Weekly (Aug–Oct) | Executive review every Monday |

**CSM–Aras Relationship Stage:** Stage 5 — Joint Operating Model (Adopted 13 Aug 2026)

---

## Pillar 1 — Cyber Intelligence

**Coordinator:** Hadri
**Scope:** GovSec, SiberSUITE, CMERP, LebahNet

### P1-1: GovSec × CMERP Platform Integration (INIT-20260804-002)

| Field | Value |
|-------|-------|
| Aras Owner | Hadri (delivery), DAF (strategic) |
| CSM Owner | Fathi Kamil Bin Mohad Zainuddin (STK-004-004) |
| Status | Active — Integration Phase |
| Readiness | Integration-phase |
| Next Action | Document Aug 12/13 session outcomes; resolve outstanding technical items |
| Dependency | CSM team availability; CMERP API documentation |
| Target Outcome | GovSec ↔ CMERP platform interoperability |
| Commercial Pathway | Embedded in GovSec TIP joint product (P4) |
| Deadline | Sep 2026 (integration validation before demo prep) |
| CyberDSA Critical? | **Yes** — platform integration is prerequisite for demo |
| Key Risk | RSK-004-001 (capacity contention), RSK-004-003 (timeline) |

### P1-2: GovSec × Threat Intelligence Integration (INIT-20260804-003)

| Field | Value |
|-------|-------|
| Aras Owner | Hadri (delivery), DAF (strategic) |
| CSM Owner | Mohamad Hafiz Bin Rahman (STK-004-010) |
| Status | Active — Session conducted 10 Aug, 3 collaboration areas identified |
| Readiness | Prototype |
| Next Action | Hadri & Fuad consolidate technical follow-up (ACT-010-001) |
| Dependency | CMERP integration (P1-1) may be prerequisite for TI data routing |
| Target Outcome | TI data feeds operational in GovSec TIP |
| Commercial Pathway | Core value proposition of GovSec TIP joint product |
| Deadline | Sep 2026 (integration validation before demo prep) |
| CyberDSA Critical? | **Yes** — TI feeds are the primary differentiator for GovSec demo |
| Key Risk | RSK-004-001 (capacity), RSK-010-002 (security hardening) |
| Sub-initiatives | P1-2a Score Card (P1-3), P1-2b CBOM Agent (P1-4) |

### P1-3: Cybersecurity Score Card Framework (INIT-20260810-001)

| Field | Value |
|-------|-------|
| Aras Owner | Hadri (delivery), Fuad (technical follow-up) |
| CSM Owner | Mohamad Hafiz Bin Rahman (STK-004-010), Mohammad Zaharudin (STK-004-011) |
| Status | Active — Framed |
| Readiness | Framed |
| Next Action | Joint exploration of scoring framework (ACT-010-003); Hadri & Fuad consolidated requirements |
| Dependency | GovSec × TI Integration (P1-2) — Score Card consumes GovSec analytics |
| Target Outcome | CNII sector cybersecurity posture scoring product |
| Commercial Pathway | Subscription per CNII sector or government licensing (TBD) |
| Deadline | CyberDSA prototype: Oct 2026; Framework: post-CyberDSA |
| CyberDSA Critical? | **Yes** — demonstrable score card strengthens GovSec demo |
| Key Risk | CSM joint exploration commitment; data availability from CNII sectors |

### P1-4: CBOM Agent — AI-Enabled Cyber Component Analysis (INIT-20260810-002)

| Field | Value |
|-------|-------|
| Aras Owner | Hadri (delivery), Fuad (technical follow-up) |
| CSM Owner | Mohamad Hafiz Bin Rahman (STK-004-010), Mohammad Zaharudin (STK-004-011) |
| Status | Active — Conceptual (downgraded from Framed per Athena) |
| Readiness | Conceptual |
| Next Action | Define concrete use case before any development starts (ACT-010-004) |
| Dependency | GovSec × TI Integration (P1-2); Score Card Framework (P1-3) |
| Target Outcome | AI agent continuously analysing cyber components, feeding Score Card |
| Commercial Pathway | Premium feature tier of GovSec or standalone licensed product (TBD) |
| Deadline | CyberDSA prototype: Oct 2026 (feasibility-dependent) |
| CyberDSA Critical? | **No** — strategic amplifier, not delivery prerequisite |
| Key Risk | Feasibility uncertainty; no defined use case yet; AI model dependency |

### P1 Pipeline Summary
```
SiberSUITE → Telemetry → GovSec Analytics → CBOM Agent → Cybersecurity Score Card
   (CSM)      (P1-2)        (P1-2)          (P1-4)         (P1-3)
```

---

## Pillar 2 — Sovereign AI Platform

**Coordinator:** DAF
**Scope:** GPU, models, tokens, APIs, AI agents

### P2-1: CSM AI Instance / Token Allocation (INIT-20260813-002)

| Field | Value |
|-------|-------|
| Aras Owner | DAF (strategic), Hadri (delivery) |
| CSM Owner | Azrul Nazim Abdul Aziz (STK-013-008, strategic/mgmt); CSM technical team (STK-013-009 through 012) |
| Status | Active — CSM formally requested access (13 Aug) |
| Readiness | Framed |
| Next Action | **P0: AI Token Alignment Session (ACT-013-008, due Aug 21)** — cover Development, Integration, Governance, Metering, Productionisation |
| Dependency | Infrastructure availability (~32 nodes); governance framework undefined |
| Target Outcome | CSM building on Aras AI infrastructure → recurring PaaS relationship |
| Commercial Pathway | Wrapped by P2-2 (Sovereign AI PaaS Commercial Model) |
| Deadline | Alignment session: Aug 21; governance framework: Sep 2026 |
| CyberDSA Critical? | **Yes** — Sovereign AI PaaS demo at DIA 2026 track |
| Key Risk | No governance, metering, or billing model defined |

### P2-2: Sovereign AI PaaS Commercial Model (INIT-20260813-003)

| Field | Value |
|-------|-------|
| Aras Owner | DAF (strategic + commercial) |
| CSM Owner | Azrul Nazim Abdul Aziz (STK-013-008) |
| Status | Active — Framed |
| Readiness | Framed |
| Next Action | Validate RM688k envelope against actual cost structure; separate PaaS commercial model from individual product sales |
| Dependency | P2-1 (token allocation) — the infrastructure this model wraps |
| Target Outcome | Recurring PaaS revenue relationship (infrastructure access + platform management fees) |
| Commercial Pathway | 4-layer: Infrastructure → AI Platform → Managed Services → Applications |
| Deadline | Commercial model draft: Sep 2026; CyberDSA-ready: Oct 2026 |
| CyberDSA Critical? | **Yes** — commercial proposition for CyberDSA B2B and VIP delegation |
| Key Risk | RM688k not validated; PaaS model not yet separated from product sales thinking |

---

## Pillar 3 — AI Cyber R&D

**Coordinator:** Hadri
**Scope:** UPM, Purple Teaming, AI security research

### P3-1: UPM × CSM × Aras Autonomous AI Cybersecurity / Purple Teaming (INIT-20260813-004)

| Field | Value |
|-------|-------|
| Aras Owner | DAF (strategic), Hadri (delivery) |
| CSM Owner | CSM technical team (STK-013-009 through 012) |
| UPM Owner | **Not yet identified** — no STK records in CognitiveOS |
| Status | Active — Conceptual |
| Readiness | Conceptual |
| Next Action | **P1: Obtain UPM validation data (ACT-013-011, due Aug 31)** — architecture, models, capabilities, deployment, maturity, use cases, security controls, infrastructure |
| Dependency | P2-1 (compute infrastructure for UPM experimentation); NACSA/MKN engagement for national-grade positioning |
| Target Outcome | National-grade / Mythos-class AI cybersecurity capability (tripartite) |
| Commercial Pathway | TBD — dependent on validation outcome and NACSA/MKN consideration |
| Deadline | UPM validation: Aug 31; NACSA/MKN engagement: TBD |
| CyberDSA Critical? | **No** — but connects to MIESAC and Siber Siaga tracks if positioned in time |
| Key Risk | Zero execution traction; UPM personnel unknown; no validation data received |
| Decision Needed | Does P3 get active investment now, or defer to post-CyberDSA? |

---

## Pillar 4 — Product & GTM

**Coordinator:** DAF
**Scope:** VoronCitadel, GovSec, chain:SENTRY, 193-account campaign

### P4-1: VoronCitadel Joint GTM Activation (INIT-20260804-001)

| Field | Value |
|-------|-------|
| Aras Owner | DAF (strategic); Kenny Kok (sales authority, STK-008-001); Shuhada (account coordination, STK-008-003) |
| CSM Owner | Mohammad Fahdzli bin Abdul Rauf (STK-004-001); Zulfeka Zainal Abidin (STK-004-002) |
| Status | Active — Execution (sales kit + database complete; alignment secured Aug 11) |
| Readiness | Execution |
| Next Action | **Aug 14: CSM VoronCitadel technical training (confirmed)**; then first-wave account shortlisting (ACT-011-008); stakeholder verification (ACT-011-009) |
| Dependency | CSM training completion; Kenny/Shuhada sales engagement; Azza campaign messaging (ACT-008-002) |
| Target Outcome | 5–6 discovery/demo sessions; 2–3 qualified POC candidates from 10–15 priority accounts |
| Commercial Pathway | 7-stage pipeline: Account Validation → Stakeholder Verification → Qualification → Discovery → Demo → POC → Commercial Conversion |
| Deadline | Ongoing — first-wave engagement Sep 2026; CyberDSA as pipeline acceleration event |
| CyberDSA Critical? | **Yes** — VoronCitadel is most commercially mature product; CyberDSA generates leads |
| Key Risk | RSK-013-002 (GTM programme management gap — no MQL pipeline mechanism) |
| Pending Actions | 13 actions pending (ACT-004-003 through ACT-011-013) |

### P4-2: GovSec CyberDSA Product Launch Readiness (INIT-20260810-003)

| Field | Value |
|-------|-------|
| Aras Owner | DAF (strategic); Hadri (lead architect); Fuad (current technical owner); Hadi (incoming PM, unconfirmed) |
| CSM Owner | Institutional — CSM (STK-025-008); operational owners distributed across integration tracks |
| Status | Active — Prototype → Demo-ready (target) |
| Readiness | Prototype |
| Next Action | Fuad: compile technical documentation + changelog (ACT-010-005); Hadri: produce CyberDSA launch checklist (ACT-010-006); structure readiness plan around 5 priorities (ACT-010-007) |
| Dependency | Hadi onboarding (RSK-010-001); CSM integration tracks (P1-1, P1-2); security hardening (RSK-010-002) |
| Target Outcome | Demo-ready GovSec TIP v3.0 at CyberDSA 5–7 Oct 2026 |
| Commercial Pathway | Joint CSM-Aras product launch; CyberDSA as market entry event |
| Deadline | **5 October 2026** (CyberDSA Day 1) |
| CyberDSA Critical? | **Critical — this IS the CyberDSA launch initiative** |
| Key Risks | RSK-010-001 (Hadi), RSK-010-002 (security), RSK-010-003 (commercial readiness), RSK-004-003 (timeline) |
| 5 Priorities | Stabilise → Close gaps → Validate → Handover → Demo prep |

### P4-3: Flagship Product Consolidation & Productisation (INIT-20260811-001)

| Field | Value |
|-------|-------|
| Aras Owner | DAF (strategic, governance); Fuad (delivery, documentation); Hadri (technical oversight) |
| CSM Owner | N/A (Aras-internal productisation; CSM benefits through joint products) |
| Status | Active — Concept (just initiated) |
| Readiness | Concept |
| Next Action | Fuad: establish centralised product repository (ACT-011-001); compile roadmaps (ACT-011-002), backlogs (ACT-011-003), commercial readiness (ACT-011-004), sales materials (ACT-011-005), governance (ACT-011-006) |
| Dependency | Fuad capacity (concurrent with P4-2 documentation); Hadri availability (oversight) |
| Target Outcome | 3 products × 6 documentation categories = 18 deliverables → commercial-ready |
| Commercial Pathway | Products become sellable: VoronCitadel (Ready), GovSec (Partial→Ready), chain:SENTRY (Partial→Ready) |
| Deadline | CyberDSA-ready docs: Sep 2026; full productisation: Oct 2026 |
| CyberDSA Critical? | **Yes** — sales/GTM materials needed for CyberDSA engagement |
| Key Risk | RSK-011-001 (productisation effort vs CyberDSA delivery capacity contention) |
| Products | VoronCitadel (Ready), GovSec TIP (Partial), chain:SENTRY (Partial) |
| Pending Actions | 7 actions pending (ACT-011-001 through ACT-011-007), all owned by Fuad |

---

## Pillar 5 — Capability Development

**Coordinator:** DAF
**Scope:** Training, technical enablement, co-development

### P5-1: CSM VoronCitadel Technical Training

| Field | Value |
|-------|-------|
| Aras Owner | DAF |
| CSM Owner | Mohammad Fahdzli bin Abdul Rauf (STK-004-001) |
| Status | **Confirmed — Aug 14, 2026** |
| Readiness | Scheduled |
| Next Action | Conduct training; assess CSM capability gaps post-training |
| Dependency | None — confirmed and scheduled |
| Target Outcome | CSM team enabled to demonstrate and support VoronCitadel independently |
| Commercial Pathway | Enables CSM to co-sell VoronCitadel (feeds P4-1 GTM) |
| Deadline | Aug 14, 2026 (tomorrow) |
| CyberDSA Critical? | **Yes** — CSM must be able to demonstrate product at CyberDSA |

### P5-2: AI Systems Co-Design Lab — CSM/MyCERT Cohort 01 (INIT-20260804-004)

| Field | Value |
|-------|-------|
| Aras Owner | DAF (strategic), Hadri (delivery) |
| CSM Owner | Fathi Kamil Bin Mohad Zainuddin (STK-004-004); Wan Roshaimi (STK-012-001) |
| Status | Active — CSM/MyCERT accepted (DEC-012-001); 23 personnel submitted |
| Readiness | Prototype |
| Next Action | Hadri review personnel list + confirm onboarding (ACT-012-001); process onboarding (ACT-012-002); DAF strategic assessment of MyCERT GenAI work (ACT-012-003, due Aug 17) |
| Dependency | GPU compute capacity; Hadri availability for onboarding |
| Target Outcome | MyCERT team actively using Aras AI platform for GenAI cybersecurity product development |
| Commercial Pathway | Recurring compute usage → PaaS relationship (feeds P2-2) |
| Deadline | Onboarding: Aug 2026; first prototypes: Sep 2026; CyberDSA demo potential: Oct 2026 |
| CyberDSA Critical? | **No** — strategic amplifier, not prerequisite |
| Key Risk | 23 personnel is larger than expected — compute capacity and onboarding bandwidth |

### P5-3: PERJASA Government AI Co-Design Lab (INIT-20260813-001)

| Field | Value |
|-------|-------|
| Aras Owner | DAF (strategic); Hadri (delivery) |
| PERJASA Owner | PERJASA Chairman (STK-013-005) |
| Status | Active — Workshop dates confirmed Sep 2–3; full 5-stage cohort programme designed |
| Readiness | Framed → Prototype (workshop agenda + cohort overview complete) |
| Next Action | DAF to confirm Sep 2–3; coordinate logistics; submit PERJASA governing body for approval |
| Dependency | PERJASA governing body approval; venue; participants (24–32) |
| Target Outcome | 5-stage cohort: AI Awareness → Design Thinking → AI Sandbox → Executive Demo Day → Alumni Network |
| Commercial Pathway | PERJASA as governance partner → government AI adoption pipeline → Sovereign AI PaaS customers |
| Deadline | Workshop: Sep 2–3; Executive Demo Day: TBD; 90-day pilot: Dec 2026 |
| CyberDSA Critical? | **No** — separate track but demonstrates Aras AI platform capability |
| Key Risk | RSK-013-001 (PERJASA workshop date confirmation delay) |

---

## Cross-Cutting Governance Layer

| Element | Status | Owner | Next Action |
|---------|--------|-------|-------------|
| CSM Programme Owner | **Not requested** | DAF to decide when | Deferred |
| Aras Programme Owner | ✅ DAF (Programme Coordinator) | DAF | Active |
| Workstream Leads | ✅ Assigned (Hadri: P1+P3, DAF: P2+P4+P5) | DAF | Active |
| Integrated Delivery Calendar | **Does not exist** | DAF | ACT-004-012 (overdue) — consolidate all CSM engagement dates |
| Action Register | ✅ CognitiveOS (this register + action-index) | DAF | Active |
| Product Ownership | Partial (Fuad/GovSec, DAF/VoronCitadel) | DAF | chain:SENTRY owner TBD; full governance in P4-3 |
| IP Framework | **Not defined** | DAF | Required before commercial engagement |
| Commercial Model | PaaS (P2-2) + product sales (P4-1) + GTM revenue | DAF | RSK-010-003 — no pricing/packaging yet |
| MQL Pipeline | **Does not exist** | DAF | RSK-013-002 — ACT-013-010 (P0, Aug 21) |
| POC Governance | **Not defined** | DAF | Standard POC process + success criteria needed |
| Monthly Executive Steering | **Not established** | DAF | Requires CSM counterpart first |

---

## Active Risk Summary (Pillar-Mapped)

| Risk ID | Risk | Pillar | Severity | Status | Mitigation |
|---------|------|--------|----------|--------|------------|
| RSK-010-001 | Hadi onboarding delay | P4 | Critical | Active | Hadri absorbs technical; start date unconfirmed |
| RSK-010-002 | GovSec security hardening gap | P1, P4 | Critical | Active | No assessment scheduled |
| RSK-010-003 | CyberDSA commercial readiness gap | P4 | High | Active | No pricing/packaging/conversion path |
| RSK-011-001 | Productisation vs delivery capacity | P4 | High | Active | 18 deliverables, limited resources |
| RSK-013-002 | GTM programme management gap | P4 | High | Active | No MQL pipeline mechanism |
| RSK-013-001 | PERJASA workshop delay | P5 | High | Active | Date confirmation pending |
| RSK-004-001 | Delivery capacity contention (4 CSM tracks) | P1, P5 | High | Mitigating | Dev freeze + Hadri absorption |
| RSK-004-003 | CyberDSA delivery timeline | P1, P4 | High | Mitigating | Dev freeze + 5-priority framework |

---

## P0 Actions (Due Aug 21)

| Action ID | Title | Owner | Pillar |
|-----------|-------|-------|--------|
| ACT-013-008 | AI Token Alignment Session | DAF | P2 |
| ACT-013-010 | GTM Programme Management Mechanism | DAF | P4 |
| ACT-013-012 | Master Workstream Register (THIS DOCUMENT) | DAF | Governance |

## P1 Actions (Due Aug 24–31)

| Action ID | Title | Owner | Pillar | Deadline |
|-----------|-------|-------|--------|----------|
| ACT-013-009 | Technical Integration Blueprint | Hadri | P1 | Aug 24 |
| ACT-013-011 | UPM Validation Data | Hadri | P3 | Aug 31 |
| ACT-012-003 | DAF Strategic Assessment of MyCERT GenAI | DAF | P5 | Aug 17 |

## Key Pending Actions (CyberDSA-Path)

| Action ID | Title | Owner | Pillar | Status |
|-----------|-------|-------|--------|--------|
| ACT-010-005 | Technical documentation + changelog for Hadri handover | Fuad | P4 | Pending |
| ACT-010-006 | CyberDSA Product Launch Checklist | Hadri | P4 | Pending |
| ACT-010-007 | GovSec readiness plan (5 priorities) | DAF/Fuad | P4 | Pending |
| ACT-011-001–007 | Productisation programme (7 actions) | Fuad/DAF | P4 | All pending |
| ACT-004-003 | First-wave account shortlisting (10–15 orgs) | DAF | P4 | Pending |
| ACT-008-002 | Campaign messaging guidance | Azza | P4 | Pending |

---

## CyberDSA 2026 Programme-Track Coverage Map

| Programme | Date | Aras Lead | CSM Counterpart | Pillar Focus |
|-----------|------|-----------|-----------------|-------------|
| Exhibition & Tech Showcase | All 3 days | Fuad / Farul | CSM technical team | P4 (GovSec, VoronCitadel demo) |
| DIA 2026 (AI/Tech Showcase) | All 3 days | Farul | CSM AI team (STK-013-009–012) | P2 (Sovereign AI PaaS demo) |
| Foreign VIP Delegation | All 3 days | DAF | CSM + DCED co-organised | P4 (strategic relationships) |
| ACDN Meeting | TBC | DAF | CSM institutional | P4 (ASEAN networks) |
| MIESAC | TBC | Hadri | CSM technical | P1, P3 (military/intel track) |
| Siber Siaga 2026 | TBC | Hadri | CSM technical | P1, P3 (ATM/DCED "Hyper War") |
| Flash Talk Zone | TBC | Azza / Shuhada | CSM commercial | P4 (product pitch) |
| B2B Networking | TBC | Azza / Shuhada / Kenny | Zulfelka (CSM) | P4 (commercial pipeline) |
| Conference & Forum | TBC | Kenny | CSM senior | P4 (thought leadership) |
| CyberDSA Dinner | TBC | Kenny / DAF | CSM senior | P4 (relationship) |

**Gap:** Commercial & Activation layer (INIT-013-006 four-layer coverage) has no Aras-side owner — Zulfelka is CSM, not Aras. **Needs resolution.**

---

## Commercial Pathway Summary

| Revenue Stream | Product/Vehicle | Pillar | Maturity | CyberDSA-Ready? |
|----------------|-----------------|--------|----------|-----------------|
| Product sale | VoronCitadel | P4 | Ready | ✅ Yes |
| Product sale | GovSec TIP | P4 | Partial | 🟡 Demo-ready (target) |
| Product sale | chain:SENTRY | P4 | Partial | 🟡 Unknown |
| PaaS recurring | Sovereign AI PaaS (RM688k/yr) | P2 | Framed | 🟡 Proposition only |
| Training/enablement | Co-Design Lab cohorts | P5 | Prototype | ❌ Not CyberDSA-focused |
| GTM pipeline | 193-account campaign | P4 | Execution | ✅ Active |

**Critical gap:** RSK-010-003 — no commercial model (pricing, packaging, post-demo conversion path) defined for CyberDSA. Leads generated at event with no mechanism to convert = technical success but commercial failure.

---

## Decision Register (Pillar-Impacting)

| Decision ID | Decision | Date | Impact |
|-------------|----------|------|--------|
| DEC-004-001 | Internal mobilisation — CyberDSA as firm delivery target | Aug 4 | All pillars |
| DEC-010-002 | GovSec development freeze | Aug 10 | P1, P4 |
| DEC-011-001 | Expanded dev freeze + productisation directive | Aug 11 | P4 |
| DEC-012-001 | CSM/MyCERT accepts Co-Design Lab Cohort 01 | Aug 12 | P5 |
| DEC-013-001 | Formal adoption of 5-pillar Joint Operating Model | Aug 13 | All pillars |

---

## Stakeholder Coverage Summary (per INIT-013-006)

| CSM Priority Stakeholder | Executive Coverage | Programme Coverage | Technical Coverage | Commercial Coverage |
|-------------------------|-------------------|-------------------|-------------------|-------------------|
| Mohammad Fahdzli | DAF | Hadri | Fuad | DAF |
| Azrul Nazim | DAF | Hadri | — | DAF |
| Mohammad Zaharudin | DAF | Hadri | Fuad | — |
| Mohamad Hafiz | DAF | Hadri | Fuad | — |
| Mohamad Iqbal | DAF | — | Fuad/Farul | — |
| Muhammad Amirul | DAF | — | Fuad/Farul | — |
| Nurshahira | DAF | — | Fuad/Farul | — |
| Nazri Zamani | DAF | Hadri | — | — |
| Suraya Hani | DAF | — | Fuad/Farul | — |
| Siti Aishah | DAF | — | Fuad/Farul | — |
| Zulfelka (CSM Head of Commercial) | DAF/Kenny | — | — | **GAP — no Aras-side owner** |

---

*This is the first issue of the CSM–Aras Master Workstream Register. It serves as the single programme view for all CSM–Aras collaborative work under the Joint Operating Model. Updates weekly.*

**Next Review:** 17 August 2026
**Owner:** DAF (Programme Coordinator)
**Decision Authority:** DEC-20260813-001
