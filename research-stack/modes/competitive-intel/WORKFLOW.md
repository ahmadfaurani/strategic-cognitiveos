# Competitive Intelligence Mode

## Purpose
Systematic tracking and analysis of competitors, market positioning, and strategic movements.

## Trigger Patterns
- "Track competitor [company]"
- "Battle card for [competitor]"
- "Product comparison: [ours] vs [theirs]"
- "Market movement summary"
- "Pricing changes for [product category]"

## Workflow Steps

### 1. Intelligence Scope
```
Input: Competitor name, product category, or market segment
Output: CI framework
  - Competitor profiles
  - Product positioning
  - Pricing signals
  - Partnership activity
  - Market movements
  - Sales enablement needs
```

### 2. Discovery Queries (SearXNG)

**Competitor Tracking:**
```
"[competitor] news 2024"
"[competitor] funding"
"[competitor] acquisition"
"[competitor] partnership"
"[competitor] layoffs"
"[competitor] executive change"
site:linkedin.com/company "[competitor]"
```

**Product Positioning:**
```
"[competitor product] features"
"[competitor product] pricing"
"[competitor product] vs [our product]"
"[competitor product] review"
"[competitor product] g2"
```

**Pricing Intelligence:**
```
"[competitor] pricing 2024"
"[competitor] price increase"
"[competitor] discount"
"[product category] pricing comparison"
```

**Partnership & Ecosystem:**
```
"[competitor] partner"
"[competitor] integration"
"[competitor] marketplace"
"[competitor] reseller"
```

**Market Signals:**
```
"[market segment] trends 2024"
"[market segment] market share"
"[market segment] analyst report"
site:gartner.com "[market segment]"
site:forrester.com "[market segment]"
```

### 3. Source Classification
| Source Type | Examples | Credibility |
|-------------|----------|-------------|
| Official | Competitor websites, press releases | High |
| Analyst | Gartner, Forrester, IDC | High |
| Review Sites | G2, Capterra, TrustRadius | Medium-High |
| News | TechCrunch, VentureBeat | Medium |
| Social | LinkedIn, Twitter | Medium (verify) |
| Job Postings | LinkedIn Jobs, Indeed | Medium (signals intent) |

### 4. Firecrawl Extraction Targets

**Competitor Website/Pricing Pages:**
```json
{
  "url": "https://[competitor]/pricing",
  "options": {
    "formats": ["markdown", "json"],
    "screenshot": true,
    "onlyMainContent": true
  }
}
```

**Product Feature Pages:**
```json
{
  "url": "https://[competitor]/product/[feature]",
  "options": {
    "formats": ["markdown"],
    "screenshot": false,
    "onlyMainContent": true
  }
}
```

**Review Platform Profiles:**
```json
{
  "url": "https://g2.com/products/[product]",
  "options": {
    "formats": ["json"],
    "extract": {
      "rating": "number",
      "reviewCount": "number",
      "pros": "array",
      "cons": "array",
      "categories": "array"
    }
  }
}
```

**Press Releases/News:**
```json
{
  "url": "https://[competitor]/news/[article]",
  "options": {
    "formats": ["markdown"],
    "screenshot": false,
    "onlyMainContent": true
  }
}
```

### 5. Analysis Framework

#### Competitor Profile Dimensions
- **Company Overview:** Size, funding, leadership
- **Product Portfolio:** Key products, roadmap signals
- **Positioning:** Value prop, target segments
- **Pricing Strategy:** Model, price points, discounts
- **Go-to-Market:** Channels, partnerships
- **Strengths:** Differentiators, moats
- **Weaknesses:** Gaps, customer complaints
- **Market Share:** Estimated position

#### Product Comparison Matrix
| Dimension | Our Product | Competitor A | Competitor B |
|-----------|-------------|--------------|--------------|
| Core Features | ... | ... | ... |
| Pricing | ... | ... | ... |
| Deployment | ... | ... | ... |
| Support | ... | ... | ... |
| Integrations | ... | ... | ... |

#### Battle Card Structure
- **Competitor Overview**
- **When We Compete** (scenarios)
- **Their Strengths** (acknowledge honestly)
- **Their Weaknesses** (exploitable gaps)
- **Key Differentiators** (our advantages)
- **Objection Handling** (responses to common objections)
- **Proof Points** (customer wins, case studies)
- **Pricing Comparison** (if available)

### 6. Output Generation

