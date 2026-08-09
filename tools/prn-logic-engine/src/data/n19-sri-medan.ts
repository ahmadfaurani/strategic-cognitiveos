/**
 * N19 Sri Medan - Voter Roll Data
 * 
 * Source: Excel intelligence (as of 19 June 2026)
 * Parliament: P.147   PARIT SULONG
 * Total Electorate: 33,875
 * Demographics: Malay 89.8% / Chinese 8.1% / Indian 0.3%
 * 
 * Tiers:
 * - Tier 1 (Kingmaker/Chinese Base): 0 PDs
 * - Tier 2 (Mixed): 1 PDs
 * - Tier 3 (Malay Heartland): 14 PDs
 */

import { Seat, PollingDistrict } from '../types';

export const n19SriMedan: Seat = {
  code: 'N19',
  name: 'Sri Medan',
  federalCode: 'P.147',
  federalName: 'PARIT SULONG',
  district: 'Sri Medan',  // TODO: Verify district
  totalElectorate: 33875,
  pollingDistricts: [
    {
      name: 'PARIT GANTONG',
      code: '147/18/01',
      electorate: 3231,
      demographics: {
        malay: 3128,
        chinese: 25,
        indian: 9,
        others: 69,
        malayPct: 96.8,
        chinesePct: 0.8,
        indianPct: 0.3
      }
    },
    {
      name: 'PARIT JAYOS',
      code: '147/18/02',
      electorate: 2450,
      demographics: {
        malay: 2373,
        chinese: 0,
        indian: 0,
        others: 77,
        malayPct: 96.9,
        chinesePct: 0.0,
        indianPct: 0.0
      }
    },
    {
      name: 'PARIT DAYONG',
      code: '147/18/03',
      electorate: 2086,
      demographics: {
        malay: 2053,
        chinese: 2,
        indian: 3,
        others: 28,
        malayPct: 98.4,
        chinesePct: 0.1,
        indianPct: 0.1
      }
    },
    {
      name: 'KAMPONG SRI PASIR',
      code: '147/18/04',
      electorate: 3568,
      demographics: {
        malay: 3500,
        chinese: 25,
        indian: 3,
        others: 40,
        malayPct: 98.1,
        chinesePct: 0.7,
        indianPct: 0.1
      }
    },
    {
      name: 'SRI MEDAN BARAT',
      code: '147/18/05',
      electorate: 1598,
      demographics: {
        malay: 1578,
        chinese: 0,
        indian: 1,
        others: 19,
        malayPct: 98.7,
        chinesePct: 0.0,
        indianPct: 0.1
      }
    },
    {
      name: 'PARIT WARIJO',
      code: '147/18/06',
      electorate: 1149,
      demographics: {
        malay: 1059,
        chinese: 80,
        indian: 0,
        others: 10,
        malayPct: 92.2,
        chinesePct: 7.0,
        indianPct: 0.0
      }
    },
    {
      name: 'PARIT KARJAN',
      code: '147/18/07',
      electorate: 1224,
      demographics: {
        malay: 1195,
        chinese: 18,
        indian: 0,
        others: 11,
        malayPct: 97.6,
        chinesePct: 1.5,
        indianPct: 0.0
      }
    },
    {
      name: 'PARIT SULONG',
      code: '147/18/08',
      electorate: 1963,
      demographics: {
        malay: 1581,
        chinese: 279,
        indian: 15,
        others: 88,
        malayPct: 80.5,
        chinesePct: 14.2,
        indianPct: 0.8
      }
    },
    {
      name: 'BANDAR PARIT SULONG',
      code: '147/18/09',
      electorate: 2642,
      demographics: {
        malay: 1798,
        chinese: 764,
        indian: 36,
        others: 44,
        malayPct: 68.1,
        chinesePct: 28.9,
        indianPct: 1.4
      }
    },
    {
      name: 'SENTANG BATU',
      code: '147/18/10',
      electorate: 2078,
      demographics: {
        malay: 1979,
        chinese: 73,
        indian: 7,
        others: 19,
        malayPct: 95.2,
        chinesePct: 3.5,
        indianPct: 0.3
      }
    },
    {
      name: 'PARIT OTHMAN',
      code: '147/18/11',
      electorate: 2706,
      demographics: {
        malay: 2634,
        chinese: 36,
        indian: 3,
        others: 33,
        malayPct: 97.3,
        chinesePct: 1.3,
        indianPct: 0.1
      }
    },
    {
      name: 'PARIT HAJI SIRAJ',
      code: '147/18/12',
      electorate: 1474,
      demographics: {
        malay: 1372,
        chinese: 73,
        indian: 1,
        others: 28,
        malayPct: 93.1,
        chinesePct: 5.0,
        indianPct: 0.1
      }
    },
    {
      name: 'PARIT BETONG',
      code: '147/18/13',
      electorate: 652,
      demographics: {
        malay: 623,
        chinese: 23,
        indian: 0,
        others: 6,
        malayPct: 95.6,
        chinesePct: 3.5,
        indianPct: 0.0
      }
    },
    {
      name: 'PARIT ABDUL RAHMAN',
      code: '147/18/14',
      electorate: 1854,
      demographics: {
        malay: 1707,
        chinese: 127,
        indian: 3,
        others: 17,
        malayPct: 92.1,
        chinesePct: 6.9,
        indianPct: 0.2
      }
    },
    {
      name: 'BANDAR SRI MEDAN',
      code: '147/18/15',
      electorate: 2103,
      demographics: {
        malay: 1234,
        chinese: 812,
        indian: 14,
        others: 43,
        malayPct: 58.7,
        chinesePct: 38.6,
        indianPct: 0.7
      }
    },
    {
      name: 'SRI MEDAN TIMOR',
      code: '147/18/16',
      electorate: 1766,
      demographics: {
        malay: 1698,
        chinese: 49,
        indian: 3,
        others: 16,
        malayPct: 96.1,
        chinesePct: 2.8,
        indianPct: 0.2
      }
    },
    {
      name: 'AIR PUTIH',
      code: '147/18/17',
      electorate: 1331,
      demographics: {
        malay: 909,
        chinese: 367,
        indian: 1,
        others: 54,
        malayPct: 68.3,
        chinesePct: 27.6,
        indianPct: 0.1
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
