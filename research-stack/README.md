# Research Automation Stack

**A unified browser and research automation operating system powered by SearXNG, Firecrawl, and DeerFlow.**

## Stack Architecture

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

## Components

| Component | Role | Status |
|-----------|------|--------|
| **SearXNG** | Discovery & meta-search | ✅ Operational |
| **Firecrawl** | Web acquisition & extraction | ✅ Operational |
| **DeerFlow** | Orchestration & reasoning | 🔄 Configuring |
| **Evidence Store** | Persistence & audit trail | 📁 Schema defined |
| **Skill Library** | Reusable workflows | 📚 Templates ready |

## Operating Modes

### 🛡️ Cyber Threat Intelligence
- CVE monitoring
- Vendor advisory tracking
- Threat actor profiling
- Daily threat digests

📖 [Workflow Details](./modes/cyber-threat-intel/WORKFLOW.md)

### 🔍 Vendor & Technology Due Diligence
- Security posture assessment
- GitHub repository review
- License auditing
- Build-vs-buy analysis

📖 [Workflow Details](./modes/vendor-due-diligence/WORKFLOW.md)

### 📊 Competitive Intelligence
- Competitor battle cards
- Product comparison matrices
- Market movement tracking
- Sales enablement briefs

📖 [Workflow Details](./modes/competitive-intel/WORKFLOW.md)

### 📜 Regulatory & Policy Monitoring
- Cybersecurity regulation tracking
- AI governance updates
- Privacy compliance monitoring
- Deadline & obligation tracking

📖 [Workflow Details](./modes/regulatory-monitoring/WORKFLOW.md)

### 🎯 Strategic Account Intelligence
- Target account research
- Stakeholder meeting preparation
- Public agency briefings
- Enterprise account planning

📖 [Workflow Details](./modes/strategic-account-intel/WORKFLOW.md)

### 📋 Tender & Opportunity Monitoring
- Tender/RFP discovery
- Grant tracking
- Bid/no-bid analysis
- Compliance checklists

📖 [Workflow Details](./modes/tender-monitoring/WORKFLOW.md)

### 📰 Media Registry & Communications
- Media outlet mapping
- Journalist research
- PR targeting lists
- Coverage tracking

📖 [Workflow Details](./modes/media-registry/WORKFLOW.md)

## Quick Start

```bash
# 1. Verify stack status
openclaw research status

# 2. Run your first research task
openclaw research start --mode cyber-threat-intel --pir "Monitor CVEs for Apache Log4j"

# 3. Check results
openclaw research evidence list --task <task_id>

# 4. Generate report
openclaw research report --task <task_id> --format markdown
```

📖 [Full Quick Start Guide](./QUICKSTART.md)

## Documentation

| Document | Description |
|----------|-------------|
| [RUNBOOK.md](./RUNBOOK.md) | Complete operational runbook |
| [QUICKSTART.md](./QUICKSTART.md) | Get started in 5 minutes |
| [Evidence Store Schema](./evidence-store/SCHEMA.md) | Data model & storage structure |
| [Skill Library](./skills/README.md) | Reusable workflow definitions |

## Directory Structure

```
research-stack/
├── README.md                 # This file
├── RUNBOOK.md               # Operational runbook
├── QUICKSTART.md            # Quick start guide
├── modes/
│   ├── cyber-threat-intel/
│   │   └── WORKFLOW.md
│   ├── vendor-due-diligence/
│   │   └── WORKFLOW.md
│   ├── competitive-intel/
│   │   └── WORKFLOW.md
│   └── regulatory-monitoring/
│       └── WORKFLOW.md
├── evidence-store/
│   └── SCHEMA.md
├── skills/
│   ├── README.md
│   └── examples/
│       └── cyber-cve-monitoring.json
└── config/                  # (Create as needed)
    ├── searxng.json
    ├── firecrawl.json
    └── deerflow.json
```

## Use Cases

### Security Operations
- Daily cyber threat digest for SOC team
- CVE impact assessment for patch prioritization
- Vendor exposure analysis after major incidents

### Product & Engineering
- Technology evaluation before adoption
- Open-source security posture checks
- Build-vs-buy decision support

### Sales & Marketing
- Competitor battle cards for AE enablement
- Product comparison matrices for RFPs
- Market movement alerts for positioning

### Legal & Compliance
- Regulatory change monitoring
- Compliance deadline tracking
- Control mapping for audits

## Evidence & Auditability

Every research task maintains:
- ✅ Raw source evidence (pre-transformation)
- ✅ Extraction timestamps and metadata
- ✅ Confidence scores per finding
- ✅ Citation chains back to sources
- ✅ Verification history

## Skill Development

Create reusable skills for repeatable research patterns:

```json
{
  "name": "cyber/cve-monitoring",
  "trigger_patterns": ["Monitor CVEs for {product}"],
  "workflow": [...],
  "output_template": "cve-impact-table.md"
}
```

📖 [Skill Library Guide](./skills/README.md)

## Configuration

See [QUICKSTART.md](./QUICKSTART.md#configuration) for endpoint configuration.

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-06-14 | Initial stack unification |

---

**Built with:** SearXNG 🔍 | Firecrawl 🔥 | DeerFlow 🦌
