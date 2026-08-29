---
id: AIP-20260829-002
record_type: artifact
artifact_type: actionable-intelligence-protocol
title: "Exec Discipline & Session Integrity — Preventing False Diagnosis, Exec Failures, and Session Fragmentation"
created_at: 2026-08-29T16:20:00+00:00
updated_at: 2026-08-29T16:20:00+00:00
owner: faurani-jaafar
status: active
priority: high
sensitivity: internal
lifecycle_state: canonical
confidence: high
tags:
  - domain/cognitiveos-operations
  - domain/governance
  - domain/cognitiveos-operations
  - framework/actionable-intelligence-protocol
  - framework/aip
  - lifecycle/active
source:
  type: cognitive-loop
  reference: AIP Gate Tracker audit session 2026-08-29 16:04-16:19 UTC
summary: "Three concurrent failure modes during the AIP Gate Tracker audit: (1) exec tool reporting false failure on grep exit code 1, (2) session fragmentation delivering 9 intermediate preambles to Telegram, (3) ADEP-001 §7 violation — presenting untested speculation as diagnosis. This AIP defines sequenced actions to prevent all three."
strategic_significance: "The ADEP-001 §7 violation is the 6th instance of the conflation/overclaim pattern. The exec failure is a recurring tool-discipline gap. The session fragmentation is a user-experience degradation. All three are preventable through procedural discipline, not infrastructure changes."
mission_alignment:
  - cognitiveos-operations
  - governance
  - agent-discipline
related_records:
  - AIP-20260829-001
  - GOV-INTAKE-SOP-001
  - GOV-ADEP-001
  - TOOLS-001
related_initiative: INIT-20260824-001
---

# AIP-20260829-002 — Exec Discipline & Session Integrity

**Classification:** Internal | **Owner:** DAF | **Created:** 2026-08-30 00:20 MYT
**Source:** AIP Gate Tracker audit session 2026-08-29 16:04-16:19 UTC
**Priority:** High | **Status:** Active

---

## Purpose

Three failure modes occurred concurrently during the AIP Gate Tracker audit. Each is preventable through procedural discipline. This AIP defines the actions, guards, and verification steps to ensure they do not recur.

**Core question:** What procedural changes prevent (1) false exec failures from non-zero grep exits, (2) session fragmentation from large in-session audits, and (3) untested speculation presented as diagnosis?

---

## Intelligence Summary

### Failure Mode 1: Exec False Failure (grep exit code 1)

**What happened:** A grep command searching for "AIP-GATE" in the original `intake-sop.md` found zero matches. grep returns exit code 1 for "no match." OpenClaw's exec tool treats any non-zero exit as failure and surfaces "⚠️ 🛠️ Exec failed" to the user.

**Why it mattered:** The exec "failure" was actually a successful search result — the file didn't contain the pattern. The error message created confusion and required a separate troubleshooting turn.

**Evidence:**
- `grep -rn "AIP-GATE\|gate.tracker\|Gate Tracker" governance/intake-sop.md 2>/dev/null` → exit 1 (no match)
- OpenClaw source: `super(\`The executable failed with exit code: ${code} and error message: ${message}.\`)` — any non-zero exit triggers ExecutableError
- Tested 3 quoting variants (double quotes `\|`, `-E` with `|`, single quotes `\|`) — all work correctly. Quoting was NOT the cause.

### Failure Mode 2: Session Fragmentation

**What happened:** A large multi-file audit ran directly in the main session. 22 model fetch calls occurred between 16:04 and 16:08 UTC (one every 8-12 seconds). Each context window reset produced a preamble ("I've been executing this across multiple turns..."). 9 of these preambles were delivered to Telegram as standalone messages.

**Why it mattered:** DAF received 9 fragmented "I was already deep into this" messages instead of one clean response. The work was correct (7 commits, all pushed) but the delivery was unacceptable.

**Evidence:**
- Gateway logs: 22 `[model-fetch] start` entries in 4 minutes
- 9 Telegram `sendMessage` deliveries of preamble fragments
- Zero gateway errors, zero model failures, zero exec failures (except the grep exit code 1)

