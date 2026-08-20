---
id: DOC-20260814-002
record_type: document
title: VoronCitadel MVP Product Specification
product: voroncitadel
initiative: INIT-20260811-001
category: mvp-specification
version: canonical
date: 2026-08-14
source_authority: DAF
sensitivity: confidential
status: archived
tags:
- domain/cybersecurity
- domain/attack-surface-management
- domain/cybersecurity-productisation
- product/voroncitadel
- workstream/cybersec-products
- portfolio/flagship
source:
  docx-upload: docx-upload
created_at: '2026-08-14T00:00:00+00:00'
updated_at: '2026-08-17T17:50:22+00:00'
owner: DAF
priority: medium
lifecycle_state: canonical
confidence: medium
summary: '> Canonical baseline document - uploaded by DAF, 14 August 2026 > > CONFIDENTIAL
  - FOR EXECUTIVE AND ENGINEERING REVIEW'
strategic_significance: 'Document record. Priority: None.'
mission_alignment: []
related_records: []
---

# VoronCitadel MVP Product Specification

> Canonical baseline document - uploaded by DAF, 14 August 2026
>
> CONFIDENTIAL - FOR EXECUTIVE AND ENGINEERING REVIEW






VORONCITADEL
Integrated GRC & Digital Risk Quantification Platform
MVP Product Specification

CONFIDENTIAL — FOR EXECUTIVE AND ENGINEERING REVIEW
Version 2.0  |  August 2026


# Executive Summary
Enterprise governance, risk and compliance management today is fragmented. Security teams manage operational risk in one tool, digital and quantitative risk exposure in another, third-party risk in a third, and compliance obligations in yet another — with no unified data model, no shared language, and no cross-domain intelligence. The result is duplicated effort, blind spots at domain boundaries, and reporting that obscures rather than illuminates the organisation's true risk posture.
VoronCitadel is a purpose-built, production-deployed integrated platform that consolidates four capabilities — Governance, Risk and Compliance (GRC), Digital Risk Management & Quantification (DRM), Attack Surface Management (ASM) via the VoronScout OSINT engine, and Third-Party Risk Management (TPRM) with a full Third-Party Risk Assessment (TPRA) pipeline — into a single data fabric running on PostgreSQL. Every risk, every asset, every control, every policy, and every vendor relationship is expressed in a shared object model, enabling correlations that no point solution can surface.
This document is the MVP product specification for the production release currently deployed and live. It is a precise, actionable guide for executive stakeholders making investment decisions and for engineering leadership planning the next release. It covers platform architecture, domain feature sets, compliance framework integration, the Sovereign AI Copilot, the underlying data model, user personas and workflows, technical architecture, and scope boundaries — all grounded in the features verified in the production deployment.




# 1. Platform Architecture & Unified Data Model
## 1.1 Architectural Philosophy

VoronCitadel High Level Architecture

The central design principle of VoronCitadel is that risk is a shared language, not a departmental dialect. Where point solutions maintain independent object models, VoronCitadel starts from a canonical data fabric: every domain reads from and writes to the same PostgreSQL entity store. This produces compound intelligence — a vendor finding from an OSINT scan can be correlated with its vendor's TPRA score, the assets it supports, the controls that mitigate the associated risk, and the compliance requirements those controls satisfy — without any human joining of records.
The MVP is architected as a single cohesive application (React SPA + Express REST API + PostgreSQL) rather than a distributed microservice mesh. This is a deliberate MVP decision: it maximises development velocity, keeps the compliance/audit data path simple, and still exposes clean domain boundaries in the schema and route structure that can be split into bounded contexts in Phase 2 without data-model rework.
## 1.2 Core Entity Model
The VoronCitadel data model consists of core entity types across four domain clusters. Every domain-specific object is either a core entity or a typed extension of one.

## 1.3 Entity Relationships
The relationships between core entities define the data fabric. Key relationships (all enforced in PostgreSQL with foreign keys and organisation-level scoping):
Organisation → Risk/Asset/Control/Policy/Vendor (1:n): root ownership of all records; the tenant isolation boundary for every query.
Risk → Control (n:m) via risk_control_mappings, with a coverage rating (none / partial / substantial / full) that drives residual-risk calculation.
Control → Framework Requirement (n:m) via control_framework_mappings — the core of the multi-framework compliance engine; one control can satisfy requirements across multiple frameworks simultaneously.
Risk → Treatment Plan (1:n) → Treatment Task (1:n): treatment strategies (mitigate, avoid, accept, transfer) cascade to tracked tasks with owners and target dates.
Policy → Attestation (1:n): bulk-assigned acknowledgements tracked per user (pending / acknowledged / declined / waived).
Vendor → Assessment / Scan Result / TPRA Score / Monitoring Alert / Remediation (1:n): the full third-party lifecycle.
Incident → CAPA (1:n): corrective and preventive actions with effectiveness review.
Incident / Loss Event → Risk (n:1): financial impact and loss events cross-referenced to the risk register.
Asset → EVAT Score (1:n): OSSTMM-style score history preserved per asset.
Requirement → Cross-Reference (n:m) via requirement_cross_references: mapped equivalences between frameworks (e.g., ISO 27001 control ↔ NIST CSF subcategory ↔ BNM RMiT paragraph).
## 1.4 Domain Boundary Map
The platform is structured around four domain clusters that share entities but own different aspects of their lifecycle:

