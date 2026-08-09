# KB-90DAY-002: Phase Breakdown — Weekly Task Lists

**Knowledge Unit ID:** KB-90DAY-002  
**Version:** 1.0  
**Classification:** TLP:AMBER (Internal Operational)  
**Created:** 2026-04-25  
**Owner:** Hadri (Technical Lead)  
**Status:** Active — Daily Execution Guidance  

---

## Phase 1: Foundation & POC Deployment (Days 1-30)

**Timeline:** May 1 - May 30, 2026  
**Budget:** RM 50K - RM 100K (Aras-funded)  
**Owner:** DAF (Commercial), Hadri (Technical), Fuad (Delivery)

### Week 1-2: Mobilization (May 1-10)

| Task ID | Task | Owner | Deliverable | Dependencies | Status |
|---------|------|-------|-------------|--------------|--------|
| **1.1** | Finalize Joint IP Framework | DAF/Farul | IP co-ownership agreement draft | None | 🔲 |
| **1.2** | Confirm POC Target List (3-5 accounts) | DAF | Named account list with executive sponsors | 1.1 | 🔲 |
| **1.3** | Deploy MCP GovSec Server | Fuad | 4 MCP tools operational | None | 🔲 |
| **1.4** | SpankRAT Threat Intel Brief | Second | Briefing deck for CSM/POC targets | None | ✅ Complete |
| **1.5** | CSM R&D Workstream Kickoff | Hadri/Nazri | 3 tracks defined (Telemetry, AI Correlation, POC Arch) | 1.2 | 🔲 |
| **1.6** | GitHub Repo Setup (Private) | Fuad | `aras-integrasi/govsec-poc` created, CSM team added | None | 🔲 |
| **1.7** | Upload 90-Day Plan to GitHub | Second | Document uploaded (private) | 1.6 | 🔲 |

### Week 3-4: POC Deployment (May 11-20)

| Task ID | Task | Owner | Deliverable | Dependencies | Status |
|---------|------|-------|-------------|--------------|--------|
| **2.1** | POC #1: CSM SpankRAT Detection | Fuad/Zaharudin | Behavioral detection agent deployed, <15min TTD | 1.5 | 🔲 |
| **2.2** | POC #2: MINDEF BSEP LotL C2 Monitoring | Fuad/Nazri | Suricata rules + AIL chat feeders operational | 1.3 | 🔲 |
| **2.3** | POC #3: UPNM DWI Lab Training Module | Hadri | ESP-Claw + AIL Framework deployed for training | 1.2 | 🔲 |
| **2.4** | POC #4: GLC Threat Intel Dashboard | DAF | Executive briefing tool deployed (OC-CIL) | 1.3 | 🔲 |
| **2.5** | POC #5: NACSA CBOM Mapping | Fuad | SBOM ingestion + supply chain risk visualization | 1.3 | 🔲 |

### Week 5-6: Value Demonstration (May 21-30)

| Task ID | Task | Owner | Deliverable | Dependencies | Status |
|---------|------|-------|-------------|--------------|--------|
| **3.1** | POC Metrics Collection | Fuad | Detection time, false positive rate, SOC triage reduction | 2.1-2.5 | 🔲 |
| **3.2** | Executive Briefing (CSM) | DAF | POC results presentation to Chairman + CSM leadership | 3.1 | 🔲 |
| **3.3** | Deployment Proposal Drafting | Hadri | Production deployment scope + pricing per POC | 3.1 | 🔲 |
| **3.4** | Contract Negotiation Kickoff | DAF/Farul | Terms sheet for converting POCs to production | 3.3 | 🔲 |

---

## Phase 2: Production Deployment (Days 31-60)

**Timeline:** June 1 - June 20, 2026  
**Budget:** RM 500K - RM 1M (Customer-funded)  
**Owner:** DAF (Commercial), Hadri (Architecture), Fuad (Delivery)

### Week 7-8: Contract Conversion (June 1-10)

| Task ID | Task | Owner | Deliverable | Dependencies | Status |
|---------|------|-------|-------------|--------------|--------|
| **4.1** | POC-to-Contract Conversion (≥30% target) | DAF | 1-2 contracts signed (RM 200K-500K each) | 3.4 | 🔲 |
| **4.2** | Production Architecture Design | Hadri | Sovereign deployment blueprint (air-gapped capable) | 4.1 | 🔲 |
| **4.3** | Data Governance Framework | Fuad | Data residency, query logging, RBAC, audit trails | 4.2 | 🔲 |
| **4.4** | OC-CIL Knowledge Base Deployment | Second | 11 knowledge units ingested, entity/relation graph | 4.2 | 🔲 |

