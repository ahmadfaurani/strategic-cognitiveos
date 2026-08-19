---
id: GOV-TEMPLATE-DISCIPLINE-001
record_type: document
title: Template Discipline SOP
created_at: 2026-08-04T00:00:00+00:00
updated_at: 2026-08-19T12:00:00+00:00
owner: DAF
status: active
priority: high
sensitivity: internal
lifecycle_state: active
confidence: high
tags:
  - domain/cognitiveos-operations
  - domain/governance
  - domain/development-governance
source:
  type: direct
  reference: "DAF authority, 2026-08-04"
summary: "Mandatory process for CognitiveOS record creation — template selection, field completion, and validation before commit. Governs the three-layer system: schema (source of truth) → template (authoring interface) → validator (gate)."
strategic_significance: "Template discipline is the structural integrity layer of CognitiveOS. Without it, records enter git with missing fields, wrong enum values, and broken cross-references — degrading the entire knowledge base."
mission_alignment:
  - sovereign-ai
  - intelligence-enablement
related_records:
  - GOV-INTAKE-SOP-001
document_type: sop
file_path: "governance/template-discipline-sop.md"
version: "1.1"
author: DAF
---

# Template Discipline SOP

> **Version:** 1.1  
> **Authority:** DAF  
> **Status:** ACTIVE — Mandatory for all CognitiveOS record creation  
> **Scope:** All agents, all sessions, all record types  
> **Related:** `governance/contribution-standard.md`, `governance/intake-sop.md`, `schemas/`, `templates/`, `taxonomy/tags.yaml`

---

## 1. Purpose

Template discipline is the structural integrity layer of CognitiveOS. Every record entered into the system must conform to its schema before it enters git. This SOP defines the mandatory process for record creation — from template selection to commit.

**Core principle:** The schema is the source of truth. The template is the authoring interface. The validator is the gate. No record enters git without passing validation.

---

## 2. The Three-Layer System

```
Layer 1: SCHEMA (source of truth)
  ↓ defines what fields exist, which are required, what values are valid
Layer 2: TEMPLATE (authoring interface)
  ↓ provides the structure to fill in during intake
Layer 3: VALIDATOR (gate)
  ↓ checks the filled template against the schema before commit
```

**If the three layers disagree, the schema wins.** Templates must be updated to match schemas. If a field is in the schema's `required` array, it must be in the template's frontmatter.

---

## 3. Record Type → Schema → Template Mapping

| Record Type | ID Prefix | Schema File | Template File | Directory | Tier |
|-------------|-----------|-------------|---------------|-----------|------|
| action | ACT- | action.schema.json | action-template.md | actions/ | Tactical |
| assessment | ASSESS- | assessment.schema.json | assessment-template.md | assessments/ | Analytical |
| artifact | ART- | artifact.schema.json | artifact-template.md | artifacts/ | Operational |
| briefing | BRIEF- | briefing.schema.json | briefing-template.md | briefings/ | Strategic |
| commitment | COM- | commitment.schema.json | commitment-template.md | commitments/ | Operational |
| conversation | CONV- | conversation.schema.json | conversation-template.md | engagements/ | Operational |
| decision | DEC- | decision.schema.json | decision-template.md | decisions/ | Strategic |
| document | DOC- | document.schema.json | document-template.md | documents/ | Operational |
| draft | DRAFT- | draft.schema.json | draft-template.md | drafts/ | Tactical |
| initiative | INIT- | initiative.schema.json | initiative-template.md | initiatives/ | Strategic |
| intelligence | INT- | intelligence.schema.json | intelligence-template.md | intelligence/ | Strategic |
| lesson | LSN- | lesson.schema.json | lesson-template.md | (governance/) | Learning |
| opportunity | OPP- | opportunity.schema.json | opportunity-template.md | opportunities/ | Strategic |
| organization | ORG- | organization.schema.json | organization-template.md | organizations/ | Strategic |
| outcome | OUT- | outcome.schema.json | outcome-template.md | outcomes/ | Operational |
| pir | PIR- | pir.schema.json | pir-template.md | (intelligence/) | Strategic |
| risk | RSK- | risk.schema.json | risk-template.md | risks/ | Operational |
| stakeholder | STK- | stakeholder.schema.json | stakeholder-template.md | stakeholders/ | Operational |

**Canonical record types: 18** (14 spec-defined + 4 operational: assessment, briefing, draft, document)

**Retired types:** event (merged into conversation), engagement (conversation is canonical for engagements/ directory)

### Non-Record Directories

The following directories exist in CognitiveOS but do NOT contain typed records and are NOT covered by the Record Type Matrix:

