# pir-entity-tagger Skill

**Purpose:** Extract entities from political news signals and tag them with PIR (Priority Intelligence Requirement) codes PIR-1 through PIR-10.

**Loop Level:** Loop 1 (Agent Loop - Core Automation)

## When to Use

Use this skill when:
- Processing raw news signals from DeerFlow collection
- Need to categorize signals by intelligence priority
- Building the Signal Registry with properly tagged entries

## PIR Taxonomy

| PIR Code | Category | Keywords/Topics |
|----------|----------|-----------------|
| **PIR-1** | Government Stability | PM, cabinet, coalition, parliament, vote of confidence, government collapse |
| **PIR-2** | Economic Policy | Budget, fiscal, taxation, subsidies, inflation, economic reforms |
| **PIR-3** | Foreign Relations | Diplomacy, bilateral, ASEAN, China, US, trade agreements, territorial disputes |
| **PIR-4** | Security & Defense | Military, defense procurement, terrorism, border security, cyber threats |
| **PIR-5** | Corruption & Governance | MACC, investigations, graft, abuse of power, whistleblower |
| **PIR-6** | Social Unrest | Protests, racial tensions, religious issues, public demonstrations |
| **PIR-7** | Electoral Politics | Elections, polling, party switching, constituency, voter sentiment |
| **PIR-8** | Regulatory Changes | Laws, amendments, compliance, licensing, policy shifts |
| **PIR-9** | Corporate & Business | GLCs, major corporations, investments, bankruptcies, mergers |
| **PIR-10** | Environmental & Health | Climate, disasters, pandemics, healthcare, environmental policy |

## Usage

```bash
openclaw skill run pir-entity-tagger \
  --input "path/to/raw-signals.jsonl" \
  --output "path/to/tagged-signals.jsonl" \
  --model "vllm/Qwen/Qwen3.5-397B-A17B"
```

## Input Format

```jsonl
{"id": "signal-001", "timestamp": "2026-06-18T10:30:00Z", "source": "The Star", "title": "...", "content": "...", "url": "..."}
```

## Output Format

```jsonl
{"id": "signal-001", "timestamp": "...", "source": "...", "title": "...", "content": "...", "url": "...", "pir_tags": ["PIR-1", "PIR-5"], "entities": [{"name": "...", "type": "PERSON|ORG|LOCATION", "confidence": 0.95}], "tagging_confidence": 0.87}
```

## Implementation Notes

1. **Entity Extraction:** Use NLP to extract PERSON, ORG, LOCATION entities
2. **PIR Tagging:** Match content against PIR keyword sets (configurable in `config.yaml`)
3. **Confidence Scoring:** Assign confidence based on keyword match strength and entity clarity
4. **Multi-tag Support:** A signal can have multiple PIR tags (e.g., corruption affecting government stability = PIR-1 + PIR-5)
5. **Validation:** Cross-reference extracted entities with known political figures/orgs database

## Configuration

Create/edit `~/.openclaw/workspace/.agents/skills/loop-engineering/pir-entity-tagger/config.yaml`:

```yaml
pir_keywords:
  PIR-1: ["prime minister", "cabinet", "coalition", "parliament", "confidence vote", "government"]
  PIR-2: ["budget", "fiscal", "tax", "subsidy", "inflation", "economy"]
  # ... etc

known_entities:
  persons: ["Anwar Ibrahim", "Muhyiddin Yassin", ...]
  organizations: ["MACC", "BNM", "Parliament", ...]

min_confidence_threshold: 0.7
max_pir_tags_per_signal: 3
```

## Verification (Loop 2 Integration)

This skill should be followed by:
- `signal-quality-grader` to validate PIR tagging accuracy
- `pir-tagging-auditor` for periodic review of tagging consistency

## Related Skills

- `threshold-escalation-checker` - Next step in pipeline
- `signal-quality-grader` - Verification loop
- `deer-flow-news-collection` - Upstream data source
