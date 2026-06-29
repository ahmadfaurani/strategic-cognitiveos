# heartbeat-daily-collection Skill

**Purpose:** Trigger daily political news collection via DeerFlow at 23:00 UTC, process through PIR tagging, quality grading, and escalation checking.

**Loop Level:** Loop 3 (Event-Driven Loop - Triggers & Integration)

## When to Use

This skill is triggered automatically by OpenClaw heartbeat cron:
- **Schedule:** Daily at 23:00 UTC
- **Trigger:** Heartbeat poll in HEARTBEAT.md
- **Alternative:** Manual trigger via Telegram/Slack command `/collect-daily`

## Workflow

```
┌─────────────────────────────────────────────────────────────┐
│  HEARTBEAT TRIGGER (23:00 UTC)                              │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│  1. deer-flow-news-collection                               │
│     - Collect from 32 Tier 1 & 2 Malaysian media sources    │
│     - Extract raw signals                                   │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│  2. pir-entity-tagger                                       │
│     - Extract entities (PERSON, ORG, LOCATION)              │
│     - Tag with PIR-1 through PIR-10                         │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│  3. signal-quality-grader (Loop 2 Verification)             │
│     - Grade against rubric (5 criteria)                     │
│     - Revise if score < 75%                                 │
│     - Max 2 iterations                                      │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│  4. threshold-escalation-checker                            │
│     - Evaluate against ESC-001 to ESC-006                   │
│     - Assign severity (CRITICAL/HIGH/MEDIUM/LOW)            │
│     - Flag for human review if CRITICAL/HIGH                │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│  5. signal-registry-writer                                  │
│     - Write to memory/signals/YYYY/MM-DD-signals.jsonl      │
│     - Validate schema                                       │
│     - Deduplicate                                           │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│  6. Check for CRITICAL/HIGH signals                         │
│     - If found: Generate immediate alert                    │
│     - If MEDIUM only: Queue for daily brief                 │
└─────────────────────────────────────────────────────────────┘
```

## Usage

### Automatic (Heartbeat)

Add to `HEARTBEAT.md`:

```markdown
## Daily Collection (23:00 UTC)
- [ ] openclaw skill run heartbeat-daily-collection
```

### Manual

```bash
openclaw skill run heartbeat-daily-collection \
  --date "2026-06-18" \
  --config "path/to/config.yaml" \
  --dry-run  # Optional: preview without writing
```

## Configuration

Create/edit `~/.openclaw/workspace/.agents/skills/loop-engineering/heartbeat-daily-collection/config.yaml`:

```yaml
schedule:
  timezone: "UTC"
  cron: "0 23 * * *"  # Daily at 23:00 UTC

deerflow:
  config_path: "/home/p62operator/tools/deer-flow/config.yaml"
  llm_provider: "PatchedChatOpenAI"
  sources_count: 32

pipeline:
  steps:
    - "deer-flow-news-collection"
    - "pir-entity-tagger"
    - "signal-quality-grader"
    - "threshold-escalation-checker"
    - "signal-registry-writer"

signal_registry:
  path: "memory/signals"
  schema_version: "1.0"
  dedup_enabled: true
  dedup_similarity_threshold: 0.85

escalation:
  critical_alert_enabled: true
  alert_channels:
    - "telegram"
    - "email"  # Optional
  human_review_required_for:
    - "CRITICAL"
    - "HIGH"

retry_policy:
  max_retries: 3
  retry_delay_seconds: 60
  exponential_backoff: true
```

## Output

### Success

```json
{
  "status": "success",
  "collection_date": "2026-06-18",
  "signals_collected": 47,
  "signals_after_dedup": 42,
  "pir_distribution": {
    "PIR-1": 8,
    "PIR-2": 12,
    "PIR-3": 5,
    "PIR-4": 3,
    "PIR-5": 6,
    "PIR-6": 2,
    "PIR-7": 4,
    "PIR-8": 1,
    "PIR-9": 0,
    "PIR-10": 1
  },
  "escalation_summary": {
    "CRITICAL": 0,
    "HIGH": 3,
    "MEDIUM": 15,
    "LOW": 24
  },
  "registry_path": "memory/signals/2026/06/18-signals.jsonl",
  "human_review_required": true,
  "review_queue_count": 3
}
```

### Failure

```json
{
  "status": "failed",
  "stage": "pir-entity-tagger",
  "error": "DeerFlow API timeout",
  "retry_count": 2,
  "next_retry_in_seconds": 120
}
```

## Human-in-the-Loop Integration

### CRITICAL/HIGH Alerts

When CRITICAL or HIGH signals detected:
1. Skill sends immediate notification via Telegram
2. Includes summary: signal count, top PIRs, escalation details
3. Provides link to review queue
4. Waits for human acknowledgment before proceeding to daily brief

### Review Queue

Human can:
- Approve signals as-is
- Request re-grading
- Downgrade escalation level
- Add manual notes

## Monitoring & Metrics

Track these metrics in `memory/heartbeat-state.json`:

```json
{
  "daily_collection": {
    "last_run": "2026-06-18T23:00:00Z",
    "next_due": "2026-06-19T23:00:00Z",
    "status": "completed",
    "signals_collected": 47,
    "avg_quality_score": 0.84,
    "human_review_count": 3
  }
}
```

## Error Handling

| Error Type | Recovery Action |
|------------|-----------------|
| DeerFlow API timeout | Retry with exponential backoff (max 3) |
| PIR tagging failure | Log error, continue with untagged signals (flag for review) |
| Quality grader error | Skip grading, flag all signals for human review |
| Registry write failure | Retry, if fails send alert to human |
| Human review timeout | Escalate after 2 hours, proceed with automated classification |

## Related Skills

- `daily-brief-generator` - Downstream, generates brief from MEDIUM/HIGH signals
- `heartbeat-weekly-synthesis` - Aggregates 7 days of collection results
- `signal-registry-writer` - Sub-skill for writing to registry
