# PIR Closure Framework — Workflow Analytical Report

**Report ID:** RPT-WF-PIR-CLOSURE-001
**Generated:** 2026-08-17T16:52:00Z
**Scope:** Review of the full workflow from initial request through CVS correction to current state
**Author:** Ember (AI-generated, T2 max per CVS Rule 6)
**Classification:** TLP:AMBER

---

## 1. Executive Summary

**What was requested:** A formal PIR Closure Framework defining the process for transitioning individual PIRs from active collection to terminal states, closing the intelligence-layer ↔ record-layer synchronisation gap identified in the Aug 3 status report.

**What happened:** The framework was drafted successfully in a single pass, but the CVS application went through two phases — an initial misapplication of the wrong CVS instrument (DUN-profiling-specific), followed by a correction to the CVS Master Framework. The correction required a full rewrite of all CVS tags, creation of Evidence Register entries, and re-scoring of every claim under the correct 5-criteria model.

**Current state:** Framework is complete and CVS-compliant under the correct instrument. Evidence Register is populated with 20 claims. One structural blocker remains (git commit blocked by `.gitignore`).

**Verdict:** Framework is ready for DAF ratification. The CVS misapplication was caught and corrected, but it consumed approximately 12 minutes of additional work that would not have been necessary if the correct instrument had been applied initially.

---

## 2. Chronological Workflow Timeline

| Time (UTC) | Phase | Event | Output |
|------------|-------|-------|--------|
| 16:36:21 | **Request** | DAF issues: "PIR closure Framework" | — |
| 16:36–16:37 | **Research** | Searched workspace, read 6 source files (closure-gate-checklist, pir-inventory-index, pir.schema.json, pir-template, pir-status-report, validate.sh) | 6 source files loaded |
| 16:37:32 | **Draft** | Framework drafted and saved — 13 sections, ~19.6KB | First version of `pir-closure-framework.md` |
| 16:39:46 | **CVS Request** | DAF issues: "CVS need to apply here" | — |
| 16:39–16:41 | **CVS Applied (WRONG)** | Applied `tools/truth-validator/CVS-MANDATE.md` — the DUN-profiling CVS (Tier 1/2/3, `[VERIFIED]`, `SPECULATION:`) | Framework tagged with wrong labels |
| 16:41:34 | **Validation** | `validate.sh` passed (0 errors, 2 warnings — both false positives for governance doc) | — |
| 16:46:56 | **Correction Flag** | DAF issues: "CVS register vs cvs" — flagging the misapplication | — |
| 16:47–16:49 | **CVS Correction** | 7 split-session fragments as Ember recognised error, read correct CVS docs (CVS-FRAMEWORK.md, CVS-SOURCE-REGISTER.md, CVS-ADAPTER-GUIDE.md) | — |
| 16:49 | **Rewrite** | Framework rewritten with correct CVS Master Framework labels, scoring, and Rule 6 application | Second version of `pir-closure-framework.md` (35KB, 531 lines) |
| 16:49 | **Evidence Register** | 20 CVS-COG claim rows appended to `CVS-EVIDENCE-REGISTER.csv` | Register: 22 total rows |
| 16:51:51 | **Report Request** | DAF issues: "Review the workflow so far and generate a detailed and structured analytical report" | This report |

**Total elapsed time:** ~16 minutes (request to report request)
**Correction overhead:** ~12 minutes (misapplication → correction → rewrite → re-register)

---

## 3. Artifacts Produced

### 3.1 Primary Deliverable

| Attribute | Value |
|-----------|-------|
| **File** | `strategic-cognitiveos/governance/pir-closure-framework.md` |
| **Size** | 35,042 bytes (35KB) |
| **Lines** | 531 |
| **Words** | 4,595 |
| **Sections** | 15 (§1–§15) |
| **Versions** | 2 (initial draft with wrong CVS, final with correct CVS) |

### 3.2 Section Inventory

