---
id: INT-20260821-002
record_type: intelligence
intelligence_type: operational
title: "VoronCitadel POC Bursa Malaysia Pre-Flight Readiness Assessment"
created_at: 2026-08-21T16:50:00+00:00
updated_at: 2026-08-21T16:50:00+00:00
owner: ember
status: active
priority: critical
sensitivity: internal
lifecycle_state: canonical
confidence: high
tags:
  - domain/csm-partnership
  - domain/cybersecurity-productisation
  - domain/commercial-development
  - product/voroncitadel
  - type/readiness-assessment
  - type/poc
source:
  type: email
  reference: CONV-20260821-002, ACT-20260820-004, COM-20260820-003
summary: "8-section readiness assessment for Bursa POC document. Overall readiness ~38%. Substantial raw material exists but zero Bursa-specific synthesis. 20-28hrs weekend sprint needed. DAF owns 5 sections, Hadri 3, Fuad validates."
strategic_significance: "First client-facing POC document from CSM channel. Quality directly affects POC conversion probability."
mission_alignment:
  - csm-partnership
  - cybersecurity-productisation
related_records:
  - CONV-20260821-002
  - ACT-20260820-004
  - COM-20260820-003
  - RSK-20260820-008
---

# VoronCitadel POC — Bursa Malaysia Pre-Flight Readiness Assessment

**Date:** 2026-08-21 16:50 UTC (Aug 22 00:50 MYT)
**Prepared by:** Ember
**Classification:** TLP:AMBER — Internal Operational Use
**CVS:** T3 [ASSESSMENT] / L2 (internal validated records) / Confidence 7/10
**Trigger:** DAF email thread Aug 19–21 (4 emails), ACT-20260820-004, COM-20260820-003

---

## Context

CSM (Azrul Nazim) confirmed VoronCitadel POC for Bursa Malaysia, deep-dive Monday Aug 24 10:00 MYT. DAF escalated to Fuad for validated positioning document. 8-section POC documentation framework requested. This assessment maps existing material against the 8 sections, identifies gaps, and recommends weekend action plan.

---

## 8-Section Readiness Matrix

| # | Section | Existing Material | Readiness | Gap | Owner |
|---|---------|------------------|-----------|-----|-------|
| 1 | POC Project Brief | Product Baseline Summary, MVP Spec Executive Summary, GTM Outreach Package | **40%** | No Bursa-specific brief. Generic product positioning exists but needs translation to Bursa context (stock exchange, capital market infrastructure, NCII) | DAF |
| 2 | POC Scope & Use Cases | MVP Spec (full feature set), Bursa Cybersecurity Controls (61 requirements in framework), CSM POC Target Analysis | **35%** | Bursa-specific use cases not defined. Which of the 4 domains (GRC, DRM, ASM, TPRM) are in scope? Which of 61 Bursa controls to target? | Hadri + Fuad |
| 3 | POC Implementation Plan | ASSESS-20260820-001 (POC FTE model, 8-week POC load math, timeline acceleration with Teras), Teras architecture (DEC-20260820-008) | **45%** | Generic POC timeline exists (8 weeks, 80-120 hrs). Needs Bursa-specific phasing, dependencies, milestones. Teras-as-infrastructure changes deployment model. | Hadri |
| 4 | Success Criteria & Acceptance Framework | GTM Outreach Package (POC targets), CSM POC Target Analysis (30-day metrics), MVP Spec (production-verified features) | **25%** | No Bursa-specific acceptance criteria. What does "successful POC" mean for Bursa? Which controls demonstrated? What evidence? | DAF |
| 5 | Testing / Validation Plan | MVP Spec (production-verified feature set, 45 tables, 295 requirements) | **20%** | No POC-specific testing plan. Which workflows to demonstrate? What evidence per control? User validation approach? | Hadri |
| 6 | POC Roles & RACI | GTM Outreach Package (RACI), COM-20260820-003 (DAF owns 5 sections, Hadri 3), ASSESS-20260820-001 (team model), Amelia as SSE Lead (DEC-20260820-012) | **55%** | Aras internal RACI clear. Missing: CSM role, Bursa role. 3-party RACI needed (Aras × CSM × Bursa). Amelia's role in POC coordination? | DAF |
| 7 | Risks, Assumptions & Dependencies | RSK-20260820-008 (convergence risk), CSM POC Target Analysis (risk assessment), MVP Spec (Phase 2 deferrals), ChainSentry Phase 0 blockers (credential rotation) | **50%** | Generic risks identified. Missing: Bursa-specific assumptions (data access, environment, stakeholders), CSM dependency as channel, Teras infrastructure readiness | DAF |
| 8 | Post-POC Pathway | CSM POC Target Analysis (upsell RM 500K-1M), ASSESS-20260820-001 (break-even 4 paying, RM 138K/yr per customer), VoronCitadel POC Mode (6-7 POCs + 3 paying) | **40%** | Commercial model exists. Missing: Bursa-specific progression (POC → pilot → production → commercial), pricing for Bursa, deployment timeline, Bursa-specific commercial terms | DAF |

