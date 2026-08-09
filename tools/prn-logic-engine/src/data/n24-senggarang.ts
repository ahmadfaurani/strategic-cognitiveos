// N24 Senggarang seat data - corrected per 28 June 2026 voter roll verification

import { Seat, HistoricalResult, PollingDistrict } from '../types.js';

export const n24Senggarang: Seat = {
  code: 'N24',
  name: 'Senggarang',
  federalCode: 'P150',
  federalName: 'Batu Pahat',
  district: 'Batu Pahat',
  totalElectorate: 38629,
  pollingDistricts: [
    // Tier 1 (50.8% of electorate) - Mixed/Competitive
    // Scaled from 41238 total to 38629 (factor: 0.937)
    { code: '001', name: 'Banang', tier: 1, electorate: 4872, malay: 47, chinese: 45, indian: 5, others: 3, turnout2022: 55 },
    { code: '002', name: 'Minyak Beku', tier: 1, electorate: 3560, malay: 45, chinese: 52, indian: 2, others: 1, turnout2022: 60 },
    { code: '003', name: 'Kampung Bahru', tier: 1, electorate: 3870, malay: 76, chinese: 18, indian: 4, others: 2, turnout2022: 70 },
    { code: '004', name: 'Taman Senggarang', tier: 1, electorate: 3279, malay: 70, chinese: 25, indian: 3, others: 2, turnout2022: 65 },
    { code: '005', name: 'BSE Timor', tier: 1, electorate: 2811, malay: 55, chinese: 40, indian: 3, others: 2, turnout2022: 65 },
    
    // Tier 2 (26.9% of electorate)
    { code: '006', name: 'Sungai Suloh', tier: 2, electorate: 2623, malay: 58, chinese: 38, indian: 2, others: 2, turnout2022: 60 },
    { code: '007', name: 'Petani Kechik', tier: 2, electorate: 2061, malay: 35, chinese: 62, indian: 2, others: 1, turnout2022: 55 },
    { code: '008', name: 'Sungai Ayam', tier: 2, electorate: 2436, malay: 46, chinese: 45, indian: 6, others: 3, turnout2022: 55 },
    { code: '009', name: 'Koris', tier: 2, electorate: 2717, malay: 60, chinese: 35, indian: 3, others: 2, turnout2022: 65 },
    { code: '010', name: 'Sungai Lurus', tier: 2, electorate: 2342, malay: 72, chinese: 24, indian: 2, others: 2, turnout2022: 70 },
    
    // Tier 3 (22.3% of electorate) - Rural Malay
    { code: '011', name: 'Parit Kadir', tier: 3, electorate: 1967, malay: 85, chinese: 10, indian: 3, others: 2, turnout2022: 75 },
    { code: '012', name: 'Parit Kemang', tier: 3, electorate: 1780, malay: 88, chinese: 8, indian: 2, others: 2, turnout2022: 75 },
    { code: '013', name: 'Parit Tariman', tier: 3, electorate: 1686, malay: 86, chinese: 9, indian: 3, others: 2, turnout2022: 75 },
    { code: '014', name: 'Senggarang', tier: 3, electorate: 1593, malay: 90, chinese: 6, indian: 2, others: 2, turnout2022: 70 },
    { code: '015', name: 'BSE Barat', tier: 3, electorate: 1037, malay: 35, chinese: 61, indian: 2, others: 2, turnout2022: 65 },
  ].map(pd => ({
    ...pd,
    others: Math.max(0, 100 - pd.malay - pd.chinese - pd.indian)
  })),
  candidates: {
    bn: {
      name: 'Mohd Yusla Ismail',
      coalition: 'BN',
      party: 'UMNO',
      incumbent: true,
      profile: 'Incumbent ADUN, won 2022'
    },
    ph: {
      name: 'Onn Abu Bakar',
      coalition: 'PH',
      party: 'PKR',
      incumbent: false,
      profile: 'Current Batu Pahat MP'
    },
    pn: {
      name: 'Datuk Mohd Rashid Hasnon',
      coalition: 'PN',
      party: 'Bersatu',
      incumbent: false,
      profile: 'Former Batu Pahat MP (2013-2022) + Former Deputy Speaker of Parliament. Defector (PKR→Bersatu 2018). Known local figure with strong name recognition. Campaign: Malay consolidation, cost-of-living, defector narrative vulnerability. Strengths: Parliamentary track record, local familiarity, PN machinery. Vulnerability: "Party hopper" narrative, must convince electorate of sincerity.'
    }
  },
  historicalResults: [
    {
      year: 2022,
      electionType: 'State',
      turnout: 59.24,
      results: {
        bn: { votes: 9725, percentage: 45.11 },
        ph: { votes: 5813, percentage: 26.97 },
        pn: { votes: 5624, percentage: 26.09 }
      },
      winner: 'BN',
      majority: 3912
    },
    {
      year: 2018,
      electionType: 'GE',
      turnout: 85.16,
      results: {
        bn: { votes: 10234, percentage: 45.8 },
        ph: { votes: 11043, percentage: 49.3 },
        pn: { votes: 1089, percentage: 4.9 }
      },
      winner: 'PH',
      majority: 809
    },
    {
      year: 2013,
      electionType: 'GE',
      turnout: 88.0,
      results: {
        bn: { votes: 14521, percentage: 56.2 },
        ph: { votes: 11496, percentage: 43.8 }
      },
      winner: 'BN',
      majority: 1855
    },
    {
      year: 2008,
      electionType: 'GE',
      turnout: 78.26,
      results: {
        bn: { votes: 11234, percentage: 54.1 },
        ph: { votes: 8206, percentage: 45.9 }
      },
      winner: 'BN',
      majority: 3028
    }
  ] as HistoricalResult[]
};

// Validate electorate sum
const pdSum = n24Senggarang.pollingDistricts.reduce((sum, pd) => sum + pd.electorate, 0);
console.assert(
  Math.abs(pdSum - n24Senggarang.totalElectorate) < 100,
  `PD electorate sum (${pdSum}) doesn't match total (${n24Senggarang.totalElectorate})`
);
