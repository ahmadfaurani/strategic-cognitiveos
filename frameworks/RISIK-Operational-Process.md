# R.I.S.I.K — Operational Process: Detailed Workflows

Companion to the R.I.S.I.K Framework. Provides step-by-step operational workflows for each layer and phase.

---

## A. Intelligence Collection Workflow (Layer 1)

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  SOURCE     │───▶│  TRIAGE     │───▶│  EXTRACT    │───▶│  VERIFY     │
│  DISCOVERY  │    │  & FILTER   │    │  & STRUCTURE│    │  & SCORE    │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
                                            │                   │
                                            ▼                   ▼
                                    ┌─────────────┐    ┌─────────────┐
                                    │  STORE &    │◀───│  CONFIDENCE │
                                    │  REGISTER   │    │  ASSESSMENT │
                                    └─────────────┘    └─────────────┘
```

### Step 1 — Source Discovery
- Identify and configure all collection sources: news APIs, social media platforms, field reporter networks, OSINT tools, survey instruments
- **Source diversity requirement:** minimum 5 independent source types
- **Coverage check:** ensure sources span official, media, community, and digital spaces
- **Output:** configured source inventory

### Step 2 — Triage and Filter
- **Automated:** relevance filtering (keyword/PIR matching), deduplication, language detection
- **Human:** source credibility assessment (A–F grading), relevance judgement
- **A–F Source Grading:**
  - A: Established official/institutional source with verified track record
  - B: Reputable media outlet with editorial standards
  - C: Community source with partial verification
  - D: Unverified digital source, anonymous account
  - E: Single-source claim, no corroboration
  - F: Known disinformation source or compromised account
- **Output:** triaged feed with source grade, timestamp, relevance score

### Step 3 — Extract and Structure
- **Fact extraction:** isolate claims (who, what, when, where, how many) from narrative framing
- **Entity extraction:** actors, organisations, locations, dates, numbers
- **Relationship extraction:** who said what about whom, who amplified whom
- **Output:** structured data records

### Step 4 — Verify and Score
- Cross-reference each extracted fact against ≥2 independent sources
- **Confidence scoring:**
  - CONFIRMED — ≥2 sources, at least one Grade A or B
  - PROBABLE — 2 sources, medium reliability (Grade B–C)
  - POSSIBLE — 1 source, or 2 low-reliability sources
  - UNVERIFIED — single weak source (Grade D–F)
- Flag contradictions: where sources disagree, record both, mark CONFLICTING
- **Output:** verified fact set with confidence tags

### Step 5 — Store and Register
- Store in signal registry: timestamp, source, confidence, extraction method, analyst ID
- Version control: every update creates a new version; nothing is overwritten
- Access control: sensitivity-tagged; need-to-know basis
- **Output:** queryable intelligence database

---

## B. Analysis and Assessment Workflow (Layers 1 → 2)

```
┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐
│ REALITY  │──▶│  ISSUE   │──▶│SENTIMENT │──▶│INFLUENCE │──▶│ ASSESS   │
│  BRIEF   │   │  REGISTER│   │   MAP    │   │   MAP    │   │ BRIEF    │
│  (SIB)   │   │  (IPM)   │   │  (SEM)   │   │  (INM)   │   │ (IAB)    │
└──────────┘   └──────────┘   └──────────┘   └──────────┘   └──────────┘
```

Each phase produces a named deliverable that feeds the next:

| Transition | What Flows | What Next Phase Does With It |
|-----------|-----------|------------------------------|
| Reality → Issue | SIB (verified facts, actors, gaps) | Extract and score issues from verified facts |
| Issue → Sentiment | IPM (priority issues, triggers) | Define which audience segments to analyse for priority issues |
| Sentiment → Influence | SEM (emotion map, vulnerable segments) | Map who is driving the emotions in those segments |
| Influence → Assessment | INM (network map, trusted messengers) | Synthesise all prior into integrated assessment |

### Integrated Assessment Brief (IAB)

The IAB is the synthesis product that goes to decision-makers. It contains:

1. **Executive Summary** — 1-page overview: situation, priority issues, sentiment state, key influencers, recommended actions
2. **Reality Section** — SIB summary with confidence assessment
3. **Issue Section** — Top 5 issues with scores, lifecycle stage, triggers
4. **Sentiment Section** — Top segments with emotion profile, risk level, threshold status
5. **Influence Section** — Top influencers with reach, resonance, narrative alignment, trusted-messenger candidates
6. **Threat Assessment** — What hostile narratives are active or emerging, what is their trajectory
7. **Recommended Actions** — Intervention options with proportionality assessment
8. **Decision Requirements** — What decisions need to be made, by whom, by when

---

## C. Decision and Authorisation Workflow (Layer 2)

```
┌──────────────┐    ┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│  ASSESSMENT  │───▶│  RESPONSE    │───▶│  LEGAL &     │───▶│  COMMAND     │
│  BRIEF       │    │  DESIGN      │    │  ETHICAL     │    │  AUTHORISATION│
│  REVIEW      │    │              │    │  REVIEW      │    │              │
└──────────────┘    └──────────────┘    └──────────────┘    └──────────────┘
                          │                                        │
                          ▼                                        ▼
                  ┌──────────────┐                        ┌──────────────┐
                  │  CONTENT     │                        │  APPROVED /  │
                  │  DRAFT      │                        │  DENIED /    │
                  └──────────────┘                        │  DEFERRED    │
                                                          └──────────────┘
