---
# === UNIVERSAL BASE ===
id: DOC-20260911-005
record_type: document
title: "VoronVigil OMS TPRM Proposal v1.1 — Sovereign AI OMS Supplier Compliance and Trust-Centric Third-Party Risk Management Platform (Submitted to CSM 11 Sep 2026)"
created_at: 2026-09-11T16:51:00+00:00
updated_at: 2026-09-11T16:51:00+00:00
owner: faurani-jaafar
status: active
priority: critical
sensitivity: confidential
lifecycle_state: candidate
confidence: high
document_type: proposal
version: "1.1"
author: "Aras Integrasi Sdn Bhd (DAF — Ahmad Faurani Jaafar, Director Cyber Security Practice)"
file_path: documents/DOC-20260911-005-voronvigil-oms-tprm-proposal.pdf
tags:
  - domain/csm-partnership
  - domain/commercial-development
  - domain/cybersecurity-productisation
  - domain/sovereign-technology
  - domain/compliance
  - type/proposal
  - product/voronvigil
  - workstream/cybersec-products
source:
  type: document
  reference: "PDF relayed by DAF (Telegram, 11 Sep 2026 16:45 UTC), 37 pages, 2,015,409 bytes. SHA-256 e80b591cc47bb270f81aefb7288546e5285791bff1f4228ce4c61c466c612755. PDF metadata: 'Microsoft Word - VoronVigil__OMS_TPRM_Proposal_v1.1'. Title page: Version 1.1, dated 11th September 2026. This is the proposal artifact referenced by ART-20260911-001, transmitted by CONV-20260911-008 (DAF → Azrul, 11 Sep 2026) and under CSM review per ACT-20260911-007."
summary: "[FACT per source document] VoronVigil Solution Proposal v1.1, 37 pages — Malaysia-hosted, Sovereign-AI-enabled TPRM platform for oversight of OMS providers used by Bursa Malaysia Participating Organisations. Structure: §1 Problem Statement (fragmented assurance; Bursa service-specificity → Required Assurance Unit = PO × OMS Provider × OMS/Service Arrangement; trust-risk gap; sovereignty/privacy challenge). §2 Proposed Solution (business outcomes; ITSS alignment table 10.3.1, 10.3.2(a)–(g), 10.4.1–10.4.3; OMS Compliance Pack Sections A–D — pack cannot be marked submission-ready if mandatory response, evidence reference, source location, reviewer approval or approved N/A rationale is missing). §3 Sovereign AI & Data Sovereignty (VoronVigil Sovereign AI Zone — Malaysia-hosted, policy-enforcing internal AI gateway recording model/prompt version, evidence IDs, reviewer outcome per execution; appropriate-AI-uses table with human/deterministic authority; AI boundaries — every AI result is a Draft AI Analysis until approved; Malaysia PDPA-by-design table; data-sovereignty commitments — Malaysia residency by default, deny-by-default egress, no shared/public model training). §4 Operating Model & Architecture (supplier assurance lifecycle; seven architecture layers — stakeholder experience, OMS compliance core, deterministic decision services, Sovereign AI Zone, enterprise/supplier inputs, approved external intelligence, protected assurance layer; critical design decisions — OMS service instance is the core record, compliance pack generated from live evidence, compliance / residual risk / CTDM kept as three separate outcomes, AI assists while deterministic services decide). §5 Evidence, Contract & Service Assurance (per-conclusion evidence model with document hash, page/section, reviewer, AI-assistance metadata; six control statuses — Pass / Partial / Fail / Insufficient Evidence / Not Applicable / Requires Review; event-driven reassessment triggers — major outage, repeated SLA breach, failed DR test, RTO breach, delayed incident notification, evidence expiry, contract amendment, unresolved audit right, material scope change). §6 CTDM (purpose, dimensions, deterministic scoring approach, OMS-specific interpretation, illustrative scenario, lifecycle use, governance & limitations). §7 Implementation Roadmap (Phase 0 Mobilise → Phase 1 Compliance Foundation → Phase 2 Sovereign AI copilot → Phase 3 Service & Contract Assurance → Phase 4 CTDM → Phase 5 Continuous Assurance). §8 Success Criteria & Decision Request — approval to commence Phase 0–1 (six work items) plus sovereign-AI architecture design in Phase 0 and private-AI copilot implementation in Phase 2 subject to PO controls. Appendices: A. Assumptions (PO to provide authoritative GTRM text and internal legal/compliance interpretation before final production control wording approved); B. Demo Example. QA flags: 'VoronSigil' naming residue in footers/figure captions (39 occurrences vs 44 VoronVigil); title-page v1.1 vs v1 in transmitting email."
strategic_significance: "Completes ART-20260911-001 evidencing — the first named product proposal in the Bursa engagement is now sha-pinned in the canonical repo rather than summary-attested from the email body. Fully specifies the ask under CSM review (ACT-20260911-007): §8.2 decision request is broader than 'commence Phase 0–1' — it additionally requests approval to design the sovereign-AI architecture during Phase 0 and implement the private-AI copilot in Phase 2, subject to PO security architecture, data classification, privacy governance, model assurance, operational-risk and cross-border transfer controls. Phase 0–1 scope confirmed as six work items: OMS service-instance inventory/ownership/criticality; ITSS 10.3/10.4 control library + OMS overview mapping; Malaysia-hosted evidence & provenance repository with secure supplier evidence workflow; agreement/SLA register + clause-to-obligation assessment; OMS-specific assessment/remediation/approval + immutable audit trail; OMS Compliance Pack generation. Submission-ready gating, three-outcome separation (compliance / residual risk / CTDM) and deterministic-AI decision split are the key differentiators vs generic TPRM tooling — directly reusable in GTM narrative and CyberDSA collateral. Phase-model conflation guard upheld: VoronVigil Phases 0–5 are distinct from the POC Build Phased model (DEC-20260824-001) and POC Validation Phase. PO-side dependency recorded (Appendix A): GTRM text + legal interpretation must come from the PO before final production control wording — sequence into Phase 0–1 mobilisation and the CSM working discussion."
mission_alignment:
  - domain/commercial-strategy
  - domain/csm-partnership
  - domain/cybersecurity-productisation
  - domain/sovereign-technology
