# OpenWiki Quickstart — Political Intelligence & War Room Automation

**Last Updated:** 2026-07-05  
**Repository Type:** Political Intelligence Operations + Commercial Cybersecurity  
**Primary Use:** Johor PRN 2026 election intelligence, war room automation, GovSec/VoronDRQ commercial operations

---

## 🎯 What This Repository Does

This is a **political intelligence and war room automation system** designed for Malaysian election operations (Johor PRN 2026), with parallel commercial cybersecurity product development (GovSec TIP and VoronDRQ GRC platforms).

### Core Capabilities

1. **Constituency Intelligence Generation** — Automated DUN (State Assembly) profiling with demographic analysis, candidate research, historical results, and campaign strategy
2. **Daily Political Monitoring** — Loop Engineering news collection pipeline with PIR (Priority Intelligence Requirement) tagging, signal grading, and escalation
3. **War Room Replication** — Turnkey deployment of intelligence repositories for constituencies (2-3 hours per seat)
4. **Commercial Operations** — GovSec threat intelligence platform and VoronDRQ digital risk quantification for government/financial sectors

---

## 📁 Repository Structure

```
/
├── openwiki/                    # This documentation
├── .agents/                     # Agent configuration and skills
├── .openclaw/                   # OpenClaw runtime state
├── memory/                      # Session memory and daily logs
├── workflows/                   # Operational workflow definitions
│   ├── dun-profiling/           # 5-step constituency profiling
│   ├── pd-profiling/            # 3-step polling district analysis
│   └── loop-engineering-news/   # 6-step daily news collection
├── tools/                       # Operational tools
│   ├── truth-validator/         # CVS validation gate
│   ├── deer-flow/               # News collection engine
│   └── prn-logic-engine/        # Election analysis logic
├── docs/                        # Reference documentation
├── cbo-01-commercial-ops/       # Commercial business operations
├── csm-alignment-meeting-18062026/  # CyberSecurity Malaysia partnership
├── n##-*/                       # Constituency workspaces (N16, N17, N27, N32, N41, etc.)
├── war-room-playbooks/          # Campaign playbooks and templates
├── intelligence/                # Raw intelligence and briefs
└── skills/                      # OpenClaw skill definitions
```

### Key Documentation Files

| File | Purpose |
|------|---------|
| [`AGENTS.md`](/AGENTS.md) | Agent workspace conventions, memory discipline, CVS mandate |
| [`DOCTRINE.md`](/DOCTRINE.md) | Operational doctrine, decision rights, authorization boundaries |
| [`SOUL.md`](/SOUL.md) | Agent personality and behavioral identity |
| [`TOOLS.md`](/TOOLS.md) | Environment credentials and local configuration |
| [`MEMORY.md`](/MEMORY.md) | Long-term session memory (political signals, decisions) |
| [`HEARTBEAT.md`](/HEARTBEAT.md) | Automated task scheduling (daily/weekly/monthly) |
| [`DREAMS.md`](/DREAMS.md) | Strategic vision and long-term aspirations |

---

## 🚀 Getting Started

### For New Agents

1. **Read Startup Context** — Runtime injects `AGENTS.md`, `SOUL.md`, `DOCTRINE.md`, `TOOLS.md`, and recent memory automatically
2. **Understand CVS** — Core Validation System is **MANDATORY** for all outputs (see [Operations → CVS Validation](operations/cvs-validation.md))
3. **Check HEARTBEAT.md** — Review scheduled automated tasks and their status
4. **Review MEMORY.md** — Understand current political signals and ongoing operations

### For War Room Operators

**Quick Deployment (Single Constituency):**

```bash
# Create workspace
mkdir -p /home/p62operator/.openclaw/workspace/<constituency-name>
cd /home/p62operator/.openclaw/workspace/<constituency-name>
git init

# Request intelligence generation via OpenClaw
# Prompt: "Create a complete PKR War Room intelligence repository for [CONST Constituency Name]"
# Requirements: 13 standard files, TLP:AMBER classification, 150-250 KB target

# Review and deploy
git remote add origin https://github.com/ahmadfaurani/<constituency-name>.git
git push -u origin main
# Configure GitHub: Settings → Visibility: PRIVATE, enable 2FA
```

**Full Guide:** See [`QUICKSTART-WAR-ROOM-REPLICATION.md`](/QUICKSTART-WAR-ROOM-REPLICATION.md)

