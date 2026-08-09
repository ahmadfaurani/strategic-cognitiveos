# Runbook: Daily Cyber Threat Intelligence Digest

## Overview

| Field | Value |
|-------|-------|
| **Name** | daily-cyber-threat-intelligence-digest |
| **Frequency** | Daily |
| **Mode** | Cyber Threat Intelligence |
| **Tools** | SearXNG, Firecrawl, DeerFlow |
| **Output** | Executive digest, CVE table, action register |

---

## Execution Workflow

### Phase 1: Intake & Scoping

```yaml
task:
  title: "Daily Cyber Threat Intelligence Digest - YYYY-MM-DD"
  objective: "Produce daily digest of cyber threats, CVEs, and vendor advisories"
  priority_intelligence_requirements:
    - "What new high-severity CVEs were published in last 24h?"
    - "What vendor security advisories were issued?"
    - "What threat actor activity was reported?"
    - "What exploits are now publicly available?"
  scope:
    geography: "Global"
    sector: "All (prioritize NCII sectors)"
    timeframe: "Last 24 hours"
    language: "English"
    source_types:
      - official (NVD, CISA, vendor PSIRT)
      - technical (GitHub, exploit-db)
      - news (security blogs, threat intel feeds)
    output_required: "Daily digest with executive summary + CVE table + actions"
    handling_classification: "Internal"
    personal_data_involved: false
    review_required: false  # Unless high-severity findings
```

### Phase 2: Research Planning

```yaml
research_plan:
  key_questions:
    - "What CVEs with CVSS ≥ 7.0 were published?"
    - "What vendors issued security advisories?"
    - "What new exploits are available?"
    - "What threat actors were active?"
  source_strategy:
    primary:
      - NVD (nvd.nist.gov)
      - CISA (cisa.gov)
      - Vendor PSIRT pages
    secondary:
      - Security blogs (BleepingComputer, The Register)
      - Threat intel feeds
    official:
      - NVD, CISA, MITRE CVE
    technical:
      - GitHub advisories, exploit-db, PacketStorm
  query_strategy:
    - "CVE published yesterday"
    - "CISA KEV catalog new"
    - "site:nvd.nist.gov CVE 2024"
    - "site:cisa.gov \"known exploited\""
    - "[major vendor] security advisory"
    - "exploit published CVE 2024"
  acquisition_strategy:
    - Scrape: NVD CVE pages, CISA KEV
    - Crawl: Vendor security advisory pages
    - Extract: CVE details, severity, affected products
  verification_strategy:
    - Cross-reference CVE details across NVD + vendor
    - Verify exploit availability on multiple sources
    - Confirm vendor advisory authenticity
  expected_outputs:
    - Executive summary (5-10 bullet points)
    - High-priority threats table
    - CVE impact table
    - Affected vendors list
    - Recommended actions
    - Evidence table with citations
  risks:
    - False positives from unverified sources
    - Incomplete CVE details
    - Stale or outdated information
  assumptions:
    - NVD is authoritative for CVE data
    - CISA KEV indicates active exploitation
    - Vendor advisories are accurate
```

### Phase 3: SearXNG Discovery

**Query Set:**

| Query | Purpose | Expected Sources |
|-------|---------|------------------|
| `"CVE" published yesterday` | New CVE discovery | NVD, MITRE, security blogs |
| `"CISA KEV" new` | Actively exploited | CISA, security news |
| `site:nvd.nist.gov CVE 2024` | Official CVE list | NVD |
| `site:cisa.gov "known exploited"` | KEV catalog | CISA |
| `"[vendor] security advisory"` | Vendor advisories | Vendor sites |
| `"exploit" CVE 2024` | Exploit availability | exploit-db, GitHub, PacketStorm |
| `"threat actor" campaign 2024` | Threat activity | Threat intel blogs |
| `"ransomware" attack 2024` | Ransomware tracking | News, threat intel |

**Discovery Output:**
- Capture all queries used
- Deduplicate URLs
- Rank by authority (official > technical > news)
- Select top 20-30 sources for acquisition

### Phase 4: Firecrawl Acquisition

**Acquisition Plan:**

