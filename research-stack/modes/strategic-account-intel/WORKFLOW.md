# Strategic Account Intelligence Mode

## Purpose
Deep research and preparation for target accounts, stakeholder meetings, and enterprise account planning.

## Trigger Patterns
- "Research [company] for meeting"
- "Account brief for [target]"
- "Stakeholder prep [name/company]"
- "Public agency briefing [agency]"
- "Meeting prep [company]"
- "Account planning [enterprise]"

## Workflow Steps

### 1. Intake & Scoping

```yaml
task:
  title: "Strategic Account Intelligence: [Company Name]"
  objective: "Prepare comprehensive intelligence brief for upcoming engagement"
  priority_intelligence_requirements:
    - "What are their current strategic priorities?"
    - "Who are the key decision makers and influencers?"
    - "What challenges/pain points are they facing?"
    - "What is our existing relationship history?"
    - "What timing/windows of opportunity exist?"
  scope:
    geography: "Global / [Specific Region]"
    sector: "[Industry vertical]"
    timeframe: "Last 12 months + recent news"
    language: "English"
    source_types:
      - official_website
      - press_releases
      - financial_reports
      - news_media
      - linkedin
      - job_postings
      - industry_analysis
    output_required: "Account intelligence brief + opportunity map"
    handling_classification: "Internal"
    personal_data_involved: true
    review_required: true
```

### 2. Research Planning

```yaml
research_plan:
  key_questions:
    - "What is the company's current strategic direction?"
    - "Who holds budget/approval authority?"
    - "What initiatives are they investing in?"
    - "What challenges are mentioned in earnings/reports?"
    - "Who have they partnered with recently?"
    - "What is their technology stack?"
  source_strategy:
    primary:
      - Company website (about, news, investor relations)
      - LinkedIn company page
      - Executive LinkedIn profiles
    secondary:
      - News articles (last 12 months)
      - Industry analyst reports
      - Competitor mentions
    official:
      - SEC filings (if public)
      - Annual reports
      - Press releases
    commercial:
      - Crunchbase
      - Gartner/Forrester (if available)
      - Industry databases
    technical:
      - GitHub org (if applicable)
      - Technology blog
      - StackShare
  query_strategy:
    - "[company] strategic priorities 2024"
    - "[company] earnings call Q4 2024"
    - "[company] partnership announcement"
    - "[company] digital transformation"
    - "[CEO name] [company] interview"
    - "[company] hiring [role type]"
    - "[company] technology stack"
    - "site:linkedin.com/company/[company]"
    - "site:[company].com/news"
  acquisition_strategy:
    - Scrape: Company news page, investor relations
    - Crawl: Executive bios, org structure
    - Extract: Financial metrics, strategic initiatives
    - Screenshot: Org charts, strategy visuals (if available)
  verification_strategy:
    - Cross-reference press releases with news coverage
    - Verify executive roles via LinkedIn + company site
    - Confirm financials via official filings
  expected_outputs:
    - Account intelligence brief
    - Stakeholder map
    - Opportunity map
    - Talking points
  risks:
    - Outdated information
    - Personal data handling (executive names/roles)
    - Speculative analysis marked as fact
  assumptions:
    - Public information is accurate
    - Recent news reflects current priorities
```

### 3. SearXNG Discovery

**Query Categories:**

**Company Overview:**
```
"[company] overview 2024"
"[company] revenue employees"
"[company] headquarters locations"
site:crunchbase.com "[company]"
site:bloomberg.com "[company]"
```

**Strategic Direction:**
```
"[company] strategic priorities 2024"
"[company] transformation initiative"
"[company] investment focus"
"[company] annual report 2024"
```

**Leadership & Stakeholders:**
```
"[company] CEO [name]"
"[company] CTO [name]"
"[company] executive team"
site:linkedin.com/in "[company] [title]"
```

**Recent News:**
```
"[company] news 2024"
"[company] partnership 2024"
"[company] acquisition 2024"
"[company] product launch 2024"
```

**Financial/Performance:**
```
"[company] earnings Q4 2024"
"[company] stock performance"
"[company] investor presentation"
site:sec.gov "[company]" (for US public companies)
```

**Challenges/Pain Points:**
```
"[company] challenges 2024"
"[company] layoffs"
"[company] restructuring"
"[company] competitive pressure"
```

