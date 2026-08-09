/**
 * N13 Bukit Batu - Voter Roll Data
 * 
 * Source: Excel intelligence (as of 19 June 2026)
 * Parliament: P.163   KULAI
 * Total Electorate: 49,963
 * Demographics: Malay 37.5% / Chinese 52.0% / Indian 8.5%
 * 
 * Tiers:
 * - Tier 1 (Kingmaker/Chinese Base): 8 PDs
 * - Tier 2 (Mixed): 3 PDs
 * - Tier 3 (Malay Heartland): 3 PDs
 */

import { Seat, PollingDistrict } from '../types';

export const n13BukitBatu: Seat = {
  code: 'N13',
  name: 'Bukit Batu',
  federalCode: 'P.163',
  federalName: 'KULAI',
  district: 'Bukit Batu',  // TODO: Verify district
  totalElectorate: 49963,
  pollingDistricts: [
    {
      name: 'ULU CHOH',
      code: '163/51/01',
      electorate: 557,
      demographics: {
        malay: 213,
        chinese: 220,
        indian: 115,
        others: 9,
        malayPct: 38.2,
        chinesePct: 39.5,
        indianPct: 20.6
      }
    },
    {
      name: 'BANDAR ULU CHOH',
      code: '163/51/02',
      electorate: 1674,
      demographics: {
        malay: 404,
        chinese: 1186,
        indian: 63,
        others: 21,
        malayPct: 24.1,
        chinesePct: 70.8,
        indianPct: 3.8
      }
    },
    {
      name: 'KAMPONG RAHMAT',
      code: '163/51/03',
      electorate: 5966,
      demographics: {
        malay: 3543,
        chinese: 1688,
        indian: 563,
        others: 172,
        malayPct: 59.4,
        chinesePct: 28.3,
        indianPct: 9.4
      }
    },
    {
      name: 'BUKIT BATU',
      code: '163/51/04',
      electorate: 4005,
      demographics: {
        malay: 1172,
        chinese: 2652,
        indian: 104,
        others: 77,
        malayPct: 29.3,
        chinesePct: 66.2,
        indianPct: 2.6
      }
    },
    {
      name: 'AYER MANIS',
      code: '163/51/05',
      electorate: 1276,
      demographics: {
        malay: 1178,
        chinese: 52,
        indian: 19,
        others: 27,
        malayPct: 92.3,
        chinesePct: 4.1,
        indianPct: 1.5
      }
    },
    {
      name: 'FELDA BUKIT BATU',
      code: '163/51/06',
      electorate: 2423,
      demographics: {
        malay: 2373,
        chinese: 22,
        indian: 5,
        others: 23,
        malayPct: 97.9,
        chinesePct: 0.9,
        indianPct: 0.2
      }
    },
    {
      name: 'AYER BEMBAN',
      code: '163/51/07',
      electorate: 1936,
      demographics: {
        malay: 448,
        chinese: 1358,
        indian: 99,
        others: 31,
        malayPct: 23.1,
        chinesePct: 70.1,
        indianPct: 5.1
      }
    },
    {
      name: 'MIDLAND KULAI YOUNG',
      code: '163/51/08',
      electorate: 820,
      demographics: {
        malay: 750,
        chinese: 20,
        indian: 34,
        others: 16,
        malayPct: 91.5,
        chinesePct: 2.4,
        indianPct: 4.1
      }
    },
    {
      name: 'PEKAN KELAPA SAWIT BARAT',
      code: '163/51/09',
      electorate: 2399,
      demographics: {
        malay: 128,
        chinese: 2193,
        indian: 51,
        others: 27,
        malayPct: 5.3,
        chinesePct: 91.4,
        indianPct: 2.1
      }
    },
    {
      name: 'PEKAN KELAPA SAWIT TENGAH',
      code: '163/51/10',
      electorate: 2996,
      demographics: {
        malay: 575,
        chinese: 2303,
        indian: 88,
        others: 30,
        malayPct: 19.2,
        chinesePct: 76.9,
        indianPct: 2.9
      }
    },
    {
      name: 'PEKAN KELAPA SAWIT TIMOR',
      code: '163/51/11',
      electorate: 1702,
      demographics: {
        malay: 58,
        chinese: 1596,
        indian: 42,
        others: 6,
        malayPct: 3.4,
        chinesePct: 93.8,
        indianPct: 2.5
      }
    },
    {
      name: 'KAMPONG SRI PAYA',
      code: '163/51/12',
      electorate: 4066,
      demographics: {
        malay: 1871,
        chinese: 1572,
        indian: 533,
        others: 90,
        malayPct: 46.0,
        chinesePct: 38.7,
        indianPct: 13.1
      }
    },
    {
      name: 'KOTA KULAI',
      code: '163/51/13',
      electorate: 4376,
      demographics: {
        malay: 621,
        chinese: 3238,
        indian: 445,
        others: 72,
        malayPct: 14.2,
        chinesePct: 74.0,
        indianPct: 10.2
      }
    },
    {
      name: 'TAMAN PUTRI',
      code: '163/51/14',
      electorate: 7816,
      demographics: {
        malay: 2017,
        chinese: 4685,
        indian: 978,
        others: 136,
        malayPct: 25.8,
        chinesePct: 59.9,
        indianPct: 12.5
      }
    },
    {
      name: 'TAMAN PERMAI',
      code: '163/51/15',
      electorate: 7951,
      demographics: {
        malay: 3380,
        chinese: 3214,
        indian: 1120,
        others: 237,
        malayPct: 42.5,
        chinesePct: 40.4,
        indianPct: 14.1
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
