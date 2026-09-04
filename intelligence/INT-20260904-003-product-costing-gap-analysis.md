---
id: INT-20260904-003
record_type: intelligence
title: "Product Costing & SKU Framework Gap Analysis — CognitiveOS Commercial Infrastructure Audit"
created_at: 2026-09-04T03:53:00+00:00
updated_at: 2026-09-04T03:53:00+00:00
owner: faurani-jaafar
intelligence_type: strategic
status: active
priority: critical
sensitivity: confidential
lifecycle_state: canonical
confidence: high
tags:
  - domain/commercial-development
  - domain/cybersecurity-productisation
  - domain/product-management
  - type/gap-analysis
  - type/commercial-infrastructure
  - portfolio/flagship
  - workstream/commercial-development
  - workstream/cybersec-products
source:
  type: cognitive-loop
  reference: "Directive B — Product Costing & SKU Framework Gap Analysis"
summary: "Comprehensive audit of CognitiveOS records for product costing, pricing, SKU, and commercialisation framework coverage. Finds that while top-line revenue projections and isolated pricing anchors exist (VoronCitadel RM 168k/368k, PaaS RM 688k envelope, Red Team Division RM 1.75M-3.8M), no systematic product costing methodology, module-level SKU structure, infrastructure cost allocation, labour cost model, licensing framework, packaging model, recurring operational cost model, deployment cost model, or margin methodology exists for any of the three flagship products. The commercial infrastructure gap is total and systemic."
strategic_significance: "Without product-level costing, the practice cannot build SKUs, cannot calculate margin per deployment, cannot price systematically, and cannot scale commercial operations beyond ad-hoc per-engagement negotiation. Every revenue projection in CognitiveOS is top-line only — no contribution margin, no cost-of-goods-sold, no unit economics. This blocks structured commercialisation at the most fundamental level."
mission_alignment:
  - commercial-development
  - cybersecurity-productisation
  - product-management
  - organisational-capability
related_records:
  - OPP-20260822-001
  - OPP-20260822-002
  - OPP-20260827-001
  - INIT-20260811-001
  - INIT-20260813-003
  - INIT-20260820-003
  - INIT-20260824-001
  - INIT-20260804-001
  - ASSESS-20260820-001
  - ART-20260822-003
  - ART-20260822-002
  - ESF-20260829-002
  - DOC-20260822-003
  - DEC-20260820-009
products:
  - voroncitadel
  - govsec-tip
  - chainsentry
  - teras
  - sovereign-ai-paas
  - voron-c2
---

# INT-20260904-003 — Product Costing & SKU Framework Gap Analysis

## Directive

**Source:** Directive B — Product Costing & SKU Framework Gap Analysis  
**Scope:** All CognitiveOS records containing pricing, costing, SKU, licensing, packaging, margin, or commercial model references  
**Products audited:** VoronCitadel, GovSec TIP, chain:SENTRY, Teras (infrastructure layer), Sovereign AI PaaS, VORON-C2  

---

## 1. Executive Summary

**Finding:** CognitiveOS contains **top-line revenue projections and isolated pricing anchors** but **no systematic product costing infrastructure** for any flagship product. The gap is total and systemic across all 11 assessed dimensions.

**Impact:** Without product-level costing, the practice cannot:
- Build module-level SKUs for structured sales
- Calculate contribution margin per deployment
- Price systematically (current pricing is ad-hoc, not cost-derived)
- Scale commercial operations beyond negotiation-per-deal
- Track unit economics or profitability per product
- Build a recurring revenue model with defensible margins

**Severity:** CRITICAL — this blocks structured commercialisation at the most fundamental level. Every revenue projection in the system is top-line only. No cost-of-goods-sold, no unit economics, no margin methodology exists for any product.

**Top-line revenue figures exist for:**
- VoronCitadel: RM 168k (early adopter) / RM 368k (retail) per licence — OPP-20260822-001
- VoronCitadel ARR: RM 414K (3 paying) → RM 1.104M (8 paying) — ASSESS-20260820-001
- Sovereign AI PaaS envelope: RM 688K first-year — INIT-20260813-003
- Project Hearth: RM 150K-300K setup + RM 138K-250K/year subscription + RM 15K-25K/month support — DOC-20260822-003
- Red Team Division: RM 1.75M-3.8M revenue, RM 612K-928K cost — RED-TEAM-DIVISION-STRUCTURE.md
- GTM programme: RM 205K-310K cost — ART-20260822-003

