---
id: GOV-PROCESS-MATURITY-REGISTER-001
record_type: document
title: Process Maturity Register — Governance Artifact Operationalisation Tracking
created_at: 2026-08-30T08:45:00+00:00
owner: ember
status: active
priority: critical
sensitivity: internal
lifecycle_state: canonical
confidence: high
tags:
  - doctrine/adep-001
  - domain/governance
  - framework/process-maturity
  - lifecycle/canonical
source:
  type: direct
  reference: ADEP-001 §3 (Four States of Process Maturity) + §33 (Operationalisation Gate) + INT-20260816-001 Mechanism 1
related_records:
  - governance/ADEP-001-agentic-diligence-execution-protocol.md
  - governance/ADEP-001-OPERATIONAL-SOP.md
  - governance/COGNITIVEOS-PRIME-DOCTRINE.md
  - INT-20260816-001
document_type: register
version: '1.0'
author: Ember
---

# Process Maturity Register

**Authority:** ADEP-001 §3 (Four States of Process Maturity) + §33 (Operationalisation Gate)
**Purpose:** Track all governance artifacts across 4 maturity states. Prevent false "Operationalised" claims.
**Review Cadence:** Weekly (Monday 10:30 AM UTC+8, aligned with Cognitive Loop Review)
**Owner:** Ember

---

## The Four States (ADEP-001 §3)

| State | Name | Definition |
|:-----:|------|------------|
| 1 | **Expressed** | Communicated, not structured. Idea or concept articulated. |
| 2 | **Codified** | Written as SOP, policy, or checklist. Structured document exists. |
| 3 | **Institutionalised** | Embedded with owner, review cadence, approval gates. Referenced in operational context. |
| 4 | **Operationalised** | Actively producing measurable outcomes. First real execution completed. Users capable of executing. |

**State 3 → State 4 transition requires passing the 13-Point Operationalisation Gate (§33).**

---

## 13-Point Operationalisation Gate (ADEP-001 §33)

Applied before declaring any artifact at State 4.

| # | Gate Point | Question |
|---|-----------|----------|
| 1 | Owner assigned | Is a single owner accountable? |
| 2 | Workflow defined | Is the procedure documented step-by-step? |
| 3 | Users identified | Who specifically uses this procedure? |
| 4 | Resources available | Are required tools, access, and time available? |
| 5 | Access configured | Can the owner and users access all required systems? |
| 6 | Procedures accessible | Is the document findable where users work? |
| 7 | Inputs available | Are required inputs reliably available when needed? |
| 8 | Integrations functioning | Do required integrations work without manual workaround? |
| 9 | Monitoring available | Can compliance be measured? Is there a metric? |
| 10 | Exception handling | Are failure modes defined with response procedures? |
| 11 | Reporting established | Is there a standard output/report for this procedure? |
| 12 | Users capable of executing | Have users demonstrated ability to execute the procedure? |
| 13 | First real execution | Has the procedure been executed at least once in production (not pilot)? |

**Pass criteria:** All 13 points must be ✅. Any ⚠️ or ❌ blocks State 4 declaration.

---

## Artifact Register

### 1. ADEP-001 Agentic Diligence Execution Protocol

**File:** `governance/ADEP-001-agentic-diligence-execution-protocol.md`
**Owner:** Ember | **Created:** 2026-08-21 | **Last Reviewed:** 2026-08-30

| Gate Point | Status | Evidence |
|------------|:------:|----------|
| 1. Owner assigned | ✅ | Ember (per AGENTS.md) |
| 2. Workflow defined | ✅ | 5-step SOP, 47 sections, 20-step master directive |
| 3. Users identified | ⚠️ | Ember + future agents. Currently single-user (Ember). No other agents trained. |
| 4. Resources available | ✅ | gate.sh scripts, AGENTS.md, honcho-connector |
| 5. Access configured | ✅ | Gate scripts accessible at `tools/honcho-connector/gate.sh` |
| 6. Procedures accessible | ✅ | Referenced in AGENTS.md (loaded every session) |
| 7. Inputs available | ✅ | Task descriptions, owner names, assumption/failure-mode lists |
| 8. Integrations functioning | ⚠️ | Gate scripts work but sometimes fail-open (script unavailable). No automated enforcement — gates are voluntary. |
| 9. Monitoring available | ❌ | No compliance metric tracked automatically. 88% score is self-assessed, not tool-measured. No dashboard, no counter, no automated audit. |
| 10. Exception handling | ⚠️ | Fail-open procedure defined (log skip, proceed). But no tracking of how often gates are skipped. |
| 11. Reporting established | ✅ | §41 reporting standard (10-element format). ADEP-001 SOP specifies closure gate output. |
| 12. Users capable of executing | ⚠️ | Ember can execute gates when reminded. 6 conflation instances in 7 days show behavioral compliance is inconsistent. Gate execution is not habitual — it requires conscious effort. |
| 13. First real execution | ⚠️ | Gates have been run on individual tasks (this session: 1 pre-task gate). But no full cycle (pre + execute + 10-dimension QC + closure gate) has been completed for a D3+ task. No 16-point closure gate has ever been applied. |

