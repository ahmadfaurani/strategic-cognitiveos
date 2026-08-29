---
id: ART-20260829-002
record_type: artifact
artifact_type: analysis
title: "Technical Execution Unit — 2 FTE Capacity Map (Sep 2026 – Jan 2027)"
created_at: 2026-08-29T08:22:00+00:00
updated_at: 2026-08-29T08:22:00+00:00
owner: faurani-jaafar
status: active
priority: critical
sensitivity: confidential
lifecycle_state: canonical
confidence: high
tags:
  - domain/cybersecurity-productisation
  - domain/strategic
  - domain/capacity-building
  - domain/product-management
  - framework/engineered-success
  - lifecycle/active
source:
  type: direct
  reference: DAF Telegram directive 2026-08-29 08:22 UTC
summary: "Maps all committed technical deliverables against 2 FTE (Fuad + Syahir) from Sep 2026 to Jan 2027. 5 phases, 7 handover items, 3 feasibility conditions."
strategic_significance: "The 2 FTE capacity map is the operational view of the Technical Execution Unit through January 2027. It defines what gets done, by whom, and what must NOT be added."
mission_alignment:
  - cybersecurity-productisation
  - cyberdsa-2026
  - organisational-capability-building
related_records:
  - AIP-20260829-001
  - ESF-20260829-002
  - STK-20260804-003
related_initiative: INIT-20260811-001
---

# Technical Deliverable Execution Review — 2 FTE Capacity Map

**Date:** 2026-08-29
**Unit:** Technical Execution Unit (Fuad + Syahir) = 2 FTE
**Constraint:** No engineering hires before January 2027. Discipline is the strategy.
**Horizon:** Sep 2026 – Jan 2027

---

## 1. Committed Technical Deliverables — Fuad

### Immediate (Aug 31 – Sep 5)

| # | Deliverable | Deadline | Status | FTE | Source |
|---|------------|----------|--------|-----|--------|
| 1 | GovSec × CMERP Gate 1 — engineering comment closure | Aug 31 | Active | Fuad | ACT-20260827-004 |
| 2 | GovSec × CMERP Gate 3 — confirm document technically complete | Sep 2 | Active | Fuad | ACT-20260827-006 |
| 3 | RSWG 9 control domains → VoronCitadel capability matrix | Aug 29 (OVERDUE) | Active | Fuad | ACT-20260827-001 |
| 4 | ITSS 12 domains — unified ITSS × RSWG × VoronCitadel matrix | Aug 29 (OVERDUE) | Active | Fuad | ACT-20260827-003 |
| 5 | Bursa POC document — RSWG alignment section | Aug 30 | Active | Fuad | ACT-20260827-002 |
| 6 | Syahir workstream review + alignment (AIP-03) | Sep 5 | PRIORITY #1 | Fuad | AIP-20260829-001 |

### Near-Term (Sep 6 – Sep 30)

| # | Deliverable | Deadline | Status | FTE | Source |
|---|------------|----------|--------|-----|--------|
| 7 | Bursa POC — TPRM + federated compliance development | NDA gates (Sep 4) → start | Pending NDA | Fuad | ACT-20260824-001 |
| 8 | Bursa POC — RSWG §2.6 / ITSS §10 technical implementation | Post-NDA | Pending | Fuad | DEC-20260827-001 |
| 9 | VoronCitadel product roadmap | Draft → committed | Draft | Fuad | ACT-20260811-006 |
| 10 | VoronCitadel product backlog | Draft → committed | Draft | Fuad | ACT-20260811-006 |
| 11 | VoronCitadel commercialisation docs | Draft → committed | Draft | Fuad | DEC-20260820-011 |
| 12 | GovSec TIP Q4 2026 roadmap items — kickoff | Sep–Oct | Active | Fuad | DOC-20260821-004 |
| 13 | Documentation drive — VoronCitadel + GovSec | Ongoing | Active | Fuad | ACT-20260820-013 |

### CyberDSA Window (Oct 1 – Oct 10)

| # | Deliverable | Deadline | Status | FTE | Source |
|---|------------|----------|--------|-----|--------|
| 14 | CyberDSA demo readiness — VoronCitadel | Oct 10 | Active | Fuad + Syahir | INIT-20260810-003 |
| 15 | CyberDSA claims validation — product baseline | Sep 28 (T-7) | Active | Syahir (Fuad validates) | DEC-20260818-007 |
| 16 | CyberDSA demo environment setup | Pre-Oct 10 | Pending | Syahir | — |

### Post-CyberDSA (Oct 11 – Jan 2027)

