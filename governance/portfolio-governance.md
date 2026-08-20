---
id: GOV-PORTFOLIO-GOVERNANCE-001
record_type: document
title: Portfolio Governance
created_at: 2026-08-04 00:00:00+00:00
updated_at: 2026-08-19 16:00:00+00:00
owner: DAF
status: active
priority: high
sensitivity: internal
lifecycle_state: canonical
confidence: high
tags:
- domain/portfolio-governance
- domain/governance
source:
  type: direct
  reference: DAF authority
summary: Governance reference document for Portfolio Governance.
strategic_significance: Governs CognitiveOS operational standards and procedures.
mission_alignment:
- sovereign-ai
- intelligence-enablement
related_records:
- GOV-INTAKE-SOP-001
document_type: reference
file_path: governance/portfolio-governance.md
version: '1.0'
author: DAF
---

# Portfolio Governance

## Portfolio Tiers

Every initiative must be classified according to its actual maturity and strategic value. No initiative should be treated as active without an assigned portfolio classification.

| Tier | Tag | Criteria | Governance | Review |
|------|-----|----------|-----------|--------|
| Flagship | `portfolio/flagship` | Strong sponsor, clear outcome, credible owner, sufficient readiness, defined pilot, material value | High | Weekly |
| Incubation | `portfolio/incubation` | Strong potential but incomplete sponsor/budget/ownership/maturity. Bounded validation with proof point and review date | Medium | Bi-weekly |
| Watch List | `portfolio/watch-list` | Strategically relevant, no immediate sponsor/budget/capacity. Maintained for intelligence | Low | Monthly |
| Operational | `portfolio/operational` | Approved execution activity, assigned owner, defined output, required delivery date, existing obligation | Medium | Weekly |

## Tier Transition

- **Watch List → Incubation**: When a sponsor or proof point emerges.
- **Incubation → Flagship**: When sponsor, delivery owner, readiness, and pilot pathway are all confirmed.
- **Flagship → Operational**: When the initiative moves from strategic development to routine delivery.
- **Any tier → Watch List**: When sponsor or capacity is lost but strategic relevance remains.
- **Any tier → Archived**: When the initiative is completed, cancelled, or no longer strategically relevant.

## Readiness Gating

External commitments must not exceed the verified readiness level:

| Readiness | External Commitment Allowed |
|-----------|------------------------------|
| concept | No |
| framed | No |
| prototype | No |
| demo-ready | Demonstration only |
| pilot-ready | Pilot scope only |
| delivery-ready | Yes |
| commercial-ready | Yes |
| scale-ready | Yes |

Violations of this gate must be flagged as risks.
