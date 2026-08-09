# Political Intelligence & Campaign Automation Workspace

> **Classification:** TLP:AMBER — Internal Operational Use  
> **Version:** 2.0  
> **Last Updated:** 2026-07-05  
> **Authority:** DAF (Director, Cyber Security Practice)

---

## 📋 Overview

This workspace is a **production-grade political intelligence and campaign automation system** built on the OpenClaw agent framework. It combines electoral analysis, commercial cybersecurity operations, and automated research pipelines with rigorous truth validation.

### Primary Focus Areas

| Domain | Purpose | Status |
|--------|---------|--------|
| **Electoral Intelligence** | Johor PRN 2026 constituency profiling & war room automation | ✅ Production |
| **Commercial Operations** | GovSec TIP & VoronDRQ GRC revenue targeting (RM 8M-10M) | ✅ Active |
| **Truth Validation** | Core Truth Validation System (CVS) for all outputs | ✅ Mandatory |
| **Signal Monitoring** | Automated political signal collection & escalation | ✅ Active |

---

## 🎯 Key Features & Capabilities

### 1. DUN Profiling V1 Workflow
Five-step analytical pipeline for constituency intelligence:
```
Step 1: Demographics → SPR XLSX parsing (PD-level voter composition)
Step 2: Candidates   → Profile + demographic alignment analysis
Step 3: Historical   → Voting patterns + swing analysis
Step 4: Synthesis    → Master operational brief
Step 5: GitHub Upload → Structured public repository
```

**Output:** 4 intelligence briefs per constituency (Demographic, Candidate, Historical, Master Operational)

### 2. PKR War Room Automation
Production-ready intelligence repositories for electoral campaigns:
- **13-file standard structure** per constituency
- **68-71% time savings** vs manual research
- **90%+ factual accuracy** with CVS validation
- **GitHub deployment** with security controls

### 3. Core Truth Validation System (CVS)
Mandatory validation gate for all outputs:
- ✅ Multi-source verification (≥2 independent sources for Tier 1 claims)
- ✅ Confidence assertion tags ([HIGH]/[MEDIUM]/[LOW])
- ✅ Speculation demarcation (`SPECULATION:` / `SCENARIO:`)
- ✅ Conflict resolution protocol
- ✅ Automated validation script (`./tools/truth-validator/validate.sh`)

### 4. Automated Signal Monitoring (Heartbeat)
- **Daily Collection** (23:00 UTC): 32 Tier 1 & 2 sources, PIR classification
- **Weekly Synthesis** (Sunday 09:00 UTC): Trend analysis, narrative clustering
- **Monthly Review** (1st of month): Pipeline accuracy refinement

### 5. Commercial Operations
Dual-product revenue targeting for 2026-2027:

| Product | Segment | Revenue Target | Deals Required |
|---------|---------|----------------|----------------|
| **GovSec TIP** | Government agencies | RM 5M-6M | 8-10 agencies |
| **VoronDRQ GRC** | Financial institutions | RM 3M-4M | 10-14 institutions |

---

## 📁 Directory Structure

```
/home/p62operator/.openclaw/workspace/
├── DUN-Profiling/                    # Electoral intelligence workflow
│   ├── README.md                     # Workflow overview
│   ├── WORKFLOW-PROMPTS.md           # Step-by-step execution prompts
│   ├── WORKFLOW-SCHEMA.md            # Input/output schemas
│   ├── CONFIG.md                     # Configuration & environment variables
│   ├── EXAMPLES.md                   # Real-world output examples
│   ├── CVS-COMPLIANCE.md             # Truth validation compliance report
│   ├── UPLOAD-SUMMARY.md             # GitHub upload procedures
│   └── spr-xlsx-parser.py            # SPR electoral roll parser
│
├── memory/                           # Intelligence briefs & session memory
│   ├── nXX-*.md                      # Constituency briefs (demographic, candidate, etc.)
│   ├── MEMORY.md                     # Long-term curated memory
│   └── signals/                      # Political signal registry
│
├── tools/
│   ├── truth-validator/              # CVS validation scripts
│   ├── git-to-drive/                 # PDF automation & Google Drive upload
│   └── prn-logic-engine/             # DUN focus list & logic
│
├── workflows/
│   └── dun-profiling/                # Workflow automation scripts
│
├── github/                           # Auto-generated repositories
│   ├── analytical-dun-profiling-n09-gambir/
│   └── n17-semerah-prn2026/
│
├── bp6_extracted/                    # Belanjawan 2026 budget analysis
│   ├── BP.6.pdf                      # Source document
│   ├── analyze_bp6.py                # Budget extraction script
│   └── *.json                        # Analysis outputs
│
├── AGENTS.md                         # Workspace agent configuration
├── DOCTRINE.md                       # Operational doctrine (mandatory compliance)
├── SOUL.md                           # Agent personality & boundaries
├── IDENTITY.md                       # Agent identity definition
├── USER.md                           # User context (DAF)
├── TOOLS.md                          # Local tool configuration
├── HEARTBEAT.md                      # Automated monitoring tasks
└── README.md                         # This file
```

