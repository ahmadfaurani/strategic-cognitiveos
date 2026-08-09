import { Seat } from '../types.js';

export const n27LayangLayang: Seat = {
  code: 'N27',
  name: 'Layang-Layang',
  parliament: 'P151 Simpang Renggam',
  district: 'Kluang',
  totalElectorate: 25181,
  pollingDistricts: [
    // Tier 1: Kingmaker Indian-Mixed PDs (10% of voters, 40% of PH path)
    { code: '04', name: 'Senda', tier: 1, electorate: 867, malay: 31.4, chinese: 22.6, indian: 44.9, others: 1.1, turnout2022: 52 },
    { code: '08', name: 'Chemara', tier: 1, electorate: 1450, malay: 53.0, chinese: 8.5, indian: 37.5, others: 1.0, turnout2022: 54 },
    { code: '07', name: 'Sembrong', tier: 1, electorate: 137, malay: 35.8, chinese: 7.3, indian: 54.0, others: 2.9, turnout2022: 50 },
    { code: '13', name: 'Ladang Southern Malay', tier: 1, electorate: 142, malay: 39.4, chinese: 14.8, indian: 43.7, others: 2.1, turnout2022: 48 },
    
    // Tier 2: Chinese-Concentration Base PDs (43% of voters)
    { code: '10', name: 'Bandar Layang-Layang Selatan', tier: 2, electorate: 3296, malay: 16.7, chinese: 69.8, indian: 11.5, others: 2.0, turnout2022: 58 },
    { code: '11', name: 'Bandar Layang-Layang Utara', tier: 2, electorate: 2986, malay: 28.9, chinese: 58.9, indian: 9.5, others: 2.7, turnout2022: 57 },
    { code: '05', name: 'Bandar Renggam', tier: 2, electorate: 3609, malay: 36.4, chinese: 46.2, indian: 16.0, others: 1.4, turnout2022: 56 },
    { code: '06', name: 'Kebun Bahru', tier: 2, electorate: 820, malay: 23.5, chinese: 42.4, indian: 33.3, others: 0.8, turnout2022: 55 },
    
    // Tier 3: Malay Heartland (Damage Limit, 47% of voters)
    { code: '14', name: 'FELDA Layang-Layang', tier: 3, electorate: 875, malay: 99.1, chinese: 0.3, indian: 0.3, others: 0.3, turnout2022: 68 },
    { code: '02', name: 'Kampung Chokro', tier: 3, electorate: 4059, malay: 90.3, chinese: 3.0, indian: 3.4, others: 3.3, turnout2022: 65 },
    { code: '03', name: 'Kampung Sahari', tier: 3, electorate: 4206, malay: 83.4, chinese: 4.4, indian: 7.6, others: 4.6, turnout2022: 64 },
    { code: '09', name: 'Layang-Layang', tier: 3, electorate: 1683, malay: 77.7, chinese: 15.8, indian: 1.5, others: 5.0, turnout2022: 62 },
    { code: '12', name: 'Renggam', tier: 3, electorate: 832, malay: 83.1, chinese: 5.3, indian: 10.0, others: 1.6, turnout2022: 64 },
    { code: '01', name: 'Ladang Tun Dr. Ismail', tier: 3, electorate: 219, malay: 64.4, chinese: 21.9, indian: 10.0, others: 3.7, turnout2022: 60 },
  ].map(pd => ({
    ...pd,
    others: Math.max(0, 100 - pd.malay - pd.chinese - pd.indian)
  })),
  historicalResults: [
    {
      year: 2022,
      turnout: 56.4,
      results: {
        bn: { party: 'BN-UMNO', votes: 7551, percentage: 55.0 },
        ph: { party: 'PH-PKR', votes: 4736, percentage: 34.5 },
        pn: { party: 'PN-PAS', votes: 1278, percentage: 9.3 }
      },
      winner: 'BN',
      majority: 2815
    },
    {
      year: 2018,
      turnout: 81.9,
      results: {
        bn: { party: 'BN-UMNO', votes: 7449, percentage: 46.9 },
        ph: { party: 'PH-PKR', votes: 7085, percentage: 44.6 },
        pn: { party: 'PAS', votes: 1339, percentage: 8.4 }
      },
      winner: 'BN',
      majority: 364
    }
  ],
  candidates: {
    bn: {
      name: 'Chua Jian Boon',
      party: 'BN-MCA',
      profile: 'MCA candidate (Chinese). Structural disadvantage in 56.6% Malay seat. Campaign: Chinese business community, economic stability. Strengths: MCA machinery, business network. Vulnerability: Chinese candidate in Malay-majority seat limits ceiling to ~25-28%. Risk of Chinese vote flight to PH.'
    },
    ph: {
      name: 'Guna Balakrishnan',
      party: 'PH-PKR',
      profile: 'Indian candidate. Campaign: Indian kingmaker consolidation + non-Malay unity + moderate Malay outreach. Strengths: Indian identity consolidates 12.4% Indian vote (kingmaker bloc), personal appeal in mixed PDs (Senda, Chemara). Vulnerability: Must achieve 30%+ Malay support to win. Ceiling depends on Indian turnout (target 75%+) and Chinese consolidation (80%+). NOTE: Profile details pending verification (do not use unconfirmed titles/affiliations).'
    },
    pn: {
      name: 'Abd Mutalip Abd Rahim',
      party: 'PN-Bersatu',
      profile: 'Incumbent (ex-BN→PN defection). Former EXCO for Islamic Religious Affairs (2013-2018). Campaign: Malay consolidation, incumbency record, defection sympathy. Strengths: Personal popularity (won 2013, 2022), Malay machinery, incumbent advantage. Vulnerability: Party switch narrative (loyalty questions), UMNO ground workers may be half-hearted.'
    }
  },
  analysis: {
    summary: 'N27 Layang-Layang is a 25,181-voter diverse seat: Malay 56.6%, Chinese 28.2%, Indian 12.4%. 2018: BN won by 364 votes (44.6% PH) at 81.9% turnout (GE14 coattails). 2022: BN won by 2,815 votes (55%) at 56.4% turnout (standalone state baseline). 2026: Three-cornered race (PH Guna, PN Abd Mutalip, BN Chua). CRITICAL: BN→PN split (Abd Mutalip ex-UMNO incumbent) + BN MCA candidate (Chua) = Malay vote fragmentation. PH is UNDERDOG (25-30% win probability). Path requires: (1) Malay split between BN/PN, (2) Indian 75%+ consolidation, (3) Chinese 80%+ turnout. Higher turnout does NOT help PH (mostly brings out Malay voters).',
    demographics: 'Malay 56.6% (14,242), Chinese 28.2% (7,100), Indian 12.4% (3,132). Youth 18-30: 23.8%. Mature electorate: 54.8% aged 46+. Tier-1 Kingmaker PDs (Senda, Chemara, Sembrong, Ladang Sth Malay): 2,596 voters (10%), 40-50% Indian — PH must win 75%+ here. Tier-2 Chinese Base (4 PDs): 10,711 voters (43%) — PH must deliver 80%+ turnout, 70%+ support. Tier-3 Malay Heartland (6 PDs): 11,874 voters (47%) — damage limit at 30-35% PH. WARNING: Higher overall turnout brings out MORE Malay voters (helps PN/BN, not PH).',
    turnout2022: '56.4% — REAL baseline for standalone state election (not depressed). 2018\'s 81.9% rode GE14 coattails (federal election brought outstation voters home). July 2026 is state-only: realistic range 58-66%. CRITICAL: Unlike Chinese-majority seats, higher turnout here does NOT help PH — most marginal voters are Malay (PN/BN lean). PH cannot rely on "just get turnout to 75%" strategy. Path is: Malay split + non-Malay consolidation at 60-65% baseline.',
    battlegrounds: 'Tier-1 Kingmaker (Senda 44.9% Indian, Chemara 37.5% Indian, Sembrong 54% Indian): Guna must personally visit, consolidate 75%+ Indian support. Tier-2 Chinese Base (Bandar Selatan 69.8% Chinese, Bandar Utara 58.9% Chinese, Bandar Renggam 46.2% Chinese): GOTV priority, 80%+ turnout target. Tier-3 Malay Heartland (FELDA 99% Malay, Kg Chokro 90% Malay, Kg Sahari 83% Malay): contain damage, target 30-35% PH from young Malays. DECISIVE FACTOR: Malay split between BN (Chua, MB officer) and PN (Abd Mutalip, incumbent). This is OUT OF PH\'S HANDS — coin flip.',
    projection: 'LEANING PN (PH 25-30% win probability, not 40%). BASE CASE (60% turnout): PN holds seat via Malay consolidation. PH WINS ONLY IF: (1) Malay vote splits 40% PN / 20% BN (or vice versa), (2) Indian 75%+ PH, (3) Chinese 80%+ turnout. This is narrow path, not baseline. BN collapses to 15-25% (Chinese candidate penalty in Malay seat), but PN inherits incumbent advantage + Malay base. PH ceiling ~38-40% without Malay split. Bersama/MUDA NOT STANDING — no reform vote fragmentation (unlike Bukit Batu/Bukit Naning).'
  }
};
