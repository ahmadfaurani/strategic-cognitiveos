---
id: INT-20260821-002
record_type: intelligence
intelligence_type: operational
title: "VoronCitadel POC Bursa Malaysia — Success Trigger Assessment (Re-engineered)"
created_at: 2026-08-21T16:50:00+00:00
updated_at: 2026-08-21T16:57:00+00:00
owner: ember
status: active
priority: high
sensitivity: internal
lifecycle_state: canonical
confidence: high
tags:
  - domain/csm-partnership
  - domain/cybersecurity-productisation
  - domain/commercial-development
  - product/voroncitadel
  - type/readiness-assessment
  - type/success-trigger
  - type/poc
source:
  type: email
  reference: CONV-20260821-002, ACT-20260820-004, COM-20260820-003, DAF directive Aug 21 16:56 UTC
summary: "Re-engineered assessment framing the 8-section POC document as a success trigger instrument, not a deadline deliverable. DAF has already drafted the document. Fuad's technical validation is the gating step. Monday is Azrul's CSM-internal briefing, not a Bursa-facing session. No POC date set. Each section must be engineered to trigger a specific decision or action from Bursa technical stakeholders."
strategic_significance: "The document is a strategic instrument — its purpose is to make the POC the obvious, low-friction next step for Bursa. Quality of engineering matters more than speed of delivery."
mission_alignment:
  - csm-partnership
  - cybersecurity-productisation
  - commercial-development
related_records:
  - CONV-20260821-002
  - ACT-20260820-004
  - COM-20260820-003
  - RSK-20260820-008
  - DEC-20260820-012
---

# VoronCitadel POC — Bursa Malaysia Success Trigger Assessment

**Date:** 2026-08-21 16:57 UTC (Aug 22 00:57 MYT)
**Revision:** v2 — re-engineered from sprint-framed to success-trigger-framed per DAF directive

---

## Corrected Context

| Parameter | Previous (Wrong) | Corrected |
|-----------|------------------|-----------|
| Monday Aug 24 | Bursa-facing deep dive | Azrul's CSM-internal briefing |
| POC date | Implied Monday | Not set — pre-POC positioning phase |
| Document status | Needs creation (38% ready) | DAF has drafted it; Fuad validation is the gate |
| Amelia's role | General SSE | CyberDSA stakeholder activation specifically |
| Urgency framing | Weekend panic sprint | Engineer for success trigger quality |
| Document purpose | POC documentation | Instrument to initiate direct Bursa technical stakeholder engagement |

---

## Success Trigger Framework

The 8-section document is not documentation. It is an instrument engineered to produce a specific outcome: **when Azrul or DAF puts it in front of Bursa's technical stakeholders, the POC becomes the obvious, low-friction next step.**

Every section has a trigger function — a specific cognitive shift it must produce in the reader. If a section doesn't trigger a decision or action, it's dead weight.

### Section-by-Section Trigger Engineering

#### Section 1: POC Project Brief
- **Trigger:** "This team understands our context — we're not just another account"
- **Engineering requirement:** Must reference Bursa-specific context (stock exchange, capital market infrastructure, NCII designation, Bursa Cybersecurity Controls) — not generic GRC positioning
- **Validation question for Fuad:** Are the product capability claims accurate and production-verified?
- **Existing material to draw from:** Product Baseline Summary, MVP Spec Executive Summary

#### Section 2: POC Scope & Use Cases
- **Trigger:** "These use cases map to our actual problems — not a vendor's product roadmap"
- **Engineering requirement:** 2-3 Bursa-specific use cases, each mapped to Bursa Cybersecurity Controls (61 requirements already in platform). In-scope and out-of-scope explicit.
- **Validation question for Fuad:** Are the use cases technically feasible with current production features? Any that require Phase 2 capabilities?
- **Existing material:** MVP Spec (full feature set), 61 Bursa Cybersecurity Controls in production database

#### Section 3: POC Implementation Plan
- **Trigger:** "This is feasible and low-risk to start — we're not signing up for a science project"
- **Engineering requirement:** Phased plan with clear dependencies, minimal Bursa-side effort, Teras as infrastructure layer (sovereign deployment, no foreign endpoints). Timeline that respects Bursa's operational constraints.
- **Validation question for Fuad:** Is the Teras-VoronCitadel deployment model accurate? Are the infrastructure assumptions correct?
- **Existing material:** ASSESS-20260820-001 (POC load math), Teras architecture (DEC-20260820-008)

#### Section 4: Success Criteria & Acceptance Framework
- **Trigger:** "We know what 'done' looks like — measurable, not vibes"
- **Engineering requirement:** Measurable outcomes per use case. Binary criteria (met/not met). Evidence artifacts defined. No vague "demonstrate capability" language.
- **Validation question for Fuad:** Can the platform actually produce the evidence artifacts specified? Are the acceptance criteria technically achievable within POC scope?
- **Existing material:** GTM Outreach Package (success metrics framework), MVP Spec (production-verified features)

#### Section 5: Testing / Validation Plan
- **Trigger:** "We'll see real evidence against our own environment — not a canned demo"
- **Engineering requirement:** Test scenarios using Bursa-relevant data (or simulated equivalent). User validation steps. Evidence per control. Live VoronScout scan as the compelling visual.
- **Validation question for Fuad:** Are the test scenarios achievable with current production capabilities? Does VoronScout work against Bursa's external footprint? Any technical constraints?
- **Existing material:** MVP Spec (production-verified feature set, 45 tables, 295 requirements)

