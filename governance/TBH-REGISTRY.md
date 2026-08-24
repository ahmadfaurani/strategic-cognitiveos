---
id: GOV-TBH-REGISTRY-001
record_type: document
title: TBH Registry — Roles To Be Hired
created_at: 2026-08-20 08:32:00+00:00
updated_at: 2026-08-20 11:14:00+00:00
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
  reference: DAF authority — created per directive 2026-08-20 08:32 UTC
summary: Registry of roles that are identified as required but not yet hired. Each
  entry tracks the role, its scope, what it blocks, and hiring status.
strategic_significance: Prevents portfolio governance gaps from remaining invisible.
  A TBH role that blocks critical actions is a structural risk — this registry makes
  it visible and trackable.
mission_alignment:
- organisational-capability
- portfolio-governance
related_records:
- GOV-PORTFOLIO-REGISTER-001
- SOP-COGNITIVE-LOOP-REVIEW-001
document_type: reference
file_path: governance/TBH-REGISTRY.md
version: '1.1'
author: DAF
---

# TBH Registry — Roles To Be Hired

**Created:** 2026-08-20 | **Authority:** DAF | **Review cadence:** Weekly (aligned with Cognitive Loop Review, Monday 10:30 AM UTC+8)

---

## Purpose

Every TBH role that blocks a portfolio action is a structural risk. This registry makes that risk visible, trackable, and enforceable. If a role is TBH and it blocks a CRITICAL action, it appears here until filled or the action is reassigned.

## Registry

| ID | Role Title | Organisation | Reports To | Scope & Responsibilities | Blocks (Actions/Initiatives) | Priority | Status | Target Fill Date | Notes |
|----|-----------|-------------|------------|--------------------------|---------------------------|----------|--------|-----------------|-------|
| TBH-001 | Project Manager — Cyber Security Practice | Aras Integrasi Sdn Bhd | Hadri (Practice COO) | Execution responsibility for POC document sections (Use Cases, Architecture, Data/Integration, Test Strategy/Scenarios) within the Cyber Security Practice. Operational coordination of POC execution, document section delivery, technical deliverable tracking. | ACT-20260820-004 (CRITICAL — VoronCitadel POC document, due Aug 24 10am MYT). ACT-20260824-004 (HIGH — Bursa POC project plan, deliverable tracking, weekly status reporting). Future POC executions through CSM channel. | 🔴 CRITICAL | Open — building the team (DAF directive 08:58 UTC) | In progress — team building underway | **Reports to:** Hadri (Practice COO). **Interim Owner: DAF (by default).** Identified 2026-08-20 when DAF corrected Hadri's non-ownership of document sections. Role is a headcount under Hadri's org. Athena authored document; Fuad reviewing; DAF approving; this role executes. DAF confirmed 08:58 UTC: "We are building the team. It's a process that we need to bear with." No pressure on fill date — registry tracks, weekly review monitors. **2026-08-24 update:** ACT-20260824-004 added — TBH-001 assigned to coordinate Bursa POC project plan (scope, milestones, owners, dependencies, risks), track ACT-20260824-001/002/003 as deliverables, run weekly status checks, surface RSK-20260824-001 timeline risk early, produce weekly POC status reports for DAF and Hadri. Interim owner DAF until role filled. |
| TBH-002 | Head of Engineering — Cyber Security Practice | Aras Integrasi Sdn Bhd | Fuad (Practice CTO) | Engineering leadership for VoronCitadel, GovSec-TIP, and chain:SENTRY. Owns technical delivery, architecture implementation, engineering standards, and team coordination across all three flagship products. Leads POC environment engineering, feature development, and production hardening. | RSK-20260820-003 (CRITICAL — No HoE, blocks POC scaling). ACT-20260820-007 (CRITICAL — Hire HoE, RM 18,888/mo). ACT-20260820-008 (CSE hire). ACT-20260820-009 (Junior Backend hire). All Phase 0 TPRM development under INIT-20260824-001. All POC scaling under INIT-20260820-003. | 🔴 CRITICAL | Open — hiring in progress (ACT-20260820-007) | ASAP — Bursa POC 4-month timeline demands it | **Reports to:** Fuad (Practice CTO). **Interim Owner: Fuad (at ~0.3 FTE — critical capacity constraint).** Identified 2026-08-20 in RSK-20260820-003 when POC Mode activation revealed current engineering capacity cannot support 6-7 POCs + 3 paying customers. Teras infrastructure (DEC-20260820-008) reduces FTE need from 5 to 3 but HoE remains the gating hire. ACT-20260821-008 accelerates hiring: post roles this week, shortlist by Sep 1, interview Sep 1-5. **2026-08-24 escalation:** Cognitive Loop Review (ASSESS-20260824-001) identified HoE absence as #2 strategic gap — 0.3 FTE cannot deliver TPRM enhancement + federated compliance architecture in 4 months. TBH-002 registered per ACT-20260824-006 directive. |

---

## Rules

1. **Every TBH role must have a named blocking action.** If nothing is blocked, the role isn't urgent enough for this registry.
2. **Priority reflects the highest-priority action blocked.** If a TBH role blocks a CRITICAL action, the role is CRITICAL.
3. **Review cadence:** Weekly, aligned with Cognitive Loop Review (Monday 10:30 AM UTC+8). Each TBH entry reviewed for: still blocked? Still relevant? Any candidates? Any workaround in place?
4. **Resolution:** When a role is filled, move entry to "Resolved" section with appointment date and named individual. Do not delete — maintain audit trail.
5. **Workaround tracking:** If a blocking action is reassigned to an existing team member as interim, note the workaround and the interim owner. The TBH entry stays open until the role is permanently filled.
6. **Escalation:** A TBH role blocking a CRITICAL action for more than 2 weeks without a workaround triggers escalation to DAF for interim assignment or action reassignment.

---

## Resolved

| ID | Role Title | Appointed To | Date | Notes |
|----|-----------|-------------|------|-------|
| — | — | — | — | No resolved entries yet |

---

*This registry is the structural complement to the Portfolio Register. The Portfolio Register tracks what programmes exist; this registry tracks what organisational capacity is missing to execute them.*