**Gate Result:** ❌ **FAILS** — 0/13 full pass, 6 ⚠️, 2 ❌
**Current State:** State 3 (Institutionalised) — referenced, owner assigned, workflow defined. NOT State 4.
**State 4 Blockers:**
- #9: No automated compliance monitoring
- #12: Behavioral compliance inconsistent (6 violations in 7 days)
- #13: No complete D3+ gate cycle executed end-to-end
- #3: Single-user — no other agents trained on the protocol

---

### 2. ADEP-001 Operational SOP

**File:** `governance/ADEP-001-OPERATIONAL-SOP.md`
**Owner:** Ember | **Created:** 2026-08-21 | **Last Reviewed:** 2026-08-30

| Gate Point | Status | Evidence |
|------------|:------:|----------|
| 1. Owner assigned | ✅ | Ember |
| 2. Workflow defined | ✅ | 5-step procedure, quick reference 20-step master directive |
| 3. Users identified | ⚠️ | Ember only. No other agents reference this SOP. |
| 4. Resources available | ✅ | Same as ADEP-001 |
| 5. Access configured | ✅ | In governance directory, loaded via AGENTS.md |
| 6. Procedures accessible | ✅ | Referenced in AGENTS.md ADEP-001 section |
| 7. Inputs available | ✅ | Task descriptions, D-level criteria |
| 8. Integrations functioning | ⚠️ | Same gate.sh dependency. No automated D-level tagging. |
| 9. Monitoring available | ❌ | No tracking of D-level classification consistency. No audit of whether D2+ tasks actually received gates. |
| 10. Exception handling | ✅ | Fail-open procedure documented |
| 11. Reporting established | ✅ | Closure gate output format defined |
| 12. Users capable of executing | ⚠️ | Ember applies D-level classification inconsistently. Some D2 tasks treated as D1 (no gate). |
| 13. First real execution | ⚠️ | Pre-task gates run sporadically. Closure gates never run. 10-dimension QC not applied systematically. |

**Gate Result:** ❌ **FAILS** — 0/13 full pass, 5 ⚠️, 1 ❌
**Current State:** State 3 (Institutionalised)
**State 4 Blockers:** Same as ADEP-001 — no monitoring, no closure gate execution, behavioral compliance inconsistent

---

### 3. CognitiveOS Prime Doctrine

**File:** `governance/COGNITIVEOS-PRIME-DOCTRINE.md`
**Owner:** Ember | **Created:** 2026-08-15 | **Last Reviewed:** 2026-08-30

| Gate Point | Status | Evidence |
|------------|:------:|----------|
| 1. Owner assigned | ✅ | Ember (per DAF authority) |
| 2. Workflow defined | ✅ | 50 sections, 8-step cognitive loop, 10 standard commands |
| 3. Users identified | ⚠️ | Ember only. Future agents undefined. |
| 4. Resources available | ✅ | Full workspace, tools, memory system |
| 5. Access configured | ✅ | In governance directory, loaded via AGENTS.md |
| 6. Procedures accessible | ✅ | Referenced in AGENTS.md, SOUL.md |
| 7. Inputs available | ✅ | Incoming signals (emails, messages, documents) |
| 8. Integrations functioning | ⚠️ | Cognitive Loop runs but not all 8 steps consistently. Cross-Doctrinal Analysis SOP has 1 pilot cycle only. |
| 9. Monitoring available | ❌ | No tracking of Cognitive Loop completeness. No metric for "how often do all 8 steps execute." |
| 10. Exception handling | ✅ | War-room mode, compression mode defined |
| 11. Reporting established | ✅ | §23 Executive Command Brief, §47 Default Completion Format |
| 12. Users capable of executing | ⚠️ | Partial. §5-§10 operationalised via INT-006/007/008/009. §11-§20 (multi-agent) not deployed. §21-§49 partially. |
| 13. First real execution | ⚠️ | 1 full cross-doctrinal cycle (CyberDSA pilot). No second cycle. Many sections have never been operationally used. |