**Technology Stack:**
```
"[company] technology stack"
"[company] cloud migration"
"[company] digital transformation"
site:stackshare.io "[company]"
```

### 4. Firecrawl Acquisition

**Target Pages:**

| Page Type | Method | Purpose |
|-----------|--------|---------|
| Company About | Scrape | Overview, mission, leadership |
| News/Press | Crawl | Recent announcements, priorities |
| Investor Relations | Crawl | Financials, strategy, risks |
| Executive Bios | Scrape | Stakeholder backgrounds |
| LinkedIn Company | Scrape | Employee count, updates |
| Executive LinkedIn | Scrape | Background, tenure, connections |
| News Articles | Scrape | Third-party perspective |
| Analyst Reports | Extract | Industry positioning |

**Extraction Schema:**
```json
{
  "source_url": "",
  "canonical_url": "",
  "title": "",
  "publisher": "",
  "retrieved_at": "",
  "published_at": "",
  "content_markdown": "",
  "structured_json": {
    "company_name": "",
    "executives": [],
    "strategic_initiatives": [],
    "financial_metrics": {},
    "recent_news": []
  },
  "screenshot_path": "",
  "extraction_status": "success|partial|failed",
  "notes": ""
}
```

### 5. Analysis Framework

#### Company Profile Dimensions
- **Overview:** Size, locations, revenue, employees
- **Industry/Vertical:** Primary markets, segments
- **Business Model:** How they make money
- **Strategic Priorities:** Current focus areas
- **Technology Posture:** Digital maturity, stack
- **Recent Movements:** M&A, partnerships, launches
- **Challenges:** Headwinds, competitive pressures

#### Stakeholder Mapping
| Name | Role | Tenure | Background | Influence | Priority |
|------|------|--------|------------|-----------|----------|
| [Name] | [Title] | [Years] | [Previous] | High/Med/Low | Decision Maker/Influencer/User |

#### Opportunity Mapping
| Opportunity | Strategic Fit | Timing | Budget Signal | Competition | Priority |
|-------------|---------------|--------|---------------|-------------|----------|
| [Opp 1] | High/Med/Low | Q1/Q2/Q3/Q4 | Yes/No/Unclear | [Competitors] | High/Med/Low |

#### Engagement Narrative
- **Current State:** Where they are now
- **Desired State:** Where they want to be
- **Gap:** What's missing
- **Our Role:** How we help close the gap

### 6. Output Generation

#### Account Intelligence Brief
```markdown
# Account Intelligence Brief: [Company Name]

**Prepared:** YYYY-MM-DD
**Classification:** Internal
**Review Required:** Yes/No

## Executive Summary
[2-3 sentence overview of company and opportunity]

## Company Overview
| Attribute | Details |
|-----------|---------|
| Headquarters | [Location] |
| Founded | [Year] |
| Employees | [Count] |
| Revenue | [Amount] |
| Industry | [Vertical] |
| Website | [URL] |

## Strategic Priorities (2024)
1. **[Priority 1]:** [Description + source]
2. **[Priority 2]:** [Description + source]
3. **[Priority 3]:** [Description + source]

## Recent Movements (Last 12 Months)
| Date | Type | Summary | Implication |
|------|------|---------|-------------|
| YYYY-MM | Partnership | [Details] | [Implication] |
| YYYY-MM | Product Launch | [Details] | [Implication] |
| YYYY-MM | Leadership Change | [Details] | [Implication] |

## Financial/Performance Snapshot
- **Revenue:** [Amount, YoY change]
- **Growth Areas:** [Segments growing]
- **Challenges:** [Headwinds mentioned]
- **Investment Focus:** [Where spending]

## Technology Posture
- **Current Stack:** [Key technologies]
- **Digital Maturity:** [Assessment]
- **Recent Initiatives:** [Cloud, transformation, etc.]
- **Gaps/Needs:** [Implied or stated]

## Stakeholder Map
| Name | Title | Tenure | Background | Influence | Notes |
|------|-------|--------|------------|-----------|-------|
| [Name] | [Title] | [X years] | [Previous co] | High | Decision maker |
| [Name] | [Title] | [X years] | [Previous co] | Medium | Influencer |

## Opportunity Map
| Opportunity | Strategic Fit | Timing | Budget Signal | Our Fit | Priority |
|-------------|---------------|--------|---------------|---------|----------|
| [Opp 1] | High | Q2 2024 | Confirmed | Strong | High |
| [Opp 2] | Medium | H2 2024 | Unclear | Moderate | Medium |

## Competitive Landscape
- **[Competitor 1]:** [Relationship/status]
- **[Competitor 2]:** [Relationship/status]
- **Our Differentiation:** [Key points]

## Recommended Talking Points
### For [Stakeholder 1]
- "[Talking point aligned to their priority]"
- "[Reference to recent company news]"
- "[Specific value prop for their challenge]"

### For [Stakeholder 2]
- "[Talking point aligned to their priority]"
- "[Reference to recent company news]"
- "[Specific value prop for their challenge]"

## Risks & Considerations
- [Risk 1: e.g., Budget constraints]
- [Risk 2: e.g., Incumbent vendor]
- [Risk 3: e.g., Timing misalignment]

## Next Steps
1. [Action item]
2. [Action item]
3. [Action item]

## Sources & Confidence
| Source | Type | Confidence |
|--------|------|------------|
| [Source 1] | Official | High |
| [Source 2] | News | Medium |
| [Source 3] | Third-party | Medium |
```

