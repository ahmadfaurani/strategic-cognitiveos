# 🦌 DeerFlow Constituency Research - Standard Operating Procedure

**Version:** 1.0  
**Effective Date:** 26 June 2026  
**Classification:** TLP:AMBER - Internal Operational Use  
**Owner:** HOI Intelligence Operations  

---

## 🎯 Purpose

This document defines the standard workflow for conducting comprehensive electoral research on Malaysian DUN constituencies using the DeerFlow automated intelligence pipeline.

**Target:** 20 Johor DUN constituencies (priority marginal seats)  
**Timeline:** Complete all 20 by 5 July 2026 (6 days before election)  
**Capacity:** 3-4 constituencies/day (automated) or 20 in single batch (overnight)

---

## 📊 Workflow Overview

```
┌─────────────────────────────────────────────────────────────────┐
│  DEERFLOW CONSTITUENCY RESEARCH PIPELINE                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  PHASE 1: Collection (15 min)                                   │
│    └─ Auto-collect from 32 media sources                        │
│                                                                 │
│  PHASE 2: Entity Extraction (5 min)                             │
│    └─ PIR-1 to PIR-10 classification                            │
│                                                                 │
│  PHASE 3: Quality Grading (5 min)                               │
│    └─ Loop 2 verification (max 2 iterations)                    │
│                                                                 │
│  PHASE 4: Escalation Check (3 min)                              │
│    └─ ESC-001 to ESC-006 threshold checks                       │
│                                                                 │
│  PHASE 5: Daily Brief (5 min)                                   │
│    └─ Structured brief from MEDIUM/HIGH signals                 │
│                                                                 │
│  PHASE 6: Repository Creation (10 min)                          │
│    └─ Generate 13-file research structure                       │
│                                                                 │
│  PHASE 7: Git Push (5 min)                                      │
│    └─ Create private GitHub repo, push all files                │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│  TOTAL TIME: 48 minutes per constituency (automated)            │
│  HUMAN REVIEW: 30-45 min (analysis + enhancement)               │
│  TOTAL: 78-93 minutes vs 150 min manual (40-50% savings)        │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🛠️ Prerequisites

### System Requirements

- ✅ DeerFlow installed: `/home/p62operator/tools/deer-flow/`
- ✅ GitHub PAT: `GITHUB_TOKEN` environment variable
- ✅ Python 3.10+ with virtualenv
- ✅ Git configured with GitHub authentication
- ✅ Aras LLM API access (Qwen3.5-397B)

### Environment Setup

```bash
# Set GitHub token (add to ~/.bashrc for persistence)
export GITHUB_TOKEN="ghp_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

# Activate DeerFlow virtualenv
cd /home/p62operator/tools/deer-flow
source .venv/bin/activate

# Verify DeerFlow is operational
python collector.py --test
```

---

## 📋 Standard Operating Procedures

### SOP-01: Single Constituency Research

**Use Case:** Research one specific constituency on-demand

**Command:**
```bash
cd /home/p62operator/tools/deer-flow/scripts
./constituency-research.sh \
  --constituency N03 \
  --name Pemanis \
  --state Johor
```

**Output:**
- ✅ Signal Registry: `memory/signals/2026/06/26-escalated.jsonl`
- ✅ Daily Brief: `memory/briefs/N03-Pemanis-20260626.md`
- ✅ Research Repo: `/tmp/n03-pemanis/` (13 files)
- ✅ GitHub Repo: `https://github.com/ahmadfaurani/n03-pemanis` (private)

**Duration:** 48 minutes (automated) + 30-45 min (human review)

---

### SOP-02: Batch Processing (Multiple Constituencies)

**Use Case:** Process multiple constituencies in sequence (overnight run)

**Command:**
```bash
cd /home/p62operator/tools/deer-flow/scripts
./constituency-research.sh --batch johor-constituencies.txt
```

**Batch File Format:**
```
N03,Pemanis,Johor
N09,Gambir,Johor
N15,Kukup,Johor
```

**Output:**
- ✅ All signals aggregated in daily Signal Registry
- ✅ Individual briefs per constituency
- ✅ 20 separate GitHub repositories (private)

**Duration:** 20 constituencies × 48 min = ~16 hours (fully automated, overnight)

