---
id: DEC-20260827-002
record_type: decision
title: CyberDSA 2026 Stakeholder Dependency Chain Reordered — Operational Before Technical, Marketing After Technical
created_at: 2026-08-27T08:00:00+00:00
updated_at: 2026-08-27T08:00:00+00:00
owner: faurani-jaafar
status: active
priority: high
sensitivity: confidential
lifecycle_state: canonical
confidence: high
tags:
  - domain/csm-partnership
  - domain/cyberdsa-2026
  - domain/stakeholder-engagement
  - domain/strategic-communications
  - lifecycle/canonical
  - priority/high
source:
  type: document
  reference: DOC-20260827-003 (V1.1 framework, DAF-authored, 23 August 2026)
summary: "DAF reordered the CyberDSA 2026 stakeholder dependency chain in V1.1 of the Activation Framework. V1.0 sequence (Azrul, Zulfeka, Bala, Wan Roshaimi, Zaharudin, Dr. Megat) replaced with V1.1 sequence (Azrul, Zulfeka, Zaharudin, Wan Roshaimi, Bala, Dr. Megat). Operational coordination now precedes technical validation; marketing/media now follows technical clearance."
strategic_significance: "Enables technical validation against real operating context rather than in isolation. Prevents marketing from making claims before technical defensibility is established. Aligns with Wan Roshaimi protocol v1.2 (integration-backed candidate, not jointly built). Gates 3 and 5 swapped — Zaharudin now Gate 3, Bala now Gate 5."
decision_type: strategic
decided_by: faurani-jaafar
decision_date: '2026-08-23'
decision_owner: faurani-jaafar
context: "CyberDSA 2026 stakeholder activation framework V1.0 (DOC-20260819-001) had marketing/media (Bala) at Gate 3 and operational coordination (Zaharudin) at Gate 5. This meant technical validation occurred before operating conditions were defined, and marketing activated before technical clearance."
decision: "Reorder dependency chain to Azrul to Zulfeka to Zaharudin to Wan Roshaimi to Bala to Dr. Megat. Operational coordination now Gate 3 (before technical), marketing/media now Gate 5 (after technical). Wan Roshaimi validates against operating conditions defined by Zaharudin."
rationale: "Operating conditions must be defined before technical validation — validate against real context, not in a vacuum. Marketing must follow technical clearance to prevent premature or undefended public claims. Aligns with Wan Roshaimi protocol v1.2."
effective_date: '2026-08-23'
impact: |
  Gate 3: Bala (Marketing & Media) → Zaharudin (Operational Coordination)
  Gate 4: Wan Roshaimi (Technical) — unchanged position, now follows Zaharudin
  Gate 5: Zaharudin (Operational) → Bala (Marketing & Media)
  Rationale: Validate technology against real operating conditions; prevent premature marketing claims.
rationale: |
  1. Operational coordination must define operating conditions BEFORE technical validation — validate against real context, not in a vacuum.
  2. Marketing/media must follow technical clearance — public claims must trace back to validated technical position.
  3. Aligns with Wan Roshaimi protocol v1.2 — "integration-backed candidate" not "jointly built". Aras owns POC delivery; CSM validates strategy/governance.
affected_stakeholders:
  - STK-20260804-011 (Zaharudin — Gate 5 → Gate 3)
  - STK-20260812-001 (Wan Roshaimi — Gate 4, now follows Zaharudin)
  - STK-20260817-001 (Bala — Gate 3 → Gate 5)
related_records:
  - DOC-20260819-001
  - DOC-20260827-003
  - ACT-20260827-009
  - STK-20260804-011
  - STK-20260812-001
  - STK-20260817-001
  - INIT-20260813-006
---

# DEC-20260827-002 — Stakeholder Dependency Chain Reordered

## Decision

The CyberDSA 2026 stakeholder dependency chain is reordered in V1.1 of the Activation Framework.

**V1.0 (19 August):** Azrul → Zulfeka → Bala → Wan Roshaimi → Zaharudin → Dr. Megat
**V1.1 (23 August):** Azrul → Zulfeka → Zaharudin → Wan Roshaimi → Bala → Dr. Megat

## What Changed

| Gate | V1.0 Lead | V1.1 Lead | Net Change |
|------|-----------|-----------|-----------|
| Gate 3 | Bala (Marketing & Media) | Zaharudin (Operational Coordination) | Swapped to Gate 3 |
| Gate 4 | Wan Roshaimi (Technical) | Wan Roshaimi (Technical) | Same gate, now follows Zaharudin |
| Gate 5 | Zaharudin (Operational) | Bala (Marketing & Media) | Swapped to Gate 5 |

## Rationale

1. **Operational before technical:** Operating conditions (access, coordination, implementation touchpoints) must be defined before technical validation. Wan Roshaimi validates against real operating context established by Zaharudin, not in isolation.

2. **Marketing after technical:** Public claims must trace back to a validated technical position. Bala's marketing/media activation follows Wan Roshaimi's technical clearance to prevent premature or undefended claims.

3. **Wan Roshaimi protocol alignment:** V1.1 explicitly states "Aras will support and execute the POC activity; CSM technical leadership is not being asked to provide POC delivery resources." This aligns with the Wan Roshaimi protocol v1.2 (integration-backed candidate, not jointly built).

## Impact

- All stakeholder records referencing gate numbers must be updated
- Existing action records (ACT-20260819-003 through ACT-20260819-009) that reference the old gate sequence need review
- The activation wave plan is restructured to match the new gate order
- Risk #7 (activation sequence bypass) now explicitly lists the correct chain order

## CVS Classification

- **Source Level:** L1 (DAF-authored strategic framework document)
- **Claim Tier:** T2 [SOURCE-BACKED]
- **Confidence Score:** 7/10 (Authority 2, Traceability 2, Recency 2, Consistency 1, Completeness 0)
- **Rule 6:** AI-capped at T2, score 7.
