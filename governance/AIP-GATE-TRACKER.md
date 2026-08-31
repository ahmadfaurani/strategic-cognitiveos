# AIP Gate Tracker

**Purpose:** Live status of all AIP productization phases. Updated at each checkpoint. Fed into weekly Cognitive Loop review.

**Rule:** A gate is not "passed" until it has evidence. A gate is not "failed" until DAF acknowledges the failure. Unknown is a valid status — it means we don't have information.

---

## Track A — VoronCitadel: GTM Activation (IMMEDIATE)

| Phase | Gate | Owner | Deadline | Status | Evidence | Notes |
|-------|------|-------|----------|--------|----------|-------|
| A1 | POC Document Finalisation (Bursa Malaysia) | Athena→Fuad(QC)→DAF(approval) | Aug 24, 02:00 UTC | ✅ PASSED | DAF approval via Telegram Aug 24 23:02 UTC. POC technical summary delivered as email (CONV-20260824-001, Aug 24 5:44 PM MYT). COM-20260820-003 fulfilled. 8-section structure: phased approach (TPRM-first), 3-4 org scope, 24-entity as hypothesis, Act 854 context, assignments to Fuad and Farul. | DAF approved. Deadline exceeded by ~21h but delivered same-day. Track A critical path unblocked. |
| A2 | CSM Channel Activation | DAF→Amelia→Aisha | Aug 28 | ✅ RESOLVED | Aishah assigned as CSM MQL Receiver (DEC-20260829-001, ACT-20260829-001). Role defined Aug 28 with 13-section role definition. | Resolved Aug 28. Aishah = CSM MQL Receiver. Gate closed. |
| A3 | Commercial Packaging | DAF+Fuad | Sep 5 | ⏳ NOT STARTED | None | Depends on A1. Pricing, POC template, SLA terms. |
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
| C1 | Credential Closure & Secret Governance | Fuad+DAF | Aug 30 | 🔴 OVERDUE — AWAITING DAF INPUT | None | 4 exposed keys, confirmed unrotated Aug 19. 12 days of exposure. Deadline passed Aug 30. C2 blocked. Security non-negotiable. DAF has not yet confirmed rotation status. |
| C2 | Deployment Parity | Fuad | Sep 10 | ⏳ NOT STARTED | None | 22-commit/32-day gap. Release manifest. Depends on C1. |
| C3 | External Access & Named Identity | Fuad+DAF | Sep 15 | ⏳ NOT STARTED | None | TLS, per-person pilot accounts. Depends on C2. |
| C4 | Live-vs-Demo Boundary | Fuad | Sep 20 | ⏳ NOT STARTED | None | No fixture data in pilot surfaces. Depends on C2+C3. |
| C5 | Pilot Scope Definition | DAF+TBH-001 | Sep 30 | ⏳ NOT STARTED | None | Target org, 6-week duration, success scorecard. Depends on C1-C4. |

**Track C critical path:** C1 → C2 → C3 → C4 → C5

**Track C risk:** C1 is a security liability regardless of commercial priority. Exposed keys worsen with time.

---

## Operationalization Layer

| Item | Owner | Deadline | Status | Evidence | Notes |
|------|-------|----------|--------|----------|-------|
| TBH-001 Hiring Approach | DAF | Aug 27 | ✅ DECIDED | JD v2 committed (commit `5b6aed7`, Aug 28). 13 sections, ITSS §10 scope, CyberDSA gate chain, NDA tracking, interim delegation plan. End-September hiring activation → Oct 13-20 start date. Reports to Hadri (COO), matrix to DAF. | Decision made Aug 28. Escalation clock stopped. Interim: POC tracking→DAF, tech review→Hadri, POC env→Fuad/Syahir, stakeholder→Amelia, NDA/legal→DAF, risk register→Ember. |
| External Security Assessor | DAF | Sep 1 | ⏳ NOT STARTED — AWAITING DAF INPUT | None | For GovSec TIP pen test (B1 gate). DAF has not yet confirmed engagement or deferral. |
| Second Engineer Assessment | DAF | Sep 15 | ⏳ NOT STARTED | None | Fuad bandwidth across 3 products. HoE hiring approval gates October 2026 — no engineering relief before Jan 2027. |

---

## Deadline Alert Register

**Checked daily. Flags within 72h of deadline.**
**Last checked:** 2026-08-31 15:48 UTC (automated daily gate check)

