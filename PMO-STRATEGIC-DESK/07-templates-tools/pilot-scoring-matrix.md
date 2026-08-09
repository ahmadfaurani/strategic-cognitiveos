# Pilot Use Case Scoring Matrix — Operational Guide

**Purpose:** Evaluate and prioritise potential AI pilot use cases for the Perdana Digital AI Cohort  
**Session:** Working Session with Bahagian Data Strategik  
**Target:** Select 2–3 priority pilots for short-cycle experimentation (2–4 week sprints)  
**Facilitator:** DAF  
**Time Allocation:** 45–60 minutes during session

---

## 🎯 Scoring Session Workflow

### Pre-Session Preparation (DAF)

**When:** 2–3 days before working session  
**Time:** 30 minutes

**Steps:**
1. [ ] Review completed Data Lake Readiness Assessment
2. [ ] Extract top 3–5 use cases from Section 3.1
3. [ ] Pre-populate scoring matrix with candidate use cases
4. [ ] Prepare model recommendations for each use case
5. [ ] Print copies for all attendees (or share digital copy)
6. [ ] Set up whiteboard/flipchart for live scoring

---

### During Session (Facilitated Scoring)

**When:** During working session (after demos)  
**Time:** 45–60 minutes  
**Participants:** All attendees (Bahagian Data Strategik + Aras Integrasi)

**Agenda:**

| Time | Activity | Facilitator | Output |
|------|----------|-------------|--------|
| 0–5 min | Explain scoring criteria & process | DAF | Shared understanding |
| 5–10 min | Review candidate use cases (3–5) | DAF | Prioritised list |
| 10–30 min | Score each use case (collaborative) | Joint | Completed scoring tables |
| 30–40 min | Calculate weighted scores | DAF | Ranked list |
| 40–50 min | Discuss top 2–3 pilots | Joint | Consensus on selection |
| 50–60 min | Define next steps for each pilot | Joint | Action items with owners |

---

## 📊 Scoring Criteria — Detailed Definitions

### 1. Strategic Impact (Weight: 30%)

**Definition:** How well does this use case align with Bahagian Data Strategik's mandate and PMO leadership priorities?

| Score | Criteria | Guiding Questions | Evidence Needed |
|-------|----------|-------------------|-----------------|
| **5** | Directly supports PMO strategic objectives; high leadership visibility | - Does this solve a pain point for PMO leadership?<br>- Will success be visible at Director-General level?<br>- Does this advance the Data Lake strategic objective? | - Reference to PMO strategic plan<br>- Leadership endorsement<br>- Clear link to Data Lake initiative |
| **4** | Supports key operational priorities; moderate visibility | - Does this improve Bahagian Data Strategik's core functions?<br>- Will division heads notice the impact?<br>- Does this reduce manual effort significantly? | - Operational mandate alignment<br>- Process improvement metrics |
| **3** | Useful but not critical; internal efficiency focus | - Does this help analysts work faster?<br>- Is this a "nice to have" or "must have"?<br>- Will this be used regularly? | - User feedback<br>- Usage frequency estimate |
| **2** | Nice-to-have; limited strategic value | - Is this experimental or exploratory?<br>- Will only a few people benefit?<br>- Is there a simpler non-AI solution? | - Cost-benefit analysis<br>- Alternative solutions |
| **1** | Low relevance to PMO mandate | - Does this distract from core priorities?<br>- Is this a solution looking for a problem?<br>- Will this be abandoned after pilot? | - Risk assessment<br>- Opportunity cost analysis |

**Scoring Method:**
1. Read guiding questions aloud
2. Ask Bahagian Data Strategik team: "On a scale of 1–5, where does this land?"
3. Discuss any score disagreements (aim for consensus)
4. Record final score + brief justification

---

### 2. Data Readiness (Weight: 25%)

**Definition:** How readily available and usable is the data needed for this use case?

