# Media Registry & Communications Intelligence Mode

## Purpose
Build and enrich media contact databases, map journalist beats, discover outlets, and support PR targeting efforts.

## Trigger Patterns
- "Build media list for [topic]"
- "Journalist research [beat]"
- "Outlet mapping [sector]"
- "Masthead discovery [publication]"
- "PR targeting [industry]"
- "Media contacts [region]"

## Workflow Steps

### 1. Intake & Scoping

```yaml
task:
  title: "Media Registry: [Topic/Sector]"
  objective: "Build comprehensive media contact list for PR targeting"
  priority_intelligence_requirements:
    - "Which outlets cover [topic]?"
    - "Who are the key journalists?"
    - "What are their beats and interests?"
    - "What are contact methods?"
    - "What is outlet reach and relevance?"
  scope:
    geography: "[Countries/Regions]"
    sector: "[Industry vertical]"
    timeframe: "Current (active journalists)"
    language: "English"
    source_types:
      - publication_websites
      - masthead_pages
      - journalist_bylines
      - linkedin
      - twitter
      - media_databases
    output_required: "Media registry table + outlet tracker + engagement brief"
    handling_classification: "Internal"
    personal_data_involved: true
    review_required: true
```

### 2. Research Planning

```yaml
research_plan:
  key_questions:
    - "Which outlets cover our sector?"
    - "Who writes about [topic]?"
    - "What are journalist beats?"
    - "How do we contact them?"
    - "What is outlet circulation/reach?"
  source_strategy:
    primary:
      - Publication websites (masthead, about pages)
      - Journalist byline pages
      - LinkedIn profiles
      - Twitter/X profiles
    secondary:
      - Media databases (if available)
      - Industry association media lists
      - Press release distribution analytics
    official:
      - Publication official sites
      - Verified social accounts
    commercial:
      - Cision
      - Meltwater
      - Muck Rack
      - MuckRack free profiles
  query_strategy:
    - "[topic] journalist"
    - "[sector] reporter [publication]"
    - "[beat] editor"
    - "site:[publication].com masthead"
    - "site:linkedin.com \"[publication]\" journalist"
    - "site:twitter.com \"[publication]\" reporter"
    - "\"writes about\" [topic]"
    - "\"covers\" [sector]"
  acquisition_strategy:
    - Scrape: Masthead pages, journalist bios
    - Crawl: Publication section pages
    - Extract: Names, titles, beats, contacts
    - Screenshot: Org charts (if useful)
  verification_strategy:
    - Cross-reference LinkedIn + publication site
    - Verify recent bylines
    - Confirm contact info from multiple sources
  expected_outputs:
    - Media registry table
    - Outlet coverage tracker
    - Collection heartbeat report
    - Source confidence scoring
    - PR engagement brief
  risks:
    - Outdated contact information
    - Personal data handling (names, emails, social)
    - Journalist preference misinterpretation
  assumptions:
    - Publication sites are current
    - LinkedIn profiles are active
    - Recent bylines indicate active coverage
```

### 3. SearXNG Discovery

**Query Categories:**

**Outlet Discovery:**
```
"[sector] news outlets"
"[industry] publications"
"[topic] media coverage"
"top [sector] blogs"
"[sector] trade publications"
"[region] business news"
```

**Journalist Discovery:**
```
"[topic] journalist"
"[sector] reporter"
"[beat] editor"
"[topic] writer"
"[publication] reporter [topic]"
```

**Masthead Discovery:**
```
site:[publication].com "masthead"
site:[publication].com "editorial team"
site:[publication].com "about us"
site:[publication].com "contact"
```

**Social/LinkedIn:**
```
site:linkedin.com "[publication]" journalist
site:linkedin.com "[publication]" editor
site:twitter.com "[publication]" reporter
"[journalist name] [topic]"
```

**Media Databases:**
```
site:muckrack.com "[topic]"
site:mediabistro.com "[sector]"
```

### 4. Firecrawl Acquisition

**Target Pages:**

