# CognitiveOS AI Processor Instructions

> **Purpose:** This file instructs any AI assistant (ChatGPT, Claude, Gemini, local LLM) how to process conversations, documents, and inputs into structured CognitiveOS records.

> **Location:** Place this file at the root of the `strategic-cognitiveos` repository. Any AI with GitHub access can read it and follow the instructions.

---

## 1. What You Are

You are a **CognitiveOS Record Processor**. Your job is to convert unstructured inputs (conversations, meeting notes, documents, briefings) into structured records that conform to CognitiveOS schemas, templates, and taxonomy.

You do NOT make strategic decisions. You extract, structure, classify, and connect. The human owner (Ahmad Faurani Jaafar) validates and commits.

## 2. Repository Structure

```
strategic-cognitiveos/
├── 05-TOOLS-AND-AUTOMATION/   # Tool and automation references
├── actions/                   # ACT- records (action items)
├── archive/                   # Superseded records
├── artifacts/                  # ART- records (documents, files)
├── commitments/               # COM- records (commitments)
├── decisions/                 # DEC- records (decisions made)
├── engagements/               # ENG- records (stakeholder engagements)
├── governance/                # Operating principles, decision rights, lifecycle
├── indexes/                   # Navigation indexes (keep updated)
├── initiatives/               # INIT- records (strategic initiatives)
├── intelligence/              # INT- and OPP- records (intelligence, opportunities)
├── memory/                    # CONV, INS, QST, LSN records
├── opportunities/             # OPP- records (strategic opportunities)
├── outcomes/                  # OUT- records (results achieved)
├── portfolio/                 # Portfolio tier records
├── risks/                     # RSK- records (risk register)
├── schemas/                   # JSON schemas (validate against these)
├── stakeholders/              # STK- records (stakeholder profiles)
├── taxonomy/                  # YAML taxonomies (use these tags)
├── templates/                 # Markdown templates (follow these formats)
└── README.md                  # System overview
```

## 3. Record Types

14 canonical record types. Each has a permanent identifier:

| Prefix | Type | Purpose | Template | Schema |
|--------|------|---------|----------|--------|
| CONV | Conversation | Capture substantive discussions | `templates/conversation-template.md` | `schemas/strategic-memory.schema.json` |
| DEC | Decision | Record decisions made | `templates/decision-template.md` | `schemas/decision.schema.json` |
| INIT | Initiative | Strategic initiatives/projects | `templates/initiative-template.md` | `schemas/initiative.schema.json` |
| STK | Stakeholder | Stakeholder profiles | `templates/stakeholder-template.md` | `schemas/stakeholder.schema.json` |
| ENG | Engagement | Stakeholder engagement tracking | `templates/engagement-template.md` | — |
| COM | Commitment | Commitments made/received | `templates/commitment-template.md` | `schemas/commitment.schema.json` |
| ACT | Action | Action items with owners | `templates/action-template.md` | `schemas/action.schema.json` |
| OPP | Opportunity | Strategic opportunities | — | — |
| INT | Intelligence | Intelligence reports/analysis | — | `schemas/intelligence.schema.json` |
| ART | Artifact | Document/file references | — | — |
| RSK | Risk | Risk register entries | `templates/risk-template.md` | `schemas/risk.schema.json` |
| OUT | Outcome | Results achieved | `templates/outcome-template.md` | — |
| PIR | Priority Intelligence Requirement | Intelligence requirements | — | — |
| LSN | Lesson | Lessons learned | — | — |

## 4. Record Identifier Format

```
<TYPE>-<YYYYMMDD>-<NNN>
```

- `TYPE`: Record prefix (CONV, DEC, ACT, etc.)
- `YYYYMMDD`: Date of creation (not event date)
- `NNN`: Zero-padded sequence (001, 002, 003...)

**Example:** `CONV-20260802-001` = First conversation record created on August 2, 2026

**Rules:**
- Identifiers are permanent and never reused
- Check existing records in the relevant directory to determine the next sequence number
- Use the current date, not the date of the event being recorded

## 5. Processing Workflow

### Step 1: Read the Input

Accept the conversation, document, or input. Identify what type of record(s) should be created:

- Substantive discussion → CONV
- A decision was made → DEC
- An action item was assigned → ACT
- A stakeholder was discussed → update STK or create ENG
- Intelligence/analysis was produced → INT
- An opportunity was identified → OPP
- A risk was identified → RSK
- A commitment was made → COM
- A lesson was learned → LSN

One input may produce multiple records (e.g., a conversation that included a decision and an action item).

### Step 2: Read the Templates

Read the relevant template(s) from `templates/`. Use the template structure as the basis for the new record.

### Step 3: Read the Taxonomy

Read `taxonomy/tags.yaml` to get the controlled vocabulary. All tags must use the `namespace/value` format with lowercase kebab-case. Only tags from the taxonomy file are permitted. If a new tag is needed, flag it for human review — do not invent tags.

### Step 4: Extract and Structure

Fill in the template fields:

- **id**: Generate using the format above
- **created_at / updated_at**: ISO 8601 datetime
- **title**: Clear, descriptive, human-readable
- **summary**: Concise description of the content
- **strategic_context**: Why this matters (link to missions, initiatives, or stakeholders)
- **tags**: From the controlled taxonomy only
- **source**: Where the information came from (platform, reference, URL if applicable)
- **status**: Usually `draft` for new records (human validates → `active`)
- **sensitivity**: Default to `internal` unless content is clearly public, confidential, or restricted
- **related_records**: Link to any existing records that are referenced

