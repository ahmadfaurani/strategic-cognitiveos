---
id: STRAT-20260807-001
record_type: strategy
title: "R.I.S.I.K Operational Development Plan — From Doctrine to Operations"
created_at: 2026-08-07T08:30:00Z
updated_at: 2026-08-07T08:30:00Z
owner: faurani-jaafar
authority: DAF
sensitivity: confidential
classification: OSA-1972-aware
status: draft
parent_initiative: INIT-20260803-002
parent_workstream: INIT-20260725-004
tags:
  - domain/information-warfare
  - domain/artificial-intelligence
  - domain/political-intelligence
  - domain/narrative-intelligence
  - domain/sentiment-analysis
  - domain/influence-operations
  - domain/counter-narrative
  - domain/national-security
  - domain/strategic-communications
  - organisation/aras-integrasi
  - organisation/uitm
  - organisation/pmo
  - mission/political-intelligence
  - readiness/development
---

# R.I.S.I.K Operational Development Plan

## From Doctrine to Operations

**Authority:** DAF
**Date:** 7 August 2026
**Classification:** Confidential — OSA 1972 Aware
**Parent Initiative:** INIT-20260803-002 — UITM-Aras Strategic Collaboration on AI Enablement of the R.I.S.I.K Framework
**Parent Workstream:** INIT-20260725-004 — Workstream D: Political & Strategic Intelligence

---

## 1. Purpose

This document converts the R.I.S.I.K Framework doctrine (23 sections, 4 layers, 5 components) into a concrete operational development plan. It maps existing Aras Integrasi infrastructure to each framework layer, identifies gaps, assigns responsibilities between Aras and UiTM, and defines a build roadmap.

**This plan serves as the primary input document for the first working session with UiTM's Centre for Media and Information Warfare Studies.**

**Strategic positioning:** UiTM receives this as "here is what Aras is building, here is where your research and Malaysian context expertise plugs in" — not "let's meet and discuss collaboration."

---

## 2. Current Maturity Assessment

**Overall: Level 1 — Reactive (approaching Level 2 — Structured)**

Per the R.I.S.I.K Maturity Model (Section 21):

| Level | Description | Status |
|-------|-------------|--------|
| Level 1 — Reactive | Ad hoc monitoring and communication | ✅ Current |
| Level 2 — Structured | Defined issue registers and reporting | ⚠️ Partial |
| Level 3 — Integrated | R/I/S/I/K linked in one workflow | ❌ Not started |
| Level 4 — Intelligence-Led | Predictive indicators, cross-agency, measurable | ❌ Not started |
| Level 5 — Adaptive | AI-enabled, continuous learning, simulation, institutionalised | ❌ Target (24-month) |

**Doctrine completeness:** 100% — all 23 sections documented.
**Operational completeness:** ~20% — doctrine exists, pipelines don't.

---

## 3. Infrastructure Audit — What We Have

### 3.1 Aras Integrasi / Ember Stack

