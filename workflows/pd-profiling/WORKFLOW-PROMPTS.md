# DUN Profiling Workflow - Three-Dimensional Analysis

**Purpose:** Complete constituency intelligence package for Johor PRN 2026 war room operations. This three-dimensional methodology transforms raw electoral data into actionable operational guidance.

**Workflow Type:** Three-dimensional analysis + synthesis (one-time per constituency)  
**Output:** Four brief documents (3 dimensions + 1 master synthesis)

---

## 📋 Workflow Overview

```
                    ┌─────────────────────────────────────┐
                    │  Input Data Sources                 │
                    │  - SPR Electoral Roll (XLSX)        │
                    │  - News sources + nominations       │
                    │  - ElectionData.MY + SPR historical │
                    └─────────────────────────────────────┘
                                    │
        ┌───────────────────────────┼───────────────────────────┐
        │                           │                           │
        ▼                           ▼                           ▼
┌───────────────────┐   ┌───────────────────┐   ┌───────────────────┐
│ Step 1:           │   │ Step 2:           │   │ Step 3:           │
│ Demographics      │   │ Candidates        │   │ Historical        │
│                   │   │                   │   │                   │
│ PD-level voter    │   │ Candidate profiles│   │ Voting patterns   │
│ composition       │   │ + demographic     │   │ + swing analysis  │
│                   │   │   alignment       │   │                   │
└───────────────────┘   └───────────────────┘   └───────────────────┘
        │                           │                           │
        └───────────────────────────┼───────────────────────────┘
                                    │
                                    ▼
                    ┌─────────────────────────────────────┐
                    │  Synthesis: Master Operational      │
                    │  Brief                              │
                    │                                     │
                    │  Integrated guidance from all 3     │
                    │  dimensions                         │
                    └─────────────────────────────────────┘
                                    │
                                    ▼
                    DELIVERY (memory/ + Telegram + GitHub)
```

---

## Step 1: Demographic Data Analysis

**Purpose:** Process raw SPR demographic data and generate structured analytical reports optimized for political intelligence operational applied use case.

**Input:** SPR demographic data (CSV/Excel format)  
**Output:** Structured demographic analysis with PD-level breakdown

### 📝 Prompt

```
You are a political data analyst specializing in electoral demographics and constituency profiling.

**Task:** Review the attached demographic data and generate a detailed and structured analytical report optimized for political intelligence operational applied use case.

**Instructions:**

1. **Data Validation:**
   - Verify data completeness (all PDs present, no missing fields)
   - Check voter totals match SPR official count
   - Validate ethnicity percentages sum to 100%
   - Flag any anomalies or inconsistencies

2. **Constituency-Level Analysis:**
   - Calculate total registered voters
   - Compute ethnicity breakdown (Malay, Chinese, Indian, Others)
   - Calculate gender split (Male/Female percentages)
   - Estimate youth vote (18-29 age group, if data available)
   - Identify dominant ethnic group per constituency

3. **Polling District-Level Breakdown:**
   For each PD, extract/calculate:
   - PD name and code
   - Total registered voters
   - Ethnicity composition (Malay%, Chinese%, Indian%, Others%)
   - Gender split (Male%, Female%)
   - Geographic location (village/town name)
   - PD type (urban, semi-urban, rural, kampung, mixed)

4. **Strategic Classification:**
   Classify each PD into tiers:
   - **Tier 1 (Stronghold):** >60% expected support for PH
   - **Tier 2 (Competitive):** 40-60% expected support (battleground)
   - **Tier 3 (Opposition):** <40% expected support

   Classification criteria:
   - Ethnic composition (Chinese/mixed PDs → Tier 1 for PH)
   - Historical voting patterns (if 2018/2022 data available)
   - Urban/rural divide (urban → Tier 1, rural kampung → Tier 3)
   - Socioeconomic factors (working class → Tier 2/3, middle class → Tier 1/2)

5. **Vote Modelling:**
   For each tier, project:
   - Target turnout percentage
   - Target vote share for PH
   - Expected vote count (voters × turnout × support%)
   - Compare against 2022 baseline

6. **Key Issues Identification:**
   Based on PD characteristics, identify likely voter concerns:
   - Rural/kampung: Cost of living, infrastructure, agriculture/fisheries
   - Urban: Housing, traffic, public services, jobs
   - Mixed: Community facilities, flood mitigation, local services

**Output Format:**

```markdown
# [Constituency Name] - Demographic Analysis

