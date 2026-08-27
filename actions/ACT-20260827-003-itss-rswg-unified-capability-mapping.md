---
id: ACT-20260827-003
record_type: action
title: "Extend Capability Mapping to Include ITSS 12 Domains — Unified ITSS × RSWG × VoronCitadel Matrix"
created_at: 2026-08-27T03:16:00+00:00
updated_at: 2026-08-27T03:16:00+00:00
owner: faurani-jaafar
assignee: faurani-jaafar
co_owner:
- Ahmad Fuad
status: draft
priority: critical
sensitivity: confidential
classification: strategic
lifecycle_state: candidate
confidence: high
action_type: analysis
tags:
- domain/cybersecurity-productisation
- domain/compliance
- domain/security-architecture
- sector/financial
source:
  type: internal
  reference: "INT-20260827-002 — ITSS × RSWG combined framework intelligence"
summary: "Extend the RSWG capability mapping (ACT-20260827-001) to include the ITSS 12 domains. Create a unified matrix mapping ITSS (existing floor) + RSWG (enhanced ceiling) to VoronCitadel capabilities. This dual-layer mapping is the foundation for the dual value proposition: VoronCitadel addresses current ITSS compliance AND future RSWG enhancement. Also verify the lineage of the 61 Bursa Cybersecurity Controls already in VoronCitadel's production database against the ITSS 12 domains."
strategic_significance: "The unified matrix converts two L1 regulatory documents into a single actionable product positioning tool. Without this, VoronCitadel's compliance alignment is asserted against one layer only. With this, it's demonstrated against the complete two-layer framework."
mission_alignment:
- productisation
related_records:
- INT-20260827-002
- INT-20260827-001
- DOC-20260827-001
- DOC-20260827-002
- ACT-20260827-001
- ACT-20260827-002
- INIT-20260824-001
required_output: "Unified capability matrix: ITSS 12 domains + RSWG 9 domains → VoronCitadel coverage (native/extension/integration/out-of-scope). Plus: 61-control lineage verification."
deadline: "2026-08-29"
dependency:
- "ACT-20260827-001 (RSWG mapping) — should be done first or merged with this"
- "DOC-20260827-001 (RSWG paper) — ✅ received"
- "DOC-20260827-002 (ITSS) — ✅ received"
- "VoronCitadel 61-control database — available (verify lineage)"
attention_level: high
related_initiative:
- INIT-20260824-001
related_stakeholder:
- STK-20260813-008
---

# Action

Create unified ITSS × RSWG × VoronCitadel capability matrix.

## Required Output

1. **ITSS 12 domains → VoronCitadel coverage** (native/extension/integration/out-of-scope)
2. **RSWG 9 domains → VoronCitadel coverage** (from ACT-20260827-001)
3. **Cross-layer mapping:** Where ITSS and RSWG overlap, note the enhanced requirements
4. **Gap analysis:** Highest-value extensions needed for dual-layer compliance
5. **61-control lineage verification:** Map the 61 Bursa Cybersecurity Controls in VoronCitadel's database to ITSS domains

## Owner

DAF (strategic), Fuad (technical validation)

## Assignee

DAF with Fuad technical input

## Completion Evidence

Unified matrix document committed to CognitiveOS, reviewed by Fuad for technical accuracy. 61-control lineage verified or documented as unverified.

## Dependencies

- ACT-20260827-001 (RSWG mapping) — should be done first or merged
- DOC-20260827-001 (RSWG paper) — ✅ received
- DOC-20260827-002 (ITSS) — ✅ received
- VoronCitadel 61-control database — available

## Related Records

- INT-20260827-002 — Combined framework intelligence
- INT-20260827-001 — RSWG intelligence
- DOC-20260827-001 — RSWG paper
- DOC-20260827-002 — ITSS directive
- ACT-20260827-001 — RSWG mapping (predecessor/merge candidate)
- ACT-20260827-002 — POC document update (depends on this)
- INIT-20260824-001 — Bursa POC
