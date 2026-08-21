---
id: GOV-CROSS-DOCTRINAL-ANALYSIS-SOP-001
record_type: document
title: Cross-Doctrinal Analysis SOP — Modus Operandi
created_at: 2026-08-04 00:00:00+00:00
updated_at: 2026-08-19 16:00:00+00:00
owner: DAF
status: active
priority: high
sensitivity: internal
lifecycle_state: canonical
confidence: high
tags:
  - cognitive-loop/full-cycle
  - deadline/gate-failed
  - deadline/gate-passed
  - doctrine/cognitiveos-prime
  - domain/cognitiveos-operations
  - domain/cyberdsa-2026
  - domain/governance
  - framework/cognitive-loop
  - framework/engineered-success
  - method/cross-doctrinal-analysis
  - method/engineered-success
  - method/triangulation
source:
  type: direct
  reference: DAF authority
summary: Governance reference document for Cross-Doctrinal Analysis SOP — Modus Operandi.
strategic_significance: Governs CognitiveOS operational standards and procedures.
mission_alignment:
- sovereign-ai
- intelligence-enablement
related_records:
- GOV-INTAKE-SOP-001
document_type: sop
file_path: governance/cross-doctrinal-analysis-sop.md
version: '1.0'
author: DAF
---

# Cross-Doctrinal Analysis SOP — Modus Operandi

> **Version:** 1.0  
> **Authority:** DAF  
> **Status:** ACTIVE — Mandatory for all major workstream analyses  
> **Institutionalized:** 2026-08-16  
> **Scope:** All CognitiveOS workstreams requiring strategic intelligence assessment  
> **Related:** `governance/COGNITIVEOS-PRIME-DOCTRINE.md` §5–§10, `governance/intake-sop.md`, `governance/template-discipline-sop.md`
> **Precedent:** CyberDSA 2026 pilot (INT-006, INT-007, INT-008, INT-009 — 146KB, 4 records, 100% ordinal convergence)

---

## 1. Purpose

This SOP defines the standard operating procedure for applying the CognitiveOS Prime Doctrine's analytical sections (§5–§10) to any major workstream. It institutionalises the **triangulation methodology** — three independent analytical methods applied to the same workstream, with convergence analysis to validate findings.

**Core principle:** No single analytical method can capture all dimensions of a complex operational workstream. Three methods with different blind spots, applied independently, produce validated intelligence through convergence. When methods that see differently agree, the agreement is structural — not an artifact of bias.

**What this SOP replaces:** Ad-hoc analytical requests. Instead of DAF asking "analyse this workstream," the analysis follows a defined protocol with known inputs, outputs, quality gates, and record types.

**What this SOP does NOT replace:** The Intake SOP (handles data ingestion), the Template Discipline SOP (handles record creation), or the Cognitive Loop itself (which runs continuously). This SOP defines how to produce **periodic deep-dive intelligence products** using doctrinal methods.

---

## 2. When to Trigger

### Mandatory Triggers (analysis MUST be produced)

| Trigger | Timing | Methods |
|---------|--------|---------|
| **Checkpoint approaching** | 7 days before each checkpoint (CP1, CP2, etc.) | Full 3-method analysis |
| **War-room activation** | Within 24 hours of war-room declaration | Full 3-method analysis |
| **New initiative launch** | Within 48 hours of INIT record creation | Methods 1+3 (Cognitive Loop + Engineered Success) |
| **Critical risk identified** | Within 24 hours of RSK record creation at HIGH/CRITICAL | Methods 1+2 (Cognitive Loop + Actionable Intelligence) |
| **Post-checkpoint review** | Within 48 hours after each checkpoint | Method 1 (Cognitive Loop) + Convergence Synthesis with prior analysis |

### Discretionary Triggers (analysis MAY be produced)

| Trigger | Timing | Methods |
|---------|--------|---------|
| Operator request for assessment | On request | Full 3-method or subset |
| Major stakeholder change | Within 48 hours | Method 2 (Actionable Intelligence) |
| Dependency chain breakage | Within 24 hours | Method 3 (Engineered Success) |
| Pattern recurrence across cycles | At next loop cycle | Method 1 (Cognitive Loop) + Convergence |

