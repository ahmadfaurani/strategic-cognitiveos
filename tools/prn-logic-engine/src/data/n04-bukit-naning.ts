import { Seat, HistoricalResult } from '../types.js';

export const n04BukitNaning: Seat = {
  code: 'N04',
  name: 'Bukit Naning',
  parliament: 'P145 Bakri',
  district: 'Muar',
  totalElectorate: 23002,
  pollingDistricts: [
    // Tier 3 - Malay rural strongholds
    { code: '01', name: 'Kampung Parit Bunga', tier: 3, electorate: 1876, malay: 88, chinese: 5, indian: 1, others: 6, turnout2022: 70 },
    { code: '02', name: 'Kampung Parit Tengah', tier: 3, electorate: 2134, malay: 92, chinese: 3, indian: 1, others: 4, turnout2022: 70 },
    { code: '03', name: 'Kampung Parit Jawa', tier: 3, electorate: 1987, malay: 90, chinese: 4, indian: 1, others: 5, turnout2022: 70 },
    { code: '04', name: 'Kampung Sungai Balang', tier: 3, electorate: 2345, malay: 94, chinese: 2, indian: 0, others: 4, turnout2022: 70 },
    { code: '05', name: 'Kampung Parit Tok Man', tier: 3, electorate: 2156, malay: 91, chinese: 3, indian: 1, others: 5, turnout2022: 70 },
    { code: '06', name: 'Kampung Parit Lintang', tier: 3, electorate: 1789, malay: 89, chinese: 5, indian: 1, others: 5, turnout2022: 70 },
    { code: '07', name: 'Kampung Bukit Naning', tier: 3, electorate: 2567, malay: 87, chinese: 6, indian: 1, others: 6, turnout2022: 70 },
    
    // Tier 1 - Mixed urban/semi-urban
    { code: '08', name: 'Bukit Naning (Pekan)', tier: 1, electorate: 3456, malay: 42, chinese: 48, indian: 5, others: 5, turnout2022: 60 },
    { code: '09', name: 'Taman Bukit Naning', tier: 1, electorate: 2890, malay: 38, chinese: 52, indian: 5, others: 5, turnout2022: 58 },
    { code: '10', name: 'Kampung Baharu', tier: 1, electorate: 1802, malay: 52, chinese: 38, indian: 6, others: 4, turnout2022: 62 },
  ].map(pd => ({
    ...pd,
    others: Math.max(0, 100 - pd.malay - pd.chinese - pd.indian)
  })),
  historicalResults: [
    {
      year: 2022,
      turnout: 58.7,
      results: {
        bn: { party: 'BN-UMNO', votes: 7234, percentage: 53.2 },
        ph: { party: 'PH-DAP', votes: 4567, percentage: 33.6 },
        pn: { party: 'PN-PAS', votes: 1789, percentage: 13.2 }
      },
      winner: 'BN',
      majority: 2667
    },
    {
      year: 2018,
      turnout: 81.3,
      results: {
        bn: { party: 'BN-UMNO', votes: 8456, percentage: 47.8 },
        ph: { party: 'PH-DAP', votes: 8923, percentage: 50.4 },
        others: { party: 'Others', votes: 318, percentage: 1.8 }
      },
      winner: 'PH',
      majority: 467
    }
  ],
  candidates: {
    bn: {
      name: 'TBD',
      party: 'BN-UMNO',
      profile: 'To be confirmed'
    },
    ph: {
      name: 'TBD',
      party: 'PH-DAP',
      profile: 'To be confirmed'
    },
    pn: {
      name: 'TBD',
      party: 'PN-PAS',
      profile: 'To be confirmed'
    }
  },
  analysis: {
    summary: 'N04 Bukit Naning is a Malay-majority (63.6%) seat with large Chinese minority (34.5%). Classic urban-rural split: rural Malay PDs (01-07) vs Chinese-majority urban areas (08-09). 2018 PH won by 467 votes with 81.3% turnout; 2022 collapse gave BN 2,667 majority.',
    demographics: 'Malay 63.6%, Chinese 34.5%, Indian 0.9%. Rural PDs 01-07 are 87-94% Malay (BN strongholds). Urban PDs 08-09 are 48-52% Chinese (PH strongholds). PD 10 is competitive mixed area.',
    turnout2022: '58.7% - collapsed from 81.3% in 2018. Chinese turnout depression decisive factor. Rural Malay maintained 65-70%, urban Chinese areas dropped to 55-58%.',
    battlegrounds: 'Urban PDs 08-09 (6,346 voters total) are PH base but need 75%+ Chinese turnout. PD 10 (Kampung Baharu) is swing area. Rural PDs 01-07 (14,854 voters) are BN fortress but low elasticity.',
    projection: 'BN-leaning but highly turnout-sensitive. PH needs 75%+ overall turnout with Chinese consolidation to win. BN wins comfortably if turnout stays <65%.'
  }
};
