---
id: GOV-PIR-CLOSURE-001
record_type: document
title: PIR Closure Framework
created_at: 2026-08-17 16:36:00+00:00
updated_at: '2026-08-17T17:50:23+00:00'
owner: DAF
authority: ADEP-001 §44 (Closure Gate) — derivative instrument for PIR-level closure
classification: CANONICAL
supersedes: N/A
related:
- closure-gate-checklist.md (initiative-level closure)
- pir.schema.json (status enum)
- pir-inventory-index.md (PIR inventory)
- process-maturity-register.md (readiness gates)
- 03-VERIFICATION/CVS-FRAMEWORK.md (CVS Master Framework)
tags:
- governance/pir
- governance/closure
- workstream/cscdc
- cvs/applied
status: active
priority: medium
sensitivity: confidential
lifecycle_state: active
confidence: medium
source:
  type: null
  reference: null
summary: 'Purpose: Define the formal process by which an individual Priority Intelligence Requirement (PIR) transitions from active collection to a terminal state — fulfilled, cancelled, superseded, or deferred'
strategic_significance: 'Document record. Priority: None.'
mission_alignment: []
related_records: []
---

# PIR Closure Framework

**Purpose:** Define the formal process by which an individual Priority Intelligence Requirement (PIR) transitions from active collection to a terminal state — fulfilled, cancelled, superseded, or deferred — with auditable evidence and record-layer synchronisation.

**CVS Framework:** This document is validated per `03-VERIFICATION/CVS-FRAMEWORK.md` (Master Framework, TLP:AMBER). Claim IDs: `CVS-COG-NNN`. Rule 6 applies — AI-generated claims capped at T2 / score 7. See §14 for CVS Compliance Statement and Evidence Register cross-references.

**Relationship to existing instruments:**

| Instrument | Scope | This Framework |
|-----------|-------|----------------|
| Closure Gate Checklist (16-point) | Initiative/workstream closure | PIR-level closure is a **prerequisite input** `[ASSESSMENT]` — all PIRs associated with an initiative must be in a terminal state before the 16-point gate can be initiated |
| PIR Schema (`pir.schema.json`) | Data model — defines allowed status values | This framework defines the **transition rules** between those statuses |
| PIR Inventory Index | Register of all PIRs | This framework governs how inventory status fields are updated |
| Intake SOP (9-step) | How records are created | This framework governs how records are **closed** |

> `[SOURCE: closure-gate-checklist.md, Governing Framework field, 2026-08-16]` — ADEP-001 §44 governs the 16-point Closure Gate.

---

## 1. Problem Statement

**Identified gap (PIR Status Report 2026-08-03):** 90 of 120 PIRs `[SOURCE-BACKED]` were intelligence-resolved or partially resolved, but only 1 PIR `[SOURCE-BACKED]` reflected that truth in its source record. The intelligence layer (cron collection output) and the record layer (source `.md` files) are decoupled. There is no formal process for:

1. Determining when a PIR is genuinely "fulfilled" vs merely "has intelligence about it"
2. Transitioning PIR status in the source record from "Open" to a terminal state
3. Handling PIRs that are structurally unresolvable via the current collection method (OSINT)
4. Preventing stale PIRs from accumulating indefinitely

This framework closes that gap.

> **Sources (L2 — Internal validated records):**
> - `pir-status-report-2026-08-03.md#L36` — cumulative intelligence signal: 90/120 (75%)
> - `pir-status-report-2026-08-03.md#L37` — 1 of 120 PIRs formally marked non-Open in source records
> - `pir-status-report-2026-08-03.md#L46` — 90 PIRs intel-confirmed but marked Open in record layer
> - `pir-inventory-index.md#L29` — Total PIRs = 120

---

## 2. PIR Lifecycle States

The PIR schema defines 20 status values `[SOURCE-BACKED]`. This framework organises them into **five lifecycle phases** `[ASSESSMENT]` (structural design based on schema analysis).

> `[SOURCE: pir.schema.json, properties.status.enum, verified programmatically 2026-08-17]` — 20 status values confirmed.
> `[SOURCE: CVS-SOURCE-REGISTER.md, L2 — Strategic CognitiveOS records]` — PIR schema is an L2 internal validated source.

```
                    ┌─────────────────────────────────────────────────────────┐
                    │                   COLLECTION PHASE                      │
                    │  open → in-progress → validated                        │
                    └───────────────┬─────────────────────┬───────────────────┘
                                    │                     │
                    ┌───────────────▼──────┐  ┌──────────▼──────────────┐
                    │   CLOSURE CANDIDATE   │  │     METHOD ESCALATION    │
                    │  (fulfilment review)  │  │  (OSINT→HUMINT/defer)    │
                    └──┬──────┬──────┬─────┘  └──────────┬───────────────┘
                       │      │      │                    │
                ┌──────▼┐  ┌──▼───┐ ┌▼────────┐  ┌───────▼────┐
                │FULFILL│  │CANC. │ │SUPERSEDE│  │  DEFERRED  │
                └───────┘  └──────┘ └─────────┘  └──────┬────┘
                                                    ┌─────▼─────┐
                                                    │  REOPENED │
                                                    │(re-enter  │
                                                    │collection)│
                                                    └───────────┘
```

