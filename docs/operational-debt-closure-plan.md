# Operational Debt Closure Plan

**Classification:** TLP:AMBER — Internal Operational  
**Date:** 2026-08-15  
**Authority:** DAF  
**Architect:** Ember (OpenClaw)  
**Status:** PROPOSED — Awaiting DAF Approval

---

## Architecture: Three-Tier Operating Model

```
┌─────────────────────────────────────────────────────────┐
│  TIER 1: OPENCLAW (Director)                            │
│  Oversight · Health Monitoring · Cross-Workstream      │
│  Alerting · Memory · Wiki · CVS Governance              │
├─────────────────────────────────────────────────────────┤
│  TIER 2: HERMES (Operator)                              │
│  Collection · Analysis · Briefs · Entity Extraction     │
│  Sentiment · Git Sync · Campaign Trail · CVS Validation │
├─────────────────────────────────────────────────────────┤
│  TIER 3: TOOLING STACK (Infrastructure)                  │
│  Crawl4AI · Firecrawl · SearXNG · DeerFlow · Browser    │
│  Ollama · MCP Servers · Signal Registry                 │
└─────────────────────────────────────────────────────────┘
```

**Principle:** OpenClaw directs. Hermes operates. The stack serves both.

---

## Phase 1: Critical Fixes (Day 1)

### 1.1 Fix SearXNG Search for Hermes

**Problem:** Hermes prompts contain stale override: "web_search is BROKEN — use web_extract instead." SearXNG is actually working (35 results on test query). Hermes is configured to use Firecrawl for `search_backend`, not SearXNG. Firecrawl search works too (5 results on test). The "broken" status is from an old incident that was never cleared from prompts.

**Action:**
1. Update Hermes config `web.search_backend` to `searxng` (localhost:8080) for broader source discovery
2. Keep `web.extract_backend` as `firecrawl` (localhost:3002) for content extraction
3. Remove the "SEARCH BACKEND OVERRIDE" warning from all 15 active Hermes job prompts
4. Add SearXNG as MCP server in Hermes config for search capability

**Hermes Config Change:**
```yaml
web:
  backend: searxng          # was: firecrawl
  search_backend: searxng   # was: firecrawl  
  extract_backend: firecrawl
  use_gateway: false
```

**SearXNG MCP Server (new):**
```yaml
mcp_servers:
  firecrawl:
    command: npx
    args: [-y, firecrawl-mcp]
    enabled: true
    env:
      FIRECRAWL_BASE_URL: http://localhost:3002
  searxng:
    command: npx
    args: [-y, searxng-mcp]
    enabled: true
    env:
      SEARXNG_URL: http://127.0.0.1:8080
```

**Prompt Cleanup:** Remove the "⚠️ SEARCH BACKEND OVERRIDE" block from all active Hermes job prompts. Replace with:
```
## Search Protocol
- Use web_search for topic discovery (SearXNG — 35+ Malaysian news sources indexed)
- Use web_extract for full content extraction (Firecrawl — localhost:3002)
- For each relevant article: web_extract the direct URL to get full content
- Batch up to 5 URLs per web_extract call
```

**Owner:** Ember  
**Effort:** 2 hours  
**Risk:** Low — SearXNG already tested and working

---

### 1.2 Integrate Crawl4AI as Hermes Collection Engine

**Problem:** System crontab runs `collect_political_news_25sources_OPERATIONAL.py` via Crawl4AI 4x/day, but output goes to `workspace-hoi/intelligence/raw/` — nobody reads it. Hermes jobs do their own URL-by-URL extraction via Firecrawl, which is slower and covers fewer sources.

**Action:** Bridge the two systems. Crawl4AI collection becomes input to Hermes entity extraction and sentiment pipelines.

