---
id: ESF-20260829-002
record_type: artifact
artifact_type: engineered-success-framework
title: "Engineered Success Framework — Fuad Practice Technical Authority (Aug 2026–Aug 2027)"
created_at: 2026-08-29T04:36:00+00:00
updated_at: 2026-08-29T04:36:00+00:00
owner: faurani-jaafar
status: active
priority: critical
sensitivity: confidential
lifecycle_state: canonical
confidence: high
tags:
  - domain/organisational-capability
  - domain/strategic
  - domain/cybersecurity-productisation
  - domain/capacity-building
  - domain/organisational-design
  - domain/product-management
  - domain/threat-intelligence
  - framework/engineered-success
  - lifecycle/active
source:
  type: cognitive-loop
  reference: FUAD-COMPREHENSIVE-PROFILE-20260829.md + AIP-20260829-001
summary: "12-month ESF for Fuad's transition from SPOF executor to technical authority scaling through engineering team, delegation, and product discipline. 5 DoD gates from Dec 2026 to Jun 2027."
strategic_significance: "Fuad is sole technical authority across 3 flagship products at ~0.3 FTE. Without structural engineering capacity, every product is one person's bandwidth from stalling. This ESF engineers the conditions under which that changes."
mission_alignment:
  - cybersecurity-productisation
  - engineering-capacity
  - organisational-capability-building
  - bursa-poc
  - cyberdsa-2026
related_records:
  - ESF-20260829-001
  - AIP-20260829-001
  - STK-20260804-003
  - RSK-20260820-003
  - RSK-20260811-001
  - ACT-20260820-007
  - ACT-20260820-008
  - DEC-20260818-007
  - DEC-20260820-007
  - DEC-20260820-009
related_initiative: INIT-20260811-001
---

# ESF-20260829-002 — Engineered Success Framework: Fuad Practice Technical Authority

## §9 Doctrine Application

This framework engineers the probability of success for Fuad's transition from **sole technical executor across 3 flagship products** to **technical authority operating through a structured engineering team** — setting architecture, validating readiness, and governing product quality while delegated engineers execute day-to-day development, POC environments, and documentation.

**Diligence Level:** D3 (Strategic) — influences product, commercial, and organisational outcomes.

**Relationship to DAF ESF (ESF-20260829-001):** The DAF ESF engineers DAF's transition from primary driver to institutional architect. This ESF engineers the technical counterpart — Fuad's transition from SPOF builder to technical leader who scales through team, process, and architecture. The two ESFs are complementary: DAF's DoD-2 (non-DAF owners) depends on Fuad's DoD-1 (engineering team operational). They share the TBH-001 and HoE dependencies.

---

## 1. Objective

**12-Month Objective (Aug 2026 → Aug 2027):**

Fuad operates as Practice Technical Authority — defining product architecture, validating technical readiness, governing quality gates, and aligning product development to strategic deliverables — while a structured engineering team (HoE + CSE + junior backend + Syahir) executes hands-on development, POC environments, documentation maintenance, and claims validation. His time shifts from ~70% hands-on development to 60% architecture/strategy, 30% technical validation, 10% hands-on intervention.

**The governing question:** What must be true for Fuad to stop being the single point of failure on all 3 products while increasing the total technical throughput of the practice?

---

## 2. Definition of Done (DoD) — 5 Checkpoints

### DoD-1: Engineering Team Operational (Q1 2027)

**Gate:** Head of Engineering hired and active. At least one additional engineering role (CSE or junior backend) filled or contractor engaged. Fuad has delegated ≥40% of hands-on technical work to team members. Engineering cadence established (code review, deployment process, technical documentation cycle).

**Constraint:** Hiring approval is October 2026. Operational hiring starts post-October. Realistic timeline: Oct posting → Nov interviews → Dec offer/accept → Jan 2027 start. DoD-1 shifts from Dec 31 to Q1 2027.

**Interim mitigation (Sep–Dec 2026):** Contractor engagement if budget allows, OR formal risk acceptance that SPOF persists through Q4 2026. Fuad carries technical execution through CyberDSA + Bursa POC window with Syahir support.

**Evidence:**
- [ ] HoE hired and in seat (ACT-20260820-007 closed)
- [ ] CSE hired or contractor engaged (ACT-20260820-008 closed or interim)
- [ ] Task assignment register shows ≥40% of technical tasks assigned to non-Fuad engineers
- [ ] Code review process documented and running (≥2 reviews/week)
- [ ] Deployment process documented (CI/CD or manual runbook)
- [ ] Fuad's direct code commit rate has decreased by ≥30% from Aug 2026 baseline

**Failure mode:** HoE hired but Fuad doesn't delegate — "I'll do it faster myself" → SPOF persists despite capacity. OR: hiring delayed past Jan 2027 → SPOF persists through Q1 2027.
**Block date:** Q1 2027 (revised from Dec 31, 2026 — hiring approval gates October)

### DoD-2: VoronCitadel Bursa POC Completed as Reference Case (Mar 31, 2027)

**Gate:** Bursa Malaysia POC completed within agreed timeline. TPRM + federated compliance features production-ready. Bursa reference case documented. RSWG §2.6 / ITSS §10 alignment demonstrated and evidenced.

