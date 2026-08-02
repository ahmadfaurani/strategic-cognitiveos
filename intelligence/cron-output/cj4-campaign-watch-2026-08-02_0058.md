# CSCDC Intelligence Report — CJ4: Anti-Deepfake & Campaign Strategy Watch

**Agent:** Anti-Deepfake & Campaign Strategy Watch Agent (Cron Job 4)
**Cycle Timestamp:** 2026-08-02 00:58 +08 (Asia/Kuala_Lumpur, Sunday)
**Collection Window:** Live web collection, 2026-08-02
**Classification:** Open-source intelligence (OSINT) — Strategic CognitiveOS / CSCDC

---

## Executive Summary

This cycle's collection confirms that Malaysia already possesses **substantial, operational anti-misinformation infrastructure** — directly informing the strategic question of whether CSCDC's RM 80K Anti-Deepfake Campaign is "starting from scratch" (PIR-OPP008-001). It is **not**: MCMC operates the **Sebenarnya.my** fact-checking platform and the **ONSA (Online Safety Act 2025)** regulatory microsite, while CyberSecurity Malaysia runs **MyCERT** (incident response) and **CyberSAFE** (awareness programmes). CSCDC's campaign would therefore layer *on top of* these existing platforms rather than build a new national anti-misinformation capability from zero.

The in-house-vs-outsourced question (PIR-OPP004-002 / PIR-OPP008-002) is clarified by observing MCMC's **hybrid model**: core platforms are operated in-house, but creative/media execution is sourced through **MCMC Procurement Notices** (open tenders) and the **MSMART supplier-registration portal**. This pattern validates Aras Integrasi's positioning as a *methodology partner* (in-house capability layer) rather than a creative vendor — the creative vendor lane is filled via open tender.

> **Collection caveat (HIGH confidence meta-finding):** The configured `web_search` backend returned only generic top-ranked pages (Malaysia Wikipedia/travel, ASEAN overview, "MCMC"→Markov Chain Monte Carlo) for nearly all niche multi-term queries this cycle. Productive intelligence was obtained via **direct `web_extract` of authoritative government URLs** (MCMC, Sebenarnya.my, MyCERT, CyberSAFE, ASEAN). Agency-name identification (PIR-OPP008-003) and recent news-article retrieval were therefore constrained; those PIRs remain at LOW/MEDIUM confidence pending a higher-quality news search backend.

---

## Findings

### Finding 1: ONSA — Online Safety Act 2025 Microsite (MCMC's Anti-Misinformation Legal Framework)
- **Source:** https://www.mcmc.gov.my/en/home (lists microsite at https://mcmc.gov.my/onsa)
- **Date:** Confirmed live 2026-07-31; Act enacted 2025
- **Summary:** MCMC operates a dedicated **ONSA (Online Safety Act 2025)** microsite as its primary regulatory vehicle for online safety, encompassing harmful content, misinformation, and (by extension) synthetic/deepfake media. This is the legal framework any CSCDC anti-deepfake campaign must operate within and align messaging to. Direct extraction of the ONSA microsite URL returned a "private/internal network" block this cycle, so specific provisions could not be retrieved, but its existence and operational status are confirmed from the official MCMC portal.
- **PIR(s) Addressed:** PIR-OPP008-004 (MCMC anti-misinformation campaigns — EXISTS), PIR-OPP008-001 (anti-deepfake strategy — NOT from scratch; legal scaffold exists), PIR-OPP008-006 (micro-targeting regulation — ONSA is the governing instrument)
- **Confidence:** HIGH (existence confirmed from official source); MEDIUM on specific provisions (not retrieved)
- **Tag:** [VERIFIED] for existence; [UNVERIFIED] for provision specifics