**Architecture:**
```
System Crontab (08:00, 12:00, 16:00, 23:00 UTC)
  ↓
Crawl4AI 25-source collection → workspace-hoi/intelligence/raw/
  ↓
Hermes CJ-MLK-07 Entity Extraction (06:00 MYT = 22:00 UTC)
  ↓ reads from workspace-hoi/intelligence/raw/ INSTEAD OF workspace-mlk/raw-scrapes/
  ↓
Hermes CJ-MLK-08 Sentiment Analysis (07:00 MYT = 23:00 UTC)
  ↓ processes entity extraction output
  ↓
Hermes CJ-MLK-05 Daily Brief (04:00 MYT = 20:00 UTC... wait, currently 04:00 UTC)
  ↓ incorporates Crawl4AI broad collection + Hermes targeted extraction
```

**Script Changes:**

1. **`mlk-entity-extraction.sh`** — change `RAW_DIR` to also read from Crawl4AI output:
```bash
# New: also scan Crawl4AI collection output
CRAWL4AI_RAW="/home/p62operator/.openclaw/workspace-hoi/intelligence/raw"
# Find today's Crawl4AI files
CRAWL4AI_TODAY=$(find "$CRAWL4AI_RAW" -name "$(date -u +%Y-%m-%dT)*_political_collection_25sources_OPERATIONAL.json" -type f 2>/dev/null | head -1)
if [ -n "$CRAWL4AI_TODAY" ]; then
    # Extract headlines from JSON and process as additional raw input
    python3 -c "
import json
with open('$CRAWL4AI_TODAY') as f:
    data = json.load(f)
for source in data.get('sources', []):
    for article in source.get('articles', []):
        print(f'## {article.get(\"title\",\"\")}\n{article.get(\"content\",\"\")}\n')
" > "${RAW_DIR}/crawl4ai-collection-${TODAY}.md"
fi
```

2. **`collect_political_news_25sources_OPERATIONAL.py`** — also write a copy to `workspace-mlk/04-DATA-AND-SOURCES/raw-scrapes/` so Hermes entity extraction picks it up natively.

**Owner:** Ember  
**Effort:** 3 hours  
**Risk:** Medium — requires script modification + testing

---

### 1.3 Install Ollama for Memory Search

**Problem:** OpenClaw config has `memorySearch.provider: "ollama"` but Ollama is not installed. Memory search is broken — affects every OpenClaw session.

**Action:**
```bash
curl -fsSL https://ollama.com/install.sh | sh
ollama pull nomic-embed-text  # 274MB, embedding model for semantic search
# Verify service
systemctl status ollama
curl -s http://127.0.0.1:11434/api/version
```

**Config Verification:**
- OpenClaw config already points to `ollama` — no config change needed
- Memory search will auto-recover once Ollama is running
- Verify with `openclaw memory search "test query"` after install

**Owner:** Ember (requires elevated)  
**Effort:** 15 minutes  
**Risk:** Low

---

### 1.4 Fix HEARTBEAT.md — Replace Fiction with Reality

**Problem:** HEARTBEAT.md references 7 non-existent `openclaw skill run` commands. It describes an aspirational pipeline that was never built.

**Action:** Rewrite HEARTBEAT.md to reflect the actual three-tier architecture:

```markdown
# HEARTBEAT.md — Operational Reality

## OpenClaw (Director) Cron
- Memory Dreaming Promotion: 03:00 UTC daily (active)

## Hermes (Operator) Cron — 15 Active Jobs
- PRN Melaka POI: 6 jobs (collection every 12h, brief daily 04:00 UTC, entity/sentiment daily, campaign trail every 6h, weekly deep-dive)
- Tabung Haji RCI: 3 jobs (MP watch every 2h, parliamentary watch every 3h, git sync daily)
- PRN NS Post-Mortem: 1 job (git sync daily)
- CVS Weekly Validation: 1 job (Monday 01:00 UTC)

## System Crontab (Collection)
- Crawl4AI 25-source: 08:00, 12:00, 16:00, 23:00 UTC → workspace-hoi/intelligence/raw/

## OpenClaw Director Tasks (New — Phase 2)
- Pipeline Health Check: every 6h (verify Hermes output + Crawl4AI output exist)
- Stale Data Alert: if no collection output in 24h, notify DAF via Telegram
- CVS Audit: weekly review of evidence register quality
```

