# Research Stack - Quick Start Guide

## Prerequisites

✅ SearXNG deployed and operational
✅ Firecrawl deployed and operational
✅ DeerFlow orchestration configured

## Verify Stack Status

```bash
# Check SearXNG
curl -s http://[searxng-host]/healthz

# Check Firecrawl
curl -s http://[firecrawl-host]/health

# Check DeerFlow
openclaw deerflow status
```

## Your First Research Task

### Example 1: Cyber Threat Intelligence

**Request:** "Monitor CVEs for Apache Log4j"

**What happens:**
1. DeerFlow parses the request and identifies it as cyber threat intel
2. Generates search queries: `"Apache Log4j CVE"`, `"Log4j vulnerability 2024"`
3. SearXNG discovers relevant sources (NVD, GitHub, security blogs)
4. Firecrawl extracts content from top sources
5. DeerFlow analyzes and generates CVE impact table
6. Output delivered with citations

**Expected output:** CVE impact table with severity, exploit status, affected versions

---

### Example 2: Vendor Due Diligence

**Request:** "Assess security posture of [vendor name]"

**What happens:**
1. DeerFlow identifies vendor due diligence mode
2. Queries: `"[vendor] security incident"`, `"[vendor] SOC2"`, `"[vendor] PSIRT"`
3. Discovers vendor security page, news articles, review sites
4. Extracts security policies, certifications, incident history
5. Analyzes against security framework
6. Generates technology assessment report

**Expected output:** Security posture assessment with risk register

---

### Example 3: Competitive Intelligence

**Request:** "Create battle card for [competitor]"

**What happens:**
1. CI mode activated
2. Queries competitor website, pricing pages, review sites, news
3. Extracts positioning, pricing, features, customer reviews
4. Analyzes strengths, weaknesses, differentiators
5. Generates battle card with objection handling

**Expected output:** Competitor battle card ready for sales team

---

### Example 4: Regulatory Monitoring

**Request:** "Track AI governance updates"

**What happens:**
1. Regulatory monitoring mode
2. Queries EU AI Act, NIST AI RMF, national AI policies
3. Extracts regulatory text, guidance documents, analysis
4. Maps requirements, identifies deadlines
5. Generates regulatory change digest

**Expected output:** Regulatory digest with compliance timeline

---

## Mode-Specific Templates

### Cyber Threat Intel Templates
- Daily digest
- High-severity alert
- CVE impact table
- Vendor exposure brief

### Vendor Due Diligence Templates
- Technology assessment report
- Maturity scorecard
- Risk register
- Deployment recommendation

### Competitive Intel Templates
- Battle card
- Product comparison matrix
- Market movement tracker
- Sales enablement brief

### Regulatory Monitoring Templates
- Regulatory change digest
- Compliance impact memo
- Control mapping table
- Deadline tracker

## Evidence Store Access

```bash
# List all tasks
openclaw research evidence tasks list

# View evidence for a task
openclaw research evidence show --task <task_id>

# Export evidence
openclaw research evidence export --task <task_id> --format json
```

## Skill Library

```bash
# List available skills
openclaw research skill list

# Execute a skill
openclaw research skill exec --name cyber/cve-monitoring --product "Apache Log4j"

# Export a skill
openclaw research skill export --name cyber/cve-monitoring
```

## Configuration

### SearXNG Settings
Edit `research-stack/config/searxng.json`:
```json
{
  "endpoint": "http://[searxng-host]",
  "engines": ["google", "bing", "duckduckgo", "github"],
  "rate_limit": "10 requests/minute",
  "timeout_seconds": 30
}
```

### Firecrawl Settings
Edit `research-stack/config/firecrawl.json`:
```json
{
  "endpoint": "http://[firecrawl-host]",
  "default_formats": ["markdown", "json"],
  "screenshot_enabled": true,
  "only_main_content": true,
  "timeout_seconds": 60
}
```

### DeerFlow Settings
Edit `research-stack/config/deerflow.json`:
```json
{
  "planning_model": "[model]",
  "analysis_model": "[model]",
  "confidence_threshold": 0.7,
  "max_sources_per_task": 20,
  "verification_required": true
}
```

## Troubleshooting

### SearXNG Not Returning Results
- Check engine status in SearXNG admin panel
- Verify rate limits not exceeded
- Try alternative search engines

### Firecrawl Extraction Failing
- Check if URL is accessible (not blocked by robots.txt)
- Verify Firecrawl service health
- Try with `screenshot: false` for problematic pages

### Low Confidence Scores
- Increase number of sources
- Prioritize official sources
- Enable cross-source verification

### Task Taking Too Long
- Reduce `max_sources_per_task`
- Limit timeframe for time-sensitive queries
- Check service health for all components

## Best Practices

1. **Be specific in requests** - "CVEs for Apache Log4j in last 30 days" vs "Log4j issues"
2. **Set clear output expectations** - Specify format (table, report, alert)
3. **Define confidence requirements** - High confidence needs more sources
4. **Review evidence before acting** - Always check source citations
5. **Save useful patterns as skills** - Build your skill library over time
6. **Archive completed tasks** - Keep evidence store manageable

## Next Steps

1. ✅ Read the full [RUNBOOK.md](./RUNBOOK.md)
2. ✅ Review mode-specific workflows in `modes/`
3. ✅ Explore the [evidence store schema](./evidence-store/SCHEMA.md)
4. ✅ Browse available skills in `skills/`
5. 🚀 Run your first research task!

---

**Need help?** Check the full documentation in each mode folder or review example tasks in the evidence store.