| Directory | Purpose |
|-----------|---------|
| `portfolio/` | Governance tier classification structure (tags: `portfolio/flagship`, `portfolio/incubation`, etc.). NOT a record directory — initiative tier is set via tags, not directory placement. |
| `products/` | Product documentation containers (e.g., `chainsentry/`, `govsec-tip/`, `voroncitadel/`). Not typed records. |
| `projects/` | Project documentation containers (e.g., `red-team-division/`, `voron-c2/`). Not typed records. |
| `profiles/` | Profile/reference materials. Not typed records. |
| `strategies/` `strategy/` | Strategic direction documents. Not typed records. |
| `governance/` | SOPs, doctrines, standards. Not typed records. |
| `indexes/` | Auto-generated index files. Updated during intake, not created as records. |
| `memory/` | Daily memory logs and long-term memory. Not typed records. |
| `taxonomy/` | Controlled vocabulary definitions. Not typed records. |
| `templates/` | Record authoring templates. Not typed records. |
| `schemas/` | JSON schemas for validation. Not typed records. |
| `tools/` | Validation scripts and utilities. Not typed records. |

---

## 4. Required Fields by Record Type (REQ = Mandatory)

### 4.1 Action (ACT-)

| Field | Required | Type | Allowed Values |
|-------|----------|------|----------------|
| id | ✅ REQ | string | `ACT-YYYYMMDD-NNN` |
| record_type | ✅ REQ | const | `action` |
| title | ✅ REQ | string | Free text, min 1 char |
| owner | ✅ REQ | string | Person accountable |
| status | ✅ REQ | enum | draft, in-progress, active, open, proposed, pending, blocked, completed, overdue, cancelled, unresolved |
| required_output | ✅ REQ | string | Description of expected deliverable. **Must not be empty.** |
| priority | optional | enum | critical, high, medium, low |
| sensitivity | optional | enum | public, internal, confidential, restricted, controlled |
| deadline | optional | date | YYYY-MM-DD |
| dependency | optional | string | What must happen first |
| attention_level | optional | enum | owner, approver, consulted, informed, delegated, deferred |
| lifecycle_state | optional | enum | candidate, structurally_valid, semantically_verified, approved, canonical, superseded, rejected |
| tags | optional | array | Controlled taxonomy |
| related_records | optional | array | Record IDs |

### 4.2 Stakeholder (STK-)

> **SCOPE:** Individual persons only. Organisations use `organization` record type (ORG- prefix).

| Field | Required | Type | Allowed Values |
|-------|----------|------|----------------|
| id | ✅ REQ | string | `STK-YYYYMMDD-NNN` |
| record_type | ✅ REQ | const | `stakeholder` |
| title | ✅ REQ | string | Person's full name or designation |
| stakeholder_type | ✅ REQ | enum | government, internal, partner, prospect, academic, technical, political, defence, regulatory, industry |
| strategic_relevance | ✅ REQ | string | Why this person matters |
| relationship_status | ✅ REQ | enum | new, developing, active, trusted, dormant, at-risk |
| relationship_owner | ✅ REQ | string | Who in our team owns this relationship |
| organisation | optional | string | Employer organisation (link ORG- if exists) |
| role | optional | string | Job title |
| influence_level | optional | enum | high, medium, low |
| interest_level | optional | enum | high, medium, low |
| lifecycle_state | optional | enum | candidate, structurally_valid, semantically_verified, approved, canonical, superseded, rejected |
| sensitivity | optional | enum | public, internal, confidential, restricted, controlled |
| tags | optional | array | Controlled taxonomy |
| related_records | optional | array | Record IDs |

### 4.3 Organization (ORG-)

> **SCOPE:** Institutions, agencies, companies, organisational entities — not individual persons.

| Field | Required | Type | Allowed Values |
|-------|----------|------|----------------|
| id | ✅ REQ | string | `ORG-YYYYMMDD-NNN` |
| record_type | ✅ REQ | const | `organization` |
| title | ✅ REQ | string | Full official organisation name |
| org_type | ✅ REQ | enum | government-agency, government-ministry, regulatory-body, state-owned-enterprise, private-company, public-company, academic-institution, research-institute, non-profit, industry-association, international-organisation, military, law-enforcement, political-party, internal-division |
| sector | ✅ REQ | enum | government, defence, financial, telecommunications, energy, healthcare, education, critical-infrastructure, private-sector, cybersecurity, technology, consulting |
| strategic_relevance | ✅ REQ | string | Why this organisation matters |
| relationship_status | ✅ REQ | enum | new, developing, active, trusted, dormant, at-risk |
| relationship_owner | ✅ REQ | string | Who in our team owns this relationship |
| key_contacts | optional | array | STK record IDs of individuals at this org |
| lifecycle_state | optional | enum | candidate, structurally_valid, semantically_verified, approved, canonical, superseded, rejected |
| sensitivity | optional | enum | public, internal, confidential, restricted, controlled |
| tags | optional | array | Controlled taxonomy |
| related_records | optional | array | Record IDs |

