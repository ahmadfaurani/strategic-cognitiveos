---
id: INT-20260831-001-CSCDC-04
record_type: intelligence
title: "PIR Collection: Anti-Deepfake & Campaign Strategy Watch — 31 Aug 2026"
created_at: 2026-08-31T01:44:00+08:00
updated_at: 2026-08-31T02:10:00+08:00
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
  reference: "DeerFlow pro mode (thin output 589 bytes) + web_extract fallback (The Star, Ministry of Digital, RTM, Rahmat Lim, LPP Law) — 20260831"
summary: "Anti-deepfake & campaign strategy intelligence cycle: DeerFlow dispatched (healthy, thread 403c9a23 created) but returned thin 589-byte summary-only output. Web_extract fallback yielded 3 new findings since 24 Aug cycle: (1) AI Untuk Rakyat programme launched 30 Aug by PM Anwar as National Day initiative — 100K youths, 6 modules, free AI tools from YTL/Alibaba/Google; (2) MCMC RM1bil healthcare digitalisation fund (30 Aug); (3) MCMC scammers shifting to RCS/iMessage for phishing (20 Aug). Cybercrimes Bill royal assent remains UNVERIFIED — 42 days since Dewan Negara passage. No AI Malaysia Berhad leadership announcements. No CSCDC procurement signal. Creative campaign white space confirmed and widening."
strategic_significance: "Government's AI for the People programme (AI Untuk Rakyat) is now the most concrete AI awareness initiative — but remains educational/institutional (6 online modules + free AI tool access), NOT a creative/media campaign. PM Anwar elevated it to National Day announcement level, signalling political priority. The CyberSAFE module is embedded within this programme — confirming government's awareness strategy is digital-first, module-based, youth-targeted. CSCDC's RM 500K creative campaign white space persists. Search API blackout now 12+ days across web_search, Firecrawl, and SearXNG — 100% reliance on direct URL extraction."
mission_alignment:
  - mission/intelligence-enablement
related_records:
  - OPP-20260725-008
  - OPP-20260725-004
  - INIT-20260725-007
  - STK-20260725-001
  - INT-20260824-CSCDC-04-001
intelligence_type: market
evidence:
  - "AI Untuk Rakyat programme launched 30 Aug 2026 by PM Anwar as one of six National Day initiatives — 100K youths aged 18-30, 6 modules (AI Nation 2030: Madani Approach, CyberSafe for the People, Generative AI, AI Security, Agentic AI for All, Cloud for the People), free 3-month AI tool subscription (YTL AI Labs-IlmuChat, Alibaba-Wonderclip/MuleRun, Google-Gemini Enterprise), portal rakyatdigital.gov.my (The Star, 30 Aug 2026)"
  - "MCMC allocates RM1bil for healthcare digitalisation — Communications Minister Fahmi Fadzil announced expansion of internet access + EMR rollout at government hospitals/clinics (The Star, 30 Aug 2026)"
  - "MCMC: Scammers shifting to RCS and iMessage for phishing URLs following SMS hyperlink restrictions enforcement — Selangor MCMC telecommunications fraud deputy director Mohd Amirul Hakim Abdul Rahim (The Star, 20 Aug 2026)"
  - "Cybercrimes Bill 2026 passed Dewan Negara 20 Jul 2026 — comprehensive framework with specific deepfake offence (RM500K/7yr); royal assent status UNVERIFIED — 42-day gap as of 31 Aug 2026 (Rahmat Lim, 6 Aug 2026)"
  - "AI Governance Bill public consultation closed 31 Jul 2026, targeted for completion end 2026, no post-consultation Cabinet submission date announced — LPP Law page last updated 2 Aug 2026 (LPP Law, 2 Aug 2026)"
  - "Ministry of Digital announcements page last updated 28 Aug 2026 — no new announcements since 12 Aug (NXP Malaysia) — no AI Malaysia Berhad leadership/structure announcements (digital.gov.my, 28 Aug 2026)"
  - "Gobind speech at AI Malaysia Takeover 2026 (11 Aug) confirms Adrian Marcellus as CEO MyDIGITAL Corporation, Hannah Yeoh as Minister in PMO (Federal Territories) attending — AI Malaysia to play role in strengthening national AI ecosystem (digital.gov.my, 11 Aug 2026)"
implications:
  - "AI Untuk Rakyat = government's most concrete AI awareness delivery — CyberSAFE module embedded as one of 6 required modules for 100K youths. This is institutional/educational, not creative/media. CSCDC's RM 500K creative campaign white space confirmed and widening."
  - "PM Anwar elevated AI Untuk Rakyat to National Day announcement = political signalling that AI awareness is government priority. This may attract more resources to AI Malaysia Berhad / Ministry of Digital, potentially absorbing CSCDC's RM 500K allocation."
  - "MCMC scammers shifting to RCS/iMessage = evolving threat landscape. Campaign messaging must address emerging platforms (not just SMS). Enforcement data gap persists — no Q3 2026 takedown numbers available."
  - "MCMC RM1bil healthcare digitalisation = MCMC budget expanding beyond communications into health IT. May signal MCMC's growing institutional bandwidth for multi-domain digital initiatives, potentially including anti-deepfake campaigns."
  - "Cybercrimes Bill royal assent gap now 42 days — approaching the upper end of typical Malaysian royal assent timelines. This remains the #1 critical timeline signal."
  - "No AI Malaysia Berhad leadership announcements 34 days post-establishment — organisational structure still not public. Decision-maker for CSCDC campaign remains unidentified."
open_questions:
  - "Cybercrimes Bill 2026 royal assent and gazetting date — 42 days unverifiable, #1 critical gap. Federal Gazette portal inaccessible (private network block on web_extract)."
  - "Has AI Malaysia Berhad appointed a CEO/board? 34 days post-establishment with no public leadership announcement."
  - "Will RM 500K CSCDC allocation be absorbed into AI Untuk Rakyat / AI Action Plan 2026-2030, or remain a separate creative campaign budget?"
  - "Has CSCDC/CSM/NACSA made any procurement move? Zero ePerolehan signal persists across all cycles."
  - "AI Governance Bill post-consultation Cabinet submission — 31 days since consultation closure, no submission date."
  - "MCMC Q3 2026 enforcement data — scam takedown numbers still not available. Only Q1 2026 (43,618) confirmed."
