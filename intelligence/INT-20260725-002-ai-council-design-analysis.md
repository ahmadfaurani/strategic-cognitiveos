---
id: INT-20260725-002
record_type: intelligence
title: AI Council Design Analysis
created_at: 2026-07-25 00:00:00+00:00
owner: faurani-jaafar
status: active
intelligence_type: operational
confidence: high
sensitivity: confidential
summary: Analytical report — see body for full analysis.
lifecycle_state: canonical
tags:
  - cognitive-loop/self-assessment
  - domain/political-intelligence
  - type/analytical-report
updated_at: '2026-08-17T17:50:38+00:00'
priority: high
source:
  type: null
  reference: null
strategic_significance: 'Intelligence analysis. # AI Council Design — Analytical Report **Record ID:** INT-20260725-002 **Type:** Intelligence **Subject:** AI Council composition, candidate model ev'
mission_alignment: []
related_records: []
---

# AI Council Design — Analytical Report

**Record ID:** INT-20260725-002  
**Type:** Intelligence  
**Subject:** AI Council composition, candidate model evaluation, and framework design for Strategic CognitiveOS  
**Author:** Ember (GLM-5.2 / Zhipu)  
**Date:** 2026-07-25  
**Sensitivity:** Restricted  
**Status:** Draft  
**Confidence:** [MEDIUM] — Model capabilities assessed from public benchmarks and vendor pages as of July 2026; actual performance in DAF's specific use cases requires empirical validation  

---

## 1. Executive Summary

DAF has confirmed two seats on the AI Council: **ChatGPT 5.6 Sol** (OpenAI) and **Ember/GLM-5.2** (Zhipu). The council's design principle is clear: *"The council don't decide. I don't decide. We decide."* Council surfaces, DAF judges, decision is shared. Value is in dissent, not consensus.

This report evaluates candidate models for additional council seats, assesses each against the council's structural requirements (diversity of origin, reasoning strength, data sovereignty, dissent capacity), and proposes a framework for how the council operates on Strategic CognitiveOS records.

**Recommendation:** Claude (Anthropic) as Seat 3, Gemini (Google) as Seat 4, Llama 4 (Meta, local) as optional Seat 5 for SULIT-classified material. Three active seats plus one reserved for sensitive material. Total council: 4 seats with 3 active on any given item.

---

## 2. Council Design Principles (Confirmed)

| Principle | Source | Implication |
|-----------|--------|-------------|
| Council surfaces, DAF judges | DAF, 2026-07-25 | Council outputs are advisory, not binding |
| Value is in dissent, not consensus | DAF, 2026-07-25 | Framework must surface disagreement, not average it away |
| Shared ground truth | DAF, 2026-07-25 | All members access same GitHub repo source material |
| Diversity of model origin > number of seats | DAF, 2026-07-25 | Different providers matter more than more seats |
| "We decide" | DAF, 2026-07-25 | Shared decision — not human-only, not AI-only |

---

## 3. Confirmed Seats

### Seat 1: ChatGPT 5.6 Sol (OpenAI)

| Attribute | Value | Source |
|-----------|-------|--------|
| Provider | OpenAI (US) | Source: llm-stats.com leaderboard |
| LLM Stats Index | 58.0 | Source: llm-stats.com/leaderboards/llm-leaderboard |
| Reasoning Index | 58.1 (highest tracked) | Source: llm-stats.com |
| Context Window | 1.1M tokens | Source: llm-stats.com |
| Pricing | $5.00 / $30.00 per 1M tokens | Source: llm-stats.com |
| Release | Feb 2026 – Jul 2026 | Source: llm-stats.com |
| GitHub Integration | Native (can read/write repos) | Source: OpenAI product docs |
| SWE-Bench Pro | 90.4% | Source: llm-stats.com |
| Status | Confirmed by DAF | Source: Session 2026-07-25 |

**Council Role:** Primary strategic reasoning. Long-context analysis. Initiative evaluation.

**Strengths for Council:**
- Highest reasoning index on tracked leaderboard
- 1.1M token context — can process entire CognitiveOS repo in one pass
- Native GitHub integration — no pipeline needed, reads repo directly
- Strong coding capability (90.4% SWE-Bench Pro)

