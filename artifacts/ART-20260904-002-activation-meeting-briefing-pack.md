---
id: ART-20260904-002
record_type: artifact
title: "Activation Meeting Briefing Pack — Sep 4 2026 (Full Detail)"
created_at: 2026-09-04T05:09:00+00:00
updated_at: 2026-09-04T05:09:00+00:00
owner: faurani-jaafar
status: active
sensitivity: confidential
lifecycle_state: canonical
tags:
  - domain/governance
  - domain/organisational-capability
  - domain/strategic
  - domain/cybersecurity-productisation
  - domain/commercial-development
  - domain/stakeholder-engagement
  - artifact/brief
  - lifecycle/canonical
source:
  type: cognitive-loop
  reference: "INT-20260904-002, INT-20260904-003, INT-20260904-004, INT-20260904-005, INT-20260904-006"
related_records:
  - INT-20260904-002
  - INT-20260904-003
  - INT-20260904-004
  - INT-20260904-005
  - INT-20260904-006
  - ART-20260904-001
---

# Activation Meeting Briefing Pack — Sep 4, 2026

**Full Detail Edition** — prepared from Discovery Directives A–D + Cognitive Loop INT-20260904-006
**Meeting purpose:** Convert discovery findings into assigned, deadline-gated actions
**Time constraint:** CyberDSA Oct 10 (T-36). QC deadline Sep 28. C1 credential rotation 16 days overdue.

---

# TOPIC 1: SYAHIR — Priority Sequencing & C1 Execution

## 1.1 Complete Assignment Inventory (19 Items in CognitiveOS)

Syahir has **4 active decisions** assigning work, plus **3 active risks** where he is the owner, plus references in **12 other records**. Total: 19 CognitiveOS items reference Syahir.

### Active Decisions (4)

| # | Decision ID | Title | Date | Status | Deadline |
|---|------------|-------|------|--------|----------|
| 1 | DEC-20260818-007 | POC Engineer Role Delegated to Syahir — No External Hire | Aug 18 | Active | Ongoing |
| 2 | DEC-20260818-009 | Claims QC Deadline Set to T-7 Before CyberDSA (Sep 28) | Aug 18 | Active | Sep 28 |
| 3 | DEC-20260829-004 | chain:SENTRY Engineering Reassigned to Syahir — Hadri Retains Roadmap | Aug 29 | Active | Phase 0 kill date Sep 15 |
| 4 | DEC-20260904-001 | C1 Credential Rotation — Delegated to Syahir via Hadri | Sep 4 | Active | IMMEDIATE (16+ days overdue) |

### Active Actions (2)

| # | Action ID | Title | Status | Deadline | Completion Evidence |
|---|-----------|-------|--------|----------|-------------------|
| 1 | ACT-20260904-001 | Syahir to execute C1 credential rotation | NOT STARTED | Immediate | 4 changed fingerprints in masked key-health output; old values rejected by providers; deployment running with new credentials |
| 2 | ACT-20260820-010 | Rotate four supplier credentials — revoke and reissue at provider | OVERDUE | Phase 0 Days 0-5 | Same as above (this is the original action, now assigned to Syahir) |

### Active Risks (3 — All CRITICAL)

| # | Risk ID | Title | Probability | Impact | Status | Mitigation |
|---|---------|-------|-------------|--------|--------|------------|
| 1 | RSK-20260820-005 | Four supplier credentials exposed and unrotated — Critical exposure window open | OCCURRED | CRITICAL | 16+ days exposure | C1 credential rotation (ASSIGNED, NOT STARTED) |
| 2 | RSK-20260820-006 | Address-security integration stubbed on trunk but live on deployment — regression risk | HIGH | HIGH | NOT STARTED | M2 on critical path — after M1 credential rotation |
| 3 | RSK-20260820-007 | Deployment not describable — 43 uncommitted mods, no migration ledger, 29 commits behind trunk | OCCURRED | HIGH | NOT STARTED | M3 manifest + M4 backup + M5 migrations |

### Capacity Risk

**RSK-20260829-001 — Syahir Capacity Risk:** Triple-hatted with competing September deadlines. Probability HIGH, Impact HIGH. Same structural pattern as Hadri SPOF — available capacity attracts work. Three competing roles:
- QC Engineer (Sep 28 hard deadline)
- chain:SENTRY Phase 0 (Sep 15 kill date)
- POC Engineer (ongoing)

**No priority sequencing has been issued by Hadri or DAF.**

### Knowledge Transfer Gap

**RSK-20260829-002 — chain:SENTRY Knowledge Transfer Gap:** No briefing scheduled. Codebase is 69% implemented with 43 uncommitted mods, 29 commits behind trunk, no migration ledger. Without structured handover, Syahir spends 1-2 weeks reverse-engineering — eating into QC prep time.

**Mitigation deadline:** Sep 5 (TODAY — before T-33 gate)

### 2 FTE Capacity Map Contradiction

The 2 FTE Capacity Map (ART-20260829-002) was created Aug 29 — the SAME DAY as DEC-20260829-004 (chain:SENTRY to Syahir). The capacity map explicitly lists chain:SENTRY as "Hadri-owned, NOT on this map." The decision transferred it to Syahir but the capacity map doesn't account for the load.

**Syahir's planned capacity allocation (from the map):**
- Phase 1 (Sep 1-5): 50% receive handover, 30% QC ramp-up, 20% POC env familiarization
- Phase 2 (Sep 6-28): 40% QC claims validation, 30% demo env setup, 20% POC env support, 10% doc updates
- Phase 3 (Sep 29-Oct 10): 60% QC verification execution, 25% demo env live, 15% POC env maintenance

**chain:SENTRY engineering is NOT in any phase.** The map and the decision contradict each other.

### AIP-03 Workstream Review (OVERDUE Sep 5)

