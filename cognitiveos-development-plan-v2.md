# CognitiveOS Core Development Plan — v2.0

**Authority:** DAF
**Architectural Input:** Athena (4-point review of v1)
**Operating Assistant:** Ember
**Date:** 2026-08-15
**Status:** Active Development Plan
**Supersedes:** v1 (4-phase linear roadmap, this session)
**Revisions:** v2.1 — Athena extended review (review policy, verifier as first-class component, record lifecycle states, canonical-vs-projection architecture, intent/execution authority, circuit breakers as governance primitives)
**Revisions:** v2.2 — Athena final review (refined circuit breakers, analytical lenses, revised implementation priority P0-P4, first prototype specification, formal architecture name: CognitiveOS Intake & Integrity Pipeline)
**Status:** ARCHITECTURE LOCKED — direction confirmed by DAF, ready for implementation

---

## 1. Architectural Correction — Two-Dimensional Roadmap

Athena's core insight: **capability ≠ autonomy**. The original plan conflated "what we build" with "how much authority it has." These are orthogonal axes.

### Axis 1 — Capability Phases (What functionality we build)

| Phase | Function |
|-------|----------|
| **C1: Integrity & Validation** | Schema validation, index reconciliation, pre-commit hooks, backfill |
| **C2: AI-Assisted Capture** | Distillation agent, deterministic gate, semantic verifier, draft queue, council |
| **C3: Platform Integration** | Notion sync, Obsidian vault, stakeholder dashboard, executive review |
| **C4: Delegation & Escalation** | Decision rights matrix, RACI, escalation triggers, outcome measurement |

### Axis 2 — Agentic Maturity Phases (How much authority we allow)

| Level | Name | Meaning |
|-------|------|---------|
| **A0** | Baseline | Human creates all records manually. AI assists with retrieval only. |
| **A1** | Shadow | AI generates draft records. Human reviews and commits every one. |
| **A2** | Delegate | AI commits low-risk records automatically. Human reviews high-impact. |
| **A3** | Supervise | AI commits records with post-hoc audit. Circuit breakers can revoke. |
| **A4** | Gated Execute | AI executes predefined action types (index updates, status changes) with human gate on novel actions. |
| **A5** | Event Driven | AI responds to triggers (email arrival, calendar event) with full intake pipeline, human gate on strategic records only. |
| **A6** | Bounded Autonomy | AI manages routine CognitiveOS operations within policy boundaries. Human intervenes by exception. |

### Current State

- **Capability:** C1 partial (schemas, templates, taxonomy exist; validation/backfill missing)
- **Autonomy:** A0 (all records manually created by Ember)

### Target State (12 weeks)

- **Capability:** C4 complete
- **Autonomy:** A2 (delegate low-risk, human gate high-impact)

---

## 2. The Intake Pipeline (C2 Core)

**Design principle:** Code validates structure. Agents validate meaning.

```
Conversation / Email / Document
         │
         ▼
┌─────────────────────┐
│  Distillation Agent  │  ← Local Ollama model (Mercury pattern)
│  (extract entities)  │     Throttled: 1x per conversation, 15 min cooldown
└──────────┬──────────┘
           │
           ▼
   Structured Candidates (YAML frontmatter + markdown body)
           │
           ▼
┌─────────────────────┐
│  Deterministic Gate  │  ← Code, not LLM
│  (schema validation) │     JSON Schema, ID format, duplicate check,
└──────────┬──────────┘     ref integrity, filename, date, directory
           │
     PASS / FAIL
     │         │
     │         ▼
     │    REJECT → Log error, flag for review
     │
     ▼
┌─────────────────────┐
│  Semantic Verifier   │  ← Agent (Artemis pattern — read-only, critical review)
│  (validate meaning)  │     Checks: semantic duplication, incorrect decision
└──────────┬──────────┘     interpretation, wrong stakeholder attribution,
           │                 commitment ambiguity, unsupported inference,
           │                 record-type misclassification
     PASS / FAIL / UNCERTAIN
     │         │         │
     │         ▼         ▼
     │    REJECT     UNCERTAIN → Route to Council
     │
     ▼
┌─────────────────────┐
│  Risk Classification │  ← Deterministic rules
└──────────┬──────────┘
           │
    ┌──────┴──────┐
    ▼             ▼
 LOW RISK     HIGH IMPACT
    │             │
    ▼             ▼
 Draft Queue   The Council
    │        (3-seat: Skeptic,
    │         Pragmatist, Synthesist)
    │             │
    └──────┬──────┘
           │
           ▼
┌─────────────────────┐
│    Commit Gate       │  ← Human at A1, policy-based at A2+
│  (human or policy)   │
└──────────┬──────────┘
           │
           ▼
   CognitiveOS Canonical Repository
   (GitHub — source of truth)
           │
           ▼
   Index Auto-Update (same commit)
```

