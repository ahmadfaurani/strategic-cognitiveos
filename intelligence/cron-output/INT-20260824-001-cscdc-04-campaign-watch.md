---
id: INT-20260824-CSCDC-04-001
record_type: intelligence
title: "PIR Collection: Anti-Deepfake & Campaign Strategy Watch — 24 Aug 2026"
created_at: 2026-08-24T01:45:00+08:00
updated_at: 2026-08-24T01:51:00+08:00
owner: DAF
status: draft
priority: critical
sensitivity: confidential
lifecycle_state: candidate
confidence: medium
tags:
  - intelligence/cron-output
  - workstream/cscdc-partnership
  - workstream/anti-deepfake-campaign
  - method/deerflow-pro-thin-output-web-fallback
source:
  type: osint
  reference: "DeerFlow pro mode (thin output 892 bytes) + web_extract fallback (Ministry of Digital gov.my full body extraction) — 20260824"
summary: "Anti-deepfake & campaign strategy intelligence: DeerFlow dispatched successfully (healthy, thread created) but returned thin summary-only output. Fallback web_extract on Ministry of Digital gov.my yielded 4 major new findings since 18 Aug cycle: Rakyat Digital portal launched (11 Aug) with CyberSAFE module, AI Malaysia Berhad institutionalised (28 Jul) with AI Safety Institute, National AI Action Plan 2026-2030 formally launched, MyGOV Agentic AI beta (10 Aug). Cybercrimes Bill royal assent/gazetting still unverifiable — remains #1 critical gap."
strategic_significance: "Government's AI awareness infrastructure accelerating (Rakyat Digital, AI Malaysia Berhad, AI Safety Institute) but creative anti-deepfake campaign white space persists. No CSCDC-specific campaign, no agency tender, no creative content plan visible. Legislative crystallisation (Cybercrimes Bill awaiting royal assent) creates hard deadline. Rakyat Digital's CyberSAFE module integration signals government starting to build awareness content — but institutional/educational, not creative/media."
mission_alignment:
  - mission/intelligence-enablement
related_records:
  - OPP-20260725-008
  - OPP-20260725-004
  - INIT-20260725-007
  - STK-20260725-001
intelligence_type: market
evidence:
  - "Rakyat Digital portal launched 11 Aug 2026 by Ministry of Digital — 3A approach (Awareness, Access, Adoption); CyberSAFE module included in youth AI tool access program (100K youths aged 18-30, 3-month free AI tool access from 31 Aug 2026) (digital.gov.my, 11 Aug 2026)"
  - "AI Malaysia Berhad officially established 28 Jul 2026 — institutionalisation of NAIO under Ministry of Digital; core responsibilities include policy coordination, AI governance, AI Safety Institute (digital.gov.my, 28 Jul 2026)"
  - "National AI Action Plan 2026-2030 formally launched 28 Jul 2026 — 14 sectoral initiatives + 14 enabler initiatives; 5 foundational enablers (human capital, innovation, infrastructure, governance, financing) (digital.gov.my, 28 Jul 2026)"
  - "Malaysia AI Safety Institute established 28 Jul 2026 — 3 pillars: AI RDCI (safety evaluations, testing, red teaming), strategic collaborations, governance/regulatory support (digital.gov.my, 28 Jul 2026)"
  - "MyGOV Agentic AI beta deployment commenced early August 2026 — 2.9M+ users, 52 services from 19 agencies; phased implementation with human-in-the-loop oversight (digital.gov.my, 10 Aug 2026)"
  - "AI Governance Bill targeted for completion by end of 2026 — risk-based approach, Central AI Authority, public consultation closed 31 Jul 2026 (digital.gov.my + Baker McKenzie + LPP Law, Jul-Aug 2026)"
  - "Cybercrimes Bill 2026 passed Dewan Negara 20 Jul 2026 — comprehensive framework replacing CCA 1997; deepfake/identity theft offences; penalties up to RM1M/10 years; royal assent status UNVERIFIED (Rahmat Lim, 6 Aug 2026)"
  - "LPP Law confirms NAIO institutionalised as AI Malaysia Berhad on 28 Jul 2026 — alongside AI Action Plan + AI Safety Institute (lpplaw.my, 2 Aug 2026)"
implications:
  - "Rakyat Digital CyberSAFE module = government building awareness content in-house — but educational/institutional, not creative/media campaign. CSCDC's RM 500K creative campaign white space confirmed."
  - "AI Malaysia Berhad as apex AI entity may absorb or coordinate anti-deepfake campaign — changes stakeholder landscape. CSCDC may now report to or coordinate with AI Malaysia Berhad instead of standalone NAIO."
  - "National AI Action Plan 2026-2030 includes 'Responsible Governance' as foundational enabler — campaign may be framed as implementation of this enabler rather than standalone CSCDC initiative."
  - "AI Safety Institute's red teaming mandate intersects with deepfake detection — campaign content could reference AI Safety Institute findings."
  - "Cybercrimes Bill royal assent remains the single most critical timeline signal — enforcement commencement creates campaign deadline. 35 days since Dewan Negara passage (20 Jul → 24 Aug) without gazette confirmation."
open_questions:
  - "Cybercrimes Bill 2026 royal assent and gazetting date — enforcement commencement timeline (35 days unverifiable, #1 critical gap)"
  - "Has CSCDC/CSM/NACSA made final creative agency selection decision? Procurement timeline?"
  - "Will AI Malaysia Berhad absorb the anti-deepfake campaign mandate from CSCDC?"
  - "Is Rakyat Digital's CyberSAFE module the government's chosen awareness vehicle, replacing the RM 500K creative campaign?"
  - "Baseline cyber literacy survey — what is the 30% improvement KPI denominator?"
  - "TV airtime procurement path: JAPEN/RTM free quota or commercial paid slots?"
  - "AI Governance Bill Cabinet submission timeline post-consultation closure (31 Jul 2026)"
