# Research Automation Stack - Unified Runbook

## Stack Overview

```
User Research Request / PIR
         ↓
DeerFlow Planning Agent
         ↓
SearXNG Discovery Layer
         ↓
Firecrawl Acquisition Layer
         ↓
Evidence Store
         ↓
DeerFlow Analysis + Verification Layer
         ↓
Structured Output / Report / Dataset / Alert
```

## Tool Responsibilities

| Tool | Role | Primary Responsibility |
|------|------|----------------------|
| SearXNG | Discovery | Query generation, source discovery, search result aggregation |
| Firecrawl | Acquisition | Scrape, crawl, extract, normalize web content → Markdown/JSON |
| DeerFlow | Orchestration | Task planning, workflow control, multi-agent reasoning, verification |
| Evidence Store | Persistence | Raw source material, metadata, citations, confidence scores |
| Skill Library | Reuse | Repeatable workflows, domain-specific methods, tool-use patterns |

---

## Operating Workflow

### Phase 1: Intake & Planning
1. Accept research task or Priority Intelligence Requirement (PIR)
2. Parse requirements → extract entities, scope, timeline, output format
3. Generate structured research plan with milestones
4. Define success criteria and confidence thresholds

### Phase 2: Discovery
5. Generate targeted search queries (primary + alternative formulations)
6. Query SearXNG with deduplication and source ranking
7. Classify discovered URLs by type (news, official, technical, social)
8. Prioritize sources based on credibility and relevance

### Phase 3: Acquisition
9. Submit selected URLs to Firecrawl for extraction
10. Extract to Markdown/JSON with metadata (timestamp, URL, title, author)
11. Capture screenshots for visual evidence where applicable
12. Store raw evidence before any transformation

### Phase 4: Analysis & Verification
13. Analyze extracted material using DeerFlow reasoning
14. Cross-reference claims against multiple sources
15. Assign confidence scores (High/Medium/Low) per finding
16. Flag contradictions or unverified claims

### Phase 5: Output
17. Generate structured output with citations
18. Produce mode-specific deliverables (see Operating Modes below)
19. Save reusable patterns to Skill Library
20. Archive evidence chain for auditability

---

## Operating Modes

### Mode 1: Cyber Threat Intelligence

**Use Cases:**
- CVE monitoring
- Vendor advisory tracking
- Exploitability checks
- Threat actor / malware reporting
- NCII sector risk monitoring
- Product security intelligence

**Expected Outputs:**
- Daily cyber threat digest
- High-severity alert
- Vendor exposure brief
- CVE impact table
- Action register
- Executive advisory

**Workflow:** `research-stack/modes/cyber-threat-intel`

---

### Mode 2: Vendor & Technology Due Diligence

**Use Cases:**
- GitHub repository review
- Product assessment
- Open-source tool evaluation
- Build-vs-buy analysis
- Security and licensing review
- Deployment viability assessment

**Expected Outputs:**
- Technology assessment report
- Operational risk register
- Maturity scorecard
- Deployment recommendation
- Integration fit assessment

**Workflow:** `research-stack/modes/vendor-due-diligence`

---

### Mode 3: Competitive Intelligence

**Use Cases:**
- Competitor tracking
- Product positioning analysis
- Pricing signal monitoring
- Partnership monitoring
- Market movement tracking

**Expected Outputs:**
- Competitor battle card
- Product comparison matrix
- Market movement tracker
- Sales enablement brief
- Objection-handling notes

**Workflow:** `research-stack/modes/competitive-intel`

---

### Mode 4: Regulatory & Policy Monitoring

**Use Cases:**
- Cybersecurity regulations
- AI governance updates
- Privacy and data protection monitoring
- Sectoral compliance requirements
- Financial-sector technology risk guidance

**Expected Outputs:**
- Regulatory change digest
- Compliance impact memo
- Control mapping table
- Executive policy brief
- Deadline and obligation tracker

**Workflow:** `research-stack/modes/regulatory-monitoring`

---

### Mode 5: Strategic Account Intelligence

**Use Cases:**
- Target account research
- Stakeholder preparation
- Public-sector agency briefing
- Enterprise account planning
- Meeting preparation

**Expected Outputs:**
- Account intelligence brief
- Opportunity map
- Public stakeholder context
- Engagement narrative
- Recommended talking points

**Workflow:** `research-stack/modes/strategic-account-intel`

---

### Mode 6: Tender & Opportunity Monitoring

**Use Cases:**
- Tender discovery
- RFP monitoring
- Grant tracking
- Procurement opportunity identification
- Bid/no-bid analysis

**Expected Outputs:**
- Tender alert
- Opportunity tracker
- Bid/no-bid memo
- Compliance checklist
- Proposal outline

**Workflow:** `research-stack/modes/tender-monitoring`

---

### Mode 7: Media Registry & Communications Intelligence

**Use Cases:**
- Public media outlet mapping
- Journalist registry enrichment
- Masthead discovery
- Public contact collection
- PR targeting by topic or beat

**Expected Outputs:**
- Media registry table
- Outlet coverage tracker
- Collection heartbeat report
- Source confidence scoring
- PR engagement brief

**Workflow:** `research-stack/modes/media-registry`

---

## Evidence Store Schema

```json
{
  "evidence_id": "uuid",
  "source_url": "string",
  "acquisition_timestamp": "ISO8601",
  "source_type": "news|official|technical|social|academic",
  "firecrawl_extract": {
    "markdown": "string",
    "metadata": {},
    "screenshot_path": "string|null"
  },
  "findings": [],
  "confidence_score": "high|medium|low",
  "citations": [],
  "verified_by": "agent_id",
  "tags": []
}
```

---

## Configuration

### SearXNG Endpoint
```
Base URL: [configured at deployment]
Rate Limit: Respect Retry-After headers
Engines: Enable all relevant (google, bing, duckduckgo, github, etc.)
```

### Firecrawl Endpoint
```
Base URL: [configured at deployment]
Default Options:
  - formats: ["markdown", "json"]
  - screenshot: true (for high-priority sources)
  - onlyMainContent: true
  - excludeTags: ["nav", "footer", "header"]
```

### DeerFlow Configuration
```
Planning Model: [configured]
Analysis Model: [configured]
Verification: Cross-source validation required
Confidence Threshold: 0.7 for high-confidence findings
```

---

## Quick Start Commands

```bash
# Initialize new research task
openclaw research start --mode <mode> --pir "<requirement>"

# Check evidence store
openclaw research evidence list --task <task_id>

# Generate report
openclaw research report --task <task_id> --format markdown|json|pdf

# Export skill for reuse
openclaw research skill export --task <task_id> --name <skill_name>
```

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-06-14 | Initial runbook creation |