| Score | Criteria | Data Characteristics | Effort Required |
|-------|----------|---------------------|-----------------|
| **5** | Data available, structured, clean, accessible | - Already in digital format (CSV, JSON, database)<br>- Clean, minimal missing values<br>- Access permissions confirmed<br>- <1 day to prepare | None — ready to use |
| **4** | Data available, minor cleanup needed | - Digital format but needs transformation<br>- Some missing values or inconsistencies<br>- Access permissions likely<br>- 1–3 days to prepare | Light data wrangling |
| **3** | Data exists but requires significant preparation | - Mix of digital and paper/PDF<br>- Significant cleanup required<br>- Access permissions unclear<br>- 1–2 weeks to prepare | Medium data engineering |
| **2** | Data partially available; gaps need filling | - Key datasets missing<br>- Major format conversion needed<br>- Access restrictions likely<br>- 2–4 weeks to prepare | Heavy data engineering |
| **1** | Data not available; would need new collection | - Data doesn't exist yet<br>- Would need to create new collection process<br>- Major access/compliance barriers<br>- 1–3 months to prepare | New data pipeline required |

**Scoring Method:**
1. Ask: "What data is needed for this use case?"
2. Ask: "Do you already have this data? In what format?"
3. Ask: "How long would it take to make this data ready?"
4. Score based on effort table above

---

### 3. Effort & Complexity (Weight: 20%)

**Definition:** How much development effort is required to build and deploy this pilot?

| Score | Criteria | Development Effort | Integration Complexity | Timeline |
|-------|----------|-------------------|------------------------|----------|
| **5** | Low effort; can be built in <2 weeks | - Single API call or simple workflow<br>- No external integrations<br>- Minimal testing required | None | 1–2 weeks |
| **4** | Moderate effort; 2–4 weeks | - Multiple API calls or workflow steps<br>- One external system integration<br>- Standard testing | Low | 2–4 weeks |
| **3** | Medium complexity; 4–8 weeks | - Complex workflow with branching logic<br>- Multiple integrations<br>- Extensive testing + UAT | Medium | 4–8 weeks |
| **2** | High complexity; 8–12 weeks | - Multi-system orchestration<br>- Custom model fine-tuning<br>- Security/compliance review | High | 8–12 weeks |
| **1** | Very complex; 3+ months, major integration | - Enterprise-scale integration<br>- New infrastructure required<br>- Multiple stakeholder approvals | Very High | 3+ months |

**Scoring Method:**
1. Ask Farul (CTO) for technical effort estimate
2. Ask Bahagian Data Strategik: "What systems need to be integrated?"
3. Consider: API calls, data pipelines, UI development, testing, approvals
4. Score based on timeline and complexity

---

### 4. Governance Risk (Weight: 15%)

**Definition:** What are the security, compliance, and reputational risks associated with this use case?

| Score | Criteria | Data Sensitivity | Compliance Requirements | Reputational Risk |
|-------|----------|-----------------|------------------------|-------------------|
| **5** | Low risk; public or internal data only | - Public data or internal-only<br>- No PII or classified content | None beyond standard policies | Low — internal use only |
| **4** | Minimal risk; standard controls sufficient | - Internal data with some sensitivity<br>- No PII or classified content | Standard access control + logging | Low — limited audience |
| **3** | Moderate risk; requires additional safeguards | - Some PII or confidential data<br>- Requires PDPA compliance | PDPA review + access control | Medium — if leaked |
| **2** | Higher risk; sensitive data, complex approvals | - Confidential or restricted data<br>- Official Secrets Act implications | Legal review + security audit | High — compliance breach |
| **1** | High risk; classified or highly sensitive data | - Classified/Secret data<br>- Cross-border transfer<br>- High-profile use case | MAMPU review + multiple approvals | Very High — national impact |

**Scoring Method:**
1. Ask: "What is the sensitivity level of the data involved?"
2. Ask: "Are there PDPA, Official Secrets Act, or MAMPU implications?"
3. Ask: "What happens if this goes wrong?"
4. Consult governance checklist (`06-governance-security/ai-governance-checklist.md`)
5. Score conservatively (err on the side of caution)

---

### 5. Scalability & Reusability (Weight: 10%)

**Definition:** Can this pilot be scaled or reused across other teams or use cases?