### For Commercial Operations

**Revenue Target:** RM 8M-10M (12 months, June 2026 - May 2027)

**Products:**
- **GovSec TIP** — Sovereign threat intelligence platform (RM 5M-6M target, 8-10 government agencies)
- **VoronDRQ GRC** — Digital risk quantification (RM 3M-4M target, 10-14 financial institutions)

**Full Plan:** See [`12-month-commercial-workplan-refined.md`](/12-month-commercial-workplan-refined.md)

---

## 🔧 Core Workflows

### 1. DUN Profiling V1 (5 Steps) ✅ VALIDATED

**Status:** Production-ready (tested on N.27 Layang-Layang)

**Purpose:** Three-dimensional constituency intelligence package

| Step | Name | Output |
|------|------|--------|
| 1 | Demographics | PD-level voter composition, tier classification |
| 2 | Candidates | Candidate profiles, vulnerabilities, vote projections |
| 3 | Historical | Election results 2018+2022, swing analysis |
| 4 | Synthesis | Master operational brief (BLUF, Strategy, Risk) |
| 5 | GitHub Upload | Private repository with structured workspace |

**Documentation:** [`workflows/dun-profiling/`](/workflows/dun-profiling/)

### 2. PD Profiling (3 Steps)

**Purpose:** Polling District-level campaign operational planning

| Step | Name | Output |
|------|------|--------|
| 1 | Demographic Data Analysis | PD-level statistics from SPR XLSX |
| 2 | PD Operational Brief | Tier classification, targets, issues |
| 3 | Campaign Strategy Matrix | Resource allocation, GOTV priorities |

**Documentation:** [`workflows/pd-profiling/`](/workflows/pd-profiling/)

### 3. Loop Engineering News Collection (6 Steps)

**Purpose:** Automated daily political intelligence monitoring

| Step | Name | Output |
|------|------|--------|
| 1 | DeerFlow News Collection | Articles from 32 Malaysian media sources |
| 2 | PIR Entity Tagger | Entities tagged with PIR-1 to PIR-10 |
| 3 | Signal Quality Grader | Loop 2 verification (5-criteria rubric) |
| 4 | Threshold Escalation Checker | ESC-001 to ESC-006 severity levels |
| 5 | Signal Registry Writer | Deduplicated signals in JSONL format |
| 6 | Daily Brief Generator | Structured intelligence brief (Telegram) |

**Schedule:** Daily at 23:00 UTC  
**Documentation:** [`workflows/loop-engineering-news/`](/workflows/loop-engineering-news/)

---

## 🧠 Core Validation System (CVS)

**MANDATORY** — All outputs must pass CVS validation before delivery

### Pre-Output Checklist

```
[ ] All Tier 1 numbers verified against ≥2 sources?
[ ] All names double-checked (spelling, position, party)?
[ ] All citations include file#line or URL?
[ ] All analytical claims have confidence tags [HIGH/MEDIUM/LOW]?
[ ] All predictive claims flagged as SPECULATION: or SCENARIO:?
[ ] Math shown explicitly for analytical claims?
```

**Validation Gate:**
```bash
./tools/truth-validator/validate.sh <output>.md || exit 1
```

**Full Documentation:** [`operations/cvs-validation.md`](operations/cvs-validation.md)

---

## 📊 Current Operations Status

### Active Constituencies (PRN 2026)

| Constituency | Code | Status | Tier | Notes |
|--------------|------|--------|------|-------|
| Layang-Layang | N27 | ✅ Complete | Tier-2 | Test run validated |
| Sungai Balang | N16 | In Progress | Tier-2 | BN-defensive, 3-cornered fight |
| Semerah | N17 | Queued | Tier-2 | BN-leaning, incumbent EXCO |
| Endau | N32 | Queued | Tier-2 | Rural Malay-majority |
| Tenggaroh | N33 | Queued | Tier-2 | — |
| Pasir Raja | N35 | Queued | Tier-2 | — |
| Johor Lama | N37 | Queued | Tier-2 | — |
| Tanjung Surat | N39 | Queued | Tier-2 | — |
| Puteri Wangsa | N41 | Queued | Tier-1 | 5-cornered urban fight, 128K voters |
| Kempas | N47 | Queued | Tier-1 | — |
| Bukit Batu | N51 | Queued | Tier-2 | — |
| Pulai Sebatang | N54 | Queued | Tier-2 | — |
| Kukup | N56 | Queued | Tier-2 | — |

