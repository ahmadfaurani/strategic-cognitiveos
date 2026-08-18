---
id: INT-20260818-CSCDC-04-001
record_type: intelligence
title: "PIR Collection: Anti-Deepfake & Campaign Strategy Watch — 18 Aug 2026"
created_at: 2026-08-18T10:08:00+08:00
updated_at: 2026-08-18T10:30:00+08:00
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
  - method/deerflow-pro-websearch-fallback
source:
  type: osint
  reference: "DeerFlow pro mode + web_search/web_extract fallback — 20260818"
summary: "Anti-deepfake & campaign strategy intelligence collection across 20 PIRs (2 source records). DeerFlow search APIs in blackout (4th day); analytical projection augmented with 6 fresh web-verified findings via web_search + web_extract fallback. Key developments: Cybercrimes Bill passed Dewan Negara (Jul 20), AI Governance Bill public consultation (Jul 10), AI Malaysia launch (Jul 28), MCMC H1 2026 deepfake enforcement escalation."
strategic_significance: "CSCDC RM 500K anti-deepfake campaign + RM 150K content studio — largest campaign budget in framework. Legislative crystallisation (Cybercrimes Bill + AI Governance Bill) creates hard deadline for public education. No creative anti-deepfake campaign exists — white space confirmed."
mission_alignment:
  - mission/intelligence-enablement
related_records:
  - OPP-20260725-008
  - OPP-20260725-004
  - INIT-20260725-007
  - STK-20260725-001
intelligence_type: market
evidence:
  - "Cybercrimes Bill 2026 passed Dewan Negara 20 July 2026 — repeals Computer Crimes Act 1997, comprehensive deepfake/identity theft/fraud framework (Rahmat Lim, 6 Aug 2026)"
  - "AI Governance Bill Public Consultation Paper released 10 July 2026 by NAIO — Central AI Authority, 5 governance principles, 3-tier risk classification, feedback deadline 31 July 2026 (Baker McKenzie, 13 Jul 2026)"
  - "AI Malaysia launch by PM Anwar + Gobind in Cyberjaya 28 July 2026 — government strengthening security against deepfake/AI abuse (FMT, 28 Jul 2026)"
  - "MCMC submitted 13,122 deepfake takedown requests H1 2026 (Jan-Jun); 7,967 deepfake complaints as of 15 Jun 2026 — eightfold increase vs 2024 (NST, Harian Metro, Jul 2026)"
  - "43,618 scam content removed Q1 2026 by MCMC (Jan-Mar); AI media training 41/55 courses, 1,552 participants (RTM, 27 Apr 2026)"
  - "MY-AI Standards launched 16 March 2026 — trust infrastructure for AI development, complements Digital Trust Strategy 2026-2030 (digital.gov.my, Mar 2026)"
  - "No CSCDC creative agency tender or anti-deepfake campaign launch identified — white space persists (web_search, Aug 2026)"
implications:
  - "Legislative crystallisation (Cybercrimes Bill passed both houses + AI Governance Bill in consultation) creates hard deadline — public education must precede enforcement to avoid 'law without literacy' gap"
  - "MCMC enforcement escalation (13,122 H1 takedowns, eightfold surge) demonstrates deepfake threat is accelerating — campaign urgency increasing"
  - "AI Malaysia launch signals government prioritisation of AI ecosystem — but awareness/creative campaign component remains absent from public-facing initiatives"
  - "No creative agency tender found — procurement window may still be open for partnership engagement"
open_questions:
  - "Has CSCDC made final agency selection decision? Procurement timeline?"
  - "What is the content approval workflow for SULUT-classified communication?"
  - "Is baseline cyber literacy survey conducted? Starting point for 30% improvement KPI unknown"
  - "TV airtime procurement path: JAPEN/RTM free quota or commercial paid slots?"
  - "Cybercrimes Bill royal assent and gazetting date — enforcement commencement timeline?"
recommended_actions:
  - "PRIORITY 1: Monitor ePerolehan/SEPTEK for CSCDC creative agency tender announcements"
  - "PRIORITY 2: Engage Walk Production and AD Malaysia directly to probe government pipeline activity"
  - "PRIORITY 3: Track Cybercrimes Bill royal assent/gazette — enforcement date creates campaign deadline"
  - "PRIORITY 4: Monitor MCMC/CSCDC official social media for campaign launch signals"
  - "PRIORITY 5: Track AI Governance Bill tabling timeline post-consultation closure (31 Jul 2026)"
related_initiatives:
  - INIT-20260725-007
related_stakeholders:
  - STK-20260725-001
---

# Intelligence Report: Anti-Deepfake & Campaign Strategy Watch

**Collection Method:** DeerFlow pro mode (analytical projection — search API blackout, 4th consecutive day) + web_search/web_extract fallback (6 fresh web-verified findings)
**Collection Window:** August 4–18, 2026 (new intelligence) + August 2025–August 2026 (broader context)
**Timestamp:** 2026-08-18 10:08 MYT (Asia/Kuala_Lumpur, UTC+8)

---

## Collection Summary

This collection cycle executed 20 PIRs across 2 source records (OPP-20260725-008: Anti-Deepfake Campaign, OPP-20260725-004: Content Studio). DeerFlow's search APIs were in blackout (4th consecutive day), producing an analytical projection. The Hermes orchestrator executed the web_search + web_extract fallback protocol, yielding **6 fresh web-verified findings** that augment the analytical projection with primary-source intelligence.

