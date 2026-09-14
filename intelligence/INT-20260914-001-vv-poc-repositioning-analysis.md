---
id: INT-20260914-001
record_type: intelligence
title: "Analytical Overview — Azrul's VoronVigil POC Feedback: Scope Correction, Repositioned Phase 1 Operating Model, G0–G6 Delivery Gates"
created_at: 2026-09-14T05:25:00+00:00
updated_at: 2026-09-14T05:25:00+00:00
owner: faurani-jaafar
intelligence_type: operational
status: active
priority: critical
sensitivity: confidential
lifecycle_state: canonical
confidence: high
tags:
  - domain/csm-partnership
  - domain/cybersecurity-productisation
  - domain/commercial-development
  - domain/sovereign-technology
  - product/voronvigil
  - framework/cognitive-loop
  - lifecycle/active
source:
  type: operator-directive
  reference: "DAF analytical overview delivered via Telegram 2026-09-14 05:19 UTC (12:19 MYT) — Directive-5 intake analysis of CSM feedback (CONV-20260914-002, OUT-20260914-001)"
summary: "DAF directive-5 analysis of Azrul's 13 Sep CSM review. Headline: interpret as scope correction, not rejection — design endorsed, approval blocked only on scope alignment. Central shift: VoronVigil Phase 1 repositioned from PO-operated TPRM platform to Bursa/CSM 'intake-and-evaluate' capability supporting the OMS thematic review, re-baselined on the mission of 24 independent PO assessment reports + 1 consolidated ITSS/GTRM report. Extends OUT-20260914-001 with structural build directives: Phase 1 title ('Sovereign AI OMS Thematic Review Intake & Evaluation Platform'), 7-actor operating model, minimalist PO submission boundary (upload + receipt only), Bursa/CSM evaluator workbench, ITSS↔GTRM core + RMiT conditional overlay + CTDM as decoupled optional annex, preserved assessment grain extended for banking-group/shared OMS, G0–G6 report-production delivery gates replacing the six-phase POC roadmap (roadmap retained as product roadmap), explicit POC Definition of Done, NDA/legal track elevated to POC mobilisation gate, and strategic interpretation: land narrowly → prove regulatory utility → establish assessment data foundation → expand later."
strategic_significance: "Converts CSM's conditional feedback into an executable re-baselining plan and resolves the strategic framing question: do not fight the scope contraction — exploit it as the shortest path to the POC. The narrow wedge (manual PDF/email process → secure evidence intake → AI-assisted Bursa/CSM assessment → 24+1 regulatory reports) builds the evidence repository, PO/OMS relationship model, ITSS/GTRM mapping, assessment history and in-environment Sovereign AI demonstration that the broader VoronVigil vision later requires. Also materially shrinks Phase 1 build scope (no PO-facing dashboard/workflow layer) — favourable against the 2-FTE engineering SPOF."
mission_alignment:
  - sovereign-ai
  - productisation
  - csm-partnership
related_records:
  - CONV-20260914-002
  - OUT-20260914-001
  - ACT-20260914-004
  - ACT-20260914-005
  - ACT-20260914-006
  - ACT-20260911-007
  - ACT-20260828-002
  - DOC-20260911-005
  - ART-20260911-001
  - STK-20260813-008
  - OPP-20260820-001
  - INIT-20260824-001
---

# Analytical Overview — Azrul's Input on VoronVigil POC

**Date:** 2026-09-14 (analysis delivered 05:19 UTC / 12:19 MYT; source feedback 13 Sep 2026 10:15 MYT)
**Subject:** CSM (Azrul) review of VoronVigil OMS TPRM Proposal — requirement-to-POC translation and re-baselining directives
**Strategic Objective:** Convert the withheld Phase 0–1 approval into a re-baselined POC with a demonstrably shorter path to approval
**Diligence:** D3 (Strategic — shapes the Bursa POC approval path, proposal v2.0 scope, and Phase 1 commercial framing)
**Evidence base:** Azrul's written 8-area review (CONV-20260914-002) + DAF analysis. CSM positions are L2-sourced (written stakeholder statement). Structural build elements are Aras-proposed and require CSM/Bursa agreement — flagged in §16.

