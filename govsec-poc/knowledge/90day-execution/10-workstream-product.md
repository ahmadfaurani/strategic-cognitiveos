# KB-90DAY-WS-004: Product Workstream — Solution Packaging, MVP, Roadmap

**Knowledge Unit ID:** KB-90DAY-WS-004  
**Version:** 1.0  
**Classification:** TLP:AMBER (Internal Operational)  
**Created:** 2026-04-25  
**Owner:** Hadri (Solutions Architect)  
**Status:** Active — Daily Execution Guidance  

---

## Purpose

**Package solutions into product-ready modules with clear capabilities, positioning, roadmap, and differentiation for Aras-CSM 90-day execution plan.**

---

## Solution Portfolio

### 1. GovSec Threat Intelligence Platform

| Attribute | Value |
|-----------|-------|
| **Target** | Government agencies, ministries, national security |
| **Core Capability** | Multi-source threat intel ingestion, correlation, alerting |
| **Key Features** | SpankRAT detection, LotL C2 monitoring, dark web analysis, MISP integration |
| **Tech Stack** | AIL Framework, OC-CIL, MISP, Suricata, Neo4j |
| **Deployment** | Sovereign, air-gapped capable |
| **POC Scope** | 4-6 weeks, behavioral detection, <15min TTD |
| **Revenue Model** | RM 100K-200K (POC), RM 500K-1.5M (deployment), RM 300K-800K/year (subscription) |
| **Annual Revenue Target** | RM 5M/year |

---

### 2. Digital Risk Quantification (DRQ) GRC Platform

| Attribute | Value |
|-----------|-------|
| **Target** | Financial institutions, regulators (BNM, MCMC), GLCs |
| **Core Capability** | Risk scoring, GRC reporting, board-level metrics |
| **Key Features** | Quantitative risk modeling, scenario analysis, regulatory reporting |
| **Tech Stack** | OC-CIL, Qwen3.5, Neo4j, BGE-M3 |
| **Deployment** | Cloud or on-prem |
| **POC Scope** | 4-6 weeks, risk model validation, board-ready reports |
| **Revenue Model** | RM 100K-200K (POC), RM 500K-1.5M (deployment), RM 300K-800K/year (subscription) |
| **Annual Revenue Target** | RM 6M/year |

---

### 3. Blockchain Intelligence Platform

| Attribute | Value |
|-----------|-------|
| **Target** | Law enforcement, central banks, FIUs |
| **Core Capability** | Crypto tracing, fraud detection, AML compliance |
| **Key Features** | Address clustering, transaction graphing, exchange identification |
| **Tech Stack** | Neo4j, graph analytics, chain APIs |
| **Deployment** | Cloud or on-prem |
| **POC Scope** | 4-6 weeks, case study tracing, fraud pattern detection |
| **Revenue Model** | RM 100K-200K (POC), RM 500K-1.5M (deployment), RM 300K-800K/year (subscription) |
| **Annual Revenue Target** | RM 5M/year |

---

### 4. LE-UIP (Unified Intelligence Platform)

| Attribute | Value |
|-----------|-------|
| **Target** | Law enforcement, intelligence units |
| **Core Capability** | Cross-domain aggregation, intelligence fusion |
| **Key Features** | Multi-source ingestion, entity resolution, timeline reconstruction |
| **Tech Stack** | OC-CIL, AIL Framework, Neo4j, MISP |
| **Deployment** | Sovereign, air-gapped capable |
| **POC Scope** | 4-6 weeks, intelligence fusion demo, case correlation |
| **Revenue Model** | RM 100K-200K (POC), RM 500K-1.5M (deployment), RM 300K-800K/year (subscription) |
| **Annual Revenue Target** | RM 5M/year |

---

## MVP Definition (Phase 3-4)

### MVP Capability Matrix

| Capability | GovSec | DRQ | Blockchain | LE-UIP | Priority |
|------------|--------|-----|------------|--------|----------|
| **Data Ingestion** | ✅ MISP, OTX, Suricata | ✅ CSV, API | ✅ Chain APIs | ✅ MISP, AIL | P0 |
| **Correlation Engine** | ✅ IOC correlation | ✅ Risk correlation | ✅ Address clustering | ✅ Entity resolution | P0 |
| **Alerting** | ✅ Behavioral alerts | ✅ Risk threshold alerts | ✅ Fraud alerts | ✅ Intelligence alerts | P0 |
| **Dashboard** | ✅ Threat intel dashboard | ✅ Risk score dashboard | ✅ Transaction graph | ✅ Intelligence graph | P0 |
| **Reporting** | ✅ Threat intel reports | ✅ Board-level reports | ✅ Investigation reports | ✅ Intelligence briefs | P1 |
| **API Access** | ✅ MCP tools | ✅ MCP tools | ✅ MCP tools | ✅ MCP tools | P1 |
| **Executive Briefing** | ✅ Auto-brief generation | ✅ Auto-brief generation | ✅ Auto-brief generation | ✅ Auto-brief generation | P1 |
| **Air-Gapped Deployment** | ✅ Capable | ⚠️ Cloud OK | ⚠️ Cloud OK | ✅ Capable | P0 |