## 1.5 Data Flow Architecture
Data flows bidirectionally between domains. Primary integration flows in the MVP:
Vendor → VoronScout (TPRM → ASM): each registered vendor seeds the VoronScout scanner (domains/IPs). Scan findings surface in the vendor's risk record and can be promoted directly to the Risk Register ("Create Risk") or to a tracked remediation item.
Scan/TPRA → Risk Register (ASM/TPRM → GRC): findings above significance are proposed as risk inputs or remediation items; analysts approve or dismiss.
Incident/Loss → Risk (GRC internal): incident financial impact and operational loss events cross-reference the risk register and its ALE.
Control → Compliance (GRC → Compliance): control effectiveness and maturity feed requirement-level coverage status for all five frameworks.
Policy → Attestation (GRC internal): policy lifecycle drives bulk attestation campaigns and compliance-rate analytics.
Quantification → Risk (DRM → GRC): FAIR ALE per risk category and Monte Carlo portfolio distribution inform the dashboard, executive view, and board report.

# 2. Domain Feature Sets
For each capability, the inclusion decision reflects the verified production feature set. Features deferred to Phase 2 are listed at the end of each domain section; a comprehensive scope boundary table appears in Section 7.
## 2.1 Governance, Risk and Compliance (GRC)
The GRC domain is the operational spine of the platform: the governance structure — risks, controls, policies — against which risk and compliance posture is measured.
### 2.1.1 Risk Register
Full CRUD risk lifecycle: open → mitigated / accepted / transferred → closed, with 9 risk categories (strategic, operational, financial, compliance, technology, cyber, third_party, reputational, legal).
Likelihood (0–100%) × impact (USD) scoring; inherent and residual risk computed; heatmap cell visualisation.
Risk–control mapping with coverage rating (none/partial/substantial/full) and control count per risk.
FAIR ALE per risk: TEF × Vulnerability × (Primary + Secondary Loss Magnitude) × (1 − Control Effectiveness), with RAV-adjusted ALE.
Treatment plans (strategies: mitigate, avoid, accept, transfer) cascading to treatment tasks with priority, assignee, due date, and status workflow.
Target/review dates with upcoming-review surfacing on the dashboard.
### 2.1.2 Control Library
Control inventory with type, implementation status (not_implemented / planned / in_progress / implemented / ineffective), maturity level (1–5), effectiveness score (0–1), implementation cost, and annual maintenance cost.
VoronRAV control classification (type + point contribution) feeding the quantification engine.
Evidence Locker per control: file upload with uploader attribution, size, timestamp; download/delete.
AI-prioritised recommendations: rule-based gap analysis (prioritizeControls) ranking recommended controls by expected ALE reduction and ROI ratio (3.0 / 1.5 / 1.0 / 0.5 / 0.25).
Maturity distribution chart and status summary metrics.
### 2.1.3 Policy Management
Policy lifecycle: draft → review → approved → retired, with four document types (Policy, Standard, Procedure, Guideline).
Version tracking (semantic versioning), effective/review dates with overdue-highlighting, document upload/download (PDF, DOCX, XLSX, PPTX, TXT, CSV, etc.), owner assignment.
Attestation-rate tracking per policy (acknowledged / total).
### 2.1.4 Policy Attestation & Acceptance
Bulk assignment of policies to users; statuses: pending / acknowledged / declined / waived; expiry dates.
Compliance-rate analytics and per-user "My Pending Attestations" view; overdue computation.
### 2.1.5 Board & Committee Management
Committees (board, audit, risk, compliance, sustainability, technology, remuneration, nomination, other) with chairperson, charter, members, frequency.
Meeting scheduling (in-person / virtual / hybrid) with agenda (items + owners + durations), minutes, and status workflow.
Action-item tracking with assignee, due date, priority, and status (open / in_progress / completed / overdue / cancelled).
### 2.1.6 Incident Management
Full incident lifecycle: reported → investigating → contained → resolved → closed, with 8 incident types and 4 severity levels.
CAPA (Corrective & Preventive Action) management with effectiveness review, verification, and closure.
Incident→risk and incident→control linking; financial impact tracking; regulatory notification flag.
Average resolution-time analytics.
### 2.1.7 Business Continuity Management (BCM)
BIA records: process-level impact analysis with RTO / RPO / MTD (in minutes, displayed in hours), staff counts, revenue impact/hour, regulatory impact, dependencies, criticality.
BCM documents: BCP, DRP, BCM policy, test plans, call trees with type/status/review dates.
BCM tests/exercises: tabletop, walkthrough, simulation, full live, technical — with status workflow and result/finding capture; links to BIA records and documents.
### 2.1.8 Operational Loss Database
14 loss event types; gross loss, net loss, recovery, and insurance amounts; risk ALE at event comparison; root-cause capture; statuses (open / under_review / closed / disputed).
YTD loss analytics and recovery-rate computation; linkage to the risk register.
### 2.1.9 Governance Support
Immutable audit log: append-only record of every CREATE, UPDATE, DELETE, LINK, UNLINK, SCORE, and QUANTIFY action with user attribution and timestamp.
User management: 7 roles, 30 permissions, invite/disable/password reset, org-scoped.
Settings: organisation profile, 8 display currencies (USD, MYR, SGD, IDR, EUR, GBP, AUD, JPY), configurable session timeout (15 min – 8 h).
## 2.2 Digital Risk Management & Quantification (DRM)
VoronCitadel's DRM domain differentiates it from generic GRC tools by making risk quantified and defensible, not just catalogued.
### 2.2.1 Asset Inventory & EVAT Scoring
Asset catalog with 7 asset types (information, hardware, software, service, people, facility, process), business unit, criticality (low/medium/high/critical), estimated value, owner.
OSSTMM-style EVAT scoring (Exposure, Visibility, Access, Trust, Controls) on 0–10 sliders plus a NIST surface-breadth score (0–100).
VoronRAV computation:
EVAT_mean = (E + V + A + T) / 4 (fusion weights: E 0.25, V 0.25, A 0.15, T 0.15, C 0.20)
RAV% = EVAT_mean × (10 − Controls_score)
Overall = w₁ × RAV + w₂ × NIST_surface (default 0.5 / 0.5)
Letter grade (A ≤ 15, B ≤ 30, C ≤ 50, D ≤ 70, F > 70) and risk band (Low → Critical).
Score history timeline per asset; bulk selection; filter/sort/pagination.
### 2.2.2 Risk Quantification Engine
FAIR ALE: ALE = TEF × Vulnerability × (PLM + SLM) × (1 − CE) with 9 category-specific default parameters; portfolio aggregation and RAV-adjusted ALE.
Monte Carlo simulation: 50,000 iterations, mulberry32 PRNG with ±20% triangular jitter, Dirichlet-distributed fusion weights; outputs mean, standard deviation, 95% and 99% confidence intervals, grade probability distribution (A–F), and 50-bucket score histogram.
Quantification run history; side-by-side asset EVAT comparison table; custom/manual EVAT input (no asset required).
### 2.2.3 Executive Analytics
C-suite metrics: open risks, total ALE, average compliance coverage, controls implemented.
Portfolio EVAT/grade distribution; total-ALE trend across runs.
Regression modelling: linear, logarithmic, and exponential fits for ALE projection; ALE-at-target-maturity projection; control-maturity-vs-ALE and compliance-vs-risk regressions.
Strategic analytics: loss exceedance curve, risk-appetite thresholding (default 25% of revenue), scenario analysis, trend forecasts, ROI.
PDF export of the executive strategic risk report.
## 2.3 Attack Surface Management — VoronScout OSINT Engine (ASM)
VoronScout is the production ASM capability: automated, outside-in discovery and scoring of the organisation's (and its vendors') externally exposed digital footprint. It runs as a server-side scanning engine with a TypeScript implementation and a Python CLI variant, exposed through the Vendors view.
### 2.3.1 External Asset Discovery
Company-mode discovery: Clearbit company autocomplete enrichment with DNS fallback to resolve candidate domains from a company name.
Domain/IP-mode discovery: direct scanning of specified domains or IPs.
Subdomain discovery: certificate-transparency monitoring via crt.sh (up to 120 subdomains per domain).
DNS resolution: A/AAAA via Node DNS and DNS-over-HTTPS (Google DoH) for A, MX, TXT (SPF/DMARC), and other record types.
TCP port scanning: non-invasive connect checks across a common-ports set; open-port enumeration per asset.
TLS/SSL assessment: certificate presence, issuer, validity, SAN list, expiry, TLS version negotiation.
RDAP/WHOIS: registrar and ownership lookup for domains and IPs.
HTTP(S) header inspection: security-header detection (HSTS, CSP, X-Frame-Options, etc.).
IP geolocation enrichment for discovered assets.
### 2.3.2 Exposure Findings & Scoring
Per-asset findings with severity, note, and value (e.g., TLS expiry ≤ 30/90 days, self-signed certs, weak ciphers, exposed management ports 22/3389, plain FTP/Telnet, HTTP-without-HTTPS, open DNS recursion, SMB exposure).
Automated mitigation recommendations per finding (e.g., harden SSH with key-only auth, block SMB, enforce HSTS).
Per-asset EVAT-style metrics (Exposure, Visibility, Access, Trust, Controls) recomputed from discovered surface; composite overall score (0–100) and letter grade (A–F).
Scan report history with reload; Rescan All batch operation across active vendors.
### 2.3.3 Threat Intelligence Integration
Scan results are cross-referenced into the vendor's TPRA composite score and surfaced in the vendor risk record.
Findings promote to the Risk Register or to tracked remediation items in one action.
## 2.4 Third-Party Risk Management & Assessment (TPRM / TPRA)
VoronCitadel governs the end-to-end third-party lifecycle and — uniquely for an MVP — runs an automated, multi-signal Third-Party Risk Assessment (TPRA) pipeline against each vendor.
### 2.4.1 Vendor Inventory
Vendor registry with type, tier (Tier 1 Critical / Tier 2 High / Tier 3 Medium / Tier 4 Low), criticality, contact, website, annual spend, contract start/expiry/notice period, data-classification, DPA/SLA flags, and status (active / inactive / under_review / terminated).
Expiring-contract alerts (90-day window); at-risk vendor flagging (overall risk score > 0.5).
Side-by-side vendor comparison; vendor dashboard with tier distribution, risk-score distribution, vendor status, and open-remediation metrics.
### 2.4.2 Vendor Assessments
Assessment types: onboarding, annual, quarterly, incident_triggered, termination; statuses: planned / in_progress / completed; score/max-score ratio.
Certification tracking (vendor-held certs with issue/expiry).
Remediation tracking per vendor with severity, assignee, priority, due date, and status workflow.
### 2.4.3 Continuous Monitoring (Production-Enabled)
Scheduled TPRA monitoring runs every 6 hours in production (configurable interval) across all active vendors.
Cyber intelligence: Shodan (open ports/services/TLS), VirusTotal (domain reputation/detections), AlienVault OTX (pulse mentions), AbuseIPDB (IP abuse reports), PhishTank (phishing checks), NVD/CVE (vulnerability lookup), GitHub Patchwork (repo freshness/commit activity).
Adverse media: GNews, GDELT, and NewsAPI aggregation with risk-keyword matching (breach, hack, ransomware, fined, penalty, lawsuit, fraud, scandal, investigation, sanction, regulatory action, outage, bankruptcy, default, suspension, revoked).
Supply-chain intelligence: OSV, npm-audit, and PyPI vulnerability scanning of vendor-linked packages.
Geopolitical & financial: Corruption Perception Index / FATF grey-list analysis, and Freedom/GPI government-policy indices.
AI-assisted threat assessment via the sovereign LLM, with provenance logging.
### 2.4.4 TPRA Composite Scoring
Weighted composite across six dimensions:
Cyber 25% · Financial 20% · Compliance 20% · Operational 15% · Reputational 10% · Geopolitical 10%
Dimension-level breakdowns; letter grade (A/B/C/D/F) and risk band (Low / Medium / High / Critical); per-vendor score history (vendor_score_history) and monitoring-alert feed (vendor_monitoring_alerts).

