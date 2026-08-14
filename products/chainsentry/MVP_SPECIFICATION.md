---
id: DOC-20260814-001
record_type: document
title: "ChainSentry MVP Product Specification v3.0"
product: chainsentry
initiative: INIT-20260811-001
category: mvp-specification
version: "3.0"
date: 2026-08-14
source_type: docx-upload
source_authority: DAF
sensitivity: confidential
status: canonical
tags:
  - domain/cybersecurity
  - domain/blockchain-forensics
  - domain/cybersecurity-productisation
  - product/chainsentry
  - workstream/cybersec-products
  - portfolio/flagship
---

# ChainSentry MVP Product Specification v3.0

> Canonical baseline document - uploaded by DAF, 14 August 2026
>
> Blockchain Forensics & Investigative Intelligence Workbench
> CONFIDENTIAL - FOR EXECUTIVE AND ENGINEERING REVIEW








Chain:SENTRY
Blockchain Forensics & Investigative Intelligence Workbench
MVP Product Specification

CONFIDENTIAL — FOR EXECUTIVE AND ENGINEERING REVIEW
Version 3.0  |  August 2026



















Executive Summary
Blockchain investigations are often fragmented across chain explorers, sanctions lists, attribution services, infrastructure tools, case files, screenshots, and manually assembled reports. The result is slow triage, inconsistent evidence handling, and findings that are difficult to explain or reproduce.
ChainSentry is a production-verified blockchain-forensics workbench for commercial-crime and cyber investigators. It consolidates address risk scoring, layered sanctions screening, entity attribution, case intake and evidence processing, transaction graphs, fund-flow tracing, infrastructure intelligence, ransomware context, monitoring, case-quality scoring, and cited dossier composition in one controlled environment.



# 1. Platform Architecture & Intelligence Data Model
## 1.1 Architectural Philosophy
ChainSentry is organised around a single investigative spine: intake, triage, expansion, fund-flow following, monitoring, and reporting. Security and evidence controls are not separate reporting overlays; they are embedded in every operation that returns or changes investigative data.
The platform favours deterministic, visible behavior. The risk engine performs no external calls, source aggregation follows an explicit priority order, and source outages degrade enrichment rather than fail the application. Core attribution and sanctions holdings remain inside the deployment so essential capability is not dependent on per-query commercial availability.


## 1.2 Core Entity Model
The repository describes a shared operational model centred on the following entities and holdings:

1.3 Entity Relationships
Organisation → User / Case / Alert (1:n): tenant-scoped ownership and access boundary.
Case → Subject / Evidence / Note / Graph (1:n): all investigative material remains attached to a numbered case.
Address → Attribution Tag (1:n): an address may carry multiple labels with confidence, source pack, and modification time.
Address → Sanctions Record (0:n): layered authorities may independently match the same subject.
Address → Risk Assessment (1:n): assessments preserve factor evidence, raw score, overrides, final score, and action band.
Case → Scorecard (1:n): case completeness is evaluated against a fixed eight-dimension rubric.
Address → Alert Rule → Alert Event (1:n → 1:n): active rules are evaluated on a fifteen-minute schedule.
Privileged Action → Audit Record (1:1): sensitive operations carry justification, legal case reference, user attribution, and correlation identifier.

## 1.4 Capability Boundary Map

## 1.5 Data Flow Architecture
Lead → Intake: a complaint, referral, address, IP, or domain becomes a numbered case or direct assessment.
Evidence → Classification: uploaded text, PDF, Word, or image content is extracted, OCR-processed where needed, translated, and used for assisted classification.
Address → Triage: sanctions, attribution, security signals, counterparties, typology and footprint feed the explainable risk model.
Triage → Expansion: graph pivots, deep trace, infrastructure profiling and ransomware context widen the investigation.
Flow → Cash-out: outbound EVM-compatible transactions are followed until an exchange endpoint is identified.
Assessment → Report: case-quality gaps and cited dossier sections convert findings into a defensible output.

## 1.6 MVP Outcomes and Acceptance Measures
Faster triage: one subject can be screened, attributed and risk-scored without manually joining separate tools.
Defensible findings: every decisive risk factor or sanctions result names its supporting evidence and source category.
Operational continuity: failure of an external enrichment role does not remove the internal attribution, sanctions or case workflow.
Actionable investigation: fund flow can be expanded to an exchange endpoint and retained with the case.
Controlled output: a reviewer can identify missing work through the scorecard and issue a cited case report or dossier.

# 2. Domain Feature Sets
Each section below reflects the verified MVP feature set. Explicit limitations and future capability are separated into Sections 6 and 7.
## 2.1 Risk Quantification & Sanctions Screening
### 2.1.1 Explainable Composite Risk
Composite score: 0–100 result across six fixed weighted factors with a plain-language evidence statement for each.
Action bands: Critical 85–100; High 65–84; Elevated 45–64; Low 20–44; Minimal 0–19.
Overrides: direct sanctions match raises the result to Critical; the raw score remains visible beside the final score.
Tenant tuning: factor weights are configurable to reflect organisational risk appetite.
Supporting views: transaction and token-balance context appears alongside the score.


### 2.1.2 Layered Sanctions Screening
Local registry: consolidates OFAC, UN, EU, UK, Japanese and Israeli lists with community fraud feeds.
Priority order: local registry → live screening service → public on-chain sanctions authority → address-security check.
Explainable result: the reason string names the matching layer or authority.
Faceted browse: actor, category, jurisdiction, programme, designation date and additional attributes.

2.2 Attribution & Verified Entities
ChainSentry separates broad coverage from high-trust curation. The bulk attribution registry provides reach; the verified entity directory provides a smaller layer with documented verification method and date.
### 2.2.1 Attribution Registry
Coverage: 583,574 tags across 524,656 addresses on 78 chains.
Search: exact address lookup and free-text label/actor search.
Provenance: category, confidence, source pack, last-modified date, and a public-source link.
Chain distribution: led by Bitcoin (499,336 attributed addresses) and Ethereum (83,859).
Refresh: automated weekly ingestion of the attribution corpus.
### 2.2.2 Verified Entity Directory
Curated set: 57 addresses with high-trust verification notes.
Verification evidence: method, explanatory note, and verification timestamp.
Role: acts as a vetted layer above the bulk tag corpus.


## 2.3 Investigations & Evidence
### 2.3.1 Guided Case Intake
Five-step wizard: Mode → Describe → Subjects → Evidence → Review.
Create early: case number CT-YYYY-NNNN is issued after description so evidence attaches to a real record.
Evidence formats: native text, PDF, Word and images; OCR and translation support non-native content.
Assisted classification: proposes category, risk level, summary and case name, with a fallback when inference is unavailable.
Case lifecycle: close, reopen, duplicate, re-analyse after new evidence, and search by case number.

