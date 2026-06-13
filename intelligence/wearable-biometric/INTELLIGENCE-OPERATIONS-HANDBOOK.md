# Intelligence Operations Handbook
## Wearable Biometric Collection Program

**Document ID:** IOH-WEARABLE-BIOMETRIC-001  
**Classification:** TLP:AMBER  
**Effective Date:** 2026-06-06  
**Review Cycle:** Quarterly  
**Owner:** AI Threat Intelligence Unit  

---

## 1. Purpose & Scope

### 1.1 Mission Statement

This handbook establishes standardized procedures for intelligence collection, analysis, and dissemination related to wearable biometric recognition systems, with primary focus on Meta's NameTag feature in the Ray-Ban/Oakley smart glasses ecosystem.

### 1.2 Scope

This handbook covers:
- Collection planning and execution
- Source evaluation and validation
- Analytical tradecraft standards
- Intelligence product development
- Security and handling requirements
- Stakeholder engagement protocols

### 1.3 Authority

This program operates under the authority of the AI Threat Intelligence Unit, with oversight from enterprise security, legal, and compliance leadership.

---

## 2. Intelligence Requirements

### 2.1 Priority Intelligence Requirements (PIRs)

| PIR ID | Requirement | Priority | Decision Supported |
|--------|-------------|----------|-------------------|
| **PIR-001** | Will Meta activate NameTag, and when? | CRITICAL | Enterprise policy timing |
| **PIR-002** | What is the regulatory enforcement trajectory? | CRITICAL | Compliance planning |
| **PIR-003** | Are there real-world abuse incidents? | HIGH | Risk assessment updates |
| **PIR-004** | How are competitors responding? | MEDIUM | Strategic positioning |

### 2.2 Intelligence Requirements (IRs)

See `collection-plan.json` for complete IR list with owners and deadlines.

### 2.3 Requests for Information (RFIs)

Stakeholders may submit RFIs via:
- **Email:** intelligence@arasintegrasi.ai
- **Telegram:** AI Threat Intel Unit channel
- **Ticket System:** [If applicable]

**RFI Response SLA:**
- CRITICAL priority: 24 hours
- HIGH priority: 72 hours
- MEDIUM priority: 7 days
- LOW priority: 14 days

---

## 3. Collection Management

### 3.1 Collection Disciplines

| Discipline | Description | Primary Tools | Automation Level |
|------------|-------------|---------------|------------------|
| **OSINT** | Open-source intelligence | Web search, RSS, social media | HIGH |
| **TECHINT** | Technical intelligence | Binary analysis, network monitoring | LOW |
| **REGINT** | Regulatory intelligence | Filing trackers, legal databases | MEDIUM |
| **HUMINT** | Human intelligence | Expert network, interviews | NONE |
| **FININT** | Financial intelligence | SEC filings, earnings calls | MEDIUM |

### 3.2 Collection Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│                    COLLECTION WORKFLOW                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  [1] REQUIREMENT IDENTIFICATION                                 │
│       ↓                                                         │
│       PIR/IR defined → Collection plan updated                  │
│                                                                 │
│  [2] COLLECTION EXECUTION                                       │
│       ↓                                                         │
│       Automated triggers + manual collection                    │
│                                                                 │
│  [3] PROCESSING                                                 │
│       ↓                                                         │
│       Raw data → Collection item template                       │
│       Location: collection/{discipline}/{item-id}.md            │
│                                                                 │
│  [4] EVALUATION                                                 │
│       ↓                                                         │
│       Source reliability + information credibility assessed     │
│                                                                 │
│  [5] ANALYSIS                                                   │
│       ↓                                                         │
│       Collection items → Analytical products                    │
│       Location: analysis/{type}/{analysis-id}.md                │
│                                                                 │
│  [6] DISSEMINATION                                              │
│       ↓                                                         │
│       Finished intelligence → Stakeholders                      │
│       Location: reports/{type}/{report-id}.md                   │
│                                                                 │
│  [7] FEEDBACK                                                   │
│       ↓                                                         │
│       Stakeholder input → Requirement refinement                │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 3.3 Collection Item Template

All collection items must use standardized format:

```markdown
# Collection Item: [Title]

**Collection ID:** [DISCIPLINE]-[YEAR]-[NNN]
**Date Collected:** [YYYY-MM-DD]
**Source Type:** [Type]
**Reliability:** [A/B/C/D/F]
**Classification:** [TLP Level]

---

## Source Metadata
[Publication, author, URL, archive link, etc.]

## Key Claims
[Table of claims with confidence levels]

## Technical Details
[Extracted technical information]

## Entities Mentioned
[Organizations, people, products]

## Gaps & Follow-Ups
[Unanswered questions, collection priorities]

## Cross-References
[Related collection items]

## Analyst Notes
[Context, observations, recommendations]

---

**Collection Timestamp:** [ISO 8601]
**Collector:** [Name/Unit]
**Status:** [ACTIVE/COMPLETE/PENDING]
```

