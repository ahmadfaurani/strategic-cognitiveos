# Truth Validation — Quick Start

## Engineered for Success: Multi-Source Verification + Confidence Assertion

---

## 🎯 Objective

**Never rely on a single source.** All factual claims must be cross-referenced from ≥2 validated sources before output, with explicit Confidence Assertion tags.

---

## 📋 Workflow

### 1. **Fetch Sources** (Before Writing)

```bash
# Fetch from all Tier 0–1 sources
./tools/source-registry/fetch-all.sh
```

### 2. **Cross-Reference Claims** (During Writing)

```bash
# Verify a specific claim
./tools/truth-validator/crossref.sh result "N17 Semerah 2022"
./tools/truth-validator/crossref.sh candidate "N33 Tenggaroh"
```

### 3. **Validate Output** (Before Delivery)

```bash
# Full validation (mandatory)
./tools/truth-validator/validate.sh memory/<brief-file>.md
```

**Must pass:**
- ✅ All factual claims have Confidence Assertion tags
- ✅ ≥2 sources for Tier 1 claims
- ✅ Analytical claims tagged [HIGH/MEDIUM/LOW]
- ✅ Predictive claims flagged SPECULATION: or SCENARIO:

### 4. **Log Feedback** (After Delivery — Loop 3)

```bash
# If validator missed something or flagged incorrectly
./tools/truth-validator/feedback-log.sh \
  --type false-negative \
  --file n17-brief.md \
  --issue "Wrong vote count" \
  --severity HIGH \
  --notes "Should be 4,041 not 4,014"
```

### 5. **Monthly Review** (Loop 4)

```bash
# First of each month
./tools/truth-validator/monthly-review.sh
```

Generates report, identifies patterns, recommends rule updates.

---

## 🏷️ Confidence Assertion Tags

| Tag | When to Use |
|-----|-------------|
| `[VERIFIED]` | ≥2 sources (≥1 Tier 0–1), converged |
| `[CORROBORATED]` | ≥2 Tier 1–2 sources, converged |
| `[SINGLE-SOURCE]` | Only 1 source available |
| `[CONFLICTING]` | Sources disagree — human review required |
| `[UNVERIFIED]` | Tier 3 only or no sources |

---

## 📊 Source Tiers

| Tier | Type | Weight | Examples |
|------|------|--------|----------|
| 0 | Official | 1.0 | SPR, official candidate lists |
| 1 | Established Media | 0.8 | Malaysiakini, The Star, NST, FMT |
| 2 | Secondary Media | 0.6 | Sinar Harian, Malaysian Insight |
| 3 | Social/Unverified | 0.3 | Twitter, Telegram |
| 4 | Internal Memory | 0.5 | MEMORY.md (derived data) |

---

## 🚨 Validation Gates

**Before any brief leaves the queue:**

```bash
./tools/truth-validator/validate.sh <file> || exit 1
```

**Exit codes:**
- `0` — Passed (safe to output)
- `1` — Failed (fix before output)

---

## 📁 File Structure

```
tools/
├── source-registry/
│   ├── sources.yaml          # Source tier definitions
│   ├── fetch-spr.sh          # Tier 0 fetch
│   ├── fetch-mkini.sh        # Tier 1 fetch
│   └── fetch-all.sh          # Run all fetches
└── truth-validator/
    ├── validate.sh           # Main validator
    ├── crossref.sh           # Cross-reference engine
    ├── feedback-log.sh       # Loop 3 feedback
    ├── monthly-review.sh     # Loop 4 improvement
    └── QUICKSTART.md         # This file
```

---

## 🔁 Loop Engineering

```
Loop 1: Generate brief
   ↓
Loop 2: Auto-validate (validate.sh + crossref.sh)
   ↓
Loop 3: Human feedback (feedback-log.sh)
   ↓
Loop 4: Monthly review → Update rules (monthly-review.sh)
   ↓
(Back to Loop 1 — improved system)
```

---

## Related

- `tools/source-registry/README.md` — Detailed source documentation
- `TOOLS.md` — Truth Validation Protocol
- `HEARTBEAT.md` — Pipeline integration
