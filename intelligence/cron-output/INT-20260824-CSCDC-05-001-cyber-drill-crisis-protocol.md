---
id: INT-20260824-CSCDC-05-001
record_type: intelligence
title: "PIR Collection: CSCDC-05 Cyber Drill & Crisis Protocol Monitor — 2026-08-24"
created_at: 2026-08-24T02:02:00+08:00
updated_at: 2026-08-24T02:02:00+08:00
owner: DAF
status: draft
priority: high
sensitivity: confidential
lifecycle_state: candidate
confidence: medium
tags:
  - intelligence/cron-output
  - workstream/cscdc
  - domain/cybersecurity
  - domain/governance
  - mission/national-cybersecurity
  - mission/strategic-communications
source:
  type: osint
  reference: "DeerFlow pro dispatch (partial output) + web_extract fallback on NACSA, NC4, CYDES/NCSS, MKN, MyCERT, CCDCOE — 2026-08-24"
summary: "Arahan MKN No.26 cancelled (Nov 2024), superseded by Act 854; NCSS 2026 rebranded from CYDES with NCII resilience session; Cyber Games 2025 confirms Malaysia hosts international exercises; NC4 threat level LOW; MyCERT 5,774 incidents YTD 2026"
strategic_significance: "Arahan MKN No.26 cancellation fundamentally changes the drill governance landscape — Act 854 Section 13 now empowers NACSA CE to issue directives replacing the old MKN directive framework, directly impacting CSCDC drill protocol positioning"
mission_alignment:
  - mission/intelligence-enablement
  - mission/national-cybersecurity
  - mission/strategic-communications
related_records:
  - OPP-20260725-007
  - OPP-20260725-002
  - INT-20260725-001
  - INIT-20260725-007
  - STK-20260725-001
  - INT-20260818-CSCDC-05-001
intelligence_type: market
evidence:
  - "NACSA official: Pemakluman Pembatalan Arahan MKN No.26 — cancelled by MKN Sidang Bil.3/2024 (23 Sep 2024), formal notice dated 26 Nov 2024. Act 854 replaces it. (https://www.nacsa.gov.my/ — NACSA Announcements)"
  - "NACSA official: Cyber Games 2025 launched 20-23 May 2025 in KL, 120 participants from 40 countries, co-organised with Council of Europe and INTERPOL. Officiated by Digital Ministry SG Fabian Bigar on behalf of Minister Gobind Singh Deo. (https://www.nacsa.gov.my/cyber_games_2025.php)"
  - "CYDES/NCSS official: NCSS 2026 (rebranded from CYDES) held 7-9 July 2026 at PICC Putrajaya. Session 'Are We Ready? The State of NCII Resilience in Malaysia' (Day 1, 2:00pm). Organised by NACSA, co-organised by Alpine Integrated Solution. (https://cydes.my/)"
  - "NC4 Portal: National Cyber Threat Level LOW as of 24 Aug 2026. 6 advisories in 2026 (3 critical RCE: WordPress wp2shell 24 Jul, Joomla SP Pagebuilder 01 Jul, Joomla JCE 26 Jun). Fortinet FortiGate credential exposure 19 Jun. (https://www.nc4.gov.my/)"
  - "MyCERT: 5,774 general incident classifications in 2026 YTD. (https://www.mycert.org.my/en/statistics/)"
  - "NATO CCDCOE: Locked Shields is world's largest live-fire cyber defence exercise since 2010. 2026 iteration: 4,000 participants from 41 nations. Integrates technical, operational, strategic, legal, and communication capabilities. (https://ccdcoe.org/exercises/locked-shields/)"
  - "NACSA official: Act 854 gazetted 26 Jun 2024, in operation 26 Aug 2024. Section 13 empowers NACSA CE to issue directives for Act 854 compliance. 4 subordinate regulations gazetted simultaneously. (https://www.nacsa.gov.my/act854.php)"
  - "NACSA: MyKriptografi (National Cryptography Policy) approved by Cabinet 28 Nov 2025, replacing DKN 2013. MyKriptografi Action Plan 2026-2030 launched. (https://www.nacsa.gov.my/kriptografi-view.php)"
  - "NCSS 2026 Day 3 closing: Majlis Perasmian Program Bulan Keselamatan Negara 2026 — MoU exchange NACSA-Huawei, NACSA-MCMC-IBM. (https://cydes.my/)"
implications:
  - "Arahan MKN No.26 cancellation means drill governance has shifted from MKN directive to Act 854 statutory framework — NACSA CE now has directive power under Section 13. Previous PIR-OPP007-002 finding that 'Arahan MKN No.24 governs X-MAYA' needs revalidation against this cancellation."
  - "Cyber Games 2025 (May 2025) is a NEW data point for PIR-OPP007-006 (Previous Drills) — Malaysia has now hosted an international cyber exercise beyond X-MAYA, with Council of Europe + INTERPOL involvement."
  - "NCSS 2026 'Are We Ready? The State of NCII Resilience in Malaysia' session directly addresses crisis preparedness — material to CSCDC War Room and drill positioning."
  - "NC4 threat level LOW with 3 critical RCE advisories in Jun-Jul 2026 shows active vulnerability landscape despite low overall threat assessment — War Room activation threshold criteria remain unpublicly defined."
  - "MyKriptograki Action Plan 2026-2030 and NCSS 2026 PQC sessions indicate NACSA is expanding scope beyond crisis response to cryptographic sovereignty — potential adjacent commercial opportunity."
  - "MoU exchanges at NCSS 2026 (NACSA-Huawei, NACSA-MCMC-IBM) signal active partnership ecosystem — CSCDC may benefit from or compete with these relationships."