### 4.4 Intelligence (INT-)

| Field | Required | Type | Allowed Values |
|-------|----------|------|----------------|
| id | ✅ REQ | string | `INT-YYYYMMDD-NNN` |
| record_type | ✅ REQ | const | `intelligence` |
| title | ✅ REQ | string | Descriptive title |
| intelligence_type | ✅ REQ | enum | stakeholder, political, market, technical, competitive, regulatory, security, operational |
| status | ✅ REQ | enum | draft, validated, active, superseded, archived |
| summary | ✅ REQ | string | Concise description |
| confidence | ✅ REQ | enum | high, medium, low |
| priority | optional | enum | critical, high, medium, low |
| sensitivity | optional | enum | public, internal, confidential, restricted, controlled |
| lifecycle_state | optional | enum | candidate, structurally_valid, semantically_verified, approved, canonical, superseded, rejected |
| tags | optional | array | Controlled taxonomy |
| source | optional | object | `{type, reference}` |
| related_records | optional | array | Record IDs |

### 4.5 Risk (RSK-)

| Field | Required | Type | Allowed Values |
|-------|----------|------|----------------|
| id | ✅ REQ | string | `RSK-YYYYMMDD-NNN` |
| record_type | ✅ REQ | const | `risk` |
| title | ✅ REQ | string | Descriptive title |
| risk_category | ✅ REQ | enum | delivery-capacity, sponsor-gap, product-maturity, commercial-viability, stakeholder-alignment, technical-debt, governance, resource-constraint, timing, dependency |
| probability | ✅ REQ | enum | high, medium, low |
| impact | ✅ REQ | enum | high, medium, low |
| status | ✅ REQ | enum | identified, mitigating, monitoring, active, realised, closed |
| priority | optional | enum | critical, high, medium, low |
| sensitivity | optional | enum | public, internal, confidential, restricted, controlled |
| lifecycle_state | optional | enum | candidate, structurally_valid, semantically_verified, approved, canonical, superseded, rejected |
| mitigation_strategy | optional | string | |
| mitigation_owner | optional | string | |
| trigger_conditions | optional | string | |
| tags | optional | array | Controlled taxonomy |
| related_records | optional | array | Record IDs |

### 4.6 Initiative (INIT-)

| Field | Required | Type | Allowed Values |
|-------|----------|------|----------------|
| id | ✅ REQ | string | `INIT-YYYYMMDD-NNN` |
| record_type | ✅ REQ | const | `initiative` |
| title | ✅ REQ | string | |
| created_at | ✅ REQ | datetime | ISO 8601 |
| updated_at | ✅ REQ | datetime | ISO 8601 |
| owner | ✅ REQ | string | |
| portfolio_tier | ✅ REQ | enum | flagship, incubation, watch-list, operational |
| status | ✅ REQ | enum | draft, in-progress, active, blocked, deferred, completed, superseded, archived |
| priority | ✅ REQ | enum | critical, high, medium, low |
| readiness_level | ✅ REQ | enum | concept, framed, prototype, demo-ready, pilot-ready, delivery-ready, commercial-ready, scale-ready, proposition, scaled |
| sensitivity | ✅ REQ | enum | public, internal, confidential, restricted, controlled |
| tags | ✅ REQ | array | Min 1 tag |
| mission_alignment | optional | array | |
| sponsor | optional | string | |
| delivery_owner | optional | string | |
| commercial_owner | optional | string | |
| source | optional | object | `{type, reference}` |
| related_records | optional | array | |

### 4.7 Decision (DEC-)

| Field | Required | Type | Allowed Values |
|-------|----------|------|----------------|
| id | ✅ REQ | string | `DEC-YYYYMMDD-NNN` |
| record_type | ✅ REQ | const | `decision` |
| title | ✅ REQ | string | |
| decision_date | ✅ REQ | date | YYYY-MM-DD |
| decision_owner | ✅ REQ | string | |
| status | ✅ REQ | enum | draft, proposed, active, superseded, archived |
| portfolio_tier | optional | enum | flagship, incubation, watch-list, operational |
| priority | optional | enum | critical, high, medium, low |
| confidence | optional | enum | high, medium, low |
| sensitivity | optional | enum | public, internal, confidential, restricted, controlled |
| tags | optional | array | |
| source | optional | object | `{type, reference}` |
| related_records | optional | array | |

