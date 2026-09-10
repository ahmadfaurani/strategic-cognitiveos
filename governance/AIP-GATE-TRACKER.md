# AIP Gate Tracker

**Purpose:** Live status of all AIP productization phases. Updated at each checkpoint. Fed into weekly Cognitive Loop review.

**Rule:** A gate is not "passed" until it has evidence. A gate is not "failed" until DAF acknowledges the failure. Unknown is a valid status — it means we don't have information.

---

## Track A — VoronCitadel: GTM Activation (IMMEDIATE)

| Phase | Gate | Owner | Deadline | Status | Evidence | Notes |
|-------|------|-------|----------|--------|----------|-------|
| A1 | POC Document Finalisation (Bursa Malaysia) | Athena→Fuad(QC)→DAF(approval) | Aug 24, 02:00 UTC | ✅ PASSED | DAF approval via Telegram Aug 24 23:02 UTC. POC technical summary delivered as email (CONV-20260824-001, Aug 24 5:44 PM MYT). COM-20260820-003 fulfilled. 8-section structure: phased approach (TPRM-first), 3-4 org scope, 24-entity as hypothesis, Act 854 context, assignments to Fuad and Farul. | DAF approved. Deadline exceeded by ~21h but delivered same-day. Track A critical path unblocked. |
| A2 | CSM Channel Activation | DAF→Amelia→Aisha | Aug 28 | ✅ RESOLVED | Aishah assigned as CSM MQL Receiver (DEC-20260829-001, ACT-20260829-001). Role defined Aug 28 with 13-section role definition. | Resolved Aug 28. Aishah = CSM MQL Receiver. Gate closed. |
| A3 | Commercial Packaging | DAF+Fuad | Sep 5 | 🔴 OVERDUE — 2 DAYS PAST DEADLINE | None | Depends on A1 (PASSED — dependency cleared). Pricing, POC template, SLA terms. NOT STARTED. CSM channel cannot quote without this. |
| A4 | White-Label Readiness | Fuad+DAF | Sep 15 | ⏳ NOT STARTED | None | Depends on A2. UI/UX for CSM co-brand. |

**Track A critical path:** A1 → A2 → A4, A1 → A3

**Track A risk:** If A1 slips past Aug 24, A2 has no document to activate CSM with. No float in schedule.

---

## Track B — GovSec TIP: CyberDSA Demo Readiness (T-12 WEEKS)

| Phase | Gate | Owner | Deadline | Status | Evidence | Notes |
|-------|------|-------|----------|--------|----------|-------|
| B1 | Security Remediation | Fuad+DAF | Sep 15 | ⏳ NOT STARTED | None | OWASP Top 10 + LLM Top 10 + 54 npm audit. Must close before build. |
| B2 | Core Build — 4 Domain Modules | Fuad+TBH-001 | Sep 30 | ⏳ NOT STARTED | None | 12 entities, 12 pipelines, 147 endpoints at 60%. Depends on B1. |
| B3 | AI Analyst Workbench | Fuad+DAF | Oct 5 | ⏳ NOT STARTED | None | RAG-powered. Demo differentiator. Depends on B2. |
| B4 | Demo Environment & Scenarios | TBH-001/DAF+Fuad | Oct 10 | ⏳ NOT STARTED | None | 3 scripted scenarios. 3 consecutive rehearsals. Depends on B2+B3. |
| B5 | CyberDSA Brand Narrative | DAF+Amelia | Oct 8 | ⏳ NOT STARTED | None | Press release, one-pager, social. Depends on B4. |

**Track B critical path:** B1 → B2 → B3 → B4 → B5

**Track B risk:** 12 weeks for 4-domain build is tight. If B1 slips, compress B2 to 2 domains (Ingestion + Analysis).

---

## Track C — chain:SENTRY: Pilot Readiness (POST-VORONCITADEL)

