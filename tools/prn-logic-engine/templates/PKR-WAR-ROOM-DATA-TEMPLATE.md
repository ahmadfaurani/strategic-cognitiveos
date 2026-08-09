# PKR War Room — Data Ingestion Template

**Classification:** TLP:AMBER — Operational Use Only  
**Version:** 1.0 (2026-06-28)  
**Purpose:** Standardized structured data ingestion for PKR Johor War Room

---

## 📋 How to Use This Template

This template ensures consistent, actionable intelligence ingestion across all 56 DUNs. Fill in **ALL** sections. If data is unavailable, mark as `TBD` with notes on what's needed.

**Submit to:** `tools/prn-logic-engine/src/data/nXX-seat-name.ts`  
**Reference:** `tools/prn-logic-engine/src/data/CANDIDATES.md`  
**Output:** `tools/prn-logic-engine/output/nXX-seat-name-war-room-brief-ph-YYYY-MM-DD.md`

---

## 🎯 Section 1: Seat Metadata

```yaml
seat_code: "N17"
seat_name: "Semerah"
parliament_code: "P147"
parliament_name: "Parit Sulong"
district: "Batu Pahat"
region: "Southern Johor"
total_electorate: 47431
polling_district_count: 26
classification: "Tier-2 Upside Seat"
priority: "MEDIUM-HIGH"
```

**Classification Guide:**
- **Tier-1 Battleground:** Must-win, high resource allocation (e.g., N41 Puteri Wangsa)
- **Tier-2 Upside:** Winnable with targeted investment (e.g., N17 Semerah, N16 Sungai Balang)
- **Tier-2 Defensive:** BN-leaning but contestable (e.g., N24 Senggarang)
- **Tier-3 Monitoring:** Low priority, minimal resources (e.g., N01 Buloh Kasap)

---

## 📊 Section 2: Demographics (PD-Level Required)

### 2.1 Overall Demographics

```yaml
demographics:
  malay:
    count: 35633
    percentage: 75.1
  chinese:
    count: 11027
    percentage: 23.2
  indian:
    count: 771
    percentage: 1.7
  others:
    count: 0
    percentage: 0.0
youth_18_29:
  count: 11722
  percentage: 24.7
gender:
  female: 51.0
  male: 49.0
```

### 2.2 Polling District Breakdown (CSV Format)

```csv
code,name,tier,electorate,malay_pct,chinese_pct,indian_pct,others_pct,turnout2022
01,Peserai,3,5986,92.5,5.9,0.5,1.1,68
02,Parit Maimon,3,5554,92.7,5.9,0.5,0.9,68
03,Separap,3,2310,96.6,1.9,0.5,1.0,70
14,Kampung Pantai Timor,1,2743,21.4,75.0,1.2,2.4,52
15,Shahbandar,1,1606,7.2,91.5,0.8,0.5,51
```

**Tier Classification:**
- **Tier 1 (Kingmaker/Chinese Base):** <40% Malay, >50% Chinese/Indian — PH must-win zones
- **Tier 2 (Mixed):** 40-75% Malay — contestable, persuasion targets
- **Tier 3 (Malay Heartland):** >75% Malay — BN/PN firewall, damage limit

---

## 🏛️ Section 3: Historical Results

### 3.1 2022 State Election

```yaml
year: 2022
election_type: "State"
turnout_percentage: 60.5
total_votes: 27908
results:
  bn:
    party: "BN-UMNO"
    candidate: "Mohd Fared Mohd Khalid"
    votes: 12542
    percentage: 44.8
  ph:
    party: "PH-PKR"
    candidate: "Mohd Khuzzan Abu Bakar"
    votes: 6265
    percentage: 22.4
  pn:
    party: "PN-PAS"
    candidate: "Halim@Othman Kepol"
    votes: 8501
    percentage: 30.4
winner: "BN"
majority: 4041
margin_percentage: 14.5
```

### 3.2 2018 GE14

