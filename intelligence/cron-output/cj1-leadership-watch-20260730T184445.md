# CSCDC Leadership & Approval Watch — Intelligence Report

**Job:** cj1-leadership-watch (CSCDC Leadership & Approval Watch Agent)
**Collection Cycle:** Thursday, 30 July 2026
**Timestamp (Asia/Kuala_Lumpur, UTC+8):** 2026-07-30 18:44 +08
**Analyst:** Strategic CognitiveOS — Cron Agent (GLM-5.2)
**Classification:** OSINT — For internal strategic planning only
**Mission:** Resolve Critical PIRs related to CSCDC leadership mapping, decision authority, framework approval status, and competitive landscape.

---

## Executive Summary

Substantial open-source confirmation of CSCDC's institutional architecture and top leadership was located this cycle, but the granular operational items (framework v2.0 approval date, 90-day mobilisation milestones, CCO appointment, vendor roster) remain non-public. The single most important new confirmation is that the **Chief Secretary to the Government (KSN), Tan Sri Shamsul Azri Abu Bakar, was formally appointed Chairman of the CSCDC Board of Directors on 4 June 2026**, witnessed by PM Anwar Ibrahim at PTPKM. This places the KSN directly at the apex of the CSCDC governance chain, which materially clarifies the approval-chain assumption (CCO → CEO → KSN/MKN → DG NACSA): the KSN is now simultaneously the board chair and the senior-most civil-service authority. NACSA CEO Dr Megat Zuhairy Megat Tajudin is confirmed as the regulatory shepherd, and CSM Acting CEO Roshdi Ahmad is the operational-continuity leader as CSM is absorbed into CSCDC. The `cscdc.my` domain is currently **parked on Hostinger** (no live corporate site), an indicator that CSCDC's external corporate-communications presence is not yet operationalised.

---

## Findings

### Finding 1: Tan Sri Shamsul Azri Abu Bakar (KSN) appointed Chairman of CSCDC Board of Directors
- **Source:** https://www.bernama.com/en/news.php?id=2564763 ; https://theedgemalaysia.com/node/805885 ; https://www.bharian.com.my/berita/nasional/2026/06/1567257/pm-tinjau-pusat-teknologi-dan-pengurusan-kriptologi-malaysia ; https://malaysiantribune.com/anwar-ibrahim-inaugurates-cyber-security-cryptology-development-centre/
- **Date:** 4 June 2026
- **Summary:** On 4 June 2026, PM Anwar Ibrahim visited PTPKM (Putrajaya) and formally witnessed the establishment of the Cyber Security Cryptology Development Centre (CSCDC). Concurrently he witnessed the appointment of the Chief Secretary to the Government, Tan Sri Shamsul Azri Abu Bakar, as Chairman (Pengerusi) of the CSCDC Board of Directors (Lembaga Pengarah). Shamsul Azri is the 16th KSN (in office since 12 Aug 2024), a Pahang-born PTD officer with a BBA from University of Tulsa and training at INTAN/Cambridge/INSEAD. This appointment was corroborated across four independent outlets (Bernama, The Edge, Berita Harian, Malaysian Tribune).
- **PIR(s) Addressed:** PIR-CSCDC-001 (CRITICAL), PIR-INIT-CSCDC-001 (CRITICAL), PIR-INIT-CSCDC-002 (CRITICAL)
- **Confidence:** HIGH
- **Tag:** [VERIFIED]

### Finding 2: Dr Megat Zuhairy Megat Tajudin confirmed as NACSA CEO — regulatory shepherd for CSCDC
- **Source:** https://www.cyberdsa.com/data/editor/2026/about-us/gov-support-message/nacsa-support-message-2026.pdf ; https://www.thestar.com.my/news/nation/2026/07/28/risk-based-approach-vital-in-ensuring-digital-safety ; https://www.hmetro.com.my/mutakhir/2025/10/1274338/pusat-pembangunan-keselamatan-siber-dan-kriptologi-langkah-strategik
- **Date:** CyberDSA 2026 support message; The Star article 28 July 2026 (most recent active confirmation)
- **Summary:** Ir. Dr. Megat Zuhairy bin Megat Tajuddin is the Chief Executive Officer of the National Cyber Security Agency (NACSA), per the CyberDSA 2026 official support message (titled "CHIEF EXECUTIVE OFFICER OF NATIONAL CYBER SECURITY AGENCY (NACSA), MALAYSIA"). The Star (28 Jul 2026) quotes him as NACSA's "chief executive" introducing the AI Systems Cyber Security Framework (AISCF). He is the public-facing voice on NACSA's CSCDC announcement (Hmetro, Oct 2025), stating CSCDC "will become the new nerve centre for building technical capability and expertise." Note a title nuance: the NACSA Act 2024 statutorily designates the head as "Chief Executive"; some outlets (e.g. completeaitraining) loosely call him "director-general." The authoritative title is CEO/Chief Executive. NACSA is CSCDC's regulatory parent under JPM.
- **PIR(s) Addressed:** PIR-CSCDC-001 (CRITICAL), PIR-INIT-CSCDC-002 (CRITICAL)
- **Confidence:** HIGH
- **Tag:** [VERIFIED]

