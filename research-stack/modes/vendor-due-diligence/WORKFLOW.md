# Vendor & Technology Due Diligence Mode

## Purpose
Systematic evaluation of vendors, products, and technologies for security, viability, and integration fit.

## Trigger Patterns
- "Evaluate [product/tool] for security"
- "Vendor assessment: [company name]"
- "Build vs buy analysis for [capability]"
- "GitHub repo review: [repo]"
- "Open-source license check: [project]"

## Workflow Steps

### 1. Due Diligence Scope Definition
```
Input: Target vendor/product/technology
Output: Assessment framework
  - Security posture
  - Technical maturity
  - Community/vendor health
  - Licensing compliance
  - Integration complexity
  - Total cost of ownership
```

### 2. Discovery Queries (SearXNG)

**Vendor/Company Research:**
```
"[company] security incident"
"[company] data breach"
"[company] compliance certification"
"[company] funding" site:crunchbase.com
"[company] reviews" site:g2.com
"[company] glassdoor"
```

**Product/Tool Assessment:**
```
"[product] security review"
"[product] vulnerability"
"[product] vs [competitor]"
"[product] deployment guide"
```

**GitHub Repository Analysis:**
```
site:github.com "[org]/[repo]"
"[repo] security issues"
"[repo] dependencies"
"[repo] license"
```

**Open-Source Intelligence:**
```
"[project] npm audit"
"[project] snyk vulnerabilities"
"[project] ossf scorecard"
```

### 3. Source Prioritization
| Source Type | Examples | Weight |
|-------------|----------|--------|
| Official Docs | Vendor security pages, docs | High |
| Code Repos | GitHub, GitLab | High |
| Independent Reviews | G2, Capterra, analyst reports | Medium-High |
| Security Databases | Snyk, npm audit, OSS Index | High |
| Community | Stack Overflow, Reddit | Medium |
| News | Tech media, blogs | Medium |

### 4. Firecrawl Extraction Targets

**Vendor Security Pages:**
```json
{
  "url": "https://[vendor]/security",
  "options": {
    "formats": ["markdown", "json"],
    "screenshot": true,
    "onlyMainContent": true
  }
}
```

**GitHub Repository:**
```json
{
  "url": "https://github.com/[org]/[repo]",
  "options": {
    "formats": ["markdown"],
    "screenshot": false,
    "onlyMainContent": true,
    "includeTags": ["README", "SECURITY.md", "LICENSE"]
  }
}
```

**Package Registry Pages:**
```json
{
  "url": "https://npmjs.com/package/[pkg]",
  "options": {
    "formats": ["json"],
    "extract": {
      "version": "string",
      "license": "string",
      "dependencies": "array",
      "vulnerabilities": "array",
      "maintainers": "array",
      "lastUpdate": "date"
    }
  }
}
```

### 5. Analysis Framework

#### Security Posture
- [ ] Security policy present (SECURITY.md)
- [ ] Vulnerability disclosure process
- [ ] Known CVEs/vulnerabilities
- [ ] Dependency security (npm audit, pip audit)
- [ ] Code signing / supply chain security
- [ ] Compliance certifications (SOC2, ISO27001, etc.)

#### Technical Maturity
- [ ] Release frequency and consistency
- [ ] Version stability (semver compliance)
- [ ] Documentation quality
- [ ] Test coverage evidence
- [ ] Issue resolution time
- [ ] Breaking change management

#### Community/Vendor Health
- [ ] Number of contributors
- [ ] Community engagement (issues, PRs, discussions)
- [ ] Vendor funding/backing
- [ ] Market presence and longevity
- [ ] Customer references/case studies

#### Licensing
- [ ] License type (MIT, Apache, GPL, etc.)
- [ ] License compatibility with intended use
- [ ] Dependency license audit
- [ ] Commercial licensing requirements

#### Integration Fit
- [ ] API availability and quality
- [ ] SDK/library support
- [ ] Authentication methods
- [ ] Deployment options (cloud, on-prem, hybrid)
- [ ] Scalability considerations

### 6. Output Generation

#### Technology Assessment Report
```markdown
# Technology Assessment: [Product/Tool]

**Assessment Date:** YYYY-MM-DD
**Assessor:** DeerFlow Agent
**Overall Recommendation:** [Proceed / Proceed with Caution / Do Not Proceed]

## Executive Summary
[Brief overview of findings and recommendation]

## Security Posture
| Criteria | Status | Notes |
|----------|--------|-------|
| Security Policy | ✅/❌ | [Details] |
| Known Vulnerabilities | ✅/❌ | [CVE list if any] |
| Dependency Security | ✅/❌ | [Audit results] |
| Compliance | ✅/❌ | [Certifications] |

**Security Risk:** Low/Medium/High

## Technical Maturity
| Criteria | Assessment |
|----------|------------|
| Release Frequency | [e.g., Weekly] |
| Documentation | [Quality rating] |
| Test Coverage | [Evidence] |
| Issue Resolution | [Avg. time] |

**Maturity Score:** X/10

## Vendor/Community Health
- **Contributors:** [Count]
- **Backing:** [Vendor/Community]
- **Market Presence:** [Assessment]
- **Longevity:** [Years in market]

**Viability Risk:** Low/Medium/High

## Licensing
- **Primary License:** [License type]
- **Compatibility:** [Assessment]
- **Commercial Terms:** [If applicable]

**Licensing Risk:** Low/Medium/High

## Integration Assessment
- **API Quality:** [Rating]
- **Deployment Options:** [List]
- **Scalability:** [Assessment]
- **Estimated Effort:** [Low/Medium/High]

## Risk Register
| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| [Risk 1] | Low/Med/High | Low/Med/High | [Action] |
| [Risk 2] | Low/Med/High | Low/Med/High | [Action] |

## Recommendation
[Detailed recommendation with justification]

## Evidence
- [Source 1] - [Confidence]
- [Source 2] - [Confidence]
```

#### Maturity Scorecard
```markdown
| Dimension | Score (1-5) | Evidence |
|-----------|-------------|----------|
| Security | X/5 | [Summary] |
| Stability | X/5 | [Summary] |
| Documentation | X/5 | [Summary] |
| Community | X/5 | [Summary] |
| Vendor Health | X/5 | [Summary] |
| **Total** | **X/25** | |
```

#### Deployment Recommendation
```markdown
# Deployment Recommendation: [Product]

**Recommendation:** Proceed / Proceed with Caution / Do Not Proceed

## Rationale
[Key factors driving recommendation]

## Conditions (if "Proceed with Caution")
1. [Condition 1]
2. [Condition 2]

## Implementation Considerations
- [Consideration 1]
- [Consideration 2]

## Monitoring Requirements
- [What to monitor post-deployment]
```

## Confidence Scoring

| Score | Criteria |
|-------|----------|
| High | ≥3 independent sources, official documentation, code review |
| Medium | 2 sources or vendor claims with some verification |
| Low | Vendor claims only, limited independent verification |

## Skill Library Entries
- `due-diligence/vendor-assessment`
- `due-diligence/github-repo-review`
- `due-diligence/license-audit`
- `due-diligence/build-vs-buy`
- `due-diligence/oss-security-check`

## Integration Points
- Procurement workflow
- Security review board
- Architecture review board
- Vendor risk management system
