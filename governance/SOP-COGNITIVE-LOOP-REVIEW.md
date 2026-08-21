---
id: GOV-SOP-COGNITIVE-LOOP-REVIEW-001
record_type: document
title: 'SOP: Cognitive Loop Review Against Strategic Objective'
created_at: 2026-08-04 00:00:00+00:00
updated_at: 2026-08-20 07:38:00+00:00
owner: DAF
status: active
priority: high
sensitivity: internal
lifecycle_state: canonical
confidence: high
tags:
  - cognitive-loop/gap-identification
  - cognitive-loop/kill-date-enforcement
  - cognitive-loop/secondary-pattern
  - cognitive-loop/self-assessment
  - cognitive-loop/stage-mapping
  - cognitive-loop/week-over-week-delta
  - deadline/gate-failed
  - deadline/gate-passed
  - deadline/tat-approval
  - deadline/tat-creation
  - deadline/tat-qc
  - domain/cognitiveos-operations
  - domain/governance
  - domain/sovereign-ai
  - framework/cognitive-loop
  - framework/engineered-success
  - framework/workflow-identification-protocol
source:
  type: direct
  reference: DAF authority
summary: 'Governance reference document for SOP: Cognitive Loop Review Against Strategic
  Objective.'
strategic_significance: Governs CognitiveOS operational standards and procedures.
mission_alignment:
- sovereign-ai
- intelligence-enablement
related_records:
- GOV-INTAKE-SOP-001
document_type: sop
file_path: governance/SOP-COGNITIVE-LOOP-REVIEW.md
version: '1.1'
author: DAF
changelog: 'v1.1 (2026-08-20): WIP integrated into Step 3 as sub-steps 3a-3b (full
  due diligence mode). v1.0 (2026-08-18): Initial SOP.'
---

# SOP: Cognitive Loop Review Against Strategic Objective

**SOP ID:** SOP-CL-001 | **Established:** 2026-08-18 | **Authority:** DAF | **TLP:** AMBER

---

## Purpose

The Cognitive Loop Review is the weekly feedback loop between strategic objective and programme execution. It tests whether programmes are actually advancing toward the strategic objective — not just whether they're active or stalled.

Without this review, the strategic objective is a document on a shelf. With it, the Monday review becomes a strategic instrument.

## Trigger

- **Schedule:** Every Monday 10:30 AM UTC+8 (02:30 UTC)
- **Executed by:** Hermes cron (isolated session)
- **Reviewed by:** Ember (cognitive layer) in conversation with DAF
- **Repo:** `ahmadfaurani/cohort-programme`

## Inputs

1. Strategic Objective (`STRATEGIC-OBJECTIVE.md`) — the canonical statement and pathway
2. Portfolio Register (`register/PORTFOLIO-REGISTER.md`) — current programme statuses
3. Previous reviews (`reviews/`) — last week's review for delta comparison
4. Joint IP Register (`register/JOINT-IP-REGISTER.csv`) — IP assets created
5. Decision log (`decisions/`) — recent decisions

## Process (7 Steps)

### Step 1: Map Each Programme Against Strategic Pathway Stages

Break the strategic objective into its pathway stages. For the Cohort Programme:

```
Cohort → Alumni Community → Co-Development → Joint IP → Validation → Pilot → Commercialisation → Sovereign Deployment → Enduring Strategic Ecosystem
```

For each programme (PRG-001 through PRG-005), assess: does this stage exist? Is it designed? Is it operational?

Output: a stage-level progression matrix (programmes × stages).

### Step 2: Identify the Single Largest Gap

Ask: what is the one gap between the strategic objective and programme reality that most blocks the objective?

This is not the most urgent programme deadline — it's the structural gap that, if closed, would most improve the probability of achieving the objective.

Output: one gap, named clearly, with explanation of why it blocks the objective.

### Step 3: Identify Secondary Patterns + Workflow Identification Protocol (WIP)

#### 3a: Secondary Patterns

Look for patterns across programmes:
- Are multiple programmes stuck at the same pathway stage?
- Are multiple programmes exhibiting the same failure mode?
- Are there structural issues (single-point dependency, no delegation, no community infrastructure) affecting multiple programmes?

Output: 2-3 secondary patterns, each with affected programmes named.

#### 3b: Workflow Identification Protocol (WIP) — Document Discovery

For any document mentioned for the first time during Cognitive Loop execution, apply the full WIP due diligence:

**3b.1 — Identify Ownership**
- Who is the creation owner(s)? (Who writes/created the document)
- Do NOT default to DAF as author. Check originator explicitly. Workspace documents may be authored by Athena, Ember, sub-agents, or team members.
- Who is the audience? (Primary recipients, reviewers, approvers — external and internal)

**3b.2 — Classify Three-Layer Importance**
- **Strategic:** How does this document advance strategic objectives? Which gates, initiatives, or portfolio items does it unlock?
- **Operational:** How does this document enable operational execution? What workflows depend on it?
- **Tactical:** What is the immediate tactical value? What is the next use case and deadline?

**3b.3 — Apply 7-Working-Day Turnaround Timeline (TAT)**

