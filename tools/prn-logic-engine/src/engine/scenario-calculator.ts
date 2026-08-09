// Turnout Scenario Calculator - N24 Senggarang Corrected Analysis

import { Seat, TurnoutScenario, ScenarioProjection, ProjectedVote, PDDProjection, EngineConfig } from '../types.js';

// Default scenarios based on N24 Senggarang corrected analysis (28 June 2026)
// N27 Layang-Layang-specific scenarios (ground truth validation 2026-06-28)
// Key insight: INDIAN VOTE (12.4%) IS KINGMAKER, but HIGHER TURNOUT DOES NOT HELP PH
// Seat is 56.6% Malay-majority — extra turnout = more Malay voters (PN/BN lean)
// PH is UNDERDOG (25-30% win probability). Path requires: (1) Malay split BN vs PN, (2) non-Malay consolidation
// Three-cornered fight (PH Guna, PN Abd Mutalip, BN Chua). BN collapses to 15-25% (Chinese candidate penalty)
// CRITICAL: Abd Mutalip (incumbent, ex-UMNO→PN) vs BN's Chua (MCA, MB officer) = Malay vote fragmentation
// This is OUT OF PH'S HANDS — coin flip. PH cannot manufacture victory via GOTV alone.
export const N27_LAYANG_LAYANG_SCENARIOS: TurnoutScenario[] = [
  {
    id: 'S1',
    name: '2022 Repeat',
    description: 'Standalone State Baseline',
    turnout: 56.4,
    assumptions: [
      'Turnout matches 2022 (56.4%) — realistic standalone state baseline',
      'Indian turnout ~60%, Chinese ~65% (depressed state-only)',
      'Malay vote consolidates behind PN (incumbent advantage)',
      'BN collapses to 18% (Chinese candidate penalty)',
      'PH stalls at 38% (non-Malay base only, no Malay split)'
    ]
  },
  {
    id: 'S2',
    name: 'Realistic Range',
    description: '60-66% Turnout (Most Likely)',
    turnout: 62,
    assumptions: [
      'Turnout 62% — realistic range for July state election (58-66%)',
      'Indian turnout 65-70%, Chinese 70-75%',
      'Malay vote splits: PN 42%, BN 22%, PH 36%',
      'Guna consolidates 70% Indian (not full 75%)',
      'PH loses by narrow margin (underdog scenario)'
    ]
  },
  {
    id: 'S3',
    name: 'Malay Split (PH Wins)',
    description: 'BN-PN Fragmentation Delivers',
    turnout: 64,
    assumptions: [
      'Turnout 64% (upper end of realistic range)',
      'CRITICAL: Malay vote splits 40% PN / 25% BN (or vice versa)',
      'Indian 75%+ consolidation (kingmaker delivers)',
      'Chinese 80%+ turnout (GOTV success)',
      'PH wins with only 39-40% vote share (plurality, not majority)',
      'This is NARROW PATH — depends on BN-PN dynamics, not PH GOTV'
    ]
  },
  {
    id: 'S4',
    name: 'Malay Consolidation (PN Hold)',
    description: 'Incumbent Advantage Holds',
    turnout: 66,
    assumptions: [
      'Turnout 66% (upper bound realistic)',
      'Malay vote consolidates 50%+ behind PN (Abd Mutalip personal vote)',
      'BN stabilizes at 20% (MCA machinery, MB connection)',
      'PH maxes at 35-38% (non-Malay base, limited Malay)',
      'PN wins comfortably despite three-cornered fight'
    ]
  },
  {
    id: 'S5',
    name: 'Low Turnout (BN Surprise)',
    description: 'Core Voters Only',
    turnout: 58,
    assumptions: [
      'Turnout 58% — low end (apathy, no GE coattails)',
      'Core Malay voters turn out (PN/BN advantage)',
      'Non-Malay turnout depressed (PH base stays home)',
      'BN performs better than expected (22-25%)',
      'PN wins, BN second, PH third'
    ]
  },
  {
    id: 'S6',
    name: 'PH Perfect Storm (Unlikely)',
    description: 'Everything Goes Right',
    turnout: 70,
    assumptions: [
      'Turnout 70% — exceptional for standalone state (requires outstation return)',
      'Malay vote splits badly: PN 38%, BN 22%, PH 40%',
      'Indian 80%+ turnout, 75%+ PH (full consolidation)',
      'Chinese 85%+ turnout (GE-level engagement)',
      'Youth (18-30) swing 40%+ to PH',
      'PH wins by thin margin (+400-600 votes)',
      'Probability: 15-20% (optimistic ceiling)'
    ]
  }
];