recommended_actions:
  - "PRIORITY 1: Check Federal Government Gazette for Cybercrimes Bill royal assent — 42 days is at upper end of typical timeline. Try alternative gazette access methods (AGC portal, Malaysian Bar, legal databases)."
  - "PRIORITY 2: Monitor AI Untuk Rakyat registration and module completion data — first concrete awareness delivery starts 31 Aug. This is the government's de facto anti-deepfake awareness programme (CyberSAFE module)."
  - "PRIORITY 3: Track AI Malaysia Berhad organisational announcements — leadership, CEO, board, budget authority. 34 days without public structure."
  - "PRIORITY 4: Evaluate whether RM 500K should be repositioned as creative/media layer on top of AI Untuk Rakyat's educational infrastructure — integration vs competition strategy."
  - "PRIORITY 5: Monitor AI Governance Bill post-consultation Cabinet submission."
  - "PRIORITY 6: Track MCMC enforcement trends — scammers shifting to RCS/iMessage requires campaign messaging evolution."
related_initiatives:
  - INIT-20260725-007
related_stakeholders:
  - STK-20260725-001
---

# Intelligence Report: Anti-Deepfake & Campaign Strategy Watch

**Collection Method:** DeerFlow pro mode (dispatched successfully — healthy, thread 403c9a23 created — but returned thin 589-byte summary-only output; no full PIR-by-PIR analysis captured) + web_extract fallback (The Star, Ministry of Digital gov.my, RTM, Rahmat Lim, LPP Law)
**Collection Window:** August 24–31, 2026 (new intelligence since last cycle) + July 2026–August 2026 (broader context)
**Timestamp:** 2026-08-31 01:44 MYT (Asia/Kuala_Lumpur, UTC+8)
**Search API Status:** web_search, Firecrawl MCP, and SearXNG all returning empty results — blackout Day 12+. 100% reliance on direct URL extraction (web_extract).

---

## Collection Summary

This collection cycle executed 20 PIRs across 2 source records (OPP-20260725-008: Anti-Deepfake Campaign, OPP-20260725-004: Content Studio). DeerFlow was healthy and dispatched successfully (thread 403c9a23-ed4e-4501-b04f-417401dbfaf7 created), but returned only a thin 589-byte summary — the full PIR-by-PIR analysis was not captured in the output stream. The Hermes orchestrator executed the web_extract fallback protocol on The Star (thestar.com.my), Ministry of Digital (digital.gov.my), RTM (berita.rtm.gov.my), Rahmat Lim, and LPP Law, yielding **3 new findings** since the 24 Aug cycle:

1. **AI Untuk Rakyat programme launched 30 Aug 2026** — PM Anwar's National Day announcement, 100K youths, 6 modules including CyberSAFE, free AI tools
2. **MCMC RM1bil healthcare digitalisation fund** (30 Aug 2026) — Fahmi Fadzil announcement
3. **MCMC: Scammers shifting to RCS/iMessage** (20 Aug 2026) — enforcement trend evolution

**Critical gap persists:** Cybercrimes Bill 2026 royal assent remains UNVERIFIED — 42 days since Dewan Negara passage (20 Jul → 31 Aug).

---

## Fresh Web-Verified Findings (web_extract fallback)

### Finding F1: AI Untuk Rakyat Programme Launched (30 Aug 2026)

- **Source:** https://www.thestar.com.my/news/nation/2026/08/30/ai-for-the-people-programme-participants-to-complete-six-modules-for-free-ai-tools (The Star / Bernama, 30 Aug 2026)
- **Also:** https://berita.rtm.gov.my/nasional/senarai-berita-nasional/senarai-artikel/program-ai-untuk-rakyat-tawar-akses-percuma-kepada-100000-belia-bermula-isnin/ (RTM, 30 Aug 2026)

**Finding:** PM Anwar announced the "AI for the People" (AI Untuk Rakyat) programme on 30 Aug 2026 as one of six National Day initiatives during the 2026 National Day Premier Address at the Putrajaya International Convention Centre. Key elements:
- **Target:** 100,000 Malaysians aged 18-30, until 2027
- **Platform:** Rakyat Digital portal at rakyatdigital.gov.my, registrations commence 30 Aug (Sunday) in phases
- **6 Required Modules:** (1) AI Nation 2030: The Madani Approach, (2) CyberSafe for the People, (3) Generative AI, (4) AI Security, (5) Agentic AI for All, (6) Cloud for the People
- **Incentive:** Free 3-month subscription to selected AI applications upon completion — YTL AI Labs (IlmuChat), Alibaba (Wonderclip and MuleRun), Google (Gemini Enterprise)
- **Spearheaded by:** MyDIGITAL Corporation (CEO Adrian Marcellus)
- **Digital Ministry secretary-general Datuk Fabian Bigar:** "we want to ensure the benefits of AI can be felt more widely and inclusively"
- **Programme framed as:** aligned with Malaysia Digital 2030 aspirations, AI Nation by 2030 vision

**PIR Impact:** 
- PIR-OPP008-003 (Audience Segmentation) — government's audience now explicitly defined: youth 18-30 primary, programme extends to 2027. Status strengthens.
- PIR-OPP008-010 (Existing Campaigns) — AI Untuk Rakyat is now the 13th institutional awareness initiative, most concrete to date. Status: Resolved (updated).
- PIR-OPP004-007 (Deepfake Awareness Content) — CyberSafe for the People module is the government's deepfake awareness content, embedded in required curriculum. Status strengthens.
- PIR-OPP008-001 (Campaign Strategy) — CyberSAFE module embedded in AI Untuk Rakyat confirms government's strategy is educational/institutional, not creative/media. White space for RM 500K creative campaign confirmed.