**Recommendation:** Run in batches of 5 to allow human review between batches

---

### SOP-03: Dry Run (Testing)

**Use Case:** Test pipeline without executing (verify configuration)

**Command:**
```bash
./constituency-research.sh \
  --constituency N03 \
  --name Pemanis \
  --state Johor \
  --dry-run
```

**Output:** Shows all commands that would be executed (no actual collection/git ops)

---

### SOP-04: Skip Collection (Use Existing Data)

**Use Case:** Re-process constituency with existing DeerFlow data

**Command:**
```bash
./constituency-research.sh \
  --constituency N03 \
  --name Pemanis \
  --state Johor \
  --skip-collection
```

**Use Case:** When DeerFlow already collected data (daily automated run)

---

### SOP-05: Skip Git (Local Research Only)

**Use Case:** Generate research locally without GitHub push

**Command:**
```bash
./constituency-research.sh \
  --constituency N03 \
  --name Pemanis \
  --state Johor \
  --skip-git
```

**Use Case:** Testing, or when GitHub is unavailable

---

## 📁 Output Structure

### Signal Registry Entry

**Location:** `memory/signals/YYYY/MM/DD-escalated.jsonl`

**Format:**
```json
{
  "id": "sig_20260626_001",
  "timestamp": "2026-06-26T14:30:00Z",
  "source": "Malay Mail",
  "url": "https://...",
  "title": "Jalex Lee to contest N03 Pemanis",
  "content": "...",
  "constituency": "N03",
  "pir_tags": ["PIR-03: Candidate Profile"],
  "sentiment": "neutral",
  "quality_score": 0.92,
  "escalation": "MEDIUM"
}
```

---

### Daily Brief

**Location:** `memory/briefs/{CODE}-{NAME}-{DATE}.md`

**Structure:**
```markdown
# Daily Intelligence Brief - N03 Pemanis

**Date:** 26 June 2026  
**Constituency:** N03 Pemanis, Johor  
**Election Date:** 11 July 2026

## Executive Summary
- 12 signals collected (3 MEDIUM, 9 LOW)
- Key development: PH candidate announcement
- No CRITICAL/HIGH signals detected

## Key Signals (MEDIUM+)
1. [MEDIUM] Jalex Lee confirmed as PKR candidate
2. [MEDIUM] BN campaign launch scheduled 28 June
3. [MEDIUM] PAS youth rally in Segamat

## PIR Trend Analysis
- PIR-03 (Candidate Profile): +5 signals
- PIR-07 (PH Strategy): +3 signals
- PIR-01 (BN Strategy): +2 signals

## Emerging Narratives
- "Youth vs Experience" narrative emerging
- Economic issues dominate (cost of living)

## Recommended Actions
- Monitor BN campaign launch (28 June)
- Track social media sentiment on Jalex Lee
- Verify PN candidate identity
```

---

### Research Repository

**Location:** `/tmp/{code}-{name}/` → Pushed to GitHub

**Structure:**
```
n03-pemanis/
├── README.md                    # Overview with DeerFlow integration notes
├── REPOSITORY-STATUS.md         # File inventory + verification status
├── .gitignore                   # Security exclusions
├── docs/
│   ├── candidate-analysis-jalex-lee.md
│   ├── candidate-analysis-anuar.md
│   ├── constituency-profile.md
│   └── polling-district-breakdown.md
├── intelligence/
│   ├── deerflow-daily-brief.md  # ← DeerFlow output
│   └── war-room-brief.md
├── strategy/
│   ├── campaign-strategy.md
│   └── messaging-framework.md
├── historical/
│   ├── 2018-election-results.md
│   └── 2022-election-results.md
└── sources/
    ├── references.md
    └── fact-check-verification.md
```

---

## 🔍 Human Review Checklist

After automated pipeline completes, conduct human review:

### Phase 1: Data Quality Check (10 min)

- [ ] Verify Signal Registry contains relevant signals
- [ ] Check PIR tags are accurate
- [ ] Confirm quality scores are reasonable (>0.7)
- [ ] Review escalation levels (any CRITICAL/HIGH?)

### Phase 2: Brief Enhancement (15 min)