---

## Product Roadmap

### Phase 1: MVP Foundation (May 1 - June 15)

| Week | Milestone | Deliverable |
|------|-----------|-------------|
| Week 1-2 | Architecture finalization | Solution architecture docs (4 domains) |
| Week 3-4 | MVP spec definition | MVP capability matrix |
| Week 5-6 | MVP development (GovSec, DRQ) | MVP v0.5 (2 domains) |
| Week 7-8 | MVP development (Blockchain, LE-UIP) | MVP v0.5 (4 domains) |
| Week 9 | Internal testing | Test reports, bug fixes |

---

### Phase 2: POC Deployment (June 16 - July 20)

| Week | Milestone | Deliverable |
|------|-----------|-------------|
| Week 10 | Demo environment ready | Live demo accessible |
| Week 11 | POC #1-2 deployment (CSM, MINDEF) | 2 POCs live |
| Week 12 | POC #3-5 deployment (UPNM, GLC, NACSA) | 5 POCs live |
| Week 13 | POC performance monitoring | Daily status reports |

---

### Phase 3: Production Readiness (July 21 - August 31)

| Week | Milestone | Deliverable |
|------|-----------|-------------|
| Week 14 | POC retrospective | Lessons learned report |
| Week 15-16 | Production hardening | MVP v2.0 (production-ready) |
| Week 17 | Compliance sign-off | ISO 27001, RMiT, GTRM alignment |
| Week 18 | Production deployment #1 | CSM production live |
| Week 19-20 | Production deployment #2-3 | MINDEF, NACSA production live |

---

### Phase 4: Scale & Enhancement (September 1 - December 31)

| Quarter | Milestone | Deliverable |
|---------|-----------|-------------|
| Q3 2026 | Multi-agency rollout | 4-6 agencies deployed |
| Q4 2026 | Feature enhancement | Advanced analytics, ML models |
| Q4 2026 | Integration expansion | CMERP, LebahNet, additional data sources |
| Q4 2026 | Revenue target | RM 21M/year pipeline achieved |

---

## Product Positioning

### Messaging Framework

| Audience | Message | Proof Point |
|----------|---------|-------------|
| **CSM Leadership** | "National capability, CSM-branded, zero capex" | 50/50 IP, CSM branding, Aras-funded infrastructure |
| **Government Agencies** | "Sovereign, air-gapped, compliant" | ISO 27001, RMiT, GTRM alignment, local data residency |
| **Financial Institutions** | "Board-level risk quantification" | Quantitative risk scoring, regulatory reporting |
| **Law Enforcement** | "Cross-domain intelligence fusion" | Multi-source aggregation, entity resolution, timeline reconstruction |
| **Technical Teams** | "MCP-enabled, agent-ready, extensible" | 4 MCP tools, OC-CIL knowledge base, graph-backed |

---

## Competitive Differentiation

| Capability | Aras-CSM | Traditional Vendors | Open Source |
|------------|----------|---------------------|-------------|
| **Sovereign Deployment** | ✅ Air-gapped capable | ❌ Cloud-dependent | ✅ Possible |
| **CSM Branding** | ✅ National trust | ❌ Vendor brand | ❌ No brand |
| **Joint IP** | ✅ 50/50 co-ownership | ❌ Vendor-owned | ✅ Community-owned |
| **Zero CSM Capex** | ✅ Aras-funded | ❌ Customer-funded | ✅ Free |
| **AI-Native** | ✅ OC-CIL, Qwen3.5, Neo4j | ⚠️ Varies | ⚠️ Varies |
| **MCP Tools** | ✅ 4 tools ready | ❌ Proprietary APIs | ⚠️ Custom |
| **Time-to-POC** | ✅ 4-6 weeks | ❌ 3-6 months | ⚠️ 2-4 months |

---

## Workstream Tasks (By Phase)

### Phase 1: Alignment & Mobilization (Day 1-15)

