---
id: DOC-20260814-003
record_type: document
title: GovSec TIP MVP Product Specification v3.0
product: govsec-tip
initiative: INIT-20260811-001
category: mvp-specification
version: '3.0'
date: 2026-08-14
source_authority: DAF
sensitivity: confidential
status: archived
tags:
- domain/cybersecurity
- domain/threat-intelligence
- domain/cybersecurity-productisation
- product/govsec-tip
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

# GovSec TIP MVP Product Specification v3.0

> Canonical baseline document - uploaded by DAF, 14 August 2026
>
> CONFIDENTIAL - FOR EXECUTIVE AND ENGINEERING REVIEW




GOVSEC
Cyber Threat Intelligence Platform
MVP Product Specification

CONFIDENTIAL — FOR EXECUTIVE AND ENGINEERING REVIEW
Version 3.0  |  August 2026

# Document Version History

This document is subject to revision as MVP development progresses. Material changes to scope or architecture will be versioned and circulated for stakeholder review.

# Executive Summary
National cybersecurity operations in Malaysia today are fragmented. Analysts manage threat intelligence in one tool, detection and alerting in another, case response in a third, and compliance evidence — PDPA obligations, classification handling, audit trails in yet another, with no unified data model and no shared language across tiers. The result is duplicated effort, missed correlations at the seams between tools, and reporting that obscures rather than illuminates the national threat posture.
GovSec3.0 is a purpose-built, integrated National Cyber Threat Intelligence Platform that consolidates the intelligence-to-response continuum Threat Intelligence and Ingest, Analysis and Detection, Alerting and Response Operations, and Malaysian Government Governance and Compliance onto a single data fabric. Every feed, every indicator, every correlation, every alert, and every case is expressed in a shared object model, enabling correlations that no point solution can surface.
This document is the MVP product specification: a precise, actionable guide for executive stakeholders making investment decisions and for engineering leadership initiating development. It covers platform architecture, domain feature sets, framework and compliance integration, the AI Analyst workbench with its Copilot interface, the underlying data model, user personas and workflows, technical architecture, and scope boundaries.

Strategic Differentiation
Unified data model: one canonical representation of feeds, indicators, correlations, alerts, cases, and actors across all four domains.
Dynamic threat scoring: every indicator carries a 0–100 composite score (severity baseline, 30-day temporal decay, cross-source boost, correlation density, and feed diversity) that keeps threat prioritisation objective and current.
AI Analyst with Copilot interface: a RAG-powered conversational workspace that replaces tab-switching with natural language queries, automated briefing, and deterministic case report generation.
Malaysian government alignment: PDPA 2010 compliance engine, national classification levels (Rahsia, Sensitif, Terhad, Pertidahan, Awam) with compartment-based access, and a national APT group library — built into the core framework layer, not bolted on.
Frameworks natively integrated: MITRE ATT&CK mapping and detection coverage, NVD/CVE with CISA KEV tracking, and STIX/TAXII interchange supported in the data model rather than as reporting overlays.

# Contents

# 1. Platform Architecture & Unified Data Model
## 1.1 Architectural Philosophy

## Diagram 1: GovSec 3.0 Architecture

The central design principle of GovSec3.0 is that threat intelligence is a shared language, not a departmental dialect. Where traditional TIP point solutions — threat feed managers, SIEM correlation, case management, and GRC evidence stores — each maintain independent object models, GovSec3.0 starts from a canonical data fabric. Every domain reads from and writes to the same entity store.
This produces compound intelligence: a newly ingested indicator is immediately scored, correlated against existing indicators, mapped to MITRE ATT&CK techniques, attributed to known APT groups where possible, and linked to affected Malaysian government organisations — without any human joining of records. This is the primary architectural advantage over a best-of-breed portfolio.

## 1.2 Core Entity Model
The GovSec3.0 data model consists of twelve core entity types. Every domain-specific object is either a core entity or a typed extension of one.

## 1.3 Entity Relationships
The relationships between core entities define the data fabric. Key relationships are:
Feed → Indicator (1:n): every indicator records its source feed; feed health and provenance are traceable end to end.
Indicator → Correlation (n:m): indicators participate in many correlations; correlation density is a direct input to the dynamic threat score.
Indicator → Framework Entity (n:m): auto-mapped and analyst-confirmed links to MITRE ATT&CK techniques drive detection coverage and gap analysis.
Indicator → CVE (n:m): indicators link to vulnerability records; KEV status and CVSS influence prioritisation.
Indicator → Actor (n:m): attribution links indicators to APT groups via the national attribution pipeline.
Indicator → Organisation (n:m): organisation-level association surfaces agency-specific threat views and sector aggregates.
Correlation → Alert (1:n): new correlations are evaluated against enabled rules to generate alerts; dedup prevents duplicate alerting.
Rule → Alert (1:n): each alert records the rule and indicator set that triggered it.
Alert → Case (n:1): alerts are escalated or triaged into investigation cases; cases can consume multiple related alerts.
User → Alert / Case (1:n): assignment and escalation ownership are tracked through the lifecycle.
Audit Event → any entity (polymorphic): all data mutations and sensitive views are recorded against the acting user and resource.

## 1.4 Domain Boundary Map
The four domains share entities but own different aspects of their lifecycle. The following table maps entity ownership and consumption by domain.

