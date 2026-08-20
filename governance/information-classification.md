---
id: GOV-INFORMATION-CLASSIFICATION-001
record_type: document
title: Information Classification
created_at: 2026-08-04 00:00:00+00:00
updated_at: 2026-08-19 16:00:00+00:00
owner: DAF
status: active
priority: high
sensitivity: internal
lifecycle_state: canonical
confidence: high
tags:
- domain/governance
- domain/compliance
source:
  type: direct
  reference: DAF authority
summary: Governance reference document for Information Classification.
strategic_significance: Governs CognitiveOS operational standards and procedures.
mission_alignment:
- sovereign-ai
- intelligence-enablement
related_records:
- GOV-INTAKE-SOP-001
document_type: reference
file_path: governance/information-classification.md
version: '1.0'
author: DAF
---

# Information Classification

## Sensitivity Levels

| Level | Description | Storage | Replication |
|-------|-------------|---------|-------------|
| public | Approved for public release | Any platform | Freely replicated |
| internal | Internal organisational information | GitHub (private), Notion, Obsidian | May be copied across platforms |
| confidential | Sensitive business or stakeholder information | GitHub (private) with access controls | Requires owner approval before copying |
| restricted | Sensitive intelligence, legal authority, protected stakeholder info | GitHub (private, access-controlled) only | Must not be replicated without explicit approval |
| controlled | Highest sensitivity; legally or operationally sensitive | Local encrypted storage only | No replication permitted |

## Rules

1. Every record must have a sensitivity classification.
2. Records classified as `restricted` or `controlled` must not be replicated to Notion or external platforms without explicit approval from the record owner.
3. Records classified as `confidential` require CVS validation for claims involving this data.
4. Records classified as `restricted` or `controlled` require mandatory CVS validation.
5. All access and changes to `controlled` records must be logged and reviewed.

## CVS Reference

The master CVS framework is located at:
`/home/p62operator/.openclaw/workspace/03-VERIFICATION/CVS-FRAMEWORK.md`

All CVS validation follows the universal 6-tier classification (T1–T6), 5-level source hierarchy (L1–L5), and 5-criteria confidence scoring (0–10). See the master framework for full specification. The CogOS domain adapter is at:
`/home/p62operator/.openclaw/workspace/strategic-cognitiveos/03-VERIFICATION/CVS-ADAPTER.md`
6. When in doubt, classify upward — it's easier to declassify than to recover from a leak.