related_records:
  - CONV-20260911-008
  - ART-20260911-001
  - ACT-20260911-007
  - ACT-20260828-002
  - INIT-20260824-001
  - DEC-20260824-001
  - OPP-20260820-001
  - STK-20260813-008
---

# Document Overview

VoronVigil Solution Proposal v1.1 — "Sovereign AI OMS Supplier Compliance and Trust-Centric Third-Party Risk Management Platform", 37 pages. Submitted by DAF to Azrul Nazim (CSM) 11 Sep 2026 (CONV-20260911-008); PDF relayed to CognitiveOS 16:45 UTC the same day and sha-pinned into the canonical repo. This record completes ART-20260911-001 evidencing (same pattern as DOC-20260911-004 intake).

# Structure (8 sections + appendices)

| Section | Content |
|---|---|
| 1. Problem Statement | OMS supplier oversight complexity and consequence; fragmented assurance practice; Bursa service-specificity → Required Assurance Unit = PO × OMS Provider × OMS/Service Arrangement; the trust-risk gap; sovereignty and privacy challenge |
| 2. Proposed Solution | Business outcomes; ITSS 10.3.1 / 10.3.2(a)–(g) / 10.4.1–10.4.3 alignment table; OMS Compliance Pack (Sections A–D) with submission-ready gating on evidence, reviewer approval and N/A rationales |
| 3. Sovereign AI & Data Sovereignty | Sovereign AI Zone (Malaysia-hosted, policy-enforcing AI gateway, per-execution audit trail); appropriate-AI-uses table with human/deterministic authority split; AI boundaries (Draft AI Analysis until approved); PDPA-by-design table; data-sovereignty commitments (deny-by-default egress, no shared-model training, documented cross-border exceptions) |
| 4. Operating Model & Architecture | Supplier assurance lifecycle; seven architecture layers; critical design decisions — OMS service instance as core record, compliance pack from live evidence, compliance/residual-risk/CTDM kept separate, AI assists + deterministic services decide |
| 5. Evidence & Service Assurance | Per-conclusion evidence model (document hash, page/section, freshness, reviewer, AI-assistance metadata); six control statuses (Pass / Partial / Fail / Insufficient Evidence / Not Applicable / Requires Review); event-driven reassessment triggers |
| 6. CTDM | Purpose; dimensions; deterministic scoring; OMS-specific interpretation; illustrative scenario; lifecycle use; governance and limitations |
| 7. Implementation Roadmap | Phase 0 Mobilise → 1 Compliance Foundation → 2 Sovereign AI (copilot) → 3 Service & Contract Assurance → 4 CTDM → 5 Continuous Assurance |
| 8. Success Criteria & Decision Request | Independently reproducible ITSS conclusions; deterministic CTDM from reviewer-validated evidence; Board reporting distinguishing compliance / residual risk / CTDM; decision requested (below) |
| Appendices | A. Assumptions (PO provides authoritative GTRM text + legal interpretation before final production control wording); B. Demo Example |

