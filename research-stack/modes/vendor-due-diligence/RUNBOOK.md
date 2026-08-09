# Runbook: Vendor and Tool Due Diligence

## Overview

| Field | Value |
|-------|-------|
| **Name** | vendor-tool-due-diligence |
| **Frequency** | Ad hoc (per evaluation request) |
| **Mode** | Vendor & Technology Due Diligence |
| **Tools** | SearXNG, Firecrawl, DeerFlow |
| **Output** | Assessment report, risk register, recommendation |

---

## Execution Workflow

### Phase 1: Intake & Scoping

```yaml
task:
  title: "Vendor Due Diligence: [Vendor/Product Name]"
  objective: "Assess security posture, viability, and fit for [use case]"
  priority_intelligence_requirements:
    - "What is the vendor's security posture?"
    - "What is the product's technical maturity?"
    - "What is the vendor's market viability?"
    - "What are the licensing terms and constraints?"
    - "What is the integration complexity?"
  scope:
    geography: "Global"
    sector: "[Relevant industry]"
    timeframe: "Last 24 months + current state"
    language: "English"
    source_types:
      - vendor official (website, security page, docs)
      - code repositories (GitHub, GitLab)
      - independent reviews (G2, analyst reports)
      - security databases (Snyk, npm audit)
      - news and media coverage
    output_required: "Technology assessment report + risk register + recommendation"
    handling_classification: "Internal"
    personal_data_involved: false
    review_required: true  # All due diligence requires human review
```

### Phase 2: Research Planning

```yaml
research_plan:
  key_questions:
    - "Does the vendor have a security program?"
    - "Are there known vulnerabilities in the product?"
    - "What is the release cadence and maintenance status?"
    - "What do customers say about the product?"
    - "What is the total cost of ownership?"
    - "What are the integration requirements?"
  source_strategy:
    primary:
      - Vendor website (security, docs, about)
      - GitHub/GitLab repository
      - Package registries (npm, PyPI, etc.)
    secondary:
      - Review sites (G2, Capterra, TrustRadius)
      - Analyst reports (Gartner, Forrester)
      - Security databases (Snyk, OSS Index)
    official:
      - Vendor security page
      - Compliance certifications (SOC2, ISO27001)
    technical:
      - GitHub repo, package registry, dependency graphs
    news:
      - Tech media, security blogs, incident reports
  query_strategy:
    - "[vendor] security"
    - "[vendor] SOC2 OR ISO27001"
    - "[vendor] security incident OR breach"
    - "[product] vulnerability OR CVE"
    - "site:github.com \"[vendor]\""
    - "site:g2.com \"[product]\""
    - "site:snyk.io \"[product]\""
    - "[product] vs [competitor]"
  acquisition_strategy:
    - Scrape: Vendor security page, docs, about
    - Crawl: GitHub repo (README, SECURITY.md, issues)
    - Extract: Package metadata, vulnerability counts
    - Screenshot: Security badges, certification logos
  verification_strategy:
    - Verify security claims on vendor site
    - Cross-reference vulnerabilities across sources
    - Confirm certifications via issuer databases
    - Validate customer reviews across platforms
  expected_outputs:
    - Technology assessment report
    - Security posture summary
    - Risk register
    - Maturity scorecard
    - Deployment recommendation
  risks:
    - Vendor marketing vs. reality gap
    - Outdated information
    - Biased review sources
    - Incomplete vulnerability disclosure
  assumptions:
    - Vendor security page is accurate
    - GitHub activity reflects maintenance status
    - Reviews are genuine (not astroturfed)
```

### Phase 3: SearXNG Discovery

**Query Set:**

| Query | Purpose | Expected Sources |
|-------|---------|------------------|
| `"[vendor]" security` | Security program | Vendor site, news |
| `"[vendor]" SOC2 OR ISO27001` | Certifications | Vendor, certifier sites |
| `"[vendor]" breach OR incident` | Security history | News, blogs |
| `"[product]" vulnerability OR CVE` | Vulnerabilities | NVD, Snyk, GitHub |
| `site:github.com "[vendor]"` | Code presence | GitHub |
| `site:g2.com "[product]"` | Customer reviews | G2 |
| `site:snyk.io "[product]"` | Security scan | Snyk |
| `"[product]" license` | Licensing | GitHub, docs |
| `"[vendor]" funding OR acquisition` | Viability | Crunchbase, news |

