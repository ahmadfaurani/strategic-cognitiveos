---
id: GOV-SOP-AV-001
record_type: document
title: "SOP-AV-001: Action Register Validation Standard — Cross-Evidence Reconciliation Protocol"
created_at: 2026-08-21 14:43:00+00:00
updated_at: 2026-08-21 14:43:00+00:00
owner: DAF
status: active
priority: critical
sensitivity: internal
lifecycle_state: canonical
confidence: high
tags:
  - deadline/gate-overdue
  - deadline/gate-passed
  - doctrine/adep-001
  - doctrine/cvs-master-framework
  - domain/action-management
  - domain/cognitiveos-operations
  - domain/data-infrastructure
  - domain/development-governance
  - domain/governance
  - domain/stakeholder-engagement
  - framework/action-validation
  - framework/cognitive-loop
  - framework/workflow-identification-protocol
  - outcome/evidence-missing
  - type/sop
  - type/validation-framework
source:
  type: direct
  reference: DAF directive via Telegram, 2026-08-21 14:43 UTC
summary: "Systematic validation protocol for reconciling CognitiveOS action records against all available evidence sources. Ensures action register status, ownership, and completion state match observed reality. Mandated after TAT review revealed 66% draft backlog with evidence of completed actions left in draft status."
---

# SOP-AV-001: Action Register Validation Standard

## Cross-Evidence Reconciliation Protocol

**Effective:** 2026-08-21
**Authority:** DAF
**Scope:** All CognitiveOS action records (ACT-*) and their status, ownership, deadline, and completion fields
**Frequency:** Weekly (every Monday 09:00 UTC+8, pre-review), plus ad-hoc on demand

---

## 1. Purpose

The action register drifts from reality because actions are completed through decisions, conversations, events, and formalisations without the corresponding ACT- record being updated. This SOP defines a systematic, repeatable validation process that cross-references every action against all available evidence sources and produces specific, actionable corrections.

**Principle:** No action status is trusted unless it can be corroborated by at least one independent evidence source, or explicitly confirmed as still-pending by absence of evidence.

---

## 2. Evidence Source Taxonomy

The validation protocol draws from 13 evidence source layers, ranked by authority:

### Tier A — Primary Evidence (direct proof of completion or status change)

| Source | Count | Path | Evidence Type |
|--------|-------|------|---------------|
| A1. Decision Records (DEC-) | 50 | `decisions/` | Formal decision that supersedes or fulfils an action's intent |
| A2. Document Records (DOC-) | 16 | `documents/` | Document whose creation IS the action's required output |
| A3. Commitment Records (COM-) | 16 | `commitments/` | Commitment that fulfils or negates an action |
| A4. Outcome Records (OUT-) | 3 | `outcomes/` | Recorded outcome that an action was targeting |

### Tier B — Corroborating Evidence (supports or refutes status)

| Source | Count | Path | Evidence Type |
|--------|-------|------|---------------|
| B1. Conversation Records (CONV-) | — | `conversations/` (via index) | Conversation where action was discussed, resolved, or assigned |
| B2. Engagement Records (ENG-) | 41 | `engagements/` | Stakeholder engagement that fulfils a relationship action |
| B3. Risk Records (RSK-) | 35 | `risks/` | Risk that blocks, supersedes, or is mitigated by an action |
| B4. Initiative Records (INIT-) | 34 | `initiatives/` | Initiative status change that implies action completion |
| B5. Assessment Records (ASSESS-) | 5 | `assessments/` | Assessment that evaluates or closes an action |

### Tier C — Contextual Evidence (ambience, requires interpretation)

| Source | Count | Path | Evidence Type |
|--------|-------|------|---------------|
| C1. Daily Memory Notes | 139 | `memory/YYYY-MM-DD*.md` | Chronological log of events, decisions, actions taken |
| C2. MEMORY.md | 1 | `MEMORY.md` | Curated long-term memory — distilled events |
| C3. Git Commit History | — | `git log` in strategic-cognitiveos | Commits that create/modify records implying action completion |
| C4. Indexes | 18 | `indexes/` | Cross-record index entries that show linkage |

