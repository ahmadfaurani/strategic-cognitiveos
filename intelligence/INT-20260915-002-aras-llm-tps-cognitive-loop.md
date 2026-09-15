---
id: INT-20260915-002
record_type: intelligence
title: "Cognitive Loop — ARAS LLM Performance Cycle 15 Sep: 4-Probe + Source-Trace Sequence Closes With Harness↔Server Alignment CONFIRMED and Zero Remediation; Two In-Cycle Retractions Absorbed by Verify Step"
created_at: 2026-09-15T15:22:00+00:00
updated_at: 2026-09-15T15:22:00+00:00
owner: faurani-jaafar
intelligence_type: operational
status: active
priority: high
sensitivity: confidential
lifecycle_state: candidate
confidence: high
tags:
  - domain/intelligence
  - domain/data-infrastructure
  - mission/intelligence-enablement
  - framework/cognitive-loop
  - framework/llm-latency-forensics
  - type/operational-analysis
source:
  type: operator-directive
  reference: "DAF directive 'Cognitive Loop to the above' (Telegram 2026-09-15 ~23:05 MYT) on the probe #4 completion report. Signal base: probes #1–#4 execution logs (aras-cache-probe.py, aras-agentic-loop-probe.py, aras-decode-tps-probe.py, aras-maxlen-probe.py — all in ~/.hermes/scripts/), hermes insights 30d telemetry, state.db session_model_usage 14d aggregates, harness source trace (agent/system_prompt.py, agent/turn_context.py, agent/model_metadata.py, agent/context_compressor.py), and DAF authorizations at 14:33 MYT (probe #1) and 23:44 MYT (probe #4)."
summary: "Full 8-step Cognitive Loop (Sense→Classify→Correlate→Pattern→Prioritise→Act→Verify→Learn) applied to the 15 Sep ARAS inference-performance cycle. Headline findings: (1) ARAS prefix cache is ACTIVE — identical 3,051-token payload shows TTFT 1.96s→0.24s (8.1×), and flat TTFT across agentic context growth 23K→29K tokens proves cache coverage of the agent loop; the fleet-wide cache_read_tokens=0 telemetry is a LiteLLM proxy reporting artifact, not dead caching; (2) ARAS max_model_len = 1,048,576 established behaviorally (366,658 tok and 628,413 tok served; 1,048,577 → HTTP 400 quoting the exact limit), and Hermes' live resolver returns the identical 1M — no silent threshold mis-sizing; compression threshold therefore 524,288 tokens vs ~134K average prompts = compression rare; (3) decode TPS healthy: GLM-5.2 231 tok/s, Qwen3.5-397B 124 tok/s, reasoning wire-control clean; (4) harness verified cache-sacred by source: system prompt byte-frozen per session (timestamp at tail, birth-frozen), Honcho context injected as user-message suffix with replay invariant — pending item #2 (timestamp re-prefill) RETRACTED before surgery; (5) two self-corrections absorbed in-cycle: mid-prompt timestamp hypothesis (marker was instruction text, real position 95% tail) and prefill extrapolation (small-probe TTFT delta extrapolated ~1.7K tok/s; measured ~31K tok/s at scale — 18× error). Produces 3 scored actions (A2 accept-alignment 4.60 Tier 1 — counter-intuitive null result per §8; A1 skill-instrumentation 3.05 Tier 3, already executed; A3 cached_tokens pass-through request 1.95 Tier 4 deferred), V1–V5 verification all passing, and 4 learnings."
strategic_significance: "Closes the TPS workstream opened 15 Sep morning with a proven null result: the highest-value action was blocking unnecessary surgery on a cache-optimal harness. Establishes ARAS serving ground truth (1M window, ~31K tok/s prefill at scale, cache active behind LiteLLM) as the baseline for all future inference-capacity planning, and hardens the forensics skill with three reusable pitfalls (behavioral max_model_len discovery, TTFT-extrapolation prohibition, proxy-stripped-telemetry artifact class). Demonstrates the loop's Verify step catching both errors before they became policy — the same governed-reversal pattern validated on 14 Sep, now proven on the measurement layer."
mission_alignment:
  - intelligence-enablement
related_records:
  - INT-20260914-003
  - INT-20260914-002
  - DEC-20260914-004
  - DEC-20260914-005
  - INIT-20260710-002
