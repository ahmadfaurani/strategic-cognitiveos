# R.I.S.I.K Framework

**Reality · Issue · Sentiment · Influence · Kontra Narrative**

An analytical and operational framework for modern psychological operations, strategic influence, and information warfare. Converts field intelligence, media data, public discourse, and audience behaviour into structured, measurable, and governed communication interventions.

---

## 1. Reality — Operational Reality

Establish the actual situation before any narrative, communication strategy, or intervention is developed.

### Key Questions
- What is actually happening?
- Who is involved and affected?
- What is the gap between fact, perception, and allegation?
- Which information has been verified?
- Which information remains uncertain, incomplete, or speculative?

### Process Steps

| Step | Action | Method | Output |
|------|--------|--------|--------|
| R-1 | Collect raw signals | Media monitoring, field reports, OSINT, social media capture | Raw signal feed |
| R-2 | Source triage | Source reliability rating (A–F), corroboration count, recency check | Triaged source list |
| R-3 | Fact extraction | Claims isolated from narrative framing; numbers, names, dates, locations verified against ≥2 independent sources | Verified fact set |
| R-4 | Gap mapping | Identify what is unknown, disputed, or speculative | Information-gap register |
| R-5 | Actor identification | Map all actors: primary, secondary, affected populations, bystanders | Actor and stakeholder map |
| R-6 | Confidence scoring | Assign confidence: CONFIRMED / PROBABLE / POSSIBLE / UNVERIFIED | Confidence-tagged fact set |
| R-7 | Baseline production | Compile situational intelligence brief | Situational Intelligence Brief (SIB) |

### Reality-Phase Deliverable: Situational Intelligence Brief (SIB)

