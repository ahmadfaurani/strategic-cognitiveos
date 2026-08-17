---
id: STRAT-20260807-001
record_type: initiative
title: R.I.S.I.K Operational Development Plan — From Doctrine to Operations
created_at: 2026-08-07 08:30:00+00:00
updated_at: '2026-08-17T17:56:20+00:00'
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
priority: high
lifecycle_state: draft
confidence: medium
source:
  type: null
  reference: null
summary: 'Authority: DAF Date: 7 August 2026 Classification: Confidential — OSA 1972 Aware Parent Initiative: INIT-20260803-002 — UITM-Aras Strategic Collaboration on AI Enablement of the R.I.S.I.K Framework Pa'
strategic_significance: Strategic initiative.
mission_alignment: []
related_records: []
portfolio_tier: strategic
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

### 2.1 Maturity Trajectory — What Moves Us Between Levels

| Transition | What Must Be True | Plan Phase | Target Date |
|-----------|-----------------|-----------|-------------|
| **Level 1 → Level 2** | Daily collection operational; claim register live; issue register with scored issues; PIR taxonomy validated; daily brief delivered on schedule | Phase 0 + Phase 1 | End Sep 2026 |
| **Level 2 → Level 3** | Sentiment pipeline running; influence network map active; narrative detection producing clusters; IAB generated from linked R→I→S→In workflow; first controlled simulation completed | Phase 2 + Phase 3 | End Jan 2027 |
| **Level 3 → Level 4** | Dashboard operational with all three views; escalation triggers wired; cross-agency workflow tested; predictive indicators validated; training programme delivered; operational exercise passed | Phase 4 | End Apr 2027 |
| **Level 4 → Level 5** | Continuous learning system active (model retraining, adaptive thresholds); scenario simulation at scale; academic publication submitted; national capability assessment completed; PoC demonstrated to stakeholders | Phase 5 | End Oct 2027 |

### 2.2 Current Level 1→2 Gap Assessment

| Level 2 Requirement (per Section 22, Phase 1-2) | Current State | Gap | Build Owner |
|------------------------------------------------|-------------|-----|------------|
| Approve doctrine and governance | ✅ Done (23 sections, CognitiveOS governance) | None | — |
| Define roles | ⚠️ Framework roles defined, not staffed | Staffing | DAF |
| Establish issue taxonomy | ✅ PIR definitions exist (10+1 PIRs) | Refinement for non-election context | UiTM |
| Establish data-source register | ⚠️ 32 sources configured in DeerFlow | Source grading A-F missing | Aras |
| Create operational templates | ✅ SIB, IAB, NIP templates in Operational Process | None | — |
| Define legal and ethical controls | ⚠️ OSA 1972 identified, protocol not agreed | Joint agreement | Joint |
| Build initial issue register | ❌ Does not exist | Build claim register + issue register | Aras |
| Identify priority use cases | ⚠️ Johor PRN 2026 seats identified | Non-election use cases needed | Joint |
| Launch daily brief | ⚠️ Generator exists, never operationalised | Wire and schedule | Aras |
| Begin claim verification | ⚠️ CVS exists, not wired to daily flow | Pipeline integration | Aras |
| Introduce issue scoring | ❌ 10-dimension model defined, not built | Build scoring engine | Aras |
| Establish sentiment baseline | ❌ No sentiment pipeline | Build sentiment pipeline | Aras (Phase 2) |
| Build initial influence maps | ❌ No actor registry or network mapping | Build influence pipeline | Aras (Phase 2) |
| Establish message approval workflow | ⚠️ CognitiveOS DEC/ACT records exist | Operationalise for R.I.S.I.K | Joint |
| Develop performance dashboard | ❌ Does not exist | Build dashboard | Aras (Phase 3) |

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

| # | AI Function | Input | Output | Engine | Priority | Effort | Depends On |
|---|-----------|-------|--------|--------|----------|--------|------------|
| 1 | Entity extraction | Raw collected text | Structured entities (actors, orgs, locations, dates, numbers) | vLLM (GLM-5.2) | P0 — blocking | 3 days | Daily collection running |
| 2 | Event detection | Entity-tagged signals | Event records with timestamp, location, actors | vLLM + PIR tagger | P0 | 3 days | #1 (entity extraction) |
| 3 | Claim extraction & clustering | Raw text | Structured claims with source attribution | vLLM + CVS | P0 | 4 days | #1, CVS integration |
| 4 | Duplicate detection | Signal registry | Deduplicated signal set | Embedding similarity (Qwen3.5-27B) | P1 | 2 days | #1, signal registry |
| 5 | Topic modelling | Collected corpus | Topic clusters with keywords | vLLM (GLM-5.2) + clustering | P1 | 3 days | #1, #4 |
| 6 | Summarisation | Daily signal corpus | Executive summary (3-5 paragraphs) | vLLM (GLM-5.2) | P1 | 2 days | #1, #4 |

