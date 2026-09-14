# Critical Delivery Tasks (CDT)

**System:** Self-Populating Task Discovery + Scoring  
**Trial Period:** 2026-05-22 → 2026-06-21 (30 Days)  
**Owner:** CognitiveOS (Second)  
**Review Cadence:** Weekly Synthesis (Sunday 09:00 UTC)

---

## 🎯 Scoring Model (3 Dimensions)

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

### Dimension Scoring Guide

| Score | Commitment | Consequence | Cash |
|-------|------------|-------------|------|
| **9-10** | National-level stakeholder (CSM, Gov) | National security, regulatory penalty | Contract value >RM500K |
| **7-8** | External partner/client expecting delivery | Reputational damage, relationship risk | Contract value RM100-500K |
| **5-6** | Internal stakeholder expecting delivery | Project delay, minor reputational hit | Revenue influence (pipeline) |
| **3-4** | Soft commitment, no deadline | Minor inconvenience, recoverable | Indirect revenue impact |
| **1-2** | No external commitment | No meaningful consequence | No revenue link |

---

## 📋 Active Tasks (Rolling 90-Day Block)

*Auto-populated by heartbeat discovery. Last updated: 2026-05-22 12:15 UTC*

| ID | Task | Commitment | Consequence | Cash | **Score** | Priority | Status |
|----|------|------------|-------------|------|-----------|----------|--------|
| **CDT-001** | CSM CVE-2026-41940: 7-day scan + 90-day POC plan | 10 | 9 | 9 | **87** | 🔴 CRITICAL | 🟡 In Progress |
| **CDT-002** | CBO-01: Finalize + sign first SOW | 9 | 8 | 10 | **85** | 🔴 CRITICAL | 🟡 Draft Ready |
| **CDT-003** | ~~HOI: June 2026 AI Threat Landscape Brief~~ | 7 | 7 | 5 | **62** | ⛔ KILLED | Retired 2026-09-14 (HOI legacy) |
| **CDT-004** | VoronDRQ: Go/No-Go launch decision | 4 | 7 | 8 | **65** | 🟠 HIGH | ⚪ Pending |
| **CDT-005** | AVR: Update registry with new AI infra CVEs | 5 | 7 | 3 | **57** | 🟠 HIGH | 🟢 Active |
| **CDT-006** | CognitiveOS: Weekly memory synthesis | 3 | 5 | 2 | **29** | 🟡 MEDIUM | 🟢 Active |
| **CDT-007** | EMNS: Architecture doc refresh | 2 | 4 | 4 | **34** | 🟡 MEDIUM | ⚪ Stale |
| **CDT-008** | Multi-Agent OS: Design doc v0.1 | 1 | 3 | 2 | **20** | 🟢 LOW | ⚪ Paused |

---

## 🔴 Critical Tasks (Score ≥70)

### CDT-001: CSM CVE-2026-41940 National Assessment

```
Score: 87/100
├─ Commitment: 10/10 (CSM national-level engagement, explicit deadline)
├─ Consequence: 9/10 (National assessment failure = relationship damage)
└─ Cash: 9/10 (7-day scan → 90-day POC = revenue pipeline)

Deadline: 2026-06-05 (7-day scan milestone)
Deliverable: Scan report + 90-day POC engagement plan
Stakeholder: CSM (National)
Status: 🟡 In Progress
Next Action: Finalize scan scope (2026-05-23)
```

### CDT-002: CBO-01 First Commercial SOW

```
Score: 85/100
├─ Commitment: 9/10 (Aras + client expecting signed SOW)
├─ Consequence: 8/10 (Delay = revenue slip, credibility hit)
└─ Cash: 10/10 (First commercial contract = revenue validation)

Deadline: 2026-06-15 (target signing)
Deliverable: Signed SOW + engagement kickoff
Stakeholder: Aras Integrasi + Client
Status: 🟡 Draft Ready (2 pending in GitHub)
Next Action: Review + finalize SOW drafts (2026-05-26)
```

---

## 🟠 High Priority Tasks (Score 50-69)

### CDT-003: HOI June 2026 AI Threat Landscape Brief

