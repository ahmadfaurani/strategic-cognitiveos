---
id: INT-20260907-001
record_type: intelligence
title: "PIR Collection: CSCDC Leadership & Approval Watch — 2026-09-07"
created_at: 2026-09-07T01:01:00+08:00
updated_at: 2026-09-07T01:01:00+08:00
owner: DAF
status: draft
priority: critical
sensitivity: confidential
lifecycle_state: candidate
confidence: medium
tags:
  - intelligence/cron-output
  - workstream/cscdc-partnership
source:
  type: osint
  reference: "Inline web_search + web_extract (DeerFlow ultra timeout fallback) — 2026-09-07"
summary: "Post-pause collection cycle (34-day gap). Key new findings: (1) CSM Board of Directors restructured under Ministry of Digital with new Chairman Al-Ishsal Ishak; (2) MyKriptografi Action Plan 2026-2030 launched at NCSS 2026 with 12 strategies/32 programmes/80 activities; (3) NACSA cyber attack alert Aug 28; (4) 34th Cyber Security Summit Malaysia Sep 10 features NACSA speaker; (5) CSM 2026 procurement expanded. CSCDC dedicated CEO and CCO remain unconfirmed."
strategic_significance: "CSM's move under Ministry of Digital creates a dual-reporting structure (CSCDC under JPM/MKN/NACSA, CSM under MoD) that may affect the consolidation timeline and engagement path. MyKriptografi Action Plan directly operationalises the PQC Sandbox PIR. NACSA's active alert posture signals elevated threat environment relevant to CSCDC War Room activation."
mission_alignment:
  - mission/intelligence-enablement
related_records:
  - STK-20260725-001
  - INIT-20260725-007
intelligence_type: leadership-mapping
evidence:
  - "CSM Board of Directors restructured: Chairman Al-Ishsal Ishak, Director/Secretary General Ministry of Digital Datuk Fabian Bigar (Source: cybersecurity.my/portal-main/about-us/board-of-directors, accessed 7 Sep 2026)"
  - "MyKriptografi Action Plan 2026-2030 launched at NCSS 2026: 4 pillars, 12 strategies, 32 programmes, 80 activities (Source: nacsa.gov.my/pelan-tindakan-mykriptografi.php; Bernama id=2577743, 7 Jul 2026)"
  - "NACSA issued cyber attack alert Aug 28 2026: intrusions, DDoS, web defacement, malware targeting government and private organisations (Source: securitystudies.info Malaysia Report Sep 4 2026)"
  - "34th Cyber Security Summit Malaysia 2026: Sep 10, InterContinental KL, NACSA speaker Nuraishah Mokhtar confirmed (Source: prnewswire.com, 1 Sep 2026)"
  - "KSN Shamsul Azri active on AI in public sector: Sep 3 2026 Bernama speech on AI productivity paradox (Source: bernama.com id=2602628)"
  - "CSM 2026 procurement: 9 new tenders (SH/01-09/2026), including SH/09/2026 Group Term Takaful currently bidding (Source: cybersecurity.my/portal-main/procurement)"
  - "NC4 threat level LOW as of 7 Sep 2026 01:00; latest advisories: WordPress wp2shell (24 Jul), Joomla CVE-2026-48908 (1 Jul), Joomla JCE CVE-2026-48907 (26 Jun) (Source: nc4.gov.my)"
implications:
  - "CSM Board under Ministry of Digital (MoD) creates potential reporting complexity — CSCDC consolidates CSM functions under JPM, but CSM's board now reports to MoD. This may slow consolidation or create dual authority."
  - "MyKriptografi Action Plan 2026-2030 provides the implementation roadmap for PQC Sandbox — 4 pillars include Pillar 3 (PKTN adoption) and Pillar 4 (RDCI for quantum era). This is the most direct OSINT evidence for PIR-CSCDC-006."
  - "NACSA's Aug 28 cyber attack alert + Prasarana ransomware (Aug 25) creates urgency context for CSCDC War Room activation (PIR-CSCDC-007) — but no public evidence of CSCDC-specific War Room protocol."
  - "Cyber Security Summit Sep 10 with NACSA speaker is a potential intelligence collection opportunity — Nuraishah Mokhtar (Senior Principal Assistant Director, NACSA) may speak to CSCDC-related initiatives."
  - "No dedicated CSCDC CEO or CCO appointment publicly announced as of 7 Sep 2026 — 95 days since CSCDC launch (4 Jun). The 90-day mobilisation window has likely elapsed or is elapsing without public disclosure of key operational leadership."
