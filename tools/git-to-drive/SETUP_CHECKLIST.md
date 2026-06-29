# ✅ Git-to-Drive Setup Checklist

Follow this checklist to get automated PDF → Google Drive working.

---

## ⏱️ Estimated Time: 10-15 minutes

---

## □ Step 1: Run Setup Script (2 min)

```bash
cd /home/p62operator/.openclaw/workspace/tools/git-to-drive
chmod +x *.sh
./setup.sh
```

**What it does:**
- ✅ Installs Pandoc + LaTeX
- ✅ Installs rclone
- ✅ Downloads Eisvogel template
- ✅ Creates config directories

**Expected output:**
```
✅ Setup complete!
Next steps:
  1. Run 'rclone config' to set up your Google Drive remote
```

---

## □ Step 2: Configure Google Drive Access (5 min)

### Option A: Service Account (Recommended)

Follow the guide: `CREDENTIALS_SETUP.md`

**Quick version:**
1. Create Google Cloud project
2. Enable Drive API
3. Create service account
4. Download JSON key
5. Move to `~/.config/rclone/gdrive-service-account.json`
6. Share Drive folder with service account email

### Option B: OAuth (Simpler, Manual)

```bash
rclone config
```

Follow prompts, browser will open for authentication.

---

## □ Step 3: Test rclone Connection (1 min)

```bash
# List configured remotes
rclone listremotes

# Should show: drive:

# Test connection
rclone ls drive:/

# Create test folder
rclone mkdir drive:/Git-PDFs
```

**Expected output:**
```
drive:
```

---

## □ Step 4: Test Full Workflow (3 min)

```bash
# Test with sample repository
./git-to-drive.sh https://github.com/octocat/Hello-World test-output
```

**Expected output:**
```
ℹ️  Repository: https://github.com/octocat/Hello-World
ℹ️  Output: test-output.pdf
ℹ️  Drive Folder: /Git-PDFs
✅ PDF generated: test-output.pdf (245K)
☁️  Uploading to Google Drive...
✅ Upload successful!
```

---

## □ Step 5: Verify in Google Drive (1 min)

1. Open [Google Drive](https://drive.google.com/)
2. Navigate to **Git-PDFs** folder
3. Verify `test-output.pdf` is there
4. Open it to check formatting

**Expected:** Professional PDF with:
- ✅ Clean layout (Eisvogel template)
- ✅ Table of contents
- ✅ Syntax highlighting (if code present)
- ✅ Section numbering

---

## □ Step 6: (Optional) Set Up GitHub Actions (5 min)

For automatic PDF generation on every push:

1. Copy workflow file:
   ```bash
   cp github-workflow.yml /path/to/your/repo/.github/workflows/pdf-to-drive.yml
   ```

2. Add GitHub Secrets:
   - `GDRIVE_SERVICE_ACCOUNT` — JSON key content
   - `GDRIVE_FOLDER_ID` — Drive folder ID (from URL)

3. Push to trigger workflow

---

## 🎯 You're Done!

### Daily Usage

```bash
# Generate PDF from any repo → Upload to Drive
./git-to-drive.sh https://github.com/user/repo

# Custom name
./git-to-drive.sh https://github.com/user/repo my-docs

# Custom folder
./git-to-drive.sh https://github.com/user/repo docs "/Team/Docs"

# Local repo
./git-to-drive.sh ./my-project project-report
```

---

## ❓ Common Issues

| Issue | Solution |
|-------|----------|
| `rclone: command not found` | Run `./setup.sh` again |
| `Permission denied` | Share Drive folder with service account |
| `Template not found` | Check `~/.pandoc/templates/eisvogel.tex` exists |
| `Upload failed` | Run `rclone config` again |

---

## 📞 Need Help?

1. Check `README.md` for detailed docs
2. Check `CREDENTIALS_SETUP.md` for Google Drive setup
3. Run test command: `./git-to-drive.sh --help`

---

**Last updated:** 2026-06-27  
**Status:** ✅ Ready for production use
