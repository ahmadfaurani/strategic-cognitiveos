# PRISM URS Analysis — JPM/BKS Delivery + R.I.S.I.K Integration Mapping

**Document:** PRISM User Requirement Specification (URS) — SaaS v1.0
**Customer:** Bahagian Keselamatan Strategik, Jabatan Perdana Menteri (BKS-JPM)
**Prepared By:** Aras Integrasi — Delivery & Business Analysis Team
**Approval Authority:** Farul Mohd Ghazali
**Date:** 20 July 2026
**Basis:** User Requirement & System Requirement Study workshop (14 July 2026)
**Classification:** Private & Confidential (Aras Integrasi)
**Review date:** Aug 25, 2026

---

## Critical Findings

### 1. PRISM Full Name Revealed
PRISM = **Predictive Real-time Intelligence Sentiment Monitoring System**

### 2. PRISM Is Already Contracted to JPM/BKS
This is not an internal product looking for a customer. PRISM is already being delivered as SaaS to the Prime Minister's Department's Strategic Security Division. The URS was based on a workshop held July 14, 2026.

### 3. R.I.S.I.K Is Already Referenced in the URS
UR-INT-09 explicitly mentions R.I.S.I.K:
> "Guided intelligence interview: a structured, framework-driven Q&A (aligned to the Customer's analytical doctrine, e.g. R.I.S.I.K — Reality, Issue, Sentiment, Influence, Kontra-narrative)"

R.I.S.I.K is named as the analytical doctrine. Status: **Planned** (not yet built).

### 4. Many Capabilities Are Already "Available"
Of the ~30 user requirements listed, a significant portion are already "Available" in the current platform baseline. Only a subset are "Planned."

### 5. SaaS Delivery Model
PRISM is delivered as subscription SaaS on Aras-managed infrastructure. Configuration-driven onboarding, not custom builds. New deployments through data + configuration, not new development.

---

## PRISM Core Flow

```
SENSE (continuous ingestion) → UNDERSTAND (AI sentiment + issue tagging) → PREDICT (per-area projections) → ALERT (threshold-based, severity-ranked) → DECIDE (human decision; results feed back)
```

This maps to the R.I.S.I.K cycle: R (SENSE) → I+S (UNDERSTAND) → I (PREDICT) → K (ALERT + DECIDE)

---

## User Roles (RBAC)

| Role | Scope | R.I.S.I.K Parallel |
|------|-------|-------------------|
| Leader (L) | Full picture, all areas, approval authority | Decision authority — Gate 3/4 |
| PMO/Analyst (P) | War-room modules, scoped to assigned areas, validates AI output | Analyst — Layers R through K |
| SME (S) | Ground intelligence, knowledgebase, validation workflows | HUMINT source + Gate 1 validation |
| System Admin (A) | User management, data connections, agents, audit | Infrastructure operator |

**Ground Volunteer (v2.0)** — deferred. In v1.0, ground input via SME role.

---

## Requirements Status Summary

### Available (in current platform baseline)

| ID | Requirement | R.I.S.I.K Layer |
|----|-----------|----------------|
| UR-CMD-01 | Decision-first Executive Dashboard | Command/Decision (K output) |
| UR-CMD-02 | Role-based default landing screens | Infrastructure |
| UR-CMD-03 | Conversational Command Chat (cited answers, Daily Brief) | All layers — AI assistant |
| UR-CMD-05 | Narrative Monitor (News Sentiment, Social Pulse, Topic Network) | R + S — Risikan + Sentimen |
| UR-CMD-08 | Escalation alerts (severity, category, recommended response) | I→K + Gate 2 |
| UR-INT-01 | Per-area contest watch (baseline, risk rating, trend) | R + I |
| UR-INT-02 | AI entity dossiers (strengths, weaknesses, sentiment, network) | I (Influens) |
| UR-INT-03 | Continuous watchlist (sentiment, mentions, issues per entity) | R + S |
| UR-INT-04 | Audience/voter segment analysis | S — Sentimen |
| UR-INT-05 | Aggregated ground-intelligence results | R (HUMINT input) |
| UR-INT-06 | Early-trend detection (Trend Scout) | R — early signals |
| UR-INT-07 | Influence mapping (KOL registers, network views, narrative gaps) | I — Influens |
| UR-RPT-01 | Scheduled intelligence reports (PERSADA standard: daily AM/PM, weekly) | K — output/delivery |
| UR-RPT-04 | Continuous alerting (24/7 threshold-based) | I→K |
| UR-ADM-01 | Role-based user management | Infrastructure |
| UR-ADM-03 | Configurable ingestion schedules | Infrastructure |
| UR-ADM-05 | Agent management console | Infrastructure |

