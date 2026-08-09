# SearXNG Query Patterns

## Purpose
Standardized query patterns for effective source discovery across different research modes.

---

## Query Construction Principles

### 1. Use Multiple Query Variants
For each research objective, run:
- **Broad query** - Cast wide net for discovery
- **Narrow query** - Target specific information
- **Domain-specific query** - Use `site:` operators
- **Alternative formulation** - Use synonyms/related terms

### 2. Leverage Search Operators

| Operator | Purpose | Example |
|----------|---------|---------|
| `site:` | Restrict to domain | `site:nvd.nist.gov CVE` |
| `""` | Exact phrase | `"security advisory"` |
| `OR` | Alternative terms | `vulnerability OR CVE` |
| `-` | Exclude terms | `CVE -discontinued` |
| `filetype:` | Specific file type | `filetype:pdf report` |
| `intitle:` | Words in title | `intitle:"security"` |
| `inurl:` | Words in URL | `inurl:/security/` |
| `after:` | Date filter | `CVE after:2024-01-01` |
| `before:` | Date filter | `news before:2024-06-01` |

### 3. Time-Bounding
Always include timeframe for time-sensitive research:
- `2024` for current year
- `last 30 days` for recent
- `after:2024-01-01` for specific date ranges

---

## Domain-Specific Query Libraries

### Cyber Threat Intelligence

```
# CVE Discovery
"CVE" published [timeframe]
"CVE-2024" [product/vendor]
site:nvd.nist.gov "[vendor]"
site:cve.mitre.org "[product]"

# Exploit Tracking
"exploit" CVE [year]
"PoC" [CVE ID]
site:github.com "exploit" [product]
site:exploit-db.com "[vendor]"

# Vendor Advisories
"[vendor] security advisory"
"[vendor] PSIRT"
"[vendor] vulnerability disclosure"
site:[vendor].com/security

# Threat Actor Activity
"[threat actor] TTPs"
"[threat actor] malware"
"[threat actor] campaign [year]"
site:mitre.org "[threat actor]"

# Active Exploitation
"CISA KEV" [vendor/product]
"known exploited" CVE
"active exploitation" CVE

# Sector-Specific
"[sector] cyber threat [year]"
"[sector] ransomware attack"
"critical infrastructure" cyber
```

### Vendor Due Diligence

```
# Security Posture
"[vendor] security"
"[vendor] SOC2 OR ISO27001"
"[vendor] security certification"
"[vendor] security policy"

# Vulnerability History
"[vendor] vulnerability"
"[vendor] CVE"
"[vendor] security incident"
"[vendor] breach OR "data breach"

# Technical Maturity
site:github.com "[vendor]"
"[vendor] release notes"
"[vendor] changelog"
"[vendor] documentation"

# Market Viability
"[vendor] funding"
"[vendor] acquisition"
"[vendor] revenue"
site:crunchbase.com "[vendor]"

# Customer Sentiment
site:g2.com "[product]"
site:capterra.com "[product]"
"[product] review"
"[product] vs [competitor]"

# Licensing
"[product] license"
"[product] MIT OR Apache OR GPL"
"[product] commercial license"
```

### Competitive Intelligence

```
# Company Overview
"[competitor] overview"
"[competitor] about"
"[competitor] leadership"
"[competitor] headquarters"

# Product Intelligence
"[competitor] product"
"[competitor] features"
"[competitor] pricing"
"[competitor] roadmap"

# Market Positioning
"[competitor] vs"
"[competitor] alternative"
"[competitor] competitor"
"[competitor] market share"

# Partnership & M&A
"[competitor] partnership"
"[competitor] acquisition"
"[competitor] integration"
"[competitor] reseller"

# Executive Movements
"[competitor] CEO"
"[competitor] executive"
"[competitor] hiring"
"[competitor] layoffs"

# Financial Signals
"[competitor] funding"
"[competitor] valuation"
"[competitor] IPO"
"[competitor] earnings"
```

### Regulatory Monitoring

```
# Regulation Discovery
"[regulation name] 2024"
"[regulation] final rule"
"[regulation] compliance deadline"
"[regulation] requirements"

# Agency Guidance
site:cisa.gov "guidance"
site:sec.gov "cybersecurity"
site:ico.org.uk "guidance"
site:edpb.europa.eu "guidelines"

# Sector-Specific
"[sector] cybersecurity regulation"
"[sector] compliance requirements"
"[sector] regulatory framework"

# Enforcement
"[agency] enforcement action"
"[agency] penalty"
"[agency] fine"
"[company] settlement"

# Policy Development
"AI governance" framework
"data protection" law
"privacy" regulation
"cybersecurity" policy
```

