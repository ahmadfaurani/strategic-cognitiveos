# CSCDC Leadership & Approval Watch — Intelligence Report

**Agent:** CSCDC Leadership & Approval Watch Agent (Cron Job cj1)
**Collection Cycle:** 2026-07-26 07:28 +08 (Asia/Kuala_Lumpur, UTC+8)
**Classification:** OSINT / Open Source
**Mission PIRs:** PIR-CSCDC-001/002/004/010, PIR-INIT-CSCDC-001/002/003/010, PIR-OPP010-001
**Prior cycle:** cj1-leadership-watch-2026-07-26T0110.md (≈6.3h earlier today)

---

## Collection Methodology & Critical Limitation

**Phase 1 — web_search (11 queries).** The eight (8) required collection queries were executed exactly as briefed, plus three (3) reality-check queries (one naming the real, publicly-documented CyberSecurity Malaysia CEO Amirudin Abdul Wahab; one for NACSA DG 2026; one for CSM merger/consolidation 2026):

1. "CSCDC" OR "Cybersecurity and Cryptology Development Centre" CEO appointment Malaysia
2. "Pusat Pembangunan Keselamatan Siber dan Kriptologi" leadership
3. CyberSecurity Malaysia PTPKM merger integration 2026
4. NACSA director general CSCDC announcement
5. "CyberSecurity Malaysia" CEO CCO appointment 2026
6. MKN cybersecurity framework approval 2026
7. CyberSecurity Malaysia vendor PR agency contract
8. NACSA framework v2.0 approval JPM
9. (reality) CyberSecurity Malaysia CEO Amirudin Abdul Wahab NACSA director general
10. (reality) NACSA Malaysia national cyber security agency director general 2026
11. (reality) "CyberSecurity Malaysia" merger agency consolidation 2026 announcement

**Result: ZERO relevant hits.** Every query returned generic noise: SAP/database docs (q1), Indonesian dictionary entries (q2), generic "What is cybersecurity?" glossary pages IBM/Cisco/Microsoft/Fortinet/CISA (q3,5,7,9,11), Microsoft stock-price pages (q4), German Bluetooth tutorials (q6), Hong Kong racing-fuel sites (q8), and an unrelated US LinkedIn CFO profile (q10). **Critically, the reality-check query naming the real CSM CEO (Amirudin Abdul Wahab) — a definitely-public figure — returned nothing**, confirming the `web_search` backend is **degraded/non-functional for Malaysia-specific proper nouns**, not merely that the entities lack a web footprint. This is the same condition observed at 01:10; it has **not recovered** in ~6 hours and should be treated as a persistent platform impairment, not a transient outage. No `web_extract` was run on these irrelevant URLs.