# 3. Compliance Framework Integration
Compliance framework support is built into the core data model, not implemented as a reporting overlay. The framework layer maps each standard's requirement tree to the platform's Control entity, so a single control record can simultaneously satisfy requirements across multiple frameworks. Analysts select the active framework context; the platform applies the corresponding requirement mapping without duplicating control records or evidence.
## 3.1 Supported Frameworks — Production (Verified in Database)

Total: 5 frameworks · 295 requirements (confirmed against the production database).
## 3.2 Framework Data Model
Each framework is a hierarchical requirement tree. Requirements carry codes, titles, descriptions, domain groupings, and framework associations.
Requirement-level coverage status: full / partial / not_covered, driven by linked controls (via control_framework_mappings).
Cross-framework references: requirement_cross_references maps equivalences between requirements across frameworks (e.g., an ISO 27001 Annex A control ↔ NIST CSF subcategory ↔ BNM RMiT paragraph), with verification and bulk propagation.
## 3.3 Multi-Framework Control Mapping
One-to-many: a single control maps to requirements in multiple frameworks simultaneously (e.g., an encryption-at-rest control satisfying ISO 27001 A.8.x, NIST CSF PR.DS, and BNM RMiT technology-security requirements).
Evidence inheritance: evidence attached to a control or requirement is visible across every framework the item maps to, without re-upload.
Gap visualisation: requirements with no mapped control, partial coverage, and full coverage are distinguishable; the compliance dashboard aggregates coverage per framework, per domain, and overall.
## 3.4 Evidence Management
Central evidence repository (compliance_evidence) with file upload, description, and status workflow (draft / submitted / approved / rejected).
AI-assisted evidence: the sovereign LLM can draft evidence descriptions for requirements and suggest coverage status with confidence and reasoning (see Section 4).
## 3.5 Compliance Dashboard & Reporting
Per-framework coverage percentage with color-coded progress bars and domain-level breakdown.
Framework list (issuing body, jurisdiction), total requirements, full-coverage count, gap count, evidence count, requirements-with-evidence count.
Compliance posture feeds the Dashboard, Executive View, Board Report, and PDF exports.
## Framework Governance
Framework requirement data is versioned in the database and maintained by the platform team; tenants can migrate mappings when a framework version changes. Custom framework addition (internal policy frameworks or additional regulatory standards) is a Phase 2 capability.

