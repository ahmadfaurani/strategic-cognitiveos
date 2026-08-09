# Runbook: Strategic Account Intelligence Pack

## Overview

| Field | Value |
|-------|-------|
| **Name** | strategic-account-intelligence-pack |
| **Frequency** | Per meeting / ad hoc |
| **Mode** | Strategic Account Intelligence |
| **Tools** | SearXNG, Firecrawl, DeerFlow |
| **Output** | Account brief, stakeholder context, talking points |

---

## Execution Workflow

### Phase 1: Intake & Scoping

```yaml
task:
  title: "Strategic Account Intelligence: [Company Name]"
  objective: "Prepare comprehensive intelligence for [meeting type] with [company]"
  priority_intelligence_requirements:
    - "What are their current strategic priorities?"
    - "Who are the key stakeholders and decision makers?"
    - "What technology initiatives are they pursuing?"
    - "What challenges or pain points are they facing?"
    - "What is our existing relationship history?"
  scope:
    geography: "[Region]"
    sector: "[Industry vertical]"
    timeframe: "Last 12 months + current state"
    language: "English"
    source_types:
      - company website (about, news, investor relations)
      - LinkedIn (company + executives)
      - news media
      - industry analysis
      - job postings (signals hiring priorities)
    output_required: "Organization profile + opportunity map + talking points"
    handling_classification: "Internal"
    personal_data_involved: true
    review_required: true
```

### Phase 2: Research Planning

```yaml
research_plan:
  key_questions:
    - "What is the company's strategic direction?"
    - "Who holds budget/approval authority?"
    - "What initiatives are they investing in?"
    - "What challenges are mentioned in earnings/reports?"
    - "Who are our contacts and what are their backgrounds?"
  source_strategy:
    primary:
      - Company website (news, investor relations, about)
      - LinkedIn company page
      - Executive LinkedIn profiles
    secondary:
      - News articles (last 12 months)
      - Industry analyst reports
      - Job postings (signals priorities)
    official:
      - SEC filings (if public)
      - Annual reports
      - Press releases
  query_strategy:
    - "[company] strategic priorities 2024"
    - "[company] earnings call Q4 2024"
    - "[company] partnership announcement"
    - "[company] digital transformation"
    - "[CEO name] [company] interview"
    - "site:linkedin.com/company/[company]"
    - "site:[company].com/news"
  acquisition_strategy:
    - Scrape: Company news, investor relations, about
    - Crawl: Executive bios, leadership pages
    - Extract: Financial metrics, strategic initiatives
  verification_strategy:
    - Cross-reference press releases with news
    - Verify executive roles via LinkedIn + company site
    - Confirm financials via official filings
  expected_outputs:
    - Organization profile
    - Public initiatives summary
    - Technology priorities
    - Opportunity map
    - Stakeholder context
    - Recommended talking points
  risks:
    - Outdated information
    - Personal data handling (executive names/roles)
    - Speculative analysis marked as fact
  assumptions:
    - Public information is accurate
    - Recent news reflects current priorities
```

### Phase 3: SearXNG Discovery

**Query Set:**

| Query | Purpose | Expected Sources |
|-------|---------|------------------|
| `"[company]" overview` | Company basics | Website, Crunchbase |
| `"[company]" strategic priorities` | Strategy | Press releases, news |
| `"[company]" earnings` | Financial performance | Investor relations |
| `"[company]" partnership` | Business developments | News, PR |
| `"[company]" technology` | Tech initiatives | News, job postings |
| `site:linkedin.com/company "[company]"` | Company profile | LinkedIn |
| `"[CEO/executive name]" [company]` | Leadership info | News, LinkedIn |

### Phase 4: Firecrawl Acquisition

**Acquisition Plan:**

| URL Type | Method | Extract Fields |
|----------|--------|----------------|
| Company About | Scrape | Overview, mission, leadership |
| News/Press | Crawl | Recent announcements |
| Investor Relations | Crawl | Financials, strategy |
| Executive Bios | Scrape | Backgrounds, tenure |
| LinkedIn Company | Scrape | Employee count, updates |
| Job Postings | Scrape | Hiring priorities, skills needed |

### Phase 5: Evidence Store

**Store:**
- All raw Firecrawl outputs
- Source metadata
- Personal data flags (for retention tracking)

### Phase 6: Analysis & Verification

**For each finding:**