| Asset | Capability | Framework Layer | Status |
|-------|-----------|----------------|--------|
| vLLM endpoint (model.arasintegrasi.ai) | 5 models: GLM-5.2 (primary), Qwen3.5-397B, Qwen3.5-27B, Kimi-K2.5, Kimi-K2.6 | All layers — AI engine | ✅ Live (auth-gated) |
| DeerFlow collection engine | 25-32 source political news collection, Crawl4AI + Firecrawl fallback | Layer 1 — Collection | ✅ Built, not operationalised on schedule |
| Unified scraper (Crawl4AI) | 100% success rate on 25 sources, anti-bot stealth, 3-8s per source | Layer 1 — Collection | ✅ Built, tested |
| PIR definitions (10+1 PIRs) | Priority Intelligence Requirements with keywords, entities, thresholds | Layer 2 — Analysis | ✅ Defined |
| PIR entity tagger skill | Automated PIR classification of collected signals | Layer 2 — Analysis | ✅ Built, not operationalised |
| Signal quality grader skill | Loop 2 verification of signal quality | Layer 2 — Analysis | ✅ Built, not operationalised |
| Threshold escalation checker | Automated alert triggers for ESC-001 to ESC-006 | Layer 2 → Layer 3 | ✅ Built, not operationalised |
| Signal Registry | JSONL-based signal storage with timestamps | Layer 1 → Layer 2 | ⚠️ Minimal data (3 files, June 2026 only) |
| CVS Truth Validator | 6-tier claim verification, source cross-referencing, election data API | Layer 2 — Analysis (Reality) | ✅ Built, integrated |
| Mr.Holmes OSINT | Username, phone, domain, email OSINT — 100+ platforms | Layer 1 — Collection | ✅ Installed, configured |
| Daily brief generator skill | Structured brief generation from signals | Layer 3 → Layer 4 | ✅ Built, not operationalised |
| CognitiveOS governance | 237 records, 8 types, 12 indexes, 11 templates, 9 schemas | Layer 3 — Decision | ✅ Active |
| OpenClaw / Ember | AI agent runtime, Telegram delivery, memory system, heartbeat | Layer 4 — Engagement | ✅ Active |
| GitHub repo (strategic-cognitiveos) | Version-controlled knowledge base, 840 files | All layers — Infrastructure | ✅ Active |
| 7 cron jobs (CJ-1 through CJ-7) | Automated scheduling | Infrastructure | ✅ Configured |

### 3.2 What Does NOT Exist

| Missing Capability | Framework Requirement | Impact |
|--------------------|----------------------|--------|
| Source reliability grading (A-F) | Section 5.4, Step 2 — every source must be graded | Cannot assess confidence of claims |
| Structured claim register | Section 5.4, Step 1 — every material claim recorded | Cannot track verification status |
| Issue scoring engine | Section 6.4 — 10-dimension weighted scoring | Cannot priorititise issues systematically |
| Issue lifecycle tracking | Section 6.3 — LATENT→EMERGING→...→DORMANT | Cannot assess issue trajectory |
| Sentiment analysis pipeline | Section 7 — emotion, trust, behavioural intent | Core R.I.S.I.K function unbuilt |
| Audience segmentation engine | Section 7.3 — geography, age, language, community | Cannot target interventions |
| Influence network mapping | Section 8 — actor discovery, relationship mapping, network roles | Core R.I.S.I.K function unbuilt |
| Actor registry | Section 13.3 — structured actor records | No persistent influence tracking |
| Narrative detection / clustering | Section 8 + Section 14 — narrative similarity, trend detection | Cannot identify emerging narratives |
| Kontra Narrative content pipeline | Section 9 — message design, approval, deployment | No intervention capability |
| Operational dashboard | Section 15 — strategic, operational, measurement views | No command visibility |
| Escalation trigger engine (live) | Section 16 — threshold-based automated escalation | Triggers defined but not wired |
| Post-intervention review process | Section 20 — structured after-action review | No measurement loop |
| Daily R.I.S.I.K Brief (operational) | Section 19 — standard daily product | Generator exists, never run on schedule |
| Role-based access control | Section 3.7 — secure execution | Single-user system |
| Audit logging | Section 3.7 — secure execution | Git commits only |
| AI pipelines (16 functions) | Section 14.1 — entity extraction, sentiment, emotion, network analysis, narrative similarity, trend detection, scenario simulation | Zero of 16 built |

---

## 4. Gap Analysis by Framework Layer

### Layer 1 — Collection and Observation

**Framework requirement:** Multi-source collection with source diversity, reliability grading, and structured claim capture.

**What exists:**
- DeerFlow: 25-32 news sources, Crawl4AI unified scraper, 100% success rate
- Mr.Holmes: OSINT for usernames, phones, domains
- PIR definitions: 10 PIRs with keywords, entities, thresholds
- Signal Registry: JSONL storage (minimal data — 3 files from June 2026)

**What's missing:**
1. Source reliability grading system (A-F per Section 5.4)
2. Structured claim register (per Section 5.4, Step 1)
3. Field/community collection channels (beyond digital news)
4. Social media collection (publicly accessible only)
5. Continuous collection schedule (daily collection exists as skill, never operationalised)
6. Deduplication and cross-source correlation

