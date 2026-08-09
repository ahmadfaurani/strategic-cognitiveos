# PRN Johor 2026 Campaign Dashboard

**Real-time multi-coalition campaign intelligence visualization**

**Classification:** TLP:AMBER - For Internal War Room Use Only

---

## Overview

React-based dashboard for visualizing PRN Johor 2026 campaign data across all coalitions:
- **PN** (PAS + Bersatu + MIPP + Pejuang)
- **BN** (UMNO + MCA + MIC + Gerakan + PBRS)
- **PH** (DAP + PKR + Amanah + UPKO)
- **Independent Candidates**

---

## Features

### 📊 Dashboard Views
- **Summary Statistics** - Total candidates, seats, ceramahs, social media reach
- **Coalition Breakdown** - Individual performance metrics per coalition
- **Seat Status Distribution** - Safe/Contested/Vulnerable pie chart
- **Ceramah Progress** - Achieved vs Target bar charts
- **Social Media Reach** - Coalition comparison
- **Risk Alerts** - High priority risks with mitigation status

### 📈 Data Visualized
- Candidate activity heatmaps (🔴🟡🟢)
- Seat-by-seat status analysis
- Performance metrics with progress bars
- Top 3 campaign developments per coalition
- Key candidate activities and events

---

## Quick Start

### Prerequisites
- Node.js 18+ 
- npm or yarn
- Git (for pulling latest reports)

### Installation

```bash
cd /home/p62operator/.openclaw/workspace-hoi/intelligence/prn-johor-2026/dashboard

# Install dependencies
npm install

# Generate data from latest markdown reports
npm run generate-data

# Start development server
npm run dev
```

Dashboard will open at: **http://localhost:3000**

---

## Production Build

```bash
# Build for production
npm run build

# Preview production build
npm run preview
```

Output: `dist/` directory (static files)

---

## Deployment Options

### Option 1: GitHub Pages (Recommended for Internal Use)

```bash
# Install gh-pages
npm install -D gh-pages

# Add to package.json scripts:
"deploy": "npm run build && gh-pages -d dist"

# Deploy
npm run deploy
```

Access at: `https://ahmadfaurani.github.io/PRN-Johor-2026-H/dashboard/`

**Note:** Repository must be private. Use GitHub Pages with private repo access.

### Option 2: Vercel

```bash
# Install Vercel CLI
npm install -g vercel

# Deploy
vercel --prod
```

Auto-detects Vite config. Deploy to: `https://prn-johor-2026-dashboard.vercel.app`

### Option 3: Local Network (War Room)

```bash
# Build
npm run build

# Serve with nginx
sudo cp -r dist/* /var/www/html/
sudo systemctl restart nginx
```

Access at: `http://<server-ip>/`

### Option 4: Docker

```dockerfile
# Dockerfile
FROM node:20-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build
FROM nginx:alpine
COPY --from=0 /app/dist /usr/share/nginx/html
EXPOSE 80
```

```bash
docker build -t prn-dashboard .
docker run -p 8080:80 prn-dashboard
```

---

## Data Flow

```
Daily Reports (Markdown)
  ↓
generate-dashboard-data.ts (Parser)
  ↓
dashboard-data.json (Structured JSON)
  ↓
React App (Visualization)
  ↓
Dashboard (Browser)
```

### Automated Updates

To auto-refresh data daily:

1. **Cron Job** (already set up for reports)
2. **Add data generation step:**

```bash
# Add to existing cron job or create new one
0 12 * * * cd /home/p62operator/.openclaw/workspace-hoi/intelligence/prn-johor-2026/dashboard && npm run generate-data
```

3. **Dashboard auto-refresh:**
   - Add `setInterval` in App.tsx to fetch new data every 5 minutes
   - Or use WebSocket for real-time updates

---

## File Structure

```
dashboard/
├── src/
│   ├── App.tsx              # Main dashboard component
│   ├── main.tsx             # React entry point
│   ├── index.css            # Dashboard styles
│   ├── data/
│   │   └── dashboard-data.json  # Generated data (gitignore)
│   └── components/          # Reusable components (future)
├── scripts/
│   └── generate-dashboard-data.ts  # Markdown → JSON parser
├── public/
├── package.json
├── tsconfig.json
├── vite.config.ts
└── README.md
```

---

## Customization

### Add New Metrics