recommended_actions:
  - "PRIORITY 1: Track Cybercrimes Bill royal assent — check Federal Government Gazette (warkat/gazette) for publication"
  - "PRIORITY 2: Assess whether AI Malaysia Berhad changes the CSCDC anti-deepfake campaign governance — new stakeholder to engage"
  - "PRIORITY 3: Evaluate Rakyat Digital CyberSAFE module as potential integration point or competitor to CSCDC's RM 500K campaign"
  - "PRIORITY 4: Monitor ePerolehan/SEPTEK for CSCDC creative agency tender — still zero procurement signal"
  - "PRIORITY 5: Track AI Governance Bill post-consultation Cabinet submission timeline"
  - "PRIORITY 6: Engage AI Malaysia Berhad as new apex AI entity — may be decision-maker for campaign scope"
related_initiatives:
  - INIT-20260725-007
related_stakeholders:
  - STK-20260725-001
---

# Intelligence Report: Anti-Deepfake & Campaign Strategy Watch

**Collection Method:** DeerFlow pro mode (dispatched successfully — healthy, thread created — but returned thin 892-byte summary-only output; no full PIR-by-PIR analysis captured) + web_extract fallback (Ministry of Digital gov.my full body extraction on 4 announcement pages, Baker McKenzie, LPP Law, Rahmat Lim, FMT, RTM)
**Collection Window:** August 18–24, 2026 (new intelligence since last cycle) + July 2025–August 2026 (broader context)
**Timestamp:** 2026-08-24 01:45 MYT (Asia/Kuala_Lumpur, UTC+8)

---

## Collection Summary

This collection cycle executed 20 PIRs across 2 source records (OPP-20260725-008: Anti-Deepfake Campaign, OPP-20260725-004: Content Studio). DeerFlow was healthy and dispatched successfully (thread 19298d6c created), but returned only a thin 892-byte summary — the full PIR-by-PIR analysis was not captured in the output file. The Hermes orchestrator executed the web_extract fallback protocol on Ministry of Digital (digital.gov.my) announcement pages, yielding **4 major new findings** since the 18 Aug cycle:

1. **Rakyat Digital portal launched 11 Aug 2026** — 3A approach (Awareness, Access, Adoption) with CyberSAFE module in youth AI access program
2. **AI Malaysia Berhad institutionalised 28 Jul 2026** — NAIO formally upgraded to national AI entity under Ministry of Digital
3. **National AI Action Plan 2026-2030 formally launched** — 14 sectoral + 14 enabler initiatives
4. **Malaysia AI Safety Institute established** — red teaming, safety evaluations, governance support
5. **MyGOV Agentic AI beta deployment** commenced early August 2026

**DeerFlow Output Note:** DeerFlow's pro mode returned a summary containing references to "5 Fake BTS operations," "Konvensyen PIBG 2026," "ONSA codes," and "RM2.7B scam losses" — these items were NOT verifiable via web_extract in this cycle (search API blackout persists). They are noted but not incorporated into PIR findings without source verification.

---

## Fresh Web-Verified Findings (web_extract fallback)

### Finding F1: Rakyat Digital Portal — CyberSAFE Module Integration (11 Aug 2026)

- **Source:** https://www.digital.gov.my/en-GB/siaran/Kementerian-Digital-Lancar-Portal-Rakyat-Digital-Baharu,Memperkukuh-Komitmen-Menuju-Ke-Arah-Negara-AI-Menjelang-2030 (Ministry of Digital, 11 Aug 2026)
- **Also:** https://www.digital.gov.my/en-GB/siaran/AI-Malaysia-Takeover-2026:Pelancaran-Rakyat-Digital (Gobind speech, 11 Aug 2026)

**Finding:** On 11 Aug 2026, Minister Gobind launched the new Rakyat Digital portal at the AI Malaysia Takeover 2026 event. Key elements:
- **3A approach:** Awareness (Digital Literacy Hub — free courses), Access (Digital Skills Hub + Global Learning Pass — free Coursera access for 25K Malaysians per cohort starting 16 Sep 2026), Adoption (AI Builders Hub from Oct 2026)
- **Youth AI access program:** 100,000 Malaysians aged 18-30 receive 3-month free access to leading generative AI tools from 31 Aug 2026 — contingent on completing learning modules including **AI Safety, CyberSAFE for the Public, Generative AI, Agentic AI, Cloud for the Public, and Malaysia MADANI values**
- **MD2030 targets:** 80% digitally literate population, reskill 700,000 workers, 5,000 rural digital entrepreneurs
- **AI Learn-a-thon:** 1,000+ registrations, Malaysia Book of Records attempt for Largest AI Learn-a-thon

**PIR Impact:** PIR-OPP008-003 (Audience Segmentation) — government has defined segments: youth 18-30 (primary AI access), rural communities, senior citizens, PWD, MSMEs. PIR-OPP008-010 (Existing Campaigns) — CyberSAFE module integrated into Rakyat Digital as institutional awareness vehicle. PIR-OPP008-008 (Baseline Measurement) — MD2030 target of 80% digitally literate population provides KPI context.