### Planned (committed roadmap)

| ID | Requirement | R.I.S.I.K Layer | Notes |
|----|-----------|----------------|-------|
| UR-CMD-06 | Scenario simulation (1/2/3-way, sandboxed) | K — Kontra-naratif | Maps to R.I.S.I.K messaging simulation |
| UR-CMD-07 | Message testing (4 strategy modes, human approval required) | K — Kontra-naratif | Direct R.I.S.I.K Layer K |
| UR-INT-08 | Configurable composite prediction index (time-decaying weights + omega) | I — Isu (triage) | Advanced prediction |
| UR-INT-09 | **Guided intelligence interview (R.I.S.I.K-aligned)** | All layers | **THE R.I.S.I.K integration point** |
| UR-SME-04 | Human validation workflow (SME review of AI outputs) | Gate 1-4 | Doctrine compliance |
| UR-SME-05 | Complaint and programme input channels | R (HUMINT) | New data channel |
| UR-RPT-02 | Canned report distribution (PDF to distribution lists) | K — output | Delivery automation |
| UR-RPT-03 | Mandatory disclaimer on all generated reports | Governance | §2.5 AI declaration |
| UR-ADM-02 | In-platform data register (owner, freshness, health) | Infrastructure | Data governance |
| UR-ADM-04 | Tamper-evident audit log | Infrastructure | OSA 1972 compliance |
| UR-ADM-06 | Kill-switch and response policy | Governance | Safety control |
| UR-ADM-07 | Two-person approval for critical actions | Governance | Human-in-the-loop |

---

## R.I.S.I.K Integration Points in URS

### UR-INT-09 — The Primary Integration Point
> "Guided intelligence interview: a structured, framework-driven Q&A (aligned to the Customer's analytical doctrine, e.g. R.I.S.I.K — Reality, Issue, Sentiment, Influence, Kontra-narrative) that starts from an issue in any area, uses platform data as evidence, and produces a structured intelligence report with a conclusion."

**Status: Planned** — This is the explicit R.I.S.I.K integration requirement. It:
- Names R.I.S.I.K as the doctrine
- Covers all 5 layers (R, I, S, I, K)
- Uses platform data as evidence (traces to source — §2.5 compliance)
- Produces structured intelligence report
- Starts from an issue (Layer I entry point)

### Other R.I.S.I.K-Aligned Requirements
- UR-CMD-07 (Message testing) → Layer K (Kontra-naratif) — human approval required ✅
- UR-CMD-08 (Escalation alerts) → Gate 2 (Keutamaan) — sensitive categories escalate to humans ✅
- UR-SME-04 (Human validation workflow) → Gates 1-4 — SME validation before projections ✅
- UR-RPT-03 (Mandatory disclaimer) → §2.5 "declare AI influence" ✅
- UR-ADM-07 (Two-person approval) → Human-in-the-loop gates ✅
- NFR-04 (Evidence over vibes) → §2.5 "every claim traced to source" ✅
- NFR-05 (Human-in-the-loop) → §2.5 "AI proposes, humans dispose" ✅

### What R.I.S.I.K Adds Beyond Current URS

| R.I.S.I.K Capability | URS Coverage | Gap |
|---------------------|-------------|-----|
| Source grading (A-F) | Not in URS | Need new requirement |
| Narrative escalation ladder (5 rungs) | Not in URS | Need new requirement |
| Reference poisoning monitor (§2.5.4) | Not in URS | Need new requirement — first-mover |
| "Ask the chatbot" intelligence requirement | Not in URS | Need new requirement — first-mover |
| Prompt injection guard (§2.5.5) | Not in URS | Need new requirement |
| Kontra-naratif effectiveness measurement (Gate 4) | Not in URS | Need new requirement |
| TULIS→BINA→SEMAK→LULUS governance | Not in URS | Process, not requirement |
| OSA 1972 classification marking | Not in URS | Need new requirement |

---

## Strategic Implications

