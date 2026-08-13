# GovSec TIP CyberDSA Readiness Plan

**Document ID:** GRP-20260813-001
**Initiative:** INIT-20260810-003
**Decision Authority:** DEC-20260810-002 (Development Freeze)
**Programme Coordinator:** DAF
**Lead Architect:** Hadri
**Current Technical Owner:** Ahmad Fuad
**Incoming Product Manager:** Hadi (start date TBC)
**Created:** 13 August 2026
**Target Readiness:** Demo-ready by 1 October 2026
**Launch Event:** CyberDSA 2026, 5–7 October, MITEC KL

---

## Execution Timeline

```
AUGUST                    SEPTEMBER                  OCTOBER
W3   W4   W5              W1   W2   W3   W4          W1
│Doc │Hand│Hardening      │Hard│Valid│Demo│Dress     │Launch
│+   │over│begins        │ening│ation│prep│rehearsal │
│Triage│  │              │    │     │    │          │
└────┴────┴──────────────┴────┴─────┴────┴──────────┘
17   24   31              7    14    21   28          5
```

**Critical path:** Documentation → Handover → Hardening → Validation → Demo Prep → Dress Rehearsal → Launch

**Zero slack.** Any slippage in Aug 24 handover docs compresses Sep hardening from 4 weeks to 3.

---

## Priority 1 — Stabilise & Harden

**Objective:** Transform v3.0 from active-development state to stable, hardened platform suitable for live public demonstration.

**Owner:** Ahmad Fuad (execution) → Hadri (post-handover, Aug 24+)
**Start:** 17 August 2026
**Target completion:** 21 September 2026

### 1.1 Stabilisation

| Task | Description | Owner | Due | Acceptance Criteria |
|------|-------------|-------|-----|---------------------|
| S-01 | Define demo-critical paths | DAF + Hadri | Aug 19 | Document listing 5–8 critical user journeys that must work flawlessly |
| S-02 | Bug triage — classify all known issues | Fuad | Aug 21 | Issue list with severity: Critical / High / Medium / Low |
| S-03 | Fix all Critical bugs in demo paths | Fuad | Aug 31 | Zero Critical bugs in demo-critical paths |
| S-04 | Fix all High bugs in demo paths | Fuad | Sep 7 | Zero High bugs in demo-critical paths |
| S-05 | Performance baseline — measure key flows | Fuad | Aug 24 | Response times recorded: dashboard load, alert query, AI analyst, threat viz |
| S-06 | Performance targets set | Hadri | Aug 28 | Targets defined: <2s page load, <5s AI analyst, <3s viz render |
| S-07 | Performance optimisation (if needed) | Fuad | Sep 14 | All demo-critical paths meet performance targets |
| S-08 | Stability test — 48h continuous run | Fuad | Sep 14 | No crashes, no memory leaks, no data inconsistencies over 48h |

### 1.2 Security Hardening

| Task | Description | Owner | Due | Acceptance Criteria |
|------|-------------|-------|-----|---------------------|
| H-01 | Engage security assessment resource | DAF | Aug 19 | Confirm who conducts assessment (internal/external); schedule date |
| H-02 | Security assessment / pentest | TBD | Sep 7 | Assessment completed; report delivered |
| H-03 | Triage security findings | Hadri | Sep 10 | Findings classified: Critical / High / Medium / Low |
| H-04 | Fix all Critical security issues | Fuad | Sep 14 | Zero Critical security findings unresolved |
| H-05 | Fix all High security issues | Fuad | Sep 21 | Zero High security findings unresolved |
| H-06 | PDPA compliance verification | Fuad | Sep 14 | PII detection, redaction, audit log, retention — all verified working |
| H-07 | RBAC verification — all roles | Fuad | Aug 31 | Each role tested: admin, analyst, executive, viewer — access correct |
| H-08 | Code review — demo-critical components | Hadri | Sep 14 | Code review completed for: auth, API endpoints, data access, AI analyst |

**Gate: Stabilised & Hardened** (Sep 21)
- Zero Critical bugs in demo paths ✅
- Zero Critical security findings ✅
- Performance targets met ✅
- 48h stability test passed ✅
- PDPA + RBAC verified ✅