### Finding 3: Roshdi Ahmad appointed Acting CEO of CyberSecurity Malaysia (effective 14 Jan 2026)
- **Source:** https://www.bernama.com/en/general/news.php?id=2512238 ; https://themalaysianreserve.com/2026/01/14/cybersecurity-malaysia-appoints-roshdi-ahmad-as-acting-ceo/ ; https://www.linkedin.com/posts/cybersecuritymalaysia_cybersecuritymalaysia-keselamatansiber-activity-7417028292626583552-_7yh
- **Date:** 14 January 2026
- **Summary:** CyberSecurity Malaysia named its COO Roshdi bin Haji Ahmad as Acting CEO with immediate effect on 14 Jan 2026, following the retirement of Datuk Dr Amirudin Abdul Wahab (who helmed CSM for 13 years). Roshdi has been at CSM since 2007, COO since Nov 2021, with prior stints at MRCB, Daihatsu, and MDEC; credentials include MSc Information Management (UiTM), Harvard Business School leadership programme. As of this cycle, no public announcement of a permanent (non-acting) CSM CEO was located, nor any CSCDC-specific CEO designation — Roshdi remains the de-facto operational head of the CSM functions being centralised into CSCDC. Separately, Roshdi was also appointed Adjunct Professor of Practice (1 Jan 2026–31 Dec 2027) per a CSM LinkedIn post.
- **PIR(s) Addressed:** PIR-CSCDC-001 (CRITICAL), PIR-OPP010-001 (HIGH), PIR-CSCDC-004 (HIGH)
- **Confidence:** HIGH
- **Tag:** [VERIFIED]

### Finding 4: CSCDC governance structure confirmed — JPM placement, NACSA + MKN as technical/operational wings, Cabinet-approved
- **Source:** https://x.com/anwaribrahim/status/2021890706303005055 (JKSN Bil. 1/2026 announcement, 12 Feb 2026) ; https://www.thevibes.com/articles/news/119457/nation-to-consolidate-cyber-defences-under-new-central-agency-says-pm
- **Date:** 12 February 2026 (JKSN Bil. 1/2026)
- **Summary:** PM Anwar chaired the first National Cyber Security Committee (JKSN) meeting of 2026 on 12 Feb 2026, which reviewed CSCDC progress. The confirmed structure: CSCDC consolidates PTPKM (which gains permanent institutional placement) and CyberSecurity Malaysia (whose functions and resources are centralised under CSCDC). CSCDC is placed under the Prime Minister's Department (JPM) and regulated by NACSA and the National Security Council (MKN), which act as its technical and operational arms. Cabinet (Jemaah Menteri) had previously approved the formation. The same meeting agreed new policy directions for the Cybercrime Bill (RUU Jenayah Siber) covering AI/deepfake misuse, intimate-image dissemination, and data-retention provisions.
- **PIR(s) Addressed:** PIR-CSCDC-001 (CRITICAL), PIR-INIT-CSCDC-002 (CRITICAL), PIR-OPP010-001 (HIGH)
- **Confidence:** HIGH
- **Tag:** [VERIFIED]

