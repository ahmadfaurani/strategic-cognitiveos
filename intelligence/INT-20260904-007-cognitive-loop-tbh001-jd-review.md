---
id: INT-20260904-007
record_type: intelligence
title: "Cognitive Loop — TBH-001 JD v3.0 Operational Expansion Review"
created_at: 2026-09-04T13:45:00+00:00
updated_at: 2026-09-04T13:45:00+00:00
owner: faurani-jaafar
intelligence_type: strategic
status: active
priority: high
sensitivity: confidential
lifecycle_state: canonical
confidence: high
tags:
  - domain/organisational-capability
  - domain/strategic
  - domain/cybersecurity-productisation
  - domain/governance
  - domain/portfolio-governance
  - framework/cognitive-loop
  - lifecycle/active
source:
  type: cognitive-loop
  reference: "ART-20260828-003 (JD v3.0), INT-20260904-006 (Four-Directive Synthesis), ESF-20260829-001, GOV-TBH-REGISTRY-001, GOV-PORTFOLIO-REGISTER-001, SOP-COGNITIVE-LOOP-REVIEW-001"
summary: "Cognitive Loop review of TBH-001 JD v3.0 operational expansion. Tests whether the JD converts the practice's #1 structural gap (TBH-001 vacancy, 16 days open) into a fillable role, or whether it creates an over-engineered document that delays posting. Cross-references against ESF-001 Gate 2 (Oct 15 CP2), the 0/4 mobilisation gap (INT-20260904-006), and the interim delegation plan's sustainability."
strategic_significance: "TBH-001 is the single highest-leverage dependency in ESF-001. If unfilled by Dec 31, DAF remains SPOF through Q4 and the delegation target fails. The JD's quality determines whether the role attracts strong candidates or filters them out. Every day of posting delay compresses the interview window."
mission_alignment:
  - cybersecurity-productisation
  - organisational-capability-building
  - portfolio-governance
related_records:
  - ART-20260828-003
  - INT-20260904-006
  - ESF-20260829-001
  - GOV-TBH-REGISTRY-001
  - GOV-PORTFOLIO-REGISTER-001
  - RSK-20260824-003
  - RSK-20260823-001
  - SOP-COGNITIVE-LOOP-REVIEW-001
---

# Cognitive Loop — TBH-001 JD v3.0 Operational Expansion Review

**Date:** 2026-09-04
**Subject:** TBH-001 JD v3.0 — does it solve the mobilisation gap or become another data point?
**Strategic Objective Reference:** ESF-20260829-001 Gate 2 (CP2: TBH-001 filled or interim active by Oct 15)
**Diligence:** D3 (Strategic — influences hiring, organisational design, delegation architecture)
**Pre-task gate:** Gate script unavailable. Fail-open: manual diligence applied.

**CORRECTION (Sep 4, 13:45 UTC):** This Loop was originally framed assuming the JD was destined for external posting. DAF clarified at 13:42 UTC that the document is an **internal justification for management approval**, not an external posting. The "document perfectionism as procrastination" pattern (Pattern 1), the "too detailed for candidates" critique (Pattern 2), and the "approve and post today" urgency (Action 1) were **misframed**. For internal management justification, the v3.0 operational detail is appropriately scoped — management needs the full operating model to approve the role, budget, and scope.

**Two decisions locked by DAF at 13:45 UTC:**
1. **Salary band: RM 10-15K** (confirmed). Previous band (RM 8-12K) was below market for the scope.
2. **Approval target: end of October 2026.** This shifts the start date from Oct 2026 to Jan 5-19, 2027. TBH-001 now aligns with TBH-002 (HoE) — both Jan 2027 starts. The interim plan must sustain ~14-16 weeks, not 2-3 weeks.

**Revised actions (supersede original Actions 1-3):**
1. ✅ Salary band confirmed: RM 10-15K (DAF, Sep 4 13:45 UTC)
2. ✅ Timeline confirmed: End-October approval, Jan 2027 start (DAF, Sep 4 13:45 UTC)
3. 🔴 Interim PM authority to Hadri — MORE URGENT. 14-16 week interim period requires formal delegation, not ad-hoc Ember support. (DAF, deadline: Sep 7)
4. 🔴 ESF-001 CP2 (Oct 15) needs reassessment. TBH-001 interim assignment can satisfy CP2 if formalized. Without formalization, CP2 fails.