### What Qualifies as a "Major Workstream"

A workstream qualifies for cross-doctrinal analysis if it meets ≥2 of:

- [ ] Has an active INIT record with portfolio_tier = flagship or incubation
- [ ] Has ≥10 success criteria across multiple dimensions
- [ ] Has ≥3 active stakeholders (individual STK records)
- [ ] Has a defined checkpoint schedule
- [ ] Has a war-room or equivalent governance structure
- [ ] Involves ≥2 organisations
- [ ] Has commercial or strategic value >RM 100K

---

## 3. The Three Methods

### Method 1: Cognitive Loop Analysis (Doctrine §5–§6)

**Question answered:** *"What is happening and what does it mean?"*

**Type:** Diagnostic — identifies dynamic patterns, correlations, and learnings from live signals.

**Doctrine sections:** §5 (Cognitive Operating Loop — 8 steps), §6 (Pattern Recognition Engine — 10 patterns)

**Output record type:** INT (intelligence)

**Output record prefix:** `-cognitive-loop-analysis`

### Method 2: Actionable Intelligence & Prioritisation (Doctrine §7–§8)

**Question answered:** *"What should we do about it?"*

**Type:** Prescriptive — converts findings into prioritised, owned, verifiable action packages.

**Doctrine sections:** §7 (Actionable Intelligence Standard — 10 elements), §8 (Prioritisation Engine — 7 dimensions)

**Output record type:** INT (intelligence)

**Output record prefix:** `-actionable-intelligence-prioritisation`

### Method 3: Engineered Success Framework (Doctrine §9–§10)

**Question answered:** *"What conditions must become true?"*

**Type:** Predictive/Structural — maps dependency chains, failure modes, critical path, and leading indicators.

**Doctrine sections:** §9 (Engineered Success Framework — 12 elements), §10 (Objective Decomposition)

**Output record type:** INT (intelligence)

**Output record prefix:** `-engineered-success`

### Method 4: Cross-Doctrinal Synthesis (Meta-Method)

**Question answered:** *"Do the three methods agree, and what does the convergence reveal?"*

**Type:** Validative — triangulates findings, identifies blind spots, produces unified action framework.

**Input:** Methods 1, 2, 3 output records

**Output record type:** INT (intelligence)

**Output record prefix:** `-cross-doctrinal-synthesis`

---

## 4. Analysis Workflow (8 Phases)

### Phase 1: Preparation (Ember, 30 min)

**Prerequisites:**
- Workstream has qualifying INIT record
- Success criteria are defined (INT or embedded in INIT)
- Stakeholder matrix exists (STK records)
- At least 1 checkpoint is defined

**Steps:**
1. Confirm workstream qualifies (§2 criteria)
2. Read all related CognitiveOS records (INIT, STK, ACT, DEC, RSK, INT, COM)
3. Identify the checkpoint or event driving the analysis
4. Confirm analysis scope with DAF if discretionary
5. Create a working note in `memory/YYYY-MM-DD.md` documenting analysis start

**Output:** Confirmed scope, complete record inventory

### Phase 2: Method 1 — Cognitive Loop Analysis (Ember, ~2 hrs)

**Execute the full 8-step loop per Doctrine §5:**

| Step | Action | Output |
|------|--------|--------|
| 1. SENSE | Capture all signals from CognitiveOS records, recent actions, daily memory | Signal inventory (≥10 signals) |
| 2. CLASSIFY | Domain, workstream, type, time horizon, importance per signal | Classification matrix |
| 3. CORRELATE | Cross-signal relationships, dependency chains, shared dependencies | Correlation maps (≥3 maps) |
| 4. PATTERN RECOGNITION | Apply §6 patterns: convergence, bottlenecks, leverage points, strategic windows, decision debt, coordination debt, execution drift, portfolio collision, compounding opportunities | Pattern catalogue (≥5 patterns) |
| 5. PRIORITISE | Score candidate actions using §8 dimensions (7-weighted) | Ranked action list (≥5 actions) |
| 6. ACT | Package top actions in §7 format (10-element standard) | Action packages (one per priority action) |
| 7. VERIFY | Define evidence standards and checkpoint verification criteria | Verification framework |
| 8. LEARN | Extract institutional learnings; define next loop cycle trigger | Learning statements (≥3) + next cycle definition |

