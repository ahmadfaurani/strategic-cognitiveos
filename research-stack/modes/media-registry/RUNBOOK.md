# Runbook: Media Registry Collection

## Overview

| Field | Value |
|-------|-------|
| **Name** | media-registry-collection |
| **Frequency** | Daily (incremental) |
| **Mode** | Media Registry |
| **Tools** | SearXNG, Firecrawl, DeerFlow |
| **Output** | Outlet registry, journalist contacts, coverage status |

---

## Execution Workflow

### Phase 1: Intake & Scoping

```yaml
task:
  title: "Media Registry Collection - [Topic/Sector]"
  objective: "Build and enrich media contact database for [topic]"
  priority_intelligence_requirements:
    - "Which outlets cover [topic]?"
    - "Who are the key journalists?"
    - "What are their beats and contact methods?"
    - "What is outlet reach and relevance?"
  scope:
    geography: "[Regions]"
    sector: "[Industry/topic]"
    timeframe: "Current (active journalists)"
    language: "English"
    source_types:
      - publication websites (mastheads, about)
      - journalist bylines
      - LinkedIn profiles
      - Twitter/X profiles
    output_required: "Outlet registry + journalist registry + heartbeat report"
    handling_classification: "Internal"
    personal_data_involved: true
    review_required: true
```

### Phase 2: Research Planning

```yaml
research_plan:
  key_questions:
    - "Which outlets cover our sector?"
    - "Who writes about [topic]?"
    - "What are journalist beats?"
    - "How do we contact them?"
  source_strategy:
    primary:
      - Publication websites (masthead, about)
      - Journalist byline pages
      - LinkedIn profiles
    secondary:
      - Twitter/X profiles
      - Media databases (Muck Rack free profiles)
  query_strategy:
    - "[topic] journalist"
    - "[sector] reporter [publication]"
    - "site:[publication].com masthead"
    - "site:linkedin.com \"[publication]\" journalist"
  acquisition_strategy:
    - Scrape: Masthead pages, journalist bios
    - Crawl: Publication section pages
    - Extract: Names, titles, beats, contacts
  verification_strategy:
    - Cross-reference LinkedIn + publication site
    - Verify recent bylines
    - Confirm contact info from multiple sources
  expected_outputs:
    - Outlet registry
    - Journalist registry
    - Public contact sources
    - Coverage status
    - Collection heartbeat report
  risks:
    - Outdated contact information
    - Personal data handling
    - Journalist preference misinterpretation
  assumptions:
    - Publication sites are current
    - LinkedIn profiles are active
```

### Phase 3: SearXNG Discovery

**Query Set:**

| Query | Purpose | Expected Sources |
|-------|---------|------------------|
| `"[topic]" journalist` | Journalist discovery | LinkedIn, publication sites |
| `"[sector]" reporter` | Beat mapping | Publication sites |
| `site:[publication].com masthead` | Masthead discovery | Publication sites |
| `site:linkedin.com "[publication]" journalist` | Profile discovery | LinkedIn |

### Phase 4: Firecrawl Acquisition

**Acquisition Plan:**

| URL Type | Method | Extract Fields |
|----------|--------|----------------|
| Masthead Page | Scrape | Names, titles, emails |
| Journalist Bio | Scrape | Beat, contact, background |
| Byline Archive | Crawl | Recent articles, topics |
| LinkedIn Profile | Scrape | Background, connections |

**Extraction Schema:**
```json
{
  "source_url": "",
  "structured_json": {
    "journalist_name": "",
    "title": "",
    "publication": "",
    "beat": [],
    "email": "",
    "twitter": "",
    "linkedin": "",
    "recent_articles": []
  }
}
```

### Phase 5: Evidence Store

**Store:**
- All raw journalist/outlet data
- Contact information (work emails only)
- Beat mappings
- Source URLs for verification

### Phase 6: Analysis & Verification

**For each finding:**

```yaml
finding:
  title: "[Journalist Name] - [Publication]"
  summary: "[Beat and contact info]"
  evidence:
    - source_url: "https://[publication]/masthead"
      supporting_excerpt: "[Name and title]"
      relevance: "Official publication roster"
    - source_url: "https://linkedin.com/in/[name]"
      supporting_excerpt: "[Background]"
      relevance: "Professional background"
  implication: "[PR targeting relevance]"
  confidence_level: "high|medium|low"
  recommended_action: "[Add to registry / Verify / Skip]"
  verification_status: "verified|pending"
  reviewer_status: "human-review-required"
  created_at: "2024-06-14T04:30:00Z"
```