**Build effort:** Medium. DeerFlow + Crawl4AI handles the hard part (scraping). Grading, claim registration, and scheduling are engineering work, not research.

### Layer 2 — Intelligence and Analysis

**Framework requirement:** Convert collected information into structured assessments — verification, entity extraction, issue classification, sentiment analysis, narrative detection, influence mapping, risk scoring, scenario development.

**What exists:**
- PIR entity tagger (classifies signals by PIR code)
- Signal quality grader (Loop 2 verification)
- CVS Truth Validator (6-tier claim verification with election data API)
- vLLM endpoint with 5 models (compute available)
- Entity extraction scripts (multiple versions in DeerFlow)

**What's missing:**
1. Sentiment classification pipeline (polarity, emotion, trust, behavioural intent)
2. Emotion analysis (anger, fear, anxiety, hope, pride, frustration)
3. Issue scoring engine (10-dimension weighted model per Section 6.4)
4. Issue lifecycle tracker (LATENT→EMERGING→...→DORMANT)
5. Influence network mapping (actor discovery, relationship mapping, network roles)
6. Actor registry (persistent structured records)
7. Narrative detection and clustering (narrative similarity, trend detection)
8. Baseline comparison engine (historical norms, seasonal patterns)
9. Confidence assessment automation (per Section 5.4, Step 4)
10. Integrated Assessment Brief (IAB) generator

**Build effort:** High. This is the core analytical layer. Most functions require AI pipelines (prompt engineering or fine-tuning) against the vLLM endpoint. The compute exists; the pipelines don't.

### Layer 3 — Decision and Governance

**Framework requirement:** Issue prioritisation, legal review, policy alignment, intervention selection, messenger approval, escalation management, senior-authority approval.

**What exists:**
- CognitiveOS governance: DEC, ACT, COM records with structured workflow
- Approval workflow documented in operational process
- Escalation triggers defined (ESC-001 to ESC-006)
- Authorisation levels defined (Routine → Critical)

**What's missing:**
1. Operational dashboard (strategic, operational, measurement views)
2. Automated escalation trigger wiring (triggers defined, not connected)
3. Live approval system (currently manual via CognitiveOS records)
4. Legal/ethical review checklist (defined in doctrine, not operationalised as tool)
5. Decision-authority delegation tracker
6. Cross-agency coordination protocol

**Build effort:** Medium. CognitiveOS provides the governance backbone. Dashboard and trigger wiring are engineering tasks. Legal review checklist is a template + process.

### Layer 4 — Engagement and Measurement

**Framework requirement:** Message preparation, stakeholder engagement, media response, public clarification, community outreach, digital communication, performance monitoring, post-intervention review.

**What exists:**
- Telegram delivery (via OpenClaw/Ember)
- Daily brief generator skill (built, not operationalised)
- Memory system for archival and retrieval

**What's missing:**
1. Channel management (multi-platform deployment coordination)
2. Messenger briefing system
3. Content preparation pipeline (format-matched to channel)
4. Measurement framework (reach, engagement, sentiment shift, narrative penetration, behavioural change)
5. Post-intervention review process (11-point checklist per Section 20)
6. Stakeholder engagement matrix
7. Adaptation trigger engine (backlash detection, amplification risk)

**Build effort:** Medium-High. Delivery exists (Telegram). Measurement requires pre/post sentiment comparison capability (depends on Layer 2 sentiment pipeline). Post-intervention review is a template + process.

---

## 5. AI Enablement Build Plan (Section 14)

The framework lists 16 AI functions. Here is the build sequence:

### Phase A — Foundation AI (Weeks 1-4)

| # | AI Function | Input | Output | Engine | Priority |
|---|-----------|-------|--------|--------|----------|
| 1 | Entity extraction | Raw collected text | Structured entities (actors, orgs, locations, dates, numbers) | vLLM (GLM-5.2) | P0 — blocking |
| 2 | Event detection | Entity-tagged signals | Event records with timestamp, location, actors | vLLM + PIR tagger | P0 |
| 3 | Claim extraction & clustering | Raw text | Structured claims with source attribution | vLLM + CVS | P0 |
| 4 | Duplicate detection | Signal registry | Deduplicated signal set | Embedding similarity | P1 |
| 5 | Topic modelling | Collected corpus | Topic clusters | vLLM + clustering | P1 |
| 6 | Summarisation | Daily signal corpus | Executive summary | vLLM (GLM-5.2) | P1 |

