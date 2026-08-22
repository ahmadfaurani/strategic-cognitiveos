---
id: DOC-20260821-004
record_type: document
title: "GovSec Product Roadmap Q3 2026 – Q2 2027"
created_at: 2026-08-21T15:03:00+00:00
updated_at: 2026-08-21T15:03:00+00:00
owner: ahmad-fuad
status: active
priority: high
sensitivity: internal
lifecycle_state: canonical
confidence: high
tags:
  - domain/commercial-development
  - domain/csm-partnership
  - domain/cyberdsa-2026
  - domain/cybersecurity-productisation
  - domain/organisational-capability
  - domain/product-management
  - framework/actionable-intelligence-protocol
  - framework/engineered-success
  - milestone/cyberdsa-2026
  - product/govsec
  - status/delivered
  - workstream/cybersec-products
source:
  type: email-attachment
  reference: CONV-20260817-003
  file: GovSec_Product_Roadmap_Q3_2026-Q2_2027.pptx
summary: "Fuad's GovSec product roadmap slide deck (16 slides). 12 project cards across 4 quarters: Q3 2026 (Productise & Pilot), Q4 2026 (Integrate & Govern), Q1 2027 (Scale Analysis), Q2 2027 (Broaden Assurance). Q3 2026 progress confirmed on track. Covers production hardening, executive visualisation, feed quality, identity/MFA, SIEM/ticketing, playbooks, exposure monitoring, RAG pipeline, AI threat hunting, CSM SOAR, BYOK/HA, and regulatory analytics. Total effort estimate: ~24-30 FTEs across all 12 projects."
strategic_significance: "First comprehensive product roadmap for GovSec — directly supports CyberDSA 2026 launch readiness, CSM co-branding discussions, and NACSA endorsement track. Provides Q3-Q4 timeline that gates commercial activation and pilot engagement. CSM SOAR integration (Q1 2027) is the deepest CSM technical integration milestone in the roadmap."
mission_alignment:
- sovereign-ai
- cybersecurity-productisation
- csm-partnership
- milestone/cyberdsa-2026
related_records:
- CONV-20260817-003
- ACT-20260817-007
- ACT-20260811-002
- ACT-20260811-006
- INIT-20260810-003
- INIT-20260804-001
document_type: roadmap
file_path: media/inbound/GovSec_Product_Roadmap_Q3_2026-Q2_2027.pptx
version: "1.0"
author: Ahmad Fuad Bin Kamarazaman
---

# GovSec Product Roadmap Q3 2026 – Q2 2027

**Author:** Ahmad Fuad Bin Kamarazaman (Principal AI Security Architect)
**Delivered:** Aug 17, 2026, 3:45 PM MYT (via email, CONV-20260817-003)
**Status:** Q3 2026 on track

---

## Executive Summary

| Quarter | Theme | Projects |
|---------|-------|----------|
| **Q3 2026** | Productise and Pilot | Production Hardening, Executive Visualisation, Feed Quality |
| **Q4 2026** | Integrate and Govern | Identity/MFA, SIEM & Ticketing, Playbooks & Case Automation, Exposure Monitoring |
| **Q1 2027** | Scale Analysis | RAG Pipeline, AI Threat Hunting, CSM SOAR Integration |
| **Q2 2027** | Broaden Assurance | BYOK/HA, Regulatory & Maturity Analytics |

**Sequencing logic:** Q3 establishes production confidence → Q4 prepares enterprise operations → Q1 expands AI analysis → Q2 broadens high-assurance resilience.

---

## 12 Project Cards

### Q3 2026 — Productise and Pilot

#### 1. Production Hardening & Pilot Enablement
- **Duration:** 8–10 weeks | **Effort:** 3 FTEs
- **Dependencies:** GovSec v3.0 baseline; security audit remediation plan
- **Deliverables:** Security remediation baseline (OWASP/LLM findings, security headers, NODE_ENV=production), pilot operating model (seeded feeds, runbooks, go/no-go report)

#### 2. Executive Posture & Threat Visualisation Release
- **Duration:** 6–8 weeks | **Effort:** 2 FTEs
- **Dependencies:** v3.0 dashboard widgets, threat map, threat graph
- **Deliverables:** Executive review cockpit (posture score narrative, 30-day movement highlights, org/sector breakdown), visual intelligence workspace (unified map/graph filters, campaign drill-down, export-ready screenshots)

#### 3. Feed Quality, Provenance & Integration Pack
- **Duration:** 8–10 weeks | **Effort:** 2 FTEs
- **Dependencies:** MVP feed registry; push ingestion API; scheduler ledger
- **Deliverables:** Feed onboarding standards (STIX/TAXII, REST JSON, CSV, Logstash, push API templates), data quality controls (dedup, validation dashboard, geo-enrichment backfill, integration guide)

### Q4 2026 — Integrate and Govern

#### 4. Enterprise Identity, MFA & Access Assurance
- **Duration:** 10–12 weeks | **Effort:** 2 FTEs
- **Dependencies:** RBAC hierarchy; classification and compartment model
- **Deliverables:** Identity integration foundation (SAML/OIDC SSO, MFA policy, session policy), access assurance (quarterly review workflow, audit dashboards, break-glass process)
- **Note:** Designed for Malaysian government deployment

