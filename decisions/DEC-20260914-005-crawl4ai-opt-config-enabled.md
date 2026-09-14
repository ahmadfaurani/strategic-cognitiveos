---
# === UNIVERSAL BASE ===
id: DEC-20260914-005
record_type: decision
title: "Crawl4ai Intelligence Collection Re-Enabled on Optimized Configuration (opt-v1) — Registry-Driven Collector Deployed, Tiered Cadence Live; Legacy Collector Remains Retired"
created_at: "2026-09-14T16:55:00+00:00"
updated_at: "2026-09-14T16:55:00+00:00"
owner: faurani-jaafar
status: active
priority: medium
sensitivity: confidential
lifecycle_state: candidate
confidence: high
channel: telegram
decision_date: '2026-09-14'
decision_owner: faurani-jaafar
decision_type: structural
decision_weight: medium
tags:
  - domain/intelligence
  - domain/data-infrastructure
  - mission/political-intelligence
  - type/optimization
source:
  type: telegram
  reference: "DAF directive via Telegram direct, 2026-09-14 16:36 UTC (directive sent 16:34, first delivery errored, repeated 16:36): 'Apply optimum spec configuration to enable optimized intelligence collection to crawl4AI'"
summary: "[FACT] DAF decision: crawl4ai-based intelligence collection is re-enabled on the optimum-configuration spec (opt-v1), superseding DEC-20260914-004's retirement for the collection function only. Implemented 16:36-16:50 UTC: (1) sources_registry.json opt-v1 - 25 sources derived from the final legacy manifest (2026-09-14T160403Z), tiered wire (6, P1) / mainstream (9, P2) / analysis (10, P3) with unique slugs, bias/reliability/intel-value carried forward, per-source sitemap pattern slots; (2) collect_optimized.py - one persistent stealth browser session per run (no per-call spin-up), registry-driven selection (--tier/--slugs), deterministic article-link extraction from landing pages with URL-pattern + blacklist filtering, standardized record schema (run_id, slug, source, tier, bias, reliability, language, url, headline, published_at, captured_at UTC+8, dedup_hash sha1(url|headline), engine, method), per-source JSONL telemetry (latency_ms, outcome, error) enabling source-health scoring, check_robots_txt compliance, boilerplate excluded_tags, remove_overlay_elements, 40s per-source timeout, jittered 2-5s inter-source delay, incremental per-source flush (records+telemetry durable against timeout kills); (3) crontab 2 lines live - wire tier every 2h even hours UTC (cap 12/headline), full 25-source at 08:00+20:00 UTC (16:00+04:00 MYT, cap 15), both flock-guarded (/tmp/collect_optimized.lock) + timeout 1800; (4) new sink intelligence/opt/<run_id>/{records,telemetry,manifest}; legacy collector + RETIRED banner unchanged, 92-day archive repo remains corpus of record for the legacy era. Validation: smoke 2/2 sources 10 records 10 unique; full-fleet run showed 15-cap extraction on sinar-harian/malaysiakini/nst, antibot failures persist on bernama-EN/the-star/utusan-malaysia (ACS-GOTO class - proxy pool is the designed fix), bernama-malay + suara-keadilan yield 0 articles (need per-source CSS selectors). Deferred slots built into config: proxy rotation (no pool acquired), per-source selector registry, sitemap discovery (AsyncUrlSeeder probes hung on both test domains from this host - mode behind --sitemap flag with 25s hard timeout, default OFF)."
strategic_significance: "Converts the retired homepage-headline scraper into a structured, deduplicated, telemetry-instrumented collection layer per the optimum spec, with tiered cadence that concentrates frequency on wire sources (10 effective wire passes/day vs legacy 4 full-scope passes). Preserves DEC-20260914-004's hygiene outcome - the legacy pipeline stays retired and archived - while restoring sovereign political-intelligence capability with a clean upgrade path (proxies, selectors, sitemap) for post-CyberDSA hardening."
mission_alignment:
  - mission/political-intelligence
related_records:
  - DEC-20260914-004
  - DEC-20260914-002
  - INIT-20260710-002
# === DECISION FIELDS [Structural] ===
context: "DEC-20260914-004 retired the crawl4ai 25-source political collection at 16:10 UTC after the purpose review found the consumption chain decayed. At 16:27 UTC DAF requested the capability overview and optimum configuration for intelligence data collection; the delivered spec identified the four biggest levers (sitemap discovery, per-source CSS selectors, persistent sessions, proxy rotation) plus tiered freshness and standardized record schema. At 16:36 UTC DAF directed: 'Apply optimum spec configuration to enable optimized intelligence collection to crawl4AI' - re-enabling collection on the new configuration rather than leaving it retired."
decision: "Deploy the optimized collector (opt-v1) and enable scheduled operation: (1) registry-driven collector script with persistent stealth session, deterministic link extraction, standardized deduplicated record schema, per-source JSONL telemetry, robots.txt compliance, and incremental durability; (2) tiered cadence - wire every 2 hours, full fleet twice daily (08:00/20:00 UTC); (3) flock + timeout guards on all cron lines; (4) new opt/ sink separate from the static legacy archive; (5) deferred slots for proxy pool, per-source selectors, and sitemap mode (experimental, default off). Legacy collector remains retired under DEC-20260914-004; this decision supersedes it for the collection function only."
rationale: "The optimum spec converts a homepage-headline scraper into a structured intelligence corpus at modest engineering cost, and DAF explicitly directed application. Tiered cadence concentrates the highest-frequency collection on wire sources where freshness matters most, reducing full-fleet load versus the legacy flat 4x/day. Instrumentation (telemetry, dedup hashes, standardized schema) makes collection quality measurable for the first time. Keeping legacy retired avoids dual-pipeline confusion; the archive repo already preserves that era cleanly."
alternatives_considered:
  - "(a) Keep collection retired until post-CyberDSA freeze lifts - rejected: DAF directed immediate application; the new collector is independent of the frozen GovSec engineering stack."
  - "(b) Revive the legacy collector unchanged - rejected: persists the known failure classes (antibot losses, no dedup, no timestamps) the optimum spec was written to fix."
  - "(c) Block deployment until proxy pool + selectors + sitemap are all ready - rejected: those are enhancement slots, not prerequisites; the deployed config already improves structure, dedup, telemetry, and cadence, and each slot upgrades independently."
