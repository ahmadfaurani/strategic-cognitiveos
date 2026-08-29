# Ahmad Fuad — Comprehensive Strategic Profile

**Compiled:** 2026-08-29 | **Sources:** CognitiveOS records (STK-20260804-003 + 60+ records referencing Fuad), product baseline, action items, decisions, risks, commitments, conversation logs

---

## 1. Identity

- **Full Name:** Ahmad Fuad Bin Kamarazaman
- **Known as:** Fuad
- **Role:** Practice Technical Authority / Practice CTO — Cyber Security Practice, Aras Integrasi Sdn Bhd
- **Email:** ahmad.fuad@arasintegrasi.ai
- **Title:** Principal AI Security Architect
- **ISC2 Role:** ISC2 Malaysia Chapter Academic Director
- **Org Position:** CyberSecurity Practice (sovereign organization aligned with Farul as org CTO)

---

## 2. Organisational Architecture

| Dimension | Detail |
|-----------|--------|
| **Reports to** | DAF (Director, Cyber Security Practice) |
| **Practice role** | Practice CTO / Practice Technical Authority |
| **Org CTO** | Farul Mohd Ghazali (STK-20260803-006) — Fuad is NOT org CTO |
| **Infrastructure layer** | Teras AI Platform (Farul's domain); Fuad's products deploy ON Teras (DEC-20260820-009) |
| **Practice scope** | VoronCitadel, GovSec TIP, Skunkworks Division |
| **FTE capacity** | 2 FTE (Fuad + Syahir) — Technical Execution Unit. Fuad as technical authority, Syahir as POC/QC engineer. Capacity model revised Aug 29: the unit is 2 FTE, not 0.3 FTE solo. Load absorption depends on effective handover and workstream alignment (AIP-03). |

**Clarified by DAF (DEC-20260820-007, Aug 20):** Fuad is Practice CTO within the Cyber Security Practice. Farul is CTO of the whole stack. The CyberSecurity Practice is a sovereign organization aligned with the CTO.

---

## 3. Products Owned

### VoronCitadel (Flagship — Most Commercially Mature)
- **Status:** Production-deployed, live (v2.0, August 2026)
- **Maturity:** MVP complete — most commercially mature of 3 flagship products
- **Commercialisation Readiness:** Ready
- **Architecture:** React SPA + Express REST API + PostgreSQL (single-node Docker Compose)
- **AI:** Sovereign LLM (Qwen 3.5-27B via Aras) — no tenant data to foreign endpoints
- **4 capability domains:**
  1. GRC — Risk Register, Control Library, Policy Management, BCM, Incident Management, Operational Loss Database
  2. DRM — Asset Inventory, FAIR ALE Risk Quantification, Monte Carlo (50K iterations), Executive Analytics
  3. ASM (VoronScout) — External asset discovery, TLS/SSL assessment, exposure scoring, threat intel integration
  4. TPRM/TPRA — Vendor inventory, 5 assessment types, continuous monitoring (6-hourly), composite scoring (6 dimensions)
- **5 compliance frameworks:** ISO 27001:2022, SC GTRM, BNM RMiT, NIST CSF 2.0, NIST RMF
- **Bursa POC focus:** ITSS §10 Supplier Management — TPRM + federated compliance document checking
- **Commercial model:** Retail RM368k, early-adopter RM168k

### GovSec TIP (Flagship — Sovereign Threat Intelligence Platform)
- **Status:** Product roadmap delivered (Q3 2026–Q2 2027, 16 slides, Aug 17)
- **12 project cards across 4 quarters:**
  - Q3 2026: Productise & Pilot (production hardening, executive visualisation, feed quality, identity/MFA)
  - Q4 2026: Integrate & Govern (SIEM/ticketing, playbooks, exposure monitoring, RAG pipeline)
  - Q1 2027: Scale Analysis (AI threat hunting, CSM SOAR integration)
  - Q2 2027: Broaden Assurance (BYOK/HA, regulatory analytics)
- **Total effort estimate:** ~24–30 FTEs across all 12 projects
- **Q3 2026 progress:** On track
- **CSM integration:** CMERP (Suricata alerts → GovSec), SiberSUITE (telemetry → analytics → CBOM → score card)
- **Integration deliverables (Aug 13 consolidated):**
  1. GovSec Repository Setup — ET Pro format for CMERP ingestion (Insight Manager)
  2. CMERP Sensor Appliance Deployment — in Aras environment (pending management approval)
  3. Suricata Alert Push — CMERP pushes Suricata format alerts to GovSec

### Skunkworks Division
- R&D / emerging capability division (limited records, referenced in STK-20260804-003)

---

## 4. People Relationships

| Person | Relationship | Context |
|--------|-------------|---------|
| **DAF** | Reports to | Director, Cyber Security Practice. DAF delegates technical execution; retains commercial/governance authority |
| **Hadri** | Technical counterpart | Solutions Architect. Owns chain:SENTRY. Co-owns GovSec × CMERP integration coordination. Hadri consolidates, Fuad provides technical content |
| **Farul** | Org CTO | CTO of whole stack. Fuad's practice aligns with Farul's infrastructure layer (Teras) |
| **Syahir** | Ramp-up responsibility | POC Engineer + QC Engineer (DEC-20260818-007). Fuad owns ramp-up. Mitigates Fuad SPOF risk |
| **Amelia Nadia** | Colleague | SSE Lead, Strategic Stakeholder Engagement Lead (DEC-20260820-012) |
| **Azrul (CSM)** | Technical counterpart | CSM partnership anchor. Fuad to engage directly on Bursa POC technical execution (ACT-20260825-001) |

---

## 5. Active Assignments (As of Aug 29)

### Critical / In Progress

| # | Action | Status | Deadline | Priority |
|---|--------|--------|----------|----------|
| 1 | **GovSec × CMERP Gate 1** — Complete engineering comment closure | Active | T-35 (Aug 31) | High |
| 2 | **GovSec × CMERP Gate 3** — Confirm document technically complete | Active | T-34 (Sep 2) | High |
| 3 | **Bursa POC targeted development** — TPRM + federated compliance | In Progress | Sep 7 | Critical |
| 4 | **Direct technical engagement with Azrul** on Bursa POC | In Progress | Was Aug 28 | Critical |
| 5 | **VoronCitadel POC technical validation** (8-section Bursa doc) | Active | TBD | High |
| 6 | **Centralised product repository** for all 3 flagship products | Active | TBD | Critical |

### Draft / Overdue

| # | Action | Status | Priority |
|---|--------|--------|----------|
| 7 | Compile Product Roadmap for each flagship product | Draft | High |
| 8 | Compile Product Backlog for each flagship product | Draft | High |
| 9 | Communicate expanded dev freeze directive to DevSecOps intern | **Overdue** | Critical |
| 10 | Evaluate Defensia WAF & production-grade infrastructure hardening | Draft (deadline Aug 27) | High |
| 11 | Documentation drive — deadlines for all product documentation | Active | High |

### Completed

| # | Action | Completed |
|---|--------|-----------|
| 12 | GovSec Product Roadmap Q3 2026–Q2 2027 delivered (16 slides) | Aug 17, on deadline |
| 13 | ACT-20260817-007 — Follow up on GovSec Roadmap deliverable | Completed |
| 14 | ACT-20260816-001 — Stakeholder engagement briefs (Fuad brief included) | Completed |

---

## 6. Key Decisions Involving Fuad

| Decision | Date | Context |
|----------|------|---------|
| DEC-20260810-002 | Aug 10 | GovSec development freeze — minimise new features, focus on CyberDSA launch readiness |
| DEC-20260811-001 | Aug 11 | Expanded development freeze across all 3 flagship products |
| DEC-20260818-007 | Aug 18 | POC Engineer role delegated to Syahir — Fuad owns ramp-up |
| DEC-20260818-008 | Aug 18 | All Product Critical Documents (PCD) due Aug 28 — single deadline |
| DEC-20260820-007 | Aug 20 | Organisational architecture confirmed — Fuad as Practice CTO, Farul as org CTO |
| DEC-20260820-009 | Aug 20 | Teras as infrastructure layer for ALL products (VoronCitadel, GovSec, chain:SENTRY) |
| DEC-20260820-011 | Aug 20 | Documentation drive with deadlines for all product documentation |

---

## 7. Risks Associated with Fuad

### RSK-20260811-001 — Productisation Documentation Effort vs CyberDSA Delivery Capacity Contention
- **Status:** Completed/mitigated
- **Context:** Fuad carrying both productisation documentation load and CyberDSA delivery
- **Mitigation:** POC Engineer role delegated to Syahir

### RSK-20260820-003 — No Head of Engineering Blocks POC Scaling
- **Status:** Active, Critical
- **Context:** Current engineering capacity is ~0.3 FTE (Fuad only). Cannot run 6-7 POCs + 3 paying customers with 3 people and no dedicated engineering lead
- **Impact:** HoE is the gating hire for POC Mode activation

### RSK-20260824-001 — Bursa 4-Month POC Timeline Compression
- **Status:** Active, High
- **Context:** Bursa proposed 4-month timeline. VoronCitadel TPRM features and federated compliance need development within the window
- **Impact:** Timeline failure damages first CSM-channel POC and Bursa reference account

### RSK-20260824-003 — Interim Ownership Concentration on DAF
- **Status:** Active, High
- **Context:** DAF carrying 4 concurrent interim roles. Fuad at 0.3 FTE is the only engineering capacity — "one person's capacity away from stalling"

---

## 8. Commitments (Fuad as Receiving Stakeholder)

| Commitment | From | Expected Delivery | Status |
|------------|------|-------------------|--------|
| COM-20260810-002 | DAF → Fuad | Oct 1, 2026 | Active — GovSec dev freeze |
| COM-20260811-001 | DAF → Fuad | Oct 1, 2026 | Active — Expanded dev freeze across all 3 products |
| COM-20260827-001 (Gates 1 & 3) | Hadri's gate chain → Fuad | T-35 (Aug 31) + T-34 (Sep 2) | Active — Engineering comment closure + technical completion confirmation |

---

## 9. Engagement Timeline

| Date | Event |
|------|-------|
| Aug 4 | CC'd on GovSec × CMERP integration kickoff (Hadri → CSM) |
| Aug 8 | DAF requested product review of CMO Outreach Package — claims validation, diagnostic feasibility, demo readiness |
| Aug 10 | Post-meeting follow-up: GovSec × CSM SiberSUITE integration session. 3 collaboration areas defined (telemetry, score card, CBOM). Fuad designated technical coordinator alongside Hadri |
| Aug 10 | DAF issued GovSec development freeze directive (DEC-20260810-002) |
| Aug 11 | DAF expanded dev freeze across all 3 flagship products (DEC-20260811-001). Fuad assigned: centralised repo, roadmap, backlog, commercialisation docs, sales materials, product governance |
| Aug 11 | Fuad directed to communicate expanded dev freeze to DevSecOps intern (ACT-20260811-007) — **OVERDUE** |
| Aug 15 | CSM VoronCitadel training delivered. CSM product feedback received |
| Aug 17 | **Delivered GovSec Product Roadmap** (16 slides, Q3 2026–Q2 2027) — on deadline. Scheduled Syahir session for Aug 20 |
| Aug 18 | POC Engineer role delegated to Syahir. Fuad owns ramp-up (DEC-20260818-007). All PCDs due Aug 28 (DEC-20260818-008) |
| Aug 19 | DAF × Fuad meeting — commercial support model validation, technical team structure, PCD status, CyberDSA technical readiness. Claims validation delegated to Syahir as QC task |
| Aug 20 | Fuad's product baseline established as reference for VoronCitadel POC brief for Bursa |
| Aug 24 | DAF briefed Fuad directly on Bursa POC targeted development. Technical alignment completed. Focus locked to TPRM + federated compliance |
| Aug 25 | Fuad directed to initiate direct technical engagement with Azrul on Bursa POC (ACT-20260825-001) |
| Aug 26 | DAF T-40 CyberDSA directive — Fuad assigned: close all engineering comments (ACT-20260826-004), provide technical support |
| Aug 27 | Hadri's T-30 closure commitment accepted by DAF. Fuad owns Gate 1 (T-35, Aug 31) and Gate 3 (T-34, Sep 2) in the 6-step chain |
| Aug 27 | Fuad sent updated engineering document with flowcharts and diagrams (confirmed by Hadri in email) |
| Aug 29 | **Profile compiled** |

---

## 10. Strategic Assessment

### Strengths
- **Built 2 of 3 flagship products** — VoronCitadel (most commercially mature) and GovSec TIP
- **Deep technical authority** — product architecture, capability claims, demo readiness all require his validation
- **Delivered on deadline** — GovSec roadmap (Aug 17), engineering document update (Aug 27)
- **Sovereign AI alignment** — built VoronCitadel with sovereign LLM, no foreign endpoint dependency
- **ISC2 connection** — Academic Director role connects to university/academic ecosystem (CRC 2026 via Dr. Ji-Jian Chin)

### Constraints
- **~0.3 FTE capacity** — split across 2 flagship products + Syahir ramp-up + Skunkworks
- **Single point of failure** — RSK-20260811-001 (mitigated by Syahir delegation) and RSK-20260820-003 (HoE not hired)
- **Documentation backlog** — roadmap, backlog, commercialisation docs, sales materials all in draft status
- **Overdue items** — dev freeze communication to intern (ACT-20260811-007), Defensia WAF evaluation
- **Bursa POC pressure** — 4-month timeline with TPRM + federated compliance development still needed

### Critical Path
Fuad sits on **3 concurrent critical paths**:
1. **GovSec × CMERP engineering document** (Gates 1 + 3, T-35/T-34) → unblocks Wan Roshaimi activation, CyberDSA co-branding
2. **Bursa POC development** (TPRM + federated compliance) → first CSM-channel POC, Bursa reference account
3. **CyberDSA launch readiness** — product documentation, demo preparation, claims validation

### Hiring Dependencies
- **Head of Engineering** (RSK-20260820-003, ACT-20260820-007) — gates POC scaling. RM18,888/month. Not yet hired
- **Customer Success Engineer** (ACT-20260820-008) — RM11,888/month. Not yet hired
- **TBH-001 PM** — JD v2 committed (Aug 28), end-September hiring activation. DAF carries PM burden until then

---

## 11. Source Records

| Record | Type | Reference |
|--------|------|-----------|
| STK-20260804-003 | Stakeholder | Primary stakeholder record |
| CONV-20260804-002 | Conversation | GovSec × CMERP integration kickoff |
| CONV-20260810-001 | Conversation | GovSec × CSM SiberSUITE integration session |
| CONV-20260811-001 | Conversation | Expanded dev freeze directive |
| CONV-20260817-003 | Conversation | GovSec Product Roadmap delivery |
| CONV-20260826-002 | Conversation | T-40 CyberDSA directive thread |
| CONV-20260827-001 | Conversation | Hadri's T-30 closure commitment |
| COM-20260810-002 | Commitment | GovSec dev freeze |
| COM-20260811-001 | Commitment | Expanded dev freeze |
| COM-20260827-001 | Commitment | T-30 closure gate chain |
| DEC-20260810-002 | Decision | GovSec dev freeze |
| DEC-20260811-001 | Decision | Expanded dev freeze |
| DEC-20260818-007 | Decision | Syahir POC Engineer delegation |
| DEC-20260818-008 | Decision | PCD single deadline |
| DEC-20260820-007 | Decision | Organisational architecture |
| DEC-20260820-009 | Decision | Teras as infra layer |
| RSK-20260811-001 | Risk | Documentation vs delivery contention |
| RSK-20260820-003 | Risk | No HoE — blocks POC scaling |
| RSK-20260824-001 | Risk | Bursa timeline compression |
| RSK-20260824-003 | Risk | DAF interim ownership concentration |
| ACT-20260824-001 | Action | Bursa POC targeted development |
| ACT-20260825-001 | Action | Direct Azrul engagement |
| ACT-20260827-004 | Action | Gate 1 — engineering comment closure |
| ACT-20260827-006 | Action | Gate 3 — technical completion confirmation |
| DOC-20260821-004 | Document | GovSec Product Roadmap Q3 2026–Q2 2027 |
| PRODUCT_BASELINE.md | Product | VoronCitadel v2.0 product baseline |

---

*This profile is a CognitiveOS analytical compilation. All claims are sourced from CognitiveOS records. Confidence: HIGH based on record density (60+ records, 25+ direct actions).*
