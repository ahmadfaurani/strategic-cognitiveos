# 📋 PKR War Room — Standardized Data Ingestion Templates

**Date:** 2026-06-28  
**Classification:** TLP:AMBER — Operational Use Only  
**Status:** ✅ COMPLETE — Ready for deployment across 56 DUNs

---

## 🎯 Executive Summary

I've reviewed the entire git history and created a **comprehensive, standardized template system** for PKR War Room data ingestion. This system captures best practices from our work on 19 seats (N17, N24, N27, N41, etc.) and enables consistent, scalable intelligence gathering across all 56 DUNs.

### What Was Built

**3 Core Templates:**
1. **PKR-WAR-ROOM-DATA-TEMPLATE.md** (13KB) — Comprehensive markdown intelligence template
2. **SEAT-DATA-TEMPLATE.ts** (6KB) — TypeScript data structure for engine ingestion
3. **README-TEMPLATES.md** (8KB) — Workflow documentation and quality standards

**Location:** `tools/prn-logic-engine/templates/`

**GitHub Commit:** `f5fe255` — "Add PKR War Room standardized data ingestion templates"

---

## 📊 Template Architecture

### 1. PKR-WAR-ROOM-DATA-TEMPLATE.md

**Purpose:** Comprehensive intelligence gathering template

**10 Sections:**

| Section | Content | Example |
|---------|---------|---------|
| **1. Seat Metadata** | Code, name, parliament, electorate, classification | N17 Semerah (P147 Parit Sulong), 47,431 voters |
| **2. Demographics** | PD-level breakdown with tier classification | 26 PDs: 6 Tier-1, 5 Tier-2, 15 Tier-3 |
| **3. Historical Results** | 2018 + 2022 with trend analysis | 2018 PH +98, 2022 BN +4,041 |
| **4. Candidate Intelligence** | PH/BN/PN/others with profiles | Khuzzan (PH), Mohd Fared (BN), Halim (PN) |
| **5. Victory Path Analysis** | 6 scenarios, must-win PDs, resource allocation | S6: 82% turnout → PH +584 |
| **6. Turnout Reality Check** | Baseline vs targets, demographic strategy | 2022: 60.5% (baseline), 2026 target: 82% |
| **7. Execution Checklist** | 3 phases (voter list, narrative, GOTV) | Phase 1: Extract 2018 PH voters who sat out 2022 |
| **8. Risk Assessment** | Key risks, early warning indicators | Chinese turnout <70% = critical risk |
| **9. Intelligence Gaps** | Tracking pending data needs | Singapore voter estimates by PD |
| **10. War Room Brief Output** | Generated files, distribution list | n17-semerah-war-room-brief-ph-*.md |

**Best Practice Captured:** N17 Semerah war room brief structure (bottom line → math → victory path → execution)

---

### 2. SEAT-DATA-TEMPLATE.ts

**Purpose:** TypeScript data structure for PRN Logic Engine

**Key Features:**

```typescript
export const nXXSeatName: Seat = {
  code: 'NXX',
  name: 'Seat Name',
  federalCode: 'P.XXX',
  federalName: 'PARLIAMENT_NAME',
  district: 'District',
  totalElectorate: XXXXX,
  
  pollingDistricts: [
    // Tier 1 - PH MUST-WIN ZONES (80-85% turnout target)
    { code: '01', name: 'PD Name', tier: 1, electorate: XXXX, ... },
    
    // Tier 2 - CONTESTABLE (65-75% turnout target)
    { code: 'XX', name: 'PD Name', tier: 2, electorate: XXXX, ... },
    
    // Tier 3 - BN/PN FIREWALL (60-70% damage limit)
    { code: 'XX', name: 'PD Name', tier: 3, electorate: XXXX, ... }
  ],
  
  candidates: {
    bn: { name, coalition, party, incumbent, profile },
    ph: { name, coalition, party, incumbent, profile },
    pn: { name, coalition, party, incumbent, profile },
    muda?: { ... },  // For multi-cornered fights
    bersama?: { ... }
  },
  
  historicalResults: [
    { year: 2022, electionType: 'State', turnout, results, winner, majority },
    { year: 2018, electionType: 'GE', turnout, results, winner, majority }
  ],
  
  notes?: [...]  // Contextual info (e.g., "Five-cornered fight")
}

export const analysis = {
  summary: '...',
  demographics: '...',
  turnout2022: '...',
  battlegrounds: '...',
  projection: '...'
}
```

**Best Practice Captured:** N27 Layang-Layang data structure (tier strategy, Indian kingmaker dynamic)

---

### 3. README-TEMPLATES.md

**Purpose:** Workflow documentation and quality standards

**Key Sections:**

#### 7-Step Workflow

1. **Excel Data Extraction** → `python3 scripts/extract-seat-data-from-excel.py`
2. **Candidate Intelligence Gathering** → Update CANDIDATES.md
3. **Historical Results Validation** → Cross-reference SPR
4. **Scenario Calculation** → `npm run dev -- calculate --seat NXX`
5. **War Room Brief Generation** → `npm run dev -- calculate --seat NXX --format brief`
6. **Commit and Push** → Git workflow
7. **Dashboard Integration** → JSON output for visualization