### Phase B — Analytical AI (Weeks 5-10)

| # | AI Function | Input | Output | Engine | Priority |
|---|-----------|-------|--------|--------|----------|
| 7 | Sentiment classification | Text by segment | Polarity, intensity, emotion tags | vLLM (Qwen3.5-397B) | P0 — core R.I.S.I.K |
| 8 | Emotion analysis | Text by segment | Emotion labels (anger, fear, hope, etc.) | vLLM (Qwen3.5-397B) | P0 — core R.I.S.I.K |
| 9 | Narrative similarity | Narrative database | Similar narrative clusters | Embedding + cosine similarity | P1 |
| 10 | Network analysis | Actor relationships | Influence network map | Graph algorithms | P1 — core R.I.S.I.K |
| 11 | Trend detection | Time-series signal data | Trend indicators, velocity, acceleration | Statistical + LLM | P1 |
| 12 | Alert generation | Threshold breaches | Structured alert with context | Rule engine + LLM | P1 |

### Phase C — Advanced AI (Weeks 11-16)

| # | AI Function | Input | Output | Engine | Priority |
|---|-----------|-------|--------|--------|----------|
| 13 | Report drafting | Structured analysis | Draft IAB / daily brief | vLLM (GLM-5.2) | P2 |
| 14 | Evidence retrieval | Claim queries | Supporting evidence from corpus | RAG + vLLM | P2 |
| 15 | Scenario simulation | Issue parameters | Scenario projections | vLLM (multi-shot) | P2 |
| 16 | Translation | BM ↔ English texts | Translated documents | vLLM (GLM-5.2) | P2 |

### AI Control Requirements (Per Section 14.2)

Every AI-generated output must include:
- Source references
- Confidence level
- Timestamp
- Model version
- Analyst review status
- Known limitations
- Human approval status

### Human-in-the-Loop Gates (Per Section 14.3)

Human review is **mandatory** before:
- Public attribution
- Issue escalation
- Sensitive actor classification
- Public communication
- High-impact intervention
- Cross-agency dissemination
- External stakeholder targeting

---

## 6. Aras vs UiTM Responsibility Assignment

### 6.1 Principle

**Aras builds the machine. UiTM validates the intelligence.**

Aras Integrasi provides the AI technology, data engineering, infrastructure, and pipeline construction. UiTM provides academic validation, Malaysian socio-cultural context, research methodology, and domain expertise in media and information warfare.

Neither side works in isolation — but the build responsibility is Aras, the validation responsibility is UiTM.

### 6.2 Responsibility Matrix

| Workstream | Primary | Support | Deliverable |
|-----------|---------|--------|------------|
| **Collection infrastructure** | Aras | — | DeerFlow + Crawl4AI operational on daily schedule, 32 sources, source grading system |
| **Claim register & verification** | Aras | UiTM (methodology) | Structured claim register with A-F source grading, CVS integration |
| **PIR taxonomy refinement** | UiTM | Aras | Refined PIR set for Malaysian information warfare context (current PIRs are election-focused) |
| **Sentiment analysis pipeline** | Aras (build) | UiTM (validate) | BM/English sentiment classifier with emotion, trust, behavioural intent dimensions |
| **Malaysian context models** | UiTM | Aras | Dataset of Malaysian media, behavioural, socio-cultural patterns for model fine-tuning |
| **Influence mapping** | Aras (build) | UiTM (validate) | Actor registry, relationship mapping, network role classification |
| **Narrative detection** | Aras (build) | UiTM (validate) | Narrative clustering, similarity detection, trend tracking |
| **Issue scoring engine** | Aras | UiTM (calibrate) | 10-dimension weighted scoring with Malaysian context calibration |
| **Kontra Narrative content pipeline** | UiTM (design) | Aras (build) | Message design model, content templates, approval workflow |
| **Operational dashboard** | Aras | — | Strategic, operational, measurement views |
| **Governance & compliance** | UiTM (legal) | Aras (implement) | OSA 1972 classification protocols, ethical review, human-authority gates |
| **Daily R.I.S.I.K Brief** | Aras (automate) | UiTM (review) | Operational daily brief generated from signal registry |
| **Controlled simulations** | UiTM (design) | Aras (execute) | Simulation scenarios to validate framework end-to-end |
| **Proof of Concept** | Joint | Joint | PoC demonstrating operational relevance |
| **Academic validation** | UiTM | — | Research methodology, peer review, publication pathway |
| **Capability-building** | Joint | Joint | Training programmes, knowledge transfer |