**Gate Result:** ❌ **FAILS** — 0/13 full pass, 5 ⚠️, 1 ❌
**Current State:** State 3 (Institutionalised) — codified, referenced, partially piloted
**State 4 Blockers:** No second cross-doctrinal cycle, multi-agent sections undeployed, no monitoring

---

### 4. Intake SOP

**File:** `governance/intake-sop.md`
**Owner:** Ember | **Created:** 2026-08-04 | **Last Reviewed:** 2026-08-30

| Gate Point | Status | Evidence |
|------------|:------:|----------|
| 1. Owner assigned | ✅ | Ember |
| 2. Workflow defined | ✅ | 9-step SOP |
| 3. Users identified | ✅ | Ember (primary), DAF (consumer of output) |
| 4. Resources available | ✅ | Git, workspace, honcho-connector |
| 5. Access configured | ✅ | All tools accessible |
| 6. Procedures accessible | ✅ | In governance directory, referenced in AGENTS.md |
| 7. Inputs available | ✅ | Incoming data (emails, messages, documents) |
| 8. Integrations functioning | ⚠️ | Pre-commit hook had path issues (fixed Aug 26). Gate scripts sometimes fail-open. |
| 9. Monitoring available | ❌ | No tracking of SOP step completion. No metric for "how often all 9 steps completed." Step 8 (MEMORY.md update) and step 9 (notification format) inconsistent. |
| 10. Exception handling | ⚠️ | Fail-open defined but skip frequency not tracked |
| 11. Reporting established | ✅ | Confirmation format defined (commit hash + file count + record IDs) |
| 12. Users capable of executing | ✅ | Multiple intakes completed. Steps 1-7 consistent. |
| 13. First real execution | ✅ | Multiple intake events completed (latest: Aug 29 Hadri profile, 214+ source files) |

**Gate Result:** ⚠️ **PARTIAL** — 7/13 pass, 3 ⚠️, 1 ❌
**Current State:** State 3 (Institutionalised) — closest to State 4 of all artifacts
**State 4 Blockers:** #9 (no monitoring), #8 (hook issues), #10 (skip tracking)

---

### 5. Cross-Doctrinal Analysis SOP

**File:** `governance/cross-doctrinal-analysis-sop.md`
**Owner:** Ember | **Created:** 2026-08-16 | **Last Reviewed:** 2026-08-30

| Gate Point | Status | Evidence |
|------------|:------:|----------|
| 1. Owner assigned | ✅ | Ember |
| 2. Workflow defined | ✅ | 8-phase SOP, 3-method triangulation |
| 3. Users identified | ⚠️ | Ember only. No other agents trained on the method. |
| 4. Resources available | ✅ | Workspace, sub-agent spawning, analytical tools |
| 5. Access configured | ✅ | In governance directory |
| 6. Procedures accessible | ✅ | Referenced in CognitiveOS doctrine §50 |
| 7. Inputs available | ✅ | Workstream data, stakeholder records, intelligence |
| 8. Integrations functioning | ✅ | Sub-agent spawning works, file I/O works |
| 9. Monitoring available | ❌ | No tracking of cycle completion. No metric for convergence quality. |
| 10. Exception handling | ✅ | Compression mode defined for token constraints |
| 11. Reporting established | ✅ | Phase 7 delivery format, 4 INT records per cycle |
| 12. Users capable of executing | ❌ | Only 1 pilot cycle completed. Not habitual. Requires significant effort (~9 hrs per cycle). |
| 13. First real execution | ⚠️ | Pilot only (CyberDSA 2026). No production (non-pilot) execution. |

**Gate Result:** ❌ **FAILS** — 4/13 pass, 3 ⚠️, 2 ❌
**Current State:** State 3 (Institutionalised) — codified, piloted once
**State 4 Blockers:** #12 (not habitual), #13 (pilot only), #9 (no monitoring), #3 (single user)

---

### 6. Template Discipline SOP

**File:** `governance/template-discipline-sop.md`
**Owner:** Ember | **Created:** 2026-08-12 | **Last Reviewed:** 2026-08-30