**Discovery Output:**
- Capture all queries used
- Deduplicate URLs
- Rank by authority (official > independent > news)
- Select top 30-40 sources for acquisition

### Phase 4: Firecrawl Acquisition

**Acquisition Plan:**

| URL Type | Method | Extract Fields |
|----------|--------|----------------|
| Vendor security page | Scrape | Certifications, policies, contact |
| GitHub repo main | Crawl | README, SECURITY.md, LICENSE, issues |
| Package registry | Extract | Version, dependencies, vulns, maintainers |
| Review site profile | Scrape | Rating, review count, pros/cons |
| Analyst report | Scrape | Quadrant position, assessment |
| News article | Scrape | Incident details, date, impact |

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
    "vendor_name": "",
    "product_name": "",
    "security_certifications": [],
    "known_vulnerabilities": [],
    "github_stats": {
      "stars": 0,
      "forks": 0,
      "contributors": 0,
      "last_commit": ""
    },
    "package_info": {
      "version": "",
      "license": "",
      "dependencies": 0,
      "vulnerabilities": 0
    },
    "review_summary": {
      "rating": 0.0,
      "review_count": 0
    }
  },
  "extraction_status": "success|partial|failed"
}
```

### Phase 5: Evidence Store

**Store:**
- All raw Firecrawl outputs
- Source metadata (URL, publisher, timestamps)
- Extraction status and notes

**Index by:**
- Vendor name
- Product name
- Source type
- Security-related flags

### Phase 6: Analysis & Verification

**For each finding, produce:**

```yaml
finding:
  title: "[Vendor] Security Posture Assessment"
  summary: "Vendor demonstrates [strong/moderate/weak] security posture with [key observations]"
  evidence:
    - source_url: "https://[vendor]/security"
      supporting_excerpt: "[Exact quote about certifications]"
      relevance: "Security program documentation"
    - source_url: "https://github.com/[vendor]/[repo]/SECURITY.md"
      supporting_excerpt: "[Vulnerability disclosure policy]"
      relevance: "Security maturity indicator"
    - source_url: "https://snyk.io/advisor/[product]"
      supporting_excerpt: "[Vulnerability count]"
      relevance: "Independent security assessment"
  implication: "[What this means for adoption decision]"
  confidence_level: "high"  # or medium, low
  recommended_action: "Proceed / Proceed with conditions / Do not proceed"
  verification_status: "verified"  # or pending, contradicted
  reviewer_status: "human-review-required"
  created_at: "2024-06-14T04:30:00Z"
```

**Verification Rules:**

| Rule | Application |
|------|-------------|
| **Security claims require proof** | Certifications must be verifiable |
| **Prefer official sources** | Vendor docs > independent > news |
| **Cross-reference vulnerabilities** | Multiple sources for vuln counts |
| **Verify certifications** | Check issuer databases when possible |
| **Flag marketing language** | Distinguish claims from evidence |
| **Check recency** | Security info >12 months = stale |
| **Contradictions = review flag** | Conflicting info → human review |

**Assessment Dimensions:**

| Dimension | Evaluation Criteria |
|-----------|---------------------|
| **Security Posture** | Certifications, policies, vulnerability history |
| **Technical Maturity** | Release cadence, docs quality, test coverage |
| **Community/Vendor Health** | Contributors, funding, market presence |
| **Licensing** | License type, compatibility, restrictions |
| **Integration Fit** | API quality, deployment options, scalability |

**Scoring Framework:**

| Score | Security | Maturity | Viability |
|-------|----------|----------|-----------|
| **5** | SOC2 + no vulns | Weekly releases, excellent docs | Well-funded, growing |
| **4** | Security page + few vulns | Regular releases, good docs | Stable, established |
| **3** | Basic security info | Irregular releases, fair docs | Small but stable |
| **2** | Limited security info | Infrequent updates, poor docs | Uncertain viability |
| **1** | No security info | Abandoned, no docs | High risk |

### Phase 7: Output Generation

**Expected Outputs:**

#### 1. Technology Assessment Report
```markdown
# Technology Assessment: [Product/Vendor]

**Assessment Date:** YYYY-MM-DD
**Assessor:** DeerFlow Agent
**Review Status:** Human Review Required

## Executive Summary
[Brief overview with recommendation]

## Vendor Overview
| Attribute | Details |
|-----------|---------|
| Company | [Name] |
| Founded | [Year] |
| Employees | [Count] |
| Funding | [Amount/Stage] |
| Headquarters | [Location] |