- [ ] Add strategic context not captured by DeerFlow
- [ ] Verify candidate names (cross-check with SPR)
- [ ] Add historical context (2018, 2022 results)
- [ ] Include demographic analysis (ethnicity, age)

### Phase 3: Document Generation (30 min)

- [ ] Generate candidate profiles (using brief data)
- [ ] Create constituency profile (demographics + economics)
- [ ] Build polling district breakdown (13 districts)
- [ ] Draft campaign strategy (14-day plan)
- [ ] Create messaging framework (segment-specific)
- [ ] Compile historical results (2018, 2022)
- [ ] Write fact-check verification report

### Phase 4: Final QA (10 min)

- [ ] No TODOs/TBDs/placeholders
- [ ] All data points sourced
- [ ] Consistent formatting
- [ ] Classification markings present
- [ ] Git commit message descriptive

---

## 📊 Priority Constituencies (Johor)

### Tier 1: Marginal Seats (<10% margin) - HIGHEST PRIORITY

| Code | Name | 2022 Winner | Margin | Priority |
|------|------|-------------|--------|----------|
| N03 | Pemanis | BN-UMNO | 60% vs 35% | 🔴 DONE |
| N09 | Bukit Batu | PH-DAP | Marginal | 🔴 HIGH |
| N15 | Kukup | BN-UMNO | Marginal | 🔴 HIGH |
| N17 | Skudai | PH-DAP | Chinese majority | 🔴 HIGH |
| N19 | Permas | PH-PKR | Marginal | 🔴 HIGH |

### Tier 2: Strategic Importance - HIGH PRIORITY

| Code | Name | 2022 Winner | Significance | Priority |
|------|------|-------------|--------------|----------|
| N01 | Buloh Kasap | BN-UMNO | Key UMNO seat | 🟠 HIGH |
| N05 | Gambir | BN-PAS | Rural Malay majority | 🟠 HIGH |
| N10 | Bentayan | PH-DAP | Muar town center | 🟠 HIGH |
| N12 | Maharani | PH-DAP | Mixed urban | 🟠 HIGH |
| N18 | Kempas | BN-UMNO | Developing area | 🟠 HIGH |

### Tier 3: Safe Seats - MEDIUM PRIORITY

| Code | Name | 2022 Winner | Status | Priority |
|------|------|-------------|--------|----------|
| N02 | Jementah | BN-UMNO | BN safe | 🟡 MEDIUM |
| N04 | Bukit Kepong | BN-UMNO | Historic seat | 🟡 MEDIUM |
| N06 | Tangkak | BN-UMNO | Mixed | 🟡 MEDIUM |
| N07 | Bukit Pasir | BN-PAS | BN safe | 🟡 MEDIUM |
| N08 | Simpang Jeram | BN-UMNO | BN safe | 🟡 MEDIUM |
| N11 | Segenting | PH-AMANAH | PH rural | 🟡 MEDIUM |
| N13 | Benut | BN-UMNO | Rural | 🟡 MEDIUM |
| N14 | Pulai Sebatang | BN-UMNO | BN safe | 🟡 MEDIUM |
| N16 | Pekan Nenas | BN-UMNO | Mixed | 🟡 MEDIUM |
| N20 | Puteri Wangsa | PH-DAP | PH safe | 🟡 MEDIUM |

---

## 📅 Production Schedule

### Week 1 (26 June - 2 July 2026)

| Date | Constituencies | Batch | Status |
|------|----------------|-------|--------|
| 26 Jun | N03 Pemanis | Manual | ✅ DONE |
| 27 Jun | N09, N15, N17, N19 | Batch 1 | ⏳ Pending |
| 28 Jun | N01, N05, N10, N12 | Batch 2 | ⏳ Pending |
| 29 Jun | N18, N02, N04, N06 | Batch 3 | ⏳ Pending |
| 30 Jun | N07, N08, N11, N13 | Batch 4 | ⏳ Pending |
| 01 Jul | N14, N16, N20 | Batch 5 | ⏳ Pending |
| 02 Jul | **Buffer day** | - | ⏳ Contingency |

### Week 2 (3-10 July 2026)

| Date | Activity |
|------|----------|
| 3-5 Jul | Human review + enhancement of all 20 constituencies |
| 6-8 Jul | Cross-constituency analysis (trends, patterns) |
| 9 Jul | State-wide synthesis report |
| 10 Jul | Final QA + delivery |

