/**
 * N41 Puteri Wangsa - Voter Roll Data
 * 
 * Source: Excel intelligence (as of 19 June 2026)
 * Parliament: P.158   TEBRAU
 * Total Electorate: 128,723
 * Demographics: Malay 35.9% / Chinese 51.4% / Indian 10.0%
 * 
 * Tiers:
 * - Tier 1 (Kingmaker/Chinese Base): 11 PDs
 * - Tier 2 (Mixed): 4 PDs
 * - Tier 3 (Malay Heartland): 3 PDs
 */

import { Seat, PollingDistrict } from '../types';

export const n41PuteriWangsa: Seat = {
  code: 'N41',
  name: 'Puteri Wangsa',
  federalCode: 'P.158',
  federalName: 'TEBRAU',
  district: 'Puteri Wangsa',  // TODO: Verify district
  totalElectorate: 128723,
  pollingDistricts: [
    {
      name: 'FELDA ULU TEBRAU',
      code: '158/41/01',
      electorate: 5618,
      demographics: {
        malay: 5297,
        chinese: 27,
        indian: 213,
        others: 81,
        malayPct: 94.3,
        chinesePct: 0.5,
        indianPct: 3.8
      }
    },
    {
      name: 'MAJU JAYA',
      code: '158/41/02',
      electorate: 5229,
      demographics: {
        malay: 4353,
        chinese: 311,
        indian: 299,
        others: 266,
        malayPct: 83.2,
        chinesePct: 5.9,
        indianPct: 5.7
      }
    },
    {
      name: 'NIPAH DELIMA',
      code: '158/41/03',
      electorate: 2440,
      demographics: {
        malay: 1050,
        chinese: 1070,
        indian: 250,
        others: 70,
        malayPct: 43.0,
        chinesePct: 43.9,
        indianPct: 10.2
      }
    },
    {
      name: 'PUTERI WANGSA 1',
      code: '158/41/04',
      electorate: 10553,
      demographics: {
        malay: 2514,
        chinese: 5747,
        indian: 1991,
        others: 301,
        malayPct: 23.8,
        chinesePct: 54.5,
        indianPct: 18.9
      }
    },
    {
      name: 'MOUNT AUSTIN',
      code: '158/41/05',
      electorate: 14058,
      demographics: {
        malay: 2778,
        chinese: 9803,
        indian: 1229,
        others: 248,
        malayPct: 19.8,
        chinesePct: 69.7,
        indianPct: 8.7
      }
    },
    {
      name: 'BERTAM DELIMA',
      code: '158/41/06',
      electorate: 2620,
      demographics: {
        malay: 796,
        chinese: 1454,
        indian: 290,
        others: 80,
        malayPct: 30.4,
        chinesePct: 55.5,
        indianPct: 11.1
      }
    },
    {
      name: 'PEKAN PANDAN',
      code: '158/41/07',
      electorate: 3463,
      demographics: {
        malay: 896,
        chinese: 2178,
        indian: 245,
        others: 144,
        malayPct: 25.9,
        chinesePct: 62.9,
        indianPct: 7.1
      }
    },
    {
      name: 'KANGKAR TEBRAU BARU',
      code: '158/41/08',
      electorate: 1819,
      demographics: {
        malay: 1066,
        chinese: 458,
        indian: 231,
        others: 64,
        malayPct: 58.6,
        chinesePct: 25.2,
        indianPct: 12.7
      }
    },
    {
      name: 'KANGKAR TEBRAU',
      code: '158/41/09',
      electorate: 1657,
      demographics: {
        malay: 1279,
        chinese: 124,
        indian: 171,
        others: 83,
        malayPct: 77.2,
        chinesePct: 7.5,
        indianPct: 10.3
      }
    },
    {
      name: 'LADANG TEBRAU',
      code: '158/41/10',
      electorate: 7925,
      demographics: {
        malay: 5080,
        chinese: 2023,
        indian: 530,
        others: 292,
        malayPct: 64.1,
        chinesePct: 25.5,
        indianPct: 6.7
      }
    },
    {
      name: 'TAMAN GEMBIRA',
      code: '158/41/11',
      electorate: 2190,
      demographics: {
        malay: 1490,
        chinese: 340,
        indian: 90,
        others: 270,
        malayPct: 68.0,
        chinesePct: 15.5,
        indianPct: 4.1
      }
    },
    {
      name: 'BUKIT JAYA',
      code: '158/41/12',
      electorate: 6050,
      demographics: {
        malay: 1380,
        chinese: 2888,
        indian: 1634,
        others: 148,
        malayPct: 22.8,
        chinesePct: 47.7,
        indianPct: 27.0
      }
    },
    {
      name: 'RUMBIA DAYA',
      code: '158/41/13',
      electorate: 5444,
      demographics: {
        malay: 1773,
        chinese: 3035,
        indian: 521,
        others: 115,
        malayPct: 32.6,
        chinesePct: 55.7,
        indianPct: 9.6
      }
    },
    {
      name: 'NIBONG DAYA',
      code: '158/41/14',
      electorate: 5016,
      demographics: {
        malay: 1949,
        chinese: 2536,
        indian: 413,
        others: 118,
        malayPct: 38.9,
        chinesePct: 50.6,
        indianPct: 8.2
      }
    },
    {
      name: 'PUTERI WANGSA 2',
      code: '158/41/15',
      electorate: 4996,
      demographics: {
        malay: 1274,
        chinese: 2550,
        indian: 1068,
        others: 104,
        malayPct: 25.5,
        chinesePct: 51.0,
        indianPct: 21.4
      }
    },
    {
      name: 'PELANGI GAYA',
      code: '158/41/16',
      electorate: 10979,
      demographics: {
        malay: 1562,
        chinese: 8641,
        indian: 593,
        others: 183,
        malayPct: 14.2,
        chinesePct: 78.7,
        indianPct: 5.4
      }
    },
    {
      name: 'PINANG SAGU',
      code: '158/41/17',
      electorate: 5795,
      demographics: {
        malay: 1924,
        chinese: 3210,
        indian: 445,
        others: 216,
        malayPct: 33.2,
        chinesePct: 55.4,
        indianPct: 7.7
      }
    },
    {
      name: 'SETIA ENAU',
      code: '158/41/18',
      electorate: 17282,
      demographics: {
        malay: 4372,
        chinese: 11373,
        indian: 1217,
        others: 320,
        malayPct: 25.3,
        chinesePct: 65.8,
        indianPct: 7.0
      }
    },
    {
      name: 'BUKIT MUTIARA',
      code: '158/41/19',
      electorate: 8242,
      demographics: {
        malay: 4000,
        chinese: 3046,
        indian: 1040,
        others: 156,
        malayPct: 48.5,
        chinesePct: 37.0,
        indianPct: 12.6
      }
    },
    {
      name: 'DESA TEBRAU',
      code: '158/41/20',
      electorate: 7347,
      demographics: {
        malay: 1336,
        chinese: 5382,
        indian: 460,
        others: 169,
        malayPct: 18.2,
        chinesePct: 73.3,
        indianPct: 6.3
      }
    },
  ],
  candidates: {
    bn: {
      name: 'Teow Chia Ling',
      coalition: 'BN',
      party: 'MCA',
      incumbent: false,
      profile: 'Focusing on local-service credibility (congestion, public facilities). MCA candidate in Chinese-majority seat — structural challenge as BN Chinese vote share collapsed since 2013.'
    },
    ph: {
      name: 'Dr Maszlee Malik',
      coalition: 'PH',
      party: 'PKR',
      incumbent: false,
      profile: 'Former Education Minister (2018-2020). PH deploying heavyweight to reclaim seat. Campaign: Youth appeal, education reform, federal coattails. Strengths: Name recognition, technocratic credibility. Vulnerability: Not local Johor figure, must overcome MUDA incumbent legacy.'
    },
    pn: {
      name: 'TBD',
      coalition: 'PN',
      party: 'BERSATU',
      incumbent: false,
      profile: 'PN candidate TBD. Structural challenge in 51.4% Chinese seat — PN ceiling likely 15-25% unless Malay consolidation exceeds expectations.'
    },
    muda: {
      name: 'Rashifa Aljunied',
      coalition: 'MUDA',
      party: 'MUDA',
      incumbent: false,
      profile: '26 years old, Chief of Staff to MUDA President. Youth appeal play. Incumbent Amira Aisya NOT defending. MUDA won in 2022 (7,114 majority) but facing retention challenge without incumbent\'s personal mandate.'
    },
    bersama: {
      name: 'Nicholas Paul Vincent',
      coalition: 'Bersama',
      party: 'Parti Bersama',
      incumbent: false,
      profile: 'Entering progressive southern Johor seat. Splitting reform vote with PH and MUDA.'
    }
  },
  notes: [
    'Five-cornered fight expected (PH, BN, MUDA, Bersama, Independent)',
    '128,723 electorate — largest in Johor',
    'Chinese 51.4%, Malay 35.9%, Indian 10.0%',
    'Youth 18-29: 35.5% (44,349 voters) — structurally decisive',
    '2022 turnout only 47.9% vs 86.9% in 2018 — mobilization is the battleground',
    'MUDA incumbent Amira Aisya NOT defending',
    'PH deploying Maszlee Malik (former Education Minister) — signals serious intent',
    'Critical issues: Flooding/drainage, traffic congestion, youth representation, urban services'
  ],
  historicalResults: [
    // TODO: Add 2022 and 2018 results from intelligence
  ],
  notes: [
    'Data extracted from Excel intelligence (19 June 2026)',
    'Tier classification: Tier1=Chinese/Indian >50%, Tier2=Mixed 30-50%, Tier3=Malay >70%',
    'Requires ground truth validation for candidate profiles and historical results'
  ]
};
