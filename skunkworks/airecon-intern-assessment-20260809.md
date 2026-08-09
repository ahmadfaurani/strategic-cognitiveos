# Skunkworks Assessment: AIRecon — Intern Project Evaluation

**Date:** 2026-08-09
**Authority:** DAF
**Project:** AIRecon (https://github.com/pikpikcu/airecon)
**Request:** Evaluate suitability for Aras Intern Skunkworks Division

---

## Executive Summary

**Verdict: CONDITIONAL YES — framed as research, extension, and integration exercise. Not recommended as a core build-from-scratch project.**

AIRecon is too immature, resource-hungry, and risky for interns to build from scratch or operationally deploy. However, it has genuine value as an **exploration platform** teaching sovereign AI principles, local LLM orchestration, and structured VAPT pipelines.

---

## Strategic Fit Assessment

| Criterion | Score | Rationale |
|---|---|---|
| **Cluster B: Cybersecurity Productisation** | ★★★★☆ | Direct VAPT/recon DNA. Pipeline structure mirrors GovSec TIP/VoronScout architecture patterns. |
| **Cluster A: Sovereign AI** | ★★★★★ | 100% offline, local LLM, no API keys, no cloud exfil — aligns perfectly with PERJASA/JDN sovereign AI narrative. |
| **Cluster F: Org Capability Building** | ★★★☆☆ | Good learning for Docker, Python async, LLM tool-calling, SQLite. Steep GPU barrier may exclude some interns. |
| **Gov Client Palatability** | ★★★★☆ | "Local only, no data leaves machine" is strong. Autonomous exploit phase creates legal/liability friction. |
| **Integration with Existing Portfolio** | ★★☆☆☆ | No native GovSec TIP, ChainSentry, or VoronDRQ connectors. Custom bridge work required. |

---

## Key Risks for Intern Context

### 1. ~~Hardware Cliff~~ — ELIMINATED
**Update (2026-08-09):** DAF confirms 32x B200 + 12x A100 available on-prem. This was the primary blocker; now resolved. All model sizes (including Qwen3.5 122B) viable. Zero cloud dependency.

### 2. Autonomous Exploitation = Liability Minefield
- Agent autonomously executes exploits, SQLi confirms, RCE chains
- `allow_destructive_testing: false` helps, but exploit phase is core value proposition
- D&B insurance and client contract nightmare without senior supervision
- **Mitigation:** Track B (Safe Mode fork) explicitly removes autonomous exploitation

### 3. Maturity Gaps
- No visible CI/CD, no test suite referenced
- "Adaptive learning" = JSON file of tool success/failure counts (telemetry, not ML)
- Knowledge base = SQLite FTS5 index (solid but not groundbreaking)

### 4. Expectation Management
- README states: *"AIRecon does not fine-tune the LLM. Its 'learning' is local, structured telemetry."*
- Interns may expect actual RL or fine-tuning

---

## Recommended Skunkworks Scope (Refactored)

**Reframe from:** "Build autonomous pentest agent"
**Reframe to:** "Extend and harden a sovereign reconnaissance pipeline"

| Track | Deliverable | Value to Aras | Difficulty |
|---|---|---|---|
| **A. Malaysian Context Skills Pack** | 15–20 `airecon-skills` playbooks for Malaysian gov/CNII (MyGov Portal recon, MS ISO 27001 checks, MCMC-relevant findings) | Reusable IP, local market differentiator | Medium |
| **B. Gov-Friendly "Safe Mode" Fork** | Read-only reconnaissance + reporting agent. PTES/OWASP-compliant reports with CVSS scoring. No exploit execution without explicit operator approval. | Client-safe, sellable as "Sovereign AI-Assisted Recon" | Medium |
| **C. GovSec TIP Integration Bridge** | MCP server/API bridge to ingest AIRecon output into GovSec TIP data lake (IOCs, endpoint maps, vulnerability findings) | Connects skunkworks to Tier 1 flagship | Medium-High |
| **D. Local Malay/Indon Dataset** | Fork `airecon-dataset` to index Malaysian CVE advisories (CyberSecurity Malaysia, MyCERT), local CTF writeups, Bahasa Melayu security terminology | Improves LLM grounding for local context | Low-Medium |
| **E. Report Generator Module** | Professional PDF/Word reports with Malaysian gov formatting (JPM/MAMPU standards, bilingual BM + English output) | Direct client deliverable | Medium |

---

## Resource Requirements

| Item | Estimate | Notes |
|---|---|---|
| **GPU** | ZERO — on-prem A100/B200 cluster available (DAF confirms 32x B200 + 12x A100) | Qwen3.5 122B easily handled. Multiple interns can run parallel model instances. |
| **Ollama + Docker** | Free | Open source |
| **Caido license** | $30/month/proxy | If proxy integration needed |
| **Intern time** | 3–6 months | Tracks A+C parallel with 2–3 interns |
| **Supervision** | 2–4 hrs/week senior engineer | Critical for safe exploitation boundaries |

### Hardware Position Update (2026-08-09)

**DAF confirms:** 32 units NVIDIA B200 + 12 units NVIDIA A100 available.

This eliminates the primary risk factor. Benchmark comparison:

| Model | VRAM Required | Your Hardware | Status |
|---|---|---|---|
| Qwen3.5 9B (minimum) | 6 GB | B200 / A100 | ✅ || Qwen3.5 35B (recommended) | 20 GB | B200 / A100 | ✅ |
| Qwen3.5 122B (best) | 48+ GB | B200 / A100 | ✅ || Multiple parallel instances | N×model VRAM | 32 B200 + 12 A100 | ✅ |

**Implications:**
- No cloud rental needed ever
- No Colab tunnel workarounds
- No 12-hour session limits
- No model size compromises
- Can run full 122B models for reliability instead of struggling with 8B hallucinations
- Multiple interns can work simultaneously with dedicated model instances

---

## Alternative Intern Projects (If Higher Impact Desired)

| Alternative | Difficulty | Strategic Value | Differentiation |
|---|---|---|---|
| **Custom sovereign SOC analyst agent** | High | Very High | High — no good open-source equivalent |
| **GovSec TIP auto-enrichment module** | Medium | Very High | Very High — directly integrated with Tier 1 |
| **Offensive AI detection tool** (AI phishing, deepfakes) | Medium | High | Medium — competitive space |
| **R.I.S.I.K data ingestion pipeline** (UiTM collab) | Low-Medium | Very High | Very High — funded academic partnership |

---

## Recommended Execution Path

**Phase 1 (Month 1–2): Audit & Extend**
- Install, audit, document AIRecon architecture
- Build Tracks A (Malaysian skills) + D (local dataset)

**Phase 2 (Month 3–4): Harden & Integrate**
- Build Track B (Safe Mode fork)
- Build Track C (GovSec TIP bridge)

**Phase 3 (Month 5–6): Productise & Demo**
- Demo sovereign, offline recon pipeline feeding structured output into GovSec TIP
- Package as "Aras Sovereign Recon Module" for stakeholder presentation

---

## Decision Options

| Option | Best If |
|---|---|
| **A. Approve Tracks A–E** | Max learning + max IP generation. Requires GPU investment. |
| **B. Approve Tracks B+C only** | Goal is demo-able product for CSM/NACSA within 6 months. Narrowest scope, highest stakeholder impact. |
| **C. Reject AIRecon; pivot to GovSec TIP-native enrichment agent** | Goal is maximum strategic alignment with existing Tier 1 flagship. Higher value, lower novelty. |
| **D. Approve as pure learning exercise (Track A only)** | Limited budget, want interns exposed to LLM tool-calling and Docker without production expectation. |

---

## Bottom Line

AIRecon is a **good vehicle** for teaching sovereign AI and structured VAPT pipelines. It is **not a production-ready platform** interns can deploy to clients. The value comes from what Aras builds *around* it — Malaysian context, safe-mode hardening, and integration with existing product stack.

If the skunkworks goal is **learning + capability building**: Approve with scope restriction (Option A or D).
If the goal is **maximum strategic impact within 6 months**: Consider Option C (GovSec TIP-native agent) instead.

---

*Assessment by: Ember*
*Next action pending: DAF decision on scope/approval*