# 4. Sovereign AI Copilot
The VoronCitadel Copilot is a production-deployed AI capability grounded in Malaysian sovereign AI: the platform calls a sovereign LLM endpoint (Qwen 3.5-27B served via Aras Integrasi) through a server-side proxy. The LLM has no direct access to tenant data — every call is prompt-constructed server-side from structured platform data, and every call is logged to an AI-provenance audit trail.
## 4.1 Architecture

## 4.2 Core Copilot Capabilities (Production)
1.  Compliance narrative generation — executive risk summary from live posture data (open risks, critical risks, total ALE, top risk, top gap, average compliance). Includes a deterministic rule-based fallback so the feature never fails when the LLM is offline.
2.  Evidence auto-drafting — generates a 2–3 sentence evidence description for a requirement given the linked control and coverage status.
3.  Coverage-status suggestion — analyses a requirement, its linked control, and attached evidence, and recommends full / partial / gap with confidence and one-line reasoning.
4.  Cross-framework cross-referencing — given a requirement, proposes equivalent requirements in other frameworks (up to 5) with overlap reasoning.
5.  Acceptance/rejection feedback loop — analysts log accepted/rejected AI recommendations, which persist to the audit trail for model tuning.
6.  AI-assisted TPRA threat assessment — vendor threat narrative generated during the third-party risk assessment pipeline.
## 4.3 AI Governance & Data Boundaries
No tenant data is used to train the underlying model; all requests are stateless completions.
All Copilot reasoning is logged and auditable (model, prompt fingerprint, output, latency, user, residency).
Rule-based fallbacks guarantee availability of the narrative and evidence features even when the model endpoint is offline.
The AI Sovereignty Score gives organisations a quantifiable measure of AI data residency and auditable AI decision-making — aligned with Malaysian regulatory expectations for data localisation and accountability.

# 5. User Personas & Core Workflows
## 5.1 Persona Definitions

## 5.2 Role-Based Access Control
Seven roles with 30 granular permissions. Every route is guarded by a RequirePermission wrapper; permissions are enforced server-side via authenticated routes.

