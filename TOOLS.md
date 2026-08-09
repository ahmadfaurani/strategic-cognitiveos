# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

Add whatever helps you do your job. This is your cheat sheet.

---

## 🔥 The Ember Cycle — Tool-to-Phase Mapping

Every tool serves one phase of the Ember Cycle:

| Phase | Tools | Purpose |
|-------|-------|--------|
| **RECEIVE** | Telegram, Discord, web_fetch, exec (input) | Knowledge comes in. User request, data collection. |
| **TEND** | read, edit, write, exec, memory_get | Process it. Analyze. Research. Do the work. |
| **VALIDATE** | truth-validator, CVS, validate.sh | Is the ember still warm? Claims verified, tagged, sourced? |
| **HOLD** | memory files, MEMORY.md, daily notes, git | Store in memory. Maintain for later. File it properly. |
| **SHARE** | Telegram replies, sessions_send, file delivery | Deliver to user. Pass the warmth. Make it usable. |
| **REST** | Heartbeat, dreaming, session end | The ember banks for the night. The cycle pauses. |

**Feeding tools:** web_search, DeerFlow, OSINT (Mr.Holmes), web_fetch — these gather new fuel. A starved ember dies.

**Sheltering tools:** CVS, validate.sh, git, memory harness — these protect from forgetting and distortion. An exposed ember dies in wind.

---

## 📄 Git-to-Drive (PDF Automation)

**Location:** `tools/git-to-drive/`

**Purpose:** Generate professional PDFs from Git repos → Auto-upload to Google Drive

### Quick Commands

```bash
# Setup (one-time)
cd tools/git-to-drive
./setup.sh
rclone config

# Generate & upload PDF
./git-to-drive.sh https://github.com/user/repo
./git-to-drive.sh https://github.com/user/repo my-documentation
./git-to-drive.sh ./local-repo report-2026 "/Shared/Docs"
```

### Configuration

- **rclone remote:** `drive`
- **Default Drive folder:** `/Git-PDFs`
- **Template:** Eisvogel (LaTeX)
- **Syntax highlighting:** Monokai

### Credentials

- **Config file:** `~/.config/rclone/rclone.conf`
- **Service account:** `~/.config/rclone/gdrive-service-account.json`
- **Setup guide:** `tools/git-to-drive/CREDENTIALS_SETUP.md`

### GitHub Actions

For CI/CD automation, use workflow in `tools/git-to-drive/github-workflow.yml`

Required secrets:
- `GDRIVE_SERVICE_ACCOUNT` — Service account JSON
- `GDRIVE_FOLDER_ID` — Target Drive folder ID

---

## 🔍 Truth Validation Protocol

**Purpose:** Prevent hallucination, factual drift, and conflation of inference with fact in long-form outputs.

**Mandatory for:** Any output containing numerical claims, named entities, historical data, or analytical assessments.

### External Verification Sources