### 3.4 Automated Collection Triggers

See `collection-plan.json` for complete trigger configuration.

**Trigger Response Protocol:**
1. Trigger fires → Automated collection item created
2. Analyst notified via Telegram/email
3. Analyst reviews within 4 hours (CRITICAL) or 24 hours (HIGH)
4. Collection item enriched with additional context
5. Cross-references added
6. Status updated to ACTIVE or COMPLETE

---

## 4. Source Evaluation

### 4.1 Reliability Scoring

| Score | Definition | Example Sources |
|-------|------------|-----------------|
| **A** | Direct, authoritative, verified | Shipped code, official filings, Meta statements |
| **B** | Reliable indirect source | WIRED, Reuters, EFF technical analysis |
| **C** | Generally reliable with caveats | Industry analyst, academic research |
| **D** | Unverified or single-source | Social media, anonymous claims |
| **F** | Known unreliable or contradicted | Rumors, debunked claims |

### 4.2 Credibility Assessment

| Factor | Questions to Ask |
|--------|------------------|
| **Directness** | Is this first-hand or second-hand information? |
| **Verifiability** | Can this claim be independently confirmed? |
| **Expertise** | Does the source have relevant technical/domain expertise? |
| **Incentive Alignment** | Does the source have bias or conflicting interests? |
| **Consistency** | Is this corroborated by other independent sources? |

### 4.3 Source Registry

All sources must be logged in:
- `sources/primary-sources.md` — Direct, authoritative sources
- `sources/secondary-sources.md` — News, analysis, commentary
- `sources/source-evaluation.md` — Reliability assessments and updates

### 4.4 Human Source Handling (HUMINT)

**Ethical Guidelines:**
- No deception about analyst identity or affiliation
- No payment for information (unless authorized)
- Respect source, privacy, and safety of sources
- Document consent for on-record vs. off-record communications

**Source Development:**
1. Identify potential sources (researchers, advocates, insiders)
2. Initial contact via public channels (email, Twitter, LinkedIn)
3. Establish rapport through shared interests
4. Request briefing or interview
5. Document conversation (with consent)
6. Maintain ongoing relationship

---

## 5. Analytical Tradecraft

### 5.1 Confidence Levels

| Level | Definition | Usage Criteria |
|-------|------------|----------------|
| **HIGH** | Multiple corroborated sources, low ambiguity | Key judgments, policy recommendations |
| **MEDIUM** | Single reliable source or multiple uncorroborated | Technical assessments, timeline estimates |
| **LOW** | Speculative, limited sourcing, high ambiguity | Future predictions, competitor analysis |

### 5.2 Analytical Standards

**Objectivity:**
- Acknowledge alternative hypotheses
- Distinguish fact from judgment
- Identify assumptions explicitly
- Update assessments when new evidence emerges

**Attribution:**
- Every claim must link to source material
- Use direct quotes where possible
- Preserve context (avoid quote mining)
- Timestamp all data (collection time, event time, publication time)

**Documentation:**
- Maintain audit trail of analytical process
- Document dissenting views if team analysis
- Preserve working notes and drafts
- Version control all analytical products

### 5.3 Alternative Analysis Techniques

| Technique | Purpose | When to Use |
|-----------|---------|-------------|
| **Analysis of Competing Hypotheses (ACH)** | Test multiple explanations | High-uncertainty situations |
| **Red Team Analysis** | Challenge assumptions | Before major judgments |
| **Devil's Advocacy** | Surface counterarguments | Contested assessments |
| **Premortem** | Identify failure modes | Before publishing recommendations |
| **What-If Analysis** | Explore scenarios | Planning and forecasting |

### 5.4 Bias Mitigation

| Bias Type | Mitigation Strategy |
|-----------|---------------------|
| **Confirmation Bias** | Actively seek disconfirming evidence |
| **Recency Bias** | Weight historical data appropriately |
| **Availability Bias** | Consider base rates, not just salient cases |
| **Mirror-Imaging** | Avoid assuming adversary thinks like us |
| **Groupthink** | Encourage dissent, rotate analysts |

---

## 6. Intelligence Products

### 6.1 Product Types

See `collection-plan.json` for complete product catalog.

**Regular Cadence Products:**
- **SITREP (Daily):** 1-page situational update
- **Weekly Synthesis:** 3-5 page analytical brief
- **Technical Deep-Dive:** 10-20 page technical report
- **Strategic Assessment:** 15-30 page quarterly analysis

**Event-Driven Products:**
- **Flash Alert:** <4 hours, urgent brief
- **Technical Advisory:** <24 hours, IOC/TTP focus
- **Policy Brief:** <48 hours, regulatory/legal focus
- **Stakeholder Note:** <24 hours, external-facing