### Phase 1: Collection (Active)

| Status | Meaning | Entry Condition |
|--------|---------|-----------------|
| `open` | PIR created, no intelligence collected yet | PIR registered in inventory |
| `in-progress` | Active collection underway, partial intelligence gathered | First intelligence signal received |
| `validated` | Intelligence sufficient to answer the PIR question; ready for fulfilment review | Collection agent assesses PIR as "Resolved" |

### Phase 2: Closure Candidate (Review)

| Status | Meaning | Entry Condition |
|--------|---------|-----------------|
| `ready_for_review` | Intelligence is sufficient; awaiting authority review before formal closure | Collection agent recommends closure |
| `ready_for_submission` | Reviewed and endorsed; awaiting final sign-off | Reviewer (Ember) endorses |

### Phase 3: Terminal States (Closed)

| Status | Meaning | Entry Condition |
|--------|---------|-----------------|
| `fulfilled` | The intelligence question has been answered with sufficient evidence | Authority sign-off (§6) |
| `cancelled` | The PIR is no longer relevant (context changed, question moot) | Authority decision |
| `superseded` | Replaced by a new PIR or a restructured intelligence requirement | New PIR created with explicit reference |
| `archived` | Terminal state reached; record preserved for historical reference | Any terminal state + 30 days elapsed |

### Phase 4: Suspension States

| Status | Meaning | Entry Condition |
|--------|---------|-----------------|
| `deferred` | PIR cannot be resolved via current collection method; parked with a review date | Method escalation exhausted (§5) |
| `blocked` | PIR resolution is blocked by a dependency; tracked for unblocking | Dependency identified and logged |
| `overdue` | PIR has exceeded its SLA (§7) without reaching a terminal state | SLA timer expires |

### Phase 5: Reopening

| Status | Meaning | Entry Condition |
|--------|---------|-----------------|
| `identified` / `proposed` | A deferred/blocked PIR is reactivated with new collection method or unblocked dependency | Review date reached OR new method available OR dependency resolved |

---

## 3. Closure Criteria

### 3.1 Fulfilled (Primary Closure Path)

A PIR may be marked `fulfilled` when **ALL** of the following are true:

| Criterion | Evidence Required | Verification |
|-----------|-------------------|--------------|
| **C1: Intelligence answers the question** | The collected intelligence directly addresses the PIR's stated information gap | Collection agent assessment + source citation |
| **C2: Source quality scored** | At least one source meets L1 (primary/official) or L2 (internal validated) per CVS Master Framework §3 | Source URL or document reference with L-tier |
| **C3: Confidence scored** | CVS 5-criteria confidence score assessed (authority, traceability, recency, consistency, completeness — 0-2 each, total 0-10) | Score breakdown recorded in Evidence Register |
| **C4: No contradiction** | No unresolved contradictory evidence from other sources | If contradiction exists, it is documented and resolved (T5 → resolution) |
| **C5: Record updated** | The PIR's source record (`.md` file) is updated with findings, sources, and status change | File modified + committed |
| **C6: Inventory index updated** | The PIR Inventory Index reflects the new status | Index file updated + committed |

**Minimum evidence by priority** `[ASSESSMENT]` (thresholds designed to align with CVS Master Framework §3 Source Reliability Hierarchy):

| PIR Priority | Min. Source Level | Min. Confidence Score | Independent Sources |
|-------------|-------------------|-----------------------|---------------------|
| 🔴 Critical | L1 (official/system-of-record) | ≥8 (High) | 2 |
| 🟠 High | L1 or L2 | ≥5 (Medium) | 2 |
| 🟡 Medium | L2 or L3 | ≥5 (Medium) | 1 |
| ⚪ Low | L3+ | ≥3 (Low) | 1 |

> `[SOURCE: CVS-FRAMEWORK.md §3, L1-L5 Source Reliability Hierarchy, 2026-08-04]` — Source levels and their trust ratings.
> `[SOURCE: CVS-FRAMEWORK.md §5, Confidence Score 5-criteria model, 2026-08-04]` — Scoring rubric (0-10).

### 3.2 Cancelled

A PIR may be marked `cancelled` when:

- The underlying initiative or opportunity it supports has been cancelled
- The intelligence question has become moot due to context change (e.g., agency restructured, programme discontinued)
- The PIR was duplicate or erroneously created

**Evidence required:** Brief justification referencing the triggering event or decision.

