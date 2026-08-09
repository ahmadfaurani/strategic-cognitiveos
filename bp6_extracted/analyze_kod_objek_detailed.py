#!/usr/bin/env python3
"""
Analisis Terperinci BP.6.pdf - Pecahan Kod Objek AM
Jabatan Perdana Menteri - Belanjawan 2026
"""

import fitz
import json
from pathlib import Path
from collections import defaultdict
import re

PDF_PATH = Path("/home/p62operator/.openclaw/workspace/bp6_extracted/BP.6.pdf")
OUTPUT_DIR = Path("/home/p62operator/.openclaw/workspace/bp6_extracted")

def extract_full_content(pdf_path):
    """Ekstrak kandungan penuh PDF"""
    doc = fitz.open(pdf_path)
    pages = []
    
    for i in range(len(doc)):
        page = doc[i]
        text = page.get_text("text")
        pages.append(text)
    
    doc.close()
    return pages

def parse_budget_tables(pages):
    """Parse jadual anggaran perbelanjaan"""
    
    # Kod Objek AM untuk Perbelanjaan Pembangunan
    KOD_OBJEK_AM = {
        '20000': 'Perkhidmatan dan Bekalan',
        '30000': 'Aset (Termasuk Aset Modal)',
        '40000': 'Pemberian dan Kenaan Bayaran Tetap'
    }
    
    # Pecahan lebih terperinci untuk Kod 30000 (Aset)
    KOD_ASET_MODAL = {
        '2100': 'Bangunan & Infrastruktur',
        '2200': 'Kenderaan',
        '2300': 'Peralatan & Mesin',
        '2400': 'Perabot & Kelengkapan',
        '2500': 'Tanah',
        '2600': 'Aset Tak Ketara',
        '2700': 'Kerja-kerja Awam',
        '2800': 'Aset Pertahanan/Keselamatan',
        '2900': 'Aset Modal Lain'
    }
    
    results = {
        'summary': {},
        'by_activity': defaultdict(dict),
        'development_projects': [],
        'asset_breakdown': {}
    }
    
    # Cari halaman ringkasan (halaman 13)
    for page_text in pages:
        lines = page_text.split('\n')
        
        # Cari jadual ringkasan perbelanjaan pembangunan
        if 'ANGGARAN PERBELANJAAN PEMBANGUNAN BAGI TAHUN 2026 MENGIKUT OBJEK AM' in page_text:
            in_table = False
            for i, line in enumerate(lines):
                if '20000' in line and 'Perkhidmatan dan Bekalan' in line:
                    # Ekstrak baris berikut
                    for j in range(i, min(i+10, len(lines))):
                        row = lines[j]
                        if '20000' in row or '30000' in row or '40000' in row:
                            parts = row.split()
                            if len(parts) >= 3:
                                kod = parts[0]
                                try:
                                    # Cari nilai RM
                                    rm_values = re.findall(r'([\d,]+)', row)
                                    if len(rm_values) >= 2:
                                        y2025 = float(rm_values[-2].replace(',', ''))
                                        y2026 = float(rm_values[-1].replace(',', ''))
                                        
                                        results['summary'][kod] = {
                                            'nama': KOD_OBJEK_AM.get(kod, 'Lain-lain'),
                                            '2025': y2025,
                                            '2026': y2026,
                                            'perubahan': y2026 - y2025,
                                            'peratus': ((y2026 - y2025) / y2025 * 100) if y2025 > 0 else 0
                                        }
                                except:
                                    pass
    
    # Analisis mengikut aktiviti
    current_activity = None
    current_code = None
    
    for page_text in pages:
        lines = page_text.split('\n')
        
        for i, line in enumerate(lines):
            # Cari kod aktiviti (contoh: 010000, 020000)
            if re.match(r'^\d{6}\s+', line.strip()):
                parts = line.strip().split()
                if len(parts) >= 2:
                    current_code = parts[0]
                    activity_name = ' '.join(parts[1:])
                    current_activity = current_code
            
            # Cari peruntukan mengikut kod objek
            if current_activity and ('10000' in line or '20000' in line or '30000' in line or '40000' in line):
                parts = line.split()
                for kod_objek in ['10000', '20000', '30000', '40000', '50000']:
                    if kod_objek in parts:
                        idx = parts.index(kod_objek)
                        if len(parts) > idx + 2:
                            try:
                                y2025 = float(parts[idx + 1].replace(',', ''))
                                y2026 = float(parts[idx + 2].replace(',', ''))
                                
                                if current_activity not in results['by_activity']:
                                    results['by_activity'][current_activity] = {}
                                
                                results['by_activity'][current_activity][kod_objek] = {
                                    '2025': y2025,
                                    '2026': y2026
                                }
                            except:
                                pass
    
    # Ekstrak projek pembangunan (halaman 23-24)
    for page_text in pages:
        lines = page_text.split('\n')
        
        if 'Maksud Pembangunan 6' in page_text:
            in_project_table = False
            current_project = {}
            
            for line in lines:
                # Cari kod projek (5 digit)
                match = re.match(r'^(\d{5})\s+(.+?)\s+([\d,]+)\s+([\d,]+)\s+([\d,]+)\s+([\d,]+)', line.strip())
                if match:
                    project_code = match.group(1)
                    project_name = match.group(2)
                    
                    try:
                        actual_2024 = float(match.group(3).replace(',', ''))
                        revised_2025 = float(match.group(4).replace(',', ''))
                        estimate_2026 = float(match.group(5).replace(',', ''))
                        
                        # Klasifikasi projek mengikut jenis aset modal
                        asset_category = categorize_project(project_name)
                        
                        results['development_projects'].append({
                            'code': project_code,
                            'name': project_name,
                            'category': asset_category,
                            'actual_2024': actual_2024,
                            'revised_2025': revised_2025,
                            'estimate_2026': estimate_2026
                        })
                    except:
                        pass
    
    return results