### Failure Mode 3: ADEP-001 §7 Violation (6th instance)

**What happened:** When asked to analyze the exec error, I led with a shell quoting theory ("the `\|` was likely misinterpreted by the shell") without testing it. When I did test it, I disproved my own theory but still presented it as the diagnosis.

**Why it mattered:** This is the 6th instance of the conflation/overclaim pattern documented in MEMORY.md. The pattern is: Ember takes untested assumptions and presents them as factual diagnosis. DAF has corrected this repeatedly. The behavioral correction has NOT taken root.

**Evidence:**
- First response: "The `\|` in the grep pattern was likely misinterpreted by the shell" — presented as diagnosis
- Test results: All 3 quoting variants work correctly — theory disproven
- Actual cause: grep exit code 1 (no match found) — a simple, boring explanation that required 5 seconds of testing to confirm

---

## High-Leverage AIP Items

### AIP-01: Normalize Non-Zero Exit Codes in Search Commands

**Leverage:** Prevents false exec failures from grep/find returning exit code 1 (no match). This is a tool-discipline fix, not an infrastructure change.

**Action:** Update TOOLS.md Exec Discipline section with:
- All grep commands must append `|| true` when used for existence checks
- Alternative: use `grep -c` (returns 0 even with 0 count) or `grep -q` (quiet mode)
- `find` commands already handle this correctly (exit 0 when no results with `-print`)
- Pattern: `grep -rn "pattern" file 2>/dev/null || true` → always exits 0

**Owner:** Ember
**Deadline:** Aug 30 (next session)
**Verification:** TOOLS.md updated. Next 10 exec calls using grep follow the pattern.

### AIP-02: Large Audits Use Subagents

**Leverage:** Prevents session fragmentation. Main session stays clean. Only the final report is delivered to the user.

**Action:** Define a size threshold for subagent delegation:
- **Threshold:** Any task requiring >5 tool calls OR >3 file edits → spawn subagent
- **Subagent type:** `sessions_spawn` with `mode="run"` and `context="isolated"`
- **Delivery:** Subagent completes work, returns result. Main session delivers only the final summary.
- **Exception:** Tasks requiring interactive DAF input stay in main session.

**Owner:** Ember
**Deadline:** Aug 30 (next session)
**Verification:** Next audit-class task (>5 tool calls) uses subagent. Main session delivers single response.

### AIP-03: ADEP-001 §7 Enforcement — Test Before Diagnose

**Leverage:** Prevents the 6th instance of the conflation/overclaim pattern. This is a behavioral discipline fix.

**Action:** Establish a mandatory pre-diagnosis protocol:
1. **State the hypothesis** explicitly: "I hypothesize X, but I have not tested it"
2. **Test the hypothesis** with a tool call BEFORE stating diagnosis
3. **If test confirms**: present as `[CONFIRMED]` with evidence
4. **If test disproves**: state "My initial hypothesis was wrong. The actual cause is Y" — do NOT lead with the disproven theory
5. **If unable to test**: state "I cannot verify this yet. My hypothesis is X, but it is untested."

**Rule:** "I think" and "I recall" and "likely" are NOT diagnostic statements. They are hypotheses. Present them as such or do not present them.

**Owner:** Ember
**Deadline:** Immediate (this session forward)
**Verification:** Next diagnostic task follows the protocol. No untested hypothesis presented as diagnosis.

### AIP-04: Document the 6th Instance in MEMORY.md

**Leverage:** Creates accountability. The pattern is persistent (6 instances in 7 days). Documentation creates a trackable record.

**Action:** Add to MEMORY.md under the cross-workstream conflation pattern:
- **Instance 6 (Aug 29):** Shell quoting theory presented as diagnosis for exec failure. Disproven by testing. Actual cause: grep exit code 1. ADEP-001 §7 violation.
- **Pattern:** Ember generates a plausible-sounding technical theory, presents it as diagnosis without testing, then when tested, the theory is disproven.
- **Behavioral correction:** Test BEFORE diagnosing. If unable to test, label as untested hypothesis.

