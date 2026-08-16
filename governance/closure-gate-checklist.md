# Closure Gate Checklist

**Created:** 2026-08-16  
**Owner:** Ember  
**Authority:** DAF  
**Governing Framework:** ADEP-001 §44 (Closure Gate)  
**Classification:** CANONICAL

---

## Purpose

No significant objective, initiative, or workstream may be declared "closed" or "completed" without passing all 16 points of this gate. This prevents premature closure — the anti-pattern of declaring success based on output production rather than outcome achievement (ADEP §1: output ≠ outcome).

---

## The 16-Point Gate

### Section A: Outcome Verification (Points 1-4)

| # | Gate Point | Evidence Required | Pass |
|---|-----------|-------------------|------|
| 1 | **Original objective achieved** | Statement of original objective + evidence it was achieved (not just that work was done) | ☐ |
| 2 | **Definition of Done met** | The DoD from the objective statement is satisfied, with evidence | ☐ |
| 3 | **Success conditions confirmed** | All Critical Success Factors are met | ☐ |
| 4 | **Adoption verified** | Intended users are actually using the output (not just that it was delivered) | ☐ |

### Section B: Evidence & Documentation (Points 5-8)

| # | Gate Point | Evidence Required | Pass |
|---|-----------|-------------------|------|
| 5 | **Evidence collected** | Concrete evidence (metrics, logs, test results, user feedback) — not assertion | ☐ |
| 6 | **Documentation complete** | All records (INT, ACT, DEC, RSK) updated to reflect final state | ☐ |
| 7 | **Lessons captured** | Post-execution learning loop (§36) completed: KEEP/IMPROVE/STOP/START/AUTOMATE/DELEGATE/ESCALATE | ☐ |
| 8 | **Assumption register reviewed** | All material assumptions validated or explicitly accepted as residual risk | ☐ |

### Section C: Risk & Dependency Closure (Points 9-12)

| # | Gate Point | Evidence Required | Pass |
|---|-----------|-------------------|------|
| 9 | **No open critical risks** | No RSK records with status=active and severity=high/critical related to this objective | ☐ |
| 10 | **Dependencies resolved** | All inbound dependencies were resolved; no orphaned dependents | ☐ |
| 11 | **Failure modes reviewed** | All identified failure modes (§25) assessed — either prevented, mitigated, or accepted as residual risk | ☐ |
| 12 | **Stop conditions checked** | No active stop conditions (§27) that would prevent closure | ☐ |

### Section D: Institutional Memory (Points 13-16)

| # | Gate Point | Evidence Required | Pass |
|---|-----------|-------------------|------|
| 13 | **Knowledge transferred** | Critical knowledge is documented and accessible to those who need it | ☐ |
| 14 | **Sustainability plan** | How will the successful state be maintained? Who owns it going forward? | ☐ |
| 15 | **Related records updated** | All records referencing this objective are updated (indexes, cross-references, parent/child links) | ☐ |
| 16 | **DAF sign-off** | The authority confirms the objective is achieved and the initiative can be closed | ☐ |

---

## Process

1. **Initiate closure request** — State the objective, reference the original DEC/INIT record
2. **Walk through all 16 points** — For each, provide evidence or identify the gap
3. **If any point fails** — The objective CANNOT be closed. Document the blocker and remediation plan.
4. **If all 16 pass** — Record the closure with evidence, update the Process Maturity Register, commit to Git
5. **Post-closure** — Trigger §36 Post-Execution Learning Loop within 7 days

---

## Anti-Patterns This Gate Prevents

- **"We shipped it" = success** — No. Point 4 (adoption) and Point 1 (outcome) must be met.
- **"All tasks are done" = success** — No. Tasks are output; outcome is what matters (§1).
- **"No one complained" = success** — No. Point 5 requires positive evidence, not absence of negative.
- **"We'll learn from this later"** — No. Point 7 requires learning loop completion before closure.
- **"The risks didn't materialize"** — No. Point 11 requires explicit assessment, not luck.

---

## Application to CyberDSA 2026

The CyberDSA 2026 initiative (INIT-20260810-003, war-room DEC-20260815-004) will be subject to this gate after the event (post-October 7). A preliminary assessment will be conducted at CP2 (Sep 5) to identify closure gaps early.
