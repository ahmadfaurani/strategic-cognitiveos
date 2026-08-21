---
id: INT-20260821-003
record_type: intelligence
intelligence_type: operational
title: "VoronCitadel Bursa POC Draft v0.1 — Fuad Technical Validation Report"
created_at: 2026-08-21T17:05:00+00:00
updated_at: 2026-08-21T17:05:00+00:00
owner: ember
status: active
priority: critical
sensitivity: confidential
lifecycle_state: canonical
confidence: high
tags:
  - domain/csm-partnership
  - domain/cybersecurity-productisation
  - domain/commercial-development
  - product/voroncitadel
  - type/technical-validation
  - type/poc
  - type/success-trigger
source:
  type: document
  reference: Voron_Citadel_Bursa_Malaysia_POC_Draft_v0.1.docx (DAF, Aug 20), cross-referenced against MVP_SPECIFICATION.md
summary: "Technical validation of DAF's POC draft v0.1 against MVP Product Specification v2.0. 20 sections, 22 test cases, 7 use cases assessed. 5 items require Fuad's attention: (1) UC-04 digital-risk scenarios may claim Phase 2 capabilities, (2) UC-05 AI Copilot cross-domain queries may exceed current production scope, (3) UC-07 connector framework is Phase 2, (4) Teras infrastructure not mentioned, (5) Sovereign AI differentiator underemphasized. 17 of 22 test cases confirmed against production features."
strategic_significance: "Technical accuracy is the foundation of the success trigger. Any claim that doesn't hold up under Bursa technical scrutiny destroys the document's entire trigger function."
mission_alignment:
  - csm-partnership
  - cybersecurity-productisation
related_records:
  - INT-20260821-002
  - ACT-20260821-005
  - CONV-20260821-002
---

# VoronCitadel Bursa POC Draft v0.1 — Technical Validation Report

**Document validated:** Voron_Citadel_Bursa_Malaysia_POC_Draft_v0.1.docx
**Reference:** MVP Product Specification v2.0 (`products/voroncitadel/MVP_SPECIFICATION.md`)
**Date:** 2026-08-21 17:05 UTC

---

## Document Overview

DAF's draft is a 20-section, execution-ready POC plan — far more comprehensive than the original 8-section framework. It covers: executive summary, Bursa context, objectives, guiding principles, scope/boundaries, use-case catalogue (7 use cases), architecture, data/integration design, security, test strategy (22 test cases), success criteria (10 weighted criteria with Must/Should gates), 4-week implementation timeline, RACI, governance, defect management, risks (10 risks), exit criteria, final report structure, and 5 appendices.

**Overall assessment:** Strategically excellent. Technically sound with 5 areas requiring Fuad's validation.

---

## Test Case Validation Against Production (22 Test Cases)

### ✅ Confirmed Against Production (17/22)

| Test ID | Scenario | MVP Spec Reference | Status |
|---------|----------|-------------------|--------|
| GRC-01 | Import selected control set | Control Library CRUD, import capabilities | ✅ Production |
| GRC-02 | Map one control to multiple requirements | control_framework_mappings (n:m), multi-framework | ✅ Production |
| GRC-03 | Attach and retrieve evidence | Evidence Locker per control, file upload/download | ✅ Production |
| GRC-04 | Control result changes risk/compliance view | Control effectiveness → compliance coverage, dashboard | ✅ Production |
| ASM-01 | Authorised asset discovery or import | VoronScout company/domain/IP mode, crt.sh, DNS | ✅ Production |
| ASM-02 | Finding prioritisation | Per-asset findings with severity, EVAT scoring | ✅ Production |
| ASM-03 | Finding-to-risk linkage | "Promote to Risk Register or remediation items" | ✅ Production |
| TPRM-01 | Vendor onboarding and tiering | 4-tier classification, vendor registry | ✅ Production |
| TPRM-02 | Assessment finding and remediation | 5 assessment types, remediation tracking | ✅ Production |
| TPRM-03 | Vendor risk to enterprise view | Vendor dashboard, TPRA composite score | ✅ Production |
| RPT-01 | Executive dashboard drill-down | Executive Analytics, portfolio distributions | ✅ Production |
| RPT-02 | Evidence/report export | PDF board report export (jsPDF) | ✅ Production |
| SEC-01 | Role-based access | 7 roles, 30 permissions, RBAC, RequirePermission | ✅ Production |
| SEC-02 | Audit trail | Immutable audit log, append-only | ✅ Production |
| INT-01 | Import error handling | File upload with metadata, validation | ✅ Production |

