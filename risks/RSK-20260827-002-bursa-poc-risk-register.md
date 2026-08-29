---
id: RSK-20260827-002
record_type: risk
title: "Bursa POC Risk Register — VoronCitadel × Bursa Malaysia"
created_at: 2026-08-27T09:23:00+00:00
updated_at: 2026-08-27T09:23:00+00:00
owner: faurani-jaafar
risk_category: delivery-capacity
probability: medium
impact: high
status: active
priority: high
sensitivity: confidential
lifecycle_state: canonical
confidence: high
tags:
  - domain/cybersecurity-productisation
  - domain/commercial-development
  - domain/csm-partnership
  - domain/compliance
  - product/voroncitadel
  - sector/financial
  - type/risk-register
source:
  type: synthesis
  reference: "INT-20260821-002, RSK-20260820-008, RSK-20260827-001, ACT-20260827-002, INIT-20260824-001, DOC-20260827-001 (RSWG), DEC-20260827-001"
summary: "Dedicated risk register for the VoronCitadel × Bursa Malaysia POC. Covers strategic, operational, technical, commercial, and compliance risks specific to the Bursa engagement. Synthesizes existing risk records and identifies POC-specific risks not yet tracked."
strategic_significance: "Bursa POC is the gating factor for first-mover advantage in the 30-broker RSWG compliance pipeline. POC success or failure determines reference case establishment and competitive positioning."
mission_alignment:
  - cybersecurity-productisation
  - commercial-growth
  - csm-partnership
related_records:
  - INT-20260821-002
  - RSK-20260820-008
  - RSK-20260827-001
  - ACT-20260827-001
  - ACT-20260827-002
  - INIT-20260824-001
  - DOC-20260827-001
  - DEC-20260827-001
---

# Bursa POC Risk Register
## VoronCitadel × Bursa Malaysia

**Classification:** TLP:AMBER — Confidential  
**Version:** 1.0  
**Created:** 2026-08-27  
**Owner:** DAF  
**Review Cadence:** Weekly until POC completion, then bi-weekly

---

## Scoring Methodology

- **Likelihood:** 1 (Rare) → 5 (Almost Certain)
- **Impact:** 1 (Negligible) → 5 (Catastrophic)
- **Score:** L × I (1–25)
- **Level:** Low (1–6) | Medium (7–12) | High (13–18) | Critical (19–25)

---

## 1. Strategic Risks

### B-STR-01: RSWG Compliance Window — Competitive First-Mover Loss
**Score:** 12 (L3 × I4) | **Level:** HIGH

| Field | Value |
|-------|-------|
| **Source** | RSK-20260827-001 |
| **Description** | RSWG Dec 31, 2026 compliance deadline creates a finite window. Brokers evaluating solutions NOW. If POC delays beyond Q4 2026, competitors (ServiceNow, OneTrust, established GRC vendors) capture the 30-broker pipeline before VoronCitadel has a reference case. |
| **Mitigation** | 1. Accelerate POC with RSWG-aligned use cases (§2.6 TPRM, §2.7 Incident Management, §2.1 Access Controls). 2. Complete RSWG→VoronCitadel capability mapping (ACT-20260827-001, due Aug 29). 3. Update POC doc with explicit RSWG alignment (ACT-20260827-002, due Aug 30). 4. Engage CSM on competitive intelligence. 5. Parallel pipeline: begin Group 2 broker awareness before POC completes. |
| **Trigger** | POC slips beyond Q4 2026; competitor visible at any Bursa broker; brokers announce vendor selections without VoronCitadel evaluation. |
| **Owner** | DAF |

### B-STR-02: POC Fails to Convert to Commercial Contract
**Score:** 9 (L3 × I3) | **Level:** MEDIUM