**Build approach:** Prompt template engineering against vLLM API. Each function is a Python script that:
1. Reads from Signal Registry (JSONL)
2. Constructs a structured prompt (system + user messages)
3. Calls vLLM endpoint (`model.arasintegrasi.ai/v1/chat/completions`)
4. Parses structured JSON response
5. Writes enriched data back to Signal Registry or claim register
6. Logs model version, confidence, timestamp per Section 14.2

**Testing approach:**
- Each function tested against 50-sample gold set (manually verified outputs)
- Accuracy threshold: ≥85% precision, ≥75% recall for entity/claim extraction
- Sentiment/emotion: ≥80% agreement with human-coded labels on 100-sample test set
- UiTM validation gate on all Malaysian-context functions before production

**Prompt template storage:** `tools/risik-ai/prompts/` — version-controlled prompt templates per function

### Phase B — Analytical AI (Weeks 5-10)

| # | AI Function | Input | Output | Engine | Priority | Effort | Depends On |
|---|-----------|-------|--------|--------|----------|--------|------------|
| 7 | Sentiment classification | Text by segment | Polarity, intensity, emotion tags (per Section 7.2 — 8 dimensions) | vLLM (Qwen3.5-397B) | P0 — core R.I.S.I.K | 5 days | #1, #4 (entity extraction, dedup) |
| 8 | Emotion analysis | Text by segment | Emotion labels: anger, fear, anxiety, hope, pride, frustration (per Section 7.2) | vLLM (Qwen3.5-397B) | P0 — core R.I.S.I.K | 4 days | #7 (sentiment pipeline) |
| 9 | Narrative similarity | Narrative database | Similar narrative clusters with cosine similarity scores | Embedding (Qwen3.5-27B) + cosine similarity | P1 | 4 days | #3 (claim clustering), #5 (topic modelling) |
| 10 | Network analysis | Actor relationships (from entity extraction) | Influence network map with network roles (per Section 8.4 Step 3) | Graph algorithms (NetworkX) + LLM classification | P1 — core R.I.S.I.K | 6 days | #1 (entity extraction), actor registry |
| 11 | Trend detection | Time-series signal data | Trend indicators: velocity, acceleration, direction change | Statistical (numpy/scipy) + LLM interpretation | P1 | 4 days | Signal registry with ≥30 days data |
| 12 | Alert generation | Threshold breaches (per Section 16) | Structured alert with context, recommended action | Rule engine + LLM (GLM-5.2) | P1 | 3 days | #11 (trend detection), escalation triggers configured |

**Model routing strategy:**
- GLM-5.2: Primary model for extraction, summarisation, report drafting, translation (fast, capable)
- Qwen3.5-397B: Analytical functions requiring deep reasoning (sentiment, emotion, narrative analysis)
- Qwen3.5-27B: Embedding and similarity tasks (lightweight, fast)
- Kimi-K2.5/K2.6: Fallback and specialised tasks (long-context analysis)

### Phase C — Advanced AI (Weeks 11-16)

| # | AI Function | Input | Output | Engine | Priority | Effort | Depends On |
|---|-----------|-------|--------|--------|----------|--------|------------|
| 13 | Report drafting | Structured analysis (IAB components) | Draft IAB / daily brief per Section 19 template | vLLM (GLM-5.2) | P2 | 4 days | #1-12 all operational |
| 14 | Evidence retrieval | Claim queries | Supporting evidence from corpus with citations | RAG (Qwen3.5-27B embeddings) + vLLM | P2 | 5 days | #3 (claim register), embedding index |
| 15 | Scenario simulation | Issue parameters + historical patterns | 3-scenario projections (best/likely/worst case) | vLLM (multi-shot, GLM-5.2) | P2 | 5 days | #11 (trend data), #9 (narrative clusters) |
| 16 | Translation | BM ↔ English texts | Translated documents with terminology glossary | vLLM (GLM-5.2) | P2 | 2 days | Glossary built from collection corpus |

