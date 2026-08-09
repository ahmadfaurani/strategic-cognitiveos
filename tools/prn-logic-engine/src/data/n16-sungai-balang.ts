/**
 * N16 Sungai Balang - Voter Roll Data
 * 
 * Source: Excel intelligence (as of 19 June 2026)
 * Parliament: P.146   MUAR
 * Total Electorate: 31,039
 * Demographics: Malay 73.6% / Chinese 25.1% / Indian 0.2%
 * 
 * Tiers:
 * - Tier 1 (Kingmaker/Chinese Base): 3 PDs
 * - Tier 2 (Mixed): 2 PDs
 * - Tier 3 (Malay Heartland): 14 PDs
 */

import { Seat, PollingDistrict } from '../types';

export const n16SungaiBalang: Seat = {
  code: 'N16',
  name: 'Sungai Balang',
  federalCode: 'P.146',
  federalName: 'MUAR',
  district: 'Sungai Balang',  // TODO: Verify district
  totalElectorate: 31039,
  pollingDistricts: [
    {
      name: 'PARIT SHAFIEE',
      code: '146/16/01',
      electorate: 704,
      demographics: {
        malay: 698,
        chinese: 1,
        indian: 0,
        others: 5,
        malayPct: 99.1,
        chinesePct: 0.1,
        indianPct: 0.0
      }
    },
    {
      name: 'PARIT KASSIM',
      code: '146/16/02',
      electorate: 2541,
      demographics: {
        malay: 1822,
        chinese: 701,
        indian: 6,
        others: 12,
        malayPct: 71.7,
        chinesePct: 27.6,
        indianPct: 0.2
      }
    },
    {
      name: 'BUKIT MOR',
      code: '146/16/03',
      electorate: 1817,
      demographics: {
        malay: 761,
        chinese: 1046,
        indian: 4,
        others: 6,
        malayPct: 41.9,
        chinesePct: 57.6,
        indianPct: 0.2
      }
    },
    {
      name: 'PARIT NAWEE',
      code: '146/16/04',
      electorate: 953,
      demographics: {
        malay: 937,
        chinese: 12,
        indian: 1,
        others: 3,
        malayPct: 98.3,
        chinesePct: 1.3,
        indianPct: 0.1
      }
    },
    {
      name: 'BANDAR PARIT JAWA UTARA',
      code: '146/16/05',
      electorate: 3810,
      demographics: {
        malay: 1265,
        chinese: 2495,
        indian: 13,
        others: 37,
        malayPct: 33.2,
        chinesePct: 65.5,
        indianPct: 0.3
      }
    },
    {
      name: 'BANDAR PARIT JAWA SELATAN',
      code: '146/16/06',
      electorate: 680,
      demographics: {
        malay: 266,
        chinese: 400,
        indian: 7,
        others: 7,
        malayPct: 39.1,
        chinesePct: 58.8,
        indianPct: 1.0
      }
    },
    {
      name: 'PARIT JAWA',
      code: '146/16/07',
      electorate: 1533,
      demographics: {
        malay: 987,
        chinese: 517,
        indian: 7,
        others: 22,
        malayPct: 64.4,
        chinesePct: 33.7,
        indianPct: 0.5
      }
    },
    {
      name: 'PARIT TENGAH',
      code: '146/16/08',
      electorate: 1208,
      demographics: {
        malay: 697,
        chinese: 485,
        indian: 1,
        others: 25,
        malayPct: 57.7,
        chinesePct: 40.1,
        indianPct: 0.1
      }
    },
    {
      name: 'PARIT JAMIL DARAT',
      code: '146/16/09',
      electorate: 1798,
      demographics: {
        malay: 1694,
        chinese: 95,
        indian: 5,
        others: 4,
        malayPct: 94.2,
        chinesePct: 5.3,
        indianPct: 0.3
      }
    },
    {
      name: 'PARIT PECHAH',
      code: '146/16/10',
      electorate: 1713,
      demographics: {
        malay: 1356,
        chinese: 328,
        indian: 3,
        others: 26,
        malayPct: 79.2,
        chinesePct: 19.1,
        indianPct: 0.2
      }
    },
    {
      name: 'SRI MENANTI',
      code: '146/16/11',
      electorate: 1431,
      demographics: {
        malay: 1176,
        chinese: 232,
        indian: 2,
        others: 21,
        malayPct: 82.2,
        chinesePct: 16.2,
        indianPct: 0.1
      }
    },
    {
      name: 'SUNGAI SUDAH',
      code: '146/16/12',
      electorate: 2008,
      demographics: {
        malay: 1695,
        chinese: 249,
        indian: 2,
        others: 62,
        malayPct: 84.4,
        chinesePct: 12.4,
        indianPct: 0.1
      }
    },
    {
      name: 'SUNGAI BALANG',
      code: '146/16/13',
      electorate: 2039,
      demographics: {
        malay: 1849,
        chinese: 172,
        indian: 2,
        others: 16,
        malayPct: 90.7,
        chinesePct: 8.4,
        indianPct: 0.1
      }
    },
    {
      name: 'SUNGAI BALANG BESAR',
      code: '146/16/14',
      electorate: 1901,
      demographics: {
        malay: 1781,
        chinese: 104,
        indian: 4,
        others: 12,
        malayPct: 93.7,
        chinesePct: 5.5,
        indianPct: 0.2
      }
    },
    {
      name: 'SUNGAI BALANG DARAT',
      code: '146/16/15',
      electorate: 626,
      demographics: {
        malay: 620,
        chinese: 2,
        indian: 0,
        others: 4,
        malayPct: 99.0,
        chinesePct: 0.3,
        indianPct: 0.0
      }
    },
    {
      name: 'SARANG BUAYA DARAT',
      code: '146/16/16',
      electorate: 1330,
      demographics: {
        malay: 1297,
        chinese: 25,
        indian: 0,
        others: 8,
        malayPct: 97.5,
        chinesePct: 1.9,
        indianPct: 0.0
      }
    },
    {
      name: 'PARIT YUSOF',
      code: '146/16/17',
      electorate: 2777,
      demographics: {
        malay: 2331,
        chinese: 417,
        indian: 2,
        others: 27,
        malayPct: 83.9,
        chinesePct: 15.0,
        indianPct: 0.1
      }
    },
    {
      name: 'SARANG BUAYA LAUT',
      code: '146/16/18',
      electorate: 1697,
      demographics: {
        malay: 1192,
        chinese: 464,
        indian: 0,
        others: 41,
        malayPct: 70.2,
        chinesePct: 27.3,
        indianPct: 0.0
      }
    },
    {
      name: 'KAMPONG PARIT BULAT',
      code: '146/16/19',
      electorate: 473,
      demographics: {
        malay: 433,
        chinese: 35,
        indian: 0,
        others: 5,
        malayPct: 91.5,
        chinesePct: 7.4,
        indianPct: 0.0
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
