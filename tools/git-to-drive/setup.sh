#!/bin/bash
# Git-to-Drive Setup Script
# Sets up Pandoc + LaTeX + rclone for automated PDF generation to Google Drive

set -e

echo "🔧 Setting up Git-to-Drive automation..."

# Install Pandoc and LaTeX
echo "📦 Installing Pandoc and LaTeX..."
sudo apt update
sudo apt install -y pandoc texlive-latex-extra texlive-fonts-extra texlive-science

# Install rclone
echo "📦 Installing rclone..."
curl https://rclone.org/install.sh | sudo bash

# Download Eisvogel template
echo "📥 Downloading Eisvogel LaTeX template..."
mkdir -p ~/.pandoc/templates
wget -O ~/.pandoc/templates/eisvogel.tex https://github.com/enhuiz/eisvogel/raw/main/eisvogel.tex

# Configure rclone for Google Drive
echo "🔐 Configuring rclone for Google Drive..."
echo ""
echo "⚠️  IMPORTANT: You need to configure rclone for Google Drive access."
echo ""
echo "Run this command and follow the prompts:"
echo "  rclone config"
echo ""
echo "Steps:"
echo "  1. Choose 'n' for New remote"
echo "  2. Name it 'drive' (or your preferred name)"
echo "  3. Select 'Google Drive' from the list"
echo "  4. Choose authentication method (recommended: Service Account for automation)"
echo "  5. Complete the OAuth flow"
echo ""
echo "For Service Account (recommended for automation):"
echo "  - Create a Google Cloud Service Account"
echo "  - Enable Drive API"
echo "  - Download JSON key file"
echo "  - Place it at ~/.config/rclone/gdrive-service-account.json"
echo ""

# Create config directory
mkdir -p ~/.config/rclone

# Create rclone config template
cat > ~/.config/rclone/rclone.conf.template << 'EOF'
[drive]
type = drive
scope = drive
service_account_file = /home/p62operator/.config/rclone/gdrive-service-account.json
acknowledge_abuse = true
EOF

echo ""
echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "  1. Run 'rclone config' to set up your Google Drive remote"
echo "  2. Test with: rclone listremotes"
echo "  3. Run the git-to-drive script: ./git-to-drive.sh <repo-url> [output-name]"
echo ""