```yaml
year: 2018
election_type: "GE"
turnout_percentage: 84.0
total_votes: 25140
results:
  bn:
    party: "BN-UMNO"
    candidate: "Mohd Fared Mohd Khalid"
    votes: 12521
    percentage: 49.8
  ph:
    party: "PH-PKR"
    candidate: "Mohd Khuzzan Abu Bakar"
    votes: 12619
    percentage: 50.2
winner: "PH"
majority: 98
margin_percentage: 0.4
```

### 3.3 Historical Trend Analysis

```markdown
**2018→2022 PH Vote Collapse:** -50.4% (12,619 → 6,265)

**Root Cause:** Chinese abstention (turnout 45-53% in Chinese PDs vs 75%+ in 2018), NOT voter defection to BN.

**Combined Opposition Math (2022):** PH 6,265 + PN 8,501 = 14,766 vs BN 12,542  
→ BN wins ONLY if opposition stays split.

**Turnout Differential:**
- 2018: 84% (GE coattails, federal + state same day)
- 2022: 60.5% (standalone state baseline)
- 2026 Projection: 62-68% (standalone state, no federal coattails)
```

---

## 👥 Section 4: Candidate Intelligence

### 4.1 PH Candidate (PKR)

```yaml
candidate:
  full_name: "Mohd Khuzzan Abu Bakar"
  party: "PKR"
  coalition: "PH"
  status: "✅ Confirmed"
  incumbent: false
  former_adun: true
  former_adun_years: "2018-2022"
  current_position: "Deputy Chairman TalentCorp"
  previous_exco: true
  exco_portfolio: "Johor EXCO (2018-2022)"
  
strengths:
  - "Won this seat in 2018 (by 98 votes)"
  - "Served as ADUN 2018-2022 + Johor EXCO"
  - "Name recognition, local track record"
  - "Federal backing (Fahmi Fadzil at nomination)"
  - "Technocratic credibility"

vulnerabilities:
  - "2022 collapse: 12,619 → 6,265 votes (-50.4%)"
  - "Must convince voters this was turnout anomaly, not mandate loss"

campaign_narrative: "The Comeback — Khuzzan delivered for Semerah 2018-2022. 2022 was a protest vote, not a rejection."

federal_backing:
  confirmed: true
  supporters:
    - "Fahmi Fadzil (PH Communications Director)"
    - "Anwar Ibrahim (campaign appearance planned)"
```

### 4.2 BN Candidate

```yaml
candidate:
  full_name: "Mohd Fared Mohd Khalid"
  party: "UMNO"
  coalition: "BN"
  status: "✅ Confirmed"
  incumbent: true
  current_position: "Johor EXCO for Islamic Religious Affairs"
  profession: "Lawyer"
  
strengths:
  - "Incumbency advantage"
  - "EXCO portfolio (Islamic Religious Affairs)"
  - "Ketua Kampung network"
  - "Service delivery track record"

vulnerabilities:
  - "Cost-of-living protest vote aggregator"
  - "Malay leakage risk to PN"

campaign_narrative: "Maju Johor stability + direct access via EXCO portfolio"
```

### 4.3 PN Candidate

```yaml
candidate:
  full_name: "Halim@Othman Kepol (Abang Halim)"
  party: "PAS"
  coalition: "PN"
  status: "✅ Confirmed"
  incumbent: false
  
strengths:
  - "Deep local embeddedness (PAS networks)"
  - "PASTI networks, mosque committees"
  - "Protest vote magnet"

vulnerabilities:
  - "Structural ceiling — near-zero Chinese vote"
  - "Needs massive Malay split to win"

campaign_narrative: "Clean Malay-Islamic alternative, cost-of-living framing"
```

### 4.4 Other Candidates (if applicable)

```yaml
muda:
  full_name: "Rashifa Aljunied"
  party: "MUDA"
  status: "✅ Confirmed"
  age: 26
  position: "Chief of Staff to MUDA President"
  incumbent: false
  notes: "Incumbent Amira Aisya NOT defending"

bersama:
  full_name: "Nicholas Paul Vincent"
  party: "Parti Bersama"
  status: "⚠️ Likely"
  
independents: []
```

---

## 🎯 Section 5: PH Victory Path Analysis

### 5.1 Turnout Scenarios