# Decision Requested (§8.2)

1. **Approval to commence Phase 0–1** — six work items: (1) OMS service-instance inventory, ownership and criticality assessment; (2) ITSS 10.3/10.4 control library and OMS overview mapping; (3) Malaysia-hosted evidence and provenance repository with secure supplier evidence workflow; (4) agreement/SLA register and clause-to-obligation assessment capability; (5) OMS-specific assessment, remediation, approval and immutable audit trail; (6) VoronVigil OMS Compliance Pack for management and regulatory-response readiness.
2. **Separate approval to design the sovereign-AI architecture during Phase 0 and implement the private-AI copilot in Phase 2**, subject to PO security architecture, data classification, privacy governance, model assurance, operational-risk and cross-border transfer controls.

# QA Flags (for DAF; pre-CyberDSA hygiene)

| Flag | Detail | Suggested action |
|---|---|---|
| Naming residue | "VoronSigil Proposal" footer throughout + Figure 2 caption "VoronSigil Sovereign AI Zone Architecture" (39 occurrences) vs product name VoronVigil (44 occurrences) | v1.2 find-and-replace pass on footers/captions before wider distribution |
| Version delta | Transmitting email and ART-20260911-001 logged v1; title page states Version 1.1 (11 September 2026) | ART corrected to v1.1 on this relay; align CSM-facing references |
| PO dependency | Appendix A: PO to supply current authoritative GTRM text and internal legal/compliance interpretation before final production control wording is approved | Sequence into Phase 0–1 mobilisation; state explicitly in the CSM working discussion |

# Provenance

Relayed by DAF via Telegram 11 Sep 2026 16:45 UTC; staged PDF copied to `documents/DOC-20260911-005-voronvigil-oms-tprm-proposal.pdf` and sha-pinned (SHA-256 e80b591cc47bb270f81aefb7288546e5285791bff1f4228ce4c61c466c612755). Content extracted and cross-checked against the email-body record (CONV-20260911-008): ITSS 10.3/10.4 mapping, CTDM dimensions, assessment unit, six-phase model and Phase 0–1 ask all confirmed consistent; §7 roadmap and §8.2 decision request extracted directly from the PDF to close the sections the email preview truncated.

# Related Records

- CONV-20260911-008 — Covering email (DAF → Azrul, 11 Sep 2026)
- ART-20260911-001 — Proposal artifact record (evidenced by this document)
- ACT-20260911-007 — CSM review + Phase 0–1 approval decision (open; §8.2 covers both approval parts)
- ACT-20260828-002 — NDA joint legal review (hard gate before Phase 0–1 execution touching restricted Bursa information)
- INIT-20260824-001 — Bursa Malaysia VoronCitadel Sectorial POC (parent initiative; phase-model separation)
- DEC-20260824-001 — TPRM-first approach (doctrine this proposal operationalises)
- OPP-20260820-001 — VoronCitadel POC — Bursa Malaysia (opportunity)
- STK-20260813-008 — Azrul Nazim (CSM)