| Phase | Gate | Owner | Deadline | Status | Evidence | Notes |
|-------|------|-------|----------|--------|----------|-------|
| C1 | Credential Closure & Secret Governance | Hadri→Syahir (DEC-20260904-001) | Aug 30 | ✅ RESOLVED — OPERATOR-CONFIRMED | DAF Telegram confirmation "C1 YES" 2026-09-08 01:29 UTC | 4 exposed keys revoked and reissued September 2026 on operator confirmation (DAF confirmed 2026-09-08 01:29 UTC). Consistent across all three Sep 7 suite documents (MVP Spec v4.2, Op Plan v1.1 §BLK-001, Roadmap v2.1 gap 1/M1). Residual evidence item: changed masked fingerprints to be recorded in the C2 release pack (Roadmap M1) and provider rejection of old values verified. C2 UNBLOCKED. |
| C2 | Deployment Parity | Fuad | **Sep 30** (re-baselined from Sep 10, DEC-20260908-002) | 🟢 RE-BASELINED — 22-day window on adopted Op Plan trajectory | None | 22-commit/32-day gap. Phase 0 M2→M7 executes against adopted Op Plan v1.1 trajectory (DEC-20260908-001): M2 regression decision (restore address-security integration vs record reduced screening), M3 manifest file-by-file, M4 backup + verified restore, M5 two migrations via runner, M6 controlled deploy, M7 verification sweep. Aligns with JD pack (Sep 16) + ACT-20260825-002 FTE-evidence window (closes Sep 30). CyberDSA consequence: chain:SENTRY presents as deployed capability (Phase 0 exit ≈77% readiness), not pilot. Sep 15 kill date superseded (DEC-20260908-002). M2 regression decision remains Fuad's first blocker. |
| C3 | External Access & Named Identity | Fuad+DAF | ~~Sep 15~~ cascade re-sequencing pending (DEC-20260908-002) | ⏳ NOT STARTED — awaiting C2 (Sep 30) + cascade confirmation | None | TLS, per-person pilot accounts. Depends on C2 (now Sep 30). Proposed: Oct 14 (Phase 1 weeks 1–2 post-Phase-0 exit) — DAF to confirm. |
| C4 | Live-vs-Demo Boundary | Fuad | ~~Sep 20~~ cascade re-sequencing pending (DEC-20260908-002) | ⏳ NOT STARTED — awaiting C3 | None | No fixture data in pilot surfaces. Depends on C2+C3. Proposed: Oct 21 — DAF to confirm. |
| C5 | Pilot Scope Definition | DAF+TBH-001 | ~~Sep 30~~ cascade re-sequencing pending (DEC-20260908-002) | ⏳ NOT STARTED — awaiting C2-C4 | None | Target org, 6-week duration, success scorecard. Depends on C1-C4. Proposed: Oct 31 (post pilot-gate assessment, Phase 1 exit) — DAF to confirm. |

**Track C critical path:** C1 → C2 → C3 → C4 → C5

**Track C risk:** M2 regression decision is the first blocker on the re-baselined Phase 0 path (restoring the address-security integration keeps the 4-layer screening claim; recording reduced screening weakens the pilot claim). Sep 15 kill date superseded by DEC-20260908-001/002 (Op Plan adopted + C2 re-baseline).

---

## Operationalization Layer

