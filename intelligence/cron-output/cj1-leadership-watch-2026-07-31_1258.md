# CSCDC Leadership & Approval Watch — Intelligence Report

**Job:** cj1-leadership-watch (CSCDC Leadership & Approval Watch Agent)
**Collection Cycle:** Friday, 31 July 2026
**Timestamp (Asia/Kuala_Lumpur, UTC+8):** 2026-07-31 12:58 +08
**Analyst:** Strategic CognitiveOS — Cron Agent (GLM-5.2)
**Classification:** OSINT — For internal strategic planning only
**Mission:** Resolve Critical PIRs related to CSCDC leadership mapping, decision authority, framework approval status, and competitive landscape.

---

## Executive Summary

This cycle (31 Jul 12:58, ~6 hours after the 06:52 baseline) produced **one new primary-source corroboration** and **two status confirmations**. The principal new value: a **primary-source NACSA directive (Arahan Ketua Eksekutif NACSA No. 9, effective 22 Sep 2025)** signed by **Ir. Dr. Megat Zuhairy Bin Megat Tajuddin** in his own hand as Ketua Eksekutif NACSA — the strongest possible confirmation of his incumbency and regulatory authority, superseding the prior cycle's third-party CyberDSA corroboration. The same document (i) establishes PTPKM as the formal coordinator under NACSA supervision for Post-Quantum Cryptography (PQC) migration — a concrete operational-integration data point for the PTPKM↔CSM relationship, and (ii) lays out the full legal timeline of Akta 854 (Cybersecurity Act 2024), which underpins NACSA's directive power over NCII entities and PTPKM. **cscdc.my was re-verified as STILL PARKED** (Hostinger CDN/hcdn, title "Parked Domain name on Hostinger DNS system") — the earlier HTTP/200 was the parked-template response, not a go-live; no change from the prior baseline. The two CSM active tenders (SH/06/2026 endpoint hardware, SH/07/2026 IT & OT Lab Software) had their document-sale window end **today (31 Jul 2026)**; bids still close **3 Aug 2026 @ 12:00**. Framework v2.0 approval date, 90-day mobilisation clock, CCO appointment, and CSCDC-specific operational CEO remain non-public — no change from the 06:52 baseline.

---

## New Findings This Cycle

### Finding 1: NACSA Arahan No. 9 — primary-source confirmation of NACSA Chief Executive Megat Zuhairy + legal authority basis (NEW primary source)
- **Source:** https://www.nacsa.gov.my/doc/Arahan%20KE%20NACSA%20No.%209.pdf
- **Date:** Effective 22 September 2025 (directive signed by NACSA Chief Executive)
- **Summary:** NACSA's official directive "Arahan Ketua Eksekutif NACSA No. 9" on PQC migration data collection is signed by **IR. DR. MEGAT ZUHAIRY BIN MEGAT TAJUDDIN, Ketua Eksekutif NACSA**, under the legal authority of Seksyen 13, Akta Keselamatan Siber 2024 [Akta 854]. This is a self-signed primary-source confirmation of his incumbency — stronger than the prior cycle's CyberDSA support-message corroboration. The directive's full title and legal basis confirm NACSA's Chief Executive has statutory power to issue binding directives to NCII Sector Heads, NCII entities, government entities, and PTPKM. This consolidates the regulatory-shepherd identification in PIR-CSCDC-001 at the highest verification tier.
- **PIR(s) Addressed:** PIR-CSCDC-001 (CRITICAL), PIR-INIT-CSCDC-002 (CRITICAL)
- **Confidence:** HIGH (primary-source government directive, self-signed by the officeholder)
- **Tag:** [VERIFIED]