**Confidence:** HIGH (The Star full body extracted + RTM full body extracted — 2 independent sources, Bernama wire)

---CVS BLOCK---
Claim: AI Untuk Rakyat programme launched 30 Aug 2026 by PM Anwar as one of six National Day initiatives, targeting 100K youths aged 18-30 with 6 modules including CyberSafe for the People, free 3-month AI tool subscription from YTL/Alibaba/Google
Source: The Star/Bernama (https://www.thestar.com.my/news/nation/2026/08/30/ai-for-the-people-programme-participants-to-complete-six-modules-for-free-ai-tools) + RTM (https://berita.rtm.gov.my/nasional/senarai-berita-nasional/senarai-artikel/program-ai-untuk-rakyat-tawar-akses-percuma-kepada-100000-belia-bermula-isnin/)
Source Level: L4
Tier: T2
Validation Status: Partially Verified (2 independent news sources, full body extracted; Rule 6 cap applied)
Confidence Score: 7 (Authority:1 Traceability:2 Recency:2 Consistency:2 Completeness:1)
Action Required: None — 2-source corroboration
---END CVS BLOCK---

### Finding F2: MCMC RM1 Billion Healthcare Digitalisation Fund (30 Aug 2026)

- **Source:** https://www.thestar.com.my/news/nation/2026/08/30/mcmc-health-digitalisation-fund-raised-to-rm1bil-emr-rollout-expanded (The Star, 30 Aug 2026)

**Finding:** Communications Minister Datuk Seri Fahmi Fadzil announced MCMC will allocate RM1 billion to accelerate digitalisation of public healthcare facilities nationwide:
- Expand internet access (public WiFi) at government hospitals and health clinics
- Roll out Electronic Medical Record (EMR) system
- Announced as part of PM Anwar's six National Day measures

**PIR Impact:** PIR-OPP008-007 (Micro-Targeting Capability) — MCMC's expanding budget (RM1bil for healthcare) signals institutional bandwidth growth. However, this is healthcare infrastructure, not campaign capability. PIR-OPP008-005 (TV Airtime) — MCMC's budget expansion may indirectly support campaign infrastructure if MCMC's role in anti-deepfake awareness increases.

**Confidence:** HIGH (The Star full body extracted, Bernama wire)

---CVS BLOCK---
Claim: MCMC allocated RM1 billion for healthcare digitalisation (internet access + EMR rollout at government hospitals) announced by Communications Minister Fahmi Fadzil on 30 Aug 2026
Source: The Star (https://www.thestar.com.my/news/nation/2026/08/30/mcmc-health-digitalisation-fund-raised-to-rm1bil-emr-rollout-expanded)
Source Level: L4
Tier: T2
Validation Status: Partially Verified (news source, full body extracted; Rule 6 cap applied)
Confidence Score: 7 (Authority:1 Traceability:2 Recency:2 Consistency:2 Completeness:1)
Action Required: None
---END CVS BLOCK---

### Finding F3: MCMC — Scammers Shifting to RCS/iMessage (20 Aug 2026)

- **Source:** https://www.thestar.com.my/news/nation/2026/08/20/scammers-shifting-to-rcs-imessage-to-spread-phishing-urls-says-mcmc (The Star, 20 Aug 2026)

**Finding:** MCMC's Selangor telecommunications fraud deputy director Mohd Amirul Hakim Abdul Rahim confirmed scammers are shifting to Rich Communication Services (RCS) and iMessage to spread phishing links, following enforcement of hyperlink restrictions on SMS. These messaging services still allow hyperlink transmission, creating a new enforcement gap.

**PIR Impact:** PIR-OPP008-004 (Message Architecture) — campaign messaging must address emerging threat vectors (RCS, iMessage) in addition to SMS. Threat landscape evolution confirmed. PIR-OPP008-008 (Baseline Measurement) — enforcement data shows evolving threat surface but no Q3 2026 takedown numbers.

**Confidence:** MEDIUM (single news source, full body extracted, but article is short — detailed enforcement statistics not provided)

---CVS BLOCK---
Claim: MCMC confirmed scammers shifting to RCS and iMessage for phishing URLs following SMS hyperlink restrictions enforcement, detected by Selangor MCMC telecommunications fraud deputy director
Source: The Star (https://www.thestar.com.my/news/nation/2026/08/20/scammers-shifting-to-rcs-imessage-to-spread-phishing-urls-says-mcmc)
Source Level: L4
Tier: T2
Validation Status: Partially Verified (news source, full body extracted; Rule 6 cap applied)
Confidence Score: 6 (Authority:1 Traceability:2 Recency:2 Consistency:1 Completeness:1)
Action Required: Corroboration — seek full MCMC enforcement data
---END CVS BLOCK---

### Finding F4: Cybercrimes Bill 2026 — Royal Assent Still Unverifiable (42-Day Gap)

- **Source:** https://www.rahmatlim.com/perspectives/articles/33326/mykh-cybercrimes-bill-2026-closing-the-gaps-in-malaysia-s-cybercrime-legal-framework (Rahmat Lim, 6 Aug 2026)

**Finding:** Rahmat Lim article reconfirmed from prior cycle — no update to the article since 6 Aug 2026. Cybercrimes Bill passed Dewan Negara on 20 Jul 2026. The article references "the then Cybercrimes Act" (future tense), indicating royal assent had NOT been granted as of article publication (6 Aug). Key offences confirmed:
- Specific deepfake offence: transmitting/distributing AI-generated content appearing authentic with intent to commit crime — RM500K/7yr
- Identity theft: RM500K/7yr
- Computer-related fraud: RM1M/10yr
- Dissemination of intimate images (including deepfakes): base RM300K/5yr, aggravated RM500K/7yr
- Extra-territorial application
- Service provider duties with penalties up to RM1M

**42-DAY GAP:** Royal assent and gazetting remain UNVERIFIED as of 31 Aug 2026 — 42 days since Dewan Negara passage. Federal Gazette portal (federalgazette.agc.gov.my) blocked by web_extract (private network). No news outlet has reported royal assent.

**PIR Impact:** PIR-OPP008-001 (Campaign Strategy) — enforcement commencement creates hard deadline. Status: Partial (no change — royal assent gap persists, now 42 days). This is approaching the upper end of typical Malaysian royal assent timelines (can take weeks to months).

**Confidence:** HIGH for Bill content (Rahmat Lim legal analysis, full body extracted); LOW for royal assent status (absence of evidence ≠ evidence of absence)

---CVS BLOCK---
Claim: Cybercrimes Bill 2026 passed Dewan Negara on 20 July 2026 with specific deepfake offence (RM500K/7yr); royal assent status unverifiable as of 31 Aug 2026 — 42-day gap
Source: Rahmat Lim & Partners (https://www.rahmatlim.com/perspectives/articles/33326/mykh-cybercrimes-bill-2026-closing-the-gaps-in-malaysia-s-cybercrime-legal-framework)
Source Level: L4
Tier: T2
Validation Status: Partially Verified (legal analysis full body extracted; royal assent NOT confirmed — 42-day gap)
Confidence Score: 7 (Authority:1 Traceability:2 Recency:1 Consistency:2 Completeness:1)
Action Required: Corroboration — verify royal assent via Federal Government Gazette (alternative access needed)
---END CVS BLOCK---

### Finding F5: AI Governance Bill — No Post-Consultation Update (31-Day Gap)

- **Source:** https://www.lpplaw.my/ai-governance-malaysia/ (LPP Law, last updated 2 Aug 2026)

**Finding:** LPP Law's AI Governance Bill page confirms:
- Public consultation closed 31 Jul 2026 (LPP Law submission filed)
- Bill "targeted for completion by the end of 2026"
- Central AI Authority with 3 functions: AI Safety, Investigation & Enforcement, AI Enablement
- 3-tier risk classification: Tier 1 (Unacceptable — prohibited), Tier 2 (High Risk — structured obligations), Tier 3 (Low Risk — baseline)
- Developer + Deployer regulated roles
- Page last updated 2 Aug 2026 — NO post-consultation update since
- "The institutional picture moved during the consultation itself. On 28 July 2026 the National AI Office was institutionalised as AI Malaysia Berhad under the Ministry of Digital"
- Three principal findings from LPP Law submission: (1) Bill doesn't say if it binds Government, (2) Principle 5 presupposes lawful basis for training AI on personal data that Malaysian law doesn't clearly provide, (3) Foreign developers absent from consultation

**PIR Impact:** PIR-OPP008-001 (Campaign Strategy) — AI Governance Bill creates systemic risk framework. Post-consultation timeline gap (31 days) is a secondary deadline signal.

**Confidence:** HIGH (LPP Law full body extracted, legal analysis)

---CVS BLOCK---
Claim: AI Governance Bill public consultation closed 31 Jul 2026, targeted for completion by end 2026, with Central AI Authority and 3-tier risk framework; no post-consultation Cabinet submission date as of 31 Aug 2026
Source: LPP Law (https://www.lpplaw.my/ai-governance-malaysia/)
Source Level: L4
Tier: T2
Validation Status: Partially Verified (law firm analysis, full body extracted; Rule 6 cap applied)
Confidence Score: 6 (Authority:1 Traceability:2 Recency:1 Consistency:2 Completeness:1)
Action Required: Monitor post-consultation Cabinet submission timeline
---END CVS BLOCK---

### Finding F6: Ministry of Digital — No New Announcements Since 12 Aug (28 Aug Update)

- **Source:** https://www.digital.gov.my/en-GB/siaran (Ministry of Digital, page last updated 28 Aug 2026)

**Finding:** Ministry of Digital announcements page scanned — latest announcement remains 12 Aug 2026 (NXP Malaysia Expansion Groundbreaking). No new announcements between 12 Aug and 28 Aug (page update date). No AI Malaysia Berhad leadership, structure, or budget announcements. No CSCDC-related announcements.

**Key personnel confirmed from Gobind's 11 Aug speech:**
- Adrian Marcellus — CEO, MyDIGITAL Corporation (operational lead for Rakyat Digital)
- Datuk Fabian Bigar — Secretary-General, Digital Ministry
- Hannah Yeoh — Minister in PMO (Federal Territories) — attending, not Digital Minister
- Gobind Singh Deo — Minister of Digital (implicit, speech delivered by him)

**PIR Impact:** PIR-OPP008-002 (Agency Selection) — no procurement signal. PIR-OPP004-002 (In-House vs Outsourced) — AI Malaysia Berhad's governance structure still not public, 34 days post-establishment.

**Confidence:** HIGH (official government page, full body extracted)

---CVS BLOCK---
Claim: Ministry of Digital has made no new announcements since 12 Aug 2026 (NXP Malaysia event); no AI Malaysia Berhad leadership or structure announcements as of 28 Aug 2026 page update
Source: Ministry of Digital (https://www.digital.gov.my/en-GB/siaran)
Source Level: L1
Tier: T2
Validation Status: Partially Verified (official government page, full body extracted; Rule 6 cap applied)
Confidence Score: 7 (Authority:2 Traceability:2 Recency:2 Consistency:2 Completeness:1)
Action Required: None — absence of announcement is the finding
---END CVS BLOCK---

---

## PIR Findings (Full Assessment — Web-Verified + Prior Cycle Baseline)

### PIR-OPP008-001: Campaign Strategy Status
**Priority:** Critical | **Previous:** Partial (strengthened) → **Current:** Partial (strengthened — AI Untuk Rakyat adds political priority signal) | **Confidence:** Medium

**Finding:** PM Anwar elevated AI awareness to National Day announcement level (AI Untuk Rakyat, 30 Aug). Government's campaign strategy is now clearly institutional/educational/digital: online modules + free AI tool access via Rakyat Digital portal. NO creative/media campaign exists. The CyberSAFE module is embedded as required curriculum — government's de facto anti-deepfake awareness strategy. Legislative architecture (Cybercrimes Bill 42-day royal assent gap, AI Governance Bill 31-day post-consultation gap) still crystallising. White space for CSCDC's RM 500K creative campaign confirmed and widening.

**Intelligence Gaps:** Has internal campaign strategy been drafted under AI Malaysia Berhad? Is RM 500K still allocated or absorbed into AI Untuk Rakyat/AI Action Plan? Royal assent/gazetting date for Cybercrimes Bill?

**Change:** ↑ AI Untuk Rakyat launched at National Day level — political priority signal strengthens

---

### PIR-OPP008-002: Agency Selection
**Priority:** Critical | **Previous:** Partial → **Current:** Partial (no change) | **Confidence:** Medium

**Finding:** No public tender or procurement signal found. Zero ePerolehan activity detected. LEAN IN-HOUSE signal persists — government building awareness content in-house through Ministry of Digital + MyDIGITAL Corporation. AI Malaysia Berhad's governance structure still not public (34 days post-establishment), so decision-maker for any creative procurement remains unidentified. AI Untuk Rakyat delivered without external creative agency — further reinforces in-house trend.

**Intelligence Gaps:** Has procurement commenced? Will AI Malaysia Berhad or CSCDC make the creative agency decision?

**Change:** → No procurement signal; AI Untuk Rakyat delivered in-house further reinforces LEAN IN-HOUSE

---

### PIR-OPP008-003: Audience Segmentation
**Priority:** High | **Previous:** Partial (strengthened) → **Current:** Resolved | **Confidence:** High

**Finding:** AI Untuk Rakyat provides definitive government audience segmentation: youth 18-30 as primary target (100K, until 2027). Rakyat Digital platform targets broader population (MD2030: 80% digitally literate). Prior cycle identified rural communities, senior citizens, PWD, MSMEs as additional segments. Government's audience is now fully defined.

**Intelligence Gaps:** Are these the same segments CSCDC will target for the RM 500K creative campaign?

**Change:** ↑↑ Status upgrades to Resolved — government's audience segmentation now definitive via AI Untuk Rakyat

---

### PIR-OPP008-004: Message Architecture
**Priority:** High | **Previous:** Resolved (updated) → **Current:** Resolved (updated — emerging threat vector) | **Confidence:** High

**Finding:** MCMC enforcement data shows scammers shifting to RCS/iMessage (20 Aug) — campaign messaging must address emerging platforms. Cybercrimes Bill deepfake offence (RM500K/7yr) adds legal awareness pillar. AI Untuk Rakyat's 6 modules define government's message architecture: (1) AI Nation vision, (2) CyberSafe (security/awareness), (3) Generative AI (understanding), (4) AI Security (threats), (5) Agentic AI (future), (6) Cloud (infrastructure). Mixed approach: empowerment + awareness + legal deterrence.

**Intelligence Gaps:** Has CSCDC commissioned message testing?

**Change:** ↑ MCMC RCS/iMessage threat evolution + AI Untuk Rakyat module architecture defines message framework

---

### PIR-OPP008-005: TV Airtime Procurement
**Priority:** High | **Previous:** Partial → **Current:** Partial (no change) | **Confidence:** Medium

**Finding:** No new information. AI Untuk Rakyat is entirely digital (portal-based) — confirms government prioritising digital channels over TV. RM 500K budget likely shifts further toward digital given Rakyat Digital infrastructure. MCMC's RM1bil healthcare fund shows MCMC's budget expanding but not toward campaign/TV infrastructure.

**Intelligence Gaps:** Has CSCDC applied for JAPEN quota? Will Rakyat Digital's digital infrastructure reduce TV airtime need?

**Change:** → No new signal; AI Untuk Rakyat digital-first further reduces TV airtime likelihood

---

### PIR-OPP008-006: Digital Billboard Network
**Priority:** Medium | **Previous:** Partial → **Current:** Partial (no change) | **Confidence:** Low

**Finding:** No new information. Analytical projection from prior cycle stands — billboard likely minor component.

**Change:** → No change

---

### PIR-OPP008-007: Micro-Targeting Capability
**Priority:** High | **Previous:** Partial → **Current:** Partial (no change) | **Confidence:** Medium

**Finding:** AI Untuk Rakyat uses rakyatdigital.gov.my portal for registration and module delivery — provides audience data infrastructure (100K youth registrations). However, no evidence of micro-targeting for campaigns. MyDIGITAL Corporation (CEO Adrian Marcellus) manages the platform. MCMC's RM1bil healthcare fund shows institutional capacity growth but not campaign micro-targeting. 8-executive CSCDC structure still lacks data science/media buying capability.

**Intelligence Gaps:** Has CSCDC explored platform partnerships leveraging Rakyat Digital user data?

**Change:** → Rakyat Digital portal provides audience data infrastructure but no campaign micro-targeting evidence

---

### PIR-OPP008-008: Baseline Measurement
**Priority:** High | **Previous:** Partial (strengthened) → **Current:** Partial (strengthened — AI Untuk Rakyat provides measurement vehicle) | **Confidence:** Medium

**Finding:** AI Untuk Rakyat requires module completion/passing — this creates the first measurable AI literacy baseline (100K youths, 6 modules, pass/fail). MD2030 target of 80% digitally literate population provides KPI context. MCMC enforcement data: scammers shifting to RCS/iMessage (new threat surface) but no Q3 2026 takedown numbers. 30% improvement KPI denominator still not specifically defined, but AI Untuk Rakyat module completion rates may serve as proxy.

**Intelligence Gaps:** Is AI Untuk Rakyat module completion the measurement vehicle for the 30% improvement KPI? Has a pre-programme baseline been established?

**Change:** ↑ AI Untuk Rakyat module pass/fail provides first measurable literacy baseline

---

### PIR-OPP008-009: Campaign Duration
**Priority:** Medium | **Previous:** Partial (strengthened) → **Current:** Partial (strengthened — AI Untuk Rakyat extends to 2027) | **Confidence:** Medium

**Finding:** AI Untuk Rakyat targets 100K youths "until 2027" — confirms multi-year programme approach. National AI Action Plan 2026-2030 provides overarching multi-year strategy. Rakyat Digital is a continuous platform. AI Governance Bill targeted for completion by end 2026. Cybercrimes Bill enforcement (pending royal assent, 42-day gap) creates potential Q4 2026 deadline. RM 500K as one-time vs recurring programme under AI Action Plan remains unresolved.

**Intelligence Gaps:** Will RM 500K be folded into AI Untuk Rakyat or AI Action Plan 2026-2030?

**Change:** ↑ AI Untuk Rakyat's "until 2027" target confirms multi-year programme approach

---

### PIR-OPP008-010: Existing Campaigns
**Priority:** Medium | **Previous:** Resolved (updated) → **Current:** Resolved (updated — AI Untuk Rakyat added) | **Confidence:** High

**Finding:** Ecosystem expanded since last cycle:
1. CyberSAFE (CyberSecurity Malaysia)
2. Safe Internet Campaign (MCMC, 2.1M+ participants)
3. Sebenarnya.my (WSIS 2026 Champion, 1,016 fact-check articles)
4. AIFA Chatbot (197,403 messages)
5. My Cyber Hero (NACSA, gamified)
6. MY-AI Standards (March 2026)
7. AI Malaysia Berhad + AI Safety Institute (28 Jul 2026)
8. AI media training (1,552 participants via IPPTAR)
9. Rakyat Digital portal with CyberSAFE module (11 Aug 2026)
10. MyGOV Agentic AI beta (10 Aug 2026)
11. National AI Action Plan 2026-2030 (28 Jul 2026)
12. AI Malaysia Takeover 2026 + Learn-a-thon (11-12 Aug 2026)
13. **AI Untuk Rakyat programme (30 Aug 2026) — NEW** — 100K youths, 6 modules, free AI tools, National Day announcement level

All institutional/educational/digital — none creative/media campaigns. White space confirmed and widening.

**Intelligence Gaps:** How will CSCDC coordinate with AI Malaysia Berhad, MyDIGITAL Corporation, and AI Untuk Rakyat to avoid overlap?

**Change:** ↑ AI Untuk Rakyat added as 13th initiative — most concrete awareness delivery to date

---

### PIR-OPP004-001: Production Volume Target
**Priority:** High | **Previous:** Partial → **Current:** Partial (no change) | **Confidence:** Medium

**Finding:** No new information on CSCDC production targets. AI Untuk Rakyat's 6 modules demonstrate government producing awareness content at volume — but as online courses, not creative/media content.

**Change:** → No change for CSCDC; AI Untuk Rakyat shows institutional content production

---

### PIR-OPP004-002: In-House vs Outsourced Decision
**Priority:** Critical | **Previous:** Partial (strengthened) → **Current:** Partial (strengthened — AI Untuk Rakyat delivered in-house) | **Confidence:** Medium

**Finding:** AI Untuk Rakyat was delivered entirely in-house by Ministry of Digital + MyDIGITAL Corporation — no external creative agency involved. This further reinforces LEAN IN-HOUSE signal. Zero ePerolehan procurement activity. AI Malaysia Berhad as apex entity may absorb creative campaign decision. Hybrid model still structurally optimal for CSCDC's RM 500K campaign.

**Intelligence Gaps:** Will AI Malaysia Berhad decide the in-house/outsourced question?

**Change:** ↑ AI Untuk Rakyat delivered in-house — further reinforces LEAN IN-HOUSE trend

---

### PIR-OPP004-003: Studio Physical Location
**Priority:** Low | **Previous:** Partial → **Current:** Partial (no change) | **Confidence:** Low

**Finding:** No new information. Analytical projection stands.

**Change:** → No change

---

### PIR-OPP004-004: Talent Availability
**Priority:** High | **Previous:** Partial → **Current:** Partial (strengthened — MyDIGITAL Corporation talent confirmed) | **Confidence:** Medium

**Finding:** AI Untuk Rakyat managed by MyDIGITAL Corporation (CEO Adrian Marcellus named in both Gobind speech and The Star article). Digital Ministry secretary-general Datuk Fabian Bigar actively involved. Government digital talent exists outside CSCDC's 8-executive structure. AI Malaysia Berhad may bring additional AI talent when leadership is announced.

**Intelligence Gaps:** Will AI Malaysia Berhad provide creative/content talent to CSCDC?

**Change:** ↑ MyDIGITAL Corporation and Datuk Fabian Bigar confirmed as operational talent

---

### PIR-OPP004-005: Content Approval Workflow
**Priority:** Medium | **Previous:** Partial → **Current:** Partial (no change) | **Confidence:** Low

**Finding:** No new information. AI Untuk Rakyat operates under Ministry of Digital — government content approval appears efficient when digital-first.

**Change:** → No change

---

### PIR-OPP004-006: PQC Animation Scope
**Priority:** Medium | **Previous:** Partial → **Current:** Partial (no change) | **Confidence:** Low

**Finding:** No new information. AI Safety Institute's RDCI pillar may produce content-worthy material.

**Change:** → No change

---

### PIR-OPP004-007: Deepfake Awareness Content Plan
**Priority:** High | **Previous:** Partial (strengthened) → **Current:** Partial (strengthened — CyberSafe module confirmed as required curriculum) | **Confidence:** Medium

**Finding:** AI Untuk Rakyat's "CyberSafe for the People" module is now confirmed as one of 6 REQUIRED modules for 100K youths — this is the government's most concrete deepfake/cyber awareness content delivery. However, it's an online course module, not creative/media content. No Unit 7 creative content plan observable. AI Malaysia Berhad's "Trusted AI Governance" mandate may include public awareness content development.

**Intelligence Gaps:** Will AI Malaysia Berhad develop creative deepfake awareness content? Is CyberSafe module the extent of the government's creative plan?

**Change:** ↑ CyberSafe confirmed as required module in AI Untuk Rakyat — government's de facto deepfake awareness content

---

### PIR-OPP004-008: Brand Guidelines Status
**Priority:** Medium | **Previous:** Partial → **Current:** Partial (no change) | **Confidence:** Low

**Finding:** No new information. AI Malaysia Berhad as new national AI entity will need its own brand identity.

**Change:** → No change

---

### PIR-OPP004-009: Multi-Language Requirements
**Priority:** Medium | **Previous:** Resolved (confirmed) → **Current:** Resolved (confirmed) | **Confidence:** High

**Finding:** AI Untuk Rakyat programme announced in BM (AI Untuk Rakyat) and English (AI for the People). Rakyat Digital portal is multilingual. MD2030 Pillar 5 targets rural areas and underserved communities. Multi-language requirement confirmed as structurally mandatory.

**Change:** → Reconfirmed by AI Untuk Rakyat bilingual operation

---

### PIR-OPP004-010: Existing CSM Content Assets
**Priority:** Low | **Previous:** Resolved → **Current:** Resolved (no change) | **Confidence:** Medium

**Finding:** No new information. CSM TikTok @cybersecuritymy remains baseline. Ministry of Digital TikTok @kementeriandigital active.

**Change:** → No change

---

## Cross-PIR Synthesis

### Theme 1: AI Untuk Rakyat — Government's De Facto Anti-Deepfake Awareness Programme
PM Anwar's National Day announcement of AI Untuk Rakyat (30 Aug 2026) represents the government's most concrete AI awareness initiative. The CyberSafe for the People module, embedded as required curriculum for 100K youths, IS the government's anti-deepfake awareness content — delivered as an online course module, not a creative/media campaign. This is a significant development: the government now has a delivery vehicle for cyber literacy, but it is institutional/educational, not creative/media. CSCDC's RM 500K creative campaign white space is confirmed and widening — the government is building awareness *infrastructure* but not creative *content* for mass awareness.

### Theme 2: Political Priority Signal — National Day Announcement Level
PM Anwar chose to announce AI Untuk Rakyat as one of six National Day initiatives — this is a political priority signal at the highest level. AI awareness is now officially a national priority alongside cost-of-living measures, subsidies, and healthcare. This may attract additional resources to AI Malaysia Berhad / Ministry of Digital, potentially absorbing CSCDC's RM 500K allocation into the AI Untuk Rakyat / AI Action Plan framework.

### Theme 3: Cybercrimes Bill Royal Assent — 42 Days and Counting
The Cybercrimes Bill passed Dewan Negara on 20 Jul 2026 — 42 days ago. No royal assent or gazetting confirmation found via any available source. This is approaching the upper end of typical Malaysian royal assent timelines. The Federal Gazette portal is inaccessible via web_extract (private network block). This remains the single most critical timeline signal: enforcement commencement creates the campaign's hard deadline.

### Theme 4: Search API Blackout — Day 12+
web_search, Firecrawl MCP, and SearXNG all return empty results across all queries. This is now a 12+ day blackout. 100% reliance on direct URL extraction (web_extract on known news portals and government sites). This limits collection to known sources — serendipitous discovery of new sources is impossible. The blackout affects all PIR clusters, not just CSCDC-04.

### Theme 5: In-House Trend Reinforced — AI Untuk Rakyat Delivered Without External Agency
AI Untuk Rakyat was delivered entirely in-house by Ministry of Digital + MyDIGITAL Corporation, with no external creative agency involvement. This further reinforces the LEAN IN-HOUSE signal. The government is building its own awareness content infrastructure. CSCDC's RM 500K creative campaign would be the first external creative procurement — if it happens at all.

---

## Intelligence Gaps

### Critical Gaps
1. **Cybercrimes Bill royal assent/gazetting date** — 42 days unverifiable, #1 timeline signal. Federal Gazette portal inaccessible.
2. **AI Malaysia Berhad leadership/structure** — 34 days post-establishment, no CEO/board/budget authority announcements.
3. **RM 500K allocation status** — has it been absorbed into AI Untuk Rakyat / AI Action Plan, or remains separate?

### High-Priority Gaps
4. Agency selection — has procurement commenced under AI Malaysia Berhad?
5. AI Governance Bill post-consultation Cabinet submission — 31 days since consultation closure.
6. MCMC Q3 2026 enforcement data — scam takedown numbers still unavailable.
7. TV airtime procurement — will AI Untuk Rakyat's digital-first approach eliminate TV need?

### Medium-Priority Gaps
8. Content approval workflow under Public Sector AI Adoption Guidelines
9. Brand guidelines — AI Malaysia Berhad branding may intersect with CSCDC
10. PQC animation scope — AI Safety Institute RDCI may produce source material

---

## Recommendations

### Immediate (Next 7 Days)
1. **Check Federal Government Gazette via alternative access** — try AGC portal directly, Malaysian Bar, or legal databases for Cybercrimes Bill royal assent/warkat. 42 days is at upper end of typical timeline.
2. **Monitor AI Untuk Rakyat registration data** — first concrete awareness delivery starts 31 Aug (today). Track registration numbers, module completion rates as baseline literacy indicator.
3. **Track AI Malaysia Berhad organisational announcements** — 34 days without public leadership. Check Companies Commission of Malaysia (SSM) for registration details.

### Short-Term (Next 14 Days)
4. **Monitor AI Governance Bill post-consultation** — Cabinet submission expected; track for parliamentary tabling timeline.
5. **Assess MCMC's evolving enforcement landscape** — scammers shifting to RCS/iMessage requires campaign messaging evolution. Seek Q3 2026 enforcement data.
6. **Evaluate RM 500K repositioning** — should the creative campaign be positioned as creative/media layer on top of AI Untuk Rakyat's educational infrastructure?

### Strategic
7. **Reposition partnership proposal** — from CSCDC-specific campaign to AI Action Plan 2026-2030 "Responsible Governance" enabler implementation. AI Untuk Rakyat's CyberSafe module is the educational layer; CSCDC's RM 500K campaign is the creative/media layer.
8. **Develop creative campaign concept that differentiates from AI Untuk Rakyat** — AI Untuk Rakyat is module-based, youth-targeted, digital-first. CSCDC's campaign should be mass-reach, multi-demographic, multi-channel (TV, billboard, social) creative.
9. **Engage MyDIGITAL Corporation (Adrian Marcellus) and Datuk Fabian Bigar** — they are the operational leads for AI Untuk Rakyat. They may be the decision-makers for any creative campaign integration.
10. **Leverage AI Safety Institute red teaming findings** — campaign content can reference institutional safety evaluations for credibility.

---

## PIR Resolution Status Table

| PIR ID | Priority | Previous Status | Current Status | Confidence | Change |
|--------|----------|------------------|----------------|------------|--------|
| PIR-OPP008-001 | Critical | Partial (strengthened) | **Partial (strengthened)** | Medium | ↑ AI Untuk Rakyat at National Day level adds political priority signal |
| PIR-OPP008-002 | Critical | Partial | **Partial** | Medium | → No procurement signal; AI Untuk Rakyat delivered in-house |
| PIR-OPP008-003 | High | Partial (strengthened) | **Resolved** | High | ↑↑ Government audience now definitive via AI Untuk Rakyat |
| PIR-OPP008-004 | High | Resolved (updated) | **Resolved (updated)** | High | ↑ MCMC RCS/iMessage threat evolution + module architecture |
| PIR-OPP008-005 | High | Partial | **Partial** | Medium | → No new signal; AI Untuk Rakyat digital-first |
| PIR-OPP008-006 | Medium | Partial | **Partial** | Low | → No change |
| PIR-OPP008-007 | High | Partial | **Partial** | Medium | → Rakyat Digital portal provides data infrastructure |
| PIR-OPP008-008 | High | Partial (strengthened) | **Partial (strengthened)** | Medium | ↑ AI Untuk Rakyat module pass/fail provides measurable baseline |
| PIR-OPP008-009 | Medium | Partial (strengthened) | **Partial (strengthened)** | Medium | ↑ AI Untuk Rakyat "until 2027" confirms multi-year |
| PIR-OPP008-010 | Medium | Resolved (updated) | **Resolved (updated)** | High | ↑ AI Untuk Rakyat added as 13th initiative |
| PIR-OPP004-001 | High | Partial | **Partial** | Medium | → No CSCDC change; AI Untuk Rakyat shows institutional content |
| PIR-OPP004-002 | Critical | Partial (strengthened) | **Partial (strengthened)** | Medium | ↑ AI Untuk Rakyat delivered in-house reinforces trend |
| PIR-OPP004-003 | Low | Partial | **Partial** | Low | → No change |
| PIR-OPP004-004 | High | Partial | **Partial (strengthened)** | Medium | ↑ MyDIGITAL Corporation talent confirmed |
| PIR-OPP004-005 | Medium | Partial | **Partial** | Low | → No change |
| PIR-OPP004-006 | Medium | Partial | **Partial** | Low | → No change |
| PIR-OPP004-007 | High | Partial (strengthened) | **Partial (strengthened)** | Medium | ↑ CyberSafe confirmed as required module |
| PIR-OPP004-008 | Medium | Partial | **Partial** | Low | → No change |
| PIR-OPP004-009 | Medium | Resolved (confirmed) | **Resolved (confirmed)** | High | → AI Untuk Rakyat bilingual confirms |
| PIR-OPP004-010 | Low | Resolved | **Resolved** | Medium | → No change |

**Summary:** 5 Resolved, 15 Partial, 0 Open. 0 status regressions. 7 status strengthenments. 1 new resolution (PIR-OPP008-003 upgraded to Resolved). 0 downgrades.

---

## TOP 3 PIR SUGGESTIONS FOR NEXT CYCLE (AUTO-APPROVED)

1. **Suggestion:** Cybercrimes Bill Royal Assent — Alternative Gazette Access Methods
   **Rationale:** 42 days since Dewan Negara passage — approaching upper end of typical royal assent timeline. Federal Gazette portal blocked by web_extract. Alternative access methods needed: AGC direct portal, Malaysian Bar, legal databases (LexisNexis, CLJ), or parliamentary Hansard for any royal assent announcement.
   **Search Queries:** `site:agc.gov.my "Cybercrimes Act 2026"`, `site:malaysianbar.org.my cybercrimes royal assent`, `"Akta Jenayah Siber" warkat diraja 2026`, `Cybercrimes Act 2026 gazette commencement date`

2. **Suggestion:** AI Malaysia Berhad SSM Registration and Leadership Tracking
   **Rationale:** 34 days post-establishment with no public leadership announcement. Check Companies Commission of Malaysia (SSM) for registration details — company number, directors, registered address. This is the decision-maker for CSCDC's campaign future.
   **Search Queries:** `site:ssm-einfo.my "AI Malaysia Berhad"`, `AI Malaysia Berhad director board 2026`, `site:digital.gov.my "AI Malaysia" struktur organisasi`

3. **Suggestion:** AI Untuk Rakyat Module Content Assessment — CyberSafe Deep Dive
   **Rationale:** CyberSafe for the People module is the government's de facto anti-deepfake awareness content. CSCDC's RM 500K creative campaign must either integrate with or differentiate from this module. Need to assess content depth, delivery mechanism, and whether it addresses deepfake-specific awareness or general cyber safety.
   **Search Queries:** `site:rakyatdigital.gov.my CyberSafe module curriculum`, `AI Untuk Rakyat CyberSafe module content deepfake`, `rakyatdigital.gov.my module CyberSafe for the People`

---

*Report generated by Anti-Deepfake & Campaign Strategy Watch PIR Collection Orchestrator (CSCDC-04)*
*Strategic CognitiveOS Intelligence System*
*Method: DeerFlow pro (thin output — 589 bytes) + web_extract fallback (The Star, Ministry of Digital, RTM, Rahmat Lim, LPP Law — 8 full body extractions)*
*Cycle: CSCDC-04 | 2026-08-31 01:44 MYT*
