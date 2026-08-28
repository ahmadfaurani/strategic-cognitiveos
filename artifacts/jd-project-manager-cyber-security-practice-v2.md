---
id: ART-20260828-003
record_type: artifact
title: "Job Description — Project Manager, Cyber Security Practice (v2)"
created_at: 2026-08-28T09:36:00+00:00
updated_at: 2026-08-28T09:36:00+00:00
owner: faurani-jaafar
status: draft
priority: critical
sensitivity: internal
lifecycle_state: candidate
confidence: high
tags:
  - domain/organisational-capability
  - domain/organisational-design
  - domain/cybersecurity-productisation
  - domain/portfolio-governance
  - type/job-description
  - type/reference-document
source:
  type: direct
  reference: "DAF directive 2026-08-28 (detailed JD for review); supersedes v1 (INIT-20260820-004)"
summary: "Revised JD for TBH-001 — Project Manager, Cyber Security Practice. v2 reflects ITSS §10 POC scope, RSWG regulatory tailwind, CSM co-branding, CyberDSA 6-step gate chain, competitive window, interim delegation plan, and end-September hiring timeline."
strategic_significance: "Resolves the primary execution scalability bottleneck — DAF carrying PM coordination by default. Enables concurrent POC delivery, disciplined document production, and frees DAF for strategic direction and stakeholder relationships."
mission_alignment:
  - cybersecurity-productisation
  - organisational-capability
  - portfolio-governance
related_records:
  - GOV-TBH-REGISTRY-001
  - INIT-20260820-004
  - INIT-20260804-001
  - INIT-20260820-003
  - RSK-20260824-003
  - RSK-20260823-001
  - RSK-20260827-002-bursa-poc-risk-register
  - INT-20260827-003-bursa-poc-cognitive-loop-analysis
  - ACT-20260828-001
  - ACT-20260827-001
  - ACT-20260827-002
---

# Job Description — Project Manager, Cyber Security Practice

**Role Title:** Project Manager — Cyber Security Practice
**Department:** Cyber Security Practice
**Reports To:** Hadri (Practice COO)
**Matrix Reporting:** DAF (Director — Cyber Security Practice) for strategic priorities and initiative alignment
**Location:** Level 30, Menara TM, KL (hybrid)
**Employment Type:** Full-time
**TBH Reference:** TBH-001 (CRITICAL)
**Initiative:** INIT-20260804-001 / INIT-20260820-003
**Version:** v2 (Revised 2026-08-28 — reflects ITSS §10 POC scope, RSWG regulatory tailwind, CSM co-branding, CyberDSA timeline, 6-step engineering gate chain)

---

## 1. Purpose

Own the execution coordination of cybersecurity practice deliverables — POC documents, technical briefs, client-facing project artefacts, and delivery tracking — ensuring they are produced on schedule, to quality, and with the right contributors.

This role exists to take project execution coordination off DAF's plate and embed it structurally under the Practice COO. Without this role, DAF carries PM duties by default, creating the exact execution scalability bottleneck the TBH Registry was designed to surface (RSK-20260824-003: DAF carrying 4 concurrent interim roles for Bursa POC alone).

**This is not a GTM programme coordination role.** The GTM Delivery Owner coordinates the go-to-market campaign (sales, marketing, pipeline). This role coordinates the **delivery side** — POC documents, technical deliverables, implementation plans, and client-facing project artefacts produced by the Practice.

---

## 2. Organisational Context

### Practice Structure

| Role | Name | Responsibility |
|------|------|---------------|
| Director — Cyber Security Practice | DAF (Faurani Jaafar) | Strategic direction, commercial owner, stakeholder relationships, final approver |
| Practice COO | Hadri | Technical delivery capability, operational command, line manager for this role |
| Practice Technical Authority | Fuad | Product ownership (VoronCitadel, GovSec TIP, chain:SENTRY), technical review |
| Blockchain Lead / COO | Hadri (dual) | Architecture, technical content for POC documents |
| POC Engineer | Syahir (TBH) | Technical environment provisioning and POC delivery |
| SSE Lead | Amelia Nadia | Stakeholder engagement alignment for POC clients |
| CSM Coordinator | Aishah | MQL Receiver — initial contact qualification in CSM (new, scope being defined) |

