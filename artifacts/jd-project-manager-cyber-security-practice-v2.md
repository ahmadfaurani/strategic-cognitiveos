---
id: ART-20260828-003
record_type: artifact
title: "Job Description — Project Manager, Cyber Security Practice (v3.1)"
created_at: 2026-08-28T09:36:00+00:00
updated_at: 2026-09-04T13:15:00+00:00
owner: faurani-jaafar
status: draft
priority: critical
sensitivity: internal
lifecycle_state: candidate
confidence: high
tags:
  - domain/organisational-capability
  - domain/organisational-design
  - domain/cybersecurity-productisation
  - domain/portfolio-governance
  - type/job-description
  - type/reference-document
source:
  type: direct
  reference: "DAF directive 2026-08-28 (detailed JD for review); supersedes v1 (INIT-20260820-004)"
summary: "Revised JD for TBH-001 — Project Manager, Cyber Security Practice. v3.1 confirms salary band RM 10-15K, reframes document as internal management justification (not external posting), adjusts timeline for end-October approval target. Start date shifts to Jan 2027."
strategic_significance: "Resolves the primary execution scalability bottleneck — DAF carrying PM coordination by default. Enables concurrent POC delivery, disciplined document production, and frees DAF for strategic direction and stakeholder relationships."
mission_alignment:
  - cybersecurity-productisation
  - organisational-capability
  - portfolio-governance
related_records:
  - GOV-TBH-REGISTRY-001
  - INIT-20260820-004
  - INIT-20260804-001
  - INIT-20260820-003
  - RSK-20260824-003
  - RSK-20260823-001
  - RSK-20260827-002-bursa-poc-risk-register
  - INT-20260827-003-bursa-poc-cognitive-loop-analysis
  - ACT-20260828-001
  - ACT-20260827-001
  - ACT-20260827-002
---

# Job Description — Project Manager, Cyber Security Practice

**Role Title:** Project Manager — Cyber Security Practice
**Department:** Cyber Security Practice
**Reports To:** Hadri (Practice COO)
**Matrix Reporting:** DAF (Director — Cyber Security Practice) for strategic priorities and initiative alignment
**Location:** Level 30, Menara TM, KL (hybrid)
**Employment Type:** Full-time
**TBH Reference:** TBH-001 (CRITICAL)
**Initiative:** INIT-20260804-001 / INIT-20260820-003
**Version:** v3.1 (Revised 2026-09-04 — salary band confirmed RM 10-15K, document reframed as internal management justification, timeline adjusted for end-October approval target)
**Supersedes:** v3.0 (2026-09-04), v2.1 (2026-09-04), v2 (2026-08-28), v1 (2026-08-20)
**Document Purpose:** Internal justification for management approval. Not for external posting. Upon management approval, a condensed external posting version will be generated.

---

## 1. Purpose

Own the execution coordination of cybersecurity practice deliverables — POC documents, technical briefs, client-facing project artefacts, and delivery tracking — ensuring they are produced on schedule, to quality, and with the right contributors.

This role exists to take project execution coordination off DAF's plate and embed it structurally under the Practice COO. Without this role, DAF carries PM duties by default, creating the exact execution scalability bottleneck the TBH Registry was designed to surface (RSK-20260824-003: DAF carrying 4 concurrent interim roles for Bursa POC alone).

**This is not a GTM programme coordination role.** The GTM Delivery Owner coordinates the go-to-market campaign (sales, marketing, pipeline). This role coordinates the **delivery side** — POC documents, technical deliverables, implementation plans, and client-facing project artefacts produced by the Practice.

**What "execution coordination" means in practice:**
- Every deliverable has a named owner, a deadline, a status, and a version — always
- No deliverable sits idle for >48 hours without the PM knowing why
- No gate slips without DAF and Hadri being notified 72 hours before the deadline
- No weekly status report is missed — it is a non-negotiable deliverable, not an ad-hoc task
- No POC engagement starts without a project plan; no POC engagement ends without a lessons-learned capture

---

## 2. Organisational Context

### Practice Structure

| Role | Name | Responsibility | PM Interaction |
|------|------|---------------|----------------|
| Director — Cyber Security Practice | DAF (Faurani Jaafar) | Strategic direction, commercial owner, stakeholder relationships, final approver | Matrix reporting line. DAF sets priorities and approves deliverables. PM does not report day-to-day operations to DAF — that goes through Hadri. PM escalates to DAF only when Hadri cannot resolve or when commercial/strategic decisions are needed. |
| Practice COO | Hadri | Technical delivery capability, operational command, line manager for this role | **Direct line manager.** Day-to-day operations, resource allocation, technical content coordination, performance management. PM's primary escalation point for resource conflicts, scheduling conflicts, and contributor accountability. |
| Practice Technical Authority | Fuad | Product ownership (VoronCitadel, GovSec TIP, chain:SENTRY), technical review | Technical reviewer on all POC documents. PM coordinates review cycle with Fuad: sends draft → tracks review SLA → follows up if overdue → routes to DAF for approval after Fuad sign-off. PM does not dictate technical content — PM tracks that technical content is produced on time and to quality. |
| POC Engineer | Syahir (TBH) | Technical environment provisioning and POC delivery | PM coordinates environment readiness with Syahir: confirms provisioning timeline, tracks deployment status, flags environment blockers to Fuad. PM ensures Syahir's capacity is not over-committed across concurrent POCs. |
| SSE Lead | Amelia Nadia | Stakeholder engagement alignment for POC clients | PM coordinates with Amelia on client-side readiness: stakeholder availability, scheduling, communication protocols. PM does not own the stakeholder relationship — Amelia does. PM ensures stakeholder-dependent tasks are tracked. |
| CSM Coordinator | Aishah | MQL Receiver — initial contact qualification in CSM | PM coordinates on CSM-channel workflow: POC-related inbound requests, scheduling with CSM counterparts, document routing through the CSM chain. PM tracks CSM-side dependencies and flags delays. |

### Products (Dev Freeze Aug 11)

