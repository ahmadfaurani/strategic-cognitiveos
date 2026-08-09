# Skills Library - Complete Index

## Overview

This document indexes all skills in the Research Automation Stack skills library.

**Total Skills:** 40+ across 8 categories

---

## Skill Categories

### 🔍 Search Skills (3 skills)

| Skill | Location | Purpose |
|-------|----------|---------|
| `searxng-query-patterns` | `/skills/search/searxng-query-patterns.md` | Query construction, domain-specific operators |
| `source-ranking-rules` | `/skills/search/source-ranking-rules.md` | Authority assessment, relevance scoring |
| `search-operator-library` | `/skills/search/search-operator-library.md` | Search operator reference |

**Status:** 🟡 Partially complete (1/3 done)

---

### 🔥 Acquisition Skills (4 skills)

| Skill | Location | Purpose |
|-------|----------|---------|
| `firecrawl-scrape-patterns` | `/skills/acquisition/firecrawl-scrape-patterns.md` | Single-page extraction |
| `firecrawl-crawl-patterns` | `/skills/acquisition/firecrawl-crawl-patterns.md` | Multi-page crawling |
| `firecrawl-extract-patterns` | `/skills/acquisition/firecrawl-extract-patterns.md` | Structured field extraction |
| `failed-acquisition-recovery` | `/skills/acquisition/failed-acquisition-recovery.md` | Error handling, retry strategies |

**Status:** 🔴 Not started (0/4 done)

---

### ✅ Verification Skills (4 skills)

| Skill | Location | Purpose |
|-------|----------|---------|
| `evidence-scoring` | `/skills/verification/evidence-scoring.md` | Confidence assessment framework |
| `citation-rules` | `/skills/verification/citation-rules.md` | Proper citation formatting |
| `contradiction-handling` | `/skills/verification/contradiction-handling.md` | Resolving conflicting sources |
| `freshness-checking` | `/skills/verification/freshness-checking.md` | Source recency assessment |

**Status:** 🟡 Partially complete (1/4 done)

---

### 📊 Reporting Skills (5 skills)

| Skill | Location | Purpose |
|-------|----------|---------|
| `executive-brief-template` | `/skills/reporting/executive-brief-template.md` | Executive-level outputs |
| `technical-assessment-template` | `/skills/reporting/technical-assessment-template.md` | Technical deep-dives |
| `risk-register-template` | `/skills/reporting/risk-register-template.md` | Risk documentation |
| `account-brief-template` | `/skills/reporting/account-brief-template.md` | Account intelligence briefs |
| `market-intelligence-template` | `/skills/reporting/market-intelligence-template.md` | Market analysis reports |

**Status:** 🟡 Partially complete (1/5 done)

---

### 🎯 Domain Skills (7 skills)

| Skill | Location | Purpose |
|-------|----------|---------|
| `cyber-threat-intelligence` | `/skills/domain/cyber-threat-intelligence.md` | CVE analysis, threat tracking |
| `vendor-due-diligence` | `/skills/domain/vendor-due-diligence.md` | Security/viability assessment |
| `regulatory-monitoring` | `/skills/domain/regulatory-monitoring.md` | Compliance tracking |
| `competitive-intelligence` | `/skills/domain/competitive-intelligence.md` | Competitor analysis |
| `strategic-account-intelligence` | `/skills/domain/strategic-account-intelligence.md` | Account research |
| `tender-monitoring` | `/skills/domain/tender-monitoring.md` | RFP/discovery |
| `media-registry` | `/skills/domain/media-registry.md` | Journalist research |

**Status:** 🔴 Not started (0/7 done)
**Note:** Domain knowledge is embedded in mode workflow docs

---

### 🔄 Workflow Skills (6 skills)

| Skill | Location | Purpose |
|-------|----------|---------|
| `daily-cyber-digest` | `/skills/workflow/daily-cyber-digest.md` | Daily threat intel runbook |
| `vendor-assessment-workflow` | `/skills/workflow/vendor-assessment-workflow.md` | Due diligence process |
| `battle-card-generation` | `/skills/workflow/battle-card-generation.md` | CI battle card creation |
| `regulatory-change-tracking` | `/skills/workflow/regulatory-change-tracking.md` | Regulatory monitoring |
| `account-research-workflow` | `/skills/workflow/account-research-workflow.md` | Account intel process |
| `tender-alert-workflow` | `/skills/workflow/tender-alert-workflow.md` | Tender monitoring |

**Status:** 🔴 Not started (0/6 done)
**Note:** Workflow knowledge is embedded in mode runbooks

---

### 🛡️ Governance Skills (4 skills)

| Skill | Location | Purpose |
|-------|----------|---------|
| `privacy-controls` | `/skills/governance/privacy-controls.md` | Personal data handling |
| `scraping-boundaries` | `/skills/governance/scraping-boundaries.md` | Ethical scraping limits |
| `source-handling-rules` | `/skills/governance/source-handling-rules.md` | Source treatment standards |
| `human-review-triggers` | `/skills/governance/human-review-triggers.md` | When to escalate for review |