**Overall Readiness: ~38%** — substantial raw material, zero Bursa-specific synthesis.

---

## What Can Be Reused Directly

| Source Document | Reuse Value |
|----------------|-------------|-------------|
| MVP Product Specification v2.0 | Sections 1-4 of POC doc can draw heavily on architecture, feature sets, compliance frameworks. The 61 Bursa Cybersecurity Controls requirement set is directly relevant. |
| Product Baseline Summary | Executive overview language, differentiators, production status. Reusable for Section 1 (Project Brief). |
| GTM Outreach Package | RACI structure, POC qualification criteria, success metrics framework. Reusable for Sections 4 and 6. |
| ASSESS-20260820-001 (FTE Model) | POC load math (80-120 hrs over 8 weeks), team capacity, timeline acceleration with Teras. Reusable for Section 3. |
| Teras AI Platform (DEC-20260820-008) | Infrastructure layer explanation. Deployment model. Reusable for Section 3 and Section 7. |
| CSM POC Target Analysis | Risk patterns, competitive landscape, regulatory drivers. Reusable for Section 7. |

---

## What Must Be Produced (Net New)

| Section | Net New Content Required | Estimated Effort |
|---------|------------------------|-----------------|
| 1. POC Project Brief | Bursa-specific objectives, Bursa context (stock exchange, NCII, regulatory drivers), engagement model (Aras-CSM-Bursa), proposed outcome | 3-4 hrs (DAF) |
| 2. POC Scope & Use Cases | Select 2-3 high-impact Bursa use cases from 4 domains. Map to Bursa Cybersecurity Controls (61 requirements). Define in-scope vs out-of-scope explicitly. | 4-6 hrs (Hadri + Fuad) |
| 3. POC Implementation Plan | Bursa-specific phasing (Week 1-8), dependencies (Bursa env access, CSM coordination), milestones, responsibilities | 3-4 hrs (Hadri) |
| 4. Success Criteria | Measurable outcomes per use case. Definition of "successful POC completion." Evidence requirements. Validation criteria. | 2-3 hrs (DAF) |
| 5. Testing / Validation Plan | Which workflows demonstrated, test scenarios, user validation steps, evidence artifacts per control | 3-4 hrs (Hadri) |
| 6. POC Roles & RACI | 3-party RACI: Aras × CSM × Bursa. Named roles. Amelia's coordination role. | 1-2 hrs (DAF) |
| 7. Risks, Assumptions & Dependencies | Bursa-specific assumptions (data access, env, stakeholder availability), CSM as channel dependency, Teras readiness, resource contention (RSK-20260820-008) | 2 hrs (DAF) |
| 8. Post-POC Pathway | Bursa-specific: POC → pilot → production. Pricing model. Deployment on Teras. Commercial terms. Timeline to production. | 2-3 hrs (DAF) |