### Finding 5: Cybercrimes Bill 2026 passed Dewan Negara (20 July 2026) — adjacent legislative milestone
- **Source:** https://www.freemalaysiatoday.com/category/nation/2026/07/20/dewan-negara-passes-cyber-security-bill-2026 ; https://thesun.my/news/malaysia-news/malaysia-senate-passes-cyber-security-bill-2026/ ; https://opengovasia.com/malaysia-cybercrime-bill-2026-to-combat-evolving-digital-threats/
- **Date:** 20 July 2026
- **Summary:** The Dewan Negara (Senate) passed the Cybercrimes Bill 2026 on 20 July 2026 — the most significant Malaysian cyber-law reform in nearly three decades, repealing the Computer Crimes Act 1997 and addressing identity theft, deepfakes, online fraud, and cross-border enforcement (extraditable offences). This is the legislative companion to the CSCDC institutional restructuring agreed at JKSN Bil. 1/2026. While not the CSCDC communication framework v2.0 itself, it is a direct sibling milestone on the same approval track (JPM/MKN/JKSN) and confirms the policy momentum through Q3 2026.
- **PIR(s) Addressed:** PIR-CSCDC-002 (CRITICAL)
- **Confidence:** HIGH
- **Tag:** [VERIFIED]

### Finding 6: cscdc.my domain is PARKED (Hostinger) — no live corporate web presence
- **Source:** https://cscdc.my/
- **Date:** Observed 30 July 2026
- **Summary:** The domain `cscdc.my` currently resolves to a Hostinger parked-domain placeholder ("Start your online journey"), not an active CSCDC corporate website. This is a useful negative indicator: CSCDC's external-facing corporate-communications and stakeholder-engagement digital presence is not yet operationalised nearly two months after the 4 June 2026 launch/Board-chairman appointment. It implies that any external partnership intake, vendor onboarding, or public-framework publication is not yet routable through a CSCDC-owned channel — engagements would for now run through NACSA/CSM/JPM channels instead.
- **PIR(s) Addressed:** PIR-CSCDC-004 (HIGH), PIR-CSCDC-010 (HIGH), PIR-INIT-CSCDC-010 (HIGH)
- **Confidence:** HIGH (domain state directly observed)
- **Tag:** [VERIFIED]

### Finding 7: Dr Solahuddin Shamsuddin identified as senior PTPKM cryptology expert (Policy & Compliance)
- **Source:** https://scholar.google.com/citations?user=zXN3b9kAAAAJ&hl=en ; https://my.linkedin.com/in/dr-solahuddin-shamsuddin-88093520 ; https://www.linkedin.com/posts/zulkifli-mamat-26b713260_strategic-business-meeting-i-met-dr-solahuddin-activity-7476574900795777024-gKJJ
- **Date:** LinkedIn/Google Scholar profiles (current as of 2026)
- **Summary:** Dr Solahuddin Shamsuddin is an Expert (Policy & Compliance) at PTPKM with 3+ decades spanning Malaysian Armed Forces Signal Corps, CyberSecurity Malaysia, UTP, and national-security cryptology. His Google Scholar affiliation reads "Expert, Pusat Teknologi dan Pengurusan Kriptografi Malaysia (PTPKM)." As PTPKM is being given permanent institutional placement inside CSCDC, Solahuddin is a plausible senior technical/policy interlocutor on the PTPKM side of the merger. (A secondary AI-generated source loosely labels him "Chief Technology Officer at CyberSecurity Malaysia" — treat as unverified; his authoritative PTPKM role is the safer attribution.)
- **PIR(s) Addressed:** PIR-CSCDC-001 (CRITICAL — secondary), PIR-OPP010-001 (HIGH)
- **Confidence:** MEDIUM
- **Tag:** [UNVERIFIED] (title specificity)

### Finding 8: CyberSecurity Malaysia procurement infrastructure (vendor onboarding channel)
- **Source:** https://www.cybersecurity.my/portal-main/procurement
- **Date:** Live as of 30 July 2026
- **Summary:** CSM maintains a public procurement portal with a defined threshold: vendor registration applies to requisitions ≤ RM50,000; procurements above RM50,000 are advertised in the site's Advertisement section. Since CSCDC's own domain is parked and its procurement function not yet public, the CSM procurement portal is the most credible existing official channel for any vendor/PR-agency engagement with the consolidating entity during the mobilisation phase. No CSCDC- or PTPKM-specific named PR agency or communications vendor was identified in public sources this cycle.
- **PIR(s) Addressed:** PIR-CSCDC-010 (HIGH), PIR-INIT-CSCDC-010 (HIGH)
- **Confidence:** MEDIUM
- **Tag:** [VERIFIED] (portal exists); [UNVERIFIED] (no named vendor confirmed)