### Phase 7: Output Generation

**Expected Outputs:**

#### 1. Outlet Registry
```markdown
# Outlet Registry: [Topic/Sector]

## Tier 1 (National/Global)
| Outlet | Reach | Focus | URL |
|--------|-------|-------|-----|
| [Outlet 1] | High | [Topics] | [URL] |
| [Outlet 2] | High | [Topics] | [URL] |

## Tier 2 (Regional/Specialized)
| Outlet | Reach | Focus | URL |
|--------|-------|-------|-----|
| [Outlet 3] | Medium | [Topics] | [URL] |

## Tier 3 (Blogs/Niche)
| Outlet | Reach | Focus | URL |
|--------|-------|-------|-----|
| [Outlet 4] | Niche | [Topics] | [URL] |
```

#### 2. Journalist Registry
```markdown
# Journalist Registry: [Topic/Sector]

| Name | Title | Outlet | Beat | Email | Twitter | LinkedIn | Confidence |
|------|-------|--------|------|-------|---------|----------|------------|
| [Name] | [Title] | [Outlet] | [Beat] | [Email] | [@handle] | [URL] | High |
| [Name] | [Title] | [Outlet] | [Beat] | [Email] | [@handle] | [URL] | Medium |

## Summary by Beat
| Beat | Journalist Count | Tier 1 | Tier 2 | Tier 3 |
|------|------------------|--------|--------|--------|
| [Beat 1] | X | X | X | X |
```

#### 3. Public Contact Sources
```markdown
# Public Contact Sources

| Journalist | Contact Method | Source URL | Verified |
|------------|----------------|------------|----------|
| [Name] | Email | [URL] | ✅ |
| [Name] | Twitter DM | [URL] | ✅ |

## Contact Preferences (If Known)
| Journalist | Preferred Method | Notes |
|------------|------------------|-------|
| [Name] | Email | "No cold calls" |
```

#### 4. Coverage Status
```markdown
# Coverage Status

## Active Coverage (Last 90 Days)
| Journalist | Outlet | Articles | Topics |
|------------|--------|----------|--------|
| [Name] | [Outlet] | X | [Topics] |

## Coverage Gaps
| Outlet | Last Article | Gap Duration | Action |
|--------|--------------|--------------|--------|
| [Outlet] | YYYY-MM-DD | X days | Re-engage |
```

#### 5. Collection Heartbeat
```markdown
# Collection Heartbeat Report

**Collection Date:** YYYY-MM-DD
**Collector:** DeerFlow Agent

## Summary
| Metric | Count |
|--------|-------|
| Outlets Identified | X |
| Journalists Profiled | X |
| Contacts Verified | X |
| High Confidence | X |
| Medium Confidence | X |
| Low Confidence | X |

## Data Quality
| Field | Completeness |
|-------|--------------|
| Names | XX% |
| Titles | XX% |
| Emails | XX% |
| Beats | XX% |

## Gaps Identified
- [Gap 1]
- [Gap 2]

## Next Collection
**Scheduled:** YYYY-MM-DD
**Focus:** [What to update/add]
```

---

## Skills Used

| Skill | Category | Purpose |
|-------|----------|---------|
| `media-registry` | Domain | Journalist research |
| `privacy-controls` | Governance | Personal data handling |
| `failed-acquisition-recovery` | Recovery | Handle blocked pages |

---

## Governance Controls

| Control | Application |
|---------|-------------|
| **Public/professional data only** | Work emails, titles, beats only |
| **No private data** | No personal emails, phones, family |
| **Source URL required** | All contacts must cite source |
| **Retention limit** | 90 days with quarterly refresh |
| **Human review** | All contact lists before use |

---

## Privacy Controls (Critical)

**Permitted:**
- ✅ Work email addresses (from publication sites)
- ✅ Professional titles
- ✅ Public social media handles
- ✅ Beat/coverage areas
- ✅ Recent bylines

**Prohibited:**
- ❌ Personal email addresses
- ❌ Personal phone numbers
- ❌ Home addresses
- ❌ Family information
- ❌ Private social media accounts

---

## Human Review Triggers

**All media registries require human review before use.**

**Escalate immediately if:**
- Personal data inadvertently collected
- Journalist opt-out preferences found
- Large-scale collection (>100 journalists)
- EU subject data (GDPR considerations)

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2024-06-14 | Initial runbook |
