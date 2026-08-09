// Core type definitions for PRN Logic Engine

export interface PollingDistrict {
  code: string;
  name: string;
  tier: 1 | 2 | 3;
  electorate: number;
  malay: number;      // percentage (0-100)
  chinese: number;    // percentage (0-100)
  indian: number;     // percentage (0-100)
  others: number;     // percentage (0-100)
  turnout2022: number; // percentage (0-100)
}

export interface Seat {
  code: string;           // e.g., "N24"
  name: string;           // e.g., "Senggarang"
  federalCode: string;    // e.g., "P150"
  federalName: string;    // e.g., "Batu Pahat"
  district: string;       // e.g., "Batu Pahat"
  totalElectorate: number;
  pollingDistricts: PollingDistrict[];
  candidates: {
    bn: Candidate;
    ph: Candidate;
    pn: Candidate;
    muda?: Candidate;     // For multi-cornered fights (e.g., N41 Puteri Wangsa)
    bersama?: Candidate;  // For multi-cornered fights
    independent?: Candidate[]; // Multiple independents possible
  };
  historicalResults: HistoricalResult[];
  notes?: string[];       // Additional context (e.g., "Five-cornered fight expected")
}

export interface Candidate {
  name: string;
  coalition: 'BN' | 'PH' | 'PN';
  party: string;
  incumbent: boolean;
  profile: string;
}

export interface HistoricalResult {
  year: number;
  electionType: 'GE' | 'State';
  turnout: number;
  results: {
    bn: VoteShare;
    ph: VoteShare;
    pn?: VoteShare;
    others?: VoteShare;
  };
  winner: 'BN' | 'PH' | 'PN' | 'Others';
  majority: number;
}

export interface VoteShare {
  votes: number;
  percentage: number;
}

export interface TurnoutScenario {
  id: string;           // e.g., "S1"
  name: string;         // e.g., "2022 Repeat"
  description: string;  // e.g., "Low Turnout"
  turnout: number;      // percentage (0-100)
  assumptions: string[];
}

export interface ScenarioProjection {
  scenario: TurnoutScenario;
  totalVotes: number;
  bn: ProjectedVote;
  ph: ProjectedVote;
  pn: ProjectedVote;
  winner: 'BN' | 'PH' | 'PN';
  margin: number;
  pdBreakdown: PDDProjection[];
}

export interface ProjectedVote {
  votes: number;
  percentage: number;
  swingFrom2022: number;
}

export interface PDDProjection {
  pdCode: string;
  pdName: string;
  turnout: number;
  bn: number;
  ph: number;
  pn: number;
}

export interface EngineConfig {
  baselineTurnout: number;      // e.g., 66 (for 66%)
  turnoutRange: {
    min: number;
    max: number;
  };
  chineseTurnoutFactor: number; // multiplier for Chinese turnout vs baseline
  malayConsolidationFactor: number; // BN Malay retention rate
  pnMalayAppeal: number;        // PN Malay vote share
  youthTurnoutDiscount: number; // discount factor for youth (they under-turnout)
}

export interface OutputBrief {
  seat: Seat;
  scenario: ScenarioProjection;
  generatedAt: string;
  classification: string;
  version: string;
}
