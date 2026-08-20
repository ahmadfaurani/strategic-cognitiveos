---
id: GOV-AIP-PROD-OPS-001
record_type: document
title: "Actionable Intelligence Protocol — Productization & Operationalization Enablement"
created_at: 2026-08-20T11:42:00+00:00
updated_at: 2026-08-20T11:42:00+00:00
owner: DAF
status: active
priority: critical
sensitivity: internal
lifecycle_state: active
confidence: high
tags:
  - domain/governance
  - domain/portfolio-governance
  - domain/productization
  - domain/operationalization
  - domain/cybersecurity-productisation
source:
  type: direct
  reference: "DAF directive 2026-08-20 11:40 UTC — post-MVP portfolio review"
summary: "Protocol converting the 3-product MVP portfolio review into sequenced, gated, actionable productization and operationalization tracks. Covers product delivery, organisational capacity, commercial activation, and operational readiness."
strategic_significance: "The portfolio has 3 MVP specs but no unified productization pathway. VoronCitadel is production-deployed but GTM-stalled. GovSec TIP targets CyberDSA Oct 2026 with 11 deferrals. ChainSentry has 4 critical gaps blocking pilot. This protocol converts those gaps into sequenced action tracks with gates, owners, and exit criteria."
mission_alignment:
  - cybersecurity-productisation
  - organisational-capability
  - portfolio-governance
related_records:
  - GOV-PORTFOLIO-REGISTER-001
  - GOV-TBH-REGISTRY-001
  - DOC-20260814-001 (ChainSentry MVP v3.0)
  - DOC-20260814-002 (VoronCitadel MVP v2.0)
  - DOC-20260814-003 (GovSec TIP MVP v3.0)
document_type: sop
file_path: "governance/AIP-PRODUCTIZATION-OPERATIONALIZATION.md"
version: "1.0"
author: DAF
---

# Actionable Intelligence Protocol — Productization & Operationalization Enablement

**Created:** 2026-08-20 | **Authority:** DAF | **Review cadence:** Weekly (aligned with Cognitive Loop Review, Monday 10:30 AM UTC+8)

---

## 1. Protocol Purpose

This protocol converts the MVP portfolio review into action. It defines three sequenced productization tracks, the organisational capacity required to execute them, and the operational readiness gates that must close before each product moves from one readiness level to the next.

**Scope:** 3 flagship products (VoronCitadel, GovSec TIP, ChainSentry) + 3 pending-spec products (VoronScout, LE-UIP, SEC-AF).

**Core question:** What actions, taken now, create the greatest improvement in the probability of achieving portfolio commercialisation objectives?

---

## 2. Portfolio State Summary

| Product | Readiness | Target | Critical Blockers | Timeline |
|---------|-----------|--------|-------------------|----------|
| VoronCitadel | Production-deployed | Commercial-ready (GTM activation) | CSM GTM stall; TBH-001 unfilled; POC doc due Aug 24 | Immediate (CSM channel live) |
| GovSec TIP | Prototype (v3.0 spec) | Demo-ready (CyberDSA Oct 2026) | 11 Phase 2 deferrals; security remediation; build not started | T-12 weeks to CyberDSA |
| ChainSentry | Prototype (v3.0, verified Aug 11) | Pilot-ready | 4 critical gaps (deployment, access, credentials, demo boundary) | Post-VoronCitadel POC |
| VoronScout | Pending | — | No spec | — |
| LE-UIP | Pending | — | No spec | — |
| SEC-AF | Pending | — | No spec | — |

**Structural constraint:** TBH-001 (PM — Cyber Security Practice) blocks execution across all tracks. DAF is interim owner by default. Without this role, every POC, pilot, and delivery falls to DAF — the portfolio's known bottleneck (§6.10, every Cognitive Loop).

---

## 3. Productization Tracks

Three parallel tracks, sequenced by commercial urgency. Each track has defined phases, gates, and exit criteria. Tracks share a common operationalization layer (Section 4).

---

### Track A — VoronCitadel: GTM Activation (IMMEDIATE)