### 6.3 Aras-Only Workstreams

These require no UiTM involvement:
- vLLM pipeline engineering (prompt templates, API calls, model routing)
- DeerFlow collection scheduling and operationalisation
- Signal Registry infrastructure
- Dashboard front-end
- Git/version control, deployment, DevOps
- OpenClaw/Ember integration

### 6.4 UiTM-Only Workstreams

These require Aras support but Aras cannot do them alone:
- Malaysian socio-cultural dataset curation
- PIR taxonomy adaptation for Malaysian information warfare
- Academic validation of analytical outputs
- Legal/ethical framework for OSA 1972 compliance
- Research methodology for controlled simulations
- Publication and academic output

---

## 7. Development Roadmap

### Phase 0 — Pre-Working Session (Aras, 7-25 August 2026)

**Goal:** Bring concrete infrastructure to the table, not just concepts.

| Task | Owner | Deliverable | Deadline |
|------|-------|------------|----------|
| Operationalise DeerFlow daily collection | Aras | Daily collection running at 23:00 UTC, signals written to registry | 15 Aug |
| Build source reliability grading system | Aras | A-F grading applied to all 32 sources, stored in signal metadata | 17 Aug |
| Build structured claim register | Aras | JSONL-based claim register with claim ID, source, confidence, verification status | 17 Aug |
| Wire PIR entity tagger to collection output | Aras | Every collected signal auto-tagged with PIR code | 15 Aug |
| Wire threshold escalation checker | Aras | Automated alerts on threshold breach (Telegram delivery) | 17 Aug |
| Operationalise daily brief generator | Aras | Daily R.I.S.I.K Brief generated and delivered via Telegram | 20 Aug |
| Draft working session agenda (ACT-20260807-002) | Aras | Structured agenda with this plan as primary input | 24 Aug |
| Prepare Aras infrastructure demo | Aras | Live demo: collection → PIR tagging → claim register → daily brief | 24 Aug |

### Phase 1 — Foundation (Weeks 1-4 of collaboration, ~Sep 2026)

**Goal:** Layer 1 fully operational, Layer 2 foundation laid.

| Task | Owner | Deliverable | Week |
|------|-------|------------|------|
| Daily collection operational on schedule | Aras | 32 sources collected, graded, tagged daily | W1 |
| Claim register live and populated | Aras | All material claims from collection registered | W1 |
| PIR taxonomy refined for Malaysian context | UiTM | Refined PIR set validated against recent information events | W2 |
| Entity extraction pipeline operational | Aras | Actors, orgs, locations, dates extracted from every signal | W2 |
| Issue register operational | Aras | Issues classified, scored, lifecycle-tracked | W3 |
| Issue scoring engine calibrated | UiTM | 10-dimension scoring calibrated for Malaysian issues | W3 |
| Daily R.I.S.I.K Brief delivered | Aras | Operational brief delivered to decision-makers | W4 |
| First weekly strategic review | Joint | Framework performance reviewed, adjustments identified | W4 |

**Phase 1 Exit Criteria:**
- [ ] Daily collection running with >90% source success rate
- [ ] All claims graded A-F with confidence levels
- [ ] All signals PIR-tagged
- [ ] Issue register with ≥20 scored issues
- [ ] Daily brief delivered for ≥5 consecutive days
- [ ] PIR taxonomy validated by UiTM
- [ ] First weekly review conducted

### Phase 2 — Analytical Core (Weeks 5-10, ~Oct-Nov 2026)