### Tier D — Absence of Evidence (negative signal)

| Source | Evidence Type |
|--------|---------------|
| D1. No evidence found in any Tier A/B/C source after exhaustive search | Indicates action is genuinely still pending (or abandoned) |

---

## 3. Validation Rules

Each rule is numbered, has a clear trigger, evidence source, and required action.

### V1: Decision Supersession Rule

**Trigger:** A DEC- record exists whose `summary`, `decision`, or `rationale` field describes an outcome that fulfils the intent of an ACT- record.

**Evidence Source:** A1 (DEC-)

**Test:** For each ACT- in status `draft` or `active`:
1. Extract the action's `title`, `summary`, and `required_output`
2. Search all DEC- records for semantic overlap on: subject matter, stakeholder names, initiative IDs, product names
3. If a DEC- explicitly resolves, formalises, appoints, approves, or decides what the action was created to achieve → **FLAG: STATUS_MISMATCH**

**Required Correction:** Update ACT- status to `completed`, add `completion_evidence` field referencing the DEC- ID, add `completed_at` matching DEC- `created_at`.

**Example:** ACT-20260802-005 (formalise stakeholder management) → superseded by DEC-20260820-012 (SSE Lead formalisation). Corrected 2026-08-21.

---

### V2: Document Fulfilment Rule

**Trigger:** A DOC- record exists whose content IS the `required_output` specified in an ACT- record.

**Evidence Source:** A2 (DOC-)

**Test:** For each ACT- in status `draft` or `active` with a `required_output` field:
1. Extract the required output description
2. Search DOC- records for matching content (title, summary, subject area)
3. If a DOC- exists that satisfies the required output specification → **FLAG: OUTPUT_DELIVERED**

**Required Correction:** Update ACT- status to `completed`, add `completion_evidence` referencing the DOC- ID.

---

### V3: Commitment Resolution Rule

**Trigger:** A COM- record exists that either (a) fulfils or (b) negates the action's required commitment.

**Evidence Source:** A3 (COM-)

**Test:** For each ACT- in status `draft` or `active`:
1. Extract action's subject and owner
2. Search COM- records for matching subject, stakeholder, or commitment scope
3. If a COM- records a commitment that fulfils the action → **FLAG: COMMITMENT_FULFILLED**
4. If a COM- records a rejection or withdrawal that makes the action moot → **FLAG: ACTION_MOOT**

**Required Correction:** (a) Update to `completed` with COM- reference. (b) Update to `cancelled` with COM- reference and reason.

---

### V4: Outcome Achievement Rule

**Trigger:** An OUT- record exists that describes an outcome the action was created to produce.

**Evidence Source:** A4 (OUT-)

**Test:** For each ACT- in status `draft` or `active`:
1. Extract the action's `strategic_significance` and `mission_alignment`
2. Search OUT- records for matching outcomes
3. If an OUT- exists that corresponds to the action's intended result → **FLAG: OUTCOME_ACHIEVED**

**Required Correction:** Update to `completed` with OUT- reference.

---

### V5: Conversation Resolution Rule

**Trigger:** A CONV- record exists in which the action's subject was discussed and either (a) resolved, (b) assigned, (c) deferred with new date, or (d) cancelled.

**Evidence Source:** B1 (CONV-)

**Test:** For each ACT- in status `draft` or `active`:
1. Extract action title keywords, stakeholder names, and initiative references
2. Search CONV- records (via conversation-index) for matching conversations
3. If a conversation explicitly resolves, reassigns, or cancels the action → **FLAG: CONV_RESOLUTION**

**Required Correction:**
- Resolved → update to `completed` with CONV- reference
- Reassigned → update `owner` field, keep status
- Deferred → update `deadline` field, add CONV- reference
- Cancelled → update to `cancelled` with CONV- reference and reason

---

### V6: Stakeholder Engagement Rule

**Trigger:** An ENG- record exists that describes engagement activity fulfilling a relationship-management action.

**Evidence Source:** B2 (ENG-)