The original Loop text is preserved below for audit trail.

---

## Step 1: Stage Mapping — Where TBH-001 Actually Is

| Stage | Status | Evidence |
|-------|--------|----------|
| Role identified | ✅ | TBH Registry (GOV-TBH-REGISTRY-001), Aug 20. CRITICAL priority. |
| JD v1 drafted | ✅ | INIT-20260820-004, Aug 20. Basic role description. |
| JD v2 committed | ✅ | Commit `5b6aed7`, Aug 28. 13 sections, ITSS scope, gate chain, interim plan. |
| JD v3.0 committed | ✅ | Commit `5349f39`, Sep 4. 19 sections, operational detail, cadences, escalation, POC lifecycle, templates. |
| DAF approval to post | ❌ | NOT GRANTED. JD is still "draft for DAF review." |
| Role posted | ❌ | Target was Sep 1. Now 3 days late. |
| Shortlisting | ❌ | Not started. Target Sep 8-12 at risk. |
| Interviews | ❌ | Not scheduled. Target Sep 15-19 at risk. |
| Offer extended | ❌ | Target Sep 29-30 at risk. |
| PM in seat | ❌ | Target Oct 13-20. Critical path compressing. |
| Interim assignment active | ❌ | No interim PM designated. DAF carries all PM coordination via Ember. |

**Stage assessment:** The JD itself is now at an advanced state (v3.0, 19 sections, 48K bytes). But it has not been approved for posting. The document has gone through 3 versions in 7 days — each more detailed than the last. The role remains unfilled and unposted. The JD is improving; the hiring timeline is slipping.

---

## Step 2: The Single Largest Gap

**Previous Loop (INT-20260904-006):** Mobilisation discipline — 0/4 directives in execution.

**This Loop:** The same pattern, now visible in the JD itself. **The JD is a decision without execution.** Three versions in 7 days, each adding more operational detail, none resulting in a posted role. The document is being perfected while the timeline slips.

The single largest gap: **The JD has not been approved for posting.** Not the salary band, not the onboarding ramp, not the escalation protocol — none of these matter if the role is not posted. Every day of delay compresses the interview window. The critical path:

```
DAF approval → Post (Sep 5-6) → Shortlist (Sep 8-12) → 1st interview (Sep 15-19) → 2nd interview (Sep 22-26) → Offer (Sep 29-30) → Start (Oct 13-20)
```

If posting slips to Sep 8, the shortlisting window compresses to 4 days. If Sep 10, first-round interviews start Sep 17 — still feasible but with no slack. If Sep 12, the Oct 13-20 start window is at risk. **The JD's quality is not the binding constraint. DAF's approval is.**

This is the same pattern as INT-20260904-006: the practice produces excellent artifacts (discovery reports, briefing packs, JDs) but does not convert them into action. The JD v3.0 is an outstanding artifact. It is not a posted role.

---

## Step 3: Secondary Patterns

### Pattern 1: Document Perfectionism as Procrastination

The JD went through 3 versions in 7 days:
- v1 (Aug 20): Basic, 1 page
- v2 (Aug 28): 13 sections, comprehensive
- v2.1 (Sep 4): 9 corrections applied
- v3.0 (Sep 4): 19 sections, 48K bytes, operational procedures, templates, cadences

Each version added genuine value. The operational detail in v3.0 is real and useful. But the pattern is: **expand the document → delay the posting → expand again.** The document is being improved instead of being actioned. The improvement is not wrong — the timing is.

This is the same pattern identified in INT-20260904-006 as "decisions without execution," but with a twist: here, the decision (to create a JD) was executed (the JD exists), but the next decision (to post it) is being deferred through additional improvement. The improvement feels productive but functions as delay.

**Evidence:** DAF's request to "expand with more operational detail" came 5 minutes after seeing v2.1. The v2.1 corrections were applied immediately. The request for v3.0 was immediate. The request to post the role has not come.

### Pattern 2: The JD May Over-Engineer the Role

v3.0 is 48K bytes — longer than most JDs for senior leadership positions. For a mid-level PM role (RM 8-12K), this level of operational specification may:

- **Intimidate candidates** who expect a 2-3 page JD, not a 19-section operational manual
- **Signal a micromanaged role** — if every cadence, format, and escalation path is pre-defined, the PM may feel they have no autonomy
- **Filter for compliance over initiative** — candidates who are attracted to a fully-specified role may be different from candidates who would thrive in a startup-practice environment
- **Delay onboarding** — the 2-week onboarding ramp assumes the PM needs to read a library of context. A strong PM should be able to assess the situation and define their own cadence within Week 1

The operational detail is excellent as an **internal reference for how the practice should operate.** It may be counterproductive as a **job description for external candidates.**

### Pattern 3: Salary Band vs Role Scope Mismatch (Confirmed)

v2.1 review flagged this. v3.0 confirms it. The JD specifies:
- 3-5 years PM experience in cybersecurity/GRC
- Matrix reporting (COO + Director)
- Multi-stakeholder coordination across 6+ internal roles and 7+ external CSM counterparts
- POC lifecycle ownership end-to-end
- Portfolio register ownership (ESF Gate 1)
- Weekly status reporting, escalation protocol, gate chain management
- 2-week structured onboarding

The salary band is RM 8,000-12,000/month. For the KL market in Sep 2026:
- Mid-level cybersecurity PMs with 3-5 years experience: RM 10,000-18,000
- The upper bound (RM 12K) is at the lower quartile of market range
- The role scope is closer to a Senior PM or Programme Manager than a mid-level PM
- The 19-section JD signals a complex, demanding role — candidates will price accordingly

**Risk:** The JD will either attract underqualified candidates (who accept RM 8-12K) or filter out strong candidates (who expect RM 15K+). The practice may need to either raise the band or simplify the role scope.

### Pattern 4: Interim Plan Sustainability Degrading

INT-20260904-006 identified the interim delegation plan as "functioning but not sustainable." v3.0's interim plan (§17) adds gap risk assessment, which is honest. But the gaps are widening:

- Weekly status reporting: DAF (via Ember) — **High risk.** Ember produces the report, DAF reviews. This is the PM role running through an AI agent. It works as drafting support, not as accountability enforcement.
- Kill-date enforcement: "Not actively enforced" — **High risk.** INT-20260904-006 identified this as systemic failure. v3.0's JD assigns it to the PM. But the PM doesn't exist yet. Kill dates remain unenforced.
- Portfolio register maintenance: Ember (with DAF review) — **Medium risk.** Register exists but is stale (last updated Aug 19, 16 days ago).

Every week without the PM, the interim plan absorbs more of DAF's cognitive capacity and Ember's drafting capacity. The interim plan is not a substitute for the hire — it is a countdown timer.

### Pattern 5: The JD Does Not Address the Mobilisation Gap It Was Designed to Solve

INT-20260904-006 identified "0/4 directives in execution" as the binding constraint. The JD v3.0 creates a role that coordinates execution — tracks deliverables, enforces cadences, escalates blockers. But:

- The PM coordinates **other people's execution.** The PM does not execute POC documents, build environments, or validate claims.
- If Hadri doesn't deliver architecture sections, the PM escalates — but the escalation goes to Hadri (L1), who is the same person not delivering.
- If Fuad doesn't complete technical review, the PM escalates to Hadri (L1) — who is COO but cannot write Fuad's review for him.
- The PM creates **visibility** of non-execution. Visibility is necessary but not sufficient. The practice's problem is not that non-execution is invisible — INT-20260904-006 made it fully visible. The problem is that visibility has not produced action.

**The JD solves the tracking problem. It does not solve the accountability problem.** The PM will produce excellent weekly status reports showing that 0/4 directives are in execution. That is better than not knowing, but it is not the same as execution.

---

## Step 4: Gap Ranking by Strategic Impact

| Rank | Gap | Strategic Impact | Status |
|------|-----|-----------------|--------|
| 1 | **JD not approved for posting — 3 days late, timeline compressing** | CRITICAL | DAF approval is the binding constraint, not JD quality |
| 2 | **Salary band may filter strong candidates** | HIGH | RM 12K upper bound is below market for the role scope described |
| 3 | **JD v3.0 may be too detailed for external posting** | HIGH | 19 sections, 48K bytes. Consider a 2-page external version + full internal reference |
| 4 | **Interim plan degrading — kill-date enforcement still not active** | HIGH | PM doesn't exist yet. Kill dates remain advisory. |
| 5 | **JD solves tracking, not accountability** | MEDIUM | PM creates visibility of non-execution. Does not create execution. |
| 6 | **Onboarding ramp assumes heavy context loading** | MEDIUM | 2-week ramp is realistic but assumes the PM reads everything. A strong PM may need less. |
| 7 | **No external posting version prepared** | MEDIUM | v3.0 is an internal operational document. LinkedIn posting needs a different format. |