| Page Type | Method | Purpose |
|-----------|--------|---------|
| Masthead Page | Scrape | Full editorial team |
| Journalist Bio | Scrape | Individual profile, contact |
| Byline Archive | Crawl | Recent articles, beat confirmation |
| Publication About | Scrape | Outlet overview, audience |
| LinkedIn Profile | Scrape | Background, connections |
| Twitter Profile | Scrape | Recent topics, contact preference |

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
    "journalist_name": "",
    "title": "",
    "publication": "",
    "beat": [],
    "email": "",
    "twitter": "",
    "linkedin": "",
    "recent_articles": [],
    "coverage_areas": [],
    "contact_preference": ""
  },
  "screenshot_path": "",
  "extraction_status": "success|partial|failed",
  "notes": ""
}
```

### 5. Analysis Framework

#### Outlet Classification
| Tier | Description | Examples |
|------|-------------|----------|
| Tier 1 | National/Global, High Reach | WSJ, FT, Reuters, Bloomberg |
| Tier 2 | Regional/Specialized | Industry trades, regional business |
| Tier 3 | Blogs/Niche | Independent, specialist writers |

#### Journalist Beat Mapping
| Journalist | Outlet | Primary Beat | Secondary Beat | Coverage Frequency |
|------------|--------|--------------|----------------|-------------------|
| [Name] | [Publication] | [Beat 1] | [Beat 2] | Weekly/Monthly |

#### Contact Method Prioritization
1. **Preferred Method** (if stated)
2. **Email** (work email)
3. **Twitter/X DM** (if active)
4. **LinkedIn Message** (if connected)
5. **Publication Contact Form** (last resort)

#### Source Confidence Scoring
| Factor | Weight | Score |
|--------|--------|-------|
| Source Authority | 30% | Official site = High |
| Recency | 25% | Last 6 months = High |
| Cross-Reference | 25% | 2+ sources = High |
| Completeness | 20% | All fields = High |

### 6. Output Generation

#### Media Registry Table
```markdown
# Media Registry: [Topic/Sector]

**Prepared:** YYYY-MM-DD
**Geography:** [Region]
**Sector:** [Industry]
**Total Contacts:** X

## Tier 1 Outlets (National/Global)

| Name | Title | Outlet | Beat | Email | Twitter | LinkedIn | Confidence |
|------|-------|--------|------|-------|---------|----------|------------|
| [Name] | [Title] | [Outlet] | [Beat] | [Email] | [@handle] | [URL] | High/Med/Low |
| [Name] | [Title] | [Outlet] | [Beat] | [Email] | [@handle] | [URL] | High/Med/Low |

## Tier 2 Outlets (Regional/Specialized)

| Name | Title | Outlet | Beat | Email | Twitter | LinkedIn | Confidence |
|------|-------|--------|------|-------|---------|----------|------------|
| [Name] | [Title] | [Outlet] | [Beat] | [Email] | [@handle] | [URL] | High/Med/Low |

## Tier 3 Outlets (Blogs/Niche)

| Name | Title | Outlet | Beat | Email | Twitter | LinkedIn | Confidence |
|------|-------|--------|------|-------|---------|----------|------------|
| [Name] | [Title] | [Outlet] | [Beat] | [Email] | [@handle] | [URL] | High/Med/Low |

## Summary by Beat
| Beat | Journalist Count | Tier 1 | Tier 2 | Tier 3 |
|------|------------------|--------|--------|--------|
| [Beat 1] | X | X | X | X |
| [Beat 2] | X | X | X | X |

## Summary by Outlet
| Outlet | Journalists | Tier | Focus Areas |
|--------|-------------|------|-------------|
| [Outlet 1] | X | 1/2/3 | [Topics] |
| [Outlet 2] | X | 1/2/3 | [Topics] |

## Contact Preferences (If Known)
| Journalist | Preferred Method | Notes |
|------------|------------------|-------|
| [Name] | Email | "No cold calls" |
| [Name] | Twitter DM | "Pitch via DM first" |

## Data Freshness
| Field | Last Verified | Source |
|-------|---------------|--------|
| Contact Info | YYYY-MM-DD | [Source] |
| Beat Info | YYYY-MM-DD | [Source] |
| Outlet Status | YYYY-MM-DD | [Source] |

## Sources & Methodology
- [Source 1] - [Method]
- [Source 2] - [Method]
- [Source 3] - [Method]
```

#### Outlet Coverage Tracker
```markdown
# Outlet Coverage Tracker: [Sector/Topic]

**Prepared:** YYYY-MM-DD
**Monitoring Period:** Last 90 days

## Coverage by Outlet

### [Outlet 1] - Tier 1
| Metric | Value |
|--------|-------|
| **Articles (90 days)** | X |
| **Authors** | [Names] |
| **Avg. Reach** | [Number] |
| **Sentiment** | Positive/Neutral/Negative |
| **Key Topics** | [Topic 1, Topic 2] |

**Recent Articles:**
| Date | Title | Author | Sentiment |
|------|-------|--------|-----------|
| YYYY-MM-DD | [Title] | [Author] | +/0/- |
| YYYY-MM-DD | [Title] | [Author] | +/0/- |

