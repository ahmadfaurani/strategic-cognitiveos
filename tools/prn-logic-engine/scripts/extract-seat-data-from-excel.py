#!/usr/bin/env python3
"""
Extract DUN seat data from Excel files and generate TypeScript data files
"""

import pandas as pd
import json
from pathlib import Path

EXCEL_DIR = Path('/home/p62operator/.openclaw/media/inbound')
OUTPUT_DIR = Path('/home/p62operator/.openclaw/workspace/tools/prn-logic-engine/src/data')

def extract_seat_data(filepath, seat_code, seat_name):
    """Extract voter data from Excel file"""
    print(f"\n📊 Processing {seat_code} {seat_name}...")
    
    # Read Excel
    xls = pd.ExcelFile(filepath)
    df = pd.read_excel(filepath, sheet_name='Johor')
    
    # Calculate totals
    total_electorate = df['PEMILIH BERDAFTAR'].sum()
    total_malay = df['MELAYU'].sum()
    total_chinese = df['CINA'].sum()
    total_indian = df['INDIA'].sum()
    total_others = df['LAIN-LAIN'].sum() + df['BUMIPUTERA SABAH'].sum() + df['BUMIPUTERA SARAWAK'].sum() + df['ORANG ASLI'].sum()
    
    # Age demographics
    youth_18_29 = df['18-20 TAHUN'].sum() + df['21-30 TAHUN'].sum()
    
    # Calculate percentages
    pct_malay = (total_malay / total_electorate * 100) if total_electorate > 0 else 0
    pct_chinese = (total_chinese / total_electorate * 100) if total_electorate > 0 else 0
    pct_indian = (total_indian / total_electorate * 100) if total_electorate > 0 else 0
    pct_others = (total_others / total_electorate * 100) if total_electorate > 0 else 0
    pct_youth = (youth_18_29 / total_electorate * 100) if total_electorate > 0 else 0
    
    # Extract polling districts
    polling_districts = []
    for idx, row in df.iterrows():
        pd_name = row['DAERAH MENGUNDI']
        pd_code = row['KOD DM']
        electorate = int(row['PEMILIH BERDAFTAR'])
        malay = int(row['MELAYU'])
        chinese = int(row['CINA'])
        indian = int(row['INDIA'])
        others = int(row['LAIN-LAIN']) + int(row['BUMIPUTERA SABAH']) + int(row['BUMIPUTERA SARAWAK']) + int(row['ORANG ASLI'])
        
        # Calculate PD percentages
        pd_total = malay + chinese + indian + others
        pct_malay_pd = (malay / pd_total * 100) if pd_total > 0 else 0
        pct_chinese_pd = (chinese / pd_total * 100) if pd_total > 0 else 0
        pct_indian_pd = (indian / pd_total * 100) if pd_total > 0 else 0
        
        polling_districts.append({
            'name': pd_name,
            'code': pd_code,
            'electorate': electorate,
            'demographics': {
                'malay': malay,
                'chinese': chinese,
                'indian': indian,
                'others': others,
                'malayPct': round(pct_malay_pd, 1),
                'chinesePct': round(pct_chinese_pd, 1),
                'indianPct': round(pct_indian_pd, 1)
            }
        })
    
    # Tier classification
    tier1 = [pd for pd in polling_districts if pd['demographics']['chinesePct'] > 50 or pd['demographics']['indianPct'] > 30]
    tier2 = [pd for pd in polling_districts if 30 <= pd['demographics']['chinesePct'] <= 50 or pd['demographics']['indianPct'] > 20]
    tier3 = [pd for pd in polling_districts if pd['demographics']['malayPct'] > 70]
    
    result = {
        'seatCode': seat_code,
        'seatName': seat_name,
        'parliament': df.iloc[0]['PARLIMEN'],
        'electorate': total_electorate,
        'pollingDistricts': len(polling_districts),
        'demographics': {
            'malay': total_malay,
            'chinese': total_chinese,
            'indian': total_indian,
            'others': total_others,
            'malayPct': round(pct_malay, 1),
            'chinesePct': round(pct_chinese, 1),
            'indianPct': round(pct_indian, 1),
            'othersPct': round(pct_others, 1),
            'youth18_29': youth_18_29,
            'youthPct': round(pct_youth, 1)
        },
        'tiers': {
            'tier1': [{'name': pd['name'], 'chinesePct': pd['demographics']['chinesePct'], 'indianPct': pd['demographics']['indianPct']} for pd in tier1],
            'tier2': [{'name': pd['name'], 'chinesePct': pd['demographics']['chinesePct']} for pd in tier2],
            'tier3': [{'name': pd['name'], 'malayPct': pd['demographics']['malayPct']} for pd in tier3]
        },
        'pollingDistricts': polling_districts
    }
    
    return result