| # | Deliverable | Timeline | Status | FTE | Source |
|---|------------|----------|--------|-----|--------|
| 17 | Bursa POC Phase 0 execution — TPRM build | Oct–Nov | Pending NDA | Fuad | INIT-20260824-001 |
| 18 | Bursa POC — federated compliance document checking | Nov–Dec | Pending | Fuad | INIT-20260824-001 |
| 19 | GovSec TIP Q4 2026 roadmap delivery | Oct–Dec | Active | Fuad | DOC-20260821-004 |
| 20 | GovSec TIP Q1 2027 roadmap — definition | Dec | Pending | Fuad | — |
| 21 | Bursa POC completion + reference case | Mar 2027 | Pending | Fuad | ESF-20260829-002 DoD-2 |

---

## 2. Deliverables Syahir Can Absorb (Post-Handover)

These are the tasks Fuad currently owns that Syahir should absorb once AIP-03 handover is complete:

| # | Task | Current Owner | Syahir Readiness | When | Impact |
|---|------|---------------|-----------------|------|--------|
| A | POC environment setup | Fuad | RAMPING | Immediately | Frees Fuad for architecture |
| B | Routine claims validation (product baseline) | Fuad | RAMPING | Pre-CyberDSA | Frees Fuad for architectural claims |
| C | Demo environment setup + maintenance | Fuad | RAMPING | Pre-Oct 10 | Frees Fuad for demo content |
| D | QC verification — CyberDSA claims | Fuad | TARGET: Sep 28 | Sep 28 gate | Critical — T-7 CyberDSA |
| E | VoronCitadel test execution (Bursa POC) | Fuad | POST-HANDOVER | Post-NDA | Frees Fuad for TPRM build |
| F | Documentation maintenance — routine updates | Fuad | POST-HANDOVER | Oct+ | Frees Fuad for architecture |
| G | GovSec TIP — routine monitoring/alerting checks | Fuad | POST-HANDOVER | Oct+ | Frees Fuad for roadmap delivery |

**If Syahir absorbs A–D by mid-September:** Fuad gains approximately 0.5 FTE of architecture/development capacity for Bursa POC + GovSec roadmap.

**If Syahir absorbs A–G by November:** Fuad gains approximately 0.8 FTE for architecture/strategy work — approaching the ESF DoD-5 target (60% architecture).

---

## 3. Capacity Allocation — 2 FTE Map (Sep – Jan)

### Phase 1: Sep 1 – Sep 5 (T-35 to T-30)

```
Fuad (1.0 FTE):
  ├── 40% — GovSec Gate 1 + Gate 3 (engineering comments + technical completion)
  ├── 25% — RSWG/ITSS capability mapping (overdue items 3-5)
  ├── 20% — Syahir workstream review + handover (AIP-03)
  └── 15% — Bursa POC prep (post-NDA technical scoping)

Syahir (1.0 FTE):
  ├── 50% — Receive handover from Fuad (AIP-03 alignment)
  ├── 30% — QC capability ramp-up (claims validation training)
  └── 20% — POC environment familiarization (VoronCitadel)
```

### Phase 2: Sep 6 – Sep 28 (T-29 to T-7 CyberDSA)

```
Fuad (1.0 FTE):
  ├── 35% — Bursa POC TPRM development (post-NDA)
  ├── 25% — VoronCitadel product docs (roadmap, backlog, commercialisation)
  ├── 20% — GovSec Q4 roadmap kickoff
  ├── 15% — Syahir supervision + technical validation
  └── 5%  — Documentation drive

Syahir (1.0 FTE):
  ├── 40% — QC claims validation (CyberDSA target Sep 28)
  ├── 30% — Demo environment setup + maintenance
  ├── 20% — POC environment support (VoronCitadel for Bursa)
  └── 10% — Routine documentation updates
```

### Phase 3: Sep 29 – Oct 10 (T-7 to CyberDSA)

```
Fuad (1.0 FTE):
  ├── 50% — CyberDSA demo readiness (technical validation)
  ├── 30% — Bursa POC TPRM development (continued)
  ├── 15% — Claims validation review (architectural claims)
  └── 5%  — Documentation finalization

Syahir (1.0 FTE):
  ├── 60% — QC verification execution (claims verified against baseline)
  ├── 25% — Demo environment live + booth technical support
  └── 15% — POC environment maintenance
```

### Phase 4: Oct 11 – Dec 31 (Post-CyberDSA)

```
Fuad (1.0 FTE):
  ├── 40% — Bursa POC Phase 0 execution (TPRM + federated compliance)
  ├── 25% — GovSec TIP Q4 roadmap delivery
  ├── 15% — VoronCitadel v3.0 architecture vision
  ├── 10% — Syahir supervision + delegation expansion
  └── 10% — Documentation maintenance (cadence)

Syahir (1.0 FTE):
  ├── 30% — Bursa POC test execution + environment
  ├── 25% — VoronCitadel routine maintenance + monitoring
  ├── 20% — Documentation updates (living docs)
  ├── 15% — GovSec TIP routine checks + alerting
  └── 10% — Continued ramp-up (advanced topics)
```

