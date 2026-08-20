---
id: GOV-RECORD-LIFECYCLE-001
record_type: document
title: Record Lifecycle
created_at: 2026-08-04 00:00:00+00:00
updated_at: 2026-08-19 16:00:00+00:00
owner: DAF
status: active
priority: high
sensitivity: internal
lifecycle_state: canonical
confidence: high
tags:
- domain/cognitiveos-operations
- domain/governance
source:
  type: direct
  reference: DAF authority
summary: Governance reference document for Record Lifecycle.
strategic_significance: Governs CognitiveOS operational standards and procedures.
mission_alignment:
- sovereign-ai
- intelligence-enablement
related_records:
- GOV-INTAKE-SOP-001
document_type: reference
file_path: governance/record-lifecycle.md
version: '1.0'
author: DAF
---

# Record Lifecycle

## Lifecycle Stages

```
draft → validated → approved → active → [completed | blocked | deferred | superseded] → archived
```

### Stage Definitions

| Stage | Meaning |
|-------|---------|
| draft | Record created but not yet validated |
| in-progress | Active work is underway |
| validated | Record has been reviewed for accuracy |
| approved | Record has been formally approved by the decision owner |
| active | Record is current and operational |
| blocked | Progress is blocked by a dependency or risk |
| deferred | Record has been intentionally postponed |
| completed | Record's objectives have been fulfilled |
| superseded | Record has been replaced by a newer version |
| archived | Record is no longer active and has been archived |

## Transition Rules

1. A `draft` record must be `validated` before it can be `approved`.
2. An `approved` decision becomes `active` upon implementation.
3. A `completed` record must have completion evidence.
4. A `superseded` record must reference its replacement in the `superseded_by` field.
5. A `superseded` record must not be edited — a new record must be created.
6. An `archived` record retains its permanent identifier and remains searchable.
7. Identifiers are permanent — they are never reused, even after archiving.

## Review Requirements

| Portfolio Tier | Review Cycle |
|----------------|--------------|
| Flagship | Weekly |
| Operational | Weekly |
| Incubation | Bi-weekly |
| Watch List | Monthly |

## Supersession Protocol

When a new record supersedes an earlier one:
1. Create the new record with a new ID.
2. Populate `supersedes` field in the new record with the old record's ID.
3. Update the old record's `superseded_by` field with the new record's ID.
4. Change the old record's status to `superseded`.
5. Commit with message: `supersede(OLD-ID): replaced by NEW-ID`
