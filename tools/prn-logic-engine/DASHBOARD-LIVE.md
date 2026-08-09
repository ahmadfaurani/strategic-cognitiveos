# 🎨 PRN Johor 2026 Dashboard - Live!

## ✅ Dashboard Successfully Deployed!

**URL:** http://localhost:3000  
**Status:** Running ✓  
**Classification:** TLP:AMBER

---

## 📊 What You'll See

### Header Section
```
🗳️ PRN Johor 2026 Campaign Dashboard
Real-time multi-coalition campaign intelligence tracking
Report Date: 2026-06-27 | Campaign Day: D+1
```

### Summary Stats (4 Cards)
| Metric | Value | Icon |
|--------|-------|------|
| Total Candidates Tracked | 14 | 📈 Trending Up |
| Seats Analyzed | 12 | 📍 Map Pin |
| Ceramahs Today | 38 | ⚡ Activity |
| Social Media Reach | 253K | 👥 Users |

### Pie Chart: Seat Status Distribution
- 🟢 **Safe:** 6 seats (50%)
- 🟡 **Contested:** 4 seats (33%)
- 🔴 **Vulnerable:** 2 seats (17%)

### Coalition Sections (PN, BN, PH, Independent)

Each coalition has:

#### 1. Top Developments Card
✓ Muhyiddin lancar jentera di Pagoh, 1000+ hadirin  
✓ PAS kempen agresif di kawasan Melayu  
✓ Bersatu fokus pengundi muda  

#### 2. Key Candidate Activities Table
| Candidate | Seat | Party | Activity | Event |
|-----------|------|-------|----------|-------|
| Muhyiddin Yassin | N14 Pagoh | Bersatu | 🔴 HIGH | Ceramah Perdana |
| Azman Ibrahim | N09 Semerah | PAS | 🔴 HIGH | Kempen masjid |
| Norhayati Omar | N23 Puteri Wangsa | Bersatu | 🟡 MEDIUM | Jumpa belia |

#### 3. Seat Status Table
| Seat | Status | Threat |
|------|--------|--------|
| N14 Pagoh | 🟢 SAFE | 🟢 |
| N09 Semerah | 🟡 CONTESTED | 🟡 |
| N23 Puteri Wangsa | 🔴 VULNERABLE | 🔴 |

#### 4. Performance Metrics Table
| Metric | Achieved | Target | Progress Bar | Status |
|--------|----------|--------|--------------|--------|
| Ceramahs Held | 15 | 18 | ████████░░ 83% | ⚠️ |
| Voter Contacts | 4,200 | 5,000 | ████████░░ 84% | ⚠️ |
| Social Media Reach | 85K | 100K | █████████░ 85% | ⚠️ |
| Volunteer Deployment | 950 | 1,200 | ████████░░ 79% | ⚠️ |

### Bar Charts

#### Ceramahs: Achieved vs Target
- Green bars = Actual ceramahs held
- Orange bars = Target
- Shows PN leading, BN trailing

#### Social Media Reach by Coalition
- PH: 120K (highest)
- PN: 85K
- BN: 45K
- Independent: 3.4K

### Risk Alert Section (Red Border Cards)

🔴 **PN: Undi Melayu Terpecah**  
Calon bebas di beberapa DUN mungkin pecah undi Melayu, bantu PH menang.

🔴 **BN: Undi Cina Rendah**  
Pengundi Cina menunjukkan minat rendah. Perlu jumpa persatuan.

🔴 **PH: Pengundi Melayu Swing**  
Risiko pengundi Melayu swing ke PN. Tonjolkan calon AMANAH.

---

## 🎨 Color Scheme