### 3.3 Superseded

A PIR may be marked `superseded` when:

- A new PIR replaces it with a refined or broadened scope
- The intelligence requirement has been restructured

**Evidence required:** Reference to the superseding PIR ID. The new PIR must link back to the superseded one in its `related_records` field.

### 3.4 Deferred

A PIR may be marked `deferred` when:

- The collection method (e.g., OSINT) is structurally insufficient to resolve it
- The PIR requires HUMINT, internal enquiry, or a method not currently available
- A dependency (e.g., a meeting, a decision) must occur before intelligence can be collected

**Evidence required:**
- Statement of why current method is insufficient
- Identified alternative method or dependency
- **Review date** (mandatory) — the PIR must be revisited by this date

**Maximum deferral period** `[ASSUMPTION]` (designed to prevent indefinite parking; calibrated to priority urgency):

| PIR Priority | Max Deferral | Review Trigger |
|-------------|-------------|----------------|
| 🔴 Critical | 30 days | `[ASSUMPTION]` Automatic reopen to `identified` on day 31 (requires CJ-7 enforcement logic not yet implemented) |
| 🟠 High | 60 days | `[ASSUMPTION]` Automatic reopen on day 61 (requires CJ-7 enforcement logic not yet implemented) |
| 🟡 Medium | 90 days | `[ASSUMPTION]` Automatic reopen on day 91 (requires CJ-7 enforcement logic not yet implemented) |
| ⚪ Low | 180 days | `[ASSUMPTION]` Automatic reopen on day 181 (requires CJ-7 enforcement logic not yet implemented) |

---

## 4. Status Transition Matrix

| From → | open | in-progress | validated | ready_for_review | ready_for_submission | fulfilled | cancelled | superseded | deferred | blocked | overdue |
|--------|------|-------------|-----------|-------------------|---------------------|----------|-----------|------------|----------|---------|---------|
| **open** | — | ✓ | ✗ | ✗ | ✗ | ✗ | ✓ | ✓ | ✓ | ✓ | ✓ (SLA) |
| **in-progress** | ✗ | — | ✓ | ✗ | ✗ | ✗ | ✓ | ✓ | ✓ | ✓ | ✓ (SLA) |
| **validated** | ✗ | ✗ | — | ✓ | ✗ | ✗ | ✓ | ✓ | ✓ | ✗ | ✗ |
| **ready_for_review** | ✗ | ✗ | ✗ (reject) | — | ✓ | ✗ | ✓ | ✓ | ✗ | ✗ | ✗ |
| **ready_for_submission** | ✗ | ✗ | ✗ | ✗ (reject) | — | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ |
| **fulfilled** | ✗ | ✗ | ✗ | ✗ | ✗ | — (archived after 30d) | ✗ | ✗ | ✗ | ✗ | ✗ |
| **deferred** | ✗ | ✓ (reopen) | ✗ | ✗ | ✗ | ✗ | ✓ | ✓ | — | ✗ | ✗ |
| **blocked** | ✗ | ✓ (unblock) | ✗ | ✗ | ✗ | ✗ | ✓ | ✓ | ✓ | — | ✗ |
| **overdue** | ✗ | ✓ | ✗ | ✗ | ✗ | ✗ | ✓ | ✓ | ✓ | ✓ | — |

**Rejection path:** `ready_for_review` → `in-progress` (back to collection with identified gap). `ready_for_submission` → `ready_for_review` (back to review with identified concern).

---

## 5. OSINT-Unresolvable Escalation Protocol

PIRs that are structurally unresolvable via OSINT `[SOURCE-BACKED]` (identified as "Tier 1" in the Aug 3 status report — 12 PIRs including 3 Critical) follow this protocol:

> `[SOURCE: pir-status-report-2026-08-03.md#L176, 2026-08-03]` — Tier 1 Structurally OSINT-unresolvable: 12 PIRs.
> `[SOURCE: pir-status-report-2026-08-03.md#L86, 2026-08-03]` — 3 Critical PIRs remain genuinely OPEN, all OSINT-unresolvable.
> `[SOURCE: pir-status-report-2026-08-03.md#L69-72, 2026-08-03]` — PIR-CSCDC-002, PIR-INIT-CSCDC-001, PIR-INIT-CSCDC-003 individually assessed as OSINT-unresolvable.

```
open/in-progress
    │
    │  (collection agent identifies structural barrier
    │   after ≥2 complete collection cycles)
    ▼
blocked (dependency = "OSINT-insufficient")
    │
    │  (method escalation assessment)
    ├──▶ HUMINT available? → deferred (review date = HUMINT tasking date)
    ├──▶ Internal enquiry possible? → deferred (review date = enquiry date)
    ├──▶ Decision pending? → deferred (review date = decision ETA)
    └──▶ No alternative method? → cancelled (justification: "structurally unresolvable, no alternative method identified")
```