| Task ID | Task | Owner | Deliverable | Due Date | Status |
|---------|------|-------|-------------|----------|--------|
| **PROD-1.1** | Define solution portfolio (4 domains) | Hadri | Solution overview docs | May 8 | 🔲 |
| **PROD-1.2** | Define MVP capability matrix | Hadri | MVP spec document | May 10 | 🔲 |
| **PROD-1.3** | Define product positioning | DAF/Hadri | Messaging framework | May 12 | 🔲 |
| **PROD-1.4** | Define competitive differentiation | DAF/Hadri | Competitive analysis | May 15 | 🔲 |

---

### Phase 2: Use Case & Early Adopter (Day 16-30)

| Task ID | Task | Owner | Deliverable | Due Date | Status |
|---------|------|-------|-------------|----------|--------|
| **PROD-2.1** | Align use cases to solutions | Joint | Use case-to-solution matrix | May 20 | 🔲 |
| **PROD-2.2** | Draft POC positioning deck | DAF/Hadri | Reusable POC deck | May 25 | 🔲 |
| **PROD-2.3** | WG review of positioning | WG | Positioning approved | May 28 | 🔲 |

---

### Phase 3: Commercial & Governance (Day 31-45)

| Task ID | Task | Owner | Deliverable | Due Date | Status |
|---------|------|-------|-------------|----------|--------|
| **PROD-3.1** | Finalize MVP specs (4 domains) | Hadri | MVP v1.0 specs | June 10 | 🔲 |
| **PROD-3.2** | Draft product roadmap | Hadri | 12-month roadmap | June 12 | 🔲 |
| **PROD-3.3** | WG review of roadmap | WG | Roadmap approved | June 15 | 🔲 |

---

### Phase 4: Technical Readiness (Day 46-60)

| Task ID | Task | Owner | Deliverable | Due Date | Status |
|---------|------|-------|-------------|----------|--------|
| **PROD-4.1** | Complete MVP development | Fuad | MVP v1.0 (4 domains) | June 25 | 🔲 |
| **PROD-4.2** | Package demo environment | Fuad | Demo-ready modules | June 28 | 🔲 |
| **PROD-4.3** | Create product datasheets | Hadri | 4 datasheets (1 per domain) | July 1 | 🔲 |
| **PROD-4.4** | WG approval of MVP | WG | MVP sign-off | July 5 | 🔲 |

---

### Phase 5: POC Launch (Day 61-75)

| Task ID | Task | Owner | Deliverable | Due Date | Status |
|---------|------|-------|-------------|----------|--------|
| **PROD-5.1** | Support POC deployments | Fuad | 5 POCs live | July 15 | 🔲 |
| **PROD-5.2** | Collect POC feedback | Hadri | Feedback report | July 18 | 🔲 |
| **PROD-5.3** | Iterate MVP based on feedback | Fuad | MVP v1.1 | July 20 | 🔲 |

---

### Phase 6: Review & Conversion (Day 76-90)

| Task ID | Task | Owner | Deliverable | Due Date | Status |
|---------|------|-------|-------------|----------|--------|
| **PROD-6.1** | Define production feature set | Hadri | Production spec | July 25 | 🔲 |
| **PROD-6.2** | Draft case studies (per POC) | Hadri | 5 case studies | July 28 | 🔲 |
| **PROD-6.3** | Update product roadmap (post-POC) | Hadri | Roadmap v2 | July 30 | 🔲 |

---

## Success Metrics

| Metric | Target | Measurement Method |
|--------|--------|--------------------|
| **MVP Completion** | 4/4 domains | MVP v1.0 deployed |
| **POC Positioning Deck** | 1 reusable deck | Deck approved by WG |
| **Product Datasheets** | 4 datasheets | 1 per domain |
| **Case Studies** | 5 case studies | 1 per POC |
| **Roadmap Approval** | WG approved | Roadmap v2 signed off |
| **Competitive Win Rate** | ≥60% | POC-to-contract conversion |

---

## Query Interface (MCP Tool Access)

```python
# Example: Query solution portfolio
portfolio = mcp.govsec.kb_query(unit_id="KB-90DAY-WS-004", section="portfolio")

# Example: Query MVP capabilities
mvp = mcp.govsec.kb_query(unit_id="KB-90DAY-WS-004", section="mvp")

# Example: Query product roadmap
roadmap = mcp.govsec.kb_query(unit_id="KB-90DAY-WS-004", section="roadmap")

# Example: Query Phase 4 product tasks
phase4 = mcp.govsec.kb_query(unit_id="KB-90DAY-WS-004", phase="Phase 4")
```

---

**Last Updated:** 2026-04-25 06:48 UTC  
**Next Review:** 2026-05-01 (Phase 1 Kickoff)  
**Retention Tier:** Operational (Active Daily Use)

#Product
#MVP
#SolutionPackaging
#Roadmap
#90DayPlan
#CSM
#Aras
#KB90Day