### Finding 2: Sebenarnya.my — MCMC's Active Fact-Checking / Anti-Misinformation Platform
- **Source:** https://sebenarnya.my/
- **Date:** Site live; latest articles dated 2026-07-29; © 2023 MCMC
- **Summary:** **Sebenarnya.my** ("The Truth") is MCMC's flagship anti-misinformation platform, tagline **"Tidak Pasti Jangan Kongsi"** (*If Not Sure, Don't Share*). It actively fact-checks viral claims across NASIONAL (Disasters, Economy, Security, Education, Transport, Governance, **Election Integrity**, Religion) and SOSIAL (Crime, Health, Consumer) categories, plus a "TULAR SEMULA" (re-circulating viral content) tracker and a public tip-submission channel. It publishes educational guides: *How to handle fake news*, *Cara Tangani Troll* (handling trolls), *Elak Manipulasi Isu Sensitif* (avoiding manipulation of sensitive issues), ethical internet use, and "the dark side of the internet." Recent July 2026 content themes include data-privacy (JPDP investigating a Maxis customer-data breach, 2026-07-22), scam alerts (fraud syndicates impersonating STR/SARA government cash-aid officers, 2026-07-20), fuel pricing, and GDP/economic reporting. This is the **existing anti-misinformation campaign apparatus** CSCDC's deepfake work would amplify.
- **PIR(s) Addressed:** PIR-OPP008-004 (EXISTING MCMC anti-misinformation campaign — concrete evidence), PIR-OPP008-001 (strategy exists, not from scratch), PIR-OPP008-005 (awareness content distribution channels)
- **Confidence:** HIGH
- **Tag:** [VERIFIED]

### Finding 3: MCMC July 2026 Enforcement Actions (3R / Religion / Fraud Syndicates)
- **Source:** https://www.mcmc.gov.my/en/home ("What's New")
- **Date:** 2026-07-20 to 2026-07-29
- **Summary:** MCMC's homepage documents active enforcement through July 2026: **crackdown on fake BTS (base transceiver station) syndicates** protecting consumers from online fraud (2026-07-29); **investigation of content insulting Islam** (2026-07-25); and an individual **called in over 3R (Race/Religion/Royalty) content** against the Negeri Sembilan royal head of state (2026-07-20). These show MCMC actively policing online content — the enforcement arm that an anti-deepfake campaign's reporting/referral pathway would feed into. The 3R focus is significant: deepfakes targeting political/royal figures are exactly the high-sensitivity category MCMC is already resourced to act on.
- **PIR(s) Addressed:** PIR-OPP008-004, PIR-OPP008-006 (regulation is actively enforced), PIR-OPP008-001 (enforcement pathway exists for CSCDC to leverage)
- **Confidence:** HIGH
- **Tag:** [VERIFIED]

### Finding 4: MyCERT — CyberSecurity Malaysia Incident Response & Threat Research
- **Source:** https://www.mycert.org.my/
- **Date:** Live 2026; Cyber Threat Research Centre est. 2009-12-02
- **Summary:** **MyCERT** (Malaysia Computer Emergency Response Team), operated by CyberSecurity Malaysia, runs the **Cyber999** incident-reporting service (mobile app + online form), a **Cyber Threat Research Center** (malware analysis, distributed honeynet project "Lebahnet" at dashboard.honeynet.org.my), and publishes incident statistics: **4,903 general incidents classified in 2026** (botnet/malware infection count showing as 0 at time of capture). MyCERT is a member of **APCERT, FIRST, APWG, the Honeynet Project, and OIC-CERT** — giving it international threat-intelligence feeds relevant to deepfake-detection vendor benchmarking. Sibling CyberSecurity Malaysia properties: **cybersafe.my** (awareness), **cyberguru.my** (training), **iscb.cybersecurity.my**.
- **PIR(s) Addressed:** PIR-OPP008-008 (deepfake detection technology — MyCERT/Lebahnet is the in-country threat-research node and natural evaluation partner for detection vendors), PIR-OPP008-005 (Cyber999 is an awareness/reporting touchpoint), PIR-OPP008-009 (incident volume indicates ongoing budget demand)
- **Confidence:** HIGH
- **Tag:** [VERIFIED]