**Total estimated effort: 20-28 hours over 2-3 days (weekend)**

---

## Recommended Bursa Use Cases (Initial — for Hadri/Fuad Validation)

Based on Bursa Malaysia's profile as a capital market infrastructure operator and NCII entity:

### Use Case 1: Bursa Cybersecurity Controls Compliance Monitoring
- **Domain:** GRC + Compliance
- **Value:** 61 Bursa Cybersecurity Controls already in the platform. Demonstrate continuous compliance monitoring against Bursa-specific framework.
- **Why:** Directly addresses Bursa's own regulatory requirements. Shows "built for you" not "generic tool."
- **Effort:** Low — framework already loaded in production.

### Use Case 2: Third-Party Risk Assessment (TPRA) for Bursa's Vendors
- **Domain:** TPRM
- **Value:** Bursa depends on trading platform vendors, clearing house, data vendors. Automated 6-hourly TPRA monitoring demonstrates continuous vendor risk visibility.
- **Why:** Supply chain risk is a BNM RMiT mandate (2026 Q3). Bursa has complex vendor ecosystem.
- **Effort:** Medium — needs Bursa vendor list (sample 5-10 vendors).

### Use Case 3: Attack Surface Management (VoronScout)
- **Domain:** ASM
- **Value:** Outside-in discovery of Bursa's externally exposed digital footprint. Real-time scan during POC demo.
- **Why:** Stock exchange = high-value target. Live ASM demo is visually compelling.
- **Effort:** Low — VoronScout is production-ready. Scan Bursa domains live.

---

## Weekend Action Plan (Aug 22-23)

| Day | DAF | Hadri | Fuad |
|-----|-----|-------|------|
| **Sat Aug 22** | Sections 1, 4, 6, 7, 8 (drafts) | Sections 2, 3, 5 (start) | Section 2 input (use case selection, capability mapping) |
| **Sun Aug 23** | Review all sections, consolidate, finalize | Submit 3 sections by noon | Review technical sections, validate product claims |
| **Sun evening** | **Single consolidated document ready** | | |

**Deliverable:** 8-section POC document, consolidated, ready for Monday 10:00 MYT pre-flight check with Azrul/CSM.

---

## Strategic Positioning Notes

1. **Bursa is NOT in the original top-5 POC targets** (CSM POC Target Analysis listed BNM, NACSA, EPF, TNB, MOH). Bursa comes through CSM channel — first named POC from the CSM partnership.

2. **CSM's role is channel + credibility, not execution.** Azrul opens the door. Aras carries execution. Amelia's email confirms this framing.

3. **The Monday session is a "deep dive project brief," not a POC kickoff.** The objective is to present a credible POC framework and identify what Bursa needs to provide (data access, environment, stakeholders). Not to have everything finished.

4. **DAF's second email (Aug 21) escalates urgency.** He wants a "validated document I can highlight to initiate direct engagement with Bursa Technical Stakeholder." This means the document must be technically credible, not just strategically framed.

5. **Teras changes the deployment story.** VoronCitadel on Teras = sovereign infrastructure, no foreign endpoints, air-gapped capability. This is a major differentiator for a stock exchange.

6. **The 5 BNM RMiT compliance frameworks (including Bursa Cybersecurity Controls, 61 requirements) are already loaded in production.** This is the strongest "built for you" evidence point.

---

## CVS Compliance

| Field | Value |
|------|-------|
| Claim Tier | T3 [ASSESSMENT] |
| Source Level | L2 (internal validated records) |
| Confidence Score | 7/10 (Authority 2, Traceability 2, Recency 1, Consistency 1, Completeness 1) |
| Rule 6 Check | ✅ AI-generated, capped at T2. T3 per §7 analytical interpretation from L2 evidence. |
| Evidence Register | Entry to be logged |