| Scenario | Turnout | PH Votes | PH % | BN Votes | PN Votes | Winner | Margin | Probability |
|----------|---------|----------|------|----------|----------|--------|--------|-------------|
| S1: 2022 Repeat | 60.5% | 6,428 | 22.4% | 12,856 | 8,684 | BN | +4,172 | High |
| S2: Baseline | 66% | 8,296 | 26.5% | 13,891 | 9,345 | BN | +4,540 | **60-65%** |
| S3: Optimistic | 70% | 9,463 | 28.5% | 14,691 | 9,883 | BN | +4,814 | 30-35% |
| S4: Chinese Recovery | 75% | 11,739 | 33.0% | 15,652 | 10,529 | BN | +2,668 | 20-25% |
| S5: PN Breakthrough | 70% | 9,629 | 29.0% | 13,047 | 11,158 | BN | +665 | Low |
| **S6: GOTV Target** | **82%** | **15,363** | **39.5%** | **16,194** | **10,585** | **PH** | **+584** | **15-20%** |

### 5.2 Must-Win Polling Districts

```yaml
must_win_pds:
  - code: "14"
    name: "Kampung Pantai Timor"
    chinese_pct: 75.0
    electorate: 2743
    turnout2022: 52
    target_turnout: 80
    ph_votes_needed: 750
    priority: "CRITICAL"
    
  - code: "15"
    name: "Shahbandar"
    chinese_pct: 91.5
    electorate: 1606
    turnout2022: 51
    target_turnout: 85
    ph_votes_needed: 600
    priority: "CRITICAL"
    
  - code: "16"
    name: "Jalan Jenang"
    chinese_pct: 92.9
    electorate: 1529
    turnout2022: 50
    target_turnout: 85
    ph_votes_needed: 550
    priority: "CRITICAL"
```

### 5.3 Resource Allocation Strategy

```yaml
resource_allocation:
  tier1_chinese_base:
    pd_count: 6
    voter_share: 16.4
    resource_share: 60
    strategy: "GOTV machinery, door-knocking, Singapore voter coordination"
    
  tier2_mixed:
    pd_count: 5
    voter_share: 13.7
    resource_share: 25
    strategy: "Khuzzan nostalgia campaign, persuasion, moderate Malay outreach"
    
  tier3_malay_heartland:
    pd_count: 15
    voter_share: 71.6
    resource_share: 15
    strategy: "Damage limit, young voter mobilization, let PN split BN vote"
```

---

## ⚠️ Section 6: Turnout Reality Check

```markdown
## Critical Turnout Insights

### 2022's ~60% is the REAL baseline
- NOT COVID-depressed
- NOT an anomaly that will "bounce back"
- This is what standalone state elections do in rural Malay seats

### 2018's 84% rode GE14 coattails
- Federal election brought home Singapore/outstation voters
- State election rode along
- Same voters voted twice in one year (March + November 2022)

### July 2026 is STATE-ONLY
- Natural turnout: 62-68% (like March 2022)
- At 66% turnout: **BN wins by +4,540**
- At 70% turnout: **BN wins by +4,814** (PN breakthrough risk)
- At 82% turnout: **PH wins by +584** ← **OUR TARGET**

**82% doesn't happen automatically. We build it.**

### Demographic-Specific Turnout Strategy

**Chinese Voters:**
- 2022 turnout: 45-53% in Chinese PDs
- 2026 target: 80-85% in 6 key PDs
- Strategy: "This vote decides the country's direction, not just who runs Johor"

**Malay Voters:**
- 2022 turnout: 65-75% in rural Malay PDs
- 2026 projection: 68-72% (slight increase)
- Reality: Higher Malay turnout helps BN/PN, not PH

**Indian Voters:**
- 2022 turnout: 50-55%
- 2026 target: 75%+ (kingmaker bloc)
- Strategy: Community leaders, temple networks, economic messaging
```

---

## 🔥 Section 7: Execution Checklist

### Phase 1: Voter List Building (Now — Nomination)