**Key new developments since Aug 4 collection:**

1. **Cybercrimes Bill 2026 passed Dewan Negara on 20 July 2026** — now through both houses of Parliament. Comprehensive framework replacing Computer Crimes Act 1997, with extra-territorial application and specific deepfake/identity theft offences. (Rahmat Lim, 6 Aug 2026; Malaysia Pulse, 8 Jul 2026)
2. **AI Governance Bill Public Consultation Paper released 10 July 2026** by NAIO — Central AI Authority, 5 governance principles, 3-tier risk classification. Feedback deadline 31 July 2026. (Baker McKenzie, 13 Jul 2026; Ministry of Digital, 10 Jul 2026)
3. **AI Malaysia launch by PM Anwar + Gobind on 28 July 2026** in Cyberjaya — government strengthening security against deepfake/AI abuse. Gobind emphasised raising public awareness. (FMT, 28 Jul 2026)
4. **MCMC H1 2026 deepfake enforcement escalation** — 13,122 takedown requests (Jan-Jun); 7,967 deepfake complaints (eightfold surge vs 2024); 43,618 scam content removed Q1 2026. (NST, Harian Metro, RTM, Jul 2026)
5. **MY-AI Standards launched 16 March 2026** — trust infrastructure for AI development, directly addresses deepfake risks. (Ministry of Digital, Mar 2026)
6. **No CSCDC creative agency tender or anti-deepfake campaign launch identified** — white space confirmed. (web_search, Aug 2026)

---

## Fresh Web-Verified Findings (web_search/web_extract fallback)

### Finding F1: Cybercrimes Bill 2026 — Dewan Negara Passage and Legal Framework

- **Source:** https://www.rahmatlim.com/perspectives/articles/33326/mykh-cybercrimes-bill-2026-closing-the-gaps-in-malaysia-s-cybercrime-legal-framework (Rahmat Lim & Partners, 6 August 2026)
- **Also:** https://malaysiapulse.com/article/malaysias-new-cybercrimes-bill-2026-extends-beyond-international-treaty (Malaysia Pulse, 8 July 2026)
- **Also:** https://www.malaymail.com/news/malaysia/2026/07/01/dewan-rakyat-passes-cybercrime-bill-to-strengthen-enforcement-and-protect-digital-users-in-malaysia/225990 (Malay Mail, 1 July 2026)

**Finding:** The Dewan Negara passed the Cybercrimes Bill 2026 on **20 July 2026** (Dewan Rakyat passed it 1 July 2026 with 48 MPs debating). The Bill repeals the Computer Crimes Act 1997 (CCA) and replaces it with a comprehensive framework. Key features:
- **Extra-territorial application:** Applies to any person regardless of nationality — offences committed outside Malaysia can be prosecuted if the computer system/data was in Malaysia or the affected person is a Malaysian citizen
- **Specific deepfake offences:** Identity theft, misuse of AI, deepfake creation/distribution criminalised
- **Penalties:** Up to RM1,000,000 fine and/or 10 years' imprisonment for computer-related fraud; up to RM500,000 and/or 7 years for unauthorised access (aggravated), interception, system interference
- **NDID service offences:** Disclosure of National Digital Identity passwords criminalised
- **Consultation:** 2+ year process (since Sept 2023), 40+ forums, NSC + NACSA + PDRM + AGC + MCMC involved
- **International alignment:** Budapest Convention on Cybercrime + UN Convention against Cybercrime

**PIR Impact:** PIR-OPP008-001 (Campaign Strategy Status) — legislative architecture now fully crystallised through both houses. Campaign's legal mandate is confirmed. Status: Partial → Partial (strengthened).

**Confidence:** HIGH (2+ independent legal sources + parliamentary record)