---

## Priority 2 — Close Critical Gaps

**Objective:** Triage and resolve known technical and security issues. No gap should be discovered during CyberDSA.

**Owner:** Ahmad Fuad (triage), Hadri (validation)
**Start:** 17 August 2026
**Target completion:** 21 September 2026

### 2.1 Gap Identification & Closure

| Task | Description | Owner | Due | Acceptance Criteria |
|------|-------------|-------|-----|---------------------|
| G-01 | Compile known issues list | Fuad | Aug 19 | Complete list from: Fuad's knowledge, changelog, email threads, git issues |
| G-02 | Classify gaps by severity + demo impact | DAF + Hadri | Aug 21 | Each gap tagged: Demo-blocking / Demo-visible / Background |
| G-03 | Resolve all Demo-blocking gaps | Fuad | Sep 7 | Zero demo-blocking gaps open |
| G-04 | Resolve all Demo-visible gaps | Fuad | Sep 14 | Zero demo-visible gaps open (or documented workaround) |
| G-05 | Document acceptable workarounds | Fuad | Sep 14 | For any unresolved gaps: documented workaround + demo script avoids them |
| G-06 | Regression test after fixes | Fuad | Sep 21 | All previously working features still working after gap closures |

**Gate: Gaps Closed** (Sep 21)
- Known issues triaged ✅
- Demo-blocking gaps: zero ✅
- Demo-visible gaps: zero or workarounds documented ✅
- Regression test passed ✅

---

## Priority 3 — Validate End-to-End Workflows

**Objective:** Every demo-critical user journey works reliably, repeatedly, and under demo conditions.

**Owner:** Ahmad Fuad (execution) → Hadri (validation)
**Start:** 24 August 2026 (after handover docs)
**Target completion:** 28 September 2026

### 3.1 Demo-Critical Path Definition

| Task | Description | Owner | Due | Acceptance Criteria |
|------|-------------|-------|-----|---------------------|
| V-01 | Define 5–8 demo-critical paths | DAF + Hadri | Aug 19 | Documented paths covering: dashboard → alerts → cases → correlations → indicators → AI analyst → threat visualization → executive dashboard |
| V-02 | Create test scenarios for each path | Hadri | Aug 28 | Step-by-step test scripts with expected outcomes |
| V-03 | First validation pass | Fuad | Sep 7 | All paths tested; pass/fail recorded; failures logged for Priority 1/2 |
| V-04 | Second validation pass (post-fixes) | Fuad | Sep 14 | All paths pass after gap closures and hardening |
| V-05 | Demo-condition validation | Fuad + Hadri | Sep 21 | Paths tested with: fresh data, populated database, realistic load, network latency simulation |
| V-06 | CSM integration validation | Fuad + CSM | Sep 21 | Telemetry feed, Score Card, CMERP integration — all tested against frozen v3.0 |
| V-07 | Final validation sign-off | Hadri | Sep 28 | Hadri confirms all demo-critical paths validated and reliable |

### 3.2 Demo-Critical Paths (Proposed)

| # | Path | Start | End | Key Features Exercised |
|---|------|-------|-----|----------------------|
| DCP-1 | Threat Detection | Dashboard | Alert → Case | Dashboard load, alert generation, case creation |
| DCP-2 | Investigation | Case | Correlation → Indicator | Case investigation, correlation analysis, IOC extraction |
| DCP-3 | AI Analysis | Alert | AI Analyst | AI analyst query, RAG response, threat assessment |
| DCP-4 | Threat Visualization | Dashboard | Threat Map + Graph | Geographic intel, threat actor mapping, correlation graph |
| DCP-5 | Executive View | Dashboard | Executive Dashboard | Executive summary, KPIs, posture overview |
| DCP-6 | Compliance | Any | PDPA + RBAC | PII detection, audit log, role-based access |
| DCP-7 | CSM Integration | Telemetry | GovSec Dashboard | SiberSUITE telemetry → GovSec analytics (if ready) |
| DCP-8 | Score Card | GovSec Analytics | Score Card | CNII posture scoring (if ready by Sep) |