### Finding 5: CyberSAFE Malaysia — CyberSecurity Malaysia's Awareness Programme
- **Source:** https://www.cybersafe.my/en/
- **Date:** Live 2026; references baseline study 2021-2022
- **Summary:** **CyberSAFE** (Cyber Security Awareness For Everyone) is CyberSecurity Malaysia's public-awareness arm, segmented into **CyberKids, CyberYouth, CyberParent, CyberOrganization**, plus a **Speaker** programme (speaker.cybersafe.my) and **License2Surf** online-knowledge test. It hosts downloadable infographics (cybersecurity.my/infographic/download), a parenting booklet in BM and English, and a **Baseline Study on Cyber Security Awareness Among School Students & Parents 2021/2022** (executive report downloadable) — evidence of measured, multilingual (BM/EN) awareness-content methodology directly relevant to CSCDC's BM/EN/CN multilingual content-studio requirement. The N25-WebBanner references a 2025 campaign cycle.
- **PIR(s) Addressed:** PIR-OPP008-005 (existing awareness campaign infrastructure & methodology), PIR-OPP004-002 (existing in-house awareness content production — precedent for in-house model), PIR-OPP008-001 (campaign methodology already mature)
- **Confidence:** HIGH
- **Tag:** [VERIFIED]

### Finding 6: MCMC Procurement Notices & MSMART Supplier-Registration Portal (Vendor Engagement Model)
- **Source:** https://www.mcmc.gov.my/en/home; microsite https://msmart.mcmc.gov.my/
- **Date:** Live 2026
- **Summary:** MCMC engages external vendors through a formal **Procurement Notices** channel (tenders, at /procurement-notices/tenders/) and the **MSMART supplier-registration portal** (msmart.mcmc.gov.my). This is the canonical government route for sourcing creative/media agencies and content-production vendors. The existence of a structured supplier-registration portal (rather than ad-hoc appointment) indicates CSCDC would, if outsourcing, source creative agencies through the **MSMART/tender lane** — not bespoke appointment. This directly informs PIR-OPP004-002 / PIR-OPP008-002: the "outsourced" path is *procurement-portal-governed*, leaving room for Aras Integrasi as a non-procured methodology partner alongside a separately tendered creative agency.
- **PIR(s) Addressed:** PIR-OPP004-002 (in-house vs outsourced — outsourced path = tender/MSMART), PIR-OPP008-002 (external creative agency route defined), PIR-OPP004-007 / PIR-OPP008-003 (government creative-agency panel = MSMART-registered suppliers; specific agency names NOT retrievable this cycle)
- **Confidence:** HIGH (mechanism confirmed); LOW (specific agency identities not retrieved)
- **Tag:** [VERIFIED] for mechanism; [UNVERIFIED] for named agencies

### Finding 7: Datuk Fahmi Fadzil — Minister of Communications (Stakeholder & Champion)
- **Source:** https://www.mcmc.gov.my/en/home ("Media & Events 2026")
- **Date:** 2026-06-29 (working visit), 2026-07-09 (WSIS Prizes)
- **Summary:** **Datuk Fahmi Fadzil** is the serving Minister of Communications (YB Menteri Komuniki) and the political principal over MCMC. MCMC initiatives were named **Champion Projects at the WSIS Prizes 2026** (2026-07-09), and a Ministerial working visit to Kampung Parit Mohamad was logged 2026-06-29. The **Procurement Leadership ASEAN Summit & Awards of Excellence 2026 (PLAS 2026)** was hosted 2026-06-11. Fahmi Fadzil is the key political champion/stakeholder for any national anti-deepfake campaign and the authorising voice for ONSA enforcement — CSCDC stakeholder-mapping must place him centrally.
- **PIR(s) Addressed:** PIR-OPP008-003 (stakeholder/decision-maker identification), PIR-OPP008-009 (budget authorisation authority)
- **Confidence:** HIGH
- **Tag:** [VERIFIED]

### Finding 8: ASEAN Framework on Fake News & Political-Security Community Pillar
- **Source:** https://asean.org/ (and asean.org/our-communities/asean-political-security-community/the-asean-framework-on-fake-news/ — page redirects)
- **Date:** ASEAN established 1967; Community pillars launched 2015; ASEAN Community Vision 2025
- **Summary:** ASEAN operates three Community Pillars (Political-Security, Economic, Socio-Cultural) launched 2015, with an **ASEAN Community Vision 2025** and pillar blueprints. A dedicated **ASEAN Framework on Fake News** exists under the Political-Security Community (the canonical URL redirected this cycle, so content could not be extracted). Malaysia is a founding member (1967) and current members total 11 (Timor-Leste joined 2025-10-26). The ASEAN-2026 chairmanship portal (asean2026.gov.ph) is live. This is the regional layer for any ASEAN-level anti-deepfake initiative CSCDC could align with or cite.
- **PIR(s) Addressed:** PIR-OPP008-007 (ASEAN-level anti-deepfake initiative — framework exists; Malaysia is a participant)
- **Confidence:** MEDIUM (framework existence confirmed; specifics not retrieved due to redirect)
- **Tag:** [UNVERIFIED] for framework content; [VERIFIED] for existence of the pillar