## 1.5 Data Flow Architecture
Data flows bidirectionally between domains. The following describes the primary integration flows in the MVP:
Ingest → Analysis Flow: Feeds (scheduled, manual, file upload, or push API) produce indicators and STIX objects. Each indicator is validated per type, deduplicated by fingerprint, geo-enriched, and assigned an initial severity and TLP. The dynamic scoring pipeline then computes a 0–100 threat score with a 30-day temporal half-life.
Analysis → Alerting Flow: The correlation engine (every 15 minutes) discovers relationships using shared-ASN, IP/domain resolution, malware family attribution, C2 infrastructure, and shared certificate techniques. New correlations trigger evaluation against enabled alert rules; matches generate alerts that are deduplicated by fingerprint and auto-escalated by severity and timeout.
Alerting → Operations Flow: Critical and High alerts not acknowledged within configured windows are escalated with a full escalation log. Analysts convert alerts into cases, attach notes and artifacts, and drive resolution with recorded response times.
Governance → All Domains Flow: Classification levels and compartments constrain visibility at every layer. The PDPA pipeline scans indicators for PII (NRIC, email, phone, bank, card), flags and redacts matches, records PII access in the audit log, and enforces retention policies. All of this is written to the immutable audit trail.

Design Decision: Scheduled Event-Driven Integration. Cross-domain flows are implemented as twelve scheduled pipelines (feed ingestion, correlation, alert evaluation, MITRE mapping, threat scoring, NLP classification, alert dedup, PII scan, data retention, hunt execution, MITRE coverage, escalation) coordinated by the platform scheduler. Each pipeline is idempotent and records its run status in scheduler_jobs, providing loose coupling between domains while maintaining data consistency.

# 2. Domain Feature Sets
This section specifies the MVP feature set for each of the four domains. For each capability, the inclusion decision is noted along with the rationale where non-obvious. Features deferred to Phase 2 are listed at the end of each domain section; a comprehensive scope boundary table appears in Section 7.

# 2.1 Threat Intelligence & Ingestion (TIP)
The ingestion domain is the entry point of the platform. It normalises intelligence from heterogeneous sources into a single indicator model, preserving provenance and feed health. The MVP integrates feed types spanning STIX/TAXII, commercial and open feeds (AlienVault OTX, Abuse.ch URLhaus, MalwareBazaar), MISP, generic REST JSON, CSV, and a Logstash ingestion bridge.
### 2.1.1 Feed Management
Feed registry with per-feed configuration, enable/disable controls, and last-run health status
Scheduled ingestion (configurable intervals) with trigger-type tracking (scheduled, manual, file_upload)
Ingestion job ledger recording processed, skipped, and errored counts per run
STIX 2.1 object storage preserving raw bundles alongside normalised indicators
Feed provenance preserved on every indicator (source_feed_id) to enable cross-source scoring
CSV and REST JSON ingestion with field mapping and per-type value validation
Push ingestion API authenticated by static API key for external integrations (e.g., Lebahnet)
Logstash ingestion bridge mapping Elastic Common Schema (ECS) fields to platform indicator types
Feed disablement and health dashboards for pipeline monitoring
### 2.1.2 Indicator Enrichment
IP geolocation enrichment via ip-api.com with batch backfill and cache
Severity and TLP assignment at ingestion with per-type defaults
Indicator tags and metadata (original timestamp, event action, event category) preserved from source
Intra-batch deduplication at ingestion and cross-batch fingerprint-based duplicate suppression
CVE reference recognition: indicators of type cve validated against NVD synchronisation
### 2.1.3 CVE and Vulnerability Data
NVD-based CVE library with search and periodic synchronisation
CVSS v3/v4 scoring stored per vulnerability
CISA Known Exploited Vulnerabilities (KEV) tracking with due dates and ransomware flags
Indicator-to-CVE linking enabling exposure-based prioritisation
TIP: Phase 2 Deferrals
Dark web monitoring (credential exposure, leaked data)
Brand and executive monitoring (impersonation, typosquatting)
Custom threat intelligence feed management console for tenant-managed MISP instances
Automated sanctions and enforcement-action monitoring feeds

# 2.2 Analysis & Detection
The analysis domain is the analytical core of the platform. It owns the indicator library, the dynamic scoring engine, the correlation engine, detection rules, MITRE ATT&CK coverage, and the threat hunting workbench.
### 2.2.1 Indicator Library
Searchable indicator repository across IP, domain, hash (MD5/SHA1/SHA256), URL, email, and CVE types
Indicator detail views with severity, TLP, tags, source feeds, correlations, MITRE mappings, and APT attribution
Type/severity filtering, country aggregation, and time-series distributions
Score history per indicator via the score_history ledger
### 2.2.2 Dynamic Threat Scoring
Each indicator carries a composite 0–100 dynamic score. The scoring model balances intrinsic severity with temporal relevance and analytical signal:
Severity baseline (0–25): critical 25, high 20, medium 15, low 10, info 5.
Temporal decay (0–25): exponential decay with a 30-day half-life — newer indicators score higher.
Cross-source boost (0–20): correlations spanning multiple feeds lift the score.
Correlation density (0–20): heavily correlated indicators are riskier.
Feed diversity (0–10): presence across distinct feeds adds confidence.
Score recomputation every 30 minutes for stale indicators (6-hour staleness window)
Score distribution analytics and top-scored indicator rankings for triage
Score history tracking enabling trend visualisation
### 2.2.3 Correlation Engine
Relationship types: resolves-to, related-to, attributed-to, uses, hosted-on, shares-infrastructure
Correlation techniques: shared-ASN, IP/domain resolution, malware family attribution, C2 infrastructure, shared registrar/certificate
Fingerprint-based deduplication of discovered correlations
Correlation feed into alert evaluation and dynamic scoring
Correlation graph visualisation (D3 force-directed) and map visualisation (Leaflet) with type/severity filters
### 2.2.4 MITRE ATT&CK Integration
Technique, group, and tactic pages with detail drill-down
Auto-mapping of unmapped indicators to techniques (hourly scheduled pipeline)
Materialised detection coverage tracking with gap analysis and heatmap
Rule binding to MITRE techniques for detection-to-framework traceability
MITRE gap map within the threat hunting workbench
### 2.2.5 Threat Hunting Workbench
JSON DSL query builder over the indicator store
Saved hunts with scheduling and repeatable execution
Hunt results with export capability
Hunt playbooks and MITRE gap map for structured hypothesis testing
### 2.2.6 Threat Actors and National APT Library
National APT group library (APT28/30/32, Lazarus, Mustang Panda, Volt Typhoon, and more) with aliases, motivations, and targeting
Indicator-to-APT attribution pipeline with attribution dashboard
Threat actor pages consolidating linked indicators, techniques, and attribution
### 2.2.7 NLP Auto-Classification
Automatic classification of new indicators into actors, malware, and campaigns via LLM
Scheduled classification every 20 minutes with rate limiting to protect the LLM endpoint
Failure tracking and skip-ahead on classification saturation
Analysis: Phase 2 Deferrals
AI-generated hunt query suggestions from natural language hypotheses
Full-text and vector semantic search for the AI Analyst context assembly
Peer/community intelligence correlation
Automated playbook execution from correlation outcomes

