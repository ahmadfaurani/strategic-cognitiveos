# PRISM System Overview — Analysis & R.I.S.I.K Integration Mapping

**Document:** PRISM System Overview v.1
**Source:** DAF (via Telegram, Aug 25, 2026)
**Author/Owner:** Aras Integrasi Sdn. Bhd.
**Classification:** Private & Confidential
**Review date:** Aug 25, 2026

---

## Document Summary

PRISM is an AI-powered campaign intelligence platform developed by Aras Integrasi. It combines real-time news/sentiment monitoring, electoral forecasting, ground canvassing, and autonomous AI agents into one command-and-control interface.

**Current focus:** Electoral campaigns (campaign directors, coordinators, ground teams)
**Strategic significance for R.I.S.I.K:** PRISM 2.0 = PRISM platform + R.I.S.I.K doctrine = KKOM system

---

## PRISM Architecture — 4 Working Layers

| Layer | Function | R.I.S.I.K Mapping |
|-------|----------|-------------------|
| **Command** | Day-to-day dashboards, AI chat, heatmap, monitoring views for leadership | Maps to KKOM dashboard (Aliran Kerja Stage 3 front-end) + Layer K output delivery |
| **Operations** | Scenario simulation, resource optimisation, volunteer management | Maps to R.I.S.I.K Layer K (Kontra-naratif) response planning + Gate 3 (Kewajaran) |
| **Intelligence** | Voter segmentation and analysis of canvassing results | Maps to R.I.S.I.K Layers R+I+S (Risikan, Isu, Sentimen) — collection and analysis |
| **Administration** | Data connections, scraping schedules, user management | Maps to Aliran Kerja Stage 1 (Data Foundation) + Stage 2 (Back-end + API) |

**Backend:** Secure multi-database (records, relationships, smart search) + external news/data feeds

---

## AI Agent Fleet — 6 Autonomous Agents

| Agent | What It Does | R.I.S.I.K Layer | Doctrine Alignment |
|-------|-------------|-----------------|-------------------|
| News & content | Gathers and tags news/social posts in near real-time | R — Risikan | Direct match. Auto-collection + tagging = Layer R foundation |
| Prediction | Scores every seat with win probability | I — Isu (triage) | Electoral-specific. Needs adaptation for information warfare scoring (triage sensitivity × reach) |
| Risk & escalation | Flags constituencies crossing risk threshold, drafts alerts | I → K transition + Gate 2 (Keutamaan) | Maps to threshold escalation. R.I.S.I.K needs issue-level escalation, not constituency-level |
| Content integrity | Screens for misinformation and inauthentic activity | R — Risikan (behavioural indicators) | Maps to SAMAR indicators (Annex 1). AI detecting coordinated inauthentic behaviour |
| Messaging simulation | Tests likely public reaction to messages before release | K — Kontra-naratif | Maps to §2.5 AI as tool — message testing before deployment. Gate 3 (Kewajaran) input |
| Trend scouting | Spots emerging topics before mainstream | R — Risikan (early signals) | Maps to "collecting too late" common error — trend scouting = early warning system |

**Key insight:** 5 of 6 agents map directly to R.I.S.I.K doctrine layers. The Prediction agent is electoral-specific and needs adaptation for information warfare context.

---

## PRISM Operational Loop

```
1. Data comes in (automated feeds + field reports)
2. AI processes it (agents curate, tag, check, score, flag)
3. Insight goes out (dashboards, heatmaps, alerts, AI assistant)
4. Decisions are made (budget, messaging, ground effort)
5. New data is created → cycle repeats
```

**R.I.S.I.K parallel:** The R.I.S.I.K cycle (R→I→S→I→K→back to R) is a closed cycle — same architecture. PRISM's loop already implements the "response becomes new signal" principle.

---

## Critical Realization: What PRISM 2.0 Actually Means

**PRISM 1.0:** Electoral campaign intelligence platform
**PRISM 2.0:** PRISM + R.I.S.I.K doctrine = information warfare + campaign intelligence

The "integration" is NOT connecting two separate systems. It's EVOLVING PRISM to incorporate the R.I.S.I.K methodology:

| PRISM 1.0 (Current) | PRISM 2.0 (Target) | Source |
|---------------------|---------------------|--------|
| Electoral monitoring | Electoral + information environment monitoring | R.I.S.I.K Layer R |
| Win probability scoring | Issue triage scoring (sensitivity × reach) | R.I.S.I.K Layer I + Gate 2 |
| Sentiment tracking | Sentiment + emotion + trust + behavioural intent | R.I.S.I.K Layer S |
- | Actor/influence network mapping | R.I.S.I.K Layer I (Influens) — NEW capability |
| Messaging simulation | Kontra-naratif response planning + effectiveness measurement | R.I.S.I.K Layer K + Gate 4 |
- | Reference poisoning monitor ("ask the chatbot") | §2.5.4 — NEW capability, first-mover |
| Constituency heatmap | Issue heatmap + narrative escalation ladder overlay | R.I.S.I.K visualization |
| AI assistant (campaign Q&A) | AI assistant + R.I.S.I.K doctrine compliance checking | §2.5 AI rules |

