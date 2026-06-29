# PDF Auto-Extraction Skill

**Purpose:** Automatically detect PDF characteristics and apply the optimal extraction tool without manual intervention.

**Location:** `~/.openclaw/workspace/.agents/skills/pdf-auto-extract/SKILL.md`

---

## Quick Start

When encountering a PDF URL or file path, this skill automatically:
1. Downloads/fetches the PDF
2. Analyzes document characteristics (scanned, tables, size, etc.)
3. Selects the optimal extraction tool
4. Extracts content efficiently
5. Returns structured output

## Invocation

### Direct Command
```bash
openclaw skill run pdf-auto-extract --source <url-or-path> [--output <path>]
```

### Programmatic
```javascript
const { autoExtractPdf } = require('./pdf-auto-extract');
const result = await autoExtractPdf({ source: 'url-or-path' });
```

## Auto-Detection Logic

### Step 1: Fetch & Analyze
```
1. Download PDF (if URL)
2. Read first 3 pages to detect:
   - Is scanned? (image-heavy, low text density)
   - Has tables? (grid patterns, cell structures)
   - Text density (chars per page)
   - Page count
   - File size
3. Classify document type
```

### Step 2: Tool Selection Matrix

| Document Type | Characteristics | Tool | Command |
|--------------|-----------------|------|---------|
| **Native Text PDF** | High text density, no scans | PyMuPDF | `fitz.open()` |
| **Table-Heavy** | Financial reports, budgets | pdfplumber | `pdfplumber.open()` |
| **Scanned/Image** | Low text, image-based | Tika + OCR | `tika.parser()` |
| **Mixed** | Some scans, some text | Hybrid | PyMuPDF + OCR pages |
| **Multi-Format** | Unknown/other formats | Tika | Universal fallback |

### Step 3: Extraction Strategy

```python
def auto_extract(source):
    # Step 1: Download if URL
    pdf_path = fetch_if_url(source)
    
    # Step 2: Analyze first 3 pages
    analysis = analyze_pdf(pdf_path)
    
    # Step 3: Select tool
    tool = select_tool(analysis)
    
    # Step 4: Extract
    if tool == 'pymupdf':
        return extract_pymupdf(pdf_path)
    elif tool == 'pdfplumber':
        return extract_pdfplumber(pdf_path, extract_tables=True)
    elif tool == 'tika':
        return extract_tika(pdf_path, ocr=analysis.is_scanned)
    elif tool == 'hybrid':
        return extract_hybrid(pdf_path, analysis)
```

## Detection Heuristics

### Is Scanned?
```python
def is_scanned(page):
    text = page.get_text()
    images = page.get_images()
    
    # Low text + many images = scanned
    text_density = len(text) / (page.rect.width * page.rect.height)
    return text_density < 0.05 and len(images) > 2
```

### Has Tables?
```python
def has_tables(page):
    # Check for table-like structures
    tables = page.find_tables()
    return len(tables) > 0 or page.extract_tables()
```

### Text Density Classification
```
High (>100 chars/1000px²): Native text PDF → PyMuPDF
Medium (20-100 chars): Mixed content → Analyze further
Low (<20 chars): Scanned/Image → Tika + OCR
```

## Tool Commands

### PyMuPDF (Fast, Native PDFs)
```bash
python3 << 'EOF'
import fitz
doc = fitz.open("<path>")
for page in doc:
    print(page.get_text())
EOF
```

### pdfplumber (Tables, Structured Data)
```bash
python3 << 'EOF'
import pdfplumber
import json

with pdfplumber.open("<path>") as pdf:
    output = {"pages": [], "tables": []}
    for i, page in enumerate(pdf.pages):
        output["pages"].append(page.extract_text())
        tables = page.extract_tables()
        if tables:
            output["tables"].append({"page": i+1, "data": tables})
    print(json.dumps(output, ensure_ascii=False, indent=2))
EOF
```

### Apache Tika (Scanned, Multi-format)
```bash
python3 << 'EOF'
from tika import parser
raw = parser.from_file("<path>")
print(raw["content"])
EOF
```

