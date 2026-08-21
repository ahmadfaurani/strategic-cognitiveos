---
id: GOV-REPORTING-STANDARD-001
record_type: document
title: Execution State Reporting Standard
created_at: 2026-08-04 00:00:00+00:00
updated_at: 2026-08-19 16:00:00+00:00
owner: DAF
status: active
priority: high
sensitivity: internal
lifecycle_state: canonical
confidence: high
tags:
  - cognitive-loop/self-assessment
  - doctrine/adep-001
  - domain/cognitiveos-operations
  - domain/development-governance
  - domain/governance
  - outcome/evidence-confirmed
source:
  type: direct
  reference: DAF authority
summary: Governance reference document for Execution State Reporting Standard.
strategic_significance: Governs CognitiveOS operational standards and procedures.
mission_alignment:
- sovereign-ai
- intelligence-enablement
related_records:
- GOV-INTAKE-SOP-001
document_type: reference
file_path: governance/reporting-standard.md
version: '1.0'
author: DAF
---

# Execution State Reporting Standard

**Created:** 2026-08-16  
**Owner:** Ember  
**Authority:** DAF  
**Governing Framework:** ADEP-001 §41 (Execution State Reporting)

---

## Purpose

All substantive workflow updates to DAF must follow this 10-element standard. This replaces ad-hoc formatting and ensures DAF receives consistent, decision-ready information.

**Rule (ADEP §1):** Reporting is not performance. Reporting is communication that enables decisions. Every element must serve DAF's decision-making, not Ember's self-assessment.

---

## The 10 Elements

### 1. Objective
> What is this workstream trying to achieve?

One sentence. The normalised objective (ADEP §6 formula): "Achieve [outcome] for [stakeholder] by [time] subject to [constraints] demonstrated through [evidence]."

### 2. Current State
> Where are we right now?

One paragraph. Factual, no spin. If the state is bad, say so (§37: resist fabricated certainty).

### 3. Completed
> What has been done since last report?

Bullet list. Each item: what was done + evidence (commit hash, file, validation result). Not "started" or "in progress" — actually done with evidence (§24).

### 4. In Progress
> What is being worked on right now?

Bullet list. Each item: what + who + expected completion. Honest status per §4 (Designed/Documented/Implemented/Verified/Operational/Outcome Confirmed).

### 5. Blocked
> What is stopped and why?

Bullet list. Each item: blocker + cause + what's needed to unblock + who can unblock it. If nothing is blocked, state "Nothing blocked."

### 6. Risks
> What could go wrong?

Bullet list. Each risk: description + probability + impact + mitigation. Tag with RSK- record ID if one exists. Include new risks discovered since last report.

### 7. Decisions Required
> What does DAF need to decide?

Bullet list. Each item: the decision + options + recommendation + deadline. Mark as RECOMMENDATION (§39). Never present a recommendation as a pre-made decision.

### 8. Next Critical Actions
> What happens next?

Ordered list. Top 3-5 actions by priority (CognitiveOS §8 scoring). Each: action + owner + deadline + what it unblocks.

### 9. Success Confidence
> How likely are we to achieve the objective?

Percentage or band:
- **>80%** — On track, no material risks
- **60-80%** — On track with identified risks that have mitigations
- **40-60%** — At risk, material dependencies or blockers
- **<40%** — High risk of failure, requires intervention

### 10. Confidence Basis
> Why this confidence level?

2-3 sentences. What drives the confidence up? What drives it down? What would change the assessment?

---

## Template

```markdown
## [Workstream Name] — Status Update

**Objective:** [normalised objective]
**Date:** [date]
**Reporter:** Ember

**Current State:** [paragraph]

**Completed:**
- [item] (evidence: [commit/file/link])
- [item] (evidence: [commit/file/link])

**In Progress:**
- [item] — owner: [who] — ETA: [date]
- [item] — owner: [who] — ETA: [date]

**Blocked:**
- [item] — blocker: [cause] — unblock requires: [what] — [who can unblock]

**Risks:**
- [risk] — P: [prob] I: [impact] — mitigation: [what] — [RSK-ID]

**Decisions Required:**
- [decision] — options: [A/B/C] — RECOMMENDATION: [X] — deadline: [date]

**Next Critical Actions:**
1. [action] — owner: [who] — deadline: [date] — unblocks: [what]
2. [action] — owner: [who] — deadline: [date] — unblocks: [what]
3. [action] — owner: [who] — deadline: [date] — unblocks: [what]

**Success Confidence:** [percentage/band]

**Confidence Basis:** [2-3 sentences]
```

---

## Rules

1. **Every substantive update uses this format.** Not optional. Not "when I remember."
2. **Element 7 (Decisions Required) is the most important.** If DAF reads nothing else, he reads this.
3. **Element 9 (Success Confidence) must be honest.** Inflated confidence is worse than no confidence (§42).
4. **Element 5 (Blocked) is not failure.** Hiding blockers is failure (§37: invisible scope creep).
5. **Keep it concise.** This is a briefing, not a report. If it takes >5 minutes to read, it's too long.
6. **RECOMMENDATION ≠ DECISION.** Tag recommendations explicitly. DAF decides (§39).

---

## Frequency

- **Routine:** At each checkpoint (CP1, CP2, etc.)
- **Triggered:** When a material change occurs (blocker, risk, decision needed)
- **On request:** When DAF asks for status
- **Heartbeat:** Abbreviated version (Elements 2, 4, 5, 7, 9 only) during heartbeat checks