**Test:** For each ACT- whose title or tags include "stakeholder", "engagement", "relationship", "formalise", "schedule", "coordinate", "contact":
1. Extract the stakeholder/org name from the action
2. Search ENG- records for matching stakeholder and engagement type
3. If an ENG- records the engagement that the action was created to initiate → **FLAG: ENG_FULFILLED**

**Required Correction:** Update to `completed` with ENG- reference.

---

### V7: Risk Mitigation Rule

**Trigger:** A RSK- record exists whose mitigation or resolution implies an action's completion, OR whose creation supersedes an action (makes it unnecessary).

**Evidence Source:** B3 (RSK-)

**Test:** For each ACT- in status `draft` or `active`:
1. Check `related_records` for RSK- references
2. Search RSK- records for the action's ID in their `related_records` or `mitigation` fields
3. If a RSK- is marked `mitigated` or `closed` and the action was its mitigation → **FLAG: RSK_MITIGATED**
4. If a RSK- was created that supersedes the action (risk accepted, different path taken) → **FLAG: RSK_SUPERSEDES**

**Required Correction:** (a) Update to `completed`. (b) Update to `cancelled` with RSK- reference.

---

### V8: Initiative Status Implied Rule

**Trigger:** An INIT- record's status changes in a way that implies actions under it should be updated.

**Evidence Source:** B4 (INIT-)

**Test:** For each ACT- with a `related_initiative` field:
1. Look up the INIT- record
2. If INIT- status is `completed`, `cancelled`, or `paused`:
   - `completed` → check if all child ACT- should be `completed`
   - `cancelled` → check if all child ACT- should be `cancelled`
   - `paused` → check if child ACT- deadlines should be extended
3. If mismatch found → **FLAG: INIT_STATUS_DRIFT**

**Required Correction:** Update child ACT- statuses to match parent INIT- status, with INIT- reference.

---

### V9: Daily Memory Event Rule

**Trigger:** A daily memory note describes an event, decision, or action taken that fulfils, supersedes, or cancels an ACT- record — but the ACT- was not updated.

**Evidence Source:** C1 (daily notes)

**Test:** For each ACT- in status `draft` or `active`:
1. Extract action title keywords, owner name, and date range (created → deadline)
2. Search daily memory notes from created date onward for:
   - Action ID explicit mention
   - Semantic match on title + subject (keyword overlap)
   - Owner name + action verb matching (e.g., "Hadri confirmed...", "Aisha appointed...")
3. If a daily note describes completion of the action's intent → **FLAG: MEMORY_EVIDENCE**

**Required Correction:** Update to `completed` with daily note date reference. Add `completion_evidence` summarising the memory note entry.

---

### V10: MEMORY.md Distilled Evidence Rule

**Trigger:** MEMORY.md contains a curated entry that describes completion or formalisation of something an ACT- record was created to achieve.

**Evidence Source:** C2 (MEMORY.md)

**Test:** For each ACT- in status `draft` or `active`:
1. Extract action title and subject keywords
2. Search MEMORY.md for matching content
3. If MEMORY.md describes the action as done, formalised, or resolved → **FLAG: MEMORY_DISTILLED**

**Required Correction:** Update to `completed` with MEMORY.md section reference.

---

### V11: Git Commit Evidence Rule

**Trigger:** A git commit in strategic-cognitiveos creates or modifies records that imply an action's completion, but the action record itself was not updated in the same commit.

**Evidence Source:** C3 (git log)

**Test:** For each ACT- in status `draft` or `active`:
1. Search git log for commits mentioning the action's subject, stakeholders, or initiative
2. Check if commits create DEC-, DOC-, OUT-, or ENG- records that fulfil the action
3. If found → **FLAG: COMMIT_EVIDENCE**

**Required Correction:** Update to `completed` with commit hash reference.

---

### V12: Owner Status Drift Rule

**Trigger:** An action's owner has been formally changed (role appointment, reassignment, departure) but the ACT- record still shows the original owner.

**Evidence Source:** A1 + C1 + C2 (DEC-, daily notes, MEMORY.md)