### 4.8 Commitment (COM-)

| Field | Required | Type | Allowed Values |
|-------|----------|------|----------------|
| id | ✅ REQ | string | `COM-YYYYMMDD-NNN` |
| record_type | ✅ REQ | const | `commitment` |
| title | ✅ REQ | string | |
| created_at | ✅ REQ | datetime | ISO 8601 |
| updated_at | ✅ REQ | datetime | ISO 8601 |
| owner | ✅ REQ | string | Person accountable for fulfilment |
| receiving_stakeholder | ✅ REQ | string | STK or ORG ID |
| status | ✅ REQ | enum | draft, in-progress, blocked, completed, overdue, cancelled |
| expected_delivery_date | ✅ REQ | date | YYYY-MM-DD |
| priority | optional | enum | critical, high, medium, low |
| sensitivity | optional | enum | public, internal, confidential, restricted, controlled |
| source_engagement | optional | string | CONV or EVT ID |
| dependencies | optional | array | |
| risk_of_non_delivery | optional | string | |
| escalation_date | optional | date | YYYY-MM-DD |
| tags | optional | array | |
| related_records | optional | array | Record IDs |

### 4.9 Conversation (CONV-)

| Field | Required | Type | Allowed Values |
|-------|----------|------|----------------|
| id | ✅ REQ | string | `CONV-YYYYMMDD-NNN` |
| record_type | ✅ REQ | const | `conversation` |
| title | ✅ REQ | string | Free text |
| created_at | ✅ REQ | datetime | ISO 8601 |
| updated_at | optional | datetime | ISO 8601 |
| date | optional | date | YYYY-MM-DD |
| owner | ✅ REQ | string | Person accountable |
| channel | optional | enum | telegram, email, discord, signal, whatsapp, in-person, phone, video-call, other |
| participants | optional | array | Stakeholder IDs or names |
| status | ✅ REQ | enum | draft, active, validated, completed, archived |
| priority | optional | enum | critical, high, medium, low |
| sensitivity | optional | enum | public, internal, confidential, restricted, controlled |
| key_decisions | optional | array | Decision summaries |
| related_initiatives | optional | array | INIT IDs |
| related_records | optional | array | Record IDs |
| tags | optional | array | Controlled taxonomy |
| summary | optional | string | Concise description |
| strategic_significance | optional | string | |
| mission_alignment | optional | array | |
| lifecycle_state | optional | enum | candidate, structurally_valid, semantically_verified, approved, canonical, superseded, rejected |

### 4.10 Document (DOC-)

| Field | Required | Type | Allowed Values |
|-------|----------|------|----------------|
| id | ✅ REQ | string | `DOC-YYYYMMDD-NNN` |
| record_type | ✅ REQ | const | `document` |
| title | ✅ REQ | string | Descriptive title |
| owner | ✅ REQ | string | Person accountable |
| status | ✅ REQ | enum | draft, in-progress, validated, approved, active, superseded, archived |
| document_type | optional | enum | contract, specification, report, proposal, policy, sop, reference, presentation, analysis |
| file_path | optional | string | Path to source file if external |
| related_initiative | optional | string | INIT ID |
| version | optional | string | Document version |
| author | optional | string | Original author |
| priority | optional | enum | critical, high, medium, low |
| sensitivity | optional | enum | public, internal, confidential, restricted, controlled |
| lifecycle_state | optional | enum | candidate, structurally_valid, semantically_verified, approved, canonical, superseded, rejected |
| confidence | optional | enum | high, medium, low |
| tags | optional | array | Controlled taxonomy |
| source | optional | object | `{type, reference}` |
| summary | optional | string | Concise description |
| strategic_significance | optional | string | |
| mission_alignment | optional | array | |
| related_records | optional | array | Record IDs |

### 4.11 Draft (DRAFT-)

| Field | Required | Type | Allowed Values |
|-------|----------|------|----------------|
| id | ✅ REQ | string | `DRAFT-YYYYMMDD-NNN` |
| record_type | ✅ REQ | const | `draft` |
| title | ✅ REQ | string | Descriptive title |
| owner | ✅ REQ | string | Person accountable |
| status | ✅ REQ | enum | draft, in-progress, validated, approved, active, superseded, archived |
| draft_type | optional | enum | email, document, proposal, report, plan, social-media |
| related_action | optional | string | ACT ID |
| content_summary | optional | string | What the draft contains |
| priority | optional | enum | critical, high, medium, low |
| sensitivity | optional | enum | public, internal, confidential, restricted, controlled |
| lifecycle_state | optional | enum | candidate, structurally_valid, semantically_verified, approved, canonical, superseded, rejected |
| confidence | optional | enum | high, medium, low |
| tags | optional | array | Controlled taxonomy |
| source | optional | object | `{type, reference}` |
| summary | optional | string | |
| strategic_significance | optional | string | |
| mission_alignment | optional | array | |
| related_records | optional | array | Record IDs |