**Structural barrier criteria** (must meet ALL):
1. Collection agent has attempted resolution across ≥2 complete collection cycles
2. The information sought is confirmed as internal/non-public (not merely undiscovered)
3. No alternative OSINT approach is identified (e.g., different source, different angle)

**Escalation output:** The blocked PIR's record must include:
- Which collection cycles attempted resolution
- Why the information is assessed as non-public
- What alternative method would resolve it (HUMINT, internal enquiry, etc.)
- Recommended action for DAF

---

## 6. Roles & Authority

| Role | Responsibility | Authority |
|------|---------------|-----------|
| **Collection Agent (CJ-1 through CJ-6)** | Collect intelligence, assess PIR as resolved/partial/open, recommend closure | Recommend `validated` status |
| **PIR Status Tracker (CJ-7)** | Meta-monitor; reconcile intelligence-layer assessments against record-layer; flag sync gaps; generate weekly status report | Recommend `ready_for_review` |
| **Ember (Reviewer)** | Review closure candidates; verify evidence quality, source levels, confidence scores; endorse or reject | Endorse to `ready_for_submission` or reject to `in-progress` |
| **DAF (Authority)** | Final sign-off on PIR closure; approve cancellations, supersessions, deferrals | Sign-off to `fulfilled` / `cancelled` / `superseded` / `deferred` |

**Authority exceptions** `[ASSESSMENT]` (operational design choice to balance throughput with oversight; Low/Medium PIRs are lower-risk to auto-close):
- Low-priority PIRs (`low`) may be auto-fulfilled by Ember after review without DAF sign-off, subject to weekly audit in the PIR Status Report.
- Medium-priority PIRs may be auto-fulfilled by Ember if confidence score ≥8 and source quality is L1/L2, subject to weekly audit.
- Critical and High PIRs **always** require DAF sign-off.

> **CVS Rule 6 note:** Ember auto-fulfilment of Low/Medium PIRs constitutes AI-generated validation. Per CVS Master Framework §7 Rule 6, these remain T2 (max score 7) until DAF review upgrades to T1. Weekly audit provides the human review path.

---

## 7. SLA Framework

### Time-to-First-Intelligence (TTFI) `[ASSUMPTION]`

> `[ASSUMPTION]` Designed targets, not empirically derived from historical collection data. Calibrated to priority urgency. Targets to be refined after first month of operational data.

| Priority | Target TTFI | Escalation if missed |
|----------|-------------|---------------------|
| 🔴 Critical | 3 days | Flag in next PIR Status Report |
| 🟠 High | 7 days | Flag in next PIR Status Report |
| 🟡 Medium | 14 days | No escalation |
| ⚪ Low | 30 days | No escalation |

### Time-to-Closure (TTC) `[ASSUMPTION]`

> `[ASSUMPTION]` Designed targets. The 30/60/90/180 hard limits mirror the deferral maxima in §3.4 for consistency. Targets to be refined after first month of operational data.

| Priority | Target TTC (from open to terminal) | Max TTC (hard limit) |
|----------|-----------------------------------|---------------------|
| 🔴 Critical | 14 days | 30 days (`[ASSUMPTION]` auto-escalate to `overdue` — requires CJ-7 enforcement logic) |
| 🟠 High | 30 days | 60 days |
| 🟡 Medium | 60 days | 90 days |
| ⚪ Low | 90 days | 180 days |

**Overdue auto-escalation** `[ASSUMPTION]`: PIRs exceeding their Max TTC are automatically marked `overdue` (requires CJ-7 timer enforcement not yet implemented) and flagged in the next PIR Status Report with:
- Days overdue
- Collection cycles attempted
- Recommended action (escalate method, defer, or cancel)

---

## 8. Record Synchronisation Protocol

This is the procedure that closes the intelligence-layer ↔ record-layer gap:

```
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│  INTELLIGENCE   │     │   SYNC PROCESS   │     │   RECORD LAYER  │
│     LAYER       │     │                  │     │                 │
│ (cron output)   │     │ (CJ-7 triggers)  │     │ (source .md)    │
│                 │     │                  │     │                 │
│ "PIR-X RESOLVED"├────▶│ 1. Match PIR ID  │────▶│ Update status   │
│ "source: URL"   │     │ 2. Verify evidence│     │ Add findings    │
│ "score: 7/10"   │     │ 3. Check criteria │     │ Add sources     │
│                 │     │ 4. Write to record│     │ Add score       │
│                 │     │ 5. Update index   │     │ Update timestamp│
│                 │     │ 6. Commit + push  │     │                 │
└─────────────────┘     └──────────────────┘     └─────────────────┘
```

### Sync Procedure (Step-by-Step)