```

### Step 1 — Assessment Brief Review
- Present IAB to decision authority
- Decision authority reviews: Is the situation accurately captured? Are priorities correct? Is the threat assessment proportionate?
- **Output:** review notes, priority confirmation, scoping direction

### Step 2 — Response Design
- Select intervention type from Intervention Selection Matrix
- Draft response using 10-point Counter-Narrative Content Requirements
- Specify: target segment, channel, messenger, timing, duration
- **Output:** response design document

### Step 3 — Legal and Ethical Review
- **Compliance check:** applicable laws, institutional policies, platform terms of service
- **Proportionality check:** is the response proportionate to the threat?
- **Deception exclusion:** verify no fabrication, impersonation, or unlawful manipulation
- **Human rights check:** respect for freedom of expression and access to information
- **Output:** sign-off or rejection with documented reasons

### Step 4 — Command Authorisation
- Present to designated authority (pre-defined by governance framework)
- Authority reviews: strategic alignment, risk assessment, resource availability
- Decision: APPROVED / DENIED / DEFERRED (with conditions)
- **Output:** authorisation record with signature, timestamp, and conditions

### Authorisation Levels

| Level | Threat Severity | Required Authority | Timeline | Documentation |
|-------|----------------|-------------------|----------|---------------|
| Routine | Low | Operations Manager | Same day | Standard form |
| Elevated | Medium | Department Head | Within 4 hours | Expanded form + rationale |
| Crisis | High | Executive/Director | Within 1 hour | Crisis protocol + risk assessment |
| Critical | Severe | Director + Legal Counsel | Immediate | Emergency protocol + full documentation |

### Decision Authority Delegation Chain

```
Director ──────────── Crisis + Critical
    │
    ├─ Department Head ── Elevated
    │      │
    │      └─ Operations Manager ── Routine
    │
    └─ Legal Counsel ──── Advisory (all levels above Routine)