| Product | Status | POC Readiness | PM Role |
|---------|--------|---------------|---------|
| **VoronCitadel** | POC-ready, Bursa Malaysia focus | 19 section files, 17 requirements (ITSS §10.1-10.4), 3 use cases, 6 test scenarios, 12 acceptance criteria. 76% Native coverage. Retail RM368k, early-adopter RM168k | **Active POC coordination.** Track all 19 sections, coordinate review cycle, manage Bursa POC project plan, maintain risk register. |
| **GovSec-TIP** | Strategic sovereign platform, dev freeze | Gate 4 technical co-branding. Layer 1 CONDITIONAL, Layer 2 CRITICAL GAP (10 missing), Layer 3 STRONG | **CyberDSA demo readiness tracking.** Track B-track gate chain (B1-B5), coordinate engineering closure, support brand narrative timeline. |
| **chain:SENTRY** | Phase 0 hardening | 69% implemented, 47% deployed. 3 Critical Phase 0 blockers | **Gate tracking only.** Track C-track gates, flag credential rotation status, surface blockers to DAF/Hadri. No engineering coordination — that's Hadri/Syahir. |

### Key Partnerships

- **CSM × Aras:** MOU signed. Co-branding confirmed (DEC-20260821-006) for all 3 products. GovSec primary proof point. 7-stakeholder chain: Roshdi → Azrul → Zulfeka → Bala → Wan Roshaimi → Zaharudin → Dr. Megat. **PM role:** Track CSM-side dependencies in the gate chain. Flag when CSM-side owners are unresponsive. Do NOT engage CSM executives directly — that's DAF's lane.
- **Bursa Malaysia:** VoronCitadel POC anchored on ITSS §10 Supplier Management (existing binding law, Directive 5.05-001). RSWG §2.6 TSP Oversight = forward enhancement path. NDA Framework sent to Azrul Aug 28 (4 IP provisions under review). **PM role:** Track NDA status, flag IP provision delays, maintain POC project plan with Bursa timeline.
- **Teras AI Platform:** Farul's 5-layer internal infrastructure layer. VoronCitadel deploys ON Teras. POC timeline 2-3 weeks (was 2-3 months). **PM role:** Track Teras dependency in POC project plan. Coordinate with Fuad/Syahir on Teras readiness.

---

## 3. Key Responsibilities

### 3.1 Bursa POC Document Execution (Immediate — ACTIVE)

The Bursa POC is the priority engagement. 19 section files are live on github.com/ahmadfaurani/bursa-poc, covering 17 requirements across ITSS §10.1-10.4, 3 use cases, 6 test scenarios, and 12 acceptance criteria.

**Document Coordination — Operational Procedure:**

1. **Section Tracker Maintenance:** Maintain a live tracker (GitHub Issues or project board) for all 19 sections with the following fields per section:
   - Section number and title
   - Content owner (author)
   - Reviewer (Fuad for technical, DAF for strategic)
   - Current state: Draft → In Review → Approved → Final
   - Deadline (working days from assignment)
   - Last updated date
   - Blockers (named, with owner and target resolution date)
   - Version/commit hash

2. **Review Cycle Coordination:**
   - When a section is ready for review: create a PR on the bursa-poc repo, assign Fuad as reviewer, set review SLA of 2 working days
   - Track review SLA: if not reviewed within 2 working days, send a reminder to Fuad via the agreed channel (Telegram or Slack). If not reviewed within 3 working days, escalate to Hadri.
   - After Fuad sign-off: route to DAF for final approval. DAF approval SLA: 1 working day. If not approved within 2 working days, remind DAF via Telegram.
   - After DAF approval: merge PR, update tracker to "Final", log the commit hash.

3. **Version Control:**
   - All POC document changes go through PRs — no direct commits to main
   - PR title format: `[Section X.Y] <brief description> — <author>`
   - PR description must include: what changed, why, which requirement it addresses, reviewer assigned
   - Merge only after review + approval. Squash-merge to keep history clean.

4. **NDA & Legal Coordination:**
   - Track NDA Framework review status with Azrul/CSM (ACT-20260828-001)
   - Maintain NDA status in POC project plan: current state, owner, deadline, next action
   - Flag any IP provision negotiation delays that compress the 6-8 week competitive window
   - If NDA is delayed >5 working days beyond deadline, escalate to DAF immediately — this is a commercial blocker, not a coordination issue

5. **Risk Tracking — POC Risk Register:**
   - Maintain Bursa POC Risk Register (RSK-20260827-002 — 17 risks, 6 categories)
   - Review the risk register every Monday during the weekly status check
   - For each risk: assess current probability and impact, update status, identify if any risk has materialised or new risks have emerged
   - Top risks to monitor actively:
     - B-STR-01: Compliance window — if RSWG alignment slips, POC loses regulatory anchor
     - B-OPS-01: CSM chain dependency — any stakeholder in the 7-person chain going dark blocks the gate
     - B-OPS-02: DAF single coordinator — this risk should reduce as PM takes over coordination
     - B-TEC-01: Test case gaps — incomplete test cases invalidate acceptance criteria
   - Escalation: any risk that moves from "Likely" to "Occurring" → immediate notification to Hadri and DAF via Telegram, not waiting for the weekly report

### 3.2 POC Execution Coordination (Ongoing)

For each POC engagement through the CSM channel, the PM owns the following lifecycle:

**POC Engagement Lifecycle:**

```
Intake → Planning → Environment Readiness → Document Production → Review & Approval → Execution → Handoff → Lessons Learned
```

**Phase 1 — Intake (Day 0):**
- Trigger: Aishah (CSM MQL Receiver) qualifies an inbound request or DAF directs a POC engagement
- PM action: Create a POC project plan from the approved template (see §3.4)
- PM action: Schedule a kick-off meeting with the delivery team (Hadri, Fuad, Syahir, Amelia) within 3 working days of intake
- PM output: POC project plan v1 (scope, stakeholders, timeline, risks, success criteria)

**Phase 2 — Planning (Week 1):**
- PM action: Work with Hadri to define technical scope and architecture sections
- PM action: Work with Fuad to define product capability mapping and test scenarios
- PM action: Work with Syahir to confirm environment provisioning timeline
- PM action: Work with Amelia to confirm client-side stakeholder availability and engagement protocol
- PM output: POC project plan v2 (final, approved by Hadri + DAF)
- PM action: Create section tracker from template, assign owners and deadlines