## Constituency Overview
- **Total Voters:** XX,XXX
- **Total PDs:** XX
- **Ethnicity:** Malay XX%, Chinese XX%, Indian XX%, Others XX%
- **Gender:** Female XX%, Male XX%
- **Youth (18-29):** XX% (est.)

## Polling District Breakdown

| PD Name | Code | Voters | Malay% | Chinese% | Tier | Location |
|---------|------|--------|--------|----------|------|----------|
| PD 1 | XXX | X,XXX | XX% | XX% | Tier 1 | Town name |
...

## Tier Classification Summary

| Tier | PD Count | Total Voters | % of Electorate | Strategy |
|------|----------|--------------|-----------------|----------|
| Tier 1 | X | X,XXX | XX% | Maximize turnout |
| Tier 2 | X | X,XXX | XX% | Persuade swing voters |
| Tier 3 | X | X,XXX | XX% | Damage limitation |

## Vote Projection (Target Scenario)

| Tier | Voters | Target Turnout | PH Support% | PH Votes |
|------|--------|----------------|-------------|----------|
| Tier 1 | X,XXX | 80% | 75% | X,XXX |
| Tier 2 | X,XXX | 70% | 45% | X,XXX |
| Tier 3 | X,XXX | 60% | 25% | X,XXX |
| **TOTAL** | **XX,XXX** | **XX%** | **XX%** | **XX,XXX** |

## Key Demographic Insights
- [Insight 1: e.g., "Chinese vote concentrated in 3 urban PDs"]
- [Insight 2: e.g., "Malay majority in 15/19 PDs"]
- [Insight 3: e.g., "Youth vote 28%, highest in X PD"]

## Data Quality Notes
- Source: SPR Electoral Roll (date)
- Confidence: [HIGH/MEDIUM/LOW]
- Gaps: [Any missing data or estimates]
```

**Analytical Approach:**
- Be systematic: process all PDs through same framework
- Be precise: show calculations explicitly
- Be strategic: focus on operational implications
- Be honest: flag uncertainties and estimates
- Be actionable: highlight what matters for campaign planning

**Confidence Tags:**
- [HIGH]: Data from official SPR source
- [MEDIUM]: Derived from multiple sources, reasonable inference
- [LOW]: Estimate or projection, requires validation

Begin analysis of the attached demographic data.
```

---

## Step 2: PD Operational Brief Generation

**Purpose:** Generate structured operational briefs for each Polling District, providing campaign teams with actionable intelligence for ground operations.

**Input:** Demographic analysis from Step 1  
**Output:** Individual PD briefs with tier strategy, targets, and issues

### 📝 Prompt

