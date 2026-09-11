---
id: GOV-TBH-REGISTRY-001
record_type: document
title: TBH Registry — Roles To Be Hired
created_at: 2026-08-20 08:32:00+00:00
updated_at: 2026-08-25 02:17:00+00:00
owner: DAF
status: active
priority: high
sensitivity: internal
lifecycle_state: canonical
confidence: high
tags:
  - domain/cognitiveos-operations
  - domain/cybersecurity-productisation
  - domain/governance
  - domain/organisational-capability
  - domain/organisational-design
  - domain/portfolio-governance
  - framework/actionable-intelligence-protocol
  - framework/cognitive-loop
source:
  type: direct
  reference: DAF authority — created per directive 2026-08-20 08:32 UTC; capacity-planning linkage clarified 2026-08-25
summary: Registry of roles that are identified as required but not yet hired. Each entry tracks the role, its scope, what it blocks, and hiring status. From 25 Aug 2026, role creation and priority are additionally governed by workstream-to-FTE evidence under ACT-20260825-002.
strategic_significance: Prevents portfolio governance gaps from remaining invisible. A TBH role that blocks critical actions is a structural risk — this registry makes it visible and trackable. Workstream-to-FTE mapping now provides the evidence layer for new or revised TBH entries.
mission_alignment:
- organisational-capability
- portfolio-governance
related_records:
- GOV-PORTFOLIO-REGISTER-001
- SOP-COGNITIVE-LOOP-REVIEW-001
- ACT-20260825-002
document_type: reference
file_path: governance/TBH-REGISTRY.md
version: '1.2'
author: DAF
---

# TBH Registry — Roles To Be Hired

**Created:** 2026-08-20 | **Authority:** DAF | **Review cadence:** Weekly (aligned with Cognitive Loop Review, Monday 10:30 AM UTC+8) | **Last updated:** 2026-09-08

---

## Purpose

Every TBH role that blocks a portfolio action is a structural risk. This registry makes that risk visible, trackable, and enforceable. If a role is TBH and it blocks a CRITICAL action, it appears here until filled or the action is reassigned.

### Capacity-Planning Linkage — 25 Aug 2026

Per **ACT-20260825-002**, the hiring plan is now explicitly derived from workstream demand. The operating sequence is:

**Workstream → Required capability → Required FTE → Current coverage → Capacity gap → TBH role / staffing response.**

The TBH Registry remains the canonical register of roles to be hired. ACT-20260825-002 is the evidence-building workstream that validates how many FTE are required, which roles are justified, what they block and how they should be prioritised. This mapping remains a work in progress through **30 September 2026**.

## Registry

