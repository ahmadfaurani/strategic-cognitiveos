# Tender & Opportunity Monitoring Mode

## Purpose
Systematic discovery, tracking, and analysis of procurement opportunities, RFPs, grants, and tenders.

## Trigger Patterns
- "Monitor tenders for [category]"
- "RFP alerts [sector]"
- "Grant opportunities [domain]"
- "Procurement tracking [agency]"
- "Bid/no-bid recommendation [opportunity]"
- "Tender pipeline [timeframe]"

## Workflow Steps

### 1. Intake & Scoping

```yaml
task:
  title: "Tender Monitoring: [Category/Sector]"
  objective: "Identify and assess procurement opportunities matching criteria"
  priority_intelligence_requirements:
    - "What tenders match our capabilities?"
    - "What are submission deadlines?"
    - "What are evaluation criteria?"
    - "What is the competitive landscape?"
    - "What is our win probability?"
  scope:
    geography: "[Countries/Regions]"
    sector: "[Industry vertical]"
    timeframe: "Next 90 days"
    language: "English"
    source_types:
      - government_procurement_portals
      - ungm
      - industry_specific_portals
      - company_websites
      - grant_databases
    output_required: "Tender alert + opportunity tracker + bid/no-bid memo"
    handling_classification: "Internal"
    personal_data_involved: false
    review_required: true
```

### 2. Research Planning

```yaml
research_plan:
  key_questions:
    - "What opportunities match our capabilities?"
    - "What are the submission requirements?"
    - "What is the evaluation methodology?"
    - "Who are the likely competitors?"
    - "What is the decision timeline?"
  source_strategy:
    primary:
      - Government procurement portals (sam.gov, tenders.gov, etc.)
      - UNGM (United Nations Global Marketplace)
      - Industry-specific tender portals
      - Agency procurement pages
    secondary:
      - Trade publications
      - Industry association boards
      - Consultant/intermediary sites
    official:
      - Official gazettes
      - Regulatory procurement notices
      - Budget appropriation documents
    commercial:
      - BidNet
      - GovWin
      - Tender tracking services
  query_strategy:
    - "RFP [category] 2024"
    - "tender [service type]"
    - "procurement [solution]"
    - "grant [domain] application"
    - "site:sam.gov \"[keyword]\""
    - "site:ungm.org \"[keyword]\""
    - "\"request for proposals\" [sector]"
    - "\"invitation to tender\" [category]"
  acquisition_strategy:
    - Scrape: Individual tender notices
    - Crawl: Portal category pages
    - Extract: Structured fields (deadline, value, criteria)
    - Batch: Multiple known portal URLs
  verification_strategy:
    - Confirm deadlines on official portal
    - Verify contact information
    - Cross-reference opportunity details
  expected_outputs:
    - Tender alert (per opportunity)
    - Opportunity tracker (consolidated)
    - Bid/no-bid memo (per priority opp)
    - Compliance checklist
    - Proposal outline
  risks:
    - Missed deadlines
    - Incomplete requirements
    - Outdated postings
    - Ambiguous evaluation criteria
  assumptions:
    - Posted tenders are active
    - Deadlines are accurate
    - Budget ranges are indicative
```

### 3. SearXNG Discovery

**Query Categories:**

**General Tender Discovery:**
```
"RFP [category] 2024"
"tender [service type]"
"procurement [solution]"
"request for proposals [sector]"
"invitation to tender [category]"
```

**Government Portals:**
```
site:sam.gov "[keyword]"
site:tenders.gov "[keyword]"
site:findtenders.gov.uk "[keyword]"
site:europa.eu "ted tender"
site:ungm.org "[keyword]"
```

**Grant Opportunities:**
```
"grant [domain] 2024"
"funding opportunity [sector]"
"RFA [topic]"
"NOFO [program]"
site:grants.gov "[keyword]"
site:ec.europa.eu "call for proposals"
```

**Industry-Specific:**
```
"[industry] procurement portal"
"[sector] tender board"
"[vertical] RFP opportunities"
```