## 5.3 Core Workflows
Risk Analyst — Daily Risk Operations
1.  Review dashboard KRIs: open risks, total ALE, controls implemented, average compliance.
2.  Review the risk register; triage by ALE; update likelihood/impact and treatment progress.
3.  Create or update treatment plans and tasks; assign owners and due dates.
4.  Map controls to risks; confirm coverage rating and residual-risk impact.
5.  Review control recommendations for the highest-gap risks; action high-ROI suggestions.
6.  Promote OSINT scan findings (from TPRM/Vendor view) into the risk register or remediation queue.
Compliance Officer — Framework Assessment
1.  Open Compliance view; review per-framework coverage and gap counts.
2.  Drill into a requirement; review linked controls and evidence.
3.  Map additional controls from the library; attach evidence (upload or AI-drafted).
4.  Use the AI Copilot to suggest coverage status and cross-framework equivalences; accept/reject.
5.  Track evidence status (draft → submitted → approved → rejected) and AI provenance.
Third-Party Risk Manager — Vendor Assessment & Monitoring
1.  Register a vendor; set tier, contract dates, and data classification.
2.  Run VoronScout scan (company or domain/IP mode); review live streaming log and asset-level findings.
3.  Run an assessment (onboarding/annual/etc.); record score and status.
4.  Trigger the TPRA pipeline; review composite score and six-dimension breakdown.
5.  Review continuous-monitoring alerts (cyber-intel, adverse media, supply chain, geopolitical); open remediations.
6.  Promote findings to risks; track remediation to closure.
CISO — Monthly Risk Review
1.  Open Executive View; review portfolio ALE, compliance coverage, and Monte Carlo distribution.
2.  Review regression projections and ALE-at-maturity.
3.  Generate the Board Report; review the eight narrative sections; export PDF.
4.  Review AI sovereignty score and AI compliance audit trail.
Board Reporting
The Board Report module aggregates ten data sources into eight narrative/visual sections: Risk Posture, Compliance, Vendors, Incidents, BCM, Loss, Attestation, and Governance (committees), exported as a structured A4 PDF via jsPDF.

# 6. Technical Architecture
## 6.1 Production Stack (Verified on the Live Server)

## 6.2 API Architecture
Versioned REST API under /api/v1-style route groups (auth, risks, controls, assets, policies, compliance, evidence, quantification, evat-scores, mappings, treatment-plans, committees, attestations, vendors, tprm, tpra, bcm, incidents, loss-events, audit, users, org, ai).
JWT bearer authentication with role-based permission checks; rate limiting per request path.
Live scan streaming via Server-Sent Events (SSE) for VoronScout runs, with client-side abort support.
File upload/download endpoints for policies and evidence with metadata capture.
All mutations append to the immutable audit_log; AI calls append to ai_compliance_audit_log.
## 6.3 Integration Connectors (Production)

## 6.4 Security Model
Authentication: JWT with refresh; brute-force protection via login_attempts tracking; configurable idle session timeout (15 min – 8 h); password hashing (bcrypt, 10 rounds).
Authorisation: server-side RBAC on every route; client route guards (RequirePermission); org-scoped queries.
Data security: all API traffic over TLS via Nginx; database isolated in Docker network (published on localhost); secrets managed in server-side environment files (not client code).
Auditability: append-only audit log for all entity mutations; AI-provenance log for all AI calls with data_residency = 'on_prem'.
AI sovereignty: sovereign LLM only; no tenant data sent to foreign-hosted model endpoints.
## 6.5 Scalability Notes
The MVP is a single-node deployment (Docker Compose on one host). The architecture supports the production load observed (single demo tenant) and scales horizontally at the Phase 2 boundary via stateless API containers, connection pooling, and separation of the VoronScout scanner into a dedicated worker pool.

# 7. MVP Scope Boundaries
## 7.1 In Production (MVP — Verified)

## 7.2 Deferred to Phase 2


# 8. Appendix: Entity Relationship Summary
## 8.1 Core Relationships (45 Production Tables)

## 8.2 Compliance Framework Requirement Counts (Production)

## 8.3 Scoring Reference

## 8.4 Glossary

# Document Version History

This document is subject to revision as the platform evolves. Material changes to scope or architecture will be versioned and circulated for stakeholder review.

| Strategic Differentiation
Unified data model: one canonical representation of risks, assets, controls, policies, vendors, findings, and evidence across all platform domains, on a single PostgreSQL instance (45 relational tables).
Quantification-first risk management: OSSTMM-inspired VoronRAV asset scoring, FAIR-model Annual Loss Expectancy (ALE), and 50,000-iteration Monte Carlo portfolio simulation built into the core engine — not bolted on.
Sovereign AI Copilot: deployed on a Malaysian sovereign LLM (Qwen 3.5-27B via Aras Integrasi), with full AI-provenance audit logging and a platform "AI Sovereignty Score". No tenant data leaves the platform's controlled data boundary.
Malaysian regulatory alignment: BNM RMiT, SC GTRM, and Bursa Malaysia Cybersecurity controls built into the core framework layer, alongside ISO 27001:2022 and NIST CSF 2.0 — a critical differentiator for the APAC market.
Automated third-party intelligence: continuous TPRA monitoring (every 6 hours in production) combining cyber-intel feeds, adverse-media, supply-chain, and geopolitical scoring with ASM-style external footprint scanning. |
|---|


| Entity | Description | Primary Domain | Cross-Domain Consumers |
|---|---|---|---|
| Organisation | Root tenant entity; contains all risks, assets, controls, policies, and relationships | Platform | All domains |
| Risk | Identified risk event with likelihood, impact, inherent/residual scores, category, owner, treatment | GRC | Quantification, Compliance, ASM, TPRM |
| Asset | Declared resource: information, hardware, software, service, people, facility, process | DRM / ASM | GRC, Compliance, TPRM |
| Control | Safeguard or countermeasure with maturity, effectiveness, implementation cost, and framework mappings | GRC | DRM, Compliance, TPRM |
| Policy | Governance document (policy, standard, procedure, guideline) with version, owner, effective/review dates | GRC | Attestation, Compliance |
| Finding / Exposure | Specific observed weakness or exposure (OSINT scan finding, vulnerability, remediation item) | ASM / TPRM | GRC, TPRM |
| Vendor / Party | Any external third party with tier, contract, data access, certifications | TPRM | ASM, GRC, DRM |
| Assessment | Structured evaluation event: vendor assessment, TPRA run, control test, incident | All domains | All domains |
| Framework | Compliance standard with its requirement tree (5 frameworks) | GRC / Compliance | All domains |
| Evidence | File or AI-generated artifact attached to a control or requirement | GRC / Compliance | Compliance, Audit |