**Quality gate:**
- [ ] ≥10 signals captured
- [ ] ≥3 correlation maps
- [ ] ≥5 patterns identified
- [ ] ≥5 actions scored and ranked
- [ ] ≥3 learnings extracted
- [ ] Next loop cycle trigger defined
- [ ] All claims have confidence tags [HIGH/MEDIUM/LOW]
- [ ] All Tier 1 data has source citations

**Output:** INT record (e.g., `INT-YYYYMMDD-NNN-<workstream>-cognitive-loop-analysis.md`)

### Phase 3: Method 2 — Actionable Intelligence & Prioritisation (Ember, ~1.5 hrs)

**Apply the 10-element standard (§7) to top findings:**

For each significant finding (≥3 findings):

| Element | Question |
|---------|----------|
| 1. SIGNAL | What happened? |
| 2. EVIDENCE | What information supports the assessment? |
| 3. PATTERN | What larger relationship or trend is visible? |
| 4. IMPLICATION | Why does this matter? |
| 5. OPPORTUNITY / RISK | What could happen? |
| 6. CONFIDENCE | High / Medium / Low |
| 7. DECISION WINDOW | When does action need to occur? |
| 8. RECOMMENDED ACTION | What should be done? |
| 9. OWNER | Who should drive it? |
| 10. VERIFICATION | How will we know the action produced the intended result? |

**Apply the Prioritisation Engine (§8) — 7-dimension weighted scoring:**

| Dimension | Weight | Scale |
|-----------|--------|-------|
| Strategic Impact | 25% | 1–5 |
| Time Criticality | 15% | 1–5 |
| Portfolio Leverage | 15% | 1–5 |
| Commercial / Mission Value | 15% | 1–5 |
| Dependency Unlock | 10% | 1–5 |
| Stakeholder Importance | 10% | 1–5 |
| Risk Reduction | 10% | 1–5 |

**Weighted score = Σ(dimension_score × weight).** Range: 1.00–5.00.

**Tier classification:**
| Score Range | Tier | Action Window |
|-------------|------|---------------|
| 4.00–5.00 | Tier 1 Critical | 48 hours |
| 3.50–3.99 | Tier 2 High | Before next checkpoint |
| 3.00–3.49 | Tier 3 Medium | Before CP+1 |
| <3.00 | Tier 4 Routine | When capacity allows |

**Resolve prioritisation conflicts explicitly:**
- Urgency vs importance conflicts
- Equal scores with different effort profiles
- Ripple effects (second-order impact not captured by direct scoring)

**Anti-pattern compliance check (§44):**
- [ ] No finding treated as independent
- [ ] No summary without implications
- [ ] No low-value actions generated
- [ ] No meetings confused with outcomes
- [ ] No ambiguous ownership
- [ ] No "ongoing" as meaningful status

**Output:** INT record (e.g., `INT-YYYYMMDD-NNN-<workstream>-actionable-intelligence-prioritisation.md`)

### Phase 4: Method 3 — Engineered Success Framework (Ember, ~2.5 hrs)

**Apply all 12 elements (§9) to the workstream:**