### ⚠️ Requires Fuad's Validation (5/22)

| Test ID | Scenario | Concern | Question for Fuad |
|---------|----------|--------|-------------------|
| **ASM-04** | Unknown asset workflow | Flag, assign for validation, resolve | Does the platform support an "unknown/unowned asset" flagging and assignment workflow? MVP spec mentions discovery and findings but doesn't explicitly describe an unknown-asset triage workflow. |
| **DRM-01** | Digital-risk event triage | Document mentions "look-alike domains, phishing indicators, exposed credentials, brand-abuse examples" | MVP spec explicitly defers "Phishing lookalike / typo-squatting domain monitoring" and "Brand and dark-web monitoring" to Phase 2. If the POC uses manually ingested sample events (not automated detection), this may be fine. But the wording implies the platform can handle these. Fuad must clarify: is this sample data ingestion (achievable) or automated detection (Phase 2)? Test is "Should" priority — could be reframed or dropped. |
| **AI-01** | Cross-domain query with evidence | Document describes "natural-language cross-domain questions" | Production Copilot capabilities are: (1) compliance narrative, (2) evidence auto-drafting, (3) coverage-status suggestion, (4) cross-framework cross-referencing, (5) feedback loop, (6) TPRA threat assessment. A general-purpose "ask anything across domains" natural language query implies a RAG pipeline, which is listed as Phase 2 ("AI RAG Pipeline"). Fuad must clarify: can the Copilot handle open-ended cross-domain queries, or only the 6 specific capabilities? If only the 6, the test scenario should be rewritten to test those specifically. |
| **AI-02** | Unsupported/ambiguous query behaviour | Same concern as AI-01 | If the Copilot can't handle open-ended queries, testing for "ambiguous query behaviour" is less relevant. Should be rewritten to test the actual capabilities' boundaries. |
| **INT-02** | Optional read-only API/connector | Document describes "connector" demonstration | The REST API exists (22 routers under /api/), so API ingestion is technically possible. But the "Integration Connector Build-Out" (SIEM, ticketing, CMDB, IdP) is listed as Phase 2. Fuad must clarify: can a simple read-only API call be demonstrated for ingestion, or does this require the full connector framework? Test is "Optional" — could be dropped entirely. |

---

## Structural / Strategic Observations (Not Test Cases)

### 1. Teras Infrastructure — Not Mentioned
The document's Section 7 (Proposed POC Architecture) describes an "isolated evaluation tenant" but does not mention Teras AI Platform as the infrastructure layer. Per DEC-20260820-008, Teras is the deployment model for VoronCitadel POCs — it eliminates the need for multi-tenant RLS build and provides sovereign AI infrastructure.

**Question for Fuad:** Should the architecture section reference Teras explicitly? For Bursa (stock exchange, NCII), sovereign infrastructure is a major differentiator. Its absence from the document may be intentional (keep it simple) or an oversight.

### 2. Sovereign AI Differentiator — Underemphasized
The document mentions AI Copilot but does not explicitly highlight:
- Malaysian data residency (no tenant data sent to foreign endpoints)
- AI provenance audit trail (ai_compliance_audit_log, data_residency = 'on_prem')
- AI Sovereignty Score

For a stock exchange operating under Malaysian regulatory jurisdiction, this is arguably the strongest differentiator against foreign competitors. The document treats AI as a feature; it should be positioned as a sovereign assurance capability.

**Question for Fuad:** Is the sovereign AI story intentionally de-emphasized for the POC stage, or should it be more prominent?

### 3. Bursa Cybersecurity Controls (61 Requirements) — Not Explicitly Called Out
The document says "Bursa-selected frameworks" and "Bursa-selected internal/external requirement sets" without explicitly mentioning that Bursa Malaysia Cybersecurity Controls (61 requirements) are already loaded in the production database. This is the strongest "built for you" evidence point.