**Gate: Workflows Validated** (Sep 28)
- All demo-critical paths pass ✅
- CSM integration tested ✅
- Demo-condition validation passed ✅
- Hadri sign-off ✅

---

## Priority 4 — Hadri Handover

**Objective:** Transfer technical delivery ownership from Fuad to Hadri with sufficient documentation for Hadri to assume architecture, delivery, and demo preparation responsibilities.

**Owner:** Ahmad Fuad (documentation), Hadri (receipt)
**Start:** 17 August 2026
**Target completion:** 31 August 2026

### 4.1 Documentation Package

| Task | Description | Owner | Due | Acceptance Criteria |
|------|-------------|-------|-----|---------------------|
| HO-01 | System architecture document | Fuad | Aug 24 | Architecture diagram, component inventory, data flow, tech stack, dependencies |
| HO-02 | Component documentation | Fuad | Aug 24 | Each component: purpose, interfaces, configuration, known issues |
| HO-03 | Full changelog (v1.0 → v3.0) | Fuad | Aug 24 | Compiled from emails, git history, release notes — every version documented |
| HO-04 | Deployment guide | Fuad | Aug 24 | Step-by-step: environment setup, configuration, deployment, rollback |
| HO-05 | Known issues + technical debt | Fuad | Aug 24 | All known issues, workarounds, technical debt items |
| HO-06 | Integration points documentation | Fuad | Aug 24 | All external integrations: MITRE ATT&CK, CVE, CISA KEV, CSM (telemetry, CMERP), APIs |
| HO-07 | Handover review session | Fuad + Hadri | Aug 28 | Hadri reviews docs, asks questions, identifies gaps |
| HO-08 | Handover sign-off | Hadri | Aug 31 | Hadri confirms sufficient context to assume delivery ownership |

### 4.2 Product Launch Checklist (Hadri's deliverable)

| Task | Description | Owner | Due | Acceptance Criteria |
|------|-------------|-------|-----|---------------------|
| HO-09 | CyberDSA Product Launch Checklist | Hadri | Aug 31 | Comprehensive checklist covering: technical, operational, demo, logistics, staffing, fallback plans |
| HO-10 | Demo environment specification | Hadri | Aug 31 | Hardware, network, software, data requirements for CyberDSA demo environment |

**Gate: Handover Complete** (Aug 31)
- All 7 documentation items delivered ✅
- Hadri review session conducted ✅
- Hadri sign-off ✅
- Launch checklist produced ✅
- Demo environment specified ✅

---

## Priority 5 — CyberDSA Demo Preparation

**Objective:** Define, build, and rehearse the CyberDSA demonstration flow. The demo must be compelling, reliable, and repeatable under live conditions.

**Owner:** Hadri (demo design), Fuad (demo environment), DAF (narrative)
**Start:** 1 September 2026 (after handover + hardening underway)
**Target completion:** 4 October 2026 (dress rehearsal)

### 5.1 Demo Design & Build

| Task | Description | Owner | Due | Acceptance Criteria |
|------|-------------|-------|-----|---------------------|
| DP-01 | Define demo narrative | DAF | Sep 7 | 5–7 minute story arc: problem → platform → value → CSM joint proposition |
| DP-02 | Define demo script | Hadri | Sep 14 | Step-by-step script: which features shown, in what order, with what data |
| DP-03 | Prepare demo dataset | Fuad | Sep 14 | Realistic Malaysian threat intelligence data pre-loaded; no live dependency on external feeds |
| DP-04 | Build demo environment | Fuad | Sep 21 | Dedicated environment: stable, pre-loaded, isolated from development |
| DP-05 | Demo integration check | Fuad + CSM | Sep 21 | CSM integration features (if demoed) working in demo environment |
| DP-06 | CSM joint demo alignment | DAF + CSM | Sep 21 | CSM aware of demo flow; joint positioning agreed; no surprise content |

### 5.2 Demo Rehearsal