**Test:** For each ACT- record:
1. Extract `owner` field
2. Check for DEC- records appointing the owner to a new role (which may change their capacity)
3. Check for DEC- records reassigning the action's scope to a different person
4. If owner has changed or role context has shifted → **FLAG: OWNER_DRIFT**

**Required Correction:** Update `owner` field, add `previous_owner` note, reference the DEC- that drove the change.

---

### V13: Deadline Staleness Rule

**Trigger:** An action has a deadline that has passed, but its status is not `overdue` (or equivalent explicit acknowledgement).

**Evidence Source:** D1 (absence of evidence — no completion evidence found)

**Test:** For each ACT- with a `deadline` field:
1. Compare deadline to current date
2. If deadline < now AND status not in (`completed`, `validated`, `cancelled`) → **FLAG: DEADLINE_STALE**
3. If no evidence of completion found in any Tier A/B/C source → **FLAG: GENUINELY_PENDING**

**Required Correction:**
- If genuinely pending: update status to `overdue` or `blocked`, add explanation
- If completed but not recorded: process through V1-V11 rules first
- If no longer relevant: update to `cancelled` with reason

---

### V14: Orphan Action Rule

**Trigger:** An action has no `related_records`, no `related_initiative`, and no evidence of being referenced by any other CognitiveOS record.

**Evidence Source:** C4 (indexes) + D1 (absence)

**Test:** For each ACT- record:
1. Check `related_records` and `related_initiative` fields
2. Search all index files for the action's ID
3. Search all other record types for references to this action
4. If no links found in either direction → **FLAG: ORPHAN**

**Required Correction:** Either (a) link to parent initiative/decision, or (b) mark for archival review. Orphan actions with no strategic context should be archived.

---

### V15: Duplicate/Superseded Action Rule

**Trigger:** Two or more ACT- records describe the same or substantially similar intent, where a later one supersedes an earlier one.

**Evidence Source:** All tiers

**Test:** For each pair of ACT- records with >60% title/summary keyword overlap:
1. Check if the later action's creation date is after the earlier action's
2. Check if the later action references the earlier one
3. If not explicitly linked but semantically superseded → **FLAG: DUPLICATE**

**Required Correction:** Mark the earlier action as `superseded` with reference to the later action. Update the later action's `related_records` to include the earlier one.

---

## 4. Severity Classification

Each flag has a severity that determines priority of correction:

| Severity | Definition | Response Time | Examples |
|----------|-----------|---------------|----------|
| **S1 — CRITICAL** | Action recorded as pending but evidence shows it's completed | 24h | V1, V2, V3 with DEC-/DOC-/COM- evidence |
| **S2 — HIGH** | Action owner or deadline is wrong, creating false reporting | 48h | V12, V13 |
| **S3 — MEDIUM** | Action is orphaned, duplicated, or lacks proper linkages | 1 week | V14, V15 |
| **S4 — LOW** | Action may be stale but no clear evidence of completion | Next review | V9, V10 with ambiguous evidence |

---

## 5. Validation Procedure

### 5.1 Automated Scan (Weekly — Monday 08:00 UTC+8)

Run validation script (TBD — `tools/action-validator/validate-actions.sh`) that:
1. Loads all ACT- records (frontmatter extraction)
2. Loads all DEC-, DOC-, COM-, OUT-, ENG-, RSK- records
3. Runs rules V1-V4, V7, V8, V13, V14, V15 (deterministic matching)
4. Outputs flagged items in structured format

### 5.2 Semantic Cross-Check (Weekly — Monday 08:30 UTC+8)

Manual or AI-assisted review that:
1. Takes the flagged list from 5.1
2. Runs rules V5, V6, V9, V10, V11, V12 (requires semantic interpretation)
3. For each flag, determines: CONFIRMED (clear evidence) / PROBABLE (strong but ambiguous) / NEEDS_REVIEW (insufficient evidence)
4. Produces correction list

### 5.3 Correction Application (Weekly — Monday 09:00 UTC+8)

