---
id: ART-20260822-003
record_type: artifact
title: "VoronCitadel GTM — Quantifiable Outcome Model (Corrected)"
created_at: 2026-08-22T08:22:00+00:00
owner: daf
artifact_type: financial-model
status: active
sensitivity: confidential
lifecycle_state: draft
tags:
  - domain/commercial-development
  - domain/cybersecurity-productisation
  - workstream/commercial-development
related_records:
  - ART-20260822-001
  - INIT-20260822-002
  - OPP-20260822-001
---

# VoronCitadel GTM — Quantifiable Outcome Model

**Purpose:** Bridge Said's GTM Strategy (9 initiatives, stops at 3 pilots) to DAF's revenue model (7 sales, RM 1.176M). Add cost recovery and ROI.

**Basis:** Said's strategic framework + DAF's conversion model + Hazdi's confirmed CyberDSA quote (RM 50k).

---

## 1. Corrected Cost Model

| Layer | Initiative | Said's Estimate (RM) | Corrected (RM) | Basis |
|-------|-----------|----------------------|----------------|-------|
| 1 | CSM LOI | 0 | 0 | No cost |
| 1 | Email outreach | 20-35k | 20-35k | Unchanged (indicative) |
| 1 | Partner referral | 0 upfront | 0 upfront | Unchanged |
| 2 | LinkedIn thought leadership | 30-50k | 30-50k | Unchanged |
| 2 | GRC in 60 Seconds | 15-30k | 15-30k | Unchanged |
| 2 | BFM Radio PR | 30-60k | 30-60k | Unchanged |
| 3 | CyberDSA 2026 | 20-35k | **50k** | Hazdi confirmed quote |
| 3 | Executive Roundtable | 45-60k | 45-60k | Unchanged |
| 3 | Workshops & Briefings | 15-25k | 15-25k | Unchanged |
| — | Marketing overhead | Not budgeted | **TBD** | DAF flagged, needs quantification |
| — | CRM (HubSpot) | Not budgeted | **TBD** | Required for execution |

**Corrected total (excluding TBD items):** RM 205k–310k (was RM 175-295k)

**With CyberDSA correction alone:** Floor rises RM 15-30k. Every TBD item pushes it further.

---

## 2. Funnel Model (Said's → DAF's)

| Stage | Said's Target | DAF's Model | Reconciled Target | Conversion Rate |
|-------|--------------|-------------|-------------------|----------------|
| Targeted contacts | 300 | 1,300 | 300 (Said's 5-month scope) | — |
| Engaged | — | 260 (20%) | 60 (20%) | 20% of contacts |
| First meetings | 40 | 78 (30%) | 40 (Said's target) | 67% of engaged |
| GRC readiness assessments | 15 | — | 15 | 38% of meetings |
| POCs / Pilots | 3 | 23 (30%) | 5 | 33% of assessments |
| Sales | Not projected | 7 (30%) | 2-3 | 40-60% of POCs |
| Revenue | Not projected | RM 1.176M | RM 336k-504k | See pricing below |

**Reconciliation logic:**
- Said's 300 contacts is the 5-month GTM programme scope (Layer 1-3 activated)
- DAF's 1,300 is the total prospect database — the full universe, not all reached in 5 months
- DAF's 23 POCs is a longer-term pipeline (12-18 months), not 5 months
- 5-month realistic: 300 → 60 engaged → 40 meetings → 15 assessments → 5 POCs → 2-3 sales

---

## 3. Revenue Projection

| Scenario | POCs | Conversion | Sales | ASP | Revenue |
|----------|------|-----------|-------|-----|---------|
| Conservative | 5 | 40% | 2 | RM 168k | RM 336k |
| Base case | 5 | 50% | 2.5 (~3) | RM 168k | RM 504k |
| Aggressive | 5 | 60% | 3 | RM 168k | RM 504k |

**ASP basis:** VoronCitadel early adopter pricing RM 168k (from OPP-20260822-001)

**Note:** DAF's RM 1.176M model (7 sales) is a 12-18 month pipeline outcome. The 5-month GTM programme initiates the funnel; revenue closes over a longer horizon. Both are correct — different timeframes.

---

## 4. ROI Model

| Scenario | Cost (low) | Cost (high) | Revenue | ROI (low) | ROI (high) |
|----------|-----------|-------------|---------|-----------|------------|
| Conservative | RM 205k | RM 310k | RM 336k | 0.08x | -0.08x |
| Base case | RM 205k | RM 310k | RM 504k | 0.63x | 1.45x |
| Aggressive | RM 205k | RM 310k | RM 504k | 0.63x | 1.45x |

**Key insight:** At the corrected cost floor (RM 205k), the base case delivers 1.45x ROI on the low-cost estimate but only 0.63x on the high end. The programme is justified if:
1. Costs stay at the lower bound, AND
2. At least 3 POCs convert to sales within the pipeline window

**Marketing overhead and CRM costs are not yet in this model.** Both will compress ROI further.

---

## 5. Pipeline Timeline

```
Aug    Sep    Oct    Nov    Dec    Jan    Feb    Mar
─────  ─────  ─────  ─────  ─────  ─────  ─────  ─────
Foundation → Publish → Scale → Convert → Close → Pipeline continues
                                        │
                                        ├── 1st meetings → assessments
                                        ├── CyberDSA → meetings → assessments  
                                        ├── Roundtable → assessments
                                        └── Workshops → POCs → sales (Jan-Mar)
```

**Revenue realisation:** POCs start Nov/Dec. Sales close Jan-Mar 2027. GTM programme cost is Aug-Dec. Revenue lag is 2-4 months after programme end.

---

## 6. What's Missing (TBD Items for Tuesday)

| Item | Who Needs to Answer | Impact |
|------|-------------------|--------|
| Marketing overhead quantification | DAF / Finance | Adds to cost, reduces ROI |
| CRM budget (HubSpot or alt) | DAF / IT | Required for email outreach + tracking |
| Layer 2 budget ownership (whose P&L) | DAF / CSM / Marketing | Determines who funds RM 75-140k |
| Execution capacity (who runs it) | DAF / Norshaza | If under-resourced, funnel collapses |
| Partner recruitment timeline | DAF / Said | If Oct start, misses Sep outreach window |
| Sales team to close POCs | DAF / Hadri | POCs without closers = no revenue |

---

## 7. Summary for Tuesday

**The ask:** Align on corrected costs, quantifiable revenue outcome, and execution ownership.

**One-line version:** "RM 205-310k investment over 5 months generates 300 contacts → 40 meetings → 15 assessments → 5 POCs → 2-3 sales worth RM 336-504k, with revenue realising Jan-Mar 2027."

**The gap:** Said's deck has the strategy. DAF has the numbers. Tuesday merges them.