### Products (Dev Freeze Aug 11)

| Product | Status | POC Readiness |
|---------|--------|---------------|
| **VoronCitadel** | POC-ready, Bursa Malaysia focus | 19 section files live, 17 requirements (ITSS §10.1-10.4), 3 use cases, 6 test scenarios, 12 acceptance criteria. 76% Native coverage. 6-9 week timeline (3 phases). Retail RM368k, early-adopter RM168k |
| **GovSec-TIP** | Strategic sovereign platform, dev freeze | Gate 4 technical co-branding. Layer 1 CONDITIONAL, Layer 2 CRITICAL GAP (10 missing), Layer 3 STRONG |
| **chain:SENTRY** | Phase 0 hardening | 69% implemented, 47% deployed. 3 Critical Phase 0 blockers |

### Key Partnerships

- **CSM × Aras:** MOU signed. Co-branding confirmed (DEC-20260821-006) for all 3 products. GovSec primary proof point. 7-stakeholder chain: Roshdi → Azrul → Zulfeka → Bala → Wan Roshaimi → Zaharudin → Dr. Megat
- **Bursa Malaysia:** VoronCitadel POC anchored on ITSS §10 Supplier Management (existing binding law, Directive 5.05-001). RSWG §2.6 TSP Oversight = forward enhancement path. NDA Framework sent to Azrul Aug 28 (4 IP provisions under review, due Sep 4)
- **Teras AI Platform:** Farul's 5-layer internal infrastructure layer. VoronCitadel deploys ON Teras. POC timeline 2-3 weeks (was 2-3 months)

---

## 3. Key Responsibilities

### 3.1 Bursa POC Document Execution (Immediate — ACTIVE)

The Bursa POC is the priority engagement. 19 section files are live on github.com/ahmadfaurani/bursa-poc, covering 17 requirements across ITSS §10.1-10.4, 3 use cases, 6 test scenarios, and 12 acceptance criteria.

**Document Coordination:**
- Track all 19 sections by owner, deadline, review state, and blockers
- Coordinate the review cycle: author → Fuad (technical review) → DAF (approval) → final
- Ensure POC document is updated with RSWG alignment (ACT-20260827-002, due Aug 30)
- Ensure capability mapping ITSS × RSWG × VoronCitadel is complete (ACT-20260827-001, due Aug 29)
- Maintain version control on the bursa-poc repo
- Prepare POC document for Fuad validation (Sep 2) and POC finalization (Sep 5)

**NDA & Legal Coordination:**
- Track NDA Framework review status with Azrul/CSM (ACT-20260828-001, due Sep 4)
- Flag any IP provision negotiation delays that compress the 6-8 week competitive window
- Maintain NDA status in POC project plan

**Risk Tracking:**
- Maintain Bursa POC Risk Register (RSK-20260827-002 — 17 risks, 6 categories)
- Monitor top risks: B-STR-01 (compliance window), B-OPS-01 (CSM chain), B-OPS-02 (DAF single coordinator), B-TEC-01 (test case gaps)
- Surface risks to DAF and Hadri before they become blockers

### 3.2 POC Execution Coordination (Ongoing)

For each POC engagement through the CSM channel:

- **Project Plan:** Maintain scope, milestones, owners, dependencies, risks, and timeline
- **Deliverable Tracking:** Coordinate technical deliverable production across Hadri (architecture), Fuad (product), and POC Engineer (environment/delivery)
- **POC Readiness:** Ensure environment provisioned, data loaded, integration scoped, success criteria defined
- **Weekly Status Checks:** Run with delivery team — surface blockers early
- **Status Reporting:** Produce weekly POC status reports for DAF and Hadri: progress, risks, decisions needed
- **Competitive Window Tracking:** Monitor the 6-8 week competitive window (INT-20260827-003). Flag if POC timeline slips relative to CyberDSA Oct 5-7 reference case deadline

### 3.3 CyberDSA Engineering Closure Support

Support the 6-step gate chain for GovSec × CMERP engineering document:

| Step | T-Minus | Date | Owner | Action | PM Role |
|------|---------|------|-------|--------|---------|
| 1 | T-35 | Aug 31 | Fuad | Complete engineering comment closure | Track status, flag delays |
| 2 | T-35 | Aug 31 | Hadri | Consolidate final document | Coordinate handoff |
| 3 | T-34 | Sep 2 | Fuad | Confirm document technically complete | Verify status, update tracker |
| 4 | T-33 | Sep 3 | Tuan Fatah | Internal technical sign-off (CRITICAL) | Track gate status, escalate if at risk |
| 5 | T-32 | Sep 4 | Hafiz Rahman (CSM) | CSM technical validation | Track CSM-side status |
| 6 | T-30 | Sep 5 | Zaharudin | Sign-off, document baselined | Confirm closure, log milestone |

### 3.4 Deliverable Management

- **Practice Deliverables Register:** Maintain what's in production, who owns it, deadline, status, review state
- **WIP Protocol:** Enforce creation owner, audience, strategic/operational/tactical importance, and 7-working-day TAT (3 creation + 2 QC + 1 approval) for every new document
- **4-Role Execution Map:** Track documents through Creation → QC → Approval → Execution
- **TBH Dependencies:** If a deliverable is blocked because a role isn't filled, log it in the TBH Registry

### 3.5 Cross-Functional Coordination

- Primary operational liaison between Practice (Hadri), Product (Fuad), and Director (DAF) for deliverable production
- Coordinate with GTM Delivery Owner on POC-to-commercial transition
- Work with POC Engineer to ensure technical environment readiness aligns with document timeline
- Coordinate with Aishah (CSM MQL Receiver) on POC-related CSM workflow items
- Flag resource conflicts to Hadri (COO) before they become blockers

### 3.6 Quality & Standards

- Ensure all POC documents follow the approved section structure (per DEC-20260820-004) or equivalent approved templates
- Ensure claims in client-facing documents pass claims review (CVS Master Framework) before external distribution
- Maintain version control and document history for all practice deliverables
- Capture lessons learned from each POC engagement: what worked, what didn't, what to improve

---

## 4. Requirements

### Essential

- 3–5 years project management experience in cybersecurity, GRC, technology consulting, or regulated industry
- Demonstrable experience coordinating technical document production across multiple contributors with competing priorities
- Strong understanding of project delivery fundamentals: scope management, milestone tracking, dependency mapping, risk logging, status reporting
- Ability to sit between technical contributors (Hadri, Fuad) and strategic approvers (DAF) without losing fidelity in either direction
- Malaysian regulatory awareness — familiarity with RMiT, SC GTRM, PDPA, BNM guidelines, and Bursa Malaysia ITSS (enough to understand document context, not to author technical content)
- Strong documentation discipline — every deliverable has an owner, deadline, status, and version
- Comfortable holding contributors accountable without having authority over them (matrix coordination)
- Excellent written communication — can produce clear status reports, project plans, and meeting minutes
- Git/GitHub familiarity — can manage document repos, track issues, coordinate PRs for POC documents

### Desirable

- PMP, PRINCE2, or equivalent project management certification
- Experience with GRC, compliance, or RegTech platform delivery
- Experience coordinating POC or pilot engagements in enterprise/B2B context
- Cybersecurity domain knowledge — understands what a POC document needs to contain even if not authoring technical sections
- Experience working in a matrix organisation with COO/Director reporting lines
- Familiarity with the CSM partnership model and institutional sales motion
- Experience with TPRM (Third-Party Risk Management) or supplier risk management frameworks

---

## 5. Success Metrics (First 90 Days)

### Phase 1: Immediate (Week 1 — First 5 Working Days)

| Metric | Target | Source |
|--------|--------|--------|
| Bursa POC document status tracker | Operational — all 19 sections tracked with owner, deadline, review state | ACT-20260827-002 |
| Capability mapping (ITSS × RSWG × VoronCitadel) | Complete and approved | ACT-20260827-001 |
| POC document updated with RSWG alignment | Complete | ACT-20260827-002 |
| POC document ready for Fuad validation | Sep 2 | Gate chain step 3 |
| Practice deliverables register | Established — all in-flight deliverables visible | JD §3.4 |
| NDA Framework review status | Tracked, Azrul response monitored | ACT-20260828-001 |

