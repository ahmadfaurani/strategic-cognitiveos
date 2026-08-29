---
id: DEC-20260829-004
record_type: decision
title: "chain:SENTRY Engineering Development Reassigned to Syahir — Hadri Retains Roadmap"
created_at: 2026-08-29T12:36:00+00:00
updated_at: 2026-08-29T12:36:00+00:00
owner: faurani-jaafar
decision_type: structural
status: active
priority: critical
sensitivity: internal
decision_date: '2026-08-29'
decision_owner: faurani-jaafar
context: 'chain:SENTRY has 3 Critical Phase 0 blockers. Hadri has 0 capacity to address them. Syahir is available engineering resource in the org. Hadri created chain:SENTRY and owns architectural vision.'
decision: 'chain:SENTRY engineering development moves to Syahir as engineering owner. Hadri retains roadmap ownership only — product direction, feature prioritization, milestone definition.'
rationale: 'Unblocks chain:SENTRY Phase 0 without external hiring. Hadri retains product vision. Syahir is the available engineering capacity. Splits product ownership: roadmap (Hadri) vs engineering (Syahir).'
tags:
  - domain/cybersecurity-productisation
  - domain/organisational-capability
  - person/hadri
  - person/syahir
  - product/chainsentry
  - lifecycle/active
related_records:
  - STK-20260803-007
  - STK-20260811-001
  - RSK-20260820-005
  - RSK-20260820-006
  - RSK-20260820-007
  - DEC-20260820-010
  - DEC-20260829-002
---

# Decision: chain:SENTRY Engineering to Syahir — Hadri Retains Roadmap

**Date:** 2026-08-29
**Authority:** DAF
**Status:** DECIDED

## Decision

1. **chain:SENTRY engineering development** moves to **Syahir** as engineering owner.
2. **Hadri retains roadmap ownership** — product direction, feature prioritization, milestone definition.
3. This splits product ownership: Hadri = roadmap (what/when), Syahir = engineering (how/build).

## Rationale

Hadri has no capacity to address the 3 Critical Phase 0 blockers (RSK-20260820-005/006/007). Syahir is already in the org, already delegated as POC Engineer (DEC-20260818-007), and is the available engineering resource. Moving engineering execution to Syahir unblocks chain:SENTRY without requiring external hiring.

Hadri created chain:SENTRY and owns the architectural vision. Retaining roadmap ownership ensures product coherence. But engineering execution — closing Phase 0 blockers, deployment, regression fixes — transitions to Syahir.

## Syahir's Expanded Scope

**Previous:** QC Engineer + POC Engineer
**New:** QC Engineer + POC Engineer + chain:SENTRY Engineering Owner

Syahir now owns:
- chain:SENTRY Phase 0 blocker resolution (credential rotation, regression fix, commit/deploy)
- chain:SENTRY deployment and maintenance
- chain:SENTRY engineering development under Hadri's roadmap direction

Syahir reports to Fuad for technical ramp-up (DEC-20260818-007) and to Hadri for chain:SENTRY roadmap alignment.

## Hadri's Retained Scope

- chain:SENTRY roadmap ownership (feature prioritization, milestone definition, phase gates)
- chain:SENTRY product specification (v4.1 MVP Spec, Roadmap v2.0)
- chain:SENTRY stakeholder representation (CyberDSA demo positioning, product narrative)

## Impact on Phase 0 Blockers

| Blocker | Risk ID | Previous Owner | New Owner |
|---------|--------|----------------|-----------|
| Credential rotation (4 exposed) | RSK-20260820-005 | Hadri | Syahir |
| Address-security regression | RSK-20260820-006 | Hadri | Syahir |
| Deployment not describable (43 uncommitted mods, 29 commits behind) | RSK-20260820-007 | Hadri | Syahir |

**Note:** Syahir needs ramp-up time. Fuad is responsible for Syahir's technical ramp-up (DEC-20260818-007). The Phase 0 blockers require immediate attention — Syahir should be briefed on chain:SENTRY architecture and blockers as a priority action.

## Risk Implications

- **RSK-20260820-005/006/007:** Ownership transfers to Syahir. Timeline for resolution depends on ramp-up speed.
- **RSK-20260804-001 (Hadri SPOF):** Partially mitigated — engineering execution distributed.
- **New risk:** Syahir capacity — now carrying QC + POC + chain:SENTRY engineering. This needs monitoring.