### Finding 2: PTPKM formally designated NACSA's PQC-migration coordinator — operational-integration data point
- **Source:** https://www.nacsa.gov.my/doc/Arahan%20KE%20NACSA%20No.%209.pdf (Section 1.4)
- **Date:** Effective 22 September 2025
- **Summary:** Arahan No. 9 §1.4 explicitly establishes **Pusat Teknologi dan Pengurusan Kriptologi Malaysia (PTPKM)** as the coordinator under NACSA supervision to collect PQC-migration data for strategic analysis and reporting. The directive's applicability (§4) names PTPKM, all NCII Sector Heads, and all NCII entities. This documents a concrete operational subordination: PTPKM acts as NACSA's operational coordinator for PQC migration — the first OSINT evidence of a defined PTPKM↔NACSA working relationship within the CSCDC consolidation. It supports the inference that, post-merger, PTPKM's coordination functions will flow through NACSA's regulatory umbrella inside CSCDC, rather than operating autonomously. Relevant to resolving granular operational-integration status (currently rated non-public at the staff/systems level).
- **PIR(s) Addressed:** PIR-OPP010-001 (HIGH), PIR-CSCDC-001 (CRITICAL)
- **Confidence:** HIGH (primary-source directive)
- **Tag:** [VERIFIED]

### Finding 3: Akta 854 (Cybersecurity Act 2024) full legal timeline mapped — regulatory context for CSCDC approval chain
- **Source:** https://www.nacsa.gov.my/doc/Arahan%20KE%20NACSA%20No.%209.pdf (Section 2)
- **Date:** Directive references Act timeline (Apr–Aug 2024); directive effective 22 Sep 2025
- **Summary:** The directive lays out the complete legislative timeline of the Cybersecurity Act 2024 [Akta 854]: passed by Parliament **3 Apr 2024**, royal assent by Yang di-Pertuan Agong Sultan Ibrahim **18 Jun 2024**, gazetted **26 Jun 2024**, effective date set by PM **26 Aug 2024**. Four subsidiary regulations (P.U.(A) 219–222/2024) cover risk-assessment/audit periods, incident notification, cybersecurity-service-provider licensing, and compounding of offences — all effective 26 Aug 2024. Perenggan 10(1)(f) gives the NACSA Chief Executive statutory power to issue directives; Subperenggan 14(1)(a)(A)–(B) gives power to collect information from any person. This is the legal foundation underpinning the CSCDC/NACSA approval chain and NACSA CEO Megat Zuhairy's authority to shepherd the framework.
- **PIR(s) Addressed:** PIR-CSCDC-001 (CRITICAL), PIR-INIT-CSCDC-001 (CRITICAL)
- **Confidence:** HIGH (primary-source legal text)
- **Tag:** [VERIFIED]

### Finding 4: cscdc.my re-verified STILL PARKED on Hostinger CDN — no go-live
- **Source:** https://cscdc.my/ (direct HTTP inspection + content extraction, 31 Jul 12:58 +08)
- **Date:** 31 July 2026
- **Summary:** Direct fetch of cscdc.my returns HTTP/2 200 but the page title is **"Parked Domain name on Hostinger DNS system"** and the body is Hostinger's standard parked-domain marketing template (web hosting / Horizons AI / VPS / business-email upsells). The server header is `hcdn` (Hostinger CDN), resolving to 2.57.91.91. The `<meta name="robots" content="noindex,nofollow">` confirms it is not a live institutional site. This corrects any misreading of the 200 status: cscdc.my remains a **non-operational parked domain** as of 31 Jul 12:58. No external-engagement function (career portal, contact, procurement) is routable via the CSCDC domain. Watch trigger unchanged: transition from parked-template to a live institutional site is the leading indicator that external-engagement / CCO functions are going live.
- **PIR(s) Addressed:** PIR-CSCDC-004 (HIGH), PIR-CSCDC-010 (HIGH)
- **Confidence:** HIGH (direct inspection)
- **Tag:** [VERIFIED]