**Owner:** Ember  
**Effort:** 30 minutes  
**Risk:** None

---

## Phase 2: OpenClaw as Director (Day 2-3)

### 2.1 OpenClaw Cron Jobs for Oversight

**Problem:** 7 weeks of silent cron failure went unnoticed. No health checks, no alerting, no cross-workstream visibility. OpenClaw should be the Director — monitoring the Operator (Hermes) and Infrastructure (crontab).

**Action:** Add 4 OpenClaw cron jobs:

#### Job 1: Pipeline Health Monitor (every 6h)
```
Schedule: 0 */6 * * *
Task: Check for:
  1. Crawl4AI output in last 12h (workspace-hoi/intelligence/raw/)
  2. Hermes output in last 12h (.hermes/cron/output/)
  3. Git commits in last 24h (workspace-mlk, workspace-th-rci, workspace-ns)
  4. CVS evidence register growth (workspace-mlk/03-VERIFICATION/CVS-EVIDENCE-REGISTER.csv)
If ANY check fails → alert DAF via Telegram with specific failure
If ALL pass → NO_REPLY (silent success)
```

#### Job 2: Stale Data Alert (daily 09:00 UTC / 17:00 MYT)
```
Schedule: 0 9 * * *
Task: Check:
  1. Last Crawl4AI collection timestamp — alert if >24h
  2. Last Hermes brief date — alert if >36h
  3. Last git commit in any workspace — alert if >24h
  4. Signal registry last update — alert if >7 days (or note it's retired)
Deliver: Summary card to DAF via Telegram
```

#### Job 3: CVS Weekly Audit (Sunday 02:00 UTC)
```
Schedule: 0 2 * * 0
Task: Review:
  1. CVS evidence register — count claims, check tier distribution, flag T6 entries
  2. Cross-reference: do Hermes brief claims appear in evidence register?
  3. Source diversity: how many unique sources cited this week?
  4. Confidence score trends — any declining?
Deliver: Weekly CVS Audit Report to DAF via Telegram
```

#### Job 4: Hermes Fleet Review (1st of month, 09:00 UTC)
```
Schedule: 0 9 1 * *
Task: Review:
  1. Hermes job count (enabled/disabled/total)
  2. Execution success rate per job
  3. Model cost analysis (Qwen 397B vs GLM-5.2 usage)
  4. Job output volume trends
  5. Recommend: re-enable, disable, re-schedule, or re-model jobs
Deliver: Monthly Fleet Report to DAF via Telegram
```

**Owner:** Ember  
**Effort:** 4 hours  
**Risk:** Low — OpenClaw cron is already functional (Memory Dreaming proves it)

---

### 2.2 Model Tiering for Hermes Jobs

**Problem:** All 9 Hermes analytical jobs use Qwen 397B. Collection jobs (entity extraction, sentiment, git sync) use default (GLM-5.2) or no model (script-only). But the 3 collection-type jobs that DO use models (CJ-MLK-01/02/03) run every 12h for broad collection — Qwen 397B is overkill for URL extraction.

**Available Models on Aras Endpoint:**
| Model | Strength | Cost Tier | Best For |
|-------|----------|-----------|----------|
| Qwen3.5-397B-A17B | Deep reasoning, analysis | High | Briefs, analysis, deep-dive |
| GLM-5.2 | Fast, capable | Medium | Collection, entity extraction, general |
| Qwen3.5-27B | Lightweight, fast | Low | Simple extraction, sentiment, git messages |
| Kimi-K2.6 | Strong reasoning | Medium-High | Alternative analysis |
| Kimi-K2.5 | Capable | Medium | Alternative collection |