1. **Trigger:** CJ-7 weekly report identifies PIRs with intelligence-layer status ≠ record-layer status
2. **Match:** For each mismatched PIR, locate its source record file
3. **Verify:** Check that intelligence findings meet closure criteria (§3.1)
4. **Write:** Update the PIR section in the source record with:
   - Status change (e.g., `open` → `fulfilled`)
   - Intelligence summary
   - Source citations with L-tier (`[SOURCE: name, URL, date]`)
   - CVS confidence score (5-criteria breakdown)
   - Last collected timestamp
5. **Update index:** Update the PIR Inventory Index with new status
6. **Commit:** Git commit with message: `pir(closure): PIR-ID status → fulfilled [CVS: <tier>, score: <n>/10]`
7. **Push:** Push to GitHub
8. **Confirm:** Log sync in CJ-7 report (synced count / total gap)

### Sync Priority Order

1. Critical PIRs (all 16 `[SOURCE-BACKED]`) — sync first, every cycle
2. High PIRs resolved in intelligence layer — sync within 1 week
3. Medium PIRs — sync within 2 weeks
4. Low PIRs — sync during monthly review

> `[SOURCE: pir-inventory-index.md#L25, 2026-07-25]` — Critical = 16 (13.3%).
> `[SOURCE: pir-inventory-index.md#L117, 2026-07-25]` — All 16 Critical PIRs covered by CJ-1 through CJ-6.

---

## 9. Audit Trail

Every PIR closure must produce:

| Artifact | Location | Content |
|----------|----------|---------|
| **Closure record** | PIR section in source `.md` file | Status, findings, sources (with L-tier), confidence score, closure date, authority |
| **CVS Evidence Register entry** | `03-VERIFICATION/CVS-EVIDENCE-REGISTER.csv` | New row: claim_id, tier, validation_status, confidence_score + 5-criteria breakdown |
| **Git commit** | Git history | `pir(closure): PIR-ID status → <terminal> [CVS: <tier>, score: <n>/10]` |
| **Index update** | `pir-inventory-index.md` | Status column updated |
| **Weekly report entry** | CJ-7 PIR Status Report | Closure logged in "PIRs closed this period" section |

**Audit checklist (for weekly review):**
- [ ] All newly-closed PIRs have CVS Evidence Register entries
- [ ] All source records match intelligence layer
- [ ] No PIR is in a terminal state without authority sign-off (except auto-fulfilled Low/Medium per §6 — T2 until human review)
- [ ] All deferred PIRs have review dates within the maximum deferral period
- [ ] No PIR has been in `overdue` status for more than 7 days without escalation
- [ ] All T2 claims >5 days pending reviewed for re-assessment (CVS §12)

---

## 10. Integration with Initiative Closure

**Rule:** An initiative cannot enter the 16-point Closure Gate (§44 ADEP-001) until ALL its associated PIRs are in a terminal state (`fulfilled`, `cancelled`, `superseded`, or `deferred`).

**Exception:** Deferred PIRs with a documented review date and accepted residual risk may proceed to closure if DAF explicitly approves.

**Pre-closure PIR audit:** Before initiating the 16-point gate, Ember runs a PIR audit:
1. List all PIRs associated with the initiative
2. Check each PIR's status in both intelligence layer and record layer
3. Flag any non-terminal PIRs
4. For each non-terminal PIR, recommend: close (evidence is sufficient), defer (method gap), or cancel (moot)
5. Resolve all PIRs to terminal state before proceeding

---

## 11. Metrics & KPIs

| Metric | Target | Source |
|--------|--------|--------|
| PIR closure rate (per month) | `[ASSUMPTION]` ≥70% of PIRs aged >30 days (designed target, no baseline data yet) | CJ-7 monthly summary |
| Sync gap (intel-layer vs record-layer) | ≤0 PIRs mismatched (current gap: 90 `[SOURCE-BACKED]` per `pir-status-report-2026-08-03.md#L46`) | CJ-7 weekly report |
| Average TTC by priority | Within SLA (§7) | CJ-7 monthly summary |
| Deferred PIRs with review dates | 100% | PIR inventory audit |
| Overdue PIRs (auto-escalated) | 0 sustained >7 days | CJ-7 weekly report |
| Evidence quality compliance | 100% of closed PIRs meet §3.1 source requirements | Monthly audit |
| CVS Evidence Register population | 100% of closed PIRs have register entries | Monthly audit |

---

## 12. Quick Reference — Closure Decision Tree

```
Is the PIR's intelligence question answered?
├── YES → Are closure criteria met (§3.1)?
│        ├── YES → Is priority Critical/High?
│        │        ├── YES → DAF sign-off → fulfilled (T1 after human review)
│        │        └── NO  → Ember auto-fulfil → fulfilled (T2, max score 7 — Rule 6)
│        └── NO  → Back to collection (in-progress)
│
├── PARTIAL → Continue collection OR assess if partial is sufficient
│            └── Sufficient for decision? → fulfilled with MEDIUM confidence (T2)
│
└── NO → Is OSINT structurally insufficient (§5)?
         ├── YES → Escalate method → deferred (with review date)
         └── NO  → Continue collection
                  └── SLA exceeded? → overdue → escalate in report
```