#### Section 6: POC Roles & RACI
- **Trigger:** "Roles are clear — nobody's confused about who does what"
- **Engineering requirement:** 3-party RACI: Aras × CSM × Bursa. Named roles (not "Team"). Amelia's CyberDSA activation role distinct from POC execution. CSM as channel, not delivery layer.
- **Validation question for Fuad:** Are the Aras technical roles and responsibilities accurate? Does the RACI reflect actual engineering capacity (3-person team, no HoE yet)?
- **Existing material:** GTM Outreach Package (RACI), ASSESS-20260820-001 (team model), DEC-20260820-012 (Amelia as SSE Lead)

#### Section 7: Risks, Assumptions & Dependencies
- **Trigger:** "They've thought about what could go wrong — and how to prevent it"
- **Engineering requirement:** Bursa-specific assumptions (data access, environment, stakeholder availability). CSM dependency as channel. Teras readiness. Resource constraints acknowledged honestly — not hidden.
- **Validation question for Fuad:** Are the technical risks accurately stated? Any missing technical dependencies (integration points, data formats, network requirements)?
- **Existing material:** RSK-20260820-008 (convergence risk), CSM POC Target Analysis, MVP Spec (Phase 2 deferrals)

#### Section 8: Post-POC Pathway
- **Trigger:** "There's a path forward — not just an experiment that ends with a report"
- **Engineering requirement:** POC → pilot → production → commercial. Pricing model. Deployment on Teras (sovereign infrastructure). Bursa-specific commercial terms. Timeline that shows institutional commitment, not transactional thinking.
- **Validation question for Fuad:** Is the deployment model technically sound? Are the production-readiness assumptions accurate?
- **Existing material:** ASSESS-20260820-001 (break-even model), CSM POC Target Analysis (upsell path), VoronCitadel POC Mode

---

## What Fuad Needs to Validate

Since DAF has already drafted the document, the assessment is not about what to create — it's about what Fuad must verify:

| Validation Area | What Fuad Checks | Why It Matters |
|----------------|-----------------|----------------|
| **Product capability claims** | Every feature claimed in the document exists in production | A single false claim destroys credibility with technical stakeholders |
| **Use case feasibility** | Each Bursa use case is achievable with current production features (not Phase 2) | Overpromising Phase 1 capabilities = failed POC |
| **Bursa Cybersecurity Controls accuracy** | 61 requirements in platform, mapping is correct | This is the "built for you" evidence — must be airtight |
| **Teras deployment model** | VoronCitadel-on-Teras is technically sound, not aspirational | Bursa will ask "how does this deploy?" — answer must be confident |
| **Testing plan technical soundness** | Test scenarios are executable, evidence artifacts are producible | A test plan that can't be executed = no POC |
| **Infrastructure requirements** | Network, compute, data access assumptions are realistic | Bursa infra team will scrutinize this |
| **Phase 2 boundary clarity** | What's NOT in scope is as accurate as what IS | Scope creep kills POCs |

---

## Existing Material Available to Fuad for Validation

| Document | Location | Validation Use |
|----------|----------|----------------|
| MVP Product Specification v2.0 | `products/voroncitadel/MVP_SPECIFICATION.md` | Authoritative feature reference — every claim should trace here |
| Product Baseline Summary | `products/voroncitadel/PRODUCT_BASELINE.md` | Executive-level capability summary |
| Teras AI Platform | `documents/DOC-20260820-003.md` | Infrastructure layer validation |
| FTE Model & Financial Analysis | `assessments/ASSESS-20260820-001.md` | POC load math, team capacity |
| Convergence Risk | `risks/RSK-20260820-008.md` | Resource contention context |
| CSM POC Target Analysis | `govsec-docs/intelligence/CSM-POC-TARGET-ANALYSIS.md` | Regulatory drivers, competitive landscape |

---

## Strategic Positioning Notes (Unchanged)

1. **Bursa is the first named POC from the CSM channel** — not in the original top-5 target list. Comes through CSM partnership, not direct outreach.

2. **CSM's role is channel + credibility.** Azrul opens the door. Aras carries execution. Amelia confirmed this framing explicitly.

3. **Monday is Azrul's briefing — CSM-internal.** The document positions Aras for when Azrul (or DAF) engages Bursa's technical stakeholders directly. No Bursa-facing deadline.

4. **The 5 compliance frameworks including Bursa Cybersecurity Controls (61 requirements) are already loaded in production.** This is the strongest "built for you" evidence point. Fuad must validate this is accurate and demonstrable.

5. **Teras changes the deployment story.** Sovereign infrastructure, no foreign endpoints, air-gapped capability. Major differentiator for a stock exchange. Fuad must validate Teras-VoronCitadel integration is real, not aspirational.

6. **The document is a success trigger, not a deliverable.** Its purpose is to make the POC the obvious next step. Every section engineered for a specific trigger. If it doesn't trigger, it doesn't go in.

---

## CVS Compliance

| Field | Value |
|------|-------|
| Claim Tier | T3 [ASSESSMENT] |
| Source Level | L2 (internal validated records + DAF directive) |
| Confidence Score | 7/10 (Authority 2, Traceability 2, Recency 1, Consistency 1, Completeness 1) |
| Rule 6 Check | ✅ AI-generated, capped at T2. T3 per §7 analytical interpretation from L2 evidence. |