## Security Posture
| Criteria | Status | Evidence |
|----------|--------|----------|
| Security Policy | ✅/❌ | [Link] |
| Certifications | ✅/❌ | [List] |
| Vulnerability Disclosure | ✅/❌ | [Link] |
| Known Vulnerabilities | ✅/❌ | [Count] |
| Dependency Security | ✅/❌ | [Audit results] |

**Security Risk:** Low/Medium/High

## Technical Maturity
| Criteria | Assessment |
|----------|------------|
| Release Frequency | [e.g., Weekly] |
| Documentation | [Quality rating] |
| Test Coverage | [Evidence] |
| Issue Resolution | [Avg. time] |
| GitHub Activity | [Stats] |

**Maturity Score:** X/5

## Product Assessment
| Attribute | Details |
|-----------|---------|
| Current Version | [X.X.X] |
| License | [Type] |
| Deployment Options | [Cloud, on-prem, hybrid] |
| API Available | ✅/❌ |
| SDKs | [List] |

## Customer Sentiment
| Platform | Rating | Reviews |
|----------|--------|---------|
| G2 | X.X/5 | X reviews |
| Capterra | X.X/5 | X reviews |
| TrustRadius | X.X/5 | X reviews |

**Common Praise:** [Themes]
**Common Complaints:** [Themes]

## Licensing Analysis
- **Primary License:** [Type]
- **Compatibility:** [Assessment]
- **Commercial Terms:** [If applicable]
- **Restrictions:** [Any limitations]

**Licensing Risk:** Low/Medium/High

## Risk Register
| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| [Risk 1] | Low/Med/High | Low/Med/High | [Action] |
| [Risk 2] | Low/Med/High | Low/Med/High | [Action] |

## Recommendation
**Decision:** Proceed / Proceed with Conditions / Do Not Proceed

**Rationale:**
[Detailed justification]

**Conditions (if applicable):**
1. [Condition 1]
2. [Condition 2]

## Evidence Summary
| Finding | Source | Confidence |
|---------|--------|------------|
| [Finding 1] | [Source] | High/Med/Low |
| [Finding 2] | [Source] | High/Med/Low |
```

#### 2. Maturity Scorecard
```markdown
# Maturity Scorecard: [Product]

| Dimension | Score (1-5) | Evidence Summary |
|-----------|-------------|------------------|
| Security | X/5 | [Brief summary] |
| Stability | X/5 | [Brief summary] |
| Documentation | X/5 | [Brief summary] |
| Community | X/5 | [Brief summary] |
| Vendor Health | X/5 | [Brief summary] |
| **Total** | **X/25** | |

**Interpretation:**
- 21-25: Enterprise-ready
- 16-20: Production-ready with minor gaps
- 11-15: Evaluate carefully, significant gaps
- 6-10: High risk, not recommended
- 1-5: Avoid
```

#### 3. Deployment Recommendation
```markdown
# Deployment Recommendation: [Product]

**Recommendation:** Proceed / Proceed with Caution / Do Not Proceed

## Summary
[One-paragraph rationale]

## Key Factors
### Favoring Adoption
- [Factor 1]
- [Factor 2]

### Concerns
- [Concern 1]
- [Concern 2]

## Implementation Considerations
- **Estimated Effort:** Low/Medium/High
- **Integration Points:** [List]
- **Resource Requirements:** [Estimate]
- **Timeline:** [Estimate]

## Monitoring Requirements
Post-deployment, monitor:
- [What to track 1]
- [What to track 2]
- [What to track 3]

## Review Triggers
Re-evaluate if:
- [Trigger 1]
- [Trigger 2]
```

---

## Skills Used

| Skill | Category | Purpose |
|-------|----------|---------|
| `vendor-due-diligence` | Domain | Security/viability assessment |
| `searxng-query-patterns` | Search | Vendor/product discovery |
| `firecrawl-scrape-patterns` | Acquisition | Vendor site, GitHub extraction |
| `firecrawl-extract-patterns` | Acquisition | Package registry extraction |
| `evidence-scoring` | Verification | Confidence assessment |
| `source-ranking-rules` | Verification | Authority assessment |

---

## Human Review Triggers

**All due diligence assessments require human review.**

**Escalate immediately if:**
- Known security vulnerabilities with exploits
- Vendor has history of breaches
- Certification claims cannot be verified
- Conflicting information across sources
- License incompatibility with intended use
- Vendor viability concerns (funding issues, layoffs)

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2024-06-14 | Initial runbook |