| § | Title | Lines | Function |
|---|-------|-------|----------|
| 1 | Problem Statement | L43–61 | Defines the 90/120 sync gap and 4 gaps the framework closes |
| 2 | PIR Lifecycle States | L62–128 | Organises 20 schema statuses into 5 phases with flow diagram |
| 3 | Closure Criteria | L130–198 | 6-point fulfilment criteria + priority-scaled evidence thresholds + cancellation/supersession/deferral rules |
| 4 | Status Transition Matrix | L200–216 | 9×11 transition grid (allowed/forbidden transitions) |
| 5 | OSINT-Unresolvable Escalation | L218–252 | Protocol for 12 structurally unresolvable PIRs (≥2 cycles → blocked → escalate/defer/cancel) |
| 6 | Roles & Authority | L254–270 | 4-role authority matrix + auto-fulfil exception + Rule 6 note |
| 7 | SLA Framework | L272–301 | TTFI targets (3/7/14/30 days) + TTC targets/limits (14-30/30-60/60-90/90-180) |
| 8 | Record Sync Protocol | L303–348 | 8-step sync procedure + priority order + flow diagram |
| 9 | Audit Trail | L350–370 | Required artifacts per closure + weekly audit checklist |
| 10 | Initiative Closure Linkage | L372–385 | PIR terminal state as prerequisite to 16-point gate |
| 11 | Metrics & KPIs | L387–399 | 7 metrics with targets and sources |
| 12 | Closure Decision Tree | L401–420 | Quick-reference decision flowchart |
| 13 | Implementation Roadmap | L422–435 | 6-phase rollout (ratification → monthly metrics) |
| 14 | CVS Compliance Statement | L437–498 | Full claim inventory (20 claims) + score breakdown + label summary |
| 15 | CVS Evidence Register Entries | L500–531 | CSV block of all 20 CVS-COG rows for audit trail |

### 3.3 Secondary Deliverable

| Attribute | Value |
|-----------|-------|
| **File** | `03-VERIFICATION/CVS-EVIDENCE-REGISTER.csv` |
| **Previous state** | 1 header + 1 example row (CVS-MAST-001) |
| **Current state** | 1 header + 21 data rows (1 master + 20 CogOS) |
| **Schema** | 20-field CSV per CVS Master Framework §6 |

---

## 4. Source Dependency Analysis

### 4.1 Primary Source Files (Cited in Framework)

