/**
 * N25 Johor Lama - Voter Roll Data
 * 
 * Source: Excel intelligence (as of 19 June 2026)
 * Parliament: P.156   KOTA TINGGI
 * Total Electorate: 32,716
 * Demographics: Malay 83.2% / Chinese 12.8% / Indian 2.5%
 * 
 * Tiers:
 * - Tier 1 (Kingmaker/Chinese Base): 2 PDs
 * - Tier 2 (Mixed): 3 PDs
 * - Tier 3 (Malay Heartland): 11 PDs
 */

import { Seat, PollingDistrict } from '../types';

export const n25JohorLama: Seat = {
  code: 'N25',
  name: 'Johor Lama',
  federalCode: 'P.156',
  federalName: 'KOTA TINGGI',
  district: 'Johor Lama',  // TODO: Verify district
  totalElectorate: 32716,
  pollingDistricts: [
    {
      name: 'LOK HENG BARAT',
      code: '156/37/01',
      electorate: 3092,
      demographics: {
        malay: 3067,
        chinese: 1,
        indian: 9,
        others: 15,
        malayPct: 99.2,
        chinesePct: 0.0,
        indianPct: 0.3
      }
    },
    {
      name: 'LOK HENG TIMUR',
      code: '156/37/02',
      electorate: 1910,
      demographics: {
        malay: 1887,
        chinese: 6,
        indian: 3,
        others: 14,
        malayPct: 98.8,
        chinesePct: 0.3,
        indianPct: 0.2
      }
    },
    {
      name: 'LOK HENG SELATAN',
      code: '156/37/03',
      electorate: 3517,
      demographics: {
        malay: 3499,
        chinese: 2,
        indian: 1,
        others: 15,
        malayPct: 99.5,
        chinesePct: 0.1,
        indianPct: 0.0
      }
    },
    {
      name: 'KOTA KECHIL TIMOR',
      code: '156/37/04',
      electorate: 2008,
      demographics: {
        malay: 501,
        chinese: 1386,
        indian: 110,
        others: 11,
        malayPct: 25.0,
        chinesePct: 69.0,
        indianPct: 5.5
      }
    },
    {
      name: 'KOTA KECHIL BARAT',
      code: '156/37/05',
      electorate: 1033,
      demographics: {
        malay: 526,
        chinese: 449,
        indian: 47,
        others: 11,
        malayPct: 50.9,
        chinesePct: 43.5,
        indianPct: 4.5
      }
    },
    {
      name: 'BUKIT KERAJAAN',
      code: '156/37/06',
      electorate: 1560,
      demographics: {
        malay: 1156,
        chinese: 242,
        indian: 122,
        others: 40,
        malayPct: 74.1,
        chinesePct: 15.5,
        indianPct: 7.8
      }
    },
    {
      name: 'JALAN MAWAI',
      code: '156/37/07',
      electorate: 2070,
      demographics: {
        malay: 601,
        chinese: 1284,
        indian: 101,
        others: 84,
        malayPct: 29.0,
        chinesePct: 62.0,
        indianPct: 4.9
      }
    },
    {
      name: 'TEMBIOH',
      code: '156/37/08',
      electorate: 673,
      demographics: {
        malay: 367,
        chinese: 255,
        indian: 18,
        others: 33,
        malayPct: 54.5,
        chinesePct: 37.9,
        indianPct: 2.7
      }
    },
    {
      name: 'KAMPONG MAKAM',
      code: '156/37/09',
      electorate: 2144,
      demographics: {
        malay: 1624,
        chinese: 207,
        indian: 163,
        others: 150,
        malayPct: 75.7,
        chinesePct: 9.7,
        indianPct: 7.6
      }
    },
    {
      name: 'FELDA PASAK',
      code: '156/37/10',
      electorate: 3306,
      demographics: {
        malay: 3196,
        chinese: 7,
        indian: 70,
        others: 33,
        malayPct: 96.7,
        chinesePct: 0.2,
        indianPct: 2.1
      }
    },
    {
      name: 'AIR TAWAR 3',
      code: '156/37/11',
      electorate: 3795,
      demographics: {
        malay: 3767,
        chinese: 0,
        indian: 2,
        others: 26,
        malayPct: 99.3,
        chinesePct: 0.0,
        indianPct: 0.1
      }
    },
    {
      name: 'AIR TAWAR 2',
      code: '156/37/12',
      electorate: 5616,
      demographics: {
        malay: 5549,
        chinese: 6,
        indian: 13,
        others: 48,
        malayPct: 98.8,
        chinesePct: 0.1,
        indianPct: 0.2
      }
    },
    {
      name: 'PANCHOR',
      code: '156/37/13',
      electorate: 449,
      demographics: {
        malay: 420,
        chinese: 5,
        indian: 22,
        others: 2,
        malayPct: 93.5,
        chinesePct: 1.1,
        indianPct: 4.9
      }
    },
    {
      name: 'JOHOR LAMA',
      code: '156/37/14',
      electorate: 242,
      demographics: {
        malay: 228,
        chinese: 3,
        indian: 7,
        others: 4,
        malayPct: 94.2,
        chinesePct: 1.2,
        indianPct: 2.9
      }
    },
    {
      name: 'PEKAN TELOK SENGAT',
      code: '156/37/15',
      electorate: 955,
      demographics: {
        malay: 567,
        chinese: 305,
        indian: 66,
        others: 17,
        malayPct: 59.4,
        chinesePct: 31.9,
        indianPct: 6.9
      }
    },
    {
      name: 'TELOK SENGAT',
      code: '156/37/16',
      electorate: 346,
      demographics: {
        malay: 262,
        chinese: 22,
        indian: 48,
        others: 14,
        malayPct: 75.7,
        chinesePct: 6.4,
        indianPct: 13.9
      }
    },
  ],
  candidates: {
    bn: { name: 'TBD', party: 'TBD', incumbent: false },
    ph: { name: 'TBD', party: 'TBD', incumbent: false },
    pn: { name: 'TBD', party: 'TBD', incumbent: false }
  },
  historicalResults: [
    // TODO: Add 2022 and 2018 results from intelligence
  ],
  notes: [
    'Data extracted from Excel intelligence (19 June 2026)',
    'Tier classification: Tier1=Chinese/Indian >50%, Tier2=Mixed 30-50%, Tier3=Malay >70%',
    'Requires ground truth validation for candidate profiles and historical results'
  ]
};