**Goal:** Layer 2 analytical functions operational. Core R.I.S.I.K capability.

| Task | Owner | Deliverable | Week |
|------|-------|------------|------|
| Sentiment classification pipeline | Aras (build) | BM/English sentiment: polarity, intensity, emotion per signal | W5-6 |
| Malaysian sentiment model validation | UiTM | Validate sentiment accuracy against Malaysian context | W6 |
| Emotion analysis pipeline | Aras | Emotion labels: anger, fear, anxiety, hope, pride, frustration | W7 |
| Audience segmentation engine | Aras | Segment by geography, age, language, community | W7-8 |
| Influence network mapping — actor discovery | Aras | Actor registry populated from collected data | W8 |
| Influence network mapping — relationship mapping | Aras | Actor-actor, actor-narrative, actor-platform relationships | W9 |
| Narrative detection & clustering | Aras | Narrative clusters with similarity scores | W9-10 |
| Influence mapping validation | UiTM | Validate actor classifications, network roles | W10 |
| Integrated Assessment Brief (IAB) generator | Aras | Auto-drafted IAB from all analytical outputs | W10 |

**Phase 2 Exit Criteria:**
- [ ] Sentiment pipeline running on all collected signals
- [ ] Emotion analysis producing actionable labels
- [ ] Actor registry with ≥100 entries
- [ ] Influence network map visualised
- [ ] Narrative clusters identified and tracked
- [ ] IAB generated for ≥5 priority issues
- [ ] UiTM validation of sentiment and influence outputs

### Phase 3 — Decision & Engagement (Weeks 11-16, ~Dec 2026 - Jan 2027)

**Goal:** Layer 3 and Layer 4 operational. Full R.I.S.I.K cycle.

| Task | Owner | Deliverable | Week |
|------|-------|------------|------|
| Operational dashboard | Aras | Strategic, operational, measurement views | W11-12 |
| Escalation trigger engine (live) | Aras | Automated alerts wired to Telegram/dashboard | W12 |
| Kontra Narrative content pipeline | UiTM (design) + Aras (build) | Message design model, content templates, approval workflow | W12-14 |
| Messenger briefing system | Aras | Briefing generation for identified trusted messengers | W13 |
| Channel management system | Aras | Multi-platform deployment coordination | W14 |
| Measurement framework | Aras | Pre/post intervention measurement: reach, engagement, sentiment shift | W14-15 |
| Post-intervention review process | Joint | 11-point review template + process | W15 |
| First controlled simulation | Joint | End-to-end simulation: detect → verify → assess → prioritise → design → approve → execute → measure → adapt | W16 |

**Phase 3 Exit Criteria:**
- [ ] Dashboard operational with all three views
- [ ] Escalation triggers firing on threshold breach
- [ ] Kontra Narrative pipeline producing approved messages
- [ ] Measurement framework tracking ≥1 intervention
- [ ] Post-intervention review conducted
- [ ] Controlled simulation completed end-to-end
- [ ] Lessons-learned report produced

### Phase 4 — Scale & Institutionalise (Weeks 17-26, ~Feb-Apr 2027)

**Goal:** Level 4 — Intelligence-Led. Cross-agency, measurable, institutionalised.

| Task | Owner | Deliverable | Week |
|------|-------|------------|------|
| Scenario simulation engine | Aras | Multi-scenario projection capability | W17-18 |
| Cross-agency workflow | Joint | Coordination protocol with other agencies | W18-20 |
| Training programme | Joint | R.I.S.I.K operator training curriculum | W20-22 |
| Operational exercise | Joint | Full-scale exercise with real-time injection | W22 |
| Monthly performance review process | Joint | Scorecard, maturity assessment, strategic forecast | W23 |
| Institutional knowledge base | Aras | Lessons-learned, case studies, best practices | W24-25 |
| Level 4 maturity assessment | Joint | Independent assessment against maturity model | W26 |

### Phase 5 — PoC & Beyond (Months 7-12, ~May-Oct 2027)

**Goal:** Level 5 — Adaptive. AI-enabled, continuous learning, institutionalised.