**Agency-Specific:**
```
"[agency name] procurement"
"[agency name] RFP"
"[agency name] contracting opportunities"
```

### 4. Firecrawl Acquisition

**Target Pages:**

| Page Type | Method | Purpose |
|-----------|--------|---------|
| Tender Notice | Scrape | Full requirements, deadlines |
| Portal Search Results | Crawl | Multiple opportunities |
| Amendment/Corrigendum | Scrape | Updated requirements |
| Award Notice | Scrape | Historical win data |
| Agency Procurement Page | Crawl | Pipeline visibility |

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
    "tender_id": "",
    "title": "",
    "issuing_agency": "",
    "category": "",
    "description": "",
    "submission_deadline": "",
    "pre_bid_deadline": "",
    "estimated_value": "",
    "currency": "",
    "contract_duration": "",
    "eligibility_criteria": [],
    "evaluation_criteria": [],
    "documents": [],
    "contact_info": {}
  },
  "screenshot_path": "",
  "extraction_status": "success|partial|failed",
  "notes": ""
}
```

### 5. Analysis Framework

#### Opportunity Assessment Dimensions
- **Fit:** Does it match our capabilities?
- **Value:** Is the opportunity size appropriate?
- **Timing:** Can we meet the deadline?
- **Competition:** Who else is likely to bid?
- **Win Probability:** What are our chances?
- **Strategic Value:** Does it advance our goals?
- **Resource Requirement:** What will it take to bid?

#### Bid/No-Bid Criteria
| Factor | Weight | Score (1-5) | Weighted Score |
|--------|--------|-------------|----------------|
| Capability Fit | 25% | | |
| Win Probability | 20% | | |
| Strategic Value | 15% | | |
| Resource Availability | 15% | | |
| Client Relationship | 10% | | |
| Competitive Position | 10% | | |
| Profitability | 5% | | |
| **Total** | **100%** | | **/5** |

**Decision Threshold:**
- **≥4.0:** Strong Bid recommendation
- **3.0-3.9:** Consider Bid (review further)
- **<3.0:** No-Bid recommendation

#### Compliance Checklist
- [ ] Eligibility criteria met
- [ ] All required documents identified
- [ ] Submission format understood
- [ ] Deadline confirmed (timezone)
- [ ] Pre-bid questions deadline noted
- [ ] Site visit requirements (if any)
- [ ] Bond/guarantee requirements
- [ ] Insurance requirements
- [ ] Certification requirements
- [ ] Joint venture rules (if applicable)

### 6. Output Generation

#### Tender Alert
```markdown
# TENDER ALERT: [Tender ID/Title]

**Issued:** YYYY-MM-DD
**Deadline:** YYYY-MM-DD HH:MM [Timezone]
**Priority:** High/Medium/Low

## Overview
| Field | Details |
|-------|---------|
| **Tender ID** | [ID] |
| **Title** | [Title] |
| **Issuing Agency** | [Agency] |
| **Category** | [Category] |
| **Location** | [Country/Region] |

