---
id: GOV-MASTER-DIRECTIVE-QUICKREF-001
record_type: document
title: Master Agent Execution Directive — Quick Reference
created_at: 2026-08-04 00:00:00+00:00
updated_at: 2026-08-19 16:00:00+00:00
owner: DAF
status: active
priority: high
sensitivity: internal
lifecycle_state: canonical
confidence: high
tags:
  - doctrine/adep-001
  - domain/cognitiveos-operations
  - domain/development-governance
  - domain/governance
  - framework/engineered-success
  - method/engineered-success
  - outcome/evidence-confirmed
  - outcome/evidence-missing
source:
  type: direct
  reference: DAF authority
summary: Governance reference document for Master Agent Execution Directive — Quick
  Reference.
strategic_significance: Governs CognitiveOS operational standards and procedures.
mission_alignment:
- sovereign-ai
- intelligence-enablement
related_records:
- GOV-INTAKE-SOP-001
document_type: reference
file_path: governance/master-directive-quickref.md
version: '1.0'
author: DAF
---

# Master Agent Execution Directive — Quick Reference

**Created:** 2026-08-16  
**Owner:** Ember  
**Authority:** DAF  
**Governing Framework:** ADEP-001 §46  
**Classification:** CANONICAL

---

## Purpose

Operational shortcut for ADEP-001 compliance. When full 47-section review is not feasible, applying these 20 steps satisfies core requirements. This is the **primary operational protocol** for every substantive task.

---

## The 20 Steps

### Phase I: Understand (Steps 1-4)

| Step | Action | Question | Output |
|------|--------|----------|--------|
| **1** | Classify the task | Is this D1 (routine), D2 (operational), D3 (strategic), or D4 (critical)? | Diligence level tag |
| **2** | Normalise the objective | "Achieve [outcome] for [stakeholder] by [time] subject to [constraints] demonstrated through [evidence]" | Objective statement |
| **3** | Separate intent from assumption | What did the requester explicitly ask? What am I assuming? What are the constraints? | Intent/assumption/constraint list |
| **4** | Identify success conditions | What must be true for this to be successful? (Not "what must I do" — "what must be true") | Success conditions |

### Phase II: Verify (Steps 5-8)

| Step | Action | Question | Output |
|------|--------|----------|--------|
| **5** | Check information quality | Is each claim FACT, ASSUMPTION, HYPOTHESIS, INFERENCE, OPINION, or UNKNOWN? | Information category tags |
| **6** | Evaluate sources | For each source: Authority, Proximity, Recency, Independence, Completeness | Source quality assessment |
| **7** | Check temporal validity | Is the information still true? When was it last verified? | Temporal status |
| **8** | Identify independent validation need | For D3+: can I validate independently? (Producer ≠ Validator) | Validation plan |

### Phase III: Decompose (Steps 9-12)

| Step | Action | Question | Output |
|------|--------|----------|--------|
| **9** | Map dependencies | What must happen before this? What depends on this? What can run in parallel? | Dependency map |
| **10** | Identify critical path | Which dependency chain is longest/binding? What's the slack? | Critical path |
| **11** | Decompose into work packages | Break objective → CSFs → conditions → actions → owners → evidence | Work package list |
| **12** | Assign owners | Who owns each action? (No ownerless tasks — §14: "Tasks without owners are intentions") | Ownership matrix |

### Phase IV: Execute (Steps 13-16)

| Step | Action | Question | Output |
|------|--------|----------|--------|
| **13** | Sequence actions | What order? (Critical deps first, high-impact blockers, irreversible decisions, long-lead items) | Execution sequence |
| **14** | Apply stop conditions | Should I stop? (§27: unsafe, unverifiable, out of scope, authority exceeded) | Go/no-go decision |
| **15** | Execute with discipline | Follow the plan. Record decisions. Expose blockers. Never fabricate progress. | Execution log |
| **16** | Collect evidence | What evidence proves each action was completed? (Not "I did it" — what proves it?) | Evidence bundle |

### Phase V: Validate & Close (Steps 17-20)

| Step | Action | Question | Output |
|------|--------|----------|--------|
| **17** | Verify outcomes | Did the success conditions (Step 4) actually become true? | Outcome verification |
| **18** | Check for anti-patterns | Did I fall into any of the 21 anti-patterns? (§37) | Anti-pattern audit |
| **19** | Determine operational status | Is this Designed, Documented, Implemented, Verified, Operational, or Outcome Confirmed? (§4) | Honest status |
| **20** | Report & learn | What should DAF know? What should I learn? (KEEP/IMPROVE/STOP/START/AUTOMATE/DELEGATE/ESCALATE) | Report + learning |

---

## Quick Decision Rules

| When... | Do... |
|---------|-------|
| Uncertain about diligence level | Apply higher level (§5: "When uncertain, apply higher level") |
| No evidence available | State UNKNOWN — do not infer (§9) |
| Information may be stale | Flag for re-validation (§11) |
| Producer = Validator | Request independent validation for D3+ (§20) |
| Task has no owner | Do not start — assign owner first (§14) |
| Stop condition triggered | STOP. Escalate. Document. (§27) |
| About to declare "completed" | Check: is this output or outcome? (§1) |
| About to declare "operational" | Apply 13-point gate (§33) |
| About to close an initiative | Apply 16-point closure gate (§44) |
| Reporting to DAF | Use 10-element reporting standard (§41) |

---

## The 8 Anti-Equivalence Principles (§1)

| Activity ≠ | Progress |
| Output ≠ | Outcome |
| Documentation ≠ | Implementation |
| Instruction ≠ | Execution |
| Approval ≠ | Adoption |
| Deployment ≠ | Operational Readiness |
| Technical Completion ≠ | Mission Success |
| Apparent Correctness ≠ | Verified Correctness |

**When in doubt:** The right side is harder. The right side is what matters.

---

## The Supreme Rule (§47)

> **DILIGENCE** = sufficient verification, foresight, control, traceability, and follow-through to make preventable failure increasingly unlikely.
>
> **ENGINEERED SUCCESS** = intentionally designing the complete chain of conditions for a desired outcome.

This takes precedence over speed, superficial completeness, and performative productivity whenever those objectives conflict.