### Hybrid (Mixed Content)
```bash
python3 << 'EOF'
import fitz
import pdfplumber

doc = fitz.open("<path>")
output = {"text": [], "tables": [], "images": []}

for i, page in enumerate(doc):
    # Try pdfplumber for tables first
    with pdfplumber.open("<path>") as pdf:
        tables = pdf.pages[i].extract_tables()
        if tables:
            output["tables"].append({"page": i+1, "data": tables})
    
    # PyMuPDF for text
    text = page.get_text()
    if text.strip():
        output["text"].append({"page": i+1, "content": text})
    
    # Flag image-heavy pages for OCR
    if len(page.get_images()) > 3 and len(text) < 100:
        output["images"].append({"page": i+1, "needs_ocr": True})

print(json.dumps(output, ensure_ascii=False, indent=2))
EOF
```

## Output Format

```json
{
  "source": "<url-or-path>",
  "metadata": {
    "title": "...",
    "author": "...",
    "pages": 24,
    "size_kb": 85,
    "creation_date": "..."
  },
  "analysis": {
    "is_scanned": false,
    "has_tables": true,
    "text_density": "high",
    "language": "ms",
    "document_type": "government_budget"
  },
  "tool_used": "pdfplumber",
  "extraction": {
    "full_text": "...",
    "pages": [...],
    "tables": [...],
    "structured_data": {...}
  },
  "processing_time_ms": 1250
}
```

## Installation Requirements

```bash
# Core (always installed)
pip install PyMuPDF pdfplumber

# Optional (for scanned PDFs)
pip install tika
# Requires: Java runtime for Tika server

# OCR (for scanned PDFs without Tika)
pip install pytesseract
# Requires: tesseract-ocr system package
```

## Workflow Integration

### For Chat/Telegram
When user shares a PDF link:
1. Auto-fetch and analyze
2. Extract with optimal tool
3. Return summary + offer full extraction
4. Cache results for follow-up questions

### For Batch Processing
```bash
# Process multiple PDFs
for pdf in *.pdf; do
    openclaw skill run pdf-auto-extract --source "$pdf" --output "extracted/${pdf%.pdf}.json"
done
```

### For RAG/Indexing
```python
from pdf_auto_extract import auto_extract

result = auto_extract(pdf_path)
# Index result["extraction"]["full_text"]
# Index result["extraction"]["tables"] separately
```

## Error Handling

| Error | Fallback |
|-------|----------|
| PyMuPDF fails | Try pdfplumber |
| pdfplumber misses content | Try Tika |
| Tika too slow | Use PyMuPDF with OCR for specific pages |
| All fail | Return metadata + error, suggest manual review |

## Performance Optimization

### Caching
- Cache analysis results (scanned/table detection)
- Cache extracted text by file hash
- Skip re-extraction if unchanged

### Parallel Processing
```python
from concurrent.futures import ThreadPoolExecutor

def extract_parallel(pdf_paths, max_workers=4):
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        results = list(executor.map(auto_extract, pdf_paths))
    return results
```

### Memory Management
- Process large PDFs page-by-page (streaming)
- Clear page objects after extraction
- Use temp files for very large documents

## Example Usage

### Budget Document (Like BP.6.pdf)
```
Input: https://belanjawan.mof.gov.my/pdf/belanjawan2026/perbelanjaan/BP.6.pdf
Detection: Native PDF, has tables, 24 pages, 85KB
Tool Selected: pdfplumber (table extraction needed)
Output: Structured budget data + full text
Time: ~1.2 seconds
```

### Scanned Invoice
```
Input: invoice_scan.pdf
Detection: Scanned (low text density, image-based), 2 pages
Tool Selected: Tika + OCR
Output: Extracted text with OCR confidence scores
Time: ~5-10 seconds (OCR dependent)
```

### Research Paper
```
Input: academic_paper.pdf
Detection: Native PDF, no tables, high text density, 15 pages
Tool Selected: PyMuPDF (fastest for text-only)
Output: Clean text extraction
Time: ~0.3 seconds
```

## Monitoring & Metrics

Track for optimization:
- Tool selection accuracy (% correct on first try)
- Extraction success rate
- Average processing time by document type
- Fallback frequency

## Related Skills

- [[pdf-tool-selector]] - Decision framework reference
- [[gitnexus-exploring]] - For codebase integration
- [[improve]] - For pipeline optimization

---

**Maintenance:** Update detection heuristics based on real-world performance data.