**Total estimated effort:** ~58 person-days across 16 functions
**Critical path:** #1 → #2 → #3 → #7 → #8 → #13 (entity extraction through report drafting)
**Parallel tracks:** #4-6 can run alongside #2-3; #9-12 can run alongside #7-8; #14-16 are independent

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
| Scenario simulation engine | Aras | Multi-scenario projection capability (best/likely/worst case per issue, with confidence intervals and historical comparison) | W17-18 |
| Cross-agency workflow | Joint | Coordination protocol with other agencies (CSM, NACSA, JDN/JDM, PMO); defined data-sharing boundaries under OSA 1972; escalation paths to national authority | W18-20 |
| Training programme | Joint | R.I.S.I.K operator training curriculum: 5 modules (Collection & Verification, Analysis & Assessment, Decision & Approval, Engagement & Measurement, Governance & Compliance); 2-day workshop format; trained operators can run daily cycle independently | W20-22 |
| Operational exercise | Joint | Full-scale exercise: real-time injection of simulated information event; tests end-to-end R.I.S.I.K cycle (detect → verify → assess → prioritise → design → approve → execute → measure → adapt); exercise report with performance scores | W22 |
| Monthly performance review process | Joint | Monthly scorecard (collection rate, verification time, sentiment accuracy, intervention effectiveness, maturity level); quarterly strategic forecast; annual capability review | W23 |
| Institutional knowledge base | Aras | Lessons-learned database, case study library, best practice guides, operator playbook, troubleshooting guide; stored in CognitiveOS with searchable index | W24-25 |
| Level 4 maturity assessment | Joint | Independent assessment against maturity model (Section 21); conducted by UiTM academic team; written report with scorecard and recommendations | W26 |

**Phase 4 Exit Criteria:**
- [ ] Scenario engine produces 3-scenario projections for ≥5 priority issues
- [ ] Cross-agency workflow tested with ≥1 partner agency
- [ ] Training curriculum delivered to ≥5 operators (Aras + UiTM)
- [ ] Operational exercise completed with end-to-end R.I.S.I.K cycle
- [ ] Monthly performance review process documented and running
- [ ] Institutional knowledge base with ≥10 case studies
- [ ] Level 4 maturity independently assessed and confirmed

### Phase 5 — PoC & Beyond (Months 7-12, ~May-Oct 2027)

**Goal:** Level 5 — Adaptive. AI-enabled, continuous learning, institutionalised.

| Task | Owner | Deliverable | Month |
|------|-------|------------|-------|
| Proof of Concept demonstration | Joint | PoC demonstrating operational relevance to stakeholders; live demonstration of full R.I.S.I.K cycle on a real priority issue; includes before/after measurement data; audience: PMO officials, CSM, NACSA, sponsor institutions | M7 |
| PoC review and stakeholder briefing | Joint | Stakeholder presentation: PoC results, capability assessment, recommended next steps (institutional adoption, funding, scaling); written briefing document for senior decision-makers | M7 |
| Continuous learning system | Aras | Feedback loops: post-intervention review data feeds back into model retraining; adaptive thresholds (escalation triggers adjust based on false positive/negative rates); model evaluation pipeline (monthly accuracy audit, drift detection) | M8-9 |
| Advanced AI: scenario simulation at scale | Aras | Multi-variable scenario modelling: inject multiple simultaneous issues, test cascade effects, model intervention sequencing; Monte Carlo simulation with 100+ iterations per scenario | M9-10 |
| Publication pathway (academic output) | UiTM | Joint research paper: framework validation, methodology, case study results, Malaysian context findings; submission to peer-reviewed journal (e.g., Journal of Information Warfare, Asian Journal of Communication); UiTM leads academic writing, Aras provides operational data | M10 |
| National capability assessment | Joint | Assessment of R.I.S.I.K as national capability: maturity scorecard against Level 5 criteria, gap analysis, recommended institutional home (PMO? NACSA? CSM?), funding model, staffing model, legal framework; written report for national decision-makers | M12 |

**Phase 5 Exit Criteria:**
- [ ] PoC demonstrated to ≥3 stakeholder institutions
- [ ] Continuous learning system operational (model retraining cycle ≤30 days)
- [ ] Scenario simulation handles ≥3 simultaneous issues
- [ ] Academic publication drafted and submitted
- [ ] National capability assessment completed with recommendations
- [ ] Level 5 maturity independently assessed