```
You are a campaign operations strategist specializing in polling district-level tactical planning.

**Task:** Review the attached demographic analysis and generate detailed and structured operational briefs for each Polling District (PD), optimized for political intelligence operational applied use case.

**Instructions:**

For EACH Polling District, create a one-page operational brief containing:

1. **PD Profile:**
   - PD name and code
   - Total registered voters
   - Ethnicity breakdown (Malay%, Chinese%, Indian%, Others%)
   - Gender split
   - Geographic description (village/town, landmarks)
   - PD type (urban/rural/kampung/mixed)

2. **Tier Classification:**
   - Assigned tier (Tier 1/2/3)
   - Justification for tier assignment
   - Strategic priority (High/Medium/Low)

3. **Vote Targets:**
   - Target turnout (%)
   - Target PH vote share (%)
   - Target vote count (absolute number)
   - 2022 baseline (if available)
   - Required swing from 2022

4. **Key Issues:**
   - Top 3 voter concerns for this PD
   - Specific local issues (flood, infrastructure, jobs, etc.)
   - Community-specific priorities (ethnic group concerns)

5. **Campaign Tactics:**
   - Recommended approach (door-to-door, ceramah, digital, community events)
   - Key messaging angles (based on demographics and issues)
   - Resource allocation priority (high/medium/low)
   - Volunteer requirements (how many needed)

6. **Risk Assessment:**
   - Main threat (BN machinery, PN religious appeal, voter apathy)
   - Vulnerability level (high/medium/low)
   - Mitigation strategies

7. **GOTV Priorities:**
   - Critical voter segments to mobilize
   - Transportation requirements (need buses/vans?)
   - Early voting strategy (if applicable)
   - Election day deployment plan

**Output Format (One Brief Per PD):**

```markdown
# PD [Name] - Operational Brief

**PD Code:** [XXX]  
**Constituency:** [N.XX Name]  
**Tier:** [Tier 1/2/3]  
**Strategic Priority:** [High/Medium/Low]  

---

## 📊 Demographics

| Metric | Value |
|--------|-------|
| Total Voters | X,XXX |
| Malay | XX% |
| Chinese | XX% |
| Indian | XX% |
| Others | XX% |
| Female | XX% |
| Male | XX% |

**Location:** [Village/town name, landmarks]  
**PD Type:** [Urban/Rural/Kampung/Mixed]  

---

## 🎯 Vote Targets

| Metric | Target | 2022 Actual | Required Swing |
|--------|--------|-------------|----------------|
| Turnout | XX% | XX% | +XX% |
| PH Support | XX% | XX% | +XX% |
| PH Votes | X,XXX | X,XXX | +XXX |

**Win Scenario:** PH needs [X,XXX] votes from this PD to [secure/maintain/challenge]

---

## 🔍 Key Issues

1. **[Issue 1]:** [Description and voter impact]
2. **[Issue 2]:** [Description and voter impact]
3. **[Issue 3]:** [Description and voter impact]

**Community Concerns:**
- **Malay voters:** [Specific concerns]
- **Chinese voters:** [Specific concerns]
- **Youth voters:** [Specific concerns]

---

## ⚔️ Campaign Tactics

**Recommended Approach:**
- [ ] Door-to-door canvassing (priority)
- [ ] Ceramah/rallies
- [ ] Digital campaigning
- [ ] Community events
- [ ] Religious/community leader engagement

**Key Messaging:**
- **Primary:** [Main message for this PD]
- **Secondary:** [Supporting message]
- **Attack vector:** [If applicable, opponent vulnerability]

**Resource Allocation:**
- **Volunteers needed:** XX people
- **Canvassing shifts:** X shifts
- **Materials:** [Banners, leaflets, etc.]
- **Budget priority:** [High/Medium/Low]

---

## ⚠️ Risk Assessment

**Main Threat:** [BN/PN/Apathy/Other]  
**Vulnerability:** [High/Medium/Low]  

**Risk Factors:**
- [Factor 1: e.g., "Strong BN incumbent machinery"]
- [Factor 2: e.g., "PN religious appeal in rural areas"]
- [Factor 3: e.g., "Historical low turnout"]

**Mitigation Strategies:**
1. [Strategy 1]
2. [Strategy 2]
3. [Strategy 3]

---

## 🚀 GOTV Priorities

**Critical Segments:**
- [Segment 1: e.g., "Chinese women 40-60"]
- [Segment 2: e.g., "First-time voters 18-21"]
- [Segment 3: e.g., "Fishing community"]

**Transportation:**
- **Need:** [Yes/No]
- **Vehicles required:** X vans/buses
- **Pickup points:** [Locations]