AIP-20260829-001 Item AIP-03: Fuad to review Syahir's workstream and align to practice strategic deliverables. Deadline Sep 5 (TODAY). Includes:
- Task-to-deliverable mapping
- Capability assessment per area
- Interim milestones

**Status:** No evidence this review has been started. If Syahir not ready by Sep 10 checkpoint: consider reassigning QC to DAF+Fuad joint review, or accepting reduced QC scope.

### chain:SENTRY Phase 0 Critical Path (6 Milestones)

| Milestone | Title | Status | Dependency | Kill Date |
|-----------|-------|--------|------------|-----------|
| M1 | Credential rotation | NOT STARTED (16d overdue) | None — first in path | IMMEDIATE |
| M2 | Address-security regression fix | NOT STARTED | M1 must complete first | — |
| M3 | Release manifest reconstruction | NOT STARTED | M2 must complete first | — |
| M4 | Backup and verified restore | NOT STARTED | — | — |
| M5 | Pending migrations applied through runner | NOT STARTED | M4 must complete first | — |
| M6 | Deploy | NOT STARTED | M3 + M5 must complete | — |

**C1 blocks C2 (Deployment Parity, Sep 10), C3 (External Access, Sep 15), C4 (Live-vs-Demo, Sep 20), C5 (Pilot Scope, Sep 30).** The entire Track C pilot chain is stopped at the gate.

### ESF-20260829-002 Dependency

Fuad's Engineered Success Framework lists Syahir as a dependency:
- CP1 (Sep 5): AIP-03 Syahir workstream reviewed + aligned — **TODAY, NO EVIDENCE**
- CP2 (Sep 10): Syahir interim capability checkpoint
- Leading indicator: Syahir independent task completion ≥3 tasks/week by Oct 15
- Risk #7: "Syahir doesn't ramp up" — probability M, impact M
- Failure condition: QC gate fails at CyberDSA → Fuad re-absorbs QC work

## Discussion Points for Meeting

1. **C1 credential rotation — execute TODAY.** 16 days of exposure. 4 supplier credentials served to unauthenticated callers for ~32 days (code defect fixed but credentials unrotated). Syahir executes, Fuud supports (2-3h). This is a security liability and blocks the entire Track C pilot chain.

2. **Priority sequencing — QC first, chain:SENTRY after.** QC deadline Sep 28 is hard-gated. chain:SENTRY Phase 0 work happens AFTER QC is on track (no later than Sep 14). If Syahir cannot do both by Sep 28: chain:SENTRY is de-scoped from CyberDSA demo. Formal decision needed — no implicit inaction.

3. **Knowledge transfer — schedule this week.** Hadri delivers 2-hour chain:SENTRY architecture briefing to Syahir. Covers: architecture overview, Phase 0 blocker context, deployment state, 43 uncommitted mods, migration ledger gap. Output: 1-2 page handover document authored by Hadri, reviewed by Fuad. If not done by Sep 7: Syahir's ramp-up starts after T-30, compressed against QC deadline.

4. **Capacity map contradiction.** The 2 FTE capacity map doesn't include chain:SENTRY. Either update the map or formally acknowledge it's outdated.

## Decisions Needed Today

