---
id: GOV-CONTRIBUTION-STANDARD-001
record_type: document
title: "Contribution Standard"
created_at: 2026-08-04T00:00:00+00:00
updated_at: 2026-08-19T16:00:00+00:00
owner: DAF
status: active
priority: high
sensitivity: internal
lifecycle_state: active
confidence: high
tags:
  - domain/development-governance
  - domain/governance
source:
  type: direct
  reference: "DAF authority"
summary: "Governance reference document for Contribution Standard."
strategic_significance: "Governs CognitiveOS operational standards and procedures."
mission_alignment:
  - sovereign-ai
  - intelligence-enablement
related_records:
  - GOV-INTAKE-SOP-001
document_type: reference
file_path: "governance/contribution-standard.md"
version: "1.0"
author: DAF
---

# Contribution Standard

> **See also:** `governance/intake-sop.md` — Standard Operating Procedure for all CognitiveOS intake events (mandatory confirmation format, 9-step workflow, record type matrix)

## Creating a New Record

1. **Determine strategic value** — Does this meet the capture criteria? (See Operating Principles §3)
2. **Select the appropriate template** — Use the matching template from `templates/`
3. **Assign a permanent identifier** — Format: `<TYPE>-<YYYYMMDD>-<SEQUENCE>`
4. **Complete all mandatory fields** — Check the schema for required fields
5. **Apply controlled tags** — Only tags from `taxonomy/tags.yaml` are permitted
6. **Classify sensitivity** — Apply the appropriate information classification level
7. **Assign ownership** — Every record must have an owner
8. **Validate** — Human owner validates accuracy, interpretation, and classification
9. **Commit** — Store in GitHub with a descriptive commit message

## Commit Message Format

```
add(ID): brief description
update(ID): brief description
supersede(OLD-ID): replaced by NEW-ID
archive(ID): reason for archiving
```

## File Naming

Records are stored as Markdown files using their permanent identifier:

```
decisions/DEC-20260725-001-govsec-tip-flagship-classification.md
stakeholders/STK-20260725-001-cybersecurity-malaysia.md
initiatives/INIT-20260725-001-govsec-tip.md
```

File names use the pattern: `<ID>-<slug>.md`

## Tagging Rules

1. All tags use lowercase kebab-case
2. All tags follow the `namespace/value` format
3. No uncontrolled tags — if a new tag is needed, update `taxonomy/tags.yaml` first
4. Every record should have at least one `domain/` tag
5. Strategic records should have at least one `mission/` tag
6. Initiative records must have a `portfolio/` tag

## Quality Checklist

Before committing a record:

- [ ] All mandatory fields completed
- [ ] ID follows the permanent identifier standard
- [ ] Tags are from the controlled taxonomy
- [ ] Sensitivity is classified
- [ ] Owner is assigned
- [ ] Related records are linked
- [ ] No placeholder text remains
- [ ] Commit message follows the standard format