| ID | Role Title | Organisation | Reports To | Scope & Responsibilities | Blocks (Actions/Initiatives) | Priority | Status | Target Fill Date | Notes |
|----|-----------|-------------|------------|--------------------------|---------------------------|----------|--------|-----------------|-------|
| TBH-001 | Project Manager — Cyber Security Practice | Aras Integrasi Sdn Bhd | Hadri (Practice COO) | Execution responsibility for POC document sections (Use Cases, Architecture, Data/Integration, Test Strategy/Scenarios) within the Cyber Security Practice. Operational coordination of POC execution, document section delivery, technical deliverable tracking. | ACT-20260820-004 (CRITICAL — VoronCitadel POC document, delivered Aug 24). ACT-20260824-004 (HIGH — Bursa POC project plan). Future POC executions through CSM channel. | 🔴 CRITICAL | Open — JD v3.1 finalised for management justification, approval target end-October 2026 | Jan 5-19, 2027 start window | **Reports to:** Hadri (Practice COO), matrix to DAF. **Interim Owner: DAF (by default).** **2026-09-04 update:** JD v3.1 finalised (commit pending). 19 sections, operational detail (cadences, escalation, POC lifecycle, templates). Salary band confirmed RM 10-15K. Document reframed as internal management justification — not for external posting. Approval target end-October 2026 → Nov posting → Jan 2027 start. **Interim period: ~14-16 weeks (Sep 4 – Jan 2027).** This is a material extension from the original 2-3 week assumption. Interim delegation: POC tracking→DAF, tech review→Hadri, POC env→Fuad/Syahir, stakeholder→Amelia, NDA/legal→DAF, risk register→Ember. Interim plan sustainability is a critical risk. |
| TBH-002 | Head of Engineering — Cyber Security Practice | Aras Integrasi Sdn Bhd | Fuad (Practice CTO) | Engineering leadership for VoronCitadel, GovSec-TIP, and chain:SENTRY. Owns technical delivery, architecture implementation, engineering standards, and team coordination across all three flagship products. Leads POC environment engineering, feature development, and production hardening. | RSK-20260820-003 (CRITICAL — No HoE, blocks POC scaling). ACT-20260820-007 (CRITICAL — Hire HoE). All Phase 0 TPRM development under INIT-20260824-001. All POC scaling under INIT-20260820-003. | 🔴 CRITICAL | Open — hiring approval gates October 2026 | ~Jan 2027 start | **Reports to:** Fuad (Practice CTO). **Interim Owner: Fuad (at ~0.3 FTE — critical capacity constraint).** **2026-08-29 update:** Hiring approval October 2026. Operational hiring post-October. HoE in seat ~Jan 2027. No engineering relief before January. SPOF (Fuad + Hadri) persists through Q4 2026. **DAF directive: discipline is the strategy through January.** No new scope on Fuad/Hadri. Scope discipline, action register hygiene, Syahir ramp-up, and execution diligence are the only mitigations. **2026-09-11 update:** Fuad career direction conversation CONDUCTED (ACT-20260829-002 completed, DEC-20260911-001) — Fuad retained as technical leadership (delegation-based scaling), so the external HoE candidate profile becomes the more likely path. ESF-20260829-002 activated. Hiring decision itself still pending; October hiring approval continues to gate operational hiring. |
| TBH-003 | chain:SENTRY Pilot Operations Unit (7-FTE coverage model) | Aras Integrasi Sdn Bhd | Hadri (product owner, Op Plan governance model) | Per adopted Op Plan v1.1 §2.3: Product/programme 1.0 · Engineering leadership 1.0 · Application engineering 1.5 · Data/intelligence engineering 1.0 · Frontend/UX 0.5 · QA/release verification 1.0 · Security/privacy/continuity 0.5 · Platform ops/support 0.5. Role breakdown, per-role JDs and salary bands defined in Hadri's Overall JD pack (ACT-20260908-002, due Sep 16). | DEC-20260908-001 (CRITICAL — capacity model adoption). Phase 0–1B gates (Op Plan §7.4/§7.5). Track C pilot chain (C2–C5). RSK-20260829-001 (Syahir triple-hat — structural mitigation). | 🔴 CRITICAL | Open — DEC-20260908-001 adopted Op Plan model 2026-09-08; JD pack due Sep 16 | Hiring sequence per Op Plan §2.7: Lead Engineer → Data Engineer → Designer/Frontend → fractional DPO → CISO contractor → ring-fenced QA/ops; earliest seats realistically mid-Oct–Nov 2026 | **2026-09-08:** DEC-20260908-001 amends the no-hire-before-Jan-2027 directive for chain:SENTRY product-operations roles (TBH-001/TBH-002 unchanged). CC-01 envelope: MYR 100,000–150,000/month (Phase 0–1). Interim capacity remains Fuad + Syahir until seats fill — C2 (Sep 10), Sep 14 trajectory gate and Sep 15 kill date are NOT re-baselined by the hiring decision. |

---

## Rules

1. **Every TBH role must have a named blocking action.** If nothing is blocked, the role isn't urgent enough for this registry.
2. **Priority reflects the highest-priority action blocked.** If a TBH role blocks a CRITICAL action, the role is CRITICAL.
3. **Review cadence:** Weekly, aligned with Cognitive Loop Review (Monday 10:30 AM UTC+8). Each TBH entry reviewed for: still blocked? Still relevant? Any candidates? Any workaround in place?
4. **Resolution:** When a role is filled, move entry to "Resolved" section with appointment date and named individual. Do not delete — maintain audit trail.
5. **Workaround tracking:** If a blocking action is reassigned to an existing team member as interim, note the workaround and the interim owner. The TBH entry stays open until the role is permanently filled.
6. **Escalation:** A TBH role blocking a CRITICAL action for more than 2 weeks without a workaround triggers escalation to DAF for interim assignment or action reassignment.
7. **FTE evidence rule (25 Aug 2026):** New or materially revised TBH roles should be traceable to workstream-to-FTE evidence from ACT-20260825-002 rather than headcount assumptions alone.

---

## Resolved

| ID | Role Title | Appointed To | Date | Notes |
|----|-----------|-------------|------|-------|
| — | — | — | — | No resolved entries yet |

---

*This registry is the structural complement to the Portfolio Register. The Portfolio Register tracks what programmes exist; this registry tracks what organisational capacity is missing to execute them.*