// N17 Semerah-specific scenarios (ground truth validation 2026-06-28)
// Key insight: 2022's ~60% is REAL baseline for standalone state election (not COVID-depressed)
// PH wins only at 80-85% turnout, which must be MANUFACTURED via targeted Chinese GOTV
export const N17_SEMERAH_SCENARIOS: TurnoutScenario[] = [
  {
    id: 'S1',
    name: '2022 Repeat',
    description: 'Standalone State Baseline',
    turnout: 60.5,
    assumptions: [
      'Turnout matches 2022 (60.5%) - realistic for standalone state election',
      'Chinese turnout remains depressed (45-53% in PDs 14-19)',
      'Malay rural PDs turn out 65-70%',
      'No significant swing from 2022 baseline'
    ]
  },
  {
    id: 'S2',
    name: 'Realistic Baseline',
    description: 'Moderate Recovery',
    turnout: 66,
    assumptions: [
      'Turnout recovers to 66% (upper bound for standalone state)',
      'Chinese turnout improves to 60-65% (partial recovery)',
      'Khuzzan personal vote adds 3-5% in mixed PDs',
      'PN holds 2022 base (8,501 votes)'
    ]
  },
  {
    id: 'S3',
    name: 'Optimistic State',
    description: 'High Turnout (State Election Peak)',
    turnout: 70,
    assumptions: [
      'Turnout reaches 70% (exceptional for standalone state)',
      'Chinese turnout 70%+ in PDs 14-19',
      'Youth mobilization adds 5% in mixed PDs',
      'Federal coattails (Fahmi Fadzil) provide modest boost'
    ]
  },
  {
    id: 'S4',
    name: 'PH Surge + Chinese Recovery',
    description: 'Targeted GOTV Success',
    turnout: 75,
    assumptions: [
      'Overall 75% turnout driven by Chinese PD surge',
      'Chinese-concentration PDs (14-19) hit 75-80% turnout',
      'Khuzzan nostalgia narrative recovers 2018 voters',
      'PN stalls at 28% (fails to exceed 2022 base)'
    ]
  },
  {
    id: 'S5',
    name: 'PN Breakthrough',
    description: 'Malay Split',
    turnout: 70,
    assumptions: [
      'Same 70% turnout as S3',
      'PN exceeds 2022 base (8,501 → 10,500+ votes)',
      'BN Malay vote leaks 8-10% to PN',
      'PH holds Chinese base but Malay vote splits'
    ]
  },
  {
    id: 'S6',
    name: 'PH Victory (GOTV Target)',
    description: 'Manufactured High Turnout',
    turnout: 82,
    assumptions: [
      '82% turnout MANUFACTURED via targeted Chinese GOTV',
      'Chinese-concentration PDs (6,967 voters) hit 85%+ turnout',
      'Mixed PDs (11-13, 20-26) swing 10% to PH on Khuzzan narrative',
      'Rural Malay PDs held at 70% (avoid over-mobilizing BN base)',
      'PN stalls at 25% (fails to expand)',
      'This is the GOTV TARGET, not a forecast - requires focused operation'
    ]
  }
];

// Default scenarios for other seats (N01, N02, N04, N24)
export const DEFAULT_SCENARIOS: TurnoutScenario[] = [
  {
    id: 'S1',
    name: '2022 Repeat',
    description: 'Low Turnout',
    turnout: 59,
    assumptions: [
      'Turnout matches 2022 collapse (59.24%)',
      'Chinese voters remain depressed (2022-style apathy)',
      'Malay voters turn out at moderate levels',
      'No significant swing from 2022 baseline'
    ]
  },
  {
    id: 'S2',
    name: 'Realistic Baseline',
    description: 'Moderate Recovery',
    turnout: 66,
    assumptions: [
      'Turnout recovers to 66% (midpoint for standalone state)',
      'Chinese turnout improves but not to 2018 levels',
      'Youth mobilization adds limited impact (headwind)',
      "Rashid's candidacy energizes PN base moderately"
    ]
  },
  {
    id: 'S3',
    name: 'Optimistic State',
    description: 'High Turnout (State Election Peak)',
    turnout: 70,
    assumptions: [
      'Turnout reaches 70% (upper bound for standalone state)',
      'Chinese turnout recovers to 70-75%',
      'Youth 18-30 turnout exceeds 60%',
      'All three parties mobilize aggressively'
    ]
  },
  {
    id: 'S4',
    name: 'PH Surge',
    description: 'Chinese + Malay Swing',
    turnout: 70,
    assumptions: [
      'Same 70% turnout as S3',
      'Chinese consolidation exceeds 80% in strongholds',
      'Malay moderates in mixed PDs swing 5-7% toward PH',
      "Rashid's candidacy fails to energize PN base"
    ]
  },
  {
    id: 'S5',
    name: 'PN Breakthrough',
    description: 'Malay Split',
    turnout: 70,
    assumptions: [
      'Same 70% turnout as S3/S4',
      'Rashid pulls 32%+ of Malay vote',
      "BN's Malay consolidation fails",
      'PH holds Chinese base but cannot expand beyond'
    ]
  },
  {
    id: 'S6',
    name: 'PH Victory',
    description: 'Perfect Storm',
    turnout: 75,
    assumptions: [
      'Turnout reaches 75% (exceptional for standalone state)',
      'Chinese turnout 80%+ with 85%+ consolidation',
      'Malay moderates swing 10%+ from BN to PH',
      'PN stalls at 22% (fails to expand beyond 2022 base)',
      'Youth 18-30 turnout exceeds 65%'
    ]
  }
];