---

## 13. Implementation Roadmap

| Phase | Action | Owner | Target |
|-------|--------|-------|--------|
| **1. Ratification** | DAF reviews and approves this framework | DAF | `[ASSUMPTION]` Aug 18, 2026 (pending DAF availability) |
| **2. Schema alignment** | Verify `pir.schema.json` status enum covers all lifecycle states `[SOURCE-BACKED: all 14 framework statuses exist in schema's 20-value enum, verified 2026-08-17]`; `ready_for_review`, `ready_for_submission` confirmed present | Ember | `[ASSUMPTION]` Aug 19, 2026 |
| **3. CJ-7 integration** | Update CJ-7 weekly report template to include closure tracking + CVS Evidence Register columns | Ember | `[ASSUMPTION]` Aug 19, 2026 |
| **4. Sync pass** | Run the first full sync pass: update all 120 PIRs `[SOURCE-BACKED]` in source records per intelligence-layer status; create CVS Evidence Register entries for each closed PIR | Ember | `[ASSUMPTION]` Aug 20-24, 2026 |
| **5. Stale PIR triage** | Apply §5 escalation protocol to all Tier-1 OSINT-unresolvable PIRs (12 `[SOURCE-BACKED]` identified Aug 3) | Ember → DAF | `[ASSUMPTION]` Aug 25, 2026 |
| **6. Monthly metrics** | First monthly closure metrics report | CJ-7 | `[ASSUMPTION]` Sep 1, 2026 |

> **Sources for roadmap claims:** `pir.schema.json` (20 status enum values, verified programmatically 2026-08-17), `pir-status-report-2026-08-03.md#L176` (12 Tier-1 OSINT-unresolvable PIRs), `pir-inventory-index.md#L29` (Total = 120 PIRs).

---

## 14. CVS Compliance Statement

**Framework:** `03-VERIFICATION/CVS-FRAMEWORK.md` (Master Framework, TLP:AMBER)
**Workstream:** CogOS (Claim ID prefix: `CVS-COG-`)
**Rule 6:** This document is AI-generated. All claims are capped at T2 / max score 7 until human (DAF) review. T1 upgrade requires human validation per CVS §7 Rule 6.

### Claim Inventory

| # | Claim | Tier | Label | Sources (L-level) | Score | Rule 6 Cap | Register ID |
|---|-------|------|-------|-------------------|-------|------------|-------------|
| 1 | 120 total PIRs in CSCDC workstream | T2 | `[SOURCE-BACKED]` | `pir-inventory-index.md` (L2), `pir-status-report-2026-08-03.md` (L2) | 7 | Yes — AI-verified | CVS-COG-001 |
| 2 | 90 PIRs intelligence-resolved or partially resolved | T2 | `[SOURCE-BACKED]` | `pir-status-report-2026-08-03.md#L36` (L2), `#L46` (L2) | 7 | Yes | CVS-COG-002 |
| 3 | 1 PIR synced to record layer | T2 | `[SOURCE-BACKED]` | `pir-status-report-2026-08-03.md#L37` (L2), `#L46` (L2) | 7 | Yes | CVS-COG-003 |
| 4 | 16 Critical PIRs in inventory | T2 | `[SOURCE-BACKED]` | `pir-inventory-index.md#L25` (L2), `#L39` (L2) | 7 | Yes | CVS-COG-004 |
| 5 | 20 status values in PIR schema | T2 | `[SOURCE-BACKED]` | `pir.schema.json` (L2), verified programmatically 2026-08-17 | 7 | Yes | CVS-COG-005 |
| 6 | 6 active collection cronjobs (CJ-1→CJ-6) | T2 | `[SOURCE-BACKED]` | `pir-inventory-index.md#L108-113` (L2), `#L117` (L2) | 7 | Yes | CVS-COG-006 |
| 7 | 12 Tier-1 OSINT-unresolvable PIRs | T2 | `[SOURCE-BACKED]` | `pir-status-report-2026-08-03.md#L176` (L2), `#L86` (L2) | 7 | Yes | CVS-COG-007 |
| 8 | 3 OSINT-unresolvable Critical PIRs | T2 | `[SOURCE-BACKED]` | `pir-status-report-2026-08-03.md#L86` (L2), `#L69-72` (L2) | 7 | Yes | CVS-COG-008 |
| 9 | 30 Resolved / 60 Partial / 30 Open | T2 | `[SOURCE-BACKED]` | `pir-status-report-2026-08-03.md#L32-34` (L2) | 7 | Yes | CVS-COG-009 |
| 10 | Workstream created 2026-07-25 | T2 | `[SOURCE-BACKED]` | `pir-status-report-2026-08-03.md#L23` (L2), `pir-inventory-index.md` updated_at (L2) | 7 | Yes | CVS-COG-010 |
| 11 | ADEP-001 §44 governs Closure Gate | T2 | `[SOURCE-BACKED]` | `closure-gate-checklist.md#L6` (L2) | 7 | Yes | CVS-COG-011 |
| 12 | PIR closure is prerequisite to 16-point gate | T3 | `[ASSESSMENT]` | Derived from ADEP-001 §44 structural design | 5 | N/A — analytical | CVS-COG-012 |
| 13 | Five lifecycle phases organise the 20 statuses | T3 | `[ASSESSMENT]` | Schema enum analysis (L2) | 5 | N/A | CVS-COG-013 |
| 14 | Minimum evidence thresholds by priority | T3 | `[ASSESSMENT]` | Designed to align with CVS §3 (L1 governance doc) | 5 | N/A | CVS-COG-014 |
| 15 | Authority exception for Low/Medium auto-fulfil | T3 | `[ASSESSMENT]` | Operational design choice | 4 | N/A | CVS-COG-015 |
| 16 | SLA targets (TTFI/TTC) | T4 | `[ASSUMPTION]` | Designed targets, no empirical baseline | 3 | N/A — projection | CVS-COG-016 |
| 17 | Auto-escalation triggers (§3.4, §7) | T4 | `[ASSUMPTION]` | Requires CJ-7 logic not yet implemented | 2 | N/A | CVS-COG-017 |
| 18 | Implementation roadmap dates (§13) | T4 | `[ASSUMPTION]` | Target dates, pending DAF availability | 3 | N/A | CVS-COG-018 |
| 19 | KPI targets (§11) | T4 | `[ASSUMPTION]` | Designed targets, no baseline data | 3 | N/A | CVS-COG-019 |
| 20 | 30/60/90/180 max deferral periods | T4 | `[ASSUMPTION]` | Designed to mirror TTC hard limits | 3 | N/A | CVS-COG-020 |

