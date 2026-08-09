# Task Execution Checklist

## Quick Reference for Every Research Task

Use this checklist to ensure compliance with the Operational Mandate.

---

## Phase 1: Plan First ☐

### Intake Block
- [ ] YAML intake block created
- [ ] Title is clear and descriptive
- [ ] Objective is specific
- [ ] PIRs are defined (≥3 key questions)
- [ ] Scope is bounded (geography, sector, timeframe)
- [ ] Output format is specified
- [ ] Handling classification is set
- [ ] Personal data flag is set (true/false)
- [ ] Review requirement is determined

### Research Plan
- [ ] Key questions documented (≥5)
- [ ] Source strategy defined (primary, secondary, official)
- [ ] Query strategy prepared (broad + narrow + domain-specific)
- [ ] Acquisition method selected (scrape/crawl/extract/screenshot)
- [ ] Verification approach defined
- [ ] Expected outputs listed
- [ ] Risks identified
- [ ] Assumptions documented

**Gate:** Do not proceed until intake and plan are complete.

---

## Phase 2: Discover Sources ☐

### SearXNG Execution
- [ ] Multiple query variants executed (≥5)
- [ ] Domain-specific queries used (site: operators)
- [ ] Time-bounding applied (after:/before:)
- [ ] All queries logged
- [ ] Results deduplicated
- [ ] Sources ranked by authority
- [ ] Low-quality sources rejected
- [ ] Selection/rejection reasons documented

### Discovery Output
- [ ] JSON discovery output created
- [ ] Query metadata recorded
- [ ] Source URLs captured
- [ ] Authority scores assigned
- [ ] Relevance scores assigned
- [ ] Selection decisions documented

**Gate:** Do not proceed until ≥10 quality sources identified.

---

## Phase 3: Acquire Evidence ☐

### Firecrawl Execution
- [ ] Correct method selected (scrape/crawl/extract)
- [ ] Extraction options configured
- [ ] Screenshots captured (where relevant)
- [ ] Extraction status recorded
- [ ] Failed extractions logged
- [ ] Recovery attempted for failures

### Acquisition Output
- [ ] JSON acquisition output created
- [ ] Raw markdown preserved
- [ ] Structured JSON extracted (where applicable)
- [ ] Metadata recorded (title, publisher, dates)
- [ ] Extraction time logged
- [ ] Content hash generated

**Gate:** Do not proceed until raw evidence is preserved.

---

## Phase 4: Preserve Raw Material ☐

### Evidence Store
- [ ] Raw Firecrawl outputs stored
- [ ] Source metadata recorded
- [ ] Content hashes generated
- [ ] Retrieval timestamps logged
- [ ] Access controls applied
- [ ] Retention policy assigned

### Audit Trail
- [ ] Processing history started
- [ ] Agent actions logged
- [ ] Evidence chain initiated

**Gate:** Do not analyze until raw evidence is immutable.

---

## Phase 5: Verify Findings ☐

### Analysis
- [ ] Each finding has title and summary
- [ ] Evidence chain complete (finding → excerpt → source)
- [ ] Confidence scores calculated
- [ ] Confidence levels assigned (High/Medium/Low)
- [ ] Fact/Inference/Recommendation distinguished
- [ ] Implications documented
- [ ] Recommended actions specified

### Verification
- [ ] Official sources prioritized
- [ ] Cross-references completed
- [ ] Contradictions flagged
- [ ] Stale sources identified (>threshold age)
- [ ] Verification status assigned (verified/pending/contradicted)
- [ ] Reviewer status assigned (auto/human)

**Gate:** Do not proceed until all findings verified.

---

## Phase 6: Produce Structured Output ☐

### Report Generation
- [ ] Mode-specific template used
- [ ] Executive summary (BLUF) included
- [ ] Key findings documented
- [ ] Evidence table complete
- [ ] Implications assessed
- [ ] Recommendations specific and actionable
- [ ] Confidence assessment included
- [ ] Gaps and limitations documented
- [ ] Next steps defined

### Quality Check
- [ ] All claims have citations
- [ ] All findings have confidence scores
- [ ] Fact/Inference/Recommendation labeled
- [ ] Contradictions flagged
- [ ] Stale sources noted
- [ ] Personal data handled correctly
- [ ] Classification marked

