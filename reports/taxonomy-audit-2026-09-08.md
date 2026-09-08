# Taxonomy Integrity Audit — 2026-09-08 (methodology v1.1-20260908)

- **repository_commit:** `361c253d0f24b413c546fa122c506d2abb2b561d`
- **audit_timestamp:** 2026-09-08T14:59:53+00:00
- **tool:** audit_taxonomy_v2.py (sha256:03a726f17e94f28f, jsonschema 4.23.0)
- **records_scanned:** 773 typed records (17 canonical record dirs)
- **methodology:** frozen — see JSON artifact; datetime-normalized full JSON Schema enforcement, additionalProperties honored

## A. JSON Schema violations (burndown metric — target 0)

| Metric | Value |
|--------|-------|
| Total violations | 689 |
| Records with ≥1 violation | 413 / 773 (53%) |
| Clean records | 360 |
| Structural (unparseable/unknown-type/no-frontmatter) | 14 |

### By record type

| Type | Violations | Records affected |
|------|-----------|------------------|
| action | 247 | 144 |
| stakeholder | 102 | 54 |
| risk | 62 | 36 |
| decision | 45 | 39 |
| organization | 39 | 20 |
| initiative | 30 | 17 |
| intelligence | 29 | 20 |
| conversation | 25 | 16 |
| commitment | 22 | 14 |
| artifact | 20 | 12 |
| lesson | 14 | 12 |
| outcome | 14 | 2 |
| opportunity | 12 | 6 |
| draft | 10 | 5 |
| assessment | 9 | 7 |
| document | 7 | 7 |
| briefing | 2 | 2 |

### Top violation categories

| Category | Count |
|----------|-------|
| action:type:source | 180 |
| stakeholder:type:source | 96 |
| action:enum:action_type | 44 |
| risk:type:source | 42 |
| organization:type:source | 36 |
| decision:type:alternatives_considered | 28 |
| initiative:type:source | 24 |
| commitment:type:source | 16 |
| intelligence:enum:intelligence_type | 15 |
| conversation:type:source | 12 |
| artifact:enum:artifact_type | 11 |
| outcome:type:success_metrics | 10 |
| action:enum:status | 8 |
| action:additionalProperties:<root> | 8 |
| decision:type:source | 8 |

### Structural violations

- `briefings/BRIEF-20260817-001-CSM-WORKSTREAM-ANALYSIS.md` — no-frontmatter
- `briefings/PORTFOLIO-EXECUTION-RESET-20260812.md` — no-frontmatter
- `decisions/DEC-20260908-003.md` — yaml-parse: while scanning a quoted scalar
- `documents/DOC-20260827-002-poitss-directive-5-05.md` — yaml-parse: while scanning a quoted scalar
- `documents/DOC-20260908-001.md` — yaml-parse: while scanning a quoted scalar
- `documents/DOC-20260908-002.md` — yaml-parse: while scanning a quoted scalar
- `documents/DOC-20260908-003.md` — yaml-parse: while scanning a quoted scalar
- `documents/DOC-20260908-004.md` — yaml-parse: while scanning a quoted scalar
- `documents/DOC-20260908-005.md` — yaml-parse: while scanning a quoted scalar
- `artifacts/ART-20260908-001-gtm-marketing-execution-plan-deck.md` — yaml-parse: while scanning a quoted scalar
- `artifacts/ART-20260908-002-cyberdsa-invitation-list.xlsx.md` — yaml-parse: while scanning a quoted scalar
- `artifacts/GRP-20260813-001-GovSec-CyberDSA-Readiness-Plan.md` — no-frontmatter
- `artifacts/MWR-20260813-001-Master-Workstream-Register.md` — no-frontmatter
- `artifacts/VoronCitadel_GTM_Strategy_Final_Draft.md` — yaml-parse: while scanning a quoted scalar

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

- records_with_field: 399
- has_offvocab_value: 334
- zero_true_mission: 224
- pure_true_mission: 61
- has_cross_facet_prefixed: 8

Top off-vocabulary values: cybersecurity-productisation (164), csm-partnership (86), cyberdsa-2026 (62), commercial-development (42), commercial-strategy (35), sovereign-capability (34), stakeholder-engagement (32), government-partnerships (30)