### Phase 5: Jan 2027 (HoE In Seat)

```
Fuad shifts to: 60% architecture / 30% validation / 10% hands-on
HoE absorbs: day-to-day development + code review + deployment
Syahir absorbs: QC + POC env + documentation + customer support
CSE absorbs: customer-facing engineering (when hired)
```

---

## 4. Conflict Points & Risk Areas

| Risk | When | Why | Mitigation |
|------|------|-----|------------|
| NDA slips past Sep 4 | Sep 4–10 | Bursa POC technical work can't start. Fuad has capacity but no document. | DAF follows up with Azrul. If slipped >Sep 10, re-baseline Bursa timeline. |
| RSWG/ITSS mapping overdue (items 3-5) | NOW | 3 items due Aug 29-30, all overdue or imminent. Fuad needs to clear these before Bursa POC starts. | Prioritize Aug 29-30 — these block Bursa POC alignment. |
| Syahir not ready for QC by Sep 28 | Sep 10 checkpoint | If Syahir can't independently verify claims, Fuad re-absorbs QC — capacity loss. | AIP-03 Sep 5 review + Sep 10 interim checkpoint. Fallback: Fuad + DAF joint QC. |
| GovSec gate chain breaks | Aug 31 – Sep 5 | If Gate 1 (Aug 31) or Gate 3 (Sep 2) slips, T-30 closure (Sep 5) is at risk. Hadri chain. | AIP-01 reminder set. DAF verifies with Fuad directly. |
| Fuad overloaded in Phase 2 | Sep 6-28 | 5 concurrent workstreams (Bursa POC + docs + GovSec + Syahir supervision + documentation) at 1.0 FTE. | Discipline: if Bursa POC starts late (NDA), Fuad has buffer. If on time, something drops. |
| CyberDSA demo not ready | Oct 1-10 | Demo env + claims + technical validation converge on same 2 FTE. | Syahir absorbs demo env + QC. Fuad validates only. No new scope in this window. |
| Bursa POC timeline compresses | Oct-Dec | 4-month timeline with TPRM + federated compliance. If NDA slips, timeline compresses. | Start ASAP post-NDA. Fuad full-time on TPRM in Phase 4. Syahir on test execution. |

---

## 5. What This Map Assumes

1. **AIP-03 handover starts immediately** — not Sep 5, but now. The 2 FTE only works if Syahir is absorbing load by Sep 10.
2. **NDA signed by Sep 4** — Bursa POC technical work starts Sep 5. If not, Fuad has buffer in Phase 2 but Bursa timeline compresses.
3. **No new scope** — anything not in this map doesn't get done. Discipline is the strategy.
4. **Syahir ramps up on schedule** — Sep 10 checkpoint shows "partially ready" minimum. Full QC readiness by Sep 28.
5. **Hadri owns the T-30 gate chain** — Fuad provides technical content (Gates 1 + 3), Hadri owns consolidation and sign-off (Gates 2 + 4). Not on this map — it's Hadri's track.
6. **chain:SENTRY is NOT on this map** — Hadri owns it. If Fuad is pulled in, something else drops.

---

## 6. What's NOT On This Map (Deliberately Excluded)

| Item | Why Excluded | Owner |
|------|-------------|-------|
| chain:SENTRY Phase 0 | Hadri-owned. Not Fuad/Syahir capacity. | Hadri |
| Defensia WAF evaluation | Hadri-owned (reassigned Aug 29). | Hadri |
| CyberDSA Product Launch Checklist | Should be reassigned from Hadri. Amelia/Fuad split. | DAF to reassign |
| MCMC workshop coordination | Hadri-owned. | Hadri |
| HoE hiring process | DAF-owned. Post-October. | DAF |
| CSM stakeholder management | Hadri + Amelia. Not technical execution. | Hadri + Amelia |

This is the Technical Execution Unit's map. Everything else is someone else's track.

---

## 7. The Question

**Is this 2 FTE map feasible?**

Yes — with three conditions:
1. AIP-03 handover starts now and Syahir is absorbing by Sep 10
2. NDA signed by Sep 4 (otherwise Bursa slips but Fuad gets buffer)
3. No new scope enters the map. Zero. Anything new displaces something committed.

Without condition 1, the 2 FTE is nominal — Fuad carries everything, Syahir stays underutilized, and the SPOF persists despite the headcount.

Without condition 3, the map breaks. 2 FTE cannot absorb new scope through January. Every new ask gets gated: "What does it displace?"

---

*This map is the operational view of the Technical Execution Unit through January 2027. It feeds into the weekly Cognitive Loop and updates as deliverables close or slip.*
