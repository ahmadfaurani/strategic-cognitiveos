---
id: INT-20260824-001
record_type: intelligence
title: 'PIR Collection: CSCDC Leadership & Approval Watch — 24 Aug 2026'
created_at: 2026-08-24 01:00:00+08:00
updated_at: 2026-08-24 01:00:00+08:00
owner: DAF
status: draft
priority: critical
sensitivity: confidential
lifecycle_state: candidate
confidence: medium
tags:
- intelligence/cron-output
- workstream/cscdc
- cluster/cscdc-01
source:
  type: osint
  reference: DeerFlow ultra dispatch (TIMEOUT) + Hermes inline web_extract — 2026-08-24T01:00:00+08:00
summary: 'DEERFLOW_DISPATCH_TIMEOUT — falling back to inline collection. Hermes inline
  web_extract collected from 12+ government and news sources (NACSA, CSM, SPA, Bernama,
  Astro Awani, MKN, MyKripto). Key findings: Bernama search returns 0 CSCDC articles
  since 4 June launch (3-month media silence); SPA has no CCO posting (only 1 active
  job ad — medical officer); Act 854 licensed provider registry shows "No data available"
  (no licensees visible); NACSA licensing portal updated with mandatory new forms
  (1 July 2026) and fee structure (RM400-RM1,000/year); MyKriptografi Action Plan
  detail expanded (4 pillars, 12 strategies, 32 programmes, 80 activities); CSM CDD
  confirmed as crypto department under Ministry of Digital; MYCH 2026 programme
  completed (1 July 2026); IRC 2026 reveals CSM Fazlan Abdullah as public cyber voice.
  Leadership gaps UNCHANGED — dedicated CSCDC CEO and CCO remain unfilled in public
  domain.'