**Owner:** Ember
**Deadline:** Aug 30 (next memory update)
**Verification:** MEMORY.md updated. Pattern counter shows 6 instances.

### AIP-05: Update AIP Gate Check Cron Job Prompt

**Leverage:** Prevents the cron job from sending false alerts when DEC records have resolved gates but the tracker hasn't been updated yet. Adds a cross-reference step.

**Action:** Update the cron job prompt to add:
- Step 2.5: "Scan recent DEC and ACT records from the same day. If any DEC/ACT record resolves a gate that is currently flagged as OVERDUE or UNKNOWN, note the discrepancy and correct the tracker BEFORE generating alerts."
- This makes the cron job self-correcting instead of just alerting.

**Owner:** Ember
**Deadline:** Sep 1 (before next cron run)
**Verification:** Cron job prompt updated. Next run cross-references DEC/ACT records.

---

## Sequencing & Dependencies

| # | Item | Deadline | Depends On | Parallel? |
|---|------|----------|------------|-----------|
| AIP-01 | Normalize grep exit codes in TOOLS.md | Aug 30 | None | Yes (with AIP-02, AIP-03) |
| AIP-02 | Large audits use subagents | Aug 30 | None | Yes (with AIP-01, AIP-03) |
| AIP-03 | Test-before-diagnose protocol | Immediate | None | Yes (with AIP-01, AIP-02) |
| AIP-04 | Document 6th instance in MEMORY.md | Aug 30 | None | Yes |
| AIP-05 | Update cron job prompt | Sep 1 | None | Yes |

**All items are independent and can be executed in parallel.**

---

## Success Metrics

| Metric | Target | Measurement | Cadence |
|--------|--------|-------------|---------|
| False exec failures from grep | 0 per week | Count of "Exec failed" from grep exit 1 | Weekly |
| Session fragmentation events | 0 per week | Count of >2 preamble messages in a single turn | Weekly |
| ADEP-001 §7 violations | 0 per week | Count of untested hypotheses presented as diagnosis | Weekly |
| Subagent usage for >5-tool-call tasks | 100% | Count of subagent spawns vs main-session audits | Weekly |

---

## Risk Assessment

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| AIP-03 protocol not internalized (7th instance) | Medium (pattern is persistent) | High (trust erosion) | AIP-04 documents the pattern. Next violation triggers a stricter gate. |
| Subagent overhead makes small tasks slower | Low | Low | Threshold set at >5 tool calls. Small tasks stay in main session. |
| Cron job cross-reference adds latency | Low | Low | Isolated session, no user-facing impact. Extra 30-60 seconds acceptable. |

---

## Relationship to Existing AIPs

| AIP | Relationship |
|-----|-------------|
| AIP-20260829-001 (Fuad Capacity) | Same date, different domain. Both address structural constraints. |
| AIP-PRODUCTIZATION-OPERATIONALIZATION | Parent framework. This AIP addresses agent operational discipline, not productization. |
| AIP-GATE-TRACKER | This AIP was triggered by the AIP Gate Tracker audit. AIP-05 improves the tracker's cron job. |

---

## Loop Output — Pending Register

| # | Item | Owner | Deadline | Status |
|---|------|-------|----------|--------|
| 1 | Update TOOLS.md with grep || true discipline | Ember | Aug 30 | Pending |
| 2 | Define subagent threshold in AGENTS.md | Ember | Aug 30 | Pending |
| 3 | Apply test-before-diagnose protocol | Ember | Immediate | Active |
| 4 | Document 6th conflation instance in MEMORY.md | Ember | Aug 30 | Pending |
| 5 | Update AIP Gate Check cron job prompt | Ember | Sep 1 | Pending |

---

*This AIP was authored in direct response to DAF's directive. It addresses three failure modes that occurred concurrently. The ADEP-001 §7 violation is the most serious — it is a trust issue, not a technical issue.*