**Phase 3 — Environment Readiness (Week 1-2):**
- PM action: Track Syahir's environment provisioning against the agreed timeline
- PM action: Confirm data loaded, integration scoped, test accounts provisioned
- PM action: Flag environment blockers to Fuad within 24 hours of identification
- PM output: Environment readiness checklist signed off by Syahir + Fuad

**Phase 4 — Document Production (Week 2-4):**
- PM action: Run the review cycle coordination procedure (see §3.1)
- PM action: Hold bi-weekly (2x per week) 15-minute standups with the delivery team: what's done, what's in progress, what's blocked
- PM action: Update the section tracker daily during production phase
- PM output: All sections at "Final" state in the tracker

**Phase 5 — Review & Approval (Week 4-5):**
- PM action: Coordinate Fuad's technical review of the complete document (not section-by-section)
- PM action: Coordinate DAF's final approval
- PM action: Track review SLA: 2 working days for Fuad, 1 working day for DAF
- PM output: Approved POC document, committed to repo, version tagged

**Phase 6 — Execution (Week 5-6):**
- PM action: Coordinate POC execution schedule with client (via Amelia)
- PM action: Track execution milestones against the project plan
- PM action: Daily status updates to DAF and Hadri during execution week (not weekly — daily)
- PM output: Execution status log, milestone confirmations

**Phase 7 — Handoff (Week 6-7):**
- PM action: Coordinate handoff to GTM Delivery Owner for commercial transition
- PM action: Ensure all POC artefacts are packaged: document, test results, environment config, stakeholder feedback
- PM action: Schedule handoff meeting with GTM Delivery Owner, DAF, and Hadri
- PM output: Handoff package, meeting minutes, transition checklist signed off

**Phase 8 — Lessons Learned (Week 7):**
- PM action: Schedule lessons-learned session within 5 working days of POC completion
- PM action: Capture: what worked, what didn't, what to improve, template updates needed
- PM action: Update POC project plan template with improvements
- PM output: Lessons-learned document, filed in the repo, shared with delivery team

**Competitive Window Tracking:**
- Monitor the 6-8 week competitive window (INT-20260827-003)
- Flag if POC timeline slips relative to CyberDSA Oct 5-7 reference case deadline
- If timeline slips >5 working days beyond plan, escalate to Hadri with a recovery plan proposal

### 3.3 CyberDSA Engineering Closure Support

Support the 6-step gate chain for GovSec × CMERP engineering document. The table below shows the CURRENT cycle (Sep 2026) as an example. The PM will own FUTURE gate chains for subsequent POC engagements and CyberDSA cycles.

**Current cycle example (CyberDSA Oct 5-7, 2026):**

| Step | T-Minus | Date | Owner | Action | PM Role |
|------|---------|------|-------|--------|---------|
| 1 | T-35 | Aug 31 | Fuad | Complete engineering comment closure | Track status, flag delays |
| 2 | T-35 | Aug 31 | Hadri | Consolidate final document | Coordinate handoff |
| 3 | T-34 | Sep 2 | Fuad | Confirm document technically complete | Verify status, update tracker |
| 4 | T-33 | Sep 3 | Tuan Fatah | Internal technical sign-off (CRITICAL) | Track gate status, escalate if at risk |
| 5 | T-32 | Sep 4 | Hafiz Rahman (CSM) | CSM technical validation | Track CSM-side status |
| 6 | T-30 | Sep 5 | Zaharudin | Sign-off, document baselined | Confirm closure, log milestone |

**Gate chain management protocol:**
- T-7 days before each gate: PM sends a reminder to the gate owner via Telegram/Slack
- T-3 days before each gate: PM sends a status check to the gate owner and escalates to Hadri if the gate is at risk
- T-1 day before each gate: PM sends a final status check. If gate is not on track to close, PM escalates to DAF immediately
- Gate closes: PM logs the closure with evidence (email confirmation, signed document, etc.) and updates the AIP Gate Tracker
- Gate slips: PM documents the slip, the reason, the new target date, and the impact on downstream gates. PM notifies DAF and Hadri within 24 hours.

### 3.4 Deliverable Management & Portfolio Register Ownership

**Portfolio Register:**
- Own and maintain the Practice Portfolio Register as canonical single-source of truth for all programmes (PRG-001+)
- Ensure every programme has: named owner, status (Active/Parked/Killed), kill date, next action, next action owner, next action deadline
- This is ESF-20260829-001 Gate 1 (Sep 30 target) — portfolio register as single-source. The PM is the operational owner of this gate post-hiring
- **Update cadence:** Review and update the register every Monday before the weekly status report. Any programme status change during the week is updated within 24 hours.
- **Kill-date enforcement:** Any programme past its kill date without a renewal decision is flagged in the weekly status report as "OVERDUE — KILL DECISION REQUIRED." PM does not make the kill decision — PM surfaces it for DAF.

**Practice Deliverables Register:**
- Maintain a live register of all in-flight deliverables: what's in production, who owns it, deadline, status, review state
- **Format:** GitHub project board or equivalent, with columns: Backlog → In Progress → In Review → Approved → Delivered
- **WIP limit:** No more than 5 deliverables in "In Progress" at any time. If more are needed, escalate to Hadri for prioritisation.

**WIP Protocol — Document Intake:**
Every new document enters the register with the following fields at intake:
1. **Title** — what is it
2. **Creation owner** — who writes it
3. **Audience** — who is it for (internal/client-facing)
4. **Importance** — Strategic / Operational / Tactical
5. **TAT** — 7 working days total (3 creation + 2 QC + 1 approval + 1 buffer)
6. **Execution map** — Creation → QC (Fuad) → Approval (DAF) → Execution (delivery)
7. **Dependencies** — what blocks this, what does this block
8. **Deadline** — working backwards from the external deadline it serves