| Date | Phase | Deadline | Hours Remaining | Alert Status |
|------|-------|----------|-----------------|--------------|
| Aug 31 | A1 (POC Doc) | Aug 24 02:00 UTC | **PASSED (~21h late)** | ✅ PASSED — DAF approved via Telegram Aug 24 23:02 UTC. Evidence: CONV-20260824-001. COM-20260820-003 fulfilled. Track A critical path unblocked. |
| Aug 31 | A2 (CSM Channel Activation) | Aug 28 | **RESOLVED** | ✅ RESOLVED — A2 closed Aug 28. Aishah assigned as CSM MQL Receiver. Gate no longer overdue. |
| Aug 31 | TBH-001 approach | Aug 27 | **DECIDED** | ✅ DECIDED — JD v2 committed Aug 28 (commit `5b6aed7`). End-September hiring activation, Oct 13-20 start window. Reports to Hadri (COO), matrix to DAF. Escalation clock stopped. |
| Aug 31 | C1 (Credentials) | Aug 30 | **OVERDUE (~40h)** | 🔴 OVERDUE (CRITICAL) — Deadline passed Aug 30. Status UNKNOWN — AWAITING DAF INPUT. 4 exposed keys unrotated since Aug 19 (12 days). Active security liability worsening. Non-negotiable per AIP §3 Track C. C2 (Deployment Parity, Sep 10) is blocked — cannot deploy exposed credentials to fresh environment. **URGENT: DAF to confirm rotation status or direct Fuad to execute IMMEDIATELY. 12 days of exposure.** |
| Aug 31 | External security assessor | Sep 1 | **~8h** | 🟡 APPROACHING (CRITICAL) — within 72h window, <8h remaining. NOT STARTED — AWAITING DAF INPUT. Required for GovSec TIP pen test (B1 gate, Sep 15). **ACTION NEEDED: DAF to engage assessor by Sep 1 or B1 gate at risk.** |
| Aug 31 | TBH-001 escalation | Sep 3 | **N/A** | ✅ MOOT — Hiring approach decided Aug 28. Escalation clock stopped. No longer applicable. |
| Aug 31 | A3 (Commercial Packaging) | Sep 5 | ~4.3 days | 🟢 OK — outside 72h window. Depends on A1 (PASSED). DAF+Fuad. Next up after urgent items. |
| Aug 31 | C2 (Deployment Parity) | Sep 10 | ~10 days | 🟢 OK — outside 72h window. **BLOCKED** by C1 (OVERDUE). Cannot proceed until credentials rotated. |
| Aug 31 | B1 (Security Remediation) | Sep 15 | ~15 days | 🟢 OK — outside 72h window. Fuad+DAF. Depends on external assessor engagement (APPROACHING). |

---

## Gate Status Summary

| Track | Total Phases | Not Started | Unknown | In Progress | Blocked | Passed/Resolved | Failed |
|------|-------------|-------------|---------|-------------|---------|-----------------|--------|
| A | 4 | 2 | 0 | 0 | 0 | 2 | 0 |
| B | 5 | 5 | 0 | 0 | 0 | 0 | 0 |
| C | 5 | 4 | 0 | 0 | 0 | 0 | 0 |
| Ops | 3 | 2 | 0 | 0 | 0 | 0 | 0 |
| **Total** | **17** | **13** | **0** | **0** | **0** | **2** | **0** |

**2/17 gates resolved with evidence. 1/17 overdue (C1). External Security Assessor approaching deadline. Both require DAF action.**

---

## Decision Points (From AIP §6)

| Date | Decision | Status |
|------|----------|--------|
| Aug 22 | CSM Aisha PIC confirmed? | ✅ RESOLVED — Aishah assigned as CSM MQL Receiver Aug 28 (DEC-20260829-001). |
| Aug 24 | VoronCitadel POC doc approved? | ✅ APPROVED — DAF via Telegram Aug 24 23:02 UTC. Evidence: CONV-20260824-001. |
| Aug 27 | TBH-001 hiring approach decided? | ✅ DECIDED — JD v2 committed Aug 28. End-Sep hiring activation, Oct 13-20 start. Escalation clock stopped. |
| Aug 30 | chain:SENTRY credential rotation verified? | 🔴 OVERDUE (CRITICAL) — Deadline passed Aug 30. C1 gate. Awaiting DAF input. 12 days since exposure. 4 exposed keys still unrotated. C2 blocked. |
| Sep 1 | External security assessor engaged? | 🟡 APPROACHING (CRITICAL) — <8h remaining. Required for B1 gate. Awaiting DAF input. |
| Sep 3 | TBH-001 escalation trigger? | ✅ MOOT — Hiring approach decided. Escalation clock stopped. |
| Sep 15 | Second engineer assessment? | 🔴 PENDING — HoE hiring approval gates October. No engineering relief before Jan 2027. |
| Sep 30 | chain:SENTRY pilot scope approved? | 🔴 PENDING |
| Oct 8 | CyberDSA demo content frozen? | 🔴 PENDING |

---

*This tracker is the operational layer of the AIP. It converts a document into a living instrument. Updated at each checkpoint and fed into the weekly Cognitive Loop review.*