**Election Day Deployment:**
- **Agents needed:** XX people
- **Shifts:** [Morning/Afternoon/Evening]
- **Commander:** [TBD/Name]

---

## 📞 Contact Points

- **Community Leaders:** [Names if known]
- **PH Volunteers:** [Count, coordinator]
- **External Support:** [NGOs, allied groups]

---

**Classification:** PH INTERNAL - WAR ROOM EYES ONLY  
**Data Source:** SPR Electoral Roll (2026-06-19)  
**Confidence:** [HIGH/MEDIUM/LOW]  
**Last Updated:** [Date]
```

**Analytical Approach:**
- Be specific: tailor each brief to the PD's unique characteristics
- Be actionable: provide clear, executable recommendations
- Be realistic: set achievable targets based on demographics
- Be strategic: align PD tactics with overall constituency strategy
- Be concise: one page per PD, decision-makers are busy

Generate operational briefs for all [X] polling districts.
```

---

## Step 3: Campaign Strategy Matrix

**Purpose:** Synthesize PD-level intelligence into a comprehensive campaign strategy matrix, resource allocation plan, and GOTV master playbook.

**Input:** PD operational briefs from Step 2  
**Output:** Constituency-wide campaign strategy, resource allocation, timeline

### 📝 Prompt

```
You are a senior campaign strategist specializing in state election operations and resource optimization.

**Task:** Review all PD operational briefs and generate a detailed and structured analytical report optimized for political intelligence operational applied use case: a comprehensive campaign strategy matrix for the entire constituency.

**Instructions:**

1. **Constituency-Wide Strategy:**
   - Synthesize PD-level data into overall constituency picture
   - Define win pathway (total votes needed,从哪里来)
   - Identify critical success factors
   - Set overall campaign narrative and themes

2. **Resource Allocation Matrix:**
   Create a prioritized resource allocation plan:
   - **Tier 1 PDs:** Maximum resource deployment (staff, volunteers, budget)
   - **Tier 2 PDs:** Balanced deployment (persuasion + GOTV)
   - **Tier 3 PDs:** Minimal deployment (damage limitation, symbolic presence)
   
   For each tier, specify:
   - Number of staff/volunteers
   - Budget allocation (%)
   - Material priorities (banners, leaflets, gifts)
   - Leadership attention (how often should candidate visit?)

3. **Timeline & Milestones:**
   Create a week-by-week campaign timeline:
   - **Week 1-2 (Foundation):** Setup war room, recruit volunteers, data preparation
   - **Week 3-4 (Soft Launch):** Quiet campaigning, community visits, issue testing
   - **Week 5-6 (Full Campaign):** Ceramah, door-to-door, media push
   - **Week 7 (Intensification):** Rallies, final push, swing voter persuasion
   - **Week 8 (GOTV):** Early voting, election day deployment

4. **GOTV Master Plan:**
   Design the Get-Out-The-Vote operation:
   - **Voter mobilization targets** by PD and demographic segment
   - **Transportation logistics** (vehicles, routes, pickup points)
   - **Election day deployment** (agents, watchers, runners)
   - **Contingency planning** (what if turnout low? what if opponent cheating?)

5. **Risk Management:**
   Identify and mitigate key risks:
   - **Strategic risks:** Wrong target PDs, misallocated resources
   - **Operational risks:** Volunteer shortage, transportation failure
   - **External risks:** Opponent dirty tricks, weather, national swing
   - **Mitigation strategies** for each risk

6. **Success Metrics:**
   Define how to measure campaign progress:
   - **Leading indicators:** Door knocks completed, ceramah attendance, social media engagement
   - **Lagging indicators:** Early voting turnout, opinion polls (if available)
   - **Election day indicators:** Turnout by PD, vote share by PD

**Output Format:**

```markdown
# [Constituency Name] - Campaign Strategy Matrix