| Item | Owner | Deadline | Status | Evidence | Notes |
|------|-------|----------|--------|----------|-------|
| TBH-001 Hiring Approach | DAF | Aug 27 | ✅ DECIDED | JD v2 committed (commit `5b6aed7`, Aug 28). 13 sections, ITSS §10 scope, CyberDSA gate chain, NDA tracking, interim delegation plan. End-September hiring activation → Oct 13-20 start date. Reports to Hadri (COO), matrix to DAF. | Decision made Aug 28. Escalation clock stopped. Interim: POC tracking→DAF, tech review→Hadri, POC env→Fuad/Syahir, stakeholder→Amelia, NDA/legal→DAF, risk register→Ember. |
| chain:SENTRY Capacity Model | DAF | Sep 16 (JD pack) | ✅ DECIDED → EXECUTION | DEC-20260908-001 (DAF Telegram 2026-09-08 03:18 UTC). Op Plan v1.1 7-FTE model ADOPTED as governing operating model; hiring JD review opened per FTE; Hadri delivers Overall JD pack by Sep 16 (ACT-20260908-002). No-hire-before-Jan-2027 amended for chain:SENTRY product-operations roles; TBH-001/002 unchanged. CC-01 envelope MYR 100–150K/mo. Interim capacity (Fuad+Syahir) still carries C2/Sep 14/Sep 15 gates. |
| External Security Assessor | DAF | Sep 1 | ✅ RESOLVED — NANOSEC ALIGNED | DEC-20260904-002 | External assessor replaced by NanoSec Community Team (DEC-20260904-002, Sep 4). Prerequisite: Hadri delivers NanoSec Collaboration Email (ACT-20260904-002). B1 gate (Sep 15) pen test via NanoSec — 2-week window feasible if email delivered this week. |
| Second Engineer Assessment | DAF | Sep 15 | ⏳ NOT STARTED | None | Fuad bandwidth across 3 products. HoE hiring approval gates October 2026 — no engineering relief before Jan 2027. |

---

## Deadline Alert Register

**Checked daily. Flags within 72h of deadline.**
**Last checked:** 2026-09-10 15:48 UTC (automated daily gate check)

| Date | Phase | Deadline | Hours Remaining | Alert Status |
|------|-------|----------|-----------------|--------------|
| Sep 10 | A3 (Commercial Packaging) | Sep 5 | **OVERDUE (~5.7 days)** | 🔴 OVERDUE (CRITICAL) — NOT STARTED. DAF+Fuad. Pricing, POC template, SLA terms. A1 PASSED so dependency cleared; Cost Centre Plan v1.0 supplies the cost baseline half. **ACTION: DAF+Fuad to deliver commercial packaging NOW — CSM channel cannot quote without it. Overdue window widening daily (day 6 past deadline).** |
| Sep 10 | B1 (Security Remediation) | Sep 15 | ~4.3 days (~104h) | 🟢 OK — outside 72h window, but pen-test math still broken: with ~4.3 days to the gate, the ~2-week NanoSec pen test window cannot fit before Sep 15. Hadri's NanoSec Collaboration Email (ACT-20260904-002) is the deciding factor — deliver immediately or DAF re-dates B1. Enters 72h alert window Sep 12. |
| Sep 10 | A4 (White-Label Readiness) | Sep 15 | ~4.3 days (~104h) | 🟢 OK — outside 72h window (enters window Sep 12). Fuad+DAF. Depends on A2 (RESOLVED). UI/UX for CSM co-brand. |
| Sep 10 | Second Engineer Assessment | Sep 15 | ~4.3 days (~104h) | 🟢 OK — outside 72h window. DAF. HoE hiring approval gates October. No engineering relief before Jan 2027. |
| Sep 10 | JD pack (chain:SENTRY capacity) | Sep 16 | ~5.3 days (~128h) | 🟢 OK — outside 72h window. Hadri delivers Overall JD pack (ACT-20260908-002) per adopted 7-FTE model (DEC-20260908-001). |
| Sep 10 | C1 (Credentials) | Aug 30 | RESOLVED | ✅ RESOLVED — operator-confirmed Sep 8 01:29 UTC (DAF Telegram "C1 YES"). 4 exposed keys revoked and reissued. C2 unblocked. Row retained for audit trail. |
| Sep 10 | C2 (Deployment Parity) | Sep 30 (re-baselined, DEC-20260908-002) | ~19.3 days (~464h) | 🟢 OK — re-baselined Sep 8 on adopted Op Plan trajectory; daily urgency signal retired. First execution checkpoint: M2 regression decision (Fuad). |
| Sep 10 | TBH-001 escalation | Sep 3 | N/A | ✅ MOOT — Hiring approach decided Aug 28. Escalation clock stopped. Interim delegation plan active. No longer applicable. |
| Sep 10 | External security assessor | Sep 1 | **RESOLVED** | ✅ RESOLVED Sep 4 — NanoSec Community Team replaces external assessor (DEC-20260904-002). Prerequisite: Hadri delivers NanoSec Collaboration Email (ACT-20260904-002). |