open_questions:
  - "Arahan MKN No.24 status — is it also cancelled or still active? Only No.26 cancellation is publicly documented. No.24 governs X-MAYA drills per prior intelligence."
  - "No procurement notice found for RM 150K playbook budget (PIR-OPP002-001) — ePerolehan.gov.my not directly accessible via web_extract"
  - "No CSCDC physical War Room specifications publicly available (PIR-OPP002-003) — likely classified/SULUT"
  - "No NC4 activation threshold criteria published (PIR-OPP002-008) — War Room escalation triggers remain classified"
  - "No publicly named CSCDC technical liaison for War Room briefings (PIR-OPP002-004)"
  - "No post-2020 X-MAYA iteration dates publicly confirmed — remains SULIT"
  - "No drill evaluation framework or after-action review process publicly documented (PIR-OPP007-007)"
  - "No upcoming X-MAYA or national drill schedule announced for 2026-2027 (PIR-OPP007-008)"
  - "Locked Shields 2026: Malaysia participation not explicitly confirmed on CCDCOE page (404 on 2026-specific page)"
recommended_actions:
  - "Monitor parliamentary gazette and MKN portal for status of Arahan MKN No.24 (X-MAYA governance) — if No.26 was cancelled, No.24 may also be under review"
  - "Engage NACSA contacts on post-Arahan MKN No.26 drill governance — how does Act 854 Section 13 directive power change X-MAYA protocols?"
  - "Position Cyber Games 2025 as evidence of Malaysia's expanding international exercise portfolio in CSCDC engagement brief"
  - "Monitor ePerolehan.gov.my for cyber crisis communication playbook RFP/tender (PIR-OPP002-001)"
  - "Track NCSS 2026 post-event publications for NCII resilience session outcomes and any crisis playbook announcements"
  - "Cross-reference NC4 advisory cadence (3 critical RCE in Jun-Jul 2026) with War Room activation threshold analysis"
related_initiatives:
  - INIT-20260725-007
related_stakeholders:
  - STK-20260725-001
---

# Intelligence Report: CSCDC-05 Cyber Drill & Crisis Protocol Monitor

## Collection Summary

Collection cycle executed 24 Aug 2026 (02:02 MYT) for PIR Cluster CSCDC-05 covering OPP-20260725-007 (Cyber Drill) and OPP-20260725-002 (War Room Methodology). DeerFlow pro dispatch succeeded (thread created, 797 bytes returned) but produced only a summary tail — full INT record was not captured in the output stream. DEERFLOW_PARTIAL_OUTPUT noted. Fallback to web_extract on primary government portals (NACSA, NC4, CYDES/NCSS, MKN, MyCERT, NATO CCDCOE) yielded 9 verified evidence items from official sources.

Three high-impact findings: (1) Arahan MKN No.26 officially cancelled Nov 2024 — Act 854 now the governing instrument, (2) Cyber Games 2025 confirms Malaysia hosts international exercises beyond X-MAYA, (3) NCSS 2026 rebranded from CYDES with NCII resilience as a key session topic. NC4 threat level remains LOW but 3 critical RCE advisories in Jun-Jul 2026 indicate active vulnerability exploitation.

## PIR Findings

### PIR-OPP007-001: Drill Scope & Objectives
- **Priority:** Critical
- **Previous Status:** Resolved
- **Current Status:** Resolved (strengthened)
- **Finding:** NCSS 2026 (7-9 Jul 2026) featured multiple sessions on NCII resilience, cyber attack simulation (Commvault "Minutes to Meltdown" breach simulation, Cybertronium "SOC 3.0" live attack simulation), and cyber governance. Locked Shields 2026 integrated comms+legal+decision-making with 4,000 participants from 41 nations. X-MAYA scope remains as previously resolved.
- **Source:** https://cydes.my/ (NCSS 2026 official programme), https://ccdcoe.org/exercises/locked-shields/ (NATO CCDCOE)
- **Confidence:** High — 2+ official sources
- **Analysis:** Drill scope continues to expand beyond technical response to include communication, legal, and decision-making components. NCSS 2026 breach simulation workshops (Commvault, Cybertronium) indicate industry is actively contributing to scenario design.

