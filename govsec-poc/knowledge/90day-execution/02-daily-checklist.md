# KB-90DAY-003: Daily Execution Checklist

**Knowledge Unit ID:** KB-90DAY-003  
**Version:** 1.0  
**Classification:** TLP:AMBER (Internal Operational)  
**Created:** 2026-04-25  
**Owner:** Hadri (Technical Lead)  
**Status:** Active — Daily Execution Guidance  

---

## Purpose

**Provide a standardized daily checklist for all team members to ensure consistent execution, memory capture, and risk escalation across the 90-day plan.**

---

## Daily Checklist (All Team Members)

### Morning Standup (9:00 AM - 9:15 AM)

| # | Action | Tool | Output |
|---|--------|------|--------|
| 1 | **Review assigned tasks** (KB-90DAY-002) | GitHub / MCP | Task list for today |
| 2 | **Check for blocked dependencies** | GitHub / MCP | Escalation if needed |
| 3 | **Update task status** (🔲 → 🔄) | GitHub | Status updated |
| 4 | **Capture daily intention** | MCP `memory_capture` | Memory entry created |

**Example Memory Capture:**
```json
{
  "date": "2026-05-01",
  "owner": "Fuad",
  "tasks": ["1.3 MCP GovSec Server Deployment", "2.1 POC #1 CSM SpankRAT"],
  "blockers": [],
  "notes": "Starting MCP server scaffold, CSM GitHub team setup pending"
}
```

---

### End-of-Day Wrap (6:00 PM - 6:15 PM)

| # | Action | Tool | Output |
|---|--------|------|--------|
| 1 | **Update task status** (🔄 → ✅ or 🔄) | GitHub | Status updated |
| 2 | **Log daily progress** | MCP `memory_capture` | Memory entry created |
| 3 | **Flag new risks** (if any) | KB-90DAY-006 | Risk register updated |
| 4 | **Prepare tomorrow's priorities** | GitHub / Notes | Task list for tomorrow |

**Example Progress Log:**
```json
{
  "date": "2026-05-01",
  "owner": "Fuad",
  "completed": ["1.6 GitHub Repo Setup"],
  "in_progress": ["1.3 MCP GovSec Server Deployment"],
  "blockers": ["Waiting for DAF approval on repo name"],
  "risks": [],
  "tomorrow": ["Complete MCP server scaffold", "Test MCP tool registration"]
}
```

---

## Weekly Checklist (Team Leads: DAF, Hadri, Fuad)

### Friday Review (4:00 PM - 5:00 PM)

| # | Action | Tool | Output |
|---|--------|------|--------|
| 1 | **Review week's completed tasks** | KB-90DAY-002 | Completion rate |
| 2 | **Identify carry-over tasks** | KB-90DAY-002 | Next week's priorities |
| 3 | **Update risk register** | KB-90DAY-006 | New risks added/updated |
| 4 | **Submit weekly status to DAF** | Email / GitHub | Status report |
| 5 | **Schedule next week's key meetings** | Calendar | Invites sent |

**Example Weekly Status Report:**
```markdown
## Week 1-2 Status (May 1-10, 2026)

### Completed
- ✅ 1.4 SpankRAT Threat Intel Brief (Second)
- ✅ 1.6 GitHub Repo Setup (Fuad)

### In Progress
- 🔄 1.3 MCP GovSec Server Deployment (Fuad) — 80% complete
- 🔄 1.5 CSM R&D Workstream Kickoff (Hadri) — Meeting scheduled May 5

### Blocked
- ⚠️ 1.1 Joint IP Framework (DAF) — Waiting for CSM legal review

### Risks
- **R-003:** CSM legal review delay (see KB-90DAY-006)

### Next Week Priorities
- Complete MCP server deployment (1.3)
- Conduct CSM R&D kickoff (1.5)
- Finalize Joint IP framework (1.1)
```

---

## Milestone Checklist (End of Each Phase)

### Phase 1 Review (May 30, 2026)

| # | Action | Owner | Deliverable |
|---|--------|-------|-------------|
| 1 | **POC deployment count** | Fuad | 3-5 POCs confirmed |
| 2 | **POC metrics collection** | Fuad | Detection time, FP rate, triage reduction |
| 3 | **Executive briefing prep** | DAF | CSM Chairman presentation |
| 4 | **Phase 2 readiness assessment** | Hadri | Go/No-Go recommendation |

### Phase 2 Review (June 20, 2026)

| # | Action | Owner | Deliverable |
|---|--------|-------|-------------|
| 1 | **Contract conversion count** | DAF | ≥30% conversion confirmed |
| 2 | **Production deployment status** | Fuad | 2-3 sites live |
| 3 | **Training completion** | Hadri | Admin + analyst training done |
| 4 | **Phase 3 readiness assessment** | DAF | Go/No-Go recommendation |

### Phase 3 Review (July 9, 2026)

| # | Action | Owner | Deliverable |
|---|--------|-------|-------------|
| 1 | **Revenue achievement** | DAF | RM 2M-5M confirmed |
| 2 | **Portfolio completion** | Hadri | 4/4 solutions production-ready |
| 3 | **90-day success metrics** | Second | Full metrics report |
| 4 | **Post-90-day roadmap** | DAF | Phase 4+ planning |

---

## Escalation Triggers

| Trigger | Severity | Action |
|---------|----------|--------|
| Task blocked >48 hours | P1 | Escalate to task owner's lead |
| Task blocked >72 hours | P0 | Escalate to DAF |
| POC deployment delay >1 week | P0 | Escalate to DAF + CSM (Zulfeka) |
| Contract negotiation stalled >2 weeks | P0 | Escalate to DAF + Farul (MTAI) |
| Team member unavailable >3 days | P2 | Hadri to reassign tasks |

---

## Memory Capture Schema

**All daily logs should follow this schema:**

```json
{
  "date": "YYYY-MM-DD",
  "owner": "Name",
  "phase": "Phase 1/2/3",
  "week": "Week 1-2/3-4/etc",
  "completed": ["Task ID + Name"],
  "in_progress": ["Task ID + Name"],
  "blockers": ["Description + Owner"],
  "risks": ["Risk ID + Description"],
  "tomorrow": ["Task ID + Name"],
  "notes": "Free-form context"
}
```

**MCP Tool:** `memory_capture` automatically structures and stores this in the knowledge base.

---

## Query Interface (MCP Tool Access)

```python
# Example: Query today's tasks for Fuad
tasks = mcp.govsec.kb_query(unit_id="KB-90DAY-003", owner="Fuad", date="2026-05-01")

# Example: Query all blocked tasks
blocked = mcp.govsec.kb_query(unit_id="KB-90DAY-003", status="blocked")

# Example: Query this week's progress
progress = mcp.govsec.kb_query(unit_id="KB-90DAY-003", week="Week 1-2")
```

---

**Last Updated:** 2026-04-25 06:34 UTC  
**Next Review:** 2026-05-01 (Phase 1 Kickoff)  
**Retention Tier:** Operational (Active Daily Use)

#KB90Day
#DailyChecklist
#GovSec
#Execution
#MemoryCapture
