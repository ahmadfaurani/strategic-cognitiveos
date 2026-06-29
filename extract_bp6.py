#!/usr/bin/env python3
"""
Extract and analyze Belanjawan 2026 BP.6.pdf
Focus: Pecahan mengikut Kod Objek AM (Aset Modal)
"""

import fitz  # PyMuPDF
import requests
import json
import re
from collections import defaultdict
from pathlib import Path

# URL dokumen
PDF_URL = "https://belanjawan.mof.gov.my/pdf/belanjawan2026/perbelanjaan/BP.6.pdf"
OUTPUT_DIR = Path("/home/p62operator/.openclaw/workspace/bp6_extracted")
OUTPUT_DIR.mkdir(exist_ok=True)

def download_pdf(url, output_path):
    """Muat turun PDF dari URL rasmi"""
    print(f"📥 Memuat turun dari {url}...")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    try:
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        with open(output_path, 'wb') as f:
            f.write(response.content)
        print(f"✅ PDF berjaya dimuat turun: {output_path}")
        print(f"   Saiz: {len(response.content) / 1024 / 1024:.2f} MB")
        return True
    except Exception as e:
        print(f"❌ Ralat memuat turun: {e}")
        return False

def extract_text_with_pymupdf(pdf_path):
    """Ekstrak teks menggunakan PyMuPDF (fitz)"""
    print(f"\n📖 Mengekstrak teks dari {pdf_path}...")
    
    doc = fitz.open(pdf_path)
    print(f"   Jumlah halaman: {len(doc)}")
    
    all_text = []
    page_data = []
    
    for page_num in range(len(doc)):
        page = doc[page_num]
        text = page.get_text("text", sort=True)
        
        # Ekstrak juga mengikut blok untuk struktur yang lebih baik
        blocks = page.get_text("blocks")
        
        page_info = {
            'page': page_num + 1,
            'text': text,
            'blocks': blocks,
            'size': page.rect
        }
        
        page_data.append(page_info)
        all_text.append(f"\n{'='*80}\nHALAMAN {page_num + 1}\n{'='*80}\n")
        all_text.append(text)
    
    doc.close()
    return page_data, ''.join(all_text)

def analyze_kod_objek(page_data):
    """Analisis Kod Objek AM dari teks yang diekstrak"""
    
    # Kod Objek AM yang biasa
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
    
    results = defaultdict(list)
    tables_found = []
    
    print(f"\n🔍 Menganalisis Kod Objek AM...")
    
    for page_info in page_data:
        page_num = page_info['page']
        text = page_info['text']
        
        # Cari nombor dalam format RM (anggaran)
        rm_pattern = r'RM[\s]?(\d{1,3}(?:,\d{3})*(?:\.\d{2})?)'
        rm_matches = re.findall(rm_pattern, text)
        
        # Cari kod objek
        for kod, nama in KOD_OBJEK.items():
            if kod in text:
                # Cari baris yang mengandungi kod objek
                lines = text.split('\n')
                for i, line in enumerate(lines):
                    if kod in line:
                        # Ambil konteks (3 baris sebelum dan selepas)
                        start = max(0, i-2)
                        end = min(len(lines), i+3)
                        context = '\n'.join(lines[start:end])
                        
                        results[kod].append({
                            'page': page_num,
                            'context': context,
                            'full_line': line.strip()
                        })
        
        # Cari jadual (blok dengan koordinat serupa)
        blocks = page_info['blocks']
        if len(blocks) > 5:  # Halaman dengan jadual biasanya mempunyai banyak blok
            tables_found.append(page_num)
    
    return results, tables_found

def extract_tables_from_blocks(page_data):
    """Cuba ekstrak struktur jadual dari blok"""
    tables = []
    
    for page_info in page_data:
        page_num = page_info['page']
        blocks = page_info['blocks']
        
        # Kumpulkan blok mengikut koordinat Y (baris)
        rows = defaultdict(list)
        for block in blocks:
            if len(block) >= 5:  # Blok teks biasa
                x0, y0, x1, y1, text = block[:5]
                # Bundarkan y0 untuk kumpulan baris
                y_key = round(y0 / 5) * 5
                rows[y_key].append((x0, text.strip()))
        
        # Jika ada baris dengan banyak kolom, mungkin jadual
        for y_key, cols in rows.items():
            if len(cols) >= 3:  # Minimum 3 kolom
                cols.sort(key=lambda x: x[0])  # Isih mengikut X
                table_row = [text for _, text in cols]
                tables.append({
                    'page': page_num,
                    'y': y_key,
                    'columns': table_row
                })
    
    return tables

def save_results(results, tables, output_dir):
    """Simpan hasil analisis"""
    
    # Simpan teks penuh
    with open(output_dir / 'bp6_full_text.txt', 'w', encoding='utf-8') as f:
        f.write("BELANJAWAN 2026 - BP.6\n")
        f.write("PERBELANJAAN PEMBANGUNAN\n")
        f.write("="*80 + "\n\n")
    
    # Simpan analisis Kod Objek
    analysis_file = output_dir / 'kod_objek_analysis.json'
    with open(analysis_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\n💾 Analisis disimpan: {analysis_file}")
    
    # Simpan jadual
    tables_file = output_dir / 'extracted_tables.json'
    with open(tables_file, 'w', encoding='utf-8') as f:
        json.dump(tables, f, ensure_ascii=False, indent=2)
    print(f"💾 Jadual disimpan: {tables_file}")
    
    # Cetak ringkasan
    print("\n" + "="*80)
    print("RINGKASAN ANALISIS KOD OBJEK AM")
    print("="*80)
    
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
    
    for kod in sorted(results.keys()):
        occurrences = len(results[kod])
        nama = KOD_OBJEK.get(kod, 'Lain-lain')
        print(f"\n📌 {kod} - {nama}")
        print(f"   Ditemui: {occurrences} kali")
        
        # Tunjukkan 2 contoh pertama
        for i, item in enumerate(results[kod][:2]):
            print(f"   Halaman {item['page']}: {item['full_line'][:100]}...")
        
        if occurrences > 2:
            print(f"   ... dan {occurrences - 2} lagi")

def main():
    print("="*80)
    print("EKSTRAKSI & ANALISIS BELANJAWAN 2026 - BP.6")
    print("Pecahan Mengikut Kod Objek AM (Aset Modal)")
    print("="*80)
    
    pdf_path = OUTPUT_DIR / "BP.6.pdf"
    
    # Langkah 1: Muat turun PDF
    if not pdf_path.exists():
        if not download_pdf(PDF_URL, pdf_path):
            print("\n❌ Gagal memuat turun PDF. Semak pautan atau sambungan internet.")
            return
    else:
        print(f"✅ PDF sudah wujud: {pdf_path}")
    
    # Langkah 2: Ekstrak teks
    page_data, full_text = extract_text_with_pymupdf(pdf_path)
    
    # Simpan teks penuh
    with open(OUTPUT_DIR / 'bp6_full_text.txt', 'w', encoding='utf-8') as f:
        f.write(full_text)
    print(f"💾 Teks penuh disimpan: {OUTPUT_DIR / 'bp6_full_text.txt'}")
    
    # Langkah 3: Analisis Kod Objek
    results, tables_found = analyze_kod_objek(page_data)
    
    # Langkah 4: Ekstrak jadual
    tables = extract_tables_from_blocks(page_data)
    
    # Langkah 5: Simpan hasil
    save_results(results, tables, OUTPUT_DIR)
    
    print(f"\n✅ Analisis selesai!")
    print(f"📂 Output disimpan di: {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
