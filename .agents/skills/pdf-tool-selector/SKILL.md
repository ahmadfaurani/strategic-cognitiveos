---
name: pdf-tool-selector
description: Intelligently select the optimal PDF processing tool (PyMuPDF, pdfplumber, or Apache Tika) based on document characteristics and use case requirements.
---

# PDF Tool Selector

This skill analyzes PDF document requirements and recommends the optimal processing tool from three options: **PyMuPDF**, **pdfplumber**, or **Apache Tika**.

## When to Use This Skill

Use this skill when:
- You need to process PDFs and are unsure which tool to choose
- You're building a RAG pipeline and need to optimize PDF extraction
- You have mixed document types and need a decision framework
- You want to understand trade-offs between speed, accuracy, and format support

## How to Invoke

### CLI Interface

```bash
# Run the selector with document characteristics
node /home/p62operator/.openclaw/workspace/.agents/skills/pdf-tool-selector/index.js \
  --scanned=false \
  --has-tables=true \
  --format=pdf \
  --volume=high \
  --needs-metadata=false
```

### Programmatic API

```javascript
const { selectPdfTool } = require('./pdf-tool-selector');

const recommendation = selectPdfTool({
  isScanned: false,
  hasTables: true,
  format: 'pdf',
  volume: 'high',
  needsMetadata: false,
  needsLayoutCoordinates: true
});

console.log(recommendation);
// { tool: 'pdfplumber', confidence: 0.92, reasoning: '...' }
```

### Python API

```python
from pdf_tool_selector import select_pdf_tool

recommendation = select_pdf_tool(
    is_scanned=False,
    has_tables=True,
    format='pdf',
    volume='high',
    needs_metadata=False,
    needs_layout_coordinates=True
)

print(recommendation)
```

## Decision Framework

### Tool Comparison Matrix

| Characteristic | PyMuPDF | pdfplumber | Apache Tika |
|----------------|---------|------------|-------------|
| **Speed** | ⚡⚡⚡ Fastest | ⚡⚡ Moderate | ⚡ Slowest |
| **Table Extraction** | ⚠️ Basic | ✅ Excellent | ⚠️ Limited |
| **Scanned PDFs (OCR)** | ❌ No | ❌ No | ⚠️ Via Tesseract |
| **Format Support** | PDF only | PDF only | 1000+ formats |
| **Layout Coordinates** | ✅ Good | ✅ Excellent | ⚠️ Basic |
| **Metadata Extraction** | ✅ Good | ✅ Good | ✅ Excellent |
| **Memory Usage** | Low | Moderate | High (Java) |
| **Best For** | High-volume, clean PDFs | Tables, forms, structured data | Multi-format, enterprise |

### Decision Logic

```
IF format != PDF:
    → Apache Tika (only option with multi-format support)

ELSE IF is_scanned == true:
    → Apache Tika + Tesseract OCR (only OCR-capable option)
    → OR PyMuPDF + external OCR service

ELSE IF has_tables == true OR needs_layout_coordinates == true:
    → pdfplumber (superior table/cell detection)

ELSE IF volume == high AND format == PDF:
    → PyMuPDF (fastest for bulk processing)

ELSE IF needs_metadata == true AND enterprise_java == true:
    → Apache Tika (comprehensive metadata)

ELSE:
    → PyMuPDF (default for clean native PDFs)
```

## Tool Profiles

### PyMuPDF (fitz)

**Best for:**
- High-volume PDF processing (1000+ documents)
- Clean, native PDFs (not scanned)
- Fast text and image extraction
- When performance is critical
- Simple text extraction without complex layouts

**Install:**
```bash
pip install PyMuPDF
# or
npm install pymupdf
```

**Example:**
```python
import fitz  # PyMuPDF

doc = fitz.open("document.pdf")
for page in doc:
    text = page.get_text()
    images = page.get_images()
```

**Strengths:**
- Fastest PDF library (C-based)
- Low memory footprint
- Excellent for text + image extraction
- Active maintenance

**Limitations:**
- PDF only
- No OCR for scanned documents
- Table extraction is basic

### pdfplumber

**Best for:**
- Tables and structured data extraction
- Financial reports, invoices, forms
- When precise layout coordinates are needed
- Cell-by-cell extraction
- Complex multi-column layouts

**Install:**
```bash
pip install pdfplumber
```

**Example:**
```python
import pdfplumber

with pdfplumber.open("report.pdf") as pdf:
    for page in pdf.pages:
        tables = page.extract_tables()
        cells = page.chars  # Individual character positions
```

**Strengths:**
- Best-in-class table detection
- Precise coordinate extraction
- Visual debugging (page.to_image())
- Built on pdfminer.six

**Limitations:**
- Slower than PyMuPDF
- Higher memory usage
- PDF only
- No OCR

