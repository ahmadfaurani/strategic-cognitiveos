# Human Review Triggers

## Purpose
Define when research outputs must be reviewed by a human before distribution or action.

---

## Automatic Review Triggers

### By Confidence Level

| Trigger | Threshold | Rationale |
|---------|-----------|-----------|
| **Low confidence finding** | Confidence < 0.50 | Insufficient certainty |
| **Medium confidence, high impact** | Confidence 0.50-0.70 + high impact | Risk of incorrect decision |
| **Unverified critical claim** | Verification status = pending | Needs confirmation |
| **Contradicted finding** | Verification status = contradicted | Requires judgment |

### By Content Type

| Content Type | Review Required | Reviewer Role |
|--------------|-----------------|---------------|
| **Security vulnerabilities** | Always | Security lead |
| **Active exploitation claims** | Always | Security lead |
| **Regulatory requirements** | Always | Legal/Compliance |
| **Financial impact assessments** | Always | Finance/Business lead |
| **M&A or funding claims** | Always | Business lead |
| **Executive misconduct allegations** | Always | Legal + Comms |
| **Breach/incident reports** | Always | Security + Comms |
| **Litigation mentions** | Always | Legal |

### By Data Quality

| Issue | Review Required | Reason |
|-------|-----------------|--------|
| **Stale source as only evidence** | Yes | Currency verification needed |
| **Single source for critical claim** | Yes | Corroboration needed |
| **Snippet-only evidence** | Yes | Full content verification |
| **Conflicting sources** | Yes | Resolution needed |
| **Anonymous source claims** | Yes | Credibility assessment |
| **Paywalled/unverifiable source** | Yes | Alternative sourcing |

### By Personal Data

| Data Type | Review Required | Reviewer Role |
|-----------|-----------------|---------------|
| **Personal data collected** | Yes | Privacy officer |
| **EU subject data** | Yes | DPO (if applicable) |
| **Special category data** | Yes + Stop processing | Privacy officer + Legal |
| **Large-scale collection (>100 individuals)** | Yes | Privacy officer |
| **Contact information for outreach** | Yes | Comms/PR lead |

### By Distribution Scope

| Distribution | Review Required | Reviewer Role |
|--------------|-----------------|---------------|
| **Executive leadership** | Yes | Comms/Chief of Staff |
| **External parties** | Yes | Legal + Comms |
| **Public release** | Yes + Legal review | Legal + Comms + Executive |
| **Regulatory submission** | Yes | Legal + Compliance |
| **Board materials** | Yes | Executive team |

### By Mode

| Mode | Automatic Review | Reviewer |
|------|------------------|----------|
| **Cyber Threat Intel** | Critical CVEs, active exploitation | Security lead |
| **Vendor Due Diligence** | All assessments | Procurement + Security |
| **Competitive Intel** | Market-moving intel | Business lead |
| **Regulatory Monitoring** | New requirements, deadlines | Legal/Compliance |
| **Account Intelligence** | All briefs | Sales/Account lead |
| **Tender Monitoring** | Bid/no-bid recommendations | Bid manager |
| **Media Registry** | Contact lists | Comms/PR lead |

---

## Review Levels

### Level 1: Auto-Approved
**Criteria:**
- All findings confidence ≥ 0.70
- No personal data
- Internal distribution only
- No high-impact claims
- No contradictions

**Process:** No review required, direct distribution

### Level 2: Technical Review
**Criteria:**
- Technical accuracy check needed
- Moderate confidence findings
- Some data quality flags

**Reviewer:** Subject matter expert
**Timeline:** Within 4 hours

### Level 3: Management Review
**Criteria:**
- Business impact
- External distribution
- Personal data involved
- Medium-risk findings

**Reviewer:** Department head / manager
**Timeline:** Within 24 hours

### Level 4: Executive/Legal Review
**Criteria:**
- High business impact
- Regulatory implications
- Legal risk
- Public/external release
- Sensitive allegations

**Reviewer:** Legal + Executive team
**Timeline:** Within 48 hours (or expedited for urgent)

---

## Review Checklist

### For Reviewers

**Before approving, verify:**

