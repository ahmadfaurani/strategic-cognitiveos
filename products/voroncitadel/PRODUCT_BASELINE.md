# VoronCitadel — Product Baseline Summary

**Full Name:** VoronCitadel (formerly VoronDRQ) — Integrated GRC & Digital Risk Quantification Platform
**Version:** 2.0 (August 2026)
**Status:** Production-deployed, live
**Maturity:** MVP complete — most commercially mature of 3 flagship products
**Commercialisation Readiness:** Ready
**Source:** MVP Product Specification v2.0 (Ahmad Fuad, Aug 2026)

---

## What It Is

A purpose-built integrated platform consolidating 4 capabilities into a single PostgreSQL data fabric:
1. **GRC** — Governance, Risk & Compliance
2. **DRM** — Digital Risk Management & Quantification
3. **ASM** — Attack Surface Management (via VoronScout OSINT engine)
4. **TPRM/TPRA** — Third-Party Risk Management & Assessment

Every risk, asset, control, policy, and vendor relationship shares a unified object model — enabling cross-domain correlations that point solutions can't surface.

## Architecture

- **Stack:** React SPA + Express REST API + PostgreSQL (single-node Docker Compose)
- **AI:** Sovereign LLM (Qwen 3.5-27B served via Aras Integrasi) — no tenant data sent to foreign endpoints
- **Design decision:** Single cohesive app (not microservices) — maximises dev velocity, clean domain boundaries for Phase 2 split
- **Security:** JWT auth, RBAC (7 roles, 30 permissions), bcrypt, TLS via Nginx, append-only audit log, AI-provenance audit trail

## Domain Feature Sets (Production-Verified)

### 1. GRC (Governance, Risk & Compliance)
- Risk Register: 9 risk categories, likelihood×impact scoring, FAIR ALE, treatment plans
- Control Library: Maturity levels, effectiveness scores, evidence locker, AI-prioritised recommendations
- Policy Management: Lifecycle (draft→review→approved→retired), versioning, attestation
- Policy Attestation: Bulk assignment, compliance-rate analytics
- Board & Committee Management: 9 committee types, meeting scheduling, action-item tracking
- Incident Management: Full lifecycle, CAPA, incident→risk linking, financial impact
- BCM: BIA records (RTO/RPO/MTD), BCM documents, test/exercise management
- Operational Loss Database: 14 loss event types, YTD analytics, recovery-rate computation
- Governance Support: Immutable audit log, 7 roles / 30 permissions, 8 display currencies

### 2. DRM (Digital Risk Management & Quantification)
- Asset Inventory: 7 asset types, OSSTOM-style EVAT scoring, VoronRAV computation
- Risk Quantification Engine: FAIR ALE, Monte Carlo (50,000 iterations), regression modelling
- Executive Analytics: C-suite metrics, portfolio distributions, PDF board report export

### 3. ASM (Attack Surface Management — VoronScout)
- External Asset Discovery: Company/domain/IP mode, subdomain discovery (crt.sh), DNS resolution, TCP port scanning
- TLS/SSL Assessment, RDAP/WHOIS, HTTP header inspection, IP geolocation
- Exposure Findings & Scoring: Per-asset findings with severity, mitigation recommendations, EVAT-style scoring
- Threat Intelligence Integration: Findings promote to Risk Register or remediation items

### 4. TPRM/TPRA (Third-Party Risk Management & Assessment)
- Vendor Inventory: 4-tier classification, contract tracking, expiring-contract alerts
- Vendor Assessments: 5 assessment types, certification tracking, remediation tracking
- Continuous Monitoring: Every 6 hours production, 7 cyber-intel sources, adverse media, supply-chain, geopolitical
- TPRA Composite Scoring: 6 dimensions (Cyber 25%, Financial 20%, Compliance 20%, Operational 15%, Reputational 10%, Geopolitical 10%)

## Compliance Framework Integration
- **5 frameworks supported:** ISO 27001:2022, SC GTRM, BNM RMiT, NIST CSF 2.0, NIST RMF
- **295 requirements** (confirmed against production database)
- Multi-framework control mapping: 1 control → many framework requirements
- Cross-framework references (requirement equivalences)
- AI-assisted evidence drafting and coverage suggestion

## Sovereign AI Copilot (Production)
1. Compliance narrative generation (with rule-based fallback)
2. Evidence auto-drafting
3. Coverage-status suggestion (with confidence + reasoning)
4. Cross-framework cross-referencing
5. Acceptance/rejection feedback loop
6. AI-assisted TPRA threat assessment
- All AI calls logged to ai_compliance_audit_log with data_residency = 'on_prem'

## User Personas
1. Risk Analyst — daily risk operations
2. Compliance Officer — framework assessment
3. Third-Party Risk Manager — vendor assessment & monitoring
4. CISO — monthly risk review, executive view, board report
5. Board — receives structured PDF board report

## Production Stack
- Frontend: React SPA
- Backend: Express REST API (Node.js)
- Database: PostgreSQL (45 production tables)
- AI: Qwen 3.5-27B (sovereign, on-prem)
- Deployment: Docker Compose, single node
- Reverse proxy: Nginx (TLS)
- Scanning: VoronScout (TypeScript + Python CLI)

## 5 Operational Dependencies (Flagged by Fuad, Apr 20)
These qualify as "previously committed integration requirements" under the freeze — permitted development:
1. UI/UX Refinement — including white-labelling for CSM engagement
2. AI Copilot RAG Pipeline & LLM Integration — core intelligence layer for Analyst Workbench
3. Compliance Framework Data Layer Population — structured seeding of all 5 frameworks
4. Integration Connector Build-Out — SIEM, ticketing, CMDB, IdP, threat intel
5. Multi-Tenant Data Isolation & Security Hardening — RBAC, RLS, audit logging, pen testing

## Phase 2 Scope (Deferred)
- Custom framework addition (internal policy frameworks)
- Microservice split (bounded contexts)
- Horizontal scaling (stateless API containers, connection pooling, VoronScout worker pool)
- Multi-tenant data isolation (RLS enforcement)
- Full integration connector suite
- Advanced AI RAG pipeline

## Key Differentiators
- **Single data fabric** — not 4 point solutions stitched together
- **Quantified risk** — FAIR ALE + Monte Carlo, not just catalogue
- **Sovereign AI** — Malaysian data residency, auditable AI, no foreign model endpoints
- **Multi-framework compliance** — 5 frameworks, 295 requirements, cross-referenced
- **Production-deployed** — not a prototype; live with verified feature set