| Task | Owner | Deliverable | Month |
|------|-------|------------|-------|
| Proof of Concept demonstration | Joint | PoC demonstrating operational relevance to stakeholders | M7 |
| PoC review and stakeholder briefing | Joint | Stakeholder presentation | M7 |
| Continuous learning system | Aras | Feedback loops, model retraining, adaptive thresholds | M8-9 |
| Advanced AI: scenario simulation at scale | Aras | Multi-variable scenario modelling | M9-10 |
| Publication pathway (academic output) | UiTM | Joint research paper / framework validation publication | M10 |
| National capability assessment | Joint | Assessment of R.I.S.I.K as national capability | M12 |

---

## 8. First Working Session — Proposed Agenda

**Date:** ~6 September 2026 (target)
**Duration:** Half-day (4 hours)
**Location:** UiTM Shah Alam or virtual
**Participants:**
- Aras: DAF (strategic), Hadri (technical), Ember (AI/infrastructure demo)
- UiTM: Prof. Suhaimee, Dr. Mohd Firdauz, En. Antashah, En. Muhd Faiz, En. Al Faliq

### Agenda

| Time | Item | Purpose | Owner |
|------|------|---------|-------|
| 0:00-0:15 | Opening & introductions | Team introductions, meeting objectives | DAF + Prof. Suhaimee |
| 0:15-0:45 | R.I.S.I.K Framework overview | Walk through doctrine, confirm shared understanding | DAF |
| 0:45-1:15 | Operational Development Plan presentation | Present this document as the proposed collaboration structure | DAF |
| 1:15-1:30 | Break | — | — |
| 1:30-2:00 | Aras infrastructure live demo | Collection → PIR tagging → claim register → daily brief (live) | Ember/Aras |
| 2:00-2:30 | UiTM capability & research presentation | UiTM team capabilities, research areas, Malaysian context expertise | Prof. Suhaimee |
| 2:30-3:15 | Responsibility matrix workshop | Review and refine Aras vs UiTM assignments | Joint |
| 3:15-3:30 | Break | — | — |
| 3:30-4:00 | **Data handling & OSA 1972 protocols** | Classification, storage, sharing, publication boundaries | Prof. Suhaimee + DAF |
| 3:30-4:00 | Next steps & timeline | Confirm Phase 1 milestones, communication cadence, decision points | DAF |

### Pre-Session Deliverables (Aras)

- [ ] This plan delivered to UiTM ≥7 days before session
- [ ] Live infrastructure demo prepared and tested
- [ ] PIR taxonomy current state document
- [ ] Sample daily brief (from operationalised pipeline)

### Pre-Session Deliverables (UiTM)

- [ ] Team capability summary (who does what)
- [ ] Research area overview (media and information warfare focus)
- [ ] Malaysian context dataset availability assessment
- [ ] OSA 1972 compliance requirements for collaboration

---

## 9. OSA 1972 Compliance Framework

UiTM's email disclaimer explicitly invokes the Akta Rahsia Rasmi 1972 (Official Secrets Act). This creates legal obligations for how collaboration materials are handled.

### Proposed Classification Protocol

| Classification | Applicability | Handling |
|---------------|--------------|----------|
| **RAHSIA** | Operational intelligence, actor registries, influence maps, intervention plans | Encrypted storage, need-to-know access, no external publication without declassification |
| **SULIT** | Draft analytical products, internal reviews, simulation results | Internal team access only, controlled distribution |
| **TERHAD** | Framework methodology, PIR definitions, non-sensitive analytical patterns | Team + approved stakeholders |
| **AWAM** | Published framework doctrine, academic outputs, non-operational descriptions | Public |

### First Working Session Decision Required

1. Which collaboration outputs fall under OSA classification?
2. What storage and access controls are required for RAHSIA/SULIT materials?
3. What is the declassification pathway for academic publication?
4. Do Aras personnel require security clearance for RAHSIA-level access?
5. What is the information-sharing protocol between Aras (commercial) and UiTM (academic) for classified materials?

---