**ElectionData.MY API** (✅ Integrated 2026-06-29)
- **Coverage:** Malaysian elections 1954–present
- **Access:** Free API key (https://electiondata.my/console)
- **Use Case:** Cross-reference historical results, candidate names, vote counts, turnout
- **Config:** `export ELECTIONDATA_API_KEY=your_key` or `./tools/truth-validator/electiondata-verify.sh --api-key <key>`
- **Docs:** `tools/truth-validator/ELECTIONDATA-INTEGRATION.md`

### Claim Tiers

#### Tier 1: Factual Claims (Must verify before output)
- Numbers: vote counts, percentages, dates, margins, electorate sizes
- Names: candidates, positions, titles, party affiliations
- Locations: constituencies, polling districts, geographic references
- Historical results: past election outcomes, majorities, turnout figures

**Validation method:** Cross-reference against source file + line number. If source is external (news, official data), fetch and cite URL.

**Output requirement:** Every Tier 1 claim must include `Source: <file#line>` or `Source: <URL>`

---

#### Tier 2: Analytical Claims (Must label confidence)
- Vote split calculations
- Turnout sensitivity analysis
- Demographic inferences
- Strategic assessments
- Mathematical derivations

**Validation method:** Show the math explicitly. Tag confidence:
- `[HIGH]` — Derived from verified Tier 1 data, straightforward calculation
- `[MEDIUM]` — Reasonable inference from multiple data points
- `[LOW]` — Speculative, depends on unverified assumptions

**Output requirement:** Confidence tag + brief justification

---

#### Tier 3: Predictive/Speculative Claims (Must flag as such)
- Future scenarios
- Emerging narratives
- Risk assessments
- "What-if" modelling

**Validation method:** Explicitly mark as `SPECULATION:` or `SCENARIO:` — never present as fact.

**Output requirement:** Clear demarcation + underlying assumptions stated

---

### Pre-Output Checklist

Before any long-form analysis leaves the queue:

```
[ ] All Tier 1 numbers verified against source?
[ ] All names double-checked (spelling, position, party)?
[ ] All citations include file#line or URL?
[ ] Confidence tags applied to Tier 2 claims?
[ ] Tier 3 speculation clearly demarcated?
[ ] Any contradictory evidence considered?
[ ] Math shown explicitly for analytical claims?
```

---

### Structured Output Format

For complex analysis, use tabular format:

```markdown
## Claim | Source | Confidence | Notes
--------|--------|--------------|------
"BN won 2022 by 4,041 votes" | MEMORY.md#L142 | HIGH | Verified from SPR data
"PN could exceed 2022 base" | Inference | MEDIUM | Depends on Malay sentiment shift
"Turnout >80% favors PH" | Historical pattern | MEDIUM | Based on 2018 vs 2022 delta
```

---

### Automated Validation Tools

**Location:** `tools/truth-validator/`

```bash
# Validate claims against source files
./tools/truth-validator/validate.sh memory/n17-semerah-war-room-brief-20260627.md

# Extract and verify all numerical claims
./tools/truth-validator/extract-numbers.sh < input.md

# Cross-reference candidate names with official registry
./tools/truth-validator/verify-names.sh < input.md
```

**Integration:** Run validator before any political brief is delivered.

---

## 🔍 Mr.Holmes OSINT Tool

**Location:** `tools/Mr.Holmes/`  
**Status:** ✅ Installed & Configured (2026-07-09)  
**Purpose:** Open Source Intelligence gathering for usernames, domains, phone numbers

### Quick Commands

```bash
# Interactive mode (full menu)
cd tools/Mr.Holmes
source .venv/bin/activate
export TERM=xterm-256color
python3 MrHolmes.py

# Programmatic access (Python wrapper)
python3 -c "
from tools.Mr.Holmes.mrholmes_wrapper import MrHolmesWrapper
mh = MrHolmesWrapper()
print(mh.search_phone('+60123456789'))
print(mh.generate_dorks('target_name'))
"

# View existing reports
ls -la tools/Mr.Holmes/GUI/Reports/
```

### Capabilities

- **Username OSINT**: Search 100+ platforms (Instagram, Twitter, TikTok, GitHub, etc.)
- **Phone Number OSINT**: Validation, carrier lookup, geographic inference
- **Domain/IP OSINT**: WhoIS lookup, DNS enumeration (requires API key)
- **Google Dorks**: Automated dork generation with date/file-type filters
- **Email OSINT**: Service association, breach checking
- **Port Scanning**: Basic TCP port enumeration
- **Report Generation**: PDF export, QR code transfer

### Integration Points

**With DeerFlow:**
```python
# After DeerFlow identifies targets
from tools.Mr.Holmes.mrholmes_wrapper import MrHolmesWrapper
mh = MrHolmesWrapper()
results = mh.search_username('target')
# Save to reports/ for archival
```

**With Truth Validator:**
```bash
# Validate OSINT findings before briefing
./tools/truth-validator/validate.sh tools/Mr.Holmes/reports/investigation.md
```

**With Memory System:**
```bash
# Archive completed investigations
mv tools/Mr.Holmes/GUI/Reports/Usernames/TARGET/ \
   memory/osint-reports/TARGET-$(date +%Y%m%d)/
```

### Configuration

**WhoIS API** (optional):
```ini
# Edit: tools/Mr.Holmes/Configuration/Configuration.ini
[WhoIs]
api_key = YOUR_API_KEY_HERE
```
Get key: https://whois.whoisxmlapi.com

**Theme**:
```json
// Edit: tools/Mr.Holmes/GUI/Theme/Mode.json
{"Color": {"Background": "Dark"}}
```

### Output Locations

| Type | Path |
|------|------|
| Username Reports | `tools/Mr.Holmes/GUI/Reports/Usernames/<username>/` |
| Domain Reports | `tools/Mr.Holmes/GUI/Reports/Websites/<domain>/` |
| Phone Reports | `tools/Mr.Holmes/GUI/Reports/Phonenumbers/<phone>/` |
| Custom Reports | `tools/Mr.Holmes/reports/` |
| Logs | `tools/Mr.Holmes/Logs/` |

### Documentation

- `tools/Mr.Holmes/QUICKSTART.md` - Quick reference
- `tools/Mr.Holmes/INTEGRATION.md` - Full integration guide
- `tools/Mr.Holmes/mrholmes_wrapper.py` - Python API

### Limitations

- ⚠️ Not 100% accurate - verify with multiple sources
- ⚠️ Educational/research use only
- ⚠️ Rate limiting may occur on some platforms
- ⚠️ PDF export requires `wkhtmltopdf` (not installed)
- ⚠️ Proxy/Tor support available but not pre-configured

---

## 🕷️ Crawl4AI Integration (2026-07-19)

**Location:** `tools/deer-flow/unified_scraper.py`
**Status:** ✅ Integrated & Operational
**Purpose:** Replace Firecrawl-only scraping with Crawl4AI (primary) → Firecrawl (fallback) adapter

### Architecture

- **unified_scraper.py** provides `scrape_url()` — a Firecrawl-compatible adapter
- Crawl4AI (Apache 2.0, Playwright-based) handles 23/25 sources at 2-12s each
- Firecrawl fallback handles anti-bot-blocked sites (Bernama, Sabah News) at ~38s
- Response shape: `{success, data: {markdown, metadata: {engine: "crawl4ai"|"firecrawl"}}}`
- Existing scripts need minimal changes — just swap `requests.post(FIRECRAWL_URL, ...)` → `scrape_url(url=...)`

### Key Functions

| Function | Type | Use |
|----------|------|-----|
| `scrape_url(url, timeout, max_retries)` | Sync | Main entry point — uses asyncio.run() internally |
| `scrape_url_async(url, ...)` | Async | For async pipelines |
| `scrape_batch(urls, max_workers)` | Sync | Parallel batch scraping |
| `scrape_firecrawl_compat(url)` | Sync | Firecrawl-shaped response |
| `cleanup()` | Async | No-op (crawler created/closed per call) |

### Patched Scripts (9 total)

| Script | Status |
|--------|--------|
| `collect_political_news_25sources_OPERATIONAL.py` | ✅ Patched & tested |
| `collector.py` | ✅ Patched & tested |
| `collect_political_news_7sources.py` | ✅ Patched |
| `collect_political_news_25sources.py` | ✅ Patched |
| `generate_daily_brief.py` | ✅ Patched |
| `run_collection.py` | ✅ Patched |
| `run_collection_parallel.py` | ✅ Patched |
| `run_collection_quick.py` | ✅ Patched |
| `e2e-test.py` | ✅ Patched |

### Performance (25-Source Benchmark, 2026-07-19)

| Metric | Pre-Crawl4AI (Firecrawl) | Post-Crawl4AI |
|--------|--------------------------|---------------|
| Success Rate | ~80-90% | 100% (25/25) |
| Total Time | ~15-20 min | ~5 min |
| Avg per Source | ~40-60s | ~3-8s (Crawl4AI) |
| Content | 656K chars | 656,456 chars |
| Headlines | ~400 | 426 |
| Political Headlines | ~15-20 | 24 |

### Anti-Bot Handling

- **Crawl4AI stealth mode:** `enable_stealth=True`, `user_agent_mode="random"`
- **Works on:** 23/25 sources (all except Bernama BM, Sabah News)
- **Fallback:** Firecrawl at `http://localhost:3002/v2/scrape` handles blocked sites automatically

### Crawl4AI v0.9.2 API Notes

- `AsyncWebCrawler(config=BrowserConfig(...))` — not `browser_config=`
- `await crawler.start()` — not `__aenter__()`
- `CrawlerRunConfig` has no `only_content` param — use `remove_overlay_elements=True` + `only_text=False`
- Create fresh crawler per `asyncio.run()` call — shared instances break across event loops

### Quick Commands

```bash
# Activate venv
source /home/p62operator/tools/deer-flow/.venv/bin/activate

# Test single URL
python3 -c "
import sys; sys.path.insert(0, '.')
from unified_scraper import scrape_url
r = scrape_url('https://www.nst.com.my/', timeout=30)
print(r['data']['metadata']['engine'], len(r['data']['markdown']), 'chars')
"

# Run full 25-source collection
python3 collect_political_news_25sources_OPERATIONAL.py

# Benchmark
python3 benchmark_scraper.py
```

---

## Related

- [Agent workspace](/concepts/agent-workspace)
- [Git-to-Drive Docs](tools/git-to-drive/README.md)
- [DeerFlow](tools/deer-flow/) - Automated news collection
- [Truth Validator](tools/truth-validator/) - Claim verification