- [ ] **Accuracy:** Claims match source evidence
- [ ] **Confidence:** Scores are appropriate
- [ ] **Completeness:** All key questions answered
- [ ] **Clarity:** Fact vs. inference vs. recommendation distinguished
- [ ] **Citations:** All findings have supporting evidence
- [ ] **Contradictions:** Resolved or flagged
- [ ] **Stale sources:** Identified and justified
- [ ] **Personal data:** Properly handled
- [ ] **Tone:** Appropriate for audience
- [ ] **Action items:** Clear and actionable

### For Authors

**Before submitting for review:**

- [ ] **Self-review completed**
- [ ] **Confidence scores calculated**
- [ ] **Evidence chain complete**
- [ ] **Triggers assessed** (see above)
- [ ] **Appropriate reviewer identified**
- [ ] **Timeline communicated**

---

## Review Documentation

### Review Record Template

```yaml
review_record:
  task_id: "[ID]"
  document_title: "[Title]"
  author: "[Name]"
  reviewer: "[Name, Role]"
  review_level: "L1/L2/L3/L4"
  review_date: "YYYY-MM-DD"
  
  findings_reviewed:
    - finding_id: "[ID]"
      accuracy_check: "pass/fail"
      confidence_check: "pass/fail"
      evidence_check: "pass/fail"
      notes: "[Any comments]"
  
  issues_identified:
    - issue: "[Description]"
      severity: "critical/high/medium/low"
      resolution: "[How resolved]"
  
  decision: "approved/approved-with-changes/rejected"
  changes_required: "[List if applicable]"
  re_review_required: true/false
  
  approved_for_distribution:
    audience: "[Who can receive]"
    classification: "[Internal/Confidential/Public]"
    expiry: "[When review expires, if applicable]"
```

---

## Expedited Review Process

**For time-critical findings (e.g., active cyber threats):**

1. **Author flags as urgent** with justification
2. **Reviewer notified** via multiple channels (email + phone/Slack)
3. **Review within 1 hour** (or as specified)
4. **Provisional approval** allowed with follow-up review
5. **Document expedited status** in review record

**Expedited Criteria:**
- Active security incident
- Imminent regulatory deadline
- Time-sensitive business decision
- Competitive threat requiring immediate response

---

## Review Escalation

**When reviewer is unavailable:**

1. **Backup reviewer** (pre-designated)
2. **Escalate to reviewer's manager**
3. **Document delay and reason**
4. **Communicate new timeline to stakeholders**

**When reviewer and author disagree:**

1. **Document disagreement** with rationales
2. **Escalate to shared manager** or higher
3. **Seek third-party expert opinion** if technical
4. **Document final decision and rationale**

---

## Post-Distribution Review

**After distribution, monitor for:**

| Issue | Response |
|-------|----------|
| **New information contradicts findings** | Issue correction/update |
| **Recipient questions accuracy** | Re-verify and respond |
| **Source retracts information** | Assess impact, update if needed |
| **Finding proves incorrect** | Document lesson, update skill |

**Correction Process:**
1. Assess impact of error
2. Prepare correction notice
3. Distribute to all original recipients
4. Document in review record
5. Update skills/templates if needed

---

## Review Metrics

**Track for continuous improvement:**

| Metric | Target | Purpose |
|--------|--------|---------|
| **Review cycle time** | <24 hours (L2), <48 hours (L3) | Efficiency |
| **First-pass approval rate** | >80% | Quality of initial work |
| **Issues found in review** | Track by type | Training needs |
| **Post-distribution corrections** | <5% | Accuracy |
| **Reviewer satisfaction** | Survey | Process quality |

---

## Common Review Pitfalls

| Pitfall | Solution |
|---------|----------|
| **Rubber-stamp approval** | Use checklist, require comments |
| **Over-review (everything escalated)** | Calibrate triggers, train authors |
| **Under-review (missed triggers)** | Automate trigger detection |
| **Unclear feedback** | Use structured feedback template |
| **Review bottlenecks** | Designate backup reviewers |
| **No documentation** | Require review records |

---

## Training Requirements

**Authors must be trained on:**
- When review is required (this document)
- How to prepare for review
- How to respond to feedback
- Review documentation requirements

**Reviewers must be trained on:**
- Review checklist and standards
- Confidence score validation
- Risk assessment
- Documentation requirements
- Escalation procedures

---

## Skill Maintenance

**Update this skill when:**
- New trigger categories identified
- Review process changes
- Incidents reveal gaps
- Regulatory requirements change

**Review frequency:** Quarterly