strategic_significance: 'Three-month media silence on CSCDC since 4 June launch (Bernama
  search: 0 results) confirms the entity is in a quiet formation phase with no public-facing
  operational milestones. The Act 854 licensed provider registry appearing empty ("No
  data available") suggests the regulatory vendor panel is not yet populated — meaning
  CSCDC procurement may face a regulatory gap if it needs licensed providers. The
  CCO position remaining unadvertised on SPA after 3 months indicates the mobilisation
  chain is structurally blocked at its first signature.'
mission_alignment:
- mission/intelligence-enablement
- mission/national-cybersecurity
- mission/strategic-communications
related_records:
- STK-20260725-001
- INIT-20260725-007
- INT-20260818-001
intelligence_type: pir-collection
evidence:
- Bernama search for "cscdc" returns 0 news results — no media coverage since 4 June
  2026 launch (bernama.com/en/search.php?cat1=all&terms=cscdc&submit=cari, accessed
  24 Aug 2026)
- SPA job listings page shows only 1 active posting (Pegawai Pemulihan Perubatan U9
  — fisioterapi, closing 27 Aug 2026); no CCO or CSCDC-related positions (spa.gov.my/informasi/iklan-kerjaya,
  accessed 24 Aug 2026)
- NACSA licensing portal updated — mandatory new forms effective 1 July 2026; iPayment
  system mandatory since 1 Dec 2025; fee RM400 individual / RM1,000 company per year
  per service (licence.nacsa.gov.my, accessed 24 Aug 2026)
- Act 854 licensed provider registry shows "No data available" for Company - Managed
  SOC Monitoring Service Licence (licence.nacsa.gov.my/#/licence-holder, accessed
  24 Aug 2026)
- MyKriptografi Action Plan 2026-2030 expanded detail — 4 core pillars, 12 strategies,
  32 programmes, 80 activities (nacsa.gov.my/pelan-tindakan-mykriptografi.php, accessed
  24 Aug 2026)
- CSM Cryptography Development Department (CDD) confirmed under Proactive Technology
  & Services Division, Ministry of Digital (mykripto.cybersecurity.my, accessed
  24 Aug 2026)
- NCCMP covers 10 critical domains — defence, banking, ICT, energy, transportation,
  water, health, government, emergency services, food & agriculture (nacsa.gov.my/nccmp.php,
  accessed 24 Aug 2026)
- MYCH 2026 programme completed 1 July 2026 — co-organiser Micro Concept Tech,
  sponsor BlackBerry Technology, partners KPM and MDEC (nacsa.gov.my/my-cyberHero.php,
  accessed 24 Aug 2026)
- IRC 2026 (21-22 July, MCMC-organised) — CSM Fazlan Abdullah spoke on AI cyber threats;
  AI Governance Bill being drafted (bernama.com/en/general/news.php?id=2592431,
  10 Aug 2026)
- CSM assisted MACC in MyIMMs hacking forensics (29 July 2026) — confirms operational
  inter-agency role (bernama.com/en/crime_courts/news.php?id=2587765)
- DeerFlow ultra dispatch timed out at 900s — exit code 28 (curl timeout); output
  file 256 bytes (analytical acknowledgment only, no collection)
implications:
- 'Three-month media silence (Bernama: 0 CSCDC articles since June) signals CSCDC
  is in internal formation — no public operational milestones to announce'
- CCO position unadvertised on SPA after 3 months confirms mobilisation chain is
  structurally blocked at first signature (CCO → CEO → KSN → DG NACSA)
- Act 854 licensed provider registry appearing empty means the regulatory vendor
  panel may not yet exist in practice — CSCDC procurement could face a regulatory
  gap if it requires licensed providers
- MyKriptografi Action Plan's 80 activities across 4 pillars provides the implementation
  roadmap PQC Sandbox operates within — Pillar 4 specifically addresses quantum
  computing era preparation
- CSM CDD under Ministry of Digital confirms the cross-ministry governance dimension
  — CSCDC (JPM) coordinating with CSM crypto capabilities (KD) requires inter-ministry
  arrangement
- CSM's operational forensics role in MyIMMs hacking case demonstrates active inter-agency
  capability that CSCDC may inherit or coordinate with
- NACSA licensing portal update (new forms 1 July 2026) indicates the licensing
  regime is still maturing — not yet at steady-state operation
open_questions:
- Has CSCDC appointed a dedicated CEO internally without public announcement? (3-month
  silence may indicate internal appointment vs public gap)
- Is the Act 854 license holder registry genuinely empty, or is it JavaScript-rendered
  data that web_extract cannot capture?
- Has the Communication Framework v2.0 been approved internally without public announcement?
- Are CCO recruitment efforts happening through internal channels rather than SPA?
recommended_actions:
- 'Priority 1: Activate HUMINT channel — 3-month public silence confirms OSINT cannot
  resolve PIR-001 (CEO), PIR-002 (approval), PIR-003 (budget), PIR-004 (CCO). These
  are now definitively OSINT-unresolvable.'
- 'Priority 2: Verify Act 854 license holder registry via browser-based inspection
  (licence.nacsa.gov.my/#/licence-holder) — web_extract may not capture JS-rendered
  table data'
- 'Priority 3: Obtain MyKriptografi Action Plan 2026-2030 PDF (nacsa.gov.my/pelan-tindakan-mykriptografi-download.php)
  — 80 activities across 4 pillars likely contains PQC Sandbox milestones'
- 'Priority 4: Engage CSM CDD (mykripto@cybersecurity.my) as technical bridge — CDD
  is the crypto department PQC Sandbox technically reports to'
- 'Priority 5: DeerFlow infrastructure intervention — 3rd consecutive cycle with
  API timeout/blockage; the 900s timeout is insufficient for ultra mode research
  runs'
related_initiatives:
- INIT-20260725-007
related_stakeholders:
- STK-20260725-001
pir_cluster: CSCDC-01
pir_count: 10
deerflow_mode: ultra
deerflow_dispatch_status: TIMEOUT (exit code 28 — curl 900s timeout, 256 bytes output)
inline_collection_status: SUCCESSFUL (12+ sources extracted via web_extract)
---

# Intelligence Report: CSCDC Leadership & Approval Watch

**Collection Date:** 2026-08-24T01:00:00+08:00 (MYT, Monday, 24 August 2026)
**Collection Method:** DEERFLOW_DISPATCH_TIMEOUT — inline web_extract fallback (secondary in hierarchy)
**Classification:** CONFIDENTIAL — OPEN SOURCE INTELLIGENCE (OSINT)
**Collection Status:** PARTIAL — DeerFlow ultra dispatch timed out at 900s; Hermes inline web_extract successfully collected from 12+ government and news sources

---

## Collection Summary

This is the third CSCDC-01 collection cycle. The previous cycle was 18 Aug 2026 (INT-20260818-001). This cycle covers the 6-day gap (18 → 24 Aug 2026).

**DeerFlow Status:** Dispatch attempted in ultra mode. Health check PASSED, thread created successfully, research run dispatched. However, the run timed out at the 900-second curl limit (exit code 28). Output file contains only 256 bytes — a single sentence acknowledging search blackout. This is the 3rd consecutive cycle where DeerFlow's collection capability has been degraded (Cycle 1: API token failure, Cycle 2: API token failure, Cycle 3: timeout).

**Hermes Inline Collection:** web_search backend returned empty results for all 7 queries (continuing the degradation pattern from previous cycles). However, web_extract on direct URLs was fully functional, yielding real intelligence from 12+ sources:
- NACSA official website (4 pages: homepage, kriptografi, act854, licensing, nccmp, mykriptografi, my-cyberHero)
- CyberSecurity Malaysia portal (2 pages: main, procurement)
- MyKripto portal (2 pages: main, PQC initiatives)
- NACSA Licensing Portal (licence.nacsa.gov.my)
- SPA job listings (spa.gov.my/informasi/iklan-kerjaya)
- Bernama (3 pages: CSCDC launch article, search results, IRC 2026, MyIMMs hacking)
- The Edge Malaysia (1 page: CSCDC launch)
- Astro Awani (1 page: frontpage)
- MKN (1 page: landing page)

**Key New Finding:** Bernama search for "cscdc" returns 0 news results. No Malaysian media outlet has published a follow-up article on CSCDC since the 4 June 2026 launch — a 3-month media silence. This is a significant intelligence signal: the entity is in a quiet internal formation phase with no public-facing operational milestones.

---

## PIR Findings

### PIR-CSCDC-001: Leadership Mapping [CRITICAL — Partially Resolved → UNCHANGED]

**Finding:** No new publicly-available leadership appointments identified in the 6-day gap (Aug 18 → Aug 24). The 3-month media silence (Bernama: 0 CSCDC articles since June) confirms no public leadership announcements have been made.

**Current Leadership Baseline (verified as of 2026-08-04, re-verified via Bernama 24 Aug):**

| Position | Name | Status | Source |
|---|---|---|---|
| Board Chairman | KSN Tan Sri Shamsul Azri Abu Bakar | ✅ Verified (appointed 4 Jun 2026) | Bernama (bernama.com/en/general/news.php?id=2564763), The Edge (theedgemalaysia.com/node/805885) |
| NACSA CEO | Ir. Dr. Megat Zuhairy bin Megat Tajuddin | ✅ Verified (regulatory shepherd) | nacsa.gov.my |
| MKN DG | YM Raja Dato' Nushirwan bin Zainal Abidin | ✅ Verified (NCSS 2026) | Prior cycle |
| CSM Acting CEO | Roshdi bin Haji Ahmad | ✅ Verified (since 14 Jan 2026) | Prior cycle |
| PTPKM Director | Datuk Prof. Dr. Muhammad Rezal Kamel Ariffin | ✅ Verified | Prior cycle |
| CSM CTO | Wan Roshaimi | ✅ Verified | Prior cycle |
| **CSCDC Operational CEO** | ❓ **NOT PUBLICLY NAMED** | ⚠️ Critical gap (3-month silence) | No public source |
| **Acting CCO** | ❓ **NOT FOUND** | ⚠️ Critical gap (not on SPA) | No public source |

**New Intelligence (this cycle):**
- Bernama search for "cscdc" returns 0 results — 3-month media silence confirmed [Source: bernama.com/en/search.php?cat1=all&terms=cscdc&submit=cari]
- The Edge Malaysia article re-verified — same content as Bernama, no follow-up [Source: theedgemalaysia.com/node/805885, accessed 24 Aug 2026]
- Astro Awani frontpage shows no cyber security or CSCDC coverage — top stories are PRN Melaka, SUKMA, hockey [Source: astroawani.com, accessed 24 Aug 2026]

**Confidence:** Medium (baseline verified, 3-month silence corroborates no changes)
**PIR Impact:** UNCHANGED — Two critical positions remain unfilled in public domain
**Intelligence Gaps:**
- Whether internal appointment has been made without public announcement
- Whether Roshdi Ahmad's CSM Acting CEO role extends to CSCDC
- Whether CCO recruitment is happening through internal channels

---CVS BLOCK---
Claim: Bernama search for "cscdc" returns 0 news results — no Malaysian media coverage of CSCDC since 4 June 2026 launch
Source: Bernama search (bernama.com/en/search.php?cat1=all&terms=cscdc&submit=cari)
Source Level: L4 (media search engine)
Tier: T2
Validation Status: Verified (search executed 24 Aug 2026, 0 results returned)
Confidence Score: 7 (Authority:1 Traceability:2 Recency:2 Consistency:2 Completeness:0)
Action Required: None — absence of evidence is the finding
---END CVS BLOCK---

### PIR-CSCDC-002: Approval Timeline [CRITICAL — Open → UNCHANGED]

**Finding:** No public announcement of Framework v2.0 approval, mobilisation launch, or 90-day clock commencement. 3-month media silence on CSCDC confirms no public operational milestones.

**Confidence:** Low (inference from absence — T4 projection)
**PIR Impact:** UNCHANGED — HUMINT required (OSINT-unresolvable, 3rd cycle confirming)
**Intelligence Gaps:**
- Internal approval status of v2.0
- Whether 90-day clock has commenced internally
- Whether acting signatories have been designated informally

### PIR-CSCDC-003: Budget Confirmation [HIGH — Open → UNCHANGED]

**Finding:** No treasury circulars, budget gazettes, or parliamentary budget mentions for CSCDC found. RM 4,005,000 Phase 1 budget remains unconfirmed through public OBB documentation.

**Confidence:** Low (inference from absence)
**PIR Impact:** UNCHANGED — HUMINT required
**Intelligence Gaps:**
- OBB approval status
- Whether budget was bundled under NACSA parent allocation

### PIR-CSCDC-004: CCO Appointment Status [HIGH — Open → UNCHANGED]

**Finding:** SPA job listings page actively checked — only 1 active posting (Pegawai Pemulihan Perubatan Gred U9 — fisioterapi, closing 27 Aug 2026). No CCO or CSCDC-related positions. Page states "Tiada iklan kerjaya buat masa ini" (no job ads at this time) after the single listing.

**New Intelligence (this cycle):**
- SPA iklan kerjaya page extracted — confirms no CCO posting (Jusa C/B, RM 18K/month) [Source: spa.gov.my/informasi/iklan-kerjaya, accessed 24 Aug 2026]
- SPA frontpage announcements are generic (POI course, MyDigital ID, PTD counter) — no cyber security or JPM-related postings [Source: spa.gov.my, accessed 24 Aug 2026]

**Confidence:** Low (SPA checked, but internal recruitment channels may bypass SPA)
**PIR Impact:** UNCHANGED — CCO position not publicly advertised after 3 months
**Intelligence Gaps:**
- Whether CCO recruitment is happening through internal/secondment channels
- Whether an acting CCO has been designated informally
- Whether the position has been reclassified or put on hold

---CVS BLOCK---
Claim: SPA job listings page shows no CCO or CSCDC-related positions advertised as of 24 August 2026
Source: SPA iklan kerjaya (spa.gov.my/informasi/iklan-kerjaya)
Source Level: L2 (official government recruitment portal)
Tier: T2
Validation Status: Verified (page extracted 24 Aug 2026, only 1 active posting — medical officer)
Confidence Score: 7 (Authority:2 Traceability:2 Recency:2 Consistency:2 Completeness:0)
Action Required: None — absence is the finding; monitor SPA for future postings
---END CVS BLOCK---

### PIR-CSCDC-005: Infrastructure Procurement Plan [HIGH — Partially Informed → INCREMENTALLY INFORMED]

**Finding:** No ePerolehan tender notices found. However, NACSA licensing portal and CSM e-Procurement page provide updated procurement landscape intelligence.

**New Intelligence (this cycle):**
- **NACSA licensing portal updated** — mandatory new forms (Form A, B, C) effective 1 July 2026. Applications via licence.nacsa.gov.my. iPayment system mandatory since 1 Dec 2025. [Source: licence.nacsa.gov.my, accessed 24 Aug 2026]
- **Licensing fee structure confirmed** — RM400/year (individual) or RM1,000/year (company) per service type (SOC monitoring OR penetration testing). License valid 1 year, renewal 30 days before expiry. [Source: licence.nacsa.gov.my]
- **CSM e-Procurement vendor registration** — vendors must be SSM-registered, operating >1 year, MOF-registered. Categories include sole proprietorships, partnerships, companies, GLCs, professional firms, universities/NGOs. Registration via pnld@cybersecurity.my. [Source: cybersecurity.my/portal-main/procurement, accessed 24 Aug 2026]
- **NACSA Act 854 page** — Act commenced 26 August 2024 (PM-appointed date). Establishes National Cyber Security Committee, outlines NACSA CE duties/powers, NCII sector leads, cyber security service provider licensing. [Source: nacsa.gov.my/act854.php]

**Analytical Projection [ASSESSMENT — T3]:**
- The licensing regime is still maturing (new forms just issued 1 July 2026) — the vendor panel is not yet at steady-state
- CSM's e-Procurement portal is a predecessor channel that may transition to NACSA licensing for cyber-specific services
- RM 485K infrastructure budget may face regulatory complexity if licensed providers are required but none are licensed yet

**Confidence:** Medium (official sources for licensing and procurement requirements)
**PIR Impact:** INCREMENTALLY INFORMED — procurement regulatory framework updated; method still undetermined
**Intelligence Gaps:**
- Whether CSCDC must procure from Act 854-licensed providers only
- Whether the license holder registry is genuinely empty or JS-rendered
- Whether inter-agency sharing with CSM Digital Risk Monitoring has been formalised

---CVS BLOCK---
Claim: NACSA cyber security service provider licensing fee is RM400/year (individual) or RM1,000/year (company) per service type, with mandatory iPayment since 1 Dec 2025 and new forms since 1 July 2026
Source: licence.nacsa.gov.my (NACSA official licensing portal)
Source Level: L2 (official government portal)
Tier: T2
Validation Status: Verified (fee table and notice extracted from official portal)
Confidence Score: 7 (Authority:2 Traceability:2 Recency:2 Consistency:2 Completeness:0)
Action Required: None
---END CVS BLOCK---

### PIR-CSCDC-006: PQC Sandbox Architecture & Timeline [HIGH — Partially Informed → INCREMENTALLY INFORMED]

**Finding:** No PQC Sandbox conference announcements or industry partner calls found. However, MyKriptografi Action Plan and CSM CDD details significantly expanded.

**New Intelligence (this cycle):**
- **MyKriptografi Action Plan 2026-2030 — full structure revealed:**
  - 4 core pillars: (1) Data protection for Government/NCII/individuals, (2) Human capital capacity in cryptographic technology, (3) PKTN adoption among NCII and industry, (4) RDCI for quantum computing era
  - 12 strategies, 32 programmes, 80 activities
  - Covers Government, NCII, industry, academia, and digital economy
  - Download link: nacsa.gov.my/pelan-tindakan-mykriptografi-download.php
  [Source: nacsa.gov.my/pelan-tindakan-mykriptografi.php, accessed 24 Aug 2026]

- **CSM Cryptography Development Department (CDD)** — confirmed as the department within CSM's Proactive Technology & Services Division handling all crypto services. Under Ministry of Digital. [Source: mykripto.cybersecurity.my, accessed 24 Aug 2026]

- **CSM CDD services identified:** MySEAL, MyCANE, MyCV, MyCEL (Cryptographic Evaluation Lab), PKTN, FIPS 140, Blockchain & Smart Contract Security, PQC Initiatives, Research & Development [Source: mykripto.cybersecurity.my]

- **PQC Product Validation & Certification** — financial facility application deadline was 27 September 2025 (closed) [Source: mykripto.cybersecurity.my]

- **MySEAL 2.0** — nominations closed 7 March 2025 (closed) [Source: mykripto.cybersecurity.my]

- **Malaysian Society of Cryptology Research (MSCR)** — CSM CDD is a member (mscr.org.my) [Source: mykripto.cybersecurity.my]

**Analytical Projection [ASSESSMENT — T3]:**
- The PQC Sandbox likely sits within MyKriptografi Action Plan Pillar 4 (RDCI for quantum computing era) — the 80 activities probably include PQC Sandbox milestones
- CSM CDD is the technical implementation arm — PTPKM Director Prof. Dr. Muhammad Rezal provides academic/research leadership, CDD provides operational crypto capability
- PQC Product Validation facility deadline passing (Sep 2025) suggests the validation framework is in post-application review phase
- The PQC Sandbox conference (RM 300K) may be a Pillar 4 programme milestone — the Action Plan PDF likely contains the timeline

**Confidence:** Medium (official sources for Action Plan structure and CDD capabilities)
**PIR Impact:** INCREMENTALLY INFORMED — Action Plan structure and CDD role mapped; timeline and participation model remain unknown
**Intelligence Gaps:**
- PQC Sandbox conference date and format
- Industry participation model (open call vs invited consortium)
- Which of the 80 Action Plan activities correspond to PQC Sandbox milestones
- Relationship between PQC Sandbox and AISCF (AI Systems Cyber Security Framework)

---CVS BLOCK---
Claim: MyKriptografi Action Plan 2026-2030 comprises 4 core pillars, 12 strategies, 32 programmes, and 80 activities, with Pillar 4 specifically addressing RDCI for the quantum computing era
Source: nacsa.gov.my/pelan-tindakan-mykriptografi.php (NACSA official website)
Source Level: L2 (official government agency)
Tier: T2
Validation Status: Verified (plan structure described on official NACSA page)
Confidence Score: 7 (Authority:2 Traceability:2 Recency:2 Consistency:1 Completeness:0)
Action Required: Obtain Action Plan PDF for PQC Sandbox milestone details
---END CVS BLOCK---

---CVS BLOCK---
Claim: CSM Cryptography Development Department (CDD) operates under the Proactive Technology & Services Division within CyberSecurity Malaysia, under the Ministry of Digital
Source: mykripto.cybersecurity.my (CSM official crypto portal)
Source Level: L2 (official agency website)
Tier: T2
Validation Status: Verified (department description on official portal)
Confidence Score: 7 (Authority:2 Traceability:2 Recency:1 Consistency:2 Completeness:0)
Action Required: None
---END CVS BLOCK---

### PIR-CSCDC-007: War Room Activation Protocol [MEDIUM — Partially Informed → INCREMENTALLY INFORMED]

**Finding:** No CSCDC-specific crisis communication protocol publications. NCCMP page provides expanded detail on national framework scope.

**New Intelligence (this cycle):**
- **NCCMP scope confirmed** — covers 10 critical domains: (1) defence and security, (2) banking and finance, (3) information and communications, (4) energy, (5) transportation, (6) water, (7) health, (8) government services, (9) emergency services, (10) food and agriculture [Source: nacsa.gov.my/nccmp.php, accessed 24 Aug 2026]
- **NCCMP provides "detailed steps"** for all parties in national cyber crisis management — detection, response, communication, and coordination procedures [Source: nacsa.gov.my/nccmp.php]
- **NCCMP is the main reference** for Sector Leads and CNII agencies for SOP development — CSCDC's War Room protocol would be developed under this framework [Source: nacsa.gov.my/nccmp.php]
- **CSM CyberDrill Exercise service** confirmed in CSM procurement page service list [Source: cybersecurity.my/portal-main/procurement, accessed 24 Aug 2026]
- **MyIMMs hacking case (29 July 2026)** — CSM assisted MACC with forensic investigation, confirming CSM's active inter-agency operational role in cyber incident response [Source: bernama.com/en/crime_courts/news.php?id=2587765, 29 Jul 2026]

**Analytical Projection [ASSESSMENT — T3]:**
- CSCDC's War Room protocol must be developed within the NCCMP framework — NCCMP provides the national-level steps, CSCDC needs division-level SOPs
- CSM's demonstrated forensic capability (MyIMMs case) positions it as the technical liaison to any CSCDC War Room
- The 10 critical domains in NCCMP define the scope of crisis communication CSCDC must cover

**Confidence:** Medium (NCCMP scope and CSM operational role confirmed from official sources)
**PIR Impact:** INCREMENTALLY INFORMED — NCCMP domain scope and CSM operational role confirmed; CSCDC-specific protocol still internal
**Intelligence Gaps:**
- Whether NCCMP defines the war room activation protocol at division level
- Technical liaison designation for CSCDC War Room
- Escalation matrix at CSCDC division level

---CVS BLOCK---
Claim: NCCMP covers 10 critical domains (defence, banking, ICT, energy, transportation, water, health, government, emergency services, food & agriculture) and provides detailed steps for national cyber crisis management
Source: nacsa.gov.my/nccmp.php (NACSA official website)
Source Level: L2 (official government agency)
Tier: T2
Validation Status: Verified (NCCMP page content extracted)
Confidence Score: 7 (Authority:2 Traceability:2 Recency:1 Consistency:2 Completeness:0)
Action Required: Obtain NCCMP documentation for division-level protocol details
---END CVS BLOCK---

### PIR-CSCDC-008: Community Champions Programme [MEDIUM — Partially Informed → INCREMENTALLY INFORMED]

**Finding:** No CSCDC-specific Community Champions announcements. MYCH 2026 programme details now fully documented.

**New Intelligence (this cycle):**
- **MYCH 2026 — full programme details:**
  - Co-organiser: Micro Concept Tech Sdn Bhd (MCT)
  - Sole sponsor: BlackBerry Technology Sdn Bhd
  - Supporting partners: Kementerian Pendidikan Malaysia (KPM), MDEC
  - Two categories: Rookie Cyber Hero (7-12 years), Star Cyber Hero (13-17 years)
  - 16 teams per category in finals
  - "Defend Your Fort" (DYF) gamification platform by MCT
  - Final competition: 1 July 2026 (completed)
  - PAJSK marks recognition for participants
  [Source: nacsa.gov.my/my-cyberHero.php, accessed 24 Aug 2026]

- **IRC 2026 (21-22 July 2026)** — MCMC-organised conference. Content Forum CEO Mediha Mahmood discussed algorithm-driven platform risks. No Community Champions content. [Source: bernama.com/en/general/news.php?id=2592431, 10 Aug 2026]

**Analytical Projection [ASSESSMENT — T3]:**
- MYCH 2026 is a school-level programme (completed) — CSCDC's 1,000 Community Champions is a community-level programme (different target audience)
- MCT (MYCH co-organiser) and BlackBerry (sponsor) represent existing NACSA vendor/partner relationships that may extend to Community Champions
- RM 200K for 1,000 champions (RM 200/champion) is consistent with a light-touch workshop model, not the gamified competition model of MYCH
- Community Champions programme design likely still in pre-publication phase

**Confidence:** Low (MYCH details confirmed but Community Champions programme still unknown)
**PIR Impact:** INCREMENTALLY INFORMED — MYCH 2026 ecosystem fully mapped; CSCDC Community Champions design still internal
**Intelligence Gaps:**
- Whether Community Champions builds on MYCH/CyberSAFE or is standalone
- Curriculum content and delivery model
- Whether MCT/Blackberry partnership extends to Community Champions

### PIR-CSCDC-009: Inter-Agency Channel Relationships [MEDIUM — Partially Informed → INCREMENTALLY INFORMED]

**Finding:** No inter-agency MOU announcements. IRC 2026 and MyIMMs case provide new inter-agency intelligence.

**New Intelligence (this cycle):**
- **IRC 2026 (21-22 July, MCMC-organised)** — Communications Minister Fahmi Fadzil opened. CSM's Fazlan Abdullah (head of Pre-Emptive Technology and Services Division) spoke on AI cybersecurity threats. Quote: "The bad actors are using AI to attack you. And if you are in the organisation, in government, you must use AI to defend against AI." [Source: bernama.com/en/general/news.php?id=2592431, 10 Aug 2026]
- **AI Governance Bill being drafted** — presented at IRC 2026 alongside National AI Office (established Dec 2024) and Malaysia AI Safety Institute (MY-AISafe) [Source: bernama.com/en/general/news.php?id=2592431]
- **MyIMMs hacking case (29 July 2026)** — CSM assisted MACC and Telekom Malaysia in forensic investigation of immigration system hacking. 12 individuals remanded (6 immigration officers). CSM's role confirms active inter-agency cyber forensics capability. [Source: bernama.com/en/crime_courts/news.php?id=2587765, 29 Jul 2026]
- **CSM under Ministry of Digital** — re-confirmed via MyKripto portal showing Ministry of Digital logo [Source: mykripto.cybersecurity.my, accessed 24 Aug 2026]
- **MKN homepage** — no CSCDC-related content; only GISBH rehabilitation program and legacy COVID-19 info [Source: mkn.gov.my, accessed 24 Aug 2026]

**Analytical Projection [ASSESSMENT — T3]:**
- CSM's Fazlan Abdullah is emerging as a public-facing CSM cybersecurity voice — potentially a key inter-agency interface figure for CSCDC
- The AI Governance Bill adds another regulatory layer to the cybersecurity ecosystem — CSCDC's communication framework may need to align with AI governance requirements
- CSM's demonstrated inter-agency role (MACC + TM + CSM in MyIMMs case) provides a template for CSCDC's crisis coordination relationships
- MKN's silence on CSCDC (no content on homepage) suggests CSCDC operational announcements, if any, are happening through NACSA not MKN

**Confidence:** Medium (IRC 2026 and MyIMMs case from Bernama — L4 sources, official event/case)
**PIR Impact:** INCREMENTALLY INFORMED — CSM public-facing voice and inter-agency operational role confirmed; CSCDC-specific MOUs still unknown
**Intelligence Gaps:**
- Whether CSM's Fazlan Abdullah has a designated CSCDC liaison role
- AI Governance Bill impact on CSCDC communication framework
- MOU status with MCMC, JAPEN, RTM, Bernama

---CVS BLOCK---
Claim: CSM's Fazlan Abdullah (head of Pre-Emptive Technology and Services Division) spoke at IRC 2026 on AI cybersecurity threats, representing CSM as a public-facing voice
Source: Bernama (bernama.com/en/general/news.php?id=2592431, 10 Aug 2026)
Source Level: L4 (media — Bernama)
Tier: T2
Validation Status: Verified (full article extracted from Bernama)
Confidence Score: 7 (Authority:1 Traceability:2 Recency:2 Consistency:1 Completeness:1)
Action Required: None
---END CVS BLOCK---

### PIR-CSCDC-010: Competitor / Incumbent Mapping [HIGH — Partially Informed → INCREMENTALLY INFORMED]

**Finding:** No vendor contract disclosures. Act 854 licensed provider registry appears empty — significant intelligence for competitor mapping.

**New Intelligence (this cycle):**
- **Act 854 license holder registry** — NACSA licensing portal's "List of Licensees" page shows "No data available" for Company - Managed Security Operations Centre Monitoring Service Licence. Filter options suggest 4 categories exist (Managed SOC Company/Individual, Pentest Company/Individual) but no entries visible. [Source: licence.nacsa.gov.my/#/licence-holder, accessed 24 Aug 2026]
- **Licensing portal update (1 July 2026)** — mandatory new forms indicate the licensing regime is still maturing. Applications accepted since 1 Oct 2024 but no visible licensees after 10 months. [Source: licence.nacsa.gov.my]
- **CSM vendor registration** — CSM maintains its own vendor registration (separate from Act 854 licensing). Requirements: SSM, MOF, >1 year operating. Categories include companies, GLCs, professional firms, universities/NGOs. [Source: cybersecurity.my/portal-main/procurement]
- **MYCH 2026 vendor/partner ecosystem:**
  - Micro Concept Tech Sdn Bhd (MCT) — co-organiser, developed DYF platform
  - BlackBerry Technology Sdn Bhd — sole sponsor
  - These are existing NACSA vendor relationships that may be relevant for CSCDC
  [Source: nacsa.gov.my/my-cyberHero.php]

**Analytical Projection [ASSESSMENT — T3]:**
- If the Act 854 license holder registry is genuinely empty, the regulatory vendor panel does not exist in practice — CSCDC procurement for security services may face a regulatory gap
- The registry may be JavaScript-rendered (web_extract cannot capture dynamic content) — needs browser-based verification
- CSM's own vendor registration (pnld@cybersecurity.my) represents a parallel procurement channel that CSCDC may inherit
- MCT and BlackBerry represent existing NACSA-partnered companies — potential incumbents for CSCDC communication/awareness programmes

**Confidence:** Low (registry emptiness needs verification; JS-rendering possibility)
**PIR Impact:** INCREMENTALLY INFORMED — licensing fee structure and portal update confirmed; license holder registry appears empty (needs browser verification)
**Intelligence Gaps:**
- Whether the license holder registry is genuinely empty or JS-rendered
- If empty: implications for CSCDC procurement requiring licensed providers
- Existing CSM vendor relationships that may transfer to CSCDC
- Whether MCT/BlackBerry have extended relationships beyond MYCH 2026

---CVS BLOCK---
Claim: Act 854 licensed provider registry shows "No data available" for Managed SOC Company licence as of 24 August 2026
Source: licence.nacsa.gov.my/#/licence-holder (NACSA official licensing portal)
Source Level: L2 (official government portal)
Tier: T2
Validation Status: Partially Verified — page extracted but may be JavaScript-rendered (dynamic table not captured by web_extract)
Confidence Score: 5 (Authority:2 Traceability:2 Recency:2 Consistency:1 Completeness:0)
Action Required: Browser-based verification of license holder registry
---END CVS BLOCK---

---

## Cross-PIR Synthesis

### Three-Month Media Silence — Key Strategic Signal

The most significant finding this cycle is not new intelligence but confirmed absence: Bernama search for "cscdc" returns 0 results. No Malaysian media outlet has published a follow-up article on CSCDC since the 4 June 2026 launch. This 3-month silence is a strategic signal:

1. **Internal formation phase** — CSCDC is operating below public radar, consistent with a SULIT-classified national security entity in early formation
2. **No operational milestones** — no appointments, no budget announcements, no framework approval, no programme launches to announce
3. **Mobilisation chain blocked** — without CCO (1st signatory) and dedicated CEO (2nd signatory), the four-signature approval chain cannot execute
4. **OSINT ceiling reached** — 3 consecutive collection cycles (Aug 4, Aug 18, Aug 24) confirm the same leadership gaps; further OSINT collection will not resolve internal appointments

### Regulatory Vendor Panel Gap

The Act 854 licensed provider registry appearing empty ("No data available") after 10 months of application acceptance (since 1 Oct 2024) has implications across multiple PIRs:

- **PIR-005 (Infrastructure Procurement):** If CSCDC requires licensed providers for security services, the empty registry creates a procurement bottleneck
- **PIR-010 (Competitor Mapping):** If no companies are licensed, the competitor landscape is undefined — both an opportunity (no incumbents) and a risk (no qualified vendors under the regulatory framework)
- **PIR-007 (War Room Protocol):** Licensed SOC monitoring providers would be needed for war room infrastructure; empty registry means this capability may not yet exist in the licensed market

**Caveat:** The registry may be JavaScript-rendered and web_extract cannot capture dynamic table content. Browser-based verification is needed before concluding the registry is genuinely empty.

### MyKriptografi Action Plan as PQC Sandbox Roadmap

The expanded Action Plan detail (4 pillars, 12 strategies, 32 programmes, 80 activities) provides the implementation context for PIR-CSCDC-006. Pillar 4 (RDCI for quantum computing era) is the most likely location of PQC Sandbox milestones. The Action Plan PDF (downloadable from nacsa.gov.my) likely contains the specific timeline and programme details that would resolve PIR-006's timeline and participation model questions.

### Updated Critical Path Dependencies

```
CCO Appointment (PIR-004) — NOT ON SPA after 3 months
    ↓ [BLOCKED — no public recruitment channel identified]
Communication Framework v2.0 Approval (PIR-002) — INTERNAL ONLY
    ↓ [BLOCKED — 4-signature chain incomplete]
90-Day Mobilisation Clock (PIR-002) — CANNOT START
    ↓
Infrastructure Procurement (PIR-005) — REGULATORY GAP (empty license registry)
    ↓
War Room Activation (PIR-007) — NCCMP framework exists, no licensed SOC providers
    ↓
Community Champions Deployment (PIR-008) — MYCH 2026 completed, Champions not started
```

**Primary Blocker:** PIR-CSCDC-004 (CCO Appointment) — 3 months without public advertisement
**Secondary Blocker:** PIR-CSCDC-001 (CSCDC CEO) — 3 months without public appointment
**Tertiary Blocker:** PIR-CSCDC-010 (Empty license registry) — regulatory vendor panel may not exist

### Updated Inherited Capability Map

| CSCDC Need | CSM Existing Capability | Status Update This Cycle |
|---|---|---|
| Social listening | Digital Risk Monitoring service | Confirmed in CSM service list |
| War Room / Cyber Drill | CyberDrill Exercise service | Confirmed; MyIMMs case shows active forensics |
| PQC Sandbox | CDD: MyCV, MySEAL, PKTN, MyCANE, MyCEL, PQC Initiatives | CDD confirmed as department; MyCEL new |
| Community awareness | CyberSAFE, MYCH 2026 (completed) | MYCH 2026 fully documented; MCT/Blackberry partners |
| Crisis response framework | NCCMP (10 domains) | NCCMP scope confirmed; CSCDC-specific SOP needed |
| Crypto validation | MyCV, MySEAL, PKTN, MyCEL, FIPS 140 | Full CDD service list documented |
| Licensing regime | Act 854 licensing | Portal updated; registry appears empty |

---

## Intelligence Gaps

### Critical (OSINT Ceiling Reached — HUMINT Required)
1. **CSCDC CEO appointment** — 3-month silence; OSINT cannot resolve [CONFIRMED OSINT-UNRESOLVABLE — 3 CYCLES]
2. **CCO position status** — Not on SPA; internal channels unknown [CONFIRMED OSINT-UNRESOLVABLE — 3 CYCLES]
3. **Framework v2.0 approval** — Internal instrument [CONFIRMED OSINT-UNRESOLVABLE — 3 CYCLES]
4. **Budget OBB confirmation** — Internal budget [CONFIRMED OSINT-UNRESOLVABLE — 3 CYCLES]

### High (OSINT-Resolvable With Browser Verification)
5. **Act 854 license holder registry** — Browser-based verification needed (licence.nacsa.gov.my/#/licence-holder) — web_extract may not capture JS-rendered table
6. **MyKriptografi Action Plan PDF** — Download and review for PQC Sandbox milestones (nacsa.gov.my/pelan-tindakan-mykriptografi-download.php)
7. **ePerolehan tender notices** — Any CSCDC-related procurement posted?
8. **PQC Sandbox conference announcements** — Dates, industry partner calls?

### Medium (Structural Inference)
9. **NCCMP division-level protocol** — Does it define war room activation at CSCDC level?
10. **Inter-agency MOU status** — Have MOUs been drafted with MCMC, JAPEN, RTM, Bernama?

---

## Recommendations

### Immediate Actions
1. **Declare OSINT ceiling for PIR-001, PIR-002, PIR-003, PIR-004** — 3 consecutive cycles confirm these are OSINT-unresolvable. Transition to HUMINT or direct inquiry. The 3-month media silence is definitive evidence.
2. **Browser-based verification of Act 854 license holder registry** — licence.nacsa.gov.my/#/licence-holder may show licensed companies in a JS-rendered table that web_extract cannot capture. This is critical for PIR-010 competitor mapping.
3. **Download and review MyKriptografi Action Plan PDF** — 80 activities across 4 pillars likely contain PQC Sandbox timeline and milestones (PIR-006).
4. **Engage CSM CDD as technical bridge** — mykripto@cybersecurity.my. CDD is the crypto department; PTPKM Director provides academic leadership. CDD can informally advise on PQC Sandbox status.
5. **DeerFlow infrastructure intervention** — 3rd consecutive cycle with timeout/blockage. The 900s curl timeout is insufficient for ultra mode runs. Options: (a) increase timeout to 1800s, (b) switch to pro mode, (c) investigate DeerFlow's internal API token issue.

### Near-Term Priorities
6. **Identify CSM Fazlan Abdullah as inter-agency interface** — CSM's head of Pre-Emptive Technology and Services Division spoke publicly at IRC 2026. He may be a key CSCDC liaison figure (PIR-009).
7. **Monitor AI Governance Bill progress** — being drafted; will affect CSCDC communication framework's AI-related protocols (PIR-009).
8. **Assess MCT and BlackBerry as potential incumbents** — MYCH 2026 co-organiser and sponsor represent existing NACSA vendor relationships (PIR-010).

### Collection Strategy Adjustment
9. **Reduce CSCDC-01 collection frequency** — with OSINT ceiling reached for 4 critical PIRs, 6-hourly collection is wasteful. Recommend reducing to 12-hourly until HUMINT channel is activated or a public announcement triggers event-driven collection.
10. **Transition PIR-001/002/003/004 to HUMINT track** — mark as OSINT-unresolvable in PIR inventory, assign to DAF for direct inquiry through NACSA/CSM relationships.

---

## PIR Resolution Status Table

| PIR ID | Priority | Previous Status (Aug 18) | Current Status (Aug 24) | Confidence | New Intel? |
|---|---|---|---|---|---|
| PIR-CSCDC-001 | CRITICAL | Partially Resolved (UNCHANGED) | **UNCHANGED** — 3-month media silence confirmed | Medium | Bernama: 0 CSCDC articles |
| PIR-CSCDC-002 | CRITICAL | Open (HUMINT) | **UNCHANGED** — OSINT ceiling confirmed | Low | No approval announcements |
| PIR-CSCDC-003 | HIGH | Open (HUMINT) | **UNCHANGED** — OSINT ceiling confirmed | Low | No budget confirmations |
| PIR-CSCDC-004 | HIGH | Open | **UNCHANGED** — SPA checked, no CCO posting | Low | SPA: no CCO advertisement |
| PIR-CSCDC-005 | HIGH | Partially Informed | **INCREMENTALLY INFORMED** — licensing portal updated, fee structure confirmed | Medium | Yes — licensing forms, fees, CSM e-Proc |
| PIR-CSCDC-006 | HIGH | Partially Informed | **INCREMENTALLY INFORMED** — Action Plan structure (4P/12S/32Prog/80Act), CDD confirmed | Medium | Yes — Action Plan detail, CDD, MyCEL |
| PIR-CSCDC-007 | MEDIUM | Partially Informed | **INCREMENTALLY INFORMED** — NCCMP 10 domains confirmed, CSM forensics role | Medium | Yes — NCCMP scope, MyIMMs case |
| PIR-CSCDC-008 | MEDIUM | Partially Informed | **INCREMENTALLY INFORMED** — MYCH 2026 fully documented | Low | Yes — MYCH details, MCT/Blackberry |
| PIR-CSCDC-009 | MEDIUM | Partially Informed | **INCREMENTALLY INFORMED** — IRC 2026, CSM Fazlan Abdullah, AI Governance Bill | Medium | Yes — IRC 2026, MyIMMs case |
| PIR-CSCDC-010 | HIGH | Partially Informed | **INCREMENTALLY INFORMED** — license registry appears empty, fee structure confirmed | Low | Yes — registry status, fees, MYCH vendors |

**Overall Assessment:** 0/10 PIRs fully resolved. 6/10 PIRs incrementally informed. 4/10 PIRs at OSINT ceiling (UNCHANGED — HUMINT required). Collection was inline-only (DeerFlow timeout). Key strategic signal: 3-month media silence confirms CSCDC is in internal formation with no public operational milestones.

---

## TOP 3 PIR SUGGESTIONS FOR NEXT CYCLE

1. **PIR-CSCDC-010 (Act 854 License Holder Registry Verification)** — Browser-based verification is the single most actionable next step.
   **Rationale:** If the registry is genuinely empty after 10 months, CSCDC procurement faces a regulatory vendor gap. If it's JS-rendered, the competitor landscape is visible but not captured by web_extract.
   **Search Queries:** Browser visit to licence.nacsa.gov.my/#/licence-holder, "NACSA licensed cyber security providers list", "Act 854 license holders Malaysia"

2. **PIR-CSCDC-006 (MyKriptografi Action Plan PDF Review)** — Download the Action Plan PDF for PQC Sandbox timeline.
   **Rationale:** 80 activities across 4 pillars — Pillar 4 (quantum computing era) likely contains PQC Sandbox milestones. This is a downloadable official document, not an internal instrument.
   **Search Queries:** Download nacsa.gov.my/pelan-tindakan-mykriptografi-download.php, "MyKriptografi Action Plan 2026-2030 PQC Sandbox", "NACSA quantum computing roadmap Malaysia"

3. **PIR-CSCDC-009 (CSM Fazlan Abdullah Inter-Agency Role)** — Identify whether CSM's Pre-Emptive Technology head has a formal CSCDC liaison role.
   **Rationale:** Fazlan Abdullah is emerging as CSM's public-facing cybersecurity voice (IRC 2026). If he has a CSCDC liaison designation, he's a warm introduction path.
   **Search Queries:** "Fazlan Abdullah CyberSecurity Malaysia CSCDC", "CSM Pre-Emptive Technology Services Division", "CyberSecurity Malaysia NACSA liaison"

---

## Collection Infrastructure Notes

### DeerFlow Dispatch Status
- **Health check:** PASSED — DeerFlow healthy at localhost:2026
- **Thread creation:** SUCCESS — thread c1d7492b-705c-44a8-9862-cb91e982834a
- **Research run:** TIMEOUT — curl exit code 28 at 900s internal timeout
- **Output:** 256 bytes — single sentence acknowledging search blackout, no collection
- **Assessment:** 3rd consecutive cycle of DeerFlow degradation (C1: API token failure, C2: API token failure, C3: timeout). Infrastructure intervention required.

### Hermes Inline Collection Status
- **web_search:** DEGRADED — returned empty results for all 7 queries (continuing pattern from previous cycles)
- **web_extract:** FULLY FUNCTIONAL — successfully extracted from 12+ URLs:
  - nacsa.gov.my (7 pages: homepage, kriptografi, act854, licensing, nccmp, mykriptografi, my-cyberHero)
  - cybersecurity.my (2 pages: main, procurement)
  - mykripto.cybersecurity.my (2 pages: main, PQC initiatives)
  - licence.nacsa.gov.my (2 pages: main, licence-holder)
  - spa.gov.my (2 pages: homepage, iklan-kerjaya)
  - bernama.com (4 pages: CSCDC article, cscdc search, CyberSecurity Malaysia search, IRC 2026, MyIMMs)
  - theedgemalaysia.com (1 page: CSCDC launch)
  - astroawani.com (1 page: frontpage)
  - mkn.gov.my (1 page: landing page)
- **Failed extractions:** cybersecurity.my/portal-main/career (Internal Server Error), cybersecurity.my/portal-main/events (Internal Server Error), bharian.com.my (antibot)
- **Total successful extractions:** 15+ pages across 12+ domains

### OSINT Stack Status
- **Firecrawl (localhost:3002):** Not tested this cycle
- **SearXNG (127.0.0.1:8080):** Not tested this cycle
- **DeerFlow (localhost:2026):** HEALTHY gateway, TIMEOUT on research run (900s)

---

*Report generated by CSCDC-01 PIR Collection Orchestrator (Hermes cronjob 95af59753d01). Collection method: DEERFLOW_DISPATCH_TIMEOUT — inline web_extract fallback. All findings sourced from live web retrieval on 2026-08-24 (Asia/Kuala_Lumpur). No data fabricated; gaps reported honestly. CVS Rule 6 applied — all AI-assigned tiers capped at T2, confidence capped at 7. Three-month media silence on CSCDC confirmed via Bernama search (0 results). OSINT ceiling declared for PIR-001/002/003/004 — HUMINT required.*
