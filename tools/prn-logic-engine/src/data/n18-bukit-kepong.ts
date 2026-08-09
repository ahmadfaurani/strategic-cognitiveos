/**
 * N18 Bukit Kepong - Voter Roll Data
 * 
 * Source: Excel intelligence (as of 19 June 2026)
 * Parliament: P.143   PAGOH
 * Total Electorate: 37,683
 * Demographics: Malay 70.3% / Chinese 25.1% / Indian 2.6%
 * 
 * Tiers:
 * - Tier 1 (Kingmaker/Chinese Base): 11 PDs
 * - Tier 2 (Mixed): 3 PDs
 * - Tier 3 (Malay Heartland): 14 PDs
 */

import { Seat, PollingDistrict } from '../types';

export const n18BukitKepong: Seat = {
  code: 'N18',
  name: 'Bukit Kepong',
  federalCode: 'P.143',
  federalName: 'PAGOH',
  district: 'Bukit Kepong',  // TODO: Verify district
  totalElectorate: 37683,
  pollingDistricts: [
    {
      name: 'BANDAR BUKIT KEPONG',
      code: '143/07/01',
      electorate: 773,
      demographics: {
        malay: 148,
        chinese: 616,
        indian: 3,
        others: 6,
        malayPct: 19.1,
        chinesePct: 79.7,
        indianPct: 0.4
      }
    },
    {
      name: 'FELCRA PAYA KEPAR',
      code: '143/07/02',
      electorate: 2059,
      demographics: {
        malay: 2041,
        chinese: 5,
        indian: 3,
        others: 10,
        malayPct: 99.1,
        chinesePct: 0.2,
        indianPct: 0.1
      }
    },
    {
      name: 'MA`OKIL',
      code: '143/07/03',
      electorate: 4329,
      demographics: {
        malay: 4305,
        chinese: 1,
        indian: 6,
        others: 17,
        malayPct: 99.4,
        chinesePct: 0.0,
        indianPct: 0.1
      }
    },
    {
      name: 'BUKIT KEPONG',
      code: '143/07/04',
      electorate: 1951,
      demographics: {
        malay: 1628,
        chinese: 180,
        indian: 3,
        others: 140,
        malayPct: 83.4,
        chinesePct: 9.2,
        indianPct: 0.2
      }
    },
    {
      name: 'LENGA UTARA',
      code: '143/07/05',
      electorate: 607,
      demographics: {
        malay: 536,
        chinese: 50,
        indian: 7,
        others: 14,
        malayPct: 88.3,
        chinesePct: 8.2,
        indianPct: 1.2
      }
    },
    {
      name: 'LENGA SELATAN',
      code: '143/07/06',
      electorate: 1108,
      demographics: {
        malay: 414,
        chinese: 683,
        indian: 2,
        others: 9,
        malayPct: 37.4,
        chinesePct: 61.6,
        indianPct: 0.2
      }
    },
    {
      name: 'KAMPONG BAHRU',
      code: '143/07/07',
      electorate: 1463,
      demographics: {
        malay: 1160,
        chinese: 51,
        indian: 0,
        others: 252,
        malayPct: 79.3,
        chinesePct: 3.5,
        indianPct: 0.0
      }
    },
    {
      name: 'LENGA',
      code: '143/07/08',
      electorate: 1415,
      demographics: {
        malay: 1396,
        chinese: 3,
        indian: 2,
        others: 14,
        malayPct: 98.7,
        chinesePct: 0.2,
        indianPct: 0.1
      }
    },
    {
      name: 'KAMPONG GOMBANG',
      code: '143/07/09',
      electorate: 415,
      demographics: {
        malay: 299,
        chinese: 112,
        indian: 0,
        others: 4,
        malayPct: 72.0,
        chinesePct: 27.0,
        indianPct: 0.0
      }
    },
    {
      name: 'LIANG BATU',
      code: '143/07/10',
      electorate: 968,
      demographics: {
        malay: 949,
        chinese: 10,
        indian: 2,
        others: 7,
        malayPct: 98.0,
        chinesePct: 1.0,
        indianPct: 0.2
      }
    },
    {
      name: 'LENGA ROAD',
      code: '143/07/11',
      electorate: 1226,
      demographics: {
        malay: 678,
        chinese: 388,
        indian: 150,
        others: 10,
        malayPct: 55.3,
        chinesePct: 31.6,
        indianPct: 12.2
      }
    },
    {
      name: 'PAGOH',
      code: '143/07/12',
      electorate: 1770,
      demographics: {
        malay: 1027,
        chinese: 446,
        indian: 276,
        others: 21,
        malayPct: 58.0,
        chinesePct: 25.2,
        indianPct: 15.6
      }
    },
    {
      name: 'BANDAR PAGOH UTARA',
      code: '143/07/13',
      electorate: 1420,
      demographics: {
        malay: 561,
        chinese: 817,
        indian: 34,
        others: 8,
        malayPct: 39.5,
        chinesePct: 57.5,
        indianPct: 2.4
      }
    },
    {
      name: 'BANDAR PAGOH SELATAN',
      code: '143/07/14',
      electorate: 1779,
      demographics: {
        malay: 598,
        chinese: 1051,
        indian: 87,
        others: 43,
        malayPct: 33.6,
        chinesePct: 59.1,
        indianPct: 4.9
      }
    },
    {
      name: 'PAYA REDAN',
      code: '143/07/15',
      electorate: 1474,
      demographics: {
        malay: 1200,
        chinese: 217,
        indian: 29,
        others: 28,
        malayPct: 81.4,
        chinesePct: 14.7,
        indianPct: 2.0
      }
    },
    {
      name: 'KAMPONG TERATAI',
      code: '143/07/16',
      electorate: 948,
      demographics: {
        malay: 37,
        chinese: 896,
        indian: 8,
        others: 7,
        malayPct: 3.9,
        chinesePct: 94.5,
        indianPct: 0.8
      }
    },
    {
      name: 'SRI LEDANG',
      code: '143/07/17',
      electorate: 1609,
      demographics: {
        malay: 1593,
        chinese: 2,
        indian: 1,
        others: 13,
        malayPct: 99.0,
        chinesePct: 0.1,
        indianPct: 0.1
      }
    },
    {
      name: 'FELDA SRI JAYA',
      code: '143/07/18',
      electorate: 2119,
      demographics: {
        malay: 2060,
        chinese: 48,
        indian: 1,
        others: 10,
        malayPct: 97.2,
        chinesePct: 2.3,
        indianPct: 0.0
      }
    },
    {
      name: 'DURIAN CHONDONG',
      code: '143/07/19',
      electorate: 736,
      demographics: {
        malay: 533,
        chinese: 187,
        indian: 1,
        others: 15,
        malayPct: 72.4,
        chinesePct: 25.4,
        indianPct: 0.1
      }
    },
    {
      name: 'KUNDANG ULU',
      code: '143/07/20',
      electorate: 2259,
      demographics: {
        malay: 2102,
        chinese: 111,
        indian: 2,
        others: 44,
        malayPct: 93.1,
        chinesePct: 4.9,
        indianPct: 0.1
      }
    },
    {
      name: 'LADANG SERAMPANG',
      code: '143/07/21',
      electorate: 179,
      demographics: {
        malay: 25,
        chinese: 79,
        indian: 74,
        others: 1,
        malayPct: 14.0,
        chinesePct: 44.1,
        indianPct: 41.3
      }
    },
    {
      name: 'PARIT RAJA',
      code: '143/07/22',
      electorate: 2285,
      demographics: {
        malay: 2129,
        chinese: 55,
        indian: 83,
        others: 18,
        malayPct: 93.2,
        chinesePct: 2.4,
        indianPct: 3.6
      }
    },
    {
      name: 'BANDAR GRISEK TIMOR',
      code: '143/07/23',
      electorate: 701,
      demographics: {
        malay: 132,
        chinese: 550,
        indian: 14,
        others: 5,
        malayPct: 18.8,
        chinesePct: 78.5,
        indianPct: 2.0
      }
    },
    {
      name: 'KAMPONG KUNDANG ULU',
      code: '143/07/24',
      electorate: 1138,
      demographics: {
        malay: 337,
        chinese: 791,
        indian: 3,
        others: 7,
        malayPct: 29.6,
        chinesePct: 69.5,
        indianPct: 0.3
      }
    },
    {
      name: 'LADANG NORDANAL',
      code: '143/07/25',
      electorate: 189,
      demographics: {
        malay: 89,
        chinese: 6,
        indian: 89,
        others: 5,
        malayPct: 47.1,
        chinesePct: 3.2,
        indianPct: 47.1
      }
    },
    {
      name: 'KEBUN BAHRU',
      code: '143/07/26',
      electorate: 930,
      demographics: {
        malay: 85,
        chinese: 811,
        indian: 29,
        others: 5,
        malayPct: 9.1,
        chinesePct: 87.2,
        indianPct: 3.1
      }
    },
    {
      name: 'GRISEK',
      code: '143/07/27',
      electorate: 1833,
      demographics: {
        malay: 447,
        chinese: 1298,
        indian: 80,
        others: 8,
        malayPct: 24.4,
        chinesePct: 70.8,
        indianPct: 4.4
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