open_questions:
  - "Has CSCDC framework v2.0 been formally approved? No public announcement found — 90-day clock status unknown."
  - "Is CSM's move under Ministry of Digital a parallel to or replacement of CSCDC consolidation? The CSM Board page says 'under the purview of the Ministry of Digital' — this may indicate CSM retains separate institutional identity even as CSCDC consolidates functions."
  - "Who is the dedicated CSCDC CEO? Roshdi Ahmad remains 'Acting CEO of CSM' (not CSCDC) 8 months into acting role."
  - "Has the CCO position been advertised through SPA (Suruhanjaya Perkhidmatan Awam) or JPA? No public advertisement found."
  - "Does the MyKriptografi Action Plan 2026-2030 contain specific PQC Sandbox launch timelines? Full document downloadable from NACSA but not extracted this cycle."
recommended_actions:
  - "Extract MyKriptografi Action Plan 2026-2030 PDF (nacsa.gov.my/pelan-tindakan-mykriptografi-download.php) for PQC Sandbox timeline details — directly addresses PIR-CSCDC-006"
  - "Monitor Cyber Security Summit Malaysia 2026 (Sep 10) outputs for CSCDC/NACSA leadership statements"
  - "Investigate CSM-Ministry of Digital reporting structure implications for CSCDC consolidation — may require updating STK-20260725-001"
  - "Check SPA/JPA vacancy portal for CCO position advertisement"
  - "Continue monitoring for dedicated CSCDC CEO appointment — 90-day mobilisation window likely closing"
related_initiatives:
  - INIT-20260725-007
related_stakeholders:
  - STK-20260725-001
---

# CSCDC Leadership & Approval Watch — Intelligence Report

**Agent:** CSCDC-01 PIR Collection Orchestrator (DeerFlow fallback → inline collection)
**Collection Cycle:** 2026-09-07 01:01 MYT (Asia/Kuala_Lumpur, UTC+8)
**Classification:** OSINT / Open-Source Intelligence
**Scope:** CSCDC leadership mapping, decision authority, framework approval status, budget, procurement, PQC Sandbox, competitive landscape
**Collection Gap:** 34 days since last cycle (2026-08-04) — first post-pause collection

**⚠️ DEERFLOW_DISPATCH_FAILED — falling back to inline collection.**
DeerFlow ultra mode dispatched successfully (thread created: 6e425d8d-fcb4-41e6-b539-f72f78ffba9a) but the streaming response timed out at 900s curl limit. Only 149 bytes of planning text were captured before timeout. Inline web_search + web_extract used per fallback hierarchy (Secondary tier).

---

## Executive Summary

This is the first CSCDC-01 collection cycle since the Aug 4 pause — a 34-day intelligence gap. Key findings: **CSM's Board of Directors has been restructured under the Ministry of Digital** (Chairman: Al-Ishsal Ishak; MoD Secretary General Datuk Fabian Bigar as Director), creating a potential dual-reporting complexity with CSCDC's JPM/MKN/NACSA governance chain. **MyKriptografi Action Plan 2026-2030** was launched at NCSS 2026 (7 Jul) with 4 pillars, 12 strategies, 32 programmes, and 80 activities — directly operationalising the National Cryptography Policy and providing the implementation roadmap for the PQC Sandbox. **NACSA issued a cyber attack alert** on Aug 28 covering intrusions, DDoS, web defacement, and malware targeting government and private organisations. The **34th Cyber Security Summit Malaysia 2026** on Sep 10 features a NACSA speaker (Nuraishah Mokhtar). **No dedicated CSCDC CEO or CCO** has been publicly named 95 days post-launch. CSM's 2026 procurement programme has expanded with 9 new tenders. The NC4 threat level stands at LOW as of 7 Sep 2026.

---

## PIR Findings

