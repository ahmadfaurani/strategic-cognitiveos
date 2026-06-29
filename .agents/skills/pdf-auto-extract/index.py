#!/usr/bin/env python3
"""
PDF Auto-Extraction Tool
Automatically detects PDF characteristics and applies optimal extraction tool.
"""

import sys
import json
import time
import hashlib
import tempfile
import subprocess
from pathlib import Path
from urllib.parse import urlparse

# Try imports, handle missing gracefully
try:
    import fitz  # PyMuPDF
    HAS_PYMUPDF = True
except ImportError:
    HAS_PYMUPDF = False

try:
    import pdfplumber
    HAS_PDFPLUMBER = True
except ImportError:
    HAS_PDFPLUMBER = False

try:
    from tika import parser as tika_parser
    HAS_TIKA = True
except ImportError:
    HAS_TIKA = False


def fetch_pdf(source):
    """Download PDF if URL, otherwise verify file exists."""
    if source.startswith(('http://', 'https://')):
        import requests
        print(f"📥 Fetching PDF from: {source}", file=sys.stderr)
        
        # Create temp file
        tmp = tempfile.NamedTemporaryFile(suffix='.pdf', delete=False)
        tmp_path = tmp.name
        
        response = requests.get(source, stream=True, timeout=30)
        response.raise_for_status()
        
        with open(tmp_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        return tmp_path
    else:
        # Local file
        path = Path(source).expanduser()
        if not path.exists():
            raise FileNotFoundError(f"PDF not found: {source}")
        return str(path)


def analyze_pdf(pdf_path):
    """Analyze first 3 pages to determine document characteristics."""
    if not HAS_PYMUPDF:
        return {"error": "PyMuPDF not installed", "fallback": "tika"}
    
    doc = fitz.open(pdf_path)
    
    analysis = {
        "page_count": len(doc),
        "file_size_kb": Path(pdf_path).stat().st_size / 1024,
        "metadata": doc.metadata,
        "is_scanned": False,
        "has_tables": False,
        "text_density": "unknown",
        "image_count": 0,
        "avg_chars_per_page": 0,
        "language_hint": None
    }
    
    # Analyze first 3 pages (or all if < 3)
    sample_pages = min(3, len(doc))
    total_chars = 0
    total_area = 0
    
    for i in range(sample_pages):
        page = doc[i]
        text = page.get_text()
        images = page.get_images()
        
        # Text density
        page_area = page.rect.width * page.rect.height
        char_count = len(text.strip())
        density = char_count / page_area if page_area > 0 else 0
        
        total_chars += char_count
        total_area += page_area
        
        # Image count
        analysis["image_count"] += len(images)
        
        # Table detection (basic)
        if HAS_PDFPLUMBER:
            try:
                with pdfplumber.open(pdf_path) as pdf:
                    if i < len(pdf.pages):
                        tables = pdf.pages[i].extract_tables()
                        if tables:
                            analysis["has_tables"] = True
            except:
                pass
    
    doc.close()
    
    # Calculate averages
    analysis["avg_chars_per_page"] = total_chars / sample_pages if sample_pages > 0 else 0
    avg_density = (total_chars / total_area) if total_area > 0 else 0
    
    # Classify text density
    if avg_density > 0.1:
        analysis["text_density"] = "high"
    elif avg_density > 0.02:
        analysis["text_density"] = "medium"
    else:
        analysis["text_density"] = "low"
    
    # Detect scanned (low text + many images)
    if analysis["text_density"] == "low" and analysis["image_count"] > sample_pages * 2:
        analysis["is_scanned"] = True
    
    # Language hint from metadata or text sample
    if analysis["metadata"].get('language'):
        analysis["language_hint"] = analysis["metadata"]["language"]
    
    return analysis


def select_tool(analysis):
    """Select optimal extraction tool based on analysis."""
    
    # Fallback if tools missing
    if not HAS_PYMUPDF and not HAS_PDFPLUMBER and not HAS_TIKA:
        return "error", "No PDF tools installed"
    
    # Scanned documents → Tika (if available)
    if analysis.get("is_scanned"):
        if HAS_TIKA:
            return "tika", "Scanned document detected, using OCR-capable tool"
        elif HAS_PYMUPDF:
            return "pymupdf", "Scanned document, PyMuPDF fallback (limited OCR)"
        else:
            return "tika", "Tika required for scanned PDFs"
    
    # Table-heavy documents → pdfplumber
    if analysis.get("has_tables"):
        if HAS_PDFPLUMBER:
            return "pdfplumber", "Tables detected, using pdfplumber for structured extraction"
        elif HAS_PYMUPDF:
            return "pymupdf", "Tables detected, pdfplumber not available, using PyMuPDF"
    
    # High text density → PyMuPDF (fastest)
    if analysis.get("text_density") == "high":
        if HAS_PYMUPDF:
            return "pymupdf", "High text density, using PyMuPDF for speed"
        elif HAS_PDFPLUMBER:
            return "pdfplumber", "PyMuPDF not available, using pdfplumber"
    
    # Default/unknown → Try pdfplumber first (better structure), fallback to PyMuPDF
    if HAS_PDFPLUMBER:
        return "pdfplumber", "Default selection for balanced extraction"
    elif HAS_PYMUPDF:
        return "pymupdf", "Default selection (pdfplumber not available)"
    else:
        return "tika", "Fallback to Tika"


def extract_pymupdf(pdf_path):
    """Extract using PyMuPDF (fast, native PDFs)."""
    doc = fitz.open(pdf_path)
    pages = []
    
    for i, page in enumerate(doc):
        text = page.get_text()
        pages.append({
            "page": i + 1,
            "text": text.strip()
        })
    
    doc.close()
    
    return {
        "pages": pages,
        "full_text": "\n\n".join([p["text"] for p in pages])
    }


def extract_pdfplumber(pdf_path, extract_tables=True):
    """Extract using pdfplumber (tables, structured data)."""
    with pdfplumber.open(pdf_path) as pdf:
        pages = []
        tables = []
        
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            pages.append({
                "page": i + 1,
                "text": text.strip() if text else ""
            })
            
            if extract_tables:
                page_tables = page.extract_tables()
                if page_tables:
                    for j, table in enumerate(page_tables):
                        tables.append({
                            "page": i + 1,
                            "table_index": j,
                            "data": table
                        })
    
    return {
        "pages": pages,
        "tables": tables,
        "full_text": "\n\n".join([p["text"] for p in pages]),
        "has_tables": len(tables) > 0
    }


def extract_tika(pdf_path, ocr=False):
    """Extract using Apache Tika (scanned, multi-format)."""
    if not HAS_TIKA:
        return {"error": "Tika not installed"}
    
    raw = tika_parser.from_file(pdf_path)
    
    return {
        "full_text": raw.get("content", ""),
        "metadata": raw.get("metadata", {}),
        "ocr_applied": ocr
    }


def auto_extract(source, output_path=None, verbose=False):
    """
    Main auto-extraction function.
    
    Args:
        source: URL or file path to PDF
        output_path: Optional path to save JSON output
        verbose: Print detailed progress
    
    Returns:
        dict with extraction results
    """
    start_time = time.time()
    
    result = {
        "source": source,
        "status": "success",
        "tool_used": None,
        "selection_reason": None,
        "analysis": None,
        "extraction": None,
        "processing_time_ms": 0,
        "errors": []
    }
    
    try:
        # Step 1: Fetch/download
        pdf_path = fetch_pdf(source)
        
        # Step 2: Analyze
        if verbose:
            print("🔍 Analyzing PDF...", file=sys.stderr)
        analysis = analyze_pdf(pdf_path)
        result["analysis"] = analysis
        
        if "error" in analysis:
            result["errors"].append(analysis["error"])
        
        # Step 3: Select tool
        tool, reason = select_tool(analysis)
        result["tool_used"] = tool
        result["selection_reason"] = reason
        
        if verbose:
            print(f"🛠️  Using {tool}: {reason}", file=sys.stderr)
        
        # Step 4: Extract
        if tool == "pymupdf":
            extraction = extract_pymupdf(pdf_path)
        elif tool == "pdfplumber":
            extraction = extract_pdfplumber(pdf_path)
        elif tool == "tika":
            extraction = extract_tika(pdf_path, ocr=analysis.get("is_scanned", False))
        else:
            raise ValueError(f"Unknown tool: {tool}")
        
        result["extraction"] = extraction
        
        # Step 5: Save output if requested
        if output_path:
            output = Path(output_path).expanduser()
            output.parent.mkdir(parents=True, exist_ok=True)
            with open(output, 'w', encoding='utf-8') as f:
                json.dump(result, f, ensure_ascii=False, indent=2, default=str)
            if verbose:
                print(f"💾 Saved to: {output}", file=sys.stderr)
        
        # Cleanup temp file if downloaded
        if source.startswith(('http://', 'https://')) and Path(pdf_path).exists():
            Path(pdf_path).unlink()
        
    except Exception as e:
        result["status"] = "error"
        result["errors"].append(str(e))
        if verbose:
            print(f"❌ Error: {e}", file=sys.stderr)
    
    result["processing_time_ms"] = int((time.time() - start_time) * 1000)
    
    return result


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='Auto-extract PDF with optimal tool')
    parser.add_argument('source', help='PDF URL or file path')
    parser.add_argument('--output', '-o', help='Output JSON file path')
    parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output')
    parser.add_argument('--summary', '-s', action='store_true', help='Show summary only')
    
    args = parser.parse_args()
    
    result = auto_extract(args.source, args.output, args.verbose)
    
    if args.summary:
        # Print summary
        print(f"Source: {result['source']}")
        print(f"Status: {result['status']}")
        print(f"Tool: {result['tool_used']} ({result['selection_reason']})")
        print(f"Pages: {result['analysis'].get('page_count', 'N/A') if result['analysis'] else 'N/A'}")
        print(f"Time: {result['processing_time_ms']}ms")
        
        if result['extraction']:
            if 'full_text' in result['extraction']:
                text = result['extraction']['full_text']
                print(f"Extracted: {len(text)} chars")
                print(f"\nFirst 500 chars:\n{text[:500]}...")
            
            if 'tables' in result['extraction']:
                print(f"Tables found: {len(result['extraction']['tables'])}")
    else:
        # Print full JSON
        print(json.dumps(result, ensure_ascii=False, indent=2, default=str))
    
    return 0 if result['status'] == 'success' else 1


if __name__ == '__main__':
    sys.exit(main())
