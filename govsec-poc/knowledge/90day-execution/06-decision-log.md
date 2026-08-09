# KB-90DAY-007: Decision Log — Key Decisions, Rationale, Owners

**Knowledge Unit ID:** KB-90DAY-007  
**Version:** 1.0  
**Classification:** TLP:AMBER (Internal Operational)  
**Created:** 2026-04-25  
**Owner:** Second (Cognitive Operations)  
**Status:** Active — Daily Execution Guidance  

---

## Purpose

**Maintain authoritative decision log for the 90-day execution plan with decision context, rationale, alternatives considered, owners, and review dates.**

---

## Decision Log

### DEC-001: 90-Day Execution Plan Structure

| Attribute | Value |
|-----------|-------|
| **Decision ID** | DEC-001 |
| **Date** | 2026-04-25 |
| **Decision** | Adopt 3-phase, 90-day execution plan (POC → Deployment → Scaling) |
| **Context** | CSM-Aras partnership requires structured, measurable pathway from strategic alignment to commercial outcomes |
| **Rationale** | 90-day timeline balances speed (revenue generation) with feasibility (technical deployment, stakeholder alignment). 3-phase approach enables incremental validation and course correction. |
| **Alternatives Considered** | 1. 6-month plan (too slow, loses momentum) 2. 30-day plan (too aggressive, high failure risk) 3. Open-ended plan (lacks accountability) |
| **Owner** | DAF |
| **Approvers** | DAF, Farul (MTAI) |
| **Review Date** | 2026-05-30 (Phase 1 Review) |
| **Status** | ✅ Approved |

---

### DEC-002: Revenue Target (RM 2M-5M by Day 90)

| Attribute | Value |
|-----------|-------|
| **Decision ID** | DEC-002 |
| **Date** | 2026-04-25 |
| **Decision** | Set revenue target of RM 2M-5M signed contracts by Day 90 |
| **Context** | Commercial success requires measurable revenue targets, not just POC deployments |
| **Rationale** | RM 2M-5M is achievable with 3-5 POCs, ≥30% conversion rate, and average contract value of RM 500K-1.5M. Aligns with CSM's expectation for "revenue-focused, business-oriented" engagement. |
| **Alternatives Considered** | 1. RM 1M target (too conservative, undervalues capability) 2. RM 10M target (too aggressive, risks credibility) 3. POC-count target only (lacks commercial discipline) |
| **Owner** | DAF |
| **Approvers** | DAF, Farul (MTAI) |
| **Review Date** | 2026-06-20 (Phase 2 Review) |
| **Status** | ✅ Approved |

---

### DEC-003: Joint IP Ownership (50/50 Split)

| Attribute | Value |
|-----------|-------|
| **Decision ID** | DEC-003 |
| **Date** | 2026-04-25 |
| **Decision** | Adopt 50/50 joint IP ownership model (CSM/Aras) with CSM branding |
| **Context** | CSM expects co-ownership of jointly developed IP; Aras requires commercialization rights |
| **Rationale** | 50/50 split reflects equal contribution (CSM: domain expertise, threat data, validation, branding; Aras: AI models, infrastructure, engineering, delivery). CSM branding reinforces national trust; Aras delivery ensures execution quality. Revenue sharing (60/40 or 40/60) provides flexibility for government vs. private sector accounts. |
| **Alternatives Considered** | 1. CSM-owned, Aras licensed (Aras loses long-term value) 2. Aras-owned, CSM royalty (CSM loses strategic control) 3. Case-by-case ownership (complex, creates precedent risk) |
| **Owner** | DAF/Farul |
| **Approvers** | DAF, Farul (MTAI), CSM (Pending Apr 29) |
| **Review Date** | 2026-04-29 (CSM Stakeholder Meeting) |
| **Status** | 🔲 Pending CSM Approval |

---

### DEC-004: No CSM Capex Required

| Attribute | Value |
|-----------|-------|
| **Decision ID** | DEC-004 |
| **Date** | 2026-04-25 |
| **Decision** | Aras funds all infrastructure (GPU compute, development, technical resources); CSM provides branding + network access only |
| **Context** | CSM may have budget constraints; Aras has sovereign GPU infrastructure ready |
| **Rationale** | Removes budget barrier for CSM participation. Aras already has 32x NVIDIA B200 GPUs deployed locally. CSM's non-financial contribution (domain expertise, government network, branding) is equally valuable. Revenue sharing model ensures CSM benefits without upfront investment. |
| **Alternatives Considered** | 1. CSM co-funds infrastructure (budget barrier, delays participation) 2. External investor funding (complex, loses sovereign control) 3. Grant funding (slow, uncertain) |
| **Owner** | DAF |
| **Approvers** | DAF, Farul (MTAI) |
| **Review Date** | 2026-04-29 (CSM Stakeholder Meeting) |
| **Status** | ✅ Approved (Pending CSM Acknowledgment) |

---

### DEC-005: GitHub Repository Structure (Single Private Repo)

