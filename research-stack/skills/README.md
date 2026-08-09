# Skill Library

Reusable workflows and patterns for the Research Automation Stack.

## Skill Naming Convention

```
{category}/{skill-name}
```

Categories:
- `cyber` - Cyber Threat Intelligence
- `due-diligence` - Vendor & Technology Due Diligence
- `ci` - Competitive Intelligence
- `regulatory` - Regulatory & Policy Monitoring

## Available Skills

### Cyber Threat Intelligence

| Skill | Description | Trigger Pattern |
|-------|-------------|-----------------|
| `cyber/cve-monitoring` | Track and analyze CVEs for specific products/vendors | "Monitor CVEs for [product]" |
| `cyber/vendor-advisory-tracking` | Collect and summarize vendor security advisories | "Vendor advisory for [vendor]" |
| `cyber/threat-actor-profile` | Build profiles of threat actors from open sources | "Profile threat actor [name]" |
| `cyber/daily-digest` | Generate daily cyber threat digest | "Daily cyber digest" |
| `cyber/exploitability-check` | Check exploit availability for specific CVEs | "Exploit check CVE-XXXX-XXXXX" |
| `cyber/ncii-sector-monitor` | Monitor threats to critical infrastructure sectors | "[Sector] threat monitoring" |

### Vendor Due Diligence

| Skill | Description | Trigger Pattern |
|-------|-------------|-----------------|
| `due-diligence/vendor-assessment` | Full vendor security and viability assessment | "Assess vendor [name]" |
| `due-diligence/github-repo-review` | Analyze GitHub repository for security and maturity | "Review repo [org/repo]" |
| `due-diligence/license-audit` | Audit software licenses and compatibility | "License check [project]" |
| `due-diligence/build-vs-buy` | Compare building vs buying a capability | "Build vs buy [capability]" |
| `due-diligence/oss-security-check` | Open-source security posture assessment | "OSS security [project]" |

### Competitive Intelligence

| Skill | Description | Trigger Pattern |
|-------|-------------|-----------------|
| `ci/competitor-battle-card` | Generate competitor battle card for sales | "Battle card [competitor]" |
| `ci/product-comparison` | Create product comparison matrix | "Compare [A] vs [B]" |
| `ci/market-movement-tracking` | Track market movements (funding, M&A, launches) | "Market movements [sector]" |
| `ci/pricing-intelligence` | Monitor competitor pricing changes | "Pricing check [product]" |
| `ci/sales-enablement-brief` | Generate sales enablement brief | "Sales brief [topic]" |

### Regulatory Monitoring

| Skill | Description | Trigger Pattern |
|-------|-------------|-----------------|
| `regulatory/cybersecurity-monitoring` | Track cybersecurity regulations | "Cyber regulation update" |
| `regulatory/ai-governance-tracking` | Monitor AI governance developments | "AI governance update" |
| `regulatory/privacy-compliance` | Track privacy and data protection laws | "Privacy law update" |
| `regulatory/sector-specific-monitor` | Sector-specific regulatory monitoring | "[Sector] regulation" |
| `regulatory/control-mapping` | Map regulations to control frameworks | "Map [regulation] to [framework]" |
| `regulatory/deadline-tracker` | Track compliance deadlines | "Compliance deadlines" |

### Strategic Account Intelligence

| Skill | Description | Trigger Pattern |
|-------|-------------|-----------------|
| `account/target-account-research` | Deep research on target accounts | "Research [company] for meeting" |
| `account/stakeholder-prep` | Prepare for stakeholder meetings | "Stakeholder prep [name]" |
| `account/public-agency-brief` | Public sector agency briefings | "Agency briefing [agency]" |
| `account/enterprise-planning` | Enterprise account planning | "Account plan [enterprise]" |
| `account/meeting-prep` | General meeting preparation | "Meeting prep [company]" |

### Tender Monitoring

| Skill | Description | Trigger Pattern |
|-------|-------------|-----------------|
| `tender/monitoring` | Monitor tender portals for opportunities | "Tender monitoring [category]" |
| `tender/alert-generation` | Generate tender alerts | "Tender alert [sector]" |
| `tender/bid-no-bid-analysis` | Analyze and recommend bid decisions | "Bid/no-bid [opportunity]" |
| `tender/compliance-checklist` | Generate compliance checklists | "Compliance check [tender]" |
| `tender/proposal-outline` | Create proposal outlines | "Proposal outline [tender]" |
| `tender/grant-tracking` | Track grant opportunities | "Grant tracking [domain]" |