| Element | Output Required |
|---------|----------------|
| 1. OBJECTIVE | Strategic objective statement + decomposition chain start |
| 2. DEFINITION OF DONE | Observable state + evidence per dimension |
| 3. SUCCESS CONDITIONS | Structural conditions (all must be true) + conditional conditions |
| 4. FAILURE CONDITIONS | Failure modes with probability, impact, mitigation — including interdependency map |
| 5. DEPENDENCIES | External dependencies + internal dependency chains (≥3 chains mapped) |
| 6. CRITICAL PATH | Longest dependency chain identified + schedule slack analysis |
| 7. OWNERSHIP | Criteria count per owner + SPOF identification + redistribution plan |
| 8. RESOURCES | Human, information, systems, budget — with gap status |
| 9. CHECKPOINTS | All checkpoints listed with criteria reviewed + risk level |
| 10. LEADING INDICATORS | ≥5 indicators with Green/Yellow/Red thresholds + current status |
| 11. LAGGING INDICATORS | Post-hoc measurement points with targets |
| 12. VERIFICATION | Evidence standards (acceptable vs not acceptable) + verification protocol |

**Apply Objective Decomposition (§10):**

```
Strategic Objective
  └─ Operational Outcomes (≥3)
      └─ Work Packages (≥3 per outcome)
          └─ Milestones (checkpoint-aligned)
              └─ Actions (with owner)
                  └─ Evidence (verifiable)
                      └─ Definition of Done (observable)
```

**Rule:** No orphan work packages. Every work package traces to an operational outcome, which traces to the strategic objective.

**Quality gate:**
- [ ] All 12 elements completed
- [ ] ≥3 dependency chains mapped
- [ ] Critical path identified
- [ ] ≥5 leading indicators with thresholds
- [ ] ≥3 failure modes with interdependency map
- [ ] Full decomposition chain with no orphans
- [ ] Predictive model: best/likely/worst case projection for next checkpoint

**Output:** INT record (e.g., `INT-YYYYMMDD-NNN-<workstream>-engineered-success.md`)

### Phase 5: Cross-Doctrinal Synthesis (Ember, ~2 hrs)

**This phase occurs ONLY after Methods 1, 2, and 3 are complete.**

**Step 1: Convergence Mapping**

For each finding identified by any method:
1. Check if Method 1 (Cognitive Loop) identified it
2. Check if Method 2 (Actionable Intelligence) identified it
3. Check if Method 3 (Engineered Success) identified it
4. Record convergence level: 3/3, 2/3, or 1/3
5. Assign confidence: 3/3 = [HIGH], 2/3 = [MEDIUM-HIGH], 1/3 = [MEDIUM]

**Step 2: Ordinal Convergence Check**

Compare action rankings across all 3 methods:
1. List all actions identified by each method in ranked order
2. Check if rankings are identical (ordinal convergence)
3. If not identical, identify divergences and explain why
4. Calculate agreement percentage

**Step 3: Blind-Spot Analysis**

For each method, identify:
1. What findings did it uniquely identify? (single-method findings)
2. What findings did it miss that other methods caught?
3. What structural reason explains the blind spot?
4. Is the blind spot acceptable (covered by other methods) or critical (requires additional analysis)?

**Step 4: Unified Action Framework**

Produce a single prioritised action list:
1. Tier 1: Triple convergence actions (3/3 methods agree) — execute immediately
2. Tier 2: Triple convergence actions — execute before next checkpoint
3. Tier 3: Double or single convergence — monitor, execute when capacity allows
4. For each action: unified score, effort, criteria unblocked, methods validating

**Step 5: Predictive Model Synthesis**

Combine predictive elements from all 3 methods:
1. INT-006: Pattern-based prediction (what patterns suggest about trajectory)
2. INT-007: Prioritisation-based prediction (what action execution changes)
3. INT-008: Leading indicator-based prediction (what indicators say about next checkpoint)

Produce: Best case / Likely case / Worst case projection for next checkpoint, with the delta explained by which actions are executed.

**Step 6: Doctrine Maturity Assessment**

Assess which doctrine sections were successfully operationalised:
- §5 Cognitive Loop: ✅ Operational / ⚠️ Partial / ❌ Failed
- §6 Pattern Recognition: ✅ / ⚠️ / ❌
- §7 Actionable Intelligence: ✅ / ⚠️ / ❌
- §8 Prioritisation Engine: ✅ / ⚠️ / ❌
- §9 Engineered Success: ✅ / ⚠️ / ❌
- §10 Objective Decomposition: ✅ / ⚠️ / ❌

