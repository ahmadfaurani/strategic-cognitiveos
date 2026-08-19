# Keep this file empty (or with only comments) to skip heartbeat API calls.

# Add tasks below when you want the agent to check something periodically.

---

## 🔥 Embering — The Daily Tending

Heartbeat = checking the ember's temperature. Each task is an act of tending: keeping the ember alive, checking whether warmth persists, adding fuel when needed. An untended ember dies.

---

## 🫀 Heartbeat Tasks

> **⚠️ REALITY NOTE (2026-08-15):** The fictional `openclaw skill run` commands below were aspirational designs never operationalized. Hermes cron IS the actual pipeline (15 active jobs, 3 workstreams). Signal Registry is RETIRED — CVS Evidence Register is canonical. These tasks are retained as design reference for future OpenClaw Director cron jobs.

### Political Monitoring (Loop Engineering Pipeline)

**Daily Collection (23:00 UTC):**
- [ ] `openclaw skill run heartbeat-daily-collection --date $(date -u +%Y-%m-%d)`
  - ~~Triggers DeerFlow collection from 32 Tier 1 & 2 sources~~ (Hermes does its own collection via Firecrawl)
  - ~~Runs `pir-entity-tagger` for PIR-1 to PIR-10 classification~~ (Hermes does entity extraction via bash scripts)
  - ~~Runs `signal-quality-grader` (Loop 2 verification, max 2 iterations)~~ (CVS validation embedded in Hermes prompts)
  - ~~Runs `threshold-escalation-checker` for ESC-001 to ESC-006~~ (CVS Evidence Register tracks escalation)
  - ~~Writes to Signal Registry (`memory/signals/YYYY/MM/DD-signals.jsonl`)~~ (Signal Registry RETIRED 2026-08-15)
  - ~~Alerts human if CRITICAL/HIGH signals detected~~

**Weekly Synthesis (Sunday 09:00 UTC):**
- [ ] `openclaw skill run heartbeat-weekly-synthesis --week $(date -u +%Y-W%V)`
  - ~~Aggregates 7-day signals from Signal Registry~~ (CVS Evidence Register is canonical)
  - Computes PIR trends (week-over-week change)
  - Identifies emerging narratives via clustering
  - Updates MEMORY.md with key insights

**Monthly Review (1st of month, 09:00 UTC):**
- [ ] `openclaw skill run monthly-pipeline-review --month $(date -u +%Y-%m)`
  - Reviews signal classification accuracy (human vs automated)
  - Refines PIR keyword sets based on false positives/negatives
  - Updates media source list (adds high-performers, removes low-quality)
  - Generates Loop 4 improvement recommendations

---

## 📊 Status Tracking

| Check Type | Last Run | Next Due | Status |
|------------|----------|----------|--------|
| Daily Collection | N/A | RETIRED | ⛔ Pipeline retired — Hermes does collection |
| Weekly Synthesis | - | TBD | ⏳ Pending OpenClaw Director cron setup |
| Monthly Review | - | TBD | ⏳ Pending OpenClaw Director cron setup |

---

## 🔧 Integration Notes

- **Hermes Config:** `/home/p62operator/.hermes/config.yaml` (model: GLM-5.2, web: Firecrawl)
- **Hermes Cron Jobs:** `/home/p62operator/.hermes/cron/jobs.json` (23 jobs: 13 enabled, 10 recently deleted)
- **CVS Evidence Register:** `03-VERIFICATION/CVS-EVIDENCE-REGISTER.csv` — Framework institutionalized, register NOT YET populated (1 example row only). Designed for OSINT data collection claim verification (T1-T6 tiers, L1-L5 sources, 20-field schema).
- ~~**Signal Registry:**~~ `memory/signals/` — **RETIRED 2026-08-15**
- **Truth Validation:** `03-VERIFICATION/CVS-FRAMEWORK.md` (Master Framework) — sole CVS instrument. `tools/truth-validator/` retired 2026-08-17 (DUN Profiling CVS archived)
- **DeerFlow venv:** `/home/p62operator/tools/deer-flow/.venv` (Crawl4AI 0.9.2 + unified_scraper.py)
- **Crawl4AI Bridge:** `/home/p62operator/.hermes/scripts/crawl4ai-bridge.sh` (Hermes → Crawl4AI stealth mode)
- **DeerFlow Skills:** 30 skills bridged to Hermes via `skills.external_dirs` in config.yaml

### Three Validation Layers — Separate Use Cases (NOT a Gap)

**1. Intake SOP (9-step)** — CognitiveOS workstream management & cataloging. How incoming data gets structured, typed, stored, committed. Operational.

**2. CVS Evidence Register** — Core truth validation for OSINT data collection. Claim-level verification with T1-T6 tiers, L1-L5 source scoring, 20-field schema. Framework institutionalized; register population is the next milestone.

**3. Hermes Inline CVS** — Condensed validation for cronjobs. T1-T6 tiering embedded in collection prompts. Fit-for-purpose for automated cron context. Operational.

**validate.sh** — RETIRED 2026-08-17. Was DUN-profiling validator, not Master Framework validator. Do not use for CVS validation. Use `03-VERIFICATION/CVS-FRAMEWORK.md` as sole CVS instrument.

Each serves a distinct checkpoint. They are separate by design, not a gap to close.


### ADEP-001 Compliance Audit (Daily, first heartbeat after 00:00 UTC)

- [ ] Run daily compliance audit
  ```bash
  bash tools/honcho-connector/audit.sh --hours 24 --threshold 80
  ```
  - Queries Honcho for compliance records from past 24h
  - Reports PASS/BLOCK score per diligence level
  - Flags exceptions and below-threshold compliance
  - If below threshold: surface to DAF in heartbeat response

---

## Related

- [Heartbeat config](/gateway/config-agents)

### Dreaming CVS Validation (Daily, 03:15 UTC)

- [ ] Run CVS validation on REM phase candidates
  ```bash
  # NOTE: dreaming-cvs-integration.sh retired 2026-08-17 (DUN Profiling CVS archived)
  # CVS validation now per 03-VERIFICATION/CVS-FRAMEWORK.md (Master Framework)
  ```
- [ ] Review `memory/dreaming-validation.jsonl` for FAILED candidates
- [ ] If PASSED: `openclaw memory promote --apply`
- [ ] If BLOCKED: Edit `memory/dreaming/rem/YYYY-MM-DD.md` to add citations, re-run validation
- [ ] Update `DREAMS.md` with any insights from validated candidates
