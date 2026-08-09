# PKR War Room — Data Ingestion Templates

**Classification:** TLP:AMBER — Operational Use Only  
**Version:** 1.0 (2026-06-28)  
**Purpose:** Standardized templates for structured data ingestion across all 56 DUNs

---

## 📋 Overview

These templates ensure consistent, actionable intelligence ingestion for the PKR Johor War Room. They are designed to:

1. **Standardize data collection** across all 56 DUNs
2. **Enable automated analysis** via the PRN Logic Engine
3. **Generate war room briefs** with consistent structure
4. **Track candidate intelligence** systematically
5. **Support dashboard integration** for real-time monitoring

---

## 🎯 Template Files

### 1. PKR-WAR-ROOM-DATA-TEMPLATE.md

**Location:** `templates/PKR-WAR-ROOM-DATA-TEMPLATE.md`

**Purpose:** Comprehensive markdown template for intelligence gathering

**Sections:**
1. Seat Metadata (code, name, parliament, electorate)
2. Demographics (PD-level breakdown)
3. Historical Results (2018, 2022, trend analysis)
4. Candidate Intelligence (PH/BN/PN/others)
5. PH Victory Path Analysis (scenarios, must-win PDs)
6. Turnout Reality Check (baseline vs targets)
7. Execution Checklist (3 phases)
8. Risk Assessment (indicators, mitigation)
9. Intelligence Gaps (tracking)
10. War Room Brief Output (distribution)

**Use Case:** Initial intelligence gathering, war room brief generation

**Example:** See `output/n17-semerah-war-room-brief-ph-2026-06-28.md`

---

### 2. SEAT-DATA-TEMPLATE.ts

**Location:** `templates/SEAT-DATA-TEMPLATE.ts`

**Purpose:** TypeScript data file for PRN Logic Engine ingestion

**Structure:**
```typescript
export const nXXSeatName: Seat = {
  code: 'NXX',
  name: 'Seat Name',
  federalCode: 'P.XXX',
  federalName: 'PARLIAMENT_NAME',
  district: 'District',
  totalElectorate: XXXXX,
  pollingDistricts: [...],
  candidates: { bn, ph, pn, muda?, bersama? },
  historicalResults: [...],
  notes?: [...]
}

export const analysis = {
  summary: '...',
  demographics: '...',
  turnout2022: '...',
  battlegrounds: '...',
  projection: '...'
}
```

**Use Case:** Engine ingestion, scenario calculations, dashboard data generation

**Example:** See `src/data/n17-semerah.ts`, `src/data/n27-layang-layang.ts`

---

### 3. CANDIDATES.md (Living Document)

**Location:** `src/data/CANDIDATES.md`

**Purpose:** Central registry for all candidate intelligence

**Features:**
- Status tracking (Confirmed/Likely/Monitoring/TBD)
- Candidate profiles with strengths/vulnerabilities
- Priority list for intelligence gathering
- Update instructions

**Use Case:** Candidate intelligence tracking, pre/post-nomination validation

---

## 🚀 Workflow

### Step 1: Excel Data Extraction

```bash
cd tools/prn-logic-engine
python3 scripts/extract-seat-data-from-excel.py
```

**Input:** Excel files from intelligence (voter roll, demographics)  
**Output:** TypeScript data file in `src/data/nXX-seat-name.ts`

---

### Step 2: Candidate Intelligence Gathering

1. Fill in `templates/PKR-WAR-ROOM-DATA-TEMPLATE.md` Section 4
2. Update `src/data/CANDIDATES.md` with candidate status
3. Update `src/data/nXX-seat-name.ts` candidates object

**Sources:**
- Public announcements
- Ground truth validation repos
- War room intelligence network
- Social media monitoring

---

### Step 3: Historical Results Validation

1. Cross-reference with SPR official results
2. Fill in `templates/PKR-WAR-ROOM-DATA-TEMPLATE.md` Section 3
3. Update `src/data/nXX-seat-name.ts` historicalResults array

**Critical:** Include both 2018 (GE) and 2022 (State) for trend analysis

---

### Step 4: Scenario Calculation

```bash
npm run dev -- calculate --seat NXX --format markdown
npm run dev -- calculate --seat NXX --format json
```

**Output:**
- `output/nXX-seat-name-scenarios-YYYY-MM-DD.md`
- `output/nXX-seat-name-scenarios-YYYY-MM-DD.json`

---

### Step 5: War Room Brief Generation

```bash
npm run dev -- calculate --seat NXX --format brief
```

**Output:** `output/nXX-seat-name-war-room-brief-ph-YYYY-MM-DD.md`