# 2.3 Alerting & Response Operations
The operations domain converts analytical signal into action. It owns detection rules, the alert lifecycle, deduplication, escalation, and case management.
### 2.3.1 Detection Rules
Rule engine with severity thresholds, indicator-type selection, and MITRE technique binding
Rule enable/disable and audit trail for every rule change
Periodic evaluation of rules against new indicators and correlations
Batch evaluation to protect memory on large datasets
### 2.3.2 Alert Lifecycle
Alert status workflow: open → acknowledged → investigating → resolved / false_positive
Fingerprint-based deduplication with auto-close of stale duplicate alerts
Rule-driven auto-escalation by severity (Critical 15 min, High 60 min) and investigation timeout
Escalation log recording every escalation decision
Alert response-time analytics for resolved alerts
Live open-alert count badge and recent critical/high alert feed
### 2.3.3 Case Management
Case creation, assignment, priority (P1–P4), and status tracking
Case detail with notes, artifacts, timeline, and linked alerts
Case priority-aware executive reporting (active cases, P1 counts)
Deterministic case report generation from the embedded MITRE ATT&CK knowledge base
### 2.3.4 Executive and Operational Dashboards
Operational dashboard with security metrics, charts, and summary widgets
Executive dashboard with 20+ parallel aggregation queries: posture indicators, metric grids, severity distributions, response times, org and sector breakdowns
Geographic intelligence map and correlation graph widgets
Threat visualisation workspace consolidating graph and map views with tabbed navigation
Operations: Phase 2 Deferrals
Bidirectional ticketing integration (Jira, ServiceNow) for remediation handoff
SIEM bidirectional integration (Splunk, Microsoft Sentinel)
SOAR-style automated response playbooks
Collaborative investigation workspaces with concurrent analyst presence

# 2.4 Governance & Compliance (Malaysian Government)
The governance domain is the trust layer of the platform. It enforces role-based access with classification-aware compartments, maintains the national organisation hierarchy, operates the PDPA compliance engine, and preserves a complete audit trail.
### 2.4.1 Government Organisation Structure
Org tree with recursive hierarchy, agency codes, org types, and sector assignment
Malaysian classification levels per node: Rahsia, Sensitif, Terhad, Pertidahan, Awam
Per-organisation threat indicator linkage and alert association
Sector-level aggregation for executive reporting
### 2.4.2 RBAC and Compartment Access
Role hierarchy: analyst → senior_analyst → administrator
Classification-level enforcement across routes, pages, and navigation
Compartment-based visibility restricting access to authorised organisations
Route-level and page-level protection with minimum-role requirements
Enforcement at both API and UI layers; no client-side authorisation decisions
### 2.4.3 PDPA Compliance Engine
PII detection across Malaysian identifiers: NRIC, email, phone, bank account, credit card
Scheduled PII scans every 4 hours over new indicators
Redaction handling for exposed personal data
PII access audit log recording every access to sensitive indicators
Data retention policy enforcement with daily purge job and per-policy counts
### 2.4.4 Audit and Administration
Immutable audit log for login, failed login, ingest, correlate, alert update, rule change, user management, export, and feed management
User administration with role assignment and account lifecycle (activate/deactivate)
Password policy enforcement (complexity, 8+ characters) and admin-mediated password change
Self-service profiles with personal audit trail
Session timeout with configurable inactivity auto-logout
Login brute-force mitigation (5 attempts / 15 minutes per account)
Scheduler status dashboard exposing all twelve pipelines and their run health
Governance: Phase 2 Deferrals
Customer-managed encryption keys (BYOK/HYOK) for high-assurance deployments
MFA / SAML 2.0 and OIDC SSO integration
Automated regulatory change monitoring for PDPA and related instruments
Multi-region active-active deployment for 99.99% availability

# 3. Framework & Compliance Integration
Framework support is built into the core data model, not implemented as a reporting overlay. The framework layer maps standards and datasets to core entities — indicators to MITRE techniques, indicators to CVEs and KEV status, personal data to PDPA obligations, and records to classification levels — enabling a single platform to simultaneously satisfy analytical and compliance requirements.
## 3.1 Supported Frameworks — MVP