2.3.2 Case Detail & Evidence Discipline
Subjects: crypto addresses and supporting infrastructure leads remain attached to the case.
Evidence: uploaded artifacts retain case association and processed text.
Notes: analyst observations remain alongside source material.
Graph tab: renders the actual investigation network inline.
Re-analysis: updated evidence can trigger renewed classification and assessment.

## 2.4 Graph Exploration & Fund-Flow Tracing
### 2.4.1 Transaction Graph
Interactive network: counterparties are rendered as nodes and transaction relationships as edges.
Pivoting: related addresses rank by interaction count and are clickable for continued investigation.
Persistence: graphs save to investigations rather than browser-local storage.
Deep trace: multi-hop expansion adds depth beyond direct counterparties.

### 2.4.2 Off-Ramp Tracing
Objective: follow outbound flow until it reaches an exchange endpoint.
Investigative value: converts a crypto trail into a possible subpoena target.
Observed timing: approximately 32 seconds for a trace to cash-out in the recorded live baseline.
Boundary: current automated transaction tracing is EVM-compatible-chain focused.


2.5 Infrastructure, Ransomware & Threat Intelligence
### 2.5.1 Infrastructure Intelligence
Host profile: ports, services, vulnerabilities, hosting organisation and jurisdiction.
Domain pivoting: DNS resolution plus shared TLS-certificate and favicon relationships.
Tiered enrichment: a free bulk source provides breadth while a metered source provides depth.
Routing: global search recognises IP addresses and domains and directs them to the infrastructure surface.

### 2.5.2 Ransomware Intelligence
Group dossiers: victims, tactics, exploited vulnerabilities, tooling and associated crypto indicators.
Inline context: the dossier panel appears when an address is attributed to a known group.
Infrastructure links: ransomware records can be paired with network-infrastructure pivots.

### 2.5.3 Threat-Intelligence Feed
Aggregation: security and crypto-crime reporting is collected into a single feed.
Operational use: analysts use current reporting to inform triage and expansion.
Resilience: source health is monitored and degraded roles are surfaced.

## 2.6 Monitoring, Scorecards & Reporting
### 2.6.1 Monitoring & Alerts
Rule scope: monitoring rules are attached per address.
Evaluation: active rules run every fifteen minutes.
Delivery: webhook is included; email and messaging delivery are planned.
Auditability: alert retrieval and related actions remain tenant-scoped.
2.6.2 Case-Quality Scorecard
Cases are graded across eight dimensions totalling 100. The result is a grade plus an explicit list of what remains missing.

### 2.6.3 Reporting & Analyst Dossier
Closed-case report: renders a completed case into report form.
Analyst dossier: composes a fully cited assessment of a single address on demand.
Citation state: source, retrieval time and confidence are retained.
Integrity: dossiers carry a digest; formal cryptographic signing is future work.
Deferred sections: behavioral and off-chain sections explicitly state no-data/deferred status rather than implying a completed search.

## 2.7 Platform, Administration & Documentation Surfaces
The MVP includes supporting platform surfaces that make the investigative modules usable and operable. Their existence does not by itself prove production completeness: several administrative and API-facing screens describe intended behavior that must be reconciled with live routes before pilot exposure.

### 2.7.1 Verified MVP Route Inventory

Total verified MVP page routes: 26. The additive next-generation route tree is tracked separately and excluded from the MVP count.
## 2.8 Functional Acceptance Summary


# 3. Security, Accountability & Data Residency
## 3.1 Security Controls

## 3.2 Data Residency
Deployment boundary: intelligence, cases and uploaded evidence reside inside the deployment.
Inference choice: language inference may be self-hosted so case narrative and evidence do not leave the organisation.
Supplier resilience: external services enrich but do not own the core attribution or sanctions holdings.
Credential handling: credentials are supplied through the deployment environment and must be rotated before pilot access.
## 3.3 Access Roles


## 3.4 Intelligence Source Framework
ChainSentry treats source integration as an evidence pipeline, not a collection of interchangeable API calls. Each source fulfils a defined intelligence role, and the platform records whether that role is available, degraded, deferred or intentionally excluded. The current baseline verifies twelve of eighteen roles as operational; unresolved roles are carried into the gap register rather than silently presented as complete coverage.


## 3.5 Evidence and Provenance Controls
Acquisition state: each retrieved finding should carry source category, retrieval time, confidence and correlation identifier.
Original artifact: uploaded evidence remains associated with its case after extraction, OCR, translation or classification.
Analyst interpretation: notes and conclusions remain distinguishable from source facts and machine-generated suggestions.
Reproducibility: risk factors preserve their evidence statements, raw weighted result, applied override and final action band.
No-data semantics: unavailable, deferred and no-match are separate states; none may be rendered as a completed negative search.
Integrity state: dossiers retain a digest now; formal signing and verification are future evidence-grade controls.



# 4. User Personas & Core Workflows
## 4.1 Persona Definitions

## 4.2 Core Investigation Workflow
Intake: capture complaint/referral/lead, create the case, process evidence, and propose classification.
Triage: calculate explainable risk, screen sanctions/watchlists, and determine attribution.
Expand: investigate counterparties, deepen the trace, profile infrastructure, and retrieve ransomware context.
Follow: trace outbound EVM-compatible flows to exchange endpoints.
Monitor: create address rules and evaluate movement every fifteen minutes.
Report: grade case completeness, name gaps, and compose cited findings.
## 4.3 Role-Specific Workflows
Investigator — Daily Case Work
Open or create a case and attach subjects/evidence.
Run risk, sanctions and attribution checks.
Expand graph and trace outbound flow.
Add infrastructure or ransomware context.
Create monitoring rules where continuing activity matters.
Review scorecard gaps and generate the report/dossier.
Reviewer — Quality & Closure
Review the risk factor evidence and sanctions authority.
Confirm evidence and trace depth against the scorecard.
Update or close the case and issue a review report.

## 4.4 Assisted Analysis and Investigator Guardrails
ChainSentry uses assisted analysis to accelerate intake, evidence handling and dossier composition while keeping investigative accountability with the named user. Assistance is bounded by live source evidence, explicit fallback behavior and a clear separation between retrieved fact, model-generated narrative and analyst conclusion.

## 4.5 Governance Requirements
Residency: inference can be deployed inside the organisation so case narrative and evidence do not leave the controlled environment.
Minimum disclosure: only the information required for the requested task should be supplied to the inference endpoint.
Provenance: cited source material, timestamps and confidence remain attached to dossier content.
Accountability: model output is a suggestion; the named investigator or reviewer remains responsible for use and interpretation.
Failure transparency: unreachable inference, deferred sources and schema-validation failure must be visible rather than silently replaced with invented content.
Release control: any new assisted workflow must pass tenant-scope, auditability, data-boundary and fallback tests before pilot exposure.



