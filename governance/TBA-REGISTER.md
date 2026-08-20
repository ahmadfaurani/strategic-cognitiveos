---
id: GOV-TBA-REGISTER-001
record_type: register
title: "TBA Register — Roles To Be Appointed"
created_at: 2026-08-20T08:32:00+00:00
updated_at: 2026-08-20T08:32:00+00:00
owner: DAF
status: active
priority: high
sensitivity: internal
lifecycle_state: active
confidence: high
tags:
  - domain/governance
  - domain/portfolio-governance
  - domain/organisational-design
source:
  type: direct
  reference: "DAF authority — created per directive 2026-08-20 08:32 UTC"
summary: "Register of roles that are identified as required but not yet filled. Each entry tracks the role, its scope, what it blocks, and hiring/appointment status."
strategic_significance: "Prevents portfolio governance gaps from remaining invisible. A TBA role that blocks critical actions is a structural risk — this register makes it visible and trackable."
mission_alignment:
  - organisational-capability
  - portfolio-governance
related_records:
  - GOV-PORTFOLIO-REGISTER-001
  - SOP-COGNITIVE-LOOP-REVIEW-001
document_type: register
file_path: "governance/TBA-REGISTER.md"
version: "1.0"
author: DAF
---

# TBA Register — Roles To Be Appointed

**Created:** 2026-08-20 | **Authority:** DAF | **Review cadence:** Weekly (aligned with Cognitive Loop Review, Monday 10:30 AM UTC+8)

---

## Purpose

Every TBA role that blocks a portfolio action is a structural risk. This register makes that risk visible, trackable, and enforceable. If a role is TBA and it blocks a CRITICAL action, it appears here until filled or the action is reassigned.

## Register

| ID | Role Title | Organisation | Reports To | Scope & Responsibilities | Blocks (Actions/Initiatives) | Priority | Status | Target Fill Date | Notes |
|----|-----------|-------------|------------|--------------------------|---------------------------|----------|--------|-----------------|-------|
| TBA-001 | Project Manager — Cyber Security Practice | Aras Integrasi Sdn Bhd | DAF (Director, Cyber Security Practice) | Execution responsibility for POC document sections (Use Cases, Architecture, Data/Integration, Test Strategy/Scenarios) within the Cyber Security Practice. Operational coordination of POC execution, document section delivery, technical deliverable tracking. | ACT-20260820-004 (CRITICAL — VoronCitadel POC document, due Aug 24 10am MYT). Future POC executions through CSM channel. | 🔴 CRITICAL | Open — building the team (DAF directive 08:58 UTC) | In progress — team building underway | **Interim Owner: DAF (by default).** Identified 2026-08-20 when DAF corrected Hadri's non-ownership of document sections. Role exists within Cyber Security Practice org structure. Athena authored document; Fuad reviewing; DAF approving; this role executes. DAF confirmed 08:58 UTC: "We are building the team. It's a process that we need to bear with." No pressure on fill date — register tracks, weekly review monitors. |

---

## Rules

1. **Every TBA role must have a named blocking action.** If nothing is blocked, the role isn't urgent enough for this register.
2. **Priority reflects the highest-priority action blocked.** If a TBA role blocks a CRITICAL action, the role is CRITICAL.
3. **Review cadence:** Weekly, aligned with Cognitive Loop Review (Monday 10:30 AM UTC+8). Each TBA entry reviewed for: still blocked? Still relevant? Any candidates? Any workaround in place?
4. **Resolution:** When a role is filled, move entry to "Resolved" section with appointment date and named individual. Do not delete — maintain audit trail.
5. **Workaround tracking:** If a blocking action is reassigned to an existing team member as interim, note the workaround and the interim owner. The TBA entry stays open until the role is permanently filled.
6. **Escalation:** A TBA role blocking a CRITICAL action for more than 2 weeks without a workaround triggers escalation to DAF for interim assignment or action reassignment.

---

## Resolved

| ID | Role Title | Appointed To | Date | Notes |
|----|-----------|-------------|------|-------|
| — | — | — | — | No resolved entries yet |

---

*This register is the structural complement to the Portfolio Register. The Portfolio Register tracks what programmes exist; this register tracks what organisational capacity is missing to execute them.*