### Daily Monitoring

- **PIR Framework:** 10 Priority Intelligence Requirements
- **Sources:** 32 Malaysian media outlets
- **Delivery:** Telegram (daily brief at 23:00 UTC)
- **Signal Registry:** `memory/signals/YYYY/MM/DD-signals.jsonl`

---

## 🔐 Security & Classification

### Traffic Light Protocol (TLP)

| Classification | Handling | Use Case |
|----------------|----------|----------|
| **TLP:GREEN** | Public disclosure | General messaging, public communications |
| **TLP:AMBER** | War room use only | Intelligence briefs, candidate analysis, strategy docs |
| **TLP:RED** | Named recipients only | Sensitive operational details, source protection |

### Decision Boundaries (DOCTRINE.md)

**✅ Auto-Approve (Internal Actions):**
- Read/analyze files, code, memory
- Web search, URL fetch
- Workspace organization
- Generate analysis, drafts, briefs
- Memory documentation

**⚠️ Require Authorization:**
- Send emails, messages, posts
- API writes to external systems
- Code commits/pushes to remote
- Public-facing outputs
- Irreversible deletions

---

## 📚 Documentation Index

### Architecture
- [System Architecture](architecture/system-overview.md)
- [OpenClaw Integration](architecture/openclaw-integration.md)
- [DeerFlow Engine](architecture/deerflow-engine.md)
- [Truth Validator](architecture/truth-validator.md)

### Workflows
- [DUN Profiling V1](workflows/dun-profiling.md)
- [PD Profiling](workflows/pd-profiling.md)
- [Loop Engineering News](workflows/loop-engineering.md)
- [War Room Replication](workflows/war-room-replication.md)

### Domain Concepts
- [PIR Framework](domain/pir-framework.md)
- [Tier Classification](domain/tier-classification.md)
- [Signal Registry](domain/signal-registry.md)
- [Escalation Levels](domain/escalation-levels.md)
- [Commercial Products](domain/commercial-products.md)

### Operations
- [CVS Validation](operations/cvs-validation.md)
- [Memory Discipline](operations/memory-discipline.md)
- [Heartbeat Tasks](operations/heartbeat-tasks.md)
- [Deployment Guide](operations/deployment.md)

### Testing & Quality
- [Validation Procedures](testing/validation.md)
- [Quality Assurance](testing/qa-checklist.md)

---

## 🆘 Getting Help

### Common Issues

**Q: CVS validation fails on my output**  
A: Check that all numerical claims have citations, all analytical claims have confidence tags, and all predictions are flagged as SPECULATION: or SCENARIO:. Run `./tools/truth-validator/validate.sh <file>` to see specific errors.

**Q: Need to replicate a war room repository**  
A: Follow [`QUICKSTART-WAR-ROOM-REPLICATION.md`](/QUICKSTART-WAR-ROOM-REPLICATION.md) or prompt OpenClaw: "Create a complete PKR War Room intelligence repository for [CONST Constituency Name]"

**Q: Daily brief not generating**  
A: Check [`HEARTBEAT.md`](/HEARTBEAT.md) for scheduled task status. Verify DeerFlow config at `/home/p62operator/tools/deer-flow/config.yaml`.

### Key Contacts

- **DAF** — Director, Cyber Security Practice (workspace owner)
- **p62operator** — Primary operator account

---

## 📈 Next Steps

**For Political Operations:**
1. Complete queued constituency profiles (N16, N17, N32, N33, N35, N37, N39, N41, N47, N51, N54, N56)
2. Monitor daily signals via Loop Engineering pipeline
3. Prepare weekly synthesis and monthly pipeline reviews

**For Commercial Operations:**
1. Execute POC deployments for GovSec TIP (target: RM 2M-3M in Months 1-3)
2. Engage financial institutions for VoronDRQ GRC
3. Achieve RM 8M-10M revenue target by May 2027

**For Documentation:**
- This OpenWiki was initialized on 2026-07-05
- Report issues or request updates via chat prompt

---

**Related Files:**
- [`AGENTS.md`](/AGENTS.md) — Agent workspace conventions
- [`DOCTRINE.md`](/DOCTRINE.md) — Operational doctrine
- [`MEMORY.md`](/MEMORY.md) — Long-term memory
- [`HEARTBEAT.md`](/HEARTBEAT.md) — Automated task schedule