### Phase 2: Short-Term (30 Days)

| Metric | Target |
|--------|--------|
| POC project plan template | Created and approved by Hadri + DAF |
| Weekly POC status check cadence | Established with delivery team |
| Document review cycle | Formalised: author → reviewer → approver → final, with SLA per stage |
| WIP Protocol | Embedded: every new document gets creation owner, audience, TAT, and execution map at intake |
| Bursa POC completion | POC finalised, ready for CyberDSA reference case |
| CyberDSA engineering gate chain | Tracked through Sep 5 closure |

### Phase 3: Medium-Term (90 Days)

| Metric | Target |
|--------|--------|
| POC engagements coordinated end-to-end | At least 2 with documented status reporting |
| Deliverables without named owner and deadline | Zero |
| POC-to-commercial handoff process | Documented and tested with GTM Delivery Owner |
| Lessons learned | Captured from each POC, fed back into template improvements |
| DAF PM coordination load | Reduced by at least 70% — DAF reviews and approves, does not chase or coordinate |
| Risk register maintenance | Active for all POC engagements, reviewed weekly |

---

## 6. Working Relationships

### Internal

| Person | Role in POC Delivery |
|--------|---------------------|
| **Hadri** (Practice COO — line manager) | Technical content owner (architecture, Sections 2, 3, 5); escalation point for resource conflicts; line manager |
| **DAF** (Director — matrix) | Strategic content owner (Sections 1, 4, 6, 7, 8); final approver; sets priorities |
| **Fuad** (Product Owner / Technical Authority) | Product capability input (Section 2); POC environment owner via POC Engineer; technical review |
| **Syahir** (POC Engineer) | Technical environment provisioning and POC delivery |
| **Amelia Nadia** (SSE Lead) | Stakeholder engagement alignment for POC clients |
| **Aishah** (CSM MQL Receiver) | Initial contact qualification, CSM-side workflow coordination |
| **GTM Delivery Owner** (TBH) | POC-to-commercial transition coordination; GTM pipeline alignment |
| **Athena** (AI agent) | Document authoring support; technical writing |

### External

| Counterpart | Role |
|-------------|------|
| CSM counterparts (Azrul, Zulfeka, Bala, Wan Roshaimi, Zaharudin, Hafiz Rahman) | POC coordination for joint accounts; technical validation; operational enablement |
| POC client teams | POC status communication (operational level) |
| Bursa Malaysia stakeholders | POC engagement coordination (via CSM channel) |

---

## 7. Boundary Exclusions

This role does **not**:

- Author technical content (Hadri/Fuad/Athena own content creation)
- Own product roadmap or feature decisions (Fuad as Product Owner)
- Own GTM campaign execution (GTM Delivery Owner)
- Own sales relationships (Account Owners)
- Make strategic/commercial decisions on POC terms (DAF)
- Own stakeholder engagement strategy (Amelia Nadia as SSE Lead)
- Execute technical POC environment work (POC Engineer)
- Engage in CSM executive stakeholder management (DAF owns Gates 0-6)

This role **coordinates execution**. It does not set strategy, own product, or own relationships. The distinction matters: this role makes other people's delivery faster and more reliable by removing coordination friction.

---

## 8. Reporting Line Rationale

**Reports to Hadri (Practice COO):** The role is a headcount under Hadri's organisation. Hadri owns the technical delivery capability and is the COO of the Practice. The PM executes under his operational command.

**Matrix to DAF (Director):** DAF sets strategic priorities, approves deliverables, and defines what the Practice needs to produce. The PM aligns execution to DAF's priorities but does not report to DAF for day-to-day operations — that goes through Hadri.

This separation is deliberate: it prevents DAF from becoming the default coordination point (the current bottleneck, per RSK-20260824-003) and embeds execution discipline structurally within the COO's org.

---

## 9. Relationship to Existing JDs