---

## 1. Executive Assessment

Azrul's response is a **scope correction, not a rejection**. He explicitly states the technical and data-sovereignty design is strong, and requires scope-alignment issues to be resolved before approval progresses.

**Central strategic shift:** VoronVigil Phase 1 must not be positioned as a TPRM platform operated by Participating Organisations (POs). It must be positioned as a **secure Bursa/CSM "intake-and-evaluate" capability** supporting the OMS thematic review.

**Re-baselined POC mission:** 24 independent PO assessment reports on OMS Providers + 1 consolidated assessment report against ITSS/GTRM. This materially simplifies the POC and gives Aras a much clearer route to approval.

## 2. Requirement-to-POC Translation

| Area | Azrul / CSM Position | POC Interpretation | Required Aras Action |
|------|----------------------|--------------------|----------------------|
| Problem statement | Fragmented OMS assurance process framing is valid | Retain current problem statement | Do not rewrite the problem; narrow the solution |
| Phase 1 objective | 24 PO assessment reports + 1 consolidated ITSS/GTRM report | Primary POC success criterion | Rebuild proposal, architecture and timeline around these outputs |
| PO role | POs must not operate a full TPRM/compliance platform | PO becomes evidence submitter only | Strip PO-facing workflow, dashboards, scoring, compliance management |
| Bursa/CSM role | All evaluation occurs on Bursa/CSM side | Bursa/CSM = assessment authority and principal platform user | Build evaluator workbench around Bursa/CSM requirements |
| Conflict of interest | CSM/Bursa cannot be assessor and vendor of a platform operated by assessed POs | Strong architectural and commercial separation required | Do not position Phase 1 as a PO operational system |
| Regulatory scope | ITSS mapping strong; SC GTRM 8.03–8.15 must be incorporated | Unified ITSS/GTRM control model | Complete clause-level cross-mapping before resubmission |
| Sovereign AI | Approach accepted; AI only on evaluator side | Major differentiator retained | Malaysian-hosted AI, deterministic assessment, AI audit logging unchanged |
| CTDM | Technically sound, outside current assessment framework | Not required for POC success | Move CTDM to optional/future annex |
| Assessment grain | PO × OMS Provider × OMS/Service Arrangement correct | Existing data model retained | Extend for banking-group/shared OMS scenarios |
| Banking POs | 11 banking-group-affiliated POs need special consideration | Additional regulatory/context dimension | Add RMiT overlay alongside ITSS/GTRM |
| Dashboards / continuous assurance | Beyond Phase 1 requirement; creates approval dependencies | Move to future-phase roadmap | Remove from Phase 1 |
| Timeline | Six-phase roadmap doesn't demonstrate report delivery within deadline | Outcome-based implementation required | Replace roadmap with report-production milestones |
| Approval | Phase 0–1 cannot currently be approved | Proposal needs re-baselining before formal approval | Resolve scope issues first; then seek approval |

Azrul is explicit that the current operational-platform concept exceeds Phase 1: POs upload evidence and see only confirmation that Bursa received it; scoring, findings, compliance status, workflow and dashboards remain invisible to POs and handled entirely within Bursa/CSM.

## 3. Recommended Phase 1 Repositioning

| | Positioning |
|---|---|
| **Current** | VoronVigil Sovereign AI OMS Supplier Compliance and Trust-Centric Third-Party Risk Management Platform — describes the broader product vision well, but raises unnecessary questions about PO adoption, commercialisation, workflow ownership, conflict of interest and continuous service delivery |
| **Recommended Phase 1** | **VoronVigil — Sovereign AI OMS Thematic Review Intake & Evaluation Platform** |

**Purpose:** Securely collect OMS supporting evidence from Bursa Participating Organisations and enable Bursa Malaysia / CyberSecurity Malaysia to perform controlled, auditable and AI-assisted evaluation against ITSS and GTRM requirements, producing 24 independent PO assessment reports and one consolidated thematic-review report.