| Gate Point | Status | Evidence |
|------------|:------:|----------|
| 1. Owner assigned | ✅ | Ember |
| 2. Workflow defined | ✅ | 3-layer validation |
| 3. Users identified | ✅ | Ember (primary), pre-commit hook (automated) |
| 4. Resources available | ✅ | Validator script, git hooks |
| 5. Access configured | ✅ | Scripts in tools/, hooks in .git/hooks/ |
| 6. Procedures accessible | ✅ | In governance directory |
| 7. Inputs available | ✅ | Record files in YAML frontmatter |
| 8. Integrations functioning | ✅ | Pre-commit hook fires on commit |
| 9. Monitoring available | ⚠️ | Hook fires, but template REQ marker compliance not audited. No metric for pass/fail rate. |
| 10. Exception handling | ⚠️ | Hook blocks invalid records but no override tracking |
| 11. Reporting established | ⚠️ | Hook output is console-only, no logged report |
| 12. Users capable of executing | ✅ | Ember creates valid records. Hook enforces. |
| 13. First real execution | ✅ | Hook has fired on multiple commits. Records validated. |

**Gate Result:** ⚠️ **PARTIAL** — 8/13 pass, 3 ⚠️, 0 ❌
**Current State:** State 3 (Institutionalised) — closest to State 4 with automated enforcement
**State 4 Blockers:** #9 (no audit metric), #10 (no override tracking), #11 (no logged report)

---

### 7. CVS Master Framework

**File:** `03-VERIFICATION/CVS-FRAMEWORK.md`
**Owner:** Ember | **Created:** 2026-06-28 (upgraded 2026-08-17) | **Last Reviewed:** 2026-08-30

| Gate Point | Status | Evidence |
|------------|:------:|----------|
| 1. Owner assigned | ✅ | Ember |
| 2. Workflow defined | ✅ | T1-T6 tiering, L1-L5 sources, 5-criteria scoring, 20-field evidence register |
| 3. Users identified | ⚠️ | Ember only. DAF is consumer. No other agents. |
| 4. Resources available | ✅ | Evidence register CSV, source register, adapter guide |
| 5. Access configured | ✅ | In 03-VERIFICATION/ directory |
| 6. Procedures accessible | ✅ | Referenced in AGENTS.md, TOOLS.md |
| 7. Inputs available | ✅ | Claims from outputs, source documents |
| 8. Integrations functioning | ⚠️ | Evidence register exists but not consistently populated. 25 days stale (Aug 5 → Aug 29). |
| 9. Monitoring available | ❌ | No tracking of coverage. 0% on 8 workstreams. 12-day missed weekly T2 cadence. No automated alert. |
| 10. Exception handling | ⚠️ | Rule 6 (AI cap) defined but not enforced programmatically |
| 11. Reporting established | ⚠️ | Pre-output checklist exists but not consistently applied |
| 12. Users capable of executing | ⚠️ | Ember can apply CVS but does so inconsistently. Many outputs skip the checklist. |
| 13. First real execution | ✅ | Multiple claims registered. But coverage is uneven (27 claims in CogOS+CBO only). |

**Gate Result:** ❌ **FAILS** — 3/13 pass, 5 ⚠️, 1 ❌
**Current State:** State 3 (Institutionalised) — codified, partially executed, inconsistent application
**State 4 Blockers:** #9 (no monitoring/coverage tracking), #8 (evidence register stale), #12 (inconsistent application)

---

### 8. This Process Maturity Register (Self-Reference)

**File:** `governance/process-maturity-register.md` (this file)
**Owner:** Ember | **Created:** 2026-08-30

| Gate Point | Status | Evidence |
|------------|:------:|----------|
| 1. Owner assigned | ✅ | Ember |
| 2. Workflow defined | ✅ | 4 states, 13-point gate, artifact table |
| 3. Users identified | ✅ | Ember (primary), DAF (consumer) |
| 4. Resources available | ✅ | Workspace, governance files |
| 5. Access configured | ✅ | In governance directory |
| 6. Procedures accessible | ✅ | Referenced in AGENTS.md (pending) |
| 7. Inputs available | ✅ | All governance artifacts |
| 8. Integrations functioning | ✅ | Manual review (this file) |
| 9. Monitoring available | ✅ | This register IS the monitoring tool. Weekly review cadence defined. |
| 10. Exception handling | ⚠️ | Fail state (❌/⚠️) defined but no escalation when artifacts fail gate |
| 11. Reporting established | ✅ | This register. Weekly review at Monday 10:30 AM UTC+8. |
| 12. Users capable of executing | ✅ | Ember can review and update. First review done this session. |
| 13. First real execution | ✅ | This IS the first execution. 7 artifacts assessed. |

