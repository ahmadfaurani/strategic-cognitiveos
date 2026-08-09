# PRN Johor 2026 - Automation Deployment Summary

**Classification:** TLP:AMBER  
**Deployment Date:** June 27, 2026  
**Campaign Period:** June 27 - July 11, 2026 (14 days)  
**Voting Day:** July 11, 2026

---

## Cron Job Architecture (5 Jobs Total)

### 1. Statewide Daily Collection
- **Job ID:** `d522b75783f2`
- **Schedule:** Daily at 10:00 UTC
- **Delivery:** Telegram (DAF home channel)
- **Mission:** Collect daily campaign intelligence across all 56 DUN seats
- **Output:** `/home/p62operator/.openclaw/workspace-hoi/intelligence/prn-johor-2026/daily-reports/PRN-JOHOR-DAILY-YYYY-MM-DD.md`
- **Coverage:**
  - SPR official announcements
  - 7 mainstream media sources
  - BN/PH/PN coalition activity
  - Key constituency tracking
  - Risk alerts

### 2. Competitive Seats Deep Dive
- **Job ID:** `eb73758ed17d`
- **Schedule:** Every Wednesday at 14:00 UTC
- **Delivery:** Local (saved to workspace)
- **Mission:** Produce deep-dive analytical reports on 10-12 most competitive seats
- **Output:** `/home/p62operator/.openclaw/workspace-hoi/intelligence/prn-johor-2026/constituency-profiles/[seat]-analysis.md`
- **Priority Seats:**
  1. N47 Kempas (TOSSUP leaning BN)
  2. N27 Layang-Layang (TOSSUP leaning PN)
  3. N07 Bukit Kepong (BN incumbent, Muhyiddin's old seat)
  4. N14 Bukit Naning (BN incumbent, 66.5% Malay)
  5. N41 Johor Lama (PN contesting)
  6. N16 Semerah (PAS stronghold potential)
  7. N50 Stulang (Urban Chinese-majority, PN contesting)
  8. N19 Bukit Pasir (PN contesting)
  9. N35 Mahkota (Urban seat)
  10. N02 [TBD - requires 2022 results check]

### 3. PN Candidate Tracking
- **Job ID:** `1e0eb4aee26e`
- **Schedule:** Daily at 16:00 UTC
- **Delivery:** Telegram (DAF home channel)
- **Mission:** Track all 33 PN candidates (PAS 11, Bersatu 16, MIPP 5, Pejuang 1)
- **Output:** `/home/p62operator/.openclaw/workspace-hoi/intelligence/prn-johor-2026/coalition-analysis/pn-daily-YYYY-MM-DD.md`
- **Coverage:**
  - Candidate activity heatmap
  - Rally/ceramah schedule
  - Messaging analysis
  - Social media metrics
  - Risk alerts

### 4. Kempas PRN Campaign Monitoring (Pre-existing)
- **Job ID:** `bfeaa7c13174`
- **Schedule:** Daily at 18:00 UTC
- **Delivery:** Telegram (DAF home channel)
- **Mission:** N47 Kempas-specific daily campaign tracking
- **Output:** GitHub repository (automated Git sync)
- **Status:** ✅ Operational (6 commits, 13 documents, ~106KB)

### 5. Git Sync Automation (NEW)
- **Job ID:** `d011d02294a8`
- **Schedule:** Daily at 20:00 UTC (after all collection jobs complete)
- **Delivery:** Local (GitHub repository)
- **Mission:** Automatically commit and push all new intelligence reports to GitHub
- **Output:** https://github.com/ahmadfaurani/PRN-Johor-2026-H
- **Coverage:**
  - All daily reports (statewide + PN tracking)
  - Constituency profiles (competitive seats)
  - Coalition analysis reports
  - Candidate profiles (future)
  - Issue tracking (future)
- **Sync Logic:**
  - Check for new/modified `.md` files
  - Commit with descriptive messages (includes file counts, TLP classification, campaign day)
  - Push to `origin/main`
  - Exit silently if no changes (normal on quiet days)
- **Status:** ✅ Deployed (first run: June 27, 2026, 20:00 UTC)

---

## Directory Structure

```
/home/p62operator/.openclaw/workspace-hoi/intelligence/prn-johor-2026/
├── daily-reports/              # Statewide daily collection (Job 1)
│   └── PRN-JOHOR-DAILY-YYYY-MM-DD.md
├── constituency-profiles/      # Competitive seats deep dive (Job 2)
│   ├── n47-kempas-analysis.md
│   ├── n27-layang-layang-analysis.md
│   ├── n07-bukit-kepong-analysis.md
│   └── [other seats]
├── coalition-analysis/         # PN tracking + BN/PH analysis (Job 3)
│   ├── pn-daily-YYYY-MM-DD.md
│   ├── bn-daily-YYYY-MM-DD.md (future expansion)
│   └── ph-daily-YYYY-MM-DD.md (future expansion)
├── candidate-tracking/         # Individual candidate profiles
│   ├── pas-candidates/
│   ├── bersatu-candidates/
│   ├── mipp-candidates/
│   └── pejuang-candidates/
└── issue-tracking/             # Cross-constituency issue monitoring
    ├── cost-of-living.md
    ├── flooding.md
    ├── infrastructure.md
    └── [other issues]
```

---

## Collection Methodology

### Source Hierarchy

**Tier 1 - Official Sources (Highest Confidence):**
- SPR Johor: https://ppn.spr.gov.my/johor/
- SPR HQ: https://www.spr.gov.my/
- Party official announcements (umno.org.my, pkr.org.my, bersatu.org.my, pas.org.my)

**Tier 2 - Mainstream Media (High Confidence):**
- Bernama (national wire service)
- The Star, NST (English broadsheets)
- FMT, Malaysiakini (digital-native)
- Harian Metro, Sinar Harian (Malay dailies)

**Tier 3 - Social Media (Medium Confidence, Requires Verification):**
- Candidate Facebook/Instagram/Twitter
- Party official social media
- Local community groups

**Tier 4 - Alternative Sources (Lower Confidence):**
- Blogs, independent media
- WhatsApp forwards (requires cross-verification)
- Rumor/unconfirmed reports (mark as "⏳ PENDING")

### Quality Gates

All intelligence products must pass:

- ✅ **G1: Source Attribution** (100%) - Every claim has URL + timestamp
- ✅ **G2: TLP Classification** (100%) - All marked TLP:AMBER
- ✅ **G3: Timestamp** (100%) - All claims dated
- ✅ **G4: Confidence Scoring** (100%) - HIGH/MEDIUM/LOW per claim
- ✅ **G5: Cross-Reference** (80%+) - Major claims verified by 2+ sources
- ✅ **G6: Analytical Rigor** (80%+) - No speculation, mark unverified as "⏳ PENDING"
- ✅ **G7: Actionability** (80%+) - Intelligence supports decision-making

---

## Integration with Existing Infrastructure

### DeerFlow Gateway (Port 2026)
- All cron jobs use `web_search()` and `web_extract()` via DeerFlow
- Firecrawl (port 3002) for JavaScript-rendered content
- SearXNG (port 8080) for alternative search queries

### HOI Workspace
- All outputs saved to `/home/p62operator/.openclaw/workspace-hoi/intelligence/prn-johor-2026/`
- Consistent with existing political monitoring pipeline structure
- TLP:AMBER classification enforced

### Telegram Delivery
- Daily reports delivered to DAF home channel (ID: 640442208)
- High-priority alerts (🔴 risk events) sent immediately
- Links to full reports in workspace

### GitHub Repository (Kempas Only)
- N47 Kempas reports automatically synced to public GitHub
- Repository: https://github.com/ahmadfaurani/N47---Kempas.-H
- Automated Git sync via `kempas-git-sync.sh` (18:00 UTC daily)
- **Note:** Other constituencies use local storage only (not auto-synced)

---

## Campaign Timeline

| Date | Event | Automation Status |
|------|-------|-------------------|
| Jun 1 | DUN dissolved | ✅ Historical |
| Jun 27 | Nomination day | ✅ Completed (172 candidates qualified) |
| Jun 27 | Campaign period begins | ✅ Automation deployed |
| Jul 1 | First competitive seats deep dive | ⏳ Scheduled (Job 2) |
| Jul 5 | Early voting | ⏳ Monitoring |
| Jul 11 | **ELECTION DAY** | ⏳ Real-time tracking |

---

## Expected Output Volume

**Daily Reports (Jobs 1, 3, 4):**
- 3 reports/day × 14 days = **42 daily reports**
- Average size: 5-10 KB each
- Total: ~210-420 KB

**Constituency Profiles (Job 2):**
- 10 seats × 2 updates/week × 2 weeks = **40 deep-dive reports**
- Average size: 15-25 KB each
- Total: ~600-1,000 KB

**Total Intelligence Product:** ~810 KB - 1.4 MB over 14-day campaign period

---

## Monitoring & Troubleshooting

### Check Cron Job Status
```bash
hermes cronjob list
```

### Manually Trigger Jobs
```bash
# Statewide collection
hermes cronjob run --job-id=d522b75783f2

# Competitive seats analysis
hermes cronjob run --job-id=eb73758ed17d

# PN tracking
hermes cronjob run --job-id=1e0eb4aee26e

# Kempas monitoring
hermes cronjob run --job-id=bfeaa7c13174
```

### Verify Output
```bash
# Check latest daily report
ls -lt /home/p62operator/.openclaw/workspace-hoi/intelligence/prn-johor-2026/daily-reports/ | head -5

# Check constituency profiles
ls -lt /home/p62operator/.openclaw/workspace-hoi/intelligence/prn-johor-2026/constituency-profiles/ | head -10

# Check PN tracking
ls -lt /home/p62operator/.openclaw/workspace-hoi/intelligence/prn-johor-2026/coalition-analysis/ | head -5
```

### Common Issues

**Job didn't run:**
- Check `hermes cronjob list` for `paused_at` or `last_delivery_error`
- Verify workspace directory is writable
- Check DeerFlow/Firecrawl/SearXNG health

**No changes to commit (Kempas Git sync):**
- Normal on quiet campaign days
- Script exits cleanly (no error)

**Telegram delivery failed:**
- Check Telegram connection status
- Verify home channel ID is correct (640442208)

---

## Expansion Options

### Phase 2 (If Needed)

**BN Candidate Tracking:**
- Mirror Job 3 for BN Johor candidates
- Focus on UMNO/MCA/MIC candidate activity
- Track minister/agency deliveries (Doctrine 4)

**PH Candidate Tracking:**
- Mirror Job 3 for PH Johor candidates
- Focus on PKR/DAP/Amanah candidate activity
- Track ground machinery mobilization (GOTV prep)

**Real-Time Election Day Monitoring:**
- July 11, 2026: Hourly turnout tracking
- Quick count aggregation
- Victory threshold monitoring
- Risk alert system (irregularities, incidents)

**Post-Election Analysis:**
- Results vs. predictions comparison
- Swing analysis
- Demographic breakdown
- Lessons learned report

---

## Reference Documents

- `political-monitoring` skill (this document)
- `references/pkr-war-room-candidate-analytical-report-methodology.md`
- `references/kempas-case-study-2026-06-27.md`
- `references/automated-git-sync-workflow.md`
- `references/electoral-intelligence-methodology.md`

---

**Deployment Status:** ✅ COMPLETE  
**Next Run:** June 28, 2026, 10:00 UTC (Statewide Daily Collection)  
**Campaign Day:** D-13 (countdown to July 11)