### 6.2 Product Templates

Located in `reports/templates/`:
- `sitrep-daily.md`
- `synthesis-weekly.md`
- `techdeep-monthly.md`
- `strategic-quarterly.md`
- `flash-alert.md`
- `tech-advisory.md`
- `policy-brief.md`
- `stakeholder-note.md`

### 6.3 Classification & Marking

| Classification | Marking | Distribution |
|----------------|---------|--------------|
| **TLP:RED** | `TLP:RED` at top and bottom | Named recipients only |
| **TLP:AMBER** | `TLP:AMBER` at top and bottom | Organization internal |
| **TLP:CLEAR** | `TLP:CLEAR` at top and bottom | Trusted partners |
| **TLP:GREEN** | `TLP:GREEN` at top and bottom | Public release |

**Marking Requirements:**
- Classification at top of document (after title)
- Classification at bottom of document (before end)
- Page numbers on multi-page documents
- Version number and date on all products

### 6.4 Quality Assurance

**Pre-Publication Review Checklist:**
- [ ] All claims sourced and attributed
- [ ] Confidence levels assigned to judgments
- [ ] Alternative hypotheses considered
- [ ] Classification marking correct
- [ ] Distribution list appropriate
- [ ] Executive summary accurate
- [ ] Recommendations actionable
- [ ] Spelling/grammar checked
- [ ] Cross-references working

**Review Levels:**
- **Level 1 (Self):** Analyst self-review (all products)
- **Level 2 (Peer):** Peer analyst review (Technical Deep-Dive, Strategic Assessment)
- **Level 3 (Lead):** Lead analyst review (Flash Alert, Policy Brief)
- **Level 4 (Leadership):** Executive review (Strategic Assessment, sensitive Flash Alerts)

---

## 7. Security & Handling

### 7.1 Storage Requirements

| Data Type | Storage Location | Encryption | Access Control |
|-----------|------------------|------------|----------------|
| **Collection data** | `collection/` directory | At rest (workspace) | Workspace access |
| **Analysis products** | `analysis/` directory | At rest (workspace) | Workspace access |
| **Finished reports** | `reports/` directory | At rest (workspace) | Workspace access |
| **Sensitive artifacts** | `artifacts/` directory | Encrypted | Lead analyst only |
| **PII (if collected)** | Minimized, access-controlled | Encrypted | Need-to-know |

### 7.2 Retention Schedule

| Record Type | Retention Period | Disposal Method |
|-------------|------------------|-----------------|
| **Collection items** | 7 years | Secure deletion |
| **Analysis products** | 7 years | Secure deletion |
| **Finished reports** | 7 years | Secure deletion |
| **Source records** | 7 years | Secure deletion |
| **PII** | Minimum necessary | Immediate deletion when no longer needed |

### 7.3 Access Control

| Role | Access Level | Approval Required |
|------|--------------|-------------------|
| **Lead Analyst** | Full access | N/A |
| **Intelligence Analyst** | Collection + analysis | Lead analyst |
| **Leadership** | Finished reports only | N/A |
| **Security Teams** | Technical reports | Lead analyst |
| **Legal/Compliance** | All reports | N/A |
| **External Partners** | TLP:CLEAR/GREEN only | Lead analyst + legal |

### 7.4 Incident Response

**Security Incident Types:**
- Unauthorized access to intelligence data
- Accidental TLP violation (wrong distribution)
- Source compromise
- Data breach or exfiltration

**Response Protocol:**
1. **Contain:** Limit further exposure
2. **Assess:** Determine scope and impact
3. **Notify:** Inform lead analyst, legal, security
4. **Remediate:** Fix vulnerability, update controls
5. **Document:** Incident report in `security/incidents/`
6. **Review:** Lessons learned, process improvement

---

## 8. Stakeholder Engagement

### 8.1 Stakeholder Mapping

| Stakeholder | Interest | Engagement Frequency |
|-------------|----------|---------------------|
| **Executive Leadership** | Strategic risk, decision support | Quarterly + event-driven |
| **Security Operations** | Technical IOCs, detection | Weekly + event-driven |
| **Legal/Compliance** | Regulatory exposure, litigation | Weekly + event-driven |
| **Privacy Engineering** | Product guidance, DPIA | Monthly |
| **Physical Security** | Facility policies, device bans | Monthly |
| **HR/Training** | Employee awareness | Quarterly |
| **External Partners** | Shared intelligence | As needed (TLP:CLEAR) |

### 8.2 Engagement Protocols

**Request Handling:**
1. Log RFI in tracking system
2. Assign priority (CRITICAL/HIGH/MEDIUM/LOW)
3. Route to appropriate analyst
4. Respond within SLA
5. Follow up for feedback