### 4.12 Assessment (ASSESS-)

| Field | Required | Type | Allowed Values |
|-------|----------|------|----------------|
| id | ✅ REQ | string | `ASSESS-YYYYMMDD-NNN` |
| record_type | ✅ REQ | const | `assessment` |
| title | ✅ REQ | string | Descriptive title |
| owner | ✅ REQ | string | Person accountable |
| status | ✅ REQ | enum | draft, in-progress, validated, approved, active, superseded, archived |
| assessment_type | optional | enum | framework-application, gap-analysis, readiness-assessment, stakeholder-evaluation, risk-assessment, performance-review, engineered-success-application |
| assessment_target | optional | string | What is being assessed |
| assessment_date | optional | date | YYYY-MM-DD |
| findings | optional | array | Assessment findings |
| recommendations | optional | array | Recommended actions |
| priority | optional | enum | critical, high, medium, low |
| sensitivity | optional | enum | public, internal, confidential, restricted, controlled |
| lifecycle_state | optional | enum | candidate, structurally_valid, semantically_verified, approved, canonical, superseded, rejected |
| confidence | optional | enum | high, medium, low |
| tags | optional | array | Controlled taxonomy |
| source | optional | object | `{type, reference}` |
| summary | optional | string | |
| strategic_significance | optional | string | |
| mission_alignment | optional | array | |
| related_records | optional | array | Record IDs |

### 4.13 Briefing (BRIEF-)

| Field | Required | Type | Allowed Values |
|-------|----------|------|----------------|
| id | ✅ REQ | string | `BRIEF-YYYYMMDD-NNN` |
| record_type | ✅ REQ | const | `briefing` |
| title | ✅ REQ | string | Descriptive title |
| owner | ✅ REQ | string | Person accountable |
| status | ✅ REQ | enum | draft, in-progress, validated, approved, active, superseded, archived |
| briefing_type | optional | enum | executive, operational, tactical, situational, strategic |
| prepared_for | optional | string | Audience |
| classification | optional | string | Sensitivity level for the briefing |
| key_findings | optional | array | Key findings |
| recommendations | optional | array | Recommended actions |
| priority | optional | enum | critical, high, medium, low |
| sensitivity | optional | enum | public, internal, confidential, restricted, controlled |
| lifecycle_state | optional | enum | candidate, structurally_valid, semantically_verified, approved, canonical, superseded, rejected |
| confidence | optional | enum | high, medium, low |
| tags | optional | array | Controlled taxonomy |
| source | optional | object | `{type, reference}` |
| summary | optional | string | |
| strategic_significance | optional | string | |
| mission_alignment | optional | array | |
| related_records | optional | array | Record IDs |

### 4.14 Artifact (ART-)

| Field | Required | Type | Allowed Values |
|-------|----------|------|----------------|
| id | ✅ REQ | string | `ART-YYYYMMDD-NNN` |
| record_type | ✅ REQ | const | `artifact` |
| title | ✅ REQ | string | Descriptive title |
| owner | ✅ REQ | string | Person accountable |
| status | ✅ REQ | enum | draft, in-progress, validated, approved, active, superseded, archived |
| artifact_type | optional | enum | proposal, report, deck, repository, specification, framework, brief, contract, template, schema, dataset, api, presentation, governance-document, analysis, plan |
| file_path | optional | string | Path to artifact file |
| related_initiative | optional | string | INIT ID |
| version | optional | string | Artifact version |
| created_by | optional | string | Creator |
| priority | optional | enum | critical, high, medium, low |
| sensitivity | optional | enum | public, internal, confidential, restricted, controlled |
| lifecycle_state | optional | enum | candidate, structurally_valid, semantically_verified, approved, canonical, superseded, rejected |
| confidence | optional | enum | high, medium, low |
| tags | optional | array | Controlled taxonomy |
| source | optional | object | `{type, reference}` |
| summary | optional | string | |
| strategic_significance | optional | string | |
| mission_alignment | optional | array | |
| related_records | optional | array | Record IDs |

### 4.15 Outcome (OUT-)

