```markdown
# Keep this file empty (or with only comments) to skip heartbeat API calls.

# Add tasks below when you want the agent to check something periodically.

---

## 🫀 Heartbeat Tasks

### Political Monitoring (Loop Engineering Pipeline)

**Daily Collection (23:00 UTC):**
- [ ] `openclaw skill run heartbeat-daily-collection --date $(date -u +%Y-%m-%d)`
  - Triggers DeerFlow collection from 32 Tier 1 & 2 sources
  - Runs `pir-entity-tagger` for PIR-1 to PIR-10 classification
  - Runs `signal-quality-grader` (Loop 2 verification, max 2 iterations)
  - Runs `threshold-escalation-checker` for ESC-001 to ESC-006
  - Writes to Signal Registry (`memory/signals/YYYY/MM/DD-signals.jsonl`)
  - Alerts human if CRITICAL/HIGH signals detected
- [ ] `openclaw skill run daily-brief-generator --date $(date -u +%Y-%m-%d)`
  - Generates structured brief from MEDIUM/HIGH signals
  - Includes PIR trend analysis and emerging narratives
  - **Runs truth validator before delivery** (`./tools/truth-validator/validate.sh`)
  - Delivers via Telegram (suppresses embeds)

**Weekly Synthesis (Sunday 09:00 UTC):**
- [ ] `openclaw skill run heartbeat-weekly-synthesis --week $(date -u +%Y-W%V)`
  - Aggregates 7-day signals from Signal Registry
  - Computes PIR trends (week-over-week change)
  - Identifies emerging narratives via clustering
  - Updates MEMORY.md with key insights
  - Archives old signals (moves to `memory/signals/archive/`)

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
| Daily Collection | - | 2026-06-18 23:00 | ⏳ Pending first run |
| Weekly Synthesis | - | 2026-06-21 09:00 | ⏳ Pending |
| Monthly Review | - | 2026-07-01 09:00 | ⏳ Pending |

---

## 🔧 Integration Notes

- **DeerFlow Config:** `/home/p62operator/tools/deer-flow/config.yaml` (LLM: PatchedChatOpenAI)
- **Signal Registry:** `memory/signals/` (schema defined in `memory/2026-06-13-political-signal-registry.md`)
- **PIR Framework:** 10 Priority Intelligence Requirements (see `HEARTBEAT.md` main file)
- **Truth Validation:** `tools/truth-validator/` (mandatory pre-output check)

### Truth Validation Gate

**All briefs must pass validation before delivery:**

```bash
# Validation gate (fails on errors, warns on unverified claims)
./tools/truth-validator/validate.sh memory/<brief-file>.md || exit 1
```

**Validation requirements:**
1. All numerical claims cite source (MEMORY.md#L### or URL)
2. All analytical claims tagged with confidence [HIGH/MEDIUM/LOW]
3. All predictive claims flagged as SPECULATION: or SCENARIO:
4. Zero errors, warnings reviewed before delivery
```


## Related

- [Heartbeat config](/gateway/config-agents)