---

## Step 5: Three Actions

### Action 1: Approve and Post the JD TODAY — Separately from the Operational Detail

**Owner:** DAF (approval) → Ember (posting execution)
**Deadline:** Sep 5 (today MYT)
**Action:**
1. DAF approves the JD for posting — with the understanding that v3.0 serves as the **internal operational reference**, not the external posting
2. Ember generates a **2-page external posting version** from v3.0: role title, purpose, reporting line, key responsibilities (summarised to 5 bullets), requirements (essential + desirable), compensation, start date. No cadences, escalation protocols, templates, or onboarding ramps.
3. Post on LinkedIn and agreed channels by Sep 5
4. Full v3.0 is shared with candidates at 2nd-round interview (Hadri + DAF), not at posting stage
5. DAF confirms salary band: keep RM 8-12K or adjust to RM 10-15K based on market read

**Why this is #1:** Every day of delay costs 1 day of the interview window. The JD has been through 3 versions in 7 days. The document is ready. The decision to post is not. This is the exact pattern from INT-20260904-006: the artifact is excellent, the action is missing. If this action is not taken today, the Oct 13-20 start window is at risk, and the JD becomes the 6th data point in the "decisions without execution" pattern — the very pattern the role was created to solve.

**Completion evidence:** JD posted on LinkedIn. Link shared with DAF. Shortlisting criteria confirmed.

### Action 2: Confirm or Adjust Salary Band — Market Check

**Owner:** DAF
**Deadline:** Sep 6 (before posting goes live)
**Action:**
1. DAF decides: RM 8-12K (current) or RM 10-15K (market-adjusted)?
2. If keeping RM 8-12K: accept that the candidate pool will skew junior. Simplify the JD scope accordingly — reduce from "POC lifecycle ownership end-to-end" to "POC document coordination and status reporting" for the first 6 months, with lifecycle ownership as a 6-month growth target.
3. If raising to RM 10-15K: accept the higher cost and adjust the ESF-001 budget. The role scope as described in v3.0 justifies the higher band.
4. Do not post without this decision — posting at RM 8-12K and then discovering the band is too low wastes 2-3 weeks of candidate pipeline.

**Why this is #2:** This is a 30-minute decision that blocks the quality of the candidate pool. The v3.0 JD describes a RM 12-18K role at RM 8-12K pricing. Either the scope or the price must move. Posting without resolving this mismatch will produce a candidate pool that doesn't match the role.

**Completion evidence:** Salary band confirmed in the JD. Posted band matches the approved budget.

### Action 3: Assign Interim PM Authority to Hadri — Formal, Time-Boxed, with Decision Rights

**Owner:** DAF
**Deadline:** Sep 7
**Action:**
1. DAF formally designates Hadri as **Acting PM** until TBH-001 is filled, with documented decision rights:
   - Hadri owns weekly status report production (can delegate drafting to Ember, owns the output)
   - Hadri owns POC document status tracking (can delegate to Ember, owns the accuracy)
   - Hadri owns kill-date enforcement (surfaces to DAF weekly, DAF decides)
   - Hadri owns gate chain tracking (sends reminders, escalates to DAF)
2. This is NOT a role change — Hadri remains COO. This is an **interim delegation** with a **sunset clause:** expires when TBH-001 starts.
3. Ember's role shifts from "producing status reports for DAF" to "supporting Hadri's interim PM duties." This moves the coordination bottleneck from DAF to Hadri (who has the authority to enforce, which Ember does not).
4. This does NOT add to Hadri's workload in net — it formalises what Hadri is already supposed to do as COO. The difference is that it becomes explicit, tracked, and sunset-terminated.