| Domain | Owns | Consumes from |
|---|---|---|
| GRC | Risk register, treatment plans, controls, policies, attestations, committees, incidents, BCM, loss database, audit log | Findings/risks from TPRM & ASM; compliance coverage from Compliance |
| DRM (Quantification) | EVAT/VoronRAV scoring, FAIR ALE, Monte Carlo simulation, quantification run history | Asset registry; control effectiveness; risk register data |
| ASM (VoronScout) | External asset discovery (domains, subdomains, IPs), exposure findings, scan history | Vendor digital identifiers from TPRM; threat data |
| TPRM | Vendor registry, tiering, assessments, TPRA composite scoring, continuous monitoring, remediation | ASM scan findings; cyber-intel/adverse-media/supply-chain/geopolitical feeds |


| Design Decision: Single-Schema Event Consistency. All cross-domain flows operate over the same PostgreSQL schema with server-generated audit logging (audit_log) for every create/update/delete/link/score action. This provides read-your-writes consistency and an immutable change trail without introducing a separate message bus in the MVP. A domain-event bus is the anticipated Phase 2 evolution (see Section 7). |
|---|


| GRC: Phase 2 Deferrals
Automated regulatory-change monitoring feed.
RCSA (Risk and Control Self-Assessment) module.
Integrated employee-facing GRC chatbot.
Automated sub-processor discovery (manual entry remains for MVP). |
|---|


| DRM: Phase 2 Deferrals
Multi-period VaR / Tail-VaR portfolio analytics.
Automated threat-intelligence feed ingestion (NVD/CVE correlation is available at vendor level in Phase 1; asset-level correlation is Phase 2).
Brand and dark-web monitoring. |
|---|


| ASM: Phase 2 Deferrals
Authenticated (credentialed) web application scanning.
Phishing lookalike / typo-squatting domain monitoring.
Mobile application surface monitoring.
Peer benchmarking against anonymised industry surface scores.
Continuous scheduled re-scanning of the full asset registry (MVP supports on-demand + vendor-triggered scans). |
|---|


| TPRM: Phase 2 Deferrals
Automated sanctions-list feed (manual flag remains in MVP).
Automated financial-health feed (credit rating, news alerts).
N-tier (vendor-of-vendor) sub-processor mapping and visualisation.
Shared vendor collaboration portal for joint remediation tracking. |
|---|


| Framework | Code | Jurisdiction | Requirements |
|---|---|---|---|
| ISO 27001:2022 | ISO_27001 | International | 93 (full Annex A) |
| NIST Cybersecurity Framework 2.0 | NIST_CSF_2.0 | United States | 57 (core functions/subcategories) |
| BNM RMiT (Risk Management in Technology) | BNM_RMiT | Malaysia | 41 |
| SC GTRM (Guidelines on Technology Risk Management) | SC_GTRM | Malaysia | 43 |
| Bursa Malaysia Cybersecurity Controls | BURSA_CYBER | Malaysia | 61 |


| Layer | Function | Technical Mechanism |
|---|---|---|
| Sovereign LLM Gateway | Proxy all AI requests to the sovereign endpoint (OpenAI-compatible /v1/chat/completions or local Ollama format) | SOVEREIGN_LLM_ENDPOINT / SOVEREIGN_LLM_MODEL / SOVEREIGN_LLM_API_KEY; 90 s timeout |
| Health Monitor | /api/ai/health — live connectivity, model identity, latency | Server ping with 30 s timeout; status: connected / degraded / offline |
| AI Provenance Log | Append-only record of every AI call: organisation, requirement, action type, model, prompt hash (SHA-256), output summary, input context, latency, user, and data_residency = 'on_prem' | ai_compliance_audit_log table |
| Sovereignty Score | Platform metric scoring data residency (30), audited decisions (30), model quality (20), AI evidence generation (20) | /api/ai/sovereignty-score |


| Persona | Description and Platform Role |
|---|---|
| Platform Administrator | Configures the platform: user management, organisation profile, settings, audit oversight. Full system access. |
| CISO / Security Director | Strategic owner of the risk programme; approves risk acceptance and escalations; consumes executive and board reporting. |
| Chief Risk Officer (CRO) | Owns the enterprise risk register; risk/committee write access; oversight across risk, controls, compliance. |
| Risk Analyst | Operational manager of the risk register: triages findings, manages treatment plans and tasks, links controls, quantifies risk. |
| Compliance Officer | Manages compliance posture across frameworks: maps controls, manages evidence, reviews coverage gaps. |
| Internal Auditor | Read-only evidence and control review for audit scoping and assurance activities. |
| Chief Financial Officer (CFO) | Consumes quantitative risk analytics: ALE, Monte Carlo, loss database, executive and board reporting. |
| Viewer | Read-only stakeholder with dashboard, risk, control, asset, compliance, and policy visibility. |


| Role | Domain Access | Permission Level |
|---|---|---|
| admin | All modules | Administer (all configuration, user management) |
| ciso | All modules | Edit (risks, controls, assets, policies, committees, BCM, incidents); Approve (risk acceptance, escalation) |
| cro | All modules | Edit (risks, committees, attestations); View elsewhere |
| cfo | Dashboard, Executive, Quantification, Compliance (read), Audit, Board Report, Loss DB, Help | View / report consumption |
| analyst | Risks, Controls, Incidents | Edit; View (assets, compliance, policies, vendors, BCM) |
| auditor | All modules (read) | View (evidence, controls, risks, assets); no user/settings management |
| viewer | Dashboard, Risk, Control, Asset, Compliance, Policy, Help | View only |


