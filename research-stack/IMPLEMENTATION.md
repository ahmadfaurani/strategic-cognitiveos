# Research Stack Implementation Guide

## Status: Ready for Operationalization

✅ **Documentation Complete**
✅ **Workflow Definitions Complete**
✅ **Schemas Defined**
✅ **Templates Created**
🔄 **Integration Pending** (DeerFlow orchestration)

---

## What's Been Built

### 📚 Documentation Structure

```
research-stack/
├── README.md                    # Stack overview & quick links
├── RUNBOOK.md                   # Complete operational runbook
├── QUICKSTART.md                # Get started guide
├── IMPLEMENTATION.md            # This file
├── modes/                       # 7 operating modes
│   ├── cyber-threat-intel/
│   ├── vendor-due-diligence/
│   ├── competitive-intel/
│   ├── regulatory-monitoring/
│   ├── strategic-account-intel/
│   ├── tender-monitoring/
│   └── media-registry/
├── evidence-store/
│   ├── SCHEMA.md                # Conceptual schema doc
│   └── schema.sql               # PostgreSQL DDL
├── skills/
│   ├── README.md                # Skill library guide
│   └── examples/
│       └── cyber-cve-monitoring.json
├── templates/
│   ├── intake-block.yaml
│   ├── research-plan.yaml
│   ├── discovery-output.json
│   └── acquisition-output.json
└── config/                      # (To be created)
    ├── searxng.json
    ├── firecrawl.json
    └── deerflow.json
```

---

## Seven Operating Modes

| # | Mode | Purpose | Key Outputs |
|---|------|---------|-------------|
| 1 | **Cyber Threat Intel** | CVE monitoring, threat tracking | Daily digest, CVE tables, alerts |
| 2 | **Vendor Due Diligence** | Security assessments, tech eval | Assessment reports, scorecards |
| 3 | **Competitive Intel** | Competitor tracking, battle cards | Battle cards, comparison matrices |
| 4 | **Regulatory Monitoring** | Compliance tracking, policy watch | Regulatory digests, deadline trackers |
| 5 | **Strategic Account Intel** | Target account research | Account briefs, stakeholder maps |
| 6 | **Tender Monitoring** | RFP/discovery, bid analysis | Tender alerts, bid/no-bid memos |
| 7 | **Media Registry** | Journalist research, PR targeting | Media lists, coverage trackers |

---

## Standard Workflow (All Modes)

```
Phase 1: Intake & Scoping
    ↓
Phase 2: Research Planning
    ↓
Phase 3: SearXNG Discovery
    ↓
Phase 4: Firecrawl Acquisition
    ↓
Phase 5: Evidence Store
    ↓
Phase 6: DeerFlow Analysis + Verification
    ↓
Phase 7: Structured Output
```

### Phase Requirements

| Phase | Tool | Output |
|-------|------|--------|
| Intake | DeerFlow | YAML intake block |
| Planning | DeerFlow | YAML research plan |
| Discovery | SearXNG | JSON discovery output |
| Acquisition | Firecrawl | JSON acquisition output + raw content |
| Evidence Store | Database | SQL records |
| Analysis | DeerFlow | Findings with confidence scores |
| Output | DeerFlow | Mode-specific template |

---

## Next Steps for Operationalization

### 1. Configure Endpoints

Create `research-stack/config/`:

**searxng.json:**
```json
{
  "endpoint": "http://[searxng-host]",
  "engines": ["google", "bing", "duckduckgo", "github"],
  "rate_limit": "10 requests/minute",
  "timeout_seconds": 30
}
```

**firecrawl.json:**
```json
{
  "endpoint": "http://[firecrawl-host]",
  "api_key": "[key]",
  "default_formats": ["markdown", "json"],
  "screenshot_enabled": true,
  "timeout_seconds": 60
}
```

**deerflow.json:**
```json
{
  "planning_model": "[model]",
  "analysis_model": "[model]",
  "confidence_threshold": 0.7,
  "max_sources_per_task": 20
}
```

### 2. Deploy Evidence Store

```bash
# Run the SQL schema
psql -h [host] -U [user] -d [database] -f research-stack/evidence-store/schema.sql

# Verify tables created
psql -h [host] -U [user] -d [database] -c "\dt"
```

### 3. Implement DeerFlow Orchestration

Create workflow executor that:
1. Parses intake block
2. Generates research plan
3. Executes SearXNG queries
4. Triggers Firecrawl extraction
5. Stores evidence
6. Analyzes and verifies findings
7. Generates mode-specific output

### 4. Test Each Mode