## 3.2 MITRE ATT&CK Integration Model
MITRE ATT&CK is the platform’s primary analytical framework. Indicators are mapped to techniques through an auto-mapping pipeline that runs hourly, with analyst confirmation available for ambiguous mappings. Detection coverage is materialised per technique, enabling:
Coverage heatmap across the full technique catalogue
Gap analysis identifying techniques with no mapped indicators or rules
Rule-to-technique binding for detection-to-framework traceability
Hunt-driven gap closure via the MITRE gap map in the hunt workbench
Case report generation grounded in the embedded MITRE ATT&CK knowledge base
## 3.3 CVE and KEV Pipeline
CVE records synchronised from NVD with CVSS v3/v4 scoring
CISA KEV enrichment: due dates and ransomware flags drive prioritisation
Indicator-to-CVE linking surfaces vulnerable-adjacent indicators in alert evidence
CVE search and library views for analysts
## 3.4 PDPA Compliance Engine
Detection of Malaysian personal identifiers across ingested indicators
Scheduled scanning every 4 hours with per-scan detection counts
Redaction workflow for exposed personal data
PII access audit log — every access to sensitive indicators is recorded
Data retention enforcement: configurable policies with daily purge and per-policy deletion counts
## 3.5 Classification and Compartment Access
All intelligence data is subject to the national classification model. Each organisation node in the hierarchy carries a classification level; user compartments gate visibility to authorised organisations and levels. The platform enforces classification at the route, page, and navigation layers, with the API enforcing the same constraints server-side.
## 3.6 Framework Governance
Framework datasets (MITRE ATT&CK, CVE/KEV, PDPA patterns, classification taxonomy) are maintained by the platform team and versioned. Regulatory or dataset updates are published as platform releases with migration scripts; tenants are notified and can re-run mapping pipelines against updated catalogues.

# 4. AI Analyst & Analyst Workbench
The Analyst Workbench is the defining UX innovation of GovSec3.0. Where analyst teams typically move between feed consoles, SIEM query tools, and case trackers to understand a threat, the Workbench presents a unified workspace where the entire intelligence-to-response continuum is reachable through a single interface, with an AI Analyst that understands the data model and can surface cross-domain insights automatically.
The AI Analyst is not a chatbot wrapper around a search function. It is an AI reasoning layer grounded in the platform data fabric that can retrieve structured context, render results as tables and charts, and generate contextualised analysis — not just retrieved facts.
## 4.1 Workbench Layout
Navigation: grouped sidebar (Overview, Intelligence, Operations, Analysis, Administration, Reference) with role-based visibility.
Primary workspace: the active dashboard, indicator, alert, case, or hunt view.
Dashboard widgets: geographic intelligence map and correlation graph widgets alongside metric summaries.
Threat visualisation: consolidated graph and map views with type/severity filters and country aggregation.
Universal search: debounced global indicator search in the header.
Alert awareness: live open-alert count badge in the header.
## 4.2 AI Analyst Architecture
The AI Analyst is powered by an LLM accessed through an OpenAI-compatible endpoint, with a structured retrieval-augmented generation (RAG) architecture. The model has no direct access to platform data; it operates through a query layer that retrieves structured context from the platform data fabric in response to the analyst’s natural language input.

## 4.3 Core AI Analyst Capabilities
### 4.3.1 Natural Language Queries
Analysts interact with the AI Analyst using natural language. It understands platform entities and relationships and can answer questions that require traversing multiple data sets:
"Summarise the threat posture for our sector in the last 30 days"
"Which indicators are correlated with this CVE and what is their dynamic score?"
"Show me all high and critical alerts opened in the last 24 hours"
"What MITRE techniques have no detection coverage for our organisation?"
"Which APT groups target our sector and what indicators are attributed to them?"
### 4.3.2 Automated Insight Generation
The AI Analyst surfaces insights based on data changes and scheduled analysis. Examples of the categories surfaced:
Scoring anomalies: indicators whose dynamic score spiked due to new correlations or cross-source confirmation.
Coverage emergence: newly discovered MITRE techniques or widening detection gaps.
Alert concentration: rule or source concentration indicating a potential campaign.
Retention and PDPA: PII detections, redactions, and upcoming retention purges.
### 4.3.3 Case AI
Deterministic case report generation from the embedded MITRE ATT&CK knowledge base
Structured narrative including affected indicators, techniques, and recommended next steps
Reduces report preparation time and standardises case documentation
### 4.3.4 NLP Auto-Classification
Automatic classification of new indicators into actors, malware, and campaigns
Scheduled pipeline with rate limiting to protect the LLM endpoint
Classification failures tracked and retried on subsequent cycles
## 4.4 Key AI Analyst Workflows

## 4.5 Learning, Privacy, and Boundaries
The AI Analyst operates within strict tenant data boundaries; no tenant data is used to train the underlying language model.
All AI queries are rate limited (20 requests/minute per user) and logged to the audit trail.
Conversation history is per-user, with ownership-enforced read and delete operations.
Prompt-injection defences screen both inputs and database-derived context before LLM interpolation.
The AI Analyst never accesses records the requesting user is not authorised to view; classification and compartment constraints apply to context assembly.
AI-initiated outputs that require platform actions (e.g., case creation) require explicit analyst confirmation and are logged.

# 5. User Personas & Core Workflows
## 5.1 Persona Definitions

## 5.2 Core Workflows by Persona
### 5.2.1 SOC Analyst — Daily Triage Workflow
1. Open the operational dashboard; review open-alert count and recent critical/high alerts.
2. Review new indicators in the library; inspect dynamic scores, correlations, and MITRE mappings.
3. Triage open alerts: acknowledge, investigate, resolve, or mark false positive with rationale.
4. Convert escalated alerts into cases; assign priority and owner.
5. Use the AI Analyst to summarise indicator context and draft case notes.
6. End of day: review personal task queue and confirm all critical alerts are acknowledged.

### 5.2.2 Senior Analyst — Threat Hunting Workflow
1. Open the threat hunting workbench; review the MITRE gap map for uncovered techniques.
2. Build a hunt query with the JSON DSL; save and schedule the hunt.
3. Review hunt results; promote high-confidence matches to alerts or cases.
4. Review escalation log; confirm escalation actions and escalate or close.
5. Author case reports using case AI; submit for sign-off.