**Phase 2 — targeted web_extract on authoritative .gov.my / .my portals (executed per prior cycle's Recommended Next-Cycle Actions).** This bypasses the broken search backend and is where real intelligence is recovered:

| URL | Result |
|---|---|
| cybersecurity.my/portal-main/career | ✅ Retrieved (was blocked at 01:10; now accessible) |
| cybersecurity.my/portal-main/procurement | ✅ Retrieved on 2nd attempt (intermittent scrape-block) |
| cybersecurity.my/portal-main/events | ✅ Retrieved |
| cybersecurity.my/ (landing) | ✅ Retrieved |
| nacsa.gov.my/ (landing) | ✅ Retrieved |
| nacsa.gov.my/kriptografi-view.php | ✅ Retrieved |
| mkn.gov.my/ (landing) | ✅ Retrieved |
| cybersecurity.my/about-main | ❌ 404 |
| cybersecurity.my/about | ❌ 404 |
| cybersecurity.my/portal-main/media | ❌ 404 |
| nacsa.gov.my/news.php | ❌ 404 |
| cybersecurity.my/portal-main/article/organization | ❌ scrape-blocked |

---

## Findings (DELTA vs 01:10 cycle emphasised)

### Finding 1 (DELTA): CyberSecurity Malaysia Career portal now accessible — NO CCO / leadership vacancy posted
- **Source:** https://www.cybersecurity.my/portal-main/career
- **Date:** accessed 26 July 2026 07:28 +08
- **Summary:** At 01:10 the CSM career portal was scrape-blocked; this cycle it is accessible. It exposes only a **generic online application form** (Name / Email / Phone / CV upload) with no enumerated open vacancies and **no CCO, CEO, or "Pusat Pembangunan Keselamatan Siber" position advertised.** This is the natural public channel through which a CCO role would be advertised (PIR-CSCDC-004). Its absence here, combined with no CSCDC-labelled procurement and no announcement on any portal, is consistent with the CCO role being **not yet advertised** (or recruited via closed/headhunt channels). Note: absence of a posting ≠ confirmation none exists; a closed search is indistinguishable from no-search via this channel.
- **PIR(s) Addressed:** PIR-CSCDC-004 (CCO appointment status — advertised/shortlisted/filled)
- **Confidence:** MEDIUM (negative-from-observation, not confirmed-absence)
- **Tag:** [VERIFIED] (portal contents); [UNVERIFIED] (inference that no CCO search is publicly open)

### Finding 2 (DELTA): CyberSecurity Malaysia confirmed under Ministry of Digital (KD) — a SECOND ministerial line distinct from NACSA's MKN/JPM line
- **Source:** https://www.cybersecurity.my/portal-main/career (org overview) + https://www.cybersecurity.my/portal-main/events (nav menu)
- **Date:** accessed 26 July 2026
- **Summary:** CSM's career page explicitly states CSM is "the national cyber security specialist agency under the purview of the **Ministry of Digital (KD)**" and links CSM's sister agencies under KD: Jabatan Digital Negara (JDN), Jabatan Perlindungan Data Peribadi (JPDP), MDEC, MYNIC, Digital Nasional, MyDigital. This is a **structural fact not surfaced in the 01:10 cycle** and materially refines the approval-chain analysis: the briefing's chain (CCO → CEO → KSN/MKN → DG NACSA) sits on the **MKN/JPM** line (NACSA's line), whereas CSM's own ministerial accountability runs through **KD (Ministry of Digital)**. If CSCDC is genuinely "formed from PTPKM + CyberSecurity Malaysia" it would by construction span **two ministries (KD for the CSM side; MKN/JPM for the NACSA side)** — making the approval chain more complex than a single vertical and raising the likelihood that a Cabinet/KSN coordination step sits above both. This dual-ministry reality should be treated as the dominant structural unknown for the introduction-path PIR.
- **PIR(s) Addressed:** PIR-CSCDC-001 (shepherds/ministerial lines), PIR-INIT-CSCDC-002 (most credible intro path — now must consider KD vs MKN/JPM vs JPM-top)
- **Confidence:** HIGH (the CSM-under-KD fact); MEDIUM (the dual-ministry CSCDC inference)
- **Tag:** [VERIFIED] for CSM→KD; [UNVERIFIED] for the CSCDC dual-ministry inference