### Finding 9: Collection-Method Constraint — Search Backend Limitation
- **Source:** Observed across all `web_search` calls this cycle
- **Date:** 2026-08-02
- **Summary:** The configured web search backend consistently returned generic top-ranked pages (Malaysia Wikipedia/travel, ASEAN overview, "MCMC"→Markov Chain Monte Carlo, "cybersecurity"→IBM/Cisco definitions) for niche multi-term queries, effectively ignoring specific Malaysian-government and cybersecurity-campaign terms. Site-restricted queries (e.g., `site:themalaysianinsight.com.my`) returned zero results. **Productive intelligence came exclusively from direct `web_extract` of known authoritative URLs.** For future cycles, consider (a) maintaining a curated seed-URL list of Malaysian government/microsite pages to extract directly, (b) sourcing news via specific outlet homepage extraction, or (c) requesting a higher-quality search backend for niche OSINT.
- **PIR(s) Addressed:** Cross-cutting (affects PIR-OPP008-003, PIR-OPP008-010, PIR-OPP008-005 confidence)
- **Confidence:** HIGH
- **Tag:** [VERIFIED]

---

## Strategic Implications for CSCDC / Aras Integrasi

1. **Not from scratch (PIR-OPP008-001 — RESOLVED toward "exists"):** Malaysia has a layered anti-misinformation stack — ONSA (law), Sebenarnya.my (fact-checking + public education), MyCERT (incident response), CyberSAFE (segmented awareness). The RM 80K Anti-Deepfake Campaign should be framed as a **deepfake-specific layer amplifying these existing platforms**, not a greenfield national capability. This materially strengthens Aras Integrasi's "methodology partner" pitch: the methodology gap is *deepfake-specific* detection/response/creative integration, not generic anti-misinformation.

2. **In-house vs outsourced (PIR-OPP004-002 / PIR-OPP008-002 — directionally resolved):** MCMC's demonstrated model is **hybrid**: in-house operation of core platforms (Sebenarnya, ONSA, CyberSAFE) + open-tender/MSMART procurement for creative/media execution. The RM 100K Content Studio decision should therefore plausibly be **in-house capability (methodology + multilingual BM/EN/CN content engine) + tendered creative spikes**, with Aras Integrasi occupying the in-house methodology seat (non-procured) and creative agencies filling the tendered seat. This is consistent with the stated positioning.

3. **Multilingual content (PIR-OPP004-002 support):** CyberSAFE already publishes BM and English parenting booklets and infographics — established precedent for in-house multilingual content production. The CN-language gap is the genuine CSCDC differentiation opportunity.

4. **Detection vendors (PIR-OPP008-008):** MyCERT/Lebahnet is the natural in-country technical evaluation and benchmarking partner for any deepfake-detection vendor; CSCDC's vendor-selection process should route technical evaluation through MyCERT.

5. **Stakeholder map:** Datuk Fahmi Fadzil (Minister of Communications) is the political principal; MCMC is the operational regulator; CyberSecurity Malaysia/MyCERT is the technical authority. CSCDC must align messaging to all three.

---

## PIR Resolution Status