| Score | Criteria | Scalability | Reusability | Strategic Value |
|-------|----------|-------------|-------------|-----------------|
| **5** | Highly scalable; reusable across multiple units | - Can be deployed PMO-wide<br>- Applicable to 5+ use cases<br>- Builds foundational capability | Very High — platform capability |
| **4** | Scalable within Bahagian Data Strategik | - Can be used by all analysts<br>- Applicable to 3–5 use cases<br>- Reusable components | High — division-wide tool |
| **3** | Limited scalability; specific to one use case | - Only useful for this specific scenario<br>- Some components reusable<br>- Moderate effort to adapt | Medium — point solution with potential |
| **2** | One-off solution; minimal reusability | - Only useful for this one task<br>- No reusable components<br>- Hard to adapt | Low — standalone |
| **1** | Point solution; no scalability | - Highly customised<br>- No reuse potential<br>- Would need rebuild for other uses | None — experimental only |

**Scoring Method:**
1. Ask: "Could this be used by other teams in PMO?"
2. Ask: "Are we building a one-off or a platform capability?"
3. Ask: "What other use cases could this enable?"
4. Score based on long-term strategic value

---

## 📝 Scoring Worksheet

### Candidate Use Case #1: [Name from Assessment]

**Description:** [2–3 sentences from assessment Section 3.2]

**Data Sources Required:** [List from assessment]

**Expected Users:** [Leadership / Analysts / All Staff / External Partners]

| Criterion | Weight | Score (1–5) | Weighted Score | Justification |
|-----------|--------|-------------|----------------|---------------|
| Strategic Impact | 30% | [ ] | × 0.30 = | |
| Data Readiness | 25% | [ ] | × 0.25 = | |
| Effort & Complexity | 20% | [ ] | × 0.20 = | |
| Governance Risk | 15% | [ ] | × 0.15 = | |
| Scalability & Reusability | 10% | [ ] | × 0.10 = | |
| **TOTAL** | **100%** | | **___ / 5.0** | |

**Weighted Score Calculation:**
```
(Impact × 0.30) + (Data × 0.25) + (Effort × 0.20) + (Risk × 0.15) + (Scale × 0.10) = Total
```

**Example:**
```
(4 × 0.30) + (5 × 0.25) + (3 × 0.20) + (4 × 0.15) + (3 × 0.10) = 3.95
```

**Recommendation:**
- ☐ **Priority 1** (Score ≥ 4.0) — Fast-track for pilot
- ☐ **Priority 2** (Score 3.0–3.9) — Strong candidate
- ☐ **Priority 3** (Score 2.0–2.9) — Consider if capacity allows
- ☐ **Defer** (Score < 2.0) — Not suitable for current phase

**Consensus Check:**
- [ ] All participants agree with score
- [ ] Disagreements discussed and resolved
- [ ] Bahagian Data Strategik lead has final say on ties

---

### Candidate Use Case #2: [Name from Assessment]

**Description:** [2–3 sentences from assessment Section 3.2]

**Data Sources Required:** [List from assessment]

**Expected Users:** [Leadership / Analysts / All Staff / External Partners]

| Criterion | Weight | Score (1–5) | Weighted Score | Justification |
|-----------|--------|-------------|----------------|---------------|
| Strategic Impact | 30% | [ ] | × 0.30 = | |
| Data Readiness | 25% | [ ] | × 0.25 = | |
| Effort & Complexity | 20% | [ ] | × 0.20 = | |
| Governance Risk | 15% | [ ] | × 0.15 = | |
| Scalability & Reusability | 10% | [ ] | × 0.10 = | |
| **TOTAL** | **100%** | | **___ / 5.0** | |

**Weighted Score Calculation:**
```
(Impact × 0.30) + (Data × 0.25) + (Effort × 0.20) + (Risk × 0.15) + (Scale × 0.10) = Total
```

**Recommendation:**
- ☐ **Priority 1** (Score ≥ 4.0) — Fast-track for pilot
- ☐ **Priority 2** (Score 3.0–3.9) — Strong candidate
- ☐ **Priority 3** (Score 2.0–2.9) — Consider if capacity allows
- ☐ **Defer** (Score < 2.0) — Not suitable for current phase

---

### Candidate Use Case #3: [Name from Assessment]

**Description:** [2–3 sentences from assessment Section 3.2]

**Data Sources Required:** [List from assessment]

