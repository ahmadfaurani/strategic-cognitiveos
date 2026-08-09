# Workflow Documentation Index

This directory contains separate, well-documented workflows for political intelligence operations.

## 📁 Workflow Separation

To avoid confusion between different operational pipelines, workflows are organized into separate directories:

---

## 1️⃣ DUN Profiling V1 (5 Steps) ✅ VALIDATED

**Location:** `workflows/dun-profiling/`  
**Workflow Name:** DUN Profiling V1  
**Status:** ✅ Production-ready (N.27 Layang-Layang test run complete)

**Purpose:** Three-dimensional constituency intelligence package (Demographics + Candidates + Historical + Synthesis + GitHub Upload).

**Steps:**
1. **Demographics** — PD-level voter composition, tier classification (SPR XLSX)
2. **Candidates** — Candidate profiles, demographic alignment, vote projections
3. **Historical** — Election results, turnout sensitivity, swing analysis
4. **Synthesis** — Master operational brief (BLUF, Strategy, Risk, Actionable Intel)
5. **GitHub Upload** — Private repository with structured workspace

**Output:** 4 brief documents + GitHub repository (TLP:AMBER, private)

**Used For:** N.27 Layang-Layang ✅, N16 Sungai Balang (queued), N17 Semerah (queued), N32 Endau (queued), N41 Puteri Wangsa (queued)

---

## 2️⃣ PD Profiling Workflow (3 Steps)

**Location:** `workflows/pd-profiling/`

**Purpose:** Generate comprehensive Polling District (PD) profiles for campaign operational planning.

**Steps:**
1. **Demographic Data Analysis** - Process SPR demographic data, extract PD-level statistics
2. **PD Operational Brief** - Generate structured briefs for each PD (tier classification, targets, issues)
3. **Campaign Strategy Matrix** - Create targeting matrix, resource allocation, GOTV priorities

**Output:** PD-level intelligence for campaign teams

**Used For:** N16 Sungai Balang, N17 Semerah, N32 Endau, etc.

---

## 3️⃣ Loop Engineering News Collection Workflow (6 Steps)

**Location:** `workflows/loop-engineering-news/` (or `.agents/skills/loop-engineering/`)

**Purpose:** Automated daily political news collection, tagging, grading, and brief generation.

**Steps:**
1. **DeerFlow News Collection** - Collect from 32 Malaysian media sources
2. **PIR Entity Tagger** - Extract entities, tag with PIR-1 to PIR-10
3. **Signal Quality Grader** - Loop 2 verification (5-criteria rubric)
4. **Threshold Escalation Checker** - Assign ESC-001 to ESC-006 severity levels
5. **Signal Registry Writer** - Write to Signal Registry with deduplication
6. **Daily Brief Generator** - Generate structured intelligence brief

**Output:** Daily political intelligence brief (Telegram delivery)

**Used For:** Daily monitoring, PIR tracking, emerging narrative detection

---

## 📊 Key Differences

| Aspect | DUN Profiling V1 | PD Profiling | Loop Engineering News |
|--------|------------------|--------------|----------------------|
| **Steps** | 5 | 3 | 6 |
| **Frequency** | Per constituency (one-time) | Per PD (one-time) | Daily (automated) |
| **Input** | SPR + News + Historical | SPR demographic data | News articles (32 sources) |
| **Output** | 4 briefs + GitHub repo | PD operational briefs | Daily intelligence brief |
| **Loop Level** | Linear workflow | Linear workflow | 4-loop framework |
| **Use Case** | Constituency intelligence | Campaign planning | Continuous monitoring |
| **Status** | ✅ Validated | Manual | Automated |

---

## 📚 Documentation

Each workflow directory contains:
- `WORKFLOW-PROMPTS.md` - Detailed prompts for each step
- `WORKFLOW-SCHEMA.md` - Input/output schemas, data structures, validation rules
- `CONFIG.md` - Configuration options, environment variables, deployment settings
- `EXAMPLES.md` - Real-world sample outputs from completed constituencies

---

**Last Updated:** 2026-07-01  
**Maintainer:** Political Intelligence Team