**Rationale:** Most mature product. Production-deployed. CSM MOU signed. Revenue path exists. Every day of delay is unrealised pipeline.

#### A1: POC Document Finalisation (CRITICAL — due Aug 24 10am MYT)

| Item | Detail |
|------|--------|
| Action | Deliver 8-section VoronCitadel POC document for Bursa Malaysia (ACT-20260820-004) |
| Owner | Creation: Athena → QC: Fuad → Approval: DAF → Execution: TBH-001 (interim: DAF) |
| Deadline | Aug 24, 10:00 AM MYT (Aug 24, 02:00 UTC) |
| Gate | Document approved and delivered to CSM channel |
| Exit criterion | Bursa Malaysia POC scope confirmed; CSM can approach with concrete offering |
| Current status | Fuad reviewing; DAF pre-flight check format elevated |
| Risk | If Fuad QC slips to Aug 23, DAF approves same-day — no float |

#### A2: CSM Channel Activation

| Item | Detail |
|------|--------|
| Action | Confirm CSM working group: Aisha as PIC, Amelia introduced to Zulfeka, sync-up week of Aug 25 |
| Owner | DAF (relationship) → Amelia (stakeholder engagement) → Aisha (CSM coordinator) |
| Deadline | Aug 28 (sync-up complete) |
| Gate | Working group confirmed; first joint outreach target identified |
| Exit criterion | CSM sales team trained on VoronCitadel positioning; first POC request through CSM channel |
| Dependency | A1 (POC document must exist before CSM approaches targets) |
| Risk | If Aisha not confirmed by Aug 22, escalate to En. Zulfeka directly |

#### A3: Commercial Packaging

| Item | Detail |
|------|--------|
| Action | Finalise pricing model, POC scope menu, and commercial SLA terms for VoronCitadel |
| Owner | DAF (pricing authority) + Fuad (technical scope) |
| Deadline | Sep 5 |
| Gate | Commercial package reviewed and approved |
| Exit criterion | Pricing sheet, POC template, and SLA terms documented; ready for CSM to quote |
| Dependency | A1 (POC document defines delivery scope) |
| Input | VoronCitadel MVP Spec v2.0 §7 (scope boundaries); ChainSentry commercial packages as reference format |

#### A4: White-Label Readiness (CSM Engagement)

| Item | Detail |
|------|--------|
| Action | UI/UX refinement including white-labelling for CSM co-branded deployment |
| Owner | Fuad (technical) + DAF (brand approval) |
| Deadline | Sep 15 |
| Gate | White-label config verified; CSM branding applied to demo instance |
| Exit criterion | CSM can present VoronCitadel under co-brand without engineering intervention |
| Dependency | A2 (CSM working group confirmed) |
| Note | This is one of Fuad's 5 flagged operational dependencies (previously committed, within freeze scope) |

---

### Track B — GovSec TIP: CyberDSA Demo Readiness (T-12 WEEKS)

**Rationale:** CyberDSA Oct 2026 is the hard external deadline. 12 weeks to move from spec to demo-ready. This is the tightest track.

#### B1: Security Remediation (CRITICAL — first)

| Item | Detail |
|------|--------|
| Action | Close OWASP Web Top 10 + LLM Top 10 critical/high findings; resolve 54 npm audit findings |
| Owner | Fuad (technical) + DAF (security approval) |
| Deadline | Sep 15 (T-8 weeks before CyberDSA) |
| Gate | Security audit sign-off; no critical/high open findings |
| Exit criterion | Penetration test passed; security review documented |
| Rationale | Cannot demo a national security platform with open critical vulnerabilities |

#### B2: Core Build — 4 Domain Modules

