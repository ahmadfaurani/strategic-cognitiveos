/**
 * N35 Pasir Raja - Voter Roll Data
 * 
 * Source: Excel intelligence (as of 19 June 2026)
 * Parliament: P.155   TENGGARA
 * Total Electorate: 29,818
 * Demographics: Malay 69.0% / Chinese 18.3% / Indian 8.4%
 * 
 * Tiers:
 * - Tier 1 (Kingmaker/Chinese Base): 4 PDs
 * - Tier 2 (Mixed): 2 PDs
 * - Tier 3 (Malay Heartland): 7 PDs
 */

import { Seat, PollingDistrict } from '../types';

export const n35PasirRaja: Seat = {
  code: 'N35',
  name: 'Pasir Raja',
  federalCode: 'P.155',
  federalName: 'TENGGARA',
  district: 'Pasir Raja',  // TODO: Verify district
  totalElectorate: 29818,
  pollingDistricts: [
    {
      name: 'FELDA SUNGAI SAYONG',
      code: '155/35/01',
      electorate: 2983,
      demographics: {
        malay: 2934,
        chinese: 4,
        indian: 4,
        others: 41,
        malayPct: 98.4,
        chinesePct: 0.1,
        indianPct: 0.1
      }
    },
    {
      name: 'FELDA BUKIT BESAR',
      code: '155/35/02',
      electorate: 3210,
      demographics: {
        malay: 3145,
        chinese: 4,
        indian: 17,
        others: 44,
        malayPct: 98.0,
        chinesePct: 0.1,
        indianPct: 0.5
      }
    },
    {
      name: 'FELDA PASIR RAJA',
      code: '155/35/03',
      electorate: 2447,
      demographics: {
        malay: 2397,
        chinese: 4,
        indian: 9,
        others: 37,
        malayPct: 98.0,
        chinesePct: 0.2,
        indianPct: 0.4
      }
    },
    {
      name: 'FELDA BUKIT RAMUN',
      code: '155/35/04',
      electorate: 2050,
      demographics: {
        malay: 2028,
        chinese: 2,
        indian: 1,
        others: 19,
        malayPct: 98.9,
        chinesePct: 0.1,
        indianPct: 0.0
      }
    },
    {
      name: 'SUNGAI TELOR',
      code: '155/35/05',
      electorate: 972,
      demographics: {
        malay: 848,
        chinese: 10,
        indian: 76,
        others: 38,
        malayPct: 87.2,
        chinesePct: 1.0,
        indianPct: 7.8
      }
    },
    {
      name: 'SUNGAI JOHOR',
      code: '155/35/06',
      electorate: 1113,
      demographics: {
        malay: 848,
        chinese: 158,
        indian: 75,
        others: 32,
        malayPct: 76.2,
        chinesePct: 14.2,
        indianPct: 6.7
      }
    },
    {
      name: 'SUNGAI KEMANG SELATAN',
      code: '155/35/07',
      electorate: 715,
      demographics: {
        malay: 118,
        chinese: 527,
        indian: 56,
        others: 14,
        malayPct: 16.5,
        chinesePct: 73.7,
        indianPct: 7.8
      }
    },
    {
      name: 'JALAN BESAR',
      code: '155/35/08',
      electorate: 66,
      demographics: {
        malay: 7,
        chinese: 58,
        indian: 0,
        others: 1,
        malayPct: 10.6,
        chinesePct: 87.9,
        indianPct: 0.0
      }
    },
    {
      name: 'JALAN JOHOR',
      code: '155/35/09',
      electorate: 3692,
      demographics: {
        malay: 608,
        chinese: 2456,
        indian: 582,
        others: 46,
        malayPct: 16.5,
        chinesePct: 66.5,
        indianPct: 15.8
      }
    },
    {
      name: 'KOTA TINGGI SELATAN',
      code: '155/35/10',
      electorate: 3229,
      demographics: {
        malay: 1447,
        chinese: 1344,
        indian: 371,
        others: 67,
        malayPct: 44.8,
        chinesePct: 41.6,
        indianPct: 11.5
      }
    },
    {
      name: 'LADANG R.E.M.',
      code: '155/35/11',
      electorate: 355,
      demographics: {
        malay: 170,
        chinese: 5,
        indian: 160,
        others: 20,
        malayPct: 47.9,
        chinesePct: 1.4,
        indianPct: 45.1
      }
    },
    {
      name: 'JALAN KOTA TINGGI',
      code: '155/35/12',
      electorate: 8428,
      demographics: {
        malay: 5522,
        chinese: 875,
        indian: 1108,
        others: 923,
        malayPct: 65.5,
        chinesePct: 10.4,
        indianPct: 13.1
      }
    },
    {
      name: 'KAMPUNG BARU SUNGAI REDAN',
      code: '155/35/13',
      electorate: 558,
      demographics: {
        malay: 502,
        chinese: 1,
        indian: 43,
        others: 12,
        malayPct: 90.0,
        chinesePct: 0.2,
        indianPct: 7.7
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
