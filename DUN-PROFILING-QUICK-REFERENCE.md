# DUN Profiling V1 — Quick Reference Card

**Last Updated:** 2026-07-03  
**Workflow:** DUN Profiling V1 (Three-Dimensional Analysis)  
**Scope:** Johor PRN 2026

---

## 🚀 Quick Start (5 Steps)

```bash
# Step 1: Demographics (SPR XLSX → Demographic Brief)
python DUN-Profiling/spr-xlsx-parser.py --input <spr-file>.xlsx --output nXX-demographic.json

# Step 2: Candidates (News → Candidate Brief)
# Execute via OpenClaw agent session

# Step 3: Historical (ElectionData.MY → Historical Brief)
# Execute via OpenClaw agent session

# Step 4: Synthesis (3 briefs → Master Operational Brief)
# Execute via OpenClaw agent session

# Step 5: GitHub Upload (4 briefs → Public Repository)
# Execute via OpenClaw agent session
```

---

## 📁 File Locations

| Resource | Path |
|----------|------|
| **Workflow Docs** | `DUN-Profiling/` |
| **Intelligence Briefs** | `memory/nXX-*.md` |
| **GitHub Repos** | `github/` |
| **Validation Scripts** | `tools/truth-validator/` |
| **SPR Parser** | `DUN-Profiling/spr-xlsx-parser.py` |
| **Focus List** | `tools/prn-logic-engine/DUN-FOCUS-LIST.md` |

---

## 📊 Completed Constituencies

| Code | Name | Parliament | Status | Briefs | GitHub |
|------|------|------------|--------|--------|--------|
| N03 | Pemanis | P145 | ✅ Partial | 3/4 | ❌ No |
| N09 | Gambir | P145 | ✅ Complete | 4/4 | ✅ Yes |
| N14 | Bukit Naning | P148 | ✅ Complete | 4/4 | ❌ No |
| N16 | Sungai Balang | P146 | ✅ Complete | 6/4 | ❌ No |
| N17 | Semerah | P147 | ✅ Complete | 7/4 | ✅ Yes |
| N32 | Endau | P154 | ⚠️ Partial | 2/4 | ❌ No |
| N33 | Tenggaroh | P154 | ⚠️ Partial | 2/4 | ❌ No |

**Total:** 6 constituencies, 28+ briefs, 2 GitHub repos

---

## 🏷️ Brief Naming Convention

**Standard Format:**
```
memory/nXX-constituency-{type}-brief-YYYYMMDD.md
```

**Types:**
- `demographic` — PD-level voter composition
- `candidate` — Candidate profiles + alignment
- `historical` — Past results + swing analysis
- `synthesis` or `master-operational` — Integrated guidance
- `war-room` — Condensed operational brief

**Examples:**
- `memory/n17-semerah-demographic-brief-20260701.md`
- `memory/n16-sungai-balang-synthesis-brief-20260701.md`

---

## ✅ CVS Validation (Mandatory)

**Before any brief is delivered:**

```bash
./tools/truth-validator/validate.sh memory/nXX-constituency-brief.md || exit 1
```

**Exit Codes:**
- `0` → PASSED (safe to deliver)
- `1` → FAILED (blocks delivery)

**Requirements:**
- ✅ All Tier 1 claims have ≥2 sources
- ✅ All analytical claims tagged [HIGH/MEDIUM/LOW]
- ✅ All predictive claims flagged SPECULATION:/SCENARIO:
- ✅ All citations valid (file#line exists)

---

## 📞 Support

| Issue | Contact |
|-------|---------|
| Workflow questions | Political Intelligence Team |
| CVS validation | Automated (validate.sh) |
| GitHub upload | DAF |
| SPR data | ElectionData.MY API |

---

## 📚 Documentation

| Doc | Purpose |
|-----|---------|
| `DUN-PROFILING-WORKSPACE.md` | Complete workspace index |
| `DUN-Profiling/README.md` | Workflow overview |
| `DUN-Profiling/WORKFLOW-PROMPTS.md` | Step-by-step prompts |
| `DUN-Profiling/CVS-COMPLIANCE.md` | Validation report |
| `tools/truth-validator/CVS-SCOPE-DUN-PROFILING.md` | CVS scope |

---

**Quick Reference Version:** 1.0  
**Print-Friendly:** Yes (1 page)