| Field | Required | Type | Allowed Values |
|-------|----------|------|----------------|
| id | ✅ REQ | string | `OUT-YYYYMMDD-NNN` |
| record_type | ✅ REQ | const | `outcome` |
| title | ✅ REQ | string | Descriptive title |
| created_at | ✅ REQ | datetime | ISO 8601 |
| updated_at | ✅ REQ | datetime | ISO 8601 |
| owner | ✅ REQ | string | Person accountable |
| status | ✅ REQ | enum | draft, in-progress, validated, approved, active, blocked, deferred, completed, superseded, archived, achieved, missed |
| priority | ✅ REQ | enum | critical, high, medium, low |
| sensitivity | ✅ REQ | enum | public, internal, confidential, restricted, controlled |
| lifecycle_state | ✅ REQ | enum | draft, validated, approved, active, completed, blocked, deferred, superseded, archived, canonical |
| confidence | ✅ REQ | enum | high, medium, low |
| tags | ✅ REQ | array | Controlled taxonomy (min 1) |
| source | ✅ REQ | object | `{type, reference}` |
| summary | ✅ REQ | string | What outcome was achieved |
| strategic_significance | ✅ REQ | string | Why this matters |
| mission_alignment | ✅ REQ | array | Mission areas |
| related_records | ✅ REQ | array | Record IDs |
| related_initiative | optional | string | INIT ID |
| outcome_date | optional | datetime | ISO 8601 |
| success_metrics | optional | array | Quantitative/qualitative metrics |
| linked_acts | optional | array | ACT IDs that produced this outcome |

### 4.16 Opportunity (OPP-)

| Field | Required | Type | Allowed Values |
|-------|----------|------|----------------|
| id | ✅ REQ | string | `OPP-YYYYMMDD-NNN` |
| record_type | ✅ REQ | const | `opportunity` |
| title | ✅ REQ | string | Descriptive title |
| owner | ✅ REQ | string | Person accountable |
| status | ✅ REQ | enum | draft, in-progress, validated, approved, active, superseded, archived |
| opportunity_type | optional | enum | commercial, partnership, strategic, technical, market |
| source_stakeholder | optional | string | STK or ORG ID |
| potential_value | optional | string | Estimated value |
| timeline | optional | string | Expected timeline |
| probability | optional | enum | low, medium, high |
| related_initiative | optional | string | INIT ID |
| priority | optional | enum | critical, high, medium, low |
| sensitivity | optional | enum | public, internal, confidential, restricted, controlled |
| lifecycle_state | optional | enum | candidate, structurally_valid, semantically_verified, approved, canonical, superseded, rejected |
| confidence | optional | enum | high, medium, low |
| tags | optional | array | Controlled taxonomy |
| source | optional | object | `{type, reference}` |
| summary | optional | string | |
| strategic_significance | optional | string | |
| mission_alignment | optional | array | |
| related_records | optional | array | Record IDs |

### 4.17 Lesson (LSN-)

| Field | Required | Type | Allowed Values |
|-------|----------|------|----------------|
| id | ✅ REQ | string | `LSN-YYYYMMDD-NNN` |
| record_type | ✅ REQ | const | `lesson` |
| title | ✅ REQ | string | Descriptive title |
| owner | ✅ REQ | string | Person accountable |
| status | ✅ REQ | enum | draft, in-progress, validated, approved, active, superseded, archived |
| lesson_source | optional | enum | project, engagement, incident, review, post-mortem, retrospective |
| lesson_date | optional | date | YYYY-MM-DD |
| lesson_category | optional | enum | process, technical, stakeholder, commercial, strategic, operational, governance |
| applies_to | optional | array | What areas this lesson applies to |
| evidence | optional | array | Supporting evidence |
| priority | optional | enum | critical, high, medium, low |
| sensitivity | optional | enum | public, internal, confidential, restricted, controlled |
| lifecycle_state | optional | enum | candidate, structurally_valid, semantically_verified, approved, canonical, superseded, rejected |
| confidence | optional | enum | high, medium, low |
| tags | optional | array | Controlled taxonomy |
| source | optional | object | `{type, reference}` |
| summary | optional | string | |
| strategic_significance | optional | string | |
| mission_alignment | optional | array | |
| related_records | optional | array | Record IDs |

### 4.18 PIR (PIR-)

