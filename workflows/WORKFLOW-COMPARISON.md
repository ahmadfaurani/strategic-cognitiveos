# Workflow Comparison Guide

This document clarifies the two distinct political intelligence workflows to prevent confusion.

---

## 🔄 Workflow Overview

| Aspect | **PD Profiling Workflow** | **Loop Engineering News Workflow** |
|--------|---------------------------|-----------------------------------|
| **Purpose** | Generate PD-level campaign intelligence | Daily automated news monitoring |
| **Steps** | **3 steps** | **6 steps** |
| **Frequency** | One-time per constituency | Daily (automated at 23:00 UTC) |
| **Loop Framework** | Linear workflow | 4-loop framework (LangChain) |
| **Primary User** | Campaign teams, war room directors | Political analysts, decision-makers |

---

## 📊 PD Profiling Workflow (3 Steps)

**Location:** `workflows/pd-profiling/WORKFLOW-PROMPTS.md`

### Purpose
Transform raw SPR demographic data into actionable polling district-level campaign intelligence.

### Steps

| Step | Name | Input | Output | Prompt Focus |
|------|------|-------|--------|--------------|
| **1** | **Demographic Data Analysis** | SPR CSV/Excel data | Demographic analysis report | "Review the attached demographic data and generate a detailed and structured analytical report optimized for political intelligence operational applied use case" |
| **2** | **PD Operational Brief Generation** | Demographic analysis | Individual PD briefs (one per PD) | "Generate detailed and structured operational briefs for each Polling District" |
| **3** | **Campaign Strategy Matrix** | PD operational briefs | Constituency-wide strategy, resource allocation, GOTV plan | "Generate a detailed and structured analytical report optimized for political intelligence operational applied use case: comprehensive campaign strategy matrix" |

### Example Use Cases
- N16 Sungai Balang: 19 PD profiles + campaign strategy
- N17 Semerah: 26 PD profiles + resource allocation
- N32 Endau: 20 PD profiles + GOTV master plan

### Output Structure
```
constituency-repo/
├── demographic-analysis.md          (Step 1)
├── pd-briefs/
│   ├── PD-01-XXX.md                (Step 2)
│   ├── PD-02-XXX.md
│   └── ...
├── campaign-strategy-matrix.md      (Step 3)
├── resource-allocation.md           (Step 3)
└── gotv-master-plan.md              (Step 3)
```

### Key Phrase
**"PD profiling workflow"** or **"3-step workflow"**

---

## 📰 Loop Engineering News Workflow (6 Steps)

**Location:** `workflows/loop-engineering-news/WORKFLOW-PROMPTS.md` (or `.agents/skills/loop-engineering/WORKFLOW-PROMPTS.md`)

### Purpose
Automated daily collection, tagging, grading, and synthesis of political news from 32 Malaysian media sources.

### Steps

| Step | Name | Input | Output | Loop Level |
|------|------|-------|--------|------------|
| **1** | **DeerFlow News Collection** | 32 media sources | Raw news signals | Loop 1 |
| **2** | **PIR Entity Tagger** | Raw signals | PIR-tagged signals (PIR-1 to PIR-10) | Loop 1 |
| **3** | **Signal Quality Grader** | Tagged signals | Graded signals (pass/fail) | Loop 2 (Verification) |
| **4** | **Threshold Escalation Checker** | Graded signals | Escalated signals (ESC-001 to ESC-006) | Loop 1 |
| **5** | **Signal Registry Writer** | Escalated signals | Signal Registry (JSONL) | Loop 3 |
| **6** | **Daily Brief Generator** | Signal Registry | Daily intelligence brief | Loop 3 |

### PIR Framework (Priority Intelligence Requirements)
- **PIR-1:** Government Stability
- **PIR-2:** Economic Policy
- **PIR-3:** Foreign Relations
- **PIR-4:** Security & Defense
- **PIR-5:** Corruption & Governance
- **PIR-6:** Social Unrest
- **PIR-7:** Electoral Politics
- **PIR-8:** Regulatory Changes
- **PIR-9:** Corporate & Business
- **PIR-10:** Environmental & Health

### Escalation Framework
- **ESC-001/002:** CRITICAL (immediate alert)
- **ESC-003/004:** HIGH (daily brief + flag)
- **ESC-005/006:** MEDIUM (daily brief only)
- **LOW:** Archive only

### Output Structure
```
memory/signals/
├── 2026/
│   └── 07/
│       ├── 01-signals.jsonl        (Step 5)
│       ├── 02-signals.jsonl
│       └── INDEX.md
memory/briefs/
└── 2026/
    └── 07/
        └── 01-brief.md             (Step 6)
```