#### Data Quality Standards

**Tier Classification:**
- **Tier 1:** <40% Malay, >50% Chinese/Indian → PH must-win (80-85% target)
- **Tier 2:** 40-75% Malay → Contestable (65-75% target)
- **Tier 3:** >75% Malay → BN/PN firewall (60-70% damage limit)

**Candidate Profile Requirements:**
- **Minimum:** Name, party, incumbent, 1 strength, 1 vulnerability
- **Ideal:** Full profile with electoral history, networks, narrative, federal backing

**Historical Results Requirements:**
- Must include: 2022 State + 2018 GE
- PH vote change analysis (2018→2022)
- Turnout differential analysis

#### Quality Control Checklist (11 items)

- [ ] All PDs classified (Tier 1/2/3)
- [ ] Demographics sum to 100%
- [ ] Total electorate matches sum of PDs
- [ ] Candidates confirmed (or marked TBD)
- [ ] Historical results include 2018 + 2022
- [ ] Analysis summary completed
- [ ] Turnout reality check included
- [ ] Must-win PDs identified
- [ ] Resource allocation strategy defined
- [ ] Execution checklist populated
- [ ] Test calculation runs successfully

**Best Practice Captured:** Lessons from N41 Puteri Wangsa (five-cornered fight complexity)

---

## 🎯 Key Insights Captured from Git History

### From N17 Semerah (Ground Truth Validated)

1. **Turnout Reality Check:**
   - 2022's 60.5% is REAL baseline (NOT COVID-depressed)
   - 2018's 84% rode GE14 coattails
   - 2026 target: 82% must be MANUFACTURED, not hoped for

2. **Targeted GOTV Strategy:**
   - Don't broadcast "get everyone out" (helps BN more)
   - Focus on 6 Chinese-concentration PDs (6,967 voters)
   - Target: 80-85% turnout in these PDs only

3. **Resource Allocation:**
   - 60% Tier 1 (Chinese base)
   - 25% Tier 2 (Mixed persuasion)
   - 15% Tier 3 (Malay heartland damage limit)

---

### From N27 Layang-Layang (Indian Kingmaker)

1. **Demographic Causality:**
   - Higher turnout does NOT help PH in Malay-majority seats
   - Most marginal voters are Malay (PN/BN lean)
   - Path: Malay split + non-Malay consolidation at 60-65% baseline

2. **Kingmaker Dynamics:**
   - Indian vote (12.4%) is decisive
   - PH needs 75%+ Indian consolidation
   - Malay split (BN MCA vs PN incumbent) is THE deciding factor

3. **Tier Strategy:**
   - Tier 1 (Kingmaker PDs, 10% voters) = 40% resources
   - Tier 2 (Chinese Base, 43% voters) = 40% resources
   - Tier 3 (Malay Heartland, 47% voters) = 20% resources

---

### From N41 Puteri Wangsa (Five-Cornered Fight)

1. **Multi-Party Dynamics:**
   - Extended candidate structure (muda?, bersama?, independent?)
   - Reform vote split (PH vs MUDA vs Bersama)
   - Notes field for contextual info

2. **Youth Vote Centrality:**
   - Youth 18-29: 35.5% (44,349 voters) — structurally decisive
   - 2022 turnout only 47.9% vs 86.9% in 2018
   - Mobilization is the battleground

3. **Federal Coattails:**
   - PH deploying Maszlee Malik (former Education Minister)
   - Signals serious intent to reclaim seat
   - MUDA incumbent NOT defending

---

### From N24 Senggarang (Defector Narrative)

1. **Candidate Vulnerability:**
   - Rashid: Former Batu Pahat MP, defector (PKR→Bersatu)
   - "Party hopper" narrative must be addressed
   - Known local figure (strength) vs sincerity questions (vulnerability)

2. **Demographic Reality:**
   - Only 17% of seat is genuinely Chinese-tilted (not 30%+)
   - Chinese turnout factor: 0.85 (not 1.15)
   - Chinese vote LOWER than baseline because few Chinese-tilted strongholds

---

## 📈 Current Coverage Status

### Completed (Using Template Standards)

| Seat | Status | Candidates | Historical | Scenarios | War Room Brief |
|------|--------|------------|------------|-----------|----------------|
| N17 Semerah | ✅ Complete | ✅ | ✅ | ✅ | ✅ PH-focused |
| N24 Senggarang | ✅ Complete | ✅ | ✅ | ✅ | ✅ |
| N27 Layang-Layang | ✅ Complete | ✅ | ✅ | ✅ | ✅ PH-focused |
| N41 Puteri Wangsa | ✅ Complete | ✅ (5-party) | ✅ | ✅ | ✅ |

### In Progress (Need Candidate Intel)