### PIR-CSCDC-001: Leadership Mapping [CRITICAL — PARTIALLY RESOLVED]
- **Priority:** Critical
- **Status:** PARTIALLY RESOLVED (unchanged from Aug 4)
- **Finding:** No NEW dedicated CSCDC CEO or CCO appointment found in public sources as of 7 Sep 2026. Previously verified leadership remains unchanged:
  - Board Chairman: KSN Tan Sri Shamsul Azri Abu Bakar [VERIFIED — confirmed active Sep 3 2026, Bernama]
  - NACSA CEO: Ir. Dr. Megat Zuhairy Megat Tajuddin [VERIFIED — NACSA portal live 7 Sep 2026]
  - MKN DG: YM Raja Dato' Nushirwan Zainal Abidin [VERIFIED — NCSS 2026]
  - CSM Acting CEO: Roshdi bin Haji Ahmad [VERIFIED — no permanent appointment announcement found]
  - PTPKM Director: Datuk Prof. Dr. Muhammad Rezal Kamel Ariffin [VERIFIED]
  - Dedicated CSCDC CEO: NOT publicly named [UNVERIFIED — 95 days post-launch]
  - Acting CCO: NOT publicly identified [UNVERIFIED]

- **NEW Finding — CSM Board of Directors Restructured:**
  CSM's Board of Directors page (accessed 7 Sep 2026) now lists a restructured board **under the Ministry of Digital**:
  - **Chairman:** Al-Ishsal Bin Prof. Dato' Ishak T. Kechik
  - **Director/Secretary General, Ministry of Digital:** Datuk Fabian Bigar
  - **Directors:** Derek John Fernandez, Norhayati Binti Masah, Datuk Haji Rostam Affendi Bin Dato' Haji Salleh, Dato' Sri Mohd Kamarudin Bin Md Din
  - The page states: "CyberSecurity Malaysia is the national cyber security specialist agency under the purview of the Ministry of Digital"

  This is a **significant structural development** — CSM was previously under JPM. The move to Ministry of Digital creates a potential dual-reporting structure: CSCDC consolidates CSM functions under JPM/MKN/NACSA, but CSM's governance board now reports to MoD. This may affect the consolidation timeline, procurement authority, and engagement path.

- **Source:** https://www.cybersecurity.my/portal-main/about-us/board-of-directors (accessed 7 Sep 2026); https://www.bernama.com/en/general/news.php?id=2602628 (KSN active Sep 3 2026)
- **Confidence:** HIGH (CSM Board fact, direct from official portal); MEDIUM (inference on dual-reporting impact)
- **Tag:** [VERIFIED] (leadership confirmations) / [NEW FINDING] (CSM Board restructuring)

---CVS BLOCK---
Claim: CSM Board of Directors is now under the Ministry of Digital, with Chairman Al-Ishsal Ishak and MoD Sec-Gen Datuk Fabian Bigar as Director
Source: cybersecurity.my/portal-main/about-us/board-of-directors (official CSM portal, accessed 7 Sep 2026)
Source Level: L1 (official government portal)
Tier: T2
Validation Status: Partially Verified (official portal, but implications for CSCDC not confirmed)
Confidence Score: 7 (Authority:2, Traceability:2, Recency:2, Consistency:1, Completeness:0)
Action Required: Human review — investigate CSM-MoD vs CSCDC-JPM reporting structure
---END CVS BLOCK---

### PIR-CSCDC-002: Approval Timeline [CRITICAL — OPEN — OSINT-UNRESOLVABLE]
- **Priority:** Critical
- **Status:** OPEN (unchanged)
- **Finding:** No public disclosure of framework v2.0 formal approval date or 90-day mobilisation clock start. The framework v2.0 final draft (10 Jul 2026) remains an internal instrument. If the 90-day clock started at the 4 Jun 2026 launch, it would have elapsed by ~3 Sep 2026 — meaning the mobilisation window may have already closed without public disclosure.
- **Source:** Web searches — no CSCDC-specific framework approval results
- **Confidence:** LOW (absence of evidence)
- **Tag:** [UNVERIFIED] — OSINT-unresolvable, internal instrument

### PIR-CSCDC-003: Budget Confirmation [HIGH — OPEN]
- **Priority:** High
- **Status:** OPEN (unchanged)
- **Finding:** No public OBB/Treasury confirmation of the RM 4,005,000 Phase 1 budget found. Budget Belanjawan 2026 (Oct 2025) announced CSCDC formation and allocated RM12M for NSRC enhancement and RM20M for digital forensics, but no CSCDC communication division budget line identified.
- **Source:** https://www.utusan.com.my/nasional/2025/10/belanjawan-2026-kerajaan-mahu-gubal-ruu-jenayah-siber/ (Utusan, Oct 2025); https://www.buletintv3.my/nasional/rm12-juta-perkasa-kecekapan-nsrc-rm20-juta-digital-forensik/
- **Confidence:** LOW
- **Tag:** [UNVERIFIED]