**Background:** Dark theme (#0f172a - Slate 900)  
**Cards:** #1e293b (Slate 800)  
**Text:** #e2e8f0 (Slate 200)  
**Borders:** #334155 (Slate 700)

**Coalition Colors:**
- PN: 🟢 Green (#16a34a)
- BN: 🟠 Orange (#f59e0b)
- PH: 🔵 Blue (#3b82f6)
- Independent: 🟣 Purple (#8b5cf6)

**Status Colors:**
- Safe: 🟢 Green (#22c55e)
- Contested: 🟡 Yellow/Orange (#f59e0b)
- Vulnerable: 🔴 Red (#ef4444)

**Activity Levels:**
- High: 🔴 Red (#ef4444)
- Medium: 🟡 Yellow/Orange (#f59e0b)
- Low: 🟢 Green (#22c55e)

---

## 🚀 How to Access

### Local Access (Development)
```bash
cd /home/p62operator/.openclaw/workspace-hoi/intelligence/prn-johor-2026/dashboard
npm run dev
```
Open: http://localhost:3000

### Production Deployment

#### Option 1: Build & Serve Locally
```bash
npm run build
# Files in dist/ directory
# Copy to web server or serve with nginx
```

#### Option 2: Deploy to Vercel
```bash
npm install -g vercel
vercel --prod
```

#### Option 3: Docker
```bash
docker build -t prn-dashboard .
docker run -p 8080:80 prn-dashboard
```

---

## 📁 Files Created

```
dashboard/
├── src/
│   ├── App.tsx                    # Main dashboard component (22KB)
│   ├── main.tsx                   # React entry point
│   ├── index.css                  # Dark theme styles
│   └── data/
│       └── dashboard-data.json    # Generated from markdown reports
├── scripts/
│   └── generate-dashboard-data.ts # Parser: Markdown → JSON
├── package.json                   # Dependencies (React, Recharts, Vite)
├── tsconfig.json                  # TypeScript config
├── vite.config.ts                 # Vite config
├── index.html                     # HTML template
└── README.md                      # Full documentation
```

---

## 🔄 Data Flow

```
Daily Reports (Markdown)
  ↓ 9:00 AM - Cron job generates reports
coalition-analysis/
  ├── pn-daily-2026-06-27.md
  ├── bn-daily-2026-06-27.md
  ├── ph-daily-2026-06-27.md
  └── independent-daily-2026-06-27.md
  ↓ 12:00 PM - Generate dashboard data
npm run generate-data
  ↓
src/data/dashboard-data.json
  ↓ Auto-refresh every 5 min (future)
React Dashboard
  ↓
http://localhost:3000
```

---

## ✨ Features

### ✅ Currently Working
- Multi-coalition overview (PN, BN, PH, Independent)
- Summary statistics cards
- Seat status pie chart
- Candidate activity tables with heatmaps
- Performance metrics with progress bars
- Ceramah comparison bar chart
- Social media reach bar chart
- Risk alert cards
- Dark theme UI
- Responsive grid layout

### 🚧 Future Enhancements
- [ ] Real-time data refresh (WebSocket)
- [ ] Interactive Johor state map
- [ ] Historical trend charts (Day 1 → Day 14)
- [ ] Search & filter functionality
- [ ] Export to PDF/PPT
- [ ] Mobile app version
- [ ] Login/authentication
- [ ] Social media API integration
- [ ] Sentiment analysis visualization
- [ ] Predictive analytics (vote projections)

---

## 📊 Sample Dashboard Data

**Total Candidates:** 14 tracked  
**Total Seats:** 12 analyzed  
**Total Ceramahs:** 38 held today  
**Total Social Reach:** 253K impressions

**Coalition Breakdown:**
- PN: 5 candidates, 3 seats, 15 ceramahs, 85K reach
- BN: 5 candidates, 3 seats, 8 ceramahs, 45K reach
- PH: 5 candidates, 3 seats, 12 ceramahs, 120K reach
- Independent: 3 candidates, 3 seats, 3 ceramahs, 3.4K reach

---

## 🔒 Security Notes

**Classification:** TLP:AMBER

✅ **DO:**
- Host on private network
- Require authentication for production
- Use HTTPS
- Keep repository private

❌ **DON'T:**
- Deploy to public URLs without auth
- Share links externally
- Commit dashboard-data.json to Git

---

## 🛠️ Troubleshooting

**Dashboard not loading?**
```bash
# Check if server is running
curl http://localhost:3000

# Restart server
npm run dev

# Clear cache
rm -rf node_modules dist
npm install
npm run dev
```

**No data showing?**
```bash
# Regenerate data
npm run generate-data

# Check if reports exist
ls -la ../coalition-analysis/*-daily-*.md
```

**Port 3000 in use?**
```bash
# Edit vite.config.ts, change port to 3001
# Or kill existing process
lsof -ti:3000 | xargs kill
```

---

## 📞 Support

**Dashboard running at:** http://localhost:3000  
**Source code:** `/home/p62operator/.openclaw/workspace-hoi/intelligence/prn-johor-2026/dashboard`  
**Data source:** `coalition-analysis/` markdown reports  

For issues, check the README.md or contact the war room tech team.

---

**🎉 Dashboard is LIVE and ready for war room use!**