## 4.6 Operational Workflow Acceptance
The workflows below define the minimum complete path for the MVP. They are product acceptance sequences, not merely interface tours: each ends with retained evidence, an attributable action and an outcome another authorised user can review.

## 4.7 Negative-Path Acceptance
Unauthenticated access: protected pages redirect to login and protected data paths return an unauthorised response.
Insufficient role: the operation fails without returning tenant data; privileged workbench access fails closed.
Cross-tenant request: no case, graph, alert, evidence or audit record from another organisation is returned.
Provider failure: the failed source is marked degraded, local results remain available, and the response cannot imply complete coverage.
Unsupported chain: the product identifies the tracing boundary and does not present EVM-only behavior as cross-chain completion.
Inference failure: intake remains usable through fallback behavior and generated narrative is not fabricated.



# 5. Technical Architecture & Operations
## 5.1 Deployment Stack

## 5.2 API & Application Behavior
Authentication gate: 19 protected page routes redirect unauthenticated users to login with callback.
API gate: protected data paths return unauthorised responses without a valid session.
Live verification: 32 of 32 authenticated GET paths returned HTTP 200 with real data.
Provider health: source availability and degradation are surfaced to investigators.
Caching: post-release migration widened supported cache kinds and restored trace cache writes.

### 5.2.1 Verified API Surface
The implementation contains 44 route handlers. The production verification exercised the authenticated GET surface and selected POST paths, while the implementation repository establishes the complete route inventory. Public regulatory-data and aggregate-statistics endpoints are intentionally distinguished from tenant-scoped investigative routes.

### 5.2.2 API Contract Boundaries
Authoritative routes: the implemented handlers above, not the illustrative /api/v1 address, transaction, entity and graph paths shown in the current in-product API-reference screen.
Authentication model: browser/session authentication is verified for operational routes; a complete production API-key authentication contract is not proven.
Rate limits: the in-product rate-limit tiers and headers are not backed by verified per-tenant enforcement and must be treated as demonstration documentation.
Response traceability: correlation identifiers support linking a response or denial to server-side audit/log evidence.
Error semantics: unauthenticated, forbidden, unsupported, degraded and no-data must remain distinct outcomes.


## 5.3 Automated Maintenance

All three jobs are additive and idempotent: re-running does not duplicate or remove records.

## 5.4 Gaps Requiring Resolution
This section reconciles two evidence sources that represent different states of ChainSentry. The implementation repository is the current development build and shows what exists in code. The verified production baseline records what was observed live on 11 August 2026, what remained undeployed, and what the backlog still requires. A feature is not treated as production-ready merely because it exists in the development branch.

### 5.4.1 Priority Gap Matrix

### 5.4.2 Resolution Sequence
Release reconciliation: freeze the pilot scope, map development commits to the verified deployment, and produce a controlled release manifest.
Safety before reachability: rotate exposed credentials before enabling external TLS access.
Truth boundary: remove or isolate every mock/demo path before partner users receive accounts.
Machine verification: make tests, typecheck and lint enforce the release rather than relying on manual audit sweeps.
Operational proof: re-run source health, scheduled-job freshness, tenant isolation, alert delivery and backup/restore checks.
Capability expansion: only after pilot readiness, address non-EVM tracing, bridges, PDF/signing and v2 evidence persistence.


## 5.5 Observed Performance

## 5.6 Scalability Notes
The product can run on a single Linux host on premises or in a private cloud. Multi-organisation separation is implemented but has not yet been exercised at scale; second-organisation verification is a productisation item before wider onboarding.

## 5.7 Release, Migration and Recovery Controls
A pilot release requires more than a successful application build. ChainSentry carries persistent cases, evidence, sanctions, attribution and audit state; therefore the deployment package, database change history, runtime configuration and rollback procedure must be treated as one controlled release unit.

## 5.8 Operational Ownership and Service Signals


# 6. MVP Scope Boundaries
## 6.1 In Production — Verified MVP

## 6.2 Explicit MVP Limitations


# 7. Pilot Readiness & Product Roadmap
## 7.1 Phase 1 — Pilot Readiness (Must Have)
Goal: make the verified capability safely reachable by named external users. Exit criterion: a partner-agency investigator can sign in over a secure connection with a named account, run a case from intake to report, and see live intelligence throughout.

## 7.2 Phase 2 — Productisation (Should Have)
Engineering foundations: CI, type enforcement, managed migrations, backup/restore, structured logging and monitoring.
Source operations: health alerting and governed credential storage/rotation.
Product completeness: email alerts, entity-name sanctions search, second-organisation verification, usage limits, PDF export, bulk screening, mixer threshold, explicit EVM-chain override.

## 7.3 Phase 3 — Capability Expansion (Future)

## 7.4 Parallel Workstreams



# 8. Appendix: Reference Data
## 8.1 Verified Baseline

## 8.2 Verification Results


## 8.3 Risk Scoring Reference

Direct sanctions match: floor at Critical. Final output retains the pre-override raw score and lists the override explicitly.

## 8.4 Core Relationship Reference

## 8.5 Operational Acceptance Reference


## 8.6 Glossary


## 8.7 Role-Permission Reference

Role permissions define what a user may do. Tenant guards independently define where the action may occur. Administrator and auditor privileges are intentionally non-hierarchical: the administrator changes configuration, while the auditor reads the audit trail.
## 8.8 Coverage and Authority Statement



# Document Version History

This document is a point-in-time baseline. Re-verify and re-issue after material deployment, source-availability, scope, or architecture changes.

| Strategic Differentiation
Explainable risk: a transparent six-factor weighted model with plain-language evidence and explicit override reporting.
Evidence discipline: source category, confidence, retrieval time, correlation identifiers, and auditability travel with findings.
Independent intelligence base: 583,574 attribution tags across 524,656 addresses and 4,633 sanctioned addresses are held internally.
Graceful degradation: external-source failure reduces enrichment depth without taking down the investigative workflow.
Investigator-centred output: the product is designed to produce a defensible assessment and actionable report, not merely a dashboard. |
|---|


| Design Decision: Deterministic Core, Resilient Enrichment
Risk scoring is repeatable for identical inputs.
The internal registry remains authoritative before external enrichment.
Every match names the authority or source category behind it.
Scheduled imports are additive and idempotent. |
|---|


