# Governance & Safety Controls

## Overview

This document defines the governance framework for the Research Automation Stack, ensuring compliance, safety, and quality across all research operations.

---

## Control Areas

### 1. Source Handling

**Requirements:**
- ✅ Preserve source URL for every finding
- ✅ Record source title and publisher
- ✅ Record publication date
- ✅ Record retrieval date
- ✅ Maintain evidence chain (finding → excerpt → source)

**Implementation:**
```yaml
evidence_record:
  source_url: "https://..."
  title: "[Page/article title]"
  publisher: "[Organization]"
  publication_date: "2024-06-13"
  retrieval_date: "2024-06-14"
  supporting_excerpt: "[Direct quote]"
```

**Validation:**
- [ ] All findings have source URLs
- [ ] Dates are recorded (publication + retrieval)
- [ ] Excerpts support the finding
- [ ] Evidence chain is complete

---

### 2. Privacy Controls

**Requirements:**
- ✅ Minimize personal data collection
- ✅ Collect only public, professional information
- ✅ No private/non-public personal data
- ✅ Respect GDPR and privacy regulations
- ✅ Retention limits enforced

**Personal Data Rules:**

| Data Type | Status | Notes |
|-----------|--------|-------|
| Work email | ✅ Permitted | From publication/company sites only |
| Work title | ✅ Permitted | Professional context |
| LinkedIn (public) | ✅ Permitted | Public profiles only |
| Personal email | ❌ Prohibited | Never collect |
| Personal phone | ❌ Prohibited | Never collect |
| Home address | ❌ Prohibited | Never collect |
| Family information | ❌ Prohibited | Never collect |
| Private social media | ❌ Prohibited | Public profiles only |

**Retention Limits:**

| Data Type | Retention | Disposal |
|-----------|-----------|----------|
| Account intelligence (personal) | 12 months or engagement end | Secure delete |
| Media contacts | 90 days with quarterly refresh | Update or delete |
| General research | Per task retention policy | Archive or delete |

**Validation:**
- [ ] Personal data flag set on task
- [ ] Only permitted data types collected
- [ ] Retention schedule applied
- [ ] Privacy review triggered where required

---

### 3. Legal Boundaries

**Requirements:**
- ✅ Do not bypass paywalls
- ✅ Do not bypass authentication
- ✅ Do not bypass CAPTCHAs
- ✅ Do not bypass access controls
- ✅ Respect robots.txt
- ✅ Respect terms of service

**Prohibited Actions:**
- ❌ Credential sharing
- ❌ Circumvention tools
- ❌ Automated bypass of access controls
- ❌ Scraping behind login (without authorization)

**Validation:**
- [ ] All sources are publicly accessible
- [ ] No paywall bypass attempts
- [ ] robots.txt respected
- [ ] ToS compliance verified

---

### 4. Rate Limiting

**Requirements:**
- ✅ Avoid aggressive crawling
- ✅ Respect site boundaries
- ✅ Implement delays between requests
- ✅ Monitor for rate limit responses
- ✅ Back off on 429 responses

**Rate Limit Guidelines:**

| Target | Max Requests/Minute | Delay Between Requests |
|--------|---------------------|------------------------|
| SearXNG | 10 | 6 seconds |
| Firecrawl | Per API limits | As configured |
| General websites | 5 | 12 seconds |
| Government sites | 2 | 30 seconds |

**Validation:**
- [ ] Rate limits configured
- [ ] Delays implemented
- [ ] 429 responses handled
- [ ] No aggressive patterns

---

### 5. Credential Handling

**Requirements:**
- ✅ Never store secrets in prompts
- ✅ Never store secrets in reports
- ✅ Never store secrets in logs
- ✅ Never store secrets in skill files
- ✅ Use secure secret management

**Prohibited:**
- ❌ API keys in code/reports
- ❌ Passwords in any output
- ❌ Tokens in logs
- ❌ Credentials in version control

**Validation:**
- [ ] No secrets in outputs
- [ ] Secret management used
- [ ] Logs reviewed for leaks
- [ ] Skills scanned for credentials

---

### 6. Evidence Quality

**Requirements:**
- ✅ Mark unsupported claims clearly
- ✅ Mark low-confidence findings
- ✅ Distinguish fact vs. inference vs. recommendation
- ✅ Require evidence for important claims
- ✅ Preserve evidence chain

**Confidence Marking:**

| Level | Criteria | Label |
|-------|----------|-------|
| **High** | ≥3 sources including official | `[CONFIDENCE: HIGH]` |
| **Medium** | 2 sources or 1 official | `[CONFIDENCE: MEDIUM]` |
| **Low** | Single unverified source | `[CONFIDENCE: LOW]` |

**Claim Types:**

| Type | Definition | Label |
|------|------------|-------|
| **Fact** | Directly stated, verifiable | `[FACT]` |
| **Inference** | Derived from facts | `[INFERENCE]` |
| **Recommendation** | Suggested action | `[RECOMMENDATION]` |

**Validation:**
- [ ] All claims have confidence scores
- [ ] Unsupported claims marked
- [ ] Fact/inference/recommendation distinguished
- [ ] Evidence chain complete

---

### 7. Human Review

**Requirements:**
- ✅ Escalate high-impact findings
- ✅ Escalate legal/privacy-sensitive outputs
- ✅ Escalate uncertain recommendations
- ✅ Document review decisions
- ✅ Track review status

**Automatic Review Triggers:**