### PIR-CSCDC-004: CCO Appointment Status [HIGH — OPEN]
- **Priority:** High
- **Status:** OPEN (unchanged)
- **Finding:** No public CCO advertisement, shortlist, or appointment found. The CEO role remains "acting" (Roshdi Ahmad) 8 months on (Jan 14 → Sep 7 2026). No SPA/JPA vacancy for CCO position found in open search. The CCO position (Jusa C/B, RM 18K/month) appears to remain unfilled or is being filled through internal/non-public channels.
- **Source:** Web searches — no CCO-specific results
- **Confidence:** LOW (absence of evidence)
- **Tag:** [UNVERIFIED]

### PIR-CSCDC-005: Infrastructure Procurement Plan [HIGH — OPEN]
- **Priority:** High
- **Status:** OPEN — CSM procurement data updated
- **Finding:** CSM procurement portal (accessed 7 Sep 2026) shows **9 new 2026 tenders** (SH/01/2026 through SH/09/2026):
  - SH/01/2026: Integrated Business Process Management System (IBPMS) — **Awarded**
  - SH/02/2026: HCL Domino Collaboration Software — **Awarded**
  - SH/03/2026: VAPT Software — **Awarded**
  - SH/04/2026: Laptops for Assessment — **Aborted**
  - SH/05/2026: DPTech Firewall/iPS & Switches Maintenance — **Awarded**
  - SH/06/2026: Endpoint Computing Hardware and Software — **Evaluation**
  - SH/07/2026: IT & OT Lab Software — **Aborted**
  - SH/08/2026: IT & OT Lab Hardware — **Evaluation**
  - SH/09/2026: Group Term Takaful Coverage — **Bidding**
  - No active tenders/quotation advertisements at time of access ("Tiada tender / sebutharga pada ketika ini")

  **Assessment:** No CSCDC-specific procurement notices found. CSM procurement remains the only active official vendor channel. The IT & OT Lab Hardware/Software tenders (SH/07/2026, SH/08/2026) may relate to CSCDC infrastructure build-out but are labelled as CSM procurements. No social listening, content studio, or encrypted portal procurement found — these remain the identified gaps.
- **Source:** https://www.cybersecurity.my/portal-main/procurement (accessed 7 Sep 2026)
- **Confidence:** HIGH (procurement data); MEDIUM (inference on CSCDC connection)
- **Tag:** [VERIFIED] (CSM procurement); [UNVERIFIED] (CSCDC-specific procurement)

---CVS BLOCK---
Claim: CSM has 9 new 2026 procurement items including IT/OT Lab Hardware (SH/08/2026, Evaluation) and IT/OT Lab Software (SH/07/2026, Aborted)
Source: cybersecurity.my/portal-main/procurement (official CSM portal, accessed 7 Sep 2026)
Source Level: L1 (official government procurement portal)
Tier: T2
Validation Status: Verified (procurement listing); Inferred (connection to CSCDC)
Confidence Score: 7 (Authority:2, Traceability:2, Recency:2, Consistency:1, Completeness:0)
Action Required: Monitor SH/06/2026 and SH/08/2026 for CSCDC infrastructure connection
---END CVS BLOCK---

### PIR-CSCDC-006: PQC Sandbox Architecture & Timeline [HIGH — PARTIALLY RESOLVED]
- **Priority:** High
- **Status:** PARTIALLY RESOLVED (UPGRADED from OPEN)
- **Finding — MyKriptografi Action Plan 2026-2030:**
  NACSA launched the MyKriptografi Action Plan 2026-2030 at NCSS 2026 (7 Jul 2026). The Action Plan:
  - **4 Core Pillars:** (1) Data protection for Government/NCII/individuals, (2) Human capital development in cryptographic technology, (3) PKTN adoption among NCII entities and industry, (4) RDCI for quantum computing era
  - **12 strategies, 32 programmes, 80 activities**
  - Explicitly mentions "preparing Malaysia for emerging cybersecurity challenges, including the quantum computing era"
  - Pillar 4 directly addresses PQC: "Empowering the sustainability of national cybersecurity through the strengthening of Research, Development, Commercialisation, and Innovation (RDCI) in the field of cryptographic technology"

  Additionally, NCSS 2026 also launched the **Artificial Intelligence Systems Cybersecurity Framework (AISCF)** — NACSA's framework for AI cybersecurity risks including data poisoning, prompt injection, adversarial attacks, model theft, and AI supply chain compromise.

  CSM's services page lists a dedicated **Post-Quantum Cryptography Initiatives** service line (cybersecurity.my/portal-main/services/post-quantum-overview), confirming PQC as an active operational programme.

