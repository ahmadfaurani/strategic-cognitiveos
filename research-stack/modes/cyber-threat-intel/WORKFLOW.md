# Cyber Threat Intelligence Mode

## Purpose
Automated cybersecurity intelligence gathering for threat monitoring, CVE tracking, and vendor advisory analysis.

## Trigger Patterns
- "Monitor CVEs for [product/vendor]"
- "Track threat actor [name]"
- "Daily cyber threat digest"
- "Vendor security advisory for [vendor]"
- "Exploitability check for CVE-XXXX-XXXXX"

## Workflow Steps

### 1. Intelligence Requirement Parsing
```
Input: PIR or natural language request
Output: Structured intelligence requirements
  - Priority (Critical/High/Medium/Low)
  - Scope (specific CVEs, vendors, threat actors, sectors)
  - Timeline (one-time, daily, weekly)
  - Output format (alert, digest, brief, table)
```

### 2. Query Generation (SearXNG)
Generate queries across multiple search patterns:

**CVE Monitoring:**
```
"CVE-2024-XXXX exploit"
"CVE-2024-XXXX PoC"
"CVE-2024-XXXX severity"
"CVE-2024-XXXX affected products"
site:github.com "CVE-2024-XXXX"
site:nvd.nist.gov "CVE-2024-XXXX"
```

**Vendor Advisory Tracking:**
```
"[vendor] security advisory 2024"
"[vendor] PSIRT"
"[vendor] vulnerability disclosure"
site:[vendor].com/security
```

**Threat Actor Monitoring:**
```
"[threat actor] TTPs"
"[threat actor] malware"
"[threat actor] recent campaigns"
site:mitre.org "[threat actor]"
```

**NCII Sector Risks:**
```
"[sector] cyber threat 2024"
"[sector] critical infrastructure attack"
"[sector] ransomware"
```

### 3. Source Classification
| Source Type | Examples | Credibility Weight |
|-------------|----------|-------------------|
| Official | CISA, NVD, vendor PSIRT | High |
| Research | Mandiant, CrowdStrike, MSFT | High |
| Technical | GitHub, exploit-db, PacketStorm | Medium-High |
| News | BleepingComputer, The Register | Medium |
| Social | Twitter, Telegram | Low (verify only) |

### 4. Firecrawl Extraction
For each prioritized URL:
```json
{
  "url": "...",
  "options": {
    "formats": ["markdown", "json"],
    "screenshot": true,
    "onlyMainContent": true,
    "includeTags": ["article", "main", "section"],
    "excludeTags": ["nav", "footer", "header", "aside"],
    "metadata": {
      "captureTime": "ISO8601",
      "purpose": "cyber-threat-intel"
    }
  }
}
```

### 5. Evidence Analysis
Extract and structure:
- CVE identifiers and severity scores
- Affected products/versions
- Exploit availability status
- Mitigation recommendations
- Threat actor attributions
- TTPs (MITRE ATT&CK mapping)
- Timeline of disclosure/exploitation

### 6. Output Generation

#### Daily Cyber Threat Digest
```markdown
# Daily Cyber Threat Digest - YYYY-MM-DD

## Critical Alerts
| CVE | Severity | Exploit | Affected | Action |
|-----|----------|---------|----------|--------|
| CVE-2024-XXXX | CVSS 9.8 | Public | Product X | Patch immediately |

## Vendor Advisories
- **Vendor A**: [Summary] - [Link]
- **Vendor B**: [Summary] - [Link]

## Threat Actor Activity
- **[Actor Name]**: [Activity summary]

## Sector-Specific Risks
- **[Sector]**: [Risk summary]

## Recommended Actions
1. [Action item]
2. [Action item]
```

#### High-Severity Alert
```markdown
# ALERT: [CVE/Threat] - [Severity]

**Issued:** YYYY-MM-DD HH:MM UTC
**Priority:** Critical/High

## Summary
[Brief description]

## Impact
[Who/what is affected]

## Exploitability
[Exploit status: Public/PoC/Contested/None]

## Immediate Actions
1. [Action]
2. [Action]

## Evidence
- [Source 1] - [Confidence]
- [Source 2] - [Confidence]

## References
- [Links with citations]
```

#### CVE Impact Table
```markdown
| CVE | CVSS | Exploit | Affected Products | Patched | Action Required |
|-----|------|---------|-------------------|---------|-----------------|
| ... | ...  | ...     | ...               | ...     | ...             |
```

## Confidence Scoring

| Score | Criteria |
|-------|----------|
| High | ≥3 independent sources, official confirmation |
| Medium | 2 sources or 1 official source |
| Low | Single unverified source, social media only |

## Skill Library Entries
- `cyber/cve-monitoring`
- `cyber/vendor-advisory-tracking`
- `cyber/threat-actor-profile`
- `cyber/daily-digest`
- `cyber/exploitability-check`

## Integration Points
- SIEM alerting (via webhook)
- Ticketing system (Jira, ServiceNow)
- Slack/Teams notifications
- Executive briefing templates
