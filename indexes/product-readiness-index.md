# Product Readiness Index

All products and their current readiness levels.

| Product | Initiative ID | Current Readiness | Target Readiness | Owner | Gaps | External Commitments | Overcommitment Risk |
|---------|-------------|-------------------|-----------------|-------|------|---------------------|---------------------|
| GovSec TIP | INIT-20260810-003 | Prototype (v3.0 spec, 12 core entities, 147 endpoints, 23 modules) | Demo-ready (CyberDSA Oct 2026) | faurani-jaafar | 11 Phase 2 deferrals (dark web, SIEM, SOAR, SSO, semantic search, AI hunt gen, BYOK, multi-region HA, regulatory monitoring); security audit completed (OWASP Web+LLM Top 10, 54 npm findings) | CyberDSA Oct 2026 joint launch with CSM | Medium — 11 deferrals are well-scoped but CyberDSA timeline is tight |
| VoronCitadel | INIT-20260811-001 | Production-deployed (v2.0, 45 tables, 5 frameworks, 295 requirements) | Commercial-ready | faurani-jaafar | Single-node deployment (Phase 2: HA); 17 Phase-2 deferrals identified; custom framework builder deferred | CSM GTM activation (INIT-20260804-001) | Low — most mature product, production-live |
| ChainSentry | INIT-20260811-001 | v4.1 spec — 12 of 17 gaps closed in code (all Critical/Must); NOT deployed (29 commits/40 days behind trunk); Implementation 69%, Deployed 47% | Pilot-ready (Phase 0 exit → 77%, Phase 1 exit → 90%) | hadri | 3 Critical Phase 0 blockers (credential rotation, address-security regression, deployment not describable); 1 Should open (investigator outputs); 2 Future (non-EVM tracing, dossier signing) | None identified | High — 3 Critical blockers, credential exposure window open |
| VoronDRQ | INIT-20260804-001 | Pilot | Commercial-ready | faurani-jaafar | GTM team mobilisation, COO approval | CSM joint GTM | Medium |
| VoronScout | — | *Pending* | — | — | — | — | — |
| LE-UIP | — | *Pending* | — | — | — | — | — |
| SEC-AF | — | *Pending* | — | — | — | — | — |

## Readiness Level Reference

| Level | External Commitment Allowed |
|-------|---------------------------|
| concept | No |
| framed | No |
| prototype | No |
| demo-ready | Demonstration only |
| pilot-ready | Pilot scope only |
| delivery-ready | Yes |
| commercial-ready | Yes |
| scale-ready | Yes |

## ChainSentry Detailed Readiness (MVP Spec v3.0, 14 Aug 2026)

### Verified Baseline (11 Aug 2026)
- Investigative surfaces: 26 page routes
- API route handlers: 44 (32/32 GET paths returned HTTP 200)
- Attribution corpus: 583,574 tags / 524,656 addresses / 78 chains
- Sanctions registry: 4,633 addresses
- Verified entity directory: 57 addresses
- Source health: 12 of 18 roles operational
- Automated jobs: 3 (daily sanctions, weekly attribution, 15-min alerts)
- Stability: No errors in 2,000-log-line window

### Critical Gaps (Must close before pilot)
1. Deployment parity — 22-commit/32-day gap between dev and deployed
2. External access & named identity — TLS termination, pilot accounts, session URL
3. Credential closure & secret governance — 4 exposed keys need rotation
4. Live-vs-demo boundary — 31-tool registry still fixture-backed

### Must-Have Gaps
1. API & documentation parity — in-product docs show illustrative routes, not implemented contract
2. Integration & anonymised-network health — 6 degraded source roles, Tor transport unreachable
3. Automated quality gates — tests don't run in CI, lint non-blocking, no risk-engine regression

### Should-Have Gaps
1. Schema migration & recovery — manual migrations, backup/restore not tested
2. Tenant isolation & quota control — only 1 tenant verified
3. Investigator outputs — no batch screening, PDF export, or audit-log UI
4. Alerting & observability — webhook-only delivery, no email, no structured logging