This retains the VoronVigil platform identity while aligning Phase 1 almost completely with Azrul's stated requirement.

## 4. Target Phase 1 Operating Model

| Actor | Interaction with VoronVigil | Visibility |
|-------|------------------------------|------------|
| Participating Organisation | Authenticate → select OMS arrangement → upload supporting documents → submit | Submission acknowledgement only |
| Bursa Malaysia | Review evidence, assessment progress and findings | Full assessment visibility |
| CyberSecurity Malaysia | Evidence evaluation, clause mapping, assessment and validation | Full evaluator functionality |
| VoronVigil Sovereign AI | Evidence extraction, classification, clause mapping, analytical assistance, report drafting | Internal Bursa/CSM capability only |
| Deterministic Assessment Engine | Apply authoritative assessment logic against controls | Bursa/CSM only |
| Human Assessor | Review AI output, validate evidence/findings, approve consequential conclusions | Final authority |
| Aras | Platform technology / implementation role | No assessment authority |

This architecture directly addresses the conflict-of-interest concern: CSM/Bursa remain assessors; VoronVigil is their assessment instrument, not a service sold to the entities being assessed.

## 5. POC Functional Boundary

### 5A. PO-Facing Submission Layer — deliberately minimalist

| Include | Exclude |
|---------|---------|
| Secure authentication | Compliance dashboard |
| OMS/service-arrangement identification | Compliance score |
| Evidence/document upload | Control-gap analysis |
| Submission metadata | Findings |
| Submission acknowledgement | Remediation workflow |
| Submission reference | CTDM score |
| Ability to provide requested additional evidence if Bursa initiates it | AI assistant/advisor |
| Receipt/status such as Submitted / Received | Bursa internal assessment progress |

**This is the single most important architectural change required by Azrul.** POs know only that documents were received; clause mapping, findings and compliance determination remain entirely within Bursa/CSM.

### 5B. Bursa/CSM Evaluator Workbench — where VoronVigil's technical value concentrates

| Capability | POC Requirement |
|------------|-----------------|
| Evidence repository | Centralised PO/OMS evidence collection |
| Document extraction | Extract relevant information from submitted documentation |
| Evidence classification | Associate evidence with appropriate assessment requirements |
| ITSS mapping | Clause-level ITSS 10.3/10.4 assessment |
| GTRM mapping | Clause-level GTRM 8.03–8.15 assessment |
| Cross-mapping | Unified ITSS ↔ GTRM assessment checklist |
| RMiT overlay | Applied where banking-group affiliation/shared OMS arrangements make it relevant |
| AI assistance | Evidence extraction, analysis, clause mapping, report drafting |
| Deterministic engine | Authoritative assessment/scoring logic |
| Human validation | Analyst approval of consequential findings |
| Audit logging | Trace AI, system and assessor actions |
| Report generator | Generate individual and consolidated reports |

Azrul accepts the current Sovereign AI model (Malaysian hosting, AI-assisted analysis, deterministic decision logic, audit logging) with the constraint that AI remains entirely on the Bursa/CSM assessment side. **Sovereign AI remains a strongest POC differentiator — do not dilute.**

## 6. Regulatory Engine — Critical Gap to Close

Azrul validated ITSS 10.3/10.4 treatment but identified an explicit proposal deficiency: equivalent clause-level treatment of SC GTRM 8.03–8.15 is missing, and must be incorporated into the proposal rather than deferred.

| Regulatory Layer | POC Treatment |
|------------------|---------------|
| Bursa ITSS 10.3 / 10.4 | Core |
| SC GTRM 8.03–8.15 | Core |
| ITSS ↔ GTRM cross-mapping | Core |
| RMiT | Conditional overlay for relevant banking-group POs |
| CTDM | Future/optional analytical layer |
| Other compliance frameworks | Future phase |

Hierarchy: **Regulatory Compliance → Core POC; Additional Trust Analytics → Future Enhancement.**

## 7. Assessment Unit — Preserved and Extended

Azrul specifically endorses the current assessment grain: **PO × OMS Provider × OMS/Service Arrangement** (correct granularity). VoronVigil must additionally support:

> PO → Banking Group → Shared/Group-Owned OMS → OMS Provider → Service Arrangement

The data model must support both direct and inherited/shared OMS relationships — particularly for the 11 banking-group-affiliated POs, where Azrul wants RMiT considered alongside ITSS/GTRM.

## 8. Phase 1 Outputs — Mandatory vs Out-of-Scope

**Mandatory Phase 1 outputs (all P0):** 24 independent PO × OMS assessment reports; 1 consolidated ITSS/GTRM thematic assessment report; evidence repository; assessment audit trail; clause/evidence mapping; assessment findings; supporting compliance evidence pack.

| Current Feature | Treatment |
|-----------------|-----------|
| PO compliance dashboard | Remove from Phase 1 |
| PO compliance score | Remove |
| PO remediation workflow | Remove |
| PO operational TPRM management | Remove |
| Continuous monitoring | Future phase |
| Service assurance | Future phase |
| Board dashboards beyond consolidated report | Future phase |
| Continuous assurance | Future phase |
| CTDM | Optional annex |
| Full trust-risk analytics | Future phase |
| Broader TPRM operating model | Future phase |

**CTDM strategy: do not delete CTDM from VoronVigil — decouple it from POC acceptance.** Azrul is positive about CTDM (compliance / residual-risk / trust-score separation) but will not let a proprietary methodology become an approval dependency.

## 9. Delivery Construct — G0–G6 Report-Production Gates

The existing Mobilise → Compliance Foundation → Sovereign AI → Service Assurance → CTDM → Continuous Assurance sequence remains the **product roadmap**, not the Bursa POC delivery plan.

| Gate | Objective | Exit Condition |
|------|-----------|----------------|
| G0 — Alignment | Freeze revised scope | Bursa/CSM agree upload-and-evaluate architecture |
| G1 — Regulatory Baseline | Complete ITSS/GTRM cross-map | Unified assessment checklist approved |
| G2 — Platform Configuration | Configure submission + evaluator workflow | End-to-end workflow demonstrated |
| G3 — Pilot Assessment | Run selected representative PO cases | Assessment/report methodology validated |
| G4 — Production Assessment | Assess all participating POs | 24 assessment reports completed |
| G5 — Consolidation | Aggregate thematic findings | Consolidated ITSS/GTRM report generated |
| G6 — Closure | POC review | Bursa/CSM formally determine next-phase direction |

This connects technical delivery directly to Bursa's required regulatory output — which the previous roadmap did not.

## 10. POC Definition of Done (North Star)

> VoronVigil Phase 1 POC is successful when Bursa/CSM can securely receive supporting OMS evidence from participating organisations, analyse and map that evidence against an approved unified ITSS/GTRM control framework using auditable Sovereign AI and deterministic assessment mechanisms, validate findings through human assessors, and produce the required 24 independent assessments and one consolidated thematic-review report — without exposing assessment logic, scoring or findings to the participating organisations.

## 11. Legal / Governance Track — a POC Mobilisation Gate, Not Ancillary

Azrul's NDA response (OUT-20260911-002) is broadly favourable: confidentiality/restricted information, no publicity, PDPA handling, Background IP disclosure, reuse restrictions and subsequent Service Agreement principles accepted; Bursa-specific foreground IP principle acceptable with detailed terms pending.

**Unresolved — legal review required:** Background IP licence; CSM/Bursa sublicensing; IP indemnity; detailed contractual rights.

Azrul wants the contractual structure determined **before** restricted Bursa information is exchanged → the legal workstream (ACT-20260828-002) is a POC mobilisation gate.

## 12. Recommended Revised POC Architecture

```
Participating Organisations
        ↓
Secure Evidence Submission Portal  (Upload + Receipt Only)
        ↓
Evidence Repository
        ↓
Bursa/CSM Restricted Assessment Zone
   → Sovereign AI Evidence Extraction
   → ITSS/GTRM Clause Mapping
   → RMiT Overlay where applicable
   → Deterministic Assessment Engine
   → Human Assessor Validation
   → Audit Trail
        ↓
Assessment Output Engine
   → 24 Independent PO Reports
   → 1 Consolidated ITSS/GTRM Report
```

