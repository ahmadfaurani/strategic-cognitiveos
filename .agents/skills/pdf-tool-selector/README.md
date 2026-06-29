# PDF Tool Selector

Intelligently select the optimal PDF processing tool based on document characteristics and use case requirements.

## Overview

This skill provides a decision framework for choosing between three PDF processing tools:

- **PyMuPDF** - Fastest option for high-volume, clean native PDFs
- **pdfplumber** - Best for tables, forms, and structured data extraction
- **Apache Tika** - Multi-format support (1000+ formats) for enterprise environments

## Quick Start

### CLI Usage

```bash
# Run with specific document characteristics
node index.js --hasTables=true --format=pdf --volume=high

# Run test scenarios
node index.js --test

# Show help
node index.js --help
```

### Programmatic Usage (Node.js)

```javascript
const { selectPdfTool } = require('./index.js');

const recommendation = selectPdfTool({
  isScanned: false,
  hasTables: true,
  format: 'pdf',
  volume: 'high',
  needsMetadata: false,
  needsLayoutCoordinates: true
});

console.log(recommendation);
// Output:
// {
//   tool: 'pdfplumber',
//   confidence: 0.92,
//   reasoning: 'Document contains tables requiring precise extraction',
//   alternatives: [...],
//   installCommand: 'pip install pdfplumber',
//   codeExample: '...'
// }
```

### Programmatic Usage (Python)

```python
# The decision logic can be ported to Python:
def select_pdf_tool(is_scanned=False, has_tables=False, format='pdf', 
                    volume='medium', needs_metadata=False, 
                    needs_layout_coordinates=False, enterprise_java=False):
    """
    Port the JavaScript decision logic to Python.
    Returns dict with tool, confidence, reasoning, alternatives.
    """
    pass
```

## Decision Matrix

| Scenario | Recommended Tool | Confidence |
|----------|-----------------|------------|
| Financial reports with tables | pdfplumber | 0.90+ |
| High-volume native PDFs | PyMuPDF | 0.85+ |
| Multi-format documents | Apache Tika | 0.95+ |
| Scanned PDFs (OCR needed) | Apache Tika + Tesseract | 0.80+ |
| Research paper RAG pipeline | PyMuPDF | 0.85+ |
| Invoice processing | pdfplumber | 0.90+ |
| Enterprise Java environment | Apache Tika | 0.80+ |

## Tool Comparison

### PyMuPDF (fitz)

**Best for:**
- High-volume processing (1000+ documents)
- Clean, native PDFs
- Fast text and image extraction
- Performance-critical applications

**Install:**
```bash
pip install PyMuPDF
# or
npm install pymupdf
```

**Example:**
```python
import fitz

doc = fitz.open("document.pdf")
for page in doc:
    text = page.get_text()
```

### pdfplumber

**Best for:**
- Tables and structured data
- Financial reports, invoices, forms
- Precise layout coordinates
- Complex multi-column layouts

**Install:**
```bash
pip install pdfplumber
```

**Example:**
```python
import pdfplumber

with pdfplumber.open("report.pdf") as pdf:
    tables = pdf.pages[0].extract_tables()
```

### Apache Tika

**Best for:**
- Multi-format support (1000+ formats)
- Enterprise Java environments
- Comprehensive metadata extraction
- Mixed document pipelines

**Install:**
```bash
pip install tika
# Requires Java 8+
```

**Example:**
```python
from tika import parser

raw = parser.from_file("document.pdf")
text = raw["content"]
metadata = raw["metadata"]
```

## Test Scenarios

Run built-in tests to validate the decision matrix:

```bash
node index.js --test
```

Expected output:
```
Running PDF Tool Selector Tests

Test: Financial Reports with Tables
  Expected: pdfplumber
  Got: pdfplumber (confidence: 0.95)
  Status: ✅ PASS

...

Results: 7 passed, 0 failed
```

## Integration Examples

### LangChain RAG Pipeline

```python
from langchain.document_loaders import PyMuPDFLoader, PDFPlumberLoader

def get_loader_for_documents(doc_characteristics):
    recommendation = select_pdf_tool(doc_characteristics)
    
    if recommendation['tool'] == 'PyMuPDF':
        return PyMuPDFLoader
    elif recommendation['tool'] == 'pdfplumber':
        return PDFPlumberLoader
    # Tika requires separate server setup
```

### LlamaIndex Integration

```python
from llama_index import SimpleDirectoryReader

def create_reader(recommendation):
    # Configure reader based on tool recommendation
    pass
```

### Batch Processing Pipeline

```python
import os
from pathlib import Path

def process_document_collection(input_dir, output_dir):
    for pdf_path in Path(input_dir).glob('*.pdf'):
        # Analyze document characteristics
        characteristics = analyze_pdf(pdf_path)
        
        # Get tool recommendation
        rec = select_pdf_tool(characteristics)
        
        # Process with recommended tool
        if rec['tool'] == 'PyMuPDF':
            process_with_pymupdf(pdf_path, output_dir)
        elif rec['tool'] == 'pdfplumber':
            process_with_pdfplumber(pdf_path, output_dir)
```

## Configuration Options

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `isScanned` | boolean | false | Document requires OCR |
| `hasTables` | boolean | false | Document contains tables |
| `format` | string | 'pdf' | Document format |
| `volume` | string | 'medium' | Processing volume (low/medium/high) |
| `needsMetadata` | boolean | false | Need comprehensive metadata |
| `needsLayoutCoordinates` | boolean | false | Need precise text positions |
| `enterpriseJava` | boolean | false | Running in Java environment |
| `language` | string | 'en' | Document language |

## Fallback Strategies

| Issue | Recommended Fallback |
|-------|---------------------|
| pdfplumber fails on corrupted PDF | Try PyMuPDF (more tolerant) |
| PyMuPDF misses table structure | Switch to pdfplumber |
| Tika too slow for volume | Use PyMuPDF for PDFs only |
| OCR quality poor in Tika | Use cloud OCR (AWS Textract, Google Vision) |
| Memory issues with Tika | Increase JVM heap or switch to PyMuPDF |

## License

MIT

## Related

- [SKILL.md](./SKILL.md) - Full skill documentation
- [index.js](./index.js) - Implementation
