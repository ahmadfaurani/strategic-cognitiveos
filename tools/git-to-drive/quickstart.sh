#!/bin/bash
# Quick Start: One-command setup and test
# Run this to get started immediately

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🚀 Git-to-Drive Quick Start"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Check if rclone is already configured
if rclone listremotes 2>/dev/null | grep -q "drive:"; then
    echo "✅ rclone Google Drive already configured"
else
    echo "⚠️  Google Drive not configured yet"
    echo ""
    echo "Please run:"
    echo "  ./setup.sh"
    echo ""
    echo "Then configure rclone with: rclone config"
    echo ""
    exit 1
fi

# Test with a sample repo
echo "📥 Testing with a sample repository..."
echo ""

./git-to-drive.sh https://github.com/octocat/Hello-World test-output

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✅ Setup complete and tested!"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "Next steps:"
echo "  1. Check your Google Drive → Git-PDFs folder"
echo "  2. Use the script: ./git-to-drive.sh <your-repo>"
echo "  3. Read the docs: cat README.md"
echo ""