### [Outlet 2] - Tier 2
[Same structure]

### [Outlet 3] - Tier 3
[Same structure]

## Coverage Trends
| Month | Article Count | Tier 1 | Tier 2 | Tier 3 |
|-------|---------------|--------|--------|--------|
| Month 1 | X | X | X | X |
| Month 2 | X | X | X | X |
| Month 3 | X | X | X | X |

## Topic Analysis
| Topic | Coverage Count | Outlets | Trend |
|-------|----------------|---------|-------|
| [Topic 1] | X | X | ↑/→/↓ |
| [Topic 2] | X | X | ↑/→/↓ |

## Author Activity
| Author | Outlet | Articles (90d) | Topics |
|--------|--------|----------------|--------|
| [Name] | [Outlet] | X | [Topics] |
| [Name] | [Outlet] | X | [Topics] |

## Engagement Opportunities
| Outlet | Opportunity | Timing | Approach |
|--------|-------------|--------|----------|
| [Outlet] | [e.g., Writing about X] | [Timing] | [Approach] |
```

#### Collection Heartbeat Report
```markdown
# Media Collection Heartbeat Report

**Collection Date:** YYYY-MM-DD
**Collector:** DeerFlow Agent
**Scope:** [Topic/Sector/Region]

## Collection Summary
| Metric | Count |
|--------|-------|
| **Outlets Identified** | X |
| **Journalists Profiled** | X |
| **Contacts Verified** | X |
| **High Confidence Records** | X |
| **Medium Confidence Records** | X |
| **Low Confidence Records** | X |

## Source Breakdown
| Source Type | Records | Confidence Avg |
|-------------|---------|----------------|
| Publication Sites | X | X.X |
| LinkedIn | X | X.X |
| Twitter | X | X.X |
| Media Databases | X | X.X |

## Data Quality Assessment
| Field | Completeness | Freshness | Accuracy |
|-------|--------------|-----------|----------|
| Names | XX% | High | High |
| Titles | XX% | Medium | High |
| Outlets | XX% | High | High |
| Beats | XX% | Medium | Medium |
| Emails | XX% | Low | Medium |
| Social Handles | XX% | High | High |

## Gaps Identified
| Gap | Impact | Remediation |
|-----|--------|-------------|
| Missing emails for X journalists | Medium | Manual research needed |
| Outdated beat info for X | Low | Verify via recent bylines |
| No social for X | Low | Not critical |

## Recommendations
1. [Action to improve data quality]
2. [Action to fill gaps]
3. [Action to maintain freshness]

## Next Collection Scheduled
**Date:** YYYY-MM-DD
**Focus:** [What to update/add]
```

#### Source Confidence Scoring
```markdown
# Source Confidence Report: Media Registry

**Prepared:** YYYY-MM-DD
**Total Records:** X

## Confidence Distribution
| Confidence Level | Count | Percentage |
|------------------|-------|------------|
| High | X | XX% |
| Medium | X | XX% |
| Low | X | XX% |

## Confidence Criteria

### High Confidence (≥0.8)
- ✅ Name + title from official publication site
- ✅ Beat confirmed via recent bylines (last 90 days)
- ✅ Contact info from ≥2 sources
- ✅ Active social presence verified

### Medium Confidence (0.5-0.79)
- ✅ Name + title from publication site OR LinkedIn
- ⚠️ Beat inferred from limited bylines
- ⚠️ Contact info from single source
- ⚠️ Social presence not verified

### Low Confidence (<0.5)
- ⚠️ Name from third-party source only
- ⚠️ Title/role unclear
- ⚠️ No recent activity confirmed
- ⚠️ Contact info unverified

## Record-Level Scoring
| Record ID | Name | Outlet | Confidence Score | Factors |
|-----------|------|--------|------------------|---------|
| 001 | [Name] | [Outlet] | 0.92 | Official site + LinkedIn + bylines |
| 002 | [Name] | [Outlet] | 0.65 | LinkedIn only, limited bylines |
| 003 | [Name] | [Outlet] | 0.40 | Third-party source only |

## Improvement Actions
| Action | Records Affected | Effort | Priority |
|--------|------------------|--------|----------|
| Verify emails via publication | X | Medium | High |
| Confirm beats via recent articles | X | Low | High |
| Cross-reference LinkedIn | X | Low | Medium |
| Remove outdated records | X | Low | Medium |

## Freshness Metrics
| Metric | Value |
|--------|-------|
| Records <30 days old | XX% |
| Records 30-90 days old | XX% |
| Records >90 days old | XX% |
| Avg. record age | X days |
```

#### PR Engagement Brief
```markdown
# PR Engagement Brief: [Campaign/Topic]