Edit `src/App.tsx`:
```typescript
// Add to CoalitionMetrics interface
interface CoalitionMetrics {
  // ... existing metrics
  newMetric: number
  newMetricTarget: number
}

// Add to table in App component
<tr>
  <td>New Metric</td>
  <td>{coalition.metrics.newMetric}</td>
  <td>{coalition.metrics.newMetricTarget}</td>
  ...
</tr>
```

### Add New Charts

Install Recharts components:
```typescript
import { LineChart, Line, AreaChart, Area } from 'recharts'

// Add new chart section
<div className="chart-container">
  <h3>📈 Trend Analysis</h3>
  <ResponsiveContainer width="100%" height={300}>
    <LineChart data={trendData}>
      ...
    </LineChart>
  </ResponsiveContainer>
</div>
```

### Theme Colors

Edit `src/index.css`:
```css
.coalition-badge.pn { background: #16a34a; }  /* Green */
.coalition-badge.bn { background: #f59e0b; }  /* Orange */
.coalition-badge.ph { background: #3b82f6; }  /* Blue */
.coalition-badge.independent { background: #8b5cf6; }  /* Purple */
```

---

## API Integration (Future)

To connect to a real-time API instead of static JSON:

1. **Create API endpoint** (Node.js/Express, Python/FastAPI, etc.)
2. **Replace mock data in App.tsx:**

```typescript
useEffect(() => {
  fetch('http://localhost:8080/api/dashboard-data')
    .then(res => res.json())
    .then(data => setData(data))
    .catch(err => console.error(err))
}, [])
```

3. **Set up WebSocket for real-time updates:**

```typescript
useEffect(() => {
  const ws = new WebSocket('ws://localhost:8080/ws')
  ws.onmessage = (event) => {
    const data = JSON.parse(event.data)
    setData(data)
  }
  return () => ws.close()
}, [])
```

---

## Security Considerations

### TLP:AMBER Classification

✅ **DO:**
- Host on private network or authenticated service
- Require login for access
- Use HTTPS in production
- Keep repository private

❌ **DON'T:**
- Deploy to public URLs without authentication
- Share dashboard links externally
- Include sensitive operational details in client-side code
- Commit `dashboard-data.json` to Git (add to `.gitignore`)

### Recommended Setup

```bash
# .gitignore
src/data/dashboard-data.json
node_modules/
dist/
.env
```

```bash
# .env (for API keys if needed)
VITE_API_URL=http://internal-server:8080
VITE_REQUIRE_AUTH=true
```

---

## Troubleshooting

### "Cannot find module 'react'"
```bash
npm install
```

### Dashboard shows mock data
```bash
npm run generate-data
# Check if markdown reports exist in coalition-analysis/
```

### Build fails
```bash
# Clear cache
rm -rf node_modules dist
npm install
npm run build
```

### Port 3000 in use
```bash
# Edit vite.config.ts
server: {
  port: 3001  // Change port
}
```

---

## Performance Optimization

For large datasets (100+ seats, 500+ candidates):

1. **Virtualize tables:**
   ```bash
   npm install react-virtualized
   ```

2. **Lazy load charts:**
   ```typescript
   const ChartComponent = lazy(() => import('./ChartComponent'))
   ```

3. **Memoize expensive calculations:**
   ```typescript
   const processedData = useMemo(() => processData(rawData), [rawData])
   ```

4. **Debounce search/filter:**
   ```typescript
   const debouncedSearch = useMemo(() => debounce(search, 300), [])
   ```

---

## Future Enhancements

- [ ] Real-time WebSocket updates
- [ ] Interactive seat maps (Johor state map visualization)
- [ ] Historical trend analysis (Day 1 vs Day 2 vs Day 3)
- [ ] Export to PDF/PPT for war room briefings
- [ ] Mobile-responsive design
- [ ] Dark/light theme toggle
- [ ] Filtering by party, seat, activity level
- [ ] Search functionality
- [ ] Alerts for critical changes (status flips, risk escalation)
- [ ] Integration with social media APIs for live metrics

---

## Support

**Maintained by:** Hermes Agent  
**Workspace:** `/home/p62operator/.openclaw/workspace-hoi/intelligence/prn-johor-2026`  
**Dashboard:** `/home/p62operator/.openclaw/workspace-hoi/intelligence/prn-johor-2026/dashboard`

For issues or feature requests, check the main repository or contact the war room tech team.

---

**Version:** 1.0  
**Last Updated:** 2026-06-27  
**Classification:** TLP:AMBER