**Evidence:**
- [ ] POC completion report signed by Bursa and Aras
- [ ] TPRM module production-ready (not just POC-grade)
- [ ] Federated compliance document-checking operational
- [ ] RSWG 9 control domains mapped to VoronCitadel capabilities (ACT-20260827-001 closed)
- [ ] ITSS §10 alignment evidenced (17 requirements, 3 use cases, 6 test scenarios passed)
- [ ] Bursa reference case document created and approved by DAF
- [ ] Lessons learned documented (what worked, what didn't, what to change for next POC)

**Failure mode:** POC runs but doesn't complete — drifts without formal closure → no reference case, no commercial proof point
**Block date:** Mar 31, 2027

### DoD-3: Product Documentation Living and Maintained (Feb 28, 2027)

**Gate:** All 3 flagship products have living documentation — roadmap, backlog, commercialisation docs, architecture diagrams — with a monthly update cadence and named documentation owners.

**Evidence:**
- [ ] VoronCitadel: roadmap, backlog, architecture diagram, commercialisation deck, claims validation report — all current (updated within 30 days)
- [ ] GovSec TIP: roadmap (Q3 2026–Q2 2027 delivered Aug 17, updated), backlog, architecture, integration diagram — all current
- [ ] chain:SENTRY: documentation status defined (Hadri-owned, Fuad-validated for security content)
- [ ] Documentation register exists with named owners and update dates
- [ ] Monthly documentation review running for 3+ consecutive months
- [ ] Claims validation process documented — Syahir-enabled for routine claims, Fuad for architectural claims
- [ ] AIP-20260829-001 AIP-03 closed: Syahir workstream aligned to strategic deliverables

**Failure mode:** Documentation exists but stale — last updated >60 days → institutional memory degrades → knowledge stays in Fuad's head
**Block date:** Feb 28, 2027

### DoD-4: GovSec TIP Q3-Q4 2026 Roadmap Items Delivered (Jan 31, 2027)

**Gate:** GovSec TIP roadmap Q3 2026 items (production hardening, executive visualisation, feed quality, identity/MFA) and Q4 2026 items (SIEM/ticketing, playbooks, exposure monitoring, RAG pipeline) delivered. At least 8 of 12 project cards across Q3-Q4 completed or on track.

**Evidence:**
- [ ] Q3 2026 project cards: production hardening ✅, executive visualisation ✅, feed quality ✅, identity/MFA ✅ (4 of 4)
- [ ] Q4 2026 project cards: ≥4 of 8 delivered or on track with evidence
- [ ] GovSec TIP deployed on Teras with documented integration (DEC-20260820-009)
- [ ] CSM integration deliverables evidenced (CMERP Suricata alerts, SiberSUITE telemetry)
- [ ] Defensia WAF evaluation completed (ACT-20260820-006, reassigned to Hadri)
- [ ] Product baseline updated to reflect Q3-Q4 changes

**Failure mode:** Roadmap items slip silently — no tracking, no escalation → roadmap becomes aspirational document
**Block date:** Jan 31, 2027

### DoD-5: Fuad Time Allocation Shifted to Architecture/Strategy (Jun 30, 2027)

**Gate:** Fuad's weekly time allocation is approximately 60% architecture/strategy, 30% technical validation, 10% hands-on development — reversed from the Aug 2026 baseline of ~70% hands-on. ≥2 team members can independently execute tasks Fuad used to do alone. Protected architecture time established (≥1 day/week, no interruptions).

**Evidence:**
- [ ] Time audit conducted (2-week sample, categorized: architecture/strategy, technical validation, hands-on development, coordination/admin)
- [ ] Architecture time = product architecture decisions, technical design, roadmap input, strategic alignment, RSWG/ITSS mapping
- [ ] Technical validation = code review, quality gates, POC validation, claims verification
- [ ] Hands-on = direct code commits, environment setup, debugging
- [ ] ≥2 team members independently executing tasks Fuad used to do alone (Syahir for QC/POC env, HoE for development, CSE for customer-facing)
- [ ] Fuad has ≥1 full day/week protected architecture time (no meetings, no operational interruptions)
- [ ] Fuad reports ≥3 days/week with ≥4 hours of focused architecture/strategy work

**Failure mode:** Fuad says "I'm delegating now" but time audit shows 50%+ hands-on → delegation is nominal, not structural
**Block date:** Jun 30, 2027

---

## 3. Success Conditions

| # | Condition | Why It Matters | How Engineered |
|---|-----------|---------------|----------------|
| 1 | HoE hired by Dec 31, 2026 | Single highest-leverage action — breaks the SPOF. Without engineering capacity, every other DoD is at risk | DAF decides hiring path by Sep 2 (AIP-04); post/shortlist/interview pipeline active by Sep 7 |
| 2 | Fuad actively delegates, not just assigns | Assignment without authority transfer = nominal delegation. HoE must own decisions, not just tasks | Fuad defines decision rights with HoE; DAF monitors delegation quality, not just quantity |
| 3 | Bursa POC NDA executed by Sep 4 | Gates document sharing → technical work → POC completion → reference case | DAF follows up with Azrul; NDA framework already sent (ACT-20260828-001) |
| 4 | Syahir workstream aligned to strategic deliverables | Syahir absorbs QC + POC env load from Fuad's critical paths — not just isolated tasks | AIP-03 updated: Fuad to review and align Syahir workstream by Sep 5 |
| 5 | Documentation is living, not static | Knowledge institutionalisation is the scaling mechanism. Stale docs = knowledge in Fuad's head | Monthly documentation review cadence; named owners; Ember monitors staleness |
| 6 | GovSec roadmap has delivery tracking, not just aspiration | Roadmap without tracking is a wish list. Card-level status prevents silent slippage | HoE owns roadmap delivery reporting; Fuad validates quality gates |
| 7 | Teras platform is stable for product deployment | All 3 products deploy ON Teras (DEC-20260820-009). Teras instability blocks all product progress | Farul owns Teras stability; Fuad owns product-side integration |
| 8 | Fuad has protected architecture time | Without protected time, operational urgency always wins — architecture is always deferred | ≥1 full day/week, calendar-enforced; DAF and HoE respect the boundary |
| 9 | Fuad's career direction aligns with this ESF | If Fuad prefers hands-on over leadership, the ESF fails. He must want to be a technical leader, not just be told to be one | DAF reviews this ESF before sharing with Fuad; Fuad consulted on career direction |
| 10 | Product claims are validated before commercial use | Unvalidated claims in customer-facing materials = credibility risk. Claims validation is a quality gate, not a nice-to-have | Syahir handles routine claims (trained); Fuad handles architectural claims; validation documented |

---

## 4. Failure Conditions

| # | Failure Condition | What It Looks Like | Root Cause |
|---|-------------------|--------------------|------------|
| 1 | HoE not hired by Dec 31 | Fuad still sole engineer across 3 products; SPOF risk persists | Hiring deprioritized; budget not approved; DAF doesn't decide hiring path |
| 2 | HoE hired but Fuad doesn't delegate | "It's faster if I do it" → HoE becomes assistant, not owner | Fuad's control habit; no delegation framework; no accountability for delegation rate |
| 3 | Bursa POC drifts without closure | POC runs but never formally completes; no reference case; no lessons learned | NDA slips; Azrul engagement stalls; technical work not scoped properly |
| 4 | Documentation exists but stale | Docs created in a burst, then abandoned; last updated >60 days | No cadence; no named owners; documentation not treated as product work |
| 5 | GovSec roadmap items slip silently | Q3-Q4 cards show "in progress" forever; no escalation | No card-level tracking; HoE not tracking delivery; Fuad too busy to chase |
| 6 | Fuad burns out | Quality drops; cadence breaks; deadlines missed; disengagement | No delegation; no protected time; 3 products × 0.3 FTE for 12 months |
| 7 | Syahir doesn't ramp up | QC gate fails at CyberDSA or post-CyberDSA; Fuad re-absorbs QC work | Ramp-up not tracked; no capability criteria; no interim checkpoints |
| 8 | Teras instability blocks deployments | Products can't deploy or update; POC environments fail | Teras not production-grade; Farul capacity constrained; integration not tested |
| 9 | Fuad leaves the practice | Technical knowledge vacuum — 2 products undocumented, no deputy | Burnout; career stagnation; better offer; lack of growth path |

---

## 5. Dependency Map

| Dependency | Type | Owner | Blocks | Status | Mitigation |
|-----------|------|-------|--------|--------|------------|
| HoE hire | Internal | DAF (authority), HR | DoD-1 (all delegation) | 🔴 NOT STARTED (active since Aug 20, 9 days no progress) | DAF decides hiring path by Sep 2 (AIP-04); contractor as fastest interim |
| CSE hire | Internal | DAF, HR | DoD-1 (customer-facing capacity) | 🔴 NOT STARTED | Engage by Oct 15 if HoE filled; contractor as interim |
| Bursa POC NDA | External | Azrul (CSM) | DoD-2 (POC execution) | 🟡 NDA framework sent Aug 28, due Sep 4 | DAF follows up; 4 IP provisions pending Azrul review |
| Syahir ramp-up | Internal | Fuad | DoD-3 (claims validation) + QC gate | 🟡 AIP-03 updated, due Sep 5 | Workstream alignment review; interim checkpoint Sep 10 |
| TBH-001 PM hire | Internal | DAF, HR | Coordination load off Fuad | 🟡 JD v2 committed, end-Sep activation | Interim: DAF carries PM burden |
| Teras platform stability | Internal | Farul | DoD-4 (GovSec deployment) | 🟡 Operational | Farul owns; Fuad owns product-side integration |
| DAF delegation willingness | Internal | DAF | DoD-1 (delegation environment) | 🟡 Improving (3/5 self-assessed) | Decision rights matrix; ESF-20260829-001 DoD-2 |
| Fuad delegation willingness | Internal | Fuad | DoD-1 (active delegation) | 🔴 UNKNOWN — not yet assessed | DAF reviews this ESF; Fuad consulted on career direction |
| Budget for engineering hires | Internal | Kenny / Management | DoD-1 (HoE + CSE salary) | 🟡 RM39,656/month total (HoE 18,888 + CSE 11,888 + Junior 8,888) | Minimum: HoE only (RM18,888/month); contractor as cost-effective interim |
| DAF ESF DoD-1 (portfolio register) | Internal | Ember + DAF | Coordination discipline | 🟡 Register exists, needs consolidation | ESF-20260829-001 DoD-1 due Sep 30 |
| CyberDSA 2026 execution | Internal | DAF, Hadri, Fuad | Market presence, product visibility | 🟡 T-30 gate chain Aug 31 → Sep 5 | 6-step sequential gate chain |
| Defensia WAF evaluation | Internal | Hadri (reassigned) | DoD-4 (production hardening) | 🟡 Due Sep 10 | ACT-20260820-006 reassigned from DAF |

---

## 6. Critical Path

```
Sep 4           Sep 30            Dec 31              Jan 31             Feb 28             Mar 31             Jun 30
NDA             Portfolio         Engineering         GovSec Q3-Q4        Documentation       Bursa POC           Fuad Time
Signed          Register          Team Operational     Roadmap Delivered   Living+Maintained   Reference Case      60/30/10
    ↓               ↓                ↓                  ↓                  ↓                  ↓                  ↓
NDA → POC     DoD-1 (DAF)     DoD-1 ──────────→ DoD-4 ──────────→ DoD-3 ──────────→ DoD-2 ──────────→ DoD-5
execution       (coord)        (Team)             (GovSec)            (Docs)              (POC)              (Time)
```

**Critical path dependencies:**
- NDA → POC technical work → POC completion → Reference case (DoD-2)
- HoE hire → Engineering team → Delegation → Documentation discipline (DoD-3) + Roadmap delivery (DoD-4)
- Engineering team → POC scaling → POC completion → Time freed for architecture (DoD-5)

**Non-critical path (parallel):**
- Syahir ramp-up (runs Sep–Oct, feeds DoD-3 claims validation + CyberDSA QC)
- CyberDSA 2026 (runs Oct, feeds market presence but doesn't block DoD gates directly)
- chain:SENTRY Phase 0 (Hadri-owned, runs independently of Fuad's DoD gates)
- MCMC AI capability workshop (runs ~Sep 18, feeds Teras/GovSec but doesn't block)

---

## 7. Ownership

| Role | Owner | Responsibility in Fuad's ESF |
|------|-------|------------------------------|
| Technical authority | Fuad | Product architecture, technical quality gates, POC validation, claims verification (architectural), roadmap input |
| Strategic authority | DAF | Direction, commercial negotiations, portfolio gating, hiring decisions, stakeholder relationships |
| Framework + tracking | Ember | §9 DoD tracking, Cognitive Loop monitoring, delegation rate metrics, documentation staleness alerts |
| Engineering execution | HoE (when hired) | Day-to-day development, code review, deployment, technical documentation, POC environment management |
| Customer-facing engineering | CSE (when hired) | Customer onboarding, POC support, technical support, environment troubleshooting |
| QC + POC env | Syahir | Claims validation (routine), POC environment setup, demo support, CyberDSA QC gate |
| Blockchain/COO | Hadri | chain:SENTRY execution, operational co-pilot, T-30 CyberDSA gate chain, Defensia WAF evaluation |
| Org CTO | Farul | Teras platform, infrastructure decisions, cross-practice technical alignment |
| PM coordination | TBH-001 (or interim) | Project plan, deliverable tracking, weekly status, gate tracking, document TAT |

---

## 8. Resources

| Resource | Type | Availability | Constraint |
|----------|------|-------------|------------|
| Fuad's time | Human | Part-time across 3 products | ~0.3 FTE allocable; currently ~70% hands-on; target 60% architecture/strategy |
| HoE | Human | NOT FILLED | RM18,888/month; single highest-leverage gap; gates DoD-1 |
| CSE | Human | NOT FILLED | RM11,888/month; gates customer-facing capacity |
| Junior backend | Human | NOT FILLED | RM8,888/month; supports development capacity |
| Syahir | Human | Available, ramping up | POC Engineer + QC Engineer; capability level not yet assessed |
| DAF's time | Human | ~50-60 hrs/week | Hiring decisions, commercial authority, stakeholder relationships |
| Hadri | Human | Full-time | COO + blockchain lead — dual role creates conflicts |
| Farul | Human | Full-time | Org CTO; Teras platform owner |
| Ember (agent) | AI system | 24/7 | DoD tracking, Cognitive Loop, documentation staleness monitoring |
| Teras AI platform | System | Operational | Infrastructure layer for all products (DEC-20260820-009) |
| VoronCitadel | Product | Production-deployed, live | v2.0; most commercially mature; Bursa POC pending NDA |
| GovSec TIP | Product | Roadmap delivered | Q3-Q4 2026 items to execute; 12 project cards |
| chain:SENTRY | Product | 69% implemented | Hadri-owned; Fuad validates security content |
| Budget (engineering hires) | Financial | Pending | RM39,656/month total; minimum RM18,888 (HoE only) |
| Strategic-cognitiveos repo | Git | GitHub private | Active, daily commits; profile + AIP + ESF |

---

## 9. Checkpoints

| CP | Date | Gate | Owner | Evidence Required |
|----|------|------|-------|-------------------|
| CP1 | Sep 5, 2026 | AIP-03: Syahir workstream reviewed + aligned | Fuad | Workstream-to-deliverable mapping; capability assessment |
| CP2 | Sep 10, 2026 | AIP-03 checkpoint: Syahir interim capability | Fuad | Ready / partially ready / not ready |
| CP3 | Oct 15, 2026 | HoE hired OR interim contractor engaged | DAF | Signed offer or contractor engagement confirmation |
| CP4 | Dec 31, 2026 | DoD-1: Engineering team operational + delegation ≥40% | Fuad + HoE | Org chart; task assignment register; code review log; commit rate delta |
| CP5 | Jan 31, 2027 | DoD-4: GovSec Q3-Q4 roadmap items delivered | Fuad + HoE | 8 of 12 Q3-Q4 project cards completed with evidence |
| CP6 | Feb 28, 2027 | DoD-3: Product documentation living and maintained | Fuad + Ember | Documentation register; 3+ monthly reviews; named owners; update dates |
| CP7 | Mar 31, 2027 | DoD-2: Bursa POC completed as reference case | Fuad + DAF | POC completion report; reference case doc; RSWG/ITSS alignment |
| CP8 | Jun 30, 2027 | DoD-5: Fuad time allocation 60/30/10 | Fuad | 2-week time audit; delegation evidence; protected architecture time |

---

## 10. Leading Indicators (measurable weekly/monthly)

| Metric | Target | Threshold | Red Flag | Cadence | Measurement |
|--------|--------|-----------|----------|---------|-------------|
| HoE hiring pipeline status | Active candidates by Sep 14 | No candidates for 2 weeks | No candidates for 4 weeks | Bi-weekly | HR update or DAF confirmation |
| Fuad delegation rate | ≥40% of technical tasks assigned to non-Fuad by Dec 31 | <20% by Nov 15 | <10% by Dec 1 | Weekly | Task assignment register analysis |
| Fuad direct code commit rate | Decreasing from Aug 2026 baseline | Flat for 4 weeks | Increasing | Weekly | Git log analysis (if repo metrics available) |
| Syahir independent task completion | ≥3 tasks/week completed without Fuad intervention by Oct 15 | <1/week by Oct 1 | 0 for 2 weeks | Weekly | Task completion log |
| Documentation freshness | All docs updated within 30 days by Feb 28 | >45 days stale | >60 days stale | Monthly | Documentation register update dates |
| POC milestone progress | On track per Bursa POC timeline | 1 milestone slipping | 2+ milestones slipping | Bi-weekly | POC milestone tracker |
| Engineering cadence (code reviews) | ≥2 reviews/week by Nov 15 | <1/week | 0 for 2 weeks | Weekly | Code review log |
| Protected architecture time | ≥1 full day/week by Jan 2027 | <4 hours/week | 0 hours for 2 weeks | Weekly | Fuad calendar audit |
| GovSec roadmap card status | Q3 cards on track by Oct 31 | 1 card slipping | 2+ cards slipping | Monthly | Roadmap card tracker |
| Claims validation throughput | Routine claims validated by Syahir; architectural by Fuad | Backlog growing | Backlog >10 unvalidated claims | Bi-weekly | Claims validation register |

---

## 11. Lagging Indicators (measurable quarterly)

| Metric | Target | Threshold | Red Flag | Cadence | Measurement |
|--------|--------|-----------|----------|---------|-------------|
| Engineering team headcount | 3 (HoE + CSE + junior) by Q2 2027 | 1 (HoE only) by Q4 2026 | 0 by Q4 2026 | Quarterly | Headcount confirmation |
| Fuad time allocation (architecture vs hands-on) | 60/30/10 by Q2 2027 | 40/40/20 by Q4 2026 | Still 70% hands-on by Q1 2027 | Quarterly | 2-week time audit sample |
| VoronCitadel POC completion | Bursa POC completed by Q1 2027 | POC active by Q4 2026 | No POC by Q1 2027 | Quarterly | POC completion report |
| GovSec roadmap delivery | 8 of 12 Q3-Q4 cards by Q1 2027 | 6 of 12 by Q4 2026 | <4 of 12 by Q1 2027 | Quarterly | Roadmap card count |
| Product documentation coverage | 3 products × 5 doc types by Q1 2027 | 2 products by Q4 2026 | 1 product by Q1 2027 | Quarterly | Documentation register count |
| Team retention | 100% of key technical roles (Fuad, HoE, Syahir) | 1 departure | 2+ departures | Quarterly | HR confirmation |
| Fuad self-assessment: delegation capability | 4/5 by Q3 2027 (from unassessed baseline) | 3/5 by Q1 2027 | Still <3/5 by Q2 2027 | Quarterly | Fuad self-assessment |
| Fuad self-assessment: architecture leadership | 4/5 by Q3 2027 | 3/5 by Q1 2027 | <3/5 by Q2 2027 | Quarterly | Fuad self-assessment |
| Delegation sustainability | Fuad reports workload is sustainable | Neutral | Reports overload | Quarterly | Fuad check-in |
| §9 DoD items completed with evidence | ≥80% by Q3 2027 | ≥50% by Q1 2027 | <30% by Q1 2027 | Quarterly | ESF DoD item count |

---

## 12. Verification

| DoD | Verification Method | Verified By | Evidence Storage |
|-----|-------------------|-------------|------------------|
| DoD-1 (Engineering Team) | Org chart + task assignment register + code review log + commit rate delta | DAF + Ember | Git commit in strategic-cognitiveos; HR records |
| DoD-2 (Bursa POC) | POC completion report signed by Bursa + reference case doc + RSWG/ITSS alignment evidence | DAF + Fuad | POC repo + strategic-cognitiveos |
| DoD-3 (Documentation) | Documentation register with update dates + 3+ monthly review records + named owners | Ember | Documentation register in repo |
| DoD-4 (GovSec Roadmap) | Roadmap card status tracker with ≥8 of 12 Q3-Q4 cards completed | Fuad + HoE | Roadmap tracker in repo |
| DoD-5 (Time Allocation) | 2-week time audit with categorized time blocks + delegation evidence + protected time confirmation | Fuad (self-report) + DAF (validation) + Ember (analysis) | Time audit doc + comparison with Aug 2026 baseline |

**Rule:** No DoD item is marked complete without evidence. Evidence must be retrievable. Ember verifies and flags false closures.

---

## 13. Risk Matrix with Triggers and Responses

| Risk | P | I | Trigger | Response | Owner |
|------|---|---|---------|----------|-------|
| HoE not hired by Dec 31 | H | H | No offer extended by Nov 15 | Engage contractor as interim engineering capacity; redefine hiring as 2027 Q1 priority | DAF |
| Fuad doesn't delegate despite HoE in seat | M | H | HoE hired but Fuad's commit rate unchanged after 4 weeks | DAF intervention; delegation framework with decision rights; Fuad-HoE working agreement documented | DAF + Fuad |
| Bursa POC stalls (NDA or technical) | M | H | NDA not signed by Sep 10 OR POC technical work not started by Sep 14 | DAF escalates with Azrul; assess timeline adjustment; consider alternative reference account | DAF |
| Fuad burns out before delegation materialises | H | C | Missed deadlines; quality drops; disengagement signals | Emergency re-prioritisation: 1 product only (VoronCitadel); defer GovSec + chain:SENTRY to Q1 2027 | DAF + Kenny |
| Syahir doesn't ramp up sufficiently | M | M | Sep 10 checkpoint shows "not ready" | Reduced QC scope; Fuad + DAF joint review as fallback; accept CyberDSA with limited QC | DAF + Fuad |
| Teras platform instability blocks deployment | M | H | Products fail to deploy or POC environments crash | Farul priority on Teras stability; alternative deployment path (standalone Docker) | Farul |
| Fuad leaves the practice | L | C | Career conversation signals dissatisfaction or external offer | Retention conversation; career growth path; compensation review; ensure knowledge is documented | DAF |
| Documentation drive abandoned | H | M | No documentation updates for 60+ days | Ember auto-flags staleness; DAF enforces monthly review; tie documentation to product release cycle | Ember + DAF |
| GovSec roadmap items slip silently | M | H | No card status updates for 4+ weeks | HoE owns weekly card status report; Fuad validates; Ember flags in Cognitive Loop | Fuad + HoE |
| Bursa POC completes but no reference case created | M | M | POC ends but no reference document, no lessons learned | DAF + Fuad debrief within 2 weeks of POC completion; reference case is a gate, not an afterthought | DAF + Fuad |
| HoE hired but wrong fit | M | M | HoE can't execute at required technical level after 60 days | Probationary review at 60 days; backup plan (contractor or senior developer); re-hire if needed | DAF + Fuad |
| Budget not approved for engineering hires | L | H | Management paper rejected | Minimum viable: HoE only (RM18,888/month); contractor as cost-effective interim; defer CSE + junior to Q2 2027 | DAF + Kenny |

---

## 14. Engineered Success Score (Self-Assessment)

| Dimension | Score (1-10) | Basis |
|-----------|:---:|-------|
| Objective clarity | 9 | Clear, specific, measurable 12-month objective with 5 DoD gates aligned to product and role outcomes |
| Requirements completeness | 9 | Full 12-element framework; dependencies, risks, indicators all mapped; product-specific evidence requirements |
| Dependency mapping | 7 | 12 dependencies identified with mitigation; HoE and NDA are critical-path risks; Fuad delegation willingness is unknown |
| Stakeholder engagement | 5 | DAF engaged; Fuad NOT yet consulted on career direction; HoE not hired; team capacity risk |
| Resource availability | 5 | Fuad at 0.3 FTE; HoE/CSE not hired; Syahir capability unassessed; budget pending |
| Execution plan quality | 8 | 5 DoD gates with clear checkpoints, evidence requirements, and failure modes |
| Evidence infrastructure | 7 | CognitiveOS repo, profile, AIP exist; code review log and task assignment register need to be created |
| Risk management | 8 | 12 risks identified with triggers, responses, and owners |
| Adoption readiness | 4 | Fuad's willingness to delegate is UNKNOWN; career direction not confirmed; this is the core risk |
| Outcome measurement | 9 | Leading + lagging indicators with thresholds and red flags; time audit methodology defined |
| **Total** | **71/100** | **Conditional readiness — proceed with DoD-1 (HoE hire) as highest leverage, lowest risk** |

**Interpretation:** 65-74 = Conditional readiness. The plan is sound but depends on two unknowns: (1) HoE hiring timeline (DAF-controlled) and (2) Fuad's willingness to transition from hands-on to architecture (not yet assessed). The plan is designed so DoD-1 can proceed independently — HoE hire doesn't require Fuad's behavioural change, it creates the conditions for it.

**Critical unknown:** Fuad's adoption readiness (4/10) is the lowest-scoring dimension. This ESF assumes Fuad wants to become a technical leader who scales through delegation. If he prefers to remain a hands-on architect, the ESF needs revision. **DAF must review this ESF and consult Fuad before activation.**

---

## 15. Relationship to Existing Frameworks

| Framework | Role in This ESF |
|-----------|-----------------|
| **DAF ESF (ESF-20260829-001)** | Complementary. DAF's DoD-2 (non-DAF owners) depends on Fuad's DoD-1 (engineering team). DAF's DoD-1 (portfolio register) feeds Fuad's coordination. DAF's DoD-5 (calendar shift) is enabled by Fuad's DoD-5 (time shift). |
| **CognitiveOS Prime Doctrine** | §9 provides the framework. §41 (`ENGINEER SUCCESS`) provides the command structure. Prime Directive includes "manual→orchestrated" — Fuad's transition from manual executor to technical orchestrator. |
| **ADEP-001** | Provides 4-state maturity model. This ESF targets State 4 (OPERATIONALISED) for Fuad's technical operating model. Diligence level: D3 (Strategic). |
| **AIP-20260829-001 (Fuad Capacity Architecture)** | Near-term (6-week) capacity fix. This ESF is the 12-month structural architecture. AIP items feed into ESF DoD gates: AIP-03 (Syahir) → DoD-3; AIP-04 (HoE) → DoD-1; AIP-06 (post-T-30 capacity plan) → DoD-5. |
| **FUAD-COMPREHENSIVE-PROFILE-20260829** | Source profile. All claims in this ESF trace to records cited in the profile. |
| **CVS Master Framework** | All claims are T3 [ASSESSMENT] based on L2 evidence (CognitiveOS records, profile, AIP). Confidence: 7/10 (Rule 6 cap). AI cannot self-certify T1. |
| **TBH Registry** | HoE is in the TBH Registry (ACT-20260820-007). TBH-001 (PM) is a related but separate hire. Both unblock Fuad's ESF. |
| **DEC-20260820-009 (Teras)** | All products deploy ON Teras. Teras stability is a dependency for DoD-4. |
| **DEC-20260818-007 (Syahir)** | Syahir ramp-up is owned by Fuad. Gates DoD-3 (claims validation) and CyberDSA QC. |
| **RSWG Paper + ITSS Directive 5.05-001** | Regulatory tailwind for DoD-2 (Bursa POC). RSWG §2.6 = VoronCitadel TPRM module. ITSS §10 = supplier management. |

---

## 16. What I Don't Know (Honest Gaps)

Per ADEP-001 §7: never present assumptions as facts.

1. **I don't know if Fuad wants to transition to a technical leadership role.** This ESF assumes he does. He may prefer to remain a hands-on architect. DAF must consult him before this ESF is activated.
2. **I don't know Fuad's current actual time allocation.** The 70% hands-on baseline is an assessment from the Cognitive Loop, not a measured audit. A 2-week time audit would establish the real baseline.
3. **I don't know if Fuad will delegate when HoE is in seat.** Delegation willingness is unassessed. Behaviour under pressure may differ from stated preference.
4. **I don't know the HoE hiring timeline.** DAF hasn't decided the hiring path (external/contractor/secondment). AIP-04 is due Sep 2.
5. **I don't know if budget will be approved for 3 engineering hires.** RM39,656/month total. Minimum viable is HoE only (RM18,888/month). Budget paper pending.
6. **I don't know Syahir's current capability level.** AIP-03 (due Sep 5) will surface this, but as of Aug 29, no capability assessment exists.
7. **I don't know if the Bursa POC will complete on the 4-month timeline.** NDA is pending (due Sep 4). Technical work hasn't started. Timeline may compress.
8. **I don't know if Teras is production-stable for 3 products.** It's operational, but production-grade stability for 3 concurrent product deployments is unverified.
9. **I don't know Fuad's career aspirations beyond Aras.** He's ISC2 Malaysia Chapter Academic Director. His career trajectory may include academic/research direction, not just technical leadership.
10. **I don't know if GovSec roadmap Q3-Q4 items are still the right items.** The roadmap was delivered Aug 17. Priorities may have shifted since then.

These gaps will be closed through: (1) DAF reviews and consults Fuad, (2) AIP-03 Syahir assessment Sep 5, (3) AIP-04 HoE hiring path Sep 2, (4) NDA outcome Sep 4, (5) 2-week time audit when Fuad is ready.

---

## 17. Fuad Action List

Actions requiring Fuad personally, ranked by leverage:

| # | Action | Deadline | Unblocks |
|---|--------|----------|----------|
| 1 | Review Syahir operational workstream — align to strategic deliverables (AIP-03) | Sep 5 | DoD-3 (claims validation + QC) |
| 2 | Close engineering comments — Gate 1 (AIP-01) | Aug 31 | GovSec gate chain → T-30 closure |
| 3 | Confirm document technically complete — Gate 3 | Sep 2 | GovSec gate chain → T-30 closure |
| 4 | Review this ESF and provide input on career direction | Sep 15 | ESF activation |
| 5 | Define delegation framework with HoE when hired — decision rights, code review ownership, deployment authority | Jan 15, 2027 | DoD-1 (active delegation) |
| 6 | Conduct 2-week time audit (categorize: architecture, technical validation, hands-on, coordination) | Mar 15, 2027 | DoD-5 baseline |
| 7 | Define product architecture vision for VoronCitadel post-POC (what does v3.0 look like?) | Feb 28, 2027 | DoD-2 (post-POC roadmap) |
| 8 | Define GovSec TIP 2027 roadmap (Q1-Q2) — update from Aug 17 version | Jan 15, 2027 | DoD-4 (roadmap continuation) |
| 9 | Establish monthly documentation review cadence — named owners per product | Nov 30, 2026 | DoD-3 (documentation living) |
| 10 | Onboard HoE to product architecture — 2-week technical handover plan when hired | Jan 31, 2027 | DoD-1 (delegation start) |

---

## 18. DAF Action List (Supporting Fuad's ESF)

Actions DAF must take to enable this ESF:

| # | Action | Deadline | Unblocks |
|---|--------|----------|----------|
| 1 | Decide HoE hiring path (external/contractor/secondment) | Sep 2 | DoD-1 (all delegation) |
| 2 | Review this ESF before sharing with Fuad | Sep 7 | ESF activation |
| 3 | Consult Fuad on career direction — technical leadership vs hands-on architect | Sep 15 | ESF adoption readiness |
| 4 | Approve engineering hire budget (or minimum: HoE only) | Oct 1 | DoD-1 (hiring) |
| 5 | Follow up with Azrul on NDA (4 IP provisions) | Sep 4 | DoD-2 (POC execution) |
| 6 | Define decision rights matrix — what Fuad decides vs what HoE decides | Dec 15 | DoD-1 (delegation framework) |

---

## ESF Status Summary

| DoD | Description | Target Date | Status | Block Risk |
|-----|-------------|-------------|--------|------------|
| DoD-1 | Engineering team operational + ≥40% delegation | Dec 31, 2026 | PENDING | HIGH — HoE not hired, Fuad delegation willingness unknown |
| DoD-2 | VoronCitadel Bursa POC completed as reference case | Mar 31, 2027 | PENDING | MEDIUM — NDA pending (Sep 4), technical work not started |
| DoD-3 | Product documentation living and maintained | Feb 28, 2027 | PENDING | MEDIUM — no cadence established, no named owners |
| DoD-4 | GovSec TIP Q3-Q4 roadmap items delivered | Jan 31, 2027 | PENDING | MEDIUM — HoE needed for execution capacity |
| DoD-5 | Fuad time allocation 60/30/10 (architecture/validation/hands-on) | Jun 30, 2027 | PENDING | HIGH — behavioural change, depends on DoD-1 through DoD-4 |

**Overall probability of success:** MEDIUM (50-60%)

- DoD-1 probability: MEDIUM (50%) — HoE hiring is DAF-controlled, not Fuad-controlled. Fuad delegation willingness unknown.
- DoD-2 probability: MEDIUM (60%) — NDA is the gate. If signed by Sep 4, POC proceeds. Technical capability exists.
- DoD-3 probability: MEDIUM (55%) — requires cadence discipline + named owners + Syahir enablement. Process risk, not capability risk.
- DoD-4 probability: MEDIUM (55%) — HoE needed for execution. Roadmap exists but card-level tracking not established.
- DoD-5 probability: LOW-MEDIUM (40%) — behavioural change is hardest to engineer. Depends on DoD-1 through DoD-4 succeeding first. Fuad's willingness to shift from hands-on is the core variable.

**The framework's job:** Move the 50% engineering team probability toward 60% by engineering the preconditions (HoE hire, delegation framework, documentation cadence), not hoping for behavioural change.

**The critical unknown:** Fuad's adoption readiness is the lowest-scoring dimension (4/10). This ESF cannot succeed without his buy-in. DAF must review and consult Fuad before activation.

---

*This document is the `ENGINEER SUCCESS` output per CognitiveOS Prime Doctrine §9 and §41. It makes execution immediately possible. Register as ES-009 in the §9 DoD Registry.*

*All claims are T3 [ASSESSMENT] based on L2 evidence (CognitiveOS records, Fuad comprehensive profile, AIP-20260829-001). Confidence: 7/10 (CVS Rule 6 cap — AI cannot self-certify T1). Human review required for T1 upgrade.*
