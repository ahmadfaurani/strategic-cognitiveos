# Risk Index

All identified risks, grouped by status.

## Active

| ID | Risk | Category | Initiative | Likelihood | Impact | Priority | Status |
|----|------|----------|-----------|------------|--------|----------|--------|
| RSK-20260802-004 | Stakeholder commitments exceeding delivery capacity | stakeholder-alignment | PRJ-20260725-C001 | Medium | High | High | Active |
| RSK-20260802-007 | Strategic documents not converted to funded execution | commercial-viability | PRJ-20260725-E001 | Medium | High | High | Active |
| RSK-20260802-010 | Ambiguous authority in collaborative partnerships | stakeholder-alignment | PRJ-20260725-C001 | Medium | Medium | Medium | Active |
| RSK-20260803-001 | NDA scope language may not fully capture Aras technology scope | governance | INIT-20260803-001 | Medium | High | High | Active |
| RSK-20260810-001 | Hadi onboarding & GovSec Product Management dependency risk for CyberDSA launch | resource-constraint | INIT-20260810-003 | Medium | Critical | Critical | Active |
| RSK-20260810-002 | GovSec TIP Security Hardening Gap — cybersecurity product without security validation | security | INIT-20260810-003 | High | Critical | Critical | Active |
| RSK-20260810-003 | CyberDSA Commercial Readiness Gap — no pricing, packaging, or post-demo conversion path | commercial-viability | INIT-20260810-003 | High | High | High | Active |
| RSK-20260811-001 | Productisation Documentation Effort vs CyberDSA Delivery Capacity Contention | resource-constraint | INIT-20260811-001 | Medium | High | High | Mitigated |
| RSK-20260813-001 | PERJASA workshop date confirmation delay | timeline | INIT-20260813-001 | Medium | High | High | Active |
| RSK-20260813-002 | GTM Programme Management Gap — MQL Pipeline Without Joint Coordination Mechanism | execution-coordination | INIT-20260804-001 | High | High | High | Active |
| RSK-20260815-001 | Absence of designated PIC for CSM-Aras communication | communication-coordination | INIT-20260804-001 | Medium | Medium | Medium | Mitigating |
| RSK-20260815-002 | MCMC funding approval risk — RM5M pricing sensitivity and budget cycle alignment | commercial-viability | INIT-20260803-002 | Medium | High | High | Identified |
| RSK-20260815-003 | Development freeze may delay product improvements needed for CyberDSA demo readiness | timing | INIT-20260811-001 | Medium | High | High | Identified |
| RSK-20260816-001 | CyberDSA 2026 Silver Sponsorship budget approval pending (RM50K, dual approval) | commercial-viability | INIT-20260813-006 | Low | Medium | Medium | Identified |
| RSK-20260816-002 | Email claim 'commercially viable product' unsupported by current product readiness state | commercial-viability | INIT-20260811-001 | High | Medium | Medium | Identified |
| RSK-20260816-003 | 'Malaysia's First' media claim unsupported — reputational exposure | reputational | INIT-20260813-006 | Medium | High | High | Mitigating — DOC-20260818-002 §9 provides messaging guardrails; ACT-20260818-004 enforces |
| RSK-20260819-001 | Personality-dependent CSM relationship — auto-aligning contacts before requirement definition | strategic | INIT-20260813-005 | Medium | High | Medium | Active |

## Mitigating

| ID | Risk | Mitigation Strategy | Mitigation Owner | Target Resolution |
|----|------|--------------------|-----------------|------------------|
| RSK-20260802-001 | Excessive parallel workstreams exceeding execution capacity | Dev freeze reduces active front count; portfolio tier enforcement; Hadri absorbing technical delivery; Hadi onboarding pending | faurani-jaafar | 2026-10-31 (post-CyberDSA review) |
| RSK-20260802-002 | Personal role overload — DAF as single point of failure | Hadri absorbs technical architecture; CognitiveOS governance reduces admin overhead; Hadi onboarding will reduce PM load; delegation still incomplete | faurani-jaafar | 2026-10-31 (post-CyberDSA review) |
| RSK-20260802-003 | Product maturity below strategic narrative | Dev freeze forces hardening; product readiness index enforces gating; GovSec TIP prototype → demo-ready; other products still at concept | faurani-jaafar | 2026-10-01 (CyberDSA launch) |
| RSK-20260802-005 | Inconsistent follow-through on strategic initiatives | CognitiveOS intake SOP enforced; action items have owners/deadlines; weekly review cadence defined; delegation still incomplete | faurani-jaafar | 2026-09-30 |
| RSK-20260802-006 | Technical leader dependency — Fuad concentration (Hadri mitigating) | Hadri absorbing GovSec architecture; handover documentation in progress (ACT-20260810-005); non-GovSec products still Fuad-dependent | faurani-jaafar | 2026-08-24 (handover completion) |
| RSK-20260802-008 | Opportunity dilution — too many initiatives at concept stage | Portfolio tier framework enforced; dev freeze concentrates effort; Tier 2/3 maintained as intelligence only | faurani-jaafar | 2026-10-31 |
| RSK-20260802-009 | Cognitive switching and decision fatigue | Dev freeze narrows focus to 5 priorities; Hadri absorbs technical context; CognitiveOS reduces admin overhead | faurani-jaafar | 2026-10-01 |
| RSK-20260804-001 | Delivery capacity/resource contention (4 parallel CSM tracks) | Dev freeze + Hadri + CSM track owners assigned; still 4 parallel tracks but structured | faurani-jaafar | 2026-10-01 |
| RSK-20260804-002 | Senior GovSec resource hiring delay (Partially Mitigated by Hadri) | Hadri mitigates technical dimension; Hadi onboarding (RSK-20260810-001) covers PM dimension; intern as interim | faurani-jaafar | 2026-08-31 (Hadi onboarding) |
| RSK-20260804-003 | CyberDSA October 2026 Launch Milestone — Delivery Timeline Risk | Dev freeze + 5-priority framework + Hadri handover + INIT-20260810-003; timeline still tight (~8 weeks) | faurani-jaafar | 2026-10-01 (launch date) |

