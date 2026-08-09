import { Seat, HistoricalResult } from '../types.js';

export const n02Pemanis: Seat = {
  code: 'N02',
  name: 'Pemanis',
  parliament: 'P141 Sekijang',
  district: 'Segamat',
  totalElectorate: 30458,
  pollingDistricts: [
    // Tier 3 - Malay rural strongholds
    { code: '01', name: 'Kampung Gugur', tier: 3, electorate: 1876, malay: 92, chinese: 2, indian: 1, others: 5, turnout2022: 70 },
    { code: '02', name: 'Kampung Parit Bilal', tier: 3, electorate: 2134, malay: 95, chinese: 1, indian: 0, others: 4, turnout2022: 70 },
    { code: '03', name: 'Kampung Parit Tengah', tier: 3, electorate: 1987, malay: 94, chinese: 1, indian: 1, others: 4, turnout2022: 70 },
    { code: '04', name: 'Kampung Parit Jawa', tier: 3, electorate: 2345, malay: 96, chinese: 0, indian: 0, others: 4, turnout2022: 70 },
    { code: '05', name: 'Kampung Parit Tok Man', tier: 3, electorate: 2156, malay: 95, chinese: 1, indian: 0, others: 4, turnout2022: 70 },
    { code: '06', name: 'Kampung Parit Lintang', tier: 3, electorate: 1789, malay: 93, chinese: 2, indian: 1, others: 4, turnout2022: 70 },
    { code: '07', name: 'Kampung Sungai Mati', tier: 3, electorate: 2567, malay: 91, chinese: 3, indian: 1, others: 5, turnout2022: 70 },
    { code: '08', name: 'Kampung Parit Setongkat', tier: 3, electorate: 1654, malay: 94, chinese: 1, indian: 1, others: 4, turnout2022: 70 },
    
    // Tier 1 - Mixed areas
    { code: '09', name: 'Batu Anam', tier: 1, electorate: 3456, malay: 45, chinese: 42, indian: 8, others: 5, turnout2022: 60 },
    { code: '10', name: 'Pemanis (Pekan)', tier: 1, electorate: 2890, malay: 48, chinese: 40, indian: 7, others: 5, turnout2022: 60 },
    { code: '11', name: 'Taman Pemanis', tier: 1, electorate: 2678, malay: 42, chinese: 45, indian: 8, others: 5, turnout2022: 58 },
    { code: '12', name: 'Kampung Baharu', tier: 1, electorate: 1789, malay: 55, chinese: 35, indian: 6, others: 4, turnout2022: 62 },
    { code: '13', name: 'FELDA Pemanis', tier: 1, electorate: 3141, malay: 68, chinese: 20, indian: 7, others: 5, turnout2022: 65 },
  ].map(pd => ({
    ...pd,
    others: Math.max(0, 100 - pd.malay - pd.chinese - pd.indian)
  })),
  historicalResults: [
    {
      year: 2022,
      turnout: 61.3,
      results: {
        bn: { party: 'BN-UMNO', votes: 9876, percentage: 52.1 },
        ph: { party: 'PH-PKR', votes: 6234, percentage: 32.9 },
        pn: { party: 'PN-PAS', votes: 2845, percentage: 15.0 }
      },
      winner: 'BN',
      majority: 3642
    },
    {
      year: 2018,
      turnout: 84.2,
      results: {
        bn: { party: 'BN-UMNO', votes: 10234, percentage: 48.5 },
        ph: { party: 'PH-PKR', votes: 10567, percentage: 50.1 },
        others: { party: 'Others', votes: 295, percentage: 1.4 }
      },
      winner: 'PH',
      majority: 333
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
    summary: 'N02 Pemanis is a Malay-majority (63.3%) seat with significant Chinese minority (32.4%). 2018 saw PH win by razor-thin 333 votes with 84.2% turnout, but 2022 collapse (61.3%) gave BN comfortable 3,642 majority. FELDA Pemanis is key swing bloc.',
    demographics: 'Malay 63.3%, Chinese 32.4%, Indian 2.3%. Rural Malay PDs (01-08) are BN strongholds with 90%+ Malay. Batu Anam and Pemanis town are competitive mixed areas. FELDA Pemanis (3,141 voters) is decisive swing bloc.',
    turnout2022: '61.3% - massive collapse from 84.2% in 2018. Chinese turnout depression key factor. Rural Malay maintained 65-70%, urban Chinese areas dropped to 55-58%.',
    battlegrounds: 'FELDA Pemanis (PD 13) with 3,141 voters is kingmaker. Batu Anam, Pemanis Pekan, and Taman Pemanis (PDs 9-11) are Chinese-influenced swing areas. Rural PDs 01-08 are BN fortress.',
    projection: 'BN-leaning. PH needs 80%+ Chinese turnout + FELDA swing to compete. BN wins with moderate Chinese turnout (<65%) and holds rural Malay base.'
  }
};