- **Source:** https://www.nacsa.gov.my/pelan-tindakan-mykriptografi.php (NACSA official); https://www.bernama.com/en/news.php?id=2577743 (Bernama, 7 Jul 2026); https://www.nacsa.gov.my/ai_systems_cyber_security_framework.php
- **Confidence:** HIGH (Action Plan existence and structure); MEDIUM (specific PQC Sandbox timeline — full PDF not extracted)
- **Tag:** [VERIFIED] (Action Plan launch); [PARTIALLY VERIFIED] (PQC Sandbox specifics)
- **GAP:** Full MyKriptografi Action Plan PDF not extracted — may contain PQC Sandbox launch timeline. Recommend extraction next cycle.

---CVS BLOCK---
Claim: NACSA launched MyKriptografi Action Plan 2026-2030 at NCSS 2026 on 7 Jul 2026, with 4 pillars/12 strategies/32 programmes/80 activities including quantum computing era preparation
Source: nacsa.gov.my/pelan-tindakan-mykriptografi.php (official NACSA portal); Bernama id=2577743 (7 Jul 2026)
Source Level: L1 (official government portal + national wire)
Tier: T2
Validation Status: Partially Verified (launch confirmed; full document not extracted)
Confidence Score: 7 (Authority:2, Traceability:2, Recency:1, Consistency:2, Completeness:0)
Action Required: Extract full Action Plan PDF for PQC Sandbox timeline
---END CVS BLOCK---

### PIR-CSCDC-007: War Room Activation Protocol [MEDIUM — OPEN]
- **Priority:** Medium
- **Status:** OPEN (unchanged)
- **Finding:** No public disclosure of CSCDC War Room activation protocol. However, NACSA's Aug 28 cyber attack alert (intrusions, DDoS, web defacement, malware targeting government and private organisations) and the Prasarana ransomware attack (Aug 25, RansomHub) create an elevated threat context. The NC4 (National Cyber Coordination and Command Centre) threat level is LOW as of 7 Sep 2026, with active advisories on WordPress wp2shell, Joomla CVEs. NC4 is the operational arm — CSCDC's War Room would interface with NC4 for crisis escalation.
- **Source:** https://www.securitystudies.info/country/malaysia/reports/malaysia-report-2026-09-04-0640/ (SecurityStudies.info, 4 Sep 2026); https://www.nc4.gov.my/ (NC4 portal, 7 Sep 2026)
- **Confidence:** MEDIUM (threat context); LOW (War Room protocol specifics)
- **Tag:** [VERIFIED] (threat environment); [UNVERIFIED] (War Room protocol)

### PIR-CSCDC-008: Community Champions Programme Design [MEDIUM — OPEN]
- **Priority:** Medium
- **Status:** OPEN (unchanged)
- **Finding:** No CSCDC-specific Community Champions curriculum found. However, NACSA operates related public-facing programmes:
  - **My Cyber Hero (MYCH) 2026:** National education initiative for primary and secondary school students on cybersecurity competency
  - **CyberSAFE Program:** CSM's cyber safety awareness programme with L.I.V.E Gallery
  - **NACSA Cyber Games 2025:** 120 participants from 40 countries (May 20-23, 2025, KL), co-organised with Council of Europe and INTERPOL
  
  These are adjacent programmes but not the CSCDC Community Champions programme (1,000 champions, RM 200K). The CSCDC programme design remains internal.
- **Source:** https://www.nacsa.gov.my/my-cyberHero.php (NACSA); https://www.nacsa.gov.my/cyber_games_2025.php (NACSA); https://www.cybersecurity.my/portal-main/services/cyber-security-awareness-program-overview (CSM)
- **Confidence:** MEDIUM (adjacent programmes exist); LOW (CSCDC programme design)
- **Tag:** [VERIFIED] (adjacent programmes); [UNVERIFIED] (CSCDC-specific design)