**4-Role Execution Map:**
Every deliverable moves through 4 roles:
```
Creator (writes) → Reviewer (QC, Fuad) → Approver (DAF) → Executor (delivers)
```
- PM is none of these 4 roles. PM is the **coordinator** who ensures each role fires on time.
- PM tracks handoff between roles: if the Creator misses their deadline, PM flags it to Hadri within 24 hours.
- If the Reviewer (Fuad) misses SLA, PM escalates to Hadri within 48 hours.
- If the Approver (DAF) misses SLA, PM sends a reminder via Telegram. If no response in 48 hours, PM escalates to Hadri.

**ESF Alignment:**
- Track ESF-001 Gate 1 (portfolio register single-source, Sep 30) and ESF-002 Gate 4 (GovSec Q3-Q4 roadmap, Jan 31) dependencies
- Surface risks to DAF if gates are at risk of slipping — 2 weeks before the deadline, not 2 days

### 3.5 Cross-Functional Coordination & Status Reporting

**Coordination responsibilities:**
- Primary operational liaison between Practice (Hadri), Product (Fuad), and Director (DAF) for deliverable production
- Coordinate with GTM Delivery Owner on POC-to-commercial transition
- Work with POC Engineer to ensure technical environment readiness aligns with document timeline
- Coordinate with Aishah (CSM MQL Receiver) on POC-related CSM workflow items
- Flag resource conflicts to Hadri (COO) before they become blockers — "before" means at the weekly status check, not after the deadline has passed

**Weekly Status Report — Format & Protocol:**

**Distribute every Monday by 10:00 AM MYT to DAF and Hadri.** This is a non-negotiable deliverable obligation.

**Template:**
```
Subject: Weekly Status Report — Week of <date>

1. SUMMARY (3-5 lines)
   - Overall status: On Track / At Risk / Slipping
   - Key achievement this week
   - Key risk this week

2. ACTIVE POCs
   For each active POC:
   - POC name, client, phase, status
   - Sections completed / in progress / blocked
   - Next milestone and date
   - Risks (if any escalated)

3. DELIVERABLES REGISTER
   - Deliverables in progress (owner, deadline, status)
   - Deliverables in review (reviewer, SLA status)
   - Deliverables blocked (blocker, owner, target resolution)

4. GATE TRACKER SUMMARY
   - Gates passed this week
   - Gates approaching (next 72 hours)
   - Gates overdue (with reason and action)

5. RISKS ESCALATED
   - New risks identified
   - Existing risks that changed status
   - Risks requiring DAF or Hadri decision

6. DECISIONS NEEDED
   - List of decisions needed from DAF or Hadri, with deadline
   - Format: [DECISION] <description> — needed by <date> — context <1-2 lines>

7. UPCOMING DEADLINES (next 2 weeks)
   - Date, deliverable, owner
```

**Distribution:** Telegram (primary), email (if requested by DAF or Hadri). Posted to the CognitiveOS repo as an artifact.

### 3.6 Quality & Standards

- Ensure all POC documents follow the approved section structure (per DEC-20260820-004) or equivalent approved templates
- Ensure claims in client-facing documents pass claims review (CVS Master Framework) before external distribution
- Maintain version control and document history for all practice deliverables
- Capture lessons learned from each POC engagement: what worked, what didn't, what to improve

**Claims Review Protocol:**
- Before any client-facing document is sent externally, PM confirms that all factual claims have been verified per the CVS Master Framework (03-VERIFICATION/CVS-FRAMEWORK.md)
- PM is NOT the claims validator — PM ensures the validation step has happened
- If a claim has not been validated, PM holds the document and routes it back to the author for validation
- Only claims tagged as T1 (Confirmed) or T2 (Source-Backed) are cleared for external distribution

**Version Control Standards:**
- All practice deliverables live in GitHub repos
- Commit message format: `[<deliverable-id>] <description> — <author>`
- Version tags for major milestones: v1.0 (draft complete), v1.1 (reviewed), v2.0 (approved), v3.0 (client-facing)
- No direct commits to main — all changes through PRs

---

## 4. Operating Cadence

### 4.1 Daily

| Time | Activity | Duration | With |
|------|----------|----------|------|
| 09:00 MYT | Review overnight messages, flag urgent items | 15 min | Solo |
| 09:15 MYT | Update section tracker — what moved overnight, what's blocked | 15 min | Solo |
| 09:30 MYT | Clear blockers — chase any overdue items from yesterday | 30 min | As needed |

### 4.2 Weekly

| Day | Time | Activity | Duration | With |
|-----|------|----------|----------|------|
| Monday | 09:00 MYT | Produce and distribute Weekly Status Report | 60 min | DAF + Hadri (recipients) |
| Monday | 11:00 MYT | Weekly status check with delivery team | 30 min | Hadri, Fuad, Syahir, Amelia (as needed) |
| Wednesday | 10:00 MYT | Mid-week blocker check — 15-min standup | 15 min | Delivery team |
| Friday | 16:00 MYT | Week wrap-up — update all trackers, plan next week | 30 min | Solo |

**Weekly Status Check Agenda (Monday 11:00 MYT, 30 min):**
1. (5 min) Review last week's action items — what's done, what's carried over
2. (10 min) POC status — each active POC: progress, blockers, next milestone
3. (5 min) Risk register — any new risks, any status changes
4. (5 min) Gate tracker — upcoming gates in the next 2 weeks
5. (5 min) Decisions needed — anything requiring Hadri or DAF decision

**Mid-Week Blocker Check (Wednesday 10:00 MYT, 15 min):**
- Async or in-person. Focus: what's stuck, who needs help, what's at risk of slipping by Friday
- If nothing is blocked, cancel and use the time for document work

### 4.3 Monthly

| Activity | When | Duration | With |
|----------|------|----------|------|
| Portfolio Register review | First Monday of each month | 60 min | DAF + Hadri |
| Lessons-learned review | After each POC completion | 60 min | Delivery team |
| Risk register deep review | First Monday of each month | 30 min | Hadri |
| POC project plan template update | After each POC completion | 30 min | Solo |
| Deliverables register cleanup | First Monday of each month | 30 min | Solo |

### 4.4 Event-Driven