### 5.2.3 Administrator — Configuration Workflow
1. Onboard users with role assignment and classification compartments.
2. Configure detection rules with severity thresholds and MITRE technique binding.
3. Manage threat feeds: enable/disable, set schedules, review feed health.
4. Review audit log for sensitive operations (exports, user management, rule changes).
5. Configure retention policies and verify PDPA enforcement runs.
6. Monitor scheduler status across all twelve pipelines.

### 5.2.4 CISO / Executive — Monthly Posture Review
1. Open the executive dashboard; review posture indicators and metric grids.
2. Review severity and score distributions; investigate movement in the 30-day ingest timeline.
3. Review alert response times for resolved alerts.
4. Review org and sector breakdowns; identify agencies with elevated threat exposure.
5. Explore the threat map and correlation graph for campaign-level context.
6. Prepare board reporting from the consolidated dashboard views.

## 5.3 Role-Based Access Control
Access control in GovSec3.0 is role-based with three dimensions: Role (analyst, senior_analyst, administrator), Classification (national levels from Awam to Rahsia), and Compartment (authorised organisations). Permission levels are enforced server-side on every route.

# 6. Technical Architecture
## 6.1 Stack Recommendation
The GovSec3.0 technology stack is selected to balance development velocity, operational maturity, and the specific demands of a data-intensive national intelligence platform. The following recommendations prioritise commercially proven technologies over novel choices.

## 6.2 Service Architecture
GovSec3.0 is implemented as a modular Node.js service architecture organised by concern. Each domain module owns its routes and services against a shared relational data model:
Feed and Ingestion: feed orchestration, STIX/CSV/REST parsing, Logstash bridge, CVE synchronisation, geo-enrichment, and push API.
Analysis: correlation engine, dynamic threat scoring, NLP classification, MITRE mapping and coverage, threat hunting, CVE/KEV, APT attribution, and gov-org linkage.
Alerting and Operations: rule evaluation, alert lifecycle, deduplication, escalation, and case management with case AI.
Governance: RBAC and classification enforcement, PDPA compliance, audit logging, profiles, and scheduler control.
AI Analyst: RAG context assembly, rate limiting, prompt-injection defence, conversation history, and structured-response rendering.

## 6.3 API Architecture
The platform exposes a versioned REST API across 23 modules and 147 endpoints, documented in an interactive API reference within the product. External API principles:
All endpoints require authentication (JWT bearer) except the push ingestion channel, which is authenticated by static API key.
RBAC and classification checks are enforced at the route layer; no client-side authorisation decisions.
Sensitive operations (export, user management, rule change, feed management) are recorded in the immutable audit log.
Payload size is capped (10 MB JSON) and query responses are batched to protect memory on large datasets.
Login is rate-limited (5 attempts / 15 minutes per account) with failed-login audit events.
Integration connectors: STIX/TAXII-compatible feeds, Logstash ECS bridge, push ingestion, and NVD CVE synchronisation.

## 6.4 Security Model
Given the sensitivity of national intelligence data, security is a first-class architectural concern, not a post-development overlay.
Data Security: encryption at rest for database storage; TLS in transit for all client-to-service communication; secrets managed through environment configuration and excluded from source control; data residency within Malaysian hosting environments.
Application Security: server-side RBAC and classification enforcement; brute-force mitigation on authentication; session timeout and inactivity auto-logout; password complexity policy; parameterised SQL throughout; audit logging of all data mutations and sensitive views.
AI Security: prompt-injection pattern screening on inputs and database-derived context; rate limiting (20 requests/minute/user); per-user conversation ownership; PII access audit on sensitive indicator retrieval; the AI Analyst never retrieves records outside the requesting user’s classification scope.
Remediation Baseline: a full security audit (OWASP Web Top 10, OWASP LLM Top 10, npm audit — 54 findings) was completed with a prioritised remediation plan; the identified critical and high items are remediated before production release.

## 6.5 Scalability Model
The MVP is designed for single-tenant government operation with national-scale data volumes. The following scaling assumptions inform the MVP architecture:
Indicator volume: designed to handle millions of indicator records with deduplication and batching; score recomputation capped at 2,000 records per cycle to bound load.
Correlation throughput: the correlation engine batches writes and deduplicates by fingerprint; alert evaluation batches by rule.
Feed cadence: scheduled ingestion with configurable intervals; the scheduler guarantees no overlapping runs per pipeline.
AI Analyst latency: context assembly is the primary latency driver and is bounded by structured SQL retrieval rather than full-dataset scanning.
Concurrency: Express handles request concurrency with per-route batching and pagination; the 10 MB body cap bounds ingress.

# 7. MVP Scope Boundaries
The following tables provide the definitive scope boundary for the MVP release. Features listed as Included are committed for the MVP. Features listed as Phase 2 are deferred — they are architecturally anticipated and will not require rework of core data structures, but are not committed for MVP delivery.
## 7.1 Included in MVP

## 7.2 Deferred to Phase 2

# 8. Appendix: Entity Relationship Summary
The following table summarises the core entity relationships described in Section 1. This is intended as a quick reference for engineering teams implementing the data model.

## 8.1 Framework Data Counts

## 8.2 Glossary


| Version | Date | Remarks |
|---|---|---|
| 1.0 | 20/3/2026 | Initial document |
| 2.0 | 6/6/2026 | Initial MVP specifications released |
| 3.0 | 6/8/2026 | Covers the four domains, framework and compliance integration, AI Analyst workbench, technical architecture, and scope boundaries. |