**Operation Codename:** [OPERASI_XXX]  
**Election Date:** [Date]  
**Campaign Duration:** [X] weeks  
**War Room Status:** [Setup/Operational]  

---

## 🎯 Win Pathway

**Total Votes Needed:** XX,XXX (XX% of electorate)

**Vote Sources:**
| Tier | PDs | Voters | Target Turnout | PH Support% | PH Votes |
|------|-----|--------|----------------|-------------|----------|
| Tier 1 | X | X,XXX | 80% | 75% | X,XXX |
| Tier 2 | X | X,XXX | 70% | 45% | X,XXX |
| Tier 3 | X | X,XXX | 60% | 25% | X,XXX |
| **TOTAL** | **XX** | **XX,XXX** | **XX%** | **XX%** | **XX,XXX** |

**Margin of Safety:** ±XXX votes  
**Confidence Level:** [HIGH/MEDIUM/LOW]  

**Critical Success Factors:**
1. [Factor 1: e.g., "Chinese turnout >75% in Tier 1 PDs"]
2. [Factor 2: e.g., "Malay vote split: BN 50%, PN 30%, PH 20%"]
3. [Factor 3: e.g., "Overall turnout >70%"]

---

## 📊 Resource Allocation Matrix

### Tier 1 PDs (High Priority)
- **PD Count:** X PDs ([Names])
- **Voter Share:** XX% of electorate
- **Staff:** X full-time organizers
- **Volunteers:** XX people (XX% of total)
- **Budget:** XX% of total budget
- **Candidate Visits:** X times per week
- **Priority Activities:** Door-to-door (100% coverage), ceramah, community events

### Tier 2 PDs (Medium Priority)
- **PD Count:** X PDs ([Names])
- **Voter Share:** XX% of electorate
- **Staff:** X full-time organizers
- **Volunteers:** XX people (XX% of total)
- **Budget:** XX% of total budget
- **Candidate Visits:** X times per week
- **Priority Activities:** Targeted door-to-door, small ceramah, digital campaign

### Tier 3 PDs (Low Priority)
- **PD Count:** X PDs ([Names])
- **Voter Share:** XX% of electorate
- **Staff:** X part-time organizer
- **Volunteers:** XX people (XX% of total)
- **Budget:** XX% of total budget
- **Candidate Visits:** X time total
- **Priority Activities:** Symbolic presence, damage limitation, social media only

### Budget Breakdown
| Category | Allocation (RM) | % of Total |
|----------|-----------------|------------|
| Staff salaries | X,XXX | XX% |
| Volunteers (food, transport) | X,XXX | XX% |
| Materials (banners, leaflets) | X,XXX | XX% |
| Ceramah/events | X,XXX | XX% |
| Digital advertising | X,XXX | XX% |
| GOTV (transportation) | X,XXX | XX% |
| Contingency | X,XXX | XX% |
| **TOTAL** | **XX,XXX** | **100%** |

---

## 📅 Campaign Timeline

### Week 1-2: Foundation Phase
**Objectives:**
- [ ] War room setup (location, equipment, communications)
- [ ] Volunteer recruitment (target: XX people)
- [ ] Data preparation (PD maps, voter lists, contact info)
- [ ] Community leader outreach (identify influencers)

**Milestones:**
- [ ] War room operational by [date]
- [ ] XX volunteers recruited by [date]
- [ ] All PD commanders appointed by [date]

### Week 3-4: Soft Launch Phase
**Objectives:**
- [ ] Quiet campaigning (community visits, no large events)
- [ ] Issue testing (which messages resonate?)
- [ ] Volunteer training (canvassing, GOTV, election law)
- [ ] Early voter registration (check registration status)

**Milestones:**
- [ ] X,XXX doors knocked by [date]
- [ ] X community events held by [date]
- [ ] Messaging framework finalized by [date]