| Trigger | Reviewer | Timeline |
|---------|----------|----------|
| Confidence < 0.50 | Subject matter expert | 24 hours |
| Security vulnerability claims | Security lead | 4 hours |
| Regulatory requirements | Legal/Compliance | 24 hours |
| Personal data involved | Privacy officer | 24 hours |
| External distribution | Comms/Legal | 48 hours |
| Executive leadership audience | Executive team | 48 hours |

**Review Levels:**

| Level | Criteria | Reviewer |
|-------|----------|----------|
| **L1** | Auto-approved (high confidence, internal) | None |
| **L2** | Technical review needed | SME |
| **L3** | Management review | Department head |
| **L4** | Executive/legal review | Legal + Executive |

**Validation:**
- [ ] Review triggers assessed
- [ ] Appropriate reviewer assigned
- [ ] Review documented
- [ ] Changes implemented

---

### 8. Auditability

**Requirements:**
- ✅ Every finding traceable to evidence
- ✅ Evidence chain preserved
- ✅ Processing history logged
- ✅ Access logs maintained
- ✅ Version control for outputs

**Audit Trail:**

```yaml
audit_record:
  task_id: "[ID]"
  finding_id: "[ID]"
  evidence_sources:
    - source_url: "..."
      excerpt: "..."
      retrieved_at: "..."
  processing_history:
    - action: "acquired"
      agent: "firecrawl"
      timestamp: "..."
    - action: "analyzed"
      agent: "deerflow"
      timestamp: "..."
  review_history:
    - reviewer: "[Name]"
      decision: "approved"
      timestamp: "..."
```

**Validation:**
- [ ] All findings have evidence links
- [ ] Processing history complete
- [ ] Access logs enabled
- [ ] Version control applied

---

### 9. Repeatability

**Requirements:**
- ✅ Successful workflows saved as skills
- ✅ Query patterns documented
- ✅ Source lists maintained
- ✅ Templates versioned
- ✅ Lessons learned captured

**Skill Development Loop:**

After every task:
```yaml
skill_review:
  what_worked:
    - "[Query pattern that found good sources]"
  what_failed:
    - "[Query that returned junk]"
  reusable_artifacts:
    - "[Query to add to library]"
  new_skill_created: "[Name]"
  improvements: "[What to improve]"
```

**Validation:**
- [ ] Skill review completed
- [ ] New skills created for repeatable patterns
- [ ] Existing skills updated
- [ ] Templates versioned

---

### 10. Cost Control

**Requirements:**
- ✅ Limit crawl depth
- ✅ Limit query volume
- ✅ Avoid unnecessary re-scraping
- ✅ Cache results
- ✅ Monitor API costs

**Cost Controls:**

| Control | Limit | Enforcement |
|---------|-------|-------------|
| Max sources per task | 30 | Hard limit |
| Max crawl depth | 3 levels | Hard limit |
| Query deduplication | Required | Automatic |
| Result caching | 7 days | Automatic |
| Re-scrape cooldown | 24 hours | Automatic |

**Validation:**
- [ ] Limits configured
- [ ] Caching enabled
- [ ] Duplicate queries blocked
- [ ] Cost monitoring active

---

## Output Standards

### Required Sections

Every completed task must include:

```yaml
final_output:
  executive_summary: "[Clear, decision-ready summary]"
  key_findings:
    - "[Finding 1 with evidence]"
    - "[Finding 2 with evidence]"
  evidence_table:
    - "[Source URL, publisher, date, confidence]"
  implications:
    - "[Operational/commercial/technical impact]"
  recommended_actions:
    - "[Specific, actionable items]"
  confidence_assessment:
    - "[Overall confidence with rationale]"
  gaps_and_limitations:
    - "[Missing data, stale sources, contradictions]"
  next_steps:
    - "[Follow-up actions]"
  skills_created_or_updated:
    - "[Skill names]"
```

### Section Requirements

| Section | Requirement |
|---------|-------------|
| **Executive Summary** | Clear, decision-ready (BLUF format) |
| **Key Findings** | Evidence-backed only, no speculation |
| **Evidence Table** | Source URL, publisher, date, relevance, confidence |
| **Risk/Impact** | Operational, commercial, technical, regulatory, or strategic |
| **Recommendations** | Specific actions, not generic advice |
| **Confidence** | High/Medium/Low with rationale |
| **Gaps** | Missing data, stale sources, failed acquisition, contradictions |

### Quality Checklist

Before distribution:

- [ ] Executive summary is decision-ready
- [ ] All findings have evidence
- [ ] Confidence scores are accurate
- [ ] Recommendations are specific
- [ ] Gaps and limitations documented
- [ ] Review completed (if required)
- [ ] Classification marked
- [ ] Distribution list appropriate

---

## Enforcement

### Automated Checks

| Check | Enforcement |
|-------|-------------|
| Source URL presence | Block output without URLs |
| Confidence score | Require score on all findings |
| Personal data flag | Trigger privacy review |
| Review trigger | Route to reviewer automatically |
| Rate limiting | Enforce delays |

### Manual Reviews

| Review Type | Frequency |
|-------------|-----------|
| Privacy audit | Quarterly |
| Evidence quality | Spot check (10% of tasks) |
| Skill review | Monthly |
| Cost review | Weekly |

### Violations

| Violation | Response |
|-----------|----------|
| Missing evidence | Return to author |
| Privacy violation | Escalate to privacy officer |
| Credential leak | Immediate remediation + review |
| Rate limit abuse | Suspend task, review configuration |

---

## Contacts

| Role | Contact |
|------|---------|
| Privacy Officer | [Name/Email] |
| Legal Counsel | [Name/Email] |
| Security Lead | [Name/Email] |
| Compliance | [Name/Email] |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2024-06-14 | Initial governance framework |