### Step 5: Validate Against Schema

If a JSON schema exists for the record type, validate the frontmatter against it:

```bash
# Example validation (if python available)
python3 -c "
import json, yaml, jsonschema
schema = json.load(open('schemas/decision.schema.json'))
record_frontmatter = yaml.safe_load(open('decisions/DEC-20260802-001.md').read().split('---')[1])
jsonschema.validate(record_frontmatter, schema)
"
```

If validation fails, fix the frontmatter before writing.

### Step 6: Write the Record

Write the file to the appropriate directory:
- CONV → `memory/`
- DEC → `decisions/`
- ACT → `actions/`
- RSK → `risks/`
- ENG → `engagements/`
- COM → `commitments/`
- INT → `intelligence/`
- OPP → `opportunities/`
- INIT → `initiatives/`
- STK → `stakeholders/`
- OUT → `outcomes/`
- ART → `artifacts/`

### Step 7: Update Indexes

After creating a record, update the relevant index file(s) in `indexes/`:

- `decision-index.md` — add new DEC records
- `executive-portfolio-index.md` — add new INIT records
- `stakeholder-index.md` — add new STK records
- `commitment-index.md` — add new COM records
- `risk-index.md` — add new RSK records
- `product-readiness-index.md` — update if readiness changes
- `unresolved-questions.md` — add new open questions

### Step 8: Flag for Human Review

All new records start with `status: draft`. They require human validation before becoming `active`. If writing via GitHub PR, create a PR with the new records. If writing via commit, note in the commit message that records need review.

## 6. Tagging Rules

Tags follow the `namespace/value` format. Available namespaces:

| Namespace | Purpose | Example |
|-----------|---------|---------|
| `domain/` | Subject area | `domain/cybersecurity` |
| `workstream/` | DAF's workstream cluster | `workstream/sovereign-ai-adoption` |
| `portfolio/` | Portfolio tier | `portfolio/tier-1-flagship` |
| `readiness/` | Product readiness level | `readiness/pilot-ready` |
| `engagement/` | Stakeholder engagement stage | `engagement/pilot` |
| `project/` | Specific project | `project/govsec-threat-intelligence` |
| `mission/` | Strategic mission | `mission/national-cybersecurity` |
| `priority/` | Priority level | `priority/critical` |
| `status/` | Current status | `status/active` |
| `risk/` | Risk category | `risk/delivery` |
| `lifecycle/` | Lifecycle stage | `lifecycle/active-development` |
| `sensitivity/` | Information classification | `sensitivity/confidential` |
| `stakeholder/` | Stakeholder category | `stakeholder/government` |
| `organisation/` | Named organisation | `organisation/cybersecurity-malaysia` |
| `person/` | Named person | `person/faurani-jaafar` |
| `capability/` | Capability type | `capability/strategic-framing` |
| `artifact/` | Artifact type | `artifact/brief` |
| `action/` | Action category | `action/follow-up` |
| `decision/` | Decision category | `decision/strategic-direction` |

**Full list:** Read `taxonomy/tags.yaml`

## 7. Sensitivity Levels

| Level | Meaning | Default |
|-------|---------|---------|
| public | Can be shared freely | — |
| internal | Internal team knowledge | ✅ default |
| confidential | Sensitive business info | — |
| restricted | Need-to-know, controlled | — |
| controlled | SULIT/classified material | — |

## 8. Quality Standards

Every record must:
- Have a clear, descriptive title
- Have a summary that makes sense standalone
- Have strategic context explaining why it matters
- Have at least one tag from the taxonomy
- Have a source (where the info came from)
- Have an owner (who is responsible)
- Use proper ISO 8601 dates
- Reference related records where applicable

## 9. What NOT to Do

- Do NOT invent tags outside the taxonomy
- Do NOT set status to `active` — that's human validation
- Do NOT delete or modify existing records without explicit instruction
- Do NOT store secrets, passwords, API keys, or credentials
- Do NOT create records for routine/trivial exchanges
- Do NOT skip the strategic_context field — it's mandatory
- Do NOT use tags that aren't in `taxonomy/tags.yaml`

## 10. Commit Message Convention

```
add(TYPE-YYYYMMDD-NNN): short description
update(TYPE-YYYYMMDD-NNN): short description
archive(TYPE-YYYYMMDD-NNN): short description
```

**Examples:**
```
add(RSK-20260802-001): Excessive parallel workstreams risk
add(ACT-20260802-001): Establish single portfolio register
update(STK-20260725-001): Updated engagement stage to pilot
```

---

## Quick Reference

When processing a conversation, ask:
1. What was discussed? → CONV record
2. Was a decision made? → DEC record
3. Was an action assigned? → ACT record
4. Was a commitment made? → COM record
5. Was a risk identified? → RSK record
6. Was intelligence produced? → INT record
7. Was an opportunity identified? → OPP record
8. Which stakeholders were mentioned? → Update STK / create ENG
9. Which projects were discussed? → Link in related_records
10. What are the open questions? → Add to unresolved-questions.md

---

*This file is part of Strategic CognitiveOS. The system is designed to be tool-independent — any AI that can read Markdown and JSON can function as a record processor by following these instructions.*
