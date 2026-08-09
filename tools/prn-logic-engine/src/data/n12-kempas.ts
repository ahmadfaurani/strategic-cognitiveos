/**
 * N12 Kempas - Voter Roll Data
 * 
 * Source: Excel intelligence (as of 19 June 2026)
 * Parliament: P.161   PULAI
 * Total Electorate: 64,244
 * Demographics: Malay 56.5% / Chinese 29.3% / Indian 11.0%
 * 
 * Tiers:
 * - Tier 1 (Kingmaker/Chinese Base): 2 PDs
 * - Tier 2 (Mixed): 3 PDs
 * - Tier 3 (Malay Heartland): 7 PDs
 */

import { Seat, PollingDistrict } from '../types';

export const n12Kempas: Seat = {
  code: 'N12',
  name: 'Kempas',
  federalCode: 'P.161',
  federalName: 'PULAI',
  district: 'Kempas',  // TODO: Verify district
  totalElectorate: 64244,
  pollingDistricts: [
    {
      name: 'KEMPAS',
      code: '161/47/01',
      electorate: 4454,
      demographics: {
        malay: 1700,
        chinese: 1942,
        indian: 680,
        others: 132,
        malayPct: 38.2,
        chinesePct: 43.6,
        indianPct: 15.3
      }
    },
    {
      name: 'PERMATANG',
      code: '161/47/02',
      electorate: 1947,
      demographics: {
        malay: 1733,
        chinese: 109,
        indian: 42,
        others: 63,
        malayPct: 89.0,
        chinesePct: 5.6,
        indianPct: 2.2
      }
    },
    {
      name: 'LEMBAH KEMPAS',
      code: '161/47/03',
      electorate: 4241,
      demographics: {
        malay: 3095,
        chinese: 730,
        indian: 348,
        others: 68,
        malayPct: 73.0,
        chinesePct: 17.2,
        indianPct: 8.2
      }
    },
    {
      name: 'JALAN TAMPOI',
      code: '161/47/04',
      electorate: 3799,
      demographics: {
        malay: 2216,
        chinese: 916,
        indian: 515,
        others: 152,
        malayPct: 58.3,
        chinesePct: 24.1,
        indianPct: 13.6
      }
    },
    {
      name: 'DENAI',
      code: '161/47/05',
      electorate: 7717,
      demographics: {
        malay: 6737,
        chinese: 256,
        indian: 325,
        others: 399,
        malayPct: 87.3,
        chinesePct: 3.3,
        indianPct: 4.2
      }
    },
    {
      name: 'TAMAN SIANTAN',
      code: '161/47/06',
      electorate: 4090,
      demographics: {
        malay: 3516,
        chinese: 224,
        indian: 238,
        others: 112,
        malayPct: 86.0,
        chinesePct: 5.5,
        indianPct: 5.8
      }
    },
    {
      name: 'TAMAN JOHOR',
      code: '161/47/07',
      electorate: 5192,
      demographics: {
        malay: 1377,
        chinese: 2870,
        indian: 824,
        others: 121,
        malayPct: 26.5,
        chinesePct: 55.3,
        indianPct: 15.9
      }
    },
    {
      name: 'TAMAN CEMPAKA',
      code: '161/47/08',
      electorate: 5232,
      demographics: {
        malay: 2905,
        chinese: 1219,
        indian: 859,
        others: 249,
        malayPct: 55.5,
        chinesePct: 23.3,
        indianPct: 16.4
      }
    },
    {
      name: 'TAMAN DAHLIA',
      code: '161/47/09',
      electorate: 4021,
      demographics: {
        malay: 3106,
        chinese: 477,
        indian: 238,
        others: 200,
        malayPct: 77.2,
        chinesePct: 11.9,
        indianPct: 5.9
      }
    },
    {
      name: 'TAMAN KOBENA',
      code: '161/47/10',
      electorate: 1855,
      demographics: {
        malay: 1500,
        chinese: 130,
        indian: 167,
        others: 58,
        malayPct: 80.9,
        chinesePct: 7.0,
        indianPct: 9.0
      }
    },
    {
      name: 'DESA RAHMAT',
      code: '161/47/11',
      electorate: 3196,
      demographics: {
        malay: 2451,
        chinese: 480,
        indian: 193,
        others: 72,
        malayPct: 76.7,
        chinesePct: 15.0,
        indianPct: 6.0
      }
    },
    {
      name: 'PEKAN TAMPOI',
      code: '161/47/12',
      electorate: 3176,
      demographics: {
        malay: 271,
        chinese: 2710,
        indian: 145,
        others: 50,
        malayPct: 8.5,
        chinesePct: 85.3,
        indianPct: 4.6
      }
    },
    {
      name: 'BUKIT MEWAH',
      code: '161/47/13',
      electorate: 7938,
      demographics: {
        malay: 2795,
        chinese: 3570,
        indian: 1338,
        others: 235,
        malayPct: 35.2,
        chinesePct: 45.0,
        indianPct: 16.9
      }
    },
    {
      name: 'BUKIT KEMPAS',
      code: '161/47/14',
      electorate: 7386,
      demographics: {
        malay: 2885,
        chinese: 3181,
        indian: 1137,
        others: 183,
        malayPct: 39.1,
        chinesePct: 43.1,
        indianPct: 15.4
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