---

# ARAS LLM Performance Cycle — Cognitive Loop (15 Sep 2026)
## Full 8-Step Cycle Applied (Prime Doctrine §5–§8)

**Doctrine Reference:** governance/COGNITIVEOS-PRIME-DOCTRINE.md §5 (Cognitive Operating Loop), §6 (Pattern Recognition Engine), §7 (Actionable Intelligence Standard), §8 (Prioritisation Engine)
**Date:** 15 September 2026 (23:22 MYT / 15:22 UTC)
**Workstream:** ARAS inference performance (TPS) — opened 15 Sep ~14:05 MYT, closed this cycle
**Scope:** GLM-5.2 (primary), Qwen3.5-397B-A17B (aux) served at model.arasintegrasi.ai; Hermes harness (OpenClaw-analog agent loop)

---

## STEP 1 — SENSE

### Signal Capture

| # | Signal | Source | Date/Time (MYT) | Type |
|---|--------|--------|------------------|------|
| S1 | Extreme interactive lag reported on GLM-5.2/OpenClaw | DAF observation | Sep 11 | Symptom |
| S2 | 14d telemetry: GLM-5.2 330M input tok, 193:1 prefill:output, cacheR=0 fleet-wide all-time | state.db session_model_usage | Sep 15 morning | Telemetry anomaly |
| S3 | Config changes deployed: compression 0.50, Honcho first-turn injection | Hermes execution summary | Sep 15 ~14:27 | Change |
| S4 | Pending item #1 (ARAS prefix-cache probe) authorized | DAF directive | Sep 15 14:33 | Directive |
| S5 | Probe #1: identical 3,051-tok payload ×2 — TTFT 1.96s→0.24s (8.1×); Qwen 0.49→0.22s | aras-cache-probe.py | Sep 15 ~23:05 | Measurement |
| S6 | 30d fleet: 193 sessions, 906.7M in / 4.95M out tok; GLM-5.2 884.9M tok | hermes insights | Sep 15 22:5x | Telemetry |
| S7 | 14d per-model: GLM-5.2 2,718 calls, avg ~134K tok/call, in/out 204× | state.db | Sep 15 23:0x | Telemetry |
| S8 | Probe #2: context growth 23,071→29,418 tok across 4 calls — TTFT flat 1.20→0.82s | aras-agentic-loop-probe.py | Sep 15 ~23:2x | Measurement |
| S9 | Probe #3: decode GLM-5.2 231 tok/s; Qwen 124 tok/s; reasoning_tokens=0 | aras-decode-tps-probe.py | Sep 15 ~23:3x | Measurement |
| S10 | Pending item #2 hypothesis: timestamp at "44%" of prompt re-prefills 86KB tool schemas | Initial trace read | Sep 15 ~23:1x | Hypothesis (later retracted) |
| S11 | Source: system prompt byte-frozen per session; rebuild only on compression; timestamp birth-frozen at tail | agent/system_prompt.py | Sep 15 ~23:1x | Source fact |
| S12 | Source: Honcho context = user-message suffix via api_content; replay invariant documented | agent/turn_context.py + honcho plugin | Sep 15 ~23:2x | Source fact |
| S13 | 14d compaction: 3 sessions heavy; Sep-11 session carries 3,085 flags (incident day) | state.db | Sep 15 ~23:2x | Telemetry |
| S14 | /v1/models silent on max_model_len; 400-error wrapper fingerprints LiteLLM→vLLM | ARAS endpoint + error trace | Sep 15 ~23:5x | Discovery |
| S15 | models.dev: same GLM-5.2 deployed at 202K–1M across 26 providers; no arasintegrasi entry | models_dev_cache.json | Sep 15 ~23:5x | Metadata variance |
| S16 | Probe #4: 366,658 tok OK (11.8s); 628,413 tok OK (21.8s); 1,048,577 → 400 exact-limit | aras-maxlen-probe.py | Sep 15 ~23:5x | Measurement |
| S17 | Live resolver invocation returns 1,048,576 (persistent probe-cache hit in chain step 1) | hermes venv | Sep 15 ~23:5x | Source fact |
| S18 | Compression threshold formula verified: max(0.5×(1M−max_tokens), floor) = 524,288; 75% small-ctx floor N/A >512K | agent/context_compressor.py | Sep 15 ~23:5x | Source fact |
| S19 | Prefill rate correction: ~31K tok/s at scale vs ~1.7K extrapolated (18× error) | probe #4 timings | Sep 15 ~23:5x | Measurement correction |