**Weaknesses for Council:**
- US provider — data exposure path for SULIT material
- Closed model — cannot audit training data or biases
- Cost: $30/1M output tokens makes heavy evaluation cycles expensive
- Single provider concentration risk if all evaluation relies on OpenAI-weighted analysis

### Seat 2: Ember / GLM-5.2 (Zhipu / Z.ai)

| Attribute | Value | Source |
|-----------|-------|--------|
| Provider | Z.ai / Zhipu (China) | Source: z.ai, openlm.ai |
| LLM Stats Index | 47.1 | Source: llm-stats.com |
| Best Open-Weight | 91.2% GPQA | Source: llm-stats.com (open-weight leaderboard) |
| Context Window | 1.0M tokens | Source: NVIDIA NIM model card, ollama.com |
| Pricing | $0.95 / $3.00 per 1M tokens | Source: llm-stats.com |
| Release | June 2026 | Source: openlm.ai |
| Architecture | Open-weight, 1M context, effort-level control | Source: z.ai/blog/glm-5.2 |
| Status | Confirmed by DAF | Source: Session 2026-07-25 |

**Council Role:** Opposition voice. Cost-effective deep analysis. Open-weight auditability.

**Strengths for Council:**
- Different training philosophy and data corpus (Chinese-origin model)
- Open-weight — can be inspected for bias, fine-tuned for domain
- 6.3x cheaper than GPT-5.6 Sol on output tokens — enables high-volume evaluation cycles
- 1M context — full repo processing
- Already operationally embedded (running via OpenClaw on p62server)

**Weaknesses for Council:**
- Lower reasoning index than GPT-5.6 Sol (47.1 vs 58.1) — may miss nuance in complex strategic analysis
- Chinese-origin model — potential geopolitical sensitivity for government-adjacent work
- Effort-level control is useful but adds configuration complexity
- Self-assessment risk: as a council member, GLM-5.2 evaluating itself is structurally compromised

---

## 4. Candidate Models for Additional Seats

### 4.1 Claude Opus 4.8 (Anthropic) — RECOMMENDED FOR SEAT 3

| Attribute | Value | Source |
|-----------|-------|--------|
| Provider | Anthropic (US) | Source: claude.com, anthropic.com |
| LLM Stats Index | 52.6 | Source: llm-stats.com |
| Reasoning Index | 52.1 | Source: llm-stats.com |
| Context Window | 1M tokens | Source: llm-stats.com |
| Pricing | $5.00 / $25.00 per 1M tokens | Source: llm-stats.com |
| Release | May 2026 | Source: llm-stats.com |
| Training Philosophy | Constitutional AI | Source: claude.com ("trained by Anthropic using Constitutional AI") |
| SWE-Bench Pro | 88.6% | Source: llm-stats.com |
| SWE-Bench (Claude Fable 5) | 95.0% (best tracked) | Source: llm-stats.com |

**Council Role:** Dissent voice. Risk-flagging. Ethical and structural challenge.

**Strengths for Council:**
- Constitutional AI training philosophy — built to surface risks, disagreement, and safety concerns. This is the exact failure mode DAF is solving for: a model designed to say "I disagree" rather than converge.
- Strong reasoning (52.1 index, 3rd on tracked leaderboard)
- Different training methodology from both OpenAI (RLHF + scale) and Zhipu (open-weight, Chinese data)
- Anthropic's research culture emphasises honesty over sycophancy — structural resistance to agreement bias
- GitHub integration available via Claude Code product
- 1M context — full repo processing