**Structure:**
- Bottom Line (verdict, baseline, victory target)
- The Math (2022 vs 2018, critical insights)
- PH Victory Path (scenarios, must-win PDs)
- Battleground Map (tier strategy)
- Turnout Reality Check
- Candidate Narrative
- Resource Allocation
- Scenario Tracking
- Execution Checklist

---

### Step 6: Commit and Push

```bash
git add src/data/nXX-seat-name.ts src/data/CANDIDATES.md output/nXX-*
git commit -m "Add NXX Seat Name — war room brief v1"
git push origin main
```

---

### Step 7: Dashboard Integration

**JSON Output:** Used for real-time dashboard visualization

**Dashboard Access:** See `DASHBOARD-ACCESS.md` for setup

**Metrics:**
- Turnout scenarios (S1-S6)
- PD-level projections
- Candidate profiles
- Win probability tracking

---

## 📊 Data Quality Standards

### Tier Classification

**Tier 1 (Kingmaker/Chinese Base):**
- Malay <40%
- Chinese/Indian >50%
- PH must-win zones
- Target turnout: 80-85%

**Tier 2 (Mixed):**
- Malay 40-75%
- Contestable
- Persuasion targets
- Target turnout: 65-75%

**Tier 3 (Malay Heartland):**
- Malay >75%
- BN/PN firewall
- Damage limit
- Target turnout: 60-70% (don't over-invest)

---

### Candidate Profile Requirements

**Minimum:**
- Full name with title
- Party and coalition
- Incumbent status (yes/no)
- Current position
- One strength
- One vulnerability

**Ideal:**
- Full name with title
- Party and coalition
- Incumbent status
- Current + previous positions
- Electoral history
- Community networks
- 3-5 strengths
- 2-3 vulnerabilities
- Campaign narrative
- Federal backing (if applicable)

---

### Historical Results Requirements

**Must Include:**
- 2022 State Election (turnout, votes, %, winner, majority)
- 2018 GE14 (turnout, votes, %, winner, majority)
- PH vote change (2018→2022)
- Turnout differential analysis

**Optional but Recommended:**
- 2013 GE13 (for long-term trend)
- By-election results (if applicable)
- Vote swing analysis

---

## 🎯 Quality Control Checklist

Before submitting a seat data file:

- [ ] All PDs classified (Tier 1/2/3)
- [ ] Demographics sum to 100% (auto-calculated)
- [ ] Total electorate matches sum of PDs
- [ ] Candidates confirmed (or marked TBD)
- [ ] Historical results include 2018 + 2022
- [ ] Analysis summary completed
- [ ] Turnout reality check included
- [ ] Must-win PDs identified
- [ ] Resource allocation strategy defined
- [ ] Execution checklist populated
- [ ] Test calculation runs successfully
- [ ] War room brief generates correctly

---

## 📝 Example: N17 Semerah

**Completed Files:**
- `src/data/n17-semerah.ts` (TypeScript data)
- `output/n17-semerah-war-room-brief-ph-2026-06-28.md` (war room brief)
- `output/n17-semerah-scenarios-2026-06-28.md` (scenario matrix)
- `src/data/CANDIDATES.md` (candidate registry entry)

**Key Features:**
- 26 PDs with tier classification
- 3 candidates with detailed profiles
- 2018 + 2022 historical results
- Turnout reality check (60.5% baseline, 82% target)
- 6 must-win Chinese PDs identified
- Resource allocation: 60% Tier 1, 25% Tier 2, 15% Tier 3
- Execution checklist (3 phases)

**See:** `output/n17-semerah-war-room-brief-ph-2026-06-28.md` for full example

---

## 🔧 Maintenance

**Template Updates:**
- Version control in git
- Changelog in this README
- Backward compatibility maintained

**Data Updates:**
- Post-nomination: validate all candidates
- Post-polling day: add 2026 results
- Continuous: update candidate intelligence

**Contact:** Loop Engineering Political Monitoring Unit

---

## 📚 Related Documentation

- `README.md` — PRN Logic Engine overview
- `DASHBOARD-ACCESS.md` — Dashboard setup guide
- `MULTI-COALITION-MONITORING.md` — Multi-coalition tracking
- `coalition-analysis/ph-daily-template.md` — PH daily report template
- `output/BATCH-PROCESSING-SUMMARY-20260628.md` — Batch processing summary

---

**Template Version:** 1.0 (2026-06-28)  
**Maintained by:** PKR Johor War Room Data Team  
**GitHub:** `https://github.com/ahmadfaurani/PRN-Johor-2026-H`