```

**Rule:** No intervention deploys without sign-off at the appropriate level. Escalation always goes upward, never sideways.

---

## D. Engagement and Execution Workflow (Layer 3)

```
┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐
│ CONTENT  │──▶│ MESSENGER│──▶│ CHANNEL  │──▶│ DEPLOY   │──▶│ MONITOR  │
│ PREP     │   │ BRIEFING │   │ ACTIVATION│   │          │   │ & MEASURE│
└──────────┘   └──────────┘   └──────────┘   └──────────┘   └──────────┘
```

### Step 1 — Content Preparation
- Finalise content in all required formats (text, video, image, audio, briefing doc)
- Format-matched to channel: TikTok ≠ press statement ≠ WhatsApp message ≠ community briefing
- Quality control: factual accuracy check, tone review, cultural sensitivity review
- **Output:** approved content package (all formats)

### Step 2 — Messenger Briefing
- Brief selected messengers on: the situation, the objective, the content, the boundaries
- Messenger understands: what to say, what not to say, what to do if challenged
- Provide messengers with: key facts sheet, FAQ, escalation contact
- **Output:** briefed and equipped messengers

### Step 3 — Channel Activation
- Confirm channel availability and readiness
- Schedule deployment: sequence, timing, coordination between channels
- Prepare backup channels in case primary channels fail or are blocked
- **Output:** activation schedule with contingencies

### Step 4 — Deployment
- Execute according to schedule
- Log: what was deployed, when, where, by whom
- Monitor initial response in real-time
- **Output:** deployment log

### Step 5 — Monitor and Measure
- Track predefined KPIs from the NIP measurement framework
- Real-time monitoring: reach, engagement, sentiment shift, backlash detection
- Early-warning triggers: unexpected negative response, amplification by hostile actors, messenger credibility challenge
- **Output:** real-time measurement dashboard, incident alerts

---

## E. Measurement and Adaptation Workflow

```
┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐
│ BASELINE │──▶│ MEASURE  │──▶│ COMPARE  │──▶│ ADAPT    │
│ SET      │   │ (KPIs)   │   │ (vs      │   │ (loop    │
│          │   │          │   │  target) │   │  back)   │
└──────────┘   └──────────┘   └──────────┘   └──────────┘
```

### Measurement Framework

| Measurement Type | What We Track | Method | Timing |
|-----------------|--------------|--------|--------|
| Reach | How many saw the intervention | Impressions, views, circulation | Real-time + 24h |
| Engagement | How many interacted | Shares, comments, saves, replies | Real-time + 48h |
| Sentiment shift | Did sentiment change in target segment | Pre/post sentiment survey | Pre + 3 days + 7 days |
| Narrative penetration | Did counter-narrative enter discourse | Keyword tracking, frame detection in public posts | 24h + 7 days |
| Behavioural change | Did audience behaviour change | Observable action (turnout, participation, compliance) | Per behavioural cycle |
| Messenger effectiveness | Did messenger resonate | Audience feedback, engagement rate on messenger content | Post-deployment |
| Backlash detection | Did intervention cause negative reaction | Sentiment monitoring for adverse response | Real-time + 48h |
| Amplification risk | Did we accidentally amplify hostile narrative | Hostile narrative volume pre/post intervention | Real-time + 24h |

### Adaptation Triggers

| Trigger | Condition | Action |
|--------|-----------|--------|
| Backlash | Negative sentiment rises > 20% post-intervention | Pause deployment, assess cause, adjust content |
| Amplification | Hostile narrative volume increases > 30% post-intervention | Stop deployment, switch to strategic silence, assess |
| Messenger failure | Messenger credibility challenged or messenger goes off-message | Withdraw messenger, assess damage, consider replacement |
| Channel failure | Channel blocks, removes, or throttles content | Switch to backup channel, document interference |
| Sentiment improvement | Target sentiment shifts positive > 15% | Continue current approach, prepare to scale down |
| No effect | No measurable change after 72 hours | Reassess: wrong audience? wrong channel? wrong message? |
| Issue escalation | Underlying issue escalates beyond current intervention scope | Loop back to Reality phase, reassess full situation |

### Post-Intervention Review (Within 7 Days)

1. What was the objective?
2. What was deployed?
3. What happened? (KPI results vs targets)
4. What worked?
5. What didn't work?
6. What would we do differently?
7. What lessons feed back into the next cycle?

**Output:** Adaptation Memo — feeds into next Reality phase assessment.

---

## F. Continuous Monitoring Cycle

The R.I.S.I.K cycle is not linear. It runs continuously, with different phases operating at different tempos:

```
 CONTINUOUS          DAILY              PER CYCLE           PER INCIDENT
 ┌─────────┐    ┌──────────┐    ┌──────────────┐    ┌──────────────┐
 │ Signals │    │ SIB      │    │ Full R.I.S.I.K│    │ Kontra       │
 │ Intake  │    │ Update   │    │ Assessment    │    │ Narrative    │
 │         │    │          │    │ (R→I→S→In)   │    │ Intervention │
 └────┬────┘    └────┬─────┘    └──────┬───────┘    └──────┬───────┘
      │              │                 │                   │
      └──────────────┴─────────────────┴───────────────────┘
                        │
                        ▼
              ┌──────────────────┐
              │  MEASURE → LEARN │
              │  → ADAPT         │
              └────────┬─────────┘
                       │
                       ▼
              ┌──────────────────┐
              │  REALITY (next    │
              │  cycle)           │
              └──────────────────┘
```

### Normal Operations Rhythm

| Timeframe | Activity |
|-----------|----------|
| Continuous | Signal intake, sentiment monitoring, narrative detection |
| Morning | SIB update, issue register review, priority check |
| Midday | Sentiment trend check, influence monitoring |
| Evening | Daily summary, flag for next cycle |
| Weekly | Full R.I.S.I.K assessment, influence network update, measurement review |
| Monthly | Framework review, source audit, PIR refinement, lesson integration |

### Crisis Operations Rhythm

| Timeframe | Activity |
|-----------|----------|
| Hourly | SIB update, sentiment pulse check |
| 2-hourly | Issue priority reassessment |
| Continuous | Real-time deployment monitoring, backlash detection |
| Per incident | Full Kontra Narrative cycle (K-1 through K-10) |
| Post-incident | Measurement + adaptation memo within 24 hours |

---

## G. Roles and Responsibilities

### Core Roles

| Role | Layer | Responsibility | Reports To |
|------|-------|---------------|------------|
| Intelligence Analyst | Layer 1 | Signal collection, fact extraction, SIB production | Intelligence Lead |
| Sentiment Analyst | Layer 1 | Emotion classification, trend detection, SEM production | Intelligence Lead |
| Influence Analyst | Layer 1 | Network mapping, actor profiling, INM production | Intelligence Lead |
| Intelligence Lead | Layer 1→2 | Coordinates all Layer 1 functions, produces IAB | Operations Director |
| Response Planner | Layer 2 | Response design, intervention selection, NIP drafting | Operations Director |
| Legal Reviewer | Layer 2 | Legal and ethical review, compliance, sign-off | Legal Counsel |
| Operations Director | Layer 2 | Decision authority (Elevated level), command authorisation | Director |
| Director | Layer 2 | Decision authority (Crisis/Critical level), strategic oversight | — |
| Content Producer | Layer 3 | Content production, format adaptation | Engagement Lead |
| Engagement Lead | Layer 3 | Channel activation, messenger briefing, deployment coordination | Operations Director |
| Measurement Analyst | Layer 3 | KPI tracking, sentiment re-measurement, adaptation memo | Operations Director |

### Role Separation Principle

**Intelligence analysts do not make deployment decisions. Engagement personnel do not verify intelligence. Legal reviewers are independent of both.** This separation prevents mission creep and ensures checks and balances.

---

## H. Document Templates

### SIB Template (Reality Phase)

```
SITUATIONAL INTELLIGENCE BRIEF
SIB-#[YEAR]-[SEQ]
Date/Time: [YYYY-MM-DD HH:MM UTC]
Version: [vX.X]
Analyst: [Name/ID]