### 2.1 Distillation Agent

**What it does:** Reads conversation/email/document, extracts entities, generates structured record candidates.

**Input:** Raw conversation text (last N messages or forwarded content)

**Output:** Array of candidate records, each as YAML frontmatter + markdown body

**Record types it can draft:** CONV, DEC, ACT, COM, RSK, STK, INT

**Model:** Local Ollama (once infrastructure fixed) or cloud model fallback

**Throttling:** Fire-and-forget, max 1x per conversation per 15 minutes

**What it does NOT do:**
- Does NOT write to canonical repository
- Does NOT update indexes
- Does NOT assign final IDs (assigns draft IDs: `DRAFT-CONV-YYYYMMDD-001`)
- Does NOT classify risk level (that's the Deterministic Gate)

### 2.2 Deterministic Gate (Code, Not LLM)

**Runs as:** Node.js script or Python script

**Validates:**

| Check | Method |
|-------|--------|
| YAML frontmatter parseable | YAML parser |
| All mandatory fields present | JSON Schema validation |
| Field types correct | JSON Schema validation |
| ID format valid | Regex: `^[A-Z]{3,4}-\d{8}-\d{3}$` |
| No duplicate IDs | Scan existing records in directory |
| References valid | Check `related_records`, `supersedes`, `stakeholders` against existing files |
| Filename convention | `<ID>.md` in correct directory |
| Date format | ISO 8601 |
| Directory placement | Record type → correct directory |
| Tag values | Against `taxonomy/tags.yaml` |
| Sensitivity level | Against `taxonomy/sensitivity-levels.yaml` |
| Portfolio tier | Against `taxonomy/portfolio-tiers.yaml` |

**Output:** PASS (proceed) or FAIL (reject with specific errors)

**Principle:** Do not ask an LLM whether YAML is valid when a parser can determine it exactly.

### 2.3 Semantic Verifier — CognitiveOS Integrity Verifier (First-Class Component)

**Status:** First-class CognitiveOS component — more important than Council.

**What it does:** Reads passed candidates and checks four dimensions of integrity.

**Model:** Cloud model (needs reasoning capability)

#### Four Integrity Dimensions

**Dimension 1: Structural Integrity** (overlaps with Deterministic Gate, but agent checks what code cannot)
- Schema compliance (semantic, not just syntactic)
- ID correctness in context
- Date reasonableness
- Reference completeness
- Index implications

**Dimension 2: Semantic Integrity**
- Does the record accurately represent the source?
- Did extraction introduce unsupported facts?
- Was intent distorted?
- Is the decision interpretation correct?
- Is the commitment clear and actionable?
- Is the record-type classification correct?

**Dimension 3: Relational Integrity**
- Does the action connect to the correct decision?
- Does the commitment connect to the correct stakeholder?
- Are dependencies represented?
- Are cross-references semantically valid (not just structurally)?

**Dimension 4: Temporal Integrity**
- Is this genuinely new? (not a duplicate of existing record)
- Does it supersede something? Is that relationship captured?
- Is an action it references already closed?
- Does the new record contradict later evidence?
- Is the temporal ordering correct?

**Output:** PASS, FAIL (with reasons), or UNCERTAIN (route to Council)

**Why first-class:** This is effectively a database integrity layer for an AI-native knowledge system. It is more important than Council because it runs on every record, not just high-impact ones.

### 2.4 Risk Classification & Review Policy (Deterministic Rules)

**Three-tier review policy:**

```yaml
review_policy:
  routine:
    validator: true
    verifier: true
    council: false
    human_approval: false
  important:
    validator: true
    verifier: true
    council: optional
    human_approval: false
  strategic:
    validator: true
    verifier: true
    council: required
    human_approval: required
```

**Record-to-tier mapping:**

| Record Type | Default Tier | Council? |
|---|---|---|
| Routine conversation | routine | No |
| Standard action item | routine | No |
| Ordinary commitment | routine | Usually no |
| Important action / commitment | important | Optional |
| Strategic decision | strategic | Yes |
| Critical stakeholder commitment | strategic | Yes |
| High-risk assessment | strategic | Yes |
| Architecture doctrine | strategic | Yes |
| Major escalation | strategic | Yes |
| Political / intelligence judgement | strategic | Yes |

**Risk classification is deterministic** — rule engine based on record type + portfolio tier + sensitivity level. No AI needed for routing.

**Determines:** Whether the Council reviews before commit, and whether human approval is required.

### 2.5 The Council (Selective, Not Default)

**Activates when:** Risk classification = HIGH, OR semantic verifier = UNCERTAIN

**Three seats:**

| Seat | Role | System Prompt Bias |
|------|------|-------------------|
| Skeptic | Challenges assumptions, finds gaps | "What's wrong with this record? What's missing?" |
| Pragmatist | Assesses actionability, feasibility | "Can this be executed? Is the owner clear?" |
| Synthesist | Identifies connections, implications | "What does this connect to? What are the second-order effects?" |

**Each seat runs independently** (parallel `sessions_spawn`), then merged.

**Output:** Consensus (commit), dissent (flag for human review), or rejection (discard)

### 2.6 Record Lifecycle States

Records pass through discrete states. These are NOT arbitrary tags — they are governance primitives.

```yaml
record_status:
  - candidate              # Generated by distillation agent, not yet validated
  - structurally_valid      # Passed deterministic gate (schema, ID, refs)
  - semantically_verified   # Passed semantic verifier (4 integrity dimensions)
  - approved                # Passed commit gate (human or policy)
  - canonical              # Committed to CognitiveOS repository
  - superseded             # Replaced by a newer record (linked via supersedes)
  - rejected               # Failed validation or verification, not committed
```

**State transitions:**
```
candidate -> structurally_valid -> semantically_verified -> approved -> canonical
     |              |                      |                     |           |
  rejected      rejected               rejected             rejected  superseded
```

**Key rule:** Only `canonical` records appear in indexes. Only `canonical` records are queryable. The gap between FILE GENERATED and RECORD CANONICAL is the entire validation pipeline.

### 2.7 Commit Gate

**At A1 (Shadow):** Human reviews every draft before commit. All tiers require human approval.
**At A2 (Delegate):** Routine tier auto-commits after verification. Important tier auto-commits with post-hoc audit. Strategic tier requires human approval.
**At A3+ (Supervise):** All tiers auto-commit with post-hoc audit. Circuit breakers can flag for review. Strategic tier still requires Council + human approval.

---

## 3. Delegation & Authority Model

### 3.1 Intent Authority vs Execution Authority

CognitiveOS tracks two separate authority dimensions per record:

```yaml
# Example: a strategic decision with delegated execution

record_type: decision
authority: DAF                    # Who made the strategic call
outcome: "Establish CyberDSA launch readiness"

delegation:
  owner: Hadri                    # Who owns execution
  execution_authority: operational # operational | tactical | strategic
  constraints:
    - launch_date: 2026-10-XX
    - product_scope: GovSec TIP + VoronCitadel
    - coordination_requirements:
      - CSM relationship management
      - B200/A100 cluster allocation
  method_autonomy: full            # DAF does not prescribe HOW
```

**The principle:** Strategic authority defines WHAT (outcome). Delegated owner determines HOW (method). CognitiveOS tracks both, and the delegation record captures constraints without prescribing execution.

**This is more powerful than a normal action tracker** because it preserves the distinction between strategic intent and execution freedom. It answers: "Who decided this should happen?" and "Who decides how it happens?" separately.

### 3.2 Circuit Breakers as Governance Primitives

Circuit breakers are NOT prompts to an LLM. They are explicit system states with defined triggers and consequences.

| Breaker ID | Name | Trigger | Consequence |
|---|---|---|---|
| CB-01 | Intent Without Execution | Decision exists but no owned action | Flag for delegation review |
| CB-02 | Repeated Slippage | Deadline missed, rescheduled, missed again | Escalate to authority |
| CB-03 | Circular Activity | Lots of updates, no measurable advancement | Escalate to authority |
| CB-04 | Verification Failure | Agent/human claims completion but evidence insufficient | Block pipeline, route to Council |
| CB-05 | Ownership Failure | Active item has no accountable owner | Flag for delegation review |
| CB-06 | Dependency Deadlock | Task blocked beyond tolerance | Escalate to authority |
| CB-07 | Contradictory Record | New record contradicts existing canonical | Route to Council for resolution |
| CB-08 | Broken Dependency | Referenced record is superseded/rejected | Flag for update |
| CB-09 | 72h No Action | Decision exists, 72 hours pass with no action created | Flag for Executive Attention Queue |
| CB-10 | Orphaned Commitment | Commitment has no stakeholder | Flag for relationship review |

**These circuit breakers eventually power an Executive Attention Queue** — surfacing what actually needs DAF's intervention. This is much closer to CognitiveOS's strategic purpose than copying Warden's operational supervision heartbeat literally.

**Each breaker has:**
- A trigger condition (deterministic, checkable by code)
- A consequence (block, flag, escalate, route)
- An audit log entry (`logs/circuit-breakers.jsonl`)
- A resolution path (how the breaker clears)

---

## 4. Platform Architecture — Canonical vs Projections

```
CognitiveOS GitHub Repository
   (Canonical Source of Truth)
           |
    +------+------+
    |      |      |
    v      v      v
Obsidian  Notion  Agent Context
(projection) (projection) (projection)
```

**Principle:** CognitiveOS repository is the single canonical source. Notion, Obsidian, and agent context windows are **projections** — read-only views or filtered interaction surfaces.

- **GitHub (CognitiveOS):** Canonical records, indexes, schemas, governance. All writes happen here.
- **Obsidian:** Knowledge graph projection. Reads from GitHub, renders as navigable wiki. No writes back to canonical.
- **Notion:** Operational command projection. Reads from GitHub, renders as dashboards/tables. Status changes can propagate back (two-way sync for operational fields only, not for canonical record content).
- **Agent Context:** Ember loads relevant records into context window as needed. Not a store — a view.

**This prevents three-equal-masters synchronization problems.** There is one source of truth. Everything else is a view.

---

## 5. Revised Development Plan — Two-Dimensional

### Sprint 1 (Week 1–2): C1 + A0→A1

**Capability: Integrity & Validation**
**Autonomy: Stay at A0, prepare for A1**

1. **Schema validation script** (Node.js)
   - Read all `.md` records, parse frontmatter, validate against JSON Schema
   - Output: pass/fail report per record
   - This becomes the Deterministic Gate's validation engine

2. **Index reconciliation**
   - Audit all 270 records against indexes
   - Identify: records not in index, index entries without files, stale entries
   - Generate reconciliation report

3. **Pre-commit hook**
   - Husky hook: run schema validation on changed files
   - Block commit if validation fails
   - Check: index files updated if records changed

4. **Index automation script**
   - Regenerate indexes from record files (not manual editing)
   - Run as pre-commit step or manual command

5. **Backfill missing records**
   - Completed actions → draft OUT records
   - Referenced documents → draft ART records
   - Commit through normal intake SOP

**Deliverable:** Clean, validated corpus. Every record passes schema. Every index is accurate. Pre-commit prevents bad data.

### Sprint 2 (Week 3–4): C2 Core + A1

**Capability: AI-Assisted Capture Pipeline**
**Autonomy: Move to A1 (Shadow — AI drafts, human commits)**

1. **Distillation agent prototype**
   - Post-conversation: local model extracts candidate records
   - Output as draft YAML + markdown to `strategic-cognitiveos/drafts/`
   - Draft IDs: `DRAFT-CONV-YYYYMMDD-001`
   - Throttled: 1x per conversation, 15 min cooldown

2. **Deterministic Gate implementation**
   - Reuse Sprint 1's schema validation script
   - Add: ID format, duplicate check, ref integrity, filename, directory
   - Runs automatically on every draft

3. **Semantic verifier prototype**
   - Cloud model, read-only
   - Checks the 7 semantic quality dimensions
   - Outputs: PASS / FAIL / UNCERTAIN

4. **Risk classification rules**
   - Rule engine: record type + portfolio tier + sensitivity → risk level
   - Determines routing: Draft Queue vs Council

5. **Draft queue UI**
   - `strategic-cognitiveos/drafts/` directory
   - Ember reviews drafts in session, commits or rejects
   - Commit triggers index auto-update

**Deliverable:** End-to-end pipeline from conversation → draft → validate → verify → queue → human commit. Operating at A1.

### Sprint 3 (Week 5–6): C2 Advanced + A1→A2

**Capability: Council + Selective Automation**
**Autonomy: Move to A2 (Delegate — low-risk auto-commit, high-impact human gate)**

1. **Council prototype**
   - Three `sessions_spawn` with different system prompts
   - Parallel execution, merge step
   - Activates only for HIGH risk or UNCERTAIN records

2. **Auto-commit for low-risk records**
   - Reference, routine action, standard engagement records
   - Auto-commit with index update
   - Post-hoc audit log

3. **Circuit breakers (initial)**
   - Intent-without-action: draft has no ACT → flag
   - Circling: same record drafted 3x → flag
   - Degenerate output: malformed content → block
   - Verification failure: semantic verifier fails → block

4. **Escalation triggers**
   - Action overdue >7 days → escalate to owner
   - Commitment due date <3 days → alert DAF
   - Risk status change → notify

**Deliverable:** Council operational for high-stakes intake. Low-risk auto-commit. Circuit breakers active. Operating at A2.

### Sprint 4 (Week 7–8): C3 Begin + A2

**Capability: Platform Integration (start)**
**Autonomy: Hold at A2**

1. **Notion sync (read)**
   - Push portfolio register to Notion
   - Push action register to Notion
   - One-way: GitHub → Notion

2. **Obsidian vault mount**
   - Expose `strategic-cognitiveos/` as Obsidian vault
   - Verify backlinks, graph view, navigation

3. **Stakeholder dashboard**
   - Live view from stakeholder records
   - Engagement status, next actions, relationship health

**Deliverable:** Notion as operational view. Obsidian as knowledge graph. GitHub remains source of truth.

### Sprint 5 (Week 9–10): C3 Complete + C4 Begin + A2

**Capability: Platform Integration (complete) + Delegation start**
**Autonomy: Hold at A2**

1. **Two-way Notion sync** (status changes propagate back)
2. **Executive portfolio review** (auto-generated weekly from records)
3. **Decision rights matrix** (per initiative, from existing `decision-rights.md`)
4. **RACI per initiative type**

### Sprint 6 (Week 11–12): C4 Complete + A2 stable

**Capability: Delegation & Escalation (complete)**
**Autonomy: A2 stable, prepare for A3**

1. **Outcome measurement loop** (action → outcome → lesson → taxonomy)
2. **Weekly executive review** (auto-generated brief)
3. **Escalation framework** (circuit breakers + escalation triggers + audit log)
4. **A3 preparation** (design post-hoc audit, revocation mechanism)

---

## 6. Key Design Principles (Revised)

1. **Code validates structure. Agents validate meaning.** — Never use an LLM for what a parser can determine exactly.

2. **Draft first, canonical later.** — AI-generated records never write directly to the canonical repository. They enter a draft queue. Human or policy gate before commit.

3. **Capability ≠ Autonomy.** — What we build is independent from how much authority it has. New features don't mean more autonomy.

4. **Council is selective, not default.** — Three-seat deliberation activates only for high-impact records or uncertain classifications. Not every intake.

5. **Rollback through separation.** — Drafts can be discarded without affecting canonical records. Committed records can be superseded but not deleted. Clean rollback at every stage.

6. **Intent authority ≠ Execution authority.** — Strategic authority defines OUTCOME. Delegated owner determines METHOD. CognitiveOS tracks both separately.

7. **Canonical source ≠ Projection surfaces.** — CognitiveOS GitHub repository is the canonical source. Notion and Obsidian are projections/interaction surfaces, not equal masters. Sync flows outward; truth flows inward.

8. **Never trust generated output merely because the producing agent claims success.** — FILE GENERATED ≠ RECORD VALIDATED ≠ RECORD CANONICAL. These are separate states.

9. **Circuit breakers are governance primitives, not prompts.** — They are explicit system states with defined triggers, not advisory instructions to an LLM.

10. **The Verifier is more important than the Council.** — Verifier runs on every record across four integrity dimensions. Council runs only on strategic/uncertain records. Priority: build verifier first, council second.

11. **Analytical Lenses before persistent agents.** — Evaluate records through perspectives (Threat Intelligence, Commercial, Stakeholder, etc.) without creating a zoo of persistent agents. Lenses graduate to agents only when frequency justifies.

12. **Reversibility by default.** — Every new capability ships with a kill switch (e.g., `auto_distillation: false`). First experiment must be almost completely reversible.

13. **Provenance is mandatory.** — Every extracted record points back to its source. No orphan records without a source trail.

---

## 7. File Structure for Pipeline

```
strategic-cognitiveos/
├── drafts/                    ← NEW: Draft queue (pre-commit)
│   ├── CONV/
│   ├── DEC/
│   ├── ACT/
│   ├── COM/
│   ├── RSK/
│   └── STK/
├── decisions/                 ← Canonical (unchanged)
├── initiatives/               ← Canonical (unchanged)
├── stakeholders/              ← Canonical (unchanged)
├── actions/                   ← Canonical (unchanged)
├── commitments/               ← Canonical (unchanged)
├── engagements/               ← Canonical (unchanged)
├── risks/                     ← Canonical (unchanged)
├── intelligence/              ← Canonical (unchanged)
├── outcomes/                  ← Canonical (currently empty)
├── artifacts/                 ← Canonical (currently empty)
├── tools/                     ← NEW: Pipeline tooling
│   ├── validate.sh            ← Deterministic Gate (schema validation)
│   ├── distill.js             ← Distillation agent runner
│   ├── verify.js              ← Semantic verifier runner
│   ├── classify-risk.js       ← Risk classification rules
│   ├── council.js             ← Council orchestrator
│   ├── commit-gate.sh         ← Commit gate logic
│   └── reconcile-indexes.js   ← Index automation
├── logs/                      ← NEW: Pipeline audit trail
│   ├── intake.jsonl           ← Every intake event logged
│   ├── council.jsonl          ← Council deliberations
│   └── circuit-breakers.jsonl ← Breaker triggers
├── schemas/                   ← Existing JSON schemas
├── templates/                 ← Existing templates
├── taxonomy/                  ← Existing taxonomy
├── indexes/                   ← Existing indexes (auto-updated)
└── governance/                ← Existing governance docs
```

---

## 8. Implementation Priority (Athena Final Sequence)

Replaces the original 6-item build order. Priority tiers P0-P4, 14 components.

| Priority | Component | Reason |
|---|---|---|
| **P0** | Schema + index integrity | Everything else depends on canonical data correctness |
| **P0** | Record state lifecycle | Enables safe automated drafting |
| **P0** | Deterministic validator | Prevent malformed records entering corpus |
| **P1** | Auto-distillation | Highest productivity impact |
| **P1** | Draft intake queue | Safety boundary |
| **P1** | Semantic verifier | Prevents silent corruption |
| **P1** | Provenance linking | Every extracted record points back to source |
| **P2** | Council | Strategic/high-risk record assurance |
| **P2** | Analytical lenses | Better contextual reasoning |
| **P2** | Notion/Obsidian projection | Human interaction surfaces |
| **P3** | Decision-rights model | Supports organisational delegation |
| **P3** | Circuit breakers | Converts CognitiveOS into active governance |
| **P3** | Executive Attention Queue | Surfaces what actually needs intervention |
| **P4** | Event-driven escalation | Controlled agentic operations |
| **P4** | Bounded autonomous workflows | Only after the integrity model proves reliable |

### 8.1 Analytical Lenses (Replaces Warden "Driving Forces")

Instead of creating a zoo of persistent agents, CognitiveOS uses **Analytical Lenses** — perspectives through which the same record can be evaluated.

**Initial lenses:**
- Threat Intelligence Lens
- Commercial Lens
- Stakeholder Lens
- Compliance Lens
- Strategic Risk Lens
- Product Lens
- Delivery Lens
- Red-Team Lens

**Principle:** The same record evaluated through different lenses without creating unnecessary persistent agents. Later, frequently used lenses can graduate to agents.

### 8.2 First Prototype — CognitiveOS Conversation Distiller

**Scope:** Narrower than full auto-writeback. Only three record types initially.

```
Conversation
    |
    v
Distiller (extract DEC / ACT / COM only)
    |
    v
JSON Schema validation
    |
    v
Verifier (4 integrity dimensions)
    |
    v
Draft Queue
```

**What it generates:**
- DEC — Decisions
- ACT — Actions
- COM — Commitments

**What it does NOT do:**
- No automatic canonical commit
- No other record types (STK, RSK, INT, etc. come later)
- No index updates

**Rollback:** Set `auto_distillation: false`. Nothing in existing CognitiveOS changes. Drafts can be discarded.

**This makes the first experiment almost completely reversible.**

### 8.3 Formal Architecture Name

The emerging CognitiveOS subsystem is formally named:

**CognitiveOS Intake & Integrity Pipeline**

```
SOURCES (Chat / Email / Documents)
    |
    v
DISTILLATION
    |
    v
CANDIDATE RECORD
    |
    v
VALIDATOR (deterministic gate)
    |
    v
VERIFIER (semantic, 4 dimensions)
    |
    v
Risk / Impact Classification
    |           |
    v           v
Standard       Council
    |           |
    +-----+-----+
          |
          v
   APPROVAL GATE
          |
          v
   CANONICAL CognitiveOS
          |
    +-----+-----+
    |     |     |
    v     v     v
Obsidian  Notion  Agents
```

**Architectural separation locked:**
- Warden inspired the agent patterns (Council, verifier, distillation)
- CognitiveOS remains the system of record and governance architecture
- These are distinct concerns. Warden is not the blueprint. CognitiveOS is.

---

## 9. Relationship to Existing Systems

| System | Role in Pipeline |
|--------|-----------------|
| **OpenClaw** | Runtime for agents (distillation, verifier, council). `sessions_spawn` for Council seats. |
| **Hermes** | Potential trigger source (email arrival → distillation). Cron for periodic validation. |
| **Ollama** | Local model for distillation agent (once installed). |
| **GitHub** | Canonical repository. Pre-commit hooks. |
| **Notion** | Operational view (Sprint 4+). |
| **Obsidian** | Knowledge graph (Sprint 4+). |
| **CVS Evidence Register** | Audit trail for Tier 1 claims in records. |
| **Intake SOP** | Human-driven intake remains valid. Pipeline automates the same 9 steps. |

---

*Architecture locked 2026-08-15. Direction confirmed by DAF. Incorporates Athena's full architectural review across two review rounds: two-dimensional roadmap, draft-first/canonical-later, strengthened pipeline, selective Council, review policy tiers, verifier as first-class component (4 integrity dimensions), record lifecycle states, canonical-vs-projection platform architecture, intent/execution authority separation, circuit breakers as governance primitives (10 breakers + Executive Attention Queue), analytical lenses, revised P0-P4 implementation priority, and the first prototype specification (CognitiveOS Conversation Distiller — DEC/ACT/COM only, fully reversible).*