### Finding 9: Datuk Dr Amirudin Abdul Wahab — former CSM CEO, still active as cybersecurity thought-leader
- **Source:** https://www.thestar.com.my/news/nation/2026/07/28/risk-based-approach-vital-in-ensuring-digital-safety
- **Date:** 28 July 2026
- **Summary:** Datuk Dr Amirudin Abdul Wahab, who retired as CSM CEO on 13 Jan 2026 after 13 years, continues to be cited as an expert voice (The Star, 28 Jul 2026) recommending Zero-Trust/least-privilege approaches for AI agents. His continued public profile suggests he remains a potential informal adviser/influencer in the CSCDC ecosystem, though he holds no confirmed CSCDC role.
- **PIR(s) Addressed:** PIR-CSCDC-001 (CRITICAL — context), PIR-INIT-CSCDC-002 (CRITICAL — relationship path)
- **Confidence:** MEDIUM
- **Tag:** [UNVERIFIED] (no formal CSCDC role confirmed)

---

## PIR Resolution Status

| PIR ID | Priority | Subject | New Intel This Cycle? | Status |
|---|---|---|---|---|
| PIR-CSCDC-001 | CRITICAL | CSCDC CEO, acting CCO, MKN/NACSA shepherds | **PARTIAL** | Board Chairman = KSN Shamsul Azri (VERIFIED). NACSA shepherd = CEO Megat Zuhairy (VERIFIED). CSM-side operational head = Acting CEO Roshdi Ahmad (VERIFIED). A CSCDC-specific CEO and any "acting CCO" were NOT publicly identified. |
| PIR-CSCDC-002 | CRITICAL | Framework v2.0 formal approval + 90-day mobilisation clock start | **PARTIAL / NEGATIVE** | No public disclosure of framework v2.0 approval date or 90-day clock. Closest confirmed adjacent milestone: Cybercrimes Bill 2026 passed Dewan Negara 20 Jul 2026. JKSN Bil. 1/2026 (12 Feb 2026) reviewed CSCDC progress. Framework v2.0 itself is non-public. |
| PIR-INIT-CSCDC-001 | CRITICAL | Who can approve external partnerships during mobilisation | **INFERRED** | Not publicly stated. By governance structure, mobilisation-phase partnership authority most plausibly flows through the CSCDC Board (chaired by KSN Shamsul Azri) with NACSA CEO (Megat Zuhairy) as regulator; operational sign-off likely via acting CSM CEO Roshdi Ahmad. Requires direct confirmation. |
| PIR-INIT-CSCDC-002 | CRITICAL | Most credible introduction path (CSM / NACSA / JPM) | **UPDATED** | Three paths now have named principals: JPM/KSN path → Shamsul Azri (Board Chair, apex authority); NACSA path → Megat Zuhairy (regulator); CSM path → Roshdi Ahmad (operational, being absorbed). The NACSA→CSM operational path offers the most credible working-level entry; the JPM/KSN path is the highest-authority but most remote. |
| PIR-INIT-CSCDC-003 | CRITICAL | Weekly milestones in the 90-day mobilisation plan | **NEGATIVE** | No public information. The 90-day plan is non-public / internal. Recommend HUMINT/internal-source acquisition. |
| PIR-CSCDC-004 | HIGH | CCO appointment status (advertised/shortlisted/filled) | **NEGATIVE** | No public "CCO" (Chief Communication Officer) vacancy, shortlist, or appointment located for CSCDC. The cscdc.my domain being parked reinforces that the comms function is not yet stood up. (Note: CSCDC is framed publicly as a technical cryptology/cybersecurity centre; the "CCO" role may be internal nomenclature.) |
| PIR-CSCDC-010 | HIGH | Existing PR agencies/consultants/vendors at CSCDC/PTPKM/CSM | **NEGATIVE** | No named PR agency or communications vendor confirmed for CSCDC/PTPKM/CSM. CSM procurement portal (RM50k threshold) is the existing official channel. cscdc.my parked. |
| PIR-INIT-CSCDC-010 | HIGH | Competitive landscape — vendors currently engaged | **NEGATIVE** | No named vendors/competitors confirmed for CSCDC engagement this cycle. Open procurement is via CSM portal + generic Malaysian cyber-security tender aggregators. Recommend monitoring ePerolehan/BidAssist for CSCDC-specific RFPs. |
| PIR-OPP010-001 | HIGH | Operational integration status PTPKM ↔ CSM | **PARTIAL** | Institutional/structural integration confirmed (Cabinet-approved merger into CSCDC under JPM, NACSA+MKN oversight; PTPKM permanent placement; CSM centralised). Operational integration (staff, systems, colocation, shared processes) details remain non-public. PTPKM expert Dr Solahuddin Shamsuddin identified. |