**Quality gate:**
- [ ] All findings from Methods 1, 2, 3 are mapped
- [ ] Convergence level assigned per finding
- [ ] Ordinal convergence calculated
- [ ] ≥3 blind spots identified and explained
- [ ] Unified action framework produced (Tier 1/2/3)
- [ ] Predictive model with best/likely/worst case
- [ ] Doctrine maturity assessed

**Output:** INT record (e.g., `INT-YYYYMMDD-NNN-<workstream>-cross-doctrinal-synthesis.md`)

### Phase 6: Validation & Commit (Ember, 15 min)

1. Run `python3 tools/validate.py` — all records must pass
2. Git add, commit with standard message format
3. Git push
4. Record commit hash in daily memory

**Commit message format:**
```
INT-YYYYMMDD-NNN: Cross-Doctrinal Analysis — <workstream name>

- Method 1 (Cognitive Loop): <record ID>, <size>
- Method 2 (Actionable Intelligence): <record ID>, <size>
- Method 3 (Engineered Success): <record ID>, <size>
- Synthesis: <record ID>, <size>
- Convergence: <X>/10 triple, <Y>/10 double, <Z>/10 single
- Ordinal convergence: <N>/<N> actions ranked identically (p<0.001)
- <total> records validated, 0 failures
```

### Phase 7: Delivery to DAF (Ember, immediate after commit)

Deliver a structured summary to DAF via the active channel containing:

1. **What was analysed** — workstream name, driving trigger
2. **Convergence score** — X% triple, Y% double, ordinal agreement %
3. **Top 3 findings** — with confidence tags
4. **Unified Tier 1 actions** — with effort, impact, and criteria unblocked
5. **CP projection** — best/likely/worst case
6. **Blind spots** — what each method alone would have missed
7. **Doctrine maturity** — which sections operationalised
8. **Key link** — connection to broader portfolio
9. **Next triggers** — what actions this analysis creates

### Phase 8: Learnings Integration (Ember, at next loop cycle)

At the next Cognitive Loop cycle (typically next checkpoint):
1. Review whether Tier 1 actions were executed
2. Check if CP projection was accurate
3. If projection was wrong — analyse why and update the model
4. Extract new learnings
5. Update this SOP if methodology improvements are identified

---

## 5. Record Structure Standards

### INT Record: Cognitive Loop Analysis

**Filename:** `INT-YYYYMMDD-NNN-<workstream>-cognitive-loop-analysis.md`

**Required frontmatter fields:** `id`, `record_type`, `title`, `created_at`, `owner`, `intelligence_type`, `status`, `priority`, `sensitivity`, `lifecycle_state`, `confidence`, `summary`, `tags`, `source`, `related_records`

**Required body sections:**
- Step 1: Sense (signal inventory, ≥10 signals)
- Step 2: Classify (domain/workstream/type/time/importance matrix)
- Step 3: Correlate (≥3 correlation maps + dependency graph)
- Step 4: Pattern Recognition (≥5 patterns, §6 reference)
- Step 5: Prioritise (≥5 actions scored per §8)
- Step 6: Act (action packages per §7 format)
- Step 7: Verify (evidence standards + checkpoint gate)
- Step 8: Learn (≥3 learnings + next cycle trigger)

### INT Record: Actionable Intelligence & Prioritisation

**Filename:** `INT-YYYYMMDD-NNN-<workstream>-actionable-intelligence-prioritisation.md`

**Required body sections:**
- Part 1: The problem §7 solves (anti-pattern contrast)
- Part 2: 10-element standard applied (≥3 findings as full 10-element packages)
- Part 3: Prioritisation Engine scoring (7-dimension matrix, ≥5 actions)
- Part 4: Signal-to-execution chain (end-to-end trace)
- Part 5: Decision conflict resolution (≥2 conflicts)
- Part 6: Verification standards (per-action)
- Part 7: Operational output (Tier 1/2/3/4)

