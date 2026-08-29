# PRISM SRS Analysis — Technical Architecture & R.I.S.I.K Integration Mapping

**Document:** PRISM System Requirement Specification (SRS) — SaaS v1.0
**Customer:** Bahagian Keselamatan Strategik, Jabatan Perdana Menteri (BKS-JPM)
**Prepared By:** Aras Integrasi
**Approval Authority:** Farul Mohd Ghazali
**Date:** 20 July 2026
**Related:** PRISM_URS_SaaS_v1.0
**Classification:** Private & Confidential (Aras Integrasi)
**Review date:** Aug 26, 2026

---

## Critical Findings

### 1. Full Technical Architecture Revealed

**Data Platform — 3 stores:**
- **PostgreSQL** (relational): articles, sentiment snapshots, ground sessions, predictions, accounts, agent run logs, schedules, segment scores
- **Neo4j** (graph): topic/area/actor nodes with co-occurrence and relationship edges — powers Topic Network and influence mapping
- **Qdrant** (vector): embeddings of articles, knowledgebase documents, ground notes — powers semantic search and RAG citations

**Data Cascade:** COLLECT → REFINE → LAKE → SERVE (collect-once, refine-in-stages, serve-everywhere)

### 2. AI/ML Components Named

| Component | Function | R.I.S.I.K Significance |
|-----------|----------|----------------------|
| **Prediction model** (anchored ensemble + LLM reasoning) | Per-area outcome projection | Maps to R.I.S.I.K Layer I (triage) — needs adaptation for issue-level |
| **MTizer sentiment engine** | Proprietary Malay/English sentiment scoring | Maps to R.I.S.I.K Layer S — already built, needs extension for emotion/trust/behavioural intent |
| **MEMber Suara STT** | Malay-primary speech-to-text | Ground input (HUMINT) — maps to Layer R |
| **MiroFish content integrity** | Fact-checking and misinformation verification | Maps to R.I.S.I.K Layer R (SAMAR indicators) — already built |
| **Eternis runtime** | Agent orchestration: scheduling, pipeline execution, inter-agent events, run logging | The agent fleet infrastructure — R.I.S.I.K agents plug in here |

### 3. R.I.S.I.K in the SRS

**SR-CHT-05** — the explicit R.I.S.I.K integration point:
> "The guided-interview service shall walk an analyst through a configurable analytical framework (e.g. R.I.S.I.K), pulling platform evidence per step and emitting a structured intelligence report with a conclusion."

This is the system-level spec for UR-INT-09. It:
- Names R.I.S.I.K as a configurable analytical framework
- Pulls platform evidence per step (traces to source — §2.5 compliance)
- Emits structured intelligence report with conclusion
- Configurable (not hard-coded) — other frameworks could be plugged in

### 4. Agent Fleet — 7 Agents Specified

| SRS Agent | SR ID | R.I.S.I.K Layer |
|----------|-------|----------------|
| News curation | SR-AGT-02 | R — Risikan |
| Prediction | SR-AGT-02 | I — Isu (triage) |
| Escalation | SR-AGT-03 | I→K + Gate 2 |
| Content integrity | SR-AGT-04 | R (SAMAR) |
| Messaging simulation | SR-PRD-06 | K — Kontra-naratif |
| Topic tagging | SR-AGT-02 | R→I transition |
| Trend detection | SR-ING-06 | R (early signals) |

### 5. Multi-Tenancy Architecture
Each Customer engagement = isolated, configuration-driven tenant. No election/region/client-specific logic hard-coded. R.I.S.I.K capabilities would be tenant-specific configuration, not core platform changes.

### 6. Key System Requirements for R.I.S.I.K

| SR ID | Requirement | R.I.S.I.K Doctrine Alignment |
|-------|------------|------------------------------|
| SR-ING-02 | Sentiment scoring (−1 to +1) with confidence, Malay + English | Layer S — needs extension for emotion/trust/behavioural intent |
| SR-ING-03 | Hierarchical issue taxonomy tagging | Layer I — adaptable for R.I.S.I.K issue classification |
| SR-ING-06 | Keyword/topic spike detection ahead of mainstream | Layer R — early warning, narrative escalation detection |
| SR-ING-07 | Point-in-time history preservation | §2.5 — provenance and audit trail |
| SR-AGT-03 | Escalation agent with configurable thresholds, structured alerts | Gate 2 (Keutamaan) — issue-level escalation |
| SR-AGT-04 | Content integrity agent flags misinformation + coordinated inauthentic behaviour | Layer R — SAMAR indicators |
| SR-AGT-05 | Sensitive-category content → human-only paths, no automated public response | §2.5 + Gate 3 (Kewajaran) — human-in-the-loop |
| SR-AGT-06 | Kill-switch for any agent/output/distribution | Governance — safety control |
| SR-PRD-05 | Simulations sandboxed, never write to live data | §2.5 — AI output not authoritative |
| SR-PRD-06 | Messaging simulation requires recorded human approval | Gate 3 — human approval before action |
| SR-CHT-01 | Command Chat with RAG, citations (sources, counts, refresh time) | §2.5 — every claim traced to source |
| SR-CHT-05 | **Guided-interview service (R.I.S.I.K)** — configurable framework, evidence per step, structured report | **THE R.I.S.I.K integration point** |
| SR-ADM-04 | Tamper-evident (hash-chained) audit log | OSA 1972 compliance |
| SR-ADM-05 | Two-person approval for critical actions | Human-in-the-loop gates |
| SNF-07 | Explainability — every AI output traceable to sources, model, refresh time | §2.5 — provenance |
| SNF-08 | Human-in-the-loop — no autonomous execution | §2.5 — AI proposes, humans dispose |