### Finding 3 (DELTA): CSM procurement portal re-checked — NO new Tender; no RM4,005,000 CSCDC Phase 1 procurement has surfaced
- **Source:** https://www.cybersecurity.my/portal-main/procurement
- **Date:** accessed 26 July 2026 07:28 +08
- **Summary:** Procurement portal re-extracted (succeeded on 2nd attempt after an intermittent scrape-block). **No change in open quotations since 01:10:** only SH/06/2026 (Endpoint Computing Hardware/Software) and SH/07/2026 (IT & OT Lab Software) remain open, both closing **03 August 2026 @ 12:00 pm**, both in the RM50k–500k quotation band. **No Tender (>RM500k) is open**, and none matches or approaches the RM4,005,000 CSCDC Phase 1 budget. The 2025–2026 awarded register is essentially unchanged (HCL, Microsoft, Sangfor, Dell, Elastic, USM Anywhere, DPTech, plus consulting items BCMS/ISPMS/PGPKS/People Certification). Newly visible line items vs the 01:10 snapshot: SH/27/2025 "Event Management for Karnival CAKNA Digital 2025 @ Lenggong, Perak" (event logistics — the closest thing to a comms/events vendor, but NOT strategic PR/comms), SH/01/2026 IBPMS, SH/02/2026 HCL Domino, SH/03/2026 VAPT; in-bidding SH/05/2026 DPTech Firewall/iPS & Switches; aborted SH/04/2026 Laptops for Assessment. **No PR / strategic-communications / public-relations agency contract appears in the awarded register.** Because CSCDC's RM4.005m budget exceeds the RM500k Tender threshold, the earliest likely public signal of CSCDC mobilisation would be a new Tender on this portal — it has **not** appeared. Watch this portal weekly; the 3 Aug 2026 quotation close is the next observable procurement event (not CSCDC-related).
- **PIR(s) Addressed:** PIR-CSCDC-002 (mobilisation clock — no procurement signal ⇒ clock likely not yet started), PIR-CSCDC-010 (existing vendors — register unchanged, no PR/comms incumbent), PIR-INIT-CSCDC-010 (competitive landscape — unchanged), PIR-OPP010-001 (no merged-entity procurement visible)
- **Confidence:** HIGH (portal contents); MEDIUM (inference that no-mobilisation-procurement ⇒ clock not started)
- **Tag:** [VERIFIED] for procurement data; [UNVERIFIED] for the clock-not-started inference

### Finding 4 (DELTA): NACSA landing "Key Announcements" — no CSCDC item; only Cyber Security Licensing + Cyber Games 2025 are tagged [NEW]
- **Source:** https://www.nacsa.gov.my/
- **Date:** accessed 26 July 2026
- **Summary:** NACSA's landing "Key Announcements" block lists (with [NEW] tags): "Application for Cyber Security Licensing" and "NACSA Leads the Way: Cyber Games 2025"; plus standing items Cyber Security Act 2024 (Act 854), Pemakluman Pembatalan Arahan MKN No.26, the 22 Mar 2024 media statement, and several technical advisories. **None reference CSCDC, a CEO/CCO appointment, a "framework v2.0", or a 90-day mobilisation.** NACSA re-identifies as "the national lead agency for cyber security matters," established Feb 2017, located at Level LG & G West Wing, Perdana Putra (same building as MKN, within JPM). This corroborates the MKN/JPM side of the chain (NACSA→MKN→JPM) but yields no new leadership or approval-timing intelligence.
- **PIR(s) Addressed:** PIR-CSCDC-001 (NACSA structural placement), PIR-CSCDC-002 (no approval announcement)
- **Confidence:** HIGH (absence on NACSA landing today)
- **Tag:** [VERIFIED] (absence); [UNVERIFIED] (any positive claim)

### Finding 5 (NO-CHANGE): NACSA MyKriptografi page unchanged — still the strongest verifiable policy hook; no implementation-body/CSCDC naming yet
- **Source:** https://www.nacsa.gov.my/kriptografi-view.php
- **Date:** published 11 Feb 2026; content last updated 3 Apr 2026; page-footer visitor-counter "Last Updated 26 July 2026" (daily auto-increment, not a content update)
- **Summary:** MyKriptografi (National Cryptography Policy) text is **identical to the 01:10 extraction**. Cabinet approved it 28 Nov 2025; it replaces DKN 2013; aligned to Cyber Security Act 2024 (Act 854) and MCSS; positioned as Malaysia's "Digital Shield" against quantum-era threats; full policy doc at nacsa.gov.my/kriptografi.php. **No reference to CSCDC, an implementation body, a CEO, or framework v2.0 has been added.** CSCDC's full Malay name (Pusat Pembangunan Keselamatan Siber dan **Kriptologi**) maps onto MyKriptografi's "cryptographic governance, research, and application" direction, so CSCDC remains the most plausible (but unstated) MyKriptografi delivery vehicle. The page's content-stability since April reinforces that no new public implementation-structure announcement has been issued.
- **PIR(s) Addressed:** PIR-CSCDC-001 (policy owner = NACSA), PIR-CSCDC-002 (v2.0 is an internal operational framework, downstream of already-approved policy), PIR-INIT-CSCDC-002 (NACSA path remains structurally strongest on the MKN/JPM side)
- **Confidence:** HIGH (policy fact, unchanged); MEDIUM (CSCDC↔MyKriptografi inference, unchanged)
- **Tag:** [VERIFIED] for policy fact; [UNVERIFIED] for the linkage inference