| Source File | Type | L-Level | Citations | Role in Framework |
|-------------|------|---------|-----------|-------------------|
| `pir-status-report-2026-08-03.md` | Internal report | L2 | 10 line refs (#L23, #L32-34, #L36, #L37, #L46, #L69-72, #L86, #L176) | Primary evidence for the sync gap |
| `pir-inventory-index.md` | Internal record | L2 | 6 line refs (#L25, #L29, #L39, #L108-113, #L117) | Inventory counts, cronjob coverage |
| `pir.schema.json` | Schema file | L2 | 1 programmatic verification (2026-08-17) | Status enum authority |
| `closure-gate-checklist.md` | Governance doc | L2 | 2 line refs (#L6) | ADEP-001 §44 authority chain |
| `CVS-FRAMEWORK.md` | Governance doc | L1 | 3 section refs (§3, §5, §7 Rule 6) | CVS standard authority |
| `CVS-SOURCE-REGISTER.md` | Governance doc | L1 | 1 ref (L2 definition) | Source hierarchy authority |

### 4.2 Source Coverage

- **Line-level citations:** 14 unique `#L` references across 4 source files
- **Programmatic verification:** 1 (schema enum via Python)
- **Section-level citations:** 3 (CVS-FRAMEWORK.md §3, §5, §7)
- **Total source files touched:** 6 primary + 3 CVS reference docs = 9

---

## 5. CVS Compliance Analysis

### 5.1 Instrument Selection (Critical Error & Correction)

| Dimension | Initial (Wrong) | Final (Correct) |
|-----------|-----------------|-----------------|
| **Instrument** | `tools/truth-validator/CVS-MANDATE.md` | `03-VERIFICATION/CVS-FRAMEWORK.md` |
| **Scope** | DUN profiling (Johor PRN 2026 election briefs) | Universal — all workstreams |
| **Tier system** | 3 tiers (T1 factual / T2 analytical / T3 predictive) | 6 tiers (T1 confirmed → T6 excluded) |
| **Source levels** | None defined | L1–L5 (official → AI/informal) |
| **Labels** | `[VERIFIED]`, `[HIGH]`, `[MEDIUM]`, `SPECULATION:` | `[CONFIRMED]`, `[SOURCE-BACKED]`, `[ASSESSMENT]`, `[ASSUMPTION]`, `[DISPUTED]`, `[EXCLUDED]` |
| **Scoring** | None | 5-criteria × 0–2 = 0–10 total |
| **Rule 6** | Not applicable | AI output capped at T2, max score 7 |
| **Evidence Register** | Not used | `CVS-EVIDENCE-REGISTER.csv` (20-field schema) |

### 5.2 Current Label Distribution in Framework

| Label | Count | Tier | Meaning |
|-------|-------|------|---------|
| `[SOURCE-BACKED]` | 20 | T2 | Supported by L2 evidence, not yet human-validated |
| `[ASSESSMENT]` | 9 | T3 | Analytical interpretation derived from facts |
| `[ASSUMPTION]` | 24 | T4 | Used for planning only, not fact |
| `[CONFIRMED]` | 1 | T1 | Appears once — in upgrade path description (§14), not as a claim label |
| `[VERIFIED]` | 0 | — | Legacy wrong label — **fully cleaned** |
| `SPECULATION:` | 0 | — | Legacy wrong label — **fully cleaned** |
| `[HIGH]` | 0 | — | Legacy wrong label — **fully cleaned** |
| `[MEDIUM]` | 0 | — | Legacy wrong label — **fully cleaned** |

### 5.3 Evidence Register Claim Distribution

| Tier | Count | Score Range | Validation Status | Rule 6 Capped? |
|------|-------|-------------|-------------------|----------------|
| **T2** | 11 | All 7/10 | Partially Verified | Yes — AI cannot exceed 7 |
| **T3** | 4 | 4–5/10 | Inferred | N/A — analytical |
| **T4** | 5 | 2–3/10 | Pending Validation | N/A — projection |
| **T1** | 0 | — | — | Blocked by Rule 6 (requires human review) |
| **T5** | 0 | — | — | No disputes detected |
| **T6** | 0 | — | — | No rejected claims |
| **Total** | 20 | — | — | — |

### 5.4 5-Criteria Score Breakdown (All T2 Claims)

| Criteria | Score | Max | Justification |
|----------|-------|-----|---------------|
| Authority | 2 | 2 | L2 sources (internal validated records) |
| Traceability | 2 | 2 | Specific file + line number citations |
| Recency | 1 | 2 | Source docs 7–23 days old (Jul 25 – Aug 3) |
| Consistency | 1 | 2 | Single workstream self-reporting — no external corroboration |
| Completeness | 1 | 2 | Complete in context, single-workstream scope |
| **Total** | **7** | **10** | **Rule 6 cap reached** |

### 5.5 T1 Upgrade Path

Per CVS §2 Tier Transition Rules: DAF reviews the framework, validates T2 claims against source files, confirms. T2 → T1 transition raises potential score to 8–10 with human authority (2) + recency confirmation (2).

---

## 6. Structural Analysis of the Framework

### 6.1 Lifecycle Model

The framework organises the PIR schema's 20 status values into 5 lifecycle phases:

- **Phase 1 (Collection):** 3 statuses — `open`, `in-progress`, `validated`
- **Phase 2 (Closure Candidate):** 2 statuses — `ready_for_review`, `ready_for_submission`
- **Phase 3 (Terminal):** 4 statuses — `fulfilled`, `cancelled`, `superseded`, `archived`
- **Phase 4 (Suspension):** 3 statuses — `deferred`, `blocked`, `overdue`
- **Phase 5 (Reopening):** 2 statuses — `identified`, `proposed`

**Coverage:** 14 of 20 schema statuses actively used (70%). 6 unused: `draft`, `active`, `approved`, `completed`, `pending`, `unresolved` — these exist in the schema enum but serve other record types or future use cases.

### 6.2 Closure Criteria Architecture

Six-point criteria (C1–C6) with priority-scaled evidence thresholds:

| Priority | Min. Source Level | Min. Score | Sources Required |
|----------|-------------------|------------|-----------------|
| Critical | L1 | ≥8 | 2 |
| High | L1/L2 | ≥5 | 2 |
| Medium | L2/L3 | ≥5 | 1 |
| Low | L3+ | ≥3 | 1 |

This aligns with CVS Master Framework §3 (Source Reliability Hierarchy) and §5 (Confidence Score model).

### 6.3 Authority Model

| Role | Can Recommend | Can Endorse | Can Sign Off |
|------|---------------|-------------|--------------|
| Collection Agent (CJ-1–6) | `validated` | — | — |
| PIR Tracker (CJ-7) | `ready_for_review` | — | — |
| Ember (Reviewer) | — | `ready_for_submission` | Low/Medium auto-fulfil (T2 cap) |
| DAF (Authority) | — | — | All priorities (T1 upgrade) |

**Rule 6 implication:** Ember auto-fulfilment produces T2 claims (max score 7). DAF review upgrades to T1. The weekly audit in §9 provides the human review path for T2→T1 upgrades.

### 6.4 SLA Framework

Two SLA clocks:

- **TTFI (Time-to-First-Intelligence):** 3/7/14/30 days by priority
- **TTC (Time-to-Closure):** 14/30/60/90 days target; 30/60/90/180 days hard limit

All SLA targets are `[ASSUMPTION]` (T4) — designed targets without empirical baseline data. Calibration requires one month of operational data.

---

## 7. Gap & Risk Analysis

### 7.1 Structural Gaps in the Framework

| # | Gap | Severity | Status |
|---|-----|----------|--------|
| G1 | CJ-7 enforcement logic (auto-escalation to `overdue`) not implemented | Medium | `[ASSUMPTION]` — documented, not yet built |
| G2 | SLA targets are designed, not empirically calibrated | Low | `[ASSUMPTION]` — calibration planned after month 1 |
| G3 | KPI targets (70% closure rate) have no baseline | Low | `[ASSUMPTION]` — data collection planned |
| G4 | Evidence Register currently has 1 master + 20 CogOS claims — other workstreams not yet populated | Low | Out of scope for this framework |
| G5 | 6 schema statuses unused in framework (`draft`, `active`, `approved`, `completed`, `pending`, `unresolved`) | Informational | Documented — may serve other record types |

### 7.2 Process Risks

| # | Risk | Probability | Impact | Mitigation |
|---|------|------------|--------|------------|
| R1 | Git commit blocked — `.gitignore` line 85 excludes `strategic-cognitiveos/` | Confirmed | Framework file not version-controlled | Resolve `.gitignore` or use `git add -f` with explicit path |
| R2 | CVS misapplication could recur if instrument selection is ambiguous | Low | Wrong validation labels | `CVS-ADAPTER-GUIDE.md` documents workstream→instrument mapping |
| R3 | Auto-fulfilment of Low/Medium PIRs without human review accumulates T2 claims | Medium | Claims stay at T2 indefinitely | Weekly audit (§9) provides review path; T2>5 days flagged per CVS §12 |
| R4 | SLA enforcement requires CJ-7 timer logic not yet built | Confirmed | Overdue auto-escalation is `[ASSUMPTION]` | Manual flagging in weekly report until CJ-7 logic implemented |
| R5 | 90 PIRs require sync — bulk sync pass could introduce errors | Medium | Record-layer corruption | Sync procedure (§8) has 8 steps; pilot with Critical PIRs first |

### 7.3 Workflow Process Observations

| # | Observation | Category |
|---|-------------|----------|
| O1 | CVS instrument was misapplied on first pass — wrong CVS selected | Process |
| O2 | Error was caught by DAF, not by internal validation (validate.sh passed either way) | Validation gap |
| O3 | Correction required 7 split-session fragments before action was taken | Execution efficiency |
| O4 | Framework structure was sound on first draft — correction was limited to CVS layer | Design quality |
| O5 | Evidence Register was empty before this workflow — first real population | System maturity |

---

## 8. Validation Results

### 8.1 `validate.sh` Run (Final)

| Check | Result |
|-------|--------|
| Analytical claims properly tagged | ✅ Pass |
| Predictive claims properly demarcated | ✅ Pass |
| Cross-reference check | ⚠ No constituency (expected — governance doc, not election brief) |
| ElectionData.MY verification | ⚠ No constituency (expected — not applicable) |
| **Summary** | **0 errors, 1 warning — PASSED** |

### 8.2 CVS Master Framework Compliance Self-Check

| CVS Requirement | Status |
|-----------------|--------|
| All claims tiered (T1–T6) | ✅ 20 claims tiered |
| All claims labelled | ✅ `[SOURCE-BACKED]` / `[ASSESSMENT]` / `[ASSUMPTION]` |
| Source levels cited (L1–L5) | ✅ L1 (CVS-FRAMEWORK) and L2 (internal records) cited |
| 5-criteria confidence scores | ✅ All 20 claims scored |
| Rule 6 applied (AI cap T2 / score 7) | ✅ No T1 claims; all T2 capped at 7 |
| Evidence Register populated | ✅ 20 rows in `CVS-EVIDENCE-REGISTER.csv` |
| Claim ID format correct | ✅ `CVS-COG-001` through `CVS-COG-020` |
| Adapter rules followed | ✅ CogOS: PIR-sourced claims → L2, AI outputs → T3/T2 per adapter guide |

---

## 9. Outstanding Items

| # | Item | Status | Owner | Target |
|---|------|--------|-------|--------|
| 1 | `.gitignore` blocks `strategic-cognitiveos/` (line 85) — framework file not committable | Blocked | Ember/DAF | Before ratification |
| 2 | DAF ratification of framework | Pending | DAF | Aug 18, 2026 `[ASSUMPTION]` |
| 3 | T2 → T1 upgrade for claims DAF can validate | Pending | DAF | Post-ratification |
| 4 | Schema alignment verification (all 14 used statuses in schema) | `[SOURCE-BACKED]` — verified programmatically 2026-08-17 | Ember | Done |
| 5 | CJ-7 weekly report template update | Pending | Ember | Aug 19, 2026 `[ASSUMPTION]` |
| 6 | First full sync pass (120 PIRs) | Pending | Ember | Aug 20–24, 2026 `[ASSUMPTION]` |
| 7 | §5 escalation protocol applied to 12 OSINT-unresolvable PIRs | Pending | Ember → DAF | Aug 25, 2026 `[ASSUMPTION]` |
| 8 | First monthly closure metrics report | Pending | CJ-7 | Sep 1, 2026 `[ASSUMPTION]` |
| 9 | Evidence Register: other workstreams not yet populated | Out of scope | — | Future |

---

## 10. Quantitative Summary

| Metric | Value |
|--------|-------|
| Total elapsed time (request → report) | ~16 minutes |
| Source files read | 9 (6 primary + 3 CVS reference) |
| Framework versions produced | 2 (wrong CVS → correct CVS) |
| Framework size (final) | 35,042 bytes / 531 lines / 4,595 words |
| Framework sections | 15 |
| CVS claims registered | 20 (CVS-COG-001 to -020) |
| Evidence Register rows (total) | 22 (1 header + 21 data) |
| Line citations in framework | 14 unique `#L` refs across 4 files |
| Legacy wrong labels remaining | 0 (all cleaned) |
| `validate.sh` errors | 0 |
| `validate.sh` warnings | 1 (expected false positive) |
| Git blockers | 1 (`.gitignore` line 85) |
| Split-session fragments during correction | 7 |

---

## 11. Assessment

**Framework quality:** The framework is structurally sound. The 5-phase lifecycle model maps cleanly to the existing schema's 20 statuses. The 6-point closure criteria with priority-scaled evidence thresholds align with the CVS Master Framework's source hierarchy and scoring model. The SLA framework, while uncalibrated, provides a reasonable starting architecture.

**CVS compliance:** Fully compliant under the correct instrument (CVS Master Framework). All 20 claims are tiered, labelled, scored, and registered. Rule 6 is properly applied — zero T1 claims, all T2 capped at score 7. The T1 upgrade path is documented and requires DAF action.

**Process quality:** The initial CVS misapplication is a process failure — the wrong instrument was selected because the DUN-profiling CVS (`tools/truth-validator/`) was the first one encountered, and the distinction between it and the Master Framework was not checked. The `CVS-ADAPTER-GUIDE.md` documents this mapping but was not consulted before the first application. The error was caught by DAF, not by internal validation (`validate.sh` passed both times — it validates the DUN-profiling format, not the Master Framework). This suggests `validate.sh` needs an upgrade to validate against the Master Framework, or a separate validation script is needed for governance documents.

**Key recommendation:** Resolve the `.gitignore` blocker and commit before ratification. The framework cannot be version-controlled or audited through git history while `strategic-cognitiveos/` is excluded.

---

*This report is AI-generated. All claims subject to CVS Rule 6 (T2 max, score 7). Human review required for T1 upgrade.*

*Report file: `reports/RPT-WF-PIR-CLOSURE-001-20260817.md`*