**What's already built (PRISM 1.0):**
- Multi-database backend
- News/social data feeds
- AI agent infrastructure (6 agents)
- Dashboard/heatmap/AI chat front-end
- Continuous loop architecture

**What R.I.S.I.K adds:**
- Doctrine (5-layer methodology, gates, source grading, narrative ladder)
- Information warfare capabilities (influence mapping, reference poisoning, kontra-naratif)
- Governance model (TULIS→BINA→SEMAK→LULUS)
- Malaysian context adaptation
- Academic validation (UiTM/CMIWS)
- OSA 1972 compliance framework

**What this means for the build:**
The Aliran Kerja 5-stage build sequence assumes building from scratch. With PRISM as the base, Stage 1 (Data Foundation) and Stage 2 (Back-end + API) are PARTIALLY COMPLETE. The build effort shifts to:
- Adapting existing data schema to R.I.S.I.K terminology
- Adding R.I.S.I.K-specific data structures (claim register, issue register, actor registry, narrative clusters)
- Extending AI agents for R.I.S.I.K functions
- Adapting front-end for R.I.S.I.K workflow (5-layer cycle, gates, source grading)
- Adding new capabilities (influence mapping, reference poisoning monitor, kontra-naratif pipeline)

**Implication for Farul's URS/SRS:** The URS (User Requirements Specification) and SRS (Software Requirements Specification) will define how PRISM 1.0 capabilities map to R.I.S.I.K requirements. This is the critical bridge document.

---

## Strategic Implications

1. **PRISM is not a dependency — it's a foundation.** The R.I.S.I.K × PRISM integration is internal product evolution, not external system integration.
2. **Build effort is lower than estimated.** The STRAT-20260807-001 plan estimated ~58 person-days for 16 AI functions. With PRISM's existing agent infrastructure, many functions are adaptations of existing agents, not new builds.
3. **MCMC proposal strengthens.** "We're enhancing an existing operational platform" is a stronger pitch than "we're building from scratch."
4. **UiTM alignment shifts.** UiTM's role becomes validating R.I.S.I.K doctrine implementation ON PRISM, not building from scratch. The TULIS→BINA→SEMAK→LULUS cycle applies to the enhancement, not the initial build.
5. **The "developer" question from Aliran Kerja is answered.** Aras/Farul's team is the developer. The "internal technical companion" is Hadri/Fuad. The RISIK team (UiTM) writes specs and reviews.
6. **The RISIK git repo DAF mentioned likely contains PRISM source code or the PRISM-RISIK integration branch.**

---

## Questions Resolved by This Document

| Aliran Kerja Question | Answer from PRISM Overview |
|-----------------------|---------------------------|
| Who is the "developer"? | Aras Integrasi (Farul's team) — PRISM is their product |
| What technology stack? | Multi-database backend, AI agent fleet, dashboard front-end (specifics in URS/SRS) |
| Is there an existing API? | Yes — PRISM has data connections and scraping schedules (Administration layer) |
| What database is being considered? | Multi-database backend already exists |
| Is there a budget or is this part of RM5M? | PRISM is Aras's existing investment. R.I.S.I.K integration is the new scope. |
| Relationship between KKOM and RISIK? | KKOM = PRISM 2.0 = PRISM enhanced with R.I.S.I.K doctrine |

## Questions Still Open (for Farul's URS/SRS)

1. What is the current PRISM tech stack (languages, frameworks, databases)?
2. How are AI agents implemented (what models, what orchestration)?
3. What's the current API structure?
4. How is user authentication/authorization handled?
5. What's the deployment architecture (cloud, on-prem, hybrid)?
6. How modular is the agent fleet — can new R.I.S.I.K-specific agents be added?
7. What's the data schema — how adaptable is it to R.I.S.I.K terminology?
8. What's the current front-end framework — can it support the 8 KKOM prototype screens?
9. What's the timeline and effort estimate for PRISM 2.0 enhancements?
10. What's the relationship between PRISM's "Intelligence" layer and R.I.S.I.K's Layers R+I+S?

---

*Analysis by Ember (Aras Integrasi) — Aug 25, 2026*
*Source: PRISM System Overview v.1 (Aras Integrasi, Private & Confidential)*