| Trigger | Action | Timeline |
|---------|--------|----------|
| New POC engagement intake | Create project plan, schedule kick-off | Within 3 working days |
| Gate approaching (T-7) | Send reminder to gate owner | T-7 days |
| Gate at risk (T-3) | Escalate to Hadri | T-3 days |
| Gate slipping (T-1) | Escalate to DAF | T-1 day |
| Risk materialising | Notify Hadri + DAF immediately | Within 24 hours |
| Deliverable blocked >48 hours | Flag to Hadri with reason and proposed action | Within 48 hours |
| Contributor unresponsive >3 working days | Escalate to Hadri | After 3 working days |
| NDA/legal delay >5 working days | Escalate to DAF (commercial blocker) | After 5 working days |

---

## 5. Escalation Protocol

### 5.1 Escalation Paths

```
Level 0: PM resolves directly (routine coordination)
    ↓ (if unresolved in 48 hours)
Level 1: Escalate to Hadri (resource conflicts, contributor accountability, scheduling)
    ↓ (if Hadri cannot resolve in 48 hours, or if issue is commercial/strategic)
Level 2: Escalate to DAF (commercial decisions, strategic priorities, stakeholder escalation)
    ↓ (if DAF decision needed and DAF unavailable)
Level 3: DAF delegates to Hadri with PM tracking (interim)
```

### 5.2 Escalation Format

All escalations follow this format (sent via Telegram or Slack):

```
🚨 ESCALATION — <level> — <date>

Issue: <1-2 line description>
Impact: <what happens if not resolved>
Owner: <who needs to act>
Requested action: <specific ask>
Deadline: <when this needs resolution by>
Context: <link to tracker, document, or relevant artifact>
```

### 5.3 What NOT to Escalate

- Routine review reminders (PM handles directly)
- Minor scheduling adjustments (PM handles directly)
- Formatting/editing issues (PM handles directly)
- Contributor availability within normal working hours (PM coordinates directly)

**Rule:** If the PM can resolve it by coordinating, the PM resolves it. If it requires authority the PM doesn't have, escalate. When in doubt, resolve first, escalate if unresolved in 48 hours.

---

## 6. Tooling & Communication Channels

### 6.1 Tooling Stack

| Tool | Purpose | PM Usage |
|------|---------|----------|
| **GitHub** (github.com/ahmadfaurani/bursa-poc, CognitiveOS repo) | Document repos, issue tracking, project boards | PR management, section tracker, deliverables register, version control |
| **Telegram** | Primary communication with DAF, Hadri, delivery team | Status report distribution, escalations, quick coordination, gate reminders |
| **Slack** (if available) | Team communication | Standups, mid-week checks, async coordination |
| **OpenClaw / Ember** | AI agent support | Drafting support, risk register maintenance, deadline tracking, document authoring assistance |
| **Google Calendar** | Scheduling | Meeting scheduling, deadline tracking, shared calendar with delivery team |
| **Email** | Formal external communication | NDA tracking, formal correspondence with CSM/Bursa (but DAF sends, PM tracks) |

### 6.2 Communication Norms

| Channel | Use For | Response Expectation |
|---------|---------|----------------------|
| Telegram (DAF) | Status reports, escalations, decisions needed | DAF responds within 24 hours (working days) |
| Telegram (Hadri) | Day-to-day coordination, resource conflicts | Hadri responds within 12 hours (working days) |
| Telegram (Fuad) | Review reminders, technical query routing | Fuad responds within 24 hours (working days) |
| Telegram (Syahir) | Environment status, provisioning tracking | Syahir responds within 24 hours (working days) |
| GitHub PRs | Document review, technical feedback | Reviewer responds within 2 working days |
| Email (external) | Formal correspondence | PM tracks, DAF sends externally |

### 6.3 Meeting Protocols

**All meetings the PM convenes:**
- Agenda circulated 24 hours in advance (or at the start of the meeting for standups)
- Minutes produced within 24 hours after the meeting
- Action items logged in the deliverables register with owner and deadline
- Action items reviewed at the next meeting

**Meeting cadence (minimum):**
- Weekly status check (Monday 11:00 MYT, 30 min) — delivery team
- Mid-week blocker check (Wednesday 10:00 MYT, 15 min) — delivery team
- POC kick-off (within 3 working days of intake) — delivery team + Amelia
- Gate review (as needed, T-7 before each gate) — gate owner
- Lessons learned (within 5 working days of POC completion) — delivery team

---

## 7. Requirements

### Essential

- 3–5 years project management experience in cybersecurity, GRC, technology consulting, or regulated industry
- Demonstrable experience coordinating technical document production across multiple contributors with competing priorities
- Strong understanding of project delivery fundamentals: scope management, milestone tracking, dependency mapping, risk logging, status reporting
- Ability to sit between technical contributors (Hadri, Fuad) and strategic approvers (DAF) without losing fidelity in either direction
- Malaysian regulatory awareness — familiarity with RMiT, SC GTRM, PDPA, BNM guidelines, and Bursa Malaysia ITSS (enough to understand document context, not to author technical content)
- Strong documentation discipline — every deliverable has an owner, deadline, status, and version
- Comfortable holding contributors accountable without having authority over them (matrix coordination)
- Excellent written communication — can produce clear status reports, project plans, and meeting minutes
- Proactive escalation instinct — surfaces risks before they become blockers, doesn't wait to be asked

### Desirable

- PMP, PRINCE2, or equivalent project management certification
- Experience with GRC, compliance, or RegTech platform delivery
- Experience coordinating POC or pilot engagements in enterprise/B2B context
- Cybersecurity domain knowledge — understands what a POC document needs to contain even if not authoring technical sections
- Experience working in a matrix organisation with COO/Director reporting lines
- Familiarity with the CSM partnership model and institutional sales motion
- Experience with TPRM (Third-Party Risk Management) or supplier risk management frameworks
- Git/GitHub familiarity — can manage document repos, track issues, coordinate PRs

---

## 8. Success Metrics (First 90 Days)

### Phase 1: Immediate (Week 1 — First 5 Working Days)