### Key Phrase
**"Loop Engineering workflow"** or **"6-step workflow"** or **"daily news collection"**

---

## 🎯 When to Use Which Workflow

### Use PD Profiling (3 Steps) When:
- ✅ Preparing for a specific constituency campaign
- ✅ Need PD-level operational intelligence
- ✅ Planning resource allocation and GOTV strategy
- ✅ One-time research project (per constituency)
- ✅ Working with SPR demographic data

### Use Loop Engineering News (6 Steps) When:
- ✅ Need continuous political monitoring
- ✅ Tracking PIR trends across all Malaysian politics
- ✅ Generating daily intelligence briefs
- ✅ Detecting emerging narratives and escalations
- ✅ Automated daily collection (heartbeat-triggered)

---

## 🔑 Distinguishing Features

### PD Profiling Workflow Identifiers:
- Mentions **SPR data**, **demographics**, **polling districts**
- Output: **PD briefs**, **campaign strategy**, **GOTV plan**
- Context: **Constituency-specific** (N16, N17, N32, etc.)
- Frequency: **One-time** per constituency
- Steps: **Always 3 steps**

### Loop Engineering News Workflow Identifiers:
- Mentions **DeerFlow**, **PIR tags**, **32 media sources**
- Output: **Signal Registry**, **daily brief**, **escalation alerts**
- Context: **National/state-wide** political monitoring
- Frequency: **Daily** (23:00 UTC heartbeat)
- Steps: **Always 6 steps** (with Loop 2 iteration)
- Framework: **4-loop architecture** (LangChain)

---

## 📝 Common Confusion Points

### ❌ Wrong:
"The Loop Engineering workflow has 3 steps for PD analysis"

### ✅ Correct:
"The **PD Profiling workflow** has 3 steps for PD analysis"  
"The **Loop Engineering news workflow** has 6 steps for daily monitoring"

---

### ❌ Wrong:
"Run the PD profiling daily brief generator"

### ✅ Correct:
"Run the **PD operational brief generator** (Step 2 of PD Profiling)"  
"Run the **daily brief generator** (Step 6 of Loop Engineering News)"

---

### ❌ Wrong:
"The 6-step workflow for constituency campaign planning"

### ✅ Correct:
"The **3-step workflow** for constituency campaign planning"  
"The **6-step workflow** for daily news monitoring"

---

## 🗂️ File Locations

### PD Profiling Workflow
- **Prompts:** `workflows/pd-profiling/WORKFLOW-PROMPTS.md`
- **Examples:** `n16-sungai-balang-repo/`, `n17-semerah-repo/`
- **Skills:** (Integrated into main agent workflow, not separate skills)

### Loop Engineering News Workflow
- **Prompts:** `.agents/skills/loop-engineering/WORKFLOW-PROMPTS.md`
- **Skills:** `.agents/skills/loop-engineering/*/SKILL.md`
- **Output:** `memory/signals/`, `memory/briefs/`
- **Config:** `HEARTBEAT.md` (triggers daily collection)

---

## 📊 Quick Reference Card

```
┌─────────────────────────────────────────────────────────────┐
│  PD PROFILING WORKFLOW (3 Steps)                           │
├─────────────────────────────────────────────────────────────┤
│  Purpose: Constituency campaign intelligence                │
│  Input: SPR demographic data                                │
│  Output: PD briefs, campaign strategy, GOTV plan            │
│  Frequency: One-time per constituency                       │
│  Steps: 1. Demographic Analysis                             │
│         2. PD Operational Briefs                            │
│         3. Campaign Strategy Matrix                         │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│  LOOP ENGINEERING NEWS WORKFLOW (6 Steps)                  │
├─────────────────────────────────────────────────────────────┤
│  Purpose: Daily political monitoring                        │
│  Input: 32 Malaysian media sources                          │
│  Output: Signal Registry, daily intelligence brief          │
│  Frequency: Daily (23:00 UTC)                               │
│  Steps: 1. DeerFlow Collection                              │
│         2. PIR Entity Tagger                                │
│         3. Signal Quality Grader (Loop 2)                   │
│         4. Threshold Escalation Checker                     │
│         5. Signal Registry Writer                           │
│         6. Daily Brief Generator                            │
└─────────────────────────────────────────────────────────────┘
```

---

**Last Updated:** 2026-07-01  
**Maintainer:** Political Intelligence Team