**Expected Users:** [Leadership / Analysts / All Staff / External Partners]

| Criterion | Weight | Score (1–5) | Weighted Score | Justification |
|-----------|--------|-------------|----------------|---------------|
| Strategic Impact | 30% | [ ] | × 0.30 = | |
| Data Readiness | 25% | [ ] | × 0.25 = | |
| Effort & Complexity | 20% | [ ] | × 0.20 = | |
| Governance Risk | 15% | [ ] | × 0.15 = | |
| Scalability & Reusability | 10% | [ ] | × 0.10 = | |
| **TOTAL** | **100%** | | **___ / 5.0** | |

**Weighted Score Calculation:**
```
(Impact × 0.30) + (Data × 0.25) + (Effort × 0.20) + (Risk × 0.15) + (Scale × 0.10) = Total
```

**Recommendation:**
- ☐ **Priority 1** (Score ≥ 4.0) — Fast-track for pilot
- ☐ **Priority 2** (Score 3.0–3.9) — Strong candidate
- ☐ **Priority 3** (Score 2.0–2.9) — Consider if capacity allows
- ☐ **Defer** (Score < 2.0) — Not suitable for current phase

---

## 🏆 Final Selection & Next Steps

### Top 3 Pilots (Post-Scoring)

| Rank | Use Case | Score | Owner | Target Delivery | Sprint Duration |
|------|----------|-------|-------|-----------------|-----------------|
| 1 | | / 5.0 | | | weeks |
| 2 | | / 5.0 | | | weeks |
| 3 | | / 5.0 | | | weeks |

**Selection Criteria:**
- Top 2 scores automatically selected (if ≥3.0)
- Third pilot: Highest score or strategic wildcard (leadership choice)
- All pilots must have governance risk score ≥3 (no high-risk pilots in Phase 1)

---

### Next Steps for Each Pilot

#### Pilot #1: [Name]

| Action | Owner | Due Date | Status |
|--------|-------|----------|--------|
| Finalise pilot scope document | | Session + 3 days | ⏳ |
| Confirm data access | | Session + 1 week | ⏳ |
| Set up development environment | | Session + 1 week | ⏳ |
| Define success metrics | | Session + 1 week | ⏳ |
| Kickoff sprint | | Session + 2 weeks | ⏳ |

---

#### Pilot #2: [Name]

| Action | Owner | Due Date | Status |
|--------|-------|----------|--------|
| Finalise pilot scope document | | Session + 3 days | ⏳ |
| Confirm data access | | Session + 1 week | ⏳ |
| Set up development environment | | Session + 1 week | ⏳ |
| Define success metrics | | Session + 1 week | ⏳ |
| Kickoff sprint | | Session + 2 weeks | ⏳ |

---

#### Pilot #3: [Name]

| Action | Owner | Due Date | Status |
|--------|-------|----------|--------|
| Finalise pilot scope document | | Session + 3 days | ⏳ |
| Confirm data access | | Session + 1 week | ⏳ |
| Set up development environment | | Session + 1 week | ⏳ |
| Define success metrics | | Session + 1 week | ⏳ |
| Kickoff sprint | | Session + 2 weeks | ⏳ |

---

## 📋 Decision Log

| Date | Decision | Rationale | Participants | Vote (if needed) |
|------|----------|-----------|--------------|------------------|
| | | | | |

---

## 🔗 Related Documents

| Document | Purpose | Link |
|----------|---------|------|
| Readiness Assessment | Source of use case candidates | `memory/pmo-datalake-readiness-assessment.md` |
| Pilot Tracking | Monitor selected pilots post-session | `03-ai-cohort-program/pilot-tracking.md` |
| Governance Checklist | Risk assessment reference | `06-governance-security/ai-governance-checklist.md` |
| Model Catalog | Model selection for each pilot | `03-ai-cohort-program/model-catalog.md` |

---

*Use this matrix during the working session to converge on 2–3 priority pilots. Complete scoring collaboratively with Bahagian Data Strategik team. Keep scoring transparent and documented.*

**Facilitator:** DAF  
**Template Version:** 1.0  
**Last Updated:** 2026-07-09  
**Print copies:** Yes (for all session attendees)