```markdown
- [ ] Extract 2018 PH voters from 6 Chinese PDs who sat out 2022
- [ ] Build WhatsApp groups for each PD
- [ ] Identify Singapore-based voters (early voting coordination)
- [ ] Map 2022 PN voters for potential persuasion (young Malays)
- [ ] Recruit polling agents (2 per stream in Tier 1/2 PDs)
```

### Phase 2: Narrative Deployment (Nomination — Campaign)

```markdown
- [ ] "Khuzzan Won This Seat in 2018" messaging
- [ ] EXCO track record: what he delivered for Semerah
- [ ] Federal coattails: Fahmi Fadzil appearances
- [ ] Social media: TikTok/Instagram youth outreach
- [ ] Traditional media: Chinese press, Tamil radio
```

### Phase 3: GOTV Manufacturing (Campaign — Polling Day)

```markdown
- [ ] Door-knock priority: 2018 PH voters who didn't vote 2022
- [ ] Transport coordination for Singapore workers
- [ ] Young voter mobilization (18-30 cohort, 24.7% of seat)
- [ ] **Target:** 6 Chinese PDs at 80-85% turnout
- [ ] Real-time turnout tracking (WhatsApp reports every 2 hours)
- [ ] 6 PM surge: target low-turnout PDs
```

---

## 📈 Section 8: Risk Assessment

### 8.1 Key Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Chinese turnout <70% | High | Critical | Early voting drives, Singapore transport |
| PN exceeds 2022 base (8,501) | Medium | High | Monitor PAS mosque networks, youth outreach |
| Malay leakage to PN >35% | Medium | High | Khuzzan's moderate Malay appeal, federal coattails |
| Federal coattails weak | Low | Medium | Ground game over-reliance, not top-down |
| Agent shortage in Tier 3 | Low | Low | Prioritize Tier 1/2, accept Tier 3 losses |

### 8.2 Early Warning Indicators

```yaml
warning_indicators:
  - indicator: "Chinese PD early voting <40%"
    threshold: "40% by Day 3"
    action: "Emergency GOTV surge, WhatsApp blast"
    
  - indicator: "PN rally attendance >2,000"
    threshold: "2,000 attendees"
    action: "Counter-rally, deploy federal VIPs"
    
  - indicator: "Social media sentiment shift"
    threshold: ">60% negative PH mentions"
    action: "Rapid response team, narrative correction"
```

---

## 📝 Section 9: Intelligence Gaps

```yaml
gaps:
  - data_type: "2026 voter roll updates"
    status: "PENDING"
    needed_by: "2026-07-01"
    owner: "Data Team"
    
  - data_type: "BN/PN candidate campaign schedules"
    status: "MONITORING"
    needed_by: "2026-07-05"
    owner: "Intel Team"
    
  - data_type: "Singapore voter estimates by PD"
    status: "IN_PROGRESS"
    needed_by: "2026-07-10"
    owner: "GOTV Team"
```

---

## 📊 Section 10: War Room Brief Output

**Generated Files:**
- `output/n17-semerah-war-room-brief-ph-2026-06-28.md` (PH-focused playbook)
- `output/n17-semerah-scenarios-2026-06-28.md` (full scenario matrix)
- `output/n17-semerah-dashboard.json` (dashboard data)

**Distribution:**
- PH Johor War Room (Telegram channel)
- PKR Batu Pahat Division
- Campaign Director (Fahmi Fadzil office)
- Ground coordinators (6 Chinese PD leads)

**Next Update:** Post-nomination candidate profiling (2026-07-05)

---

## 🔧 Appendix: Data Ingestion Commands

```bash
# Process Excel file for seat N17
cd tools/prn-logic-engine
python3 scripts/extract-seat-data-from-excel.py

# Generate war room brief
npm run dev -- calculate --seat N17 --format markdown

# Test scenario calculations
npm run dev -- calculate --seat N17 --scenario S6

# List all available seats
npm run dev -- list-seats

# Commit and push
git add src/data/n17-semerah.ts output/n17-*
git commit -m "Update N17 Semerah — war room brief v2"
git push origin main
```

---

**Template Version:** 1.0 (2026-06-28)  
**Maintained by:** Loop Engineering Political Monitoring Unit  
**Contact:** PKR Johor War Room Data Team