```
Score: 62/100
├─ Commitment: 7/10 (Internal/partner expectation, monthly cadence)
├─ Consequence: 7/10 (Missed brief = intel gap, manageable)
└─ Cash: 5/10 (Indirect revenue support via positioning)

Deadline: 2026-06-30
Deliverable: Monthly Intel Brief
Stakeholder: Internal / Partners
Status: ⛔ KILLED 2026-09-14 — HOI agent retired (legacy); deliverable superseded by CognitiveOS AVR workflow
```

### CDT-004: VoronDRQ Go/No-Go Decision

```
Score: 65/100
├─ Commitment: 4/10 (Internal decision, no external deadline)
├─ Consequence: 7/10 (Decision delay = opportunity cost)
└─ Cash: 8/10 (Product launch = revenue potential)

Deadline: 2026-07-15 (self-imposed)
Deliverable: Go/No-Go decision + launch plan OR pause memo
Stakeholder: Internal
Status: ⚪ Pending
Next Action: Decision brief prep (2026-05-29)
```

### CDT-005: AVR Registry Updates

```
Score: 57/100
├─ Commitment: 5/10 (Internal operational baseline)
├─ Consequence: 7/10 (Stale AVR = intel gap on emerging threats)
└─ Cash: 3/10 (Indirect, supports credibility)

Deadline: Ongoing (heartbeat-driven)
Deliverable: Updated AVR entries + changelog
Stakeholder: Internal
Status: 🟢 Active (AVR Agent)
```

---

## 🟡 Medium Priority Tasks (Score 30-49)

| ID | Task | Score | Status | Notes |
|----|------|-------|--------|-------|
| **CDT-006** | Weekly memory synthesis | 29 | 🟢 Active | Baseline continuity |
| **CDT-007** | EMNS architecture refresh | 34 | ⚪ Stale | No deadline, no stakeholder |

---

## 🟢 Low Priority Tasks (Score <30)

| ID | Task | Score | Status | Notes |
|----|------|-------|--------|-------|
| **CDT-008** | Multi-Agent OS design | 20 | ⚪ Paused | Moonshot, revisit Q1 2027 |

---

## 🤖 Discovery Sources

| Source | What We Scan | Cadence |
|--------|--------------|---------|
| **GitHub** (cbo-01) | Draft documents, pending PRs, stale branches, issues with deadlines | Every heartbeat |
| **Telegram/Email** | Explicit commitments ("I'll deliver X by Y"), stakeholder requests | Every heartbeat |
| **Memory Files** (daily logs) | Unresolved decisions, follow-ups marked "TODO" | Daily synthesis |

### Discovery Rules

**Auto-Create Task When:**
- ≥3 discovery signals (e.g., GitHub draft + email mention + memory note)
- OR explicit stakeholder commitment with deadline
- OR national-level engagement (CSM, government)

**Auto-Archive Task When:**
- Score <30 for >30 days
- No stakeholder commitment
- No discovery signal refresh in 60 days

**Auto-Escalate When:**
- Deadline within 7 days → Telegram alert
- Score increases ≥20 points (new stakeholder commitment)
- New CRITICAL task emerges (score ≥70)

---

## 📊 Block Capacity

| Priority | Capacity | Current Load | Status |
|----------|----------|--------------|--------|
| **CRITICAL (≥70)** | 2-3 tasks | 2 tasks | ✅ Optimal |
| **HIGH (50-69)** | 3-4 tasks | 3 tasks | ✅ Optimal |
| **MEDIUM (30-49)** | 2-3 tasks | 2 tasks | ✅ Optimal |
| **LOW (<30)** | 0-1 tasks | 1 task | ⚠️ At limit |

**Block Status:** 🟢 **OPTIMAL** — New CRITICAL tasks require displacement.

---

## 📝 Change Log

| Date | Change | Reason |
|------|--------|--------|
| 2026-05-22 | System created (30-day trial) | 3-dimension scoring (Commitment, Consequence, Cash) |
| 2026-05-22 | Initial 8 tasks scored | Auto-populated from GitHub + memory scan |

---

## 🧪 Trial Success Criteria (Day 30: 2026-06-21)

**Pass If:**
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

**System Owner:** CognitiveOS (Second)  
**Last Heartbeat Scan:** 2026-05-22 12:15 UTC  
**Next Review:** 2026-05-25 (Sunday 09:00 UTC)