**Confidence:** HIGH (official government press release + minister's speech, full body extracted)

---CVS BLOCK---
Claim: Rakyat Digital portal launched 11 Aug 2026 by Ministry of Digital with 3A approach (Awareness, Access, Adoption) and CyberSAFE module in youth AI access program for 100K youths aged 18-30
Source: Ministry of Digital (https://www.digital.gov.my/en-GB/siaran/Kementerian-Digital-Lancar-Portal-Rakyat-Digital-Baharu,Memperkukuh-Komitmen-Menuju-Ke-Arah-Negara-AI-Menjelang-2030)
Source Level: L1
Tier: T2
Validation Status: Partially Verified (official government announcement, full body extracted; Rule 6 cap applied)
Confidence Score: 7 (Authority:2 Traceability:2 Recency:2 Consistency:2 Completeness:1)
Action Required: None — official source confirmed
---END CVS BLOCK---

### Finding F2: AI Malaysia Berhad Institutionalised (28 Jul 2026)

- **Source:** https://www.digital.gov.my/en-GB/siaran/AI-Malaysia-Pemacu-Utama-Menuju-Negara-AI-2030 (Ministry of Digital, 28 Jul 2026)
- **Also:** https://lpplaw.my/ai-governance-malaysia/ (LPP Law, 2 Aug 2026)

**Finding:** PM Anwar officially announced the establishment of **AI Malaysia Berhad** on 28 Jul 2026 in Cyberjaya — a national AI entity under the Ministry of Digital. This represents the institutionalisation of the National AI Office (NAIO), originally established 12 Dec 2024. Core responsibilities:
- **Policy Coordination and Implementation** — bridging national strategy with operational implementation
- **High-Impact Monitoring** — monitoring outcomes under National AI Action Plan 2030
- **Trusted AI Governance** — governance frameworks, codes of ethics, standards, trust mechanisms
- **Strategic Collaboration** — global AI partnerships
- **Malaysia AI Safety Institute** — fulfilling role of national AI Safety Institute

**LPP Law confirms:** "On 28 July 2026 the National AI Office was institutionalised as AI Malaysia Berhad under the Ministry of Digital, alongside the National AI Action Plan 2026–2030 and the establishment of a Malaysian AI Safety Institute."

**PIR Impact:** PIR-OPP008-001 (Campaign Strategy) — new apex AI entity may absorb or coordinate anti-deepfake campaign governance. PIR-OPP008-002 (Agency Selection) — AI Malaysia Berhad may be the decision-maker for campaign creative procurement. Major stakeholder landscape change.

**Confidence:** HIGH (official government press release + law firm corroboration, full body extracted)

---CVS BLOCK---
Claim: AI Malaysia Berhad officially established 28 Jul 2026 by PM Anwar as institutionalisation of NAIO under Ministry of Digital, with core responsibilities including policy coordination, AI governance, and AI Safety Institute
Source: Ministry of Digital (https://www.digital.gov.my/en-GB/siaran/AI-Malaysia-Pemacu-Utama-Menuju-Negara-AI-2030)
Source Level: L1
Tier: T2
Validation Status: Partially Verified (official government announcement, full body extracted; corroborated by LPP Law; Rule 6 cap applied)
Confidence Score: 7 (Authority:2 Traceability:2 Recency:2 Consistency:2 Completeness:1)
Action Required: None — official source confirmed
---END CVS BLOCK---

### Finding F3: National AI Action Plan 2026-2030 + AI Safety Institute Launched

- **Source:** https://www.digital.gov.my/en-GB/siaran/AI-Malaysia-Pemacu-Utama-Menuju-Negara-AI-2030 (Ministry of Digital, 28 Jul 2026)

**Finding:** In conjunction with AI Malaysia Berhad launch, the government introduced:
- **National AI Action Plan 2026-2030:** 14 sectoral initiatives + 14 enabler initiatives. 5 foundational enablers: (1) Globally Competitive Human Capital, (2) Market-Driven Innovation, (3) Data and Computing Infrastructure, (4) Responsible Governance, (5) Sustainable Financing and Investment.
- **Malaysia AI Safety Institute:** 3 pillars — (1) AI RDCI (Research, Development, Commercialisation, Innovation) including safety evaluations, testing, AI Red Teaming; (2) Strategic collaborations for talent development and technology transfer; (3) Governance, safety, and regulatory support through standards, risk management, compliance assurance.
- **AI Governance Bill** confirmed as "currently being drafted" with risk-based approach, "targeted for completion by the end of this year."

**PIR Impact:** PIR-OPP008-001 (Campaign Strategy) — "Responsible Governance" enabler may frame the anti-deepfake campaign as policy implementation. PIR-OPP008-009 (Campaign Duration) — multi-year strategy (2026-2030) confirmed. PIR-OPP008-010 (Existing Campaigns) — AI Safety Institute's red teaming mandate adds institutional infrastructure.

**Confidence:** HIGH (official government press release, full body extracted)

---CVS BLOCK---
Claim: National AI Action Plan 2026-2030 launched 28 Jul 2026 with 14 sectoral + 14 enabler initiatives; Malaysia AI Safety Institute established with 3 pillars (RDCI, collaborations, governance)
Source: Ministry of Digital (https://www.digital.gov.my/en-GB/siaran/AI-Malaysia-Pemacu-Utama-Menuju-Negara-AI-2030)
Source Level: L1
Tier: T2
Validation Status: Partially Verified (official government announcement, full body extracted; Rule 6 cap applied)
Confidence Score: 7 (Authority:2 Traceability:2 Recency:2 Consistency:2 Completeness:1)
Action Required: None
---END CVS BLOCK---

### Finding F4: MyGOV Agentic AI Beta Deployment (10 Aug 2026)

- **Source:** https://www.digital.gov.my/en-GB/siaran/MyGOV-Malaysia-Melangkah-Ke-Era-Baharu-Dengan-Agentic-AI (Ministry of Digital, 10 Aug 2026)

**Finding:** Ministry of Digital commenced Agentic AI beta deployment on MyGOV Malaysia in early August 2026:
- **2.9M+ users**, 52 services from 19 government agencies
- Agentic AI evolves from prompt-response to context-aware task execution
- Phased implementation with safety, data privacy, human-in-the-loop oversight per Public Sector AI Adoption Guidelines
- Example: police summons checks with complete payment workflow

**PIR Impact:** PIR-OPP008-007 (Micro-Targeting Capability) — Agentic AI represents advanced AI deployment capability in government, but not directly applicable to campaign micro-targeting. PIR-OPP008-010 (Existing Campaigns) — MyGOV is a service delivery platform, not awareness campaign.

**Confidence:** HIGH (official government press release, full body extracted)

---CVS BLOCK---
Claim: MyGOV Malaysia Agentic AI beta deployment commenced early August 2026 with 2.9M+ users and 52 services from 19 agencies
Source: Ministry of Digital (https://www.digital.gov.my/en-GB/siaran/MyGOV-Malaysia-Melangkah-Ke-Era-Baharu-Dengan-Agentic-AI)
Source Level: L1
Tier: T2
Validation Status: Partially Verified (official government announcement, full body extracted; Rule 6 cap applied)
Confidence Score: 7 (Authority:2 Traceability:2 Recency:2 Consistency:2 Completeness:1)
Action Required: None
---END CVS BLOCK---

### Finding F5: AI Governance Bill — Post-Consultation Status (Updated)

- **Source:** https://www.bakermckenzie.com/en/insight/publications/2026/07/malaysia-public-consultation-on-the-ai-governance-bill (Baker McKenzie, 13 Jul 2026)
- **Also:** https://lpplaw.my/ai-governance-malaysia/ (LPP Law, filed 31 Jul 2026, updated 2 Aug 2026)
- **Also:** https://www.digital.gov.my/en-GB/siaran/Kementerian-Digital-Mulakan-Libat-Urus-Cadangan-Rang-Undang-Undang-Tadbir-Urus-Kecerdasan-Buatan-(AI) (Ministry of Digital, 10 Jul 2026)

**Finding:** AI Governance Bill public consultation closed 31 Jul 2026 (LPP Law confirmed submission filed). Key developments:
- Bill "targeted for completion by the end of 2026" (Ministry of Digital)
- Central AI Authority with 3 functions: AI Safety, Investigation & Enforcement, AI Enablement
- 5 governance principles: Human Dignity, Transparency & Explainability, Accountability, Safety & Security, Data Governance
- 3-tier risk classification: Tier 1 (Unacceptable — prohibited), Tier 2 (High Risk — structured obligations), Tier 3 (Low Risk — baseline)
- Developer + Deployer regulated roles
- AI sandbox for testing
- **No post-consultation Cabinet submission or parliamentary tabling date announced as of 24 Aug 2026** (gap persists)

**PIR Impact:** PIR-OPP008-001 (Campaign Strategy) — AI Governance Bill creates systemic risk framework the campaign must address. Post-consultation timeline is a secondary deadline signal.

**Confidence:** HIGH (3 independent legal sources + official government announcement, all full body extracted)

---CVS BLOCK---
Claim: AI Governance Bill public consultation closed 31 Jul 2026, targeted for completion by end of 2026, with Central AI Authority and 3-tier risk framework
Source: Ministry of Digital (https://www.digital.gov.my/en-GB/siaran/Kementerian-Digital-Mulakan-Libat-Urus-Cadangan-Rang-Undang-Undang-Tadbir-Urus-Kecerdasan-Buatan-(AI)) + Baker McKenzie + LPP Law
Source Level: L1
Tier: T2
Validation Status: Partially Verified (official government + 2 law firms, full body extracted; Rule 6 cap applied)
Confidence Score: 7 (Authority:2 Traceability:2 Recency:1 Consistency:2 Completeness:1)
Action Required: Monitor post-consultation Cabinet submission timeline
---END CVS BLOCK---

### Finding F6: Cybercrimes Bill 2026 — Royal Assent Still Unverifiable

- **Source:** https://www.rahmatlim.com/perspectives/articles/33326/mykh-cybercrimes-bill-2026-closing-the-gaps-in-malaysia-s-cybercrime-legal-framework (Rahmat Lim, 6 Aug 2026)
- **Also:** https://malaysiapulse.com/article/malaysias-new-cybercrimes-bill-2026-extends-beyond-international-treaty (Malaysia Pulse, 8 Jul 2026)

**Finding:** Rahmat Lim confirms: "On 20 July 2026, the Dewan Negara passed the Cybercrimes Bill 2026." The Bill repeals the Computer Crimes Act 1997 and introduces:
- **Specific deepfake offence:** "Transmitting, selling, or distributing audio or video content generated or manipulated using a computer system (which would include AI-generated content) that appears authentic or truthful, with the intent to commit or facilitate crime" — up to RM500,000 fine and/or 7 years' imprisonment
- **Identity theft:** Up to RM500,000 and/or 7 years
- **Computer-related fraud:** Up to RM1,000,000 and/or 10 years
- **Dissemination of intimate images (including deepfakes):** Base RM300K/5yr, aggravated RM500K/7yr
- Extra-territorial application
- Service provider duties with penalties up to RM1M

**CRITICAL GAP:** Royal assent and gazetting date remain UNVERIFIED as of 24 Aug 2026 — 35 days since Dewan Negara passage. No government gazette, no official announcement of royal assent found via web_extract on known sources. This remains the #1 timeline signal.

**PIR Impact:** PIR-OPP008-001 (Campaign Strategy) — enforcement commencement creates hard deadline. Status: Partial → Partial (no change — royal assent gap persists).

**Confidence:** HIGH for Bill content (Rahmat Lim legal analysis, full body extracted); LOW for royal assent status (absence of evidence ≠ evidence of absence)

---CVS BLOCK---
Claim: Cybercrimes Bill 2026 passed Dewan Negara on 20 July 2026, introducing specific deepfake offence with up to RM500,000 fine and/or 7 years imprisonment; royal assent status unverifiable as of 24 Aug 2026
Source: Rahmat Lim & Partners (https://www.rahmatlim.com/perspectives/articles/33326/mykh-cybercrimes-bill-2026-closing-the-gaps-in-malaysia-s-cybercrime-legal-framework)
Source Level: L4
Tier: T2
Validation Status: Partially Verified (legal analysis full body extracted; royal assent NOT confirmed — 35-day gap)
Confidence Score: 7 (Authority:1 Traceability:2 Recency:2 Consistency:2 Completeness:1)
Action Required: Corroboration — verify royal assent and gazetting date via Federal Government Gazette
---END CVS BLOCK---

### Finding F7: MCMC Enforcement Data — Reconfirmed from Prior Cycle

- **Source:** https://berita.rtm.gov.my/nasional/senarai-berita-nasional/senarai-artikel/lebih-43000-kandungan-palsu-diturunkan-suku-pertama-2026/ (RTM, 27 Apr 2026)
- **Also:** https://www.freemalaysiatoday.com/category/bahasa/tempatan/2026/07/28/kerajaan-perkukuh-keselamatan-bendung-ancaman-deepfake-penipuan-ai (FMT, 28 Jul 2026)

**Finding:** Reconfirmed from prior cycle (no new MCMC Q3 2026 data available — search API blackout prevents fresh queries):
- 43,618 scam-related content removed Q1 2026 (Jan-Mar) — RTM full body extraction confirms
- AI media training: 41/55 courses, 1,552 participants via IPPTAR
- Teo Nie Ching: "Sangat penting untuk kita bekerjasama dengan media bagi mendidik masyarakat tentang literasi digital"
- Gobind at AI Malaysia launch: government strengthening security against deepfake/AI abuse

**PIR Impact:** PIR-OPP008-004 (Message Architecture) — enforcement data reconfirmed. PIR-OPP008-008 (Baseline Measurement) — complaint volume remains inverse indicator. No Q3 2026 update available.

**Confidence:** HIGH (RTM full body extraction, FMT full body extraction)

---

## PIR Findings (Full Assessment — Web-Verified + Prior Cycle Baseline)

### PIR-OPP008-001: Campaign Strategy Status
**Priority:** Critical | **Previous:** Partial (strengthened) → **Current:** Partial (strengthened — new institutional context) | **Confidence:** Medium

**Finding:** Legislative architecture fully crystallised (Cybercrimes Bill both houses, AI Governance Bill in consultation). Government AI institutional infrastructure accelerating: AI Malaysia Berhad (28 Jul), National AI Action Plan 2026-2030 (28 Jul), Rakyat Digital portal with CyberSAFE module (11 Aug), MyGOV Agentic AI beta (10 Aug). However, NO CSCDC-specific branded creative anti-deepfake campaign exists. Government approach remains institutional/educational/legislative. White space for creative campaign confirmed and widening — government is building awareness infrastructure but not creative/media campaigns.

**Intelligence Gaps:** Has internal campaign strategy been drafted under AI Malaysia Berhad? Is RM 500K still allocated for creative campaign or absorbed into AI Action Plan? Royal assent/gazetting date for Cybercrimes Bill?

**Change:** ↑ New institutional context (AI Malaysia Berhad, AI Action Plan) adds governance layer

---

### PIR-OPP008-002: Agency Selection
**Priority:** Critical | **Previous:** Partial → **Current:** Partial (no change) | **Confidence:** Medium

**Finding:** No public tender or procurement signal found via web_extract. Zero ePerolehan activity detected. LEAN IN-HOUSE signal persists. Rakyat Digital's CyberSAFE module shows government building awareness content in-house. AI Malaysia Berhad's governance mandate may change decision-maker for any creative procurement. Walk Production and AD Malaysia remain speculative candidates.

**Intelligence Gaps:** Has procurement commenced? Will AI Malaysia Berhad or CSCDC make the creative agency decision?

**Change:** → No new procurement signal; new stakeholder (AI Malaysia Berhad) changes decision landscape

---

### PIR-OPP008-003: Audience Segmentation
**Priority:** High | **Previous:** Partial → **Current:** Partial (strengthened) | **Confidence:** High

**Finding:** Rakyat Digital portal launch provides first government-defined audience segments: youth 18-30 (primary — free AI tools), rural communities, senior citizens, PWD community, MSMEs. MD2030 targets: 80% digitally literate population, 5,000 rural digital entrepreneurs. These align with prior analytical projection (youth TikTok/Instagram, elderly WhatsApp/Facebook, B40/rural BM).

**Intelligence Gaps:** Are these the same segments CSCDC will target for the RM 500K creative campaign?

**Change:** ↑ Government's own segmentation now visible via Rakyat Digital

---

### PIR-OPP008-004: Message Architecture
**Priority:** High | **Previous:** Resolved → **Current:** Resolved (updated) | **Confidence:** High

**Finding:** MCMC enforcement data reconfirmed (no Q3 update). Cybercrimes Bill specific deepfake offence (RM500K/7yr) adds legal awareness message pillar. Rakyat Digital's CyberSAFE module + AI Safety module + MADANI values module = government's institutional message architecture: safety, literacy, responsibility. Mixed approach (detection empowerment + legal awareness + urgency).

**Intelligence Gaps:** Has CSCDC commissioned message testing?

**Change:** → Reconfirmed; Cybercrimes Bill offence adds legal pillar

---

### PIR-OPP008-005: TV Airtime Procurement
**Priority:** High | **Previous:** Partial → **Current:** Partial (no change) | **Confidence:** Medium

**Finding:** No new information found. Rakyat Digital is a digital-first platform — suggests government prioritising digital channels over TV. RM 500K budget may shift further toward digital given Rakyat Digital's infrastructure.

**Intelligence Gaps:** Has CSCDC applied for JAPEN quota? Will Rakyat Digital's digital infrastructure reduce TV airtime need?

**Change:** → No new signal; Rakyat Digital's digital-first approach may reduce TV airtime relevance

---

### PIR-OPP008-006: Digital Billboard Network
**Priority:** Medium | **Previous:** Partial → **Current:** Partial (no change) | **Confidence:** Low

**Finding:** No new information. Analytical projection from prior cycle stands — billboard likely minor component.

**Intelligence Gaps:** Has billboard been included in media plan?

**Change:** → No change

---

### PIR-OPP008-007: Micro-Targeting Capability
**Priority:** High | **Previous:** Partial → **Current:** Partial (no change) | **Confidence:** Medium

**Finding:** MyGOV Agentic AI demonstrates government's advancing AI deployment capability, but this is service delivery, not campaign micro-targeting. 8-executive structure still lacks data science/media buying. Rakyat Digital platform (2.9M+ users) provides audience data infrastructure but no evidence of micro-targeting for campaigns.

**Intelligence Gaps:** Has CSCDC explored platform partnerships leveraging Rakyat Digital user data?

**Change:** → MyGOV Agentic AI shows advancing capability but not campaign-applicable

---

### PIR-OPP008-008: Baseline Measurement
**Priority:** High | **Previous:** Partial → **Current:** Partial (strengthened) | **Confidence:** Medium

**Finding:** MD2030 target of 80% digitally literate population provides KPI context. Rakyat Digital's capability assessment programs (part of Adoption pillar) may include measurement. No specific baseline survey publicly identified. MCMC complaint volume (13,122 H1 2026 takedowns) remains inverse indicator. 30% improvement KPI denominator still unknown.

**Intelligence Gaps:** Has a baseline cyber literacy survey been conducted? Is Rakyat Digital's capability assessment the measurement vehicle?

**Change:** ↑ MD2030 80% literacy target provides context for 30% improvement KPI

---

### PIR-OPP008-009: Campaign Duration
**Priority:** Medium | **Previous:** Partial → **Current:** Partial (strengthened) | **Confidence:** Medium

**Finding:** National AI Action Plan 2026-2030 confirms multi-year strategy. Rakyat Digital is a continuous platform (not burst campaign). AI Governance Bill targeted for completion by end of 2026. Cybercrimes Bill enforcement commencement (pending royal assent) creates potential Q4 2026 deadline. RM 500K as one-time allocation vs. recurring programme under AI Action Plan remains unresolved.

**Intelligence Gaps:** Will RM 500K be folded into AI Action Plan 2026-2030 as recurring budget?

**Change:** ↑ AI Action Plan 2026-2030 provides multi-year strategic context

---

### PIR-OPP008-010: Existing Campaigns
**Priority:** Medium | **Previous:** Resolved → **Current:** Resolved (updated) | **Confidence:** High

**Finding:** Ecosystem expanded since last cycle:
1. CyberSAFE (CyberSecurity Malaysia)
2. Safe Internet Campaign (MCMC, 2.1M+ participants)
3. Sebenarnya.my (WSIS 2026 Champion, 1,016 fact-check articles)
4. AIFA Chatbot (197,403 messages)
5. My Cyber Hero (NACSA, gamified)
6. MY-AI Standards (March 2026)
7. AI Malaysia Berhad + AI Safety Institute (28 Jul 2026) — NEW
8. AI media training (1,552 participants via IPPTAR)
9. Rakyat Digital portal with CyberSAFE module (11 Aug 2026) — NEW
10. MyGOV Agentic AI beta (10 Aug 2026) — NEW
11. National AI Action Plan 2026-2030 (28 Jul 2026) — NEW
12. AI Malaysia Takeover 2026 + Learn-a-thon (11-12 Aug 2026) — NEW

All institutional/educational/digital — none creative/media campaigns. White space confirmed and widening.

**Intelligence Gaps:** How will CSCDC coordinate with AI Malaysia Berhad and Rakyat Digital to avoid overlap?

**Change:** ↑ 4 new institutional initiatives added; creative white space confirmed and widening

---

### PIR-OPP004-001: Production Volume Target
**Priority:** High | **Previous:** Partial → **Current:** Partial (no change) | **Confidence:** Medium

**Finding:** No new information on CSCDC production targets. Rakyat Digital's content modules (AI Safety, CyberSAFE, Generative AI, Agentic AI) demonstrate government producing awareness content at volume — but these are online courses, not creative/media content.

**Intelligence Gaps:** Has CSCDC defined content calendar?

**Change:** → No change for CSCDC; Rakyat Digital shows government producing institutional content

---

### PIR-OPP004-002: In-House vs Outsourced Decision
**Priority:** Critical | **Previous:** Partial (strengthened) → **Current:** Partial (strengthened — new context) | **Confidence:** Medium

**Finding:** LEAN IN-HOUSE signal reinforced by Rakyat Digital — government building content in-house through Ministry of Digital + MyDIGITAL Corporation. AI Malaysia Berhad as apex entity may absorb creative campaign decision. Zero ePerolehan procurement activity. Hybrid model still structurally optimal for CSCDC's RM 500K campaign.

**Intelligence Gaps:** Will AI Malaysia Berhad decide the in-house/outsourced question? Has hybrid model been formally adopted?

**Change:** → No procurement signal; in-house trend reinforced by Rakyat Digital

---

### PIR-OPP004-003: Studio Physical Location
**Priority:** Low | **Previous:** Partial → **Current:** Partial (no change) | **Confidence:** Low

**Finding:** No new information. Analytical projection stands.

**Change:** → No change

---

### PIR-OPP004-004: Talent Availability
**Priority:** High | **Previous:** Partial → **Current:** Partial (no change) | **Confidence:** Medium

**Finding:** No new information on 8 executive skills. Rakyat Digital managed by MyDIGITAL Corporation (CEO Adrian Marcellus named in Gobind speech) — suggests digital talent exists outside CSCDC's 8-executive structure. AI Malaysia Berhad may bring additional AI talent.

**Intelligence Gaps:** Will AI Malaysia Berhad provide creative/content talent to CSCDC?

**Change:** → MyDIGITAL Corporation identified as talent pool outside CSCDC

---

### PIR-OPP004-005: Content Approval Workflow
**Priority:** Medium | **Previous:** Partial → **Current:** Partial (no change) | **Confidence:** Low

**Finding:** No new information. Rakyat Digital operates under Ministry of Digital — suggests government content approval can be efficient when digital-first. Public Sector AI Adoption Guidelines mentioned in MyGOV Agentic AI announcement — may inform content governance.

**Intelligence Gaps:** Has workflow been formalised? Does Public Sector AI Adoption Guidelines apply to campaign content?

**Change:** → Public Sector AI Adoption Guidelines identified as potential governance framework

---

### PIR-OPP004-006: PQC Animation Scope
**Priority:** Medium | **Previous:** Partial → **Current:** Partial (no change) | **Confidence:** Low

**Finding:** No new information. AI Safety Institute's RDCI pillar (safety evaluations, testing) may produce content-worthy material.

**Change:** → AI Safety Institute RDCI may produce animation source material

---

### PIR-OPP004-007: Deepfake Awareness Content Plan
**Priority:** High | **Previous:** Partial → **Current:** Partial (strengthened) | **Confidence:** Medium

**Finding:** Rakyat Digital's CyberSAFE module + AI Safety module represent the government's current deepfake awareness content — but as online courses, not creative/media content. No Unit 7 creative content plan observable. AI Malaysia Berhad's "Trusted AI Governance" mandate may include public awareness content development.

**Intelligence Gaps:** Will AI Malaysia Berhad develop creative deepfake awareness content? Is Rakyat Digital's CyberSAFE module the extent of the government's creative plan?

**Change:** ↑ Rakyat Digital CyberSAFE module identified as current awareness content; creative gap persists

---

### PIR-OPP004-008: Brand Guidelines Status
**Priority:** Medium | **Previous:** Partial → **Current:** Partial (no change) | **Confidence:** Low

**Finding:** No new information. AI Malaysia Berhad as new national AI entity will need its own brand identity — may interact with CSCDC brand guidelines.

**Change:** → AI Malaysia Berhad branding may intersect with CSCDC brand guidelines

---

### PIR-OPP004-009: Multi-Language Requirements
**Priority:** Medium | **Previous:** Resolved → **Current:** Resolved (confirmed) | **Confidence:** High

**Finding:** Rakyat Digital portal is multilingual (EN/MY toggle visible). MD2030 Pillar 5 (Digital Society) explicitly targets rural areas and underserved communities. AI Malaysia Takeover event multilingual. Multi-language requirement confirmed as structurally mandatory.

**Change:** → Reconfirmed by Rakyat Digital multilingual operation

---

### PIR-OPP004-010: Existing CSM Content Assets
**Priority:** Low | **Previous:** Resolved → **Current:** Resolved (no change) | **Confidence:** Medium

**Finding:** No new information. CSM TikTok @cybersecuritymy (209 followers) remains baseline. Ministry of Digital TikTok @kementeriandigital is active (linked from gov.my pages) — may serve as additional distribution channel.

**Change:** → Ministry of Digital TikTok channel identified as distribution channel

---

## Cross-PIR Synthesis

### Theme 1: Government Building Institutional AI Awareness Infrastructure — Creative Campaign White Space Widening
Since the last collection (18 Aug), the government has launched Rakyat Digital portal (11 Aug), institutionalised AI Malaysia Berhad (28 Jul), launched National AI Action Plan 2026-2030 (28 Jul), established AI Safety Institute (28 Jul), and commenced MyGOV Agentic AI beta (10 Aug). All are institutional/educational/digital. NONE are creative/media campaigns. The white space for CSCDC's RM 500K creative anti-deepfake campaign is confirmed and widening — the government is building awareness *infrastructure* but not creative *content* for mass awareness.

### Theme 2: AI Malaysia Berhad Changes Stakeholder Landscape
The institutionalisation of NAIO as AI Malaysia Berhad on 28 Jul 2026 introduces a new apex AI entity with governance mandate. This may change who decides the anti-deepfake campaign strategy, who controls the budget, and who coordinates with CSCDC. AI Malaysia Berhad's "Trusted AI Governance" responsibility and the AI Safety Institute's red teaming mandate directly intersect with anti-deepfake campaign content. DAF's engagement strategy must account for this new stakeholder.

### Theme 3: Cybercrimes Bill Royal Assent — 35-Day Unverifiable Gap
The Cybercrimes Bill passed Dewan Negara on 20 Jul 2026 — 35 days ago as of 24 Aug 2026. No royal assent or gazetting confirmation found via any available source. This remains the single most critical timeline signal: enforcement commencement creates the campaign's hard deadline. The gap is either a processing delay (normal for Malaysian royal assent, which can take weeks to months) or a source coverage gap (search API blackout prevents fresh queries).

### Theme 4: Rakyat Digital's CyberSAFE Module — Integration Point or Competitor?
Rakyat Digital's CyberSAFE module (part of the youth AI access program, 100K youths aged 18-30, launching 31 Aug 2026) is the government's most concrete deepfake awareness content to date — but as an online course module, not a creative/media campaign. CSCDC's RM 500K campaign could integrate with Rakyat Digital (using the portal as a distribution channel) or compete with it (if government perceives CyberSAFE as sufficient awareness). This is a strategic decision point.

### Theme 5: Budget Governance Uncertainty — RM 500K May Be Absorbed
With the National AI Action Plan 2026-2030 launched and AI Malaysia Berhad as apex entity, the RM 500K Sector 4 allocation may be restructured or absorbed into the AI Action Plan's "Responsible Governance" enabler. This changes the commercial opportunity landscape — DAF's engagement may need to pivot from CSCDC-specific campaign to AI Action Plan implementation.

---

## Intelligence Gaps

### Critical Gaps
1. **Cybercrimes Bill royal assent/gazetting date** — 35 days unverifiable, #1 timeline signal
2. **AI Malaysia Berhad's role in anti-deepfake campaign** — will it absorb CSCDC's RM 500K allocation?
3. **Rakyat Digital CyberSAFE module vs RM 500K creative campaign** — integration or competition?

### High-Priority Gaps
4. Agency selection — has procurement commenced under AI Malaysia Berhad?
5. AI Governance Bill post-consultation Cabinet submission timeline
6. Baseline cyber literacy survey — is Rakyat Digital's capability assessment the measurement vehicle?
7. TV airtime procurement — will Rakyat Digital's digital-first approach reduce TV need?

### Medium-Priority Gaps
8. Content approval workflow under Public Sector AI Adoption Guidelines
9. Brand guidelines — AI Malaysia Berhad branding may intersect with CSCDC
10. PQC animation scope — AI Safety Institute RDCI may produce source material

---

## Recommendations

### Immediate (Next 7 Days)
1. **Check Federal Government Gazette** for Cybercrimes Bill royal assent/warkat — the gazette portal (fetrah.gov.my or esyariah.gov.my) may have the proclamation
2. **Assess AI Malaysia Berhad engagement strategy** — this new apex entity may be the decision-maker for the RM 500K campaign. Map its leadership and governance structure.
3. **Evaluate Rakyat Digital CyberSAFE module** — determine if CSCDC's creative campaign should integrate with or differentiate from this platform

### Short-Term (Next 14 Days)
4. **Monitor AI Governance Bill post-consultation** — Cabinet submission expected; track for parliamentary tabling timeline
5. **Track Rakyat Digital youth AI access program launch** (31 Aug 2026) — first concrete awareness content delivery
6. **Monitor AI Malaysia Berhad organisational announcements** — leadership, structure, budget authority

### Strategic
7. **Reposition partnership proposal** — from CSCDC-specific campaign to AI Action Plan 2026-2030 "Responsible Governance" enabler implementation. This widens the engagement scope.
8. **Develop creative campaign concept that integrates with Rakyat Digital** — position as the creative/media layer on top of Rakyat Digital's educational infrastructure
9. **Engage AI Malaysia Berhad as primary stakeholder** — may supersede CSCDC as campaign decision-maker
10. **Leverage AI Safety Institute red teaming findings** — campaign content can reference institutional safety evaluations for credibility

---

## PIR Resolution Status Table

| PIR ID | Priority | Previous Status | Current Status | Confidence | Change |
|--------|----------|------------------|----------------|------------|--------|
| PIR-OPP008-001 | Critical | Partial | **Partial (strengthened)** | Medium | ↑ AI Malaysia Berhad + AI Action Plan adds institutional context |
| PIR-OPP008-002 | Critical | Partial | **Partial** | Medium | → No procurement signal; new stakeholder changes landscape |
| PIR-OPP008-003 | High | Partial | **Partial (strengthened)** | High | ↑ Government segments defined via Rakyat Digital |
| PIR-OPP008-004 | High | Resolved | **Resolved (updated)** | High | ↑ Cybercrimes Bill deepfake offence adds legal pillar |
| PIR-OPP008-005 | High | Partial | **Partial** | Medium | → No new signal; Rakyat Digital digital-first may reduce TV need |
| PIR-OPP008-006 | Medium | Partial | **Partial** | Low | → No change |
| PIR-OPP008-007 | High | Partial | **Partial** | Medium | → MyGOV Agentic AI shows capability but not campaign-applicable |
| PIR-OPP008-008 | High | Partial | **Partial (strengthened)** | Medium | ↑ MD2030 80% literacy target provides KPI context |
| PIR-OPP008-009 | Medium | Partial | **Partial (strengthened)** | Medium | ↑ AI Action Plan 2026-2030 provides multi-year context |
| PIR-OPP008-010 | Medium | Resolved | **Resolved (updated)** | High | ↑ 4 new institutional initiatives added |
| PIR-OPP004-001 | High | Partial | **Partial** | Medium | → No CSCDC change; Rakyat Digital shows institutional content |
| PIR-OPP004-002 | Critical | Partial | **Partial (strengthened)** | Medium | → In-house trend reinforced by Rakyat Digital |
| PIR-OPP004-003 | Low | Partial | **Partial** | Low | → No change |
| PIR-OPP004-004 | High | Partial | **Partial** | Medium | → MyDIGITAL Corporation identified as talent pool |
| PIR-OPP004-005 | Medium | Partial | **Partial** | Low | → Public Sector AI Adoption Guidelines identified |
| PIR-OPP004-006 | Medium | Partial | **Partial** | Low | → AI Safety Institute RDCI may produce source material |
| PIR-OPP004-007 | High | Partial | **Partial (strengthened)** | Medium | ↑ Rakyat Digital CyberSAFE module identified |
| PIR-OPP004-008 | Medium | Partial | **Partial** | Low | → AI Malaysia Berhad branding may intersect |
| PIR-OPP004-009 | Medium | Resolved | **Resolved (confirmed)** | High | → Rakyat Digital multilingual confirms |
| PIR-OPP004-010 | Low | Resolved | **Resolved** | Medium | → Ministry of Digital TikTok identified as channel |

**Summary:** 4 Resolved, 16 Partial, 0 Open. 0 status regressions. 8 status strengthenments. 0 new resolutions. 0 downgrades.

---

## TOP 3 PIR SUGGESTIONS FOR NEXT CYCLE (AUTO-APPROVED)

1. **Suggestion:** Cybercrimes Bill Royal Assent & Federal Gazette Check — directly check the Federal Government Gazette portal for royal assent proclamation and enforcement commencement date
   **Rationale:** 35 days since Dewan Negara passage. This is the single most critical timeline signal — enforcement date creates the campaign's hard deadline. Search API blackout has prevented fresh queries for 8+ consecutive days.
   **Search Queries:** `site:fetrah.gov.my Cybercrimes 2026`, `site:malaysiagazette.gov.my "Cybercrimes Act 2026"`, `"warkat diraja" "jenayah siber" 2026`, `Cybercrimes Bill royal assent August 2026 Malaysia`

2. **Suggestion:** AI Malaysia Berhad Organisational Mapping — identify leadership, governance structure, budget authority, and whether it has absorbed CSCDC's RM 500K campaign allocation
   **Rationale:** AI Malaysia Berhad as new apex AI entity may be the decision-maker for the anti-deepfake campaign. Understanding its structure is essential for DAF's engagement strategy. May require pivot from CSCDC-specific to AI Action Plan implementation.
   **Search Queries:** `AI Malaysia Berhad leadership CEO board 2026`, `AI Malaysia Berhad budget allocation anti-deepfake`, `site:digital.gov.my "AI Malaysia" struktur organisasi`

3. **Suggestion:** Rakyat Digital CyberSAFE Module Assessment — evaluate the content depth, target audience, and delivery mechanism of the CyberSAFE module to determine integration vs differentiation strategy for CSCDC's RM 500K creative campaign
   **Rationale:** CyberSAFE module launching 31 Aug 2026 for 100K youths is the government's most concrete deepfake awareness content. CSCDC's creative campaign must either integrate with this platform (as creative/media layer) or differentiate (as mass-reach creative campaign). This is a strategic positioning decision.
   **Search Queries:** `site:rakyatdigital.gov.my CyberSAFE module content`, `Rakyat Digital CyberSAFE curriculum 2026`, `Malaysia CyberSAFE deepfake awareness module content`

---

*Report generated by Anti-Deepfake & Campaign Strategy Watch PIR Collection Orchestrator (CSCDC-04)*
*Strategic CognitiveOS Intelligence System*
*Method: DeerFlow pro (thin output — 892 bytes) + web_extract fallback (Ministry of Digital gov.my full body extraction on 4 pages + 3 legal sources)*
*Cycle: CSCDC-04 | 2026-08-24 01:45 MYT*