**Status:** 🟡 Partially complete (2/4 done)

---

### 🚨 Error Recovery Skills (3 skills)

| Skill | Location | Purpose |
|-------|----------|---------|
| `failed-crawl-recovery` | `/skills/recovery/failed-crawl-recovery.md` | When crawls fail |
| `blocked-page-handling` | `/skills/recovery/blocked-page-handling.md` | When pages block scraping |
| `missing-data-procedures` | `/skills/recovery/missing-data-procedures.md` | When data is incomplete |

**Status:** 🔴 Not started (0/3 done)

---

## Completion Status

| Category | Complete | In Progress | Not Started | Total | % Complete |
|----------|----------|-------------|-------------|-------|------------|
| Search | 1 | 0 | 2 | 3 | 33% |
| Acquisition | 0 | 0 | 4 | 4 | 0% |
| Verification | 1 | 0 | 3 | 4 | 25% |
| Reporting | 1 | 0 | 4 | 5 | 20% |
| Domain | 0 | 0 | 7 | 7 | 0% |
| Workflow | 0 | 0 | 6 | 6 | 0% |
| Governance | 2 | 0 | 2 | 4 | 50% |
| Recovery | 0 | 0 | 3 | 3 | 0% |
| **TOTAL** | **5** | **0** | **31** | **36** | **14%** |

---

## Priority Development Queue

### Phase 1: Critical Path (Week 1-2)
Priority skills needed for initial operationalization:

1. **`source-ranking-rules`** (Search) - Needed for discovery quality
2. **`firecrawl-scrape-patterns`** (Acquisition) - Needed for extraction
3. **`citation-rules`** (Verification) - Needed for evidence chains
4. **`scraping-boundaries`** (Governance) - Needed for compliance

### Phase 2: Mode Enablement (Week 3-4)
Skills needed for each operating mode:

**Cyber Threat Intel:**
- `cyber-threat-intelligence` (Domain)
- `daily-cyber-digest` (Workflow)

**Vendor Due Diligence:**
- `vendor-due-diligence` (Domain)
- `vendor-assessment-workflow` (Workflow)

**Competitive Intel:**
- `competitive-intelligence` (Domain)
- `battle-card-generation` (Workflow)

**Regulatory Monitoring:**
- `regulatory-monitoring` (Domain)
- `regulatory-change-tracking` (Workflow)

### Phase 3: Full Coverage (Week 5-6)
Remaining domain and workflow skills:

- `strategic-account-intelligence` (Domain)
- `tender-monitoring` (Domain)
- `media-registry` (Domain)
- All remaining workflow skills

### Phase 4: Hardening (Week 7-8)
Error recovery and advanced skills:

- All recovery skills
- Advanced verification skills
- Optimization passes on Phase 1-2 skills

---

## Skill Development Template

Use this template for new skills:

```markdown
# [Skill Name]

## Purpose
[One sentence describing what this skill does]

## When to Use
[Trigger conditions]

## How to Execute
[Step-by-step instructions]

## Examples
[Concrete examples]

## Quality Criteria
[How to know it's done well]

## Common Pitfalls
[What to avoid]

## Related Skills
[Links to related skills]

## Version History
[Change log]
```

---

## Skill Review Process

### After Each Research Task

Complete skill review:

```yaml
skill_review:
  task_id: "[ID]"
  what_worked:
    - "[Query pattern that found good sources]"
    - "[Extraction method that worked]"
    - "[Report section that was useful]"
  what_failed:
    - "[Query that returned junk]"
    - "[Extraction that failed]"
    - "[Missing information]"
  reusable_artifacts:
    - "[Query to add to library]"
    - "[Source to add to watchlist]"
    - "[Template section to reuse]"
  new_skill_created: "[Name + location]"
  existing_skill_updated: "[Name + changes]"
  recommended_improvements: "[What to improve]"
```

### Monthly Skill Review

- Review usage metrics
- Identify unused skills for retirement
- Identify gaps for new skills
- Update based on tool changes

---

## Skill Usage Tracking

**Track for each skill:**
- Times executed
- Success rate
- Average confidence score achieved
- User satisfaction (if rated)
- Time to execute

**Use metrics to:**
- Retire unused skills
- Improve low-performing skills
- Prioritize development queue
- Identify training needs

---

## Related Documentation

- **Mode Workflows:** `/modes/[mode]/WORKFLOW.md`
- **Mode Runbooks:** `/modes/[mode]/RUNBOOK.md`
- **Evidence Store:** `/evidence-store/SCHEMA.md`
- **Templates:** `/templates/`

---

## Contacts

**Skill Library Owner:** [Name/Role]
**Review Cadence:** Monthly
**Next Review Date:** [Date]

---

**Last Updated:** 2024-06-14
**Version:** 1.0