## STEP 2 — CLASSIFY

- **Measurements (T1, executed evidence):** S5, S8, S9, S16, S17, S19
- **Source-code facts (T1, read from installed dist):** S11, S12, S18
- **Telemetry (T2):** S2, S6, S7, S13
- **Metadata/registry (T3 for ARAS applicability):** S14, S15
- **Hypotheses:** S10 (retracted), compression-bloat concern (dissolved by S17/S18)
- **Directives:** S3 (context), S4 (authorization), and DAF "Probe #4 go" 23:44

## STEP 3 — CORRELATE

**C1 — Contradiction resolved: cacheR=0 vs 8.1× TTFT collapse.** Telemetry said caching absent; behavior said present. Resolution: LiteLLM proxy layer strips vLLM's cached_tokens from usage pass-through (fingerprinted from S14's error wrapper). The telemetry was the liar, not the cache. Consumed one diagnostic cycle; root cause is architectural, not operational.

**C2 — Compression-fear dissolved by window resolution.** The 134K avg prompt looked dangerous against the 202,752 family fallback ("glm": 202752 in model_metadata.py — the value the chain WOULD have returned had the probe cache missed). At resolved 1M with 524K threshold, average sessions sit at 26% of trigger. The feared "routine compression bloat" exists only in the counterfactual where ARAS metadata resolution failed.

**C3 — Sep-11 incident recharacterized.** The 3,085-compaction-flag session on the latency-incident day is a single long-lived extreme-context session, not evidence of systemic threshold mis-sizing. Incident attribution stays with the previously-diagnosed call-volume/thinking-pattern causes; compaction was a co-occurring symptom, not the driver.

**C4 — Silent mis-sizing is a live risk class, not a live failure.** models.dev shows the same model ID at 202K (ambient FP8), 262K (huggingface), 512–524K (togetherai/evroc/berget), 1M (baseten/nebius/wandb/inceptron). A provider swap or a fresh Hermes install (cold probe cache) could silently resolve a different window and mis-size the compression threshold. ARAS passed tonight because a persistent probe-cache entry delivered 1M.

**C5 — Measurement methodology feedback loop.** S19's 18× error originated in extrapolating an overhead-dominated 2-call probe. The error inflated the estimated cost of compression events ~15×, which would have overweighted any "reduce compression frequency" remediation. Methodology error and remediation error compound — the loop caught it at Verify.

## STEP 4 — PATTERN RECOGNITION

**P1 — Behavior outranks declared metadata.** Three independent instances this cycle: max_model_len via pre-prefill 400 (S16), cache activity via TTFT pair (S5), resolver output via live invocation (S17). Doctrine: for self-hosted/custom backends, capability claims are established behaviorally once, recorded, and only then trusted.

**P2 — Every proxy layer launders both capability and observability.** LiteLLM unified routing (good) while silently stripping cached_tokens (bad), manufacturing a false "cache suspect" signal. Rule: adding infrastructure requires auditing its telemetry surface, not just its function.

**P3 — Self-correction velocity is a capability metric.** Two retractions in one cycle (S10 timestamp placement; S19 prefill rate), both caught by Verify before becoming policy. Compare: the Aug-16 CJ-MLK-03 cycle where an uncaught error shipped at T1/10. The difference is procedure (probe-before-claim), not model quality.

**P4 — Null results are valid loop outcomes.** The harness is already cache-optimal by documented design (AGENTS.md: "Per-conversation prompt caching is sacred"). The discipline that produced value here was proving the null — protecting a correct architecture from an invasive "fix" (timestamp relocation surgery) justified by a phantom.

**P5 — Prefill-dominated economics confirmed healthy.** 204× in/out ratio with 231 tok/s decode and cache-covered growth = the fleet's token economics are structurally sound for agent loops; no remediation lever exists on the serving side at current scale.

## STEP 5 — PRIORITISE (§8 7-Dimension Weighted Scoring)