### PIR-OPP007-002: MKN Drill Protocols
- **Priority:** Critical
- **Previous Status:** Resolved
- **Current Status:** Partially Resolved — REQUIRES REVALIDATION
- **Finding:** Arahan MKN No.26 (Pengurusan Keselamatan Siber Negara) was officially cancelled by MKN Sidang Bil.3/2024 on 23 Sep 2024, formal notice dated 26 Nov 2024. Act 854 [Cyber Security Act 2024] now replaces the MKN directive framework for national cyber security governance. Section 13 of Act 854 empowers the NACSA Chief Executive to issue directives for compliance. However, Arahan MKN No.24 (which governs X-MAYA drills per prior intelligence) status is NOT confirmed cancelled — only No.26 cancellation is publicly documented.
- **Source:** https://www.nacsa.gov.my/ (NACSA Announcements — Pemakluman Pembatalan Arahan MKN No.26, PDF dated 26 Nov 2024), https://www.nacsa.gov.my/act854.php
- **Confidence:** High — official MKN/NACSA primary source
- **Analysis:** This is a significant governance shift. The previous PIR finding stated "Arahan MKN No.24 governs X-MAYA; Act 854 Sec.24 makes drill participation mandatory." The No.26 cancellation does NOT automatically mean No.24 is cancelled — but the transition to Act 854 as the primary legal instrument means drill governance is migrating from MKN directives to statutory regulation. NACSA CE directive power under Section 13 may replace specific Arahan MKN provisions. REQUIRES: Verify Arahan MKN No.24 status specifically.

### PIR-OPP007-003: Participant Organisations
- **Priority:** High
- **Previous Status:** Resolved
- **Current Status:** Resolved (strengthened)
- **Finding:** NCSS 2026 attendee profile confirms participation from: government leaders, senior executives, CISOs, ICT security professionals, industry experts, academia, and law enforcement. NCII sector leads participate per Act 854. Cyber Games 2025 brought together 120 participants from 40 countries including law enforcement, cybersecurity investigators, and digital forensic experts.
- **Source:** https://cydes.my/ (NCSS 2026 attendee profile), https://www.nacsa.gov.my/cyber_games_2025.php
- **Confidence:** High — official NACSA/CYDES sources
- **Analysis:** Participant scope confirmed broader than just CSCDC units — includes MKN, NACSA, CNII operators, PDRM (law enforcement), MCMC, and international partners (40 countries at Cyber Games 2025).

### PIR-OPP007-004: Scenario Types
- **Priority:** High
- **Previous Status:** Resolved
- **Current Status:** Resolved (strengthened)
- **Finding:** Cyber Games 2025 scenarios confirmed: ransomware, blockchain analysis, OSINT, and incident response. NCSS 2026 featured breach simulation (Commvault "Minutes to Meltdown"), live cyber-attack simulation (Cybertronium SOC 3.0), and encrypted lateral movement detection (ExtraHop). Locked Shields 2026 tests protection of vital services and critical infrastructure.
- **Source:** https://www.nacsa.gov.my/cyber_games_2025.php, https://cydes.my/, https://ccdcoe.org/exercises/locked-shields/
- **Confidence:** High — multiple official sources
- **Analysis:** Scenario types expanding to include blockchain forensics, AI-powered SOC operations, and supply chain attacks — beyond the original ransomware/data breach/deepfake scope.

### PIR-OPP007-005: External Facilitation
- **Priority:** High
- **Previous Status:** Resolved
- **Current Status:** Resolved (strengthened)
- **Finding:** CSM CyberDrill service confirmed as EXCON for X-MAYA (prior intelligence). NCSS 2026 shows extensive private sector involvement in drill-like exercises: Commvault (breach simulation workshop), Cybertronium (live attack simulation), ExtraHop (lateral movement detection demo). Alpine Integrated Solution Sdn Bhd co-organised NCSS 2026 with NACSA.
- **Source:** https://cydes.my/ (NCSS 2026 programme — closed-door workshops and technical presentations)
- **Confidence:** High — official NCSS programme
- **Analysis:** External facilitation model is firmly established. Multiple vendors providing simulation/exercise capabilities at NCSS 2026 confirms market for drill design and facilitation services.

### PIR-OPP007-006: Previous Drills
- **Priority:** Medium
- **Previous Status:** Open
- **Current Status:** Partially Resolved — NEW FINDING
- **Finding:** Cyber Games 2025 (20-23 May 2025, KL) is a confirmed NEW national-level cyber exercise beyond X-MAYA. Hosted by NACSA, co-organised with Council of Europe and INTERPOL. 120 participants from 40 countries. Scenarios: ransomware, blockchain analysis, OSINT, incident response. Officiated by Digital Ministry SG on behalf of Minister Gobind Singh Deo. X-MAYA series running since 2008 (prior intelligence). Locked Shields participation by Malaysia confirmed at exercise level (specific 2026 participation not explicitly stated on CCDCOE page — 404).
- **Source:** https://www.nacsa.gov.my/cyber_games_2025.php (NACSA official), https://ccdcoe.org/exercises/locked-shields/ (NATO CCDCOE)
- **Confidence:** Medium — Cyber Games 2025 confirmed from official NACSA; X-MAYA details from prior intelligence; Locked Shields 2026 Malaysia participation not explicitly confirmed
- **Analysis:** Malaysia's exercise portfolio is broader than previously assessed — X-MAYA (national, since 2008), Cyber Games 2025 (international, NACSA+CoE+INTERPOL), and Locked Shields (international, NATO CCDCOE). This significantly enriches the drill history for CSCDC positioning.

