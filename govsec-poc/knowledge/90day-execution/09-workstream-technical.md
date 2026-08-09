# KB-90DAY-WS-003: Technical Workstream — Architecture, Integration, Deployment

**Knowledge Unit ID:** KB-90DAY-WS-003  
**Version:** 1.0  
**Classification:** TLP:AMBER (Internal Operational)  
**Created:** 2026-04-25  
**Owner:** Hadri (Technical Lead)  
**Status:** Active — Daily Execution Guidance  

---

## Purpose

**Translate strategy into deployable and demonstrable technical capability with architecture, integration, deployment, security, and compliance alignment for Aras-CSM 90-day execution plan.**

---

## Technical Architecture Overview

### Solution Domains

| Domain | Core Capability | Tech Stack | Deployment Model |
|--------|-----------------|------------|------------------|
| **GovSec Threat Intelligence** | Multi-source ingestion, correlation, alerting | AIL Framework, MISP, Suricata, OC-CIL | Sovereign, air-gapped capable |
| **Digital Risk Quantification (DRQ)** | Risk scoring, GRC reporting, board-level metrics | OC-CIL, Neo4j, Qwen3.5, BGE-M3 | Cloud or on-prem |
| **Blockchain Intelligence** | Crypto tracing, fraud detection, AML compliance | Graph analysis, chain analytics | Cloud or on-prem |
| **LE-UIP (Unified Intelligence Platform)** | Cross-domain aggregation, intelligence fusion | OC-CIL, Neo4j, AIL, MISP | Sovereign, air-gapped capable |

---

### Infrastructure Requirements

| Component | Specification | Owner | Location |
|-----------|---------------|-------|----------|
| **GPU Compute** | 32x NVIDIA B200 (local) | Aras | Aras data center |
| **LLM Runtime** | vLLM/Ollama, Qwen3.5-397B, Mixtral | Aras | Local deployment |
| **Embeddings** | BGE-M3, Nomic Embed | Aras | Local deployment |
| **Reranker** | BGE Reranker | Aras | Local deployment |
| **Vector Database** | Qdrant (local) | Aras | Local deployment |
| **Graph Database** | Neo4j (local) | Aras | Local deployment |
| **MCP Server** | mcp-govsec-server (4 tools) | Aras | Local deployment |
| **Memory Layer** | OC-CIL knowledge base (11 units) | Aras | Local deployment |

**Total Infrastructure:** Sovereign, air-gapped capable, no external API dependency

---

### Integration Points

| Integration | System | Protocol | Owner | Status |
|-------------|--------|----------|-------|--------|
| **CMERP** | CSM Threat Intel Platform | API (pending spec) | Nazri (CSM) | 🔲 Pending |
| **LebahNet** | CSM Network Monitoring | API (pending spec) | Nazri (CSM) | 🔲 Pending |
| **MISP** | Threat Intel Sharing | MISP API | Fuad | ✅ Ready |
| **OTX** | AlienVault OTX | REST API | Fuad | ✅ Ready |
| **Suricata** | IDS/IPS Rules | File-based | Fuad | ✅ Ready |
| **AIL Framework** | Dark Web Monitoring | Chat feeders | Fuad | 🔲 Week 2-3 |
| **ESP-Claw** | Edge IoT Sensors | MQTT/HTTP | Fuad | 🔲 Week 1-2 |
| **SwarmForge** | Multi-Agent Orchestration | tmux-based | Hadri | 🔲 Week 1-2 |

---

## Security & Compliance Alignment

| Standard | Requirement | Alignment Status | Owner |
|----------|-------------|------------------|-------|
| **ISO 27001** | ISMS, risk assessment, access control | 🔲 To Align | Hadri |
| **RMiT** (BNM) | Technology risk management, outsourcing | 🔲 To Align | Hadri |
| **GTRM** (GovTech) | Government cloud security | 🔲 To Align | Hadri |
| **PDPA** | Personal data protection | 🔲 To Align | Hadri |
| **Data Residency** | Malaysia-based storage | ✅ Compliant | Aras |
| **Air-Gapped Deployment** | No external API dependency | ✅ Capable | Aras |