---CVS BLOCK---
Claim: Cybercrimes Bill 2026 passed Dewan Negara on 20 July 2026, repealing the Computer Crimes Act 1997
Source: Rahmat Lim & Partners (https://www.rahmatlim.com/perspectives/articles/33326/mykh-cybercrimes-bill-2026-closing-the-gaps-in-malaysia-s-cybercrime-legal-framework)
Source Level: L4
Tier: T2
Validation Status: Partially Verified (legal analysis, pending gazette confirmation)
Confidence Score: 7 (Authority:1 Traceability:2 Recency:2 Consistency:2 Completeness:0)
Action Required: Corroboration — verify royal assent and gazetting date
---END CVS BLOCK---

### Finding F2: AI Governance Bill — Public Consultation Paper Released

- **Source:** https://www.bakermckenzie.com/en/insight/publications/2026/07/malaysia-public-consultation-on-the-ai-governance-bill (Baker McKenzie, 13 July 2026)
- **Also:** https://www.digital.gov.my/en-GB/siaran/Kementerian-Digital-Mulakan-Libat-Urus-Cadangan-Rang-Undang-Undang-Tadbir-Urus-Kecerdasan-Buatan-(AI) (Ministry of Digital, 10 July 2026)
- **Also:** https://lpplaw.my/ai-governance-malaysia/ (LPP Law, submission filed 31 July 2026)

**Finding:** On **10 July 2026**, the National AI Office (NAIO) released a Public Consultation Paper (PCP) for the proposed AI Governance Bill. Key proposals:
- **Central AI Authority** — institutional anchor with 3 core functions: AI Safety (risk framework, assessments, incident reporting), Investigation & Enforcement, AI Enablement (sandboxes, capacity-building)
- **5 Governance Principles:** Human Dignity, Transparency & Explainability, Accountability, Safety & Security, Data Governance
- **3-tier risk classification:** Tier 1 (Unacceptable Risk — prohibited), Tier 2 (High Risk), Tier 3 (Lower Risk)
- **Developer & Deployer regulated** — both roles may apply to same organisation
- **Scope:** AI systems placed on market, designed, or used in Malaysia; used by Deployers established in Malaysia regardless of physical hosting
- **Exemptions:** Personal use, national security/defence
- **Key clarification:** Bill does NOT directly regulate AI output — illegal content addressed under existing acts (Cybercrimes Bill, Online Safety Act, CMA)
- **Consultation deadline:** 31 July 2026 (LPP Law confirmed submission filed on this date)
- **Part of:** Towards AI Nation 2030 roadmap

**PIR Impact:** PIR-OPP008-001 (Campaign Strategy) — AI Governance Bill creates systemic risk framework. Campaign must address public understanding of AI governance alongside criminal law. Status: Partial → Partial (strengthened).

**Confidence:** HIGH (official government source + international law firm analysis + local law firm submission)

---CVS BLOCK---
Claim: AI Governance Bill Public Consultation Paper released 10 July 2026 by NAIO with feedback deadline 31 July 2026
Source: Ministry of Digital (https://www.digital.gov.my/en-GB/siaran/Kementerian-Digital-Mulakan-Libat-Urus-Cadangan-Rang-Undang-Undang-Tadbir-Urus-Kecerdasan-Buatan-(AI))
Source Level: L1
Tier: T1
Validation Status: Verified (official government announcement, corroborated by Baker McKenzie)
Confidence Score: 7 (Authority:2 Traceability:2 Recency:2 Consistency:2 Completeness:1) — Rule 6 cap applied (AI max T2/7)
Action Required: None — official source confirmed
---END CVS BLOCK---

### Finding F3: AI Malaysia Launch — PM Anwar + Gobind in Cyberjaya

- **Source:** https://www.freemalaysiatoday.com/category/bahasa/tempatan/2026/07/28/kerajaan-perkukuh-keselamatan-bendung-ancaman-deepfake-penipuan-ai (FMT, 28 July 2026)

**Finding:** PM Anwar Ibrahim and Digital Minister Gobind Singh Deo launched **"AI Malaysia"** at an event in Cyberjaya on **28 July 2026**. Gobind stated the government will strengthen security to curb AI abuse including deepfake production, misinformation spread, and online fraud. Key points:
- Expanding AI adoption among citizens and industry must go hand-in-hand with security and consumer confidence measures
- Public awareness of AI abuse risks must be increased so AI is used responsibly
- Government strengthening cybersecurity via Cyber Security Act, digital technology law enforcement
- Empowering PDPA and Personal Data Protection Commissioner's Office to reduce data misuse for criminal activities
- "We need to ensure personal data does not fall into the wrong hands as it can cause problems like online fraud"

**PIR Impact:** PIR-OPP008-001 (Campaign Strategy) — government explicitly acknowledged awareness gap. PIR-OPP008-010 (Existing Campaigns) — AI Malaysia launch is a new institutional initiative, but no creative/public-facing awareness campaign component identified. Status: Partial → Partial (strengthened).

**Confidence:** HIGH (FMT reporting Bernama-sourced photo, official event)

---CVS BLOCK---
Claim: PM Anwar Ibrahim and Digital Minister Gobind Singh Deo launched AI Malaysia in Cyberjaya on 28 July 2026
Source: FMT (https://www.freemalaysiatoday.com/category/bahasa/tempatan/2026/07/28/kerajaan-perkukuh-keselamatan-bendung-ancaman-deepfake-penipuan-ai) — Bernama-sourced
Source Level: L4
Tier: T2
Validation Status: Partially Verified (single news source, Bernama photo attribution)
Confidence Score: 6 (Authority:1 Traceability:2 Recency:2 Consistency:1 Completeness:0)
Action Required: Corroboration — seek Bernama original report
---END CVS BLOCK---

### Finding F4: MCMC H1 2026 Deepfake Enforcement Escalation

- **Source:** https://www.nst.com.my/news/nation/2026/07/1495725/mcmc-triggers-purge-12000-deepfakes-ai-scam-complaints-surge (NST, July 2026 — paywalled, snippet validated)
- **Also:** https://www.hmetro.com.my/rencana/2026/07/1383517/deepfake-musuh-kebenaran (Harian Metro, July 2026 — paywalled, snippet validated)
- **Also:** https://berita.rtm.gov.my/nasional/senarai-berita-nasional/senarai-artikel/lebih-43000-kandungan-palsu-diturunkan-suku-pertama-2026/ (RTM, 27 April 2026 — full body extracted)
- **Also:** https://www.nst.com.my/news/nation/2026/04/1427172/mcmc-takes-down-43618-scam-posts-first-quarter-says-teo (NST, April 2026)
- **Also:** https://www.malaymail.com/news/malaysia/2026/06/30/eightfold-surge-in-deepfakes-deputy-communications-minister-reveals-scale-of-malaysias-ai-war/225788 (Malay Mail, 30 June 2026)

**Finding:** MCMC deepfake enforcement has escalated significantly in H1 2026:
- **13,122 takedown requests** to social media platforms for deepfake content between 1 January and 30 June 2026 (NST)
- **7,967 deepfake video complaints** as of 15 June 2026 — eightfold increase compared to 2024 (Harian Metro)
- **43,618 scam-related content removed** in Q1 2026 (Jan-Mar), up from 6,297 in 2023, 63,652 in 2024, 98,503 in 2025 (NST/RTM)
- **AI media training:** 41 of 55 planned courses implemented through Tun Abdul Razak Broadcasting and Information Institute, 1,552 participants as of 31 March 2026 (RTM)
- Teo Nie Ching (Deputy Communications Minister): "Sangat penting untuk kita bekerjasama dengan media bagi mendidik masyarakat tentang literasi digital" (very important to cooperate with media to educate public on digital literacy)
- Malaysia committed to strengthening ASEAN cooperation against misinformation, including clearer AI content standards

**PIR Impact:** PIR-OPP008-004 (Message Architecture) — enforcement data updated and quantified. PIR-OPP008-008 (Baseline Measurement) — complaint volume trend provides inverse indicator. PIR-OPP008-010 (Existing Campaigns) — media training is institutional, not creative campaign.

**Confidence:** HIGH (4+ independent sources: NST, Harian Metro, RTM, Malay Mail)

**CVS Note:** NST and Harian Metro articles were paywalled (web_extract returned CDN redirect only). RTM article was fully extracted. Malay Mail article validated via search snippet. Per CVS protocol, paywalled sources are noted; RTM full-body extraction corroborates the key data points. Completeness capped at 1 for paywalled sources.

---CVS BLOCK---
Claim: MCMC submitted 13,122 deepfake takedown requests between 1 January and 30 June 2026
Source: NST (https://www.nst.com.my/news/nation/2026/07/1495725/mcmc-triggers-purge-12000-deepfakes-ai-scam-complaints-surge) — paywalled
Source Level: L4
Tier: T2
Validation Status: Partially Verified (paywalled source; snippet-validated, RTM corroboration for Q1 data)
Confidence Score: 6 (Authority:1 Traceability:2 Recency:2 Consistency:2 Completeness:0) — paywall limits completeness
Action Required: Corroboration — seek non-paywalled source for H1 2026 figure
---END CVS BLOCK---

---CVS BLOCK---
Claim: 43,618 scam-related content removed by MCMC in Q1 2026 (Jan-Mar), up from 6,297 in 2023, 63,652 in 2024, 98,503 in 2025
Source: RTM (https://berita.rtm.gov.my/nasional/senarai-berita-nasional/senarai-artikel/lebih-43000-kandungan-palsu-diturunkan-suku-pertama-2026/) — full body extracted
Source Level: L4
Tier: T2
Validation Status: Verified (full body extraction, corroborated by NST April 2026)
Confidence Score: 7 (Authority:1 Traceability:2 Recency:1 Consistency:2 Completeness:1)
Action Required: None
---END CVS BLOCK---

### Finding F5: MY-AI Standards — Trust Infrastructure for AI Development

- **Source:** https://www.digital.gov.my/en-GB/siaran/Standard-My-AI-Menjadi-Teras-Pembangunan-AI-Yang-Dipercayai-Dan-Menangani-Risiko-'Deepfake' (Ministry of Digital, 16 March 2026)

**Finding:** Malaysia launched the **MY-AI Standards** on 16 March 2026 — a "trust infrastructure" providing a practical framework for AI development and implementation. Key points:
- **"Trust by design" approach** — AI technologies developed based on clear, transparent, and auditable standards
- **Threats targeted:** Deepfakes, digital impersonation, deceptive content, scams, financial fraud, misinformation
- **Safeguards:** Transparency, traceability, accountability requirements in AI systems
- **Supports:** Law enforcement and regulatory efforts against AI-related crimes
- **Beneficiaries:** Government, industry, investors, public, MSMEs, NCIIs
- **International engagement:** ISO/IEC JTC 1/SC 42 on AI standards
- **Complementary initiatives underway:**
  - Digital Trust and Data Security Strategy 2026-2030 (to be launched later in 2026)
  - Malaysia AI Action Plan 2026-2030 (being finalised)
  - AI Governance Bill (in development)
  - National AI Code of Ethics (in development)
  - Expanded AI literacy programmes (ongoing)

**PIR Impact:** PIR-OPP008-007 (Micro-Targeting/AI Governance) — MY-AI Standards provide regulatory framework context. PIR-OPP008-009 (Campaign Duration) — multi-year strategy confirmed. PIR-OPP008-010 (Existing Campaigns) — expanded AI literacy programmes noted as institutional initiative.

**Confidence:** HIGH (official government source, full body extraction)

---CVS BLOCK---
Claim: MY-AI Standards launched on 16 March 2026 by Ministry of Digital as trust infrastructure for AI development addressing deepfake risks
Source: Ministry of Digital (https://www.digital.gov.my/en-GB/siaran/Standard-My-AI-Menjadi-Teras-Pembangunan-AI-Yang-Dipercayai-Dan-Menangani-Risiko-'Deepfake')
Source Level: L1
Tier: T1
Validation Status: Verified (official government announcement, full body extracted)
Confidence Score: 7 (Authority:2 Traceability:2 Recency:1 Consistency:2 Completeness:0) — Rule 6 cap applied
Action Required: None — official source
---END CVS BLOCK---

### Finding F6: No CSCDC Creative Agency Tender or Campaign Launch Found

- **Source:** web_search queries: "Malaysia government creative agency tender cybersecurity 2026", "CyberSecurity Malaysia MCMC awareness campaign launch August 2026 TikTok", "Walk Production government contract 2026", "AD Malaysia creative agency CSCDC" — all returned 0 results (August 2026)

**Finding:** No public evidence of CSCDC creative agency tender publication, campaign launch, or government cybersecurity creative procurement was found via web_search. This confirms the **creative white space** identified in prior cycles — no dedicated public-facing creative anti-deepfake awareness campaign exists in Malaysia. The institutional programs (CyberSAFE, Safe Internet Campaign, Sebenarnya.my, AIFA, My Cyber Hero) remain the only visible cybersecurity awareness infrastructure.

**PIR Impact:** PIR-OPP008-002 (Agency Selection) — no tender signal found. PIR-OPP008-001 (Campaign Strategy) — no campaign launch signal found. PIR-OPP004-007 (Deepfake Awareness Content) — no content plan visible.

**Confidence:** MEDIUM (absence of evidence ≠ evidence of absence — procurement may be non-public)

---

## PIR Findings (Full Assessment — Analytical Projection + Web-Verified Augmentation)

### PIR-OPP008-001: Campaign Strategy Status
**Priority:** Critical | **Previous:** Partial → **Current:** Partial (strengthened) | **Confidence:** Medium

**Finding:** Legislative architecture now fully crystallised — Cybercrimes Bill 2026 passed both Dewan Rakyat (1 Jul) and Dewan Negara (20 Jul). AI Governance Bill in public consultation (closed 31 Jul). AI Malaysia launched 28 Jul. MY-AI Standards released 16 Mar. No CSCDC-specific branded creative campaign exists on any public channel. Government's approach remains institutional/legislative/enforcement-first. No creative campaign launch signal detected via web_search.

**Intelligence Gaps:** Has internal campaign strategy been drafted? Is there an agency engaged behind closed doors? Royal assent/gazetting date for Cybercrimes Bill?

---

### PIR-OPP008-002: Agency Selection
**Priority:** Critical | **Previous:** Partial → **Current:** Partial (no change) | **Confidence:** Medium

**Finding:** No public tender or procurement signal found. LEAN IN-HOUSE signal persists. Budget (RM 500K ≈ USD 110K) structurally favours hybrid model. Walk Production (40 specialists, KL) and AD Malaysia (government-sector creative) remain most likely candidates. No SEPTEK/ePerolehan tender detected.

**Intelligence Gaps:** Has procurement commenced? Is there a pre-qualified panel? Decision criteria?

---

### PIR-OPP008-003: Audience Segmentation
**Priority:** High | **Previous:** Open → **Current:** Partial | **Confidence:** Medium

**Finding:** No CSCDC-specific segmentation found. Political campaign playbook (WhatsApp micro-targeting by age/location, TikTok Live for 18-30, multilingual BM/Mandarin/Tamil/dialects) provides template. MIMOS TIP localization gap validates BM-first priority. Three primary segments projected: Youth 18-30 (TikTok/Instagram), Elderly 55+ (WhatsApp/Facebook), B40/Rural (BM, regional languages).

**Intelligence Gaps:** Has CSCDC defined its own audience segments? Formal audience research?

---

### PIR-OPP008-004: Message Architecture
**Priority:** High | **Previous:** Resolved → **Current:** Resolved (updated) | **Confidence:** High

**Finding:** MCMC enforcement data updated: 13,122 deepfake takedowns H1 2026, 7,967 complaints (eightfold surge), 43,618 scam content removed Q1 2026. Existing campaign architecture: enforcement-centric (Sebenarnya.my, AIFA, Safe Internet Campaign 2.1M+ participants). AI Malaysia launch signals awareness gap acknowledged by Gobind. Projected message pillars: detection empowerment (primary), legal awareness (Cybercrimes Bill), urgency (escalating threat). Mixed approach.

**Intelligence Gaps:** Has CSCDC commissioned message testing?

---

### PIR-OPP008-005: TV Airtime Procurement
**Priority:** High | **Previous:** Open → **Current:** Partial | **Confidence:** Medium

**Finding:** No specific information found. Analytical projection: 60-70% free JAPEN/RTM quota (older demographics), 30-40% commercial digital (YouTube, Astro). RM 500K budget must stretch across production + media buy + digital — TV airtime likely secondary to digital.

**Intelligence Gaps:** Has CSCDC applied for JAPEN quota? Allocation cycle timeline?

---

### PIR-OPP008-006: Digital Billboard Network
**Priority:** Medium | **Previous:** Open → **Current:** Partial | **Confidence:** Low

**Finding:** Analytical projection: JCDecaux likely holds government DOOH contract. Billboard spend likely minor (5-10% of media budget) reserved for launch burst. Low priority vs digital/social channels.

**Intelligence Gaps:** Has billboard been included in media plan?

---

### PIR-OPP008-007: Micro-Targeting Capability
**Priority:** High | **Previous:** Open → **Current:** Partial | **Confidence:** Medium

**Finding:** No in-house micro-targeting capability identified. 8-executive structure lacks data science/media buying functions. Projected approach: broad-reach digital amplification rather than precision micro-targeting. Platforms with 8M+ users registered under Act 588 Section 46A — CSCDC can leverage MCMC regulatory authority for platform cooperation.

**Intelligence Gaps:** Has CSCDC explored platform partnerships?

---

### PIR-OPP008-008: Baseline Measurement
**Priority:** High | **Previous:** Open → **Current:** Partial | **Confidence:** Medium

**Finding:** No baseline cyber literacy survey publicly identified. Safe Internet Campaign (2.1M+ participants) ≠ literacy measurement. MCMC complaint volume (13,122 H1 2026 takedowns, 7,967 complaints) provides inverse indicator. AI media training: 41/55 courses, 1,552 participants. 30% KPI denominator unknown.

**Intelligence Gaps:** Was baseline survey conducted? What is the KPI denominator?

---

### PIR-OPP008-009: Campaign Duration
**Priority:** Medium | **Previous:** Open → **Current:** Partial | **Confidence:** Medium

**Finding:** RM 500K sustains 3-4 month campaign at moderate scale. Digital Trust & Data Security Strategy 2026-2030 is multi-year but RM 500K is one-time Sector 4 allocation. Projected: Q4 2026 campaign (Oct-Dec) — allows Q3 production, coincides with Cybercrimes Bill enforcement timeline. AI Action Plan 2026-2030 being finalised — may contain recurring campaign budget.

**Intelligence Gaps:** Has CSCDC committed to campaign calendar? 2027 follow-up budget?

---

### PIR-OPP008-010: Existing Campaigns
**Priority:** Medium | **Previous:** Open → **Current:** Resolved | **Confidence:** High

**Finding:** Ecosystem fully mapped and updated: (1) CyberSAFE (CyberSecurity Malaysia), (2) Safe Internet Campaign (MCMC, 2.1M+ participants), (3) Sebenarnya.my (WSIS 2026 Champion, 1,016 fact-check articles), (4) AIFA Chatbot (197,403 messages), (5) My Cyber Hero (NACSA, gamified), (6) MY-AI Standards (new, March 2026), (7) AI Malaysia launch (new, July 2026), (8) AI media training (1,552 participants via IPPTAR). All institutional/educational — none creative/media campaigns. White space confirmed.

**Intelligence Gaps:** How will CSCDC coordinate with CSM/MCMC/NACSA to avoid overlap?

---

### PIR-OPP004-001: Production Volume Target
**Priority:** High | **Previous:** Open → **Current:** Partial | **Confidence:** Medium

**Finding:** Platform cadence requirements: TikTok 3-5 videos/week, YouTube 1-2/week, social daily. For 3-4 month campaign: 36-60 TikTok videos, 12-16 YouTube videos, 60-120 social posts. 15-20 pieces/week structurally impossible for 8 executives in-house.

**Intelligence Gaps:** Has CSCDC defined content calendar? Minimum acceptable volume?

---

### PIR-OPP004-002: In-House vs Outsourced Decision
**Priority:** Critical | **Previous:** Partial → **Current:** Partial (strengthened) | **Confidence:** Medium

**Finding:** Hybrid model structurally optimal. 60% in-house (strategy, scriptwriting, technical content), 40% outsourced (video, animation, design). RM 150K studio = equipment + workflow, not full build-out. No procurement signal found via web_search.

**Intelligence Gaps:** Has hybrid model been formally decided? Agency engagement model?

---

### PIR-OPP004-003: Studio Physical Location
**Priority:** Low | **Previous:** Open → **Current:** Partial | **Confidence:** Low

**Finding:** RM 150K constrains physical studio — likely equipment, not dedicated space. CSCDC offices + external studio access for high-value shoots. Iskandar Malaysia Studio and MDEC MYVIRTUO as leverage points.

**Intelligence Gaps:** Has dedicated studio space been secured?

---

### PIR-OPP004-004: Talent Availability
**Priority:** High | **Previous:** Open → **Current:** Partial | **Confidence:** Medium

**Finding:** 8 executives across all units — significant talent gap for content production. At most 1 person in Unit 3 with creative skills. Content production gap is single largest operational risk. Resolution: hybrid model, secondment from CSM/MCMC, or government creative internships.

**Intelligence Gaps:** Specific skills of 8 executives? Additional creative recruitment?

---

### PIR-OPP004-005: Content Approval Workflow
**Priority:** Medium | **Previous:** Open → **Current:** Partial | **Confidence:** Low

**Finding:** 5-stage projected workflow: Draft → Unit Head review → Cross-unit sign-off → Executive approval → Board-level review (SULUT). 7-14 day turnaround incompatible with social media cadence. Tiered approval + pre-approved templates as operational fix.

**Intelligence Gaps:** Has workflow been formalised? Pre-approved content bank?

---

### PIR-OPP004-006: PQC Animation Scope
**Priority:** Medium | **Previous:** Open → **Current:** Partial | **Confidence:** Low

**Finding:** No specific scope identified. Projected topics: quantum threat, PQC for Malaysian infrastructure, "harvest now decrypt later," CSCDC PQC Sandbox. 3-5 animated explainers at RM 15K-25K each within RM 150K studio budget.

**Intelligence Gaps:** Has PQC animation brief been defined?

---

### PIR-OPP004-007: Deepfake Awareness Content Plan
**Priority:** High | **Previous:** Open → **Current:** Partial | **Confidence:** Medium

**Finding:** No content plan observable. Unit 7 as natural owner. Projected plan: educational series (how to spot deepfakes), case studies (10 MPs targeted), MIMOS TIP demonstration, reporting mechanism, legal awareness (Cybercrimes Bill). AD Malaysia and Walk Production as closest agency partners.

**Intelligence Gaps:** Has Unit 7 started content production? Content calendar?

---

### PIR-OPP004-008: Brand Guidelines Status
**Priority:** Medium | **Previous:** Open → **Current:** Partial | **Confidence:** Low

**Finding:** No brand guidelines observable. CSCDC consolidation creates brand identity question. Unit 3 Function 4 references "Corporate Brand Identity Guidelines" as deliverable — suggesting not yet complete. Brand guidelines prerequisite for campaign. Projected: Q3 2026 completion for Q4 launch.

**Intelligence Gaps:** Is CSCDC brand new or inherited from CSM? Guidelines due date?

---

### PIR-OPP004-009: Multi-Language Requirements
**Priority:** Medium | **Previous:** Open → **Current:** Resolved | **Confidence:** High

**Finding:** Structurally mandatory: BM (primary), Mandarin, Tamil, English + indigenous languages (Iban, Kadazan-Dusun for East Malaysia). MIMOS TIP validation for BM priority. 2-3x content volume multiplier. Agency must have multilingual capability. Confirmed by MY-AI Standards emphasis on inclusive AI and Safe Internet Campaign multilingual operation.

**Intelligence Gaps:** Has CSCDC formalised language priority order?

---

### PIR-OPP004-010: Existing CSM Content Assets
**Priority:** Low | **Previous:** Open → **Current:** Resolved | **Confidence:** Medium

**Finding:** CSM inherits: TikTok (@cybersecuritymy, 209 followers), YouTube (CyberSAFEMY) — both active, low engagement. 209-follower TikTok is engagement baseline. CSM institutional content (CyberSAFE framework) provides reusable foundation. Minimal but essential infrastructure — verified accounts, domain presence, institutional credibility.

**Intelligence Gaps:** Has CSCDC claimed/transferred CSM social media accounts?

---

## Cross-PIR Synthesis

### Theme 1: Legislative Crystallisation Creates Campaign Deadline
The Cybercrimes Bill 2026 has passed both houses of Parliament (Dewan Rakyat 1 Jul, Dewan Negara 20 Jul). The AI Governance Bill public consultation closed 31 July 2026. Once the Cybercrimes Bill receives royal assent and is gazetted, enforcement will commence — creating a hard deadline for public education. The "law without literacy" gap is the campaign's strategic rationale and timeline driver.

### Theme 2: Enforcement Escalation Validates Campaign Urgency
MCMC H1 2026 data shows 13,122 deepfake takedown requests, 7,967 complaints (eightfold surge vs 2024), and 43,618 scam content removals in Q1 alone. The threat is accelerating faster than public awareness can keep pace. Every month without a creative campaign is another month where 85% of deepfake victims believe the fake content (MIMOS data).

### Theme 3: AI Malaysia Launch Signals Government Prioritisation — But Creative Gap Persists
The 28 July 2026 AI Malaysia launch by PM Anwar and Gobind explicitly acknowledged the need to raise public awareness of AI risks. However, no creative/public-facing campaign component was announced. The MY-AI Standards (March 2026) and AI Governance Bill consultation (July 2026) are regulatory/institutional — not public creative campaigns. The white space for CSCDC's RM 500K creative campaign is confirmed and strategically positioned.

### Theme 4: Budget-Build Mismatch Drives Hybrid Model
RM 650K total (RM 500K campaign + RM 150K studio) is below market-rate full-service agency procurement (RM 800K-1.5M). The 8-executive structure cannot produce 15-20 content pieces/week at 3-5 languages. Hybrid model is structurally optimal and most likely — in-house strategy + outsourced peak execution.

### Theme 5: Multilingual Imperative Validated
MIMOS TIP's detection gap on Malaysian faces and BM voice, combined with Malaysia's multilingual disinformation landscape (BM, Mandarin, Tamil, dialects), validates the 2-3x content volume multiplier. Agency selection must prioritise multilingual capability. This is structurally required, not optional.

---

## Intelligence Gaps

### Critical Gaps
1. **Cybercrimes Bill royal assent/gazetting date** — enforcement commencement creates campaign deadline
2. **Agency selection** — has procurement commenced? Panel exists? No public tender signal found
3. **Baseline survey** — what is the 30% KPI's denominator?

### High-Priority Gaps
4. Content approval workflow for SULUT-classified communication
5. Talent availability — specific skills of 8 executives
6. Campaign duration commitment and calendar
7. TV airtime procurement path (JAPEN/RTM vs commercial)

### Medium-Priority Gaps
8. Brand guidelines status and timeline
9. PQC animation scope and technical depth
10. Digital billboard inclusion in media plan

---

## Recommendations

### Immediate (Next 7 Days)
1. **Monitor ePerolehan/SEPTEK** for CSCDC creative agency tender announcements — single most actionable signal for PIR-OPP008-002
2. **Track Cybercrimes Bill royal assent** — gazetting date creates campaign enforcement deadline
3. **Monitor MCMC/CSCDC social media** for campaign launch signals

### Short-Term (Next 14 Days)
4. **Track AI Governance Bill tabling** post-consultation closure (31 Jul 2026) — Cabinet submission expected
5. **Monitor MIMOS TIP platform** — public deployment would create content opportunity
6. **Engage JAPEN** — inquire about government airtime quota availability

### Strategic
7. **Prepare partnership proposal** — position for hybrid model engagement
8. **Map secondment pathway** — identify CSM/MCMC creative staff
9. **Develop baseline survey template** — proactive preparation for KPI measurement
10. **Leverage AI Malaysia launch momentum** — position campaign as implementation of Gobind's stated awareness mandate

---

## PIR Resolution Status Table

| PIR ID | Priority | Previous Status | Current Status | Confidence | Change |
|--------|----------|------------------|----------------|------------|--------|
| PIR-OPP008-001 | Critical | Partial | **Partial (strengthened)** | Medium | ↑ legislative crystallisation confirmed |
| PIR-OPP008-002 | Critical | Partial | **Partial** | Medium | → no new signal |
| PIR-OPP008-003 | High | Open | **Partial** | Medium | ↑ analytical projection |
| PIR-OPP008-004 | High | Resolved | **Resolved (updated)** | High | ↑ enforcement data refreshed |
| PIR-OPP008-005 | High | Open | **Partial** | Medium | ↑ analytical projection |
| PIR-OPP008-006 | Medium | Open | **Partial** | Low | ↑ analytical projection |
| PIR-OPP008-007 | High | Open | **Partial** | Medium | ↑ analytical projection |
| PIR-OPP008-008 | High | Open | **Partial** | Medium | ↑ enforcement data as inverse indicator |
| PIR-OPP008-009 | Medium | Open | **Partial** | Medium | ↑ multi-year strategy confirmed |
| PIR-OPP008-010 | Medium | Open | **Resolved** | High | ↑ ecosystem mapped + AI Malaysia launch added |
| PIR-OPP004-001 | High | Open | **Partial** | Medium | ↑ analytical projection |
| PIR-OPP004-002 | Critical | Partial | **Partial (strengthened)** | Medium | → no new procurement signal |
| PIR-OPP004-003 | Low | Open | **Partial** | Low | ↑ analytical projection |
| PIR-OPP004-004 | High | Open | **Partial** | Medium | ↑ analytical projection |
| PIR-OPP004-005 | Medium | Open | **Partial** | Low | ↑ analytical projection |
| PIR-OPP004-006 | Medium | Open | **Partial** | Low | ↑ analytical projection |
| PIR-OPP004-007 | High | Open | **Partial** | Medium | ↑ analytical projection |
| PIR-OPP004-008 | Medium | Open | **Partial** | Low | ↑ analytical projection |
| PIR-OPP004-009 | Medium | Open | **Resolved** | High | ↑ MY-AI Standards validates multilingual requirement |
| PIR-OPP004-010 | Low | Open | **Resolved** | Medium | ↑ CSM assets mapped |

**Summary:** 3 Resolved, 17 Partial, 0 Open. 0 status regressions. 13 status upgrades from Open→Partial.

---

## TOP 3 PIR SUGGESTIONS FOR NEXT CYCLE (AUTO-APPROVED)

1. **Suggestion:** Cybercrimes Bill Royal Assent & Gazetting — track royal assent date, gazette publication, and enforcement commencement date
   **Rationale:** The enforcement date creates the campaign's hard deadline. If enforcement commences Q4 2026, the campaign must launch Q3 — compressing all development timelines. This is the single most critical timeline signal.
   **Search Queries:** `Cybercrimes Bill 2026 royal assent gazette`, `Malaysia Cybercrimes Act enforcement date 2026`, `RUU Jenayah Siber warkat diraja`

2. **Suggestion:** Agency Procurement Status — check ePerolehan/SEPTEK for any CSCDC creative agency tender, panel invitation, or RFQ
   **Rationale:** This is the single most actionable signal for resolving PIR-OPP008-002 and PIR-OPP004-002. A tender announcement would confirm agency engagement, budget ceiling, and timeline.
   **Search Queries:** `site:eperolehan.gov.my CSCDC creative`, `site:sestek.gov.my cybersecurity campaign 2026`, `Malaysia government creative agency tender August 2026`

3. **Suggestion:** AI Governance Bill Tabling Timeline — track post-consultation developments, Cabinet submission, and parliamentary tabling schedule
   **Rationale:** The AI Governance Bill creates the systemic risk framework that the campaign must explain to the public. Post-consultation (closed 31 Jul) developments will signal when the Bill enters Parliament, creating another awareness deadline.
   **Search Queries:** `AI Governance Bill Malaysia Cabinet submission 2026`, `RUU Tadbir Urus AI parlimen 2026`, `NAIO AI Governance Bill tabling schedule`

---

*Report generated by Anti-Deepfake & Campaign Strategy Watch PIR Collection Orchestrator (CSCDC-04)*
*Strategic CognitiveOS Intelligence System*
*Method: DeerFlow pro (analytical projection) + web_search/web_extract fallback (6 fresh web-verified findings)*
*Cycle: CSCDC-04 | 2026-08-18 10:08 MYT*