| Section | Title |
|---|---|
| 1 | Platform Architecture & Unified Data Model |
| 2 | Domain Feature Sets |
| 2.1 | Threat Intelligence & Ingestion (TIP) |
| 2.2 | Analysis & Detection |
| 2.3 | Alerting & Response Operations |
| 2.4 | Governance & Compliance (Malaysian Government) |
| 3 | Framework & Compliance Integration |
| 4 | AI Analyst & Analyst Workbench |
| 5 | User Personas & Core Workflows |
| 6 | Technical Architecture |
| 7 | MVP Scope Boundaries |
| 8 | Appendix: Entity Relationship Summary |


| Entity | Description | Primary Domain | Cross-Domain Consumers |
|---|---|---|---|
| Organisation | Malaysian government agency; node in the org hierarchy with classification level and sector | Governance | All domains |
| Feed | External or internal source of intelligence (STIX/TAXII, OTX, URLhaus, MalwareBazaar, MISP, REST JSON, CSV, Logstash) | Ingestion | Analysis, Governance |
| Indicator | Observable: IP, domain, hash (MD5/SHA1/SHA256), URL, email, CVE — with severity, TLP, tags, and dynamic score | Analysis | Ingestion, Alerting, Governance |
| Correlation | A detected relationship between indicators (resolves-to, related-to, attributed-to, uses, hosted-on, shares-infrastructure) | Analysis | Alerting, Governance |
| Rule | Detection logic (severity threshold, indicator types, MITRE techniques) that evaluates indicators and correlations | Detection | Alerting |
| Alert | A rule-triggered notification with severity, status lifecycle, dedup fingerprint, and escalation state | Alerting | Operations, Governance |
| Case | An investigation container with priority (P1–P4), notes, artifacts, and closure workflow | Operations | Alerting, Governance |
| Actor | A threat actor or national APT group with aliases, motivations, targeting profile, and attribution links | Analysis | Alerting, Governance |
| CVE | A vulnerability record with CVSS v3/v4 scoring and CISA KEV status (due date, ransomware flag) | Analysis | Ingestion, Alerting |
| Framework Entity | MITRE ATT&CK technique, tactic, or group used to map detection coverage | Analysis | All domains |
| User / Profile | Platform account with role (analyst, senior_analyst, administrator), classification compartments, and personal audit trail | Governance | All domains |
| Audit Event | An immutable, append-only record of platform activity (login, ingest, correlate, alert update, rule change, user manage, export) | Governance | All domains |


| Entity | Intelligence & Ingestion | Analysis & Detection | Alerting & Operations | Governance & Compliance |
|---|---|---|---|---|
| Feed | Owns feed configuration, scheduling, and health | Consumes feed provenance for scoring | Consumes feed health for alert context | Audits feed creation and updates |
| Indicator | Creates and enriches indicators; runs geo-enrichment | Owns scoring, correlation, MITRE mapping, attribution | Consumes indicators as alert evidence | Scans for PII; enforces retention |
| Correlation | Consumes new indicators as inputs | Owns the correlation engine and techniques | Triggers alert evaluation | Audits correlation discovery |
| Alert | Consumes alert evidence | Consumes correlated context | Owns alert lifecycle, dedup, escalation | Tracks alert audit trail |
| Case | Consumes case evidence | Consumes analytic context | Owns case lifecycle and prioritisation | Audits case activity |
| Rule | Consumes rule metadata | Provides rule definitions and MITRE technique binding | Evaluates rules to create alerts | Audits rule changes |
| Actor | Consumes actor intelligence | Owns APT library and attribution | Consumes attribution for alert context | Audits attribution changes |
| CVE | Syncs from NVD; flags KEV | Owns CVSS context and linkage | Consumes CVEs in alert evidence | Audits sync and links |
| Organisation | Consumes org classification | Filters by org and compartment | Assigns cases by org | Owns org tree, classification, PDPA |


| Framework | Coverage Scope in GovSec3.0 MVP |
|---|---|
| MITRE ATT&CK | Technique, tactic, and group library; auto-mapping of indicators to techniques; materialised detection coverage with gap analysis and heatmap; technique-bound detection rules. |
| NVD / CVE | CVE library with CVSS v3/v4 scoring, NVD synchronisation, search, and indicator-to-CVE linking. |
| CISA KEV | Known Exploited Vulnerabilities tracking with due dates and ransomware flags; integration into vulnerability prioritisation. |
| STIX / TAXII 2.1 | Structured threat intelligence interchange; STIX object storage and bundle ingestion from compliant feeds. |
| PDPA 2010 (Malaysia) | Personal Data Protection Act compliance engine: PII detection, redaction, access audit log, and data retention policy enforcement. |
| Malaysian Classification | National classification levels (Rahsia, Sensitif, Terhad, Pertidahan, Awam) and compartment-based access control over intelligence data. |
| OWASP (Engineering) | Application security baseline applied to platform development: OWASP Web Top 10 and OWASP LLM Top 10 risk categories remediated before release. |


| Copilot Layer | Function | Technical Mechanism |
|---|---|---|
| Input Understanding | Parse analyst query; identify intent, entity references, and domain context | Input validation, length caps, and injection-pattern screening |
| Context Assembly | Retrieve relevant indicators, alerts, correlations, and cases to ground the response | Structured SQL context assembly over the platform data fabric |
| Reasoning | Generate analysis grounded in retrieved context | LLM reasoning constrained to retrieved data; no access to unretrieved records |
| Response Generation | Generate natural-language response with structured data (tables, charts, matrices) | Streaming chat with structured-data rendering; per-user conversation history |
| Action Support | Support deterministic outputs such as case reports | Deterministic case report generation from the embedded MITRE knowledge base |


