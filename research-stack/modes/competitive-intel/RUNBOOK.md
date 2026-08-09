# Runbook: Competitive Intelligence Tracker

## Overview

| Field | Value |
|-------|-------|
| **Name** | competitive-intelligence-tracker |
| **Frequency** | Weekly |
| **Mode** | Competitive Intelligence |
| **Tools** | SearXNG, Firecrawl, DeerFlow |
| **Output** | Competitor updates, battle cards, market signals |

---

## Execution Workflow

### Phase 1: Intake & Scoping

```yaml
task:
  title: "Competitive Intelligence Tracker - [Week/Date Range]"
  objective: "Track competitor movements and market signals"
  priority_intelligence_requirements:
    - "What product changes did competitors announce?"
    - "What pricing signals were observed?"
    - "What partnerships or M&A activity occurred?"
    - "What market positioning changes were made?"
  scope:
    geography: "[Regions]"
    sector: "[Industry]"
    timeframe: "Last 7 days"
    language: "English"
    source_types:
      - competitor websites
      - news media
      - review sites (G2, Capterra)
      - analyst firms
      - social media (LinkedIn, Twitter)
    output_required: "Competitor updates + battle card updates + market signals"
    handling_classification: "Internal"
    personal_data_involved: false
    review_required: true
```

### Phase 2: Research Planning

```yaml
research_plan:
  key_questions:
    - "What did competitors announce this week?"
    - "What pricing changes were observed?"
    - "What partnerships were announced?"
    - "What customer wins/losses were reported?"
  source_strategy:
    primary:
      - Competitor websites (news, blogs, product pages)
      - Press releases
      - Review sites (G2, Capterra)
    secondary:
      - Tech news (TechCrunch, VentureBeat)
      - Analyst reports
      - Social media (LinkedIn, Twitter)
  query_strategy:
    - "[competitor] news this week"
    - "[competitor] product launch"
    - "[competitor] pricing"
    - "[competitor] partnership"
    - "[competitor] customer win"
    - "[product category] comparison"
  acquisition_strategy:
    - Scrape: Competitor news, product pages
    - Crawl: Review site profiles
    - Extract: Pricing, features, ratings
  verification_strategy:
    - Cross-reference announcements with news
    - Verify pricing on official sites
    - Check review authenticity
  expected_outputs:
    - Competitor updates summary
    - Product positioning changes
    - Pricing signals
    - Partnership signals
    - Battle card updates
  risks:
    - Rumors marked as fact
    - Outdated pricing/feature info
    - Biased review sources
  assumptions:
    - Official announcements are accurate
    - News reports are verified
```

### Phase 3: SearXNG Discovery

**Query Set:**

| Query | Purpose | Expected Sources |
|-------|---------|------------------|
| `"[competitor]" news` | General news | News sites, PR |
| `"[competitor]" product launch` | Product updates | Competitor site, news |
| `"[competitor]" pricing` | Pricing changes | Competitor site, reviews |
| `"[competitor]" partnership` | Business deals | News, PR |
| `"[competitor] vs"` | Comparisons | Review sites, blogs |
| `"[product category]" trends` | Market trends | Analyst reports, news |

### Phase 4: Firecrawl Acquisition

**Acquisition Plan:**

| URL Type | Method | Extract Fields |
|----------|--------|----------------|
| Competitor News | Scrape | Title, date, summary |
| Product Pages | Scrape | Features, pricing |
| Review Profiles | Crawl | Ratings, reviews, trends |
| Press Releases | Scrape | Full announcement |

### Phase 5: Evidence Store

**Store:**
- All raw competitor content
- Pricing snapshots
- Review data
- News articles

### Phase 6: Analysis & Verification

**For each finding:**

```yaml
finding:
  title: "[Competitor] Launched [Product/Feature]"
  summary: "[2-3 sentence summary]"
  evidence:
    - source_url: "https://[competitor]/news/[article]"
      supporting_excerpt: "[Direct quote]"
      relevance: "Official announcement"
    - source_url: "https://news.site/[article]"
      supporting_excerpt: "[Direct quote]"
      relevance: "Third-party coverage"
  implication: "[What this means for us]"
  confidence_level: "high|medium|low"
  recommended_action: "[Specific response]"
  verification_status: "verified|pending"
  reviewer_status: "human-review-required"
  created_at: "2024-06-14T04:30:00Z"
```

**Contradiction Handling:**
```yaml
contradiction:
  claim: "[Competitor] pricing is $X"
  source_a:
    url: "https://[competitor]/pricing"
    claim: "$X"
  source_b:
    url: "https://review.site/[product]"
    claim: "$Y"
  assessment: "Competitor site is authoritative"
  resolution: "Use competitor site pricing"
```

### Phase 7: Output Generation

**Expected Outputs:**

#### 1. Competitor Updates
```markdown
# Competitor Updates - [Week of YYYY-MM-DD]

## [Competitor A]

### Product Changes
- **[Feature]:** [Description]
- **Impact:** [High/Medium/Low]
- **Source:** [Link]

### Business Movements
- **[Partnership/M&A/Hiring]:** [Details]
- **Impact:** [High/Medium/Low]
- **Source:** [Link]

## [Competitor B]
[Same structure]
```

#### 2. Product Positioning Changes
```markdown
# Product Positioning Changes

| Competitor | Old Positioning | New Positioning | Evidence |
|------------|-----------------|-----------------|----------|
| [Competitor] | [Previous] | [New] | [Link] |

## Messaging Shifts
- **[Competitor]:** Now emphasizing [theme] vs. previous [theme]
```

#### 3. Pricing Signals
```markdown
# Pricing Signals

| Competitor | Product | Old Price | New Price | Change | Source |
|------------|---------|-----------|-----------|--------|--------|
| [Competitor] | [Product] | $X | $Y | +Z% | [Link] |

## Observations
- [Competitor] increased pricing by X%
- [Competitor] introduced new tier at $X
```

#### 4. Partnership Signals
```markdown
# Partnership Signals

| Competitor | Partner | Type | Scope | Impact |
|------------|---------|------|-------|--------|
| [Competitor] | [Partner] | Technology | [Details] | High |

## Market Implications
- [What this means for market dynamics]
```

#### 5. Battle Card Updates
```markdown
# Battle Card Updates: [Competitor]

## What Changed This Week
- [Change 1]
- [Change 2]

## Updated Differentiators
| Our Advantage | Evidence |
|---------------|----------|
| [Differentiator] | [Evidence] |

## New Objection Handling
**Objection:** "[New objection based on their announcement]"
**Response:** "[Updated response]"

## Full Battle Card: [Link]
```

---

## Skills Used

| Skill | Category | Purpose |
|-------|----------|---------|
| `competitive-intelligence` | Domain | Competitor analysis |
| `market-intelligence-template` | Reporting | Report formatting |
| `contradiction-handling` | Verification | Resolving conflicts |

---

## Governance Controls

| Control | Application |
|---------|-------------|
| **Official source priority** | Competitor sites > news > rumors |
| **No speculation** | Mark analysis clearly |
| **Contradiction flagging** | Resolve or escalate |
| **Human review** | All CI before distribution |

---

## Human Review Triggers

**All CI trackers require human review.**

**Escalate immediately if:**
- Major competitor movement (M&A, pivot)
- Pricing war signals
- Market-moving announcement
- Contradictory information unresolved

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2024-06-14 | Initial runbook |
