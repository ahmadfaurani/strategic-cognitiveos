# CDT Discovery Agent

**Purpose:** Auto-discover and score Critical Delivery Tasks (CDT) from workspace signals.  
**Trial Period:** 2026-05-22 → 2026-06-21 (30 days)  
**Owner:** CognitiveOS (Second)

---

## Discovery Sources

| Source | Location | What We Extract |
|--------|----------|-----------------|
| **GitHub** | `cbo-01-commercial-ops`, `hoi-intelligence-ops` | Draft documents, pending PRs, issues with deadlines, stale branches |
| **Telegram/Email** | Memory files (daily logs) | Explicit commitments ("I'll deliver X by Y"), stakeholder requests |
| **Memory Files** | `memory/YYYY-MM-DD.md` | Unresolved decisions, TODOs, follow-ups |

---

## Scoring Model (3 Dimensions)

### Dimensions

| Dimension | Weight | Question |
|-----------|--------|----------|
| **Commitment** | 3.0x | Is an external party expecting this? |
| **Consequence** | 3.0x | What happens if we slip or fail? |
| **Cash** | 4.0x | Does this directly generate or protect revenue? |

### Score Calculation

```
CDT Score = (Commitment × 3.0) + (Consequence × 3.0) + (Cash × 4.0)

Maximum Score: 100
Critical Threshold: ≥70
High Priority: 50-69
Medium Priority: 30-49
Low Priority: <30
```

### Auto-Scoring Defaults

| Pattern | Commitment | Consequence | Cash | Default Score |
|---------|------------|-------------|------|---------------|
| **CSM national engagement** | 10 | 9 | 9 | 87 |
| **SOW pending signature** | 9 | 8 | 10 | 85 |
| **Monthly intel brief (HOI)** | 7 | 7 | 5 | 62 |
| **Internal decision (no deadline)** | 4 | 7 | 8 | 65 |
| **AVR heartbeat update** | 5 | 7 | 3 | 57 |
| **Memory synthesis** | 3 | 5 | 2 | 29 |
| **Architecture doc refresh** | 2 | 4 | 4 | 34 |
| **Moonshot design** | 1 | 3 | 2 | 20 |

---

## Discovery Rules

### Auto-Create Task When:
- ≥3 discovery signals (e.g., GitHub draft + email mention + memory note)
- OR explicit stakeholder commitment with deadline
- OR national-level engagement (CSM, government)

### Auto-Archive Task When:
- Score <30 for >30 days
- No stakeholder commitment
- No discovery signal refresh in 60 days

### Auto-Escalate When:
- Deadline within 7 days → Telegram alert
- Score increases ≥20 points (new stakeholder commitment)
- New CRITICAL task emerges (score ≥70)

---

## Heartbeat Integration

**Every heartbeat cycle:**

1. **Scan GitHub** → Check for new drafts, PRs, issues with deadlines
2. **Scan Memory** → Extract commitments, TODOs, unresolved decisions
3. **Score New Tasks** → Apply 3-dimension rubric
4. **Update `critical-delivery-tasks.md`** → Refresh task list
5. **Check Escalation** → Alert if CRITICAL or deadline <7 days
6. **Log to `memory/heartbeat-state.json`** → Update `cdt_discovery` timestamp

---

## Output Format

### Task Entry Template

```markdown
### CDT-XXX: [Task Name]

```
Score: XX/100
├─ Commitment: X/10 (reason)
├─ Consequence: X/10 (reason)
└─ Cash: X/10 (reason)

Deadline: YYYY-MM-DD
Deliverable: [Concrete artifact]
Stakeholder: [Internal/External + name]
Status: [🟡 In Progress | 🟢 Active | ⚪ Pending | ⚪ Stale | ⚪ Paused]
Next Action: [Specific action + date]
```
```

### Heartbeat Log Entry

```markdown
### CDT Discovery (HH:MM UTC)
| Metric | Value |
|--------|-------|
| Tasks Scanned | N |
| New Tasks Created | N |
| Scores Updated | N |
| Escalations Triggered | N |
| Critical Tasks | N |

**Changes:** [Summary of what changed since last heartbeat]
**Alerts:** [Any escalations triggered]
```

---

## Files Managed

| File | Purpose |
|------|---------|
| `critical-delivery-tasks.md` | Living task list (root workspace) |
| `memory/heartbeat-state.json` | CDT trial metadata + last scan timestamp |
| `memory/YYYY-MM-DD.md` | Daily heartbeat log with CDT summary |

---

## Trial Success Metrics

**Pass If (Day 30: 2026-06-21):**
- [ ] DAF reviewed task list ≥3x/week without nagging
- [ ] At least one task deprioritized (score < threshold)
- [ ] At least one decision made faster due to score clarity
- [ ] Zero "Where did that commitment come from?" incidents

**Fail If:**
- [ ] Manual scoring required (not automated)
- [ ] List has 20+ items (discovery runaway)
- [ ] DAF ignoring list, using mental list instead
- [ ] Second nagging for reviews

---

## Escalation Paths

| Trigger | Action | Channel |
|---------|--------|---------|
| **New CRITICAL task (≥70)** | Telegram alert with task summary | Telegram |
| **Deadline <7 days** | Telegram alert + draft prep offer | Telegram |
| **Score increase ≥20 points** | Log to daily memory, flag for weekly review | Memory |
| **Discovery runaway (>20 tasks)** | Auto-archive lowest 5, alert DAF | Telegram + Memory |

---

**Agent Owner:** CognitiveOS (Second)  
**Created:** 2026-05-22  
**Trial Ends:** 2026-06-21