| URL Type | Method | Extract Fields |
|----------|--------|----------------|
| NVD CVE page | Scrape | CVE ID, CVSS, severity, affected, published |
| CISA KEV entry | Scrape | CVE ID, vendor, product, date added |
| Vendor advisory | Scrape | Advisory ID, affected products, remediation |
| Exploit-db entry | Scrape | CVE ID, exploit type, date, author |
| Security blog | Scrape | Title, summary, threat details, IOCs |

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
    "cve_id": "",
    "cvss_score": 0.0,
    "severity": "",
    "affected_products": [],
    "exploit_available": false,
    "exploit_maturity": "",
    "remediation_available": false
  },
  "extraction_status": "success|partial|failed"
}
```

### Phase 5: Evidence Store

**Store:**
- All raw Firecrawl outputs
- Source metadata (URL, publisher, timestamps)
- Extraction status and notes

**Index by:**
- CVE ID
- Vendor name
- Source type
- Date published

### Phase 6: Analysis & Verification

**For each finding, produce:**

```yaml
finding:
  title: "[CVE-2024-XXXX] Remote Code Execution in [Product]"
  summary: "Critical RCE vulnerability in [product] allowing unauthenticated remote code execution"
  evidence:
    - source_url: "https://nvd.nist.gov/vuln/detail/CVE-2024-XXXX"
      supporting_excerpt: "[Exact quote from source]"
      relevance: "Primary CVE definition and severity"
    - source_url: "https://[vendor]/security/advisory-XXX"
      supporting_excerpt: "[Exact quote from vendor]"
      relevance: "Vendor confirmation and remediation"
    - source_url: "https://github.com/[exploit]"
      supporting_excerpt: "[Exploit details]"
      relevance: "Public exploit availability"
  implication: "Active exploitation likely; immediate patching required"
  confidence_level: "high"  # or medium, low
  recommended_action: "Patch to version X.X.X immediately; monitor for IOCs"
  verification_status: "verified"  # or pending, contradicted
  reviewer_status: "auto-approved"  # or human-review-required
  created_at: "2024-06-14T04:30:00Z"
```

**Verification Rules:**

| Rule | Requirement |
|------|-------------|
| **Important claims require evidence** | CVE severity, exploit status, active exploitation |
| **Prefer official sources** | NVD, CISA, vendor PSIRT over blogs |
| **Secondary sources as context** | News/threat intel supports but doesn't prove |
| **Mark contradictions** | If sources disagree, flag explicitly |
| **Don't hide weak confidence** | Low confidence = clearly marked |
| **Snippets ≠ evidence** | Full content required, not search snippets |
| **Distinguish fact/inference/recommendation** | Label each clearly |
| **Preserve dates** | Publication date AND retrieval date |
| **Flag stale sources** | >90 days old = stale for threat intel |
| **Escalate high-impact** | Critical CVEs → human review |

**Confidence Scoring:**

| Level | Criteria |
|-------|----------|
| **High** | Official source (NVD/CISA/vendor) + exploit confirmed |
| **Medium** | Official source only OR multiple technical sources |
| **Low** | Single technical source OR unverified claims |

### Phase 7: Output Generation

**Expected Outputs:**

#### 1. Executive Summary
```markdown
# Daily Cyber Threat Digest - YYYY-MM-DD

## Bottom Line
- **High-Severity CVEs:** X new (Y with exploits)
- **Active Exploitation:** Z CVEs in CISA KEV
- **Vendor Advisories:** N major vendors
- **Threat Actors:** M active campaigns

## Critical Actions Required
1. [Action 1]
2. [Action 2]
3. [Action 3]
```

#### 2. High-Priority Threats Table
```markdown
| CVE | Severity | Exploit | Active | Affected | Action |
|-----|----------|---------|--------|----------|--------|
| CVE-2024-XXXX | Critical | ✅ | ✅ | [Product] | Patch now |
| CVE-2024-XXXX | High | ✅ | ❌ | [Product] | Patch soon |
```

#### 3. CVE Impact Table
```markdown
| CVE | CVSS | Product | Exploit | Remediation | Source |
|-----|------|---------|---------|-------------|--------|
| ... | ... | ... | ... | ... | ... |
```

#### 4. Affected Vendors
```markdown
- **Vendor A:** X CVEs, Y critical
- **Vendor B:** X CVEs, Y critical
- **Vendor C:** X CVEs, Y critical
```

#### 5. Recommended Actions
```markdown
### Immediate (24h)
- [ ] Patch [product] for CVE-2024-XXXX
- [ ] Monitor for [IOC]

### This Week
- [ ] Review [vendor] advisory
- [ ] Update [system] to version X

### Ongoing
- [ ] Monitor CISA KEV updates
- [ ] Track [threat actor] activity
```

#### 6. Evidence Table
```markdown
| Finding | Source | Type | Confidence | Date |
|---------|--------|------|------------|------|
| CVE-2024-XXXX | NVD | Official | High | 2024-06-13 |
| Exploit available | GitHub | Technical | High | 2024-06-13 |
```

---

## Skills Used

| Skill | Category | Purpose |
|-------|----------|---------|
| `cyber-threat-intelligence` | Domain | CVE analysis, threat assessment |
| `searxng-query-patterns` | Search | Effective CVE/threat queries |
| `firecrawl-scrape-patterns` | Acquisition | NVD, CISA, vendor extraction |
| `evidence-scoring` | Verification | Confidence assessment |

---

## Automation Schedule

| Time (UTC) | Action |
|------------|--------|
| 00:00 | Trigger digest run |
| 00:00-00:15 | SearXNG discovery |
| 00:15-00:30 | Firecrawl acquisition |
| 00:30-00:45 | Analysis & verification |
| 00:45-01:00 | Output generation & delivery |

---

## Human Review Triggers

**Auto-escalate to human review if:**
- CVSS 10.0 (Critical) CVE with public exploit
- Active exploitation in CISA KEV affecting core systems
- Vendor advisory indicates breach/disclosure
- Contradictory findings across sources
- Low confidence on high-impact finding

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2024-06-14 | Initial runbook |