Everything below the submission boundary is Bursa/CSM-facing. **This separation must be visible in the next diagram presented to Azrul** — he has explicitly requested a walkthrough showing the PO upload-only model.

## 13. Alignment Session Positioning

Meeting objective is NOT to defend the existing proposal — it is to demonstrate that Aras has absorbed Azrul's guidance and already restructured the POC accordingly.

| Discussion | Desired Decision |
|------------|------------------|
| Phase 1 mission | Confirm 24 + 1 reports |
| PO experience | Confirm upload/acknowledgement only |
| Evaluator experience | Confirm Bursa/CSM-only evaluation |
| Regulatory baseline | Freeze ITSS 10.3/10.4 + GTRM 8.03–8.15 |
| Banking POs | Confirm RMiT overlay treatment |
| Assessment unit | Confirm PO × OMS Provider × OMS/Service |
| Sovereign AI | Confirm evaluator-side use |
| CTDM | Agree optional annex/future phase |
| Output template | Bursa/CSM approve report structure |
| Data required | Determine evidence/data requirements |
| Timeline | Freeze assessment/report milestones |
| Governance | Establish NDA/legal gate |
| Architecture | Approve revised upload-and-evaluate model |
| POC approval | Define exact approval authority and next gate |

## 14. Priority Actions for Aras (Execution Order)

1. Re-baseline the proposal around the 24 + 1 reporting outcome
2. Redraw the architecture showing the PO as upload-only
3. Build GTRM 8.03–8.15 into the compliance engine and proposal
4. Design the ITSS/GTRM unified assessment checklist
5. Add the RMiT overlay/data model for the 11 banking-affiliated POs
6. Remove PO dashboards, scoring and remediation functionality from Phase 1
7. Move CTDM, continuous assurance, service assurance and broader dashboards into a clearly labelled Future Phase / Optional Annex
8. Replace the six-phase POC roadmap with report-production gates
9. Prepare sample outputs: one individual PO assessment report + one consolidated thematic report
10. Advance NDA/Teaming Agreement/legal alignment before exchanging Bursa-restricted information

## 15. Strategic Interpretation

The feedback **improves** the probability of getting VoronVigil into Bursa. The earlier proposal attempted a substantial federated TPRM operating model in one approval motion. Azrul has provided the wedge:

> Current manual PDF/email process → VoronVigil secure evidence intake → AI-assisted Bursa/CSM assessment → 24 + 1 regulatory reports

Once VoronVigil has ingested real OMS evidence, established the PO/OMS relationship model, implemented ITSS/GTRM mapping, built the assessment history and demonstrated Sovereign AI within Bursa/CSM's environment, much of the foundation for the broader VoronVigil vision already exists.

**Optimal commercial and technical strategy:** Land narrowly → prove regulatory utility → establish the assessment data foundation → expand later into remediation, CTDM, dashboards and continuous assurance. **Do not fight the scope contraction — exploit it as the shortest path to the POC.**

## 16. CV Qualification — Source Classification

- **CSM positions** ( §§1–2 core conditions, PO receipt-only visibility, GTRM incorporation requirement, AI evaluator-side constraint, CTDM decoupling, banking-group/RMiT extension, timeline objection, legal-gate requirement): L2-sourced from Azrul's written review of 13 Sep (CONV-20260914-002) — HIGH confidence, already captured in OUT-20260914-001.
- **Aras-proposed structural elements** (§3 Phase 1 title, §4 operating model, §5 boundary tables, §9 G0–G6 gates, §10 Definition of Done, §13 session decision list): operator-authored analysis (DAF), single-source internal — HIGH confidence as direction, but these represent Aras positions **pending CSM/Bursa agreement** at the alignment meeting (ACT-20260914-006). They must not be presented as CSM-agreed.
- **No independent multi-source verification performed** — not required: the record consolidates directive guidance on an internally-controlled workstream, not external claims.
