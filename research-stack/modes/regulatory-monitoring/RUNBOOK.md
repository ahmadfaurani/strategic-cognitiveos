# Runbook: Regulatory & Policy Monitoring

## Overview

| Field | Value |
|-------|-------|
| **Name** | regulatory-policy-monitoring |
| **Frequency** | Weekly |
| **Mode** | Regulatory Monitoring |
| **Tools** | SearXNG, Firecrawl, DeerFlow |
| **Output** | Regulatory digest, compliance impact, deadlines |

---

## Execution Workflow

### Phase 1: Intake & Scoping

```yaml
task:
  title: "Regulatory Monitoring Digest - [Week/Date Range]"
  objective: "Track regulatory changes affecting [sector/domains]"
  priority_intelligence_requirements:
    - "What new regulations were published this week?"
    - "What compliance deadlines are approaching?"
    - "What guidance documents were issued?"
    - "What enforcement actions were taken?"
  scope:
    geography: "[Regions: US, EU, UK, etc.]"
    sector: "[Industry vertical]"
    timeframe: "Last 7 days"
    language: "English"
    source_types:
      - regulatory bodies (CISA, SEC, ICO, etc.)
      - official gazettes
      - government agencies
      - standards bodies (NIST, ISO)
      - legal analysis
    output_required: "Regulatory change digest + compliance impact + deadlines"
    handling_classification: "Internal"
    personal_data_involved: false
    review_required: true
```

### Phase 2: Research Planning

```yaml
research_plan:
  key_questions:
    - "What regulations changed this week?"
    - "What deadlines are in next 90 days?"
    - "What sectors are affected?"
    - "What actions are required?"
  source_strategy:
    primary:
      - Regulatory body websites (CISA, SEC, ICO, EDPB)
      - Official gazettes (Federal Register, EU OJ)
      - Government agency sites
    secondary:
      - Legal analysis (law firm blogs)
      - Compliance news (Regulatory Intelligence)
    official:
      - All .gov, .europa.eu, official gazettes
  query_strategy:
    - "cybersecurity regulation 2024"
    - "site:cisa.gov guidance"
    - "site:sec.gov cybersecurity"
    - "site:federalregister.gov final rule"
    - "EU AI Act update"
    - "GDPR enforcement"
  acquisition_strategy:
    - Scrape: Regulatory notices, guidance docs
    - Crawl: Agency news pages
    - Extract: Deadlines, requirements, affected entities
  verification_strategy:
    - Confirm on official source (.gov, .europa.eu)
    - Cross-reference with legal analysis
    - Verify effective dates and deadlines
  expected_outputs:
    - Regulatory change digest
    - Affected sectors summary
    - Obligations list
    - Deadlines tracker
    - Compliance impact assessment
    - Control mapping (if applicable)
  risks:
    - Misinterpreting regulatory language
    - Missing jurisdiction-specific requirements
    - Outdated information
  assumptions:
    - Official sources are authoritative
    - Legal analysis is from reputable firms
```

### Phase 3: SearXNG Discovery

**Query Set:**

| Query | Purpose | Expected Sources |
|-------|---------|------------------|
| `"final rule" cybersecurity` | New regulations | Federal Register, agency sites |
| `site:cisa.gov "guidance"` | CISA guidance | CISA |
| `site:sec.gov "cybersecurity"` | SEC rules | SEC |
| `site:ico.org.uk guidance` | ICO guidance | ICO (UK) |
| `"AI Act" EU update` | EU AI regulation | EU sites, news |
| `"GDPR" enforcement` | GDPR actions | EDPB, ICO, news |
| `"compliance deadline" 2024` | Upcoming deadlines | Various |

### Phase 4: Firecrawl Acquisition

**Acquisition Plan:**

| URL Type | Method | Extract Fields |
|----------|--------|----------------|
| Regulatory Notice | Scrape | Title, effective date, requirements |
| Guidance Document | Scrape | Summary, applicability, deadlines |
| Enforcement Action | Scrape | Violation, penalty, lessons |
| Agency News Page | Crawl | Multiple notices |

**Extraction Schema:**
```json
{
  "source_url": "",
  "title": "",
  "publisher": "",
  "retrieved_at": "",
  "published_at": "",
  "structured_json": {
    "regulation_name": "",
    "effective_date": "",
    "compliance_deadline": "",
    "affected_entities": [],
    "requirements": [],
    "penalties": ""
  }
}
```

### Phase 5: Evidence Store

**Store:**
- All raw regulatory texts
- Guidance documents
- Enforcement action notices
- Deadline metadata

### Phase 6: Analysis & Verification

**For each finding:**