## 10. Risk Register

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| Aras-U'iTM timeline mismatch (commercial delivery vs academic pace) | Medium | High | Clear phase milestones with joint sign-off; Aras builds infrastructure independently of UiTM research pace |
| OSA 1972 classification blocks collaboration | Medium | High | Resolve in first working session; engage legal counsel if needed; separate classified vs unclassified workstreams |
| PMO engagement remains informal | Medium | Medium | Continue to inform PMO officials (CC'd); formal engagement is a Phase 4 milestone |
| Sentiment models fail on Malaysian context | Medium | High | UiTM validation gate; Malaysian dataset curation by UiTM; fine-tuning on local corpus |
| Funding gap | Medium | High | Phase 0 is Aras-funded (infrastructure already exists); Phase 1-2 low cost (compute is available); Phase 3+ may require sponsorship |
| AI hallucination in analytical outputs | Medium | Critical | CVS mandatory on all outputs; human-in-the-loop gates; confidence tags on all AI-generated content |
| Single-person dependency (DAF) | High | High | Ember handles operational continuity; CognitiveOS captures institutional knowledge; UiTM partnership distributes ownership |

---

## 11. Success Metrics

### Collaboration-Level Metrics

| Metric | Target | Measurement |
|--------|--------|------------||
| First working session conducted | By 6 Sep 2026 | Session held, agenda completed |
| Phase 1 exit criteria met | By end Sep 2026 | All exit criteria checked |
| Sentiment pipeline validated | By end Nov 2026 | UiTM validation report |
| First controlled simulation completed | By end Jan 2027 | Simulation report |
| PoC delivered | By May 2027 | Stakeholder demonstration |
| Academic publication submitted | By Oct 2027 | Draft paper |

### Operational Metrics (Per Framework KPIs)

| Metric | Phase 1 Target | Phase 2 Target |
|--------|----------------|----------------|
| Daily collection success rate | >90% | >95% |
| Average claims verified per day | ≥10 | ≥25 |
| Issue register size | ≥20 | ≥50 |
| Actor registry size | — | ≥100 |
| Sentiment coverage of priority issues | — | 100% |
| Daily brief delivered on time | ≥5 consecutive | Every weekday |
| IABs produced | — | ≥5 |
| Controlled simulations | — | 1 |

---

## 12. Decision Requirements

### Decisions Required from DAF

1. **Approve this plan as the basis for the UiTM working session** — or provide modifications
2. **Authorise Phase 0 build** — Aras operationalises collection, claim register, and daily brief before working session
3. **Confirm OSA 1972 classification approach** — or modify before session

### Decisions Required from UiTM

1. **Accept the responsibility matrix** — or propose modifications
2. **Confirm team member roles** — who leads what within UiTM's 5-person team
3. **Provide Malaysian context dataset assessment** — what data exists, what needs to be collected
4. **Confirm OSA 1972 classification protocol** — or propose alternative

### Decisions Required Jointly

1. **Confirm Phase 1 timeline** — start date, milestones, exit criteria
2. **Establish communication cadence** — weekly check-in? Biweekly review?
3. **Identify first priority use case** — what issue/narrative to use for Phase 1 operational testing

---

## 13. Related Records

- **INIT-20260803-002** — UITM-Aras Strategic Collaboration on AI Enablement of the R.I.S.I.K Framework
- **INIT-20260725-004** — Workstream D: Political & Strategic Intelligence
- **CONV-20260807-001** — UiTM Acceptance-in-Principle email thread
- **DEC-20260807-001** — UiTM agreement in principle to collaborate
- **ACT-20260807-001** — Initiate contact with UiTM team (deadline: 17 Aug)
- **ACT-20260807-002** — Prepare working session agenda (deadline: 24 Aug)
- **COM-20260807-001** — UiTM coordination commitment (due: 6 Sep)
- **RISIK-Framework.md** — Full framework doctrine (23 sections)
- **RISIK-Operational-Process.md** — Detailed operational workflows
- **PIR-definitions.yaml** — Current 10+1 PIR definitions

---

*Document authority: DAF*
*Classification: Confidential — OSA 1972 Aware*
*Status: Draft for DAF review*
*Next action: DAF review → modify → approve → deliver to UiTM as primary working session input*
