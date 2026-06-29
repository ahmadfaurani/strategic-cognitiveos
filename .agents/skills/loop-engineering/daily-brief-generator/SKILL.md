# daily-brief-generator Skill

**Purpose:** Generate structured daily intelligence brief from MEDIUM/HIGH priority signals. Produces actionable summaries for human review.

**Loop Level:** Loop 3 (Event-Driven Loop) with Loop 2 (Verification) integration

## When to Use

This skill runs automatically after daily collection:
- **Trigger:** Completion of `heartbeat-daily-collection` with MEDIUM/HIGH signals
- **Schedule:** Daily at 23:30 UTC (30 min after collection)
- **Alternative:** Manual trigger via `/generate-brief [date]`

## Brief Structure

```markdown
# Daily Political Intelligence Brief
**Date:** 2026-06-18
**Collection Period:** 2026-06-17 23:00 - 2026-06-18 23:00 UTC
**Signals Analyzed:** 42
**Escalation Summary:** 0 CRITICAL | 3 HIGH | 15 MEDIUM

---

## 🔴 HIGH PRIORITY (Immediate Attention Required)

### [Signal Title]
**PIR Tags:** PIR-3, PIR-1
**Source:** The Star, Bernama (multi-source confirmation)
**Escalation:** ESC-003 (Foreign relations incident)
**Summary:** 2-3 sentence executive summary
**Key Entities:** Anwar Ibrahim, Chinese Embassy, Ministry of Foreign Affairs
**Recommended Action:** Monitor for diplomatic response, prepare briefing note
**Signal ID:** signal-2026-06-18-003

---

## 🟡 MEDIUM PRIORITY (Situational Awareness)

### [Signal Title]
**PIR Tags:** PIR-2
**Source:** The Edge
**Escalation:** ESC-005 (Policy change)
**Summary:** ...
**Signal ID:** signal-2026-06-18-007

---

## 📊 PIR Trend Analysis (24h)

| PIR | Signal Count | Change vs Previous Day |
|-----|--------------|------------------------|
| PIR-1 (Govt Stability) | 8 | ↑ +3 |
| PIR-2 (Economic Policy) | 12 | → 0 |
| PIR-3 (Foreign Relations) | 5 | ↓ -2 |
...

## 🚨 Emerging Narratives
- Narrative A: Budget revision discussions gaining momentum (3 signals)
- Narrative B: Coalition speculation resurfaces (2 signals)

## 📝 Analyst Notes
[Any automated observations or flags for human review]
```

## Usage

### Automatic (Post-Collection)

```bash
# Triggered automatically by heartbeat-daily-collection
openclaw skill run daily-brief-generator \
  --date "2026-06-18" \
  --signals "memory/signals/2026/06/18-signals.jsonl" \
  --output "memory/briefs/2026/06/18-brief.md"
```

### Manual

```bash
openclaw skill run daily-brief-generator \
  --date "2026-06-18" \
  --format "markdown" \
  --include-trends true \
  --send-to "telegram"
```

## Configuration

Create/edit `~/.openclaw/workspace/.agents/skills/loop-engineering/daily-brief-generator/config.yaml`:

```yaml
schedule:
  timezone: "UTC"
  cron: "30 23 * * *"  # Daily at 23:30 UTC

input:
  signals_path_pattern: "memory/signals/{YYYY}/{MM}/{DD}-signals.jsonl"
  min_escalation_level: "MEDIUM"  # Include MEDIUM and above only

output:
  briefs_path: "memory/briefs"
  format: "markdown"
  filename_pattern: "{YYYY}-{MM}-{DD}-brief.md"
  
  delivery:
    telegram:
      enabled: true
      chat_id: "640442208"
      suppress_embeds: true
    email:
      enabled: false
      recipients: []
    file_only:
      enabled: true

content:
  include_trend_analysis: true
  trend_comparison_days: 7
  include_emerging_narratives: true
  narrative_clustering_threshold: 0.75
  max_signals_per_section: 10
  entity_highlighting: true

llm:
  model: "vllm/Qwen/Qwen3.5-397B-A17B"
  temperature: 0.3
  max_tokens: 4000

verification:
  fact_check_enabled: true
  cross_reference_sources: true
  flag_unverified_claims: true
```

## LLM Prompt Template

```
You are a political intelligence analyst. Generate a daily brief from the following signals.

**Instructions:**
1. Group signals by escalation level (HIGH first, then MEDIUM)
2. For each signal, write a 2-3 sentence executive summary
3. Highlight multi-source confirmed signals
4. Identify emerging narratives (clusters of 2+ related signals)
5. Compute PIR trend vs previous 7 days
6. Flag any unverified or single-source claims

**Tone:** Professional, concise, actionable
**Format:** Markdown with clear section headers

**Signals:**
{signals_json}

**Previous Day Trends:**
{trend_data}
```

## Verification (Loop 2 Integration)

Before delivery, brief is validated:

| Criterion | Check |
|-----------|-------|
| **Factual Accuracy** | All claims traced to source signals |
| **No Hallucination** | No entities/events not in source data |
| **Escalation Correctness** | HIGH signals appear in HIGH section |
| **Trend Accuracy** | PIR counts match signal registry |
| **Completeness** | All MEDIUM/HIGH signals included |

If validation fails:
1. Regenerate with specific feedback
2. Max 2 iterations
3. If still fails, flag for human review

## Human-in-the-Loop Integration

### Pre-Delivery Review (Optional)

For HIGH-priority briefs (any CRITICAL/HIGH signals):
1. Generate brief
2. Send to human for review
3. Human can: approve, edit, request regeneration
4. After approval, deliver to channels

### Post-Delivery Feedback

Human can react to brief with:
- 👍 Useful / 👎 Not useful
- 📝 Comment with corrections
- 🔄 Request follow-up analysis

Feedback logged for Loop 4 (Hill Climbing) analysis.

## Integration with MiroFish

Brief output can feed MiroFish scenario simulation:

```python
# Extract key signals for MiroFish
mirofish_input = {
    "date": "2026-06-18",
    "high_priority_signals": [...],
    "pir_trends": {...},
    "emerging_narratives": [...]
}

# POST to MiroFish API
requests.post("http://localhost:3000/api/scenarios/simulate", json=mirofish_input)
```

## Metrics & Monitoring

Track in `memory/heartbeat-state.json`:

```json
{
  "daily_brief": {
    "last_generated": "2026-06-18T23:30:00Z",
    "signals_included": 18,
    "high_priority_count": 3,
    "delivery_status": "sent",
    "human_feedback": null,
    "generation_time_seconds": 45
  }
}
```

## Related Skills

- `heartbeat-daily-collection` - Upstream data source
- `heartbeat-weekly-synthesis` - Aggregates daily briefs into weekly report
- `mirofish-scenario-feeder` - Downstream scenario simulation
