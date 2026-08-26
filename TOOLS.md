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

## 🔧 Exec Discipline — Case Sensitivity (R1 Fix, 2026-08-23)

**Lesson:** Linux filesystems are case-sensitive. Glob patterns must match exact case.

**Rules:**
- Use `find -iname "*pattern*"` (case-insensitive) when casing is uncertain
- Use exact filenames when known
- Never chain `ls` with different globs via `;` — the last failing glob sets the exit code
- For multi-pattern searches: `find <dir> -maxdepth 1 \( -iname "*pattern1*" -o -iname "*pattern2*" \)`

**Example:**
```bash
# ❌ Wrong: lowercase glob on UPPERCASE filenames
ls .../governance/*cognitive* 2>/dev/null  # exit 2, no match

# ✅ Correct: case-insensitive find
find .../governance/ -maxdepth 1 -iname "*cognitive*"  # matches COGNITIVEOS-PRIME-DOCTRINE.md
```

## 🔧 Incomplete Turn Protocol (R4 Fix, 2026-08-23)

When "Agent couldn't generate a response" appears:

1. Check `journalctl --user -u openclaw-gateway` for the specific `runId`
2. Verify: main session or isolated session?
3. Check memory pressure level at that timestamp
4. Check concurrent sessions/cron jobs active
5. Note `stopReason` and `tools` count for pattern tracking
6. **Never** tell the user "harmless" without completing steps 1–5

**ADEP-001 §7:** Dismissing an error without investigation is a violation. "I don't know yet, let me check" is valid. "Harmless" requires evidence.

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
| **VALIDATE** | CVS Master Framework, Evidence Register, 03-VERIFICATION/ | Is the ember still warm? Claims verified, tagged, sourced? |
| **HOLD** | memory files, MEMORY.md, daily notes, git | Store in memory. Maintain for later. File it properly. |
| **SHARE** | Telegram replies, sessions_send, file delivery | Deliver to user. Pass the warmth. Make it usable. |
| **REST** | Heartbeat, dreaming, session end | The ember banks for the night. The cycle pauses. |

**Feeding tools:** web_search, DeerFlow, OSINT (Mr.Holmes), web_fetch — these gather new fuel. A starved ember dies.

**Sheltering tools:** CVS Master Framework (`03-VERIFICATION/`), Evidence Register, git, memory harness — these protect from forgetting and distortion. An exposed ember dies in wind.

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

**Sole CVS Instrument:** `03-VERIFICATION/CVS-FRAMEWORK.md` (Master Framework)

**Retired (2026-08-17):** `tools/truth-validator/CVS-MANDATE.md` (DUN Profiling CVS) — archived. No longer authoritative.

**Mandatory for:** Any output containing numerical claims, named entities, historical data, or analytical assessments.

### CVS Master Framework (T1–T6, L1–L5, 5-Criteria Scoring)

All claims must be:
1. **Tiered** — T1 `[CONFIRMED]` → T2 `[SOURCE-BACKED]` → T3 `[ASSESSMENT]` → T4 `[ASSUMPTION]` → T5 `[DISPUTED]` → T6 `[EXCLUDED]`
2. **Source-levelled** — L1 (Official) → L2 (Internal validated) → L3 (HUMINT) → L4 (OSINT) → L5 (AI/Secondary)
3. **Scored** — 5 criteria (Authority, Traceability, Recency, Consistency, Completeness), 0–2 each, total 0–10
4. **Rule 6** — AI output capped at T2, max score 7. Human review required for T1 upgrade.
5. **Registered** — All claims logged in `03-VERIFICATION/CVS-EVIDENCE-REGISTER.csv` (20-field schema)
6. **Workstream-adapted** — Domain rules per `03-VERIFICATION/CVS-ADAPTER-GUIDE.md`

### External Verification Sources

