# Source Registry — Multi-Source Verification

## Purpose

Enable **Confidence Assertion** by cross-referencing claims across multiple validated sources before output.

## Source Tier Hierarchy

| Tier | Type | Examples | Weight | Use Case |
|------|------|----------|--------|----------|
| **0** | Official Primary | SPR, official candidate lists | 1.0 | Election results, demographics |
| **1** | Established Media | Malaysiakini, The Star, NST, FMT, Bernama | 0.8 | Real-time news, analysis |
| **2** | Secondary Media | Sinar Harian, Harian Metro, Malaysian Insight | 0.6 | Local coverage, regional context |
| **3** | Social/Unverified | Twitter, Telegram, Facebook | 0.3 | Tips only — must verify with Tier 0–2 |
| **4** | Internal Memory | MEMORY.md, signal registry | 0.5 | Derived data — refresh against Tier 0–1 |

## Confidence Assertion Tags

| Tag | Requirement | Meaning |
|-----|-------------|---------|
| `[VERIFIED]` | ≥2 sources (≥1 Tier 0–1), converged | Highest confidence |
| `[CORROBORATED]` | ≥2 Tier 1–2 sources, converged | Strong confidence |
| `[SINGLE-SOURCE]` | Only 1 source | Use with caution |
| `[CONFLICTING]` | Sources disagree | Human review required |
| `[UNVERIFIED]` | Tier 3 only or no sources | Do not rely on |

## Quick Start

```bash
# Fetch from all Tier 0–1 sources
./tools/source-registry/fetch-all.sh

# Cross-reference a specific claim
./tools/truth-validator/crossref.sh candidate "N17 Semerah"
./tools/truth-validator/crossref.sh result "N17 Semerah 2022"

# Validate a brief (enforces multi-source + Confidence Assertion)
./tools/truth-validator/validate.sh memory/n17-semerah-brief.md
```

## Fetch Scripts

| Script | Source | Status |
|--------|--------|--------|
| `fetch-spr.sh` | SPR Official (Tier 0) | ✅ Ready (placeholder) |
| `fetch-mkini.sh` | Malaysiakini (Tier 1) | ✅ Ready |
| `fetch-thestar.sh` | The Star (Tier 1) | ⏳ TODO |
| `fetch-nst.sh` | NST (Tier 1) | ⏳ TODO |
| `fetch-fmt.sh` | FMT (Tier 1) | ⏳ TODO |
| `fetch-bernama.sh` | Bernama (Tier 1) | ⏳ TODO |

## Verification Rules

1. **Tier 1 Claims (Factual):** Require ≥2 sources from Tier 0–2, with at least one Tier 0–1
2. **Tier 2 Claims (Analytical):** Require ≥1 Tier 1–2 source + explicit reasoning
3. **Tier 3 Claims (Predictive):** Flag as `SPECULATION:` or `SCENARIO:` regardless of source
4. **Conflicting Sources:** If Tier 0 conflicts with Tier 1, prefer Tier 0. If Tier 1 vs Tier 1, flag `[CONFLICTING]`
5. **Stale Data:** Any claim >30 days old must be re-verified or tagged `[STALE]`

## Confidence Assertion Formula

```
Confidence = Source Quality × Convergence × Recency

Where:
- Source Quality = Max tier of sources used (0.3–1.0)
- Convergence = 1.0 if ≥2 sources agree, 0.6 if single source, 0.3 if conflicting
- Recency = 1.0 if <7 days old, 0.8 if <30 days, 0.5 if older
```

## Files

- `sources.yaml` — Source registry with tier ratings
- `fetch-*.sh` — Fetch scripts for each source
- `fetch-all.sh` — Run all fetches in parallel
- `README.md` — This file

## Related

- `tools/truth-validator/` — Validation and cross-reference engines
- `HEARTBEAT.md` — Integration into daily collection pipeline