### 7. What the SRS Tells Us About Build Approach

**Already architected (infrastructure exists):**
- Agent orchestration runtime (Eternis) — R.I.S.I.K agents plug into this
- Multi-store data platform (PostgreSQL + Neo4j + Qdrant) — R.I.S.I.K data structures use these
- RAG with vector store — R.I.S.I.K evidence retrieval uses this
- Graph store for influence mapping — R.I.S.I.K Layer I (Influens) uses Neo4j
- Sentiment engine (MTizer) — R.I.S.I.K Layer S extends this
- Content integrity (MiroFish) — R.I.S.I.K SAMAR indicators extend this
- Reporting engine — R.I.S.I.K daily brief uses this
- RBAC + audit log — R.I.S.I.K governance uses this

**R.I.S.I.K build = configuration + extension, not new infrastructure:**
- SR-CHT-05 (guided interview) = configuring a new analytical framework in existing conversational AI
- Source grading A-F = extending SR-ING-02 scoring pipeline
- Narrative escalation ladder = extending SR-ING-03 taxonomy
- Reference poisoning monitor = new agent on Eternis runtime
- "Ask the chatbot" = new agent querying external chatbot APIs
- TULIS→BINA→SEMAK→LULUS = workflow configuration on existing audit/approval infrastructure

### 8. External Interfaces

| Interface | Direction | R.I.S.I.K Use |
|-----------|-----------|---------------|
| News feeds (RSS/API) | Inbound | Layer R collection |
| Social-listening provider | Inbound (needs credentials) | Layer R SOCMINT |
| Official electoral/registry data | Inbound (needs credentials) | Layer R baseline |
| Resource-management backend | Inbound (needs Customer system) | Operations |
| Report distribution channels | Outbound (PDF) | Layer K output |
| Speech-to-text service | Internal | Layer R HUMINT (voice ground reports) |

---

## Revised Build Assessment

With URS + SRS, the technical picture is now complete:

| Build Category | Effort | Basis |
|---------------|-------|-------|
| R.I.S.I.K guided interview (SR-CHT-05) | 5-7 days | Configure analytical framework in existing conversational AI + RAG |
| Source grading A-F extension | 1-2 days | Extend SR-ING-02 scoring pipeline |
| Narrative escalation ladder | 1-2 days | Extend SR-ING-03 taxonomy with 5-rung classification |
| Sentiment extension (emotion/trust/behavioural) | 3-4 days | Extend MTizer engine for R.I.S.I.K Layer S dimensions |
| Reference poisoning monitor | 4 days | New agent on Eternis runtime + external chatbot API queries |
| "Ask the chatbot" requirement | 2-3 days | New agent capability, queries external AI systems |
| Prompt injection guard | 2 days | Input sanitisation layer for agent pipeline |
| Gate 4 effectiveness measurement | 2-3 days | Post-intervention sentiment comparison (uses existing sentiment engine) |
| OSA 1972 classification marking | 1 day | Extension to existing audit log + document marking |
| TULIS→BINA→SEMAK→LULUS workflow | 2-3 days | Workflow configuration on existing approval/audit infrastructure |
| Issue-level escalation adaptation | 2 days | Adapt SR-AGT-03 from area-level to issue-level thresholds |
| Kontra-naratif pipeline (message testing → approval → measurement) | 3-4 days | Extend SR-PRD-06 + SR-AGT-05 + Gate 4 |

**Revised total: ~28-35 days** (down from ~40-47 URS-based estimate and ~45 original estimate)

The SRS reveals that most infrastructure already exists. R.I.S.I.K integration is primarily configuration + agent extension + new agents on existing runtime.

---

## Questions Resolved by SRS

| Previous Question | SRS Answer |
|------------------|-----------|
| Tech stack? | PostgreSQL + Neo4j + Qdrant, browser-based War Room app, Eternis agent runtime |
| AI agent implementation? | Eternis orchestration runtime — scheduling, pipeline execution, inter-agent events |
| API structure? | RAG-based conversational AI with vector store retrieval, pluggable connectors |
| How modular is agent fleet? | Each agent independently start/stop-able and configurable (SR-AGT-02) |
| How does UR-INT-09 work? | SR-CHT-05: configurable analytical framework in conversational AI, pulls evidence per step |
| Data schema adaptability? | Hierarchical configurable issue taxonomy (SR-ING-03), multi-store architecture |
| Front-end framework? | Browser-based War Room application with Command/Intelligence/Operations/Admin layers |
| Timeline for Planned items? | Not specified in SRS — operational detail |
| Multi-tenancy for R.I.S.I.K? | Each engagement = isolated configuration-driven tenant, no hard-coded logic |
| Prediction engine implementation? | Anchored ensemble + LLM reasoning, configurable inputs with time-decaying weights |

## Questions Still Open

1. What LLM models power the agents (GLM-5.2? Qwen? Custom?)
2. What's the deployment infrastructure (cloud provider, containers, orchestration)?
3. How is the Eternis runtime configured for new agents?
4. What's the MTizer training data and can it be extended for R.I.S.I.K-specific sentiment dimensions?
5. How does the guided-interview framework configuration work (SR-CHT-05) — what's the config format?
6. What's the relationship between PRISM's Eternis runtime and Aras's vLLM endpoint?

---

*Analysis by Ember (Aras Integrasi) — Aug 26, 2026*
*Source: PRISM SRS SaaS v1.0 (Aras Integrasi, Private & Confidential)*
*Received via Telegram from DAF, Aug 26, 00:08 UTC*
