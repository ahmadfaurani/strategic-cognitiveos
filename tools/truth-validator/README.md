# Truth Validator — Automated Claim Verification

## Purpose

Prevents hallucination, factual drift, and conflation of inference with fact in long-form outputs.

## Quick Start

```bash
# Full validation (recommended before any output)
./tools/truth-validator/validate.sh <input-file>

# Extract numerical claims for manual review
./tools/truth-validator/extract-numbers.sh < input.md

# Extract named entities (candidates, parties, constituencies)
./tools/truth-validator/verify-names.sh < input.md
```

## Validation Tiers

| Tier | Claim Type | Requirement |
|------|------------|-------------|
| 1 | Factual (numbers, names, dates, results) | Must cite source file#line |
| 2 | Analytical (calculations, inferences) | Must tag confidence [HIGH/MEDIUM/LOW] |
| 3 | Predictive (scenarios, forecasts) | Must flag as SPECULATION: or SCENARIO: |

## Output Codes

- ✅ **VALIDATION PASSED** — Safe to output
- ⚠️ **VALIDATION PASSED WITH WARNINGS** — Review before output
- ❌ **VALIDATION FAILED** — Fix errors before output

## Common Failures

### Missing Citations
```
✗ MEMORY.md#L999 (line exceeds file length)
✗ MEMORY.md#L123 (file not found)
```
**Fix:** Add proper citations or remove unverified claims.

### Untagged Analytical Claims
```
⚠ 3 analytical claims without confidence tags
```
**Fix:** Add [HIGH], [MEDIUM], or [LOW] to analytical statements.

### Unflagged Predictions
```
⚠ 2 predictive claims without speculation flags
```
**Fix:** Prefix with `SPECULATION:` or `SCENARIO:`.

## Integration

### Pre-Output Hook (Manual)
Run validator before any political brief delivery:
```bash
./tools/truth-validator/validate.sh memory/<brief-file>.md
```

### Heartbeat Integration
Add to daily collection pipeline:
```bash
# After brief generation, before delivery
./tools/truth-validator/validate.sh "$BRIEF_FILE" || exit 1
```

### CI/CD (GitHub Actions)
```yaml
- name: Validate Truth Claims
  run: ./tools/truth-validator/validate.sh memory/*.md
```

## Limitations

- Does not verify external data (news, official results) — manual review required
- Does not check mathematical accuracy of calculations — shows math but doesn't recalculate
- Citation verification only checks file existence and line bounds, not content relevance

## Files

- `validate.sh` — Main validation script
- `extract-numbers.sh` — Extract numerical claims
- `verify-names.sh` — Extract named entities
- `README.md` — This file