**PoC Scope Definition:**
- **What:** Full R.I.S.I.K cycle applied to one real priority issue (selected jointly by Aras + UiTM)
- **Duration:** 30-day operational period (collection → analysis → intervention → measurement)
- **Success criteria:** Detect issue ≤24h after emergence; verify ≤48h; produce IAB ≤72h; design intervention ≤96h; deploy ≤120h; measure impact ≤14 days post-intervention; post-intervention review ≤21 days
- **Stakeholder audience:** PMO officials (informal), CSM, NACSA, UiTM leadership, Aras leadership
- **Output:** PoC Report (operational timeline, KPI results, lessons learned, capability assessment, recommendation for institutional adoption)

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
| 4:00-4:30 | Next steps & timeline | Confirm Phase 1 milestones, communication cadence, decision points, next meeting date | DAF |

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
| **RAHSIA** | Operational intelligence, actor registries, influence maps, intervention plans, simulation results | Encrypted storage, need-to-know access, no external publication without declassification |
| **SULIT** | Draft analytical products, internal reviews, IAB drafts, sentiment assessments | Internal team access only, controlled distribution |
| **TERHAD** | Framework methodology, PIR definitions, non-sensitive analytical patterns, training materials | Team + approved stakeholders |
| **AWAM** | Published framework doctrine, academic outputs (post-review), non-operational descriptions | Public |

### Data Flow Classification

| Data Stage | Default Classification | Rationale |
|-----------|---------------------|-----------|
| Raw collected signals (news, OSINT) | TERHAD | Open-source data, but aggregation pattern reveals collection priorities |
| Source reliability grades | TERHAD | Reveals source assessment methodology |
| Claim register (verified/unverified) | SULIT | Pre-decisional analytical product |
| Issue register (scored issues) | SULIT | Pre-decisional, reveals strategic priorities |
| Sentiment assessments | SULIT | Analytical product with audience segmentation data |
| Actor registry / influence maps | RAHSIA | Names individuals with influence assessments — security-sensitive |
| Narrative threat assessments | RAHSIA | Reveals counter-narrative strategy and vulnerability analysis |
| Intervention plans (NIPs) | RAHSIA | Pre-deployment operational plans |
| Post-intervention measurement | SULIT | Post-deployment, but reveals effectiveness of operations |
| Daily R.I.S.I.K Brief | SULIT | Distributed to decision-makers; contains assessments |
| IAB (Integrated Assessment Brief) | RAHSIA | Comprehensive intelligence product for command authority |
| Framework doctrine (published) | AWAM | Intended for public reference |
| Academic research outputs (pre-review) | SULIT | Subject to OSA review before declassification to AWAM |
| Academic research outputs (post-review) | AWAM | Declassified after OSA review and approval |

### Publication Review Process

1. **Draft produced** by researcher (UiTM or Aras)
2. **Internal review** by author's institution (UiTM academic review or Aras internal review)
3. **OSA classification check** — does the output contain RAHSIA or SULIT material? If no → proceed to publication. If yes → proceed to step 4.
4. **Declassification review** by joint Aras-UiTM committee (DAF + Prof. Suhaimee or delegates). Criteria: (a) operational security not compromised, (b) no protected sources revealed, (c) no actor identities disclosed without consent, (d) no intervention methodology that could be counter-exploited.
5. **Redaction or sanitisation** — if partial declassification is approved, redact protected elements and mark as TERHAD or AWAM as appropriate.
6. **Final approval** — DAF (Aras) + Prof. Suhaimee (UiTM) joint sign-off for any AWAM publication derived from RAHSIA/SULIT source material.
7. **Audit trail** — all classification decisions logged in CognitiveOS with reviewer, date, rationale.

### Aras Personnel Clearance

- **Current state:** DAF holds Director-level authority. No formal security clearance framework exists for Aras personnel.
- **Proposed:** Phase 1 (Sep 2026) — DAF and named Aras technical personnel (currently Hadri/Ember operator) are designated RAHSIA-access personnel. Access list maintained in CognitiveOS.
- **Phase 3+ (Dec 2026+):** If cross-agency workflow requires formal clearance, DAF to initiate clearance process through appropriate national authority (e.g., JPN/JDN).
- **Principle:** Access is need-to-know, logged, and revocable. No blanket access.