| Metric | Target | Source |
|--------|--------|--------|
| Bursa POC document status tracker | Operational — all 19 sections tracked with owner, deadline, review state | ACT-20260827-002 |
| Capability mapping (ITSS × RSWG × VoronCitadel) | Complete and approved | ACT-20260827-001 |
| POC document updated with RSWG alignment | Complete | ACT-20260827-002 |
| POC document ready for Fuad validation | Per gate chain | Gate chain step 3 |
| Practice deliverables register | Established — all in-flight deliverables visible | JD §3.4 |
| NDA Framework review status | Tracked, Azrul response monitored | ACT-20260828-001 |
| Weekly status report | First report produced and distributed | JD §3.5 |
| Tooling access | GitHub, Telegram, OpenClaw/Ember, calendar — all operational | JD §6 |

### Phase 2: Short-Term (30 Days)

| Metric | Target |
|--------|--------|
| POC project plan template | Created and approved by Hadri + DAF |
| Weekly POC status check cadence | Established with delivery team — no missed weeks |
| Document review cycle | Formalised: author → reviewer → approver → final, with SLA per stage |
| WIP Protocol | Embedded: every new document gets creation owner, audience, TAT, and execution map at intake |
| Bursa POC completion | POC finalised, ready for CyberDSA reference case |
| CyberDSA engineering gate chain | Tracked through closure |
| Portfolio register | Updated and reconciled — all programmes have owner, status, kill date |
| Mid-week blocker check | Running consistently — cancelled only when nothing is blocked |
| Escalation protocol | Active — at least 1 escalation resolved through the protocol |

### Phase 3: Medium-Term (90 Days)

| Metric | Target |
|--------|--------|
| POC engagements coordinated end-to-end | At least 2 with documented status reporting |
| Deliverables without named owner and deadline | Zero |
| POC-to-commercial handoff process | Documented and tested with GTM Delivery Owner |
| Lessons learned | Captured from each POC, fed back into template improvements |
| DAF PM coordination load | Reduced by at least 70% — DAF reviews and approves, does not chase or coordinate |
| Risk register maintenance | Active for all POC engagements, reviewed weekly |
| Kill-date enforcement | 100% — no programme past kill date without a DAF decision logged |
| Weekly status report on-time rate | ≥95% — no more than 1 missed/late report per quarter |
| Gate tracker accuracy | 100% — every gate closure backed by evidence, every slip documented |

---

## 9. Working Relationships

### Internal

| Person | Role in POC Delivery | PM Interaction Cadence |
|--------|---------------------|----------------------|
| **Hadri** (Practice COO — line manager) | Technical content owner (architecture); escalation point for resource conflicts; line manager | Daily (Telegram), weekly (status check), monthly (1:1 performance review) |
| **DAF** (Director — matrix) | Strategic content owner; final approver; sets priorities | Weekly (status report via Telegram), ad-hoc (escalations, decisions needed) |
| **Fuad** (Product Owner / Technical Authority) | Product capability input; POC environment owner via POC Engineer; technical review | Weekly (status check), per-PR (review cycle), ad-hoc (technical blockers) |
| **Syahir** (POC Engineer) | Technical environment provisioning and POC delivery | Weekly (status check), bi-weekly (environment readiness), ad-hoc (blockers) |
| **Amelia Nadia** (SSE Lead) | Stakeholder engagement alignment for POC clients | Weekly (status check), per-POC (kick-off, stakeholder scheduling) |
| **Aishah** (CSM MQL Receiver) | Initial contact qualification, CSM-side workflow coordination | Per-POC (intake, CSM-chain tracking), ad-hoc (inbound requests) |
| **GTM Delivery Owner** (TBH) | POC-to-commercial transition coordination; GTM pipeline alignment | Per-POC (handoff), quarterly (pipeline alignment) |
| **Ember** (AI agent — OpenClaw) | Document authoring support; technical writing; risk register maintenance; deadline tracking | Daily (drafting, tracker updates, deadline flags) |

### External

| Counterpart | Role | PM Interaction |
|-------------|------|----------------|
| CSM counterparts (Azrul, Zulfeka, Bala, Wan Roshaimi, Zaharudin, Hafiz Rahman) | POC coordination for joint accounts; technical validation; operational enablement | Gate-chain tracking only. PM does NOT contact CSM executives directly — DAF owns Gates 0-6. PM tracks CSM-side dependencies and flags delays. |
| POC client teams | POC status communication (operational level) | Via Amelia. PM does not own the client relationship. |
| Bursa Malaysia stakeholders | POC engagement coordination (via CSM channel) | Via CSM chain. PM tracks Bursa-side dependencies in the project plan. |

---

## 10. Boundary Exclusions

This role does **not**:

- Author technical content (Hadri/Fuad/Ember own content creation)
- Own product roadmap or feature decisions (Fuad as Product Owner)
- Own GTM campaign execution (GTM Delivery Owner)
- Own sales relationships (Account Owners)
- Make strategic/commercial decisions on POC terms (DAF)
- Own stakeholder engagement strategy (Amelia Nadia as SSE Lead)
- Execute technical POC environment work (POC Engineer)
- Engage in CSM executive stakeholder management (DAF owns Gates 0-6)
- Make kill decisions on portfolio programmes (DAF decides, PM surfaces)
- Validate claims for CVS compliance (PM ensures the step happened, does not perform validation)
- Negotiate NDA terms (DAF owns, PM tracks)

This role **coordinates execution**. It does not set strategy, own product, or own relationships. The distinction matters: this role makes other people's delivery faster and more reliable by removing coordination friction.

---

## 11. Reporting Line Rationale

**Reports to Hadri (Practice COO):** The role is a headcount under Hadri's organisation. Hadri owns the technical delivery capability and is the COO of the Practice. The PM executes under his operational command.

**Matrix to DAF (Director):** DAF sets strategic priorities, approves deliverables, and defines what the Practice needs to produce. The PM aligns execution to DAF's priorities but does not report to DAF for day-to-day operations — that goes through Hadri.

This separation is deliberate: it prevents DAF from becoming the default coordination point (the current bottleneck, per RSK-20260824-003) and embeds execution discipline structurally within the COO's org.