| Entity | Description | Primary Use | Cross-Capability Consumers |
|---|---|---|---|
| Organisation | Tenant boundary for accounts and scoped data | Platform | All investigative surfaces |
| User / Role | Named account with one of five permission sets | Security | Cases, screening, audit, administration |
| Investigation / Case | Case number, narrative, subjects, status and report state | Investigations | Evidence, graph, scorecard, reports |
| Subject / Address | Address or infrastructure lead under assessment | Triage | Risk, sanctions, attribution, tracing, monitoring |
| Evidence | Uploaded file and extracted/OCR/translated content | Investigations | Classification, notes, case-quality review |
| Attribution Tag | Address label, actor, category, confidence and source | Attribution | Risk, lookup, dossier, graph |
| Sanctions Record | Listed address and authority attributes | Sanctions | Risk override, screening, dossier |
| Alert Rule / Event | Monitoring condition and resulting trigger | Monitoring | Dashboard, investigation follow-up |


| Domain | Owns | Consumes From |
|---|---|---|
| Triage & Screening | Risk factors, score bands, sanctions results | Internal registries, on-chain authority, address-security signals |
| Attribution | Bulk tags and curated verified entities | Weekly attribution corpus refresh, manual vetting |
| Investigations | Cases, subjects, evidence, notes and status | Extraction, OCR, translation, assisted classification |
| Tracing & Graph | Counterparties, edges, outbound cash-out path | EVM chain data, attribution and risk context |
| Infrastructure & Threat | IP/domain profile, ransomware dossier, news | Internet-infrastructure OSINT and threat feeds |
| Monitoring & Reporting | Alert rules/events, scorecards, reports, dossiers | Cases, risk, sanctions, attribution and trace output |


| Factor | Weight | What It Measures |
|---|---|---|
| Sanctions & watchlist exposure | 30% | Direct or one-hop presence on sanctions/watchlists |
| Entity & attribution risk | 20% | Known actor/category risk from the attribution corpus |
| Illicit-activity flags | 15% | Scam, theft, ransomware and related adverse signals |
| Counterparty exposure | 15% | Share of traced counterparties assessed as high risk |
| Behavioural / typology risk | 12% | Adverse behavioral patterns and freeze status |
| Financial materiality & footprint | 8% | Balance, chain spread and history length |


| Attribution Scope Boundary
Attribution and sanctions screening cover Bitcoin and other non-EVM chains.
Equivalent transaction tracing and alerting do not yet extend to those chains.
A tag or dark-web observation is not automatically a criminal designation; provenance and context must remain visible. |
|---|


| Tracing Deferrals
Automatic bridge-hop following is not included.
Non-EVM tracing, beginning with Bitcoin, is a future capability.
Advanced anonymised-network transport still requires provisioning. |
|---|


| Dimension | Weight | Purpose |
|---|---|---|
| Risk coverage | 15 | Confirms the subject has been risk-assessed |
| Sanctions reach | 15 | Confirms sanctions screening depth |
| Mixer and darknet flags | 15 | Checks adverse typology coverage |
| Documentation | 15 | Measures evidence and narrative completeness |
| Entity attribution | 10 | Confirms known ownership/category context |
| Trace depth | 10 | Measures transaction-network expansion |
| Exchange touch-point | 10 | Looks for actionable cash-out endpoint |
| Chain coverage | 10 | Assesses coverage of relevant networks |


| Surface | MVP Purpose | Current Boundary |
|---|---|---|
| Dashboard | Authenticated landing area with quick actions and a live recent-alert indicator. | Personal operational overview; no verified director/team dashboard. |
| Global search | Routes recognised addresses, case numbers, IP addresses and domains to the relevant investigative surface. | Universal transaction-hash and saved-search behavior is not part of the verified MVP. |
| Settings | Profile, notification, security and API-related controls plus intelligence-pipeline status. | Some controls are presentation-level or future-facing and require live-save verification. |
| API-key health | Shows masked key fingerprints, provider state, usage, failures and key-rotation statistics. | Restricted to authorised roles; previously exposed credentials must still be rotated. |
| Intelligence health/log | Surfaces provider reachability, degradation and supporting error state. | Health is visible in-product; operational paging is not yet implemented. |
| Documentation | API reference, examples, rate-limit guidance and demo-mode explanation. | Some pages contain aspirational or demonstration claims and are not the authoritative contract for the live API. |
| Next-generation experience | Dormant additive investigation-board prototype and re-skinned existing surfaces. | Not part of the MVP or pilot; no new backend contract is established by its presence. |


| Surface Group | Routes | Count / Access |
|---|---|---|
| Authentication | /login; /signup | 2 public |
| Core investigation | /dashboard; /benchmark; /lookup; /sanctions; /attribution; /entities | 6; dashboard and investigative surfaces are protected |
| Case, graph and output | /investigations; /investigations/new; /investigations/[id]; /visualizer; /reports; /scorecards; /alerts | 7 protected |
| Intelligence | /infrastructure; /news; /workbench | 3; news public, workbench administrator-only |
| Settings and documentation | /settings; /settings/api; /settings/api-keys; /settings/intel; /docs/api-reference; /docs/code-examples; /docs/rate-limits; /docs/demo-mode | 8; settings protected, documentation public in the verified baseline |


| Capability Group | Minimum MVP Acceptance |
|---|---|
| Triage | Returns a five-band risk assessment with six factor scores, evidence statements, consulted source categories, raw score and explicit overrides. |
| Screening | Returns a cited positive match or an explainable negative/degraded state without hiding which screening layer responded. |
| Attribution | Supports exact and free-text lookup with chain, category, confidence, provenance and recency where held. |
| Case work | Creates a numbered tenant-scoped case, retains subjects/evidence, supports re-analysis and preserves named-user actions. |
| Graph and trace | Persists investigation graphs, supports counterparty expansion and identifies the current EVM-only tracing boundary. |
| Monitoring | Evaluates active rules every fifteen minutes, baselines the first run, deduplicates by rule/transaction and records delivery outcome. |
| Reporting | Names case-quality gaps and produces a report or dossier whose populated claims retain citation state. |
| Administration | Enforces the central role matrix, masks credential material, and distinguishes operational data from demonstration content. |


| Control | MVP Implementation |
|---|---|
| Authentication | Session-based access; protected surfaces gated |
| Authorisation | Central role-permission matrix consulted by data-returning operations |
| Privileged workbench | Administrator-only; fails closed if role cannot be resolved |
| Sensitive searches | Active clearance, written justification and legal case reference required |
| Transport security | Strict content-security policy, HSTS, framing and content-type protections |
| Audit | Privileged actions recorded; administrators cannot edit their own audit trail |
| Traceability | Correlation identifier returned for matching activity to audit records |