### INT Record: Engineered Success Framework

**Filename:** `INT-YYYYMMDD-NNN-<workstream>-engineered-success.md`

**Required body sections:**
- Part 1: The problem §9 solves (anti-pattern contrast)
- Part 2: 12-element framework (all 12 elements completed)
- Part 3: Objective decomposition in detail (full chain, no orphans)
- Part 4: Predictive model (best/likely/worst case)
- Part 5: Engineered Success vs Reactive Management (contrast table)
- Part 6: Operational output (scorecard + priority actions)

### INT Record: Cross-Doctrinal Synthesis

**Filename:** `INT-YYYYMMDD-NNN-<workstream>-cross-doctrinal-synthesis.md`

**Required body sections:**
- Part 1: Methodology (triangulation principle)
- Part 2: Convergence map (all findings by method)
- Part 3: Convergence summary matrix
- Part 4: Blind-spot analysis
- Part 5: Unified action framework (Tier 1/2/3)
- Part 6: Predictive model (synthesised)
- Part 7: Doctrine effectiveness assessment
- Part 8: Unified recommendation
- Part 9: Doctrine maturity assessment
- Appendix: Convergence evidence matrix (action rankings across methods)

---

## 6. Quality Gates

### Per-Method Quality Gates

Each method's output record must pass its quality gate (defined in §4 Phases 2–4) before the synthesis phase begins. If any method fails its quality gate:
1. Re-work the method until it passes
2. Do NOT proceed to synthesis with incomplete methods
3. If re-work is not possible (data gap), document the gap and proceed with reduced confidence

### Synthesis Quality Gates

| Gate | Requirement | If Failed |
|------|-------------|-----------|
| Convergence mapping | All findings from all 3 methods mapped | Re-review methods for missed findings |
| Ordinal convergence | Action rankings compared | If <70% agreement, flag as DIVERGENT and explain why |
| Blind-spot analysis | ≥3 blind spots identified | Review methods for additional gaps |
| Unified framework | Tier 1/2/3 actions produced | Re-prioritise using synthesised scoring |
| Predictive model | Best/likely/worst case defined | Gather additional leading indicator data |
| Doctrine maturity | All 6 sections assessed | Complete assessment |

### Cross-Method Consistency Check

Before committing:
- [ ] All 3 methods reference the same success criteria
- [ ] All 3 methods reference the same stakeholder base
- [ ] All 3 methods use the same checkpoint definitions
- [ ] Action owners are consistent across methods (no method assigns a different owner to the same criterion)
- [ ] Failure modes in Method 3 correspond to patterns in Method 1
- [ ] Priority actions in Method 2 correspond to leverage points in Method 1 and chain origins in Method 3

---

## 7. Roles & Responsibilities

| Role | Who | Responsibility |
|------|-----|----------------|
| **Authority** | DAF | Approves analysis scope, receives delivery, authorises actions |
| **Analyst** | Ember (or designated agent) | Executes all 4 methods, produces INT records, delivers summary |
| **Validator** | `tools/validate.py` | Schema validation gate — all records must pass |
| **Reviewer** | DAF (at delivery) | Reviews findings, authorises Tier 1 actions, provides feedback |
| **Tracker** | Programme Coordinator (when confirmed) | Tracks action execution against projections, feeds back to next loop cycle |

---

## 8. Timing & Resource Budget

| Phase | Responsible | Time Budget | Output Size |
|-------|------------|:-----------:|:-----------:|
| Phase 1: Preparation | Ember | 30 min | Working note |
| Phase 2: Method 1 (Cognitive Loop) | Ember | 2 hrs | ~30KB |
| Phase 3: Method 2 (Actionable Intelligence) | Ember | 1.5 hrs | ~25KB |
| Phase 4: Method 3 (Engineered Success) | Ember | 2.5 hrs | ~50KB |
| Phase 5: Cross-Doctrinal Synthesis | Ember | 2 hrs | ~40KB |
| Phase 6: Validation & Commit | Ember | 15 min | 4 INT records |
| Phase 7: Delivery to DAF | Ember | Immediate | Structured summary |
| Phase 8: Learnings Integration | Ember | At next cycle | Updated learnings |
| **Total** | | **~9 hrs** | **~145KB across 4 records** |

