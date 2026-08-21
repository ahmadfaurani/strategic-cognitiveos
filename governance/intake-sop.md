---
id: GOV-INTAKE-SOP-001
record_type: document
title: CognitiveOS Intake SOP — Standard Operating Procedure
created_at: 2026-08-04 00:00:00+00:00
updated_at: 2026-08-21T15:00:00+08:00
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
summary: Governance reference document for CognitiveOS Intake SOP — Standard Operating
  Procedure.
strategic_significance: Governs CognitiveOS operational standards and procedures.
mission_alignment:
- sovereign-ai
- intelligence-enablement
related_records:
- GOV-INTAKE-SOP-001
- GOV-TEMPLATE-DISCIPLINE-001
paired_sops:
- GOV-TEMPLATE-DISCIPLINE-001
document_type: sop
file_path: governance/intake-sop.md
version: '1.3'
author: DAF
---

# CognitiveOS Intake SOP — Standard Operating Procedure

> **Version:** 1.3  
> **Authority:** Ahmad Faurani Jaafar (DAF)  
> **Status:** Active — institutionalized 2026-08-04  
> **Scope:** All CognitiveOS ingestion events, all sessions, all agents  
> **Related:** `governance/contribution-standard.md`, `governance/template-discipline-sop.md` (paired), `AI-PROCESSOR-INSTRUCTIONS.md`, `schemas/`

---

## 1. Purpose

Every time information is ingested into CognitiveOS — whether from an email, conversation, document, meeting, or external source — the intake must follow this standard operating procedure. The SOP ensures:

- **Completeness** — all relevant data is captured with correct record types
- **Traceability** — every record has a permanent ID, provenance, and commit hash
- **Index integrity** — all indexes are updated in the same commit
- **Consistency** — the same confirmation format is delivered every time
- **Accountability** — the intake is committed, pushed, and auditable

---

## 2. Intake Workflow (9 Steps)

### Step 1: Receive & Classify Source

- Identify what the source is (email, conversation, document, meeting notes, intelligence report)
- Determine sensitivity level (public / internal / confidential / restricted / controlled)
- Identify the authority (who provided it, what decision weight it carries)

### Step 2: Extract & Structure

- Read the full source material
- Identify all entities: initiatives, stakeholders, conversations, actions, decisions, commitments, risks, intelligence, outcomes
- For each entity, determine the correct record type (see §3 Record Type Matrix)

### Step 3: Create Records

- Create a markdown file for each record in the correct directory
- Use the appropriate template from `templates/`
- Assign permanent ID: `<TYPE>-<YYYYMMDD>-<SEQUENCE>` (e.g., `INIT-20260804-001`)
- Complete all mandatory fields per the schema
- Apply controlled tags from `taxonomy/`
- Set sensitivity classification
- Assign owner and related records

### Step 4: Update Indexes

Every intake must update all relevant indexes in the same commit:

| Index File | When to Update |
|-----------|----------------|
| `indexes/initiative-index.md` | New INIT record created |
| `indexes/stakeholder-index.md` | New STK record created |
| `indexes/conversation-index.md` | New CONV record created |
| `indexes/executive-portfolio-index.md` | New INIT record created or tier changed |
| `indexes/commitment-index.md` | New COM record created |
| `indexes/decision-index.md` | New DEC record created |
| `indexes/risk-index.md` | New RSK record created |
| `indexes/product-readiness-index.md` | Product readiness status changed |

### Step 5: Update Daily Memory

- Log the intake in `memory/YYYY-MM-DD.md` with:
  - Time and authority
  - Channel
  - What was ingested
  - Records created (with IDs)
  - Commit hash (after commit)

### Step 6: Commit