| Item | Detail |
|------|--------|
| Action | Build the 4 domain modules: TIP Ingestion, Analysis & Detection, Alerting & Operations, Governance & Compliance |
| Owner | Fuad (build) + TBH-001 (execution coordination, when filled) |
| Deadline | Sep 30 (T-5 weeks) |
| Gate | All 4 domains functional with seed data |
| Exit criterion | 12 core entities, 12 scheduled pipelines, 147 API endpoints — at least 60% functional with demo data |
| Dependency | B1 (security remediation first — don't build on vulnerable foundation) |
| Sequence | Ingestion → Analysis → Alerting → Governance (data flow order) |
| Risk | 12 weeks is tight for a 4-domain build. If B1 slips, compress B2 by scoping to 2 domains (Ingestion + Analysis) for demo |

#### B3: AI Analyst Workbench (Demo Differentiator)

| Item | Detail |
|------|--------|
| Action | Build RAG-powered AI Analyst with natural language query, case AI, and NLP classification |
| Owner | Fuad (RAG pipeline) + DAF (sovereign AI endpoint config) |
| Deadline | Oct 5 (T-2 weeks) |
| Gate | AI Analyst responds to 5 canonical queries with structured results |
| Exit criterion | Demo scenario: analyst asks "brief me on today" → receives prioritised summary with live data |
| Dependency | B2 (needs data in the platform for RAG to retrieve) |
| Differentiator | This is the UX innovation that separates GovSec from commodity TIPs — must be in the demo |

#### B4: Demo Environment & Scenario Pack

| Item | Detail |
|------|--------|
| Action | Prepare demo instance with Malaysian government seed data, 3 scripted scenarios, and live AI Analyst walkthrough |
| Owner | TBH-001 (when filled) or DAF (interim) + Fuad (technical setup) |
| Deadline | Oct 10 (T-1 week) |
| Gate | Demo runs end-to-end without failure for 3 consecutive rehearsals |
| Exit criterion | CSM/DAF can present GovSec TIP at CyberDSA booth with 15-min demo cycle |
| Dependency | B2 + B3 |
| Scenarios | (1) Daily triage with AI Analyst, (2) Threat hunting with MITRE gap map, (3) Executive posture review |

#### B5: CyberDSA Brand Narrative

| Item | Detail |
|------|--------|
| Action | Execute cyberdsa-media repo: 13 section directories, press release, social media, one-pager, QC checklist |
| Owner | DAF (brand authority) + Amelia (stakeholder/media) |
| Deadline | Oct 8 (content frozen; materials printed/deployed by Oct 10) |
| Gate | All content QC-checked per cyberdsa-media checklist |
| Exit criterion | Press release, booth one-pager, social media pack, and demo handouts ready |
| Dependency | B4 (demo must work before promoting it) |
| Input | cyberdsa-media repo (TLP:AMBER), brand glossary, templates |

---

### Track C — ChainSentry: Pilot Readiness (POST-VORONCITADEL)

**Rationale:** 4 critical gaps block pilot. VoronCitadel GTM is more urgent, but ChainSentry gaps are security liabilities that worsen with time. Credential rotation is non-negotiable regardless of commercial priority.

#### C1: Credential Closure & Secret Governance (CRITICAL — security)

| Item | Detail |
|------|--------|
| Action | Rotate 4 exposed keys; implement managed secret storage; verify masked health output |
| Owner | Fuad (technical) + DAF (security approval) |
| Deadline | Aug 30 (regardless of commercial priority — security liability) |
| Gate | All exposed credentials revoked; replacements verified; rotation cadence documented |
| Exit criterion | Key-health endpoint shows no exposed credentials; rotation owner and cadence assigned |
| Rationale | Exposed keys are an active security liability. This is non-negotiable. |

#### C2: Deployment Parity

| Item | Detail |
|------|--------|
| Action | Create release manifest; deploy controlled release; re-run authenticated API/risk regression sweep |
| Owner | Fuad (technical) |
| Deadline | Sep 10 |
| Gate | Deployment matches development branch; regression sweep passes |
| Exit criterion | 22-commit/32-day gap closed; release manifest documented; all 32 GET paths return HTTP 200 |
| Dependency | C1 (don't deploy exposed credentials to fresh environment) |

#### C3: External Access & Named Identity

| Item | Detail |
|------|--------|
| Action | Provision TLS termination; correct callback/session URL; issue per-person pilot accounts |
| Owner | Fuad (technical) + DAF (identity approval) |
| Deadline | Sep 15 |
| Gate | End-to-end login from pilot network verified |
| Exit criterion | Named investigator can sign in over TLS; role-appropriate access confirmed |
| Dependency | C2 (deployment must be current) |

#### C4: Live-vs-Demo Boundary

| Item | Detail |
|------|--------|
| Action | Inventory every pilot route/tool; label or remove demo-only behavior; wire mock registry to live providers or exclude |
| Owner | Fuad (technical) |
| Deadline | Sep 20 |
| Gate | No pilot result returns fixture data |
| Exit criterion | Every pilot surface proven to return live or correctly-labelled unavailable/deferred data |
| Dependency | C2 + C3 |

#### C5: Pilot Scope Definition

| Item | Detail |
|------|--------|
| Action | Define pilot scope: target organisation (LE/FIU/regulator), success criteria, duration, data boundary |
| Owner | DAF (commercial) + TBH-001 (execution, when filled) |
| Deadline | Sep 30 |
| Gate | Pilot scope document approved |
| Exit criterion | Named pilot target, 6-week pilot duration, success scorecard defined |
| Dependency | C1-C4 (all critical gaps closed before pilot commitment) |
| Input | ChainSentry MVP v3.0 §7.1 (pilot readiness requirements); Product Brief commercial packages |

---

## 4. Operationalization Enablement Layer

This layer is shared across all tracks. Without it, productization stalls regardless of technical readiness.

### 4.1 TBH-001 — Project Manager (Cyber Security Practice)

| Item | Detail |
|------|--------|
| Current state | Open in TBH Registry. Interim owner: DAF. Blocks ACT-20260820-004 + all future POC executions |
| Action | Define hiring approach (internal secondment vs external hire vs contractor) |
| Owner | DAF |
| Deadline | Aug 27 (Wave 2 hiring window) |
| Gate | Hiring approach decided; JD circulated (already exists: `strategic-cognitiveos/artifacts/jd-poc-engineer.md`) |
| Exit criterion | Named individual in role; DAF no longer interim owner for POC execution |
| Escalation | TBH escalation rule: >2 weeks blocking CRITICAL without workaround → DAF must assign interim or reassign action. Clock started Aug 20. Escalation date: Sep 3 |
| Impact if unfilled | Every POC (VoronCitadel Bursa, ChainSentry pilot, future CSM channel) defaults to DAF. Portfolio collision risk (§6.10). This is the single highest-leverage hire in the portfolio |

### 4.2 Delivery Capability Matrix

| Capability | Current Owner | Required Owner | Gap | Resolution |
|------------|--------------|----------------|-----|------------|
| POC document creation | Athena (AI) | Athena | None | ✅ Operational |
| POC document QC | Fuad | Fuad | None (but bandwidth risk) | Monitor load; consider second reviewer for ChainSentry track |
| POC document approval | DAF | DAF | None | ✅ Operational |
| POC execution | TBH-001 (TBA) | TBH-001 | 🔴 Critical | Hire or assign by Aug 27 |
| Technical build (all products) | Fuad | Fuad + additional eng | Bandwidth risk | Fuad is sole technical across 3 products. Assess need for second engineer by Sep 15 |
| Commercial pricing & packaging | DAF | DAF | None | ✅ DAF authority |
| CSM channel management | DAF → Amelia/Aisha | Amelia + Aisha | In transition | Confirm Aisha PIC by Aug 22 |
| Brand & media (CyberDSA) | DAF → Amelia | Amelia | In transition | Amelia leads, DAF approves |
| Security audit & sign-off | DAF | DAF + external assessor | External assessor TBA | Engage assessor by Sep 1 for GovSec TIP pen test |

### 4.3 Quality Gate Framework

Each productization track has a quality gate at each phase boundary. Gates are pass/fail — no partial credit.

**Universal gates (apply to all tracks):**

| Gate | Check | Owner | Evidence Required |
|------|-------|-------|-------------------|
| Security | No open critical/high vulnerabilities | DAF (approval) | Audit report; pen test results |
| Deployment | Build deployed and verified | Fuad (technical) | Regression sweep; API check; build manifest |
| Identity | Named accounts with role-appropriate access | DAF (approval) | Account list; RBAC verification |
| Data boundary | No fixture/demo data in pilot surfaces | Fuad (technical) | Surface inventory; data provenance check |
| Documentation | Spec, API contract, and runbook current | TBH-001 (when filled) or DAF | Document review sign-off |
| Commercial | Pricing, POC template, SLA terms ready | DAF | Commercial package approved |

**Track-specific gates:** defined inline in each track section above.

### 4.4 Cross-Track Dependencies

```
Track A (VoronCitadel)
  A1 POC Document ──────┬──> A2 CSM Activation ──> A4 White-Label
                        └──> A3 Commercial Packaging

Track B (GovSec TIP)
  B1 Security ──> B2 Core Build ──> B3 AI Analyst ──> B4 Demo Env ──> B5 Brand
                                                        │
Track C (ChainSentry)                                    │
  C1 Credentials ──> C2 Deployment ──> C3 Access ──> C4 Demo Boundary ──> C5 Pilot Scope
                                                        │
                                                        ▼
                                              TBH-001 (shared blocker)
```

**Critical path:** C1 (credentials) runs in parallel with A1 (POC doc) — both are Aug deadlines. B1 (security) starts after C1 method is established (secret governance pattern reusable). TBH-001 gates A2 execution, B4 demo rehearsals, and C5 pilot scope — hire by Aug 27 or all three tracks absorb DAF as interim.

### 4.5 Pending-Spec Products (VoronScout, LE-UIP, SEC-AF)

These products remain at *Pending* status. No spec, no build, no commercial commitment. They enter this protocol only when:

1. A sponsor or commercial trigger materialises
2. DAF authorises spec development
3. A product brief is drafted and enters the Product Readiness Index

**Current action:** None. Monitor as intelligence. Reassess post-CyberDSA (Nov 2026 review).

---

## 5. Sequencing & Timeline

| Week | Track A (VoronCitadel) | Track B (GovSec TIP) | Track C (ChainSentry) | Ops Layer |
|------|----------------------|---------------------|---------------------|-----------|
| W1 (Aug 20-26) | A1 POC doc (CRITICAL) | — | C1 Credentials (CRITICAL) | TBH-001 hiring approach decided |
| W2 (Aug 27-Sep 2) | A2 CSM activation | B1 Security starts | C2 Deployment parity | TBH-001 target fill; Fuad bandwidth check |
| W3 (Sep 3-9) | A3 Commercial packaging | B1 Security continues | C2 continues; C3 starts | External security assessor engaged |
| W4 (Sep 10-16) | A4 White-label starts | B2 Core build starts | C3 Access; C4 Demo boundary | — |
| W5 (Sep 17-23) | A4 continues | B2 continues | C4 continues; C5 Pilot scope | Second engineer assessment |
| W6 (Sep 24-30) | A4 complete | B2 continues; B3 starts | C5 Pilot scope complete | — |
| W7 (Oct 1-7) | — | B3 AI Analyst; B4 Demo env | — | — |
| W8 (Oct 8-14) | — | B4 Demo rehearsals; B5 Brand | — | CyberDSA prep final |
| W9 (Oct 15-21) | — | **CyberDSA 2026** | — | Post-event debrief |

---

## 6. Decision Points

Decisions required from DAF by date. Non-decision defaults are noted.

| Date | Decision | Options | Default if no decision |
|------|----------|---------|----------------------|
| Aug 22 | CSM Aisha PIC confirmed | Confirm / escalate to Zulfeka | Escalate (PRG-002 kill date Aug 22) |
| Aug 24 | VoronCitadel POC doc approved | Approve / request changes | DAF same-day approval (no float) |
| Aug 27 | TBH-001 hiring approach | Internal secondment / external hire / contractor | Contractor (fastest path to interim) |
| Aug 30 | ChainSentry credential rotation verified | Accept / reject | Reject (security non-negotiable) |
| Sep 1 | External security assessor engaged for GovSec pen test | Engage / defer | Engage (CyberDSA deadline requires it) |
| Sep 3 | TBH-001 escalation trigger | Assign interim / reassign actions / accept DAF as interim | DAF absorbs (portfolio collision risk) |
| Sep 15 | Second engineer assessment | Hire / defer / redistribute | Defer (Fuad continues solo) |
| Sep 30 | ChainSentry pilot scope approved | Approve / defer to post-CyberDSA | Defer to post-CyberDSA |
| Oct 8 | CyberDSA demo content frozen | Freeze / allow changes | Freeze |

---

## 7. Risk Register

| ID | Risk | Track | Probability | Impact | Mitigation | Owner |
|----|------|-------|------------|--------|------------|-------|
| RSK-PO-001 | TBH-001 unfilled >4 weeks | All | High | High | Contractor interim; escalate at 2-week mark per TBH rules | DAF |
| RSK-PO-002 | Fuad bandwidth overload (sole tech across 3 products) | B, C | Medium | High | Second engineer by Sep 15; scope B2 to 2 domains if needed | DAF |
| RSK-PO-003 | CyberDSA timeline slip (B2 incomplete by Sep 30) | B | Medium | High | Demo with 2 domains (Ingestion + Analysis) + AI Analyst; defer Alerting + Governance to post-event | DAF |
| RSK-PO-004 | ChainSentry credential exposure exploited | C | Low | Critical | C1 by Aug 30 regardless of commercial priority | Fuad |
| RSK-PO-005 | CSM channel stall (Aisha not confirmed) | A | Medium | High | Direct escalation to Zulfeka; PRG-002 kill date Aug 22 | DAF |
| RSK-PO-006 | VoronCitadel POC doc QC slips past Aug 23 | A | Low | Medium | DAF approves same-day; no float in schedule | DAF |
| RSK-PO-007 | GovSec pen test fails | B | Medium | Critical | Start B1 early; engage assessor Sep 1; 2-week remediation window | Fuad |

---

## 8. Success Metrics

| Metric | Target | Measurement | Cadence |
|--------|--------|-------------|---------|
| VoronCitadel POC delivered | Aug 24 10am MYT | Document approved by DAF | One-time |
| CSM channel first POC request | Sep 15 | Named POC request through CSM channel | Weekly |
| ChainSentry critical gaps closed | 4/4 by Sep 20 | Gap matrix review | Weekly |
| GovSec demo rehearsal success | 3 consecutive by Oct 10 | Rehearsal log | Weekly from Oct 1 |
| TBH-001 filled | Aug 27 (target) | Named individual in role | Weekly |
| Fuad bandwidth | <80% allocation across tracks | DAF assessment | Weekly |

---

## 9. Review Cadence

**Weekly:** Aligned with Cognitive Loop Review (Monday 10:30 AM UTC+8). Review all 3 tracks, update status, check gates, flag risks.

**Daily (Aug 20-24):** VoronCitadel POC doc sprint. Status check each evening.

**Post-CyberDSA (Oct 21):** Full protocol review. Update Product Readiness Index. Reassess pending-spec products. Close completed tracks.

---

## 10. Protocol Authority

This protocol is a governance instrument of the CognitiveOS framework. It is binding on all agents and team members involved in productization execution. Deviations require DAF approval and are logged to the audit trail.

**Related instruments:**
- TBH Registry (`governance/TBH-REGISTRY.md`) — tracks TBH-001 and future hiring gaps
- Portfolio Register (`governance/PORTFOLIO-REGISTER.md`) — tracks programme-level status and kill dates
- Product Readiness Index (`indexes/product-readiness-index.md`) — tracks product readiness levels
- MVP Specifications (`products/[product]/MVP_SPECIFICATION.md`) — canonical product baselines

---

*This protocol converts a portfolio review into action. Its success is measured not by analysis depth but by products delivered, gates closed, and commercial pipeline activated.*
