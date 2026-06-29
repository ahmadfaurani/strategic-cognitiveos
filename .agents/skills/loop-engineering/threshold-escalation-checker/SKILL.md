# threshold-escalation-checker Skill

**Purpose:** Evaluate tagged signals against escalation thresholds (ESC-001 through ESC-006) and determine severity levels.

**Loop Level:** Loop 1 (Agent Loop - Core Automation)

## When to Use

Use this skill when:
- PIR-tagged signals need severity classification
- Determining if a signal requires immediate escalation
- Generating daily briefs (only MEDIUM/HIGH signals included)

## Escalation Thresholds

| Threshold Code | Severity | Criteria | Action |
|----------------|----------|----------|--------|
| **ESC-001** | CRITICAL | Direct threat to government stability + multiple sources confirm | Immediate alert to human |
| **ESC-002** | CRITICAL | Major corruption case involving senior officials + evidence | Immediate alert to human |
| **ESC-003** | HIGH | Foreign relations incident with potential diplomatic fallout | Include in daily brief, flag for review |
| **ESC-004** | HIGH | Security/defense threat with national implications | Include in daily brief |
| **ESC-005** | MEDIUM | Significant policy change affecting multiple sectors | Include in daily brief |
| **ESC-006** | MEDIUM | Social unrest with potential to escalate | Include in daily brief, monitor |

## Usage

```bash
openclaw skill run threshold-escalation-checker \
  --input "path/to/tagged-signals.jsonl" \
  --output "path/to/escalated-signals.jsonl" \
  --config "path/to/config.yaml"
```

## Input Format

```jsonl
{"id": "signal-001", "pir_tags": ["PIR-1", "PIR-5"], "entities": [...], "content": "...", "source": "...", "timestamp": "..."}
```

## Output Format

```jsonl
{"id": "signal-001", "...": "...", "escalation_level": "HIGH", "escalation_threshold": "ESC-003", "escalation_reason": "Foreign relations incident involving major power", "requires_human_review": true, "daily_brief_include": true}
```

## Severity Classification Logic

```python
def classify_severity(signal):
    # CRITICAL conditions
    if signal.pir_tags includes PIR-1 AND PIR-5 AND senior_official_involved:
        return "CRITICAL", "ESC-002"
    if signal.pir_tags includes PIR-1 AND government_stability_keywords AND multi_source_confirm:
        return "CRITICAL", "ESC-001"
    
    # HIGH conditions
    if signal.pir_tags includes PIR-3 AND diplomatic_keywords:
        return "HIGH", "ESC-003"
    if signal.pir_tags includes PIR-4 AND security_threat_keywords:
        return "HIGH", "ESC-004"
    
    # MEDIUM conditions
    if signal.pir_tags includes PIR-2 AND policy_change_keywords:
        return "MEDIUM", "ESC-005"
    if signal.pir_tags includes PIR-6 AND protest_keywords:
        return "MEDIUM", "ESC-006"
    
    # LOW (no escalation)
    return "LOW", None
```

## Configuration

Create/edit `~/.openclaw/workspace/.agents/skills/loop-engineering/threshold-escalation-checker/config.yaml`:

```yaml
escalation_rules:
  ESC-001:
    severity: CRITICAL
    pir_required: ["PIR-1"]
    keywords: ["collapse", "resign", "vote of no confidence", "coalition breaks"]
    min_source_count: 2
    action: immediate_alert
  
  ESC-002:
    severity: CRITICAL
    pir_required: ["PIR-5"]
    keywords: ["charged", "investigation", "corruption", "MACC", "senior official"]
    min_source_count: 1
    action: immediate_alert
  
  ESC-003:
    severity: HIGH
    pir_required: ["PIR-3"]
    keywords: ["diplomatic", "embassy", "tension", "dispute", "sanction"]
    min_source_count: 1
    action: daily_brief_flag
  
  # ... etc

senior_officials:
  - "Prime Minister"
  - "Deputy Prime Minister"
  - "Minister"
  - "Chief Minister"
  - "Governor"

human_review_required:
  - "CRITICAL"
  - "HIGH"
```

## Human-in-the-Loop Integration

For CRITICAL and HIGH escalations:
1. Skill flags `requires_human_review: true`
2. OpenClaw sends notification to human via preferred channel
3. Human can approve, downgrade, or request more info
4. Skill waits for human input before finalizing escalation

## Verification (Loop 2 Integration)

This skill should be followed by:
- `threshold-calibration-checker` - Periodic review of threshold accuracy
- Human review for CRITICAL/HIGH escalations

## Related Skills

- `pir-entity-tagger` - Upstream tagging
- `daily-brief-generator` - Downstream reporting
- `signal-quality-grader` - Quality verification