### Week 5-6: Full Campaign Phase
**Objectives:**
- [ ] Door-to-door canvassing (target: 100% Tier 1, 50% Tier 2)
- [ ] Ceramah series (X events across constituency)
- [ ] Media push (social, traditional, influencers)
- [ ] Opponent research (identify vulnerabilities)

**Milestones:**
- [ ] XX,XXX voters contacted by [date]
- [ ] X ceramahs with X,XXX attendance by [date]
- [ ] Social media reach: X,XXX impressions by [date]

### Week 7: Intensification Phase
**Objectives:**
- [ ] Mega rallies (X events, target X,XXX attendance)
- [ ] Swing voter persuasion (focus on Tier 2 PDs)
- [ ] Final media blitz
- [ ] Early voting mobilization (if applicable)

**Milestones:**
- [ ] X% of voters contacted at least once by [date]
- [ ] X% of voters committed to vote PH by [date]
- [ ] Early voting turnout target: XX% by [date]

### Week 8: GOTV Phase
**Objectives:**
- [ ] Final voter contact (reminders, transportation arrangement)
- [ ] Election day deployment (agents, watchers, runners)
- [ ] Rapid response team (handle issues, rumors, cheating)
- [ ] Vote count monitoring (real-time tally)

**Milestones:**
- [ ] 100% polling stations covered by [date]
- [ ] XX vehicles ready for GOTV by [date]
- [ ] War room operational 24/7 from [date]

---

## 🚀 GOTV Master Plan

### Voter Mobilization Targets

| PD | Tier | Target Turnout | PH Votes Needed | Transportation |
|----|------|----------------|-----------------|----------------|
| PD 1 | Tier 1 | 85% | XXX | 2 vans |
| PD 2 | Tier 1 | 80% | XXX | 2 vans |
...
| **TOTAL** | - | **XX%** | **X,XXX** | **XX vehicles** |

### Transportation Logistics
- **Total Vehicles Needed:** XX vans/buses
- **Pickup Points:** XX locations across constituency
- **Routes:** X optimized routes (minimize time, maximize pickups)
- **Drivers:** XX volunteers (trained, licensed)
- **Fuel Budget:** RM X,XXX

### Election Day Deployment
- **Total Polling Stations:** XX
- **Agents Required:** XX (2 per station, 3 shifts)
- **Watchers Required:** XX (vote counting center)
- **Runners Required:** XX (coordinate between stations and war room)
- **Command Structure:**
  - **Overall Commander:** [Name]
  - **Tier Commanders:** X people (one per tier)
  - **PD Commanders:** XX people (one per PD)
  - **Station Chiefs:** XX people (one per polling station)

### Contingency Plans
- **Low Turnout Scenario:** Activate emergency contact tree, deploy additional transportation
- **Opponent Cheating:** Document incidents, report to SPR/Police, mobilize legal team
- **Weather Emergency:** Reschedule outdoor events, increase digital outreach
- **Rumor/Fake News:** Rapid response team debunks within 1 hour

---

## ⚠️ Risk Management

### Strategic Risks
| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Wrong target PDs | Medium | High | Weekly review of polling data, adjust strategy |
| Resource misallocation | Medium | High | Daily tracking, reallocate based on progress |
| National swing against PH | High | High | Focus on local issues, candidate accessibility |

### Operational Risks
| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Volunteer shortage | Medium | High | Early recruitment, backup pool, incentives |
| Transportation failure | Low | High | Multiple vendors, backup vehicles, maintenance checks |
| Communication breakdown | Medium | Medium | Redundant systems (WhatsApp, phone, radio) |

### External Risks
| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Opponent dirty tricks | High | Medium | Pre-bunking, rapid response, legal preparation |
| Bad weather (rain) | Medium | Medium | Indoor venues, tents, reschedule flexibility |
| Economic crisis | Low | High | Pivot messaging to economic competence |

---

## 📊 Success Metrics

