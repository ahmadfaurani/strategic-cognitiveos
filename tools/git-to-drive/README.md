# 📄 Git-to-Drive: Automated PDF Generation → Google Drive

**Always outputs to Google Drive** - Generate professional PDFs from any Git repository using Pandoc + LaTeX (Eisvogel template) and automatically upload to Google Drive.

---

## 🚀 Quick Start

### 1. Initial Setup (One-Time)

```bash
# Run the setup script
cd /home/p62operator/.openclaw/workspace/tools/git-to-drive
chmod +x setup.sh
./setup.sh

# Configure Google Drive access
rclone config
```

**rclone config steps:**
1. Choose `n` for New remote
2. Name it `drive`
3. Select `Google Drive`
4. Use Service Account for automation (recommended)
5. Complete OAuth flow

### 2. Generate & Upload PDF

```bash
# Basic usage
./git-to-drive.sh https://github.com/user/repo

# With custom output name
./git-to-drive.sh https://github.com/user/repo my-documentation

# Custom Drive folder
./git-to-drive.sh https://github.com/user/repo my-docs "/Shared/Docs"

# Local repository
./git-to-drive.sh ./my-local-repo report-2026
```

---

## 📋 Features

✅ **Professional PDF Output**
- Eisvogel LaTeX template (clean, modern design)
- Syntax highlighting for code (Monokai theme)
- Table of contents with section numbering
- Professional typography

✅ **Automatic Google Drive Upload**
- Uploads to `/Git-PDFs` folder by default
- Configurable destination folder
- Generates shareable links

✅ **Smart File Detection**
- Automatically includes README.md
- Scans docs/ folder for documentation
- Includes other markdown files (max 20)

✅ **Flexible Options**
- Custom output names
- Custom Drive folders
- Keep local copy option
- Disable TOC or syntax highlighting

---

## ⚙️ Configuration

### Default Settings

| Setting | Value |
|---------|-------|
| Drive Remote | `drive` |
| Default Folder | `/Git-PDFs` |
| Template | `eisvogel` |
| Highlight Style | `monokai` |
| Keep Local | `false` |

### Environment Variables

```bash
export RCLONE_REMOTE="drive"           # rclone remote name
export DEFAULT_DRIVE_FOLDER="/Git-PDFs" # Default Drive folder
export TEMPLATE="eisvogel"              # LaTeX template
export HIGHLIGHT_STYLE="monokai"        # Syntax highlighting
```

---

## 📖 Usage Examples

### Basic Usage
```bash
# Generate PDF from GitHub repo → Upload to Drive
./git-to-drive.sh https://github.com/torvalds/linux
```

### Custom Output Name
```bash
./git-to-drive.sh https://github.com/user/repo linux-kernel-docs
```

### Custom Drive Folder
```bash
./git-to-drive.sh https://github.com/user/repo docs "/Team/Documentation"
```

### Keep Local Copy
```bash
./git-to-drive.sh https://github.com/user/repo --keep-local
```

### Disable Features
```bash
# No table of contents
./git-to-drive.sh https://github.com/user/repo --no-toc

# No syntax highlighting
./git-to-drive.sh https://github.com/user/repo --no-highlight
```

### Custom Template
```bash
./git-to-drive.sh https://github.com/user/repo --theme kaobook
```

---

## 🔧 Troubleshooting

### rclone not configured
```bash
rclone config
rclone listremotes
```

### LaTeX template not found
```bash
# Reinstall template
wget -O ~/.pandoc/templates/eisvogel.tex https://github.com/enhuiz/eisvogel/raw/main/eisvogel.tex
```

### PDF generation fails
```bash
# Test pandoc manually
pandoc README.md --output=test.pdf --template=eisvogel --listings
```

### Upload fails
```bash
# Test rclone connection
rclone ls drive:/
rclone mkdir drive:/Git-PDFs
```

---

## 📁 File Structure

```
tools/git-to-drive/
├── setup.sh          # One-time setup script
├── git-to-drive.sh   # Main automation script
├── README.md         # This file
└── config/
    └── rclone.conf   # rclone configuration (auto-created)
```

---

## 🎯 Output Location

PDFs are uploaded to:
```
Google Drive → Git-PDFs → [OUTPUT_NAME].pdf
```

Default folder: `/Git-PDFs`

Change with third argument:
```bash
./git-to-drive.sh repo name "/Custom/Folder"
```

---

## 📝 Requirements

- **Pandoc** (installed by setup.sh)
- **LaTeX** (texlive-latex-extra, installed by setup.sh)
- **rclone** (installed by setup.sh)
- **Google Drive** with rclone configured
- **Git** (for cloning repositories)

---

## 🔐 Security Notes

- Service Account JSON stored in `~/.config/rclone/gdrive-service-account.json`
- File permissions: `chmod 600` recommended for service account file
- Share links are generated but not automatically made public
- Review Google Drive sharing settings in your Google Cloud Console

---

## 📚 Related

- [Pandoc Documentation](https://pandoc.org/)
- [Eisvogel Template](https://github.com/enhuiz/eisvogel)
- [rclone Documentation](https://rclone.org/)
- [Google Drive API](https://developers.google.com/drive)

---

**Made for DAF's automated documentation workflow** 🚀
