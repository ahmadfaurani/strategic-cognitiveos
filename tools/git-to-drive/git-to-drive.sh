#!/bin/bash
# Git-to-Drive: Automatic PDF Generation & Upload to Google Drive
# Usage: ./git-to-drive.sh <repo-url> [output-name] [drive-folder]
#
# Always outputs to Google Drive - no local PDF kept unless specified

set -e

# Configuration
RCLONE_REMOTE="drive"
DEFAULT_DRIVE_FOLDER="/Git-PDFs"
TEMPLATE="eisvogel"
HIGHLIGHT_STYLE="monokai"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Functions
log_info() {
    echo -e "${GREEN}ℹ️  $1${NC}"
}

log_warn() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

log_error() {
    echo -e "${RED}❌ $1${NC}"
}

show_help() {
    cat << EOF
📄 Git-to-Drive: Generate PDF from Git repo → Upload to Google Drive

Usage: $0 <repo-url> [output-name] [drive-folder]

Arguments:
  repo-url      GitHub/Git repository URL (or local path)
  output-name   Output PDF name (default: auto-generated from repo name)
  drive-folder  Google Drive folder path (default: $DEFAULT_DRIVE_FOLDER)

Options:
  -h, --help     Show this help message
  --no-toc       Disable table of contents
  --no-highlight Disable syntax highlighting
  --theme NAME   Use different LaTeX template (default: eisvogel)
  --keep-local   Keep local PDF copy after upload

Examples:
  $0 https://github.com/user/repo
  $0 https://github.com/user/repo my-documentation
  $0 https://github.com/user/repo my-docs "/Shared/Docs"
  $0 ./local-repo-path report-2026

EOF
}

# Parse arguments
KEEP_LOCAL=false
NO_TOC=false
NO_HIGHLIGHT=false

while [[ $# -gt 0 ]]; do
    case $1 in
        -h|--help)
            show_help
            exit 0
            ;;
        --keep-local)
            KEEP_LOCAL=true
            shift
            ;;
        --no-toc)
            NO_TOC=true
            shift
            ;;
        --no-highlight)
            NO_HIGHLIGHT=true
            shift
            ;;
        --theme)
            TEMPLATE="$2"
            shift 2
            ;;
        *)
            if [[ -z "$REPO_URL" ]]; then
                REPO_URL="$1"
            elif [[ -z "$OUTPUT_NAME" ]]; then
                OUTPUT_NAME="$1"
            elif [[ -z "$DRIVE_FOLDER" ]]; then
                DRIVE_FOLDER="$1"
            fi
            shift
            ;;
    esac
done

# Validate inputs
if [[ -z "$REPO_URL" ]]; then
    log_error "Repository URL or path is required"
    show_help
    exit 1
fi

# Set defaults
DRIVE_FOLDER="${DRIVE_FOLDER:-$DEFAULT_DRIVE_FOLDER}"
TEMP_DIR=$(mktemp -d)