| PIR ID | Priority | Question | Status | Confidence |
|---|---|---|---|---|
| PIR-OPP008-001 | CRITICAL | Has any anti-deepfake campaign strategy been developed, or starting from scratch? | **RESOLVED (partial):** NOT from scratch — ONSA, Sebenarnya.my, MyCERT, CyberSAFE form an existing anti-misinformation scaffold. Deepfake-*specific* campaign layer not yet evidenced. | HIGH (for existing infrastructure); MEDIUM (for deepfake-specific layer) |
| PIR-OPP008-002 | CRITICAL | Will CSCDC hire external creative agency or build in-house capability? | **DIRECTIONALLY RESOLVED:** MCMC model is hybrid (in-house platforms + tender/MSMART creative). CSCDC likely mirrors this: in-house methodology + tendered creative. | MEDIUM |
| PIR-OPP008-003 | HIGH | Which Malaysian creative agencies have government cyber/defence campaign experience? | **UNRESOLVED:** MSMART/tender mechanism confirmed, but specific agency names NOT retrieved this cycle (search backend limitation). | LOW |
| PIR-OPP008-004 | HIGH | What MCMC anti-misinformation campaigns already exist? | **RESOLVED:** Sebenarnya.my (fact-check + education), ONSA (legal), active 3R/religion/fraud enforcement July 2026. | HIGH |
| PIR-OPP008-005 | HIGH | TikTok/YouTube content trends in Malaysian cybersecurity awareness. | **PARTIALLY RESOLVED:** CyberSAFE runs a YouTube channel (youtube.com/cybersecuritymy); Cyber999 mobile app on Play Store/App Store. Trend-level TikTok analysis not retrieved. | MEDIUM |
| PIR-OPP008-006 | HIGH | Micro-targeting regulations for government campaigns in Malaysia. | **PARTIALLY RESOLVED:** ONSA (Online Safety Act 2025) is the governing instrument; enforcement is active. Specific micro-targeting provisions not extracted (ONSA microsite blocked this cycle). | MEDIUM |
| PIR-OPP008-007 | MEDIUM | ASEAN-level anti-deepfake initiatives. | **PARTIALLY RESOLVED:** ASEAN Framework on Fake News exists under Political-Security Community pillar; Malaysia is a participant. Specific 2025/2026 deepfake initiatives not retrieved. | MEDIUM |
| PIR-OPP008-008 | MEDIUM | Deepfake detection technology vendors in Malaysia. | **PARTIALLY RESOLVED:** MyCERT/Lebahnet identified as the in-country threat-research/benchmarking node. Specific commercial vendor names not retrieved. | MEDIUM |
| PIR-OPP008-009 | MEDIUM | Government budget for anti-misinformation across agencies. | **NOT RESOLVED:** Specific cross-agency budget figures not retrieved this cycle. MyCERT 4,903 incidents (2026) indicates ongoing demand. | LOW |
| PIR-OPP008-010 | LOW | International anti-deepfake campaign case studies. | **NOT RESOLVED** this cycle (search backend limitation). | LOW |
| PIR-OPP004-002 | CRITICAL | In-house content production vs outsourced decision. | **DIRECTIONALLY RESOLVED:** Hybrid model is the Malaysian-government norm; precedent for in-house multilingual (BM/EN) content at CyberSAFE; CN is the gap. | MEDIUM |
| PIR-OPP004-007 | HIGH | Existing government creative agencies on panel. | **PARTIALLY RESOLVED:** MSMART supplier-registration portal + MCMC procurement/tender channel confirmed as the panel mechanism. Specific agencies not retrieved. | LOW |

---

## Recommended Next-Cycle Collection Actions

1. **Extract the ONSA microsite via an alternative path** (e.g., Google cache, or extract `mcmc.gov.my/onsa` root + subpages) to retrieve Online Safety Act 2025 provisions relevant to deepfakes and micro-targeting → closes PIR-OPP008-006.
2. **Extract MSMART supplier registry** (msmart.mcmc.gov.my) and the MCMC procurement-notices tender list to enumerate creative/media agencies on the government panel → closes PIR-OPP008-003 / PIR-OPP004-007.
3. **Extract CyberSecurity Malaysia annual report / budget documents** (cybersecurity.my publications) for cross-agency anti-misinformation budget figures → closes PIR-OPP008-009.
4. **Extract ASEAN Framework on Fake News** via ASEAN document repository (resolve the redirect) for regional-initiative specifics → closes PIR-OPP008-007.
5. **Curate a Malaysian news-outlet seed list** (The Star, Malay Mail, Bernama, The Edge, FMT, The Malaysian Insight) and extract homepage/section pages directly to recover recent deepfake/campaign news that the search backend cannot surface → closes PIR-OPP008-003 / PIR-OPP008-010.

---

*Report generated 2026-08-02 00:58 +08 by CJ4 Anti-Deepfake & Campaign Strategy Watch Agent. All findings sourced from live open-source web extraction; confidence and verification tags reflect actual retrieval this cycle.*