### Media Registry

| Skill | Description | Trigger Pattern |
|-------|-------------|-----------------|
| `media/outlet-discovery` | Discover relevant media outlets | "Media outlets [sector]" |
| `media/journalist-research` | Research journalists by beat | "Journalist [beat]" |
| `media/masthead-extraction` | Extract masthead information | "Masthead [publication]" |
| `media/beat-mapping` | Map journalist beats and interests | "Beat mapping [topic]" |
| `media/pr-targeting` | Build PR targeting lists | "PR list [topic]" |
| `media/coverage-tracking` | Track media coverage trends | "Coverage tracking [topic]" |

## Skill Structure

Each skill is defined as a JSON file with the following structure:

```json
{
  "skill_id": "uuid-v4",
  "name": "cyber/cve-monitoring",
  "category": "cyber_threat_intel",
  "description": "Monitor and analyze CVEs for specified products or vendors",
  
  "trigger_patterns": [
    "Monitor CVEs for {product}",
    "CVE tracking {vendor}",
    "Check CVEs {product} {timeframe}"
  ],
  
  "parameters": {
    "product": {
      "type": "string",
      "required": true,
      "description": "Product or vendor name"
    },
    "timeframe": {
      "type": "string",
      "required": false,
      "default": "30d",
      "description": "Lookback period (7d, 30d, 90d)"
    },
    "min_severity": {
      "type": "string",
      "required": false,
      "default": "medium",
      "enum": ["low", "medium", "high", "critical"],
      "description": "Minimum CVSS severity to include"
    }
  },
  
  "workflow": [
    {
      "step": 1,
      "action": "generate_queries",
      "tool": "deerflow",
      "description": "Generate targeted search queries for CVE discovery"
    },
    {
      "step": 2,
      "action": "search",
      "tool": "searxng",
      "description": "Execute queries against SearXNG"
    },
    {
      "step": 3,
      "action": "extract",
      "tool": "firecrawl",
      "description": "Scrape and extract content from discovered sources"
    },
    {
      "step": 4,
      "action": "analyze",
      "tool": "deerflow",
      "description": "Analyze extracted content for CVE mentions"
    },
    {
      "step": 5,
      "action": "output",
      "tool": "deerflow",
      "description": "Generate structured CVE impact table"
    }
  ],
  
  "output_template": "cyber/cve-impact-table.md",
  
  "quality_thresholds": {
    "min_confidence": 0.7,
    "min_sources": 2,
    "require_official_source": true
  }
}
```

## Creating a New Skill

1. **Define the use case** - What research need does this address?
2. **Identify trigger patterns** - How will users invoke this skill?
3. **Map the workflow** - What steps are needed from discovery to output?
4. **Specify parameters** - What inputs does the skill need?
5. **Define output format** - What does the deliverable look like?
6. **Set quality thresholds** - What confidence/source requirements apply?
7. **Test and iterate** - Execute the skill, refine based on results
8. **Document** - Add to this README with examples

## Skill Execution

Skills can be executed via:

```bash
# Execute skill with parameters
openclaw research skill exec --name cyber/cve-monitoring --product "Apache Log4j"

# List available skills
openclaw research skill list

# Export skill for sharing
openclaw research skill export --name cyber/cve-monitoring --output ./skills/

# Import skill from file
openclaw research skill import --file ./new-skill.json
```

## Skill Versioning

Skills follow semantic versioning:
- **Major** - Breaking changes to workflow or output format
- **Minor** - New features, backward-compatible changes
- **Patch** - Bug fixes, query improvements

## Contributing Skills

To contribute a skill:
1. Create skill definition in `skills/{category}/`
2. Add workflow documentation in `modes/{category}/`
3. Test with at least 3 different inputs
4. Document in this README
5. Submit for review

## Metrics & Analytics

Track skill performance:
- **Execution count** - How often is each skill used?
- **Avg processing time** - How long does execution take?
- **Confidence scores** - What's the average output confidence?
- **User satisfaction** - Explicit ratings if available
- **Reuse rate** - How often are skills reused vs ad-hoc research?
