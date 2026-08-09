/**
 * N14 Pulai Sebatang - Voter Roll Data
 * 
 * Source: Excel intelligence (as of 19 June 2026)
 * Parliament: P.164   PONTIAN
 * Total Electorate: 47,651
 * Demographics: Malay 62.3% / Chinese 33.2% / Indian 1.5%
 * 
 * Tiers:
 * - Tier 1 (Kingmaker/Chinese Base): 4 PDs
 * - Tier 2 (Mixed): 3 PDs
 * - Tier 3 (Malay Heartland): 13 PDs
 */

import { Seat, PollingDistrict } from '../types';

export const n14PulaiSebatang: Seat = {
  code: 'N14',
  name: 'Pulai Sebatang',
  federalCode: 'P.164',
  federalName: 'PONTIAN',
  district: 'Pulai Sebatang',  // TODO: Verify district
  totalElectorate: 47651,
  pollingDistricts: [
    {
      name: 'KAMPONG PARIT KAHAR',
      code: '164/54/01',
      electorate: 1257,
      demographics: {
        malay: 1218,
        chinese: 18,
        indian: 1,
        others: 20,
        malayPct: 96.9,
        chinesePct: 1.4,
        indianPct: 0.1
      }
    },
    {
      name: 'PARIT KEROMA',
      code: '164/54/02',
      electorate: 1505,
      demographics: {
        malay: 1150,
        chinese: 314,
        indian: 2,
        others: 39,
        malayPct: 76.4,
        chinesePct: 20.9,
        indianPct: 0.1
      }
    },
    {
      name: 'AYER BALOI',
      code: '164/54/03',
      electorate: 564,
      demographics: {
        malay: 490,
        chinese: 63,
        indian: 0,
        others: 11,
        malayPct: 86.9,
        chinesePct: 11.2,
        indianPct: 0.0
      }
    },
    {
      name: 'BANDAR AYER BALOI SELATAN',
      code: '164/54/04',
      electorate: 978,
      demographics: {
        malay: 793,
        chinese: 159,
        indian: 4,
        others: 22,
        malayPct: 81.1,
        chinesePct: 16.3,
        indianPct: 0.4
      }
    },
    {
      name: 'BANDAR AYER BALOI UTARA',
      code: '164/54/05',
      electorate: 3147,
      demographics: {
        malay: 2719,
        chinese: 362,
        indian: 8,
        others: 58,
        malayPct: 86.4,
        chinesePct: 11.5,
        indianPct: 0.3
      }
    },
    {
      name: 'PARIT PANJANG',
      code: '164/54/06',
      electorate: 257,
      demographics: {
        malay: 236,
        chinese: 19,
        indian: 2,
        others: 0,
        malayPct: 91.8,
        chinesePct: 7.4,
        indianPct: 0.8
      }
    },
    {
      name: 'KAMPONG PARIT HAJI KARIM',
      code: '164/54/07',
      electorate: 1142,
      demographics: {
        malay: 1113,
        chinese: 19,
        indian: 2,
        others: 8,
        malayPct: 97.5,
        chinesePct: 1.7,
        indianPct: 0.2
      }
    },
    {
      name: 'PARIT SIKOM',
      code: '164/54/08',
      electorate: 2630,
      demographics: {
        malay: 1970,
        chinese: 623,
        indian: 6,
        others: 31,
        malayPct: 74.9,
        chinesePct: 23.7,
        indianPct: 0.2
      }
    },
    {
      name: 'KAMPONG JAWA',
      code: '164/54/09',
      electorate: 501,
      demographics: {
        malay: 402,
        chinese: 95,
        indian: 0,
        others: 4,
        malayPct: 80.2,
        chinesePct: 19.0,
        indianPct: 0.0
      }
    },
    {
      name: 'PULAI SEBATANG',
      code: '164/54/10',
      electorate: 3968,
      demographics: {
        malay: 3273,
        chinese: 558,
        indian: 9,
        others: 128,
        malayPct: 82.5,
        chinesePct: 14.1,
        indianPct: 0.2
      }
    },
    {
      name: 'API-API',
      code: '164/54/11',
      electorate: 996,
      demographics: {
        malay: 831,
        chinese: 123,
        indian: 1,
        others: 41,
        malayPct: 83.4,
        chinesePct: 12.3,
        indianPct: 0.1
      }
    },
    {
      name: 'SUNGAI TRUS',
      code: '164/54/12',
      electorate: 3189,
      demographics: {
        malay: 2454,
        chinese: 668,
        indian: 11,
        others: 56,
        malayPct: 77.0,
        chinesePct: 20.9,
        indianPct: 0.3
      }
    },
    {
      name: 'PONTIAN BESAR KIRI',
      code: '164/54/13',
      electorate: 2384,
      demographics: {
        malay: 1736,
        chinese: 481,
        indian: 10,
        others: 157,
        malayPct: 72.8,
        chinesePct: 20.2,
        indianPct: 0.4
      }
    },
    {
      name: 'JALAN ALSAGOFF',
      code: '164/54/14',
      electorate: 6172,
      demographics: {
        malay: 3524,
        chinese: 2088,
        indian: 265,
        others: 295,
        malayPct: 57.1,
        chinesePct: 33.8,
        indianPct: 4.3
      }
    },
    {
      name: 'PANTAI BANDAR PONTIAN',
      code: '164/54/15',
      electorate: 413,
      demographics: {
        malay: 134,
        chinese: 259,
        indian: 11,
        others: 9,
        malayPct: 32.4,
        chinesePct: 62.7,
        indianPct: 2.7
      }
    },
    {
      name: 'PEGAWAI',
      code: '164/54/16',
      electorate: 974,
      demographics: {
        malay: 519,
        chinese: 407,
        indian: 33,
        others: 15,
        malayPct: 53.3,
        chinesePct: 41.8,
        indianPct: 3.4
      }
    },
    {
      name: 'JALAN TAIB',
      code: '164/54/17',
      electorate: 2152,
      demographics: {
        malay: 346,
        chinese: 1738,
        indian: 45,
        others: 23,
        malayPct: 16.1,
        chinesePct: 80.8,
        indianPct: 2.1
      }
    },
    {
      name: 'BAKEK',
      code: '164/54/18',
      electorate: 2353,
      demographics: {
        malay: 142,
        chinese: 2181,
        indian: 13,
        others: 17,
        malayPct: 6.0,
        chinesePct: 92.7,
        indianPct: 0.6
      }
    },
    {
      name: 'PARIT SEMERAH',
      code: '164/54/19',
      electorate: 4032,
      demographics: {
        malay: 2820,
        chinese: 870,
        indian: 136,
        others: 206,
        malayPct: 69.9,
        chinesePct: 21.6,
        indianPct: 3.4
      }
    },
    {
      name: 'PARIT MESJID',
      code: '164/54/20',
      electorate: 4874,
      demographics: {
        malay: 1474,
        chinese: 3117,
        indian: 75,
        others: 208,
        malayPct: 30.2,
        chinesePct: 64.0,
        indianPct: 1.5
      }
    },
    {
      name: 'PARIT MESJID DARAT',
      code: '164/54/21',
      electorate: 4163,
      demographics: {
        malay: 2323,
        chinese: 1672,
        indian: 71,
        others: 97,
        malayPct: 55.8,
        chinesePct: 40.2,
        indianPct: 1.7
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