### Week 9: Deployment Execution (June 11-20)

| Task ID | Task | Owner | Deliverable | Dependencies | Status |
|---------|------|-------|-------------|--------------|--------|
| **5.1** | Production Deployment #1 (CSM) | Fuad | GovSec platform operational at CSM SOC | 4.2, 4.3 | 🔲 |
| **5.2** | Production Deployment #2 (MINDEF/GLC) | Fuad | GovSec platform operational at customer site | 4.2, 4.3 | 🔲 |
| **5.3** | Training & Handover | Hadri | Admin + analyst training completed | 5.1, 5.2 | 🔲 |
| **5.4** | SLA Definition | DAF | Support model, escalation paths, response times | 5.1, 5.2 | 🔲 |

---

## Phase 3: Scaling & Portfolio Expansion (Days 61-90)

**Timeline:** June 21 - July 9, 2026  
**Budget:** RM 2M - RM 5M (Customer-funded)  
**Owner:** DAF (Commercial), Hadri (Program), Fuad (Technical)

### Week 10-11: Multi-Agency Rollout (June 21-30)

| Task ID | Task | Owner | Deliverable | Dependencies | Status |
|---------|------|-------|-------------|--------------|--------|
| **6.1** | NACSA Engagement | DAF | CBOM mapping + supply chain risk platform deployed | 5.1 | 🔲 |
| **6.2** | BNM Engagement | DAF/Farul | Digital Risk Quantification GRC pilot initiated | 5.1 | 🔲 |
| **6.3** | MCMC Engagement | DAF | CII protection monitoring deployed (telco/broadcasting) | 5.1 | 🔲 |
| **6.4** | Joint IP Registration | DAF/Farul | IP co-ownership documentation filed | 4.1 | 🔲 |

### Week 12-13: Portfolio Completion (July 1-9)

| Task ID | Task | Owner | Deliverable | Dependencies | Status |
|---------|------|-------|-------------|--------------|--------|
| **7.1** | GovSec Threat Intelligence Platform | Fuad | Production-ready, RM 5M/year revenue target | 6.1 | 🔲 |
| **7.2** | Digital Risk Quantification GRC | Hadri | Production-ready, RM 6M/year revenue target | 6.2 | 🔲 |
| **7.3** | Blockchain Intelligence Platform | Fuad | Production-ready, RM 5M/year revenue target | 6.1 | 🔲 |
| **7.4** | Unified Intelligence Platform | Second | Production-ready, RM 5M/year revenue target | 6.3 | 🔲 |

---

## Task Status Legend

| Symbol | Meaning |
|--------|---------|
| 🔲 | Not Started |
| 🔄 | In Progress |
| ✅ | Complete |
| ⚠️ | Blocked (see Risk Register KB-90DAY-006) |
| ❌ | Cancelled |

---

## Daily Execution Guidance

**Each morning, team members should:**
1. Review their assigned tasks for current week
2. Update task status (🔄, ✅, ⚠️)
3. Escalate blocked tasks per KB-90DAY-001 escalation protocol
4. Log daily progress in memory capture (MCP tool: `memory_capture`)

**Each Friday, team leads should:**
1. Review week's completed tasks
2. Identify carry-over tasks for next week
3. Update risk register (KB-90DAY-006) if new risks identified
4. Submit weekly status report to DAF

---

## Query Interface (MCP Tool Access)

```python
# Example: Query Week 1-2 tasks
tasks = mcp.govsec.kb_query(unit_id="KB-90DAY-002", phase="Week 1-2")

# Example: Query tasks by owner
fuad_tasks = mcp.govsec.kb_query(unit_id="KB-90DAY-002", owner="Fuad")

# Example: Query blocked tasks
blocked = mcp.govsec.kb_query(unit_id="KB-90DAY-002", status="blocked")
```

---

**Last Updated:** 2026-04-25 06:34 UTC  
**Next Review:** 2026-05-01 (Phase 1 Kickoff)  
**Retention Tier:** Operational (Active Daily Use)

#KB90Day
#PhaseBreakdown
#GovSec
#TaskList
#DailyExecution
