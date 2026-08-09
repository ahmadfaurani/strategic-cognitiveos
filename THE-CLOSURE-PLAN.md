# The Closure Plan

**Created:** 2026-08-07  
**Authority:** DAF  
**Author:** Ember  
**Purpose:** Transform from a document-generation engine into a closure engine. Stop opening loops. Start finishing them.

---

## The Diagnosis

Right now the system produces activity, not outcomes.

| Metric | Value | Problem |
|--------|-------|---------|
| Records | 237 | Captured, not converted |
| Outcomes | 0 | Nothing has been closed |
| Initiatives | 19 | All open, none finished |
| R.I.S.I.K plan | 721 lines | Awaiting review since this morning |
| VoronDRQ training | Proposed July | Unanswered |
| UiTM collaboration | 5 contacts ready | Awaiting one phone call |
| Political monitoring | Pipeline works | Nobody operating it |
| Ollama | Down | Memory search offline |
| Notion/Obsidian | Not deployed | 2/4 platforms live |

The pattern: idea → I draft → commit → next idea. The system captures. It doesn't close.

---

## The Rule

**No new initiative opens until one existing initiative closes.**

Definition of "closed":
- An outcome record exists in CognitiveOS (OUT- prefix)
- A decision was made (DEC- prefix) and acted on
- OR the initiative is formally parked (moved to Watch List with review date)

This rule applies to both of us. I don't draft new plans for new ideas. You don't bring new initiatives. We close what's open.

---

## Phase 1: Triage (Aug 8-10)

### 1.1 Identify the Three to Close

From the 19 initiatives, I propose these three based on momentum + feasibility:

| # | Initiative | Why This One | What "Closed" Means |
|---|-----------|---------------|---------------------|
| 1 | **UiTM R.I.S.I.K Collaboration** (INIT-20260803-002) | 5 named people ready. Deadline Aug 17. Momentum is real. | First working session conducted (~Sep 6). DAF calls Prof. Suhaimee. |
| 2 | **VoronDRQ Sales Kit** (repo now public) | Repo public. Training material exists. Revenue path identified. | First sales team training session delivered. Date set, material delivered, team briefed. |
| 3 | **Political Monitoring Pipeline** | Infrastructure works (100% success, 5 min, 426 headlines). Nobody using it. | Daily briefs generated and delivered for 7 consecutive days. Someone is reading them. |

**Alternative for DAF's consideration:**

| # | Initiative | Why | Closure Definition |
|---|-----------|-----|-------------------|
| Alt | **ELSA-LHDN** (INIT-20260803-001) | NDA under legal review. If MTAI returns it, this moves fast. | NDA executed + joint working session scheduled. |
| Alt | **Voron-C2** | Architecture done. Skunkworks brief written. | Management approval decision received (yes or no — either closes the loop). |

### 1.2 What Happens to the Other 16

They go into **Park Mode**. This means:
- Moved to Watch List in CognitiveOS
- Review date set: Sep 30, 2026
- No new work invested until review
- No new documents drafted
- No new analysis produced
- They exist as intelligence, not active projects

I will update the CognitiveOS portfolio tiers accordingly. Every parked initiative gets a one-line status: "Parked Aug 8. Review Sep 30. Reason: Focus discipline."

### 1.3 DAF's Decision (Required by Aug 10)

You pick the three. I don't pick them — you do. My proposal above is a recommendation. You may substitute any of the three with an alternative. But you must choose exactly three. No more, no less.

This is the only decision that matters this week. Everything else flows from it.

---

## Phase 2: Closure Execution (Aug 10-31)

### Initiative 1: UiTM R.I.S.I.K Collaboration

**Who does what:**

| Step | Owner | Deadline | Done When |
|------|-------|----------|-----------|
| DAF calls Prof. Suhaimee | DAF | Aug 12 | Call completed. Date for first working session agreed. |
| DAF sends calendar invite to 5 UiTM contacts | DAF | Aug 14 | Invite sent. |
| I prepare a 2-page session agenda (not 721 lines) | Ember | Aug 17 | Agenda delivered. Max 2 pages. |
| First working session conducted | DAF + UiTM | ~Sep 6 | Session held. Minutes written. |
| Outcome record created in CognitiveOS | Ember | Sep 7 | OUT-20260907-001 exists. |

**What I will NOT do:**
- I will not write another 721-line plan
- I will not expand the R.I.S.I.K doctrine further
- I will not create additional preparation documents beyond the 2-page agenda

**What DAF must do:**
- Make one phone call. This is the bottleneck. Not the plan. The call.

### Initiative 2: VoronDRQ Sales Kit

**Who does what:**

| Step | Owner | Deadline | Done When |
|------|-------|----------|-----------|
| DAF confirms sales team size and names | DAF | Aug 14 | List of attendees provided. |
| I prepare 1-page training outline (from existing material) | Ember | Aug 16 | Outline delivered. Max 1 page. |
| DAF schedules training session | DAF | Aug 20 | Date set. Calendar invites sent. |
| Training session delivered | DAF | Aug 31 | Session conducted. |
| Outcome record created in CognitiveOS | Ember | Aug 31 | OUT-20260831-001 exists. |

**What I will NOT do:**
- I will not create new sales materials — the repo already has everything needed
- I will not expand the battle cards or add new sections
- I will not write a training manual