| Workflow | Trigger | AI Analyst Actions |
|---|---|---|
| "Brief me on today" | Analyst opens AI Analyst after shift handover | Retrieves indicators and alerts since the last briefing, groups by significance, and generates a prioritised summary with links to affected records. |
| "Assess this indicator" | Analyst selects an indicator and invokes the AI Analyst | Retrieves dynamic score components, correlations, MITRE mappings, attribution, and PII status; generates a risk narrative and recommended triage action. |
| "Check detection coverage" | Analyst selects a technique in the MITRE view | Retrieves mapped indicators and rules, identifies coverage gaps, and proposes hunt queries to close the gap. |
| "Draft case report" | Analyst invokes case AI on an open case | Generates a deterministic report grounded in the MITRE knowledge base and case timeline for sign-off. |


| Persona | Description and Platform Role |
|---|---|
| SOC Analyst | Operational role responsible for day-to-day triage of alerts, indicators, and cases. Primary user of the operational dashboard, indicator library, alert queue, and AI Analyst. Needs: efficient triage, cross-domain context, dynamic score understanding, case documentation. |
| Senior Analyst | Leads investigations and owns the threat hunting function. Uses the hunt workbench, MITRE coverage, escalation review, and correlation analysis. Needs: hypothesis testing, gap closure, escalation decisions, case report sign-off. |
| Administrator | Owns platform configuration: users, roles, rules, feeds, and scheduler. Uses administration pages and the audit log. Needs: feed management, rule management, user administration, retention configuration, audit review. |
| CISO / Executive | Strategic owner of the national security posture. Primary consumer of the executive dashboard and threat visualisations. Needs: posture score, metric grids, severity distributions, response times, org and sector breakdowns, board-level reporting. |
| External Feed Operator | An external partner (e.g., Lebahnet) pushing intelligence into the platform via the authenticated push API. Needs: a stable, authenticated ingestion contract with validated response payloads. |


| Persona | Domain Access | Permission Level | Scope |
|---|---|---|---|
| SOC Analyst | Intelligence, Analysis, Alerting, Operations; Governance (view audit trail limited to own activity) | View/Edit (indicators, alerts, cases, hunts); View (rules, feeds, MITRE) | Assigned compartments and organisations |
| Senior Analyst | All domains | Edit (hunts, escalations, cases, correlations); Approve (case reports) | All compartments within classification limits |
| Administrator | All domains (configuration) | Administer (users, rules, feeds, retention, scheduler); View audit log | Tenant-wide |
| CISO / Executive | All domains (dashboard and reporting) | View all; Approve (case sign-off, escalations) | All organisations |
| External Feed Operator | Ingestion only (push API) | Ingest (authenticated API key) | Push channel only |


| Layer | Technology Choice | Rationale |
|---|---|---|
| Frontend | React 18 + TypeScript; Vite build tool; Tailwind CSS; D3.js for graph visualisation; Leaflet for map visualisation | Mature ecosystem with strong TypeScript support; D3 and Leaflet provide high-fidelity threat graph and geographic visualisations; Tailwind enforces a consistent design system |
| Backend | Node.js (Express) REST API with ES modules; PostgREST proxy for relational access patterns | Productive, well-understood runtime; the proxy provides flexible SQL-backed endpoints while the Express layer owns authentication and domain orchestration |
| Database | PostgreSQL with pg_trgm (fuzzy search) and pgcrypto extensions; Docker Compose for local development | ACID integrity for intelligence records; trigram indexes support indicator search; PostgREST maps the relational model to HTTP |
| AI / LLM | OpenAI-compatible endpoint (model.arasintegrasi.ai) with configurable model; RAG context assembly in-house | LLM provides language understanding and generation; all retrieval is performed by the platform’s own query layer — the model never has direct database access |
| Scheduler | node-cron in-process scheduler with scheduler_jobs ledger | Twelve idempotent pipelines with per-run status, duration, and error tracking; no external scheduler dependency in MVP |
| Authentication | JWT bearer tokens (bcrypt password hashing); role hierarchy with classification compartments | Stateless authentication with server-side role and classification enforcement |
| Deployment | Nginx reverse proxy; systemd service; production build served from the Express static layer; CI/CD tooling for deploy and verify | Standard, auditable deployment for government hosting environments |


| Domain | Feature Area | Included Capability |
|---|---|---|
| Ingestion | Feed Management | Feed registry; scheduled/manual/file ingestion; STIX 2.1; REST JSON; CSV; Logstash bridge; push API; feed health |
| Ingestion | Indicator Enrichment | Type validation; geo-enrichment; severity/TLP assignment; intra-batch and fingerprint dedup; provenance |
| Ingestion | CVE & KEV | NVD CVE library; CVSS v3/v4; CISA KEV tracking with due dates and ransomware flags; indicator-to-CVE links |
| Analysis | Indicator Library | Searchable repository across IP, domain, hashes, URL, email, CVE; detail views; filters; distributions |
| Analysis | Dynamic Threat Scoring | 0–100 composite score; five components; 30-day half-life decay; score history; score distribution analytics |
| Analysis | Correlation Engine | Six relationship types; five techniques; fingerprint dedup; alert and scoring integration |
| Analysis | MITRE ATT&CK | Technique/group/tactic library; auto-mapping; detection coverage; gap analysis and heatmap |
| Analysis | Threat Hunting | JSON DSL workbench; saved and scheduled hunts; results export; playbooks; MITRE gap map |
| Analysis | Threat Actors | National APT library; attribution pipeline; actor detail views |
| Analysis | NLP Classification | Auto-classification of indicators into actors, malware, campaigns |
| Operations | Detection Rules | Severity thresholds; indicator-type selection; MITRE technique binding; enable/disable; audit trail |
| Operations | Alert Lifecycle | open → acknowledged → investigating → resolved/false_positive; dedup with stale auto-close; escalation rules; escalation log |
| Operations | Case Management | Creation, assignment, P1–P4 priority, notes, artifacts, timeline; deterministic case AI reports |
| Operations | Dashboards | Operational dashboard; executive dashboard with 20+ KPIs; threat graph and map; visualisation workspace |
| Governance | Org Structure | Recursive org tree; classification levels; sector assignment; org-linked indicators and alerts |
| Governance | RBAC & Compartments | Role hierarchy; classification enforcement; compartment-based visibility; server-side enforcement |
| Governance | PDPA Compliance | PII detection (NRIC, email, phone, bank, card); redaction; PII access audit; retention enforcement |
| Governance | Audit & Admin | Immutable audit log; user administration; password policy; profiles; session timeout; brute-force mitigation |
| Platform | AI Analyst | RAG assistant; streaming chat; structured rendering; NL queries; case AI; NLP classification; rate limiting; injection defence |
| Platform | Scheduler | Twelve automated pipelines; run ledger; status dashboard; no overlapping runs |
| Platform | API & Docs | 147 endpoints across 23 modules; interactive API documentation; health endpoint |