| Field | Value |
|-------|-------|
| **Description** | POC completes but does not result in a commercial engagement. Bursa may treat POC as a learning exercise without procurement intent. |
| **Mitigation** | 1. Clear success criteria and acceptance framework (POC Section 4). 2. Post-POC pathway with pricing model defined (Section 8: Retail RM368k, early-adopter RM168k). 3. Executive sponsorship from CSM channel (Azrul). 4. RSWG compliance urgency as conversion driver — POC demonstrates ITSS §10 compliance. |
| **Trigger** | Bursa declines commercial discussion after POC; POC success criteria met but no procurement action; Bursa requests "more time to evaluate." |
| **Owner** | DAF |

### B-STR-03: Bursa Treats POC as Proof-of-Concept Only, Not Procurement Path
**Score:** 10 (L4 × I3) | **Level:** MEDIUM-HIGH

| Field | Value |
|-------|-------|
| **Description** | Bursa's internal culture may frame POC as experimental/educational, not as a procurement precursor. Without explicit POC→pilot→production pathway acknowledged by Bursa, the POC becomes a dead-end demonstration. |
| **Mitigation** | 1. Post-POC pathway section must reference Bursa's own procurement cycle. 2. CSM channel to pre-position commercial framing with Bursa stakeholders before POC starts. 3. POC document language: "evaluation" not "demonstration" — frames the engagement as procurement evaluation, not a science project. 4. Success criteria must include a binary "proceed to pilot" decision gate. |
| **Trigger** | Bursa schedules POC with no follow-up commitment; Bursa frames POC as "exploratory" in internal communications; no named Bursa commercial owner for POC. |
| **Owner** | DAF |

---

## 2. Operational Risks

### B-OPS-01: CSM 7-Stakeholder Chain Bottleneck
**Score:** 12 (L4 × I3) | **Level:** HIGH

| Field | Value |
|-------|-------|
| **Source** | MEMORY.md — Gate structure |
| **Description** | 7-stakeholder chain: Roshdi → Azrul → Zulfeka → Bala → Wan Roshaimi → Zaharudin → Dr. Megat. Each gate is a potential bottleneck. Gate 0 (Roshdi executive authorization) is the top risk — 4th cycle flagging as UNVERIFIED. |
| **Mitigation** | 1. Gate 0 and Gates 3-5 run in parallel (corrected understanding, Aug 27). 2. DAF owns Gates 3-5 stakeholder coordination. 3. Weekly gate status tracking. 4. Escalation protocol if any gate stalls >5 business days. |
| **Trigger** | Any gate stalls >5 business days; Roshdi declines or delays Gate 0; CSM internal coordination breaks down. |
| **Owner** | DAF |

### B-OPS-02: Resource Contention — DAF as Single Coordinator
**Score:** 12 (L4 × I3) | **Level:** HIGH

| Field | Value |
|-------|-------|
| **Source** | RSK-20260820-008 (convergence risk pattern) |
| **Description** | DAF is the single coordinator across Bursa POC, CyberDSA, RISIK, PERJASA, and CSM gates. No PM hired (TBH-001). No HoE (RSK-20260820-003). Every track depends on DAF's direct involvement. |
| **Mitigation** | 1. TBH-001 PM hire remains critical (JD drafted). 2. Amelia as SSE Lead can absorb CyberDSA-specific stakeholder activation. 3. Fuad owns technical validation — delegate explicitly. 4. Hadri owns Teras deployment model validation. 5. DAF protects focused strategy time (90-day agenda item 10). |
| **Trigger** | DAF capacity <20% for Bursa POC in any given week; simultaneous gate deadlines across workstreams; quality degradation under concurrent pressure. |
| **Owner** | DAF |

### B-OPS-03: POC Timeline Slippage Beyond Q4 2026
**Score:** 10 (L3 × I4) | **Level:** MEDIUM-HIGH