### Leading Indicators (Track Weekly)
- **Door Knocks:** Target X,XXX/week | Actual: ___
- **Ceramah Attendance:** Target X,XXX/week | Actual: ___
- **Social Media Engagement:** Target X,XXX impressions/week | Actual: ___
- **Volunteer Hours:** Target XXX hours/week | Actual: ___
- **Voter Commitments:** Target X,XXX committed/week | Actual: ___

### Lagging Indicators (Track Bi-Weekly)
- **Early Voting Turnout:** Target XX% | Actual: ___
- **Opinion Poll (if available):** Target XX% PH support | Actual: ___
- **Community Leader Endorsements:** Target X leaders | Actual: ___

### Election Day Indicators (Track Hourly)
- **Turnout by PD:** Target XX% | Actual: ___
- **PH Vote Share by PD:** Target XX% | Actual: ___
- **Total PH Votes:** Target X,XXX | Actual: ___

---

## 📞 Command Structure

**War Room Director:** [Name] - Overall command, decision-making  
**Operations Chief:** [Name] - Day-to-day operations, volunteer coordination  
**Data Team Lead:** [Name] - Voter data, progress tracking, analytics  
**Communications Lead:** [Name] - Media, social media, messaging  
**GOTV Commander:** [Name] - Election day deployment, transportation  
**Legal Team Lead:** [Name] - Compliance, dispute resolution  

**Meeting Schedule:**
- **Daily:** 8:00 PM - War room standup (all commanders)
- **Weekly:** Sunday 10:00 AM - Strategy review (director + chiefs)
- **Emergency:** As needed (director convenes)

---

**Classification:** PH INTERNAL - WAR ROOM EYES ONLY  
**Version:** 1.0  
**Last Updated:** [Date]  
**Next Review:** [Date + 1 week]
```

**Analytical Approach:**
- Be strategic: align resources with win pathway
- Be realistic: set achievable targets based on data
- Be specific: name names, assign responsibilities
- Be flexible: build in contingency plans
- Be actionable: every recommendation should be executable

Generate the complete campaign strategy matrix.
```

---

## 📊 Workflow Outputs

### Step 1 Output:
- `demographic-analysis.md` - Constituency-wide demographic breakdown
- `pd-breakdown.csv` - Structured PD-level data

### Step 2 Output:
- `pd-briefs/PD-01-XXX.md` through `PD-XX-XXX.md` - Individual PD operational briefs
- `pd-briefs/README.md` - Index of all PD briefs

### Step 3 Output:
- `campaign-strategy-matrix.md` - Constituency-wide strategy
- `resource-allocation.md` - Budget and staffing plan
- `gotv-master-plan.md` - GOTV operational details
- `timeline-milestones.md` - Week-by-week campaign calendar

---

## 🔧 Configuration

Each step can be configured via command-line flags:

```bash
# Step 1: Demographic Analysis
openclaw skill run pd-demographic-analyzer \
  --input "data/spr-demographic-data.csv" \
  --output "demographic-analysis.md" \
  --constituency "N.16 Sungai Balang"

# Step 2: PD Operational Briefs
openclaw skill run pd-operational-briefs \
  --input "demographic-analysis.md" \
  --output-dir "pd-briefs/" \
  --tier-thresholds "tier1=60,tier2=40"

# Step 3: Campaign Strategy Matrix
openclaw skill run campaign-strategy-matrix \
  --input "pd-briefs/" \
  --output "campaign-strategy-matrix.md" \
  --budget "50000" \
  --volunteers "100"
```

---

## 📚 Related Documentation

- [N16 Sungai Balang Example](/home/p62operator/.openclaw/workspace/n16-sungai-balang-repo/)
- [N17 Semerah Example](/home/p62operator/.openclaw/workspace/n17-semerah-repo/)
- [Candidate Profiling Workflow Review](docs/candidate-profiling-workflow-review.md)

---

**Document Version:** 1.0  
**Last Updated:** 2026-07-01  
**Maintainer:** Political Intelligence Team