---

## Workstream Tasks (By Phase)

### Phase 1: Alignment & Mobilization (Day 1-15)

| Task ID | Task | Owner | Deliverable | Due Date | Status |
|---------|------|-------|-------------|----------|--------|
| **TECH-1.1** | Define solution architecture (all 4 domains) | Hadri | Architecture document | May 10 | 🔲 |
| **TECH-1.2** | Confirm infrastructure readiness | Fuad | Infrastructure checklist | May 8 | 🔲 |
| **TECH-1.3** | Define integration requirements (CMERP, LebahNet) | Nazri (CSM) | Integration spec draft | May 12 | 🔲 |
| **TECH-1.4** | Set up GitHub repo (private) | Fuad | `aras-integrasi/govsec-poc` | May 5 | 🔲 |
| **TECH-1.5** | Upload technical docs to GitHub | Second | Architecture, specs uploaded | May 6 | 🔲 |
| **TECH-1.6** | WG review of technical architecture | WG | Architecture approved | May 15 | 🔲 |

---

### Phase 2: Use Case & Early Adopter (Day 16-30)

| Task ID | Task | Owner | Deliverable | Due Date | Status |
|---------|------|-------|-------------|----------|--------|
| **TECH-2.1** | Define data requirements per POC | Joint | Data onboarding checklist | May 20 | 🔲 |
| **TECH-2.2** | Define success criteria matrix (quantifiable) | Joint | KPI definition per POC | May 22 | 🔲 |
| **TECH-2.3** | Draft POC implementation plan (per account) | Fuad | 5 POC implementation plans | May 25 | 🔲 |
| **TECH-2.4** | Draft demo & technical architecture pack | Hadri | Demo architecture document | May 28 | 🔲 |
| **TECH-2.5** | WG approval of POC implementation plans | WG | Plans approved | May 30 | 🔲 |

---

### Phase 3: Commercial & Governance (Day 31-45)

| Task ID | Task | Owner | Deliverable | Due Date | Status |
|---------|------|-------|-------------|----------|--------|
| **TECH-3.1** | Finalize MVP capability list (4 domains) | Hadri | MVP modules spec | June 5 | 🔲 |
| **TECH-3.2** | Begin MVP development (GovSec, DRQ) | Fuad | MVP v0.5 | June 10 | 🔲 |
| **TECH-3.3** | Begin MVP development (Blockchain, LE-UIP) | Fuad | MVP v0.5 | June 10 | 🔲 |
| **TECH-3.4** | Define security compliance checklist | Hadri | ISO 27001, RMiT, GTRM alignment | June 12 | 🔲 |
| **TECH-3.5** | WG review of MVP capabilities | WG | MVP spec approved | June 15 | 🔲 |

---

### Phase 4: Technical Readiness (Day 46-60)

| Task ID | Task | Owner | Deliverable | Due Date | Status |
|---------|------|-------|-------------|----------|--------|
| **TECH-4.1** | Complete MVP development (all 4 domains) | Fuad | MVP v1.0 ready | June 25 | 🔲 |
| **TECH-4.2** | Deploy demo environment | Fuad | Live demo accessible | June 28 | 🔲 |
| **TECH-4.3** | Conduct internal testing (all 4 domains) | Hadri | Test reports | July 1 | 🔲 |
| **TECH-4.4** | Security compliance review | Hadri | Compliance sign-off | July 3 | 🔲 |
| **TECH-4.5** | WG approval of demo readiness | WG | Demo sign-off | July 5 | 🔲 |

---

### Phase 5: POC Launch (Day 61-75)

