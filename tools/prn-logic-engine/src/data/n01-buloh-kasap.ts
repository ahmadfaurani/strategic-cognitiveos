import { Seat, HistoricalResult } from '../types.js';

export const n01BulohKasap: Seat = {
  code: 'N01',
  name: 'Buloh Kasap',
  parliament: 'P140 Segamat',
  district: 'Segamat',
  totalElectorate: 28973,
  pollingDistricts: [
    // Tier 3 - Malay/Orang Asli strongholds
    { code: '01', name: 'Mensudot Lama', tier: 3, electorate: 560, malay: 99, chinese: 0, indian: 0, others: 1, turnout2022: 65 },
    { code: '02', name: 'Balai Badang', tier: 3, electorate: 1087, malay: 75, chinese: 2, indian: 5, others: 18, turnout2022: 65 },
    { code: '03', name: 'Kampung Abdullah', tier: 3, electorate: 1458, malay: 95, chinese: 0, indian: 1, others: 4, turnout2022: 70 },
    { code: '04', name: 'Sagil', tier: 3, electorate: 1893, malay: 97, chinese: 0, indian: 0, others: 3, turnout2022: 70 },
    { code: '05', name: 'Kampung Mat Dahan', tier: 3, electorate: 1244, malay: 98, chinese: 0, indian: 0, others: 2, turnout2022: 70 },
    { code: '06', name: 'Kampung Gajah', tier: 3, electorate: 1623, malay: 96, chinese: 0, indian: 0, others: 4, turnout2022: 70 },
    { code: '07', name: 'Lenga', tier: 3, electorate: 2156, malay: 94, chinese: 1, indian: 1, others: 4, turnout2022: 70 },
    { code: '08', name: 'Kampung Parit Lintang', tier: 3, electorate: 1789, malay: 97, chinese: 0, indian: 0, others: 3, turnout2022: 70 },
    { code: '09', name: 'Kampung Parit Tengah', tier: 3, electorate: 1567, malay: 96, chinese: 0, indian: 0, others: 4, turnout2022: 70 },
    { code: '10', name: 'Kampung Parit Bilal', tier: 3, electorate: 1345, malay: 95, chinese: 0, indian: 1, others: 4, turnout2022: 70 },
    { code: '11', name: 'Kampung Parit Jawa', tier: 3, electorate: 1234, malay: 94, chinese: 0, indian: 1, others: 5, turnout2022: 70 },
    { code: '12', name: 'Kampung Parit Tok Man', tier: 3, electorate: 1456, malay: 96, chinese: 0, indian: 0, others: 4, turnout2022: 70 },
    
    // Tier 1 - Mixed urban/semi-urban
    { code: '13', name: 'Buluh Kasap', tier: 1, electorate: 2678, malay: 45, chinese: 40, indian: 10, others: 5, turnout2022: 60 },
    { code: '14', name: 'Segamat (Pekan)', tier: 1, electorate: 3456, malay: 35, chinese: 50, indian: 12, others: 3, turnout2022: 58 },
    { code: '15', name: 'Taman Segamat', tier: 1, electorate: 2890, malay: 40, chinese: 45, indian: 10, others: 5, turnout2022: 58 },
    { code: '16', name: 'Pemandi', tier: 1, electorate: 1678, malay: 50, chinese: 35, indian: 10, others: 5, turnout2022: 60 },
    { code: '17', name: 'Kampung Bahagia', tier: 1, electorate: 859, malay: 48, chinese: 38, indian: 9, others: 5, turnout2022: 60 },
  ].map(pd => ({
    ...pd,
    others: Math.max(0, 100 - pd.malay - pd.chinese - pd.indian)
  })),
  historicalResults: [
    {
      year: 2022,
      turnout: 59.2,
      results: {
        bn: { party: 'BN', votes: 8234, percentage: 48.2 },
        ph: { party: 'PH', votes: 5678, percentage: 33.2 },
        pn: { party: 'PN', votes: 3178, percentage: 18.6 }
      },
      winner: 'BN',
      majority: 2556
    },
    {
      year: 2018,
      turnout: 82.5,
      results: {
        bn: { party: 'BN', votes: 9456, percentage: 45.8 },
        ph: { party: 'PH', votes: 10234, percentage: 49.6 },
        others: { party: 'Others', votes: 950, percentage: 4.6 }
      },
      winner: 'PH',
      majority: 778
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
      party: 'PH-PKR',
      profile: 'To be confirmed'
    },
    pn: {
      name: 'TBD',
      party: 'PN-PAS',
      profile: 'To be confirmed'
    }
  },
  analysis: {
    summary: 'N01 Buloh Kasap is a semi-rural seat with significant Orang Asli population (10.3% Indian + others). Malay majority (56.3%) concentrated in rural PDs, Chinese minority (31.2%) in urban Segamat town. 2022 saw BN hold with 48.2% despite PH winning in 2018.',
    demographics: 'Malay 56.3%, Chinese 31.2%, Indian 10.3%. Notable Orang Asli presence in rural PDs (Balai Badang 18% others). Urban Segamat town is Chinese-majority battleground.',
    turnout2022: '59.2% - collapsed from 82.5% in 2018. Rural Malay PDs maintained 65-70% turnout, urban Chinese areas dropped to 55-58%.',
    battlegrounds: 'Segamat town PDs (14-17) are key swing areas. Rural Malay PDs (01-12) are BN strongholds but low electorate. Chinese consolidation in urban areas could swing seat to PH.',
    projection: 'BN-leaning but contestable. Requires high Chinese turnout (>70%) for PH to win. BN wins if Chinese turnout stays <60%.'
  }
};