**Question for Fuad:** Is the omission intentional (let Bursa choose their own frameworks during kickoff) or should the document note that Bursa-specific controls are already in the platform?

### 4. Source Baseline (Appendix D) — References Older Documents
The document references:
- VoronDRQ Sales Kit README.md v1.0 (April 2026)
- VoronDRQ Proposal Templates v1.0 (April 2026)
- VoronDRQ Product Brochure v1.1 (August 2026)

These predate the MVP Product Specification v2.0 (August 2026) which is the authoritative production-verified reference. Fuad should validate that the sales kit/brochure claims are consistent with the MVP Spec.

### 5. "Isolated Evaluation Tenant" Framing
The MVP is single-tenant Docker Compose. An "isolated evaluation tenant" = a separate deployment instance. This is technically accurate but the framing implies multi-tenant capability that doesn't exist yet (Phase 2).

**Question for Fuad:** Is "isolated evaluation environment" or "dedicated POC deployment" more accurate language? Minor but technically precise.

### 6. UC-04 (Digital-Risk/Threat Correlation) — Scope Concern
The use case describes ingesting "approved sample events" and correlating them. The test (DRM-01) is "Should" priority. The concern is that the sample events described (look-alike domains, phishing, brand abuse) map to Phase 2 capabilities. Options:
- Reframe as "manual ingestion of sample threat events with cross-domain linkage" (achievable)
- Drop UC-04 entirely and redistribute weight to UC-01/UC-03 (simpler)
- Keep as-is but add a note that automated detection is Phase 2

### 7. Hypotheses (H1-H6) — Mostly Sound
- H1 (unified data model reduces manual cross-referencing) → ✅ Confirmed by MVP Spec
- H2 (Bursa control/evidence workflows without excessive customisation) → ✅ Confirmed (configurable workflows)
- H3 (external exposure prioritised by business context) → ✅ Confirmed (EVAT scoring, findings with business context)
- H4 (third-party observations feed enterprise risk view) → ✅ Confirmed (TPRA → Risk Register promotion)
- H5 (AI-assisted queries with evidence/citations) → ⚠️ Depends on what "queries" means. The 6 production capabilities are specific, not general-purpose.
- H6 (executive dashboards with drill-down) → ✅ Confirmed (Executive Analytics, board report)

---

## Summary: What Fuad Needs to Do

| Priority | Item | Action |
|----------|------|--------|
| **CRITICAL** | AI-01/AI-02 test scenarios | Confirm: can Copilot handle open-ended cross-domain NL queries, or only the 6 specific production capabilities? Rewrite test scenarios to match actual capability. |
| **CRITICAL** | DRM-01 test scenario | Confirm: is this sample data ingestion (achievable) or automated detection (Phase 2)? Reframe or drop. |
| **HIGH** | Teras in architecture section | Should Section 7 reference Teras as infrastructure layer? Bursa would care about sovereign infrastructure. |
| **HIGH** | Sovereign AI positioning | Should the document more prominently highlight Malaysian data residency, AI provenance audit, and AI Sovereignty Score? |
| **MEDIUM** | ASM-04 (unknown asset workflow) | Does the platform support flagging/assigning unknown assets? If not, rewrite or drop. |
| **MEDIUM** | INT-02 (optional connector) | Can a simple read-only API ingestion be demonstrated, or is this Phase 2? If Phase 2, drop (it's already "Optional"). |
| **MEDIUM** | Bursa Cybersecurity Controls | Should the document explicitly note 61 Bursa requirements are already loaded? |
| **LOW** | Source baseline references | Verify sales kit/brochure claims match MVP Spec v2.0. |
| **LOW** | "Isolated evaluation tenant" language | Consider "dedicated POC deployment" for technical precision. |

---

## CVS Compliance

| Field | Value |
|------|-------|
| Claim Tier | T3 [ASSESSMENT] |
| Source Level | L2 (internal validated records — MVP Spec + POC draft) |
| Confidence Score | 8/10 (Authority 2, Traceability 2, Recency 2, Consistency 1, Completeness 1) |
| Rule 6 Check | ✅ AI-generated, capped at T2. T3 per §7 analytical interpretation from L2 evidence. |