| Field | Value |
|-------|-------|
| **Description** | No POC date is set yet. POC document is still being updated (ACT-20260827-002 due Aug 30). RSWG capability mapping (ACT-20260827-001) due Aug 29. If document finalization slips, POC scheduling slips, and the Q4 2026 window narrows. |
| **Mitigation** | 1. Hard deadline: POC document finalized by Sep 5 (after Aug 30 RSWG update + Fuad validation). 2. POC scheduling target: Sep 15–30 execution window. 3. Weekly timeline tracking. 4. If Fuad validation reveals capability gaps, scope-down rather than delay. |
| **Trigger** | POC document not finalized by Sep 5; Fuad validation reveals material gaps; no POC date set by Sep 15. |
| **Owner** | DAF |

### B-OPS-04: RACI Ambiguity — 3-Party Engagement
**Score:** 8 (L3 × I3) | **Level:** MEDIUM

| Field | Value |
|-------|-------|
| **Description** | 3-party RACI (Aras × CSM × Bursa) exists but needs revision, not recreation. Roles between CSM (channel) and Aras (delivery) may blur during POC execution. Amelia's CyberDSA activation role is distinct from POC execution. |
| **Mitigation** | 1. RACI revision as part of POC document finalization (Section 6). 2. CSM explicitly framed as channel + credibility, not delivery layer. 3. Named roles (not "Team") in RACI. 4. Amelia's role scoped to CyberDSA stakeholder activation only. |
| **Trigger** | CSM attempts to own delivery decisions; Aras and CSM give Bursa conflicting information; role confusion during POC execution. |
| **Owner** | DAF |

---

## 3. Technical Risks

### B-TEC-01: CRITICAL Test Case Gaps — AI-01/AI-02 (RAG Phase 2) + DRM-01
**Score:** 12 (L3 × I4) | **Level:** HIGH

| Field | Value |
|-------|-------|
| **Source** | INT-20260821-002 — 17/22 test cases confirmed |
| **Description** | 2 CRITICAL test cases unconfirmed: AI-01/AI-02 (RAG Phase 2 — requires capabilities not in Phase 1) and DRM-01 (manual vs automated — process question, not technical). If these remain unaddressed, POC success criteria cannot be fully met. |
| **Mitigation** | 1. Scope AI-01/AI-02 explicitly OUT of Phase 1 POC — document as Phase 2 roadmap items. 2. For DRM-01: document the manual workflow and automate in Phase 2. 3. POC document must clearly state Phase 1 vs Phase 2 boundary (per Fuad validation requirement). 4. If Bursa requires AI-01/AI-02 in POC, flag timeline impact immediately. |
| **Trigger** | Bursa insists on AI-01/AI-02 in POC scope; Fuad confirms RAG Phase 2 is not production-ready; DRM-01 resolution requires Bursa process change. |
| **Owner** | Fuad (technical validation) → DAF (scope decision) |

### B-TEC-02: Product Capability Claims — Accuracy Risk
**Score:** 10 (L4 × I3) | **Level:** MEDIUM-HIGH