**ElectionData.MY API** (✅ Integrated 2026-06-29)
- **Coverage:** Malaysian elections 1954–present
- **Access:** Free API key (https://electiondata.my/console)
- **Use Case:** Cross-reference historical results, candidate names, vote counts, turnout
- **Config:** `export ELECTIONDATA_API_KEY=your_key` or `./tools/truth-validator/electiondata-verify.sh --api-key <key>`
- **Docs:** `tools/truth-validator/ELECTIONDATA-INTEGRATION.md`

### Pre-Output Checklist

```
[ ] All claims tiered (T1–T6) and labelled?
[ ] All source levels cited (L1–L5)?
[ ] 5-criteria confidence score recorded for each claim?
[ ] Rule 6 applied — no AI-claimed T1, no score >7?
[ ] Claims registered in CVS-EVIDENCE-REGISTER.csv?
[ ] Workstream adapter rules followed?
```

### Reference Documents

- **Master Framework:** `03-VERIFICATION/CVS-FRAMEWORK.md`
- **Source Register:** `03-VERIFICATION/CVS-SOURCE-REGISTER.md`
- **Adapter Guide:** `03-VERIFICATION/CVS-ADAPTER-GUIDE.md`
- **Evidence Register:** `03-VERIFICATION/CVS-EVIDENCE-REGISTER.csv`

### Legacy Tools (Retired 2026-08-17)

The following `tools/truth-validator/` scripts are **retired** for CVS validation purposes. They may still be used as utility scripts for election-specific tasks (name verification, number extraction) but are NOT CVS validation instruments:

- `validate.sh` — was DUN-profiling validator, not Master Framework validator
- `CVS-MANDATE.md` — archived
- `CVS-OPERATIONAL-GUIDE.md` — archived
- `CVS-SCOPE-DUN-PROFILING.md` — archived
- `dreaming-cvs-integration.sh` — archived

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
# Validate OSINT findings before briefing (CVS Master Framework)
# Note: tools/truth-validator/validate.sh retired 2026-08-17 (DUN Profiling CVS archived)
# Use 03-VERIFICATION/CVS-FRAMEWORK.md for claim validation
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

## 🔧 Memory Threshold Patch — Reapply After OpenClaw Updates

**Date:** Aug 26, 2026
**Reason:** Default RSS warning threshold was 1.5 GiB — too low for 188 GB server, caused 126 warnings/day noise
**Patched to:** Warning 6 GB, Critical 8 GB

### What to Patch

**File:** `~/.npm-global/lib/node_modules/openclaw/dist/diagnostic-DhwkYT4X.js`

**Find (line ~138):**
```js
const DEFAULT_RSS_WARNING_BYTES = 1536 * MB;
const DEFAULT_RSS_CRITICAL_BYTES = 3072 * MB;
```

**Replace with:**
```js
const DEFAULT_RSS_WARNING_BYTES = 6144 * MB;
const DEFAULT_RSS_CRITICAL_BYTES = 8192 * MB;
```

### Reapply After Update

```bash
# After npm update openclaw, reapply the patch:
sed -i 's/const DEFAULT_RSS_WARNING_BYTES = 1536 \* MB;/const DEFAULT_RSS_WARNING_BYTES = 6144 * MB;/' ~/.npm-global/lib/node_modules/openclaw/dist/diagnostic-DhwkYT4X.js
sed -i 's/const DEFAULT_RSS_CRITICAL_BYTES = 3072 \* MB;/const DEFAULT_RSS_CRITICAL_BYTES = 8192 * MB;/' ~/.npm-global/lib/node_modules/openclaw/dist/diagnostic-DhwkYT4X.js

# Verify:
grep -n 'DEFAULT_RSS_WARNING_BYTES\|DEFAULT_RSS_CRITICAL_BYTES' ~/.npm-global/lib/node_modules/openclaw/dist/diagnostic-DhwkYT4X.js | head -2

# Restart gateway:
openclaw gateway restart
```

### Validation

After restart, confirm 0 memory pressure warnings:
```bash
journalctl --user -u openclaw-gateway --since "<restart time>" --no-pager 2>&1 | grep -c "memory pressure"
# Should return 0
```

### Notes

- This is a source patch in the OpenClaw dist directory — NOT a config file. It WILL be overwritten on `npm update openclaw`.
- The `resolveThresholds()` function accepts overrides but the diagnostics config schema doesn't expose `rssWarningBytes` as a user-configurable field.
- No env var override exists (`OPENCLAW_*_THRESHOLD` not implemented).
- If OpenClaw adds a config-based threshold in a future version, switch to that instead of patching source.
- File name may change between versions (`diagnostic-DhwkYT4X.js` is the hash-suffixed name for 2026.7.1-2). Use `grep -rl 'DEFAULT_RSS_WARNING_BYTES' ~/.npm-global/lib/node_modules/openclaw/dist/` to find the correct file if the name changes.

---

## Related

- [Agent workspace](/concepts/agent-workspace)
- [Git-to-Drive Docs](tools/git-to-drive/README.md)
- [DeerFlow](tools/deer-flow/) - Automated news collection
- [CVS Master Framework](03-VERIFICATION/CVS-FRAMEWORK.md) - Claim verification (sole CVS instrument)
- [Truth Validator (retired)](tools/truth-validator/) - DUN-profiling scripts, archived 2026-08-17