- [ ] C1 execution confirmed for today/tomorrow (Syahir + Fuud support)
- [ ] Priority sequence confirmed: QC first, chain:SENTRY after Sep 14
- [ ] chain:SENTRY CyberDSA demo: in scope or de-scoped? (contingency decision if Syahir can't start Phase 0 by Sep 14)
- [ ] Knowledge transfer session scheduled (date + time this week)
- [ ] AIP-03 workstream review: Fuud confirms completion by Sep 5 or slips to Sep 10

---

# TOPIC 2: PRODUCT COSTING — Owner Assignment & Input Chain

## 2.1 Executive Summary

**The CognitiveOS repository contains no product costing infrastructure.** The gap is not partial — it is total. Every dimension assessed is absent for all three flagship products.

### What Exists (Fragmented, Top-Line Only)

| Product | Revenue References | Pricing Anchors | Costing | SKU | Licensing |
|---------|-------------------|-----------------|---------|-----|-----------|
| VoronCitadel | RM 414K→1.104M ARR | RM 138K/168K/368K (3 points) | ❌ None | ❌ None | ❌ Undefined |
| GovSec TIP | None | None | ❌ None | ❌ None | ❌ None |
| chain:SENTRY | None | None | ❌ None | ❌ None | ❌ None |
| Teras | None (bundled) | RM 138K-250K/year (bundled) | ❌ None | N/A | N/A |
| Sovereign AI PaaS | RM 688K envelope | RM 688K | ❌ None | ❌ None | ❌ None |
| Red Team Division | RM 1.75M-3.8M | RM 50K-1M per service line | ⚠️ Partial | ❌ None | ✅ $0 OSS |

## 2.2 VoronCitadel — Detailed Pricing Problem

### Three Price Points with No Rationale

| Price | Context | Source | Notes |
|-------|---------|--------|-------|
| RM 138,000/year | Existing paying customers (3) | ASSESS-20260820-001 | What this covers is undefined. Appears to be annual subscription |
| RM 168,000 | Early adopter price | OPP-20260822-001 | "Per licence" — licence terms undefined |
| RM 368,000 | Retail price | OPP-20260822-001 | "Per licence" — licence terms undefined |
| RM 500K-1M | Enterprise (Group 1 brokers) | OPP-20260827-001 | "Integration/partnership level" |
| RM 100K-200K | Niche (Group 3 brokers) | OPP-20260827-001 | "Local compliance adaptation" |

**Critical issue:** The price spread from RM 138K to RM 500K+ is 3.6× with no documented rationale. No document explains:
- Whether RM 138K is a legacy/grandfathered price
- Whether RM 168K is a time-limited early adopter price
- Whether RM 368K is the standard going-forward price
- Whether RM 500K-1M includes services beyond the software licence
- What cost basis justifies any of these price points

### VoronCitadel Cost References (Practice-Level, NOT Product-Level)

| Cost Item | Monthly (RM) | Annual (RM) | Source |
|-----------|-------------|-------------|--------|
| Hadri (existing) | 13,888 | 166,656 | ASSESS-20260820-001 |
| Head of Engineering | 18,888 | 226,656 | ASSESS-20260820-001 |
| Customer Success Engineer | 11,888 | 142,656 | ASSESS-20260820-001 |
| Junior Backend Engineer | 8,888 | 106,656 | ASSESS-20260820-001 |
| 3 new hires total | 39,656 | 475,968 | ASSESS-20260820-001 |
| GTM programme | — | 205K-310K | ART-20260822-003 |
| CyberDSA booth | — | 50K | ART-20260904-003 |

**Problem:** These are practice-level costs, not per-product. No FTE allocation to VoronCitadel specifically vs other products. No Teras cost allocation. Fuad and DAF salaries excluded from the model.

### Break-Even Analysis Is Overstated

ASSESS-20260820-001 claims break-even at 4 paying customers (4 × RM 138K = RM 552K > RM 476K). But this:
- Excludes Teras infrastructure cost ("absorbed by Farul's org" — unquantified)
- Excludes DAF and Fuad salaries
- Excludes GTM programme cost (RM 205K-310K)
- Excludes overhead
- Only compares revenue to 3 new hire FTE salaries

**The true break-even is higher than 4 customers.**

### VoronCitadel 4 Modules — No Per-Module Costing Exists

| Module | Description | Costing | Licensing | SKU |
|--------|-------------|---------|-----------|-----|
| GRC | Governance, Risk & Compliance | ❌ | ❌ | ❌ |
| DRM | Digital Risk Quantification | ❌ | ❌ | ❌ |
| ASM | Attack Surface Management | ❌ | ❌ | ❌ |
| TPRM | Third-Party Risk Management | ❌ | ❌ | ❌ |

**No document defines what's included at RM 168K vs RM 368K.** Is TPRM extra? Is ASM extra? Is AI Copilot included? Unknown.

## 2.3 GovSec TIP — Zero Commercial Framework

| Dimension | Status | Notes |
|-----------|--------|-------|
| Pricing | ❌ None | No direct pricing references found |
| Costing | ❌ None | FTE allocation: Fuad ~0.3 FTE across ALL 3 products, not isolated |
| Infrastructure | ❌ None | Teras GPU for AI Analyst unquantified. Air-gapped deployment cost unquantified |
| Licensing | ❌ None | Government agency licensing model undefined |
| Packaging | ❌ None | Multi-agency deployment isolation model undefined commercially |
| Recurring revenue | ❌ None | No recurring revenue model |
| SKU | ❌ None | No SKU |

**CyberDSA October is the commercial launch event. No commercial framework exists.**

## 2.4 chain:SENTRY — Zero Commercial Framework

Same as GovSec TIP. No pricing, no costing, no licensing, no packaging, no SKU. Fuad ~0.3 FTE across all 3 products. chain:SENTRY MVP_SPECIFICATION.md (62,090 bytes) contains zero pricing information.

## 2.5 Teras — The Hidden Cost Layer

Teras is the infrastructure layer for ALL 3 products (DEC-20260820-009). Without Teras cost allocation, no product can have accurate COGS.

- Hardware: 4× NVIDIA RTX PRO 6000 Blackwell (cost not stated)
- "Infrastructure cost absorbed by Farul's org" (ASSESS-20260820-001) — unquantified transfer pricing
- No model for how much Teras cost each product consumes
- No internal chargeback mechanism

## 2.6 Circular Dependencies (Must Be Broken)

1. **Pricing → Costing → Pricing:** Current prices are market-based or arbitrary, not cost-derived. Must establish costing first.
2. **Licence definition → SKU → Pricing:** A "licence" is referenced but undefined. Must define licence terms before SKU. Must define SKU before systematic pricing.
3. **Teras cost → Product COGS → Product Pricing:** Must allocate Teras cost before product COGS is known.

## 2.7 Commercialisation Readiness Action — 18 Days Overdue

**ACT-20260811-004 (Commercialisation Readiness):** Created Aug 11. Was supposed to answer costing questions. 18 days overdue. NOT STARTED. No alternative owner or path has been mobilised.

## 2.8 Documents That SHOULD Contain Costing But Don't

| Document | What It Is | What's Missing |
|----------|-----------|---------------|
| products/voroncitadel/PRODUCT_BASELINE.md | Product baseline | Zero pricing/costing |
| products/voroncitadel/MVP_SPECIFICATION.md | Full MVP spec | Zero pricing/costing |
| products/govsec-tip/MVP_SPECIFICATION.md | Full MVP spec (50,956 bytes) | Zero pricing/costing |
| products/chainsentry/MVP_SPECIFICATION.md | Full MVP spec (62,090 bytes) | Zero pricing/costing |
| products/teras/PLATFORM_OVERVIEW.md | Platform overview | Zero pricing/costing |

## 2.9 Cross-Product Gap Matrix

| Dimension | VoronCitadel | GovSec TIP | chain:SENTRY | Teras | PaaS | Red Team |
|-----------|-------------|------------|-------------|-------|------|----------|
| Costing methodology | ❌ | ❌ | ❌ | ❌ | ❌ | ⚠️ |
| Module-level costing | ❌ | ❌ | ❌ | N/A | ❌ | ❌ |
| Infrastructure costing | ❌ | ❌ | ❌ | ❌ | ❌ | ⚠️ |
| Labour/service costing | ❌ | ❌ | ❌ | N/A | ❌ | ⚠️ |
| Licensing model | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ ($0 OSS) |
| Packaging model | ❌ | ❌ | ❌ | ❌ | ❌ | ⚠️ |
| Recurring op cost | ❌ | ❌ | ❌ | ❌ | ❌ | ⚠️ |
| Deployment cost | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Margin assumption | ❌ | ❌ | ❌ | ❌ | ❌ | ⚠️ |
| Module-level SKU | ❌ | ❌ | ❌ | N/A | ❌ | ❌ |
| Product-level SKU | ❌ | ❌ | ❌ | N/A | ❌ | ❌ |

## Discussion Points for Meeting

1. **Owner assignment.** Who owns the costing framework?
   - Recommendation: Fuud owns costing methodology (engineering effort per module, Teras cost allocation). DAF owns commercial pricing (licence terms, margin, SKU structure, packaging).
   - Input owners: Fuud (engineering effort, infrastructure), Hadri (operational cost, service delivery), DAF (pricing, licensing, margin)

2. **First deliverable: VoronCitadel Costing Sheet.** 1 page. Module-level cost breakdown for GRC, DRM, ASM, TPRM. Due Sep 14.

3. **Licensing model — define before CyberDSA.** What does a "licence" cover? Per org? Per user? Per module? Per deployment? Time-limited or perpetual?

4. **VoronCitadel price points — confirm relationship.** Is RM 138K grandfathered? Is RM 168K time-limited early adopter? Is RM 368K standard? What drives the 3.6× spread?

5. **Teras cost allocation.** Even rough (GPU-hours × cost per GPU-hour). Without this, no product has accurate COGS.

6. **ACT-20260811-004 — replace or revive?** 18 days overdue. Either assign a new owner and deadline, or formally replace it with the VoronCitadel Costing Sheet action.

## Decisions Needed Today

- [ ] Costing owner assigned (Fuud confirmed for methodology?)
- [ ] VoronCitadel Costing Sheet deadline set (Sep 14?)
- [ ] Licensing model scope defined — what needs answering before CyberDSA
- [ ] VoronCitadel price points: confirm relationship (grandfathered / early adopter / retail)
- [ ] Teras cost allocation: rough model or detailed? By when?
- [ ] ACT-20260811-004: revive or replace?

---

# TOPIC 3: PORTFOLIO REGISTER — Kill Date Enforcement & Shadow Programmes

## 3.1 Current Portfolio Register State

| PRG | Programme | Recorded Status | Actual Status | Kill Date | Days Past | Next Action |
|-----|-----------|----------------|---------------|-----------|-----------|------------|
| PRG-001 | PERJASA AI Cohort Workshop | 🟢 Active | ⚠️ UNKNOWN | Sep 2 | 2 | Logistics execution (no evidence) |
| PRG-002 | CSM × Aras GTM Partnership | 🟡 Stalled | 💀 ZOMBIE | Aug 22 | 13 | Aisha PIC + POC scope (not completed) |
| PRG-003 | PMO AI Cohort Initiative | 🔴 Stalled | 💀 ZOMBIE | Aug 25 | 10 | Re-engagement email (not sent) |
| PRG-004 | R.I.S.I.K × UiTM | 🟡 Planned | ⚠️ KILL DATE PASSED | Sep 3 | 1 | Build Phase 0 deliverables (unknown) |
| PRG-005 | VORON-C2 Internship | ⚪ Design | ⚪ Design (accurate) | Oct 1 | — | Launch decision review |

## 3.2 PRG-001: PERJASA AI Cohort Workshop — Detail

- **Workshop dates:** Sep 2-3, 2026 (confirmed Aug 18, RSK-20260813-001 resolved)
- **Hard kill date:** Sep 2 (PASSED 2 days ago)
- **Commitment:** COM-20260813-001 — expected delivery Sep 3, status still "Active"
- **Completion evidence required:** "Workshop executed on confirmed dates"
- **No execution evidence ingested.** No post-workshop report, no outcome record, no daily memory entry for Sep 2-3.
- **Two scenarios:** (a) Workshop happened but outcomes not yet ingested (likely if DAF was physically there), or (b) Workshop did not happen or was delayed.
- **If executed:** Trigger 90-day post-workshop continuation (COM-20260813-003)
- **If not executed:** Mark 💀 Killed and archive.

## 3.3 PRG-002: CSM × Aras GTM Partnership — Detail

- **Kill date:** Aug 22 (passed 13 days ago)
- **Kill criteria:** "If Aisha PIC not confirmed + POC scope not agreed by Aug 22, CyberDSA silver sponsorship (RM50K) is at risk. Kill = withdraw sponsorship + pause GTM."
- **No evidence** that:
  - Aisha was confirmed as PIC (RSK-20260815-001 mentions Aisha was "proposed" as PIC but no confirmation record)
  - POC scope was agreed with Zulfeka
  - The kill decision was formally logged
- **But CSM partnership activity continues** extensively through other workstreams: INIT-20260804-004 (Co-Design Lab Cohort 01), multiple stakeholders (STK-20260812-001 through 017), DEC-20260812-001 (MyCERT accepts Cohort 01), CONV-20260817-002 (Hadri's MyCERT onboarding).
- **Assessment:** The specific GTM partnership gate (Aisha PIC + POC scope) was bypassed rather than formally killed. The broader CSM relationship is alive through other channels.
- **Decision needed:** Kill (withdraw sponsorship, pause GTM track) OR merge into CSM Joint Operating Model (INIT-20260813-005) and close the PRG-002 slot.

## 3.4 PRG-003: PMO AI Cohort Initiative — Detail

- **Kill date:** Aug 25 (passed 10 days ago)
- **Kill criteria:** "If no response by Aug 25, formally park. Send: 'We'll pause this initiative and revisit when timing aligns.' Free the cognitive slot. No zombie programmes."
- **The Strategic Objective document** (GOV-STRATEGIC-OBJECTIVE-COHORT-PROGRAMME-001) explicitly labels PRG-003 as "Status: Zombie. Kill Aug 25."
- **The ESF-20260829-001 DAF Strategic Leader Profile** (Aug 29) identifies this as a known gap: "PRG-003 passed kill date with no decision logged" and lists "Enforce PRG-003 kill decision — first kill-date enforcement test" as a DoD-1 action with Sep 7 deadline.
- **No initiative record, no stakeholder record, no conversation record, no commitment, and no action record** exists for a "PMO AI Cohort Initiative." This programme appears to have never been formally ingested beyond the Portfolio Register entry itself.
- **This is the FIRST kill-date enforcement test.** If not enforced, every future kill date is advisory.

## 3.5 PRG-004: R.I.S.I.K × UiTM — Detail

- **Kill date:** Sep 3 (passed 1 day ago)
- **Kill criteria:** "If Phase 0 deliverables (daily collection script, claim register, sample brief) not built by Sep 3, push UiTM session to Sep 20. Do not walk in with concepts only."
- **DeerFlow** (INIT-20260611-001) has been operational since July 2026 with 100% success rate on 25-source collection. The daily collection capability exists as infrastructure.
- **Whether the claim register and sample brief were built specifically for RISIK Phase 0 by Sep 3 is unclear** — no completion evidence found.
- **This is NOT a kill — it's a slip.** The contingency action is clear: push UiTM working session to Sep 20.
- **Substantial momentum exists:** RM 5M cost structure, MCMC funding pathway, PRISM 2.0 integration, academic validation.

## 3.6 Shadow Programmes — Not in Portfolio Register

### CSM Co-Design Lab Cohort 01 (INIT-20260804-004)
- **Status:** Active — Prototype
- **23 MyCERT personnel onboarded** (Aug 12-17)
- This is the CSM/MyCERT track of the Co-Design Lab
- **NOT in the Portfolio Register** — violates Rule 5: "New programmes must enter the register before work begins. No shadow portfolios."
- Has more active momentum than PRG-002 or PRG-003

### Other References Found
- **R.I.S.I.K Cohort Programme** — referenced in DEC-20260818-012, COM-20260818-001 as "practitioner/SME development platform." Currently tracked under INIT-20260803-002 (same as PRG-004).
- **Perdana Digital AI Cohort** — referenced in INIT-20260725-001, listed as "active, JDN stakeholder, pilot stage." No dedicated INIT record. NOT in the Portfolio Register.

## 3.7 Kill-Date Enforcement Failure — Systemic

The Portfolio Register explicitly states:
- "No programme without a kill date"
- "Parked programmes free cognitive capacity. Zombies drain it."
- "No zombie programmes"

Yet 3 of 5 programmes have passed kill dates with no enforcement. The register's own rules are being violated. The pattern the register was designed to prevent ("the five-programme pattern from repeating on the next five") is actively repeating.

**The ESF profile flagged PRG-003 on Aug 29.** Six days later, still unenforced. This is now the longest-standing unaddressed governance finding.

## 3.8 MEISAC × NanoSec × Aras Cohort — Full Discovery

- **MEISAC:** ZERO occurrences in entire CognitiveOS repository. No initiative, no stakeholder, no organisation, no conversation, no decision, no commitment, no action, no intelligence record. No expansion, acronym definition, or contextual mention exists.
- **NanoSec:** Exists as ORG-20260904-001 (created today). Pentesting resource for GovSec TIP B1 Security Remediation gate (Sep 15). NOT a cohort partner.
- **Trifecta / Third cohort:** ZERO occurrences of "trifecta" or "third cohort" anywhere.
- **Conclusion:** MEISAC × NanoSec × Aras cohort programme does NOT exist. If DAF intends to create it, it requires: (1) MEISAC intake, (2) new PRG entry, (3) initiative record, (4) kill date and next action.

## Discussion Points for Meeting

1. **PRG-003 — enforce NOW.** First kill-date enforcement test. Sets binding precedent. 30 minutes to update the register and log the decision.
2. **PRG-002 — kill or merge?** The GTM gate failed. CSM relationship continues through other channels. Either formally kill or merge into CSM JOM.
3. **PRG-004 — push to Sep 20.** Not a kill. Confirm Phase 0 deliverable status. Update next action.
4. **PRG-001 — confirm workshop status.** DAF was there. If executed → intake + trigger 90-day continuation. If not → update status.
5. **Add shadow programmes to register.** CSM Co-Design Lab Cohort 01 as PRG-006. Check Perdana Digital AI Cohort.
6. **MEISAC — does it exist?** If yes → full intake needed. If no → drop from discussion.
7. **Third cohort — concept or initiative?** If concept → Watch List. If initiative → PRG-007 with kill date.

## Decisions Needed Today

- [ ] PRG-001: workshop execution confirmed? Intake scheduled?
- [ ] PRG-002: kill or merge into CSM JOM?
- [ ] PRG-003: formal park (first kill-date enforcement)
- [ ] PRG-004: UiTM session pushed to Sep 20?
- [ ] PRG-006: CSM Co-Design Lab Cohort 01 added to register?
- [ ] MEISAC: exists or not?
- [ ] Third cohort: concept (Watch List) or initiative (PRG-007)?

---

# TOPIC 4: AMELIA — 77-Person High-Touch Stakeholder Activation

## 4.1 Current Stakeholder Data Foundation

### Total Existing STK Records: 108

| Category | Count | High-Touch Eligible? | Notes |
|----------|-------|---------------------|-------|
| CSM (CyberSecurity Malaysia) | ~40 | ✅ Yes | Primary engagement targets |
| Internal (Aras/WIG/MTAI) | ~20 | ❌ No | Internal team |
| Government (non-CSM) | ~18 | ✅ Partially | JDN, NACSA, MCMC, PMO leadership |
| Partner/Academic | ~14 | ✅ Partially | ELSA, UiTM, UPM, Plymouth |
| Intelligence Subjects | ~5 | ❌ No | OSINT only |
| Misc/Dormant | ~11 | ❌ No | Reclassified/superseded |

**Total externally engaging:** ~62

### CSM Stakeholder Breakdown (40 records)

| Sub-category | Count | Key Individuals |
|--------------|-------|-----------------|
| CSM Leadership/Strategic | 6 | Fahdzli, Zulfeka, Roshdi, Azrul, Bala, Amirudin (retired) |
| CSM Technical/Gate Owners | 5 | Zaharudin, Wan Roshaimi, Hafiz Rahman, Iqbal, Amirul |
| CSM Co-Design Lab (MyCERT) | 17 | Fathi Kamil, Izzatul, Imran, Qurratu, Lukman, Syahidah, + 11 others |
| CSM Other | 6 | Nurshahira, Suraya Hani, Zulfelka, Fazlan, Tuan Fatah, Shamsul Azri |
| CSM-Adjacent | 6 | Aisha, Dr. Megat/NACSA, Nushirwan/MKN, Mohamad Salim/MCMC, Fabian Bigar/KKD, Fahmi Fadzil |

### Total Existing ORG Records: 24

| Type | Count | Organisations |
|------|-------|---------------|
| Government Agency | 7 | CSM, NACSA, JDN, PMO, PERJASA, MKN, MAPO |
| Private Company | 2 | Nexuscorpgroup, Al Khairi Group |
| Internal Division | 1 | RADAR |
| Community Team | 1 | NanoSec |
| Other/Backfilled | 13 | CSCDC, LHDN, WIG, MTAI, ELSA, MOH, UiTM, etc. |

**Organisation index is stale:** Only 6 of 24 ORG files are in the formal index. 18 need indexing.

## 4.2 The 193-Organisation Segmentation Framework

**Document:** SEG-20260818-001
**CSV Data:** SEG-193-org-segmentation-20260818.csv (191 rows)
**Raw Mapping:** STAKEHOLDER_MAPPING_193.csv (193 rows × 7 contact roles = ~1,351 contact cells)

### Scale

| Metric | Value |
|--------|-------|
| Unique organisations | 191 (after dedup in v5.51) |
| Total stakeholder entries | 150 unique (43 share parent org stakeholders) |
| Contact functions per org | 7 (CISO, Head of GRC, CFO, CRO, Head of Compliance, CIO, Head of Internal Audit) |
| Unique named CISOs | ~94 (after dedup) |
| Directionally actionable | 65.4% |
| Explicit numeric confidence | Only 4.7% of entries |

### Sector Breakdown

| Tier | Count | Segments |
|------|-------|---------|
| Tier 1 | 32 | Licensed Banks |
| Tier 2 | 52 | Insurers (26), Investment Banks (14), Takaful (12) |
| Tier 3 | 34 | Development FIs (13), MSBs (16), Asset Management (5) |
| Tier 4 | 35 | E-Money (17), Card Schemes (10), Payment Operators (8) |
| Tier 5 | 23 | GLC-Linked |
| Tier 6 | 17 | Fintech Registered (6), Fintech Sandbox (11) |
| **Total** | **193** | **13 market segments** |

### Priority Classification

| Class | Score | Count | CyberDSA Action |
|-------|-------|-------|-----------------|
| A — Target | ≥50 | 93 | Pre-schedule meeting before CyberDSA |
| B — Engage | 40-49 | 35 | Send collateral + personal invitation to booth |
| C — Monitor | 30-39 | 44 | Include in mailing list |
| D — Watch | <30 | 19 | Database only, no active outreach |

### Top 15 VIP Targets

Maybank, CIMB, Public Bank, HSBC, AmBank, RHB, Hong Leong, Bank Islam, OCBC, Standard Chartered, Prudential, Great Eastern, Etiqa, Tokio Marine, Liberty General.

### Data Quality

- 135 organisations (71%) have 3+ identified contacts (enriched)
- 18 organisations (9%) have 1-2 contacts (partial)
- 38 organisations (20%) have 0 contacts (bare — primarily Tier 3 MSBs and Tier 6 fintechs)
- Tier 1 and Tier 2 are **fully enriched** — 26/30 Tier 1 and 54/54 Tier 2 have 3+ contacts

## 4.3 The 77-Person Gap

### What the 77 Is NOT

- It is NOT the 193-org database — that's a market intelligence asset, not an activation list
- It is NOT the 108 STK records — those include 20 internal, 5 OSINT, 11 dormant = only ~62 external
- It is NOT the existing TRK-20260818-001 tracker — that's stale and incomplete (~85 rows, many placeholders)

### What the 77 IS (Probable Interpretation)

The 77-person target = the set of named, reachable decision-makers requiring personalised, relationship-based activation. Most likely drawn from:
1. A-Target tier (93 organisations): Named CISOs and Heads of GRC
2. Existing CSM stakeholders (40): Already engaged
3. Government stakeholders (18): JDN, NACSA, MCMC, PMO
4. Partner/Academic (14): ELSA, UiTM, UPM

### Gap Calculation

| Metric | Value |
|--------|-------|
| Target high-touch stakeholders | 77 |
| Existing named external stakeholders | ~62 |
| **Gap (all external scope)** | **15 missing** |
| **Gap (CSM-only scope)** | **37 missing** |

### What's Missing

1. **STK records for the 77:** Most of the 77 individuals exist only in CSV data, not as stakeholder records
2. **Amelia's activation tracker:** No dedicated tracker for the 77-person programme
3. **Engagement status:** No contact history, relationship owner, or next-action data for market contacts
4. **Organisation index:** 18 of 24 ORG files not reflected in the index
5. **Clear definition of "the 77":** No document explicitly defines who the 77 are or selection criteria

## 4.4 Existing Trackers (Incomplete)

### TRK-20260818-001 — Stakeholder Coverage Tracker
- CSV with 18 columns (stakeholder_id, name, role, organisation, relationship_status, priority, last_contact_date, days_since_contact, staleness, engagement_depth, etc.)
- ~85 rows but many placeholders (reclassified, dormant, no-contact)
- Created Aug 18 as CyberDSA preparation
- Appears to be a one-time export, not a living document
- Many entries have empty owner/action fields

### INT-20260815-003 — CyberDSA RACI Matrix
- 10 named stakeholders × 6 CyberDSA execution dimensions
- Execution matrix, not relationship activation matrix

### INT-20260815-004 — CSM-Aras Stakeholder Coverage Plan
- 4-layer coverage model (Primary, Secondary, Specialist, Executive)
- 10 CSM stakeholders with Aras coverage
- Communication Ownership Model (7 topic areas)
- Coverage Readiness Metrics (8 metrics, all targeting 100%/0 SPOF)

## 4.5 CyberDSA Timeline Pressure

- **Pre-schedule meetings with A-Target orgs before Oct 10.** That's 93 orgs, 5 weeks out.
- At ~4 meetings/week = 20 meetings in 5 weeks.
- Amelia needs the 77-person target list, STK records, and tracker BEFORE she can start scheduling.
- **Every day of delay reduces the pre-engagement window.**

## Discussion Points for Meeting

1. **Define the 77.** Selection criteria: is it 77 individuals from A-Target orgs (CISO + GRC Head), or 77 across all categories (CSM + government + market)?
2. **Create STK records for the 77.** Each needs: named contact, organisation context, engagement tier (high-touch = A-Target VIP), relationship owner (Amelia or DAF), contact status and history.
3. **Build the activation tracker.** Either upgrade TRK-20260818-001 or create a new tracker specifically for the 77-person programme. Must be a living document, not a one-time export.
4. **Amelia's authority scope.** Can she initiate contact directly with A-Target stakeholders, or does she need DAF approval per contact?
5. **Weekly meeting target.** 93 A-Target orgs, 5 weeks to CyberDSA. At 4 meetings/week = 20 meetings. Is that the target? What's the priority sequence (Tier 1 banks first)?
6. **Organisation index update.** 18 of 24 ORG files not in the index. Low effort, should be cleaned up.

## Decisions Needed Today

- [ ] 77-person target list: selection criteria defined? By when?
- [ ] Activation tracker: upgrade existing or create new? Format decided?
- [ ] Amelia's authority: direct contact or DAF-approved?
- [ ] Weekly meeting target for CyberDSA pre-engagement: 20? 15? 10?
- [ ] Priority sequence: Tier 1 banks first?
- [ ] Organisation index update: assign to Ember?

---

# TOPIC 5: PERJASA WORKSHOP OUTCOMES — Intake

## 5.1 What We Know

- **Workshop dates:** Sep 2-3, 2026
- **Date confirmed:** Aug 18 (RSK-20260813-001 resolved)
- **Venue:** Not ingested
- **DAF attendance:** Yes (DAF was physically at the workshop)
- **Commitment:** COM-20260813-001 — expected delivery Sep 3, status still "Active"
- **Completion evidence required:** "Workshop executed on confirmed dates"
- **Post-workshop continuation:** COM-20260813-003 (90-day continuation) — trigger if executed

## 5.2 What's NOT Ingested

- No post-workshop report
- No outcome record
- No daily memory entry for Sep 2-3
- No new stakeholder records from workshop attendees
- No new initiative records from workshop outcomes
- No follow-up commitments logged
- COM-20260813-001 not updated to "delivered"

## 5.3 What Needs to Happen

1. DAF shares workshop outcomes (attendance, key discussions, commitments, next steps)
2. Intake follows CognitiveOS Intake SOP (9-step process):
   - Receive & classify
   - Extract & structure all entities
   - Create records with permanent typed IDs
   - Update indexes
   - Update daily memory
   - Commit with standard format
   - Push to GitHub
   - Deliver confirmation notification
   - Update MEMORY.md if strategically significant
3. Update COM-20260813-001 to delivered
4. If workshop was executed: trigger COM-20260813-003 (90-day post-workshop continuation)
5. PRG-001 status update in Portfolio Register

## Discussion Points for Meeting

1. Workshop execution confirmed?
2. Key outcomes: attendance numbers, organisations represented, commitments made?
3. New stakeholders to ingest?
4. New initiatives or follow-up commitments?
5. When can intake be completed? (recommend within 48 hours)

## Decisions Needed Today

- [ ] Workshop execution confirmed (yes/no)
- [ ] Intake scheduled (today? tomorrow?)
- [ ] COM-20260813-001 status updated
- [ ] 90-day continuation (COM-20260813-003) triggered?

---

# TOPIC 6: CROSS-CUTTING — Governance & Mobilisation Discipline

## 6.1 The Pattern: Decisions Without Execution (5th Consecutive Review)

| Directive | Decisions Made | In Execution | Completion Evidence |
|-----------|---------------|-------------|-------------------|
| A: Syahir | 4 (Aug 18–Sep 4) | 0 of 4 | 0 of 4 |
| B: Costing | ACT-20260811-004 assigned | NOT STARTED (18d overdue) | None |
| C: Portfolio | Kill dates defined for 3 PRGs | 0 of 3 enforced | 0 of 3 |
| D: Amelia | Role assigned, data exists | No target list, no tracker | None |

**4 directives, 0 in execution. 100% decision-to-execution gap.**

This is the 5th consecutive Cognitive Loop identifying this pattern. It has not been corrected. It has widened.

## 6.2 The Honest Finding

DAF was at the PERJASA workshop Sep 2-3. The practice is not failing to act — it is failing to **track** action. The gap is not between decision and execution. It is between execution and **evidence of execution**.

The intervention needed is **intake discipline**: every action, every outcome, every completion gets ingested into CognitiveOS within 24 hours. The discovery reports show what happens when intake is delayed — the system shows zeros where there is actual progress, and the Loop reports deterioration that may not exist.

## 6.3 Three Systemic Actions (From Cognitive Loop INT-20260904-006)

### Action 1: Enforce Kill Dates — NOW
**Owner:** DAF → Ember (register update)
**Deadline:** Sep 5
**Effort:** 30 minutes
**Impact:** Sets governance precedent. Validates that kill dates are binding.

### Action 2: Mobilise C1 Credential Rotation — Today
**Owner:** DAF → Hadri → Syahir (Fuud support)
**Deadline:** Sep 5
**Effort:** 2-3 hours
**Impact:** Closes 16-day security liability. Unblocks Track C pilot chain (C2-C5).

### Action 3: Assign Product Costing Owner
**Owner:** DAF (assignment) → Fuud (costing methodology)
**Deadline:** Sep 7
**Effort:** Define input chain + first deliverable (VoronCitadel Costing Sheet by Sep 14)
**Impact:** Unblocks CyberDSA commercial launch and Q4 sales.

## 6.4 Full Kill Date Enforcement Register

| Item | Kill Date | Days Past | Status | Action |
|------|-----------|-----------|--------|--------|
| PRG-003 (PMO AI Cohort) | Aug 25 | 10 | UNENFORCED | Park immediately |
| PRG-002 (CSM GTM) | Aug 22 | 13 | UNENFORCED | Kill or merge |
| PRG-004 (RISIK × UiTM) | Sep 3 | 1 | UNENFORCED | Push to Sep 20 |
| PRG-001 (PERJASA) | Sep 2 | 2 | UNKNOWN | Confirm status |
| C1 Credential Rotation | Sep 5 | 0 (today) | NOT STARTED | Execute today |
| Hadri→Syahir briefing | Sep 7 | — | NOT SCHEDULED | Schedule this week |
| VoronCitadel Costing Sheet | Sep 14 | — | NOT STARTED | Assign owner |
| QC Claims Verification | Sep 28 | — | NO PROGRESS EVIDENCE | Monitor |
| PRG-005 (VORON-C2) | Oct 1 | — | ON TRACK | Monitor |
| Fuud career conversation | Week of Sep 7 | — | SCHEDULED | Confirm |

## 6.5 Fuud Career Conversation — The Next Structural Gate

**Week of Sep 7.** This conversation gates:
- HoE decision (who owns engineering practice-wide)
- Fuud's formal designation as Acting Practice Technical Authority (or not)
- Next structural intervention possibility
- ESF-20260829-002 DoD gates activation

**No engineering relief before January 2027.** DAF directive: discipline is the strategy through January. No new scope on Fuud/Hadri. Scope discipline, action register hygiene, Syahir ramp-up, and execution diligence are the only mitigations.

---

## Pre-Meeting Summary: Full Decisions Queue

| # | Decision | Owner | Urgency | Topic |
|---|----------|-------|---------|-------|
| 1 | C1 credential rotation — execute today | Syahir (Hadri directs, Fuud supports) | 🔴 16d overdue | Syahir |
| 2 | Priority sequence: QC first, chain:SENTRY after | DAF confirms | 🔴 This week | Syahir |
| 3 | chain:SENTRY CyberDSA demo: in scope or de-scoped? | DAF | 🔴 Contingency | Syahir |
| 4 | Knowledge transfer session scheduled | Hadri | 🟡 This week | Syahir |
| 5 | AIP-03 workstream review completion | Fuud | 🟡 Sep 5 or slip to Sep 10 | Syahir |
| 6 | Costing owner assigned | DAF | 🟡 By Sep 7 | Costing |
| 7 | VoronCitadel Costing Sheet deadline | Fuud (if assigned) | 🟡 Sep 14 | Costing |
| 8 | Licensing model scope for CyberDSA | DAF | 🟡 Before Oct 10 | Costing |
| 9 | VoronCitadel price points: confirm relationship | DAF | 🟡 Before CyberDSA | Costing |
| 10 | Teras cost allocation: rough or detailed? | Fuud | 🟡 Before Costing Sheet | Costing |
| 11 | ACT-20260811-004: revive or replace? | DAF | 🟡 18d overdue | Costing |
| 12 | PRG-001: workshop execution confirmed? | DAF | 🟡 2d past | Portfolio |
| 13 | PRG-002: kill or merge into CSM JOM? | DAF | 🔴 13d overdue | Portfolio |
| 14 | PRG-003: formal park (first kill-date enforcement) | DAF | 🔴 10d overdue | Portfolio |
| 15 | PRG-004: UiTM session pushed to Sep 20? | DAF | 🟡 1d overdue | Portfolio |
| 16 | PRG-006: CSM Co-Design Lab added to register? | DAF/Ember | 🟡 This week | Portfolio |
| 17 | MEISAC: exists or not? | DAF | 🟢 Clarify today | Portfolio |
| 18 | Third cohort: concept or initiative? | DAF | 🟢 Clarify today | Portfolio |
| 19 | 77-person target list: selection criteria | DAF/Amelia | 🟡 By Sep 14 | Amelia |
| 20 | Activation tracker: upgrade or new? | DAF | 🟡 By Sep 14 | Amelia |
| 21 | Amelia's contact authority scope | DAF | 🟡 This week | Amelia |
| 22 | Weekly meeting target for CyberDSA | DAF | 🟡 This week | Amelia |
| 23 | PERJASA workshop intake scheduled | DAF | 🟡 Within 48h | PERJASA |
| 24 | 90-day continuation (COM-20260813-003) triggered? | DAF | 🟡 If workshop executed | PERJASA |
| 25 | Organisation index update (18 ORG files) | Ember | 🟢 Low effort | Amelia |
| 26 | Capacity map update (add chain:SENTRY) | Ember/DAF | 🟡 This week | Syahir |
| 27 | Fuud career conversation confirmed for Sep 7 week | DAF | 🟡 Next week | Cross-cutting |

---

*Briefing pack prepared from CognitiveOS Discovery Directives A-D (INT-20260904-002 through 005) and Cognitive Loop INT-20260904-006. All claims T3 [ASSESSMENT], L2 evidence, confidence 7/10 (Rule 6 cap — AI-generated, human review required for T1 upgrade). DAF retains all decision authority.*