## Opportunity Summary
[Brief description of what's being procured]

## Key Details
| Detail | Value |
|--------|-------|
| **Estimated Value** | [Amount/Currency] |
| **Contract Duration** | [Period] |
| **Submission Deadline** | [Date/Time] |
| **Pre-Bid Deadline** | [Date/Time] |
| **Site Visit** | [Yes/No + Date] |

## Eligibility Criteria
- [Criterion 1]
- [Criterion 2]
- [Criterion 3]

## Evaluation Criteria
| Criterion | Weight |
|-----------|--------|
| [Technical Approach] | XX% |
| [Experience] | XX% |
| [Price] | XX% |
| [Other] | XX% |

## Required Documents
- [Document 1]
- [Document 2]
- [Document 3]

## Submission Details
- **Method:** [Online/Physical]
- **Portal:** [URL]
- **Contact:** [Name, Email]

## Recommended Action
[Bid / Consider / No-Bid] - [Brief rationale]

## Next Steps
1. [Action + Owner + Deadline]
2. [Action + Owner + Deadline]
3. [Action + Owner + Deadline]

## Source
[URL to tender notice] - [Confidence]
```

#### Opportunity Tracker
```markdown
# Tender Opportunity Tracker

**Last Updated:** YYYY-MM-DD
**Reporting Period:** [Date Range]

## Active Opportunities

| ID | Title | Agency | Category | Deadline | Value | Status | Priority |
|----|-------|--------|----------|----------|-------|--------|----------|
| [ID] | [Title] | [Agency] | [Cat] | YYYY-MM-DD | $XM | Open | High |
| [ID] | [Title] | [Agency] | [Cat] | YYYY-MM-DD | $XM | Open | Medium |

## Pipeline Summary
| Status | Count | Total Value |
|--------|-------|-------------|
| Open | X | $XM |
| Pre-Bid (questions due) | X | $XM |
| Proposal Due (this week) | X | $XM |
| Submitted (pending) | X | $XM |
| Awarded | X | $XM |
| Lost | X | $XM |

## Upcoming Deadlines (Next 14 Days)
| Date | Tender ID | Title | Action Required |
|------|-----------|-------|-----------------|
| YYYY-MM-DD | [ID] | [Title] | Submit proposal |
| YYYY-MM-DD | [ID] | [Title] | Pre-bid questions |

## Win/Loss Analysis (Last 90 Days)
| Metric | Value |
|--------|-------|
| Tenders Pursued | X |
| Proposals Submitted | X |
| Wins | X |
| Losses | X |
| Win Rate | XX% |
| Total Value Won | $XM |

## By Category
| Category | Pursued | Wins | Win Rate |
|----------|---------|------|----------|
| [Category 1] | X | X | XX% |
| [Category 2] | X | X | XX% |

## By Agency
| Agency | Pursued | Wins | Win Rate |
|--------|---------|------|----------|
| [Agency 1] | X | X | XX% |
| [Agency 2] | X | X | XX% |
```

#### Bid/No-Bid Memo
```markdown
# Bid/No-Bid Recommendation: [Tender ID/Title]

**Date:** YYYY-MM-DD
**Prepared By:** [Name]
**Recommendation:** BID / NO-BID / CONSIDER

## Executive Summary
[Brief rationale for recommendation]

## Opportunity Overview
| Field | Details |
|-------|---------|
| **Tender ID** | [ID] |
| **Title** | [Title] |
| **Agency** | [Agency] |
| **Deadline** | [Date] |
| **Value** | [Amount] |

## Assessment

### Capability Fit (Weight: 25%)
**Score:** X/5
[Assessment of how well requirements match capabilities]

### Win Probability (Weight: 20%)
**Score:** X/5
[Assessment of competitive position, relationships, differentiators]

### Strategic Value (Weight: 15%)
**Score:** X/5
[Assessment of strategic importance, reference value, market entry]

### Resource Availability (Weight: 15%)
**Score:** X/5
[Assessment of team availability, capacity, timeline feasibility]

### Client Relationship (Weight: 10%)
**Score:** X/5
[Assessment of existing relationship, past performance, incumbent status]

### Competitive Position (Weight: 10%)
**Score:** X/5
[Assessment of likely competitors, our differentiation]

### Profitability (Weight: 5%)
**Score:** X/5
[Assessment of margin potential, pricing pressure]

## Weighted Score Calculation
| Factor | Weight | Score | Weighted |
|--------|--------|-------|----------|
| Capability Fit | 25% | X/5 | X.XX |
| Win Probability | 20% | X/5 | X.XX |
| Strategic Value | 15% | X/5 | X.XX |
| Resource Availability | 15% | X/5 | X.XX |
| Client Relationship | 10% | X/5 | X.XX |
| Competitive Position | 10% | X/5 | X.XX |
| Profitability | 5% | X/5 | X.XX |
| **TOTAL** | **100%** | | **X.XX/5** |

## Recommendation
**Score:** X.XX/5 → **BID / NO-BID / CONSIDER**

### Rationale
[Detailed explanation of recommendation]

### If BID: Key Success Factors
1. [Critical success factor 1]
2. [Critical success factor 2]
3. [Critical success factor 3]

### If NO-BID: Reasons
- [Reason 1]
- [Reason 2]
- [Reason 3]

### If CONSIDER: Questions to Resolve
1. [Question 1] - [Owner] - [Deadline]
2. [Question 2] - [Owner] - [Deadline]

## Resource Requirements (If Bid)
| Resource | Requirement | Availability |
|----------|-------------|--------------|
| Proposal Manager | [Name/Role] | [Status] |
| Technical Lead | [Name/Role] | [Status] |
| Pricing Lead | [Name/Role] | [Status] |
| Subject Experts | [Count] | [Status] |

## Timeline (If Bid)
| Milestone | Deadline | Owner |
|-----------|----------|-------|
| Kickoff | YYYY-MM-DD | [Name] |
| Outline Complete | YYYY-MM-DD | [Name] |
| Draft Complete | YYYY-MM-DD | [Name] |
| Internal Review | YYYY-MM-DD | [Name] |
| Final Submission | YYYY-MM-DD | [Name] |

## Approval
| Role | Name | Decision | Date |
|------|------|----------|------|
| Proposal Manager | [Name] | | |
| Business Unit Lead | [Name] | | |
| Finance | [Name] | | |
```

#### Compliance Checklist
```markdown
# Compliance Checklist: [Tender ID/Title]

**Tender ID:** [ID]
**Deadline:** YYYY-MM-DD
**Prepared By:** [Name]

## Eligibility Requirements
| Requirement | Status | Evidence | Notes |
|-------------|--------|----------|-------|
| [Requirement 1] | ✅/❌ | [Document] | [Notes] |
| [Requirement 2] | ✅/❌ | [Document] | [Notes] |
| [Requirement 3] | ✅/❌ | [Document] | [Notes] |

## Mandatory Documents
| Document | Required | Status | Owner | Due |
|----------|----------|--------|-------|-----|
| Company Registration | Yes | ✅ | [Name] | YYYY-MM-DD |
| Financial Statements | Yes | ✅ | [Name] | YYYY-MM-DD |
| Technical Proposal | Yes | 🔄 | [Name] | YYYY-MM-DD |
| Price Proposal | Yes | ⏳ | [Name] | YYYY-MM-DD |
| References | Yes | ⏳ | [Name] | YYYY-MM-DD |
| [Other] | [Yes/No] | Status | [Name] | Date |

## Submission Requirements
| Requirement | Status | Notes |
|-------------|--------|-------|
| Submission Format | ✅/❌ | [Online portal / Physical] |
| File Format | ✅/❌ | [PDF, Word, etc.] |
| File Naming Convention | ✅/❌ | [As specified] |
| Page Limits | ✅/❌ | [Confirmed] |
| Font/Formatting | ✅/❌ | [As specified] |
| Signed Declarations | ✅/❌ | [If required] |

## Pre-Submission Requirements
| Requirement | Deadline | Status | Owner |
|-------------|----------|--------|-------|
| Site Visit | YYYY-MM-DD | ✅/❌ | [Name] |
| Pre-Bid Questions | YYYY-MM-DD | ✅/❌ | [Name] |
| Registration on Portal | YYYY-MM-DD | ✅/❌ | [Name] |
| Bid Bond/Security | YYYY-MM-DD | ✅/❌ | [Name] |

## Certification/Insurance
| Requirement | Required | Status | Expiry |
|-------------|----------|--------|--------|
| ISO 9001 | Yes/No | ✅/❌ | YYYY-MM-DD |
| ISO 27001 | Yes/No | ✅/❌ | YYYY-MM-DD |
| Professional Indemnity | Yes/No | ✅/❌ | YYYY-MM-DD |
| [Other] | Yes/No | Status | Date |

## Final Compliance Check
| Check | Status | Verified By |
|-------|--------|-------------|
| All mandatory sections complete | ✅/❌ | [Name] |
| Page count within limits | ✅/❌ | [Name] |
| All attachments included | ✅/❌ | [Name] |
| Pricing math verified | ✅/❌ | [Name] |
| Contact information correct | ✅/❌ | [Name] |
| Submission before deadline | ✅/❌ | [Name] |

## Overall Compliance Status
**READY TO SUBMIT** / **NOT READY - GAPS REMAINING**

### Outstanding Gaps
| Gap | Action Required | Owner | Deadline |
|-----|-----------------|-------|----------|
| [Gap 1] | [Action] | [Name] | YYYY-MM-DD |
| [Gap 2] | [Action] | [Name] | YYYY-MM-DD |
```

#### Proposal Outline
```markdown
# Proposal Outline: [Tender ID/Title]

**Tender ID:** [ID]
**Prepared By:** [Name]
**Version:** 1.0

## Executive Summary
- [Opening: Understanding of requirement]
- [Our solution overview]
- [Key differentiators]
- [Value proposition]
- [Call to action]

## Section 1: Understanding of Requirements
1.1 Background and Context
1.2 Statement of Requirements
1.3 Key Challenges Identified
1.4 Success Criteria

## Section 2: Proposed Solution
2.1 Solution Overview
2.2 Technical Approach
2.3 Methodology
2.4 Deliverables
2.5 Timeline/Schedule
2.6 Quality Assurance

## Section 3: Company Profile
3.1 Company Overview
3.2 Relevant Experience
3.3 Case Studies/References
3.4 Certifications/Compliance

## Section 4: Project Team
4.1 Organizational Structure
4.2 Key Personnel (CVs)
4.3 Roles and Responsibilities
4.4 Resource Allocation

## Section 5: Implementation Plan
5.1 Phase 1: [Name]
5.2 Phase 2: [Name]
5.3 Phase 3: [Name]
5.4 Risk Management
5.5 Change Management

## Section 6: Pricing
6.1 Pricing Summary
6.2 Detailed Breakdown
6.3 Assumptions
6.4 Payment Terms
6.5 Optional Items

## Section 7: Value-Add
7.1 Differentiators
7.2 Additional Benefits
7.3 Innovation
7.4 Long-Term Partnership

## Appendices
- Appendix A: CVs of Key Personnel
- Appendix B: Case Studies
- Appendix C: Certifications
- Appendix D: Technical Specifications
- Appendix E: References

## Compliance Matrix
| RFP Requirement | Section Reference | Page |
|-----------------|-------------------|------|
| [Requirement 1] | Section X.X | XX |
| [Requirement 2] | Section X.X | XX |
| [Requirement 3] | Section X.X | XX |

## Review Schedule
| Review | Date | Reviewers |
|--------|------|-----------|
| Outline Review | YYYY-MM-DD | [Names] |
| Draft Review | YYYY-MM-DD | [Names] |
| Final Review | YYYY-MM-DD | [Names] |
```

## Confidence Scoring

| Score | Criteria |
|-------|----------|
| High | Official procurement portal, complete details, verified contact |
| Medium | Reputable aggregator, most details present |
| Low | Third-party listing, incomplete information, unverified |

## Skill Library Entries
- `tender/monitoring`
- `tender/alert-generation`
- `tender/bid-no-bid-analysis`
- `tender/compliance-checklist`
- `tender/proposal-outline`
- `tender/grant-tracking`

## Integration Points
- CRM (opportunity tracking)
- Proposal management software
- Document management systems
- Calendar/deadline reminders
- Team collaboration platforms

## Portal Watchlist

### United States
- SAM.gov (federal)
- State procurement portals
- Local government portals

### European Union
- TED (Tenders Electronic Daily)
- National portals (FindTenders UK, etc.)

### United Nations
- UNGM (United Nations Global Marketplace)
- Agency-specific portals (UNDP, UNICEF, etc.)

### International
- World Bank eConsultant
- Asian Development Bank
- African Development Bank
