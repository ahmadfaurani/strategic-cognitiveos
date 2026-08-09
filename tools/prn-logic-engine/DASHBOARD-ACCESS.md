# 🎉 PRN Johor 2026 Dashboard - ACCESS GUIDE

## ✅ Dashboard is LIVE and Accessible!

---

## 🔗 **Access URLs**

### **Local Network Access** (From any device on your WiFi/LAN)
```
http://192.168.1.102:8082
```

### **Localhost Access** (From the server itself)
```
http://localhost:8082
```

---

## 📱 **How to Access from Your Phone/Computer**

1. **Make sure you're on the same network** as the server (same WiFi)

2. **Open your browser** (Chrome, Safari, Firefox, etc.)

3. **Type this URL:**
   ```
   http://192.168.1.102:8082
   ```

4. **You should see the dashboard!** 🎊

---

## 🖥️ **What You'll See**

The dashboard displays:

- **Summary Statistics** - Total candidates, seats, ceramahs, social media reach
- **Seat Status Pie Chart** - Safe/Contested/Vulnerable distribution
- **Coalition Breakdowns** (PN, BN, PH, Independent):
  - Top 3 campaign developments
  - Candidate activity tables with heatmaps (🔴🟡🟢)
  - Seat status tables
  - Performance metrics with progress bars
- **Bar Charts** - Ceramahs comparison, Social media reach
- **Risk Alerts** - High priority risks with mitigation notes

---

## 🎨 **Visual Features**

- **Dark theme** - Easy on the eyes for war room displays
- **Responsive design** - Works on phones, tablets, and desktops
- **Color-coded coalitions**:
  - PN = 🟢 Green
  - BN = 🟠 Orange
  - PH = 🔵 Blue
  - Independent = 🟣 Purple

---

## 🔄 **Updating Dashboard Data**

The dashboard currently shows **mock data**. To update with real data from your markdown reports:

```bash
cd /home/p62operator/.openclaw/workspace-hoi/intelligence/prn-johor-2026/dashboard
npm run generate-data
```

Then refresh your browser.

---

## 🚀 **Making it Publicly Accessible** (Optional)

If you need to access the dashboard from **outside your local network** (e.g., from mobile data or a different location), you have a few options:

### **Option 1: Deploy to Vercel** (Recommended - Free, 5 minutes)

```bash
cd /home/p62operator/.openclaw/workspace-hoi/intelligence/prn-johor-2026/dashboard
npm install -g vercel
vercel --prod
```

You'll get a URL like: `https://prn-johor-2026-dashboard.vercel.app`

### **Option 2: GitHub Pages** (Free, 10 minutes)

```bash
cd dashboard
npm install -D gh-pages
npm run deploy
```

Access at: `https://ahmadfaurani.github.io/PRN-Johor-2026-H/dashboard/`

### **Option 3: Cloudflare Tunnel** (Free, secure, 10 minutes)

```bash
# Install cloudflared
curl -L --output cloudflared.deb https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb
sudo dpkg -i cloudflared.deb

# Create tunnel (follow prompts)
cloudflared tunnel login
cloudflared tunnel create prn-dashboard

# Run tunnel
cloudflared tunnel run prn-dashboard
```

You'll get a secure URL like: `https://prn-dashboard.trycloudflare.com`

---

## 📊 **Current Server Info**

- **Server IP:** 192.168.1.102
- **Port:** 8082
- **Status:** ✅ Running
- **Process ID:** Check with `ps aux | grep python3`

---

## 🛑 **Stopping the Dashboard Server**

```bash
# Find the process
ps aux | grep "http.server 8082"

# Kill it (replace PID with actual number)
kill <PID>
```

---

## 🔄 **Restarting the Dashboard**

```bash
cd /home/p62operator/.openclaw/workspace-hoi/intelligence/prn-johor-2026/dashboard

# Rebuild (if you made changes)
npm run build

# Serve
cd dist
python3 -m http.server 8082 --bind 0.0.0.0
```

---

## 📱 **Mobile Access Tips**

- The dashboard is **responsive** and works on mobile browsers
- For best experience, use **landscape mode** on phones
- Add to home screen for quick access:
  - **iOS Safari:** Share → Add to Home Screen
  - **Android Chrome:** Menu → Add to Home screen

---

## 🔒 **Security Notes**

**Current setup:**
- ✅ Accessible only on local network (192.168.x.x)
- ✅ No authentication required (LAN-only is considered secure enough for internal use)
- ⚠️ **Do NOT expose port 8082 to the internet** without authentication

**For public access:**
- Use Vercel/GitHub Pages (they handle security)
- Or add authentication middleware before deploying publicly

---

## 📞 **Troubleshooting**

### "Can't connect to 192.168.1.102:8082"

1. **Check if server is running:**
   ```bash
   curl http://localhost:8082
   ```
   Should return HTML

2. **Check firewall:**
   ```bash
   sudo ufw allow 8082/tcp
   ```

3. **Verify you're on the same network** as the server

4. **Try pinging the server:**
   ```bash
   ping 192.168.1.102
   ```

### "Dashboard shows blank page"

1. **Check browser console** (F12) for errors
2. **Clear browser cache** and reload
3. **Try a different browser**

### "Data looks wrong/outdated"

```bash
cd dashboard
npm run generate-data
# Then refresh browser
```

---

## 📈 **Next Steps**

1. ✅ **Access the dashboard** from your device
2. ✅ **Verify all data displays correctly**
3. 🔄 **Set up automated data refresh** (optional)
4. 🌐 **Deploy to public URL** if you need remote access (optional)
5. 🎨 **Customize** colors, metrics, or add new features (optional)

---

## 🎯 **Quick Access Bookmark**

**Bookmark this URL:** `http://192.168.1.102:8082`

---

**Dashboard Version:** 1.0  
**Last Updated:** 2026-06-27  
**Classification:** TLP:AMBER - For Internal War Room Use Only

**Need help?** Check the full README at `dashboard/README.md`