**NEVER use `git add -A`.** This sweeps non-record files from shared workspaces into the commit (Lesson #6, SOUL.md). Use scoped `git add` with an explicit path whitelist:

```bash
cd strategic-cognitiveos

# Stage ONLY the record directories that were modified
git add initiatives/ stakeholders/ engagements/ actions/ decisions/ \
       commitments/ risks/ intelligence/ outcomes/ artifacts/ \
       assessments/ briefings/ documents/ drafts/ organizations/ \
       opportunities/ lessons/ indexes/ governance/ schemas/ taxonomy/

# Verify what is staged BEFORE committing
git diff --cached --stat

git commit -m "CognitiveOS: <brief description> — <record count> records

New records:
- <ID> — <title>
- <ID> — <title>

Indexes updated: <list>"
```

**Pre-commit validation:** The pre-commit hook runs BOTH `tools/validate.py` (schema conformance) AND `tools/validate_taxonomy.py` (tag conformance against `taxonomy/tags.yaml`). If either validator fails, the commit is blocked. Do not bypass with `--no-verify` unless explicitly authorised.

### Step 7: Push

```bash
git push origin main
```

### Step 8: Deliver Confirmation Notification

Send the standardized confirmation (see §4) to the requesting authority.

### Step 9: Update Memory (Long-term)

If the intake contains significant strategic information, update `MEMORY.md` with a distilled entry.

---

## 3. Record Type Matrix

All 18 active record types. Each has a schema in `schemas/`, a template in `templates/`, and a canonical directory. Records must be placed in their canonical directory — no exceptions.

| Type | Prefix | Directory | Schema | When to Create |
|------|--------|-----------|--------|----------------|
| Initiative | `INIT-` | `initiatives/` | `initiative.schema.json` | New project, workstream, or strategic initiative |
| Stakeholder | `STK-` | `stakeholders/` | `stakeholder.schema.json` | New person, organisation, or entity relationship |
| Conversation | `CONV-` | `engagements/` | `conversation.schema.json` | Email thread, meeting, or significant exchange |
| Action | `ACT-` | `actions/` | `action.schema.json` | Task, next step, or required action |
| Decision | `DEC-` | `decisions/` | `decision.schema.json` | Formal decision or determination |
| Commitment | `COM-` | `commitments/` | `commitment.schema.json` | Formal commitment by either party |
| Risk | `RSK-` | `risks/` | `risk.schema.json` | Identified risk or threat |
| Intelligence | `INT-` | `intelligence/` | `intelligence.schema.json` | Intelligence product or assessment |
| Outcome | `OUT-` | `outcomes/` | `outcome.schema.json` | Result or delivered outcome |
| Artifact | `ART-` | `artifacts/` | `artifact.schema.json` | Deliverable file, document, or produced asset |
| Assessment | `ASSESS-` | `assessments/` | `assessment.schema.json` | Analytical assessment of a situation, entity, or initiative |
| Briefing | `BRIEF-` | `briefings/` | `briefing.schema.json` | Executive or operational briefing document |
| Document | `DOC-` | `documents/` | `document.schema.json` | External or reference document ingested into CognitiveOS |
| Draft | `DRAFT-` | `drafts/` | `draft.schema.json` | Draft communication, document, or deliverable in progress |
| Organization | `ORG-` | `organizations/` | `organization.schema.json` | New organization entity tracked in CognitiveOS |
| Opportunity | `OPP-` | `opportunities/` | `opportunity.schema.json` | New strategic or commercial opportunity |
| Lesson | `LSN-` | `lessons/` | `lesson.schema.json` | Lesson learned from execution, success, or failure |
| PIR | `PIR-` | `intelligence/` | `pir.schema.json` | Priority Intelligence Requirement (standalone or embedded in parent record) |

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

### ID Convention

- Format: `<TYPE>-<YYYYMMDD>-<SEQUENCE>`
- Date: the date the record is created (not the date of the event)
- Sequence: 3-digit zero-padded, starting at 001, per type per day
- IDs are permanent — never reused, even after archiving

---

## 4. Confirmation Notification Format (MANDATORY)

Every CognitiveOS intake MUST conclude with this confirmation delivered to the requesting authority:

```
Commit <hash> — <N> files, <N> insertions.

<N> new records:
• <ID> — <title> (<tier/stage>)
• <ID> — <title> (<role/context>)
• <ID> — <title> (<role/context>)
...

<N> indexes updated — <index names>

Key link: <one-line summary of strategic connection to existing initiatives/workstreams>

Next triggers:
1. <next action required>
2. <next action required>
```

### Format Rules

1. **Commit hash** — always the short hash (7 chars)
2. **File/insertion count** — from `git commit` output
3. **Record list** — every new record with its typed ID
4. **Index list** — every index file modified
5. **Key link** — one line connecting this intake to the broader strategic picture
6. **Next triggers** — the immediate next actions that this intake creates or enables

### Example (from 2026-08-04 CSM VoronDRQ GTM intake)

```
Commit 9c72e36 — 13 files, 830 insertions.

9 new records:
• INIT-20260804-001 — CSM × Aras VoronDRQ Joint GTM Activation (Flagship/Pilot)
• CONV-20260804-001 — CSM Post-MoU VoronDRQ GTM Email Thread
• STK-20260804-001 — Mohammad Fahdzli Bin Abdul Rauf, Head of Cyber Solutions, CSM
• STK-20260804-002 — Zulfeka Zainal Abidin, CSM Senior
• STK-20260804-003 — Ahmad Fuad, Aras Integrasi
• ACT-20260804-001 — Confirm Voron Citadel training reschedule (Aug 12/13/14)
• ACT-20260804-002 — Conduct VoronDRQ sales enablement session with CSM
• ACT-20260804-003 — First-wave account shortlisting (10–15 orgs)
• ACT-20260804-004 — Assign joint account ownership (1 CSM + 1 Aras per account)

4 indexes updated — Initiative Index, Stakeholder Index, Conversation Index, Executive Portfolio Index.

Key link: This initiative advances VoronDRQ from proposition (INIT-20260725-002, Workstream B) to pilot-stage GTM activation under the CSM MoU.

Next triggers:
1. CSM confirmation of training reschedule (Aug 12/13/14) → ACT-20260804-001
2. VoronDRQ sales enablement session → ACT-20260804-002
```

---

## 5. Intake Triggers

CognitiveOS intake is triggered when any of the following are received:

| Trigger | Typical Source | Expected Records |
|---------|---------------|-----------------|
| Email thread forwarded | Email | CONV, STK (new people), ACT (action items), INIT (if new) |
| Meeting or call notes | Conversation | CONV, DEC (if decisions made), ACT (action items) |
| Strategic document | Document | INIT (if new initiative), STK (if new stakeholders) |
| Intelligence report | Intelligence | INT, RSK (if risks identified) |
| News or media item | External | INT (if strategically material) |
| Partner or client communication | Email/letter | CONV, STK, ACT, COM (if commitments made) |
| Internal decision or determination | Conversation | DEC, ACT |
| Risk identification | Analysis | RSK, ACT (mitigation actions) |
| **"That's it" trigger** | **Telegram (DAF)** | **Session-wide intake — all entities, decisions, risks, and actions from the entire conversation** |

### "That's it" Trigger — Standard Modus Operandi

**Authority:** DAF (2026-08-20)
**Status:** Institutionalized as standard operating procedure

When DAF sends the message **"that's it"** (or close variant), the agent MUST:

1. **Review the entire session** — scan all conversation content from the session
2. **Extract all entities** — initiatives, stakeholders, decisions, risks, actions, documents, assessments, organizations, lessons learned
3. **Create or update records** following the 9-step Intake Workflow (§2)
4. **Update all indexes** in the same commit
5. **Commit with scoped `git add`** (never `git add -A`)
6. **Push to remote**
7. **Deliver confirmation notification** (§4 format)

This trigger is **always-on** — it does not require a per-event directive to activate. The session IS the intake event. Every decision, risk, action, and entity discussed during the session is material for CognitiveOS ingestion.

**Key principle:** The "that's it" trigger is the session-level analog of the email intake trigger. Just as a forwarded email triggers intake of that email's content, "that's it" triggers intake of the entire session's strategic content.

---

## 6. Quality Checklist (Pre-Commit)

Before committing any intake:

```
[ ] All records have permanent IDs following the convention
[ ] All mandatory schema fields are completed
[ ] All records have owners assigned
[ ] All records have sensitivity classified
[ ] All tags are from controlled taxonomy — VALIDATED by `tools/validate_taxonomy.py` (not aspirational — enforced at pre-commit)
[ ] All related records are cross-linked
[ ] All relevant indexes are updated
[ ] Daily memory log entry written
[ ] Commit message follows the standard format
[ ] Confirmation notification prepared
[ ] No `git add -A` used — scoped `git add` with path whitelist only
```

If any box is unchecked, the intake is not complete.

---

## 7. Compliance

This SOP is mandatory for all CognitiveOS intake events. Non-compliance indicators:

- Missing confirmation notification (no record of intake)
- Indexes not updated (orphaned records)
- Records without permanent IDs
- Records without sensitivity classification
- Records without owner assignment
- Intake without commit/push (local-only changes)

Any intake that fails to produce the confirmation notification should be treated as incomplete and re-processed.

---

## 8. Paired SOP Version-Locking

**Principle:** This SOP is paired with `GOV-TEMPLATE-DISCIPLINE-001` (Template Discipline SOP). Both govern the same CognitiveOS intake pipeline. When a change to either SOP affects a shared surface — record type matrix, validation rules, git staging procedures, pre-commit hook configuration, or directory structure — both SOPs must be updated in the same commit with aligned version numbers.

**Shared surfaces:**
- §3 Record Type Matrix ↔ Template SOP §3 Record Type → Schema → Template Mapping
- §6 Quality Checklist (pre-commit validation) ↔ Template SOP §6 Pre-Commit Hook v2
- §6 scoped `git add` path whitelist ↔ Template SOP §5 Step 5 scoped `git add`
- Non-Record Directories list (identical in both SOPs)

**Procedure:** Before committing a change to this SOP, check whether the change touches a shared surface. If yes, update the paired SOP in the same commit. If no (SOP-specific change like the v1.2 "that's it" trigger), an independent update is correct — no version-lock required.

**Field:** `paired_sops` in YAML frontmatter lists all SOPs that share governance surfaces with this SOP.

---

## 9. Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-08-04 | DAF (authority), Ember (drafter) | Initial institutionalization. Confirmation format standardized based on UITM (Aug 3) and CSM VoronDRQ GTM (Aug 4) intake precedents. |
| 1.1 | 2026-08-19 | DAF (authority), Laras (drafter) | §3 Record Type Matrix expanded from 9 to 18 types (added ART, ASSESS, BRIEF, DOC, DRAFT, LSN, OPP, ORG, PIR). Non-Record Directories section added. §6 `git add -A` replaced with scoped `git add` path whitelist (Lesson #6 enforcement). Taxonomy validation added to Quality Checklist as enforced step. `outcome.schema.json` created (was missing). Root cause: schemas expanded to 18 types but SOP never updated — recurring meta-pattern of canonical layer evolving without enforcement layer following. |
| 1.2 | 2026-08-20 | DAF (authority), Laras (drafter) | §5 "That's it" trigger added as standard modus operandi — session-level intake trigger. When DAF sends "that's it", the entire session is ingested as a CognitiveOS intake event. Institutionalized as always-on SOP. |
| 1.3 | 2026-08-21 | DAF (authority), Laras (drafter) | YAML `version` field corrected from stale 1.0 → 1.3 (was not updated through v1.1/v1.2 body changes). `GOV-TEMPLATE-DISCIPLINE-001` added to `related_records` (fixes asymmetric pairing — Template SOP already referenced Intake SOP). `paired_sops` field added to YAML frontmatter. §8 Paired SOP Version-Locking section added — mirrors Template SOP §8 Step 7 but broadens from new-record-type-specific to all shared-surface changes. Version-locking principle now visible from both SOPs. Root cause: LSN-20260821-005 — governance drift in paired SOPs. |