---

## 🚀 Getting Started

### Prerequisites

1. **OpenClaw** installed and configured (`npm install -g openclaw`)
2. **GitHub CLI** authenticated with `repo` scope
3. **SPR Electoral Roll XLSX** files for target constituencies
4. **ElectionData.MY API key** (https://electiondata.my/console)
5. **Git token** with repository permissions

### Environment Setup

```bash
# Required environment variables
export SPR_DATA_PATH="/home/p62operator/data/spr/"
export ELECTIONDATA_API_KEY="edmy_xxxxxxxxxxxx"
export GITHUB_TOKEN="ghp_xxxxxxxxxxxx"
export MEMORY_PATH="/home/p62operator/memory/"

# Optional configuration
export GITHUB_ORG="johor-war-room"
export REPO_VISIBILITY="private"
export TLP_MARKING="TLP:AMBER"
export ENABLE_CVS_VALIDATION="true"
```

### Quick Start: Single Constituency Analysis

```bash
# Step 1: Parse SPR data
python DUN-Profiling/spr-xlsx-parser.py --input 6_SEMERAH_as_of_190626.xlsx --output n17-demographic.json

# Step 2-4: Execute via OpenClaw agent session
openclaw skill run dun-profiling-step2 --code N17 --news-sources "..."
openclaw skill run dun-profiling-step3 --code N17 --api-key ${ELECTIONDATA_API_KEY}
openclaw skill run dun-profiling-step4 --demographic-brief <path> --candidate-brief <path> --historical-brief <path>

# Step 5: Upload to GitHub
openclaw skill run dun-profiling-step5 --brief-files <paths> --github-token ${GITHUB_TOKEN}

# Validate before delivery
./tools/truth-validator/validate.sh memory/n17-semerah-master-operational-brief.md || exit 1
```

---

## ⚙️ Configuration

### Core Configuration Files

| File | Purpose | Location |
|------|---------|----------|
| `config.yaml` | Workflow configuration | `workflows/dun-profiling/config.yaml` |
| `constituencies.yaml` | Johor DUN registry | `workflows/dun-profiling/constituencies.yaml` |
| `HEARTBEAT.md` | Automated monitoring tasks | Root directory |
| `TOOLS.md` | Local tool specifics | Root directory |

### Truth Validation (CVS) Requirements

All outputs must pass validation before delivery:

```bash
./tools/truth-validator/validate.sh <output>.md || exit 1
```

**Validation Checklist:**
- [ ] All Tier 1 numbers verified against ≥2 sources
- [ ] All names double-checked (spelling, position, party)
- [ ] All citations include `file#line` or URL
- [ ] All analytical claims have confidence tags
- [ ] All predictive claims flagged as `SPECULATION:` or `SCENARIO:`

### Decision Boundaries (DOCTRINE.md)

| Action Type | Authorization Required |
|-------------|----------------------|
| ✅ Read/analyze files, code, memory | Auto-approve (Internal) |
| ✅ Web search, URL fetch | Auto-approve (Internal) |
| ✅ Generate analysis, drafts, briefs | Auto-approve (Internal) |
| ⚠️ Send emails, messages, posts | Require Authorization (External) |
| ⚠️ API writes to external systems | Require Authorization (External) |
| ⚠️ Code commits/pushes to remote | Require Authorization (External) |
| ⚠️ Deletions without backup | Require Authorization (Irreversible) |

---

## 📊 Completed Work

### DUN Profiling Status (Johor PRN 2026)

| Constituency | Code | Parliament | Status | Briefs | GitHub |
|--------------|------|------------|--------|--------|--------|
| Pemanis | N03 | P145 | ✅ Partial | 3/4 | ❌ No |
| Gambir | N09 | P145 | ✅ Complete | 4/4 | ✅ Yes |
| Bukit Naning | N14 | P148 | ✅ Complete | 4/4 | ❌ No |
| Sungai Balang | N16 | P146 | ✅ Complete | 6/4 | ❌ No |
| Semerah | N17 | P147 | ✅ Complete | 7/4 | ✅ Yes |
| Endau | N32 | P154 | ⚠️ Partial | 2/4 | ❌ No |
| Tenggaroh | N33 | P154 | ⚠️ Partial | 2/4 | ❌ No |

**Total:** 6 constituencies, 28+ briefs, 2 GitHub repositories

### PKR War Room Repositories

| Repository | URL | Status | Size | Files |
|------------|-----|--------|------|-------|
| PRN Johor Focus Seat | github.com/ahmadfaurani/prn-johor-focus-seat | ✅ Complete | 1.0 MB | 30 |
| N15 Kukup | github.com/ahmadfaurani/n15-kukup | ✅ Complete | 220 KB | 13 |

---

## 🔒 Security & Classification

### TLP Markings

| Marking | Distribution |
|---------|-------------|
| **TLP:RED** | Named recipients only |
| **TLP:AMBER** | War room team only (default) |
| **TLP:GREEN** | Community limited |
| **TLP:CLEAR** | Public distribution |

### Protected Data (.gitignore)

- SPR Electoral Roll XLSX files (do not upload raw data)
- API keys and credentials
- Rclone configuration
- Memory files (store in `/home/p62operator/memory/`)
- Personal notes and scratch files

### Repository Security

- GitHub repos set to **PRIVATE** by default
- **Two-factor authentication** required for collaborators
- **Branch protection** on main branch
- **CVS validation** mandatory before any public output

---

## 📞 Support & Escalation

| Issue | Contact/Action |
|-------|---------------|
| Workflow questions | Political Intelligence Team |
| CVS validation failures | Automated (`validate.sh`) |
| GitHub upload issues | DAF |
| SPR data access | ElectionData.MY API |
| Decision boundary exceeded | Escalate per DOCTRINE.md |
| Truth conflicts | Tag `[CONFLICTING]`, request human review |

---

## 📚 Documentation Index

| Document | Purpose |
|----------|---------|
| `DUN-Profiling/README.md` | Workflow overview & quick start |
| `DUN-Profiling/WORKFLOW-PROMPTS.md` | Detailed step-by-step prompts |
| `DUN-Profiling/WORKFLOW-SCHEMA.md` | Technical schemas & validation |
| `DUN-Profiling/CONFIG.md` | Configuration & deployment |
| `DUN-Profiling/EXAMPLES.md` | Real-world output examples |
| `DUN-Profiling/CVS-COMPLIANCE.md` | Truth validation compliance |
| `OPERATIONAL_PLAYBOOK-PKR-WAR-ROOM-AUTOMATION.md` | War room tech stack |
| `QUICKSTART-WAR-ROOM-REPLICATION.md` | Fast deployment guide |
| `12-month-commercial-workplan-refined.md` | Revenue targets & strategy |
| `DOCTRINE.md` | Operational doctrine (mandatory) |
| `AGENTS.md` | Workspace agent configuration |
| `HEARTBEAT.md` | Automated monitoring tasks |

---

## 🧠 Memory System

### Session Continuity

| File | Purpose | Load Context |
|------|---------|--------------|
| `MEMORY.md` | Long-term curated memory | Main sessions only |
| `memory/YYYY-MM-DD.md` | Daily raw logs | All sessions |
| `USER.md` | User context | All sessions |
| `SOUL.md` | Agent personality | All sessions |

### Memory Discipline

- **Write significant events** to `memory/YYYY-MM-DD.md`
- **Curate long-term insights** to `MEMORY.md`
- **Do not load MEMORY.md** in shared contexts (Discord, group chats)
- **Review daily files** weekly to update long-term memory

---

## 📈 Performance Metrics

| Metric | Target | Current |
|--------|--------|---------|
| CVS Compliance Rate | 100% | 100% (16/16 briefs) |
| Factual Accuracy | 90%+ | 90.4% (N15 Kukup) |
| Time Savings vs Manual | 65%+ | 68-71% |
| Repository Deployment | <3 hours | 2-3 hours |
| Signal Collection | Daily | 23:00 UTC |

---

## 🔄 Update Cadence

| Document | Review Frequency | Owner |
|----------|-----------------|-------|
| Commercial Workplan | Weekly (Commercial), Monthly (JSC) | DAF |
| MEMORY.md | Ongoing (main sessions) | Agent |
| DUN Briefs | Per constituency | Political Intelligence Team |
| DOCTRINE.md | As needed | DAF |
| HEARTBEAT Tasks | Daily/Weekly/Monthly | Automated |

---

*This workspace operates under the Core Truth Validation System (CVS). All outputs must pass validation before delivery. Compliance is mandatory.*