### Apache Tika

**Best for:**
- Multi-format support (1000+ formats)
- Enterprise Java environments
- Comprehensive metadata extraction
- When format coverage > layout fidelity
- Mixed document pipelines (PDF, DOCX, PPTX, etc.)

**Install:**
```bash
# Java required
# Use tika-python wrapper
pip install tika

# Or use tika-server directly
docker pull apache/tika
```

**Example:**
```python
from tika import parser

raw = parser.from_file("document.pdf")
text = raw["content"]
metadata = raw["metadata"]
```

**Strengths:**
- 1000+ file formats
- Excellent metadata extraction
- Enterprise-grade
- OCR via Tesseract integration

**Limitations:**
- Slowest option (Java overhead)
- High memory usage
- Layout fidelity lower than pdfplumber
- Requires JVM

## Example Scenarios

### Scenario 1: Financial Reports Pipeline
```
Input: 500 quarterly reports with tables
Requirements: Extract tables, preserve structure, moderate volume
Recommendation: pdfplumber (confidence: 0.95)
Reason: Superior table extraction, coordinate precision for financial data
```

### Scenario 2: Legal Document Archive
```
Input: 10,000 mixed-format documents (PDF, DOCX, scanned PDFs)
Requirements: Full-text search, metadata indexing, format-agnostic
Recommendation: Apache Tika (confidence: 0.98)
Reason: Only option supporting 1000+ formats, comprehensive metadata
```

### Scenario 3: Research Paper RAG
```
Input: 2,000 academic PDFs (native, no scans)
Requirements: Fast ingestion, clean text, moderate layout awareness
Recommendation: PyMuPDF (confidence: 0.90)
Reason: Best speed/quality ratio for high-volume native PDFs
```

### Scenario 4: Invoice Processing
```
Input: Mixed invoices (some scanned, some native PDFs)
Requirements: Table extraction, handle scans, moderate volume
Recommendation: Hybrid approach
  - Native PDFs → pdfplumber
  - Scanned PDFs → Tika + Tesseract OCR
  - Or: Use cloud OCR API (AWS Textract, Google Vision)
```

## Configuration Options

### Input Parameters

| Parameter | Type | Description | Values |
|-----------|------|-------------|--------|
| `isScanned` | boolean | Document is image-based (requires OCR) | true/false |
| `hasTables` | boolean | Document contains tabular data | true/false |
| `format` | string | Document format | pdf, docx, pptx, etc. |
| `volume` | string | Processing volume | low, medium, high |
| `needsMetadata` | boolean | Extract full metadata | true/false |
| `needsLayoutCoordinates` | boolean | Need precise text positions | true/false |
| `enterpriseJava` | boolean | Running in Java environment | true/false |
| `language` | string | Document language | en, es, zh, etc. |

### Output Format

```json
{
  "tool": "pdfplumber",
  "confidence": 0.92,
  "reasoning": "Document contains tables requiring precise cell extraction",
  "alternatives": [
    {"tool": "PyMuPDF", "confidence": 0.65, "tradeoff": "Faster but poor table support"},
    {"tool": "Apache Tika", "confidence": 0.40, "tradeoff": "Overkill for PDF-only workload"}
  ],
  "installCommand": "pip install pdfplumber",
  "codeExample": "import pdfplumber; ..."
}
```

## Integration with RAG Pipelines

### LangChain Integration

```python
from langchain.document_loaders import PyMuPDFLoader, PDFPlumberLoader

def get_loader(recommendation):
    if recommendation['tool'] == 'PyMuPDF':
        return PyMuPDFLoader
    elif recommendation['tool'] == 'pdfplumber':
        return PDFPlumberLoader
    # Tika requires separate setup
```

### LlamaIndex Integration

```python
from llama_index import SimpleDirectoryReader, PDFReader

def get_reader(recommendation):
    # Configure based on tool recommendation
    pass
```

## Fallback Recommendations

| Primary Issue | Fallback |
|---------------|----------|
| pdfplumber fails on corrupted PDF | Try PyMuPDF (more tolerant) |
| PyMuPDF misses table structure | Switch to pdfplumber |
| Tika too slow for volume | Use PyMuPDF for PDFs only |
| OCR quality poor in Tika | Use cloud OCR (Textract/Vision) |
| Memory issues with Tika | Increase JVM heap or use PyMuPDF |

## Testing the Selector

Run the built-in test scenarios:

```bash
node /home/p62operator/.openclaw/workspace/.agents/skills/pdf-tool-selector/index.js --test
```

This validates the decision matrix against known scenarios.

## Related Skills

- [[gitnexus-exploring]] - For understanding codebase structure when integrating PDF tools
- [[improve]] - For auditing PDF processing pipelines and finding optimization opportunities