**Why not report directly to DAF?** Because if the PM reports to DAF, DAF becomes the coordination hub again — every question, every blocker, every scheduling conflict flows to DAF. The PM exists to absorb that flow, not redirect it. Hadri as line manager means operational issues go to Hadri, and only strategic/commercial decisions reach DAF.

---

## 12. Relationship to Existing JDs

| Role | Reports To | Scope | Distinction from TBH-001 |
|------|-----------|-------|--------------------------|
| **TBH-001: PM — Cyber Security Practice** | Hadri (COO) | Practice-level POC document & deliverable execution | Coordinates **what gets produced** and **on what schedule** |
| GTM Delivery Owner | DAF | GTM programme coordination (sales, marketing, pipeline) | Coordinates **go-to-market campaign execution** |
| POC Engineer | Fuad | Technical POC environment & client liaison | Owns **technical delivery** of POC engagements |
| Account Owner | Shuhada | Sales relationship for 5-7 accounts | Owns **client relationship** through POC |
| Marketing Ops Specialist | Azzatullina | CRM, email automation, attribution | Owns **campaign instrumentation** |
| CSM MQL Receiver | Aishah | Initial contact qualification in CSM | Owns **inbound lead qualification and routing** |

TBH-001 is the missing piece: nobody coordinates the **production of practice deliverables**. The GTM Delivery Owner coordinates the campaign. The POC Engineer handles technical environment. But someone needs to ensure the document sections are written, reviewed, approved, and delivered on time. That's TBH-001.

---

## 13. Key Risks This Role Mitigates

| Risk | How TBH-001 Mitigates | Residual Risk After Mitigation |
|------|----------------------|-------------------------------|
| Interim ownership concentration on DAF — 4 concurrent roles | Absorbs PM coordination role, reduces DAF from 4 roles to 2 (strategic + commercial) | DAF still owns strategic + commercial — 2 roles, not 0 |
| TBH-001 case dismissed on methodology | Role justified by structural vacancy, not quantitative claims | None — role exists because there's a gap, not because a metric says so |
| DAF single coordinator for Bursa POC | PM becomes primary coordinator, DAF becomes approver | DAF still approves — but doesn't chase |
| CSM chain dependency | PM tracks CSM-side dependencies, flags delays early | PM cannot force CSM to respond — escalation to DAF for stakeholder pressure |
| Test case gaps | PM tracks test case status, flags incomplete cases before validation gates | PM cannot write test cases — can only ensure they're written on time |

---

## 14. Compensation & Benefits

**Salary Range:** RM 10,000 – RM 15,000/month (commensurate with experience)

**Budget Justification:** The role scope — matrix reporting (COO + Director), POC lifecycle ownership end-to-end, portfolio register governance, multi-stakeholder coordination across 6+ internal and 7+ external parties, gate chain management, and weekly executive reporting — is equivalent to a Senior PM / Programme Manager role. The RM 10-15K band aligns with the KL market for mid-to-senior cybersecurity PMs with 3-5 years experience in GRC/regulated industry. The previous band (RM 8-12K) was below market for the scope described.

**Benefits:**
- EPF, SOCSO, EIS (statutory)
- Medical coverage
- Annual leave (standard Aras Integrasi policy)
- Professional development budget (certification support: PMP, PRINCE2)
- Hybrid work arrangement (office + remote)

**Performance Review:** Quarterly, aligned with Cognitive Loop Review cadence

**Performance criteria (ongoing, post-90 days):**
- Weekly status report on-time rate ≥ 95%
- Gate tracker accuracy = 100% (every closure backed by evidence)
- Kill-date enforcement = 100% (no programme past kill date without DAF decision)
- DAF PM coordination load reduction sustained (DAF reviews, does not chase)
- POC engagements delivered on schedule (≤5 working days slippage per POC without escalation)
- Risk register currency (reviewed weekly, no risk >2 weeks stale)

---

## 15. Hiring Timeline

| Milestone | Target Date | Status |
|-----------|-------------|--------|
| JD v3.1 finalised for management review | Sep 4, 2026 | ✅ This document |
| Management review and approval | End of October 2026 | Pending — this document serves as the justification |
| External posting (LinkedIn, job portals, internal referral) | Nov 1-7, 2026 | Post-approval |
| Shortlisting | Nov 8-14, 2026 | Post-approval |
| First-round interviews | Nov 17-21, 2026 | Post-approval |
| Second-round interviews (Hadri + DAF) | Nov 24-28, 2026 | Post-approval |
| Offer extended | Dec 1-5, 2026 | Post-approval |
| Target start date | Jan 5-19, 2027 | 2-3 weeks notice period |

**Note on timeline:** The previous timeline (Sep posting, Oct start) has been superseded. This document is positioned as an internal management justification with an end-October approval target. The interim delegation plan (§17) must sustain through the approval period (~8 weeks) plus the hiring process (~6-8 weeks). Total interim period: ~14-16 weeks. This is a material extension from the original 2-3 week interim assumption.

---

## 16. Onboarding Ramp (Week 1-2)

The role is complex enough that "day 1 productive" is unrealistic. A structured 2-week onboarding ramp:

**Week 1 — Context Loading:**

| Day | Activity | With | Output |
|-----|----------|------|--------|
| Day 1 | Briefing: Strategic context, portfolio overview, CSM partnership, 3 products, key partnerships | DAF (90 min) | Notes, initial questions list |
| Day 2 | Briefing: Technical delivery capability, current POC status, team dynamics, operational norms, expectations | Hadri (90 min) | Notes, understanding of line manager expectations |
| Day 3 | Tooling access: GitHub (bursa-poc, CognitiveOS repos), OpenClaw/Ember walkthrough, Telegram channels, calendar setup | Hadri/Fuad/Ember (60 min) | All accounts operational, first PR created (test) |
| Day 4 | Read: Bursa POC document (all 19 sections), Portfolio Register, AIP Gate Tracker, Bursa POC Risk Register | Solo | Understanding of current state, questions list |
| Day 5 | Shadow: DAF on POC coordination calls or meetings. Observe current coordination model. | DAF (as available) | Notes on current pain points, improvement opportunities |

**Week 2 — Shadowed Execution:**