| Role | Intended Holder | Access |
|---|---|---|
| Administrator | Platform owner | Full tenant access, privileged workbench, membership and configuration |
| Investigator | Daily analyst | Cases, lookups, screening, tracing, alerts, reports and exports |
| Reviewer | Supervising officer | Read all; update/close cases; issue review reports |
| Auditor | Compliance / oversight | Read-only across tenant including audit trail |
| Observer | Limited stakeholder | Read cases and graphs only |


| Source Role | MVP Contribution | Control Expectation |
|---|---|---|
| Internal attribution | Actor, entity and category labels across supported chains | Authoritative local lookup with source-pack and confidence metadata |
| Internal sanctions | Consolidated address records from multiple authorities | Daily additive refresh; authority named in every match |
| Live screening | Supplementary watchlist and address-risk checks | Fail independently; never replace the local deterministic result |
| On-chain authority | Public contract or registry confirmation | Return chain, authority and retrieval time |
| Blockchain data | Balances, transfers, counterparties and trace expansion | Chain-aware provider selection and explicit unsupported states |
| Infrastructure intelligence | Host, domain, TLS, DNS, service and vulnerability context | Metered-depth source layered over a free bulk source |
| Threat intelligence | Ransomware, adverse reporting and supporting indicators | Source health visible; stale or failed retrieval cannot appear current |
| Inference | Evidence classification, narrative support and dossier composition | Self-hostable; deterministic fallback for intake classification |


| Evidence Governance Rule
A result is operationally useful only when an investigator can state what was checked, when it was checked, what was returned, how confident the platform is, and which part is analyst judgement.
Source failure reduces enrichment depth but must not erase the local evidence base or misrepresent coverage. |
|---|


| Persona | Description and Platform Role |
|---|---|
| Platform Administrator | Owns deployment configuration, access, source health and privileged workbench use. |
| Investigator | Runs daily case intake, screening, attribution, tracing, monitoring and reporting. |
| Reviewer | Supervises case quality, updates or closes cases, and issues review reports. |
| Auditor | Reviews tenant activity and privileged audit records without mutating operational data. |
| Observer | Consumes case and graph information without investigative or administrative permissions. |


| Assisted Capability | MVP Behaviour | Human Control |
|---|---|---|
| Case classification | Proposes category, risk level, summary and case name from the submitted narrative and processed evidence. | Investigator reviews and may revise the proposal before relying on it. |
| Evidence processing | Extracts native text, applies OCR to images and supports translation for non-native material. | Original artifact remains attached; processed text is not a substitute for the source file. |
| Dossier composition | Assembles a cited single-address assessment from available intelligence roles. | Deferred and no-data sections remain explicit; the investigator owns the final conclusion. |
| Case-quality guidance | Uses an eight-dimension rubric to identify missing investigative work. | Score guides completion; it does not close or approve a case. |
| Inference outage | Falls back during assisted classification and preserves the core workflow. | The user can continue intake without treating an unavailable model as a negative finding. |


| Assistance Boundary
ChainSentry may draft, organise and explain; it does not make an autonomous criminal designation.
A platform score, attribution tag or dark-web observation must be reviewed in context before it becomes an investigative conclusion. |
|---|


| Workflow | Required Sequence | Completion Evidence |
|---|---|---|
| Address triage | Enter subject → screen sanctions → retrieve attribution → calculate composite risk → inspect factor evidence. | Assessment stores raw score, final band, any override, sources and retrieval state. |
| Case intake | Describe matter → create numbered case → add subjects → upload/process evidence → review proposed classification. | Case, original files, processed text and named-user actions remain tenant-scoped. |
| Fund-flow investigation | Open subject graph → rank counterparties → expand multi-hop trace → follow outbound value → identify exchange touch-point. | Saved graph and trace preserve the path, chain context and endpoint attribution. |
| Infrastructure pivot | Enter IP/domain → retrieve host/service context → resolve domain/TLS pivots → add relevant findings to case. | Finding identifies the source role, retrieval time and infrastructure relationship. |
| Monitoring | Create rule → wait for scheduled evaluation → trigger event → deliver webhook → review in tenant dashboard. | Rule, evaluation result, event, delivery result and user action are auditable. |
| Quality and report | Open case scorecard → resolve material gaps → close/review case → generate report or dossier. | Output reflects available evidence, names deferred sections and retains citation state. |


| Workflow Exit Rule
No pilot workflow is accepted solely because the interface renders. It must complete with live or correctly labelled data, retain the resulting state, enforce the assigned role, and produce evidence that can be reviewed after the session. |
|---|


| Layer | Technology / Requirement | Notes |
|---|---|---|
| Client | Investigator browser | TLS-terminated access |
| Application | Containerised investigative application | 26 page routes and 44 API handlers in the recorded baseline |
| Database | PostgreSQL with persistent volume | Attribution, sanctions, cases, users, alerts and audit data |
| Evidence storage | Persistent volume | Uploaded case-file evidence |
| Scheduling | Host-level scheduler | Daily sanctions, weekly attribution, 15-minute alerts |
| Chain access | Public blockchain node endpoint | Required for on-chain investigation |
| Inference | Reachable language-inference endpoint | May be self-hosted for residency |
| External enrichment | Outbound HTTPS to approved sources | Eighteen source roles; health surfaced in product |


| Route Group | Representative Paths | Access / State |
|---|---|---|
| Risk & intelligence | /api/risk/[address]; /api/intel/[address]; /api/intel/deep-trace; /api/intel/health; /api/intel/log; /api/intel/key-health | Session/permission gated except explicitly documented public data; live health and masked key state. |
| Sanctions | /api/sanctions/check; /api/sanctions/search; /api/sanctions/facets | Public by design for published regulatory data; entity-name search remains a gap. |
| Attribution & entities | /api/attribution; /api/attributes; /api/entities | Attribution/entity detail is protected; aggregate attribute counts may be public. |
| Investigations | /api/investigations; /[id]; /graph; /nodes; /nodes/bulk; /documents; /duplicate; /reanalyze; /resolve | Tenant-scoped and permission-gated; supports case, graph, evidence and enrichment lifecycle. |
| Alerts | /api/alerts; /api/alerts/[id]; /api/alerts/events | User/tenant scoped; active rules evaluated by scheduled job. |
| Infrastructure & ransomware | /api/infra/host/[ip]; /api/infra/domain/[domain]; /api/ransomware/lookup/[address]; /group/[slug] | Protected investigative enrichment; provider degradation remains visible. |
| Quality & tracing | /api/scorecards; /api/scorecards/[id]; /api/trace/offramp/[address] | Protected case-quality and EVM off-ramp functions. |
| Workbench | /api/v1/workbench/dossier; /api/mcp/tools; /api/mcp/call | Administrator-only; dossier registry is live, separate tool-call registry remains mock-backed. |
| Platform | /api/auth/[...nextauth]; /api/auth/register; /api/news; /api/news/refresh | Authentication plus public news read; refresh behavior requires appropriate control. |