---

## Analytical Notes & Recommendations

1. **Approval-chain refinement.** The mission's assumed approval chain (CCO → CEO → KSN/MKN → DG NACSA) is now better resolved: the KSN is *simultaneously* the CSCDC Board Chairman, which collapses one link — partnership/framework approvals effectively route to the KSN-as-Chair, with NACSA CEO as the regulator-of-record. "DG NACSA" in the chain should be updated to "CEO NACSA" (Dr Megat Zuhairy), the statutorily correct title.

2. **No public CCO.** No open-source evidence supports a filled/shortlisted/advertised "Chief Communication Officer" role at CSCDC. Given cscdc.my is parked, the comms/external-engagement function is not yet externally routable. Any external partnership overture during mobilisation should therefore target the *operational* heads (Roshdi Ahmad / NACSA CEO office) rather than a non-existent CCO inbox.

3. **Framework v2.0 is non-public.** The "framework v2.0 final draft dated 10 July 2026" appears to be an internal working document not mirrored in any public source. Expect the formal approval trigger to surface first via a JKSN meeting communiqué or a Bernama/PMO release — set a watch on `jendelamadani.net`, Bernama CSCDC keyword, and the PM's X/Facebook for the next JKSN sitting.

4. **Domain watch.** Add `cscdc.my` to the recurring watch — transition from "parked" to a live site (likely NACSA- or JPM-hosted) will be a leading indicator that the corporate-comms function and external-partnership intake are going live, which in turn signals the 90-day mobilisation clock is near/at start.

5. **Highest-value next collection targets (HUMINT/internal):** (a) CSCDC CEO identity and start date; (b) framework v2.0 sign-off date and 90-day milestone schedule; (c) named mobilisation-phase vendors/PR agency; (d) any advertised CCO/comms role. These are unlikely to resolve from open sources alone.

---

## Sources Consulted (key URLs)
- https://www.bernama.com/en/news.php?id=2564763 (CSCDC launch + KSN chair appointment, 4 Jun 2026)
- https://theedgemalaysia.com/node/805885 (Anwar visits PTPKM, witnesses CSCDC launch)
- https://www.bharian.com.my/berita/nasional/2026/06/1567257/pm-tinjau-pusat-teknologi-dan-pengurusan-kriptologi-malaysia
- https://malaysiantribune.com/anwar-ibrahim-inaugurates-cyber-security-cryptology-development-centre/
- https://en.wikipedia.org/wiki/Shamsul_Azri_Abu_Bakar (KSN profile)
- https://www.cyberdsa.com/data/editor/2026/about-us/gov-support-message/nacsa-support-message-2026.pdf (NACSA CEO title)
- https://www.thestar.com.my/news/nation/2026/07/28/risk-based-approach-vital-in-ensuring-digital-safety (Megat Zuhairy active, 28 Jul 2026)
- https://www.bernama.com/en/general/news.php?id=2512238 (Roshdi Ahmad acting CSM CEO, 14 Jan 2026)
- https://themalaysianreserve.com/2026/01/14/cybersecurity-malaysia-appoints-roshdi-ahmad-as-acting-ceo/
- https://x.com/anwaribrahim/status/2021890706303005055 (JKSN Bil. 1/2026, 12 Feb 2026)
- https://www.thevibes.com/articles/news/119457/nation-to-consolidate-cyber-defences-under-new-central-agency-says-pm
- https://www.freemalaysiatoday.com/category/nation/2026/07/20/dewan-negara-passes-cyber-security-bill-2026 (Cybercrimes Bill passed, 20 Jul 2026)
- https://cscdc.my/ (domain parked — observed 30 Jul 2026)
- https://www.cybersecurity.my/portal-main/procurement (CSM procurement portal)
- https://scholar.google.com/citations?user=zXN3b9kAAAAJ&hl=en (Dr Solahuddin Shamsuddin, PTPKM)

---

*End of report. Generated 2026-07-30 18:44 +08 by CSCDC Leadership & Approval Watch Agent.*