| Field | Required | Type | Allowed Values |
|-------|----------|------|----------------|
| id | ✅ REQ | string | `PIR-YYYYMMDD-NNN` |
| record_type | ✅ REQ | const | `pir` |
| title | ✅ REQ | string | Intelligence question |
| owner | ✅ REQ | string | Person accountable |
| status | ✅ REQ | enum | open, in-progress, validated, ready_for_review, ready_for_submission, fulfilled, cancelled, superseded, deferred, blocked, overdue, identified, proposed, draft, approved, active, completed, captured, pending, unresolved, archived |
| pir_priority | ✅ REQ | enum | critical, high, medium, low |
| pir_tier | ✅ REQ | enum | tier-1-immediate, tier-2-routine, tier-3-background, Tier 1, Tier 2, Tier 3 |
| collection_cycle | optional | enum | continuous, daily, weekly, bi-weekly, monthly, quarterly |
| related_intelligence | optional | array | INT IDs |
| last_collected | optional | datetime | ISO 8601 |
| next_collection | optional | datetime | ISO 8601 |
| priority | optional | enum | critical, high, medium, low |
| sensitivity | optional | enum | public, internal, confidential, restricted, controlled |
| lifecycle_state | optional | enum | candidate, structurally_valid, semantically_verified, approved, canonical, superseded, rejected |
| confidence | optional | enum | high, medium, low |
| tags | optional | array | Controlled taxonomy |
| source | optional | object | `{type, reference}` |
| summary | optional | string | |
| strategic_significance | optional | string | |
| mission_alignment | optional | array | |
| related_records | optional | array | Record IDs |

---

### Step 1: Select Record Type

Determine the correct record type BEFORE writing. Use this decision tree:

```
Is this about an individual person?
  → YES → stakeholder (STK-)
  → NO → Is this about an org/institution?
           → YES → organization (ORG-)
           → NO → Is this a task someone needs to do?
                    → YES → action (ACT-)
                    → NO → Is this a risk to an initiative?
                             → YES → risk (RSK-)
                             → NO → Is this an analytical finding?
                                      → YES → intelligence (INT-)
                                      → NO → Is this a formal decision?
                                               → YES → decision (DEC-)
                                               → NO → Is this a new initiative/workstream?
                                                        → YES → initiative (INIT-)
                                                        → NO → Is this a promise made to someone?
                                                                 → YES → commitment (COM-)
                                                                 → NO → ... continue
```

### Step 2: Copy Template

Copy the matching template from `templates/`. Do NOT create records from memory or scratch.

### Step 3: Fill ALL Required Fields

Fill every field marked ✅ REQ in §4. Do not leave required fields empty. If a required field cannot be filled, the record is not ready for commit.

**Rules:**
- `required_output` on actions must describe the deliverable, not be `null` or empty
- `status` must use hyphens (`in-progress`), not underscores (`in_progress`)
- `title` on stakeholders = person's name or designation
- `title` on organizations = full official organisation name
- `confidence` on intelligence = `high`, `medium`, or `low` (not `HIGH`, not `High`)
- All enum values are lowercase

### Step 4: Validate Before Commit

```bash
cd strategic-cognitiveos
python3 tools/validate.py --file <path-to-record>
```

If validation fails → fix the record → re-validate → repeat until clean.

### Step 5: Commit