| API Documentation Correction Required
Before external use, generate or publish an API contract from implemented routes and remove illustrative endpoints, bearer-key claims and rate-limit tiers that are not enforced by the verified MVP.
Until that correction is complete, the in-product API documentation is not a reliable external integration specification. |
|---|


| Job | Frequency | Purpose |
|---|---|---|
| Sanctions refresh | Daily | Merge newly listed addresses from upstream authorities |
| Attribution refresh | Weekly | Re-ingest the attribution corpus |
| Alert evaluation | Every 15 minutes | Evaluate active address-monitoring rules |


| Evidence Source | What It Establishes | Interpretation Rule |
|---|---|---|
| Implementation repository | Current application code, CI workflow, nine Vitest files, database/init scripts, next-generation experience, provider adapters and current branch history. | Use to determine whether a capability or control exists in the build. |
| Verified production baseline | Three live verification rounds, deployment status, supplier health, defects, pilot blockers, roadmap and 74-item internal backlog. | Use to determine whether the capability was deployed, verified and operationally ready. |


| Priority | Gap | Implementation Evidence | Verified Baseline | Required Resolution / Exit Evidence |
|---|---|---|---|---|
| Critical | Deployment parity | Development branch contains later fixes, CI/tests, v2 and label-aggregation work. | TEC-012 records a 22-commit / 32-day deployment gap and accumulated release risk. | Create a release manifest, deploy in a controlled window, apply migrations, and repeat the authenticated API/risk regression sweep. |
| Critical | External access and named identity | Application includes session authentication and role-aware routes. | BLK-002/003: service unreachable externally; named pilot accounts not issued; session URL requires correction. | Provision TLS termination, correct callback/session URL, issue per-person roles, and prove end-to-end login from the pilot network. |
| Critical | Credential closure and secret governance | Key-health gating/fingerprinting fix and CI secret scan exist in code. | BLK-001: four keys were previously exposed; rotation remains outstanding. TEC-009 calls for managed secret storage. | Rotate/revoke every exposed key, update providers, validate masked health output, and document an owner/cadence for rotation. |
| Critical | Live-versus-demo boundary | Repository contains a demo-mode page stating that all data is mocked; the build also has live provider-backed surfaces. | DEF-009 identifies a separate 31-tool registry that remains fixture-backed while the dossier registry is live. | Inventory every pilot route/tool, label or remove demo-only behavior, wire the mock registry to live providers or exclude it, and prove no pilot result is fixture data. |
| Must | API and documentation parity | In-product documentation shows illustrative /api/v1 routes, bearer-key authentication and rate-limit tiers that are not established by the implemented handler inventory. | The verified baseline proves session-gated operational routes and identifies per-tenant rate limiting as an outstanding item. | Generate a versioned contract from implemented routes, correct authentication and rate-limit claims, label demonstration content, and add contract tests for every externally supported endpoint. |
| Must | Integration and anonymised-network health | Provider adapters, health surfaces and SOCKS/Tor support exist in the build. | Six source roles were degraded; DEF-014 records unreachable Tor transport from the container. | Renew the live sanctions credential; disable superseded providers; re-point retired feeds; pass proxy variables through Compose; retest health and dossier coverage. |
| Must | Automated quality gates | CI runs typecheck/build, demo-marker discipline, dependency audit and secret scan; nine Vitest files exist. Lint is non-blocking and the workflow does not run tests. | TEC-001/002/005 record type debt, missing machine gates and missing risk-engine regression protection in the verified baseline. | Add npm test to CI, make lint/typecheck blocking, clear the accepted type baseline, add deterministic risk-model tests, and update the obsolete “no test suite” workflow comment. |
| Should | Schema migration and recovery | Schema changes are maintained under database/init; later cache migration code exists. | TEC-004/008: subsequent migrations were manual; backup/restore was not documented and tested. | Adopt a migration runner with version history; test backup and restore of cases, attribution, sanctions and audit data; record recovery evidence. |
| Should | Tenant isolation and quota control | Tenant-aware roles and organisation-scoped data paths exist; legacy backfill retains nullable tenant columns for one migration cycle. | Only one tenant was verified; SHD-004 and ENH-011 require second-tenant isolation testing and per-tenant rate limits. | Create two test tenants, run cross-tenant negative tests, promote required tenant columns to NOT NULL after code-path verification, enforce tenant quotas, and retain audit evidence. |
| Should | Investigator outputs and oversight surfaces | Reports, scorecards, bulk case-node ingestion and auditor permissions exist in the build. | ENH-007/008/015: no batch screening workflow, attachable PDF report export, or dedicated audit-log UI. | Deliver explicit batch screening, signed/hashed PDF export, and an auditor-facing immutable activity view with acceptance tests. |
| Should | Alerting and operational observability | Alert rules, scheduled evaluation and notification preference fields exist. | DEF-007: delivery is webhook-only. TEC-007/010/011 require provider alerts, structured logging and job-freshness monitoring. | Implement and test email delivery, hide unsupported channels, alert on provider/job staleness, and establish structured operational dashboards. |
| Future | Chain and trace completeness | Bitcoin validation, attribution and sanctions datasets exist; EVM tracing paths are implemented. | ENH-002/005/014: non-EVM tracing, bridge following and explicit EVM-chain override remain absent. | Add chain-specific trace providers beginning with Bitcoin, explicit chain selection, and controlled bridge-hop continuation with provenance. |
| Future | Evidence-grade assurance | Dossiers retain citations, confidence, timestamps and a SHA-256 integrity digest. | ENH-001: dossiers are not cryptographically signed; v2 pins are not yet persisted with full provenance. | Introduce signing/key custody, verification tooling, immutable pin persistence and complete source/confidence/retrieval-time capture. |


| Definition of “Addressed”
Implemented in the current ChainSentry build.
Deployed to the target environment with required migration/configuration changes.
Verified against live data with recorded results.
Covered by an automated regression check where practical.
Documented in the controlled ChainSentry baseline so the specification, roadmap and implementation no longer disagree. |
|---|


| Operation | Typical Response |
|---|---|
| Sanctions screening | Under 20 ms |
| Attribution lookup | Under 20 ms |
| Case and alert retrieval | Under 50 ms |
| Attribution free-text search | Approximately 240 ms |
| Infrastructure profiling | Under 1 s |
| Ransomware dossier | Approximately 1.4 s |
| Composite risk score | 1.4–1.5 s warm in the published external baseline |
| Assisted classification | Approximately 20 s |
| Fund-flow trace to cash-out | Approximately 32 s |