def generate_typescript_file(data):
    """Generate TypeScript data file"""
    # Convert to camelCase export name (matching existing seats like n01BulohKasap)
    seat_code = data['seatCode'].replace('N', 'n')
    seat_name_camel = ''.join(word.capitalize() for word in data['seatName'].replace('.', '').split())
    export_name = f"{seat_code}{seat_name_camel}"
    
    # Extract parliament code and name
    parliament_full = data['parliament']
    parts = parliament_full.split()
    parliament_code = parts[0] if parts else parliament_full
    parliament_name = ' '.join(parts[1:]) if len(parts) > 1 else parliament_full
    
    # Build polling districts array as TypeScript
    pd_lines = []
    for pd in data['pollingDistricts']:
        pd_lines.append(f'''    {{
      name: '{pd['name']}',
      code: '{pd['code']}',
      electorate: {pd['electorate']},
      demographics: {{
        malay: {pd['demographics']['malay']},
        chinese: {pd['demographics']['chinese']},
        indian: {pd['demographics']['indian']},
        others: {pd['demographics']['others']},
        malayPct: {pd['demographics']['malayPct']},
        chinesePct: {pd['demographics']['chinesePct']},
        indianPct: {pd['demographics']['indianPct']}
      }}
    }},''')
    
    polling_districts_ts = '\n'.join(pd_lines)
    
    ts_content = f'''/**
 * {data['seatCode']} {data['seatName']} - Voter Roll Data
 * 
 * Source: Excel intelligence (as of 19 June 2026)
 * Parliament: {parliament_full}
 * Total Electorate: {data['electorate']:,}
 * Demographics: Malay {data['demographics']['malayPct']}% / Chinese {data['demographics']['chinesePct']}% / Indian {data['demographics']['indianPct']}%
 * 
 * Tiers:
 * - Tier 1 (Kingmaker/Chinese Base): {len(data['tiers']['tier1'])} PDs
 * - Tier 2 (Mixed): {len(data['tiers']['tier2'])} PDs
 * - Tier 3 (Malay Heartland): {len(data['tiers']['tier3'])} PDs
 */

import {{ Seat, PollingDistrict }} from '../types';

export const {export_name}: Seat = {{
  code: '{data['seatCode']}',
  name: '{data['seatName']}',
  federalCode: '{parliament_code}',
  federalName: '{parliament_name}',
  district: '{data['seatName']}',  // TODO: Verify district
  totalElectorate: {data['electorate']},
  pollingDistricts: [
{polling_districts_ts}
  ],
  candidates: {{
    bn: {{ name: 'TBD', party: 'TBD', incumbent: false }},
    ph: {{ name: 'TBD', party: 'TBD', incumbent: false }},
    pn: {{ name: 'TBD', party: 'TBD', incumbent: false }}
  }},
  historicalResults: [
    // TODO: Add 2022 and 2018 results from intelligence
  ],
  notes: [
    'Data extracted from Excel intelligence (19 June 2026)',
    'Tier classification: Tier1=Chinese/Indian >50%, Tier2=Mixed 30-50%, Tier3=Malay >70%',
    'Requires ground truth validation for candidate profiles and historical results'
  ]
}};
'''
    
    output_path = OUTPUT_DIR / f'{seat_code}-{data["seatName"].lower().replace(" ", "-").replace(".", "")}.ts'
    output_path.write_text(ts_content)
    
    print(f"✅ Generated: {output_path}")
    return output_path

# Process the 4 new seats
seats_to_process = [
    ('5_SUNGAI_BALANG_as_of_190626---190553de-daf5-47ee-8f7a-471bdb1a9dd1.xlsx', 'N16', 'Sungai Balang'),
    ('9_ENDAU_as_of_190626---ecda7b55-9bab-42ae-829b-fd2b508f67d5.xlsx', 'N32', 'Endau'),
    ('10_PASIR_RAJA_as_of_190626---2315db07-00df-4a4e-9473-837099ea6b3c.xlsx', 'N35', 'Pasir Raja'),
    ('11_PUTERI_WANGSA_as_of_190626---960f7a4d-cf0d-4cd4-9e9d-dfe29db6a9e4.xlsx', 'N41', 'Puteri Wangsa'),
]

# Batch 2: 6 additional seats
seats_batch2 = [
    ('12_KEMPAS_as_of_190626---b6d3a822-4371-4b3d-9b70-0d3c53e533f6.xlsx', 'N12', 'Kempas'),
    ('13_BUKIT_BATU_as_of_190626---5ffaecb9-9ce2-46a1-aed5-ceecaca83ae1.xlsx', 'N13', 'Bukit Batu'),
    ('14_PULAI_SEBATANG_as_of_190626---3128b667-31b2-40c0-bbf1-a575252373aa.xlsx', 'N14', 'Pulai Sebatang'),
    ('15_KUKUP_as_of_190626---d074ba33-5bc8-4038-a74b-102362eadcc9.xlsx', 'N15', 'Kukup'),
    ('16_BUKIT_KEPONG_as_of_190626---c04c498b-cc63-4679-90ad-b80ec7eadc96.xlsx', 'N18', 'Bukit Kepong'),
    ('17_SRI_MEDAN_as_of_190626---2a7ac0df-b076-4311-bc37-5626216e6a8b.xlsx', 'N19', 'Sri Medan'),
]

