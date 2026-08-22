# AIP Gate Tracker

**Purpose:** Live status of all AIP productization phases. Updated at each checkpoint. Fed into weekly Cognitive Loop review.

**Rule:** A gate is not "passed" until it has evidence. A gate is not "failed" until DAF acknowledges the failure. Unknown is a valid status — it means we don't have information.

---

## Track A — VoronCitadel: GTM Activation (IMMEDIATE)

| Phase | Gate | Owner | Deadline | Status | Evidence | Notes |
|-------|------|-------|----------|--------|----------|-------|
| A1 | POC Document Finalisation (Bursa Malaysia) | Athena→Fuad(QC)→DAF(approval) | Aug 24, 02:00 UTC | 🔴 UNKNOWN | None | Fuad reviewing. DAF elevated to pre-flight check. Deadline in ~60h. |
| A2 | CSM Channel Activation | DAF→Amelia→Aisha | Aug 28 | ⏳ NOT STARTED | None | Depends on A1. Aisha PIC confirmation by Aug 22. |
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
| C1 | Credential Closure & Secret Governance | Fuad+DAF | Aug 30 | 🔴 UNKNOWN | None | 4 exposed keys, confirmed unrotated Aug 19. Security non-negotiable. |
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
| TBH-001 Hiring Approach | DAF | Aug 27 | 🔴 UNKNOWN | None | Blocks A2 execution, B4 rehearsals, C5 scope. Escalation Sep 3. |
| External Security Assessor | DAF | Sep 1 | ⏳ NOT STARTED | None | For GovSec TIP pen test (B1 gate). |
| Second Engineer Assessment | DAF | Sep 15 | ⏳ NOT STARTED | None | Fuad bandwidth across 3 products. |

---

## Deadline Alert Register

**Checked daily. Flags within 72h of deadline.**

| Date | Phase | Deadline | Hours Remaining | Alert Status |
|------|-------|----------|-----------------|--------------|
| Aug 22 | A1 (POC Doc) | Aug 24 02:00 UTC | ~34h | 🟡 APPROACHING — confirm Fuad QC status urgently |
| Aug 22 | CSM Aisha PIC (Decision) | Aug 22 | TODAY | 🔴 DUE NOW — confirm Aisha or escalate to Zulfeka |
| Aug 22 | TBH-001 approach | Aug 27 | ~5 days | 🟢 OK for now |
| Aug 22 | TBH-001 escalation | Sep 3 | ~12 days | 🟢 OK for now — 2-day mark, not yet 2-week trigger |
| Aug 22 | C1 (Credentials) | Aug 30 | ~8 days | 🟢 OK for now |

---

## Gate Status Summary

| Track | Total Phases | Not Started | Unknown | In Progress | Blocked | Passed | Failed |
|------|-------------|-------------|---------|-------------|---------|--------|--------|
| A | 4 | 3 | 1 | 0 | 0 | 0 | 0 |
| B | 5 | 5 | 0 | 0 | 0 | 0 | 0 |
| C | 5 | 4 | 1 | 0 | 0 | 0 | 0 |
| Ops | 3 | 2 | 1 | 0 | 0 | 0 | 0 |
| **Total** | **17** | **14** | **3** | **0** | **0** | **0** | **0** |

**0/17 gates passed with evidence. 3/17 unknown. This is the honest starting position.**

---

## Decision Points (From AIP §6)

| Date | Decision | Status |
|------|----------|--------|
| Aug 22 | CSM Aisha PIC confirmed? | 🔴 PENDING |
| Aug 24 | VoronCitadel POC doc approved? | 🔴 PENDING (A1) |
| Aug 27 | TBH-001 hiring approach decided? | 🔴 PENDING |
| Aug 30 | chain:SENTRY credential rotation verified? | 🔴 PENDING (C1) |
| Sep 1 | External security assessor engaged? | 🔴 PENDING |
| Sep 3 | TBH-001 escalation trigger? | 🔴 PENDING |
| Sep 15 | Second engineer assessment? | 🔴 PENDING |
| Sep 30 | chain:SENTRY pilot scope approved? | 🔴 PENDING |
| Oct 8 | CyberDSA demo content frozen? | 🔴 PENDING |

---

*This tracker is the operational layer of the AIP. It converts a document into a living instrument. Updated at each checkpoint and fed into the weekly Cognitive Loop review.*
