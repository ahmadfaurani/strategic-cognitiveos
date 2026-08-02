# CSCDC Leadership & Approval Watch — Intelligence Report

**Agent:** CSCDC Leadership & Approval Watch Agent (Cron Job cj1)
**Collection Cycle:** 2026-07-26 01:10 +08 (Asia/Kuala_Lumpur, UTC+8)
**Classification:** OSINT / Open Source
**Mission PIRs:** PIR-CSCDC-001/002/004/010, PIR-INIT-CSCDC-001/002/003/010, PIR-OPP010-001

---

## Collection Methodology & Critical Limitation

Eight (8) web_search queries were executed exactly as specified in the task brief:
1. "CSCDC" OR "Cybersecurity and Cryptology Development Centre" CEO appointment Malaysia
2. "Pusat Pembangunan Keselamatan Siber dan Kriptologi" leadership
3. CyberSecurity Malaysia PTPKM merger integration 2026
4. NACSA director general CSCDC announcement
5. "CyberSecurity Malaysia" CEO CCO appointment 2026
6. MKN cybersecurity framework approval 2026
7. CyberSecurity Malaysia vendor PR agency contract
8. NACSA framework v2.0 approval JPM

**⚠️ TOOLING LIMITATION (must be read before interpreting this report):**
The `web_search` backend is **degraded/non-functional for these queries**. Even highly specific proper-noun queries returned unrelated generic pages — e.g. query #4 ("NACSA Malaysia director general 2026 Megat Zuhairi") returned Vietnamese food guides; query #6 ("MKN cybersecurity framework approval") returned a German kitchen manufacturer; queries containing "cybersecurity" returned only generic "What is cybersecurity?" glossary pages (IBM, Cisco, Microsoft, Fortinet, CompTIA, CISA) regardless of the Malaysia-specific qualifiers. No Malaysia-specific news, government, or press results were surfaced for ANY of the 8 required queries. This is a genuine collection failure of the search backend, not an absence of information on the public web.

**Fallback collection path (executed):** Direct `web_extract` retrieval from the four authoritative Malaysian government portals — NACSA (nacsa.gov.my), CyberSecurity Malaysia (cybersecurity.my), MKN (mkn.gov.my), JPM (jpm.gov.my) — plus targeted sub-pages (NACSA MyKriptografi policy page, NACSA MCSS page, CyberSecurity Malaysia procurement portal, CyberSecurity Malaysia career portal). This produced verifiable OSINT even though the search backend did not.

---

## Findings

### Finding 1: MyKriptografi (National Cryptography Policy) approved by Cabinet 28 November 2025 — strongest verifiable policy hook to CSCDC's cryptology mandate
- **Source:** https://www.nacsa.gov.my/kriptografi-view.php
- **Date:** Policy published 11 February 2026; content last updated 3 April 2026; page footer last updated 26 July 2026 (today).
- **Summary:** NACSA's MyKriptografi was officially approved by Cabinet on 28 November 2025 and replaces the 2013 National Cryptography Policy (DKN 2013). It is developed "in alignment with the Cyber Security Act 2024 [Act 854] and the Malaysia Cyber Security Strategy (MCSS)," and is positioned as Malaysia's "Digital Shield" against sophisticated/quantum-era threats, aiming to build "a resilient, self-reliant cryptographic ecosystem." CSCDC's full name — *Pusat Pembangunan Keselamatan Siber dan Kriptologi* (Cybersecurity and **Cryptology** Development Centre) — maps directly onto MyKriptografi's "cryptographic governance, research, and application" direction, making it the most plausible policy vehicle CSCDC serves.
- **PIR(s) Addressed:** PIR-CSCDC-001 (shepherds/policy owner), PIR-CSCDC-002 (framework approval context), PIR-INIT-CSCDC-002 (intro path via NACSA)
- **Confidence:** HIGH (policy approval itself); MEDIUM (inference that CSCDC is the MyKriptografi delivery vehicle — not stated on any source)
- **Tag:** [VERIFIED] for the policy fact; [UNVERIFIED] for the CSCDC↔MyKriptografi linkage inference