**Briefing Standards:**
- **Executive:** 10-15 minutes, focus on key judgments and recommendations
- **Technical:** 30-60 minutes, deep-dive on IOCs and TTPs
- **Legal:** 30 minutes, regulatory exposure and precedent
- **All-hands:** 15-20 minutes, awareness and policy updates

### 8.3 Feedback Loop

**Stakeholder Feedback Collection:**
- Quarterly surveys
- Post-briefing feedback forms
- Ad-hoc check-ins
- Usage analytics (report downloads, views)

**Feedback Integration:**
- Monthly review of stakeholder feedback
- Adjust collection priorities based on feedback
- Update product templates for clarity
- Refine analytical focus areas

---

## 9. Training & Development

### 9.1 Required Training

| Training | Frequency | Audience |
|----------|-----------|----------|
| **Analytical Tradecraft** | Annual | All analysts |
| **Source Handling** | Annual | HUMINT collectors |
| **Security Awareness** | Annual | All personnel |
| **TLP Classification** | Annual | All personnel |
| **Technical Tools** | As needed | TECHINT collectors |

### 9.2 Skill Development

| Skill | Development Method |
|-------|-------------------|
| **OSINT Collection** | Online courses, practice exercises |
| **Technical Analysis** | Reverse engineering training, tool certification |
| **Regulatory Analysis** | Legal briefings, CPE courses |
| **Analytical Writing** | Peer review, editing workshops |
| **Briefing Skills** | Practice sessions, feedback |

### 9.3 Knowledge Management

**Internal Resources:**
- `README.md` — Workspace index
- `collection-plan.json` — Collection strategy
- `sources/` — Source registry
- `analysis/` — Analytical products
- `reports/` — Finished intelligence

**External Resources:**
- MITRE ATT&CK Framework
- NIST AI Risk Management Framework
- ODNI Intelligence Community Directives
- IALEA Analytical Standards

---

## 10. Performance Metrics

### 10.1 Collection Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| **IR Coverage** | 90% of IRs have active collection | Weekly review |
| **Source Diversity** | Minimum 3 independent sources per HIGH confidence judgment | Report audit |
| **Collection Timeliness** | <24 hours from event to collection item | Timestamp comparison |

### 10.2 Analysis Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| **Accuracy** | <5% correction rate | Track updates/corrections |
| **Confidence Calibration** | 80% of HIGH confidence judgments validated | Retrospective review |
| **Alternative Analysis** | 100% of key judgments consider competing hypotheses | Report audit |

### 10.3 Dissemination Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| **Timeliness** | 100% of products within SLA | Timestamp comparison |
| **Actionability** | 80% of recommendations implemented | Stakeholder follow-up |
| **Satisfaction** | >4/5 stakeholder rating | Quarterly surveys |

### 10.4 Security Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| **Classification Compliance** | 100% of products correctly marked | Spot audits |
| **Access Control** | 0 unauthorized access incidents | Incident tracking |
| **Retention Compliance** | 100% of records disposed per schedule | Annual audit |

---

## 11. Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-06-06 | AI Threat Intel Unit | Initial handbook creation |

---

## Appendix A: Glossary

| Term | Definition |
|------|------------|
| **BIPA** | Biometric Information Privacy Act (Illinois) |
| **Collection Item** | Raw intelligence from a single source |
| **DPIA** | Data Protection Impact Assessment |
| **EFF** | Electronic Frontier Foundation |
| **FR** | Facial Recognition |
| **HUMINT** | Human Intelligence |
| **IOC** | Indicator of Compromise |
| **IR** | Intelligence Requirement |
| **OSINT** | Open Source Intelligence |
| **PII** | Personally Identifiable Information |
| **PIR** | Priority Intelligence Requirement |
| **REGINT** | Regulatory Intelligence |
| **TECHINT** | Technical Intelligence |
| **TLP** | Traffic Light Protocol (classification system) |
| **TTP** | Tactics, Techniques, and Procedures |

---

## Appendix B: Templates & Forms

- Collection Item Template: See Section 3.3
- RFI Submission Form: `forms/rfi-submission.md`
- Source Evaluation Form: `forms/source-evaluation.md`
- Product QA Checklist: `forms/qa-checklist.md`
- Incident Report Form: `forms/incident-report.md`

---

## Appendix C: Contact Information

| Role | Contact | Hours |
|------|---------|-------|
| **Lead Analyst** | intelligence@arasintegrasi.ai | 24/7 (urgent only) |
| **Security Operations** | soc@arasintegrasi.ai | 24/7 |
| **Legal/Compliance** | legal@arasintegrasi.ai | Business hours |
| **Privacy Officer** | privacy@arasintegrasi.ai | Business hours |

---

**Document Owner:** AI Threat Intelligence Unit  
**Next Review:** 2026-09-06 (Quarterly)  
**Classification:** TLP:AMBER