Only after validation passes, stage and commit. **NEVER use `git add -A`.** This sweeps non-record files from shared workspaces into the commit (Lesson #6, SOUL.md). Use scoped `git add` with an explicit path whitelist:

```bash
cd strategic-cognitiveos

# Stage ONLY the record directories that were modified
git add initiatives/ stakeholders/ engagements/ actions/ decisions/ \
       commitments/ risks/ intelligence/ outcomes/ artifacts/ \
       assessments/ briefings/ documents/ drafts/ organizations/ \
       opportunities/ lessons/ indexes/ governance/ schemas/ taxonomy/

# Verify what is staged BEFORE committing
git diff --cached --stat

git commit -m "add(ID): brief description"
```

**Pre-commit validation:** The pre-commit hook (v2) runs BOTH `tools/validate.py` (schema conformance) AND `tools/validate_taxonomy.py` (tag conformance against `taxonomy/tags.yaml`). If either validator fails, the commit is blocked. Do not bypass with `--no-verify` unless explicitly authorised.

### Step 6: Full Corpus Validation (Periodic)

```bash
python3 tools/validate.py
```

Run after batch intakes to catch any drift.

---

## 6. Pre-Commit Hook v2 (Automated Gate)

A git pre-commit hook (v2) runs BOTH `tools/validate.py` (schema validation) AND `tools/validate_taxonomy.py` (taxonomy validation) on staged `.md` files in record directories. If any staged record fails either validator, the commit is blocked.

**Installation:**

```bash
cd strategic-cognitiveos
cp tools/pre-commit-validate .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

**Phase 1 — Schema Validation (`tools/validate.py`):**
- Detects staged `.md` files in record directories (17 canonical dirs)
- Checks YAML frontmatter against the corresponding `schemas/*.schema.json`
- Verifies required fields, enum values, ID patterns, datetime formats
- Blocks commit if any record fails schema validation

**Phase 2 — Taxonomy Validation (`tools/validate_taxonomy.py`):**
- Checks all `tags` in record frontmatter against `taxonomy/tags.yaml`
- Verifies each tag namespace exists and each tag value is in the controlled vocabulary
- Blocks commit if any tag is not in the taxonomy (e.g., `domain/fake-namespace` → blocked)

**Pass condition:** Both phases must pass. Either failure blocks the commit.
**Bypass:** `--no-verify` bypasses the hook. Do not use unless explicitly authorised.

---

## 7. Common Violations and Prevention

| Violation | Cause | Prevention |
|-----------|-------|------------|
| Missing `required_output` | Describing output in body, not frontmatter | Template now has `required_output: ""` — fill it |
| `in_progress` vs `in-progress` | Python convention leak | Template comment says "Use hyphen" |
| STK record for an organisation | No ORG type existed | ORG type now exists — use it |
| Missing `intelligence_type` | Rich body, poor frontmatter | Template has it in required frontmatter |
| Missing `risk_category`, `probability`, `impact` | Same | Template has all three in frontmatter |
| Missing `title` on STK | Used `name:` instead | Template uses `title:` — schema requires `title` |
| No YAML frontmatter | Pure markdown filed as record | All records must start with `---` frontmatter |

---

## 8. Template Maintenance Protocol

When a schema changes:
1. Update the schema file in `schemas/`
2. Update the corresponding template in `templates/`
3. Update §4 of this SOP
4. Run `python3 tools/validate.py` to check existing records
5. Run `python3 tools/validate_taxonomy.py` to check tag conformance
6. Run `python3 tools/backfill.py` if migration is needed
7. Commit schema + template + SOP changes in one commit (scoped `git add` — never `git add -A`)

When a new record type is added:
1. Create schema in `schemas/`
2. Create template in `templates/`
3. Create directory for records
4. Add type-to-dir mapping in `tools/validate.py`
5. Add to `RECORD_DIRS` in BOTH `tools/validate.py` AND `tools/validate_taxonomy.py` — **critical: both validators must have the same `RECORD_DIRS` set**
6. Add to §3 and §4 of this SOP
7. Add to Intake SOP §3 Record Type Matrix (version-lock both SOPs in the same commit)
8. Test with a sample record (must pass both validators)

---

## 9. Authority and Enforcement

- **Authority:** DAF
- **Mandatory for:** All agents creating CognitiveOS records
- **Enforcement:** Pre-commit hook (automated) + Post-commit validation (audit)
- **Non-compliance:** Records failing validation are blocked from commit. Repeated violations trigger review of agent's intake process.

---

## 11. Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-08-04 | DAF (authority), Ember (drafter) | Initial institutionalization. Three-layer system defined. 8 record types with §4 field specs. Pre-commit hook (schema-only). |
| 1.1 | 2026-08-19 | DAF (authority), Laras (drafter) | YAML frontmatter added (governance doc now passes its own validation). §4 expanded from 8 to 18 types (added CONV, DOC, DRAFT, ASSESS, BRIEF, ART, OUT, OPP, LSN, PIR — all derived from schemas/*.schema.json). §5 Step 5: scoped `git add` with path whitelist added (Lesson #6 enforcement). §6: pre-commit hook updated to v2 (both `validate.py` and `validate_taxonomy.py`). §8: maintenance protocol updated with taxonomy validator + `RECORD_DIRS` harmonization requirement + version-lock with Intake SOP. Non-Record Directories section added after §3. Root cause: Intake SOP upgraded to v1.1 without version-locking the paired Template SOP — same recurring meta-pattern of one governance instrument updated while its paired instrument stays stale. |

---

## 10. Quick Reference Card

```
BEFORE WRITING A RECORD:
  1. What record type is this? → Check decision tree (§5.1)
  2. Copy the template → templates/<type>-template.md
  3. Fill ALL ✅ REQ fields → Check §4 for required fields
  4. Use correct enum values → Lowercase, hyphens not underscores
  5. Validate → python3 tools/validate.py --file <path>
  6. Commit only if validation passes

REMEMBER:
  - Stakeholder = individual person (STK-)
  - Organization = institution/agency/company (ORG-)
  - required_output is MANDATORY on every action
  - Status uses hyphens: in-progress, not in_progress
  - All enum values are lowercase
  - title field is required on every record type
```
