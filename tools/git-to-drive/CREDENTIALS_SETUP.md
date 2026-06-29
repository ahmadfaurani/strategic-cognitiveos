# 🔐 Google Drive Credentials Setup Guide

This guide walks you through setting up Google Drive access for automated PDF uploads.

---

## 🎯 Option 1: Service Account (Recommended for Automation)

**Best for:** Automated scripts, CI/CD, server deployments

### Step 1: Create Google Cloud Project

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Click **Create Project** or select existing project
3. Name it (e.g., "Git-to-Drive-Automation")

### Step 2: Enable Drive API

1. In your project, go to **APIs & Services → Library**
2. Search for "Google Drive API"
3. Click **Enable**

### Step 3: Create Service Account

1. Go to **APIs & Services → Credentials**
2. Click **Create Credentials → Service Account**
3. Fill in:
   - **Service account name:** `git-to-drive-automation`
   - **Description:** Automated PDF uploads to Google Drive
4. Click **Create and Continue**
5. Skip role assignment (not needed for personal Drive)
6. Click **Done**

### Step 4: Generate JSON Key

1. Click on the newly created service account
2. Go to **Keys** tab
3. Click **Add Key → Create new key**
4. Select **JSON** format
5. Click **Create**
6. Download the JSON file (auto-downloads)

### Step 5: Secure the Key File

```bash
# Move to rclone config directory
mv ~/Downloads/your-key-file.json ~/.config/rclone/gdrive-service-account.json

# Set secure permissions
chmod 600 ~/.config/rclone/gdrive-service-account.json
```

### Step 6: Configure rclone

```bash
rclone config
```

Follow these prompts:
```
name> drive
Storage> drive
client_id> (leave blank)
client_secret> (leave blank)
service_account_file> /home/p62operator/.config/rclone/gdrive-service-account.json
scope> drive
edit_advanced_settings> n
```

### Step 7: Share Google Drive Folder

**Important:** Service accounts can't access your personal Drive by default.

1. Go to [Google Drive](https://drive.google.com/)
2. Create a folder (e.g., "Git-PDFs")
3. Right-click → **Share**
4. Paste the **service account email** (from the JSON file, looks like: `git-to-drive-automation@project-id.iam.gserviceaccount.com`)
5. Give **Editor** permissions
6. Click **Share**

### Step 8: Test Connection

```bash
# List files in Drive
rclone ls drive:/

# Create test folder
rclone mkdir drive:/Git-PDFs

# Upload test file
echo "test" > test.txt
rclone copy test.txt drive:/Git-PDFs/
rm test.txt

# Verify upload
rclone ls drive:/Git-PDFs/
```

---

## 🎯 Option 2: OAuth (Interactive Use)

**Best for:** Personal use, manual uploads

```bash
rclone config
```

Follow prompts:
```
name> drive
Storage> drive
client_id> (leave blank)
client_secret> (leave blank)
scope> drive
remote> (leave blank)
service_account_file> (leave blank)
use_auto_config> y
```

Browser will open for OAuth authentication.

---

## 📋 Configuration File Location

```
~/.config/rclone/rclone.conf
```

Example content:
```ini
[drive]
type = drive
scope = drive
service_account_file = /home/p62operator/.config/rclone/gdrive-service-account.json
acknowledge_abuse = true
```

---

## 🔍 Finding Your Google Drive Folder ID

For GitHub Actions workflow, you need the folder ID:

1. Open Google Drive in browser
2. Navigate to the folder
3. Look at the URL: `https://drive.google.com/drive/folders/1ABC123xyz...`
4. The ID is: `1ABC123xyz...`

Use this in GitHub Secrets as `GDRIVE_FOLDER_ID`.

---

## 🛡️ Security Best Practices

1. **Never commit** service account JSON to git
2. **Set permissions:** `chmod 600 ~/.config/rclone/gdrive-service-account.json`
3. **Limit scope:** Only share specific folders with service account
4. **Rotate keys:** Regenerate service account keys periodically
5. **Monitor usage:** Check Google Cloud Console for unusual activity

---

## 🧪 Testing

```bash
# Test rclone connection
rclone listremotes

# Test Drive access
rclone ls drive:/

# Test upload
echo "test" | rclone rcat drive:/Git-PDFs/test.txt

# Verify
rclone cat drive:/Git-PDFs/test.txt

# Cleanup
rclone delete drive:/Git-PDFs/test.txt
```

---

## ❓ Troubleshooting

### "Permission denied"
- Make sure you shared the folder with the service account email
- Check folder ID is correct

### "Service account not found"
- Verify path in rclone.conf
- Check file exists: `ls -la ~/.config/rclone/gdrive-service-account.json`

### "API not enabled"
- Enable Drive API in Google Cloud Console
- Wait 5 minutes for propagation

### "Quota exceeded"
- Google Drive has API rate limits
- Wait and retry, or request quota increase

---

## 📚 References

- [rclone Google Drive Setup](https://rclone.org/drive/)
- [Google Drive API Docs](https://developers.google.com/drive/api)
- [Service Account Authentication](https://cloud.google.com/docs/authentication/production)

---

**Need help?** Run `./setup.sh` for guided setup.