| Task | Description | Owner | Due | Acceptance Criteria |
|------|-------------|-------|-----|---------------------|
| DR-01 | First rehearsal (internal) | Hadri + Fuad | Sep 21 | Full demo run-through; timing recorded; issues logged |
| DR-02 | Fix rehearsal issues | Fuad | Sep 28 | All issues from first rehearsal resolved |
| DR-03 | Second rehearsal (with DAF) | Hadri + DAF | Sep 28 | DAF reviews demo; narrative alignment confirmed; timing within target |
| DR-04 | Dress rehearsal | Full team | Oct 2 | Full dress rehearsal: live conditions, backup tested, timing confirmed |
| DR-05 | Demo fallback plan | Hadri | Sep 28 | Documented: what to show if X fails, offline demo option, pre-recorded backup |
| DR-06 | Booth staffing schedule | DAF | Oct 2 | Who demos when; rotation; breaks; technical support on standby |

**Gate: Demo-Ready** (Oct 1–2)
- Demo narrative defined ✅
- Demo script finalised ✅
- Demo environment stable ✅
- Two rehearsals completed ✅
- Dress rehearsal passed ✅
- Fallback plan ready ✅
- Booth staffing scheduled ✅

---

## CSM Integration Validation

Three integration tracks depend on frozen v3.0. Each must be validated before demo prep.

| Track | Init | Readiness | Validation Due | Demo-Critical? | Owner |
|-------|------|----------|----------------|----------------|-------|
| Telemetry Integration | INIT-004-002 | Integration-phase | Sep 21 | **Yes** | Fuad + CSM |
| Score Card Framework | INIT-010-001 | Framed | Sep 21 (if feasible) | **Yes** | Fuad + CSM |
| CBOM Agent | INIT-010-002 | Conceptual | N/A | No | Deferred |

**Rule:** Integration features are only demoed if validated by Sep 21. If not ready, demo runs without them. No exceptions. No live integration dependencies in the demo.

---

## Hadi Onboarding (PM Track)

| Task | Description | Owner | Due | Acceptance Criteria |
|------|-------------|-------|-----|---------------------|
| PM-01 | Confirm Hadi start date | DAF | Aug 17 | Official start date confirmed |
| PM-02 | Hadi onboarded | DAF + Hadi | Aug 24 | Hadi has system access, understands product, can participate in planning |
| PM-03 | Hadi produces commercial readiness outline | Hadi | Sep 7 | Commercial model, pricing, packaging, POC process — draft outline |
| PM-04 | Hadi owns PM dimension of launch | Hadi | Sep 14 | Hadi leads commercial readiness, demo support, stakeholder coordination |

**If Hadi not onboarded by Aug 24:** PM track defaults to DAF. Commercial readiness (RSK-010-003) remains DAF-owned. Risk to launch increases.

---

## Commercial Readiness (Parallel Track)

Runs parallel to technical readiness. Owned by DAF (until Hadi onboarded).

| Task | Description | Owner | Due | Acceptance Criteria |
|------|-------------|-------|-----|---------------------|
| C-01 | Define pricing model | DAF (→Hadi) | Sep 7 | Per-product pricing: VoronCitadel, GovSec, ChainSentry — at least draft |
| C-02 | Define packaging | DAF (→Hadi) | Sep 14 | What's included in demo, what's POC scope, what's full deployment |
| C-03 | Define post-demo conversion path | DAF (→Hadi) | Sep 14 | What happens after CyberDSA lead: follow-up process, POC terms, timeline |
| C-04 | Prepare commercial materials | DAF + Azza | Sep 21 | One-pager, pricing sheet, POC template — ready for CyberDSA distribution |
| C-05 | CSM joint proposition | DAF + CSM | Sep 21 | Joint CSM-Aras value proposition document — agreed by both sides |

**Gate: Commercial-Ready** (Sep 21)
- Pricing model defined ✅
- Packaging documented ✅
- Post-demo conversion path agreed ✅
- Commercial materials produced ✅
- CSM joint proposition agreed ✅

---

## Risk Mitigation Actions