**Test Tasks:**
1. Cyber: "Monitor CVEs for Apache Log4j"
2. Vendor: "Assess security of [vendor]"
3. CI: "Battle card for [competitor]"
4. Regulatory: "AI governance updates"
5. Account: "Research [company] for meeting"
6. Tender: "Monitor RFPs for [category]"
7. Media: "Build media list for [topic]"

### 5. Build Skill Library

Convert workflow patterns to executable skills:
- `cyber/cve-monitoring` ✅ (example created)
- `due-diligence/vendor-assessment`
- `ci/competitor-battle-card`
- `regulatory/cybersecurity-monitoring`
- `account/target-account-research`
- `tender/monitoring`
- `media/outlet-discovery`

---

## Evidence Store Quick Reference

### Key Tables

| Table | Purpose |
|-------|---------|
| `research_tasks` | Top-level task containers |
| `research_sources` | Discovered/acquired sources |
| `research_findings` | Extracted insights |
| `research_outputs` | Generated reports |
| `skills` | Reusable workflow definitions |
| `skill_executions` | Skill usage tracking |

### Common Queries

**List active tasks:**
```sql
SELECT id, title, mode, status, created_at 
FROM research_tasks 
WHERE status IN ('planning', 'discovery', 'acquisition', 'analysis');
```

**Get sources for a task:**
```sql
SELECT source_url, source_type, confidence_score, retrieved_at
FROM research_sources
WHERE task_id = '[task_id]'
ORDER BY confidence_score DESC;
```

**Get high-confidence findings:**
```sql
SELECT finding_title, finding_summary, confidence_score, verified
FROM research_findings
WHERE task_id = '[task_id]'
  AND confidence_score >= 0.7
ORDER BY confidence_score DESC;
```

---

## Personal Data Handling

⚠️ **Critical for Modes 5 & 7** (Strategic Account Intel, Media Registry)

**Requirements:**
- Flag tasks with `personal_data_involved: true`
- Collect only work-related info (names, titles, work emails)
- Do not collect personal details (private emails, family info)
- Review and purge after 12 months or engagement ends
- Classify as Internal - not for external distribution
- Comply with GDPR/privacy laws for EU subjects

---

## Quality Assurance

### Confidence Scoring

| Score | Criteria |
|-------|----------|
| **High (≥0.7)** | ≥3 independent sources OR official confirmation |
| **Medium (0.5-0.69)** | 2 sources OR 1 official source |
| **Low (<0.5)** | Single unverified source |

### Verification Requirements

- **High-stakes findings** (security vulnerabilities, regulatory requirements): Require official source confirmation
- **Standard findings**: Cross-reference from ≥2 independent sources
- **Contextual findings** (market trends, stakeholder backgrounds): Single reputable source acceptable

---

## Integration Points

| System | Integration Method | Modes Affected |
|--------|-------------------|----------------|
| SIEM | Webhook/API | Cyber Threat Intel |
| CRM (Salesforce) | API | Account Intel, CI, Tender |
| GRC Platform | API | Regulatory Monitoring |
| PR Software (Cision) | Import/Export | Media Registry |
| Ticketing (Jira) | API | All modes (task tracking) |
| Slack/Teams | Webhook | All modes (alerts) |

---

## Metrics to Track

### Operational Metrics
- Tasks completed per mode
- Average processing time per task
- Sources discovered vs. acquired ratio
- High-confidence findings percentage

### Quality Metrics
- User satisfaction ratings (if collected)
- Finding accuracy (spot-check audits)
- Source diversity scores
- Verification rates

### Efficiency Metrics
- Cost per task (API calls, compute)
- Reuse rate of skills
- Time saved vs. manual research

---

## Version Control

**Documentation Version:** 1.0.0
**Date:** 2026-06-14
**Status:** Ready for implementation

### Change Log

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-06-14 | Initial stack unification complete |

---

## Support & Maintenance

### Documentation Updates
- Update workflow docs when processes change
- Add new skills to library as patterns emerge
- Revise templates based on user feedback

### Schema Evolution
- Use migration scripts for schema changes
- Maintain backward compatibility where possible
- Document breaking changes

### Skill Library Growth
- Capture successful patterns as skills
- Retire unused or outdated skills
- Version skills using semantic versioning

---

## Ready to Execute

The Research Automation Stack is **fully documented and ready for operationalization**. 

**To begin:**
1. Configure endpoints in `research-stack/config/`
2. Deploy the evidence store schema
3. Implement DeerFlow orchestration layer
4. Run test tasks for each mode
5. Iterate based on results

**Stack powered by:**
- 🔍 **SearXNG** - Discovery layer
- 🔥 **Firecrawl** - Acquisition layer  
- 🦌 **DeerFlow** - Orchestration & analysis