| Role | Reports To | Scope | Distinction from TBH-001 |
|------|-----------|-------|--------------------------|
| **TBH-001: PM — Cyber Security Practice** | Hadri (COO) | Practice-level POC document & deliverable execution | Coordinates **what gets produced** and **on what schedule** |
| GTM Delivery Owner | DAF | GTM programme coordination (sales, marketing, pipeline) | Coordinates **go-to-market campaign execution** |
| POC Engineer | Fuad | Technical POC environment & client liaison | Owns **technical delivery** of POC engagements |
| Account Owner | Shuhada | Sales relationship for 5-7 accounts | Owns **client relationship** through POC |
| Marketing Ops Specialist | Azzatullina | CRM, email automation, attribution | Owns **campaign instrumentation** |
| CSM MQL Receiver | Aishah | Initial contact qualification in CSM | Owns **inbound lead qualification and routing** |

TBH-001 is the missing piece: nobody coordinates the **production of practice deliverables**. The GTM Delivery Owner coordinates the campaign. The POC Engineer handles technical environment. But someone needs to ensure the document sections are written, reviewed, approved, and delivered on time. That's TBH-001.

---

## 10. Key Risks This Role Mitigates

| Risk ID | Risk | How TBH-001 Mitigates |
|---------|------|----------------------|
| RSK-20260824-003 | Interim ownership concentration on DAF — 4 concurrent roles | Absorbs PM coordination role, reduces DAF from 4 roles to 2 (strategic + commercial) |
| RSK-20260823-001 | TBH-001 case dismissed on methodology | Role justified by structural vacancy, not quantitative claims |
| RSK-20260827-002 (B-OPS-02) | DAF single coordinator for Bursa POC | PM becomes primary coordinator, DAF becomes approver |
| RSK-20260827-002 (B-OPS-01) | CSM chain dependency | PM tracks CSM-side dependencies, flags delays early |
| RSK-20260827-002 (B-TEC-01) | Test case gaps | PM tracks test case status, flags incomplete cases before validation gates |

---

## 11. Compensation & Benefits

**Salary Range:** RM 8,000 – RM 12,000/month (commensurate with experience)

**Benefits:**
- EPF, SOCSO, EIS (statutory)
- Medical coverage
- Annual leave (standard Aras Integrasi policy)
- Professional development budget (certification support: PMP, PRINCE2)
- Hybrid work arrangement (office + remote)

**Performance Review:** Quarterly, aligned with Cognitive Loop Review cadence

---

## 12. Hiring Timeline

| Milestone | Target Date | Status |
|-----------|-------------|--------|
| JD finalised and approved | Aug 28, 2026 | This document — for DAF review |
| Role posted (LinkedIn, job portals, internal referral) | Sep 1, 2026 | Pending DAF approval |
| Shortlisting | Sep 8-12, 2026 | — |
| First-round interviews | Sep 15-19, 2026 | — |
| Second-round interviews (Hadri + DAF) | Sep 22-26, 2026 | — |
| Offer extended | Sep 29-30, 2026 | — |
| Hiring activation | End of September 2026 | Per DAF directive Aug 28 |
| Target start date | Oct 13-20, 2026 | 2-3 weeks notice period |

**Note:** DAF carries PM interim responsibilities through hiring activation. Explicit delegation to Fuad, Hadri, and Amelia should be assigned for the interim period to avoid SPOF concentration.

---

## 13. Interim Delegation Plan (Until TBH-001 Filled)

| Responsibility | Interim Owner | Rationale |
|----------------|---------------|-----------|
| POC document status tracking | DAF (with Ember support) | Ember can maintain trackers and flag deadlines; DAF reviews |
| Technical review cycle coordination | Hadri | Already owns technical content; add review cycle management |
| POC environment readiness tracking | Fuad (via Syahir) | Fuad already owns POC environment via POC Engineer |
| Stakeholder engagement tracking | Amelia Nadia | SSE Lead already owns stakeholder alignment |
| NDA/legal status tracking | DAF | Commercial/legal stays with Director |
| Risk register maintenance | Ember (with DAF review) | Ember can maintain registers; DAF approves |
| Weekly status reporting | DAF | Until PM hired, DAF produces (or delegates to Ember for drafting) |

---

*This role is the execution backbone of the Practice. Without it, the Director carries coordination by default, the COO can't operationalise delivery, and POC documents depend on individual heroics rather than systematic project management. With it, the Practice gains the discipline to deliver concurrently — multiple POCs, multiple documents, multiple clients — without everything flowing through one person.*
