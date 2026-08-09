# KB-90DAY-006: Risk Register — Risks, Mitigations, Owners

**Knowledge Unit ID:** KB-90DAY-006  
**Version:** 1.0  
**Classification:** TLP:AMBER (Internal Operational)  
**Created:** 2026-04-25  
**Owner:** Hadri (Technical Lead)  
**Status:** Active — Daily Execution Guidance  

---

## Purpose

**Maintain authoritative risk register for the 90-day execution plan with severity ratings, mitigation strategies, owners, and escalation paths.**

---

## Active Risks

### R-001: POC Timeline Slippage

| Attribute | Value |
|-----------|-------|
| **Risk ID** | R-001 |
| **Description** | POC deployment delayed beyond Week 3-4 target (May 11-20) |
| **Probability** | Medium (40-60%) |
| **Impact** | High (Revenue delay, CSM confidence erosion) |
| **Severity** | **P1** (High Priority) |
| **Owner** | Fuad |
| **Mitigation** | Phased approach: Week 1-2 foundation, Week 3-4 deployment, Week 5-6 validation. Pre-stage all dependencies (MCP server, threat intel, GitHub repo) before POC start. |
| **Trigger** | Any POC task delayed >3 days |
| **Escalation Path** | Fuad → Hadri → DAF → CSM (Zulfeka) |
| **Status** | 🔲 Monitoring |
| **Last Review** | 2026-04-25 |

---

### R-002: Budget Concerns (CSM)

| Attribute | Value |
|-----------|-------|
| **Risk ID** | R-002 |
| **Description** | CSM raises budget/capex concerns during Apr 29 meeting or POC phase |
| **Probability** | Low (10-30%) |
| **Impact** | Medium (POC delay, renegotiation required) |
| **Severity** | **P2** (Medium Priority) |
| **Owner** | DAF |
| **Mitigation** | Emphasize **RM 0 CSM capex** in all communications. Aras funds infrastructure (GPU compute, development, technical resources). CSM provides branding + network access only. Revenue sharing model (60/40 or 40/60) requires no upfront investment. |
| **Trigger** | CSM stakeholder asks about budget/capex |
| **Escalation Path** | DAF → Farul (MTAI) → CSM Chairman (Al-Ishsal) |
| **Status** | 🔲 Monitoring |
| **Last Review** | 2026-04-25 |

---

### R-003: IP Ownership Disagreement

| Attribute | Value |
|-----------|-------|
| **Risk ID** | R-003 |
| **Description** | CSM legal/leadership disagrees with 50/50 joint IP ownership model |
| **Probability** | Medium (40-60%) |
| **Impact** | High (Partnership stalled, POC delay) |
| **Severity** | **P1** (High Priority) |
| **Owner** | DAF/Farul |
| **Mitigation** | Flexible model: CSM branding + revenue sharing + joint registration. Offer tiered ownership: 60/40 (CSM/Aras) for government accounts, 40/60 for private sector. Emphasize co-development contribution (CSM: domain expertise, threat data, validation; Aras: AI models, infrastructure, engineering). |
| **Trigger** | CSM legal review delays IP agreement |
| **Escalation Path** | DAF/Farul → CSM (Zulfeka/Zaharudin) → CSM Chairman |
| **Status** | 🔲 Monitoring |
| **Last Review** | 2026-04-25 |

---

### R-004: Technical Integration Delays

| Attribute | Value |
|-----------|-------|
| **Risk ID** | R-004 |
| **Description** | CMERP/LebahNet integration takes longer than expected (Week 1-2 target) |
| **Probability** | Medium (40-60%) |
| **Impact** | Medium (POC scope reduction, timeline adjustment) |
| **Severity** | **P2** (Medium Priority) |
| **Owner** | Hadri/Nazri |
| **Mitigation** | Focus on 1-2 integration points first (CMERP **or** LebahNet, not both). Use interim data feeds (MISP, OTX, Suricata rules) while waiting for official API access. Document integration blockers for escalation. |
| **Trigger** | Integration task delayed >5 days |
| **Escalation Path** | Hadri → Nazri (CSM) → Zaharudin (CSM) |
| **Status** | 🔲 Monitoring |
| **Last Review** | 2026-04-25 |

---

### R-005: POC-to-Contract Conversion <30%