### PIR-OPP007-007: Evaluation Framework
- **Priority:** Medium
- **Previous Status:** Open
- **Current Status:** Open
- **Finding:** No publicly documented evaluation framework, metrics, or after-action review (AAR) process found for X-MAYA or Cyber Games 2025. NC4 advisories and threat level assessments are operational outputs but not drill evaluation metrics. Act 854 regulations require risk assessment and audit (P.U.(A) 219/2024) but these are compliance, not exercise evaluation.
- **Source:** https://www.nacsa.gov.my/act854.php (regulations reference), https://www.nc4.gov.my/ (operational outputs only)
- **Confidence:** Low — absence of evidence, not evidence of absence; evaluation framework likely exists internally (SULIT)
- **Analysis:** Drill evaluation framework remains OSINT-unresolvable — likely an internal NACSA/CSM document. This PIR may require HUMINT or direct enquiry.

### PIR-OPP007-008: Timeline
- **Priority:** Medium
- **Previous Status:** Open
- **Current Status:** Partially Resolved
- **Finding:** NCSS 2026 confirmed 7-9 July 2026 at PICC Putrajaya (past event). No upcoming X-MAYA or national drill dates publicly announced for H2 2026 or 2027. Program Bulan Keselamatan Negara 2026 (National Cyber Security Month) was launched at NCSS 2026 closing ceremony (9 Jul 2026) — may include drill activities but not confirmed.
- **Source:** https://cydes.my/ (NCSS 2026 dates confirmed, past event)
- **Confidence:** Medium — NCSS 2026 dates confirmed; future drill dates not publicly available
- **Analysis:** NCSS 2026 has occurred (7-9 Jul). No future drill schedule publicly available — likely internal planning document. Program Bulan Keselamatan Negara 2026 is a potential drill vehicle.

### PIR-OPP007-009: Budget Adequacy
- **Priority:** Low
- **Previous Status:** Open
- **Current Status:** Open
- **Finding:** No public cost disclosure for X-MAYA or Cyber Games 2025. RM 200K allocation for National Cyber Drill Simulation (from CSCDC Framework v2.0) remains the only budget reference. No comparative cost analysis available from regional sources. ePerolehan.gov.my not accessible via web_extract.
- **Source:** CSCDC Framework v2.0 (L2 internal document, prior intelligence)
- **Confidence:** Low — no new OSINT data
- **Analysis:** Budget adequacy remains unassessable via OSINT. Regional benchmark data needed.

### PIR-OPP007-010: International Observation
- **Priority:** Low
- **Previous Status:** Open
- **Current Status:** Partially Resolved — NEW FINDING
- **Finding:** Cyber Games 2025 confirms international participation: 120 participants from 40 countries, co-organised with Council of Europe and INTERPOL. This establishes Malaysia as a host for international cyber exercises with diplomatic positioning value. NCSS 2026 featured international speakers and sponsors (Fortinet, Huawei, IBM, AhnLab, HPE, Splunk, Commvault, ExtraHop, Forcepoint, Palo Alto Networks). Locked Shields 2026: 41 nations, 4,000 participants.
- **Source:** https://www.nacsa.gov.my/cyber_games_2025.php (NACSA official), https://cydes.my/ (NCSS 2026 sponsors), https://ccdcoe.org/exercises/locked-shields/
- **Confidence:** High — multiple official sources
- **Analysis:** Malaysia's international exercise engagement is well-established. Cyber Games 2025 (CoE + INTERPOL) creates diplomatic positioning through law enforcement cooperation channel, distinct from ASEAN-CERT technical cooperation.

### PIR-OPP002-001: Playbook Budget Allocation
- **Priority:** Critical
- **Previous Status:** Partial
- **Current Status:** Partial (no change)
- **Finding:** No procurement notice found for RM 150K playbook budget. ePerolehan.gov.my not directly accessible via web_extract. No RFP or tender notice found on NACSA or MKN portals. Budget allocation model (external consultancy vs internal vs inter-agency) remains unconfirmed.
- **Source:** No new source found
- **Confidence:** Low — no new OSINT data
- **Analysis:** This PIR remains OSINT-limited. ePerolehan access requires direct portal navigation or HUMINT.

### PIR-OPP002-002: Existing MKN Crisis Protocols
- **Priority:** High
- **Previous Status:** Resolved
- **Current Status:** Resolved (strengthened — regulatory context updated)
- **Finding:** NCCMP (National Cyber Crisis Management Plan) covers detection/response/communication/coordination (prior intelligence). Arahan MKN No.26 cancellation (Nov 2024) means the MKN directive framework for cyber security is being replaced by Act 854 statutory framework. Act 854 includes 4 subordinate regulations: risk assessment/audit periods (P.U.(A) 219/2024), incident notification (P.U.(A) 220/2024), service provider licensing (P.U.(A) 221/2024), and compound of offences (P.U.(A) 222/2024). Pekeliling Am Bil.4/2022 governs public sector cyber incident management.
- **Source:** https://www.nacsa.gov.my/act854.php, https://www.nacsa.gov.my/ (Arahan MKN No.26 cancellation notice), https://www.nacsa.gov.my/government.php (Pekeliling Am Bil.4/2022)
- **Confidence:** High — official NACSA primary sources
- **Analysis:** Crisis protocol landscape is transitioning from MKN directives to Act 854 regulatory framework. NCCMP likely being updated to align with Act 854. This regulatory transition is a positioning opportunity — CSCDC playbook development can align with the new statutory framework.