| Control Point | Required Control | Release Evidence |
|---|---|---|
| Build identity | Immutable application revision and dependency lockfile identify the shipped build. | Release manifest records revision, build result and artefact digest. |
| Configuration | Environment-specific values are separated from code and supplied through controlled secret/configuration channels. | Approved configuration inventory with masked validation output. |
| Schema | Every post-initialisation database change is versioned and repeatable. | Migration history shows ordered application and successful completion. |
| Data refresh | Sanctions and attribution jobs are idempotent and their freshness can be checked. | Job run, record counts, duration and last-success timestamp are retained. |
| Backup | Persistent database and evidence volumes are included in a documented backup set. | Timestamped backup completes without excluding case or audit state. |
| Restore | Recovery is tested into an isolated target, not assumed from backup success. | Restored cases, evidence, attribution, sanctions and audit samples are verified. |
| Rollback | Application and schema rollback boundaries are known before the release. | Go/no-go plan names decision owner, rollback trigger and recovery sequence. |
| Post-release | Authenticated route, risk-band and source-health checks run after deployment. | Recorded sweep confirms expected live responses and no critical regression. |


| Signal | Expected Owner / Response |
|---|---|
| External availability | Platform operations owns TLS endpoint, callback URL and access-path monitoring. |
| Authentication failure rate | Security/platform owner investigates abnormal failures and account issues. |
| Provider health | Intelligence-source owner renews, replaces or retires degraded roles. |
| Scheduled-job freshness | Data operations responds to missed sanctions, attribution or alert evaluations. |
| Error and correlation IDs | Engineering uses structured logs to connect a user-visible failure to server activity. |
| Storage and backup status | Operations monitors database/evidence capacity and backup completion. |
| Alert delivery failures | Platform operations retries or escalates failed webhook/email delivery. |
| Audit exceptions | Security or oversight reviews privileged activity and unexpected access patterns. |


| Domain | Feature Area | Included Capability |
|---|---|---|
| Triage | Risk Console | Six factors, 0–100 score, five bands, evidence strings, explicit overrides |
| Screening | Sanctions | Layered local/live/on-chain/security screening; faceted registry |
| Attribution | Registry | 524,656 addresses; 583,574 tags; 78 chains; free-text and exact search |
| Attribution | Verified Entities | 57 curated addresses with verification method/date |
| Cases | Investigations | Guided intake, numbering, evidence, OCR, translation, classification |
| Graph | Visualizer | Interactive counterparties, saved to investigation, multi-hop expansion |
| Tracing | Off-Ramp | Outbound EVM flow to exchange endpoints |
| Infrastructure | Host / Domain | Ports, services, CVEs, hosting, jurisdiction, certificate/co-host pivots |
| Threat | Ransomware | Group dossiers, victims, tactics, vulnerabilities, tooling and indicators |
| Quality | Scorecards | Eight-dimension case completeness rubric |
| Reporting | Reports / Dossier | Closed-case report and cited address assessment |
| Monitoring | Alerts | Per-address rules evaluated every fifteen minutes |
| Security | RBAC / Audit | Five roles, privileged clearance, correlation IDs and audit trail |


| MVP Scope Boundaries
Tracing and monitoring are EVM-compatible-chain focused; non-EVM chains retain attribution and sanctions coverage.
EVM address auto-detection defaults to Ethereum because address formats are shared.
Dossiers are digest-protected but not cryptographically signed.
Alert delivery is webhook-only; email and messaging delivery are planned.
Sanctions free-text search matches addresses; entity-name search is planned.
Cross-chain bridge activity requires manual continuation.
Enrichment is request-time or scheduled rather than streaming.
Multi-organisation separation still requires verification at scale.
The current content-security policy permits inline script execution; a nonce-based policy is deferred.
The in-product API reference, bearer-key guidance and rate-limit tiers are not verified as an implemented external API contract.
Some settings and demonstration screens contain aspirational or mocked behavior and must not be treated as live platform evidence. |
|---|


| Item | Status / Outcome |
|---|---|
| Security hardening and credential rotation | Hardening released; service credential rotation remains outstanding. |
| TLS-terminated external access | Gating item before external users can reach the platform. |
| Named role-appropriate accounts | Required so every action is attributable. |
| Advanced tracing | Restored and verified; anonymised-network transport still requires provisioning. |
| Dossier source coverage | Five of seven sections populate; two remain explicitly deferred. |
| Live intelligence confirmation | Every pilot surface must be confirmed non-demonstration data. |
| Degraded source disposition | Renew or retire sources and document reduced enrichment. |
| Controlled backlog deployment | Bring deployment current before the pilot rather than during it. |


| Capability | Value |
|---|---|
| Cryptographic dossier signing | Completes the step from integrity digest toward formal evidentiary use. |
| Bitcoin and non-EVM tracing | Closes the largest tracing gap against the existing attribution corpus. |
| Cross-chain bridge following | Closes a common route for evasion across networks. |
| Real-time streaming ingestion | Moves monitoring beyond the fifteen-minute evaluation cycle. |
| Messaging-channel alerts | Completes the notification matrix. |
| Case collaboration and assignment | Supports multi-investigator teams. |
| Saved searches and watchlists | Supports recurring monitoring programmes. |
| Self-service organisation onboarding | Enables scale beyond a small number of organisations. |


| Next-Generation Investigation Experience
Working prototype; not part of the pilot.
A case opens as a board; investigators pin findings with capture timestamps.
Pinned evidence is intended to assemble into a structured report.
Phase 2: confirm direction after pilot feedback, persist pins, and review access control.
Phase 3: support large cases, carry full provenance, and progressively adopt the interface. |
|---|


| Dark-Web Intelligence Source
Separate collector; not part of the pilot.
Verified contribution: 1,790 new addresses with source, context and first-seen date.
Corpus remediated to 100% checksum-verified addresses before integration.
Observations must be labelled as “observed on dark web,” not as criminal attribution.
Phase 2: graded-confidence ingestion, curation and scheduled refresh; Phase 3: live dossier lookup. |
|---|


| Measure | Recorded Baseline |
|---|---|
| Investigative surfaces | 26 |
| API route handlers | 44; all 32 reviewed GET paths returned live data |
| Attribution corpus | 583,574 tags across 524,656 addresses on 78 chains |
| Sanctions registry | 4,633 addresses |
| Verified entity directory | 57 addresses |
| Source health | 12 of 18 roles operational |
| Automated maintenance | Three scheduled jobs verified |
| Stability | No errors in the reviewed 2,000-log-line window |