### Strategic Account Intelligence

```
# Company Overview
"[company] overview"
"[company] about"
"[company] mission"
"[company] strategy"

# Strategic Direction
"[company] strategic priorities"
"[company] transformation"
"[company] investment"
"[company] initiative"

# Leadership
"[company] CEO"
"[company] executive team"
"[company] CIO OR CTO"
site:linkedin.com/in "[company]"

# Financial Performance
"[company] earnings"
"[company] annual report"
"[company] revenue"
"[company] investor presentation"

# Recent News
"[company] news"
"[company] announcement"
"[company] partnership"
"[company] acquisition"

# Technology Stack
"[company] technology stack"
"[company] cloud migration"
"[company] digital transformation"
site:stackshare.io "[company]"

# Challenges
"[company] challenges"
"[company] restructuring"
"[company] layoffs"
"[company] competitive pressure"
```

### Tender Monitoring

```
# General Tender Discovery
"RFP" [category] [year]
"tender" [service type]
"procurement" [solution]
"request for proposals"

# Portal-Specific
site:sam.gov "[keyword]"
site:ungm.org "[keyword]"
site:tenders.gov "[keyword]"
site:europa.eu "TED tender"

# Grant Opportunities
"grant" [domain] [year]
"funding opportunity" [sector]
"RFA" [topic]
"NOFO" [program]

# Agency-Specific
"[agency] procurement"
"[agency] RFP"
"[agency] contracting"
"[agency] solicitation"

# Industry-Specific
"[industry] tender board"
"[sector] procurement portal"
"[vertical] RFP opportunities"
```

### Media Registry

```
# Outlet Discovery
"[sector] news outlets"
"[industry] publications"
"[topic] media coverage"
"top [sector] blogs"
"[sector] trade publications"

# Journalist Discovery
"[topic] journalist"
"[sector] reporter"
"[beat] editor"
"[topic] writer"

# Masthead Discovery
site:[publication].com "masthead"
site:[publication].com "editorial team"
site:[publication].com "about us"
site:[publication].com "contact"

# Social/LinkedIn
site:linkedin.com "[publication]" journalist
site:linkedin.com "[publication]" editor
site:twitter.com "[publication]" reporter
"[journalist name]" [topic]

# Beat Mapping
"writes about" [topic]
"covers" [sector]
"specializes in" [beat]
```

---

## Query Execution Strategy

### Step 1: Broad Discovery
Run 3-5 broad queries to map the landscape:
```
"[topic] overview"
"[topic] news"
"[topic] 2024"
```

### Step 2: Targeted Search
Run 5-10 targeted queries based on initial findings:
```
site:[domain] "[keyword]"
"[specific aspect]"
"[specific entity]"
```

### Step 3: Deep Dive
Run 3-5 deep queries for specific information:
```
"[specific requirement]"
"[specific metric]"
"[specific event]"
```

### Step 4: Verification
Run 2-3 verification queries:
```
"[claim]" OR "[alternative]"
"[source1]" vs "[source2]"
```

---

## Query Performance Tracking

Track for each query:
- **Total results** - Volume of matches
- **Results selected** - How many were useful
- **Results rejected** - How many were irrelevant
- **Rejection reasons** - Why rejected (irrelevant, low authority, duplicate, outdated)

**Optimize queries that have:**
- Low selection rate (<30%)
- High irrelevance rate
- Consistently outdated results

---

## Common Pitfalls

| Pitfall | Solution |
|---------|----------|
| Too broad | Add specific terms, use `site:` |
| Too narrow | Remove restrictive terms, use `OR` |
| Outdated results | Use `after:` date filter |
| Low authority sources | Use `site:` for official domains |
| Missing synonyms | Use `OR` with alternative terms |
| Snippet-only results | Add `intitle:` or `inurl:` |

---

## Skill Maintenance

**Update this skill when:**
- New search operators become available
- New authoritative sources are discovered
- Query patterns prove consistently effective
- SearXNG engine behavior changes

**Review frequency:** Monthly