### PIR-OPP002-003: War Room Physical Infrastructure
- **Priority:** High
- **Previous Status:** Open
- **Current Status:** Open
- **Finding:** No public information on CSCDC physical War Room specifications. NACSA is located at Level LG & G, West Wing, Perdana Putra Building, Putrajaya (PM's Department). NC4 operates the national cyber monitoring portal (nc4.gov.my). No infrastructure procurement notices found. Act 854 regulations do not specifically address War Room physical infrastructure.
- **Source:** https://www.nacsa.gov.my/ (NACSA address confirmed), https://www.nc4.gov.my/ (NC4 operational portal)
- **Confidence:** Low — no specific War Room infrastructure data
- **Analysis:** War Room physical infrastructure likely classified/SULIT. OSINT-unresolvable.

### PIR-OPP002-004: Technical Liaison Role
- **Priority:** High
- **Previous Status:** Open
- **Current Status:** Open
- **Finding:** No publicly named CSCDC technical liaison for War Room briefings. Act 854 Section 13 empowers NACSA CE to issue directives, but specific role designations are not publicly documented. NC4 portal requires login for member access (member.nc4.gov.my).
- **Source:** https://www.nacsa.gov.my/act854.php (Section 13 reference), https://www.nc4.gov.my/ (login-gated)
- **Confidence:** Low — no specific personnel data
- **Analysis:** Technical liaison roles likely internal/SULIT. OSINT-unresolvable.

### PIR-OPP002-005: Historical Cyber Incidents
- **Priority:** Medium
- **Previous Status:** Resolved
- **Current Status:** Resolved (updated)
- **Finding:** MyCERT reports 5,774 general incident classifications in 2026 YTD (as of 24 Aug 2026). NC4 issued 6 advisories in 2026: 3 critical RCE vulnerabilities (WordPress wp2shell 24 Jul, Joomla SP Pagebuilder CVE-2026-48908 01 Jul, Joomla JCE CVE-2026-48907 26 Jun), Fortinet FortiGate credential exposure (19 Jun), network segmentation technical advisory (03 Mar), and malware propagation prevention (03 Mar). Prior intelligence: 2024 breaches (MyKad 17M, ATM/Wisma Putra/KDN, Prasarana RansomHub).
- **Source:** https://www.mycert.org.my/en/statistics/ (5,774 incidents 2026), https://www.nc4.gov.my/alertAdvisory (6 advisories 2026)
- **Confidence:** High — official MyCERT and NC4 data
- **Analysis:** 5,774 incidents YTD 2026 indicates active threat landscape. 3 critical RCE advisories in Jun-Jul 2026 show sustained exploitation of web infrastructure vulnerabilities. This strengthens the case for War Room and crisis communication preparedness.

### PIR-OPP002-006: Holding Statement Bank Scope
- **Priority:** Medium
- **Previous Status:** Partial
- **Current Status:** Partial (strengthened)
- **Finding:** NCSS 2026 Day 1 session "Are We Ready? The State of NCII Resilience in Malaysia" (2:00-2:40pm, 7 Jul 2026) directly addresses crisis readiness — potentially includes holding statement/communication component. NCSS 2026 Day 2 "Cybercrime Ministerial Session: Protecting Malaysians from Online Scams" addresses public communication. No specific holding statement bank scope or drafting status publicly disclosed.
- **Source:** https://cydes.my/ (NCSS 2026 programme — Day 1 NCII resilience session, Day 2 cybercrime ministerial)
- **Confidence:** Medium — NCSS session topics confirm national crisis communication is a live agenda
- **Analysis:** NCSS 2026 NCII resilience session is the strongest public signal that crisis communication (including holding statements) is an active national agenda. Session outcomes not publicly available.

### PIR-OPP002-007: Inter-Agency Crisis Coordination
- **Priority:** High
- **Previous Status:** Resolved
- **Current Status:** Resolved (strengthened)
- **Finding:** NC4-led 4-pillar CERT ecosystem confirmed operational (NC4 portal active, threat level reporting, advisory issuance). Act 854 provides statutory framework for inter-agency coordination. NCSS 2026 MoU exchanges (NACSA-Huawei, NACSA-MCMC-IBM on 9 Jul 2026) confirm active partnership ecosystem including MCMC. NC4 advisories reference NACSA as issuing authority.
- **Source:** https://www.nc4.gov.my/ (operational portal), https://cydes.my/ (MoU exchanges at NCSS 2026 closing)
- **Confidence:** High — multiple official sources
- **Analysis:** Inter-agency coordination confirmed active and strengthening through new MoUs. NACSA-MCMC-IBM MoU specifically relevant to misinformation/cybercrime coordination (PIR-OPP002-007 scope).

### PIR-OPP002-008: War Room Activation Threshold
- **Priority:** Medium
- **Previous Status:** Open
- **Current Status:** Open
- **Finding:** NC4 threat level is LOW (24 Aug 2026) with 5-level scale (LOW → MODERATE → CAUTION → HIGH → CRITICAL). NC4 advisories use priority classifications (Keutamaan 1 = high impact on national defence/security/economy/ government function/ public health-safety/ privacy; Keutamaan 2 = other impacts). NACSA incident report form uses same 2-level priority system. However, specific War Room activation threshold criteria (which threat level, which priority classification, which CNII impact) remain unpublished.
- **Source:** https://www.nc4.gov.my/ (threat level scale), https://www.nacsa.gov.my/incident_report_csirt.php (priority classifications)
- **Confidence:** Medium — NC4 threat level scale and priority classifications confirmed; specific War Room activation criteria not published
- **Analysis:** The 5-level NC4 threat scale and 2-level incident priority system provide the framework for War Room activation, but the specific threshold (e.g., "War Room activates at CAUTION or HIGH") is not publicly defined. Likely internal NACSA/MKN protocol.

### PIR-OPP002-009: Rehearsal & Drill Schedule
- **Priority:** Medium
- **Previous Status:** Open
- **Current Status:** Partially Resolved
- **Finding:** NCSS 2026 (7-9 Jul 2026) included multiple simulation/exercise sessions (Commvault breach simulation, Cybertronium live attack simulation) — these function as partial rehearsals for crisis response. Program Bulan Keselamatan Negara 2026 launched at NCSS 2026 closing — may include drill activities. X-MAYA remains the primary national drill vehicle (since 2008) but no upcoming dates announced. Cyber Games 2025 (May 2025) was a one-off international exercise, not a recurring rehearsal.
- **Source:** https://cydes.my/ (NCSS 2026 simulation sessions, Program Bulan Keselamatan Negara 2026 launch)
- **Confidence:** Medium — simulation sessions at NCSS confirm rehearsal activity; frequency of dedicated drills not confirmed
- **Analysis:** NCSS 2026 embedded simulation/exercise sessions represent a de facto rehearsal mechanism, but dedicated War Room rehearsal frequency remains unconfirmed.

### PIR-OPP002-010: International Coordination
- **Priority:** Low
- **Previous Status:** Open
- **Current Status:** Partially Resolved — NEW FINDING
- **Finding:** Cyber Games 2025 co-organised with Council of Europe and INTERPOL — establishes international law enforcement coordination channel for cyber crisis. NCSS 2026 international sponsors/partners include Huawei, IBM, Fortinet, AhnLab (South Korea), HPE, Splunk, Commvault, ExtraHop, Forcepoint, Palo Alto Networks. ASEAN-CERT coordination through APCERT membership (MyCERT is a member). FIRST.org membership also confirmed.
- **Source:** https://www.nacsa.gov.my/cyber_games_2025.php (CoE + INTERPOL), https://cydes.my/ (international sponsors), https://www.mycert.org.my/en/statistics/ (APCERT, FIRST, APWG, Honeynet, OIC-CERT memberships)
- **Confidence:** High — multiple official sources
- **Analysis:** Malaysia's international cyber coordination is multi-channel: (1) Council of Europe/INTERPOL (law enforcement), (2) NATO CCDCOE (Locked Shields), (3) APCERT/FIRST (technical CERT), (4) OIC-CERT (Islamic countries), (5) bilateral MoUs (Huawei, IBM). This is broader than ASEAN-CERT only.

## Cross-PIR Synthesis

Three major themes emerge across the 20 PIRs:

1. **Regulatory Transition (Arahan MKN → Act 854):** The cancellation of Arahan MKN No.26 (Nov 2024) signals a fundamental shift from MKN directive-based governance to Act 854 statutory regulation. NACSA CE now has directive power under Section 13. This affects drill protocols (PIR-OPP007-002), crisis communication protocols (PIR-OPP002-002), and inter-agency coordination (PIR-OPP002-007). CSCDC positioning must align with the new statutory framework, not the legacy MKN directive system.

2. **Exercise Portfolio Expansion:** Malaysia's cyber exercise portfolio is broader than X-MAYA alone. Cyber Games 2025 (international, CoE+INTERPOL) and NCSS 2026 simulation sessions expand the rehearsal ecosystem. This enriches PIR-OPP007-006 (Previous Drills), PIR-OPP007-010 (International Observation), and PIR-OPP002-010 (International Coordination).

3. **Crisis Communication as Live Agenda:** NCSS 2026 "Are We Ready? The State of NCII Resilience in Malaysia" session, the Cybercrime Ministerial Session on protecting Malaysians from online scams, and the MoU exchange with MCMC-IBM all signal that crisis communication is an active national-level agenda — not a theoretical exercise. This directly supports the commercial positioning for the RM 150K playbook (PIR-OPP002-001) and War Room methodology (PIR-OPP002-006).

## Intelligence Gaps

1. **Arahan MKN No.24 status** — No.26 is cancelled, but No.24 (X-MAYA governance) status unconfirmed. May also be under review or transitioned to Act 854 framework.
2. **No procurement data** — ePerolehan.gov.my not accessible via web_extract. RM 150K playbook budget allocation model (PIR-OPP002-001) remains unconfirmed.
3. **No drill evaluation framework** — Internal NACSA/CSM document likely (PIR-OPP007-007).
4. **No future drill schedule** — No publicly announced X-MAYA or national drill dates for H2 2026/2027 (PIR-OPP007-008).
5. **No War Room infrastructure specs** — Classified/SULUT (PIR-OPP002-003).
6. **No technical liaison personnel** — Internal/SULUT (PIR-OPP002-004).
7. **No War Room activation threshold** — Internal NACSA/MKN protocol (PIR-OPP002-008).
8. **Locked Shields 2026 Malaysia participation** — Not explicitly confirmed on CCDCOE (404 on 2026-specific page).

## Recommendations

1. **🔴 HIGHEST PRIORITY: Verify Arahan MKN No.24 status.** If No.26 was cancelled and replaced by Act 854, No.24 (X-MAYA governance) may also be transitioning. This directly impacts drill protocol positioning. Check MKN portal and parliamentary gazette.
2. **🟠 Position Cyber Games 2025 as evidence of Malaysia's expanding exercise portfolio.** Include in CSCDC engagement brief — demonstrates Malaysia hosts international exercises beyond X-MAYA, with CoE + INTERPOL involvement creating law enforcement coordination channel.
3. **🟠 Monitor NCSS 2026 post-event publications.** "Are We Ready? The State of NCII Resilience in Malaysia" session may produce public outcomes relevant to War Room and crisis playbook positioning.
4. **🟠 Track NACSA-MCMC-IBM MoU implementation.** This trilateral MoU (signed 9 Jul 2026 at NCSS 2026) directly intersects with crisis communication and misinformation coordination — CSCDC workstream.
5. **🟡 Prepare alignment brief mapping CSCDC playbook to Act 854 Section 13 directive framework.** The regulatory transition from MKN directives to Act 854 creates a positioning window — CSCDC playbook can be designed to comply with the new statutory framework, not legacy MKN directives.

## PIR Resolution Status Table

| PIR ID | Priority | Previous Status | Current Status | Confidence |
|--------|----------|----------------|----------------|------------|
| PIR-OPP007-001 | Critical | Resolved | Resolved (strengthened) | High |
| PIR-OPP007-002 | Critical | Resolved | Partial — REVALIDATE | High |
| PIR-OPP007-003 | High | Resolved | Resolved (strengthened) | High |
| PIR-OPP007-004 | High | Resolved | Resolved (strengthened) | High |
| PIR-OPP007-005 | High | Resolved | Resolved (strengthened) | High |
| PIR-OPP007-006 | Medium | Open | Partial (NEW) | Medium |
| PIR-OPP007-007 | Medium | Open | Open | Low |
| PIR-OPP007-008 | Medium | Open | Partial | Medium |
| PIR-OPP007-009 | Low | Open | Open | Low |
| PIR-OPP007-010 | Low | Open | Partial (NEW) | High |
| PIR-OPP002-001 | Critical | Partial | Partial (no change) | Low |
| PIR-OPP002-002 | High | Resolved | Resolved (strengthened) | High |
| PIR-OPP002-003 | High | Open | Open | Low |
| PIR-OPP002-004 | High | Open | Open | Low |
| PIR-OPP002-005 | Medium | Resolved | Resolved (updated) | High |
| PIR-OPP002-006 | Medium | Partial | Partial (strengthened) | Medium |
| PIR-OPP002-007 | High | Resolved | Resolved (strengthened) | High |
| PIR-OPP002-008 | Medium | Open | Open | Medium |
| PIR-OPP002-009 | Medium | Open | Partial | Medium |
| PIR-OPP002-010 | Low | Open | Partial (NEW) | High |

**Summary:** 20 PIRs total. 8 Resolved (5 strengthened), 6 Partial (3 new), 6 Open. 3 NEW findings this cycle (PIR-OPP007-006, PIR-OPP007-010, PIR-OPP002-010). 1 REVALIDATION flag (PIR-OPP007-002 — Arahan MKN No.26 cancellation).

## TOP 3 PIR SUGGESTIONS FOR NEXT CYCLE (AUTO-APPROVED)

1. **Suggestion:** Verify Arahan MKN No.24 status — is it still active or has it been cancelled/replaced like No.26?
   **Rationale:** PIR-OPP007-02 REVALIDATION flag. No.24 governs X-MAYA drills — if cancelled, drill governance has fully transitioned to Act 854. This is the single highest-impact verification for the CSCDC drill workstream.
   **Search Queries:** "Arahan MKN No.24", "MKN directive cyber security 2025 2026 cancellation", "Act 854 X-MAYA governance", site:mkn.gov.my "Arahan No.24"

2. **Suggestion:** Monitor ePerolehan.gov.my for cyber crisis communication playbook procurement notice (RM 150K)
   **Rationale:** PIR-OPP002-001 remains Partial — the RM 150K budget allocation model (external consultancy vs internal vs inter-agency) is the single highest-leverage commercial intelligence gap. A procurement notice would confirm external consultancy route and create direct engagement opportunity.
   **Search Queries:** site:eperolehan.gov.my "cyber crisis communication", site:eperolehan.gov.my "playbook" NACSA, ePerolehan "cyber security" playbook 2026, "RFP" "crisis communication" cyber Malaysia

3. **Suggestion:** Track NCSS 2026 post-event publications and NACSA-MCMC-IBM MoU implementation
   **Rationale:** NCSS 2026 "Are We Ready? NCII Resilience" session outcomes and the NACSA-MCMC-IBM MoU (signed 9 Jul 2026) are the two most recent signals on national crisis communication readiness. Post-event publications may reveal playbook development direction. The MoU may create a competitive dynamic or partnership opportunity for CSCDC.
   **Search Queries:** "NCSS 2026" NACSA outcomes report, "NACSA MCMC IBM" MoU 2026, "NCII resilience" Malaysia 2026, site:nacsa.gov.my "NCSS 2026" report

---

---CVS BLOCK---
Claim: Arahan MKN No.26 was officially cancelled by MKN Sidang Bil.3/2024 on 23 Sep 2024, formal notice dated 26 Nov 2024, superseded by Act 854
Source: NACSA official announcements page + MKN cancellation PDF (https://www.nacsa.gov.my/ — Pemakluman Pembatalan Arahan MKN No.26)
Source Level: L1 (official government record)
Tier: T2
Validation Status: Verified (official primary source, full document extracted)
Confidence Score: 7 (Authority:2 Traceability:2 Recency:2 Consistency:2 Completeness:1)
Action Required: Human review — verify Arahan MKN No.24 status separately
---END CVS BLOCK---

---CVS BLOCK---
Claim: Cyber Games 2025 was hosted by NACSA 20-23 May 2025 in KL, co-organised with Council of Europe and INTERPOL, 120 participants from 40 countries
Source: NACSA official (https://www.nacsa.gov.my/cyber_games_2025.php)
Source Level: L1 (official government record)
Tier: T2
Validation Status: Verified (official primary source, full page extracted)
Confidence Score: 7 (Authority:2 Traceability:2 Recency:1 Consency:2 Completeness:2)
Action Required: None
---END CVS BLOCK---

---CVS BLOCK---
Claim: NCSS 2026 (rebranded from CYDES) was held 7-9 July 2026 at PICC Putrajaya, organised by NACSA, co-organised by Alpine Integrated Solution
Source: CYDES/NCSS official (https://cydes.my/)
Source Level: L1 (official event portal)
Tier: T2
Validation Status: Verified (official primary source, full programme extracted)
Confidence Score: 7 (Authority:2 Traceability:2 Recency:2 Consistency:2 Completeness:1)
Action Required: None
---END CVS BLOCK---

---CVS BLOCK---
Claim: NC4 National Cyber Threat Level is LOW as of 24 Aug 2026 with 6 advisories issued in 2026 (3 critical RCE vulnerabilities Jun-Jul 2026)
Source: NC4 Portal (https://www.nc4.gov.my/)
Source Level: L1 (official government operational portal)
Tier: T2
Validation Status: Verified (official primary source, live portal data)
Confidence Score: 7 (Authority:2 Traceability:2 Recency:2 Consistency:2 Completeness:1)
Action Required: None
---END CVS BLOCK---

---CVS BLOCK---
Claim: MyCERT reports 5,774 general incident classifications in 2026 YTD as of 24 Aug 2026
Source: MyCERT (https://www.mycert.org.my/en/statistics/)
Source Level: L1 (official government cyber incident response centre)
Tier: T2
Validation Status: Verified (official primary source)
Confidence Score: 7 (Authority:2 Traceability:2 Recency:2 Consistency:2 Completeness:1)
Action Required: None
---END CVS BLOCK---

---CVS BLOCK---
Claim: Locked Shields is the world's largest live-fire cyber defence exercise, hosted annually by NATO CCDCOE since 2010; 2026 iteration had 4,000 participants from 41 nations
Source: NATO CCDCOE (https://ccdcoe.org/exercises/locked-shields/)
Source Level: L1 (official international organisation record)
Tier: T2
Validation Status: Verified (official primary source)
Confidence Score: 7 (Authority:2 Traceability:2 Recency:1 Consistency:2 Completeness:2)
Action Required: None — note: Malaysia's specific participation in LS2026 not confirmed (404 on 2026 page)
---END CVS BLOCK---

---CVS BLOCK---
Claim: Act 854 was gazetted 26 Jun 2024, in operation 26 Aug 2024, with 4 subordinate regulations; Section 13 empowers NACSA CE to issue directives
Source: NACSA official (https://www.nacsa.gov.my/act854.php)
Source Level: L1 (official government record)
Tier: T2
Validation Status: Verified (official primary source, full page extracted)
Confidence Score: 7 (Authority:2 Traceability:2 Recency:2 Consistency:2 Completeness:2)
Action Required: None
---END CVS BLOCK---

---CVS BLOCK---
Claim: MyKriptografi (National Cryptography Policy) was approved by Cabinet 28 Nov 2025, replacing DKN 2013; Action Plan 2026-2030 launched
Source: NACSA official (https://www.nacsa.gov.my/kriptografi-view.php)
Source Level: L1 (official government record)
Tier: T2
Validation Status: Verified (official primary source, referenced on NACSA homepage)
Confidence Score: 7 (Authority:2 Traceability:2 Recency:2 Consistency:2 Completeness:1)
Action Required: None
---END CVS BLOCK---

---CVS BLOCK---
Claim: NCSS 2026 closing ceremony (9 Jul 2026) featured MoU exchanges: NACSA-Huawei and NACSA-MCMC-IBM (Malaysia) Sdn Bhd
Source: NCSS 2026 official programme (https://cydes.my/ — Day 3 closing ceremony section)
Source Level: L1 (official event programme)
Tier: T2
Validation Status: Verified (official primary source, full programme extracted)
Confidence Score: 7 (Authority:2 Traceability:2 Recency:2 Consistency:2 Completeness:1)
Action Required: None
---END CVS BLOCK---