#### Competitor Battle Card
```markdown
# Battle Card: [Competitor Name]

**Last Updated:** YYYY-MM-DD
**Confidence:** High/Medium/Low

## Competitor Overview
- **Headquarters:** [Location]
- **Founded:** [Year]
- **Funding:** [Amount/Stage]
- **Employees:** [Count]
- **Target Market:** [Segments]

## When We Compete
[Scenarios where this competitor appears in deals]

## Their Strengths
| Strength | Evidence | How to Counter |
|----------|----------|----------------|
| [Strength 1] | [Source] | [Counter strategy] |
| [Strength 2] | [Source] | [Counter strategy] |

## Their Weaknesses
| Weakness | Evidence | How to Exploit |
|----------|----------|----------------|
| [Weakness 1] | [Source] | [Exploitation strategy] |
| [Weakness 2] | [Source] | [Exploitation strategy] |

## Key Differentiators (Our Advantages)
1. **[Differentiator 1]:** [Explanation + proof point]
2. **[Differentiator 2]:** [Explanation + proof point]
3. **[Differentiator 3]:** [Explanation + proof point]

## Common Objections & Responses

**Objection:** "[Competitor] is cheaper"
**Response:** [Value-based response with ROI framing]

**Objection:** "[Competitor] has [feature]"
**Response:** [Context on why our approach is better]

**Objection:** "[Competitor] is more established"
**Response:** [Innovation/agility counter]

## Pricing Comparison
| Tier | Us | [Competitor] | Notes |
|------|-----|--------------|-------|
| Entry | $X | $Y | [Details] |
| Mid | $X | $Y | [Details] |
| Enterprise | Custom | Custom | [Details] |

## Proof Points
- [Customer win story 1]
- [Customer win story 2]
- [Analyst recognition]

## Recent Movements
- [Date]: [Movement summary]
- [Date]: [Movement summary]

## Intelligence Sources
- [Source 1] - [Confidence]
- [Source 2] - [Confidence]
```

#### Product Comparison Matrix
```markdown
# Product Comparison: [Category]

| Feature/Capability | [Our Product] | [Competitor A] | [Competitor B] | [Competitor C] |
|--------------------|---------------|----------------|----------------|----------------|
| **Core Features** |
| Feature 1 | ✅ | ✅ | ❌ | ✅ |
| Feature 2 | ✅ | Partial | ✅ | ❌ |
| **Pricing** |
| Starting Price | $X | $Y | $Z | $W |
| Model | [Model] | [Model] | [Model] | [Model] |
| **Deployment** |
| Cloud | ✅ | ✅ | ✅ | ✅ |
| On-Prem | ✅ | ❌ | ✅ | ❌ |
| **Support** |
| SLA | [Details] | [Details] | [Details] | [Details] |
| **Integrations** |
| Count | X | Y | Z | W |
| Key Partners | [List] | [List] | [List] | [List] |

## Summary
**Best for [use case]:** [Product]
**Best value:** [Product]
**Most features:** [Product]
```

#### Market Movement Tracker
```markdown
# Market Movement Report - [Month/Quarter YYYY]

## Funding Activity
| Company | Amount | Round | Lead Investor | Implication |
|---------|--------|-------|---------------|-------------|
| [Co A] | $XM | Series B | [Investor] | [Analysis] |

## M&A Activity
| Acquirer | Target | Value | Strategic Rationale |
|----------|--------|-------|---------------------|
| [Co A] | [Co B] | $XM | [Analysis] |

## Product Launches
| Company | Product | Key Features | Market Impact |
|---------|---------|--------------|---------------|
| [Co A] | [Product] | [Summary] | [Analysis] |

## Pricing Changes
| Company | Change | Details | Market Signal |
|---------|--------|---------|---------------|
| [Co A] | Increase | X% | [Analysis] |

## Executive Movements
| Company | Executive | Change | From/To | Signal |
|---------|-----------|--------|---------|--------|
| [Co A] | [Name] | Hired/Left | [Details] | [Analysis] |

## Partnership Activity
| Companies | Type | Scope | Market Impact |
|-----------|------|-------|---------------|
| [A] + [B] | Strategic | [Details] | [Analysis] |

## Analyst Coverage
| Firm | Report | Key Finding | Relevance |
|------|--------|-------------|-----------|
| Gartner | [Title] | [Summary] | [Analysis] |
```

#### Sales Enablement Brief
```markdown
# Sales Enablement: [Competitor/Market Update]

**Date:** YYYY-MM-DD
**Audience:** Sales Team

## What Changed
[Brief summary of key developments]

## What It Means for Deals
[Implications for ongoing/prospective deals]

## Talking Points
1. [Talking point 1]
2. [Talking point 2]
3. [Talking point 3]

## Updated Battle Cards
- [Link to updated battle card]

## New Proof Points
- [Proof point 1]
- [Proof point 2]

## Questions?
[Contact for CI team]
```

## Confidence Scoring

| Score | Criteria |
|-------|----------|
| High | Official sources, multiple confirmations, recent data |
| Medium | Single official source or multiple secondary sources |
| Low | Unofficial sources, outdated information, social media |

## Skill Library Entries
- `ci/competitor-battle-card`
- `ci/product-comparison`
- `ci/market-movement-tracking`
- `ci/pricing-intelligence`
- `ci/sales-enablement-brief`

## Integration Points
- CRM (Salesforce, HubSpot)
- Sales enablement platform (Seismic, Highspot)
- Competitive intelligence platforms (Crayon, Klue)
- Slack/Teams sales channels
