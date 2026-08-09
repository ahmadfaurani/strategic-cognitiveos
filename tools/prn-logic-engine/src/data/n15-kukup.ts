/**
 * N15 Kukup - Voter Roll Data
 * 
 * Source: Excel intelligence (as of 19 June 2026)
 * Parliament: P.165   TANJUNG PIAI
 * Total Electorate: 34,968
 * Demographics: Malay 60.2% / Chinese 36.7% / Indian 0.9%
 * 
 * Tiers:
 * - Tier 1 (Kingmaker/Chinese Base): 4 PDs
 * - Tier 2 (Mixed): 2 PDs
 * - Tier 3 (Malay Heartland): 8 PDs
 */

import { Seat, PollingDistrict } from '../types';

export const n15Kukup: Seat = {
  code: 'N15',
  name: 'Kukup',
  federalCode: 'P.165',
  federalName: 'TANJUNG PIAI',
  district: 'Kukup',  // TODO: Verify district
  totalElectorate: 34968,
  pollingDistricts: [
    {
      name: 'LADANG SUNGAI BURONG',
      code: '165/56/01',
      electorate: 558,
      demographics: {
        malay: 482,
        chinese: 53,
        indian: 0,
        others: 23,
        malayPct: 86.4,
        chinesePct: 9.5,
        indianPct: 0.0
      }
    },
    {
      name: 'JALAN RIMBA TERJUN',
      code: '165/56/02',
      electorate: 2893,
      demographics: {
        malay: 534,
        chinese: 2271,
        indian: 56,
        others: 32,
        malayPct: 18.5,
        chinesePct: 78.5,
        indianPct: 1.9
      }
    },
    {
      name: 'KAMPONG DUKU',
      code: '165/56/03',
      electorate: 6220,
      demographics: {
        malay: 2283,
        chinese: 3718,
        indian: 92,
        others: 127,
        malayPct: 36.7,
        chinesePct: 59.8,
        indianPct: 1.5
      }
    },
    {
      name: 'KAMPONG RIMBA TERJUN',
      code: '165/56/04',
      electorate: 3241,
      demographics: {
        malay: 2263,
        chinese: 904,
        indian: 29,
        others: 45,
        malayPct: 69.8,
        chinesePct: 27.9,
        indianPct: 0.9
      }
    },
    {
      name: 'PARIT HJ. ISMAIL',
      code: '165/56/05',
      electorate: 1540,
      demographics: {
        malay: 953,
        chinese: 558,
        indian: 7,
        others: 22,
        malayPct: 61.9,
        chinesePct: 36.2,
        indianPct: 0.5
      }
    },
    {
      name: 'RAMBAH',
      code: '165/56/06',
      electorate: 2171,
      demographics: {
        malay: 1034,
        chinese: 1039,
        indian: 70,
        others: 28,
        malayPct: 47.6,
        chinesePct: 47.9,
        indianPct: 3.2
      }
    },
    {
      name: 'PARIT RAMBAI',
      code: '165/56/07',
      electorate: 1324,
      demographics: {
        malay: 1164,
        chinese: 116,
        indian: 5,
        others: 39,
        malayPct: 87.9,
        chinesePct: 8.8,
        indianPct: 0.4
      }
    },
    {
      name: 'PERADIN',
      code: '165/56/08',
      electorate: 832,
      demographics: {
        malay: 749,
        chinese: 47,
        indian: 1,
        others: 35,
        malayPct: 90.0,
        chinesePct: 5.6,
        indianPct: 0.1
      }
    },
    {
      name: 'TELOK KERANG',
      code: '165/56/09',
      electorate: 2509,
      demographics: {
        malay: 2145,
        chinese: 273,
        indian: 9,
        others: 82,
        malayPct: 85.5,
        chinesePct: 10.9,
        indianPct: 0.4
      }
    },
    {
      name: 'PENEROK',
      code: '165/56/10',
      electorate: 2572,
      demographics: {
        malay: 1705,
        chinese: 749,
        indian: 18,
        others: 100,
        malayPct: 66.3,
        chinesePct: 29.1,
        indianPct: 0.7
      }
    },
    {
      name: 'SUNGAI BOH',
      code: '165/56/11',
      electorate: 873,
      demographics: {
        malay: 853,
        chinese: 8,
        indian: 1,
        others: 11,
        malayPct: 97.7,
        chinesePct: 0.9,
        indianPct: 0.1
      }
    },
    {
      name: 'BANDAR PERMAS KECHIL',
      code: '165/56/12',
      electorate: 774,
      demographics: {
        malay: 284,
        chinese: 463,
        indian: 7,
        others: 20,
        malayPct: 36.7,
        chinesePct: 59.8,
        indianPct: 0.9
      }
    },
    {
      name: 'PERMAS KECHIL',
      code: '165/56/13',
      electorate: 3282,
      demographics: {
        malay: 1063,
        chinese: 2156,
        indian: 9,
        others: 54,
        malayPct: 32.4,
        chinesePct: 65.7,
        indianPct: 0.3
      }
    },
    {
      name: 'SUNGAI DURIAN',
      code: '165/56/14',
      electorate: 2102,
      demographics: {
        malay: 1712,
        chinese: 315,
        indian: 4,
        others: 71,
        malayPct: 81.4,
        chinesePct: 15.0,
        indianPct: 0.2
      }
    },
    {
      name: 'SERKAT',
      code: '165/56/15',
      electorate: 2269,
      demographics: {
        malay: 2190,
        chinese: 35,
        indian: 1,
        others: 43,
        malayPct: 96.5,
        chinesePct: 1.5,
        indianPct: 0.0
      }
    },
    {
      name: 'ANDEK MORI',
      code: '165/56/16',
      electorate: 1808,
      demographics: {
        malay: 1634,
        chinese: 132,
        indian: 4,
        others: 38,
        malayPct: 90.4,
        chinesePct: 7.3,
        indianPct: 0.2
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
