/**
 * NXX SEAT NAME — PKR War Room Data File
 * 
 * Classification: TLP:AMBER — Operational Use Only
 * Source: Excel intelligence (as of 19 June 2026)
 * Last Updated: YYYY-MM-DD
 * 
 * Parliament: P.XXX PARLIAMENT_NAME
 * Total Electorate: XX,XXX
 * Demographics: Malay XX.X% / Chinese XX.X% / Indian X.X%
 * 
 * Tiers:
 * - Tier 1 (Kingmaker/Chinese Base): X PDs, XX% voters
 * - Tier 2 (Mixed): X PDs, XX% voters
 * - Tier 3 (Malay Heartland): X PDs, XX% voters
 */

import { Seat } from '../types.js';

export const nXXSeatName: Seat = {
  code: 'NXX',
  name: 'Seat Name',
  federalCode: 'P.XXX',
  federalName: 'PARLIAMENT_NAME',
  district: 'District Name',
  totalElectorate: XXXXX,
  
  pollingDistricts: [
    // Tier 1 - Kingmaker/Chinese Base (<40% Malay, >50% Chinese/Indian)
    // PH MUST-WIN ZONES - Target 80-85% turnout
    { 
      code: '01', 
      name: 'PD Name', 
      tier: 1, 
      electorate: XXXX, 
      malay: XX.X, 
      chinese: XX.X, 
      indian: X.X, 
      others: X.X, 
      turnout2022: XX 
    },
    // ... add all Tier 1 PDs
    
    // Tier 2 - Mixed (40-75% Malay)
    // CONTESTABLE - Persuasion targets
    { 
      code: 'XX', 
      name: 'PD Name', 
      tier: 2, 
      electorate: XXXX, 
      malay: XX.X, 
      chinese: XX.X, 
      indian: X.X, 
      others: X.X, 
      turnout2022: XX 
    },
    // ... add all Tier 2 PDs
    
    // Tier 3 - Malay Heartland (>75% Malay)
    // BN/PN FIREWALL - Damage limit, don't over-invest
    { 
      code: 'XX', 
      name: 'PD Name', 
      tier: 3, 
      electorate: XXXX, 
      malay: XX.X, 
      chinese: X.X, 
      indian: X.X, 
      others: X.X, 
      turnout2022: XX 
    },
    // ... add all Tier 3 PDs
  ].map(pd => ({
    // Auto-calculate 'others' to ensure percentages sum to 100
    ...pd,
    others: Math.max(0, 100 - pd.malay - pd.chinese - pd.indian)
  })),
  
  candidates: {
    bn: {
      name: 'Candidate Full Name',
      coalition: 'BN',
      party: 'UMNO/MCA/MIC',
      incumbent: true/false,
      profile: 'Detailed profile with strengths, vulnerabilities, campaign narrative, community networks'
    },
    ph: {
      name: 'Candidate Full Name',
      coalition: 'PH',
      party: 'PKR/DAP/AMANAH',
      incumbent: true/false,
      profile: 'Detailed profile with strengths, vulnerabilities, campaign narrative, federal backing'
    },
    pn: {
      name: 'Candidate Full Name',
      coalition: 'PN',
      party: 'PAS/Bersatu',
      incumbent: true/false,
      profile: 'Detailed profile with strengths, vulnerabilities, campaign narrative, local embeddedness'
    },
    // Optional: for multi-cornered fights (e.g., N41 Puteri Wangsa)
    muda: {
      name: 'Candidate Full Name',
      coalition: 'MUDA',
      party: 'MUDA',
      incumbent: true/false,
      profile: 'Profile details'
    },
    bersama: {
      name: 'Candidate Full Name',
      coalition: 'Bersama',
      party: 'Parti Bersama',
      incumbent: false,
      profile: 'Profile details'
    }
  },
  
  historicalResults: [
    {
      year: 2022,
      electionType: 'State',
      turnout: XX.X,
      results: {
        bn: { 
          party: 'BN-UMNO', 
          votes: XXXXX, 
          percentage: XX.X 
        },
        ph: { 
          party: 'PH-PKR', 
          votes: XXXXX, 
          percentage: XX.X 
        },
        pn: { 
          party: 'PN-PAS', 
          votes: XXXXX, 
          percentage: XX.X 
        }
      },
      winner: 'BN',
      majority: XXXX
    },
    {
      year: 2018,
      electionType: 'GE',
      turnout: XX.X,
      results: {
        bn: { 
          party: 'BN-UMNO', 
          votes: XXXXX, 
          percentage: XX.X 
        },
        ph: { 
          party: 'PH-PKR', 
          votes: XXXXX, 
          percentage: XX.X 
        }
      },
      winner: 'PH',
      majority: XXX
    }
  ],
  
  // Optional: contextual notes for multi-cornered fights, special dynamics
  notes: [
    'Five-cornered fight expected (PH, BN, MUDA, Bersama, Independent)',
    'Incumbent NOT defending',
    'Federal minister deploying heavyweight candidate',
    // ... add relevant notes
  ]
};

/**
 * SEAT ANALYSIS SUMMARY
 * 
 * Use this section for detailed analysis that informs the war room brief.
 * This is read by the output generator to create the markdown brief.
 */
export const analysis = {
  /**
   * One-paragraph executive summary
   */
  summary: 'NXX Seat Name is a XX,XXX-voter [demographic description] seat. 2018: [result] at XX% turnout. 2022: [result] at XX% turnout. CRITICAL: [key insight about vote split, turnout dynamics, or demographic reality].',
  
  /**
   * Demographic breakdown with strategic implications
   */
  demographics: 'Malay XX.X% (XX,XXX), Chinese XX.X% (XX,XXX), Indian X.X% (X,XXX). Youth 18-30: XX.X% (XX,XXX). Tier-1 PDs (X PDs, XX% voters) are [description]. Tier-2 PDs (X PDs, XX% voters) are [description]. Tier-3 PDs (X PDs, XX% voters) are [description]. WARNING: [critical demographic insight].',
  
  /**
   * Turnout reality check — baseline vs targets
   */
  turnout2022: 'XX.X% — [realistic baseline description]. 2018\'s XX% rode [GE coattails/special circumstances]. July 2026 is state-only → natural turnout XX-XX%. [Critical insight: does higher turnout help PH or hurt?].',
  
  /**
   * Battleground PDs — where the election is won/lost
   */
  battlegrounds: '[Tier-1 PD names] (X,XXX voters, XX% of seat) are PH ceiling — 2022 turnout XX-XX%, need XX%+ to compete. [Tier-3 PD names] (XX,XXX voters) are BN firewall — must hold at XX%+ turnout. [Mixed PDs] are swing zones where [candidate]\'s personal vote matters.',
  
  /**
   * Projection with win probability
   */
  projection: '[BN/PH/PN]-leaning (XX-XX% probability). Baseline S2 (XX% turnout): [coalition] +X,XXX. PH upset requires [specific conditions: manufactured turnout, vote split, consolidation]. [Priority level: main battleground/upside seat/defensive/monitoring]. [Resource allocation guidance].'
};