| Field | Value |
|-------|-------|
| **Source** | INT-20260821-002 — Fuad validation gate |
| **Description** | POC document contains product capability claims. A single false claim (feature that doesn't exist in production, or is only in Phase 2) destroys credibility with Bursa's technical stakeholders. 5 compliance frameworks including Bursa Cybersecurity Controls (61 requirements) are claimed as loaded in production. |
| **Mitigation** | 1. Fuad validates EVERY capability claim against MVP Product Specification v2.0. 2. Claims trace to `products/voroncitadel/MVP_SPECIFICATION.md` as authoritative reference. 3. Phase 2 features explicitly marked. 4. "Built for you" evidence (61 Bursa Cybersecurity Controls) must be demonstrable live, not just listed. |
| **Trigger** | Fuad identifies a claim not supported by production; Bursa technical team challenges a capability during POC and Aras cannot demonstrate; 61 controls mapping found inaccurate. |
| **Owner** | Fuad |

### B-TEC-03: Teras-VoronCitadel Deployment Model Not Validated
**Score:** 10 (L3 × I4) | **Level:** MEDIUM-HIGH

| Field | Value |
|-------|-------|
| **Source** | INT-20260821-002 — DEC-20260820-008/009 |
| **Description** | POC positions VoronCitadel deploying ON Teras (sovereign infrastructure, no foreign endpoints, air-gapped capability). This is a major differentiator for a stock exchange. But Teras-VoronCitadel integration must be validated as real, not aspirational. Bursa infra team will scrutinize deployment architecture. |
| **Mitigation** | 1. Fuad validates Teras-VoronCitadel deployment model (INT-20260821-002 validation item). 2. Hadri confirms Teras architecture (DEC-20260820-008/009). 3. POC document includes deployment architecture diagram, not just narrative. 4. If Teras integration is not yet live, scope POC deployment on dedicated infrastructure with Teras as the production target. |
| **Trigger** | Fuad/Hadri cannot confirm Teras-VoronCitadel integration is functional; Bursa infra team questions deployment architecture; Teras readiness not sufficient for POC timeline. |
| **Owner** | Fuad + Hadri |

### B-TEC-04: VoronScout Scan Against Bursa External Footprint
**Score:** 8 (L3 × I3) | **Level:** MEDIUM

| Field | Value |
|-------|-------|
| **Source** | INT-20260821-002 — Section 5 testing plan |
| **Description** | POC testing plan includes live VoronScout scan of Bursa's external footprint as the compelling visual. If VoronScout cannot scan Bursa's environment (security restrictions, WAF, IP blocking), the most compelling POC element fails. |
| **Mitigation** | 1. Pre-POC: test VoronScout against Bursa's known external assets (with authorization). 2. Have simulated/sanitized Bursa-equivalent data as fallback. 3. If scan restricted, demonstrate against a comparable NCII environment. 4. Clear scope: what is scanned, what is not, authorization requirements. |
| **Trigger** | VoronScout blocked by Bursa security controls; Bursa declines external scan authorization; scan results show no meaningful findings (undermines value proposition). |
| **Owner** | Fuad |

### B-TEC-05: Bursa Cybersecurity Controls Mapping Accuracy
**Score:** 9 (L3 × I3) | **Level:** MEDIUM

| Field | Value |
|-------|-------|
| **Description** | 61 Bursa Cybersecurity Controls are claimed as loaded in the production platform. This is the strongest "built for you" evidence point. If the mapping is inaccurate (controls are generic, not Bursa-specific, or mapping is superficial), the differentiation claim collapses. |
| **Mitigation** | 1. Fuad validates: are the 61 controls genuinely Bursa Cybersecurity Controls (not generic ISO/CSF mapped to Bursa)? 2. Demonstrable: can the platform show a control → evidence → Bursa requirement trace? 3. POC demo includes live control mapping walkthrough. |
| **Trigger** | Controls found to be generic re-badged; mapping is superficial (control exists but evidence chain is weak); Bursa team identifies controls not covered. |
| **Owner** | Fuad |

---

## 4. Commercial Risks

### B-COM-01: Pricing Misalignment with Bursa Expectations
**Score:** 8 (L3 × I3) | **Level:** MEDIUM

| Field | Value |
|-------|-------|
| **Source** | MEMORY.md — VoronCitadel pricing |
| **Description** | Retail RM368k, early-adopter RM168k. Bursa as a stock exchange may have different budget expectations — either much higher (enterprise scale) or much lower (comparing to commodity GRC tools). Misalignment on either end kills commercial conversion. |
| **Mitigation** | 1. Post-POC pathway section includes tiered pricing (per-broker vs exchange-level). 2. Early-adopter pricing positioned as founding-customer privilege. 3. CSM channel tests pricing perception with Bursa stakeholders. 4. RSWG compliance cost context: cost of non-compliance >> cost of VoronCitadel. |
| **Trigger** | Bursa balks at pricing; Bursa compares to commodity GRC tools; Bursa expects free POC → free pilot → free production (loss-leader trap). |
| **Owner** | DAF |

### B-COM-02: CSM Channel Dependency — Azrul Engagement Level
**Score:** 9 (L3 × I3) | **Level:** MEDIUM

| Field | Value |
|-------|-------|
| **Description** | Bursa POC comes through CSM channel, not direct outreach. Azrul's level of engagement with Bursa stakeholders determines whether the POC document reaches the right technical audience. If Azrul deprioritizes Bursa relative to other CSM priorities, the POC stalls at the channel level. |
| **Mitigation** | 1. DAF maintains direct relationship with Bursa technical stakeholders (not fully CSM-dependent). 2. POC document engineered as self-sufficient — works even if Azrul's briefing is brief. 3. Regular CSM coordination check-ins. 4. Gate status tracking includes CSM engagement level. |
| **Trigger** | Azrul postpones Bursa briefing; CSM channel goes quiet for >1 week; Azrul assigns Bursa to a junior CSM staff member. |
| **Owner** | DAF |

### B-COM-03: 30-Broker Pipeline — Parallel Pipeline Risk
**Score:** 8 (L3 × I3) | **Level:** MEDIUM

| Field | Value |
|-------|-------|
| **Source** | RSK-20260827-001 mitigation |
| **Description** | Waiting for Bursa POC to complete before approaching other brokers serializes the pipeline. With RSWG Dec 31 deadline, brokers may select alternatives while waiting for Bursa reference case. |
| **Mitigation** | 1. Group 2 broker awareness campaign starts before Bursa POC completes. 2. RSWG compliance positioning (not Bursa-case-dependent) as the primary pitch. 3. Bursa POC = reference validation, not pipeline gate. 4. CSM channel for parallel broker engagement. |
| **Trigger** | Bursa POC takes >6 weeks; competitor approaches Group 2 brokers; brokers ask for reference case and none exists. |
| **Owner** | DAF |

---

## 5. Compliance & Regulatory Risks

### B-REG-01: RSWG → VoronCitadel Capability Mapping Gap
**Score:** 10 (L4 × I3) | **Level:** MEDIUM-HIGH

| Field | Value |
|-------|-------|
| **Source** | ACT-20260827-001 (due Aug 29) |
| **Description** | RSWG Recommendation Paper contains 9 control domains, 30 broker classifications. ACT-20260827-001 (capability mapping) due Aug 29 has not been completed. If VoronCitadel covers <70% of RSWG control domains natively, the "RSWG-ready" positioning is weakened. |
| **Mitigation** | 1. Complete ACT-20260827-001 by Aug 29. 2. Map gaps explicitly — identify what VoronCitadel covers natively vs what requires customization vs what is out of scope. 3. Position as "ITSS §10 compliance today + RSWG §2.6 readiness tomorrow" (DEC-20260827-001) — does not require 100% RSWG coverage. 4. Gap areas become Phase 2 roadmap items, not POC blockers. |
| **Trigger** | Capability mapping shows <50% RSWG coverage; key RSWG control domains (§2.6 TSP Oversight) not covered; mapping reveals material technical gaps requiring development. |
| **Owner** | DAF (with Fuad technical input) |

### B-REG-02: ITSS §10.0 Mapping Accuracy
**Score:** 8 (L3 × I3) | **Level:** MEDIUM

| Field | Value |
|-------|-------|
| **Source** | DEC-20260827-001, ACT-20260827-002 |
| **Description** | POC now leads with ITSS §10.0 Supplier Management as the binding compliance hook (Directive 5.05-001). VoronCitadel's TPRM module must map cleanly to §10.1 (policy), §10.2 (engagement), §10.3 (agreements), §10.4 (service delivery). If mapping is forced or superficial, Bursa's compliance team will reject the claim. |
| **Mitigation** | 1. ACT-20260827-003 (ITSS capability mapping) must complete before POC document update. 2. Each §10 sub-section mapped to specific VoronCitadel features with evidence. 3. Fuad validates technical capability for each mapped item. 4. Compliance team (Hadri) validates regulatory interpretation. |
| **Trigger** | ITSS §10 mapping reveals VoronCitadel TPRM module is incomplete; regulatory interpretation challenged by Bursa compliance; §10.4 (service delivery monitoring) requires features not in Phase 1. |
| **Owner** | DAF + Hadri |

### B-REG-03: RSWG Compliance Deadline — Bursa Internal Prioritization
**Score:** 9 (L3 × I3) | **Level:** MEDIUM

| Field | Value |
|-------|-------|
| **Description** | RSWG compliance deadline is Dec 31, 2026. But Bursa's internal prioritization of the RSWG recommendations is not yet known. If Bursa treats RSWG as a 2027 initiative (planning year, not implementation year), the urgency lever weakens. |
| **Mitigation** | 1. POC positioning leads with ITSS §10 (already binding) — not dependent on RSWG urgency. 2. CSM channel ascertains Bursa's internal RSWG timeline. 3. If Bursa is in 2026 implementation mode, amplify RSWG urgency. If 2027 planning mode, lead with ITSS §10 + position RSWG as forward readiness. |
| **Trigger** | Bursa indicates RSWG is a 2027 initiative; Bursa compliance team is unaware of RSWG paper; Bursa has existing TPRM solution they believe satisfies RSWG requirements. |
| **Owner** | DAF |

---

## 6. Cross-Cutting Risks

### B-XC-01: Scope Creep During POC Execution
**Score:** 10 (L4 × I3) | **Level:** MEDIUM-HIGH

| Field | Value |
|-------|-------|
| **Description** | Bursa stakeholders may request additional use cases, integrations, or capabilities during POC execution. Without rigid scope management, POC expands beyond Phase 1 capabilities and timeline. |
| **Mitigation** | 1. POC document Section 2 (Scope) explicitly lists in-scope and out-of-scope. 2. Change request process defined — any scope addition requires DAF + Bursa mutual agreement. 3. Phase 2 roadmap document maintained separately — out-of-scope items captured, not discarded. 4. "Scope creep kills POCs" — stated principle in POC document. |
| **Trigger** | Bursa requests additional use cases mid-POC; Bursa asks for integration with internal systems not in original scope; POC timeline extends beyond agreed window. |
| **Owner** | DAF |

### B-XC-02: Data Access & Environment Constraints
**Score:** 8 (L3 × I3) | **Level:** MEDIUM

| Field | Value |
|-------|-------|
| **Description** | POC requires access to Bursa-relevant data (vendor inventory, supplier risk records, control evidence). Bursa may restrict data access due to confidentiality, regulatory, or operational concerns. Without representative data, POC becomes a generic demo, not a Bursa-specific validation. |
| **Mitigation** | 1. POC document Section 5 (Testing Plan) defines data requirements upfront. 2. Simulated/sanitized Bursa-equivalent data prepared as fallback. 3. Data access agreement signed before POC starts. 4. Minimum viable data set defined — what's the least we need to demonstrate value? |
| **Trigger** | Bursa declines data access; data provided is too sanitized to be meaningful; data access delayed beyond POC start date. |
| **Owner** | DAF + Fuad |

### B-XC-03: Single Point of Failure — Fuad Technical Validation
**Score:** 10 (L4 × I3) | **Level:** MEDIUM-HIGH

| Field | Value |
|-------|-------|
| **Description** | All technical validation gates through Fuad. If Fuad is unavailable, delayed, or identifies material gaps, the POC document cannot be finalized. No alternative technical validator identified (Hadri is blockchain lead, not VoronCitadel product owner). |
| **Mitigation** | 1. Fuad validation scheduled with explicit deadline (target: Sep 2). 2. Hadri can validate Teras deployment model independently. 3. If Fuad identifies gaps, scope-down decision (DAF) rather than development sprint. 4. MVP Spec v2.0 as authoritative reference — reduces validation scope to traceability check, not exploratory analysis. |
| **Trigger** | Fuad unavailable for >3 business days; Fuad identifies material capability gaps; Fuad validation requires development work (not just validation). |
| **Owner** | DAF |

---

## Risk Heat Map

| Level | Count | Risk IDs |
|-------|-------|----------|
| **Critical (19-25)** | 0 | — |
| **High (13-18)** | 0 | — |
| **Medium-High (10-12)** | 8 | B-STR-01, B-OPS-01, B-OPS-02, B-TEC-01, B-TEC-03, B-REG-01, B-XC-01, B-XC-03 |
| **Medium (7-9)** | 8 | B-STR-02, B-STR-03, B-OPS-03, B-OPS-04, B-TEC-02, B-TEC-04, B-TEC-05, B-COM-01, B-COM-02, B-COM-03, B-REG-02, B-REG-03, B-XC-02 |

**Top 5 Priority Risks:**
1. **B-STR-01** — RSWG competitive window (score 12)
2. **B-OPS-01** — CSM 7-stakeholder chain (score 12)
3. **B-OPS-02** — DAF single coordinator (score 12)
4. **B-TEC-01** — CRITICAL test case gaps (score 12)
5. **B-TEC-03** — Teras deployment not validated (score 10)

---

## Escalation Matrix

| Risk Level | Trigger | Action | Timeline |
|------------|---------|--------|----------|
| Any risk score → Critical (19+) | Any risk escalates to Critical | Immediate stakeholder escalation | 2 hours |
| High (13-18) | Risk score increases ≥5 points | DAF → CTO escalation | 24 hours |
| Medium-High (10-12) | Mitigation plan fails (2 consecutive weeks) | DAF internal review | 48 hours |
| Medium (7-9) | Risk score increases ≥3 points | Track in weekly review | 7 days |

---

## Review Cadence

| Review | Frequency | Focus |
|--------|-----------|-------|
| **Weekly** | Every Monday (MYT) | All active risks, mitigation progress, trigger status |
| **Pre-POC Gate** | Before POC date set | All B-TEC and B-REG risks must be Medium or lower |
| **POC Execution** | Daily during POC | B-XC risks (scope, data, Fuad availability) |
| **Post-POC** | Within 1 week of POC completion | B-STR-02, B-COM-01 conversion risks |

---

## Related Records

| Record | Type | Relationship |
|--------|------|-------------|
| INT-20260821-002 | Intelligence | POC readiness assessment — source for technical risks |
| RSK-20260820-008 | Risk | Convergence risk pattern — source for operational risks |
| RSK-20260827-001 | Risk | RSWG competitive risk — source for strategic risks |
| ACT-20260827-001 | Action | RSWG capability mapping (due Aug 29) |
| ACT-20260827-002 | Action | POC document RSWG update (due Aug 30) |
| INIT-20260824-001 | Initiative | Bursa POC — parent initiative |
| DOC-20260827-001 | Document | RSWG Recommendation Paper — L1 source |
| DEC-20260827-001 | Decision | POC focus: ITSS §10 primary, RSWG §2.6 forward |

---

## CVS Compliance

| Field | Value |
|-------|-------|
| Claim Tier | T3 [ASSESSMENT] — analytical synthesis from L2 internal records |
| Source Level | L2 (internal validated records + L1 RSWG paper) |
| Confidence Score | 7/10 (Authority 2, Traceability 2, Recency 1, Consistency 1, Completeness 1) |
| Rule 6 Check | ✅ AI-generated, capped at T2. T3 per §7 analytical interpretation from L2 evidence. |

---

**Document Control:**
- **Classification:** TLP:AMBER — Confidential
- **Storage:** `strategic-cognitiveos/risks/RSK-20260827-002-bursa-poc-risk-register.md`
- **Version:** 1.0
- **Last Updated:** 2026-08-27
- **Next Review:** 2026-09-03 (Weekly)