# Generate output name from repo if not specified
if [[ -z "$OUTPUT_NAME" ]]; then
    if [[ "$REPO_URL" =~ ^https?:// ]]; then
        # Extract repo name from URL
        REPO_NAME=$(basename "$REPO_URL" .git | sed 's/\.git$//')
        OUTPUT_NAME="${REPO_NAME}-$(date +%Y%m%d-%H%M%S).pdf"
    else
        # Local path
        REPO_NAME=$(basename "$REPO_URL")
        OUTPUT_NAME="${REPO_NAME}-$(date +%Y%m%d-%H%M%S).pdf"
    fi
fi

PDF_FILE="$TEMP_DIR/$OUTPUT_NAME"

log_info "📥 Repository: $REPO_URL"
log_info "📄 Output: $OUTPUT_NAME"
log_info "📁 Drive Folder: $DRIVE_FOLDER"
log_info "🎨 Template: $TEMPLATE"

# Clone or copy repository
log_info "📥 Fetching repository..."
if [[ "$REPO_URL" =~ ^https?:// ]]; then
    git clone --depth 1 "$REPO_URL" "$TEMP_DIR/repo" 2>/dev/null || {
        log_error "Failed to clone repository"
        exit 1
    }
else
    # Local path
    if [[ ! -d "$REPO_URL" ]]; then
        log_error "Local path does not exist: $REPO_URL"
        exit 1
    fi
    cp -r "$REPO_URL" "$TEMP_DIR/repo"
fi

cd "$TEMP_DIR/repo"

# Find markdown files to include
MARKDOWN_FILES=""
if [[ -f "README.md" ]]; then
    MARKDOWN_FILES="README.md"
fi

# Add docs folder if exists
if [[ -d "docs" ]]; then
    MARKDOWN_FILES="$MARKDOWN_FILES docs/**/*.md"
fi

# Add all other .md files
OTHER_MD=$(find . -maxdepth 3 -name "*.md" ! -path "./.git/*" ! -name "README.md" 2>/dev/null | head -20 | tr '\n' ' ')
if [[ -n "$OTHER_MD" ]]; then
    MARKDOWN_FILES="$MARKDOWN_FILES $OTHER_MD"
fi

if [[ -z "$MARKDOWN_FILES" || "$MARKDOWN_FILES" == "README.md" ]]; then
    # Just use README if nothing else found
    MARKDOWN_FILES="README.md"
fi

log_info "📝 Including files: $MARKDOWN_FILES"

# Build pandoc command
PANDOC_CMD="pandoc $MARKDOWN_FILES --output=$PDF_FILE"

# Add template
PANDOC_CMD="$PANDOC_CMD --template=$TEMPLATE"

# Add syntax highlighting
if [[ "$NO_HIGHLIGHT" == false ]]; then
    PANDOC_CMD="$PANDOC_CMD --listings --highlight-style=$HIGHLIGHT_STYLE"
fi

# Add table of contents
if [[ "$NO_TOC" == false ]]; then
    PANDOC_CMD="$PANDOC_CMD --toc --toc-depth=3"
fi

# Add section numbering
PANDOC_CMD="$PANDOC_CMD --number-sections"

# Add metadata
PANDOC_CMD="$PANDOC_CMD --metadata title=\"$OUTPUT_NAME\""
PANDOC_CMD="$PANDOC_CMD --metadata date=\"$(date +%Y-%m-%d)\""

log_info "📝 Generating PDF with Pandoc + LaTeX..."
log_info "   Command: $PANDOC_CMD"

# Execute pandoc
eval $PANDOC_CMD || {
    log_error "PDF generation failed"
    exit 1
}

# Verify PDF was created
if [[ ! -f "$PDF_FILE" ]]; then
    log_error "PDF file was not created"
    exit 1
}

PDF_SIZE=$(du -h "$PDF_FILE" | cut -f1)
log_info "✅ PDF generated: $OUTPUT_NAME ($PDF_SIZE)"

# Upload to Google Drive
log_info "☁️  Uploading to Google Drive..."

# Create folder if it doesn't exist
rclone mkdir "$RCLONE_REMOTE:$DRIVE_FOLDER" 2>/dev/null || true

# Upload file
rclone copy "$PDF_FILE" "$RCLONE_REMOTE:$DRIVE_FOLDER/" || {
    log_error "Upload to Google Drive failed"
    log_warn "Make sure rclone is configured: run 'rclone config'"
    exit 1
}

# Get shareable link
SHARE_LINK=$(rclone link "$RCLONE_REMOTE:$DRIVE_FOLDER/$OUTPUT_NAME" 2>/dev/null || echo "N/A")

log_info "✅ Upload successful!"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📊 Summary"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "   Repository:  $REPO_URL"
echo "   PDF Name:    $OUTPUT_NAME"
echo "   File Size:   $PDF_SIZE"
echo "   Drive Path:  $RCLONE_REMOTE:$DRIVE_FOLDER/$OUTPUT_NAME"
if [[ "$SHARE_LINK" != "N/A" ]]; then
    echo "   Share Link:  $SHARE_LINK"
fi
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Cleanup
if [[ "$KEEP_LOCAL" == false ]]; then
    log_info "🧹 Cleaning up temporary files..."
    rm -rf "$TEMP_DIR"
else
    log_info "📁 Local copy kept at: $PDF_FILE"
fi

echo ""
log_info "✨ Done! PDF is now in your Google Drive."