### Future Capabilities (Post-Pilot)
- Cryptographic dossier signing
- Bitcoin/non-EVM tracing
- Cross-chain bridge following
- Real-time streaming ingestion
- Messaging-channel alerts
- Case collaboration & assignment
- Saved searches & watchlists
- Self-service org onboarding

## VoronCitadel Detailed Readiness (MVP Spec v2.0, 14 Aug 2026)

### Verified Production Baseline
- Production deployment: live on vcitadeldemo host (Docker Compose, Nginx TLS, Tailscale access)
- Database: PostgreSQL 16, 45 relational tables, schema auto-applied (idempotent)
- API: 22 REST routers under /api/, JWT auth, rate limiting, SSE for live scans
- Frontend: React 18 + TypeScript 5 + Vite 8 + Tailwind CSS 3
- AI: Sovereign LLM (Qwen 3.5-27B via Aras Integrasi), on-prem data residency, AI provenance audit log

### Domain Coverage (4 domains, all production-verified)
1. **GRC** — Risk register (9 categories, FAIR ALE), controls (maturity 1-5, effectiveness), policies (lifecycle, attestation), committees (9 types), incidents (CAPA), BCM (BIA, tests), loss database (14 event types), audit log
2. **DRM** — Asset inventory (7 types), EVAT/VoronRAV scoring, FAIR ALE quantification, 50K-iteration Monte Carlo, executive analytics (regressions, PDF export)
3. **ASM (VoronScout)** — External discovery (company/domain/IP modes), crt.sh subdomain enum, DNS/DoH, port scanning, TLS assessment, WHOIS/RDAP, HTTP header inspection, findings + scoring, SSE live streaming
4. **TPRM** — Vendor registry (4 tiers), assessments (5 types), continuous monitoring (6-hourly TPRA), composite scoring (6 dimensions), 14 intelligence connectors

### Compliance Frameworks (5, 295 requirements — verified in production database)
- ISO 27001:2022 (93 requirements)
- NIST CSF 2.0 (57 requirements)
- BNM RMiT (41 requirements)
- SC GTRM (43 requirements)
- Bursa Malaysia Cybersecurity (61 requirements)

### Sovereign AI Copilot (6 production capabilities)
1. Compliance narrative generation (with rule-based fallback)
2. Evidence auto-drafting
3. Coverage-status suggestion
4. Cross-framework cross-referencing
5. Acceptance/rejection feedback loop
6. AI-assisted TPRA threat assessment
- AI Sovereignty Score metric (data residency 30, audited decisions 30, model quality 20, AI evidence 20)

### Phase 2 Deferrals (17 items)
- GRC: Regulatory change monitoring, RCSA, AI policy drafting
- DRM: Asset-level TI, dark web/brand monitoring
- ASM: Authenticated scanning, continuous full-surface rescan, benchmarking
- TPRM: Sanctions feed, financial feed, sub-processors, vendor portal
- Compliance: Custom framework builder, SoA auto-generation
- Platform: Multi-tenant console, domain events, active-active HA

### Key Differentiators
- Unified data model (single PostgreSQL, 45 tables, all domains)
- Quantification-first (FAIR ALE + Monte Carlo built into core)
- Sovereign AI (Malaysian-hosted, auditable, no tenant data leaves boundary)
- Malaysian regulatory alignment (BNM RMiT, SC GTRM, Bursa — built into core)
- Automated TPRA (6-hourly, 14 connectors, 6-dimension composite scoring)

## GovSec TIP Detailed Readiness (MVP Spec v3.0, 14 Aug 2026)

### Architecture Baseline
- 12 core entity types on shared data fabric (PostgreSQL)
- 4 domains: Threat Intelligence & Ingestion, Analysis & Detection, Alerting & Response Operations, Governance & Compliance
- 23 API modules, 147 endpoints (interactive API documentation)
- 12 scheduled pipelines (feed ingestion, correlation, alert eval, MITRE mapping, threat scoring, NLP classification, alert dedup, PII scan, retention, hunt execution, MITRE coverage, escalation)
- Frontend: React 18 + TypeScript + Vite + Tailwind + D3.js (graphs) + Leaflet (maps)
- Backend: Node.js + Express REST API + PostgREST proxy
- AI: OpenAI-compatible endpoint (model.arasintegrasi.ai), RAG architecture, no direct DB access for LLM