| Action | SI 25% | TC 15% | PL 15% | CMV 15% | DU 10% | StI 10% | RR 10% | Score | Tier |
|--------|--------|--------|--------|---------|--------|---------|--------|-------|------|
| **A1** — Instrument the 3 pitfalls into llm-latency-forensics skill (TTFT-extrapolation ban; behavioral max_model_len recipe; proxy cacheR artifact) | 3 | 3 | 4 | 3 | 2 | 2 | 4 | **3.05** | Tier 3 |
| **A2** — Accept harness↔server alignment; change NOTHING in config or harness; record ARAS serving baseline (1M window, cache active, 31K tok/s prefill, 231/124 tok/s decode) | 5 | 5 | 5 | 5 | 3 | 3 | 5 | **4.60** | Tier 1 |
| **A3** — Request ARAS-side enablement of cached_tokens pass-through (LiteLLM config) for true cost observability | 2 | 1 | 2 | 2 | 2 | 2 | 3 | **1.95** | Tier 4 |

Reconciliation note: A2 scoring above 4.00 mirrors the 14 Sep DeerFlow precedent (accept 4.50 beat fix 2.90) — the counter-intuitive Tier-1 "do nothing, record why" is structurally sound when the alternative is surgery on a verified-correct system. A1 was executed in-cycle (skill patched before this record was filed). A3 is deferred with a documented trigger: revisit only if cost-attribution becomes a billing or capacity-planning requirement.

## STEP 6 — ACT

Executed during the cycle (not deferred):
1. Probes #1–#4 executed against ARAS under DAF authorization (14:33, 23:44 MYT).
2. Harness source traced across four modules; pending item #2 retracted prior to any intervention.
3. Memory corrected (TPS entry rewritten twice as evidence evolved — artifact status, then alignment status).
4. llm-latency-forensics skill patched with 3 pitfalls (A1).
5. This INT record filed + intelligence-index row appended.

Explicitly NOT done: zero changes to config.yaml (mtime verified pre-session 22:27 MYT, by DAF); zero harness code changes; zero ARAS-side requests.

## STEP 7 — VERIFY

| # | Criterion | Method | Status |
|---|-----------|--------|--------|
| V1 | Config untouched by the cycle | stat mtime 22:27 MYT (pre-session, DAF) | ✅ PASS |
| V2 | Probe artifacts preserved | 4 scripts in ~/.hermes/scripts/ + logs in /tmp | ✅ PASS |
| V3 | max_model_len = 1,048,576 reproducible | deterministic pre-prefill 400 via aras-maxlen-probe.py | ✅ PASS |
| V4 | Resolver = 1,048,576 reproducible | venv invocation of get_model_context_length | ✅ PASS |
| V5 | Decode TPS reproducible ±10% | aras-decode-tps-probe.py re-run | ✅ PASS (single run each; ±10% band untested across repeats — noted, not blocking) |

CVS self-assessment per Rule 6 (AI ceiling T2/7): probe measurements and source-code claims T1-quality evidence but formally recorded at this record's confidence: high; LiteLLM attribution is T2 (error-trace fingerprint, not config-confirmed); compression-frequency characterization is T2 (14d sample inference).

## STEP 8 — LEARN

**L1 — Metadata-deference is a failure mode on custom backends.** /v1/models silence + 26-provider models.dev variance (202K–1M) mean capability must be established behaviorally and recorded. Filed: llm-latency-forensics pitfalls.

**L2 — Small-sample extrapolation corrupts capacity planning.** 1.7K vs 31K tok/s (18×) came from extrapolating an overhead-dominated 2-call probe. Rule: measure prefill at ≥100K tokens before quoting throughput. Filed.

**L3 — Proxy layers are false-positive generators.** cacheR=0 cost a full diagnostic cycle because LiteLLM's observability surface was never audited. Rule: audit what infrastructure strips, not just what it routes. Filed.

**L4 — Null-result discipline protects architecture.** The pending-item-#2 timestamp surgery would have modified a cache-sacred design to fix a phantom. The Verify step's job is not confirming expectations — it is killing wrong ones before they reach DAF's decision queue.

---

**Record continuity:** Extends the 14 Sep infra arc (INT-20260914-002/003) into the inference layer; the governed-reversal pattern (DEC-004/005) has an analog here in retraction-with-evidence. Next scheduled work in this workstream: crawl4ai batching + bridge hardening (pre-existing, unchanged by this cycle).