```yaml
finding:
  title: "[Regulation Name] - [Key Change]"
  summary: "[2-3 sentence summary]"
  evidence:
    - source_url: "https://[agency].gov/[document]"
      supporting_excerpt: "[Direct quote]"
      relevance: "Official regulatory text"
    - source_url: "https://[lawfirm].com/analysis"
      supporting_excerpt: "[Analysis quote]"
      relevance: "Expert interpretation"
  implication: "[What this means for compliance]"
  confidence_level: "high"
  recommended_action: "[Specific compliance action]"
  verification_status: "verified"
  reviewer_status: "human-review-required"
  created_at: "2024-06-14T04:30:00Z"
```

### Phase 7: Output Generation

**Expected Outputs:**

#### 1. Regulatory Change Digest
```markdown
# Regulatory Change Digest - [Week of YYYY-MM-DD]

## New Regulations

### [Regulation Name]
- **Jurisdiction:** [Country/Region]
- **Effective Date:** YYYY-MM-DD
- **Compliance Deadline:** YYYY-MM-DD
- **Affected Entities:** [Description]
- **Summary:** [Brief overview]
- **Key Requirements:**
  1. [Requirement 1]
  2. [Requirement 2]
- **Source:** [Link] - [Confidence]

## Updated Guidance

### [Guidance Title]
- **Issuer:** [Regulatory body]
- **Updated:** YYYY-MM-DD
- **Summary of Changes:** [What changed]
- **Action Required:** [What to do]

## Enforcement Actions

### [Case Name]
- **Regulator:** [Body]
- **Entity:** [Company]
- **Violation:** [What happened]
- **Penalty:** [Amount/Action]
- **Lesson:** [Key takeaway]
```

#### 2. Affected Sectors
```markdown
# Affected Sectors Summary

| Sector | Regulations | Key Changes | Impact Level |
|--------|-------------|-------------|--------------|
| Financial | [List] | [Summary] | High/Med/Low |
| Healthcare | [List] | [Summary] | High/Med/Low |
| Technology | [List] | [Summary] | High/Med/Low |
```

#### 3. Obligations List
```markdown
# Compliance Obligations

| Obligation | Regulation | Requirement | Deadline | Status |
|------------|------------|-------------|----------|--------|
| [What] | [Regulation] | [Requirement] | YYYY-MM-DD | Not Started |
| [What] | [Regulation] | [Requirement] | YYYY-MM-DD | In Progress |
```

#### 4. Deadlines Tracker
```markdown
# Compliance Deadlines

## Upcoming (Next 90 Days)

| Deadline | Requirement | Regulation | Owner | Status |
|----------|-------------|------------|-------|--------|
| YYYY-MM-DD | [What] | [Regulation] | [Owner] | 🟢 On Track |
| YYYY-MM-DD | [What] | [Regulation] | [Owner] | 🟡 At Risk |

## Status Legend
- 🟢 On Track
- 🟡 At Risk
- 🔴 Behind
```

#### 5. Compliance Impact
```markdown
# Compliance Impact Assessment

## Executive Summary
[Brief overview of impact]

## Affected Business Units
| Unit | Impact | Key Changes |
|------|--------|-------------|
| [Unit 1] | High | [Summary] |
| [Unit 2] | Medium | [Summary] |

## Resource Requirements
- **Personnel:** [Estimate]
- **Technology:** [Tools needed]
- **External:** [Consultants/auditors]
- **Estimated Cost:** [Range]

## Risk of Non-Compliance
| Risk | Likelihood | Impact |
|------|------------|--------|
| Regulatory Penalty | Medium | High |
| Reputational Damage | Low | High |
```

#### 6. Control Mapping (if applicable)
```markdown
# Control Mapping: [Regulation] to [Framework]

| Regulatory Requirement | [Framework] Control | Gap | Priority |
|------------------------|---------------------|-----|----------|
| [Req 1] | [Control ID] | Yes/No | High |
| [Req 2] | [Control ID] | Yes/No | Medium |
```

---

## Skills Used

| Skill | Category | Purpose |
|-------|----------|---------|
| `regulatory-monitoring` | Domain | Regulatory analysis |
| `freshness-checking` | Verification | Date/recency assessment |
| `executive-brief-template` | Reporting | Brief formatting |

---

## Governance Controls

| Control | Application |
|---------|-------------|
| **Official source priority** | Always verify on .gov/.europa.eu |
| **Date preservation** | Publication + retrieval dates required |
| **Legal review** | All regulatory interpretations need legal review |
| **No speculation** | Mark interpretations clearly |

---

## Human Review Triggers

**All regulatory digests require human review.**

**Escalate immediately if:**
- New regulation with imminent deadline (<30 days)
- High penalty for non-compliance
- Conflicting interpretations across sources
- Sector-specific impact requiring business decision

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2024-06-14 | Initial runbook |