1. SITUATION SUMMARY
   [2–3 paragraphs: what is happening, who is involved, current state]

2. VERIFIED FACT SET
   F-01: [Fact statement] | Confidence: [CONFIRMED/PROBABLE/POSSIBLE] | Sources: [S-01, S-02]
   F-02: [Fact statement] | Confidence: [...] | Sources: [...]
   ...

3. ACTOR AND STAKEHOLDER MAP
   A-01: [Actor name] | Role: [Primary/Secondary/Affected/Bystander] | Interest: [...] | Position: [...]
   ...

4. INFORMATION-GAP REGISTER
   G-01: [What we don't know] | Why it matters: [...] | Collection priority: [High/Med/Low]
   ...

5. SOURCE RELIABILITY ASSESSMENT
   S-01: [Source name] | Grade: [A–F] | Bias: [...] | Corroboration: [Y/N, by whom]
   ...

6. CONFIDENCE ASSESSMENT
   Overall confidence: [High/Medium/Low]
   Per-claim: [summary of confidence distribution]

7. ANALYST NOTES
   [Contextual judgement, caveats, alternative interpretations]
```

### NIP Template (Kontra Narrative Phase)

```
NARRATIVE INTERVENTION PLAN
NIP-#[YEAR]-[SEQ]
Date/Time: [YYYY-MM-DD HH:MM UTC]
Version: [vX.X]
Planner: [Name/ID]

1. NARRATIVE THREAT PROFILE
   Hostile narrative: [statement]
   Source: [who originated it]
   Spread: [platform, velocity, reach to date]
   Target audience: [segment]
   Harm assessment: [what happens if unaddressed]
   Threat level: [Low/Elevated/Crisis/Critical]

2. INTERVENTION SELECTION
   Selected: [Primary intervention type]
   Secondary: [Secondary intervention type, if any]
   Justification: [why this matches the narrative type]

3. AUDIENCE-CHANNEL PLAN
   Segment: [name] → Channel: [platform] → Messenger: [name] → Content: [reference]

4. CONTENT DRAFT
   [Attached: full content with 10-point checklist]

5. LEGAL AND ETHICAL REVIEW
   Reviewer: [name] | Date: [YYYY-MM-DD]
   Compliance: [PASS/FAIL] | Proportionality: [PASS/FAIL] | Deception: [PASS/FAIL]
   Notes: [...]

6. COMMAND AUTHORISATION
   Authority: [name/role] | Date: [YYYY-MM-DD HH:MM]
   Decision: [APPROVED/DENIED/DEFERRED]
   Conditions: [...]

7. DEPLOYMENT SCHEDULE
   T+0: [action] | T+[Xh]: [action] | ...

8. MEASUREMENT FRAMEWORK
   KPI | Baseline | Target | Method | Frequency
   [Reach] | [X] | [Y] | [platform analytics] | [24h, 48h, 7d]
   [Sentiment] | [X%] | [Y%] | [survey] | [pre, 3d, 7d]
   ...

9. RISK ASSESSMENT
   Amplification risk: [Low/Med/High] | Mitigation: [...]
   Backlash risk: [Low/Med/High] | Mitigation: [...]
   Misinterpretation risk: [Low/Med/High] | Mitigation: [...]

10. ADAPTATION TRIGGERS
    [Condition] → [Action]
    ...
```

---

*Companion document to R.I.S.I.K Framework*
*Saved: 2026-08-04*
*Authority: DAF*