def categorize_project(project_name):
    """Kategorikan projek mengikut Kod Objek AM"""
    
    project_lower = project_name.lower()
    
    if any(word in project_lower for word in ['bangunan', 'pejabat', 'perumahan', 'kompleks', 'academi', 'institut']):
        return '2100 - Bangunan'
    elif any(word in project_lower for word in ['jalan', 'jambatan', 'infrastruktur', 'pagar']):
        return '2700 - Kerja Awam'
    elif any(word in project_lower for word in ['kenderaan', 'jentera', 'bas', 'feri']):
        return '2200 - Kenderaan'
    elif any(word in project_lower for word in ['sistem', 'ikt', 'komputer', 'digital', 'pengkomputeran']):
        return '2300 - Peralatan & Mesin'
    elif any(word in project_lower for word in ['masjid', 'surau', 'islamik', 'dakwah']):
        return '2100 - Bangunan'
    elif any(word in project_lower for word in ['keselamatan', 'pertahanan', 'bencana']):
        return '2800 - Aset Pertahanan'
    else:
        return '2900 - Lain-lain'

def generate_detailed_report(results):
    """Jana laporan terperinci"""
    
    print("="*80)
    print("ANALISIS TERPERINCI BELANJAWAN 2026 - BP.6")
    print("Jabatan Perdana Menteri - Pecahan Kod Objek AM")
    print("="*80)
    
    # 1. Ringkasan Perbelanjaan Pembangunan
    print("\n📊 RINGKASAN PERBELANJAAN PEMBANGUNAN 2026")
    print("-"*80)
    
    total_2025 = 0
    total_2026 = 0
    
    for kod, data in sorted(results['summary'].items()):
        print(f"\n{kod} - {data['nama']}")
        print(f"  2025: RM {data['2025']:>15,.2f}")
        print(f"  2026: RM {data['2026']:>15,.2f}")
        print(f"  Perubahan: RM {data['perubahan']:>15,.2f} ({data['peratus']:>+6.2f}%)")
        
        total_2025 += data['2025']
        total_2026 += data['2026']
    
    print(f"\n{'JUMLAH':<40} RM {total_2025:>15,.2f} RM {total_2026:>15,.2f}")
    
    # 2. Analisis Projek Pembangunan
    print("\n\n🏗️ PROJEK PEMBANGUNAN UTAMA (Top 20)")
    print("-"*80)
    
    # Sort by 2026 estimate
    sorted_projects = sorted(results['development_projects'], 
                           key=lambda x: x['estimate_2026'], 
                           reverse=True)
    
    print(f"\n{'Kod':<8} {'Nama Projek':<50} {'2026 (RM)':>15} {'Kategori':<25}")
    print("-"*100)
    
    for proj in sorted_projects[:20]:
        print(f"{proj['code']:<8} {proj['name'][:48]:<50} RM {proj['estimate_2026']:>14,.0f} {proj['category']}")
    
    # 3. Pecahan Mengikut Kategori Aset Modal
    print("\n\n📈 PECAHAN MENGIKUT KATEGORI ASET MODAL")
    print("-"*80)
    
    category_totals = defaultdict(lambda: {'2024': 0, '2025': 0, '2026': 0})
    
    for proj in results['development_projects']:
        cat = proj['category'].split(' - ')[0]
        category_totals[cat]['2024'] += proj['actual_2024']
        category_totals[cat]['2025'] += proj['revised_2025']
        category_totals[cat]['2026'] += proj['estimate_2026']
    
    print(f"\n{'Kategori':<30} {'2024 (Actual)':>15} {'2025 (Revised)':>18} {'2026 (Estimate)':>18}")
    print("-"*85)
    
    for cat, totals in sorted(category_totals.items()):
        cat_name = dict([
            ('2100', 'Bangunan & Infrastruktur'),
            ('2200', 'Kenderaan'),
            ('2300', 'Peralatan & Mesin'),
            ('2700', 'Kerja-kerja Awam'),
            ('2800', 'Aset Pertahanan'),
            ('2900', 'Lain-lain')
        ]).get(cat, cat)
        
        print(f"{cat_name:<30} RM {totals['2024']:>14,.0f} RM {totals['2025']:>17,.0f} RM {totals['2026']:>17,.0f}")
    
    # 4. Projek Mengikut Aktiviti
    print("\n\n📋 PERUNTUKAN MENGIKUT AKTIVITI (Top 15)")
    print("-"*80)
    
    activity_totals = {}
    for activity, codes in results['by_activity'].items():
        total = sum(data.get('2026', 0) for data in codes.values())
        activity_totals[activity] = total
    
    sorted_activities = sorted(activity_totals.items(), key=lambda x: x[1], reverse=True)
    
    for activity, total in sorted_activities[:15]:
        # Cari nama aktiviti
        activity_name = activity
        for page in pages:
            if activity in page:
                lines = page.split('\n')
                for line in lines:
                    if activity in line:
                        activity_name = line.strip()
                        break
        
        print(f"\n{activity}: RM {total:>15,.2f}")
    
    print("\n" + "="*80)

def save_analysis(results, output_dir):
    """Simpan hasil analisis"""
    
    output_file = output_dir / 'bp6_kod_objek_analysis.json'
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2, default=str)
    
    print(f"\n💾 Analisis disimpan: {output_file}")

# Global pages variable
pages = []

def main():
    global pages
    
    print("🔄 Memproses BP.6.pdf...")
    
    # Ekstrak kandungan
    pages = extract_full_content(PDF_PATH)
    print(f"✅ {len(pages)} halaman diekstrak")
    
    # Parse jadual
    print("📊 Menganalisis jadual anggaran...")
    results = parse_budget_tables(pages)
    
    # Jana laporan
    print("\n")
    generate_detailed_report(results)
    
    # Simpan hasil
    save_analysis(results, OUTPUT_DIR)
    
    print(f"\n✅ Analisis selesai!")

if __name__ == "__main__":
    main()