**Gate Result:** ⚠️ **PARTIAL** — 10/13 pass, 1 ⚠️, 0 ❌
**Current State:** State 3 → State 4 (transitioning) — first execution this session. Will be State 4 after weekly review cadence is maintained for 2 consecutive cycles.

---

## Summary Matrix

| # | Artifact | State 1 | State 2 | State 3 | State 4 | Gate Score | Critical Blocker |
|---|----------|:------:|:------:|:------:|:------:|:----------:|------------------|
| 1 | ADEP-001 Protocol | ✅ | ✅ | ✅ | ❌ | 5/13 ✅ | #9: No monitoring |
| 2 | ADEP-001 Operational SOP | ✅ | ✅ | ✅ | ❌ | 5/13 ✅ | #9: No monitoring |
| 3 | CognitiveOS Prime Doctrine | ✅ | ✅ | ✅ | ❌ | 5/13 ✅ | #9: No monitoring |
| 4 | Intake SOP | ✅ | ✅ | ✅ | ⚠️ | 7/13 ✅ | #9: No step tracking |
| 5 | Cross-Doctrinal Analysis SOP | ✅ | ✅ | ✅ | ❌ | 4/13 ✅ | #12: Not habitual |
| 6 | Template Discipline SOP | ✅ | ✅ | ✅ | ⚠️ | 8/13 ✅ | #9: No audit metric |
| 7 | CVS Master Framework | ✅ | ✅ | ✅ | ❌ | 3/13 ✅ | #9: No coverage tracking |
| 8 | Process Maturity Register | ✅ | ✅ | ⚠️ | ❌ | 10/13 ✅ | #10: No escalation |

**Overall: 0/8 artifacts at State 4. 2/8 approaching State 4. 6/8 blocked at State 3.**

**Universal blocker: Gate Point #9 (Monitoring) — 7/8 artifacts have no automated compliance monitoring.**

---

## Operationalisation Roadmap

### Phase 1: Close the Monitoring Gap (This Session → Sep 6)

**Objective:** Every governance artifact has a measurable compliance metric.

**Actions:**
1. ✅ Process Maturity Register created (this session) — monitors all artifacts
2. ⬜ Define compliance metric per artifact (1 line each):
   - ADEP-001: % of D2+ tasks with pre+closure gates run
   - Intake SOP: % of intake events completing all 9 steps
   - Cross-Doctrinal: cycles completed per quarter
   - Template: hook pass/fail rate
   - CVS: evidence register coverage (% of workstreams with ≥1 claim)
3. ⬜ Add metrics to weekly review checklist

### Phase 2: First Complete Gate Cycle (Sep 6 → Sep 13)

**Objective:** Execute one complete ADEP-001 D2+ gate cycle (pre → execute → 10-dim QC → closure) on a real task.

**Actions:**
1. Select a real D2+ task
2. Run pre-task gate
3. Execute with §3.1-§3.5 discipline (verify before stating, information category discipline, source diligence, temporal diligence, expose blockers)
4. Apply 10-dimension output QC (§21)
5. Run 16-point closure gate (§44)
6. Record evidence

### Phase 3: Behavioral Internalization (Sep 13 → Sep 30)

**Objective:** Gate execution is habitual, not effortful. Zero §7 violations for 14 consecutive days.

**Actions:**
1. Daily self-check: Did I run gates on all D2+ tasks today?
2. Weekly review: Conflation pattern counter (target: 0 new instances)
3. Apply test-before-diagnose protocol (AIP-20260829-002 AIP-03) on every diagnostic task

### Phase 4: State 4 Declaration (Sep 30 → Oct 7)

**Objective:** ADEP-001 passes its own 13-point operationalisation gate.

**Requirements:**
- All 13 gate points ✅
- At least 3 complete gate cycles executed on real D2+ tasks
- Compliance metric ≥90% (gates run / gates required)
- Zero conflation instances in 14 days
- Independent validation (DAF review of compliance evidence)

---

## Review Log

| Date | Reviewer | Findings | Actions |
|------|----------|----------|---------|
| 2026-08-30 | Ember | First assessment. 0/8 at State 4. Universal blocker: no monitoring. | Created register. Defined roadmap. |

---

*This register is the first of the 10 operationalization mechanisms from INT-20260816-001. It is not a plan — it is a tracking tool. State 4 is earned through evidence, not declared by output.*