**Parallelisation:** Methods 1, 2, and 3 can be executed in parallel if multiple agents are available. Each method reads the same CognitiveOS record base and produces independent output. The synthesis phase requires all 3 to be complete.

**Compression mode (for urgent triggers):** If full 3-method analysis is not feasible within the trigger window:
- Execute Methods 1+2 only (Cognitive Loop + Actionable Intelligence)
- Skip Method 3 (Engineered Success) — note this in the synthesis
- Reduce convergence analysis to 2-method agreement
- Flag that Method 3 should be executed at next opportunity

---

## 9. Convergence Interpretation Guide

### Convergence Levels

| Level | Meaning | Confidence | Action |
|-------|---------|:----------:|--------|
| **3/3 Triple Convergence** | All 3 methods independently identify this finding | [HIGH] | Act immediately — structural property of the system |
| **2/3 Double Convergence** | 2 of 3 methods identify this finding | [MEDIUM-HIGH] | Act with moderate confidence — review why 3rd method missed it |
| **1/3 Single Method** | Only 1 method identifies this finding | [MEDIUM] | Monitor — may be a blind spot in other methods OR an artifact of one method's bias |

### Ordinal Convergence

| Agreement | Interpretation | Action |
|-----------|---------------|--------|
| **100% (7/7)** | Perfect ordinal convergence — structural property | Execute with full confidence |
| **≥70% (5/7)** | Strong convergence — minor methodological differences | Execute with high confidence; explain divergences |
| **<70% (<5/7)** | Divergent — methods disagree on priorities | Flag as DIVERGENT; DAF review required before execution |

### What Convergence Does NOT Mean

- Convergence does not guarantee correctness — all 3 methods could share the same blind spot
- Convergence does not replace DAF's judgment — it informs it with structural validation
- Convergence does not eliminate the need for execution — intelligence without action is analysis, not intelligence (Doctrine §44 anti-pattern)

---

## 10. Integration with Existing SOPs

### Relationship to Intake SOP

- The Intake SOP handles **data ingestion** (incoming information → CognitiveOS records)
- This SOP handles **analytical processing** (existing records → intelligence products)
- Intake creates the records that this SOP analyses
- This SOP may trigger new intake events (e.g., new risks identified → RSK records created via Intake SOP)

### Relationship to Template Discipline SOP

- All 4 output records (INT × 4) must conform to the intelligence schema
- Template Discipline SOP validation gate applies — no record enters git without passing validation
- The pre-commit hook enforces this

### Relationship to Cognitive Loop (§5)

- The Cognitive Loop runs **continuously** (every session, every signal)
- This SOP produces **periodic deep-dive** analysis (triggered by checkpoints, risks, war-room activations)
- The Loop feeds this SOP (provides signal inventory)
- This SOP feeds the Loop (learnings from Step 8 become inputs to next cycle)

### Relationship to War-Room Mode (§38)

- War-room activation triggers this SOP (mandatory trigger)
- This SOP's output directly supports war-room execution (prioritised actions, predictive model)
- War-room deactivation triggers post-checkpoint review (Phase 8)

---

## 11. Revision & Improvement

### When to Revise This SOP

| Trigger | Action |
|---------|--------|
| Method produces inaccurate prediction | Review and adjust that method's quality gate |
| New doctrine section becomes operational | Add as Method 5 (or integrate into existing method) |
| Blind spot identified across 3+ cycles | Add explicit check for that blind spot |
| DAF feedback on process | Update workflow and quality gates |
| Agent capability improvement (e.g., multi-agent parallelisation) | Update timing budget and parallelisation section |

### Improvement Protocol