**Gate:** Do not distribute until quality check passed.

---

## Phase 7: Update Reusable Skills ☐

### Skill Review
- [ ] Skill review completed (YAML format)
- [ ] What worked documented (≥3 items)
- [ ] What failed documented (≥3 items)
- [ ] Reusable artifacts identified
- [ ] New skill created (if applicable)
- [ ] Existing skill updated (if applicable)
- [ ] Improvements recommended

### Skill Library
- [ ] New skill file created (if applicable)
- [ ] Existing skill updated (if applicable)
- [ ] Skill version incremented
- [ ] Change log updated

**Gate:** Task not complete until skill review done.

---

## Phase 8: Record Gaps & Improvements ☐

### Gap Analysis
- [ ] Missing data documented
- [ ] Failed acquisitions listed
- [ ] Unanswered PIRs identified
- [ ] Source gaps noted
- [ ] Tool limitations recorded

### Improvement Recommendations
- [ ] Process improvements suggested
- [ ] Query improvements suggested
- [ ] Tool configuration improvements suggested
- [ ] Template improvements suggested
- [ ] Training needs identified

### Handoff
- [ ] Next steps assigned
- [ ] Follow-up tasks created
- [ ] Knowledge transferred (if team task)

**Gate:** Task not closed until improvements recorded.

---

## Governance Compliance ☐

### Privacy
- [ ] Personal data minimized
- [ ] Only public/professional data collected
- [ ] No private information gathered
- [ ] Retention policy applied
- [ ] Privacy review triggered (if required)

### Legal
- [ ] No paywall bypass attempted
- [ ] No auth circumvention
- [ ] robots.txt respected
- [ ] ToS compliance verified

### Security
- [ ] No credentials in outputs
- [ ] No secrets in logs
- [ ] Rate limits respected
- [ ] Access controls applied

### Audit
- [ ] Evidence chain complete
- [ ] Processing history logged
- [ ] Review decisions documented
- [ ] Version control applied

---

## Human Review ☐

### Trigger Assessment
- [ ] Confidence <0.50 findings → SME review
- [ ] Security claims → Security lead review
- [ ] Regulatory claims → Legal/Compliance review
- [ ] Personal data → Privacy officer review
- [ ] External distribution → Comms/Legal review
- [ ] Executive audience → Executive review

### Review Execution
- [ ] Reviewer assigned
- [ ] Review request sent
- [ ] Review feedback received
- [ ] Changes implemented
- [ ] Re-review completed (if required)
- [ ] Final approval granted

**Gate:** Do not distribute until review approved.

---

## Final Sign-Off ☐

### Quality Assurance
- [ ] All 8 phases complete
- [ ] All gates passed
- [ ] Governance compliance verified
- [ ] Human review approved (if required)
- [ ] Output quality verified
- [ ] Skills updated
- [ ] Improvements recorded

### Distribution
- [ ] Classification confirmed
- [ ] Distribution list confirmed
- [ ] Delivery method selected
- [ ] Delivery confirmed
- [ ] Feedback mechanism enabled

### Closure
- [ ] Task status set to "complete"
- [ ] Metrics recorded
- [ ] Lessons learned captured
- [ ] Archive scheduled

---

## Quick Reference: Common Failure Modes

| Failure | Prevention |
|---------|------------|
| Missing evidence | Require source URL for every finding |
| No confidence score | Block output without scores |
| Undated claims | Require publication + retrieval dates |
| Hidden contradictions | Explicit contradiction section |
| Privacy violations | Personal data checklist |
| Rate limit violations | Configured delays + monitoring |
| Skill stagnation | Mandatory skill review per task |

---

## Emergency Contacts

| Issue | Contact |
|-------|---------|
| Privacy concern | Privacy Officer |
| Legal question | Legal Counsel |
| Security incident | Security Lead |
| Quality dispute | Stack Owner |
| Tool failure | Technical Lead |

---

**Checklist Version:** 1.0
**Effective Date:** 2024-06-14
**Required for:** All research tasks

---

**Remember:** This checklist is not optional. It is the operational manifestation of the mandate.

**No shortcuts. No exceptions. Every task, every time.**