| Check | Recorded Result |
|---|---|
| Page routing | 26 of 26 correct under unauthenticated probing |
| Authenticated API sweep | 32 of 32 GET paths returned HTTP 200 with real data |
| Risk discrimination | Exchange 16/Minimal; OFAC-listed 90/Critical; mixer router 65/High |
| Factor decomposition | Six-factor table with evidence strings and source categories |
| Sanctions controls | Listed address true with citation; clean address false |
| Workbench dossier | Citations, retrieval timestamps, confidence and schema-valid structure |
| Production build | Exit 0; routes compiled |
| Post-release regression | Authenticated sweep and risk bands unchanged |


| Factor | Weight |
|---|---|
| Sanctions and watchlist exposure | 30 |
| Entity and attribution risk | 20 |
| Illicit-activity flags | 15 |
| Counterparty exposure | 15 |
| Behavioural and typology risk | 12 |
| Financial materiality and footprint | 8 |


| Relationship | Cardinality | Operational Meaning |
|---|---|---|
| Organisation → User | 1:n | Named users and assigned roles exist inside one tenant boundary. |
| Organisation → Case | 1:n | Every case and its investigative material is tenant-owned. |
| Case → Subject | 1:n | One investigation may contain multiple addresses or infrastructure leads. |
| Case → Evidence | 1:n | Uploaded artifacts and processed content remain tied to the case. |
| Case → Note | 1:n | Analyst observations remain separate from source evidence. |
| Case → Graph | 1:n | Saved transaction networks can be reopened within the investigation. |
| Address → Attribution Tag | 1:n | One address may have several labels with independent provenance. |
| Address → Sanctions Record | 0:n | Multiple authorities may designate or reference the same address. |
| Address → Risk Assessment | 1:n | Repeated assessments preserve point-in-time evidence and overrides. |
| Address → Alert Rule | 1:n | A subject may be monitored under more than one condition. |
| Alert Rule → Alert Event | 1:n | Each evaluation can produce a separately auditable event. |
| Case → Scorecard | 1:n | Quality can be re-evaluated as evidence and trace depth increase. |
| Dossier → Citation | 1:n | Every populated dossier section may reference multiple sources. |
| Privileged Action → Audit Record | 1:1 | Sensitive actions retain user, justification, legal reference and correlation ID. |


| Area | Minimum Acceptance Evidence |
|---|---|
| Release | Approved manifest maps build commits, schema changes and configuration to the deployed version. |
| Identity | Named role-based accounts authenticate over TLS from the pilot network. |
| Secrets | Previously exposed credentials are revoked; replacements pass masked provider-health checks. |
| Live data | Every pilot surface is proven to return live or clearly labelled unavailable/deferred data. |
| Regression | Build, tests, typecheck, lint and deterministic risk cases pass as release gates. |
| Operations | Source health, scheduled-job freshness, alert delivery, backup and restore are evidenced. |
| Isolation | A two-tenant negative test proves that users cannot retrieve another tenant’s data. |
| Reporting | Generated output retains citations, timestamps, confidence and integrity state. |


| Term | Definition as Used in This Document |
|---|---|
| Attribution | Assignment of an address to an actor, entity or category with provenance and confidence. |
| Cash-out point | Exchange endpoint where crypto value may exit into fiat or another controlled account. |
| Correlation ID | Identifier used to match a response or action to the audit record. |
| EVM | Ethereum Virtual Machine-compatible blockchain environment. |
| MVP | Minimum Viable Product: the verified current production capability defined here. |
| OCR | Optical Character Recognition used to extract text from image evidence. |
| RBAC | Role-Based Access Control: permissions assigned by user role. |
| Risk override | Rule that raises a weighted result because a decisive condition applies. |
| Scorecard | Eight-dimension case-quality assessment that names missing work. |
| OSINT | Open-source intelligence used for infrastructure, threat and attribution enrichment. |
| Webhook | Machine-to-machine destination used for current alert delivery. |


| Capability | Administrator | Investigator | Reviewer | Auditor | Observer |
|---|---|---|---|---|---|
| Tenant settings | Read / update | Read | Read | Read | Read |
| Member management | Read / invite / remove / role | Read | Read | Read | — |
| Investigations | Create / read / update / delete / export | Create / read / update / export | Read / update / export | Read | Read |
| Graph | Read / update | Read / update | Read | Read | Read |
| Address / sanctions / entities | Read; label write; batch screen | Read; batch screen | Read | Read | Read |
| Alerts | Create / read / update / delete | Create / read / update | Read / update | Read | Read |
| Reports / evidence | Read / create / export | Read / create / export | Read / create / export | Read | Read |
| Audit log | — | — | — | Read | — |
| API-key state | Read / create / revoke | — | — | Read | — |
| Analyst dossier | Generate / read | — | — | — | — |


| Specification Layer | Covered Here | Authority |
|---|---|---|
| Product / MVP | Purpose, verified features, users, workflows, boundaries, pilot gates and roadmap. | This document. |
| Functional behavior | Capability behavior and acceptance summaries for all verified MVP surfaces. | This document plus implemented route/surface behavior. |
| Technical platform | Stack, runtime topology, route groups, data relationships, providers, jobs, security and operations. | This document plus implementation source. |
| Detailed integration contract | Every request/response schema, status code, pagination rule and versioned public API. | Not yet an implemented authoritative contract; must be generated and verified. |
| Physical data dictionary | Every table, column, constraint, index, retention rule and migration state. | Database migrations; summarised, not duplicated exhaustively here. |
| Operations runbook | Step-by-step production commands, owners, escalation contacts, RTO/RPO and supplier procedures. | Requires a controlled environment-specific runbook. |
| User manual | Screen-by-screen instructions and troubleshooting for each role. | Separate user guide; not the purpose of an MVP product specification. |


| Completeness Statement
This is the comprehensive ChainSentry MVP platform and product specification for the supplied implementation and verified baseline.
It intentionally does not pretend to be an exhaustive OpenAPI definition, physical database dictionary, environment-specific operating manual or screen-by-screen user guide.
Where an interface or documentation page is aspirational, mocked or inconsistent with the implemented route set, the gap is stated explicitly rather than promoted to verified capability. |
|---|


| Version | Date | Notes |
|---|---|---|
| 3.1 | August 2026 | Coverage-verified ChainSentry specification. Added platform/admin surfaces, implemented API inventory and contract boundaries, functional acceptance, exact role-permission reference, and a formal coverage statement. |
| 3.0 | August 2026 | Comprehensive single-name ChainSentry specification. Rebuilt directly from the uploaded reference template, with implementation evidence, verified-production evidence, gaps, scope and roadmap clearly separated. |
| 2.1 | August 2026 | Introduced a structured implementation-to-production gap analysis. |
| 2.0 | August 2026 | Initial expanded ChainSentry MVP product specification based on the verified production baseline. |
