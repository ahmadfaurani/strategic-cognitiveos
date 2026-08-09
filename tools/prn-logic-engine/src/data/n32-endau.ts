/**
 * N32 Endau - Voter Roll Data
 * 
 * Source: Excel intelligence (as of 19 June 2026)
 * Parliament: P.154   MERSING
 * Total Electorate: 28,767
 * Demographics: Malay 79.6% / Chinese 13.4% / Indian 0.7%
 * 
 * Tiers:
 * - Tier 1 (Kingmaker/Chinese Base): 1 PDs
 * - Tier 2 (Mixed): 1 PDs
 * - Tier 3 (Malay Heartland): 14 PDs
 */

import { Seat, PollingDistrict } from '../types';

export const n32Endau: Seat = {
  code: 'N32',
  name: 'Endau',
  federalCode: 'P.154',
  federalName: 'MERSING',
  district: 'Endau',  // TODO: Verify district
  totalElectorate: 28767,
  pollingDistricts: [
    {
      name: 'PADANG ENDAU',
      code: '154/32/01',
      electorate: 3581,
      demographics: {
        malay: 3046,
        chinese: 456,
        indian: 23,
        others: 56,
        malayPct: 85.1,
        chinesePct: 12.7,
        indianPct: 0.6
      }
    },
    {
      name: 'BANDAR ENDAU UTARA',
      code: '154/32/02',
      electorate: 3048,
      demographics: {
        malay: 1318,
        chinese: 1643,
        indian: 14,
        others: 73,
        malayPct: 43.2,
        chinesePct: 53.9,
        indianPct: 0.5
      }
    },
    {
      name: 'BANDAR ENDAU SELATAN',
      code: '154/32/03',
      electorate: 1521,
      demographics: {
        malay: 1058,
        chinese: 393,
        indian: 13,
        others: 57,
        malayPct: 69.6,
        chinesePct: 25.8,
        indianPct: 0.9
      }
    },
    {
      name: 'KAMPUNG HUBONG',
      code: '154/32/04',
      electorate: 1716,
      demographics: {
        malay: 1304,
        chinese: 15,
        indian: 3,
        others: 394,
        malayPct: 76.0,
        chinesePct: 0.9,
        indianPct: 0.2
      }
    },
    {
      name: 'KAMPUNG HUBONG BARAT',
      code: '154/32/05',
      electorate: 970,
      demographics: {
        malay: 596,
        chinese: 364,
        indian: 0,
        others: 10,
        malayPct: 61.4,
        chinesePct: 37.5,
        indianPct: 0.0
      }
    },
    {
      name: 'RANCANGAN FELDA ENDAU',
      code: '154/32/06',
      electorate: 1137,
      demographics: {
        malay: 1124,
        chinese: 1,
        indian: 1,
        others: 11,
        malayPct: 98.9,
        chinesePct: 0.1,
        indianPct: 0.1
      }
    },
    {
      name: 'TRIANG',
      code: '154/32/07',
      electorate: 1398,
      demographics: {
        malay: 1376,
        chinese: 10,
        indian: 3,
        others: 9,
        malayPct: 98.4,
        chinesePct: 0.7,
        indianPct: 0.2
      }
    },
    {
      name: 'PENYABONG',
      code: '154/32/08',
      electorate: 847,
      demographics: {
        malay: 834,
        chinese: 0,
        indian: 1,
        others: 12,
        malayPct: 98.5,
        chinesePct: 0.0,
        indianPct: 0.1
      }
    },
    {
      name: 'TANJONG RESANG',
      code: '154/32/09',
      electorate: 324,
      demographics: {
        malay: 315,
        chinese: 0,
        indian: 1,
        others: 8,
        malayPct: 97.2,
        chinesePct: 0.0,
        indianPct: 0.3
      }
    },
    {
      name: 'AYER PAPAN',
      code: '154/32/10',
      electorate: 611,
      demographics: {
        malay: 600,
        chinese: 3,
        indian: 0,
        others: 8,
        malayPct: 98.2,
        chinesePct: 0.5,
        indianPct: 0.0
      }
    },
    {
      name: 'TANJONG GENTING',
      code: '154/32/11',
      electorate: 834,
      demographics: {
        malay: 815,
        chinese: 1,
        indian: 5,
        others: 13,
        malayPct: 97.7,
        chinesePct: 0.1,
        indianPct: 0.6
      }
    },
    {
      name: 'MERSING KANAN',
      code: '154/32/12',
      electorate: 1792,
      demographics: {
        malay: 1667,
        chinese: 88,
        indian: 16,
        others: 21,
        malayPct: 93.0,
        chinesePct: 4.9,
        indianPct: 0.9
      }
    },
    {
      name: 'JALAN ENDAU',
      code: '154/32/13',
      electorate: 4370,
      demographics: {
        malay: 3677,
        chinese: 594,
        indian: 50,
        others: 49,
        malayPct: 84.1,
        chinesePct: 13.6,
        indianPct: 1.1
      }
    },
    {
      name: 'JALAN ABDULLAH',
      code: '154/32/14',
      electorate: 717,
      demographics: {
        malay: 667,
        chinese: 35,
        indian: 11,
        others: 4,
        malayPct: 93.0,
        chinesePct: 4.9,
        indianPct: 1.5
      }
    },
    {
      name: 'KAMPONG TENGAH',
      code: '154/32/15',
      electorate: 817,
      demographics: {
        malay: 721,
        chinese: 78,
        indian: 3,
        others: 15,
        malayPct: 88.2,
        chinesePct: 9.5,
        indianPct: 0.4
      }
    },
    {
      name: 'SAWAH DATO`',
      code: '154/32/16',
      electorate: 2650,
      demographics: {
        malay: 2398,
        chinese: 144,
        indian: 56,
        others: 52,
        malayPct: 90.5,
        chinesePct: 5.4,
        indianPct: 2.1
      }
    },
    {
      name: 'TENGLU',
      code: '154/32/17',
      electorate: 1407,
      demographics: {
        malay: 1374,
        chinese: 16,
        indian: 3,
        others: 14,
        malayPct: 97.7,
        chinesePct: 1.1,
        indianPct: 0.2
      }
    },
    {
      name: 'TANAH ABANG',
      code: '154/32/18',
      electorate: 580,
      demographics: {
        malay: 13,
        chinese: 9,
        indian: 0,
        others: 558,
        malayPct: 2.2,
        chinesePct: 1.6,
        indianPct: 0.0
      }
    },
    {
      name: 'KAMPONG PUNAN',
      code: '154/32/19',
      electorate: 234,
      demographics: {
        malay: 6,
        chinese: 7,
        indian: 0,
        others: 221,
        malayPct: 2.6,
        chinesePct: 3.0,
        indianPct: 0.0
      }
    },
    {
      name: 'KAMPONG PETA',
      code: '154/32/20',
      electorate: 213,
      demographics: {
        malay: 2,
        chinese: 1,
        indian: 1,
        others: 209,
        malayPct: 0.9,
        chinesePct: 0.5,
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