```yaml
finding:
  title: "[Company] Strategic Priority: [Initiative]"
  summary: "[2-3 sentence summary]"
  evidence:
    - source_url: "https://[company]/news/[article]"
      supporting_excerpt: "[Direct quote]"
      relevance: "Official statement of priority"
    - source_url: "https://news.site/[article]"
      supporting_excerpt: "[Direct quote]"
      relevance: "Third-party confirmation"
  implication: "[What this means for our engagement]"
  confidence_level: "high|medium|low"
  recommended_action: "[Specific action]"
  verification_status: "verified|pending"
  reviewer_status: "human-review-required"
  created_at: "2024-06-14T04:30:00Z"
```

### Phase 7: Output Generation

**Expected Outputs:**

#### 1. Organization Profile
```markdown
# Organization Profile: [Company Name]

## Overview
| Attribute | Details |
|-----------|---------|
| Headquarters | [Location] |
| Founded | [Year] |
| Employees | [Count] |
| Revenue | [Amount] |
| Industry | [Vertical] |
| Website | [URL] |

## Business Model
[How they make money, key products/services]

## Market Position
[Competitive position, market share if known]

## Recent Performance
[Financial highlights, growth trends]
```

#### 2. Public Initiatives
```markdown
# Public Initiatives: [Company]

## Strategic Priorities (2024)
1. **[Priority 1]:** [Description + source]
2. **[Priority 2]:** [Description + source]
3. **[Priority 3]:** [Description + source]

## Recent Announcements (Last 90 Days)
| Date | Type | Summary | Implication |
|------|------|---------|-------------|
| YYYY-MM | Partnership | [Details] | [Implication] |
| YYYY-MM | Product | [Details] | [Implication] |
| YYYY-MM | Leadership | [Details] | [Implication] |
```

#### 3. Technology Priorities
```markdown
# Technology Priorities: [Company]

## Current Stack
- **Cloud:** [AWS/Azure/GCP/Multi]
- **Key Technologies:** [List]
- **Recent Investments:** [Areas of spending]

## Digital Transformation
[Initiatives mentioned in public sources]

## Hiring Signals
[Roles they're hiring for indicates priorities]
```

#### 4. Opportunity Map
```markdown
# Opportunity Map: [Company]

| Opportunity | Strategic Fit | Timing | Budget Signal | Priority |
|-------------|---------------|--------|---------------|----------|
| [Opp 1] | High | Q2 2024 | Confirmed | High |
| [Opp 2] | Medium | H2 2024 | Indicated | Medium |

## Entry Points
- [Initiative 1] → [Our solution area]
- [Initiative 2] → [Our solution area]
```

#### 5. Stakeholder Context
```markdown
# Stakeholder Context

## Decision Makers
| Name | Title | Tenure | Background | Influence |
|------|-------|--------|------------|-----------|
| [Name] | [Title] | [X yrs] | [Previous] | High |

## Our Contacts
| Name | Title | Relationship | Last Contact |
|------|-------|--------------|--------------|
| [Name] | [Title] | [Warm/Warm-Cold] | [Date] |

## Additional Stakeholders to Identify
- [Role 1] - [Why important]
- [Role 2] - [Why important]
```

#### 6. Recommended Talking Points
```markdown
# Talking Points: [Company] Meeting

## For [Stakeholder 1]
### Opening
- "[Personalized opening based on their background]"

### Strategic Alignment
- "I noticed [company] is prioritizing [initiative]..."
- "This aligns with [our capability]..."

### Value Proposition
- "[Specific value prop for their challenge]"

### Proof Points
- "[Relevant customer story]"

### Questions to Ask
- "[Question 1 to uncover needs]"
- "[Question 2 to understand timeline]"

## For [Stakeholder 2]
[Same structure]

## Common Objections & Responses
| Objection | Response |
|-----------|----------|
| "[Objection 1]" | "[Response]" |
| "[Objection 2]" | "[Response]" |
```

---

## Skills Used

| Skill | Category | Purpose |
|-------|----------|---------|
| `strategic-account-intelligence` | Domain | Account research methodology |
| `account-brief-template` | Reporting | Brief formatting |
| `source-ranking-rules` | Verification | Authority assessment |
| `privacy-controls` | Governance | Personal data handling |

---

## Governance Controls

| Control | Application |
|---------|-------------|
| **Personal data minimization** | Collect only work emails, titles, public info |
| **Source URL preservation** | All findings must cite sources |
| **No private data** | No personal emails, phones, family info |
| **Retention limit** | 12 months or engagement end |
| **Human review** | All briefs require review before meeting |

---

## Human Review Triggers

**All account intelligence briefs require human review before use.**

**Escalate immediately if:**
- Sensitive executive information found
- Negative findings about company/leadership
- Competitive intelligence that could be misconstrued
- Personal data beyond work contact info

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2024-06-14 | Initial runbook |
