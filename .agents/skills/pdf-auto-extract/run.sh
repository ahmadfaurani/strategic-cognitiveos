#!/usr/bin/env bash
# PDF Auto-Extract Skill Runner
# Usage: openclaw skill run pdf-auto-extract --source <url-or-path>

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON_SCRIPT="$SCRIPT_DIR/index.py"

# Check Python dependencies
check_deps() {
    python3 -c "import fitz" 2>/dev/null || {
        echo "⚠️  PyMuPDF not installed. Installing..." >&2
        pip3 install PyMuPDF --quiet
    }
    
    python3 -c "import pdfplumber" 2>/dev/null || {
        echo "⚠️  pdfplumber not installed. Installing..." >&2
        pip3 install pdfplumber --quiet
    }
}

# Main
main() {
    check_deps
    
    if [ $# -eq 0 ]; then
        echo "PDF Auto-Extraction Skill"
        echo ""
        echo "Usage:"
        echo "  openclaw skill run pdf-auto-extract --source <url-or-path> [options]"
        echo ""
        echo "Options:"
        echo "  --source, -s    PDF URL or file path (required)"
        echo "  --output, -o    Output JSON file path (optional)"
        echo "  --verbose, -v   Verbose output"
        echo "  --summary       Show summary only"
        echo "  --help, -h      Show this help"
        echo ""
        echo "Examples:"
        echo "  openclaw skill run pdf-auto-extract --source https://example.com/doc.pdf"
        echo "  openclaw skill run pdf-auto-extract -s ./document.pdf --summary"
        echo "  openclaw skill run pdf-auto-extract -s file.pdf -o extracted.json"
        exit 0
    fi
    
    python3 "$PYTHON_SCRIPT" "$@"
}

main "$@"