### PIR-CSCDC-009: Inter-Agency Channel Relationships [MEDIUM — OPEN]
- **Priority:** Medium
- **Status:** OPEN (unchanged)
- **Finding:** No new information on CSCDC inter-agency communication relationships with MCMC, JAPEN, RTM, Bernama. The NC4 portal confirms NACSA's coordination role through NC4. CSM's collaboration programme (CSM-CP) exists as a vendor/academic collaboration framework. The NACSA-MKN-JPM chain remains the confirmed governance structure.
- **Source:** https://www.nc4.gov.my/ (NC4 portal); https://www.nacsa.gov.my/ (NACSA portal)
- **Confidence:** LOW
- **Tag:** [UNVERIFIED]

### PIR-CSCDC-010: Competitor / Incumbent Mapping [HIGH — OPEN]
- **Priority:** High
- **Status:** OPEN (unchanged)
- **Finding:** No named PR/communications vendor for CSCDC found. CSM procurement shows tech vendors (HCL, Microsoft, DPTech, Dell, Elastic, Sangfor) but no PR/strategic communications consultancy. The 34th Cyber Security Summit Malaysia 2026 (Sep 10, InterContinental KL) is organised by **Exito Media Concepts** (a B2B events company, not a strategic comms partner). Confirmed summit speakers include NACSA's Nuraishah Mokhtar (Senior Principal Assistant Director) — indicating NACSA's active participation in industry events but not a vendor relationship.
- **Source:** https://www.prnewswire.com/apac/news-releases/malaysias-cybersecurity-leaders-to-convene-at-the-34th-edition-cyber-security-summit-malaysia-2026-302866158.html (PR Newswire, 1 Sep 2026); https://www.cybersecurity.my/portal-main/procurement
- **Confidence:** LOW (no PR vendor found)
- **Tag:** [UNVERIFIED]

---

## Cross-PIR Synthesis

**Theme 1: Governance Complexity Increasing.** The CSM Board restructuring under Ministry of Digital creates a dual-track governance structure. CSCDC consolidates CSM functions under JPM/MKN/NACSA, but CSM's institutional board now reports to MoD (Secretary General Datuk Fabian Bigar is a CSM Director). This may mean: (a) CSM retains institutional identity as a MoD agency while CSCDC absorbs its operational functions, or (b) the MoD role is transitional during consolidation. Either way, the engagement path now has an additional node: MoD Secretary General.

**Theme 2: Cryptography Policy Operationalised.** The MyKriptografi Action Plan 2026-2030 is the most significant new intelligence product. It directly operationalises the National Cryptography Policy (Cabinet-approved 28 Nov 2025) into 12 strategies and 80 activities. Pillar 4 (RDCI for quantum era) is the PQC Sandbox's policy anchor. The AISCF launch alongside it creates a dual framework covering both cryptography and AI cybersecurity — positioning CSCDC/NACSA at the intersection of post-quantum and AI governance.

**Theme 3: Threat Environment Elevated.** NACSA's Aug 28 cyber attack alert, the Prasarana ransomware attack (Aug 25, RansomHub), and RM28.67M in QR code scam losses (H1 2026) create an elevated threat context. This increases the urgency of CSCDC's War Room and crisis communication functions but no public evidence shows CSCDC has activated these capabilities yet.

**Theme 4: Mobilisation Window Likely Elapsing.** If the 90-day mobilisation clock started at the 4 Jun 2026 launch, it elapsed ~3 Sep 2026. Without a dedicated CEO or CCO, key mobilisation milestones may be unmet or being met internally without public disclosure. This is a critical watch item.

---

## PIR Resolution Status Table