### 1. PRISM is already operational with JPM/BKS
This is not a greenfield build. PRISM has a paying customer (JPM), a workshop-derived URS, and many capabilities already "Available." The R.I.S.I.K integration enhances an existing contracted platform.

### 2. R.I.S.I.K is already named in the URS
UR-INT-09 names R.I.S.I.K as "the Customer's analytical doctrine." This means JPM/BKS has already been exposed to the R.I.S.I.K framework. The integration is not a new proposal — it's fulfilling an existing planned requirement.

### 3. The SRS is still needed
The URS defines WHAT. The SRS will define HOW. The SRS is where the technical architecture for R.I.S.I.K integration will be specified. Still awaiting from Farul.

### 4. Many R.I.S.I.K capabilities are already built
The URS shows that influence mapping (UR-INT-07), narrative monitoring (UR-CMD-05), trend detection (UR-INT-06), entity dossiers (UR-INT-02), escalation alerts (UR-CMD-08), and scheduled reporting (UR-RPT-01) are already Available. This further reduces the build effort.

### 5. The "Planned" items are the R.I.S.I.K build scope
Most "Planned" requirements map directly to R.I.S.I.K doctrine capabilities:
- UR-INT-09 (guided intelligence interview) = the R.I.S.I.K 5-layer cycle
- UR-CMD-06/07 (simulation + message testing) = Layer K
- UR-SME-04 (human validation) = Gates 1-4
- UR-ADM-07 (two-person approval) = human-in-the-loop

### 6. MCMC proposal may need repositioning
If PRISM is already contracted to JPM/BKS, the MCMC proposal may need to position R.I.S.I.K as an enhancement to an existing JPM platform, not a standalone new capability. Or: MCMC funds the R.I.S.I.K doctrine integration + academic validation, while JPM funds the platform operation.

### 7. The workshop was July 14 — before UiTM collaboration
The URS workshop (July 14) predates the UiTM collaboration formalization (Aug 7-16). This means the R.I.S.I.K reference in UR-INT-09 was DAF's doing — he already embedded R.I.S.I.K into the PRISM requirements before UiTM was engaged. UiTM's role is to provide the doctrine content for UR-INT-09's implementation.

---

## Revised Build Effort Assessment

With URS requirements mapped:

| Category | URS Status | R.I.S.I.K Build Effort |
|----------|-----------|----------------------|
| Already Available (17 requirements) | ✅ Built | Zero — extend with R.I.S.I.K terminology |
| Planned (12 requirements) | 🟡 Committed roadmap | ~30-35 days (the core build) |
| Not in URS (8 R.I.S.I.K-specific) | ❌ Missing | ~10-12 days (new requirements needed) |

**Revised total: ~40-47 days** (down from ~45 days, because some "Planned" items may partially overlap with existing build effort)

---

## Questions Resolved

| Previous Question | URS Answer |
|------------------|-----------|
| Who is the customer? | BKS-JPM (Bahagian Keselamatan Strategik, Jabatan Perdana Menteri) |
| Is PRISM contracted? | Yes — SaaS subscription, workshop July 14, URS July 20 |
| Is R.I.S.I.K in the requirements? | Yes — UR-INT-09 explicitly names R.I.S.I.K |
| What's the delivery model? | SaaS on Aras-managed infrastructure |
| What's the onboarding model? | Configuration-driven, weeks not months |
| Is automated messaging enabled? | No — deliberately disabled pending content-moderation workflow (aligns with R.I.S.I.K Gate 3) |

## Questions Still Open (for SRS)

1. What is the current tech stack (languages, frameworks, databases)?
2. How are AI agents implemented (models, orchestration)?
3. What's the API structure?
4. How modular is the agent fleet for R.I.S.I.K-specific additions?
5. How does UR-INT-09 (guided intelligence interview) architecture work?
6. What's the data schema for influence mapping (UR-INT-07)?
7. How is the prediction engine (UR-INT-08) implemented?
8. What's the timeline for "Planned" items?
9. How does the SaaS multi-tenancy work for R.I.S.I.K-specific capabilities?
10. What's the feedback cycle mechanism for enhancement requests?

---

*Analysis by Ember (Aras Integrasi) — Aug 25/26, 2026*
*Source: PRISM URS SaaS v1.0 (Aras Integrasi, Private & Confidential)*
*Received via Telegram from DAF, Aug 25, 23:35 UTC*