### Finding 5: CSM active tenders — document-sale window closes TODAY (31 Jul); bids close 3 Aug 2026; full awarded-vendor list re-confirmed
- **Source:** https://www.cybersecurity.my/portal-main/procurement
- **Date:** 31 July 2026 (portal state as of this cycle)
- **Summary:** The two CSM active quotations remain open: **SH/06/2026** (Provision of Endpoint Computing Hardware & Software) and **SH/07/2026** (Provision of IT & Operational Technology (OT) Lab Software). Both had document-sale periods of **23–31 July 2026** (the sale window ends today); both close **03 August 2026 @ 12:00 pm**. Bids are submitted to the CSM tender box; eligibility requires MoF registration (codes 210101/210102/210103 for SH/06; 210103 for SH/07) and Authorized-Reseller status. SH/07/2026 (IT & OT Lab Software) is directly relevant to PTPKM↔CSM technical-capability buildout. The full 2025 awarded-vendor list was re-confirmed and now fully enumerated, including: **HCL** (Domino, SH/01), **Microsoft** (M365, SH/02/10), **Sangfor** (NGFW, SH/06), **USM Anywhere/SIEM** (SH/05), **Dell** (PowerEdge SH/17, warranty SH/20), **Elastic** (X-Pack SH/18), **DPTech**, plus a **Security Operator Services** award (SH/24/2025, Menara Cyber Axis Cyberjaya) and a **BCMS/ISO 22301 consultancy** award (SH/12/2025). This is the most complete public competitive-landscape snapshot available. Next cycle (after 3 Aug) should check for award outcomes on SH/06 and SH/07.
- **PIR(s) Addressed:** PIR-INIT-CSCDC-010 (HIGH), PIR-CSCDC-010 (HIGH), PIR-OPP010-001 (HIGH)
- **Confidence:** HIGH (official procurement portal)
- **Tag:** [VERIFIED]

---

## Previously Established Baseline (re-verified this cycle — unchanged)

The following findings remain valid and were re-confirmed via fresh extraction this cycle:
- **KSN Tan Sri Shamsul Azri Abu Bakar** — CSCDC Board Chairman (re-verified via Berita Harian/Bernama, KLSE Screener/The Edge, Media Perpaduan, Harapan Madani, UPM Science Park; 4 Jun 2026). Note: Malay Mail (23 Jul 2026) confirms Shamsul Azri remains active KSN intervening on operational governance matters (UMMC complaints) — incumbency intact.
- **Dr Megat Zuhairy Megat Tajudin** — NACSA Chief Executive / regulatory shepherd (UPGRADED this cycle to primary-source verification via Arahan No. 9; previously corroborated via CyberDSA 2026 support message).
- **Dato' Raja Nushirwan bin Zainal Abidin** — MKN Director General (Ketua Pengarah Keselamatan Negara), MKN-side shepherd (VERIFIED prior cycle via JPM/BIUPA register updated 02 Mar 2026 + NCSS 2026 opening speech 07 Jul 2026; not re-verified this cycle but <24h old).
- **Roshdi Ahmad** — CSM Acting CEO (VERIFIED prior cycle via thesun.my/Bernama 14 Jan 2026; ex-COO since Nov 2021, joined CSM 2007; not re-verified this cycle).
- **Datuk Dr Amirudin Abdul Wahab** — former CSM CEO, retired 13 Jan 2026 after 13 years (prior cycle).
- **CSCDC governance structure** — JPM placement, NACSA regulator + MKN technical/operational arm, Cabinet-approved (re-verified via The Vibes, Malay Mail, VOM24; JKSN Bil. 1/2026, 12/13 Feb 2026).
- **Cybercrimes Bill 2026** — passed Dewan Negara 20 Jul 2026 (prior cycle; not re-verified this cycle).
- **NCSS 2026** — held 7–9 Jul 2026, MKN DG opened, CSCDC cited as flagship, 100 exhibitors (prior cycle).
- **NCSS 2026 vendors (prior cycle):** Alpine Integrated Solution Sdn Bhd (AIS) = NCSS co-organiser; Micro Concept Tech Sdn Bhd = MYSH gamification programme.
- **Other prior items (not re-verified this cycle):** PTPKM expert Dr Solahuddin Shamsuddin; CSM CTO Wan Roshaimi Wan Abdullah.