**What does NOT exist (for any product):**
- Costing methodology (how cost is calculated)
- Module-level costing (per-module cost breakdown)
- Infrastructure costing (Teras compute allocation per product)
- Labour/service costing (FTE allocation per product per deployment)
- Licensing model (terms, tiers, entitlements)
- Packaging model (what's in each tier/edition)
- Recurring operational cost model (ongoing cost per customer)
- Deployment cost model (cost to stand up a new customer)
- Margin assumption methodology (contribution margin per sale)
- Module-level SKU structure
- Product-level SKU structure

---

## 2. Per-Product Gap Assessment

### 2.1 VoronCitadel (GRC & Digital Risk Quantification)

**Pricing references found:**
| Source | Reference | Value |
|--------|----------|-------|
| OPP-20260822-001 | Early adopter price | RM 168,000 per licence |
| OPP-20260822-001 | Retail price | RM 368,000 per licence |
| ASSESS-20260820-001 | Existing paying customers | RM 138,000/year each (3 customers = RM 414K ARR) |
| ASSESS-20260820-001 | 18-month target | 8 customers × RM 138K = RM 1.104M ARR |
| ART-20260822-002 | Phase 1 revenue target | RM 168K-336K (1-2 sales) |
| ART-20260822-003 | 5-month revenue projection | RM 336K-504K (2-3 sales) |
| OPP-20260827-001 | RSWG Group 2 brokers | RM 168K-368K each (13 brokers) |
| OPP-20260827-001 | RSWG Group 1 brokers | RM 500K-1M each (11 brokers, enterprise) |
| OPP-20260827-001 | RSWG Group 3 brokers | RM 100K-200K each (6 brokers, niche) |
| DOC-20260822-003 | Project Hearth setup | RM 150K-300K |
| DOC-20260822-003 | Project Hearth subscription | RM 138K-250K/year |
| DOC-20260822-003 | Project Hearth support | RM 15K-25K/month |

**Critical inconsistency:** VoronCitadel has THREE different price points — RM 138K/year (existing), RM 168K (early adopter), RM 368K (retail). No document explains the relationship between these prices, what drives the differential, or what cost basis justifies any of them.

**Cost references found:**
| Source | Reference | Value |
|--------|----------|-------|
| ASSESS-20260820-001 | New hire cost (3 FTE) | RM 39,656/month total |
| ASSESS-20260820-001 | Bridge capital | ~RM 260,000 (6 months) |
| ASSESS-20260820-001 | Break-even | 4 paying customers (RM 552K > RM 476K) |
| ASSESS-20260820-001 | Hadri cost | RM 13,888/month |
| ASSESS-20260820-001 | HoE cost | RM 18,888/month |
| ASSESS-20260820-001 | CSE cost | RM 11,888/month |
| ASSESS-20260820-001 | Jr Backend cost | RM 8,888/month |
| ART-20260822-003 | GTM programme cost | RM 205K-310K |
| ART-20260822-003 | CyberDSA booth | RM 50K (confirmed quote) |

**Gap assessment:**

| Dimension | Exists? | Source | Notes |
|-----------|---------|--------|-------|
| Costing methodology | **N** | — | No methodology document. FTE costs in ASSESS-20260820-001 are practice-level, not per-product or per-deployment |
| Module-level costing | **N** | — | VoronCitadel has 4 modules (GRC, DRM, ASM, TPRM). No per-module cost exists |
| Infrastructure costing | **N** | — | Teras provides infrastructure (DEC-20260820-008/009). No cost allocation from Teras to VoronCitadel per deployment. "Infrastructure cost absorbed by Farul's org" (ASSESS-20260820-001) — unquantified |
| Labour/service costing | **N** | — | FTE model exists at practice level (ASSESS-20260820-001) but no allocation to VoronCitadel specifically vs other products. POC load math (80-120 hours/POC) exists but is not costed |
| Licensing model | **N** | — | "Per licence" used in OPP-20260822-001 but no licensing terms defined. What does a licence cover? Per org? Per user? Per module? Per deployment? Unknown |
| Packaging model | **N** | — | No edition/tier structure. No definition of what's included at RM 168K vs RM 368K. Is TPRM extra? Is ASM extra? Unknown |
| Recurring operational cost model | **N** | — | RM 138K/year is charged to existing customers but no model for what this covers (Teras compute? AI inference? Support? Updates? Monitoring?) |
| Deployment cost model | **N** | — | POC load (80-120 hours/POC) is quantified but not costed. No deployment fee structure |
| Margin assumption | **N** | — | LSN-20260823-001 explicitly flags: "revenue is not contribution margin." No margin calculation exists. Break-even analysis (ASSESS-20260820-001) compares top-line revenue to FTE salaries only — excludes Teras, overhead, GTM, and other costs |
| Module-level SKU | **N** | — | No SKU structure exists |
| Product-level SKU | **N** | — | No SKU structure exists |

**Additional notes:**
- INIT-20260811-001 states "Commercial pricing decisions handled by commercial readiness assessment, not this initiative" — but the commercial readiness assessment (ACT-20260811-004) has not been completed
- VoronCitadel MVP_SPECIFICATION.md and PRODUCT_BASELINE.md contain no pricing/costing information
- No product document defines what constitutes a "licence" or what entitlements it carries

---

### 2.2 GovSec TIP (National Cyber Threat Intelligence Platform)

**Pricing references found:**
- No direct pricing references for GovSec TIP found in any CognitiveOS record

**Cost references found:**
- FTE allocation: Fuad ~0.3 FTE across ALL 3 products (not isolated to GovSec TIP)
- Hadri RM 13,888/month across 4 CSM tracks (not isolated to GovSec TIP)
- No GovSec-specific infrastructure cost identified (assumed on Teras, unquantified)

**Gap assessment:**

| Dimension | Exists? | Source | Notes |
|-----------|---------|--------|-------|
| Costing methodology | **N** | — | None |
| Module-level costing | **N** | — | GovSec has 4 domains (TI/Ingest, Analysis/Detection, Alerting/Response, Governance/Compliance). No per-domain cost |
| Infrastructure costing | **N** | — | Teras GPU compute for AI Analyst unquantified. Air-gapped deployment cost unquantified |
| Labour/service costing | **N** | — | No FTE allocation to GovSec TIP specifically |
| Licensing model | **N** | — | No licensing terms. Government agency licensing model undefined |
| Packaging model | **N** | — | No edition/tier structure. Multi-agency deployment isolation model undefined commercially |
| Recurring operational cost model | **N** | — | No recurring revenue model. No operational cost model |
| Deployment cost model | **N** | — | No deployment cost structure. Air-gapped/on-premise deployment cost unquantified |
| Margin assumption | **N** | — | No margin model |
| Module-level SKU | **N** | — | No SKU |
| Product-level SKU | **N** | — | No SKU |

**Additional notes:**
- GovSec TIP MVP_SPECIFICATION.md (50,956 bytes) contains zero pricing information
- GovSec TIP roadmap (DOC-20260821-004) contains no commercial pricing
- INIT-20260811-001 flags GovSec commercialisation as "Partial" — CyberDSA October is the commercial launch event, but no commercial framework exists
- ESF-20260829-002 DoD-4 tracks GovSec roadmap delivery but no commercial/costing framework

---

### 2.3 chain:SENTRY (Blockchain Forensics & Investigative Intelligence Workbench)

**Pricing references found:**
- No direct pricing references for chain:SENTRY found in any CognitiveOS record

**Cost references found:**
- No chain:SENTRY-specific cost identified
- Fuad ~0.3 FTE across ALL 3 products (not isolated to chain:SENTRY)

**Gap assessment:**

| Dimension | Exists? | Source | Notes |
|-----------|---------|--------|-------|
| Costing methodology | **N** | — | None |
| Module-level costing | **N** | — | chain:SENTRY has multiple capabilities (address scoring, sanctions screening, case management, transaction graphs, monitoring). No per-capability cost |
| Infrastructure costing | **N** | — | Teras GPU for assisted classification unquantified. OCR/Translation services unquantified |
| Labour/service costing | **N** | — | No FTE allocation to chain:SENTRY |
| Licensing model | **N** | — | No licensing terms. Investigation platform licensing model undefined |
| Packaging model | **N** | — | No edition/tier structure |
| Recurring operational cost model | **N** | — | No recurring revenue model |
| Deployment cost model | **N** | — | No deployment cost. Air-gapped for sensitive investigations — unquantified |
| Margin assumption | **N** | — | No margin model |
| Module-level SKU | **N** | — | No SKU |
| Product-level SKU | **N** | — | No SKU |

**Additional notes:**
- chain:SENTRY MVP_SPECIFICATION.md (62,090 bytes) contains zero pricing information
- INIT-20260811-001 flags chain:SENTRY commercialisation as "Partial" — "requires commercial model development"
- RSK-20260829-002 (chain:SENTRY Knowledge Transfer Gap) highlights product risk but no commercial framework

---

### 2.4 Teras AI Platform (Infrastructure Layer)

**Pricing references found:**
- No standalone Teras pricing found
- DOC-20260822-003 references RM 138K-250K/year "Teras compute + CognitiveOS + applications" but this is bundled, not Teras-alone

**Cost references found:**
- Hardware: 4× NVIDIA RTX PRO 6000 Blackwell (cost not stated)
- ASSESS-20260820-001: "Infrastructure (Teras): cost absorbed by Farul's org (not CyberSec Practice cost)" — unquantified transfer pricing

**Gap assessment:**

| Dimension | Exists? | Source | Notes |
|-----------|---------|--------|-------|
| Costing methodology | **N** | — | No methodology for Teras cost allocation to products |
| Infrastructure costing | **N** | — | Hardware cost unquantified. GPU-hours per product unquantified. Power/cooling unquantified |
| Transfer pricing model | **N** | — | "Absorbed by Farul's org" is not a transfer pricing model. No internal chargeback mechanism defined |
| Per-product infrastructure allocation | **N** | — | No model for how much Teras cost each product consumes |
| Margin on infrastructure | **N** | — | No margin model for infrastructure layer |

**Critical gap:** Teras is the infrastructure layer for ALL 3 products (DEC-20260820-009). Without Teras cost allocation, no product can have accurate COGS. The "absorbed by Farul's org" assumption masks the true cost of every product.

---

### 2.5 Sovereign AI PaaS (CSM-Aras Commercial Model)

**Pricing references found:**
- INIT-20260813-003: "first-year commercial envelope around RM 688,000"
- 4-layer architecture defined (Infrastructure → AI Platform → Managed Services → Applications)

**Cost references found:**
- No PaaS-specific cost breakdown found
- No layer-level costing (Layer 1 compute cost, Layer 2 platform cost, Layer 3 managed service cost, Layer 4 application cost)

**Gap assessment:**

| Dimension | Exists? | Source | Notes |
|-----------|---------|--------|-------|
| Costing methodology | **N** | — | None. RM 688K is a commercial envelope, not a costed model |
| Layer-level costing | **N** | — | 4-layer architecture defined but no per-layer cost |
| Recurring revenue model | **N** | — | "Recurring PaaS / managed sovereign AI relationship" stated but no recurring revenue structure |
| Licensing model | **N** | — | No PaaS licensing terms |
| Packaging model | **N** | — | No tier/edition structure for PaaS offering |
| Margin assumption | **N** | — | None |

---

### 2.6 VORON-C2 / Red Team Division

**Pricing references found:**
- RED-TEAM-DIVISION-STRUCTURE.md: 7 service lines with revenue ranges (RM 50K-1M per service)
- Total Year 1 revenue: RM 1.75M (conservative) to RM 3.8M (target)
- Dark web monitoring: RM 3K-8K/month per client

**Cost references found:**
- RED-TEAM-DIVISION-STRUCTURE.md: Personnel RM 552K-828K, Infrastructure RM 30K-50K, Tooling RM 10K-20K, Training RM 20K-30K = Total RM 612K-928K
- Gross Margin: RM 1.0M (Year 1), RM 2.95M (Year 2)
- VORON-C2: $0 licensing (open-source stack)

**Gap assessment:**

| Dimension | Exists? | Source | Notes |
|-----------|---------|--------|-------|
| Costing methodology | **P** | RED-TEAM-DIVISION-STRUCTURE.md | Partial — cost categories defined but not per-engagement |
| Service-line costing | **P** | RED-TEAM-DIVISION-STRUCTURE.md | Partial — revenue per service line defined, cost per service line not isolated (personnel cost is pooled) |
| Infrastructure costing | **P** | RED-TEAM-DIVISION-STRUCTURE.md | Partial — RM 30K-50K aggregate, not per service line |
| Labour costing | **P** | RED-TEAM-DIVISION-STRUCTURE.md | Partial — 5 FTE with individual salaries, but allocation per service line not defined |
| Licensing model | **Y** | RED-TEAM-DIVISION-STRUCTURE.md | $0 licensing (open-source) — defined for VORON-C2 |
| Packaging model | **P** | RED-TEAM-DIVISION-STRUCTURE.md | Partial — 7 service lines defined with pricing, but no edition/tier structure |
| Recurring operational cost model | **P** | RED-TEAM-DIVISION-STRUCTURE.md | Partial — subscription retainer for dark web monitoring defined |
| Deployment cost model | **N** | — | No per-engagement deployment cost |
| Margin assumption | **P** | RED-TEAM-DIVISION-STRUCTURE.md | Partial — gross margin calculated (RM 1.0M Year 1) but methodology is revenue minus aggregate cost, not per-engagement |
| Module-level SKU | **N** | — | No SKU per service line |
| Product-level SKU | **N** | — | No division-level SKU |

**Note:** Red Team Division has the most developed commercial framework in CognitiveOS, but it is still partial. It is also a separate division, not one of the 3 flagship products.

---

## 3. Cross-Product Gap Matrix

| Dimension | VoronCitadel | GovSec TIP | chain:SENTRY | Teras | PaaS | Red Team |
|-----------|-------------|------------|-------------|-------|------|----------|
| Costing methodology | ❌ | ❌ | ❌ | ❌ | ❌ | ⚠️ Partial |
| Module-level costing | ❌ | ❌ | ❌ | N/A | ❌ | ❌ |
| Infrastructure costing | ❌ | ❌ | ❌ | ❌ | ❌ | ⚠️ Partial |
| Labour/service costing | ❌ | ❌ | ❌ | N/A | ❌ | ⚠️ Partial |
| Licensing model | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ ($0 OSS) |
| Packaging model | ❌ | ❌ | ❌ | ❌ | ❌ | ⚠️ Partial |
| Recurring op cost model | ❌ | ❌ | ❌ | ❌ | ❌ | ⚠️ Partial |
| Deployment cost model | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Margin assumption | ❌ | ❌ | ❌ | ❌ | ❌ | ⚠️ Partial |
| Module-level SKU | ❌ | ❌ | ❌ | N/A | ❌ | ❌ |
| Product-level SKU | ❌ | ❌ | ❌ | N/A | ❌ | ❌ |

**Legend:** ✅ = Exists | ⚠️ Partial = Partially defined | ❌ = Missing | N/A = Not applicable

---

## 4. Existing Pricing References (Consolidated)

### 4.1 VoronCitadel Price Points

| Price | Context | Source | Notes |
|-------|---------|--------|-------|
| RM 138,000/year | Existing paying customers (3) | ASSESS-20260820-001 | What this covers is undefined. Appears to be annual subscription |
| RM 168,000 | Early adopter price | OPP-20260822-001 | "Per licence" — licence terms undefined |
| RM 368,000 | Retail price | OPP-20260822-001 | "Per licence" — licence terms undefined |
| RM 500K-1M | Enterprise (Group 1 brokers) | OPP-20260827-001 | "Integration/partnership level" |
| RM 100K-200K | Niche (Group 3 brokers) | OPP-20260827-001 | "Local compliance adaptation" |

**Critical issue:** The price spread from RM 138K to RM 500K+ is 3.6× with no documented rationale for the differential. No document explains:
- Whether RM 138K is a legacy/grandfathered price
- Whether RM 168K is a time-limited early adopter price
- Whether RM 368K is the standard going-forward price
- Whether RM 500K-1M includes services beyond the software licence
- What cost basis justifies any of these price points

### 4.2 Project Hearth / CognitiveOS Pricing

| Price | Context | Source |
|-------|---------|--------|
| RM 150K-300K | Setup and configuration | DOC-20260822-003 |
| RM 138K-250K/year | Annual subscription (Teras + CognitiveOS + apps) | DOC-20260822-003 |
| RM 15K-25K/month | Cognitive partner support (ongoing advisory) | DOC-20260822-003 |
| RM 3M+ ARR | Cognitive infrastructure layer revenue target | DOC-20260822-003 |

### 4.3 Sovereign AI PaaS

| Price | Context | Source |
|-------|---------|--------|
| RM 688,000 | First-year commercial envelope | INIT-20260813-003 |

### 4.4 GTM Programme

| Cost | Context | Source |
|------|---------|--------|
| RM 205K-310K | 5-month GTM programme cost | ART-20260822-003 |
| RM 175K-295K | Original GTM strategy budget | ART-20260822-001 (VoronCitadel_GTM_Strategy_Final_Draft) |
| RM 50K | CyberDSA booth (confirmed quote) | ART-20260822-003 |

### 4.5 Red Team Division

| Revenue | Context | Source |
|---------|---------|--------|
| RM 500K-1M | Government red team engagement | RED-TEAM-DIVISION-STRUCTURE.md |
| RM 400K-800K | Commercial red team engagement | RED-TEAM-DIVISION-STRUCTURE.md |
| RM 300K-600K | Dark web intelligence service (retainer) | RED-TEAM-DIVISION-STRUCTURE.md |
| RM 200K-500K | Purple team / detection engineering | RED-TEAM-DIVISION-STRUCTURE.md |
| RM 200K-400K | National cyber exercise | RED-TEAM-DIVISION-STRUCTURE.md |
| RM 100K-300K | Training & certification | RED-TEAM-DIVISION-STRUCTURE.md |
| RM 50K-200K | Vulnerability research / advisories | RED-TEAM-DIVISION-STRUCTURE.md |
| RM 3K-8K/month | Dark web monitoring per client | RED-TEAM-DIVISION-STRUCTURE.md |
| RM 612K-928K | Year 1 total cost | RED-TEAM-DIVISION-STRUCTURE.md |
| RM 1.0M | Year 1 gross margin | RED-TEAM-DIVISION-STRUCTURE.md |

### 4.6 FTE Cost Model (Practice-Level, Not Product-Level)

| Role | Monthly (RM) | Annual (RM) | Source |
|------|-------------|-------------|--------|
| Head of Engineering | 18,888 | 226,656 | ASSESS-20260820-001 |
| Customer Success Engineer | 11,888 | 142,656 | ASSESS-20260820-001 |
| Junior Backend Engineer | 8,888 | 106,656 | ASSESS-20260820-001 |
| Hadri (existing) | 13,888 | 166,656 | ASSESS-20260820-001 |
| 3 new hires total | 39,656 | 475,968 | ASSESS-20260820-001 |
| Fuad (existing) | Not stated | — | ASSESS-20260820-001 |
| DAF (existing) | Not stated | — | ASSESS-20260820-001 |

---

## 5. Existing Commercial Framework References

### 5.1 Documents That Reference Commercial Models

| Document | What It Contains | What It Lacks |
|----------|-------------------|---------------|
| INIT-20260813-003 (CSM-Aras PaaS) | 4-layer architecture, RM 688K envelope | Layer costing, recurring revenue structure, licensing terms |
| INIT-20260820-003 (VoronCitadel POC Mode) | FTE model, bridge capital, break-even | Per-product costing, per-deployment costing, margin model |
| ASSESS-20260820-001 (FTE Model) | FTE costs, break-even at 4 customers | Contribution margin, COGS, Teras cost, overhead allocation |
| OPP-20260822-001 (Revenue Projection) | Conversion funnel, RM 1.176M projection | Cost per acquisition, cost per POC, margin per sale |
| ART-20260822-003 (GTM Outcomes) | GTM cost model (RM 205-310K), ROI model | Marketing overhead, CRM cost, per-lead cost, per-POC cost |
| OPP-20260822-002 (MQL Framework) | MQL = "requested a meeting", framework concept | Cost per MQL, conversion economics, per-product targets |
| DOC-20260822-003 (Project Hearth) | 3-tier pricing (setup + subscription + support) | Cost basis, margin, COGS breakdown |
| RED-TEAM-DIVISION-STRUCTURE.md | Revenue per service line, aggregate cost, gross margin | Per-engagement costing, per-service-line cost isolation |

### 5.2 Documents That SHOULD Contain Costing But Don't

| Document | What It Is | What's Missing |
|----------|-----------|---------------|
| products/voroncitadel/PRODUCT_BASELINE.md | Product baseline | Zero pricing/costing |
| products/voroncitadel/MVP_SPECIFICATION.md | Full MVP spec | Zero pricing/costing |
| products/govsec-tip/MVP_SPECIFICATION.md | Full MVP spec | Zero pricing/costing |
| products/chainsentry/MVP_SPECIFICATION.md | Full MVP spec | Zero pricing/costing |
| products/teras/PLATFORM_OVERVIEW.md | Platform overview | Zero pricing/costing |
| INIT-20260811-001 (Product Consolidation) | Productisation programme | ACT-20260811-004 (commercialisation readiness) not completed |

---

## 6. Dependency Contradictions

### 6.1 Commercialisation Deliverable Due Before Upstream Dependency

| Deliverable | Due | Upstream Dependency | Status | Impact |
|-------------|-----|-------------------|--------|--------|
| VoronCitadel sales at RM 168K (OPP-20260822-001) | 2026-Q4 to 2027-Q1 | No licensing model defined | ❌ Blocked | Cannot sell a "licence" without licence terms |
| VoronCitadel POC conversion to paying (INIT-20260820-003) | 4-6 months after POC start | No packaging model (what POC customers get vs paying customers) | ❌ Blocked | Cannot convert POC to sale without packaging definition |
| Bursa POC (INIT-20260824-001) | 4 months | POC cost model (what does the POC cost Aras?) | ❌ Unquantified | Cannot price the POC or the post-POC commercial terms |
| GovSec TIP CyberDSA launch (INIT-20260810-003) | October 2026 | No commercial model for GovSec TIP | ❌ Blocked | Cannot launch commercially without pricing |
| Sovereign AI PaaS RM 688K envelope (INIT-20260813-003) | Active | No layer-level costing | ⚠️ At risk | Cannot validate whether RM 688K covers cost |
| Break-even at 4 paying customers (ASSESS-20260820-001) | Month 10-12 | Teras cost unquantified, Fuad/DAF salary excluded | ⚠️ At risk | Break-even claim is incomplete |
| Red Team Division RM 1.75M revenue (RED-TEAM-DIVISION-STRUCTURE.md) | Month 12 | No per-engagement costing | ⚠️ At risk | Cannot validate margin per engagement |
| ACT-20260811-004 (Commercialisation Readiness) | Not started | Product documentation complete | ❌ Not started | Blocks all commercial readiness assessment |

### 6.2 Circular Dependencies

1. **Pricing → Costing → Pricing:** Current prices (RM 138K/168K/368K) appear to be market-based or arbitrary, not cost-derived. Without costing, prices cannot be validated. Without prices, costing cannot be validated against margin targets. This is a circular dependency that must be broken by establishing costing first.

2. **Licence definition → SKU → Pricing:** A "licence" is referenced in OPP-20260822-001 but licence terms are undefined. Without licence terms, SKU structure cannot be built. Without SKU structure, pricing cannot be systematically applied. Without pricing, licence value cannot be defined.

3. **Teras cost → Product COGS → Product Pricing:** Teras is the infrastructure for all 3 products. Without Teras cost allocation, product COGS is unknown. Without COGS, pricing is arbitrary. Without valid pricing, commercial model is unvalidated.

---

## 7. Identified Gaps — Prioritized

### Priority 1 — Blocks All Commercialisation (Must-Have Before First Sale)

| # | Gap | Impact | Products Affected |
|---|-----|--------|-------------------|
| G1 | No costing methodology | Cannot derive price from cost | All products |
| G2 | No licensing model | Cannot define what a "licence" covers | VoronCitadel, GovSec TIP, chain:SENTRY |
| G3 | No packaging model | Cannot define editions/tiers | VoronCitadel, GovSec TIP, chain:SENTRY |
| G4 | No product-level SKU | Cannot sell systematically | All products |
| G5 | No Teras cost allocation | Product COGS unknown | All Teras-dependent products |
| G6 | No margin methodology | Cannot validate pricing viability | All products |

### Priority 2 — Blocks Scaled Commercial Operations

| # | Gap | Impact | Products Affected |
|---|-----|--------|-------------------|
| G7 | No module-level costing | Cannot price modules separately | VoronCitadel (4 modules), GovSec TIP (4 domains), chain:SENTRY (multiple capabilities) |
| G8 | No module-level SKU | Cannot sell modules separately | All products |
| G9 | No deployment cost model | Cannot price deployments | All products |
| G10 | No recurring operational cost model | Cannot validate subscription pricing | All products |
| G11 | No labour allocation per product | Cannot determine product profitability | All products |
| G12 | No POC cost model | Cannot price POCs or determine POC-to-sale conversion cost | VoronCitadel, GovSec TIP |

### Priority 3 — Blocks Commercial Optimisation

| # | Gap | Impact | Products Affected |
|---|-----|--------|-------------------|
| G13 | No cost-per-MQL model | Cannot optimise GTM spend | VoronCitadel |
| G14 | No cost-per-POC model | Cannot optimise POC pipeline | VoronCitadel |
| G15 | No contribution margin per sale | Cannot rank deals by profitability | All products |
| G16 | No transfer pricing for Teras | Cannot allocate infrastructure cost fairly | All products |
| G17 | No service-level cost for Red Team | Cannot optimise service mix | Red Team Division |

---

## 8. Pricing Inconsistencies

| Issue | Details | Risk |
|-------|---------|------|
| 3 price points for VoronCitadel | RM 138K (existing), RM 168K (early adopter), RM 368K (retail) — no documented rationale | Customer confusion, margin erosion, sales team uncertainty |
| Project Hearth overlaps VoronCitadel pricing | RM 138K-250K/year subscription includes "Teras + CognitiveOS + applications" — is this the same as VoronCitadel RM 138K/year? | Product boundary confusion, potential cannibalisation |
| "Per licence" undefined | OPP-20260822-001 uses "per licence" but no document defines what a licence is | Legal/commercial risk |
| RSWG pricing 3.6× spread | RM 100K-1M across 3 broker groups — no cost basis for differential | May leave margin on the table or price below cost |
| Red Team Division revenue vs cost gap | RM 1.75M revenue, RM 612K-928K cost — but personnel cost is pooled, not per service line | Cannot identify which services are profitable |
| Break-even excludes key costs | ASSESS-20260820-001 break-even (4 customers × RM 138K = RM 552K > RM 476K) excludes Teras, DAF/Fuad salaries, GTM, overhead | Break-even claim is overstated |

---

## 9. What Exists vs What's Needed

### What Exists (Fragmented, Top-Line Only)

1. ✅ Revenue projections (VoronCitadel funnel, Red Team service lines, PaaS envelope)
2. ✅ FTE cost model (practice-level, ASSESS-20260820-001)
3. ✅ GTM programme cost (ART-20260822-003)
4. ✅ VoronCitadel price points (3 points, undefined basis)
5. ✅ Red Team Division revenue/cost structure (partial)
6. ✅ Project Hearth pricing tiers (setup + subscription + support)
7. ✅ Break-even analysis (incomplete — ASSESS-20260820-001)

### What's Needed (Systematic, Bottom-Up)

1. ❌ Product costing methodology (how cost is calculated per product)
2. ❌ Module-level costing (per-module cost for each product)
3. ❌ Infrastructure cost allocation (Teras → products)
4. ❌ Labour allocation model (FTE % per product, per deployment)
5. ❌ Licensing framework (terms, entitlements, restrictions, tiers)
6. ❌ Packaging model (editions, what's included, what's extra)
7. ❌ SKU structure (product-level and module-level)
8. ❌ Recurring operational cost model (per-customer ongoing cost)
9. ❌ Deployment cost model (per-new-customer setup cost)
10. ❌ Margin methodology (contribution margin per sale, per product)
11. ❌ POC cost model (cost to run a POC, POC-to-sale conversion cost)
12. ❌ Teras transfer pricing mechanism (internal chargeback)
13. ❌ Commercialisation readiness assessment (ACT-20260811-004 — not started)

---

## 10. Recommendations

### Immediate (Before Any New Commercial Engagement)

1. **Define VoronCitadel licensing model** — What does a "licence" cover? Per org? Per deployment? Per user? Per module? Time-limited or perpetual? This is the gating dependency for all VoronCitadel commercial activity.

2. **Define VoronCitadel packaging model** — What's included at RM 168K vs RM 368K? Is TPRM extra? Is ASM extra? Is AI Copilot included? This determines whether the 3 price points are editions or discounts.

3. **Allocate Teras cost to products** — Even a rough allocation (e.g., GPU-hours per product × cost per GPU-hour) would make COGS estimable. Without this, no product has accurate cost.

4. **Complete ACT-20260811-004 (Commercialisation Readiness)** — This was identified as the action for commercialisation readiness in INIT-20260811-001 but has not been started. It's 18 days overdue.

### Short-Term (Before Scaled Commercial Operations)

5. **Build VoronCitadel module-level costing** — 4 modules (GRC, DRM, ASM, TPRM). Allocate FTE time, infrastructure, and overhead per module.

6. **Build VoronCitadel SKU structure** — Product-level SKU + module-level SKUs. Define SKU codes, descriptions, and entitlements.

7. **Build deployment cost model** — How much does it cost to stand up a new VoronCitadel customer? POC setup + production setup + training + handover.

8. **Build recurring operational cost model** — Per-customer ongoing cost: Teras compute, AI inference, monitoring, support, updates.

9. **Build margin methodology** — Contribution margin per sale = price - COGS (Teras allocation + deployment labour + ongoing operational cost allocation).

10. **Repeat for GovSec TIP and chain:SENTRY** — Same framework, different products.

### Medium-Term (Before Commercial Optimisation)

11. **Build POC cost model** — Cost per POC (80-120 hours × hourly rate + infrastructure + support).

12. **Build cost-per-MQL model** — GTM spend / MQLs generated.

13. **Build transfer pricing mechanism for Teras** — Internal chargeback from products to infrastructure.

14. **Validate Red Team Division per-service-line costing** — Isolate personnel cost per service line.

---

## 11. Methodology Note

**Assessment method:** Full-text grep of all `.md` files in `strategic-cognitiveos/` for 15 search terms (case-insensitive): "costing", "cost template", "SKU", "pricing", "price", "margin", "licensing", "packaging", "selling price", "commercial model", "revenue", "RM ", "licence", "license", "subscription". Followed by targeted reading of 20 key records.

**Records read in full:** OPP-20260822-001, OPP-20260822-002, OPP-20260827-001, INIT-20260811-001, INIT-20260813-003, INIT-20260820-003, INIT-20260824-001, INIT-20260804-001, ASSESS-20260820-001, ART-20260822-003, ART-20260822-002, ESF-20260829-002, DOC-20260822-003, VoronCitadel_GTM_Strategy_Final_Draft.md, VoronCitadel PRODUCT_BASELINE.md, VoronCitadel MVP_SPECIFICATION.md, GovSec TIP MVP_SPECIFICATION.md (partial), chain:SENTRY MVP_SPECIFICATION.md (partial), Teras PLATFORM_OVERVIEW.md, RED-TEAM-DIVISION-STRUCTURE.md (partial)

**Files not found:** INIT-20260813-007 through INIT-20260813-010 — these files do not exist in the initiatives directory. The INIT-20260813 series only goes to 006.

**Confidence:** High — the grep was comprehensive across all `.md` files. The targeted reading covered all records specified in the directive plus additional records surfaced by grep results.

---

## 12. Conclusion

**The CognitiveOS repository contains no product costing infrastructure.** Top-line revenue projections exist for VoronCitadel and Red Team Division, and isolated pricing anchors exist for VoronCitadel (RM 138K/168K/368K), Project Hearth (RM 150-300K setup + RM 138-250K/year), and Sovereign AI PaaS (RM 688K envelope). However, no systematic costing methodology, SKU structure, licensing framework, packaging model, or margin methodology exists for any of the three flagship products.

**The gap is not partial — it is total.** Every dimension assessed (costing methodology, module-level costing, infrastructure costing, labour costing, licensing, packaging, recurring op cost, deployment cost, margin, module SKU, product SKU) is absent for VoronCitadel, GovSec TIP, and chain:SENTRY. Red Team Division has partial coverage but is a separate division, not a flagship product.

**This blocks structured commercialisation at the most fundamental level.** Without costing, the practice cannot build SKUs, cannot calculate margin, cannot price systematically, and cannot scale beyond ad-hoc negotiation. The first VoronCitadel sale at RM 168K will occur without a defined licence, without a cost basis, without a margin calculation, and without a SKU. This is commercial risk.

**The immediate priority is to define VoronCitadel licensing and packaging models** (what is being sold), **allocate Teras cost** (what infrastructure costs), and **complete ACT-20260811-004** (the overdue commercialisation readiness assessment that was supposed to answer these questions).