### Information-Sharing Protocol (Aras ↔ UiTM)

| Sharing Direction | Mechanism | Controls |
|-----------------|----------|----------|
| Aras → UiTM (operational data for analysis) | GitHub repo (strategic-cognitiveos, private) + shared drive | RAHSIA/SULIT materials in designated directories with access controls; UiTM team members added as collaborators with need-to-know access |
| UiTM → Aras (research outputs, Malaysian context data) | Same GitHub repo + academic data sharing | UiTM materials classified on creation; Aras accesses per classification |
| Joint → External (publications, PoC) | Publication review process (above) | Joint sign-off required for any AWAM output derived from classified source |

### First Working Session Decisions Required

1. Which collaboration outputs fall under OSA classification? (Proposed: see Data Flow Classification table above)
2. What storage and access controls are required for RAHSIA/SULIT materials? (Proposed: GitHub private repo + access list in CognitiveOS)
3. What is the declassification pathway for academic publication? (Proposed: see Publication Review Process above)
4. Do Aras personnel require formal security clearance for RAHSIA-level access? (Proposed: Phase 1 need-to-know designation; Phase 3+ formal clearance if cross-agency)
5. What is the information-sharing protocol between Aras (commercial) and UiTM (academic) for classified materials? (Proposed: see Information-Sharing Protocol table above)

---

## 10. Risk Register

| # | Risk | Probability | Impact | Owner | Early Warning Indicators | Mitigation | Contingency |
|---|------|------------|--------|-------|------------------------|------------|-------------|
| R1 | Aras-UiTM timeline mismatch (commercial delivery vs academic pace) | Medium | High | DAF | UiTM misses ≥2 consecutive deadlines; no response within 7 days on action items | Clear phase milestones with joint sign-off; Aras builds infrastructure independently of UiTM research pace; biweekly check-in cadence | Decouple Aras build schedule from UiTM validation; Aras proceeds with self-validation, UiTM validates retrospectively |
| R2 | OSA 1972 classification blocks collaboration | Medium | High | DAF + Prof. Suhaimee | Legal counsel flags unresolved classification issue; UiTM blocks data sharing; publication review stalls | Resolve in first working session; engage legal counsel if needed; separate classified vs unclassified workstreams; publication review process defined before Phase 2 | Limit collaboration to TERHAD/AWAM classified outputs; pause RAHSIA-level work until protocol agreed |
| R3 | PMO engagement remains informal | Medium | Medium | DAF | PMO officials not responding to CC'd communications; no follow-up after 30 days | Continue to inform PMO officials; formal engagement is a Phase 4 milestone; PoC demonstration as conversion trigger | Proceed without formal PMO engagement; position R.I.S.I.K as Aras-UiTM academic-commercial capability seeking institutional adoption |
| R4 | Sentiment models fail on Malaysian context | Medium | High | Aras (build) + UiTM (validate) | Accuracy <80% on UiTM validation set; BM-language texts misclassified; sarcasm/irony not detected | UiTM validation gate; Malaysian dataset curation by UiTM; fine-tuning on local corpus; code-switching (BM-English) test set | Fall back to human-coded sentiment for priority issues; use LLM few-shot with Malaysian examples instead of fine-tuned model |
| R5 | Funding gap | Medium | High | DAF | Phase 3+ timeline approaches without sponsor identified; compute costs exceed budget | Phase 0 is Aras-funded (infrastructure already exists); Phase 1-2 low cost (compute is available); Phase 3+ may require sponsorship | Phase 3+ scope reduced to what Aras can fund internally; seek government grant (e.g., MDEC, MOSTI) or PMO sponsorship |
| R6 | AI hallucination in analytical outputs | Medium | Critical | Aras | Confidence tags consistently LOW on specific function; false positive rate >15% on validation set; human reviewer overrides >25% of AI outputs | CVS mandatory on all outputs; human-in-the-loop gates; confidence tags on all AI-generated content; per-function accuracy audit monthly | Disable specific AI function and revert to human-only for affected pipeline; investigate model/prompt issues; switch model (e.g., GLM-5.2 → Qwen3.5-397B) |
| R7 | Single-person dependency (DAF) | High | High | DAF | DAF unavailable >72h; no delegated authority for decisions; UiTM requests go unanswered | Ember handles operational continuity; CognitiveOS captures institutional knowledge; UiTM partnership distributes ownership; document decision rights for delegation | DAF delegates strategic authority to named Aras colleague; UiTM point-of-contact shifts to Prof. Suhaimee for academic matters; Ember maintains operational pipeline independently |
| R8 | UiTM team member turnover | Medium | Medium | Prof. Suhaimee | Team member leaves UiTM or Centre; response times increase; quality of Malaysian context input declines | Knowledge transfer within UiTM team (5 members provide redundancy); document all UiTM contributions in CognitiveOS; cross-train across team | UiTM recruits replacement; Aras absorbs affected workstream temporarily; reduce scope of UiTM-dependent functions |
| R9 | Data breach / unauthorised access to RAHSIA materials | Low | Critical | Aras (data governance) | Unusual access patterns in Git logs; unauthorised IP accessing repo; RAHSIA materials found outside controlled environment | GitHub private repo with 2FA; access list in CognitiveOS; audit logging; need-to-know principle | Immediate access revocation; breach assessment; notify all parties; engage cybersecurity incident response (Aras core capability) |