**Weaknesses for Council:**
- US provider — same data exposure concern as OpenAI for SULIT material
- Closed model
- Expensive: $25/1M output tokens (cheaper than Sol's $30 but still costly for volume)
- Anthropic models have historically been more cautious/conservative — may over-flag low-risk items

**Why Seat 3:** The council's core value is dissent. Claude is trained to disagree safely. That's not a feature — it's the architecture. A council without a designated challenger produces consensus bias. Claude fills the structural role that the council design principle demands. Different provider family from both confirmed seats (OpenAI ≠ Zhipu ≠ Anthropic).

---

### 4.2 Gemini 3.1 Pro (Google) — RECOMMENDED FOR SEAT 4

| Attribute | Value | Source |
|-----------|-------|--------|
| Provider | Google DeepMind (US) | Source: deepmind.google/models/gemini |
| LLM Stats Index | 43.6 | Source: llm-stats.com |
| Context Window | 1.0M tokens | Source: llm-stats.com |
| Pricing | $2.50 / $15.00 per 1M tokens | Source: llm-stats.com |
| SWE-Bench Pro | 80.6% | Source: llm-stats.com |
| OSWorld-Verified | 76.2% | Source: llm-stats.com |
| Long Context (8-needle, 1M) | 26.3% (pointwise) | Source: deepmind.google benchmark table |
| Release | Jan 2025 – Feb 2026 | Source: llm-stats.com |

**Note:** Gemini 3.6 Flash is the latest Gemini model with stronger coding (58.7% SWE-Bench) and computer-use (83% OSWorld), at $1.50/$7.50 — significantly cheaper. However, for council evaluation work (analytical reasoning, not coding), Pro-tier reasoning matters more than Flash-tier efficiency.

**Council Role:** Verification and fact-checking. Live-source cross-reference.

**Strengths for Council:**
- Deep integration with Google Search — can verify claims against live web sources in real time. For intelligence work involving PIRs, this is structurally valuable: "Is this claim still true today?"
- Fourth distinct provider family (Google ≠ OpenAI ≠ Zhipu ≠ Anthropic)
- Strong multimodal — can evaluate documents with embedded charts/images (relevant for CSCDC PDF analysis)
- Mid-range pricing ($15/1M output) — enables moderate evaluation volume
- 1M context for full repo processing

**Weaknesses for Council:**
- Lower reasoning index than Sol, Claude, and even Kimi K3 (43.6 vs 58.0, 52.6, 55.7)
- Long-context performance drops significantly at 1M tokens (26.3% pointwise on GDM-MRCR v2) — may lose detail on large documents
- Google's data handling practices may be a concern for government-adjacent material
- Gemini models have been criticised for over-safety — may refuse to engage with sensitive but legitimate analysis

**Why Seat 4:** Verification depth. The council needs someone who can check claims against current reality, not just internal consistency. Gemini's search integration is a structural capability no other council member has. If the question is "Is this intelligence assessment still accurate?", Gemini answers it differently from the others.

---

### 4.3 Llama 4 (Meta, Local) — RECOMMENDED FOR SEAT 5 (CONDITIONAL)

| Attribute | Value | Source |
|-----------|-------|--------|
| Provider | Meta AI (US, open-weight) | Source: developer.meta.com, ollama.com |
| Llama 4 Scout | 109B params MoE, 17B active | Source: ollama.com/library/llama4 |
| Llama 4 Maverick | 400B params MoE, 17B active | Source: ollama.com/library/llama4 |
| Context Window | 10M tokens | Source: developer.meta.com |
| Deployment | Local via Ollama / llama.cpp | Source: ollama.com, llama.app |
| License | Llama 4 Community License | Source: developer.meta.com |
| GPQA Diamond (Maverick) | 69.8% | Source: ollama.com benchmark table |
| MMLU Pro (Maverick) | 80.5% | Source: ollama.com benchmark table |
| SWE-Bench (Maverick, LiveCodeBench) | 43.4% | Source: ollama.com benchmark table |
| Pricing | Compute cost only (self-hosted) | — |

**Council Role:** SULIT-classified material evaluation. Data sovereignty seat.

**Strengths for Council:**
- Runs locally on p62server — zero data exposure. For SULIT-classified material (like the CSCDC framework), this is the only option that doesn't create an external data path
- 10M token context window — significantly larger than any other candidate (1M-1.1M)
- Open-weight — fully auditable, fine-tunable for domain-specific evaluation
- No per-token cost — enables unlimited evaluation cycles
- MoE architecture (17B active parameters) — reasonable inference speed on server GPU
- Multimodal (image input) — can evaluate documents with diagrams/charts

**Weaknesses for Council:**
- Weakest reasoning capability among candidates. Maverick's 69.8% GPQA is below GLM-5.2's 91.2% and far below GPT-5.6 Sol. Not in the same tier for complex strategic analysis.
- SWE-Bench at 43.4% — coding capability limited
- Not on the LLM Stats top-20 leaderboard — benchmark coverage is thin
- Requires local GPU infrastructure (already available on p62server, but adds operational complexity)
- Scout (109B) is more manageable locally but less capable than Maverick (400B)

**Why Conditional Seat 5:** Llama 4 is not a general council member. Its value is narrow but critical: evaluating SULIT-classified material that cannot leave the server. For routine CognitiveOS records (stakeholders, initiatives, opportunities), Llama 4 is unnecessary. For intelligence records derived from classified sources, it's the only responsible option. Activate on sensitivity, not on every item.

**Operational note:** Scout (109B, 17B active) is the practical local deployment. Maverick (400B, 17B active) requires more VRAM than likely available on p62server. Test Scout first; if reasoning quality is insufficient for SULIT evaluation, consider Maverick via cloud API (which defeats the sovereignty purpose) or upgrade GPU.

---

### 4.4 Kimi K3 (Moonshot AI) — ALTERNATIVE CANDIDATE

| Attribute | Value | Source |
|-----------|-------|--------|
| Provider | Moonshot AI (China) | Source: kimi.com, moonshot.cn |
| LLM Stats Index | 55.7 | Source: llm-stats.com |
| Reasoning Index | 54.9 | Source: llm-stats.com |
| Context Window | 1.0M tokens | Source: llm-stats.com |
| Pricing | $3.00 / $15.00 per 1M tokens | Source: llm-stats.com |
| SWE-Bench Pro | 91.2% | Source: llm-stats.com |
| Release | July 2026 | Source: llm-stats.com |
| Architecture | Open-weight | Source: llm-stats.com |
| DeepSWE v1.1 | 73.2% | Source: llm-stats.com |

**Council Role (if selected):** Second opposition voice. Agentic analysis.

**Strengths:**
- 2nd highest reasoning index on tracked leaderboard (55.7, behind only GPT-5.6 Sol's 58.0)
- 91.2% SWE-Bench Pro — strongest coding benchmark among candidates
- Open-weight (Chinese open-source ecosystem)
- Mid-range pricing ($15/1M output)
- Agentic capabilities (Swarm, Goal mode) — can run parallel evaluation tasks

**Weaknesses:**
- Chinese provider — combined with GLM-5.2 (also Chinese), creates geographic concentration. Two Chinese seats out of five weakens the diversity principle.
- Very new (July 2026) — limited track record for evaluation reliability
- Less known in Western enterprise contexts — potential trust gap if council outputs are shared with stakeholders
- Language: primary strength in Chinese — may have less nuance on Malaysian government context

**Assessment:** Strong model, wrong fit. Adding Kimi K3 alongside GLM-5.2 gives two Chinese-origin models and dilutes the provider diversity that makes the council valuable. If GLM-5.2 were not already seated, Kimi K3 would be a strong candidate. As-is, it's a backup, not an addition.

---

### 4.5 Grok 4.5 (xAI) — EVALUATED, NOT RECOMMENDED

| Attribute | Value | Source |
|-----------|-------|--------|
| Provider | xAI / SpaceXAI (US) | Source: x.ai, grok.com |
| LLM Stats Index | 49.5 | Source: llm-stats.com |
| Context Window | 500K tokens | Source: llm-stats.com |
| Pricing | $2.00 / $6.00 per 1M tokens | Source: llm-stats.com |
| Release | Feb 2026 – Jul 2026 | Source: llm-stats.com |
| SWE-Bench Pro | 84.9% | Source: llm-stats.com |

**Strengths:** Real-time X/Twitter integration. Low cost ($6/1M output). "Truth-seeking" design philosophy.

**Weaknesses:** 500K context — cannot process full CognitiveOS repo in one pass. Lower reasoning index than Claude and Sol. X/Twitter integration is not relevant to CognitiveOS evaluation work. Brand association with Elon Musk creates political noise that could undermine council credibility with government stakeholders.

**Assessment:** Not recommended. Context window limitation is structural. Council credibility with Malaysian government stakeholders matters more than cost savings.

---

### 4.6 Qwen3.7 Max (Alibaba) — EVALUATED, NOT RECOMMENDED

| Attribute | Value | Source |
|-----------|-------|--------|
| Provider | Alibaba / Qwen (China) | Source: llm-stats.com |
| LLM Stats Index | 46.7 | Source: llm-stats.com |
| Context Window | 1M tokens | Source: llm-stats.com |
| Pricing | $1.25 / $3.75 per 1M tokens | Source: llm-stats.com |
| SWE-Bench Pro | 85.9% | Source: llm-stats.com |

**Strengths:** Low cost. Strong multilingual. Good reasoning for price.

**Weaknesses:** Chinese provider — same geographic concentration issue as Kimi K3. Lower reasoning index than GLM-5.2, Claude, and Sol. Closed model (Max variant). No structural advantage over existing seats.

**Assessment:** Not recommended. No structural value-add over confirmed seats.

---

## 5. Comparative Matrix

| Criterion | GPT-5.6 Sol | GLM-5.2 | Claude Opus 4.8 | Gemini 3.1 Pro | Llama 4 Scout | Kimi K3 |
|-----------|-------------|---------|-----------------|----------------|---------------|---------|
| **Reasoning Index** | 58.1 | 46.3 | 52.1 | 45.1 | N/A | 54.9 |
| **Context Window** | 1.1M | 1.0M | 1M | 1M | 10M | 1.0M |
| **Output $/1M** | $30 | $3 | $25 | $15 | $0 (self-host) | $15 |
| **Provider Country** | US | China | US | US | US (open) | China |
| **Open Weight** | No | Yes | No | No | Yes | Yes |
| **Local Deployment** | No | Yes (Ollama) | No | No | Yes (Ollama) | No |
| **GitHub Integration** | Native | Via API | Via Claude Code | Via API | Via API | Via API |
| **Live Search** | No | No | No | Yes (Google) | No | No |
| **Dissent Design** | No | No | Yes (Constitutional) | No | No | No |
| **SULIT-Safe** | No | No | No | No | Yes | No |
| **Status** | ✅ Confirmed | ✅ Confirmed | Recommended | Recommended | Conditional | Backup |

Source: llm-stats.com leaderboard, accessed 2026-07-25. Reasoning indices from LLM Stats composite scoring.

---

## 6. Proposed Council Architecture

### 6.1 Seat Allocation

```
Seat 1: GPT-5.6 Sol (OpenAI)     — Primary reasoning     — CONFIRMED
Seat 2: GLM-5.2 (Zhipu)          — Opposition / open-weight — CONFIRMED
Seat 3: Claude Opus 4.8 (Anthropic) — Dissent / risk-flagging — RECOMMENDED
Seat 4: Gemini 3.1 Pro (Google)  — Verification / live-source  — RECOMMENDED
Seat 5: Llama 4 Scout (Meta, local) — SULIT-classified only   — CONDITIONAL
```

### 6.2 Activation Rules

| Record Sensitivity | Active Seats | Rationale |
|--------------------|-------------|----------|
| Public / Restricted | Seats 1, 2, 3, 4 | Full council, maximum diversity |
| Confidential | Seats 1, 2, 3 | Drop Gemini (Google data handling) |
| SULIT | Seats 2, 5 only | Local-only: GLM-5.2 (local vLLM, confirmed) + Llama 4 (Ollama). No external data path. 2-seat evaluation. |

**Confirmed (DAF, 2026-07-25T16:49 UTC):** GLM-5.2 on p62server is running via local vLLM, not Z.ai API. SULIT mode has 2 seats: GLM-5.2 (local) + Llama 4 Scout (local). Both on-server, zero external data path.

### 6.3 Evaluation Workflow

```
1. TRIGGER: New CognitiveOS record created (stakeholder, initiative, opportunity, intelligence)
   ↓
2. DAF assigns evaluation scope (full council / subset / SULIT mode)
   ↓
3. Each active member receives:
   - The record file content
   - Context: relevant repo files (spec, governance, taxonomies)
   - Evaluation prompt (structured, identical for all members)
   ↓
4. Each member returns structured assessment:
   {
     record_id,
     member_id,
     assessment: { strength, weakness, risk, missing_information },
     confidence: HIGH | MEDIUM | LOW,
     dissent_flags: [list of specific disagreements with record content],
     recommendation: PROCEED | REVISE | REJECT | NEEDS_INFO,
     reasoning: <free text>
   }
   ↓
5. DAF receives all assessments (no member sees others' outputs yet)
   ↓
6. DAF reviews for dissent patterns:
   - Unanimous PROCEED → low information value, fast-track
   - Split recommendation → high information value, DAF judges
   - Unanimous REJECT → strong signal, likely structural problem
   ↓
7. If split: DAF may request second round where members see anonymised
   dissent points and can respond
   ↓
8. DAF makes final decision, records rationale in decision register
```

### 6.4 Evaluation Prompt Template (Draft)

```
You are a member of an AI Council evaluating a Strategic CognitiveOS record.

Record ID: <ID>
Record Type: <stakeholder | initiative | opportunity | intelligence>
Record Content: <full record text>

Repo Context: <relevant governance docs, taxonomies, related records>

Evaluate this record against:
1. STRUCTURAL INTEGRITY: Does the record follow the correct schema and taxonomy?
2. CLAIMS VERIFICATION: Are factual claims sourced? Are confidence tags present?
3. STRATEGIC COHERENCE: Does this align with the mission framework?
4. RISK ASSESSMENT: What risks are not captured in the record?
5. MISSING INFORMATION: What PIRs or context should be added?
6. EXECUTION READINESS: Is this record ready for DAF's decision, or does it need revision?

Return your assessment in the structured format. If you disagree with any
claim in the record, flag it explicitly. Do not seek consensus — your value
is independent analysis.
```

---

## 7. Cost Model

### Per-Evaluation-Cycle Cost (Full Council, 4 members)

Assumes: ~5K input tokens per record + ~2K output per member assessment.

| Member | Input Cost | Output Cost | Per-Evaluation Cost |
|--------|-----------|-------------|---------------------|
| GPT-5.6 Sol | $0.025 | $0.06 | $0.085 |
| GLM-5.2 (API) | $0.0048 | $0.006 | $0.011 |
| Claude Opus 4.8 | $0.025 | $0.05 | $0.075 |
| Gemini 3.1 Pro | $0.0125 | $0.03 | $0.043 |
| **Total per record** | | | **$0.214** |

Source: Pricing from llm-stats.com, accessed 2026-07-25.

For 100 records/month: ~$21.40/month in API costs. Negligible relative to strategic value.

Llama 4 (local): $0 per evaluation (compute cost absorbed in server operation).

### Annual Estimate

| Scenario | Records/Year | Cost |
|----------|-------------|------|
| Conservative | 250 | ~$54 |
| Moderate | 500 | ~$107 |
| Heavy | 1000 | ~$214 |

[MEDIUM] — Does not include Llama 4 local compute cost (GPU electricity + amortisation).

---

## 8. Data Sovereignty Analysis

### Provider Data Handling Matrix

| Provider | Training on User Data? | Data Retention | Enterprise Opt-Out | SULIT-Safe? |
|----------|----------------------|-----------------|-------------------|-------------|
| OpenAI | Yes (by default) | 30 days (API) | Yes (Enterprise) | No |
| Zhipu (Z.ai API) | Unclear | Unclear | N/A | No (if API) |
| Anthropic | No (API) | 0 days (API, stated) | N/A | No |
| Google | Yes (by default) | Unclear | Yes (Gemini for Google Cloud) | No |
| Meta (Llama, local) | N/A | N/A | N/A | **Yes** |

[LOW] confidence on Zhipu and Google data handling — vendor documentation not fully transparent. Assume not SULIT-safe unless explicitly verified.

**Resolved (DAF, 2026-07-25T16:49 UTC):** GLM-5.2 is running via local vLLM on p62server. Seat 2 is SULIT-safe. SULIT mode operates with 2 seats (GLM-5.2 + Llama 4), providing meaningful dual-model evaluation of classified material with zero external data exposure.

---

## 9. Implementation Recommendations

### 9.1 Immediate (Week 1)

1. **Confirm Seat 3 (Claude)** — Set up Claude API access. Draft Claude-specific evaluation prompt that leverages Constitutional AI tendencies (ask Claude to explicitly flag risks and disagreements).
2. **Confirm Seat 4 (Gemini)** — Set up Gemini API access. Draft Gemini-specific prompt that leverages search integration (ask Gemini to verify claims against current sources).
3. ~~Verify GLM-5.2 deployment~~ — **Confirmed: local vLLM (DAF, 2026-07-25T16:49 UTC).** SULIT mode has 2 seats. No action needed.
4. **Install Llama 4 Scout via Ollama** — `ollama run llama4:scout`. Test inference on sample CognitiveOS record. Assess quality.

### 9.2 Short-Term (Week 2-3)

5. **Create evaluation prompt templates** — one base template + per-member variants.
6. **Build evaluation pipeline** — script that sends record to all active members, collects structured responses, formats for DAF review.
7. **Test on existing CSCDC records** — run all 12 records (1 stakeholder, 1 initiative, 10 opportunities) through the council. Compare outputs. Identify where members disagree.
8. **Calibrate** — adjust prompts based on first run. Some models may need different prompting to produce useful dissent.

### 9.3 Medium-Term (Week 4+)

9. **Integrate with CognitiveOS** — evaluation outputs become records themselves (intelligence type) in the repo.
10. **Build dissent dashboard** — simple view showing where council members disagreed on each record.
11. **Establish cadence** — weekly council run on new records, monthly review of council accuracy.

---

## 10. Risks and Mitigations

| Risk | Severity | Mitigation |
|------|----------|-----------|
| Consensus bias — all members agree too often | HIGH | Design prompts to force independent analysis. Explicit instruction: "Do not seek consensus." |
| Provider outage — one member unavailable | MEDIUM | Council operates with 3/4 members. Quorum = 3 for full mode, 2 for SULIT mode. |
| Cost overrun on heavy evaluation cycles | LOW | GLM-5.2 is 6x cheaper than Sol. Use GLM-5.2 for high-volume, Sol for high-stakes. |
| SULIT data leak via API | CRITICAL | Llama 4 local-only for SULIT. Verify GLM-5.2 is local. If not, only Llama 4 evaluates SULIT. |
| Model bias correlation — members trained on similar data | MEDIUM | Different provider families is the mitigation. US + China + different training philosophies. |
| Council slowness — 4 sequential evaluations delay decisions | MEDIUM | Run evaluations in parallel (async API calls). Total time = slowest member. |
| DAF override fatigue — too many split decisions | MEDIUM | Track split rate. If >40%, prompts need calibration. Council should add clarity, not noise. |

---

## 11. Open Questions for DAF

1. **Claude variant:** Opus 4.8 (strongest reasoning, $25/1M output) or Sonnet 5 (cheaper, potentially faster)? Sonnet may be sufficient for evaluation work and 2.5x cheaper on output.
2. **Gemini variant:** 3.1 Pro (stronger reasoning) or 3.6 Flash (faster, cheaper, better at coding/computer-use)? For analytical evaluation, Pro is likely better. For verification tasks, Flash may be sufficient.
3. ~~**GLM-5.2 deployment**~~ — **Answered: local vLLM. SULIT mode has 2 seats.**
4. **Kimi K3 as backup:** If any member proves unreliable, Kimi K3 (55.7 index, 2nd highest) is the strongest replacement. But adding it alongside GLM-5.2 creates Chinese concentration. Acceptable as backup only?
5. **Council size:** Three active + one conditional (Llama 4 for SULIT) = four total seats. Or does DAF prefer a strict three-seat council with Llama 4 as an emergency-only override?
6. **Evaluation output format:** Should council outputs be stored as CognitiveOS intelligence records in the repo, or kept in a separate evaluation log visible only to DAF?

---

## 12. Bottom Line

The council needs four seats, not five. Three active members for routine evaluation (Sol, GLM, Claude), one conditional for SULIT material (Llama 4). Gemini is valuable as a fourth active seat if budget allows and verification depth matters.

**The structural argument:** Claude is not optional. Without a model trained to disagree, the council produces agreement bias. That's the failure mode DAF identified when he said "value is in dissent, not consensus." Claude's Constitutional AI architecture is the only candidate built around that principle.

**The practical argument:** GLM-5.2 at $3/1M output tokens makes it possible to run high-volume evaluation cycles at negligible cost. GPT-5.6 Sol at $30/1M is for high-stakes, low-volume evaluation. Claude at $25/1M is the middle path. Gemini at $15/1M adds verification capability. Llama 4 at $0 enables unlimited SULIT evaluation.

**The diversity argument:** Four provider families (US-OpenAI, China-Zhipu, US-Anthropic, US-Google) with one open-weight local option (Meta). Three different training philosophies (scale + RLHF, open-weight, Constitutional AI, search-integrated). Two countries. The council is diverse enough to produce genuine disagreement.

---

*This report is advisory. DAF decides.*