| Feature Area | Phase 2 Capability |
|---|---|
| Dark Web Monitoring | Credential exposure and leaked data detection |
| Brand & Executive Monitoring | Impersonation, typosquatting, social media monitoring |
| SIEM Integration | Bidirectional integration with Splunk and Microsoft Sentinel |
| Ticketing Integration | Jira and ServiceNow remediation ticket sync |
| SOAR / Automation | Automated response playbooks and orchestration |
| SSO / MFA | SAML 2.0 and OIDC single sign-on; multi-factor authentication |
| Semantic Search | Vector-based semantic retrieval for AI Analyst context assembly |
| AI Hunt Generation | Natural-language hypothesis to hunt query translation |
| BYOK / HYOK | Customer-managed encryption keys for high-assurance deployments |
| Multi-Region HA | Active-active multi-region deployment for high availability |
| Regulatory Change Monitoring | Automated monitoring of PDPA and related regulatory updates |


| Relationship | Cardinality | Owning Domain | Cross-Domain Significance |
|---|---|---|---|
| Organisation → Indicator | n:m | Governance | Agency-level attribution of threat exposure; drives sector aggregates |
| Organisation → Alert / Case | 1:n | Governance | Agency context on operational activity |
| Feed → Indicator | 1:n | Ingestion | Core provenance link; enables cross-source scoring and feed health |
| Feed → Ingestion Job | 1:n | Ingestion | Run-level ledger of processed/skipped/errored counts |
| Indicator → Correlation | n:m | Analysis | Correlation density feeds dynamic scoring and alert evaluation |
| Indicator → MITRE Technique | n:m | Analysis | Drives detection coverage and gap analysis |
| Indicator → CVE | n:m | Analysis | Exposes vulnerable-adjacent intelligence; KEV-aware prioritisation |
| Indicator → Actor (APT) | n:m | Analysis | National attribution pipeline; attribution dashboards |
| Indicator → Organisation | n:m | Governance | Per-agency threat views and compartment filtering |
| Rule → Alert | 1:n | Operations | Every alert records its triggering rule |
| Alert → Case | n:1 | Operations | Cases aggregate related alerts for investigation |
| Alert → Escalation | 1:n | Operations | Escalation log records every severity/timeout-driven decision |
| User → Alert / Case | 1:n | Governance | Assignment and escalation ownership tracking |
| Audit Event → Entity | polymorphic | Governance | Immutable record of all mutations and sensitive views |


| Framework / Dataset | Coverage in MVP |
|---|---|
| MITRE ATT&CK | Full technique, tactic, and group catalogue; materialised detection coverage with gap analysis |
| NVD / CVE | CVE records with CVSS v3/v4; synchronised from NVD |
| CISA KEV | Known exploited vulnerabilities with due dates and ransomware flags |
| STIX / TAXII | STIX 2.1 object storage; bundle ingestion; ECS bridge for Logstash |
| PDPA 2010 | Malaysian personal identifiers: NRIC, email, phone, bank account, credit card |
| Classification | Rahsia, Sensitif, Terhad, Pertidahan, Awam levels with compartment access |


| Term | Definition as Used in This Document |
|---|---|
| APT | Advanced Persistent Threat — a sophisticated adversary, often state-sponsored; tracked in the national APT library |
| ASN | Autonomous System Number — used in the shared-ASN correlation technique |
| CVE | Common Vulnerabilities and Exposures — a public identifier for a known vulnerability |
| CVSS | Common Vulnerability Scoring System — v3/v4 scoring stored per CVE |
| Dynamic Score | The 0–100 composite threat score computed for each indicator |
| Feed | A configured source of intelligence consumed by the ingestion pipeline |
| KEV | CISA Known Exploited Vulnerabilities catalogue — vulnerabilities confirmed exploited in the wild |
| Indicator (IOC) | An observable such as an IP, domain, hash, URL, email, or CVE used as a compromise signal |
| MITRE ATT&CK | A globally accessible knowledge base of adversary tactics and techniques |
| PDPA | Malaysia’s Personal Data Protection Act 2010 — basis of the compliance engine |
| RAG | Retrieval-Augmented Generation — the architecture grounding AI Analyst responses in platform data |
| RBAC | Role-Based Access Control — access model enforced across routes, pages, and navigation |
| STIX/TAXII | Structured Threat Information Expression and Trusted Automated Exchange of Intelligence Information |
| TLP | Traffic Light Protocol — red/amber/green/white information-sharing markings |
| Workbench | The unified analyst workspace and AI Analyst interface in GovSec3.0 |
