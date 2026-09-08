# Taxonomy Integrity Audit — 2026-09-08 (methodology v1.2-20260908)

- **repository_commit:** `80ec91e1dd3174ac875ca6ced0322447d98c9c85`
- **audit_timestamp:** 2026-09-08T15:31:30+00:00
- **tool:** audit_taxonomy_v2.py (sha256:508c945035fc0b13, jsonschema 4.23.0)
- **records_scanned:** 787 typed records (17 canonical record dirs)
- **methodology:** frozen — see JSON artifact; datetime-normalized full JSON Schema enforcement, additionalProperties honored

## A. JSON Schema violations (burndown metric — target 0)

| Metric | Value |
|--------|-------|
| Total violations | 273 |
| Records with ≥1 violation | 216 / 787 (27%) |
| Clean records | 571 |
| Structural (unparseable/unknown-type/no-frontmatter) | 0 |

### By record type

| Type | Violations | Records affected |
|------|-----------|------------------|
| action | 67 | 55 |
| decision | 38 | 36 |
| intelligence | 23 | 18 |
| artifact | 23 | 15 |
| risk | 20 | 15 |
| lesson | 14 | 12 |
| conversation | 13 | 13 |
| document | 13 | 12 |
| opportunity | 12 | 6 |
| outcome | 12 | 2 |
| draft | 8 | 5 |
| assessment | 7 | 6 |
| commitment | 6 | 6 |
| initiative | 6 | 5 |
| stakeholder | 6 | 6 |
| organization | 3 | 2 |
| briefing | 2 | 2 |

### Top violation categories

| Category | Count |
|----------|-------|
| action:enum:action_type | 44 |
| decision:type:alternatives_considered | 28 |
| intelligence:enum:intelligence_type | 15 |
| artifact:enum:artifact_type | 14 |
| document:enum:document_type | 11 |
| outcome:type:success_metrics | 10 |
| action:enum:status | 8 |
| action:additionalProperties:<root> | 8 |
| decision:additionalProperties:<root> | 8 |
| conversation:additionalProperties:<root> | 8 |
| lesson:additionalProperties:<root> | 7 |
| artifact:pattern:id | 7 |
| risk:type:related_initiative | 6 |
| assessment:enum:assessment_type | 5 |
| initiative:enum:readiness_level | 5 |

## C. Open-namespace tag census (informational)

| Namespace | Used | Registered | Unregistered |
|-----------|------|-----------|--------------|
| application | 1 | 1 | 0 |
| channel | 2 | 8 | 0 |
| cluster | 0 | 0 | 0 |
| cognitive-doctrine | 2 | 4 | 1 |
| cognitive-loop | 5 | 15 | 0 |
| deadline | 7 | 12 | 1 |
| doctrine | 3 | 3 | 0 |
| framework | 10 | 5 | 5 |
| initiative | 7 | 9 | 0 |
| mechanism | 1 | 1 | 0 |
| meeting | 1 | 1 | 0 |
| method | 5 | 6 | 0 |
| milestone | 9 | 6 | 3 |
| org | 24 | 28 | 7 |
| outcome | 3 | 9 | 0 |
| person | 26 | 3 | 26 |
| product | 6 | 13 | 3 |
| project | 4 | 22 | 0 |
| role | 20 | 11 | 9 |
| type | 196 | 3 | 193 |
| **TOTAL** | **332** | **160** | **248** |

## D. mission_alignment facet-leakage census (informational)

- records_with_field: 403
- has_offvocab_value: 334
- zero_true_mission: 224
- pure_true_mission: 65
- has_cross_facet_prefixed: 8

Top off-vocabulary values: cybersecurity-productisation (164), csm-partnership (86), cyberdsa-2026 (62), commercial-development (42), commercial-strategy (35), sovereign-capability (34), stakeholder-engagement (32), government-partnerships (30)