#### 5. SIEM & Ticketing Integration Blueprint
- **Duration:** 8–10 weeks | **Effort:** 1 FTE
- **Dependencies:** API reference; Logstash ECS bridge; alert/case lifecycle
- **Deliverables:** SIEM integration blueprint (Splunk + Microsoft Sentinel connectors, alert/evidence mapping), ticketing workflow design (Jira/ServiceNow case mapping, state synchronisation)
- **Note:** Blueprint + prototypes, not full integration

#### 6. Operational Playbooks & Case Automation
- **Duration:** 8–10 weeks | **Effort:** 1.5 FTEs
- **Dependencies:** Alert lifecycle, escalation log, case AI reports
- **Deliverables:** Response playbooks (triage SOPs, case priority matrix, hunt-to-case promotion), automated reporting (case AI report templates, executive summary + technical appendix, sign-off workflow)

#### 10. External Exposure, Dark Web & Brand Monitoring
- **Duration:** 10–12 weeks | **Effort:** 3 FTEs
- **Dependencies:** Feed quality pack; actor/indicator/organisation linkage
- **Deliverables:** Monitoring expansion (dark web credential detection, brand/executive/typosquatting monitoring), operationalisation (exposure-to-indicator normalisation, notification workflow, monthly trend report)

### Q1 2027 — Scale Analysis

#### 7. RAG Pipeline Hardening & Semantic Search
- **Duration:** 10–12 weeks | **Effort:** 3 FTEs
- **Dependencies:** AI Analyst RAG; conversation history; audit controls; security audit findings #43, #51, #55
- **Deliverables:** RAG security & scoping (role-aware context assembly, classification-aware retrieval filters), semantic retrieval & model refinement (vector index, retrieval evaluation, domain prompt tuning)

#### 8. AI-Assisted Threat Hunting Generation
- **Duration:** 8–10 weeks | **Effort:** 2 FTEs
- **Dependencies:** Threat hunting JSON DSL; MITRE coverage heatmap
- **Deliverables:** Hunt generation assistant (NL hypothesis capture, DSL query generation with safety checks, MITRE technique suggestions), hunt operations (scheduled hunts with approval controls, result promotion to alerts/cases, reusable playbooks)

#### 9. CSM SOAR Integration
- **Duration:** 6–8 weeks | **Effort:** 2 FTEs
- **Dependencies:** Operational playbooks; CSM SOAR API documentation; SIEM/ticketing blueprint
- **Deliverables:** Integration layer (CSM SOAR API connector, playbook trigger mapping, response action routing), operational alignment (severity/status mapping, audit trail, integration test harness)
- **Strategic significance:** Deepest CSM technical integration milestone — bi-directional alert/case sync with CSM's existing SOAR platform

### Q2 2027 — Broaden Assurance

#### 11. High Assurance Resilience: BYOK/HYOK & HA
- **Duration:** 12–14 weeks | **Effort:** 4 FTEs
- **Dependencies:** Production hardening; deployment baseline; data residency requirements
- **Deliverables:** Key management design (BYOK/HYOK architecture, secret rotation, database encryption, key custody/recovery), resilience roadmap (backup/restore validation, RTO/RPO targets, multi-region HA reference architecture, failover test plan)

#### 12. Regulatory Change & Maturity Analytics
- **Duration:** 8–10 weeks | **Effort:** 2 FTEs
- **Dependencies:** PDPA engine; audit log; executive dashboard
- **Deliverables:** Regulatory monitoring (PDPA change tracker, MyCERT/CsIRT feed integration, impact assessment workflow), maturity analytics (quarterly control effectiveness scorecard, KPI dashboard, roadmap refresh pack for Q3 2027)

---

## Resource Summary

| Quarter | Projects | Total FTEs | Duration Range |
|---------|----------|-----------|----------------|
| Q3 2026 | 3 | 7 | 6–10 weeks each |
| Q4 2026 | 4 | 7.5 | 8–12 weeks each |
| Q1 2027 | 3 | 7 | 6–12 weeks each |
| Q2 2027 | 2 | 6 | 8–14 weeks each |
| **Total** | **12** | **~27.5** | **6–14 weeks each** |

---

## Strategic Observations

1. **CyberDSA alignment:** Q3 projects (hardening, visualisation, feed quality) are the CyberDSA demo foundation. On-track status confirms readiness trajectory.
2. **CSM deepening:** Q1 2027 CSM SOAR Integration is the first bi-directional technical integration with CSM's operational platform — moves GovSec from "product CSM uses" to "platform CSM's SOC runs on."
3. **Government-grade:** Q4 identity/MFA + Q2 BYOK/HA are the government deployment gating items — Malaysian government classification compartments and data residency requirements explicitly named.
4. **Resource risk:** 27.5 FTEs total across 12 projects. Current team: Fuad + Syahir + hadri (partial). Hiring (HoE, CSE, Junior Backend — ACT-20260820-007/008/009) is on the critical path for Q4+ delivery.
5. **Gap — no explicit chain:SENTRY/VoronCitadel cross-references:** Roadmap is GovSec-only. chain:SENTRY and VoronCitadel roadmaps not included (separate documents needed for ACT-20260811-002 closure).