export const DEFAULT_CONFIG: EngineConfig = {
  baselineTurnout: 66,
  turnoutRange: { min: 64, max: 69 },
  chineseTurnoutFactor: 0.85,
  malayConsolidationFactor: 0.60,
  pnMalayAppeal: 0.28,
  youthTurnoutDiscount: 0.75
};

/**
 * Calculate vote projection for a single scenario
 * Uses seat-specific percentage targets from ground truth validation
 */
export function calculateScenario(
  seat: Seat,
  scenario: TurnoutScenario,
  config: EngineConfig = DEFAULT_CONFIG
): ScenarioProjection {
  const totalVotes = Math.round(seat.totalElectorate * (scenario.turnout / 100));

  // Seat-specific targets (ground truth validation)
  const isN27 = seat.code === 'N27';
  const isN17 = seat.code === 'N17';
  
  let bnPercentage: number;
  let phPercentage: number;
  let pnPercentage: number;
  
  if (isN27) {
    // N27 Layang-Layang calibrated targets (Indian kingmaker dynamic)
    switch (scenario.id) {
      case 'S1': // 2022 Repeat at 56.4%
        bnPercentage = 18.0; phPercentage = 40.0; pnPercentage = 42.0;
        break;
      case 'S2': // Realistic Baseline at 65%
        bnPercentage = 22.0; phPercentage = 42.0; pnPercentage = 36.0;
        break;
      case 'S3': // Competitive Tossup at 70%
        bnPercentage = 20.0; phPercentage = 44.0; pnPercentage = 36.0;
        break;
      case 'S4': // PH Victory (Kingmaker Delivers) at 75%
        bnPercentage = 18.0; phPercentage = 46.0; pnPercentage = 36.0;
        break;
      case 'S5': // PN Breakthrough at 70%
        bnPercentage = 20.0; phPercentage = 35.0; pnPercentage = 45.0;
        break;
      case 'S6': // PH Landslide (Perfect Storm) at 80%
        bnPercentage = 15.0; phPercentage = 50.0; pnPercentage = 35.0;
        break;
      default:
        bnPercentage = 22.0; phPercentage = 42.0; pnPercentage = 36.0;
    }
  } else if (isN17) {
    // N17 Semerah calibrated targets
    switch (scenario.id) {
      case 'S1': // 2022 Repeat at 60.5%
        bnPercentage = 44.8; phPercentage = 22.4; pnPercentage = 30.4;
        break;
      case 'S2': // Realistic Baseline at 66%
        bnPercentage = 44.0; phPercentage = 26.5; pnPercentage = 27.5;
        break;
      case 'S3': // Optimistic State at 70%
        bnPercentage = 43.0; phPercentage = 28.5; pnPercentage = 26.5;
        break;
      case 'S4': // PH Surge + Chinese Recovery at 75%
        bnPercentage = 40.5; phPercentage = 33.0; pnPercentage = 25.0;
        break;
      case 'S5': // PN Breakthrough at 70%
        bnPercentage = 36.5; phPercentage = 29.0; pnPercentage = 32.5;
        break;
      case 'S6': // PH Victory (GOTV Target) at 82%
        bnPercentage = 38.0; phPercentage = 39.5; pnPercentage = 21.0;
        break;
      default:
        bnPercentage = 44.0; phPercentage = 26.5; pnPercentage = 27.5;
    }
  } else {
    // Default targets for other seats (N01, N02, N04, N24)
    switch (scenario.id) {
      case 'S1':
        bnPercentage = 45.0; phPercentage = 25.5; pnPercentage = 24.7;
        break;
      case 'S2':
        bnPercentage = 44.3; phPercentage = 29.4; pnPercentage = 26.3;
        break;
      case 'S3':
        bnPercentage = 43.5; phPercentage = 29.6; pnPercentage = 25.9;
        break;
      case 'S4':
        bnPercentage = 39.9; phPercentage = 33.3; pnPercentage = 25.1;
        break;
      case 'S5': // PN Breakthrough
        bnPercentage = 34.0; phPercentage = 31.5; pnPercentage = 34.5;
        break;
      case 'S6':
        bnPercentage = 36.2; phPercentage = 40.7; pnPercentage = 22.4;
        break;
      default:
        bnPercentage = 44.3; phPercentage = 29.4; pnPercentage = 26.3;
    }
  }

  // Calculate votes from percentages
  let bnVotes = Math.round(totalVotes * (bnPercentage / 100));
  let phVotes = Math.round(totalVotes * (phPercentage / 100));
  let pnVotes = Math.round(totalVotes * (pnPercentage / 100));

  // Adjust to ensure total matches (rounding correction)
  const totalValidVotes = bnVotes + phVotes + pnVotes;
  const adjustment = totalVotes - totalValidVotes;
  pnVotes += adjustment;

  // Determine winner
  const votes = [
    { party: 'BN' as const, count: bnVotes },
    { party: 'PH' as const, count: phVotes },
    { party: 'PN' as const, count: pnVotes }
  ];
  votes.sort((a, b) => b.count - a.count);

  const winner = votes[0].party;
  const margin = votes[0].count - votes[1].count;

  // Get 2022 baseline for swing calculation
  const result2022 = seat.historicalResults.find(r => r.year === 2022);
  const bn2022 = result2022?.results.bn.votes || 9725;
  const ph2022 = result2022?.results.ph.votes || 5813;
  const pn2022 = result2022?.results.pn?.votes || 5624;

  // Calculate PD-level breakdown (simplified - distributes proportionally)
  const pdBreakdown = calculatePDBreakdown(seat, scenario, bnPercentage, phPercentage, pnPercentage);

  return {
    scenario,
    totalVotes: totalValidVotes,
    bn: {
      votes: bnVotes,
      percentage: parseFloat(bnPercentage.toFixed(1)),
      swingFrom2022: parseFloat(((bnVotes - bn2022) / bn2022 * 100).toFixed(1))
    },
    ph: {
      votes: phVotes,
      percentage: parseFloat(phPercentage.toFixed(1)),
      swingFrom2022: parseFloat(((phVotes - ph2022) / ph2022 * 100).toFixed(1))
    },
    pn: {
      votes: pnVotes,
      percentage: parseFloat(pnPercentage.toFixed(1)),
      swingFrom2022: parseFloat(((pnVotes - pn2022) / pn2022 * 100).toFixed(1))
    },
    winner,
    margin,
    pdBreakdown
  };
}