| Layer | Technology Choice | Notes |
|---|---|---|
| Frontend | React 18 + TypeScript 5 + Vite 8 + Tailwind CSS 3; Recharts; jsPDF + jspdf-autotable; Lucide icons | SPA served by the Express app |
| Backend | Node.js 22 + Express 4 + TypeScript; JWT (15-min access / refresh) + bcryptjs; express-rate-limit | 22 REST routers under /api/ |
| Database | PostgreSQL 16 (Docker, postgres:16-alpine); pg driver; schema auto-applied on startup (idempotent CREATE ... IF NOT EXISTS) | 45 tables; single instance |
| Containerisation | Docker Compose (db + app); Nginx reverse proxy with TLS; Tailscale network access | Production: vcitadeldemo host |
| Monitoring | Node cron-style scheduler for TPRA (enabled in production, 360-minute interval) | server/scripts/monitoring/monitor.ts |
| AI | Sovereign LLM via Aras Integrasi (Qwen 3.5-27B), OpenAI-compatible endpoint | No external-hosted model; on-prem data residency |
| OSINT | VoronScout (TypeScript engine + Python CLI) | In-process scanning workers |


| Category | Provider |
|---|---|
| Cyber Intelligence | Shodan, VirusTotal, AlienVault OTX, AbuseIPDB, PhishTank, NVD (CVE), GitHub Patchwork |
| Adverse Media | GNews, GDELT, NewsAPI |
| Supply Chain | OSV, npm audit, PyPI |
| Geopolitical / Financial | CPI / FATF, Freedom / GPI indices |
| OSINT Discovery | Clearbit, crt.sh, DNS/DoH, RDAP/WHOIS, TCP port probes, TLS inspection, HTTP header checks, IP geolocation |


| Domain | Feature Area | Included Capability |
|---|---|---|
| GRC | Risk Register | Full CRUD; 9 categories; likelihood×impact scoring; risk–control mapping; treatment plans + tasks; FAIR ALE per risk |
| GRC | Control Library | Inventory; maturity (1–5); effectiveness; implementation/maintenance cost; VoronRAV classification; evidence locker; AI-prioritised recommendations |
| GRC | Policy Management | Lifecycle (draft→review→approved→retired); 4 document types; versioning; document upload/download; attestation-rate tracking |
| GRC | Attestation | Bulk assignment; 4 statuses; compliance-rate analytics; overdue tracking |
| GRC | Committees | 9 committee types; meetings with agenda/minutes; action items |
| GRC | Incidents | Lifecycle; CAPA; risk/control linking; financial impact; regulatory flag |
| GRC | BCM | BIA (RTO/RPO/MTD); BCM documents; tests/exercises |
| GRC | Loss Database | 14 event types; gross/net/recovery/insurance; ALE comparison; YTD analytics |
| GRC | Governance | Immutable audit log; user management; org settings; 8 currencies; session timeout |
| DRM | Asset & EVAT | 7 asset types; EVAT sliders; VoronRAV grade/band; score history |
| DRM | Quantification | VoronRAV; FAIR ALE; 50k Monte Carlo; run history; asset comparison |
| DRM | Executive Analytics | Portfolio metrics; regressions; ALE-at-maturity; strategic analytics; PDF export |
| ASM | VoronScout | Company & domain/IP discovery; crt.sh; DNS/DoH; port scan; TLS; WHOIS/RDAP; HTTP headers; findings + mitigations; SSE live log; scan history; rescan |
| ASM | Promotion | Finding→Risk; finding→Remediation |
| TPRM | Vendor Inventory | Registry; 4 tiers; contracts; DPA/SLA; comparison; dashboard |
| TPRM | Assessments | 5 assessment types; score ratio; certifications |
| TPRM | Continuous Monitoring | 6-hourly scheduled TPRA; cyber-intel, adverse media, supply chain, geopolitical, AI threat assessment |
| TPRM | TPRA Scoring | 6-dimension weighted composite; grade/band; score history; alerts |
| Compliance | Frameworks | ISO 27001:2022 (93), NIST CSF 2.0 (57), BNM RMiT (41), SC GTRM (43), Bursa Cyber (61) = 295 requirements |
| Compliance | Mapping & Evidence | Control↔requirement mapping; requirement cross-references; evidence repository + workflow |
| Compliance | AI | Narrative; evidence drafting; coverage suggestion; cross-referencing; provenance audit; sovereignty score |
| Platform | Dashboard | KRI cards; radar; RAV gauge; ALE; compliance state; grade distribution; recent incidents; upcoming reviews |
| Platform | Board Report | 8 narrative sections; 10 data sources; PDF export |
| Platform | Reporting | Executive PDF; A4 board PDF |


| Feature Area | Phase 2 Capability |
|---|---|
| GRC — Regulatory Change | Automated regulatory-feed monitoring and change-impact analysis |
| GRC — RCSA | Risk and Control Self-Assessment module |
| GRC — AI Policy Drafting | AI-assisted policy drafting with regulatory-language suggestions |
| DRM — Asset-level TI | NVD/CVE correlation at asset level (vendor-level exists in Phase 1) |
| DRM — Dark Web / Brand | Dark-web credential monitoring; brand impersonation & typosquatting detection |
| ASM — Authenticated Scanning | Credentialed web application scanning |
| ASM — Continuous Full-surface Rescan | Scheduled re-scanning of the complete asset registry |
| ASM — Benchmarking | Peer/industry attack-surface benchmarking |
| TPRM — Sanctions Feed | Automated sanctions and regulatory-enforcement monitoring (manual flag in Phase 1) |
| TPRM — Financial Feed | Automated financial-health feed (credit rating, news) |
| TPRM — Sub-processors | Automated sub-processor discovery and N-tier mapping |
| TPRM — Vendor Portal | Shared remediation tracking with vendors |
| Frameworks — Custom | Custom framework builder and internal-policy frameworks |
| Compliance — SoA | ISO 27001 Statement of Applicability auto-generation |
| Platform — Multi-Tenant Console | Multi-organisation oversight console (subsidiary consolidation) |
| Platform — Domain Events | Domain-event bus / message-based cross-domain integration |
| Platform — Active-Active HA | Multi-region active-active deployment and customer-managed keys (BYOK) |