### Score Breakdown (5-Criteria Model)

For all T2 claims (items 1-11), the AI self-scoring per CVS §10 is:

| Criteria | Score | Justification |
|----------|-------|---------------|
| Authority | 2 | L2 sources (internal validated records, Strategic CognitiveOS) |
| Traceability | 2 | Specific file + line number citations provided |
| Recency | 1 | Source documents dated 2026-07-25 to 2026-08-03 (7-23 days old) |
| Consistency | 1 | Single workstream's internal reports — no cross-source contradiction found, but no independent external corroboration |
| Completeness | 1 | Claims are complete in context but from a single workstream's self-reporting |
| **Total** | **7** | **Rule 6 cap reached — AI cannot exceed 7 without human review** |

> **Upgrade path to T1:** DAF reviews this document, validates claims against source files, and confirms. T2 → T1 transition per CVS §2 Tier Transition Rules. Confidence score may increase to 8-10 with human authority (2) + recency confirmation (2).

### Labels Applied

| Label | Count | Meaning (CVS §9) |
|-------|-------|------------------|
| `[SOURCE-BACKED]` | 11 | T2 — supported by L2 evidence, not yet fully validated by human |
| `[ASSESSMENT]` | 5 | T3 — analytical interpretation derived from facts |
| `[ASSUMPTION]` | 5 | T4 — used for planning only, not fact |
| `[CONFIRMED]` | 0 | T1 — would require human validation (upgrade path) |
| `[DISPUTED]` | 0 | T5 — no conflicts detected |
| `[EXCLUDED]` | 0 | T6 — no rejected claims |

### Evidence Register

All 20 claims are registered in `03-VERIFICATION/CVS-EVIDENCE-REGISTER.csv` with full 20-field schema. See §15 for the appended rows.

---

## 15. CVS Evidence Register Entries

The following rows are appended to `03-VERIFICATION/CVS-EVIDENCE-REGISTER.csv`:

```csv
CVS-COG-001,CogOS,120 total PIRs in CSCDC workstream,pir-inventory-index.md,L2,,2026-07-25,Internal record,T2,Partially Verified,7,2,2,1,1,1,None,Ember,None,2026-08-17
CVS-COG-002,CogOS,90 PIRs intelligence-resolved or partially resolved,pir-status-report-2026-08-03.md,L2,,2026-08-03,Internal report,T2,Partially Verified,7,2,2,1,1,1,None,Ember,None,2026-08-17
CVS-COG-003,CogOS,1 PIR synced to record layer,pir-status-report-2026-08-03.md,L2,,2026-08-03,Internal report,T2,Partially Verified,7,2,2,1,1,1,None,Ember,None,2026-08-17
CVS-COG-004,CogOS,16 Critical PIRs in inventory,pir-inventory-index.md,L2,,2026-07-25,Internal record,T2,Partially Verified,7,2,2,1,1,1,None,Ember,None,2026-08-17
CVS-COG-005,CogOS,20 status values in PIR schema,pir.schema.json,L2,,2026-07-25,Schema file,T2,Partially Verified,7,2,2,2,1,1,None,Ember,None,2026-08-17
CVS-COG-006,CogOS,6 active collection cronjobs CJ-1 through CJ-6,pir-inventory-index.md,L2,,2026-07-25,Internal record,T2,Partially Verified,7,2,2,1,1,1,None,Ember,None,2026-08-17
CVS-COG-007,CogOS,12 Tier-1 OSINT-unresolvable PIRs,pir-status-report-2026-08-03.md,L2,,2026-08-03,Internal report,T2,Partially Verified,7,2,2,1,1,1,None,Ember,None,2026-08-17
CVS-COG-008,CogOS,3 OSINT-unresolvable Critical PIRs,pir-status-report-2026-08-03.md,L2,,2026-08-03,Internal report,T2,Partially Verified,7,2,2,1,1,1,None,Ember,None,2026-08-17
CVS-COG-009,CogOS,30 Resolved 60 Partial 30 Open PIRs,pir-status-report-2026-08-03.md,L2,,2026-08-03,Internal report,T2,Partially Verified,7,2,2,1,1,1,None,Ember,None,2026-08-17
CVS-COG-010,CogOS,Workstream created 2026-07-25,pir-status-report-2026-08-03.md,L2,,2026-08-03,Internal report,T2,Partially Verified,7,2,2,1,1,1,None,Ember,None,2026-08-17
CVS-COG-011,CogOS,ADEP-001 §44 governs Closure Gate,closure-gate-checklist.md,L2,,2026-08-16,Governance doc,T2,Partially Verified,7,2,2,2,1,1,None,Ember,None,2026-08-17
CVS-COG-012,CogOS,PIR closure is prerequisite to 16-point gate,ADEP-001 §44 structural design,L2,,2026-08-16,Governance doc,T3,Inferred,5,2,2,1,1,0,None,Ember,None,2026-08-17
CVS-COG-013,CogOS,Five lifecycle phases organise 20 statuses,pir.schema.json analysis,L2,,2026-08-17,Schema analysis,T3,Inferred,5,2,2,2,1,0,None,Ember,None,2026-08-17
CVS-COG-014,CogOS,Minimum evidence thresholds by priority,CVS-FRAMEWORK.md §3,L1,,2026-08-04,Governance doc,T3,Inferred,5,2,2,1,1,1,None,Ember,None,2026-08-17
CVS-COG-015,CogOS,Authority exception for Low/Medium auto-fulfil,Operational design choice,L5,,2026-08-17,Design decision,T3,Inferred,4,0,1,2,1,0,None,Ember,None,2026-08-17
CVS-COG-016,CogOS,SLA targets TTFI/TTC,Designed targets,L5,,2026-08-17,Design decision,T4,Pending Validation,3,0,0,1,1,1,None,Ember,Empirical calibration needed,2026-08-17
CVS-COG-017,CogOS,Auto-escalation triggers §3.4 §7,CJ-7 enforcement logic,L5,,2026-08-17,Design decision,T4,Pending Validation,2,0,0,0,1,1,Not implemented,Ember,Implementation required,2026-08-17
CVS-COG-018,CogOS,Implementation roadmap dates §13,Target dates,L5,,2026-08-17,Planning,T4,Pending Validation,3,0,1,0,1,1,Pending DAF availability,Ember,None,2026-08-17
CVS-COG-019,CogOS,KPI targets §11,Designed targets,L5,,2026-08-17,Design decision,T4,Pending Validation,3,0,0,0,1,1,No baseline data,Ember,Data collection needed,2026-08-17
CVS-COG-020,CogOS,30/60/90/180 max deferral periods,Designed to mirror TTC limits,L5,,2026-08-17,Design decision,T4,Pending Validation,3,0,1,0,1,1,None,Ember,None,2026-08-17
```

---

*This framework is a derivative instrument of ADEP-001 §44 `[SOURCE-BACKED: closure-gate-checklist.md#L6]`. It does not modify the 16-point Closure Gate; it operates one level below it, ensuring that the PIR-level intelligence requirements are formally closed before the initiative-level closure gate can be initiated.*

*CVS validation per `03-VERIFICATION/CVS-FRAMEWORK.md`. All claims subject to Rule 6 (AI output cap: T2, max score 7). Human review required for T1 upgrade. Evidence Register: `03-VERIFICATION/CVS-EVIDENCE-REGISTER.csv`.*