For each CONFIRMED flag:
1. Update the ACT- record with correct status, dates, references
2. Add `validation_note` field: `Validated per SOP-AV-001 rule V<N> on YYYY-MM-DD. Evidence: <source reference>`
3. Commit with message: `fix(action): SOP-AV-001 V<N> — <ACT-ID> status correction (evidence: <source>)`
4. Push

For each PROBABLE flag:
1. Present to DAF for confirmation at Monday review
2. Apply correction if confirmed

For each NEEDS_REVIEW flag:
1. Present to DAF for manual determination
2. Log as unresolved question in `indexes/unresolved-questions.md`

### 5.4 Validation Report Format

Each weekly validation produces a report:

```
SOP-AV-001 VALIDATION REPORT — YYYY-MM-DD
=========================================
Actions scanned: 145
Evidence sources: DEC-(50), DOC-(16), COM-(16), OUT-(3), ENG-(41), RSK-(35), INIT-(34), daily notes (139), MEMORY.md, git log, indexes (18)

Flags raised: N
  S1 CRITICAL:  X
  S2 HIGH:      Y
  S3 MEDIUM:    Z
  S4 LOW:       W

Corrections applied: N (auto), M (DAF-approved)
Records updated: <list of ACT- IDs with before→after status>

Remaining flags: <list with NEEDS_REVIEW status>
```

---

## 6. Audit Trail

All validation runs and corrections are logged:
- **Path:** `logs/validation-YYYY-MM-DD.md`
- **Content:** Full flag list, evidence references, corrections applied, DAF approvals, unresolved items
- **Retention:** 90 days, then archive

---

## 7. Exclusion Criteria

Actions are excluded from validation if:
- `status: cancelled` — no longer needs validation
- `lifecycle_state: archived` — historical record only
- `created_at` > 90 days ago AND no deadline AND no related_records — candidate for archival, not validation

---

## 8. Rule Conflict Resolution

When multiple rules flag the same action with conflicting corrections:
1. Higher-tier evidence wins (Tier A > Tier B > Tier C)
2. More recent evidence wins (later DEC- over earlier daily note)
3. Explicit evidence wins over inferred (DEC- saying "formalise X" > daily note mentioning X)
4. If still ambiguous → escalate to DAF

---

## 9. Performance Metrics

The validation protocol itself is measured:

| Metric | Target | Measurement |
|--------|--------|-------------|
| Drift rate | <5% | % of actions with status mismatch after validation |
| Validation coverage | 100% | % of non-excluded actions validated per cycle |
| Correction latency | <24h (S1), <48h (S2) | Time from flag to correction applied |
| False positive rate | <10% | % of auto-flags rejected by semantic review |
| Repeat flags | <5% | % of flags raised for same action in consecutive cycles |

---

## 10. Implementation Roadmap

| Phase | Timeline | Scope |
|-------|----------|-------|
| Phase 1: Manual validation | Immediate (this session) | Run all 15 rules against current 145 actions, produce correction list |
| Phase 2: Semi-automated script | 1 week | `validate-actions.sh` for deterministic rules (V1-V4, V7, V8, V13, V14, V15) |
| Phase 3: Full automation | 2 weeks | Semantic matching via Honcho/AI for rules V5, V6, V9-V12 |
| Phase 4: Continuous validation | 1 month | Run on every intake event, not just weekly |

---

## 11. Relationship to Existing Frameworks

| Framework | Relationship |
|-----------|-------------|
| Intake SOP (9-step) | Step 6 (update indexes) should trigger SOP-AV-001 for any new ACT- |
| CVS Master Framework | Validation evidence is subject to CVS tiering (DEC- = L2, daily note = L2, MEMORY.md = L5) |
| WIP Protocol (7-day TAT) | Deadline staleness rule (V13) enforces WIP TAT standard |
| ADEP-001 | This SOP is a D2 task (governance process, has dependencies on record system) |
| SOP-CL-001 (Cognitive Loop Review) | Weekly review should include validation report as standing agenda item |

---

## 12. Version Control

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-08-21 | Initial creation. 15 validation rules, 4 severity levels, 4-phase implementation roadmap. Triggered by TAT review revealing ACT-20260802-005 status mismatch. |