## Monitoring

| ID | Risk | Trigger Conditions | Next Review |
|----|------|-------------------|------------|
| RSK-20260802-001 | >3 initiatives needing DAF direct intervention; stakeholder meetings without prep time; quality degradation; >48h response delays | Weekly executive review |
| RSK-20260802-002 | DAF unavailable >3 working days; commitments missed; no deputy available | Weekly executive review |
| RSK-20260802-003 | Stakeholder requests demo of concept product; external timeline commitments without delivery owner; product fails during evaluation | Monthly portfolio review |
| RSK-20260802-004 | >3 active commitments without delivery timelines; stakeholder follows up on unowned commitment; team capacity overload | Weekly executive review |
| RSK-20260802-005 | Initiative no update >14 days; action items without owner; weekly review missed 2 weeks | Weekly executive review |
| RSK-20260802-006 | Fuad unavailable >1 week; technical questions unanswerable by others; roadmap blocked pending Fuad | Monthly portfolio review |
| RSK-20260802-007 | Strategic document >90 days without conversion target; pilot completed without contract proposal; engagement without commercial next step | Monthly pipeline review |
| RSK-20260802-008 | >3 Tier 1 initiatives active; Tier 2 consuming delivery resources; no readiness gate advance in 30 days | Monthly portfolio review |
| RSK-20260802-009 | DAF reports feeling scattered; rushed thinking in documents; >3 workstream topics in one day | Weekly executive review |
| RSK-20260802-010 | Partnership meeting ends without clear owner; both sides waiting; decision reversed by wrong approver | Monthly partnership review |
| RSK-20260810-001 | Hadi not onboarded by 2026-08-24; no confirmed start date by 2026-08-17 | Weekly (Aug) |
| RSK-20260810-002 | Security assessment not scheduled by 2026-08-31; vulnerability discovered during hardening; PDPA feature failure | Bi-weekly (Aug–Sep) |
| RSK-20260810-003 | No commercial model defined by 2026-09-15; CSM joint proposition not discussed; no post-demo conversion path by Sep 30 | Weekly (Sept) |

## Realised

| ID | Risk | Initiative | Impact Assessment | Response |
|----|------|-----------|-------------------|----------|
| — | *None realised* | — | — | — |

---

## Risk Relationships

| Link | Relationship | Notes |
|------|-------------|-------|
| RSK-002-001 → RSK-002-002 | Compounding | Overloaded workstreams → DAF overload |
| RSK-002-001 → RSK-002-009 | Compounding | Overloaded workstreams → cognitive switching |
| RSK-002-002 → RSK-002-006 | Parallel | DAF overload + Fuad concentration = dual key-person dependency |
| RSK-002-003 → RSK-002-007 | Compounding | Immature products can't convert to funded execution |
| RSK-04-001 → RSK-04-003 | Causal | Delivery capacity contention → timeline risk |
| RSK-04-002 → RSK-10-001 | Instantiation | Senior GovSec resource gap → Hadi onboarding (PM dimension) |
| RSK-04-002 → RSK-002-006 | Related | Senior resource gap + Fuad concentration = technical delivery risk |
| RSK-10-002 → RSK-10-003 | Compounding | Security gap + commercial gap = launch credibility risk |
| RSK-10-001 → RSK-10-002 | Compounding | No PM → no one prioritises security hardening |
| RSK-10-001 → RSK-10-003 | Compounding | No PM → no one owns commercial model |

---

## Risk Register Maintenance

- **Created:** 2026-08-02 (10 initial risks from portfolio assessment)
- **Last Review:** 2026-08-10 (full register refresh — status updates, 2 new risks added, relationships mapped)
- **Next Review:** 2026-08-17 (weekly, aligned with ACT-20260810-007 deadline)
- **Review Cadence:** Weekly during CyberDSA runway (Aug–Oct 2026), monthly thereafter

---

_Updated 2026-08-10: Full register refresh. 10 Aug 2 risks status-updated (Identified → Mitigating/Active). RSK-04-002 linked to RSK-10-001 (Hadi = senior GovSec resource). 2 new risks added: RSK-20260810-002 (security hardening gap), RSK-20260810-003 (commercial readiness gap). Risk relationships mapped. Maintenance cadence established._