| Phase | Owner | Duration | Purpose |
|-------|------|----------|---------|
| Creation | Creation owner(s) | 3 working days | Author draft, structure, content |
| QC / Review | Reviewer(s) | 2 working days | Quality control, technical validation, product review |
| Approval / Finalise | Approval owner | 1 working day | Sign-off, finalise version |
| **Total** | | **7 working days** | |

- Assess current status against TAT: Is the document on track, ahead, or compressed?
- If timeline is compressed (deadline < 7 working days from creation), flag the compression risk explicitly.
- Identify critical path: which phase is currently active, and what blocks it from completing?

**3b.4 — Execution Responsibility Alignment**

For each document, identify who holds execution responsibility within the relevant practice/department. This may differ from the creation owner. For example:
- Athena may author the document (creation owner)
- DAF may approve it (approval owner)
- A Practice PM (FTE) may hold execution responsibility for sections within the Cyber Security Practice
- Hadri may hold technical advisory role but not section ownership

Map: Creation Owner → QC Reviewer → Approval Owner → Execution Owner. All four roles must be identified. If any role is TBA, flag it.

**3b.5 — Output**

For each new document identified during the Cognitive Loop, produce:
- Document identification (title, version, date, status, classification)
- Creation owner(s) — checked, not assumed
- Audience — primary and secondary
- Three-layer importance assessment (strategic, operational, tactical)
- 7-working-day TAT assessment with current status
- Execution responsibility alignment map
- Critical path item (what blocks completion right now?)

This WIP output is part of Step 3's deliverable and feeds into Step 4 (ranking) and Step 5 (three actions).

### Step 4: Rank Gaps by Strategic Impact

Rank gaps by what blocks the strategic objective specifically — not just programme execution. A programme being late is an execution issue. A programme not having an IP framework is a strategic issue. Strategic issues rank higher.

### Step 5: Produce Three Actions

Answer the daily operating question: *What three actions create the greatest improvement in the probability of achieving the strategic objective?*

Each action must:
- Be specific (not "improve governance" but "define IP ownership framework before PERJASA workshop")
- Have a named owner
- Have a deadline
- Target the strategic objective, not just a programme's schedule

### Step 6: Kill Date Enforcement

For each programme, check: has the kill date passed? If yes:
- Recommend status change to ⛔ Parked or 💀 Killed
- Log the kill/park decision in the decision log with rationale
- Note freed cognitive capacity

### Step 7: Process Self-Assessment

Include a brief self-assessment:
- What did the review get right?
- What did it get wrong or miss?
- What patterns are recurring across weekly reviews?

This catches process errors and creates a longitudinal record of review quality.

## Output

The review produces a markdown file saved to `reviews/YYYY-MM-DD-review.md` in the cohort-programme repo with:

1. **Stage-level progression matrix** (programmes × pathway stages)
2. **Single largest gap** (named, with rationale)
3. **Secondary patterns** (2-3, with affected programmes)
4. **Three actions** (specific, owned, deadline, targeting strategic objective)
5. **Kill date enforcement** (any programmes past kill date)
6. **Self-assessment** (what was right, what was wrong)
7. **Week-over-week delta** (what changed since last review)

The review is committed to the repo and a concise brief is delivered to Telegram.

## Brief Format (Telegram)

```
📊 Cognitive Loop Review — YYYY-MM-DD

Stage Progression:
- PRG-001: [current stage] → [next stage]
- PRG-002: [current stage] → [next stage]
- [etc.]

Largest Gap: [one sentence]

Three Actions:
1. [action] — [owner] — [deadline]
2. [action] — [owner] — [deadline]
3. [action] — [owner] — [deadline]

Kills: [none / programme name + decision]

Full review: [repo link]
```

## Key Principles

1. **Stage-level measurement, not status-only.** "Which stage did it advance to?" not just "is it active or stalled?"
2. **Strategic impact ranking.** Strategic gaps rank higher than execution delays.
3. **Three actions maximum.** Focus forces prioritisation. More than three dilutes impact.
4. **Self-assessment is mandatory.** Reviews that don't assess themselves are summaries, not instruments.
5. **Kill dates are enforced.** Parking is discipline, not failure. Zombies drain capacity.
6. **The review serves the objective.** If the review doesn't improve the probability of achieving the strategic objective, it failed.

## Review Cadence

| Element | Schedule |
|---------|----------|
| Hermes cron execution | Monday 10:30 AM UTC+8 (02:30 UTC) |
| Review committed to repo | Same execution |
| Telegram brief delivered | Same execution |
| Ember interpretation for DAF | Monday, in conversation |
| DAF decision on actions | Monday or Tuesday |

## History

- **First run:** 2026-08-18 (manual, inaugural analytical report)
- **First automated run:** 2026-08-24 (scheduled)
- **Test cases for first run:** PMO (Aug 25 kill date — one day after review), CSM-Aras (Aug 25 kill date)

---

*This SOP is the highest-impact process extracted from the 2026-08-18 cohort programme governance session. It creates the feedback loop between strategy and execution that prevents the strategic objective from becoming a document on a shelf.*
