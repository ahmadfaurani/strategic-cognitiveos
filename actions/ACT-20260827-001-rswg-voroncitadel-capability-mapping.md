---
id: ACT-20260827-001
record_type: action
title: "Map RSWG 9 Control Domains to VoronCitadel Capability Matrix"
created_at: 2026-08-27T02:54:00+00:00
updated_at: 2026-08-27T02:54:00+00:00
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
tags:
- domain/cybersecurity-productisation
- domain/compliance
- domain/security-architecture
- sector/financial
source:
  type: internal
  reference: "INT-20260827-001 — RSWG strategic intelligence assessment"
summary: "Create a detailed mapping of RSWG's 9 control domains (§2.1-§2.9) to VoronCitadel's existing capability matrix. For each domain: (1) what VoronCitadel addresses natively, (2) what requires extension/configuration, (3) what requires integration with external tools, (4) what is out of scope. This mapping becomes the foundation for the POC document update (ACT-20260827-002) and the commercial pipeline positioning."
strategic_significance: "Without this mapping, VoronCitadel's RSWG alignment is asserted, not demonstrated. The mapping converts regulatory intelligence into actionable product positioning."
mission_alignment:
- productisation
related_records:
- INT-20260827-001
- DOC-20260827-001
- ACT-20260827-002
- INIT-20260824-001
required_output: "Capability matrix document — RSWG domain → VoronCitadel coverage (native/extension/integration/out-of-scope)"
deadline: "2026-08-29"
dependency:
- "DOC-20260827-001 (RSWG paper) — received ✅"
- "VoronCitadel feature documentation — available"
attention_level: high
related_initiative:
- INIT-20260824-001
related_stakeholder:
- STK-20260813-008
---

# Action

Map RSWG 9 control domains to VoronCitadel capability matrix.

## Required Output

A capability matrix document with 4 columns per RSWG domain:
1. **Native** — VoronCitadel addresses this directly out of the box
2. **Extension** — VoronCitadel can address with configuration/customization
3. **Integration** — Requires integration with external tool (name the tool)
4. **Out of Scope** — VoronCitadel does not address this

Plus: Gap analysis identifying the 3 highest-value extensions needed for RSWG compliance positioning.

## Owner

DAF (strategic), Fuad (technical validation)

## Assignee

DAF with Fuad technical input

## Completion Evidence

Mapping document committed to CognitiveOS, reviewed by Fuad for technical accuracy.

## Dependencies

- DOC-20260827-001 (RSWG paper) — ✅ received
- VoronCitadel feature documentation — available

## Related Records

- INT-20260827-001 — Intelligence assessment
- DOC-20260827-001 — Source document
- ACT-20260827-002 — POC document update (depends on this)
- INIT-20260824-001 — Bursa POC