---

## PIR Resolution Status

| PIR ID | Priority | Subject | New Intel This Cycle? | Status |
|---|---|---|---|---|
| PIR-CSCDC-001 | CRITICAL | CSCDC CEO, acting CCO, MKN/NACSA shepherds | **YES — STRENGTHENED (primary source)** | NACSA CEO Megat Zuhairy now confirmed via self-signed primary directive (Arahan No. 9, 22 Sep 2025) — highest verification tier. Board Chairman = KSN Shamsul Azri (VERIFIED). MKN DG = Raja Nushirwan (VERIFIED prior cycle). CSM operational head = Acting CEO Roshdi Ahmad (VERIFIED). Approval chain fully mapped at oversight level: **KSN Shamsul Azri → MKN DG Raja Nushirwan → NACSA CEO Megat Zuhairy**. **A CSCDC-specific operational CEO and any "acting CCO" remain NOT publicly identified** — last open items. |
| PIR-CSCDC-002 | CRITICAL | Framework v2.0 formal approval + 90-day mobilisation clock start | **NO** | No public disclosure of framework v2.0 approval date or 90-day clock. Framework v2.0 (final draft 10 Jul 2026) remains non-public. No new JKSN meeting announced since Bil. 1/2026 (Feb). Closest legal milestone: Cybercrimes Bill passed Dewan Negara 20 Jul 2026 (prior cycle). Establishment window remains 3–4 Jun 2026 (90 days ≈ early Sep 2026, inference). |
| PIR-INIT-CSCDC-001 | CRITICAL | Who can approve external partnerships during mobilisation | **NO (context added)** | Partnership-approval authority per se remains unconfirmed publicly. New context: Arahan No. 9 confirms NACSA CEO Megat Zuhairy holds statutory directive power (§10(1)(f) Akta 854) over PTPKM and NCII entities — implying regulatory-level sign-off authority flows through NACSA. Operational sign-off likely via Acting CSM CEO Roshdi Ahmad; apex via CSCDC Board (KSN chair). Requires direct confirmation. |
| PIR-INIT-CSCDC-002 | CRITICAL | Most credible introduction path (CSM / NACSA / JPM) | **NO CHANGE** | All three paths confirmed with named incumbents (prior cycle + this cycle's primary-source upgrade). Assessment unchanged: **NACSA path (Megat Zuhairy / NACSA event + procurement ecosystem) = most credible working-level entry**; **MKN path (Raja Nushirwan) = most credible policy-level shepherd** (publicly owns CSCDC narrative at NCSS 2026). JPM/KSN path = apex governance. |
| PIR-INIT-CSCDC-003 | CRITICAL | Weekly milestones in the 90-day mobilisation plan | **NO** | No public information. The 90-day plan is non-public/internal. Only inferred anchor: establishment window 3–4 Jun 2026 → 90 days ≈ early Sep 2026. Recommend HUMINT/internal-source acquisition. |
| PIR-CSCDC-004 | HIGH | CCO appointment status (advertised/shortlisted/filled) | **NO** | No public "CCO" vacancy, shortlist, or appointment located for CSCDC. cscdc.my re-confirmed STILL PARKED (Hostinger CDN) as of 31 Jul 12:58 — comms function not externally routable. |
| PIR-CSCDC-010 | HIGH | Existing PR agencies/consultants/vendors at CSCDC/PTPKM/CSM | **YES — EXPANDED** | No PR-agency vendor confirmed. Full CSM 2025 awarded list now enumerated (Finding 5): named vendors HCL, Microsoft, Sangfor, USM Anywhere/SIEM, Dell, Elastic, DPTech; plus Security Operator Services (SH/24/2025) and BCMS/ISO 22301 consultancy (SH/12/2025). NACSA ecosystem vendors (prior cycle): AIS (event co-organiser), Micro Concept Tech (MYSH). No named PR/comms incumbent. |
| PIR-INIT-CSCDC-010 | HIGH | Competitive landscape — vendors currently engaged | **YES — EXPANDED** | Full CSM awarded-vendor list enumerated (Finding 5). Two CSM tenders close 3 Aug 2026 (SH/06 hardware, SH/07 IT & OT Lab Software — doc-sale ends today). NACSA-engaged vendors: AIS, Micro Concept Tech. No CSCDC-specific procurement published. NCSS 2026's 100-exhibitor scale = crowded competitive field. |
| PIR-OPP010-001 | HIGH | Operational integration status PTPKM ↔ CSM | **YES — PARTIAL** | Structural integration confirmed (Cabinet-approved merger into CSCDC under JPM, NACSA+MKN oversight). **NEW this cycle:** Arahan No. 9 §1.4 documents a concrete operational subordination — PTPKM acts as NACSA's coordinator for PQC-migration data collection under NACSA supervision (effective 22 Sep 2025). This is the first OSINT evidence of a defined PTPKM↔NACSA working relationship within the consolidation. Granular integration (staff, systems, colocation) remains non-public. SH/07/2026 (IT & OT Lab Software, closes 3 Aug) may signal technical-capability buildout. |

---

## Analytical Notes & Recommendations

1. **NACSA shepherd now confirmed at primary-source tier.** Arahan No. 9 is signed by Megat Zuhairy himself as Ketua Eksekutif NACSA, under explicit statutory authority (§10(1)(f) Akta 854). This is the strongest available OSINT verification and supersedes the prior cycle's third-party corroboration. The approval chain (KSN → MKN DG Raja Nushirwan → NACSA CEO Megat Zuhairy) is now fully mapped and verified at the apex/oversight level. The remaining open items in PIR-CSCDC-001 — a CSCDC operational CEO and an "acting CCO" — have not surfaced in any open source across multiple cycles; these likely require a human/relationship channel or the cscdc.my site going live.

2. **First OSINT evidence of PTPKM↔NACSA operational subordination.** Arahan No. 9 §1.4 naming PTPKM as NACSA's PQC-migration coordinator (under NACSA supervision) is a concrete, dated (22 Sep 2025) operational-relationship data point. It supports the inference that post-merger PTPKM coordination functions flow through NACSA's regulatory umbrella inside CSCDC. This partially advances PIR-OPP010-001 (operational integration), though staff/systems/colocation-level integration remains non-public.

3. **cscdc.my go-live remains the leading external indicator.** Despite returning HTTP/2 200, the domain is still a Hostinger parked page (verified by title + template content + noindex meta). Transition to a live institutional site remains the watch trigger for CCO/external-engagement functions going live. No change this cycle.

4. **Time-sensitive: CSM tenders close 3 August 2026 @ 12:00.** SH/06/2026 (endpoint hardware) and SH/07/2026 (IT & OT Lab Software) — document-sale window ended today (31 Jul). SH/07/2026 may be directly relevant to PTPKM↔CSM technical integration. Next cycle after 3 Aug should check the CSM procurement portal for award outcomes and winning vendors.

5. **Competitive landscape is well-mapped and crowded.** The full CSM 2025 awarded list (HCL, Microsoft, Sangfor, Dell, Elastic, USM/SIEM, security-operator, BCMS consultancy) plus NACSA-event vendors (AIS, Micro Concept Tech) plus NCSS 2026's 100-exhibitor footprint indicate a dense incumbent ecosystem. Differentiation for any new entrant should emphasise CSCDC-specific framework/communications specialisation rather than general cyber-event or infrastructure capability.

6. **No movement on the highest-value non-public PIRs.** PIR-CSCDC-002 (framework v2.0 approval / 90-day clock), PIR-INIT-CSCDC-003 (weekly milestones), and PIR-CSCDC-004 (CCO appointment) remain unchanged across cycles and are unlikely to resolve from OSINT. Watch triggers: next JKSN meeting communiqué, Bernama "CSCDC" keyword alert, PMO release, or cscdc.my transitioning from parked to live.

---

## Sources Consulted

### New this cycle (primary / direct inspection)
- https://www.nacsa.gov.my/doc/Arahan%20KE%20NACSA%20No.%209.pdf (NACSA Chief Executive Directive No. 9, effective 22 Sep 2025 — signed by Megat Zuhairy; PTPKM coordinator designation; Akta 854 legal timeline)
- https://cscdc.my/ (direct HTTP + content inspection — STILL PARKED on Hostinger CDN/hcdn, 31 Jul 12:58)
- https://www.cybersecurity.my/portal-main/procurement (CSM procurement portal — active tenders + full 2025 awarded-vendor list)

### Re-verified this cycle (baseline confirmation)
- https://www.thevibes.com/articles/news/119457/nation-to-consolidate-cyber-defences-under-new-central-agency-says-pm (governance structure, 13 Feb 2026)
- https://www.malaymail.com/news/malaysia/2026/02/13/anwar-national-cybersecurity-agenda-to-be-boosted-amid-rising-global-threats/209038 (JKSN Bil. 1/2026, 13 Feb 2026)
- https://www.bharian.com.my/berita/nasional/2026/06/1567257/pm-tinjau-pusat-teknologi-dan-pengurusan-kriptologi-malaysia (PM visit + KSN chair, 4 Jun 2026)
- https://www.klsescreener.com/v2/news/view/1732913/anwar-visits-cryptology-centre-witnesses-launch-of-cscdc (The Edge/Bernama, 4 Jun 2026)
- https://sciencepark.upm.edu.my/berita/malaysia_perkukuh_kedaulatan_digital_pm_saksikan_penubuhan_cscdc-93753 (UPM, 4 Jun 2026)
- https://media-perpaduan.com/2026/06/04/pm-tinjau-pusat-teknologi-dan-pengurusan-kriptologi-malaysia/ (4 Jun 2026)
- https://harapanmadani.com/pusat-teknologi-dan-pengurusan-kriptologi-malaysia-terima-kunjungan-pm-anwar/ (4 Jun 2026)
- https://vom24.com/malaysia-strengthens-cybersecurity-framework-advances-national-cybercrime-bill-pm-anwar/ (12 Feb 2026)
- https://www.nacsa.gov.my/about-us.php (NACSA location/contact — Perdana Putra, JPM)

### Prior cycle (unchanged, not re-verified this cycle)
- https://www.istiadat.gov.my/wp-content/uploads/2026/03/Ketua-Pengarah-02.03.2026.pdf (MKN DG register, 02 Mar 2026)
- https://digital-id.my/articles/NCSS2026 (NCSS 2026 opening-speech coverage, 07 Jul 2026)
- https://thesun.my/news/malaysia-news/cybersecurity-malaysia-appoints-roshdi-ahmad-as-acting-ceo/ (CSM acting CEO, 14 Jan 2026)
- https://www.businesstoday.com.my/2025/12/18/cybersecurity-malaysia-ceo-dato-amirudin-retires-after-13-years/ (Amirudin retirement, 13 Jan 2026)
- https://www.cyberdsa.com/data/editor/2026/about-us/gov-support-message/nacsa-support-message-2026.pdf (NACSA CEO, CyberDSA 2026)
- https://cydes.my/nacsa-cybersecurity-summit (NCSS 2026 event page)

---

*End of report. Generated 2026-07-31 12:58 +08 by CSCDC Leadership & Approval Watch Agent.*