---

## 🚨 Troubleshooting

### Issue: DeerFlow Collection Fails

**Symptoms:** `collector.py` exits with error

**Solutions:**
1. Check Aras API connectivity: `curl https://model.arasintegrasi.ai/v1`
2. Verify `.env` file has `ARAS_LLM_API_KEY`
3. Check virtualenv is activated: `source .venv/bin/activate`
4. Review logs: `cat logs/collector.log`

---

### Issue: GitHub Repository Creation Fails

**Symptoms:** `curl` returns 401/403 error

**Solutions:**
1. Verify `GITHUB_TOKEN` is set: `echo $GITHUB_TOKEN`
2. Check token has `repo` scope
3. Ensure token hasn't expired
4. Check rate limits: `curl -H "Authorization: token $GITHUB_TOKEN" https://api.github.com/rate_limit`

---

### Issue: Signal Registry Empty

**Symptoms:** No signals collected for constituency

**Solutions:**
1. Broaden search queries (add more keywords)
2. Check media source list (32 sources active?)
3. Verify date range (not collecting from future)
4. Manual web_search as fallback

---

### Issue: PIR Tagging Inaccurate

**Symptoms:** Signals tagged with wrong PIR categories

**Solutions:**
1. Review PIR framework definition
2. Update entity extraction prompts
3. Manual review + correction of tags
4. Retrain entity extraction model (if needed)

---

## 📈 Performance Metrics

### Target Performance

| Metric | Target | Current (N03 Manual) | Target (Automated) |
|--------|--------|---------------------|--------------------|
| **Time per constituency** | <90 min | 150 min | 48 min |
| **Factual accuracy** | >95% | 90% | 92% (automated) + human review |
| **Source coverage** | 32+ sources | 8 sources | 32 sources |
| **Signal volume** | 20+ signals | 12 signals | 30+ signals |
| **Human review time** | <45 min | N/A | 30-45 min |

---

## 🔐 Security & Classification

### Classification Levels

| Level | Marking | Distribution |
|-------|---------|--------------|
| **TLP:GREEN** | Public | Open publication |
| **TLP:AMBER** | Internal | Campaign team only |
| **TLP:RED** | Confidential | Senior leadership only |

**All constituency research:** TLP:AMBER (Internal Campaign Use Only)

### GitHub Repository Security

- ✅ All repositories set to **PRIVATE**
- ✅ No sensitive data in git history (use `.gitignore`)
- ✅ Access limited to campaign team members
- ✅ Two-factor authentication required for collaborators

### Data Retention

- **Signal Registry:** Retain indefinitely (historical record)
- **Daily Briefs:** Retain for 1 year post-election
- **Research Repos:** Retain indefinitely (reference)
- **Working files:** Delete after final QA

---

## 📞 Support & Escalation

### Technical Issues

- **DeerFlow bugs:** Check `/home/p62operator/tools/deer-flow/docs/`
- **GitHub issues:** `https://github.com/ahmadfaurani/deer-flow/issues`
- **LLM API issues:** Contact Aras Integrasi support

### Operational Issues

- **Data quality concerns:** Escalate to campaign manager
- **Classification questions:** Consult TLP guidelines
- **Timeline delays:** Adjust batch schedule accordingly

---

## 📝 Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 26 Jun 2026 | HOI Intel Ops | Initial release |
| - | - | - | - |

---

## 📚 Related Documents

- **DeerFlow Config:** `/home/p62operator/tools/deer-flow/config.yaml`
- **Pipeline Script:** `/home/p62operator/tools/deer-flow/scripts/constituency-research.sh`
- **Batch List:** `/home/p62operator/tools/deer-flow/scripts/johor-constituencies.txt`
- **Workflow Review:** `/home/p62operator/.openclaw/workspace/docs/candidate-profiling-workflow-review.md`
- **Integration Guide:** `/home/p62operator/.openclaw/workspace/docs/deerflow-constituency-research-integration.md`
- **Signal Registry Schema:** `memory/2026-06-13-political-signal-registry.md`

---

*Last updated: 26 June 2026, 06:30 UTC*  
**Next review:** After Batch 1 completion (27 June 2026)
