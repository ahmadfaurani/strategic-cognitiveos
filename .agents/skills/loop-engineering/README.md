# Loop Engineering Skills for Political Monitoring

This directory contains OpenClaw skills implementing the **4-loop framework** from LangChain's "Art of Loop Engineering" for Malaysian political intelligence monitoring.

## Framework Overview

| Loop | Purpose | Skills |
|------|---------|--------|
| **Loop 1** | Core Automation | `pir-entity-tagger`, `threshold-escalation-checker` |
| **Loop 2** | Quality Control | `signal-quality-grader` |
| **Loop 3** | Event-Driven | `heartbeat-daily-collection`, `daily-brief-generator` |
| **Loop 4** | Continuous Improvement | *(planned: `trace-analysis-agent`, `pir-keyword-optimizer`)* |

## Directory Structure

```
loop-engineering/
├── pir-entity-tagger/
│   ├── SKILL.md           # Skill documentation
│   └── config.yaml        # PIR taxonomy, known entities
├── threshold-escalation-checker/
│   ├── SKILL.md           # Skill documentation
│   └── config.yaml        # ESC-001 to ESC-006 rules
├── signal-quality-grader/
│   ├── SKILL.md           # Skill documentation
│   └── config.yaml        # Grading rubric, tier lists
├── heartbeat-daily-collection/
│   ├── SKILL.md           # Skill documentation
│   └── config.yaml        # Pipeline, schedule, alerts
├── daily-brief-generator/
│   ├── SKILL.md           # Skill documentation
│   └── config.yaml        # Brief template, delivery
└── README.md              # This file
```

## Pipeline Flow

```
┌──────────────────────────────────────────────────────────────┐
│  HEARTBEAT TRIGGER (23:00 UTC daily)                        │
└──────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌──────────────────────────────────────────────────────────────┐
│  LOOP 1: Agent Loop                                          │
│  ┌────────────────────────────────────────────────────────┐  │
│  │ 1. deer-flow-news-collection                           │  │
│  │    → Collect from 32 Malaysian media sources           │  │
│  └────────────────────────────────────────────────────────┘  │
│                            │                                   │
│                            ▼                                   │
│  ┌────────────────────────────────────────────────────────┐  │
│  │ 2. pir-entity-tagger                                   │  │
│  │    → Extract entities, tag PIR-1 to PIR-10             │  │
│  └────────────────────────────────────────────────────────┘  │
│                            │                                   │
│                            ▼                                   │
│  ┌────────────────────────────────────────────────────────┐  │
│  │ 3. threshold-escalation-checker                        │  │
│  │    → Evaluate ESC-001 to ESC-006                       │  │
│  └────────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌──────────────────────────────────────────────────────────────┐
│  LOOP 2: Verification Loop                                   │
│  ┌────────────────────────────────────────────────────────┐  │
│  │ 4. signal-quality-grader                               │  │
│  │    → Grade against 5-criteria rubric                   │  │
│  │    → Revise if score < 75% (max 2 iterations)          │  │
│  └────────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌──────────────────────────────────────────────────────────────┐
│  LOOP 3: Event-Driven Loop                                   │
│  ┌────────────────────────────────────────────────────────┐  │
│  │ 5. signal-registry-writer                              │  │
│  │    → Write to memory/signals/YYYY/MM/DD-signals.jsonl  │  │
│  └────────────────────────────────────────────────────────┘  │
│                            │                                   │
│                            ▼                                   │
│  ┌────────────────────────────────────────────────────────┐  │
│  │ 6. daily-brief-generator (23:30 UTC)                   │  │
│  │    → Generate structured brief                         │  │
│  │    → Deliver via Telegram                              │  │
│  └────────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌──────────────────────────────────────────────────────────────┐
│  LOOP 4: Hill Climbing (Planned)                            │
│  - Analyze traces to improve PIR keywords                   │
│  - Optimize escalation thresholds                           │
│  - Refine grader rubric based on human feedback             │
└──────────────────────────────────────────────────────────────┘
```

## PIR Framework (Priority Intelligence Requirements)

