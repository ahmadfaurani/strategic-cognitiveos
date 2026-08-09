#!/usr/bin/env python3
"""
Analisis lengkap BP.6.pdf - Fokus Kod Objek AM
"""

import fitz
import json
import re
from collections import defaultdict
from pathlib import Path

PDF_PATH = Path("/home/p62operator/.openclaw/workspace/bp6_extracted/BP.6.pdf")
OUTPUT_DIR = Path("/home/p62operator/.openclaw/workspace/bp6_extracted")

def extract_all_pages(pdf_path):
    """Ekstrak semua halaman"""
    doc = fitz.open(pdf_path)
    pages = []
    
    for page_num in range(len(doc)):
        page = doc[page_num]
        text = page.get_text("text")
        blocks = page.get_text("blocks")
        
        pages.append({
            'page': page_num + 1,
            'text': text,
            'blocks': blocks
        })
    
    doc.close()
    return pages

def find_kod_objek_references(pages):
    """Cari semua rujukan Kod Objek AM"""
    
    # Kod Objek AM standard
    KOD_OBJEK = {
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
    
    results = {}
    
    for page in pages:
        page_num = page['page']
        text = page['text']
        
        for kod, nama in KOD_OBJEK.items():
            if kod in text:
                if kod not in results:
                    results[kod] = {
                        'nama': nama,
                        'pages': [],
                        'amounts': [],
                        'contexts': []
                    }
                
                # Cari baris dengan kod
                lines = text.split('\n')
                for i, line in enumerate(lines):
                    if kod in line:
                        # Cari nilai RM dalam baris atau berhampiran
                        rm_pattern = r'RM\s*([\d,]+(?:\.\d{2})?)'
                        rm_matches = re.findall(rm_pattern, line)
                        
                        context_start = max(0, i-1)
                        context_end = min(len(lines), i+2)
                        context = '\n'.join(lines[context_start:context_end])
                        
                        results[kod]['pages'].append(page_num)
                        results[kod]['contexts'].append(context)
                        
                        if rm_matches:
                            for match in rm_matches:
                                amount = float(match.replace(',', ''))
                                results[kod]['amounts'].append(amount)
    
    return results

def extract_budget_tables(pages):
    """Ekstrak jadual peruntukan"""
    tables = []
    
    for page in pages:
        page_num = page['page']
        blocks = page['blocks']
        
        # Kumpulkan blok mengikut koordinat Y
        rows = defaultdict(list)
        for block in blocks:
            if len(block) >= 5 and block[4]:  # Blok dengan teks
                x0, y0, x1, y1, text = block[:5]
                y_key = round(y0 / 10) * 10  # Kumpulan baris
                rows[y_key].append((x0, text.strip()))
        
        # Cari baris dengan banyak kolom
        for y_key, cols in rows.items():
            if len(cols) >= 2:
                cols.sort(key=lambda x: x[0])
                row_data = [text for _, text in cols]
                
                # Semak jika ada nilai RM
                has_rm = any('RM' in str(cell) for cell in row_data)
                has_number = any(re.search(r'\d{3}', str(cell)) for cell in row_data)
                
                if has_rm or has_number:
                    tables.append({
                        'page': page_num,
                        'y': y_key,
                        'data': row_data
                    })
    
    return tables

def analyze_by_ministry(pages):
    """Analisis peruntukan mengikut kementerian/jabatan"""
    ministries = {}
    
    current_ministry = None
    current_amount = None
    
    for page in pages:
        page_num = page['page']
        text = page['text']
        lines = text.split('\n')
        
        for line in lines:
            line = line.strip()
            
            # Cari nama kementerian/jabatan
            if any(keyword in line.upper() for keyword in ['JABATAN', 'KEMENTERIAN', 'AGENSI']):
                if 'RM' in line:
                    # Ada jumlah dalam baris yang sama
                    rm_match = re.search(r'RM\s*([\d,]+(?:\.\d{2})?)', line)
                    if rm_match:
                        amount = float(rm_match.group(1).replace(',', ''))
                        ministries[line.split('RM')[0].strip()] = {
                            'page': page_num,
                            'amount': amount
                        }
    
    return ministries

def generate_report(kod_results, tables, ministries):
    """Jana laporan analisis"""
    
    print("="*80)
    print("LAPORAN ANALISIS BELANJAWAN 2026 - BP.6")
    print("Pecahan Mengikut Kod Objek AM (Aset Modal)")
    print("="*80)
    
    # Ringkasan Kod Objek
    print("\n📊 RINGKASAN KOD OBJEK AM")
    print("-"*80)
    
    KOD_DESC = {
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
    
    for kod in sorted(kod_results.keys()):
        data = kod_results[kod]
        desc = KOD_DESC.get(kod, 'Lain-lain')
        
        print(f"\n📌 {kod} - {desc}")
        print(f"   Ditemui di halaman: {', '.join(map(str, sorted(set(data['pages']))))}")
        print(f"   Bilangan rujukan: {len(data['pages'])}")
        
        if data['amounts']:
            total = sum(data['amounts'])
            avg = total / len(data['amounts'])
            print(f"   Jumlah nilai: RM {total:,.2f}")
            print(f"   Purata: RM {avg:,.2f}")
        
        # Tunjukkan contoh konteks
        if data['contexts']:
            print(f"   Contoh:")
            for ctx in data['contexts'][:1]:
                # Clean up context
                ctx_clean = ' '.join(ctx.split())
                print(f"      {ctx_clean[:150]}...")
    
    # Jadual yang diekstrak
    print("\n\n📋 JADUAL PERUNTUKAN DIEKSTRAK")
    print("-"*80)
    
    # Kumpulan jadual mengikut halaman
    tables_by_page = defaultdict(list)
    for table in tables:
        tables_by_page[table['page']].append(table)
    
    for page_num in sorted(tables_by_page.keys())[:10]:  # Tunjukkan 10 halaman pertama
        page_tables = tables_by_page[page_num]
        print(f"\nHalaman {page_num} ({len(page_tables)} jadual):")
        
        for i, tbl in enumerate(page_tables[:3]):  # 3 jadual pertama per halaman
            print(f"  Jadual {i+1}: {' | '.join(str(x)[:30] for x in tbl['data'][:4])}")
    
    # Analisis Kementerian
    print("\n\n🏛️ PERUNTUKAN MENGIKUT KEMENTERIAN/JABATAN")
    print("-"*80)
    
    sorted_ministries = sorted(ministries.items(), key=lambda x: x[1].get('amount', 0), reverse=True)
    
    for ministry, data in sorted_ministries[:20]:  # Top 20
        amount = data.get('amount', 0)
        page = data.get('page', '?')
        print(f"   {ministry[:60]:60} RM {amount:>15,.2f} (hal {page})")
    
    print("\n" + "="*80)

def main():
    print("🔄 Memproses BP.6.pdf...")
    
    # Ekstrak semua halaman
    pages = extract_all_pages(PDF_PATH)
    print(f"✅ {len(pages)} halaman diekstrak")
    
    # Cari Kod Objek
    print("🔍 Menganalisis Kod Objek AM...")
    kod_results = find_kod_objek_references(pages)
    
    # Ekstrak jadual
    print("📊 Mengekstrak jadual peruntukan...")
    tables = extract_budget_tables(pages)
    
    # Analisis kementerian
    print("🏛️ Menganalisis peruntukan kementerian...")
    ministries = analyze_by_ministry(pages)
    
    # Jana laporan
    print("\n")
    generate_report(kod_results, tables, ministries)
    
    # Simpan hasil
    output_file = OUTPUT_DIR / 'bp6_analysis_full.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump({
            'kod_objek': kod_results,
            'tables_count': len(tables),
            'ministries_count': len(ministries)
        }, f, ensure_ascii=False, indent=2, default=str)
    
    print(f"\n💾 Hasil penuh disimpan: {output_file}")

if __name__ == "__main__":
    main()
