/**
 * N33 Tenggaroh - Voter Roll Data
 * 
 * Source: Excel intelligence (as of 19 June 2026)
 * Parliament: P.154   MERSING
 * Total Electorate: 39,001
 * Demographics: Malay 83.3% / Chinese 12.7% / Indian 1.4%
 * 
 * Tiers:
 * - Tier 1 (Kingmaker/Chinese Base): 4 PDs
 * - Tier 2 (Mixed): 0 PDs
 * - Tier 3 (Malay Heartland): 18 PDs
 */

import { Seat, PollingDistrict } from '../types';

export const n33Tenggaroh: Seat = {
  code: 'N33',
  name: 'Tenggaroh',
  federalCode: 'P.154',
  federalName: 'MERSING',
  district: 'Tenggaroh',  // TODO: Verify district
  totalElectorate: 39001,
  pollingDistricts: [
    {
      name: 'BANDAR UTARA',
      code: '154/33/01',
      electorate: 527,
      demographics: {
        malay: 105,
        chinese: 413,
        indian: 7,
        others: 2,
        malayPct: 19.9,
        chinesePct: 78.4,
        indianPct: 1.3
      }
    },
    {
      name: 'JALAN JAMALUANG',
      code: '154/33/02',
      electorate: 1220,
      demographics: {
        malay: 409,
        chinese: 768,
        indian: 22,
        others: 21,
        malayPct: 33.5,
        chinesePct: 63.0,
        indianPct: 1.8
      }
    },
    {
      name: 'FELDA NITAR 2',
      code: '154/33/03',
      electorate: 2989,
      demographics: {
        malay: 2935,
        chinese: 5,
        indian: 7,
        others: 42,
        malayPct: 98.2,
        chinesePct: 0.2,
        indianPct: 0.2
      }
    },
    {
      name: 'FELDA NITAR 1',
      code: '154/33/04',
      electorate: 2570,
      demographics: {
        malay: 2553,
        chinese: 2,
        indian: 3,
        others: 12,
        malayPct: 99.3,
        chinesePct: 0.1,
        indianPct: 0.1
      }
    },
    {
      name: 'PENGKALAN BATU',
      code: '154/33/05',
      electorate: 3184,
      demographics: {
        malay: 2374,
        chinese: 690,
        indian: 87,
        others: 33,
        malayPct: 74.6,
        chinesePct: 21.7,
        indianPct: 2.7
      }
    },
    {
      name: 'JALAN ISMAIL',
      code: '154/33/06',
      electorate: 377,
      demographics: {
        malay: 262,
        chinese: 79,
        indian: 33,
        others: 3,
        malayPct: 69.5,
        chinesePct: 21.0,
        indianPct: 8.8
      }
    },
    {
      name: 'PEJABAT KERAJAAN',
      code: '154/33/07',
      electorate: 994,
      demographics: {
        malay: 684,
        chinese: 252,
        indian: 17,
        others: 41,
        malayPct: 68.8,
        chinesePct: 25.4,
        indianPct: 1.7
      }
    },
    {
      name: 'PEKAN MERSING KECHIL',
      code: '154/33/08',
      electorate: 4419,
      demographics: {
        malay: 3119,
        chinese: 988,
        indian: 275,
        others: 37,
        malayPct: 70.6,
        chinesePct: 22.4,
        indianPct: 6.2
      }
    },
    {
      name: 'SRI PANTAI',
      code: '154/33/09',
      electorate: 5869,
      demographics: {
        malay: 5061,
        chinese: 67,
        indian: 61,
        others: 680,
        malayPct: 86.2,
        chinesePct: 1.1,
        indianPct: 1.0
      }
    },
    {
      name: 'BANDAR JAMALUANG TIMOR',
      code: '154/33/10',
      electorate: 797,
      demographics: {
        malay: 29,
        chinese: 758,
        indian: 5,
        others: 5,
        malayPct: 3.6,
        chinesePct: 95.1,
        indianPct: 0.6
      }
    },
    {
      name: 'JAMALUANG TIMOR',
      code: '154/33/11',
      electorate: 558,
      demographics: {
        malay: 556,
        chinese: 0,
        indian: 0,
        others: 2,
        malayPct: 99.6,
        chinesePct: 0.0,
        indianPct: 0.0
      }
    },
    {
      name: 'JAMALUANG',
      code: '154/33/12',
      electorate: 1061,
      demographics: {
        malay: 86,
        chinese: 937,
        indian: 9,
        others: 29,
        malayPct: 8.1,
        chinesePct: 88.3,
        indianPct: 0.8
      }
    },
    {
      name: 'RISDA SUNGAI AMBAT',
      code: '154/33/13',
      electorate: 316,
      demographics: {
        malay: 302,
        chinese: 1,
        indian: 5,
        others: 8,
        malayPct: 95.6,
        chinesePct: 0.3,
        indianPct: 1.6
      }
    },
    {
      name: 'FELDA TENGGAROH 5',
      code: '154/33/14',
      electorate: 3383,
      demographics: {
        malay: 3367,
        chinese: 2,
        indian: 1,
        others: 13,
        malayPct: 99.5,
        chinesePct: 0.1,
        indianPct: 0.0
      }
    },
    {
      name: 'FELDA TENGGAROH 3',
      code: '154/33/15',
      electorate: 1258,
      demographics: {
        malay: 1252,
        chinese: 0,
        indian: 1,
        others: 5,
        malayPct: 99.5,
        chinesePct: 0.0,
        indianPct: 0.1
      }
    },
    {
      name: 'FELDA TENGGAROH 6',
      code: '154/33/16',
      electorate: 1827,
      demographics: {
        malay: 1810,
        chinese: 2,
        indian: 2,
        others: 13,
        malayPct: 99.1,
        chinesePct: 0.1,
        indianPct: 0.1
      }
    },
    {
      name: 'FELDA TENGGAROH 4',
      code: '154/33/17',
      electorate: 603,
      demographics: {
        malay: 600,
        chinese: 2,
        indian: 0,
        others: 1,
        malayPct: 99.5,
        chinesePct: 0.3,
        indianPct: 0.0
      }
    },
    {
      name: 'FELDA TENGGAROH 2',
      code: '154/33/18',
      electorate: 3944,
      demographics: {
        malay: 3893,
        chinese: 1,
        indian: 16,
        others: 34,
        malayPct: 98.7,
        chinesePct: 0.0,
        indianPct: 0.4
      }
    },
    {
      name: 'FELDA TENGGAROH 1',
      code: '154/33/19',
      electorate: 2415,
      demographics: {
        malay: 2397,
        chinese: 0,
        indian: 3,
        others: 15,
        malayPct: 99.3,
        chinesePct: 0.0,
        indianPct: 0.1
      }
    },
    {
      name: 'PULAU SIBU',
      code: '154/33/20',
      electorate: 175,
      demographics: {
        malay: 170,
        chinese: 2,
        indian: 0,
        others: 3,
        malayPct: 97.1,
        chinesePct: 1.1,
        indianPct: 0.0
      }
    },
    {
      name: 'PULAU TINGGI',
      code: '154/33/21',
      electorate: 211,
      demographics: {
        malay: 204,
        chinese: 0,
        indian: 0,
        others: 7,
        malayPct: 96.7,
        chinesePct: 0.0,
        indianPct: 0.0
      }
    },
    {
      name: 'PULAU BESAR',
      code: '154/33/22',
      electorate: 32,
      demographics: {
        malay: 29,
        chinese: 3,
        indian: 0,
        others: 0,
        malayPct: 90.6,
        chinesePct: 9.4,
        indianPct: 0.0
      }
    },
    {
      name: 'PULAU AUR',
      code: '154/33/23',
      electorate: 181,
      demographics: {
        malay: 181,
        chinese: 0,
        indian: 0,
        others: 0,
        malayPct: 100.0,
        chinesePct: 0.0,
        indianPct: 0.0
      }
    },
    {
      name: 'PULAU PEMANGGIL',
      code: '154/33/24',
      electorate: 91,
      demographics: {
        malay: 91,
        chinese: 0,
        indian: 0,
        others: 0,
        malayPct: 100.0,
        chinesePct: 0.0,
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