**Proposed Tiering:**

| Job | Current Model | Proposed Model | Rationale |
|-----|--------------|----------------|-----------|
| CJ-MLK-01 Executive Leadership | Qwen 397B | GLM-5.2 | Collection — URL extraction doesn't need 397B |
| CJ-MLK-02 Defence & Parliament | Qwen 397B | GLM-5.2 | Collection — same |
| CJ-MLK-03 Coalition Dynamics | Qwen 397B | GLM-5.2 | Collection — same |
| CJ-MLK-04 Grassroots & Secondary | Qwen 397B | GLM-5.2 | Collection — same |
| CJ-MLK-05 Daily Brief | Qwen 397B | Qwen 397B | ✅ Keep — synthesis requires deep reasoning |
| CJ-MLK-09 Campaign Trail | Qwen 397B | GLM-5.2 | Collection — URL extraction + summarization |
| CJ-MLK-10 Weekly Deep-Dive | Qwen 397B | Qwen 397B | ✅ Keep — deep analysis |
| CJ-TH-01 Parliamentary Watch | Qwen 397B | GLM-5.2 | Collection — MP statement tracking |
| CJ-TH-05 High-Risk MP Watch | Qwen 397B | GLM-5.2 | Collection — every 2h, high frequency |

**Result:** 4 jobs on Qwen 397B (brief, deep-dive) → 5 jobs on GLM-5.2 (collection). Estimated 60% reduction in high-cost model usage.

**Owner:** Ember  
**Effort:** 1 hour (update Hermes job configs)  
**Risk:** Low — GLM-5.2 is the Hermes default model, proven capable for collection tasks

---

### 2.3 Hermes Job Prompt Cleanup

**Problem:** Job prompts contain stale instructions:
- "SEARCH BACKEND OVERRIDE — USE web_extract INSTEAD OF web_search" (search works now)
- References to deprecated "COLLECTION SEARCH QUERIES" sections
- Inconsistent CVS validation instructions across jobs

