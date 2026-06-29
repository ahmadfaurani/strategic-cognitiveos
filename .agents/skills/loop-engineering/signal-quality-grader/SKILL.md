# signal-quality-grader Skill

**Purpose:** Grade signal quality using LLM-as-a-judge pattern against a defined rubric. Implements Loop 2 (Verification Loop) for the political monitoring workflow.

**Loop Level:** Loop 2 (Verification Loop - Quality Control)

## When to Use

Use this skill when:
- Validating PIR tagging accuracy before writing to Signal Registry
- Ensuring only high-quality signals proceed to escalation checking
- Periodic audit of historical signals for quality assurance

## Grading Rubric

| Criterion | Pass Condition | Weight |
|-----------|----------------|--------|
| **PIR Relevance** | Signal references at least one valid PIR keyword (PIR-1 to PIR-10) | 25% |
| **Source Reliability** | Source is in approved Tier 1 or Tier 2 list | 20% |
| **Entity Quality** | Extracted entities match known political figures/orgs (confidence > 0.7) | 20% |
| **Content Originality** | No duplicate content (similarity < 0.85 to existing signals) | 15% |
| **Escalation Accuracy** | Escalation level matches severity keywords in content | 20% |

**Passing Score:** ≥ 75% overall, with no single criterion below 50%

## Usage

```bash
openclaw skill run signal-quality-grader \
  --input "path/to/tagged-signals.jsonl" \
  --output "path/to/graded-signals.jsonl" \
  --model "vllm/Qwen/Qwen3.5-397B-A17B" \
  --grader-model "smaller-model-for-cost-efficiency" \
  --max-iterations 2
```

## Input Format

```jsonl
{"id": "signal-001", "pir_tags": ["PIR-1", "PIR-5"], "entities": [...], "content": "...", "source": "...", "escalation_level": "HIGH"}
```

## Output Format

```jsonl
{
  "id": "signal-001",
  "...": "...",
  "grade": {
    "overall_score": 0.87,
    "passed": true,
    "criteria_scores": {
      "pir_relevance": 0.95,
      "source_reliability": 1.0,
      "entity_quality": 0.82,
      "content_originality": 0.78,
      "escalation_accuracy": 0.85
    },
    "feedback": "Entity confidence slightly low for 'Minister X' - consider manual verification",
    "requires_revision": false
  }
}
```

## Grading Process (LLM-as-a-Judge)

```
1. Signal processed by pir-entity-tagger → tagged signal
2. signal-quality-grader receives tagged signal
3. Grader model evaluates against rubric criteria
4. If score < 75% or any criterion < 50%:
   - Generate specific feedback per failed criterion
   - Send back to pir-entity-tagger for revision
   - Increment iteration counter
5. If iterations >= max_iterations:
   - Flag for human review
   - Output with warning
6. If passed:
   - Proceed to threshold-escalation-checker
```

## Configuration

Create/edit `~/.openclaw/workspace/.agents/skills/loop-engineering/signal-quality-grader/config.yaml`:

```yaml
rubric:
  pir_relevance:
    weight: 0.25
    min_score: 0.5
    description: "Signal must reference at least one valid PIR keyword"
  
  source_reliability:
    weight: 0.20
    min_score: 0.5
    description: "Source must be in approved Tier 1 or Tier 2 list"
  
  entity_quality:
    weight: 0.20
    min_score: 0.5
    description: "Extracted entities must match known figures/orgs with confidence > 0.7"
  
  content_originality:
    weight: 0.15
    min_score: 0.5
    description: "No duplicate content (similarity < 0.85 to existing signals)"
  
  escalation_accuracy:
    weight: 0.20
    min_score: 0.5
    description: "Escalation level must match severity keywords in content"

grading_thresholds:
  overall_pass: 0.75
  criterion_min: 0.50
  max_iterations: 2

tier_1_sources:
  - "The Star"
  - "New Straits Times"
  - "Malay Mail"
  - "Bernama"
  # ... etc

tier_2_sources:
  - "Malaysiakini"
  - "The Edge"
  - "Free Malaysia Today"
  # ... etc
```

## Revision Feedback Format

When a signal fails grading, feedback is injected back:

```json
{
  "signal_id": "signal-001",
  "verdict": "needs_revision",
  "feedback": {
    "pir_relevance": "PIR-7 tag applied but content discusses economic policy (PIR-2) - retag",
    "entity_quality": "Entity 'Datuk X' not found in known figures - verify or remove",
    "escalation_accuracy": "MEDIUM escalation but content mentions 'protest' which should be HIGH (ESC-006)"
  }
}
```

## Human-in-the-Loop Integration

Signals that fail after max_iterations:
1. Flagged with `requires_human_review: true`
2. Added to review queue
3. Human can: approve as-is, reject, or provide correction
4. Correction fed back to improve future grading

## Metrics & Monitoring

Track these metrics for Loop 4 (Hill Climbing):
- Grade pass rate by source
- Average iteration count per signal
- Most common failure criteria
- Human override rate
- Grader model consistency (compare with human grades)

## Related Skills

- `pir-entity-tagger` - Upstream, receives revision feedback
- `threshold-escalation-checker` - Downstream, receives graded signals
- `pir-tagging-auditor` - Periodic audit of grading consistency
