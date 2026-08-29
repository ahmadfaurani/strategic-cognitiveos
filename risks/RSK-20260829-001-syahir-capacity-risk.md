---
id: RSK-20260829-001
record_type: risk
title: "Syahir Capacity Risk — Triple-Hatted with Competing September Deadlines"
created_at: 2026-08-29T13:22:00+00:00
updated_at: 2026-08-29T13:22:00+00:00
owner: hadri
status: active
priority: high
risk_category: operational
sensitivity: internal
lifecycle_state: canonical
confidence: high
tags:
  - domain/organisational-capability
  - domain/cybersecurity-productisation
  - domain/quality-assurance
  - framework/engineered-success
  - priority/high
  - person/syahir
  - product/chainsentry
  - milestone/cyberdsa-2026
source:
  type: cognitive-loop
  reference: "INT-20260829-004, DEC-20260829-004"
summary: "Syahir assigned 3 roles (QC Engineer + POC Engineer + chain:SENTRY Engineering Owner) with competing September deadlines. QC deadline Sep 28 is hard-gated. chain:SENTRY Phase 0 kill date Sep 15. No priority sequencing from operational owner. Same structural pattern that created Hadri SPOF — available capacity attracts work."
strategic_significance: "Syahir is the practice's only engineering relief vector through January. If capacity is not sequenced, all 3 roles underdeliver."
mission_alignment:
  - cybersecurity-productisation
  - organisational-capability-building
  - cyberdsa-2026
related_records:
  - DEC-20260829-004
  - DEC-20260818-007
  - DEC-20260818-009
  - RSK-20260820-005
  - RSK-20260820-006
  - RSK-20260820-007
  - STK-20260811-001
  - INT-20260829-004
  - CONV-20260829-001
probability: high
impact: high
mitigation: "Hadri (operational) sequences Syahir's deliverables. Fuad (tactical) tracks execution. QC is hard-gated at Sep 28. chain:SENTRY Phase 0 kill date Sep 15 — if Syahir can't start by Sep 14, de-scope from CyberDSA."
---

# Risk: Syahir Capacity — Triple-Hatted with Competing Deadlines

**Identified:** 2026-08-29
**Source:** INT-20260829-004 Cognitive Loop on Hadri Role Restructure
**Owner:** Hadri (operational sequencing) / Fuad (tactical tracking)
**Status:** Active

## Description

Syahir has been assigned 3 roles over 11 days:
1. **QC Engineer** (Aug 18, DEC-20260818-009) — deadline Sep 28
2. **POC Engineer** (Aug 18, DEC-20260818-007) — ongoing, no ramp-up evidence
3. **chain:SENTRY Engineering Owner** (Aug 29, DEC-20260829-004) — 3 Critical Phase 0 blockers, kill date Sep 15

All three compete for Syahir's time in September. QC has a hard deadline (Sep 28, T-7 CyberDSA). chain:SENTRY Phase 0 has a proposed kill date (Sep 15). POC Engineer ramp-up is ongoing. No priority sequencing has been issued by the operational owner (Hadri).

## Structural Pattern

This is the same pattern that created the Hadri SPOF: available capacity attracts work. Syahir is the only available engineering resource, so work flows to him. Without explicit sequencing, context-switching degrades all three roles.

## Capacity Conflict Matrix

| Role | Deadline | Effort | Window | Priority |
|------|----------|--------|--------|----------|
| QC Engineer | Sep 28 (hard) | 2-3 weeks prep | Sep 7 – Sep 28 | TBD — Hadri to sequence |
| POC Engineer | Ongoing | Ramp-up (unknown) | Sep – Oct | TBD — Hadri to sequence |
| chain:SENTRY Phase 0 | Sep 15 (kill date) | 2-3 weeks if briefed | Sep 5 – Sep 28 | TBD — Hadri to sequence |

## Mitigation

- **Operational:** Hadri sequences deliverables — QC first (hard-gated), chain:SENTRY after QC is on track
- **Tactical:** Fuad tracks ramp-up progress and technical execution
- **Kill date:** If Syahir cannot start chain:SENTRY Phase 0 by Sep 14, chain:SENTRY is de-scoped from CyberDSA demo
- **Strategic:** DAF decides if 3 roles are sustainable or if one de-scopes