**Action:** Standardize all 15 active job prompts with:
1. Updated search protocol (SearXNG + Firecrawl both available)
2. Consistent CVS validation block (reference the CVS skill, don't inline 500 lines of CVS doc)
3. Standardized output format (claim blocks, evidence register entries, file paths)
4. Remove deprecated sections

**Owner:** Ember  
**Effort:** 3 hours  
**Risk:** Medium — requires careful prompt engineering, test each job after update

---

## Phase 3: Stack Integration (Day 4-5)

### 3.1 Activate Signal Registry as Hermes Output Target

**Problem:** Signal registry has 3 test entries from June, stale 49 days. HEARTBEAT.md references non-existent signal pipeline tools.

**Action:** Retire the aspirational signal registry concept. Replace with what Hermes actually produces:

1. **Delete** `memory/signals/registry-index.json` and the 3 test signal files
2. **Remove** all signal-related references from HEARTBEAT.md and AGENTS.md
3. **Acknowledge** that Hermes's CVS Evidence Register (`workspace-mlk/03-VERIFICATION/CVS-EVIDENCE-REGISTER.csv`) IS the operational signal registry — 210 claims with full validation metadata
4. **Add** a cross-reference in AGENTS.md: "Signal Registry → see CVS Evidence Register in each workspace"

**Alternative (if DAF wants to keep the concept):**
1. Create a lightweight signal extractor script that reads Hermes daily briefs and extracts signals into the registry format
2. Run as a Hermes cron job after the daily brief (05:00 UTC)
3. Signals = key claims from briefs, scored by CVS tier and confidence

**Owner:** Ember  
**Effort:** 2 hours (retire) or 6 hours (activate)  
**Risk:** Low

---

### 3.2 Integrate Truth Validator with Hermes CVS

**Problem:** Two parallel validation systems exist:
- `tools/truth-validator/validate.sh` — referenced in AGENTS.md, TOOLS.md, HEARTBEAT.md but never called
- Hermes CVS skill — embedded in job prompts, actively producing 210+ validated claims

**Action:** Unify. Hermes CVS is the operational system. `validate.sh` becomes the OpenClaw Director's audit tool.

1. **Update `validate.sh`** to accept Hermes CVS Evidence Register as input:
   ```bash
   ./validate.sh --evidence-register workspace-mlk/03-VERIFICATION/CVS-EVIDENCE-REGISTER.csv
   ```
2. **Add OpenClaw cron job** (CVS Weekly Audit — already in Phase 2) that runs `validate.sh` against all workspace evidence registers
3. **Remove** missing references from AGENTS.md/TOOLS.md:
   - `CVS-MANDATE.md` — doesn't exist, remove reference
   - `ELECTIONDATA-INTEGRATION.md` — doesn't exist, remove reference  
   - `electiondata-verify.sh` — doesn't exist, remove reference
4. **Update AGENTS.md** CVS section to point to the actual framework: `workspace/03-VERIFICATION/CVS-FRAMEWORK.md` (which exists)

**Owner:** Ember  
**Effort:** 3 hours  
**Risk:** Low

---

### 3.3 Fix Browser Gateway & Configure MCP

**Problem:** 
- OpenClaw browser tool broken (gateway pairing scope error)
- MCP registry empty (`openclaw mcp list → {}`)
- Browser could be used by Hermes for visual verification of news sites

**Action:**

1. **Update OpenClaw** to 2026.7.1-2 (may fix gateway pairing):
   ```bash
   openclaw update
   ```
2. **After update, re-pair browser:**
   ```bash
   openclaw browser status  # check if scope error persists
   openclaw browser pair    # re-pair if needed
   ```
3. **Configure MCP servers for OpenClaw:**
   ```bash
   # Firecrawl MCP
   openclaw mcp add firecrawl -- npx -y firecrawl-mcp
   # Set env
   openclaw mcp config firecrawl FIRECRAWL_BASE_URL http://localhost:3002
   
   # SearXNG MCP (if available)
   openclaw mcp add searxng -- npx -y searxng-mcp
   openclaw mcp config searxng SEARXNG_URL http://127.0.0.1:8080
   ```
4. **Verify:**
   ```bash
   openclaw mcp list  # should show firecrawl + searxng
   ```

**Owner:** Ember (requires elevated for update)  
**Effort:** 1.5 hours  
**Risk:** Medium — OpenClaw update may require gateway restart

---

### 3.4 DeerFlow Docker Stack Decision

**Problem:** 3 DeerFlow containers running (gateway, nginx, frontend) but not used by any active pipeline. Stack Unification Plan exists at 45-55% utilization but was never completed.

**Options:**

**Option A: Shut Down (Recommended)**
- Hermes + Crawl4AI + Firecrawl + SearXNG already cover collection and extraction
- DeerFlow orchestration engine adds complexity without current value
- Shut down 3 containers, save ~500MB RAM
- Keep DeerFlow venv (Crawl4AI, unified_scraper.py) — these are used by system crontab

**Option B: Activate as Orchestration Layer**
- Use DeerFlow planning agent for complex multi-source research tasks
- Integrate as middleware between OpenClaw Director and Hermes Operator
- Requires building API integration that doesn't exist yet

**Recommendation:** Option A. The operational pipeline works without DeerFlow orchestration. Shut down the Docker stack, keep the venv.

```bash
cd /home/p62operator/tools/deer-flow
docker compose down
# Keep .venv, scripts, unified_scraper.py
```

**Owner:** Ember (requires DAF approval)  
**Effort:** 15 minutes  
**Risk:** Low — containers can be restarted if needed

---

### 3.5 Crawl4AI Broader Source Discovery via SearXNG

**Problem:** Crawl4AI collects from a fixed list of 25 hardcoded sources. No dynamic discovery. SearXNG indexes 35+ Malaysian news sources but isn't used for discovery.

**Action:** Add SearXNG-powered source discovery to the collection pipeline:

1. **Create `discover_sources.py`:**
   ```python
   #!/usr/bin/env python3
   """Discover trending Malaysian political articles via SearXNG."""
   import requests
   import json
   from datetime import datetime
   
   SEARXNG_URL = "http://127.0.0.1:8080/search"
   
   QUERIES = [
       "PRN Melaka 2026",
       "Ab Rauf Yusoh",
       "Muhamad Akmal Saleh", 
       "PKR congress 2026",
       "Tabung Haji RCI",
       "Malaysia politik hari ini",
   ]
   
   def discover():
       results = []
       for q in QUERIES:
           r = requests.get(SEARXNG_URL, params={
               "q": q, "format": "json", "time_range": "day",
               "categories": "news"
           })
           results.extend(r.json().get("results", []))
       # Deduplicate by URL
       seen = set()
       unique = []
       for r in results:
           if r["url"] not in seen:
               seen.add(r["url"])
               unique.append(r)
       return unique
   
   if __name__ == "__main__":
       articles = discover()
       print(f"Discovered {len(articles)} unique articles")
       # Output as JSON for Crawl4AI to scrape
       with open(f"discovered-{datetime.now().strftime('%Y%m%d')}.json", "w") as f:
           json.dump(articles, f, indent=2)
   ```

2. **Integrate into `heartbeat-crawl4ai.sh`:** Run discovery before collection, merge discovered URLs with the 25 hardcoded sources.

**Owner:** Ember  
**Effort:** 4 hours  
**Risk:** Low — additive, doesn't change existing pipeline

---

## Phase 4: Fleet Optimization (Day 6-7)

### 4.1 Re-enable or Retire 18 Disabled Hermes Jobs

**Problem:** 18 disabled jobs spanning 4 workstreams. Some are post-election (PRN NS — should be retired), some are valuable but paused (CSCDC watches, Cyber Drill monitor).

**Decision Matrix:**

| Job ID | Name | Action | Rationale |
|--------|------|--------|-----------|
| bf8a4c1fb881 | PRN NS Daily News Collection | ❌ Delete | Election passed, post-mortem complete |
| 3c9e6756876a | PRN NS Entity Extraction | ❌ Delete | Same |
| 02e588724145 | PRN NS Sentiment Analysis | ❌ Delete | Same |
| b8f69d6f990d | PRN NS Daily Intelligence Brief | ❌ Delete | Same |
| 2df980e8e094 | PRN NS Git Sync | ❌ Delete | Same as git sync job 884c3de01f28 still active |
| 10d9c6242b4e | PRN NS Candidate Campaign Trail | ❌ Delete | Same |
| a9b955d541da | PRN NS Post-Mortem News Collection | ❌ Delete | Same |
| ee978476ef2d | PRN NS Analyst & Academic Commentary | ❌ Delete | Same |
| eece39e9186f | PRN NS EXCO/Governance Formation | ❌ Delete | Same |
| f5fbb87e77cc | PRN NS Daily Post-Mortem Brief | ❌ Delete | Same |
| 95af59753d01 | CSCDC Leadership & Approval Watch | ✅ Re-enable | Active monitoring need |
| 0a0770f21820 | PQC Sandbox & Sovereign AI Monitor | ✅ Re-enable | Active monitoring need |
| ee49690d9b66 | Gov Infrastructure & Procurement Watch | ✅ Re-enable | Active monitoring need |
| bb5795421110 | Anti-Deepfake & Campaign Strategy | ✅ Re-enable | Active monitoring need |
| efb27cfe4011 | Cyber Drill & Crisis Protocol Monitor | ✅ Re-enable | Active monitoring need |
| 656efb0feade | CSCDC Programme & Community Champions | ✅ Re-enable | Active monitoring need |
| ed94da585cad | Strategic CognitiveOS PIR Status | ⚠️ Decision needed | Depends on whether PIR tracking is still active |
| 5f92c372dd4d | Strategic CognitiveOS Git Sync | ⚠️ Decision needed | Same |

**Result:** 10 PRN NS jobs deleted, 6 re-enabled, 2 pending DAF decision.

**Re-enabled jobs need:**
1. Model assignment (GLM-5.2 for collection, Qwen 397B for analysis)
2. Workspace assignment (new `workspace-cscdc` or reuse existing)
3. Prompt update with current search protocol + CVS validation
4. Test run before going live

**Owner:** Ember (requires DAF approval for re-enables)  
**Effort:** 2 hours  
**Risk:** Medium — re-enabled jobs need prompt updates and workspace setup

---

### 4.2 Standardize Hermes Job Prompts

**Problem:** Each Hermes job has a unique prompt written at different times with different conventions. Inconsistent CVS blocks, deprecated search instructions, varying output formats.

**Action:** Create a standard prompt template:

```
# [JOB NAME] ([JOB ID])

## Mission
[1-2 sentence mission statement]

## Search Protocol
- Use web_search for topic discovery (SearXNG — 35+ sources)
- Use web_extract for content extraction (Firecrawl — localhost:3002)
- Batch up to 5 URLs per web_extract call

## PIRs Covered
[List PIR IDs and POI names]

## Collection Steps
1. [Specific steps for this job]
2. [Specific steps]

## CVS Validation
[Reference to CVS skill — don't inline 500 lines]

## Output
- File: [specific path]
- Format: [specific format]
- Git: [commit message template]

## Escalation
- If no new findings: report "No new findings" + skip
- If CRITICAL finding: [escalation protocol]
```

Update all 15 active + 6 re-enabled jobs to this template.

**Owner:** Ember  
**Effort:** 4 hours  
**Risk:** Medium — each job needs custom collection steps while following the standard structure

---

### 4.3 OpenClaw Update

**Problem:** OpenClaw 2026.5.6, update to 2026.7.1-2 available. May fix browser gateway scope error and other bugs.

**Action:**
```bash
# Backup config first
cp ~/.openclaw/openclaw.json ~/.openclaw/openclaw.json.bak-20260815
# Update
openclaw update
# Verify
openclaw status
openclaw browser status  # check if scope error fixed
# If gateway needs restart
openclaw gateway restart
```

**Owner:** Ember (requires elevated)  
**Effort:** 30 minutes  
**Risk:** Medium — may require gateway restart, brief downtime

---

## Phase 5: Documentation & Governance (Day 8-10)

### 5.1 Update AGENTS.md

Remove all references to non-existent files:
- `tools/truth-validator/CVS-MANDATE.md` → replace with `workspace/03-VERIFICATION/CVS-FRAMEWORK.md`
- `tools/truth-validator/CVS-SYSTEM-PROMPT.md` → remove
- `electiondata-verify.sh` → remove
- `ELECTIONDATA-INTEGRATION.md` → remove

Update CVS section to reflect actual architecture:
- Hermes CVS skill (operational, embedded in prompts)
- CVS Evidence Register (operational, 210+ claims)
- `validate.sh` (OpenClaw Director's audit tool)

### 5.2 Update TOOLS.md

- Remove DeerFlow section as active tool (keep as archived venv reference)
- Remove Mr.Holmes section if not actively used
- Remove ElectionData.MY section (API key not configured, integration never completed)
- Update Crawl4AI section with current status (integrated into Hermes pipeline)
- Add SearXNG section (discovery layer for Hermes)
- Add Firecrawl section (extraction layer for Hermes)

### 5.3 Create Operational Runbook

Create `docs/operational-runbook.md` with:
1. Architecture diagram (three-tier model)
2. Cron job inventory (OpenClaw + Hermes + System crontab)
3. Model tiering policy
4. CVS validation workflow
5. Health check procedures
6. Escalation protocols
7. Disaster recovery (how to restart each component)

**Owner:** Ember  
**Effort:** 4 hours  
**Risk:** None

---

## Summary: Operational Debt Closure Checklist

| # | Item | Phase | Effort | Status |
|---|------|-------|--------|--------|
| 1 | Fix SearXNG search for Hermes | P1 | 2h | Pending |
| 2 | Integrate Crawl4AI → Hermes pipeline | P1 | 3h | Pending |
| 3 | Install Ollama | P1 | 15m | Pending |
| 4 | Rewrite HEARTBEAT.md | P1 | 30m | Pending |
| 5 | OpenClaw Director cron jobs (4) | P2 | 4h | Pending |
| 6 | Hermes model tiering | P2 | 1h | Pending |
| 7 | Hermes prompt cleanup | P2 | 3h | Pending |
| 8 | Signal registry decision | P3 | 2-6h | Pending |
| 9 | Unify truth validator + CVS | P3 | 3h | Pending |
| 10 | Fix browser + configure MCP | P3 | 1.5h | Pending |
| 11 | DeerFlow Docker decision | P3 | 15m | Pending |
| 12 | Crawl4AI + SearXNG discovery | P3 | 4h | Pending |
| 13 | Hermes disabled jobs cleanup | P4 | 2h | Pending |
| 14 | Standardize Hermes prompts | P4 | 4h | Pending |
| 15 | OpenClaw update | P4 | 30m | Pending |
| 16 | Update AGENTS.md + TOOLS.md | P5 | 3h | Pending |
| 17 | Create operational runbook | P5 | 4h | Pending |
| 18 | Fix root-owned files in DeerFlow | P1 | 5m | Pending |

**Total estimated effort:** 38-42 hours  
**Timeline:** 10 days  
**Dependencies:** DAF approval for re-enabling jobs, shutting down DeerFlow Docker, OpenClaw update

---

## Target End State

```
OpenClaw (Director)
├── Cron: Pipeline Health Monitor (6h)
├── Cron: Stale Data Alert (daily)
├── Cron: CVS Weekly Audit (Sunday)
├── Cron: Hermes Fleet Review (monthly)
├── Cron: Memory Dreaming (daily 03:00)
├── Browser: ✅ Operational
├── MCP: Firecrawl + SearXNG configured
├── Memory Search: ✅ Ollama operational
└── Truth Validator: Audit tool for CVS evidence registers

Hermes (Operator) — 21 Active Jobs
├── PRN Melaka POI (6 jobs, GLM-5.2 for collection, Qwen 397B for analysis)
├── Tabung Haji RCI (3 jobs, GLM-5.2 for collection)
├── CSCDC Watches (6 re-enabled jobs, GLM-5.2)
├── PRN NS Post-Mortem (1 job, git sync only)
├── CVS Weekly Validation (1 job)
├── Strategic CognitiveOS (2 jobs, if approved)
├── SearXNG search: ✅ Integrated
├── Firecrawl extract: ✅ Integrated
├── Crawl4AI broad collection: ✅ Fed into entity extraction
└── CVS Evidence Register: ✅ 210+ claims, growing daily

Infrastructure
├── Crawl4AI: ✅ 4x/day collection → Hermes pipeline
├── SearXNG: ✅ Discovery layer for Hermes + Crawl4AI
├── Firecrawl: ✅ Extraction layer for Hermes
├── DeerFlow Docker: ❌ Shut down (venv retained)
├── Ollama: ✅ Memory search for OpenClaw
├── Browser: ✅ Fixed after OpenClaw update
└── Signal Registry: ✅ Retired or operationalized
```

**Stack utilization target: 14/14 components operational and leveraged.**
