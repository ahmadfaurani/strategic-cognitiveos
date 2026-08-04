# CognitiveOS Intake SOP — Standard Operating Procedure

> **Version:** 1.0  
> **Authority:** Ahmad Faurani Jaafar (DAF)  
> **Status:** Active — institutionalized 2026-08-04  
> **Scope:** All CognitiveOS ingestion events, all sessions, all agents  
> **Related:** `governance/contribution-standard.md`, `AI-PROCESSOR-INSTRUCTIONS.md`, `schemas/`

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

```bash
cd strategic-cognitiveos
git add -A
git commit -m "CognitiveOS: <brief description> — <record count> records

New records:
- <ID> — <title>
- <ID> — <title>

Indexes updated: <list>"
```

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

---

## 6. Quality Checklist (Pre-Commit)

Before committing any intake:

```
[ ] All records have permanent IDs following the convention
[ ] All mandatory schema fields are completed
[ ] All records have owners assigned
[ ] All records have sensitivity classified
[ ] All tags are from controlled taxonomy
[ ] All related records are cross-linked
[ ] All relevant indexes are updated
[ ] Daily memory log entry written
[ ] Commit message follows the standard format
[ ] Confirmation notification prepared
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

## 8. Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-08-04 | DAF (authority), Ember (drafter) | Initial institutionalization. Confirmation format standardized based on UITM (Aug 3) and CSM VoronDRQ GTM (Aug 4) intake precedents. |