1. Situation Summary (2–3 paragraphs)
2. Verified Fact Set (each item with source citations and confidence tag)
3. Actor and Stakeholder Map (with roles, interests, positions)
4. Information-Gap Register (what we don't know, why it matters)
5. Source Reliability Assessment (per source: grade, bias, corroboration)
6. Confidence Assessment (overall and per claim)
7. Analyst Notes (contextual judgement, caveats)

### Decision Gate: R → I
- [ ] At least one verified fact set exists for the situation
- [ ] Actor map is populated with primary actors
- [ ] Information gaps are logged (not hidden)
- [ ] Confidence is assessed — no claim presented as CONFIRMED without ≥2 sources
- [ ] SIB is timestamped and version-controlled

---

## 2. Issue — Core Issue

Identify the issues that carry political, social, emotional, operational, or reputational significance for the target audience.

### Process Steps

| Step | Action | Method | Output |
|------|--------|--------|--------|
| I-1 | Issue harvesting | Extract issues from SIB, media scan, field reports, audience signals | Raw issue list |
| I-2 | Issue definition | Each issue as one sentence: "[Actor] faces [problem] because [cause], affecting [population]" | Defined issue register |
| I-3 | Dimensional scoring | Score each issue 1–5 across 8 dimensions | Scored issue register |
| I-4 | Lifecycle assessment | Map: Emerging → Developing → Peak → Declining → Resolved | Issue lifecycle map |
| I-5 | Trigger identification | Define observable escalation indicators | Trigger indicator set |
| I-6 | Priority ranking | Weighted: Priority = (Relevance × Urgency × Magnitude × Strategic Impact) / Persistence | Issue priority matrix |
| I-7 | Contested-issue flag | Mark issues where actors disagree on facts, framing, or significance | Contestation map |

### Issue Assessment Dimensions

| Dimension | Assessment Focus | Score |
|-----------|-----------------|-------|
| Relevance | Affects the target audience | 1–5 |
| Urgency | Speed of development | 1–5 |
| Magnitude | Size of affected population | 1–5 |
| Credibility | Believability of the claim | 1–5 |
| Exploitation Potential | Likelihood of manipulation by others | 1–5 |
| Escalation Risk | Potential to trigger crisis | 1–5 |
| Persistence | Expected duration (inverse — longer = lower priority) | 1–5 |
| Strategic Impact | Effect on institutional objectives | 1–5 |

### Issue Lifecycle Stages

```
EMERGING → DEVELOPING → PEAK → DECLINING → RESOLVED
```

### Issue-Phase Deliverable: Issue Priority Matrix (IPM)

1. Issue Register (numbered, one-sentence definitions)
2. Dimensional Scores (per issue, per dimension, 1–5)
3. Priority Ranking (weighted, formula shown)
4. Lifecycle Assessment (per issue, stage and trajectory)
5. Trigger Indicators (observable, measurable, with thresholds)
6. Escalation Indicators (what moves issue to higher priority)
7. Contestation Map (where actors disagree, on what, with what evidence)
8. Strategic Impact Assessment (per issue: institutional, reputational, operational)

### Decision Gate: I → S
- [ ] At least 3 issues are defined and scored
- [ ] Top-priority issues are ranked with explicit formula
- [ ] Trigger indicators are specific and observable
- [ ] Issue lifecycle stage is assessed for each priority issue
- [ ] Contested issues are flagged for sentiment analysis

---

## 3. Sentiment — Audience Sentiment

Assess underlying emotions that influence perception, decision-making, and behaviour.

### Process Steps

| Step | Action | Method | Output |
|------|--------|--------|--------|
| S-1 | Data collection | Social media sampling, surveys, field reports, media tone analysis | Raw sentiment data |
| S-2 | Segmentation | Segment by demographics, geography, community, affiliation, platform, engagement, stakeholder, voter segment, issue exposure, behaviour | Segmented dataset |
| S-3 | Polarity scoring | Per segment: % positive, % negative, % neutral, % mixed | Sentiment distribution |
| S-4 | Emotion classification | Map to 10 emotional categories | Emotional driver analysis |
| S-5 | Intensity rating | Per emotion per segment: Low / Moderate / High / Volatile | Emotion intensity map |
| S-6 | Trend detection | Compare to previous window — rising, falling, stable, volatile | Sentiment-shift detection |
| S-7 | Threshold setting | Define escalation thresholds per segment | Escalation thresholds |
| S-8 | Behavioural risk assessment | Identify segments where sentiment → action | Behavioural-risk indicators |

### Emotional Categories

| Emotion | Indicators | Behavioural Implication |
|---------|-----------|------------------------|
| Anger | Blame language, accountability calls, aggressive posts | Confrontation, mobilisation |
| Fear | Safety concerns, protective language, rumour amplification | Withdrawal, panic |
| Frustration | Complaints about inaction, grievance repetition | Disengagement, protest vote |
| Distrust | Skepticism of official claims, conspiracy engagement | Rejection of messaging |
| Hope | Aspirational language, positive expectations | Engagement, cooperation |
| Pride | Identity affirmations, group solidarity | Mobilisation, loyalty |
| Apathy | Low engagement, disinterest | Non-participation, low turnout |
| Anxiety | Uncertainty expressions, future concern | Risk-averse behaviour |
| Solidarity | Group cohesion, mutual support | Collective action |
| Resentment | Perceived injustice, grievance accumulation | Score-settling, retaliation |

### Sentiment-Phase Deliverable: Sentiment and Emotion Map (SEM)

1. Sentiment Heatmap (segment × polarity, colour-coded)
2. Emotional-Driver Analysis (per segment: dominant emotions, intensity, triggers)
3. Audience Segmentation Matrix (segments with size, characteristics, sentiment profile)
4. Sentiment-Shift Detection (current vs previous: direction, velocity, volatility)
5. Behavioural-Risk Indicators (segments at risk of: protest, disengagement, vote shift, radicalisation)
6. Escalation Thresholds (per segment: numeric triggers for alert levels)

### Decision Gate: S → In
- [ ] At least 3 audience segments are defined and profiled
- [ ] Dominant emotions per segment are identified with evidence
- [ ] Sentiment trends are established (≥2 measurement points)
- [ ] Escalation thresholds are quantified
- [ ] Behavioural-risk segments are flagged

---

## 4. Influence — Influence Mapping

Identify the individuals, organisations, platforms, networks, and channels that shape public understanding, perception, and behaviour.

### Process Steps

| Step | Action | Method | Output |
|------|--------|--------|--------|
| In-1 | Actor discovery | Identify all actors producing, amplifying, or shaping narratives | Raw actor list |
| In-2 | Actor classification | Categorise: official, media, community, digital, anonymous, automated | Classified registry |
| In-3 | Reach assessment | Estimate audience size per actor | Reach scoring |
| In-4 | Resonance assessment | Measure engagement rates: shares, comments, sentiment of responses | Resonance scoring |
| In-5 | Authority mapping | Document formal/informal authority | Authority profile per actor |
| In-6 | Network analysis | Map: who amplifies whom, coordinated patterns, clusters | Influence network map |
| In-7 | Narrative alignment | Map each actor to positions on priority issues | Narrative distribution map |
| In-8 | Vulnerability mapping | Identify audience clusters most exposed to each actor | Vulnerable clusters |
| In-9 | Trusted-messenger identification | High credibility + high reach + objective alignment | Trusted-messenger matrix |
| In-10 | Credibility risk assessment | Flag actors with reputational or manipulation exposure | Credibility risk register |

### Influence Assessment Factors

| Factor | Assessment Focus | Measurement Method |
|--------|-----------------|-------------------|
| Reach | Audience size | Follower count, group membership, circulation |
| Resonance | Message acceptance | Engagement rate, share-to-comment ratio |
| Authority | Formal/informal standing | Position verification, community recognition |
| Network Position | Location in network | Centrality analysis, bridge detection |
| Mobilisation Capacity | Ability to trigger action | Historical calls to action → behaviour |
| Narrative Alignment | Position on issues | Content analysis of recent statements |
| Credibility | Trust level | Surveys, peer assessment, fact-check history |
| Amplification Capacity | Visibility boosting | Cross-platform presence, syndication |
| Credibility Risk | Exposure to compromise | Scandal history, conflicts, inconsistency |

### Influence-Phase Deliverable: Influence Network Map (INM)

1. Key Influencer Registry (ranked by reach × resonance × authority)
2. Influence Network Map (nodes = actors, edges = amplification, clusters = communities)
3. Amplification Pathway (message origin → mass audience)
4. Narrative Distribution Map (which actors advance which narratives)
5. Vulnerable Audience Clusters (segments most exposed to specific actors)
6. Engagement Priority List (who to engage first, and why)
7. Trusted-Messenger Matrix (actor × issue × credibility × reach × alignment)
8. Credibility Risk Register (actors flagged with risk type and severity)

### Decision Gate: In → K
- [ ] Key influencers are identified and ranked
- [ ] Network map shows amplification pathways
- [ ] Narrative distribution is mapped
- [ ] Trusted messengers are identified for priority issues
- [ ] Vulnerable audience clusters are defined
- [ ] Credibility risks are flagged and assessed

---

## 5. Kontra Narrative — Counter-Narrative

Replace harmful, misleading, or destabilising interpretations with explanations that are more credible, relevant, evidence-based, and meaningful to the intended audience.

### Principles
- Address the audience's actual concerns
- Acknowledge realities that cannot reasonably be denied
- Use language that is understandable and culturally appropriate
- Be delivered through credible and trusted messengers
- Provide both explanation and practical action
- Avoid unnecessarily repeating or amplifying hostile narratives
- Be proportionate to the actual level of threat
- Be measured through changes in perception, confidence, and behaviour
- Remain grounded in verified facts
- Comply with legal, ethical, and institutional governance requirements

### Process Steps

| Step | Action | Method | Output |
|------|--------|--------|--------|
| K-1 | Narrative threat assessment | Map hostile narrative: claim, source, spread, target, harm | Narrative threat profile |
| K-2 | Intervention selection | Match narrative type to intervention type | Selected intervention(s) |
| K-3 | Audience targeting | Segment → channel → messenger | Audience-channel plan |
| K-4 | Messenger selection | Match messenger to segment via trusted-messenger matrix | Messenger assignment |
| K-5 | Content development | Draft: factual base, emotional register, cultural framing, CTA | Content draft |
| K-6 | Legal and ethical review | Truth compliance, proportionality, non-deception | Review sign-off |
| K-7 | Command authorisation | Present to designated authority for approval | Authorisation record |
| K-8 | Execution | Deploy through approved channels and messengers | Deployment log |
| K-9 | Measurement | Track KPIs: reach, engagement, sentiment shift, behaviour | Measurement report |
| K-10 | Adaptation | Review results, adjust, feed learnings back to Reality | Updated plan |

### Intervention Selection Matrix

| Narrative Type | Primary Intervention | Secondary | When to Use |
|---------------|---------------------|-----------|------------|
| False factual claim | Debunking | Evidence amplification | Claim verifiably false and spreading |
| Misleading framing | Reframing | Contextual clarification | Facts true, interpretation distorted |
| Emotional manipulation | Positive replacement | Trusted-messenger | Exploits fear/anger without factual basis |
| Emerging threat | Pre-bunking | Strategic silence | Narrative predicted but not yet circulating |
| Low-impact rumour | Strategic silence | Contextual clarification | Responding would amplify more than ignoring |
| Coordinated disinformation | Evidence amplification | Trusted-messenger | False narrative with organised amplification |
| Legitimate grievance | Contextual clarification | Behavioural intervention | Concern is real but being exploited |
| Call to harmful action | Behavioural intervention | Debunking (trigger claim) | Narrative mobilising toward harm |

### Counter-Narrative Content Requirements (10-Point Checklist)

1. **Factual Base** — What verified facts support this? (cite SIB)
2. **Acknowledgement** — What legitimate concern is acknowledged?
3. **Reframing** — What is the more accurate or constructive frame?
4. **Evidence** — What specific evidence is presented? (verifiable, cited)
5. **Messenger** — Who delivers this and why are they credible?
6. **Channel** — Where does this reach the target audience?
7. **Cultural Adaptation** — How is language tailored to the audience?
8. **Call to Action** — What should the audience do after receiving this?
9. **Measurement Hook** — How will we know if this worked? (KPI)
10. **Risk Assessment** — What are the risks? (amplification, backlash, misinterpretation)

### Intervention Types — Detailed

**Pre-bunking** — Before harmful narrative circulates. Warn about likely manipulation, inoculate with critical thinking frames. KPI: audience recognition of pattern when it appears.

**Debunking** — After false claim spreads. Present claim briefly, then detailed correction with evidence. Rule: don't repeat false claim more prominently than correction. KPI: correction reach vs original; belief change in surveys.

**Reframing** — Facts correct, interpretation misleading. Shift frame without denying facts. KPI: frame adoption in discourse.

**Positive Replacement** — Harmful narrative fills a vacuum. Provide more compelling, credible alternative. KPI: narrative adoption.

**Evidence Amplification** — Verified evidence exists but is under-visible. Increase visibility through trusted channels. KPI: evidence reach; citation in discussion.

**Trusted-Messenger Intervention** — Institutional messaging lacks credibility. Deploy community-trusted figures. KPI: audience response to messenger vs institutional source.

**Contextual Clarification** — Key facts or context are missing. Provide missing information without counter-attack framing. KPI: information absorption; speculation reduction.

**Strategic Silence** — Responding would amplify low-impact narrative. Do not respond publicly; monitor; prepare response in case of escalation. KPI: narrative decay rate.

**Behavioural Intervention** — Audience needs to act, not just understand. Provide clear, actionable steps paired with explanation. KPI: behavioural uptake.

### Kontra-Phase Deliverable: Narrative Intervention Plan (NIP)

1. Narrative Threat Profile (claim, source, spread trajectory, harm, target audience)
2. Selected Intervention Type(s) with justification
3. Audience-Channel Plan (segment → channel → messenger → content)
4. Content Draft(s) with all 10 content requirements
5. Legal and Ethical Review Sign-off
6. Command Authorisation Record
7. Deployment Schedule (sequence, timing, dependencies)
8. Measurement Framework (KPIs, baseline, target, method, frequency)
9. Risk Assessment (amplification, backlash, misinterpretation, mitigation)
10. Adaptation Trigger Criteria (what would cause mid-execution change)

### Decision Gate: K → Execute
- [ ] Intervention type justified by narrative type
- [ ] Content grounded in verified facts (SIB cited)
- [ ] Messenger credible to target audience (trusted-messenger matrix cited)
- [ ] Legal and ethical review completed and signed off
- [ ] Command authorisation obtained and recorded
- [ ] KPIs defined with baselines and targets
- [ ] Risk assessment completed with mitigation plan
- [ ] Adaptation triggers defined

---

## R.I.S.I.K Operational Flow

```
REALITY                      Layer 1: Intelligence
What is actually happening?
 ↓
ISSUE
Which issue is most significant
and most likely to escalate?
 ↓
SENTIMENT
What is the audience feeling, and why?
 ↓
INFLUENCE
Who is shaping and spreading the perception?
 ↓
KONTRA NARRATIVE            Layer 2: Decision
What communication               ↓
intervention is most        Layer 3: Engagement
appropriate?
 ↓
MEASURE → LEARN → ADAPT → (loop back to REALITY)
```

### Cycle Timing

| Phase | Normal Tempo | Crisis Tempo | Continuous? |
|-------|-------------|-------------|------------|
| Reality | Daily | Hourly | Monitoring continuous; SIB updated per cycle |
| Issue | Daily | 2× daily | Issue register updated as signals arrive |
| Sentiment | 2× weekly | Daily | Automated monitoring continuous |
| Influence | Weekly | Daily | Network map updated as new actors emerge |
| Kontra Narrative | Per incident | Per incident | Pre-positioned content maintained continuously |
| Measure → Adapt | Weekly | Post-intervention | Continuous measurement; formal review per cycle |

---

## Three-Layer Operating Model

### Layer 1 — Intelligence

Establishes situational awareness and identifies emerging threats, issues, actors, and narratives.

| Function | Activities | Cadence | Output |
|----------|-----------|---------|--------|
| Media monitoring | Multi-source news collection, social media scan, narrative detection | Continuous | Signal feed |
| Field intelligence | Reports from ground teams, community contacts, observers | Per report | Field report |
| OSINT | Public source analysis, platform research, digital footprint | Daily | OSINT product |
| Issue analysis | Issue harvesting, dimensional scoring, lifecycle assessment | Daily | Issue register |
| Actor analysis | Actor identification, classification, motivation assessment | Daily | Actor registry |
| Audience analysis | Segmentation, profiling, behavioural assessment | Per cycle | Audience profiles |
| Sentiment intelligence | Emotion classification, trend detection, threshold monitoring | Continuous | Sentiment feed |
| Narrative detection | Emerging narrative identification, trajectory tracking | Continuous | Narrative tracker |
| Influence-network analysis | Network mapping, amplification tracking, broker identification | Weekly | Network map |
| Disinformation detection | Pattern recognition, coordination analysis, bot identification | Continuous | Threat alerts |

### Layer 2 — Decision

Converts intelligence into governed strategic and operational decisions.

| Function | Activities | Cadence | Output |
|----------|-----------|---------|--------|
| Risk assessment | Threat scoring, vulnerability mapping, probability estimation | Per issue | Risk assessment |
| Issue prioritisation | Weighted ranking, resource allocation, focus determination | Daily | Priority matrix |
| Audience identification | Target segment selection, message-audience matching | Per intervention | Target audience list |
| Response selection | Intervention type matching, proportionality check | Per intervention | Response plan |
| Channel selection | Platform fit, audience reach, cost-benefit | Per intervention | Channel plan |
| Messenger selection | Trusted-messenger matching, credibility verification | Per intervention | Messenger assignment |
| Narrative approval | Content review, factual verification, strategic alignment | Per intervention | Approved content |
| Escalation-threshold setting | Define triggers for escalation/de-escalation | Per issue | Threshold set |
| Legal and ethical review | Compliance, proportionality, deception exclusion | Per intervention | Review sign-off |
| Command authorisation | Authority review, approval/denial, documentation | Per intervention | Authorisation record |

### Layer 3 — Engagement

Executes the approved intervention through appropriate channels, messengers, and engagement mechanisms.

| Function | Activities | Cadence | Output |
|----------|-----------|---------|--------|
| Strategic content | Content production, format adaptation, quality control | Per intervention | Content product |
| Leadership briefings | Executive preparation, talking points, Q&A prep | Per intervention | Briefing pack |
| Community engagement | Local activation, grassroots deployment, feedback collection | Per intervention | Engagement log |
| Media response | Press statements, interview prep, journalist management | Per intervention | Media package |
| Stakeholder activation | Ally coordination, coalition messaging, partner briefing | Per intervention | Stakeholder log |
| Public communication | Direct public address, platform posting, broadcast | Per intervention | Publication record |
| Counter-disinformation | Targeted correction, platform reporting, fact-deployment | Per intervention | Correction record |
| Trusted-messenger mobilisation | Messenger briefing, content provision, deployment support | Per intervention | Deployment log |
| Performance measurement | KPI tracking, audience polling, sentiment re-measurement | Post-intervention | Measurement report |
| Continuous adaptation | Strategy review, content adjustment, lesson capture | Post-intervention | Adaptation memo |

---

## R.I.S.I.K Operational Matrix

| Component | Operational Question | Primary Deliverable | Key Inputs | Decision Gate |
|-----------|---------------------|-------------------|------------|---------------|
| Reality | What is true and verifiable? | Situational intelligence brief | Signals, sources, field reports | SIB complete with confidence tags |
| Issue | What is the primary area of contestation? | Issue priority matrix | SIB, media scan, field reports | ≥3 issues scored and ranked |
| Sentiment | What is the audience feeling, and why? | Sentiment and emotion map | Social data, surveys, field reports | ≥3 segments profiled with thresholds |
| Influence | Who is shaping perception and behaviour? | Influence network map | Actor registry, network analysis | Trusted messengers identified |
| Kontra Narrative | How should perceptions be addressed? | Narrative intervention plan | All prior deliverables | Legal review + command authorisation |

---

## Operating Principles

- **Truth-grounded** — based on verified and defensible facts
- **Evidence-led** — supported by reliable sources and analytical confidence
- **Audience-specific** — tailored to each audience segment
- **Proportionate** — calibrated to actual severity
- **Measurable** — supported by clear indicators and defined outcomes
- **Adaptive** — continuously updated as conditions change
- **Legally governed** — compliant with applicable laws and controls
- **Ethically controlled** — subject to ethical boundaries and human oversight
- **Non-deceptive** — excluding fabrication, impersonation, unlawful manipulation
- **Human-authorised** — significant interventions under accountable human authority
- **Secure by design** — protecting sensitive data, sources, methods, and decisions

---

## Strategic Positioning

R.I.S.I.K is a structured framework for establishing reality, identifying the central issue, understanding audience sentiment, mapping influence networks, and executing lawful, evidence-based, and measurable counter-narrative interventions.

### Application Domains

- Strategic communication operations
- Psychological operations
- Information warfare analysis
- Political intelligence operations
- Election operations centres
- Government crisis communication
- Counter-disinformation operations
- Stakeholder influence mapping
- Cognitive security operations
- National security communication
- Public sentiment and policy engagement
- Media and information warfare studies
- Strategic decision-support systems

---

*Document saved: 2026-08-04*
*Source: DAF — R.I.S.I.K Framework specification (expanded with operational process)*
*Authority: DAF*