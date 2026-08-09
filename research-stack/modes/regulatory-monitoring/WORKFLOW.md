# Regulatory & Policy Monitoring Mode

## Purpose
Track and analyze regulatory changes, compliance requirements, and policy developments affecting cybersecurity, AI governance, privacy, and sector-specific regulations.

## Trigger Patterns
- "Monitor cybersecurity regulations"
- "AI governance updates"
- "GDPR compliance changes"
- "Financial sector tech guidance"
- "Regulatory change digest"
- "Compliance deadline tracker"

## Workflow Steps

### 1. Regulatory Scope Definition
```
Input: Regulatory domain, sector, or jurisdiction
Output: Monitoring framework
  - Regulatory bodies to track
  - Compliance requirements
  - Reporting obligations
  - Deadline tracking
  - Impact assessment criteria
```

### 2. Discovery Queries (SearXNG)

**Cybersecurity Regulations:**
```
"cybersecurity regulation 2024"
"CISA cybersecurity performance goals"
"SEC cybersecurity disclosure"
"NIS2 directive"
"cyber incident reporting requirement"
site:cisa.gov "regulation" OR "guidance"
site:sec.gov "cybersecurity"
```

**AI Governance:**
```
"AI Act EU 2024"
"AI governance framework"
"algorithmic accountability"
"AI risk management"
site:nist.gov "AI RMF"
site:ec.europa.eu "artificial intelligence"
```

**Privacy & Data Protection:**
```
"GDPR enforcement 2024"
"data protection regulation"
"privacy law update"
"cross-border data transfer"
site:edpb.europa.eu "guidelines"
site:ico.org.uk "guidance"
```

**Sector-Specific (Financial):**
```
"financial sector cybersecurity"
"FFIEC cybersecurity"
"PCI DSS update"
"operational resilience regulation"
site:basel.org "cyber"
site:ffiec.gov "guidance"
```

**Sector-Specific (Healthcare):**
```
"HIPAA update 2024"
"healthcare cybersecurity"
"FDA medical device security"
site:hhs.gov "HIPAA"
site:fda.gov "cybersecurity"
```

### 3. Source Prioritization
| Source Type | Examples | Authority Level |
|-------------|----------|-----------------|
| Legislative | Official gazettes, parliament sites | Highest |
| Regulatory Bodies | CISA, SEC, ICO, EDPB | Highest |
| Standards Bodies | NIST, ISO, ENISA | High |
| Government Agencies | HHS, FDA, FFIEC | High |
| Legal Analysis | Law firms, compliance consultancies | Medium |
| News | Regulatory news outlets | Medium |

### 4. Firecrawl Extraction Targets

**Regulatory Body Pages:**
```json
{
  "url": "https://cisa.gov/cybersecurity-performance-goals",
  "options": {
    "formats": ["markdown", "json"],
    "screenshot": true,
    "onlyMainContent": true
  }
}
```

**Official Documents/Notices:**
```json
{
  "url": "https://[agency].gov/[document]",
  "options": {
    "formats": ["markdown"],
    "screenshot": false,
    "onlyMainContent": true,
    "includeTags": ["article", "main", "document"]
  }
}
```

**Compliance Guidance:**
```json
{
  "url": "https://[regulator].gov/guidance/[topic]",
  "options": {
    "formats": ["markdown", "json"],
    "extract": {
      "title": "string",
      "effectiveDate": "date",
      "complianceDeadline": "date",
      "affectedEntities": "array",
      "requirements": "array"
    }
  }
}
```

### 5. Analysis Framework

#### Regulatory Change Assessment
- **What Changed:** New regulation, amendment, guidance
- **Effective Date:** When does it take effect
- **Compliance Deadline:** When must entities comply
- **Affected Entities:** Who must comply
- **Key Requirements:** Specific obligations
- **Penalties:** Non-compliance consequences
- **Enforcement:** Which body enforces