| Task ID | Task | Owner | Deliverable | Due Date | Status |
|---------|------|-------|-------------|----------|--------|
| **TECH-5.1** | Deploy POC #1 (CSM SpankRAT) | Fuad | POC live | July 8 | 🔲 |
| **TECH-5.2** | Deploy POC #2 (MINDEF LotL C2) | Fuad | POC live | July 10 | 🔲 |
| **TECH-5.3** | Deploy POC #3 (UPNM Training) | Fuad | POC live | July 12 | 🔲 |
| **TECH-5.4** | Deploy POC #4 (GLC Dashboard) | Fuad | POC live | July 14 | 🔲 |
| **TECH-5.5** | Deploy POC #5 (NACSA CBOM) | Fuad | POC live | July 15 | 🔲 |
| **TECH-5.6** | Monitor POC performance (daily) | Fuad | Daily status reports | July 20 | 🔲 |

---

### Phase 6: Review & Conversion (Day 76-90)

| Task ID | Task | Owner | Deliverable | Due Date | Status |
|---------|------|-------|-------------|----------|--------|
| **TECH-6.1** | Collect POC performance metrics | Fuad | Performance report | July 25 | 🔲 |
| **TECH-6.2** | Conduct POC retrospective (all accounts) | Hadri | Retrospective report | July 27 | 🔲 |
| **TECH-6.3** | Define production deployment plan | Hadri | Deployment roadmap | July 28 | 🔲 |
| **TECH-6.4** | Support conversion negotiations | Hadri | Technical Q&A | July 30 | 🔲 |

---

## Technical Deliverables Checklist

| Deliverable | Phase | Owner | Status |
|-------------|-------|-------|--------|
| Solution Architecture Document | Phase 1 | Hadri | 🔲 |
| Infrastructure Readiness Checklist | Phase 1 | Fuad | 🔲 |
| Integration Spec (CMERP, LebahNet) | Phase 1 | Nazri | 🔲 |
| Data Onboarding Checklist | Phase 2 | Joint | 🔲 |
| Success Criteria Matrix | Phase 2 | Joint | 🔲 |
| POC Implementation Plans (5x) | Phase 2 | Fuad | 🔲 |
| Demo Architecture Pack | Phase 2 | Hadri | 🔲 |
| MVP Capability Specs (4 domains) | Phase 3 | Hadri | 🔲 |
| MVP v1.0 (4 domains) | Phase 4 | Fuad | 🔲 |
| Demo Environment | Phase 4 | Fuad | 🔲 |
| Compliance Sign-off | Phase 4 | Hadri | 🔲 |
| POC Deployments (5x) | Phase 5 | Fuad | 🔲 |
| POC Performance Report | Phase 6 | Fuad | 🔲 |
| Production Deployment Plan | Phase 6 | Hadri | 🔲 |

---

## Success Metrics

| Metric | Target | Measurement Method |
|--------|--------|--------------------|
| **MVP Completion** | 4/4 domains | MVP v1.0 deployed |
| **Demo Readiness** | 100% | Live demo accessible |
| **POC Deployment** | 5/5 POCs | All POCs live by Day 75 |
| **Compliance Alignment** | ISO 27001, RMiT, GTRM | Compliance sign-off |
| **Integration Readiness** | CMERP + LebahNet | API integration complete |
| **POC Performance** | ≥90% detection rate, <5min TTD | POC metrics report |

---

## Query Interface (MCP Tool Access)

```python
# Example: Query technical architecture
arch = mcp.govsec.kb_query(unit_id="KB-90DAY-WS-003", section="architecture")

# Example: Query Phase 4 technical tasks
phase4 = mcp.govsec.kb_query(unit_id="KB-90DAY-WS-003", phase="Phase 4")

# Example: Query MVP capabilities
mvp = mcp.govsec.kb_query(unit_id="KB-90DAY-WS-003", section="mvp")

# Example: Query compliance requirements
compliance = mcp.govsec.kb_query(unit_id="KB-90DAY-WS-003", section="compliance")
```

---

**Last Updated:** 2026-04-25 06:48 UTC  
**Next Review:** 2026-05-01 (Phase 1 Kickoff)  
**Retention Tier:** Operational (Active Daily Use)

#Technical
#Architecture
#Integration
#Deployment
#90DayPlan
#CSM
#Aras
#KB90Day