| PIR ID | Priority | Previous Status (Aug 4) | Current Status (Sep 7) | Confidence | New Intel? |
|--------|----------|------------------------|------------------------|------------|------------|
| PIR-CSCDC-001 | CRITICAL | Partially Resolved | **Partially Resolved** (CSM Board restructured — new finding) | HIGH | YES |
| PIR-CSCDC-002 | CRITICAL | Open (OSINT-unresolvable) | **Open** (OSINT-unresolvable) | LOW | NO |
| PIR-CSCDC-003 | HIGH | Open | **Open** | LOW | NO |
| PIR-CSCDC-004 | HIGH | Open | **Open** (8 months acting, no CCO) | LOW | NO |
| PIR-CSCDC-005 | HIGH | Open | **Open** (CSM 2026 procurement updated, no CSCDC-specific) | MEDIUM | YES |
| PIR-CSCDC-006 | HIGH | Open | **Partially Resolved** (MyKriptografi Action Plan 2026-2030 launched) | HIGH | YES |
| PIR-CSCDC-007 | MEDIUM | Open | **Open** (threat context updated, protocol still internal) | LOW | YES |
| PIR-CSCDC-008 | MEDIUM | Open | **Open** (adjacent programmes mapped, CSCDC-specific still internal) | LOW | YES |
| PIR-CSCDC-009 | MEDIUM | Open | **Open** | LOW | NO |
| PIR-CSCDC-010 | HIGH | Open | **Open** (no PR vendor found, Summit organiser identified) | LOW | YES |

---

## Intelligence Gaps

1. **Dedicated CSCDC CEO identity** — 95 days post-launch, no public appointment
2. **CCO appointment status** — no advertisement, shortlist, or appointment found
3. **Framework v2.0 approval date** — internal instrument, 90-day clock status unknown
4. **CSCDC-specific procurement** — no social listening, content studio, or encrypted portal tenders
5. **CSM-MoD vs CSCDC-JPM reporting structure** — new ambiguity from CSM Board restructuring
6. **PQC Sandbox technical architecture** — MyKriptografi Action Plan PDF not extracted
7. **War Room activation protocol** — internal, not public
8. **Community Champions curriculum** — CSCDC-specific design not public
9. **Inter-agency communication MOUs** — not public

---

## TOP 3 PIR SUGGESTIONS FOR NEXT CYCLE

1. **Suggestion:** Extract and analyse MyKriptografi Action Plan 2026-2030 PDF for PQC Sandbox launch timeline and industry engagement model
   **Rationale:** The Action Plan (12 strategies, 80 activities) is the most direct policy document for PIR-CSCDC-006. Pillar 4 (RDCI for quantum era) likely contains PQC Sandbox milestones.
   **Search Queries:** "MyKriptografi Action Plan 2026-2030 PQC sandbox", site:nacsa.gov.my "post-quantum", "NACSA PQC sandbox launch timeline"

2. **Suggestion:** Monitor Cyber Security Summit Malaysia 2026 (Sep 10) outputs for CSCDC/NACSA leadership statements and programme announcements
   **Rationale:** NACSA speaker Nuraishah Mokhtar (Senior Principal Assistant Director) may reveal CSCDC operational details. Summit theme "Identity, Intelligence & Resilience" aligns with CSCDC mandate.
   **Search Queries:** "Cyber Security Summit Malaysia 2026 NACSA speech", "Nuraishah Mokhtar NACSA CSCDC", "exito cybersecurity summit malaysia 2026 outcomes"

3. **Suggestion:** Investigate CSM-Ministry of Digital reporting structure and implications for CSCDC consolidation
   **Rationale:** CSM Board page says "under the purview of the Ministry of Digital" — this may indicate CSM retains separate identity or is transitional. This affects engagement path (PIR-INIT-CSCDC-002) and decision authority (PIR-INIT-CSCDC-001).
   **Search Queries:** "CyberSecurity Malaysia Ministry of Digital 2026", "Datuk Fabian Bigar Ministry of Digital cybersecurity", "CSM CSCDC Ministry Digital reporting structure"

---

*Report generated 2026-09-07 01:01 MYT by CSCDC-01 PIR Collection Orchestrator (cron, DeerFlow fallback mode). All timestamps Asia/Kuala_Lumpur (UTC+8).*

*CVS Note: DeerFlow ultra dispatch timed out at 900s. Inline collection via web_search + web_extract used per fallback hierarchy (Secondary tier). All claims sourced. Rule 6 applied — AI max tier T2, max confidence 7.*

---

---CVS BLOCK---
Claim: DeerFlow ultra mode dispatch timed out at 900s curl limit; only 149 bytes of planning text captured before timeout
Source: /tmp/pir-CSCDC-01-output.txt (DeerFlow dispatch output, 7 Sep 2026)
Source Level: L5 (AI-generated output / system log)
Tier: T2
Validation Status: Verified (system log confirms timeout)
Confidence Score: 7 (Authority:2, Traceability:2, Recency:2, Consistency:1, Completeness:0)
Action Required: None — fallback to inline collection executed per protocol
---END CVS BLOCK---