| Risk | Mitigation Action | Owner | Due |
|------|-------------------|-------|-----|
| RSK-010-001 (Hadi delay) | Confirm start date by Aug 17; if unconfirmed, DAF absorbs PM track | DAF | Aug 17 |
| RSK-010-002 (Security gap) | Schedule security assessment by Aug 19; complete by Sep 7 | DAF | Aug 19 |
| RSK-010-003 (Commercial gap) | Commercial readiness track (C-01 through C-05) | DAF → Hadi | Sep 21 |
| RSK-004-003 (Timeline) | Weekly milestone reviews; any slippage triggers scope reduction | DAF | Weekly |
| Demo failure | Fallback plan (DR-05): pre-recorded demo, offline mode, reduced scope | Hadri | Sep 28 |

---

## Escalation & Decision Points

| Date | Decision | Decision Authority | Options |
|------|----------|-------------------|---------|
| Aug 17 | Hadi start date confirmed? | DAF | If no → DAF absorbs PM; commercial gap risk increases |
| Aug 24 | Handover docs delivered? | DAF | If no → hardening compressed to 3 weeks; scope reduction needed |
| Aug 31 | Hadri sign-off + launch checklist? | DAF | If no → demo prep starts late; rehearsal time reduced |
| Sep 7 | Security assessment complete? | DAF | If findings severe → scope reduction; demo avoids affected areas |
| Sep 14 | All High bugs/gaps closed? | DAF | If no → demo scope reduced to validated paths only |
| Sep 21 | All validations passed? | DAF + Hadri | **Go / No-Go for full demo scope** — if fail, reduced demo scope |
| Sep 28 | Dress rehearsal passed? | DAF | **Final Go / No-Go** — if fail, fallback demo plan activated |
| Oct 2 | Final readiness check | DAF | Confirm: environment, staff, materials, logistics |

---

## Scope Reduction Triggers

If timeline slips, reduce scope in this order (last cut first):

1. **Cut:** CBOM Agent demo (already not critical)
2. **Cut:** Score Card demo (if not validated by Sep 21)
3. **Cut:** CSM integration demo (if not validated by Sep 21)
4. **Cut:** AI Analyst demo (reduced to pre-set query, not live)
5. **Cut:** Threat Visualization (use pre-loaded data, not live query)
6. **Never cut:** Core Platform MVP demo (Dashboard → Alerts → Cases → Correlations → Indicators) — this is the minimum viable demo

**Minimum viable demo:** Dashboard → Alert → Case → Correlation → Indicator (3-minute script, pre-loaded data, no external dependencies).

---

## Weekly Milestone Review

**Cadence:** Every Monday, 17:00 MYT (09:00 UTC), starting Aug 17
**Chair:** DAF
**Attendees:** Hadri, Fuad (Hadi when onboarded)
**Agenda:**

1. Milestone status (this plan's tasks)
2. Blockers and risks
3. Scope decisions (if slippage)
4. CSM integration progress
5. Commercial readiness progress
6. Next week's priorities

**Standing question:** "Are we on track for demo-ready by October 1?"

---

## Summary: Critical Path at a Glance

```
Aug 17 ─ DAF structures readiness plan (THIS DOCUMENT) ✅
         DAF confirms Hadi start date
Aug 19 ─ Demo-critical paths defined
         Known issues compiled
         Security assessment resource engaged
Aug 21 ─ Gaps classified by severity
Aug 24 ─ Fuad delivers handover docs (HO-01 to HO-06)
         Hadi onboarding deadline
Aug 28 ─ Performance targets set
         Test scenarios created
         Handover review session
Aug 31 ─ Hadri sign-off
         Launch checklist delivered
         RBAC verified
Sep  7 ─ Critical bugs fixed
         Security assessment complete
         Demo narrative defined
         Commercial pricing draft
Sep 14 ─ High bugs fixed
         Security issues resolved
         Demo script finalised
         Demo dataset prepared
         Commercial packaging defined
Sep 21 ─ 48h stability test
         Demo environment built
         CSM integration validated
         CSM joint proposition agreed
         Commercial materials ready
Sep 28 ─ All validations passed
         Dress rehearsal
         Fallback plan ready
         Booth staffing scheduled
Oct  1 ─ DEMO-READY ✅
Oct  2 ─ Dress rehearsal (final)
Oct  4 ─ Final readiness check
Oct  5 ─ CyberDSA Day 1 🚀
```

---

*This plan is a living document. Updated weekly during milestone review. Any scope or timeline changes require DAF approval.*