### Finding 6 (DELTA, NEGATIVE): MKN landing and CSM events calendar show NO CSCDC / framework-v2.0 / launch content
- **Sources:** https://www.mkn.gov.my/ ; https://www.cybersecurity.my/portal-main/events
- **Date:** accessed 26 July 2026
- **Summary:** MKN's landing is oriented to GISBH voluntary rehabilitation, MySejahtera/COVID-19, and general contact info (Aras LG & G, Blok Barat, Bangunan Perdana Putra, Putrajaya — same complex as NACSA). **No CSCDC, no cybersecurity framework v2.0, no CEO appointment, no merger/consolidation announcement.** CSM's events calendar lists 4 upcoming events (FutureCISO 5 Nov 2026; GISEC Global 16–18 Sep 2026; CloudTech & DataCentre 12–13 Aug 2026; AI & Cybersecurity Leaders Summit 6 Aug 2026) — **none is a CSCDC launch, framework-signing, or mobilisation-kickoff event.** Had a 90-day mobilisation clock started recently (the briefing's v2.0 final draft is dated 10 July 2026, i.e. ~16 days ago), one might expect at least an internal-launch or signing event to surface on a public calendar; none has. (Caveat: internal government mobilisation events are routinely not publicised.)
- **PIR(s) Addressed:** PIR-CSCDC-002 (no public launch/announcement ⇒ approval/clock not yet public), PIR-INIT-CSCDC-003 (no public milestone schedule), PIR-OPP010-001 (no integration/merger event)
- **Confidence:** HIGH (absence on these two channels today); LOW (as evidence the clock has not started internally)
- **Tag:** [VERIFIED] (absence); [UNVERIFIED] (positive claims)

### Finding 7 (NEGATIVE, carried forward): "CSCDC" / "PTPKM" / merger-CEO / "framework v2.0" absent from every accessible authoritative channel
- **Sources:** nacsa.gov.my (landing + kriptografi-view), cybersecurity.my (landing + career + procurement + events), mkn.gov.my (landing)
- **Date:** 26 July 2026 07:28 +08
- **Summary:** Across all portals extracted this cycle, the strings "CSCDC", "Pusat Pembangunan Keselamatan Siber dan Kriptologi", "PTPKM", and "framework v2.0" do **not appear**, nor does any CEO/CCO appointment or merger/consolidation announcement. The CSM public portal exposes **no About/Leadership page** (every candidate URL 404'd or scrape-blocked), so CSM's CEO cannot be verified via the portal this cycle. **Net:** as of 26 July 2026 07:28, the CSCDC entity, its CEO/CCO, and framework v2.0 approval are **not publicly disclosed** via these channels — consistent with pre-announcement, internally-named, or publicly framed under MyKriptografi/MCSS without the "CSCDC" label.
- **PIR(s) Addressed:** PIR-CSCDC-001/002/004, PIR-OPP010-001 (all: absence evidence)
- **Confidence:** HIGH (absence across these channels); LOW (for concluding the entity/appointments do not exist — the dual-ministry KD↔MKN/JPM structure and the real CSM/NACSA bodies do exist)
- **Tag:** [VERIFIED] (absence); [UNVERIFIED] (positive existence/identity claims)

---

## Analytical Assessment (UNVERIFIED, analyst inference — not sourced)

Synthesising both cycles, the most defensible working picture (to be confirmed, not relied upon as fact):

- **Approval chain & shepherds (PIR-CSCDC-001):** The structural skeleton is corroborated, but this cycle adds a **second ministerial line**: NACSA sits in MKN within JPM (Perdana Putra), and under Act 854 NACSA's "Chief Executive" (DG NACSA) is the statutory licensing/approval authority; **but CSM itself sits under the Ministry of Digital (KD)**. A CSCDC "formed from PTPKM + CyberSecurity Malaysia" would therefore bridge **two ministries**. The briefing's chain (CCO → CEO → KSN/MKN → DG NACSA) captures the MKN/JPM side; the KD side (CSM's minister, the Digital Minister) is an unnamed additional node. **No named individual** (CEO, acting CCO, DG NACSA, KSN) was identified this cycle.
- **Framework v2.0 & 90-day clock (PIR-CSCDC-002 / PIR-INIT-CSCDC-003):** National cryptography *policy* already Cabinet-approved (28 Nov 2025). The "framework v2.0 final draft 10 July 2026" is best read as an internal operational implementation framework; its approval is an internal sign-off, not a Cabinet event. **No public approval date, no launch event, no mobilisation procurement, no weekly-milestone schedule** has surfaced — consistent with the clock **not yet publicly started** (or started quietly without public disclosure). ~16 days have elapsed since the draft date with zero public signal.
- **Most credible intro path (PIR-INIT-CSCDC-002):** Reframed by the dual-ministry finding. The **NACSA path remains structurally strongest on the MKN/JPM side** (national lead agency, MyKriptografi owner, statutory licensing authority). The **CSM path** now carries added weight as the KD-ministerial operational delivery arm and the home of Malaysia's deepest in-house cryptology capacity (MyCANE, MyCV, PKTN, MySEAL, FIPS 140-3, PQC initiatives — all confirmed live on the CSM portal this cycle). The **JPM-top path** is the formal-political apex over both. Recommendation: a **dual-track approach (NACSA/MKN for policy/approval + CSM/KD for operational/capability)** is now more credible than a single-track NACSA-only approach.
- **External-partnership authority in mobilisation (PIR-INIT-CSCDC-001):** Unchanged — no source. Inference: terminates at/through DG NACSA under Act 854 for cyber-security *service* licensing, but a strategic-comms/framework partnership may also require CSM/KD sign-off on the operational side.
- **Competitive landscape & existing vendors (PIR-INIT-CSCDC-010 / PIR-CSCDC-010):** Unchanged vendor set (HCL, Microsoft, Sangfor, Dell, Elastic, USM Anywhere, DPTech + cyber-consultancies); **no PR/strategic-comms incumbent** in CSM's awarded register. The strategic-communications framework space (CSCDC's apparent remit) remains comparatively open — but this is an inference from absence, not confirmation.
- **CCO appointment status (PIR-CSCDC-004):** Upgraded from "inaccessible" to "accessible, no public CCO posting." Working assessment: **not publicly advertised** (no vacancy on CSM career portal). Status indistinguishable from a closed/headhunt search via this channel.
- **PTPKM↔CSM integration (PIR-OPP010-001):** No merged-entity procurement, no integration announcement, no joint event on any channel.

---

## PIR Resolution Status

| PIR ID | Priority | Question (short) | New Intel This Cycle? | Status |
|---|---|---|---|---|
| PIR-CSCDC-001 | CRITICAL | CEO / acting CCO / MKN-NACSA shepherds | PARTIAL (refinement) | Chain structure corroborated + **dual-ministry (KD for CSM, MKN/JPM for NACSA) added**. DG NACSA = statutory authority. Named individuals NOT identified. |
| PIR-CSCDC-002 | CRITICAL | Framework v2.0 approval date / 90-day clock | PARTIAL (negative) | National crypto policy already approved 28 Nov 2025; v2.0 = internal operational framework. **No public approval date, no launch event, no mobilisation procurement** — clock not publicly started. ~16 days post-draft with zero signal. |
| PIR-INIT-CSCDC-001 | CRITICAL | External-partnership approval authority in mobilisation | NO | Not resolved. Inference: DG NACSA (Act 854, service licensing) + possibly CSM/KD (operational). |
| PIR-INIT-CSCDC-002 | CRITICAL | Most credible intro path (CSM/NACSA/JPM) | PARTIAL (refinement) | **Reframed: dual-track (NACSA/MKN for policy/approval + CSM/KD for operational/capability) now more credible than single-track NACSA.** CSM's deep in-house cryptology capacity confirmed. |
| PIR-INIT-CSCDC-003 | CRITICAL | Weekly milestones in 90-day mobilisation plan | NO | Not resolved — no public source found; no launch event on CSM calendar. |
| PIR-CSCDC-004 | HIGH | CCO appointment status (advertised/shortlisted/filled) | PARTIAL (delta) | CSM career portal now accessible → **no CCO posting visible**. Working assessment: not publicly advertised (closed/headhunt indistinguishable). |
| PIR-CSCDC-010 | HIGH | Existing PR/consultants/vendors engaged | PARTIAL (unchanged) | CSM procurement register re-confirmed: technical/IT/cyber-consultancy vendors; **no PR/comms vendor**. Closest adjacent: SH/27/2025 event-management (Karnival CAKNA), not strategic PR. |
| PIR-INIT-CSCDC-010 | HIGH | Competitive landscape — vendors currently engaged | PARTIAL (unchanged) | Same vendor set (HCL, Microsoft, Sangfor, Dell, Elastic, USM Anywhere, DPTech…); comms/PR gap persists. No new Tender; no RM4M CSCDC procurement. |
| PIR-OPP010-001 | HIGH | PTPKM↔CSM operational integration status | NO | No merged-entity procurement, integration announcement, or joint event on any channel. |

**Summary:** 0 of 9 PIRs fully resolved; 6 of 9 advanced partially (3 with genuine delta vs the 01:10 cycle: dual-ministry structural finding, CSM-career-portal CCO absence, procurement no-new-tender); 3 of 9 unchanged-unresolved. **No named CEO, acting CCO, DG NACSA, framework-v2.0 approval date, or weekly mobilisation milestones were identified.** No fabricated data was introduced; all sourced facts are [VERIFIED] from .gov.my / .my domains; all inferences are marked [UNVERIFIED].

---

## Recommended Next-Cycle Actions

1. **Flag search-backend degradation as a persistent (not transient) platform defect.** 11 queries across two cycles (~6h apart) all failed; even a real public figure (CSM CEO Amirudin Abdul Wahab) does not surface. OSINT on Malaysia-specific proper nouns is currently impossible via web_search; rely on direct web_extract.
2. **Retry the CSM procurement portal each cycle** (intermittent scrape-block) and watch for any new **Tender >RM500k** — the earliest likely public signal of CSCDC's RM4,005,000 Phase 1 mobilisation. Next known procurement event: SH/06–07/2026 close 3 Aug 2026.
3. **Find and extract a CSM leadership/About page** — every candidate URL (/about, /about-main) 404'd this cycle; try /portal-main/about, /portal-main/leadership, or the CSM-CP / advisory microsites. PIR-CSCDC-001 needs the named CSM CEO (currently unverifiable via portal).
4. **Extract the full MyKriptografi policy document** at nacsa.gov.my/kriptografi.php (linked but not yet extracted) — it may name the implementation body / CSCDC.
5. **Add a Ministry of Digital (KD) collection node** (kd.gov.my / mydigital.gov.my) to the watch — since CSM sits under KD, any CSCDC mobilisation announcement could appear on a KD-channel rather than MKN/JPM.
6. **Re-extract NACSA MyKriptografi page weekly** for any "implementation body / delivery arm" naming (CSCDC may be publicly named as MyKriptografi's delivery arm before the "CSCDC" label surfaces independently).
7. **Monitor CSM events calendar** for any CSCDC launch/signing event (none today).