# Batch 3: 3 additional seats (Mersing)
seats_batch3 = [
    ('18_TENGGAROH_as_of_190626---bd590a4b-eba9-4d30-9d1c-bc0c5f447a8b.xlsx', 'N33', 'Tenggaroh'),
    ('19_JOHOR_LAMA_as_of_190626---396d6a5f-36da-49e2-a2b3-f79430e9473a.xlsx', 'N25', 'Johor Lama'),
    ('20_TANJUNG_SURAT_as_of_190626---00fce108-0c3e-4c4a-9696-47207f13b99b.xlsx', 'N26', 'Tanjung Surat'),
]

print("="*70)
print("📊 DUN INTELLIGENCE EXTRACTION - 4 NEW SEATS")
print("="*70)

for filename, seat_code, seat_name in seats_to_process:
    filepath = EXCEL_DIR / filename
    if not filepath.exists():
        print(f"❌ File not found: {filepath}")
        continue
    
    # Extract data
    data = extract_seat_data(filepath, seat_code, seat_name)
    
    # Print summary
    print(f"\n📋 Summary for {seat_code} {seat_name}:")
    print(f"   Parliament: {data['parliament']}")
    print(f"   Electorate: {data['electorate']:,} ({data['pollingDistricts']} PDs)")
    print(f"   Demographics: Malay {data['demographics']['malayPct']}% / Chinese {data['demographics']['chinesePct']}% / Indian {data['demographics']['indianPct']}%")
    print(f"   Youth (18-29): {data['demographics']['youth18_29']:,} ({data['demographics']['youthPct']}%)")
    print(f"   Tier 1 (Kingmaker): {len(data['tiers']['tier1'])} PDs")
    print(f"   Tier 2 (Mixed): {len(data['tiers']['tier2'])} PDs")
    print(f"   Tier 3 (Malay): {len(data['tiers']['tier3'])} PDs")
    
    # Generate TypeScript file
    generate_typescript_file(data)

print("\n" + "="*70)
print("✅ BATCH 1 COMPLETE")
print("="*70)
print("\nNext steps:")
print("1. Review generated .ts files in src/data/")
print("2. Add historical results (2022, 2018)")
print("3. Add candidate profiles (post-nomination)")
print("4. Run: npm run dev -- calculate --seat N16 (etc.)")

# Process Batch 2
print("\n" + "="*70)
print("📊 BATCH 2 - 6 ADDITIONAL SEATS")
print("="*70)

for filename, seat_code, seat_name in seats_batch2:
    filepath = EXCEL_DIR / filename
    if not filepath.exists():
        print(f"❌ File not found: {filepath}")
        continue
    
    # Extract data
    data = extract_seat_data(filepath, seat_code, seat_name)
    
    # Print summary
    print(f"\n📋 Summary for {seat_code} {seat_name}:")
    print(f"   Parliament: {data['parliament']}")
    print(f"   Electorate: {data['electorate']:,} ({data['pollingDistricts']} PDs)")
    print(f"   Demographics: Malay {data['demographics']['malayPct']}% / Chinese {data['demographics']['chinesePct']}% / Indian {data['demographics']['indianPct']}%")
    print(f"   Youth (18-29): {data['demographics']['youth18_29']:,} ({data['demographics']['youthPct']}%)")
    print(f"   Tier 1 (Kingmaker): {len(data['tiers']['tier1'])} PDs")
    print(f"   Tier 2 (Mixed): {len(data['tiers']['tier2'])} PDs")
    print(f"   Tier 3 (Malay): {len(data['tiers']['tier3'])} PDs")
    
    # Generate TypeScript file
    generate_typescript_file(data)

print("\n" + "="*70)
print("✅ ALL BATCHES COMPLETE")
print("="*70)

# Process Batch 3
print("\n" + "="*70)
print("📊 BATCH 3 - 3 ADDITIONAL SEATS (MERSING)")
print("="*70)

for filename, seat_code, seat_name in seats_batch3:
    filepath = EXCEL_DIR / filename
    if not filepath.exists():
        print(f"❌ File not found: {filepath}")
        continue
    
    # Extract data
    data = extract_seat_data(filepath, seat_code, seat_name)
    
    # Print summary
    print(f"\n📋 Summary for {seat_code} {seat_name}:")
    print(f"   Parliament: {data['parliament']}")
    print(f"   Electorate: {data['electorate']:,} ({data['pollingDistricts']} PDs)")
    print(f"   Demographics: Malay {data['demographics']['malayPct']}% / Chinese {data['demographics']['chinesePct']}% / Indian {data['demographics']['indianPct']}%")
    print(f"   Youth (18-29): {data['demographics']['youth18_29']:,} ({data['demographics']['youthPct']}%)")
    print(f"   Tier 1 (Kingmaker): {len(data['tiers']['tier1'])} PDs")
    print(f"   Tier 2 (Mixed): {len(data['tiers']['tier2'])} PDs")
    print(f"   Tier 3 (Malay): {len(data['tiers']['tier3'])} PDs")
    
    # Generate TypeScript file
    generate_typescript_file(data)

print("\n" + "="*70)
print("✅ ALL BATCHES (1-3) COMPLETE")
print("="*70)
