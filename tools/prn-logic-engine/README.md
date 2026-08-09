# PRN Logic Engine v0.1

**Johor State Election 2026 - Turnout Scenario Calculator**

## Purpose

Calculate vote projections for Johor PRN 2026 seats based on turnout scenarios, demographic analysis, and ground intelligence.

## Quick Start

```bash
cd tools/prn-logic-engine

# Install dependencies
npm install

# Run calculations for N24 Senggarang
npm run dev -- calculate --seat N24

# List available seats
npm run dev -- list-seats

# List available scenarios
npm run dev -- list-scenarios
```

## Output

Generates two files in `./output/`:
- **Markdown brief** - Human-readable war room brief with scenario matrix, PD-level targets, strategic analysis
- **JSON output** - Machine-readable data for dashboards, APIs, or further processing

## Scenarios

| ID | Name | Turnout | Description |
|----|------|---------|-------------|
| S1 | 2022 Repeat | 59% | Low turnout, Chinese apathy continues |
| S2 | Realistic Baseline | 66% | Moderate recovery (MOST LIKELY) |
| S3 | Optimistic State | 70% | High turnout for standalone state |
| S4 | PH Surge | 70% | Chinese + Malay swing to PH |
| S5 | PN Breakthrough | 70% | Malay split, PN upsets |
| S6 | PH Victory | 75% | Perfect storm for PH |

## Architecture

```
src/
├── cli.ts                    # Command-line interface
├── types.ts                  # TypeScript type definitions
├── data/
│   └── n24-senggarang.ts    # Seat data (PD demographics, candidates, history)
├── engine/
│   └── scenario-calculator.ts # Core calculation logic
└── output/
    └── generator.ts          # Markdown + JSON output generation
```

## Adding New Seats

1. Create `src/data/<seat-code>-<name>.ts` following N24 template
2. Add seat to `cli.ts` seatMap
3. Run `npm run dev -- calculate --seat <CODE>`

## Configuration

Edit `DEFAULT_CONFIG` in `scenario-calculator.ts`:
- `baselineTurnout`: Default turnout percentage
- `chineseTurnoutFactor`: Multiplier for Chinese voter turnout
- `malayConsolidationFactor`: BN Malay retention rate
- `pnMalayAppeal`: PN Malay vote share
- `youthTurnoutDiscount`: Youth turnout discount (they under-turnout)

## Example Output (N24 Senggarang)

```
Scenario Matrix:
─────────────────────────────────────────────────────────────────────────────
ID    | Turnout | BN %   | PH %   | PN %   | Winner | Margin
─────────────────────────────────────────────────────────────────────────────
S1    | 59%       | 45%      | 25.5%      | 24.7%      | BN     | +3533
S2    | 66%       | 44.3%      | 29.4%      | 26.3%      | BN     | +3798
S3    | 70%       | 43.5%      | 29.6%      | 25.9%      | BN     | +3758
S4    | 70%       | 39.9%      | 33.3%      | 25.1%      | BN     | +1785
S5    | 70%       | 34%      | 31.5%      | 34.5%      | PN     | +134
S6    | 75%       | 36.2%      | 40.7%      | 22.4%      | PH     | +1304
─────────────────────────────────────────────────────────────────────────────

Most Likely: BN wins by 3,798 votes (66% turnout)
Confidence: Moderate-High (60-65%)
```

## Classification

**TLP:AMBER** — Operational Use Only. Do not distribute publicly.

## Version History

- **v0.1** (2026-06-28): Initial release with N24 Senggarang corrected analysis
  - Implements 6 turnout scenarios (S1-S6)
  - PD-level projections (Tier 1/2/3)
  - Markdown + JSON output
  - Calibrated to corrected voter roll demographics (60% Malay / 33% Chinese)

## TODO

- [ ] Add remaining 55 Johor seats
- [ ] Integrate with DeerFlow collection pipeline
- [ ] Add real-time turnout tracking (polling day)
- [ ] Dashboard integration (JSON → visualization)
- [ ] Sensitivity analysis automation
- [ ] Historical trend analysis (2008-2022 comparison)

---

**Built for:** Johor PRN 2026 War Room  
**Engine:** Node.js + TypeScript  
**License:** Internal Use Only
