/**
 * N26 Tanjung Surat - Voter Roll Data
 * 
 * Source: Excel intelligence (as of 19 June 2026)
 * Parliament: P.157   PENGERANG
 * Total Electorate: 26,943
 * Demographics: Malay 80.8% / Chinese 15.3% / Indian 0.8%
 * 
 * Tiers:
 * - Tier 1 (Kingmaker/Chinese Base): 1 PDs
 * - Tier 2 (Mixed): 3 PDs
 * - Tier 3 (Malay Heartland): 10 PDs
 */

import { Seat, PollingDistrict } from '../types';

export const n26TanjungSurat: Seat = {
  code: 'N26',
  name: 'Tanjung Surat',
  federalCode: 'P.157',
  federalName: 'PENGERANG',
  district: 'Tanjung Surat',  // TODO: Verify district
  totalElectorate: 26943,
  pollingDistricts: [
    {
      name: 'TANJONG SURAT',
      code: '157/39/01',
      electorate: 468,
      demographics: {
        malay: 456,
        chinese: 8,
        indian: 1,
        others: 3,
        malayPct: 97.4,
        chinesePct: 1.7,
        indianPct: 0.2
      }
    },
    {
      name: 'TANJONG SERINDIT',
      code: '157/39/02',
      electorate: 633,
      demographics: {
        malay: 446,
        chinese: 47,
        indian: 95,
        others: 45,
        malayPct: 70.5,
        chinesePct: 7.4,
        indianPct: 15.0
      }
    },
    {
      name: 'ADELA',
      code: '157/39/03',
      electorate: 2994,
      demographics: {
        malay: 2979,
        chinese: 1,
        indian: 1,
        others: 13,
        malayPct: 99.5,
        chinesePct: 0.0,
        indianPct: 0.0
      }
    },
    {
      name: 'BUKIT TUNGGAL',
      code: '157/39/04',
      electorate: 3487,
      demographics: {
        malay: 3455,
        chinese: 5,
        indian: 11,
        others: 16,
        malayPct: 99.1,
        chinesePct: 0.1,
        indianPct: 0.3
      }
    },
    {
      name: 'SENING',
      code: '157/39/05',
      electorate: 3305,
      demographics: {
        malay: 3288,
        chinese: 2,
        indian: 3,
        others: 12,
        malayPct: 99.5,
        chinesePct: 0.1,
        indianPct: 0.1
      }
    },
    {
      name: 'BUKIT KELEDANG',
      code: '157/39/06',
      electorate: 2500,
      demographics: {
        malay: 2479,
        chinese: 3,
        indian: 10,
        others: 8,
        malayPct: 99.2,
        chinesePct: 0.1,
        indianPct: 0.4
      }
    },
    {
      name: 'LADANG SANTI',
      code: '157/39/07',
      electorate: 130,
      demographics: {
        malay: 86,
        chinese: 41,
        indian: 1,
        others: 2,
        malayPct: 66.2,
        chinesePct: 31.5,
        indianPct: 0.8
      }
    },
    {
      name: 'KAMPONG PASIR GOGOK',
      code: '157/39/08',
      electorate: 638,
      demographics: {
        malay: 441,
        chinese: 176,
        indian: 1,
        others: 20,
        malayPct: 69.1,
        chinesePct: 27.6,
        indianPct: 0.2
      }
    },
    {
      name: 'PENGERANG',
      code: '157/39/09',
      electorate: 2932,
      demographics: {
        malay: 2315,
        chinese: 173,
        indian: 38,
        others: 406,
        malayPct: 79.0,
        chinesePct: 5.9,
        indianPct: 1.3
      }
    },
    {
      name: 'KAMPONG JAWA',
      code: '157/39/10',
      electorate: 513,
      demographics: {
        malay: 313,
        chinese: 190,
        indian: 1,
        others: 9,
        malayPct: 61.0,
        chinesePct: 37.0,
        indianPct: 0.2
      }
    },
    {
      name: 'KAMPONG SUNGAI KAPAL',
      code: '157/39/11',
      electorate: 1610,
      demographics: {
        malay: 815,
        chinese: 772,
        indian: 1,
        others: 22,
        malayPct: 50.6,
        chinesePct: 48.0,
        indianPct: 0.1
      }
    },
    {
      name: 'LEPAU',
      code: '157/39/12',
      electorate: 194,
      demographics: {
        malay: 190,
        chinese: 0,
        indian: 0,
        others: 4,
        malayPct: 97.9,
        chinesePct: 0.0,
        indianPct: 0.0
      }
    },
    {
      name: 'SUNGAI RENGIT',
      code: '157/39/13',
      electorate: 1113,
      demographics: {
        malay: 793,
        chinese: 284,
        indian: 7,
        others: 29,
        malayPct: 71.2,
        chinesePct: 25.5,
        indianPct: 0.6
      }
    },
    {
      name: 'PEKAN SUNGAI RENGIT',
      code: '157/39/14',
      electorate: 1819,
      demographics: {
        malay: 216,
        chinese: 1560,
        indian: 10,
        others: 33,
        malayPct: 11.9,
        chinesePct: 85.8,
        indianPct: 0.5
      }
    },
    {
      name: 'TELOK RAMUNIA',
      code: '157/39/15',
      electorate: 4607,
      demographics: {
        malay: 3511,
        chinese: 869,
        indian: 25,
        others: 202,
        malayPct: 76.2,
        chinesePct: 18.9,
        indianPct: 0.5
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