/**
 * Calculate polling district-level projections (simplified proportional distribution)
 */
function calculatePDBreakdown(
  seat: Seat,
  scenario: TurnoutScenario,
  bnPct: number,
  phPct: number,
  pnPct: number
): PDDProjection[] {
  return seat.pollingDistricts.map(pd => {
    // Tier-based turnout adjustment
    const tierAdjustment = pd.tier === 1 ? 5 : pd.tier === 2 ? 0 : -5;
    const pdTurnout = Math.min(95, Math.max(40, scenario.turnout + tierAdjustment));
    const pdVotes = Math.round(pd.electorate * (pdTurnout / 100));

    // Distribute votes proportionally with slight PD-level variation
    const variation = (pd.tier === 1 ? 0 : pd.tier === 2 ? 2 : 4) * (pd.malay > 70 ? 1 : -1);

    const bn = Math.round(pdVotes * ((bnPct + variation) / 100));
    const ph = Math.round(pdVotes * ((phPct - variation/2) / 100));
    const pn = pdVotes - bn - ph;

    return {
      pdCode: pd.code,
      pdName: pd.name,
      turnout: pdTurnout,
      bn,
      ph,
      pn
    };
  });
}

/**
 * Calculate all scenarios for a seat
 */
export function calculateAllScenarios(
  seat: Seat,
  scenarios: TurnoutScenario[] = DEFAULT_SCENARIOS,
  config: EngineConfig = DEFAULT_CONFIG
): ScenarioProjection[] {
  return scenarios.map(scenario => calculateScenario(seat, scenario, config));
}