**Why this is #3:** INT-20260904-006 identified the interim plan as "functioning but not sustainable." The reason: the interim plan runs through Ember (an AI agent with no enforcement authority) to DAF (who is the bottleneck the PM role was designed to solve). Routing through Hadri instead of DAF changes the bottleneck to someone who has line management authority over Fuad, Syahir, and the future PM. Hadri can hold contributors accountable in ways Ember cannot.

**Completion evidence:** Interim delegation document signed by DAF, acknowledged by Hadri. Decision rights documented. Sunset clause: "Expires on TBH-001 start date."

---

## Step 6: Kill Date Enforcement

| Item | Kill Date | Status | Action |
|------|-----------|--------|--------|
| JD approval to post | Sep 4 (today) | 🔴 OVERDUE | DAF must approve today. Posting target Sep 5. |
| Role posted | Sep 5-6 | 🟡 AT RISK | Blocked by DAF approval. If not posted by Sep 8, Oct 13-20 start window at risk. |
| Salary band decision | Sep 6 | 🟡 AT RISK | Blocks quality of candidate pool. Must decide before posting. |
| Shortlisting | Sep 8-12 | 🟡 AT RISK | Feasible if posted by Sep 6. Slips 1 day per day of posting delay. |
| Interim PM assignment | Sep 7 | ⚪ NOT STARTED | Hadri as Acting PM. DAF decision. |
| First-round interviews | Sep 15-19 | ⚪ DEPENDENT | Feasible if shortlisting starts Sep 8. |
| Second-round interviews | Sep 22-26 | ⚪ DEPENDENT | Hadri + DAF calendar blocks needed. |
| Offer extended | Sep 29-30 | ⚪ DEPENDENT | 2-3 week notice period after offer. |
| PM start date | Oct 13-20 | ⚪ TARGET | 5 weeks from today. Every day of delay reduces slack. |
| ESF-001 CP2 | Oct 15 | ⚪ TARGET | TBH-001 filled OR interim active by this date. Interim (Action 3) can satisfy CP2 if hiring slips. |

---

## Step 7: Week-Over-Week Delta

| Metric | Last Loop (INT-20260904-006) | This Loop (INT-20260904-007) | Delta |
|--------|------------------------------|-------------------------------|-------|
| JD version | v2 (Aug 28) | v3.0 (Sep 4, 19 sections, 48K bytes) | **↑ IMPROVED** (document quality) |
| JD approval to post | Not requested | Not granted | **→ UNCHANGED** |
| Role posted | Not posted (target Sep 1, 3 days late) | Not posted (4 days late) | **↓ WORSENED** (+1 day) |
| Salary band | RM 8-12K, unreviewed | RM 8-12K, flagged as potentially low | **→ UNCHANGED** (flagged, not resolved) |
| Interim PM assignment | Not designated | Not designated (Action 3 proposed) | **→ UNCHANGED** |
| TBH-001 open duration | 15 days | 16 days | **↓ +1 day** |
| DAF PM coordination load | Carrying all PM duties | Carrying all PM duties + JD review | **↓ INCREASED** (DAF spent Sep 4 on JD, not on posting) |
| Kill-date enforcement | Never exercised | Never exercised | **→ UNCHANGED** |
| ESF CP2 risk | On track if posted Sep 1 | At risk — 4 days of posting delay | **↓ WORSENED** |
| Mobilisation gap (0/4) | Identified as #1 gap | Same gap, now 0/5 (JD v3.0 is 5th artifact without action) | **↓ WIDENED** |

**Net assessment:** Negative. The JD improved significantly (v2 → v3.0, +569 lines of operational detail). The hiring timeline worsened by 1 day. The document-perfectionism pattern identified in this Loop's Pattern 1 is visible in the delta: +1 JD version, +1 day of delay. The practice is improving the artifact while the timeline slips.

Score: +1 document improvement, -1 day timeline, -1 worsened (CP2 risk), -1 widened (0/4 → 0/5). Net: **-2 structural deterioration.** The JD is better; the hiring is not.

---

## Step 8: Process Self-Assessment