### Domain Coverage (4 domains)
1. **Threat Intelligence & Ingestion** — Feed management (STIX/TAXII, OTX, URLhaus, MalwareBazaar, MISP, REST JSON, CSV, Logstash bridge, push API); indicator enrichment (geo, severity, TLP, dedup); CVE/KEV pipeline (NVD sync, CVSS v3/v4, CISA KEV)
2. **Analysis & Detection** — Indicator library (IP, domain, hash, URL, email, CVE); dynamic threat scoring (0-100, 5 components, 30-day half-life); correlation engine (6 relationship types, 5 techniques); MITRE ATT&CK (auto-mapping, coverage heatmap, gap analysis); threat hunting workbench (JSON DSL, saved hunts, playbooks); national APT library; NLP auto-classification
3. **Alerting & Response Operations** — Detection rules (severity thresholds, MITRE binding); alert lifecycle (open→ack→investigating→resolved/false_positive); fingerprint dedup; auto-escalation (Critical 15min, High 60min); case management (P1-P4, notes, artifacts, timeline); deterministic case AI reports; executive + operational dashboards (20+ KPIs)
4. **Governance & Compliance** — Government org tree (recursive, classification levels: Rahsia/Sensitif/Terhad/Pertidahan/Awam); RBAC with compartment access; PDPA compliance engine (NRIC, email, phone, bank, card detection; 4-hourly scans; redaction; access audit; retention enforcement); immutable audit log; scheduler status dashboard

### Framework Integration (6 frameworks/datasets)
- MITRE ATT&CK — full technique/tactic/group catalogue, auto-mapping, detection coverage
- NVD/CVE — CVSS v3/v4 scoring, NVD synchronisation
- CISA KEV — known exploited vulnerabilities with due dates and ransomware flags
- STIX/TAXII 2.1 — structured threat intelligence interchange
- PDPA 2010 (Malaysia) — PII detection, redaction, access audit, retention
- Malaysian Classification — national levels with compartment-based access control

### AI Analyst (RAG-powered workbench)
- Natural language queries across platform data
- Automated insight generation (scoring anomalies, coverage gaps, alert concentrations, PDPA/retention)
- Deterministic case report generation from MITRE knowledge base
- NLP auto-classification (actors, malware, campaigns)
- Rate limiting (20 req/min/user), injection defence, per-user conversation history

### Security Baseline
- OWASP Web Top 10 + OWASP LLM Top 10 audit completed
- npm audit: 54 findings with prioritised remediation plan
- Critical/high items remediated before production release
- Server-side RBAC + classification enforcement on every route
- Brute-force mitigation (5 attempts/15 min), session timeout, parameterised SQL

### Phase 2 Deferrals (11 items)
- Dark web monitoring (credential exposure, leaked data)
- Brand & executive monitoring (impersonation, typosquatting)
- SIEM bidirectional integration (Splunk, Sentinel)
- Ticketing integration (Jira, ServiceNow)
- SOAR automated response playbooks
- SSO/MFA (SAML 2.0, OIDC)
- Vector semantic search for AI Analyst
- AI-generated hunt queries from NL hypotheses
- BYOK/HYOK encryption
- Multi-region active-active HA
- Automated regulatory change monitoring (PDPA)

### Key Differentiators
- Malaysian government alignment (PDPA, classification levels, national APT library — built into core)
- Dynamic threat scoring (0-100, 5 components, 30-day temporal decay)
- Unified data fabric (single PostgreSQL, 12 entities, all domains)
- AI Analyst with RAG architecture (not a chatbot wrapper — structured retrieval, not search)
- 12 scheduled pipelines with run ledger (idempotent, no overlapping runs)
- STIX/TAXII 2.1 native support + Logstash ECS bridge + push API for external partners (Lebahnet)
