# ElectionData.MY API Integration Guide

**Purpose:** Integrate ElectionData.MY as an authoritative external verification source for the Core Truth Validation System (CVS).

**Status:** ✅ Integrated (2026-06-29)

---

## 🔑 API Key Setup

### Option 1: Environment Variable (Recommended for scripts)

```bash
export ELECTIONDATA_API_KEY=your_api_key_here
```

Add to `~/.bashrc` or `~/.zshrc` for persistence.

### Option 2: Config File (Recommended for shared workspace)

```bash
./tools/truth-validator/electiondata-verify.sh --api-key your_api_key_here
```

This creates `~/.openclaw/workspace/.electiondata-config` with restricted permissions (600).

### Get Your API Key

1. Visit: https://electiondata.my/console
2. Generate API key (instant, free)
3. Copy and configure using one of the methods above

---

## 🛠️ Usage

### Standalone Verification

```bash
# Verify constituency data
./tools/truth-validator/electiondata-verify.sh "N16 Sungai Balang"

# Verify specific year
./tools/truth-validator/electiondata-verify.sh "N17 Semerah" 2022

# Verify Parliament seat
./tools/truth-validator/electiondata-verify.sh "P146 Muar" 2022
```

### Integrated Validation (Automatic)

When validating war-room briefs, ElectionData.MY verification runs automatically:

```bash
./tools/truth-validator/validate.sh memory/n16-sungai-balang-war-room-brief-20260627.md
```

This will:
1. Extract constituency name from the brief
2. Query ElectionData.MY API
3. Cross-reference historical results, candidate names, vote counts
4. Report discrepancies or confirm accuracy

---

## 📊 Integration with CVS

### Tier 1 Claims (Factual)

ElectionData.MY serves as **Source #1** or **Source #2** for multi-source verification:

| Claim Type | Primary Source | Secondary Source |
|------------|---------------|------------------|
| Historical results (2018, 2022) | SPR official | ElectionData.MY API |
| Candidate names | Nomination records | ElectionData.MY API |
| Vote counts, margins | SPR official | ElectionData.MY API |
| Electorate size | SPR official | ElectionData.MY API |
| Turnout percentages | Calculated from SPR | ElectionData.MY API |

### Citation Format

When citing ElectionData.MY in briefs:

```markdown
Source: https://electiondata.my/constituency/N16-sungai-balang
Source: ElectionData.MY API (2026-06-29 query)
```

For API queries with specific parameters:

```markdown
Source: ElectionData.MY API v1, /constituencies?q=N16+Sungai+Balang (2026-06-29)
```

---

## 🔍 Validation Workflow

### Pre-Output Checklist (Updated)

```
[ ] All Tier 1 numbers verified against ≥2 sources?
    ✓ Cross-reference: MEMORY.md + ElectionData.MY API
[ ] All names double-checked (spelling, position, party)?
    ✓ Cross-reference: Nomination records + ElectionData.MY API
[ ] All citations include file#line or URL?
    ✓ External URLs must be fetchable
[ ] Confidence tags applied to Tier 2 claims?
[ ] Tier 3 speculation clearly demarcated?
[ ] Any contradictory evidence considered?
[ ] Math shown explicitly for analytical claims?
```

### Conflict Resolution

If ElectionData.MY conflicts with other sources:

1. **Flag as `[CONFLICTING]`** in the brief
2. **Show both values** with citations
3. **Request human review** if unresolved
4. **Capture feedback** via `feedback-capture.sh`

Example:

```markdown
| Claim | Source A | Source B | Status |
|-------|----------|----------|--------|
| 2022 turnout | 61.8% (MEMORY.md#L142) | 60.5% (ElectionData.MY) | [CONFLICTING] |
```

---

## 📈 API Endpoints (Reference)

Based on ElectionData.MY documentation:

| Endpoint | Purpose | Example |
|----------|---------|---------|
| `/constituencies` | Search constituencies | `?q=N16+Sungai+Balang` |
| `/constituencies/{id}` | Get constituency details | `/N16-sungai-balang` |
| `/elections` | List elections | `?year=2022` |
| `/results` | Get election results | `?constituency=N16&year=2022` |
| `/candidates` | Search candidates | `?name=Selamat+Takim` |

**Note:** Actual endpoint structure may vary. Adjust `electiondata-verify.sh` based on live API testing.

---

## 🧪 Testing

### Test Query

```bash
# Test API connectivity
curl -H "Authorization: Bearer $ELECTIONDATA_API_KEY" \
     -H "Accept: application/json" \
     "https://electiondata.my/api/v1/constituencies?q=N16"
```

### Expected Response

```json
{
  "constituency": {
    "id": "n16-sungai-balang",
    "name": "Sungai Balang",
    "state": "Johor",
    "parliament": "P146 Muar",
    "elections": [...]
  }
}
```

---

## 🔄 Feedback Loop

### When to Capture Feedback

- ElectionData.MY data differs from MEMORY.md
- API returns unexpected format
- Constituency not found in API
- Historical results mismatch

### Capture Command

```bash
./tools/memory-harness/feedback-capture.sh add \
  -f memory/n16-sungai-balang-war-room-brief-20260627.md \
  -c "2022 turnout: 61.8%" \
  -t source \
  -o "61.8% (MEMORY.md)" \
  -n "60.5% (ElectionData.MY)" \
  -s "https://electiondata.my/api/v1/results?constituency=N16&year=2022"
```

---

## 📝 Best Practices

1. **Always cross-reference** — ElectionData.MY is one source, not the definitive source
2. **Cache important queries** — Save API responses for critical constituencies
3. **Document discrepancies** — Use `[CONFLICTING]` tag and capture feedback
4. **Update MEMORY.md** — When ElectionData.MY corrects our data, update the brief
5. **Test before deployment** — Verify API connectivity before running validation gates

---

## 🚨 Troubleshooting

### "No API key found"

```bash
# Check environment variable
echo $ELECTIONDATA_API_KEY

# Or check config file
cat ~/.openclaw/workspace/.electiondata-config
```

### "API call failed"

- Check network connectivity
- Verify API key is valid
- Check ElectionData.MY service status

### "Constituency not found"

- Try alternative naming (e.g., "N16" vs "N16 Sungai Balang")
- Check if constituency exists in database (some new seats may not be added yet)

---

## 📚 Related Documents

- `CVS-MANDATE.md` — Core Truth Validation System mandate
- `validate.sh` — Main validation script
- `TOOLS.md` — Truth Validation Protocol (claim tiers, output format)
- `memory/2026-06-13-political-signal-registry.md` — Signal Registry schema

---

**Integration Date:** 2026-06-29  
**Maintained By:** DAF  
**Next Review:** After first 10 constituency verifications