### What this Loop got right:
- Identified the document-perfectionism-as-procrastination pattern — this is a new insight. The practice's "decisions without execution" pattern has a sub-pattern: the artifact is continuously improved to defer the action. The improvement is genuine, but the function is delay.
- Flagged the salary band vs scope mismatch with market data — this is a practical issue that will affect candidate quality and was not addressed in the JD review.
- Proposed the external posting version (2 pages) vs internal reference (19 sections) split — this resolves the tension between operational detail and candidate accessibility.
- Routed the interim plan through Hadri instead of DAF — this addresses the accountability gap that the PM role itself cannot solve (the PM tracks, but who enforces before the PM exists?).

### What this Loop might have wrong:
- The "document perfectionism as procrastination" framing may be unfair. DAF may have been planning to approve and post today, and the v3.0 expansion request was a genuine refinement before a final review. The 5-minute turnaround between v2.1 and v3.0 request suggests DAF was actively engaged with the document, not avoiding it.
- The salary market data (RM 10-18K) is an estimate. The actual KL market for cybersecurity PMs in Sep 2026 may differ. DAF has hiring experience and market knowledge that this Loop does not.
- The interim-to-Hadri proposal (Action 3) adds formal authority to someone who is already COO. If Hadri was going to do these things, he would already be doing them. The issue may not be authority but capacity — Hadri is also triple-loaded (COO, architecture, CyberDSA coordination). Adding "Acting PM" may not change behaviour; it may just add a title.
- The "0/5" widening framing treats the JD v3.0 as another decision without execution. This is arguably wrong — the JD is a draft artifact, not a decision. The decision is to approve and post. That decision has not been made, but the JD's existence is not itself a failure. The framing conflates artifact production with decision-making.

### Recurring patterns across reviews:
- **"Decisions without execution" — 6th consecutive review.** Now visible in the JD process itself: the JD is produced, refined, expanded — but not posted. The pattern is meta: the practice's approach to solving the "decisions without execution" gap is to produce more artifacts about it.
- **"Artifact quality is not the binding constraint" — 2nd review.** INT-20260904-006 identified that "the practice knows exactly what needs to happen. The question is whether it will." This Loop confirms: the JD v3.0 is an excellent artifact. The binding constraint is DAF's approval to post, not the JD's content.
- **"Interim plan degrading" — 2nd review.** Every week without the PM, the interim plan absorbs more capacity. The plan was designed as a stopgap, not a substitute. It is now in its 3rd week of operation as the de facto PM model.

### Honest Assessment

The JD v3.0 is genuinely better than v2. The operational detail — cadences, escalation protocols, POC lifecycle, templates — will serve the PM well once they're in seat. The expansion was worth doing.

But the expansion took time that could have been spent posting v2.1. The marginal value of v3.0 over v2.1 — for the purpose of attracting candidates — is near zero. No candidate will see the escalation protocol or the POC project plan template at the posting stage. The value of v3.0 is internal: it defines how the practice should operate. That value is real, but it is not urgent. The posting is urgent.

The honest read: DAF engaged with the JD deeply today (3 versions in one session). That engagement is positive — it shows ownership of the role design. But engagement with the document is not the same as action on the hiring. The practice is 4 days behind on posting. Every additional day of refinement without posting widens the gap.

**What matters now, in priority order:**
1. Approve and post (today)
2. Decide salary band (before posting)
3. Assign interim PM authority to Hadri (this week)
4. Prepare Hadri + DAF calendar blocks for Sep 22-26 interviews (this week)
5. Begin shortlisting as CVs arrive (next week)

The JD is ready. The question is the same one from INT-20260904-006: will the artifact convert to action?

**CVS Status:** All claims T3 [ASSESSMENT] based on L2 evidence (JD versions, commit history, ESF-001, TBH Registry, INT-20260904-006). Confidence 7/10 (Rule 6 cap). The salary market claim (RM 10-18K) is T4 [ASSUMPTION] — unverified market estimate, not a sourced data point. DAF should validate before relying on it.

---

*This Cognitive Loop is the second Loop today. It does not replace INT-20260904-006 — it supplements it by focusing on TBH-001 as the structural lever. INT-20260904-006 identified the mobilisation gap; this Loop identifies that the same gap is now visible in the hiring process for the role designed to close it.*

*This Loop's value is determined by whether the JD receives management approval by end of October 2026, and whether the interim plan is formally strengthened to sustain 14-16 weeks.*

*Original Loop text preserved for audit trail. Correction applied Sep 4, 13:45 UTC per DAF clarification on document purpose and timeline.*