---

## 11. Success Metrics

### Collaboration-Level Metrics

| Metric | Target | Measurement Method | Reporting Cadence |
|--------|--------|-------------------|-----------------|
| First working session conducted | By 6 Sep 2026 | Session held, agenda completed, minutes filed in CognitiveOS | One-time |
| Phase 1 exit criteria met | By end Sep 2026 | Exit criteria checklist (8 items) all signed off | One-time |
| Sentiment pipeline validated | By end Nov 2026 | UiTM validation report with accuracy scores against gold set | One-time per validation cycle |
| First controlled simulation completed | By end Jan 2027 | Simulation report with timeline, KPI results, lessons learned | One-time |
| PoC delivered | By May 2027 | PoC report + stakeholder presentation; attendee feedback survey | One-time |
| Academic publication submitted | By Oct 2027 | Draft paper submitted to peer-reviewed journal; submission confirmation | One-time |
| Maturity level advancement | Level 2 by Sep 2026; Level 3 by Jan 2027; Level 4 by Apr 2027; Level 5 by Oct 2027 | Independent assessment against Section 21 maturity model | Quarterly |

### Operational Metrics (Per Framework KPIs)

| Metric | Phase 1 Target | Phase 2 Target | Measurement Method | Framework Section |
|--------|----------------|----------------|-------------------|-----------------|
| Daily collection success rate | >90% | >95% | DeerFlow run log: successful sources / total sources per day | Section 5.6 |
| Average time to verify a material claim | ≤48 hours | ≤24 hours | Claim register timestamps: detection → verification | Section 5.6 |
| Percentage of priority claims verified | ≥80% | ≥95% | Claim register: verified claims / total priority claims | Section 5.6 |
| Average claims verified per day | ≥10 | ≥25 | Claim register daily count | Section 5.6 |
| Number of independent sources per assessment | ≥2 | ≥3 | IAB source count audit | Section 5.6 |
| Issue register size | ≥20 | ≥50 | Issue register query count | Section 6.7 |
| Time taken to classify a new issue | ≤24 hours | ≤4 hours | Issue register timestamps: detection → classification | Section 6.7 |
| Percentage of high-priority issues with assigned owners | 100% | 100% | Issue register owner field check | Section 6.7 |
| Actor registry size | — | ≥100 | Actor registry count | Section 8.6 |
| Percentage of priority actors mapped | — | ≥80% | Influence map coverage check | Section 8.6 |
| Sentiment coverage of priority issues | — | 100% | Sentiment pipeline output count vs priority issue count | Section 7.7 |
| Change in trust score | — | Measurable for ≥3 issues | Pre/post sentiment comparison | Section 7.7 |
| Daily brief delivered on time | ≥5 consecutive | Every weekday | Brief delivery timestamp vs schedule | Section 19 |
| IABs produced | — | ≥5 | IAB count in CognitiveOS | Operational Process B |
| Controlled simulations | — | 1 | Simulation report filed | Operational Process A-E |
| Intervention effectiveness measured | — | ≥1 intervention with pre/post data | Measurement framework report | Section 9.8 |
| Post-intervention reviews completed | — | 100% of interventions | Review report count vs intervention count | Section 20 |
| AI function accuracy audit | — | Monthly, ≥85% precision per function | Per-function validation against gold set | Section 14.2 |
| Human-in-the-loop gate compliance | 100% | 100% | Audit log: all gated actions have human approval record | Section 14.3 |

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