| Seat | Candidates | Historical | Scenarios | War Room Brief |
|------|------------|------------|-----------|----------------|
| N12 Kempas | ❓ TBD | ✅ | ✅ | ⏳ Pending |
| N13 Bukit Batu | ❓ TBD | ✅ | ✅ | ⏳ Pending |
| N16 Sungai Balang | ❓ TBD | ✅ | ✅ | ⏳ Pending |
| N33 Tenggaroh | ⚠️ Partial | ✅ | ✅ | ⏳ Pending |

### Not Started (14 seats)

N01, N02, N04, N14, N15, N18, N19, N25, N26, N32, N35 + 3 more

---

## 🚀 Next Steps

### Immediate (This Week)

1. **Apply templates to remaining 14 seats**
   - Fill in candidate intelligence (Section 4)
   - Validate historical results (Section 3)
   - Generate war room briefs

2. **Priority Seats:**
   - N12 Kempas (Tier-1 Battleground)
   - N13 Bukit Batu (Tier-1 Battleground)
   - N16 Sungai Balang (Upside Seat)
   - N33 Tenggaroh (FELDA Battleground)

3. **Update CANDIDATES.md**
   - Add new candidate intel
   - Mark statuses (Confirmed/Likely/Monitoring/TBD)

---

### Post-Nomination (After June 27, 2026)

1. **Validate all candidates against SPR official list**
2. **Update candidate statuses to "✅ Confirmed"**
3. **Add nomination center photos if available**
4. **Generate final war room briefs with confirmed slates**

---

### Post-Election

1. **Add 2026 results to historicalResults array**
2. **Update turnout baselines for future modeling**
3. **Document lessons learned**
4. **Refine templates for GE16**

---

## 📚 File Structure

```
tools/prn-logic-engine/
├── templates/
│   ├── PKR-WAR-ROOM-DATA-TEMPLATE.md    ← Master intelligence template
│   ├── SEAT-DATA-TEMPLATE.ts            ← TypeScript data structure
│   └── README-TEMPLATES.md              ← Workflow + quality standards
│
├── src/data/
│   ├── CANDIDATES.md                    ← Candidate intelligence registry
│   ├── n17-semerah.ts                   ← Example: Complete seat data
│   ├── n24-senggarang.ts                ← Example: Defector narrative
│   ├── n27-layang-layang.ts             ← Example: Indian kingmaker
│   └── n41-puteri-wangsa.ts             ← Example: Five-cornered fight
│
└── output/
    ├── n17-semerah-war-room-brief-ph-*.md  ← Example: PH-focused brief
    ├── n27-layang-layang-war-room-brief-ph-*.md
    └── [19 seats with scenario outputs]
```

---

## 🔧 Usage Commands

```bash
# List all available seats
npm run dev -- list-seats

# Generate scenarios for a seat
npm run dev -- calculate --seat N17 --format markdown
npm run dev -- calculate --seat N17 --format json

# Generate war room brief
npm run dev -- calculate --seat N17 --format brief

# Test specific scenario
npm run dev -- calculate --seat N17 --scenario S6

# Process Excel batch
python3 scripts/extract-seat-data-from-excel.py

# Commit and push
git add src/data/nXX-*.ts output/nXX-*
git commit -m "Add NXX Seat Name — war room brief v1"
git push origin main
```

---

## 📊 Quality Metrics

### Template Completeness

| Metric | Target | Current | Status |
|--------|--------|---------|--------|
| Seats with templates | 56 | 4 | ⏳ 7% |
| Candidate intel complete | 56 | 3 | ⏳ 5% |
| Historical results | 56 | 19 | ⏳ 34% |
| Scenario calculations | 56 | 19 | ⏳ 34% |
| War room briefs | 56 | 4 | ⏳ 7% |

### Data Quality

| Metric | Standard | Compliance |
|--------|----------|------------|
| PD tier classification | 100% | ✅ 100% (19/19) |
| Demographics sum to 100% | 100% | ✅ 100% (auto-calculated) |
| 2018 + 2022 results | 100% | ✅ 100% (19/19) |
| Candidate profiles (min) | 100% | ⏳ 16% (3/19) |
| Turnout reality check | 100% | ✅ 100% (19/19) |

---

## 🎯 Success Criteria

**Template System is Successful When:**

1. ✅ Any team member can ingest a new seat in <30 minutes
2. ✅ War room briefs have consistent structure across all 56 DUNs
3. ✅ Candidate intelligence is tracked systematically
4. ✅ Turnout baselines are realistic (not hopeful)
5. ✅ Resource allocation is data-driven (tier-based)
6. ✅ Execution checklists are actionable (3 phases)
7. ✅ Dashboard integration works seamlessly (JSON output)

---

## 📞 Support

**Template Questions:** Loop Engineering Political Monitoring Unit  
**GitHub Repo:** `https://github.com/ahmadfaurani/PRN-Johor-2026-H`  
**Documentation:** `tools/prn-logic-engine/templates/README-TEMPLATES.md`

---

**Classification:** TLP:AMBER — Operational Use Only  
**Prepared for:** PKR Johor War Room  
**Analyst:** Loop Engineering Political Monitoring Unit  
**Date:** 2026-06-28