1. After each full analysis cycle, Ember extracts process learnings
2. If a process learning suggests SOP change, draft revision
3. DAF reviews and approves
4. Update version number and revision history
5. Git commit and push

### Version Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-08-16 | DAF (authority), Ember (drafter) | Initial institutionalization. Based on CyberDSA 2026 pilot (INT-006/007/008/009). 80% triple convergence, 100% ordinal convergence achieved in pilot. |

---

## 12. Reference: CyberDSA 2026 Pilot Results

The pilot application of this SOP produced:

| Metric | Value |
|--------|-------|
| Records produced | 4 INT records (INT-006, INT-007, INT-008, INT-009) |
| Total analytical output | ~146KB |
| Findings identified | 10 |
| Triple convergence | 8/10 (80%) |
| Double convergence | 2/10 (20%) |
| Single-method findings | 0/10 (0%) |
| Ordinal convergence | 7/7 (100%, p<0.001) |
| Blind spots identified | 6 |
| Unified Tier 1 actions | 3 (executable in 60 min, unblocking 32% of mission) |
| Doctrine sections operationalised | 6/6 (§5–§10) |
| CP1 prediction accuracy | Pending (CP1 = Aug 22) |

**Key pilot insight:** *"Three independent methods — dynamic, prescriptive, and structural — all discovered the same leverage points through different analytical foundations. The convergence is not coincidental. It reflects a structural property of the system: any method that correctly maps the dependency architecture will identify the same leverage points in the same order."*

---

## Appendix A: Quick-Reference Card

```
CROSS-DOCTRINAL ANALYSIS — QUICK REFERENCE

TRIGGER: Checkpoint -7d | War-room | New INIT | Critical RSK | DAF request

METHOD 1 (§5-§6): Cognitive Loop — "What's happening?"
  → 8 steps: Sense → Classify → Correlate → Pattern → Prioritise → Act → Verify → Learn
  → Output: INT-*-cognitive-loop-analysis.md

METHOD 2 (§7-§8): Actionable Intelligence — "What should we do?"
  → 10-element standard × ≥3 findings + 7-dimension scoring × ≥5 actions
  → Output: INT-*-actionable-intelligence-prioritisation.md

METHOD 3 (§9-§10): Engineered Success — "What must become true?"
  → 12 elements + objective decomposition (no orphans)
  → Output: INT-*-engineered-success.md

SYNTHESIS: Cross-Doctrinal — "Do they agree?"
  → Convergence map + ordinal check + blind spots + unified framework
  → Output: INT-*-cross-doctrinal-synthesis.md

QUALITY GATES:
  [ ] Each method passes its quality gate
  [ ] Cross-method consistency check passed
  [ ] Validator passes (0 failures)
  [ ] Convergence ≥70% for high confidence
  [ ] Tier 1 actions identified with owners and verification

DELIVERY: Structured summary to DAF with:
  → Convergence score, top findings, Tier 1 actions, CP projection, blind spots
```

---

## Appendix B: Method Selection Matrix

| Situation | Methods to Use | Rationale |
|-----------|---------------|-----------|
| Full checkpoint review | All 3 + Synthesis | Maximum validation; standard deep-dive |
| War-room activation | All 3 + Synthesis | Need complete picture immediately |
| New initiative launch | Methods 1+3 | Need loop + structure; actions will follow |
| Critical risk identified | Methods 1+2 | Need diagnosis + prescription; structure already exists |
| Post-checkpoint review | Method 1 + Synthesis with prior | Need to verify predictions and extract learnings |
| Quick assessment (DAF request, time-constrained) | Method 2 only | Fastest path to prioritised actions |
| Pattern recurrence | Method 1 + Synthesis with prior | Need to detect if pattern is strengthening or resolving |
| Stakeholder change | Method 2 only | Need to re-prioritise based on new ownership landscape |
| Dependency breakage | Method 3 only | Need to re-map critical path and failure modes |

**Default:** When in doubt, run all 3 + synthesis. The convergence value exceeds the time cost.