### Finding 2: NACSA is the national lead agency, structurally under MKN/JPM, and the "Chief Executive" (DG NACSA) is the statutory licensing/approval authority
- **Source:** https://www.nacsa.gov.my/ and https://www.nacsa.gov.my/kriptografi-view.php
- **Date:** accessed 26 July 2026
- **Summary:** NACSA is "the national lead agency for cyber security matters," physically co-located with MKN at "Level LG & G, West Wing, Perdana Putra Building, Putrajaya" (the same building as MKN and within the Prime Minister's Department). Per the Cyber Security Act 2024, applications for a licence to provide cyber security services are made "to the Chief Executive" of NACSA (i.e. the Director General, NACSA). External links from NACSA's own page explicitly reference JPM and MKN, confirming the JPM → MKN → NACSA hierarchy. This corroborates the briefing's approval chain (CCO → CEO → KSN/MKN → DG NACSA) and establishes DG NACSA as the terminal approval authority in the chain.
- **PIR(s) Addressed:** PIR-CSCDC-001 (DG NACSA shepherd; NACSA/JPM hierarchy), PIR-INIT-CSCDC-002 (most credible intro path), PIR-INIT-CSCDC-001 (external-partnership authority likely terminates at/through DG NACSA under Act 854)
- **Confidence:** HIGH
- **Tag:** [VERIFIED]

### Finding 3: Governing framework context — Cyber Security Act 2024 (Act 854) + Malaysia Cyber Security Strategy (MCSS) 2025–2030
- **Source:** https://www.nacsa.gov.my/ (landing + mcss.php)
- **Date:** Act 854 gazetted 26 June 2024; MCSS 2025–2030 in force; pages accessed 26 July 2026
- **Summary:** The Cyber Security Act 2024 (Act 854) was gazetted by the Attorney General's Chambers on 26 June 2024 and supersedes MKN (NSC) Directive No. 26 on National Cyber Security Management. The MCSS 2025–2030 is the current national cyber security strategy document. MyKriptografi is explicitly built "in alignment with" both. **Reframe for PIR-CSCDC-002:** because the national cryptography *policy* was already Cabinet-approved on 28 Nov 2025, the briefing's "framework v2.0 final draft dated 10 July 2026" is most likely an *operational/organisational implementation framework* (for delivering MyKriptografi/MCSS via CSCDC), not the national policy itself — so its approval clock is a separate, downstream internal approval, not a Cabinet-level event.
- **PIR(s) Addressed:** PIR-CSCDC-002 (framework v2.0 approval nature/timing), PIR-INIT-CSCDC-003 (mobilisation plan framing)
- **Confidence:** HIGH (Act/MCSS facts); MEDIUM (reframe inference)
- **Tag:** [VERIFIED] for Act 854 + MCSS; [UNVERIFIED] for the v2.0 reframe inference

### Finding 4: CyberSecurity Malaysia active procurement & historical vendor landscape — comms/PR vendors ABSENT from awarded contracts
- **Source:** https://www.cybersecurity.my/portal-main/procurement
- **Date:** procurement portal current as of 26 July 2026; open quotations closing 3 August 2026
- **Summary:** CyberSecurity Malaysia's procurement portal shows two open quotations (SH/06/2026 Endpoint Computing Hardware/Software; SH/07/2026 IT & OT Lab Software, both closing 3 Aug 2026, RM50k–500k range) and a full 2025–2026 awarded-tender register. Awarded vendors/products are predominantly **technical cyber/IT resellers and cyber-consultancies**: HCL (Domino), Microsoft (M365/Exchange Online), Sangfor (NGFW), Dell (PowerEdge/warranty), Elastic (X-Pack/backup), USM Anywhere (SIEM), DPTech (firewall/iPS/switches), plus consulting items (BCMS ISO 22301, ISPMS, PGPKS SME guidelines, People Certification Scheme). **Notably, no strategic-communications / PR / public-relations agency contracts appear in the awarded register.** Procurement thresholds: RFP >RM50k; Quotation RM50k–500k; Tender >RM500k. **Operational note:** CSCDC's RM4,005,000 Phase 1 budget exceeds the RM500k tender threshold, so formal CSCDC procurement would require a Tender (not a quotation). No "CSCDC" or "PTPKM" tagged procurement exists on the CSM portal.
- **PIR(s) Addressed:** PIR-CSCDC-010 (existing vendors), PIR-INIT-CSCDC-010 (competitive landscape), PIR-OPP010-001 (indirectly — CSM continues independent procurement, no PTPKM/merged entity procurement visible)
- **Confidence:** HIGH (portal contents); MEDIUM (inference that the strategic-comms space is comparatively open because no PR/comms vendor is visible)
- **Tag:** [VERIFIED] for procurement data; [UNVERIFIED] for the "open comms space" inference

### Finding 5: CyberSecurity Malaysia Career portal inaccessible to scraper — CCO appointment status NOT verifiable this cycle
- **Source:** https://www.cybersecurity.my/portal-main/career
- **Date:** attempted 26 July 2026
- **Summary:** The CyberSecurity Malaysia career portal returned an internal scrape failure ("All scraping engines failed... page requires authentication or is blocking automated access"). This is the natural source to verify whether a CCO role is advertised/shortlisted/filled (PIR-CSCDC-004). It could not be retrieved this cycle. **No other source surfaced a CCO appointment.** PIR-CSCDC-004 remains unresolved via OSINT this cycle.
- **PIR(s) Addressed:** PIR-CSCDC-004 (attempted, not resolved)
- **Confidence:** LOW (negative result due to access failure, not confirmed absence)
- **Tag:** [UNVERIFIED]

### Finding 6 (Negative): "CSCDC" / "PTPKM" / merger CEO appointment absent from all four authoritative government portals
- **Sources:** nacsa.gov.my, cybersecurity.my, mkn.gov.my, jpm.gov.my (all extracted 26 July 2026)
- **Date:** 26 July 2026
- **Summary:** Across NACSA, CyberSecurity Malaysia, MKN, and JPM landing pages (plus NACSA cryptography/MCSS sub-pages and the CSM procurement portal), the strings "CSCDC", "Pusat Pembangunan Keselamatan Siber dan Kriptologi", and "PTPKM" do **not appear**, nor is any merger/consolidation announcement, CEO appointment, or "framework v2.0" approval visible. Combined with the search backend returning no usable results, this indicates that as of 26 July 2026 the CSCDC entity, its CEO/CCO, and framework v2.0 approval are **not publicly disclosed** via these channels — consistent with the entity being either pre-announcement, internally named, or framed publicly under MyKriptografi/MCSS without the "CSCDC" label.
- **PIR(s) Addressed:** PIR-CSCDC-001, PIR-CSCDC-002, PIR-CSCDC-004, PIR-OPP010-001 (all: negative/absence evidence)
- **Confidence:** HIGH (that the term is absent from these portals today); LOW (for concluding the entity/appointments do not exist)
- **Tag:** [VERIFIED] (absence); [UNVERIFIED] (any positive existence claim)

---

## Analytical Assessment (UNVERIFIED, analyst inference — not sourced)

Synthesising the above, the most defensible working picture (to be confirmed, not relied upon as fact):

- **Approval chain (PIR-CSCDC-001):** Corroborated structurally — NACSA sits within MKN within JPM at the Perdana Putra building, and the Cyber Security Act 2024 makes NACSA's "Chief Executive" (DG NACSA) the statutory authority for cyber-security service licensing. The briefing's chain (CCO → CEO → KSN/MKN → DG NACSA) is therefore plausible and the terminal node (DG NACSA) is the named approval authority. The specific individuals for CEO/acting CCO/DG NACSA were NOT identified this cycle.
- **Framework v2.0 (PIR-CSCDC-002):** The national cryptography *policy* was already approved (28 Nov 2025). The "framework v2.0 final draft 10 July 2026" is best read as an internal operational implementation framework, so its approval (and the 90-day mobilisation clock) depends on an internal sign-off, not a Cabinet event. No public date for that sign-off was found.
- **Most credible intro path (PIR-INIT-CSCDC-002):** Structurally, the **NACSA path** is the most credible — NACSA is the national lead agency, owns the cryptography mandate (MyKriptografi) that CSCDC's name maps onto, and is the statutory licensing authority under Act 854. The CSM path is viable for delivery/operational ties; the JPM path is the formal-political top. NACSA is the strongest single entry point.
- **Competitive landscape (PIR-INIT-CSCDC-010 / PIR-CSCDC-010):** CSM's current vendor base is technical cyber/IT resellers and cyber-consultancies; **no PR/strategic-comms agency is visible** in CSM's awarded procurement — suggesting the strategic communications framework space (CSCDC's apparent remit) is comparatively open, but this is an inference from absence, not confirmation.
- **PIR-INIT-CSCDC-003 (weekly 90-day milestones) and PIR-INIT-CSCDC-001 (in-mobilisation partnership authority):** No source found. These remain internal/undisclosed.

---

## PIR Resolution Status

| PIR ID | Priority | Question (short) | New Intel This Cycle? | Status |
|---|---|---|---|---|
| PIR-CSCDC-001 | CRITICAL | CEO / acting CCO / MKN-NACSA shepherds | PARTIAL | Chain structure corroborated (NACSA→MKN→JPM; DG NACSA = statutory authority). Named individuals NOT identified. |
| PIR-CSCDC-002 | CRITICAL | Framework v2.0 approval date / 90-day clock | PARTIAL | National crypto policy already approved 28 Nov 2025; v2.0 reframed as internal operational framework. Approval date NOT found. |
| PIR-INIT-CSCDC-001 | CRITICAL | External-partnership approval authority in mobilisation | NO | Not resolved. Inference: terminates at/through DG NACSA under Act 854. |
| PIR-INIT-CSCDC-002 | CRITICAL | Most credible intro path (CSM/NACSA/JPM) | PARTIAL | Structurally, NACSA path assessed most credible (national lead agency, crypto mandate owner, statutory licensing authority). |
| PIR-INIT-CSCDC-003 | CRITICAL | Weekly milestones in 90-day mobilisation plan | NO | Not resolved — no public source found. |
| PIR-CSCDC-004 | HIGH | CCO appointment status (advertised/shortlisted/filled) | NO | CSM career portal inaccessible to scraper; no other source. |
| PIR-CSCDC-010 | HIGH | Existing PR/consultants/vendors engaged | PARTIAL | CSM procurement vendor register extracted (technical/IT/cyber-consultancy vendors); no PR/comms vendor visible. |
| PIR-INIT-CSCDC-010 | HIGH | Competitive landscape — vendors currently engaged | PARTIAL | Current CSM vendors listed (Sangfor, Dell, Elastic, HCL, Microsoft, DPTech, USM Anywhere, etc.); comms/PR gap noted. |
| PIR-OPP010-001 | HIGH | PTPKM↔CSM operational integration status | NO | No merged-entity procurement or integration announcement found on any portal. |

**Summary:** 4 of 9 PIRs advanced partially via authoritative-source extraction (context/structure + CSM vendor landscape). 5 of 9 PIRs unresolved this cycle due to (a) degraded web_search backend and (b) CSCDC/PTPKM not being publicly disclosed on any .gov.my portal as of 26 July 2026. No fabricated data was introduced; all sourced facts are [VERIFIED] from .gov.my domains; inferences are marked [UNVERIFIED].

---

## Recommended Next-Cycle Actions

1. **Re-attempt search backend** — the degraded web_search behaviour may be transient; retry the 8 queries next cycle and add a `site:gov.my` and `site:com.my`-style restriction if the backend supports it.
2. **Targeted sub-page extraction** — extract NACSA news/announcement index and CyberSecurity Malaysia "About/Leadership" and "Media/News" pages directly (bypassing search), and retry the CSM career portal (PIR-CSCDC-004).
3. **Monitor CSM procurement portal weekly** for any new Tender (>RM500k) that could correspond to the CSCDC RM4,005,000 Phase 1 budget — this is the earliest likely public signal of CSCDC mobilisation.
4. **Monitor NACSA MyKriptografi page** for implementation-body announcements (CSCDC may be publicly named as MyKriptografi's delivery arm before the "CSCDC" label itself surfaces).
5. **Flag the search-backend degradation** to the platform operator — it is materially impairing OSINT collection on Malaysia-specific proper nouns.