confirmed_by: faurani-jaafar
confirmed_at: '2026-09-14T16:36:00+00:00'
---

# Context

Following DEC-20260914-004 (collection retired 16:10 UTC), DAF requested the capability overview and optimum configuration for intelligence collection (16:27 UTC). The delivered spec identified: persistent stealth sessions (vs per-call browser spin-up), sitemap-driven discovery, per-source CSS extraction, proxy rotation, tiered freshness (wire/mainstream/analysis), standardized deduplicated record schema, and JSONL telemetry. At 16:36 UTC DAF directed: "Apply optimum spec configuration to enable optimized intelligence collection to crawl4AI."

# Decision

Deploy and enable the optimized configuration (opt-v1). Executed 16:36-16:50 UTC:

- **`sources_registry.json` (opt-v1):** 25 sources derived from the final legacy manifest (`2026-09-14T160403Z`) — wire tier 6 (P1), mainstream 9 (P2), analysis 10 (P3); unique slugs; bias/reliability/intel-value carried forward; sitemap-pattern and selector slots per source.
- **`collect_optimized.py`:** single persistent stealth browser session per run; registry-driven selection (`--tier`/`--slugs`); deterministic article-link extraction (URL-pattern match + blacklist filter) from landing pages; standardized records — `run_id, slug, source, tier, bias, reliability, language, url, headline, published_at, captured_at (UTC+8), dedup_hash (sha1 url|headline), engine, method`; per-source JSONL telemetry (`latency_ms, outcome, error`) for source-health scoring; `check_robots_txt=True`; boilerplate `excluded_tags` + overlay removal; 40s per-source timeout; jittered 2-5s inter-source delay; **incremental per-source flush** (records + telemetry durable against timeout kills; manifest written on clean completion only).
- **Crontab (2 lines live):** wire tier every 2h at even hours UTC (cap 12); full 25-source fleet at 08:00 + 20:00 UTC = 16:00 + 04:00 MYT (cap 15); both `flock -n /tmp/collect_optimized.lock` + `timeout 1800` guarded. Legacy 4-line cadence not restored.
- **Sink:** `~/.openclaw/workspace-hoi/intelligence/opt/<run_id>/` — `records.jsonl`, `telemetry.jsonl`, `manifest.json`. Legacy sink stays static; archive repo remains corpus of record for 14 Jun - 14 Sep.
- **Validation:** smoke run 2/2 sources, 10 records, 10 unique (~3s/source). First full-fleet run was killed by its own 540s watch at source ~8 (motivating the incremental-flush patch); partial results: 15-cap extraction on sinar-harian/malaysiakini/nst; antibot failures on bernama-EN/the-star/utusan-malaysia (ACS-GOTO class, same as legacy era); 0-article yields on bernama-malay/suara-keadilan. Clean full-fleet validation run (timeout 900) launched 16:49 UTC, incremental flush live.
- **Deferred slots (configurable, not blockers):** proxy rotation (`proxy_config` slot present, no pool acquired yet — the designed fix for the antibot class); per-source CSS selector registry (fixes 0-article sources, enables true `published_at`); sitemap discovery via `AsyncUrlSeeder` — probes hung on both test domains from this host, so mode sits behind `--sitemap` with a 25s hard per-source timeout, default OFF.

# Rationale

DAF directed application of the optimum spec. The deployed configuration delivers the structural improvements (dedup, schema, telemetry, persistent session, tiered cadence) immediately, while proxy/selectors/sitemap are staged as independent upgrade slots rather than prerequisites — each can land without redeployment. Tiered cadence concentrates frequency where freshness matters (wire) and reduces full-fleet churn versus the legacy flat schedule.

# Alternatives Considered

- Keep retired until post-CyberDSA — rejected: explicit DAF directive; new collector is independent of the frozen GovSec engineering stack.
- Revive legacy unchanged — rejected: persists known failure classes the spec fixes.
- Block on full spec completion (proxies + selectors + sitemap) — rejected: enhancement slots upgrade independently; deployed config already improves structure, dedup, telemetry, cadence.

# Confirmation

DAF, Telegram direct, 14 September 2026 16:36 UTC (directive first sent 16:34, delivery errored, repeated 16:36).