| Attribute | Value |
|-----------|-------|
| **Decision ID** | DEC-005 |
| **Date** | 2026-04-25 |
| **Decision** | Use single private GitHub repo (`aras-integrasi/govsec-poc`) for POC phase; grant CSM read access via GitHub team |
| **Context** | Need secure document sharing for POC deployment; balance transparency with confidentiality |
| **Rationale** | Single repo simplifies access control, faster setup, easier CSM onboarding. Private visibility protects revenue targets, pricing, internal strategy. CSM read access ensures transparency without edit rights. Public repo (sanitized) can be created post-POC for marketing. |
| **Alternatives Considered** | 1. Multi-repo strategy (complex, overhead) 2. Public repo from Day 1 (exposes sensitive info) 3. No GitHub (loses version control, collaboration) |
| **Owner** | Fuad |
| **Approvers** | DAF, Fuad |
| **Review Date** | 2026-05-01 (Phase 1 Kickoff) |
| **Status** | 🔲 Pending DAF Confirmation |

---

### DEC-006: MCP-First Skill Development Strategy

| Attribute | Value |
|-----------|-------|
| **Decision ID** | DEC-006 |
| **Date** | 2026-04-24 |
| **Decision** | Develop GovSec skills at L1 (MCP Tools) for maximum portability across Codex, Claude Code, OpenClaw |
| **Context** | Agent skills interchangeability assessment identified 3-tier portability framework |
| **Rationale** | L1 (MCP Tools) provides maximum portability, lowest coupling, easiest maintenance. 80% effort on Tier 1 (MCP), 20% on Tier 2-3 (diligence only). Enables deployment across multiple agent platforms without rewrite. |
| **Alternatives Considered** | 1. SKILL.md-first (L2) — locks to specific agent platform 2. Markdown-first (L3) — limited automation capability 3. Multi-tier parallel development — resource-intensive |
| **Owner** | Second |
| **Approvers** | DAF (Apr 24, 2026) |
| **Review Date** | 2026-05-15 (Phase 1 Midpoint) |
| **Status** | ✅ Approved |

---

### DEC-007: AIL Framework Reclassification (UPNM DWI Standalone)

| Attribute | Value |
|-----------|-------|
| **Decision ID** | DEC-007 |
| **Date** | 2026-04-25 |
| **Decision** | Reclassify AIL Framework as UPNM DWI standalone tooling (educational); defer operational integration to Phase 2-3 (Jun-Jul 2026) |
| **Context** | AIL Framework ready for threat intel, but CSM/MINDEF POCs require immediate capability (May 2026) |
| **Rationale** | Interim solution (MISP + OTX + Suricata rules) available for May 2026 POCs. AIL operational integration deferred to Phase 2-3 allows focused POC deployment without dependency risk. UPNM DWI educational track proceeds independently (no operational risk). |
| **Alternatives Considered** | 1. AIL operational integration (May 2026) — high dependency risk, delays POC 2. Drop AIL entirely — loses long-term capability 3. Hybrid approach (interim + AIL Phase 2-3) — recommended |
| **Owner** | Second |
| **Approvers** | DAF (Apr 25, 2026) |
| **Review Date** | 2026-06-01 (Phase 2 Kickoff) |
| **Status** | ✅ Approved |

---

## Decision Status Legend

| Symbol | Meaning |
|--------|---------|
| 🔲 | Pending (Awaiting approval) |
| 🔄 | Under Review |
| ✅ | Approved (Active) |
| ❌ | Rejected (Superseded) |
| ⏸️ | Deferred (Future review) |

---

## Decision Review Cadence

| Review Type | Frequency | Owner | Audience |
|-------------|-----------|-------|----------|
| **Daily Standup** | Daily (9:00 AM) | Hadri | Internal team |
| **Weekly Decision Review** | Weekly (Friday, 4:00 PM) | Second | DAF, Hadri, Fuad |
| **Phase Decision Review** | End of Phase (May 30, June 20, July 9) | DAF | CSM (Zulfeka/Zaharudin) |
| **Ad-Hoc Escalation** | As needed | Any team member | DAF → CSM Leadership |

---

## Query Interface (MCP Tool Access)

```python
# Example: Query pending decisions
pending = mcp.govsec.kb_query(unit_id="KB-90DAY-007", status="pending")

# Example: Query decisions by owner
daf_decisions = mcp.govsec.kb_query(unit_id="KB-90DAY-007", owner="DAF")

# Example: Query decisions requiring CSM approval
csm_approval = mcp.govsec.kb_query(unit_id="KB-90DAY-007", approvers__contains="CSM")

# Example: Generate decision report
report = mcp.govsec.decision_report(phase="Phase 1")
```

---

**Last Updated:** 2026-04-25 06:34 UTC  
**Next Review:** 2026-05-01 (Phase 1 Kickoff)  
**Retention Tier:** Operational (Active Daily Use)

#KB90Day
#DecisionLog
#GovSec
#Governance
#Approval