**Prepared:** YYYY-MM-DD
**Campaign:** [Name/Topic]
**Target Geography:** [Region]
**Objective:** [Media coverage goal]

## Executive Summary
[Brief overview of media landscape and recommended approach]

## Target Outlet Priority List

### Priority 1 (Tier 1 - Must Secure)
| Outlet | Journalist | Angle | Timing | Status |
|--------|------------|-------|--------|--------|
| [Outlet] | [Name] | [Angle] | [Timing] | Not Contacted |
| [Outlet] | [Name] | [Angle] | [Timing] | Not Contacted |

### Priority 2 (Tier 2 - Should Secure)
| Outlet | Journalist | Angle | Timing | Status |
|--------|------------|-------|--------|--------|
| [Outlet] | [Name] | [Angle] | [Timing] | Not Contacted |

### Priority 3 (Tier 3 - Nice to Have)
| Outlet | Journalist | Angle | Timing | Status |
|--------|------------|-------|--------|--------|
| [Outlet] | [Name] | [Angle] | [Timing] | Not Contacted |

## Messaging Framework

### Core Narrative
[Key message in 1-2 sentences]

### Supporting Points
1. [Point 1 with proof]
2. [Point 2 with proof]
3. [Point 3 with proof]

### Tailored Angles by Beat
| Beat | Angle | Relevance |
|------|-------|-----------|
| [Beat 1] | [Angle tailored to beat] | [Why it matters] |
| [Beat 2] | [Angle tailored to beat] | [Why it matters] |

## Journalist-Specific Pitches

### For [Journalist 1] - [Outlet]
**Beat:** [Their beat]
**Recent Work:** [Reference to their article]
**Pitch Angle:** [Tailored angle]
**Hook:** [Why now]
**Available Assets:** [Spokesperson, data, visuals]

### For [Journalist 2] - [Outlet]
[Same structure]

## Contact Strategy
| Phase | Action | Timeline | Owner |
|-------|--------|----------|-------|
| Phase 1 | Email Priority 1 targets | Week 1 | [Name] |
| Phase 2 | Follow-up + Tier 2 outreach | Week 2 | [Name] |
| Phase 3 | Tier 3 + social engagement | Week 3 | [Name] |

## Embargo Strategy (If Applicable)
- **Embargo Date:** YYYY-MM-DD HH:MM
- **Embargo Recipients:** [List]
- **Release Date:** YYYY-MM-DD HH:MM

## Spokesperson Availability
| Name | Title | Availability | Expertise |
|------|-------|--------------|-----------|
| [Name] | [Title] | [Dates] | [Topics] |

## Success Metrics
| Metric | Target |
|--------|--------|
| Placements Secured | X |
| Tier 1 Placements | X |
| Estimated Reach | X |
| Message Penetration | XX% |
| Sentiment | Positive |

## Risk Mitigation
| Risk | Mitigation |
|------|------------|
| No response from Tier 1 | Escalate via warm intro |
| Negative coverage | Prepare Q&A, monitoring |
| Competitor news same day | Have backup timing |

## Appendix: Contact List
[Link to full media registry]
```

## Confidence Scoring

| Score | Criteria |
|-------|----------|
| High | Official publication site + LinkedIn + recent bylines |
| Medium | Publication site OR LinkedIn + some bylines |
| Low | Third-party source only, unverified, outdated |

## Personal Data Handling

⚠️ **Important:** This mode collects journalist names, contact info, and social profiles.

- **Collect only:** Work email, work title, publication, public social handles
- **Do not collect:** Personal emails, private phone numbers, family info
- **Retention:** Review and update every 90 days; purge outdated records
- **Classification:** Internal - not for external distribution
- **Compliance:** GDPR/privacy law considerations for EU journalists

## Skill Library Entries
- `media/outlet-discovery`
- `media/journalist-research`
- `media/masthead-extraction`
- `media/beat-mapping`
- `media/pr-targeting`
- `media/coverage-tracking`

## Integration Points
- CRM (contact management)
- PR software (Cision, Meltwater)
- Email platforms (Mailchimp, Outreach)
- Social media management (Hootsuite, Buffer)
- Media monitoring (Mention, Brandwatch)

## Ethical Considerations

- **Respect journalist preferences:** Some explicitly state "no cold pitches"
- **Verify opt-in status:** Don't add to mailing lists without consent
- **Honor embargoes:** Respect confidential advance information
- **Accurate representation:** Don't misrepresent your relationship or news value
- **Frequency limits:** Don't spam the same journalists repeatedly