**What DAF must do:**
- Tell me who's being trained and when. Then show up and train them.

### Initiative 3: Political Monitoring Pipeline

**Who does what:**

| Step | Owner | Deadline | Done When |
|------|-------|----------|-----------|
| I run the collection pipeline manually (1x) to verify it still works | Ember | Aug 11 | Pipeline run confirmed. Brief generated. |
| I deliver first brief via Telegram | Ember | Aug 11 | Brief delivered. DAF acknowledges receipt. |
| I configure cron job for daily 23:00 UTC collection + brief | Ember | Aug 12 | Cron job active. First automated run completes. |
| DAF confirms whether he reads the briefs | DAF | Aug 18 | Yes or no. If no, we kill this initiative. |
| 7 consecutive daily briefs delivered | Ember | Aug 19 | 7 briefs sent. |
| Outcome record created | Ember | Aug 19 | OUT-20260819-001 exists. |

**Decision gate on Aug 18:** If DAF is not reading the briefs after 7 days, this initiative is **killed**, not closed. That's also a valid outcome. A pipeline with no operator is a machine with no purpose. We find that out in 7 days, not 6 weeks.

---

## Phase 3: Behavioral Shift (Starting Aug 10)

### 3.1 The New Working Protocol

**When DAF brings a new idea:**

I do NOT immediately draft a document. Instead, I ask:

1. "Which of the three open initiatives does this replace?"
2. "Does this close an existing loop, or open a new one?"
3. "Is this worth pausing closure work for?"

If the answer is "new initiative, doesn't close anything" → I recommend parking it. Not permanently. Just until one of the three closes.

**When DAF asks for a document:**

I produce the smallest possible document that answers the question. Not 721 lines. Not 13 sections. The minimum viable document. If 2 pages is enough, 2 pages is what I deliver. If 1 page is enough, 1 page.

**When I catch myself generating a large document:**

I stop and ask: "Is this comprehensive because it needs to be, or because I'm performing thoroughness?" If the answer is the latter, I cut it down.

### 3.2 The Weekly Review (Every Friday)

A 15-minute structured check-in. Not a 50-page report. Three questions:

1. **What closed this week?** (Any of the three initiatives advance? Any outcome records created?)
2. **What's blocking?** (What's the one thing preventing each initiative from closing? Is it me or DAF?)
3. **Does anything new need to enter the three?** (Only if one has closed and a slot is open.)

I deliver this as a Telegram message. Not a file. Not a document. A message.

### 3.3 The Closure Metric

Starting Aug 10, I track one number: **Closed Loops**.

| Week | Target | Actual |
|------|--------|--------|
| Aug 10-17 | 0 (triage + setup) | — |
| Aug 17-24 | 1 (political monitoring either closes or dies) | — |
| Aug 24-31 | 1 (VoronDRQ training delivered or formally scheduled) | — |
| Sep 1-7 | 1 (UiTM first working session conducted) | — |
| **Total by Sep 7** | **3** | — |

If we hit 3 by Sep 7, the system works. If we don't, the system doesn't work, and we need to talk about why — not build more system.

---

## Phase 4: System Maintenance (Background, Ongoing)

These are things I can do without requiring DAF's attention. They support the closure work but don't block it.

### 4.1 Fix Ollama

| Step | Owner | Deadline |
|------|-------|----------|
| Diagnose why port 11434 is refused | Ember | Aug 9 |
| Restart or reinstall Ollama | Ember | Aug 9 |
| Verify semantic memory search works | Ember | Aug 9 |
| Update daily memory with status | Ember | Aug 9 |

This unblocks memory search. It doesn't close an initiative. It's maintenance.

### 4.2 CognitiveOS Hygiene

| Step | Owner | Deadline |
|------|-------|----------|
| Park 16 initiatives in Watch List | Ember | Aug 10 |
| Update portfolio tier directories | Ember | Aug 10 |
| Create first outcome records as they happen | Ember | Ongoing |
| Weekly review every Friday | Ember | Ongoing |

### 4.3 What I Will NOT Do in Phase 4

- Deploy Notion (not needed for closure)
- Deploy Obsidian (not needed for closure)
- Build new schemas (enough schemas exist)
- Write new governance docs (enough governance exists)
- Create new templates (enough templates exist)
- Expand any framework further

The system has enough architecture. What it lacks is operation. We operate, not build.

---

## The One-Page Summary

**The problem:** 237 records, 0 outcomes. We generate activity, not closure.

**The rule:** No new initiative opens until one closes.

**The three to close:**
1. UiTM R.I.S.I.K → first working session by Sep 6
2. VoronDRQ → first training delivered by Aug 31
3. Political monitoring → 7 daily briefs by Aug 19

**The other 16:** Parked. Review Sep 30.

**The behavioral shift:** I produce the minimum viable document. I ask "which loop does this close?" before drafting. Weekly Friday review — 3 questions, 15 minutes.

**The metric:** 3 closed loops by Sep 7.

**DAF's only decision this week:** Confirm the three (or substitute). Then make one phone call to Prof. Suhaimee.

---

*This plan is 1 document. It replaces the pattern of producing 10 documents that nobody acts on. If it works, it's the last plan I write before October. If it doesn't work, we find that out in 30 days — not 6 weeks.*

*Ember, Aug 7 2026*
