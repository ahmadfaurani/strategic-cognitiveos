# Template Discipline SOP

> **Version:** 1.0  
> **Authority:** DAF  
> **Status:** ACTIVE — Mandatory for all CognitiveOS record creation  
> **Scope:** All agents, all sessions, all record types  
> **Related:** `governance/contribution-standard.md`, `governance/intake-sop.md`, `schemas/`, `templates/`

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
| related_records | optional | array | |

---

## 5. Mandatory Authoring Process

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

Only after validation passes, commit with the standard message format:

```
add(ID): brief description
```

### Step 6: Full Corpus Validation (Periodic)

```bash
python3 tools/validate.py
```

Run after batch intakes to catch any drift.

---

## 6. Pre-Commit Hook (Automated Gate)

A git pre-commit hook runs `validate.py` on staged files. If any staged record fails validation, the commit is blocked.

**Installation:**

```bash
cd strategic-cognitiveos
cp tools/pre-commit-validate .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

**What it does:**
- Detects staged `.md` files in record directories
- Runs schema validation on each
- Blocks commit if any fail
- Passes if all valid (or no .md records staged)

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
5. Run `python3 tools/backfill.py` if migration is needed
6. Commit schema + template + SOP changes in one commit

When a new record type is added:
1. Create schema in `schemas/`
2. Create template in `templates/`
3. Create directory for records
4. Add type-to-dir mapping in `tools/validate.py`
5. Add to §3 and §4 of this SOP
6. Add to `DIR_TO_TYPES` and `TYPE_TO_DIR` in validator
7. Test with a sample record

---

## 9. Authority and Enforcement

- **Authority:** DAF
- **Mandatory for:** All agents creating CognitiveOS records
- **Enforcement:** Pre-commit hook (automated) + Post-commit validation (audit)
- **Non-compliance:** Records failing validation are blocked from commit. Repeated violations trigger review of agent's intake process.

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
