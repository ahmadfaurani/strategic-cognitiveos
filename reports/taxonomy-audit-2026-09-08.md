# Taxonomy Integrity Audit — 2026-09-08

- **repository_commit:** `7381d32c01016ee7eb0c908e7b38d573df37d089`
- **audit_timestamp:** 2026-09-08T14:39:04+00:00
- **tool:** audit_taxonomy_v2.py (sha256:c2ff69f1369aad72, jsonschema 4.23.0)
- **records_scanned:** 780 typed records
- **methodology:** frozen — see JSON artifact; datetime-normalized full JSON Schema enforcement, additionalProperties honored

## A. JSON Schema violations (burndown metric — target 0)

| Metric | Value |
|--------|-------|
| Total violations | 682 |
| Records with ≥1 violation | 415 / 780 (53%) |
| Clean records | 365 |
| Structural (unparseable/unknown-type) | 37 |

### By record type

| Type | Violations | Records affected |
|------|-----------|------------------|
| action | 247 | 144 |
| stakeholder | 102 | 54 |
| risk | 62 | 36 |
| decision | 45 | 39 |
| organization | 39 | 20 |
| initiative | 34 | 18 |
| intelligence | 29 | 20 |
| conversation | 28 | 19 |
| commitment | 22 | 14 |
| artifact | 20 | 12 |
| lesson | 14 | 12 |
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
| initiative:type:source | 26 |
| commitment:type:source | 16 |
| intelligence:enum:intelligence_type | 15 |
| conversation:type:source | 12 |
| artifact:enum:artifact_type | 11 |
| conversation:additionalProperties:<root> | 10 |
| action:enum:status | 8 |
| action:additionalProperties:<root> | 8 |
| decision:type:source | 8 |

### Structural violations

- `03-VERIFICATION/CVS-ADAPTER.md` — no-frontmatter
- `actions/ACT-20260824-001.md` — yaml-parse: mapping values are not allowed here
- `actions/ACT-20260825-002.md` — yaml-parse: mapping values are not allowed here
- `artifacts/ART-20260908-001-gtm-marketing-execution-plan-deck.md` — yaml-parse: while scanning a quoted scalar
- `artifacts/ART-20260908-002-cyberdsa-invitation-list.xlsx.md` — yaml-parse: while scanning a quoted scalar
- `artifacts/GRP-20260813-001-GovSec-CyberDSA-Readiness-Plan.md` — no-frontmatter
- `artifacts/MWR-20260813-001-Master-Workstream-Register.md` — no-frontmatter
- `artifacts/VoronCitadel_GTM_Strategy_Final_Draft.md` — yaml-parse: while scanning a quoted scalar
- `briefings/BRIEF-20260817-001-CSM-WORKSTREAM-ANALYSIS.md` — no-frontmatter
- `briefings/PORTFOLIO-EXECUTION-RESET-20260812.md` — no-frontmatter
- `decisions/DEC-20260908-003.md` — yaml-parse: while scanning a quoted scalar
- `documents/DOC-20260827-002-poitss-directive-5-05.md` — yaml-parse: while scanning a quoted scalar
- `documents/DOC-20260908-001.md` — yaml-parse: while scanning a quoted scalar
- `documents/DOC-20260908-002.md` — yaml-parse: while scanning a quoted scalar
- `documents/DOC-20260908-003.md` — yaml-parse: while scanning a quoted scalar
- `documents/DOC-20260908-004.md` — yaml-parse: while scanning a quoted scalar
- `documents/DOC-20260908-005.md` — yaml-parse: while scanning a quoted scalar
- `events/EVT-20260908-001.md` — unknown-or-retired-record_type: event
- `logs/validation-2026-08-21.md` — no-frontmatter
- `logs/validation-2026-08-23.md` — no-frontmatter
- `logs/validation-2026-08-30.md` — no-frontmatter
- `logs/validation-2026-09-06.md` — no-frontmatter
- `memory/2026-08-04.md` — no-frontmatter
- `memory/2026-08-18.md` — no-frontmatter
- `memory/2026-08-21.md` — no-frontmatter
- `memory/2026-08-25.md` — no-frontmatter
- `memory/2026-08-26.md` — no-frontmatter
- `memory/2026-09-03.md` — no-frontmatter
- `memory/2026-09-05.md` — no-frontmatter
- `memory/ATHENA-COGNITIVEOS-INTAKE-MODUS-OPERANDI.md` — no-frontmatter
- `osint-stack/ARCHITECTURE.md` — no-frontmatter
- `outcomes/OUT-20260815-001.md` — unknown-or-retired-record_type: outcome
- `outcomes/OUT-20260819-001.md` — unknown-or-retired-record_type: outcome
- `outcomes/OUT-20260819-002.md` — unknown-or-retired-record_type: outcome
- `profiles/DAF-COMPREHENSIVE-PROFILE-20260815.md` — no-frontmatter
- `profiles/FUAD-COMPREHENSIVE-PROFILE-20260829.md` — no-frontmatter
- `profiles/HADRI-COMPREHENSIVE-PROFILE-20260829.md` — no-frontmatter

## C. Open-namespace tag census (informational)

| Namespace | Used | Registered | Unregistered |
|-----------|------|-----------|--------------|
| application | 1 | 1 | 0 |
| channel | 3 | 8 | 0 |
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
| milestone | 10 | 6 | 4 |
| org | 25 | 28 | 8 |
| outcome | 3 | 9 | 0 |
| person | 26 | 3 | 26 |
| product | 6 | 13 | 3 |
| project | 4 | 22 | 0 |
| role | 20 | 11 | 9 |
| type | 194 | 3 | 191 |
| **TOTAL** | **333** | **160** | **248** |

## D. mission_alignment facet-leakage census (informational)

- records_with_field: 404
- has_offvocab_value: 335
- zero_true_mission: 225
- pure_true_mission: 65
- has_cross_facet_prefixed: 8

Top off-vocabulary values: cybersecurity-productisation (165), csm-partnership (87), cyberdsa-2026 (62), commercial-development (43), commercial-strategy (35), sovereign-capability (34), stakeholder-engagement (32), cognitiveos-operations (30)