| Code | Category | Description |
|------|----------|-------------|
| **PIR-1** | Government Stability | PM, cabinet, coalition, parliament |
| **PIR-2** | Economic Policy | Budget, fiscal, taxation, subsidies |
| **PIR-3** | Foreign Relations | Diplomacy, ASEAN, China, US |
| **PIR-4** | Security & Defense | Military, terrorism, border |
| **PIR-5** | Corruption & Governance | MACC, investigations, graft |
| **PIR-6** | Social Unrest | Protests, racial/religious tensions |
| **PIR-7** | Electoral Politics | Elections, polling, party switching |
| **PIR-8** | Regulatory Changes | Laws, amendments, compliance |
| **PIR-9** | Corporate & Business | GLCs, investments, mergers |
| **PIR-10** | Environmental & Health | Climate, disasters, healthcare |

## Escalation Framework

| Code | Severity | Criteria |
|------|----------|----------|
| **ESC-001** | CRITICAL | Government stability threat + multi-source |
| **ESC-002** | CRITICAL | Senior official corruption + evidence |
| **ESC-003** | HIGH | Foreign relations incident |
| **ESC-004** | HIGH | Security/defense threat |
| **ESC-005** | MEDIUM | Significant policy change |
| **ESC-006** | MEDIUM | Social unrest potential |

## Usage

### Manual Execution

```bash
# Run full daily collection pipeline
openclaw skill run heartbeat-daily-collection --date 2026-06-18

# Generate daily brief
openclaw skill run daily-brief-generator --date 2026-06-18

# Run individual skills
openclaw skill run pir-entity-tagger --input signals.jsonl --output tagged.jsonl
openclaw skill run signal-quality-grader --input tagged.jsonl --output graded.jsonl
openclaw skill run threshold-escalation-checker --input graded.jsonl --output escalated.jsonl
```

### Automatic (Heartbeat)

Skills are triggered automatically by OpenClaw heartbeat cron:
- **Daily Collection:** 23:00 UTC
- **Daily Brief:** 23:30 UTC
- **Weekly Synthesis:** Sunday 09:00 UTC
- **Monthly Review:** 1st of month, 09:00 UTC

See `HEARTBEAT.md` for task definitions.

## Configuration

Each skill has its own `config.yaml`:

- **pir-entity-tagger/config.yaml** - PIR keywords, known entities
- **threshold-escalation-checker/config.yaml** - ESC rules, senior officials
- **signal-quality-grader/config.yaml** - Grading rubric, tier lists
- **heartbeat-daily-collection/config.yaml** - Pipeline, schedule, alerts
- **daily-brief-generator/config.yaml** - Brief template, delivery

## Human-in-the-Loop

| Loop | Human Oversight Point |
|------|-----------------------|
| Loop 1 | Review CRITICAL/HIGH escalations |
| Loop 2 | Override grader verdicts, review failed signals |
| Loop 3 | Approve new sources, review daily briefs |
| Loop 4 | Review harness improvements before deployment |

## Metrics & Monitoring

Track in `memory/heartbeat-state.json`:

```json
{
  "daily_collection": {
    "last_run": "2026-06-18T23:00:00Z",
    "signals_collected": 47,
    "avg_quality_score": 0.84,
    "human_review_count": 3
  },
  "daily_brief": {
    "last_generated": "2026-06-18T23:30:00Z",
    "delivery_status": "sent",
    "human_feedback": null
  }
}
```

## Planned Loop 4 Skills

| Skill | Purpose | Status |
|-------|---------|--------|
| `trace-analysis-agent` | Analyze collection traces | Planned |
| `pir-keyword-optimizer` | Refine PIR taxonomy | Planned |
| `threshold-tuning-advisor` | Adjust escalation rules | Planned |
| `source-performance-tracker` | Track source reliability | Planned |
| `grader-calibration-monitor` | Monitor grader consistency | Planned |

## Related Documentation

- [LangChain: The Art of Loop Engineering](https://www.langchain.com/blog/the-art-of-loop-engineering)
- [HEARTBEAT.md](/home/p62operator/.openclaw/workspace/HEARTBEAT.md)
- [Signal Registry Schema](memory/2026-06-13-political-signal-registry.md)