#### Public Stakeholder Context (for Public Sector)
```markdown
# Public Agency Brief: [Agency Name]

**Prepared:** YYYY-MM-DD
**Agency Type:** [Federal/State/Local]
**Jurisdiction:** [Geography]

## Agency Mission
[Official mission statement]

## Leadership
| Name | Title | Appointed | Background |
|------|-------|-----------|------------|
| [Name] | [Title] | [Date] | [Previous role] |

## Strategic Plan
- **[Goal 1]:** [Description]
- **[Goal 2]:** [Description]
- **[Goal 3]:** [Description]

## Budget & Funding
- **Annual Budget:** [Amount]
- **Key Funding Sources:** [Grants, appropriations]
- **Funding Priorities:** [Areas of investment]

## Recent Initiatives
| Initiative | Status | Timeline | Budget |
|------------|--------|----------|--------|
| [Initiative 1] | Active | 2024-2025 | $XM |
| [Initiative 2] | Planning | 2025 | $XM |

## Procurement Patterns
- **Typical Process:** [RFP, cooperative, etc.]
- **Cycle Timing:** [When budgets approved]
- **Decision Criteria:** [Evaluation factors]

## Relevant Contacts
| Name | Role | Portfolio | Contact Method |
|------|------|-----------|----------------|
| [Name] | [Title] | [Area] | [Email/Phone] |

## Political/Policy Context
- **[Policy 1]:** [Impact on agency]
- **[Policy 2]:** [Impact on agency]

## Engagement Recommendations
- [Approach recommendation]
- [Timing consideration]
- [Key messaging]
```

#### Engagement Narrative
```markdown
# Engagement Narrative: [Company/Agency]

## Current State
[Where they are today - challenges, constraints, context]

## Desired State
[Where they want to be - goals, aspirations, mandates]

## The Gap
[What's missing - capabilities, resources, timing]

## Our Role
[How we help close the gap - specific value proposition]

## Proof Points
- [Customer story 1 - similar situation]
- [Customer story 2 - similar situation]
- [Capability demonstration]

## Call to Action
[Specific next step we're recommending]
```

## Confidence Scoring

| Score | Criteria |
|-------|----------|
| High | Official sources (company site, filings, press releases) |
| Medium | Reputable news, analyst reports, LinkedIn verified |
| Low | Unverified third-party, speculation, outdated sources |

## Personal Data Handling

⚠️ **Important:** This mode often involves executive names, roles, and backgrounds.

- **Collect only:** Name, title, tenure, public background
- **Do not collect:** Personal contact info, private details, family info
- **Retention:** Review and purge after 12 months or engagement ends
- **Classification:** Internal - not for external distribution

## Skill Library Entries
- `account/target-account-research`
- `account/stakeholder-prep`
- `account/public-agency-brief`
- `account/enterprise-planning`
- `account/meeting-prep`

## Integration Points
- CRM (Salesforce, HubSpot) - account records
- Sales enablement platforms
- Meeting scheduling tools
- Account-based marketing platforms