| Attribute | Value |
|-----------|-------|
| **Risk ID** | R-005 |
| **Description** | Fewer than 30% of POCs convert to paid contracts by Day 60 |
| **Probability** | Medium (40-60%) |
| **Impact** | High (Revenue target missed, RM 2M-5M at risk) |
| **Severity** | **P1** (High Priority) |
| **Owner** | DAF |
| **Mitigation** | Pre-negotiate deployment terms during POC phase. Tie POC success metrics to contract triggers (e.g., "If detection time <15min and FP rate <5%, deployment contract auto-triggers at RM X"). Maintain executive visibility (CSM Chairman, MINDEF leadership) throughout POC. |
| **Trigger** | POC completed without contract discussion |
| **Escalation Path** | DAF → Farul (MTAI) → CSM Chairman / MINDEF Leadership |
| **Status** | 🔲 Monitoring |
| **Last Review** | 2026-04-25 |

---

### R-006: Chairman Availability (CSM)

| Attribute | Value |
|-----------|-------|
| **Risk ID** | R-006 |
| **Description** | CSM Chairman (Al-Ishsal Ishak) unavailable for Apr 29 meeting or key milestones |
| **Probability** | Low (10-30%) |
| **Impact** | Medium (Decision delay, follow-up meeting required) |
| **Severity** | **P2** (Medium Priority) |
| **Owner** | DAF |
| **Mitigation** | Proceed with Zulfeka/Zaharudin as primary decision-makers for Apr 29 meeting. Schedule follow-up with Chairman within 7 days (May 6-8) for final sign-off. Prepare executive summary deck for Chairman review (1-page brief + 5-slide overview). |
| **Trigger** | Chairman declines Apr 29 invitation |
| **Escalation Path** | DAF → Zulfeka → Chairman's Office |
| **Status** | 🔲 Monitoring |
| **Last Review** | 2026-04-25 |

---

### R-007: Team Resource Constraints

| Attribute | Value |
|-----------|-------|
| **Risk ID** | R-007 |
| **Description** | Aras team (Hadri, Fuad, Second) overloaded with parallel workstreams |
| **Probability** | Medium (40-60%) |
| **Impact** | Medium (Task delays, quality degradation) |
| **Severity** | **P2** (Medium Priority) |
| **Owner** | DAF |
| **Mitigation** | Prioritize 90-day plan as **P0** (highest priority) for all team members. Defer non-critical tasks to Phase 2-3. Use MCP tools for automation (memory capture, metrics tracking, stakeholder updates). Consider contractor support for POC deployment if needed. |
| **Trigger** | Team member reports >80% capacity utilization |
| **Escalation Path** | Team Member → Hadri → DAF |
| **Status** | 🔲 Monitoring |
| **Last Review** | 2026-04-25 |

---

## Risk Severity Legend

| Severity | Probability | Impact | Response Time |
|----------|-------------|--------|---------------|
| **P0 (Critical)** | High (>60%) | High (Revenue/Partnership at risk) | 24 hours |
| **P1 (High)** | Medium (40-60%) | High (Revenue/Partnership at risk) | 48 hours |
| **P2 (Medium)** | Low-Medium (10-60%) | Medium (Timeline delay) | 72 hours |
| **P3 (Low)** | Low (<10%) | Low (Minor inconvenience) | 1 week |

---

## Risk Review Cadence

| Review Type | Frequency | Owner | Audience |
|-------------|-----------|-------|----------|
| **Daily Standup** | Daily (9:00 AM) | Hadri | Internal team |
| **Weekly Risk Review** | Weekly (Friday, 4:00 PM) | Hadri | DAF, Fuad, Second |
| **Phase Risk Review** | End of Phase (May 30, June 20, July 9) | DAF | CSM (Zulfeka/Zaharudin) |
| **Ad-Hoc Escalation** | As needed | Any team member | DAF → CSM Leadership |

---

## Risk Status Legend

| Symbol | Meaning |
|--------|---------|
| 🔲 | Monitoring (No action required) |
| 🔄 | Mitigation in Progress |
| ⚠️ | Triggered (Escalation initiated) |
| ✅ | Closed (Risk retired) |
| ❌ | Materialized (Issue occurred, recovery plan active) |

---

## Query Interface (MCP Tool Access)

```python
# Example: Query all P1 risks
p1_risks = mcp.govsec.kb_query(unit_id="KB-90DAY-006", severity="P1")

# Example: Query risks by owner
fuad_risks = mcp.govsec.kb_query(unit_id="KB-90DAY-006", owner="Fuad")

# Example: Query triggered risks
triggered = mcp.govsec.kb_query(unit_id="KB-90DAY-006", status="triggered")

# Example: Generate risk report
report = mcp.govsec.risk_report(phase="Phase 1")
```

---

**Last Updated:** 2026-04-25 06:34 UTC  
**Next Review:** 2026-05-01 (Phase 1 Kickoff)  
**Retention Tier:** Operational (Active Daily Use)

#KB90Day
#RiskRegister
#GovSec
#Mitigation
#Escalation