| Day | Activity | With | Output |
|-----|----------|------|--------|
| Day 6 | Co-produce first weekly status report with Ember support. DAF reviews before distribution. | Ember + DAF | Weekly status report v1 (reviewed) |
| Day 7 | Deliver weekly status report. Attend weekly status check. Take notes. | Delivery team | Status report distributed, meeting minutes |
| Day 8 | Take over POC document status tracker. Review all 19 sections, confirm owners and deadlines. | Solo | Updated tracker, current state confirmed |
| Day 9 | Hadri introduces PM to CSM counterparts (operational level). Confirm communication protocols. | Hadri | Contact list, communication norms established |
| Day 10 | First independent weekly status report. DAF reviews but does not edit. PM owns the tracker from this point. | DAF (review only) | Weekly status report v2 (independent) |

**End of Week 2 target:** PM owns status tracking, weekly reporting, and risk register maintenance independently. DAF reviews but does not coordinate. PM has met all internal stakeholders and understands the delivery team dynamics.

**30-day check-in:** Hadri conducts a 30-day performance check-in. Review against Phase 2 metrics. Identify any gaps, provide feedback, adjust priorities.

**90-day review:** DAF + Hadri conduct a 90-day performance review against Phase 3 metrics. Confirm whether the role has achieved the DAF coordination load reduction target.

---

## 17. Interim Delegation Plan (Until TBH-001 Filled)

| Responsibility | Interim Owner | Rationale | Gap Risk |
|----------------|---------------|-----------|----------|
| POC document status tracking | DAF (with Ember support) | Ember maintains trackers and flags deadlines; DAF reviews | Medium — DAF still reviews, not just approves |
| Technical review cycle coordination | Hadri | Already owns technical content; add review cycle management | Low — Hadri has the authority |
| POC environment readiness tracking | Fuad (via Syahir) | Fuad already owns POC environment via POC Engineer | Low — existing process works |
| Stakeholder engagement tracking | Amelia Nadia | SSE Lead already owns stakeholder alignment | Medium — Amelia has overdue items |
| NDA/legal status tracking | DAF | Commercial/legal stays with Director | Low — DAF is engaged |
| Risk register maintenance | Ember (with DAF review) | Ember maintains registers; DAF approves | Low — Ember is operational |
| Weekly status reporting | DAF | Until PM hired, DAF produces (or delegates to Ember for drafting) | High — DAF is the bottleneck |
| Portfolio register maintenance | Ember (with DAF review) | Ember maintains; DAF approves | Medium — register exists but not enforced |
| Kill-date enforcement | Not actively enforced | Requires PM ownership to surface overdue programmes | High — systemic failure (per INT-20260904-004) |

**Interim mitigation:** Ember produces the weekly status report draft (like ART-20260904-002), DAF reviews and approves. This is functioning as a stopgap but is NOT sustainable — Ember cannot chase contributors, attend meetings, or hold people accountable in real-time.

---

## 18. POC Project Plan Template

Every POC engagement starts with a project plan created from this template:

```
POC PROJECT PLAN — <Client Name> — <Product> — <Date>

1. ENGAGEMENT SUMMARY
   - Client: <name>
   - Product: <VoronCitadel / GovSec-TIP / chain:SENTRY>
   - POC scope: <1-2 line description>
   - Target start: <date>
   - Target completion: <date>
   - Competitive window: <if applicable>

2. STAKEHOLDERS
   - Internal: DAF (approver), Hadri (architecture), Fuad (product/review), Syahir (env), Amelia (stakeholder)
   - External: <client-side names and roles>
   - CSM chain: <names if applicable>

3. DELIVERABLES
   | # | Section | Owner | Reviewer | Approver | Deadline | Status |
   |---|---------|-------|---------|---------|----------|--------|
   | 1 | <section> | <author> | Fuad | DAF | <date> | Draft |
   ...

4. ENVIRONMENT READINESS
   - Provisioning owner: Syahir
   - Target ready date: <date>
   - Dependencies: <Teras, data, integrations>
   - Readiness checklist: [ ] Environment provisioned [ ] Data loaded [ ] Test accounts [ ] Integration scoped

5. TIMELINE & MILESTONES
   | Milestone | Date | Owner | Dependencies |
   |-----------|------|-------|--------------|
   | Kick-off | <date> | PM | Stakeholders available |
   | Draft complete | <date> | Authors | Environment ready |
   | Technical review | <date> | Fuad | Draft complete |
   | Final approval | <date> | DAF | Review complete |
   | POC execution | <date> | Syahir/PM | Approval + env ready |
   | Handoff | <date> | PM → GTM | Execution complete |

6. RISKS
   | ID | Risk | Probability | Impact | Mitigation | Owner |
   |----|------|-------------|--------|------------|-------|
   ...

7. NDA / LEGAL STATUS
   - NDA status: <draft/sent/under review/signed>
   - IP provisions: <list any open>
   - Deadline: <date>
   - Owner: DAF

8. SUCCESS CRITERIA
   - <criterion 1>
   - <criterion 2>
   - ...

9. COMPETITIVE WINDOW
   - Window: <6-8 weeks from intake>
   - CyberDSA reference: Oct 5-7, 2026
   - If POC slips >5 working days: escalate with recovery plan
```

---

## 19. Decision Log Protocol

Every decision made during a POC engagement is logged:

**Format:**
```
[DECISION] <date> — <description>
  Context: <why this decision was needed>
  Options considered: <option A, option B, option C>
  Decision: <what was decided>
  Decision maker: <DAF / Hadri / Fuad>
  Rationale: <1-2 lines>
  Impact: <what this affects downstream>
```

**Storage:** Decision log appended to the POC project plan file. For programme-level decisions, logged in the CognitiveOS decisions/ directory with a DEC-YYYYMMDD-NNN ID.

**PM role:** PM does not make decisions. PM ensures decisions are logged when they happen, not reconstructed later.

---

*This role is the execution backbone of the Practice. Without it, the Director carries coordination by default, the COO can't operationalise delivery, and POC documents depend on individual heroics rather than systematic project management. With it, the Practice gains the discipline to deliver concurrently — multiple POCs, multiple documents, multiple clients — without everything flowing through one person.*