| Relationship | Cardinality | Owning Domain | Cross-Domain Significance |
|---|---|---|---|
| Organisation → Risk | 1:n | GRC | Root ownership; tenant isolation boundary |
| Organisation → Asset | 1:n | DRM/ASM | Root ownership of asset records |
| Organisation → Vendor | 1:n | TPRM | Root ownership of third-party records |
| Organisation → Framework | n:m (selected) | Compliance | Defines active frameworks |
| Risk → Control | n:m | GRC | Coverage rating drives residual risk |
| Risk → Treatment Plan → Task | 1:n → 1:n | GRC | Treatment cascade with tracked tasks |
| Asset → EVAT Score | 1:n | DRM | Score history preserved per asset |
| Control → Requirement | n:m | Compliance | Core of multi-framework compliance engine |
| Requirement → Framework | n:1 | Compliance | Each requirement belongs to one framework |
| Requirement → Cross-Reference | n:m | Compliance | Equivalences across frameworks |
| Control → Evidence | 1:n | Compliance | Evidence locker |
| Requirement → Evidence | 1:n | Compliance | Compliance evidence repository |
| Policy → Attestation | 1:n | GRC | Bulk acknowledgements per user |
| Vendor → Assessment | 1:n | TPRM | Periodic assessment history |
| Vendor → Scan Result | 1:n | TPRM/ASM | VoronScout scan history per vendor |
| Vendor → TPRA Score | 1:n | TPRM | Composite score; current = latest |
| Vendor → Score History | 1:n | TPRM | Score trending |
| Vendor → Monitoring Alert | 1:n | TPRM | Continuous-monitoring alert feed |
| Vendor → Remediation | 1:n | TPRM | Remediation workflow |
| Vendor → Certification | 1:n | TPRM | Certification expiry tracking |
| Incident → CAPA | 1:n | GRC | Corrective/preventive actions |
| Incident / Loss → Risk | n:1 | GRC | Financial impact & loss cross-reference |
| AI Call → Requirement/Org | n:1 | Platform | AI provenance audit trail (on_prem) |


| Framework | Requirement Tree |
|---|---|
| ISO 27001:2022 | 93 requirements (full Annex A) |
| NIST CSF 2.0 | 57 requirements (functions/subcategories) |
| BNM RMiT | 41 requirements (Risk Management in Technology policy) |
| SC GTRM | 43 requirements (Securities Commission technology risk guidelines) |
| Bursa Malaysia Cybersecurity | 61 requirements |
| Total | 295 requirements across 5 frameworks |


| Engine | Formula / Parameters |
|---|---|
| VoronRAV | EVAT_mean = (E+V+A+T)/4 · RAV% = EVAT_mean × (10−C) · Overall = 0.5·RAV + 0.5·NIST; weights E .25 / V .25 / A .15 / T .15 / C .20 |
| FAIR ALE | ALE = TEF × Vulnerability × (PLM + SLM) × (1 − Control_Effectiveness) |
| Monte Carlo | 50,000 iterations; mulberry32; ±20% triangular jitter; Dirichlet fusion; 95%/99% CI; grade probabilities; 50-bucket histogram |
| TPRA Composite | Cyber 25% + Financial 20% + Compliance 20% + Operational 15% + Reputational 10% + Geopolitical 10% |
| Grades / Bands | A/B/C/D/F; bands Low / Medium / Medium-High / High / Critical |


| Term | Definition as Used in This Document |
|---|---|
| ASM | Attack Surface Management — continuous outside-in discovery and monitoring of externally exposed digital assets |
| ALE | Annual Loss Expectancy — expected financial loss per year from a risk event (FAIR-style) |
| CAPA | Corrective And Preventive Action — follow-up actions attached to incidents |
| DRM | Digital Risk Management — quantification and management of digital/quantitative risk exposure |
| EVAT | Exposure, Visibility, Access, Trust — OSSTMM-inspired asset exposure dimensions |
| GRC | Governance, Risk and Compliance |
| KRI | Key Risk Indicator — metric signalling current or future risk exposure |
| MC | Monte Carlo simulation — 50,000-iteration portfolio risk simulation |
| MVP | Minimum Viable Product — the initial production release (this document) |
| RAV | Relative Attack-Surface Value — VoronRAV posture score |
| RBAC | Role-Based Access Control — permissions assigned to roles, users to roles |
| RTO/RPO/MTD | Recovery Time / Recovery Point Objective / Maximum Tolerable Downtime |
| RSWG | Bursa Malaysia Risk-Based Standards Working Group |
| SoA | Statement of Applicability (ISO 27001) |
| SSE | Server-Sent Events — used for live VoronScout scan streaming |
| Sovereign AI | LLM inference via a Malaysian-hosted/controlled model endpoint (Aras Integrasi / Qwen 3.5-27B) |
| TPRA | Third-Party Risk Assessment — automated multi-signal vendor risk pipeline |
| TPRM | Third-Party Risk Management |
| VoronRAV | VoronCitadel's OSSTMM-inspired composite asset risk score |


| Version | Date | Notes |
|---|---|---|
| 1.0 | August 2026 | Initial MVP specification grounded in the verified production deployment (VoronCitadel, vcitadeldemo host, PostgreSQL 16, Node 22). Covers GRC, DRM/Quantification, ASM (VoronScout), TPRM/TPRA, five compliance frameworks, Sovereign AI Copilot, technical architecture, and scope boundaries. |