#### Control Mapping
Map regulatory requirements to:
- Existing controls (NIST CSF, ISO 27001, SOC 2)
- Gap analysis (what's missing)
- Implementation effort (Low/Medium/High)
- Priority (based on deadline and risk)

#### Impact Assessment Dimensions
- **Operational Impact:** Process changes required
- **Technical Impact:** System/tool changes needed
- **Documentation Impact:** Policies/procedures to update
- **Training Impact:** Staff awareness/training needs
- **Reporting Impact:** New reporting obligations
- **Cost Impact:** Estimated compliance cost

### 6. Output Generation

#### Regulatory Change Digest
```markdown
# Regulatory Change Digest - [Month/Quarter YYYY]

**Prepared:** YYYY-MM-DD
**Scope:** [Regulatory domains covered]

## New Regulations

### [Regulation Name]
- **Jurisdiction:** [Country/Region]
- **Effective Date:** YYYY-MM-DD
- **Compliance Deadline:** YYYY-MM-DD
- **Affected Entities:** [Description]
- **Summary:** [Brief overview]
- **Key Requirements:**
  1. [Requirement 1]
  2. [Requirement 2]
- **Penalties:** [Non-compliance consequences]
- **Source:** [Link] - [Confidence]

## Updated Guidance

### [Guidance Title]
- **Issuer:** [Regulatory body]
- **Updated:** YYYY-MM-DD
- **Summary of Changes:** [What changed]
- **Action Required:** [What entities should do]
- **Source:** [Link] - [Confidence]

## Enforcement Actions

### [Case/Action]
- **Regulator:** [Body]
- **Entity:** [Company/Organization]
- **Violation:** [What happened]
- **Penalty:** [Fine/Action]
- **Lesson:** [Key takeaway]
- **Source:** [Link] - [Confidence]

## Upcoming Deadlines (Next 90 Days)
| Deadline | Requirement | Affected Entities | Status |
|----------|-------------|-------------------|--------|
| YYYY-MM-DD | [Requirement] | [Entities] | Not Started/In Progress |

## Recommended Actions
1. [Action item with priority]
2. [Action item with priority]
3. [Action item with priority]
```

#### Compliance Impact Memo
```markdown
# Compliance Impact Memo: [Regulation/Guidance]

**Date:** YYYY-MM-DD
**Regulation:** [Name/Reference]
**Impact Level:** High/Medium/Low

## Executive Summary
[Brief overview of regulation and business impact]

## What Changed
[Detailed explanation of new/updated requirements]

## Affected Business Units
| Unit | Impact Level | Key Changes |
|------|--------------|-------------|
| [Unit 1] | High/Med/Low | [Summary] |
| [Unit 2] | High/Med/Low | [Summary] |

## Requirements Mapping

### [Requirement Category 1]
| Regulatory Requirement | Current Control | Gap | Remediation |
|------------------------|-----------------|-----|-------------|
| [Requirement] | [Control ID/Name] | Yes/No | [Action] |

### [Requirement Category 2]
[Same structure]

## Compliance Timeline
| Milestone | Deadline | Owner | Status |
|-----------|----------|-------|--------|
| Gap Analysis | YYYY-MM-DD | [Owner] | Pending |
| Remediation Plan | YYYY-MM-DD | [Owner] | Pending |
| Implementation | YYYY-MM-DD | [Owner] | Pending |
| Audit/Assessment | YYYY-MM-DD | [Owner] | Pending |

## Resource Requirements
- **Personnel:** [Estimated FTE/time]
- **Technology:** [Tools/systems needed]
- **External:** [Consultants/auditors]
- **Estimated Cost:** [Range if available]

## Risk of Non-Compliance
| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Regulatory Penalty | Low/Med/High | High | [Action] |
| Reputational Damage | Low/Med/High | High | [Action] |
| Operational Disruption | Low/Med/High | Medium | [Action] |

## Recommended Next Steps
1. [Immediate action]
2. [Short-term action]
3. [Long-term action]

## References
- [Regulation text] - [Link]
- [Guidance document] - [Link]
- [Industry analysis] - [Link]
```

#### Control Mapping Table
```markdown
# Control Mapping: [Regulation] to [Framework]

**Regulation:** [Name]
**Framework:** [NIST CSF / ISO 27001 / SOC 2 / etc.]

| Regulatory Requirement | [Framework] Control | Control Status | Gap | Priority |
|------------------------|---------------------|----------------|-----|----------|
| [Req 1.1] | [Control ID] | Implemented | No | - |
| [Req 1.2] | [Control ID] | Partial | Yes | High |
| [Req 2.1] | [Control ID] | Not Implemented | Yes | Critical |

## Gap Summary
| Priority | Count | Estimated Effort |
|----------|-------|------------------|
| Critical | X | [Estimate] |
| High | X | [Estimate] |
| Medium | X | [Estimate] |
| Low | X | [Estimate] |

## Remediation Roadmap
| Phase | Timeline | Gaps Addressed | Dependencies |
|-------|----------|----------------|--------------|
| Phase 1 | Q1 2024 | [List] | [Dependencies] |
| Phase 2 | Q2 2024 | [List] | [Dependencies] |
```

#### Executive Policy Brief
```markdown
# Executive Policy Brief: [Regulatory Topic]

**Date:** YYYY-MM-DD
**Classification:** Internal
**Prepared For:** Executive Leadership

## Bottom Line Up Front (BLUF)
[1-2 sentence summary of key message]

## Context
[Why this matters now]

## Key Developments
1. **[Development 1]:** [One sentence summary]
2. **[Development 2]:** [One sentence summary]
3. **[Development 3]:** [One sentence summary]

## Business Impact
- **Regulatory Risk:** [Assessment]
- **Compliance Obligation:** [What we must do]
- **Timeline:** [Key dates]
- **Resource Need:** [High-level estimate]

## Recommended Decision/Action
[Clear recommendation for leadership]

## Discussion Points
- [Point 1 for discussion]
- [Point 2 for discussion]

## Appendix: Detailed Analysis
[Reference to full memo if needed]
```

#### Deadline & Obligation Tracker
```markdown
# Compliance Deadline Tracker

**Last Updated:** YYYY-MM-DD

## Active Obligations

| Deadline | Requirement | Regulation | Owner | Status | Notes |
|----------|-------------|------------|-------|--------|-------|
| YYYY-MM-DD | [Requirement] | [Regulation] | [Owner] | 🟢 On Track / 🟡 At Risk / 🔴 Behind | [Notes] |
| YYYY-MM-DD | [Requirement] | [Regulation] | [Owner] | Status | Notes |

## Status Legend
- 🟢 On Track: Remediation on schedule
- 🟡 At Risk: Potential delay, attention needed
- 🔴 Behind: Action required to meet deadline

## Upcoming (Next 30 Days)
| Date | Deadline | Requirement | Action Needed |
|------|----------|-------------|---------------|
| YYYY-MM-DD | [Deadline] | [Requirement] | [Action] |

## Overdue
| Original Deadline | Requirement | Regulation | Reason for Delay | New Target |
|-------------------|-------------|------------|------------------|------------|
| YYYY-MM-DD | [Requirement] | [Regulation] | [Reason] | YYYY-MM-DD |

## Quarterly Compliance Review
**Q1 2024:**
- Obligations Met: X
- Obligations Missed: X
- Key Learnings: [Summary]
```

## Confidence Scoring

| Score | Criteria |
|-------|----------|
| High | Official regulatory source, original text, multiple confirmations |
| Medium | Official source summary, reputable legal analysis |
| Low | News reporting only, unofficial interpretation |

## Skill Library Entries
- `regulatory/cybersecurity-monitoring`
- `regulatory/ai-governance-tracking`
- `regulatory/privacy-compliance`
- `regulatory/sector-specific-monitoring`
- `regulatory/control-mapping`
- `regulatory/deadline-tracker`

## Integration Points
- GRC platforms (OneTrust, MetricStream, Archer)
- Compliance management systems
- Policy management tools
- Legal/regulatory alerting services
- Board reporting templates

## Regulatory Body Watchlist

### United States
- CISA (Cybersecurity and Infrastructure Security Agency)
- SEC (Securities and Exchange Commission)
- FTC (Federal Trade Commission)
- HHS OCR (Health and Human Services - Office for Civil Rights)
- FDA (Food and Drug Administration)
- FFIEC (Federal Financial Institutions Examination Council)
- NIST (National Institute of Standards and Technology)

### European Union
- European Commission (DG CONNECT)
- EDPB (European Data Protection Board)
- ENISA (European Union Agency for Cybersecurity)
- National supervisory authorities (ICO, CNIL, etc.)

### International
- ISO (International Organization for Standardization)
- IEC (International Electrotechnical Commission)
- Basel Committee on Banking Supervision
- FATF (Financial Action Task Force)