---

## Gate Status Summary

| Track | Total Phases | Not Started | Unknown | In Progress | Blocked | Passed/Resolved | Failed |
|------|-------------|-------------|---------|-------------|---------|-----------------|--------|
| A | 4 | 1 | 0 | 0 | 0 | 2 | 0 |
| B | 5 | 5 | 0 | 0 | 0 | 0 | 0 |
| C | 5 | 3 | 0 | 0 | 1 | 0 | 0 |
| Ops | 3 | 1 | 0 | 0 | 0 | 2 | 0 |
| **Total** | **17** | **10** | **0** | **0** | **1** | **4** | **0** |

**5/17 gates resolved with evidence (A1, A2, TBH-001, External Assessor→NanoSec, C1 operator-confirmed Sep 8). 1/17 overdue (A3 — ~5.7 days overdue as of Sep 10 check, NOT STARTED; Cost Centre Plan v1.0 supplies the cost baseline half). 0/17 approaching: nearest open gates are Sep 15 (B1, A4, Second Engineer Assessment) at ~4.3 days and Sep 16 (JD pack) at ~5.3 days — all outside the 72h alert window; the Sep 15 cohort enters the window on Sep 12. C2 re-baselined to Sep 30 (DEC-20260908-002) on the adopted Op Plan trajectory — daily urgency signal retired; first execution checkpoint is the M2 regression decision. B1 gate (Sep 15): with ~4.3 days remaining, the ~2-week NanoSec pen test window cannot fit before the gate — Hadri's NanoSec Collaboration Email (ACT-20260904-002) now decides whether B1 holds Sep 15 or is re-dated. A3 is the remaining active crisis — blocks commercial quoting; day 6 past deadline. C2 timeline risk: roadmap Phase 0 sequencing is strictly sequential (M2→M6); 2 days for 6 deliverables with 2 FTE is the portfolio's tightest float.**

---

## Decision Points (From AIP §6)

| Date | Decision | Status |
|------|----------|--------|
| Aug 22 | CSM Aisha PIC confirmed? | ✅ RESOLVED — Aishah assigned as CSM MQL Receiver Aug 28 (DEC-20260829-001). |
| Aug 24 | VoronCitadel POC doc approved? | ✅ APPROVED — DAF via Telegram Aug 24 23:02 UTC. Evidence: CONV-20260824-001. |
| Aug 27 | TBH-001 hiring approach decided? | ✅ DECIDED — JD v2 committed Aug 28. End-Sep hiring activation, Oct 13-20 start. Escalation clock stopped. |
| Aug 30 | chain:SENTRY credential rotation verified? | ✅ RESOLVED — operator-confirmed Sep 8 01:29 UTC (DAF Telegram "C1 YES"). 4 exposed keys revoked and reissued. C2 unblocked. |
| Sep 1 | External security assessor engaged? | ✅ RESOLVED Sep 4 — NanoSec Community Team replaces external assessor (DEC-20260904-002). Prerequisite: Hadri delivers NanoSec Collaboration Email (ACT-20260904-002). |
| Sep 3 | TBH-001 escalation trigger? | ✅ MOOT — Hiring approach decided. Escalation clock stopped. |
| Sep 15 | Second engineer assessment? | 🔴 PENDING — HoE hiring approval gates October. No engineering relief before Jan 2027. |
| Sep 30 | chain:SENTRY pilot scope approved? | 🔴 PENDING |
| Oct 8 | CyberDSA demo content frozen? | 🔴 PENDING |

---

*This tracker is the operational layer of the AIP. It converts a document into a living instrument. Updated at each checkpoint and fed into the weekly Cognitive Loop review.*
