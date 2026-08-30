---
id: INT-20260831-CSCDC-05-001
record_type: intelligence
title: "PIR Collection: CSCDC-05 Cyber Drill & Crisis Protocol Monitor — 2026-08-31"
created_at: 2026-08-31T02:00:54+08:00
updated_at: 2026-08-31T02:00:54+08:00
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
  reference: "DeerFlow pro dispatch (summary output) + web_extract on NACSA, NC4, MyCERT, CYDES/NCSS, MKN, Arahan MKN No.26 PDF, NCII, NCCMP, AISCF, Act 854, licensing — 2026-08-31"
summary: "Arahan MKN No.24 status unverified but analytically assessed as likely still active; NACSA publishes new AISCF framework; NCII expanded to 11 sectors but NCCMP still references 10 domains (stale); NC4 threat level LOW unchanged since 24 Aug; no new NC4 advisories since 24 Jul; MyCERT 5,774 incidents unchanged; state-level NCII sector leads appointed 28 Jan 2025"
strategic_significance: "Arahan MKN No.24 likely-still-active assessment means X-MAYA drill governance is in a transition limbo — No.26 cancelled and replaced by Act 854, but No.24 (which specifically governs X-MAYA) has not been cancelled, creating a dual-framework period where both Act 854 statutory provisions and legacy MKN directive No.24 may apply simultaneously. NACSA's new AISCF and expanded NCII sectors signal institutional maturation but NCCMP staleness (10 vs 11 domains) indicates the crisis management plan has not been updated to match current NCII structure."
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
  - INT-20260824-CSCDC-05-001
  - INT-20260818-CSCDC-05-001
intelligence_type: market
evidence:
  - "NACSA official homepage — Arahan MKN No.26 cancellation notice prominently displayed; NO mention of Arahan MKN No.24 anywhere on site (Last Updated: 31 August 2026). (https://www.nacsa.gov.my/)"
  - "Arahan MKN No.26 cancellation PDF — full text extracted. Para 6: Act 854 'mengambil kira isu-isu penyelarasan termasuk isu tadbir urus yang dihadapi sebelum ini berpandukan kepada Arahan Majlis Keselamatan Negara No. 26' — only No.26 referenced. Signed by IR. DR. MEGAT ZUHAIRY BIN MEGAT TAJUDDIN, NACSA CE, dated 26 Nov 2024, ref MKN.600-2/1/6 (S)(53). (https://www.nacsa.gov.my/doc/PEMAKLUMAN%20PEMBATALAN%20ARAHAN%20MAJLIS%20KESELAMATAN%20NEGARA%20NO.26%20...pdf)"
  - "NC4 Portal — National Cyber Threat Level: LOW as of 31 Aug 2026 (last updated 31 Aug 2026 01 AM). Q3 2026 trends: attribution ▲ upward, vulnerable service ▲ upward. 6 advisories in 2026, latest 24 Jul 2026 (NC4-ALR-2026-000006 WordPress wp2shell). No new advisories between 24 Jul and 31 Aug (38-day gap). (https://www.nc4.gov.my/)"
  - "NC4 Advisory list — confirmed 6 advisories for 2026: NC4-ALR-2026-000001 (03 Mar, network segmentation), 000002 (19 Jun, Fortinet FortiGate), 000004 (26 Jun, Joomla JCE), 000005 (01 Jul, Joomla SP Pagebuilder), 000006 (24 Jul, WordPress wp2shell). (https://www.nc4.gov.my/alertAdvisory)"
  - "MyCERT — 5,774 general incident classifications for 2026 YTD. Unchanged since 24 Aug 2026 extraction. APCERT, FIRST, APWG, Honeynet, OIC-CERT memberships confirmed. (https://www.mycert.org.my/en/statistics/)"
  - "NACSA AISCF — AI Systems Cyber Security Framework published by NACSA. Covers data poisoning, prompt injection, adversarial attacks, model theft, AI supply chain compromise. Promotes Secure-by-Design, Defence-in-Depth, risk-based governance. NEW since prior cycle. (https://www.nacsa.gov.my/ai_systems_cyber_security_framework.php)"
  - "NACSA NCII page — 11 NCII sectors confirmed: (1) Government, (2) Banking and finance, (3) Transportation, (4) Defence and national security, (5) Information, communication and digital, (6) Healthcare services, (7) Water, sewerage and waste management, (8) Energy, (9) Agriculture and plantation, (10) Trade, industry and economy, (11) Science, technology and innovation. NCII sector leads appointed under Section 15(1) Act 854 effective 11 Sep 2024. State-level sector leads (Pejabat SUK Negeri) appointed effective 28 Jan 2025. (https://www.nacsa.gov.my/NCII.php)"
  - "NACSA NCCMP page — references 10 CNII domains (defence & security; banking & finance; info & comms; energy; transportation; water; health; government services; emergency services; food and agriculture) — uses old 'CNII' term, not current 'NCII'. Does NOT include 'Science, technology and innovation' as 11th sector. (https://www.nacsa.gov.my/nccmp.php)"
  - "NACSA Licensing — Act 854 cybersecurity service provider licensing active since 1 Oct 2024. Governing directive: 'Arahan Ketua Eksekutif NACSA No. 2' — a NACSA CE directive issued under Section 13 Act 854 powers. (https://www.nacsa.gov.my/application-licensing.php)"
  - "NACSA Government page — public sector circulars: Pekeliling Am Bil.4/2022 (cyber incident management), Pekeliling Am Bil.3/2024 (risk management guidelines, 21 Mar 2024), Pekeliling Am Bil.4/2024 (ICT security assessment, 21 Mar 2024). No new circulars since 2024. (https://www.nacsa.gov.my/government.php)"
  - "MKN portal landing page — no cybersecurity content visible. Mentions Arahan MKN No.1 as founding authority. COVID-19 legacy and GISB rehabilitation content only. (https://www.mkn.gov.my/)"
  - "DeerFlow pro dispatch — summary output (977 bytes). Analytical assessment: Arahan MKN No.24 'likely still active (no cancellation mechanism applied)'. MCSS 2025-2030 strategy document confirmed published. 5 open intelligence gaps confirmed. 83% extraction success rate. (Thread bd41a0d4, 2026-08-31)"
implications:
  - "Arahan MKN No.24 likely-still-active means X-MAYA drill governance operates under a dual framework: Act 854 (statutory, NACSA CE directives) + Arahan MKN No.24 (legacy MKN directive). CSCDC drill protocol positioning must acknowledge BOTH instruments — aligning with Act 854 while respecting any remaining No.24 provisions."
  - "NCCMP staleness (10 domains vs 11 NCII sectors) means the national crisis management plan has NOT been updated since Act 854 expanded the NCII from 10 to 11 sectors. The 11th sector (Science, technology and innovation) is not covered by NCCMP crisis procedures — a potential gap in crisis response coverage."
  - "NACSA AISCF publication signals NACSA is expanding its regulatory framework beyond traditional cybersecurity into AI systems security. This creates an adjacent capability area for CSCDC engagement — AI-driven crisis scenarios may require new drill types."
  - "38-day NC4 advisory gap (24 Jul to 31 Aug) may indicate reduced threat activity, reduced advisory publication capacity, or a shift in advisory prioritisation. The Q3 attribution ▲ and vulnerable service ▲ upward trends suggest the threat landscape is active despite LOW overall level."
  - "State-level NCII sector leads appointment (28 Jan 2025) extends Act 854 compliance to state government level — CSCDC drill scope may need to include state-level NCII entities."
  - "Arahan Ketua Eksekutif NACSA No. 2 (service provider licensing directive) confirms NACSA CE is actively exercising Section 13 directive powers — this governance model (NACSA CE directives replacing MKN directives) is now the operational norm."
open_questions:
  - "Arahan MKN No.24 status — analytically assessed as likely still active, but NO public cancellation notice or confirmation found. Requires HUMINT or direct MKN enquiry."
  - "No procurement notice for RM 150K playbook budget (PIR-OPP002-001) — ePerolehan.gov.my not accessible via web_extract. DeerFlow reported DNS failure."
  - "No CSCDC physical War Room specifications (PIR-OPP002-003) — likely classified/SULUT"
  - "No publicly named CSCDC technical liaison (PIR-OPP002-004) — internal/SULUT"
  - "No NC4 activation threshold criteria (PIR-OPP002-008) — War Room escalation triggers remain classified"
  - "No drill evaluation framework (PIR-OPP007-007) — likely internal NACSA/CSM document"
  - "No upcoming X-MAYA or national drill schedule announced (PIR-OPP007-008)"
  - "NCCMP update timeline — when will NCCMP be updated to align with Act 854's 11-sector NCII framework?"
  - "AISCF implementation status — is AISCF being integrated into drill scenarios and crisis communication playbooks?"
  - "NC4 advisory gap — 38 days since last advisory (24 Jul). Is this reduced threat activity or reduced publication capacity?"
recommended_actions:
  - "Engage NACSA/MKN contacts via classified channel to confirm Arahan MKN No.24 status — highest priority intelligence gap for drill governance positioning"
  - "Prepare CSCDC positioning brief acknowledging dual-framework period: Act 854 (statutory) + potential Arahan MKN No.24 (legacy directive) — show understanding of the governance transition complexity"
  - "Flag NCCMP staleness (10 vs 11 sectors) as a value-add observation in CSCDC engagement — crisis management plan not yet aligned with current NCII structure"
  - "Monitor AISCF implementation for integration into drill scenario design — AI-driven attack scenarios (data poisoning, prompt injection) may become new drill types"
  - "Track state-level NCII sector lead appointments (effective 28 Jan 2025) — state-level drill participation may be expanding"
  - "Continue monitoring ePerolehan.gov.my for playbook procurement notice (PIR-OPP002-001)"
related_initiatives:
  - INIT-20260725-007
related_stakeholders:
  - STK-20260725-001
---

# Intelligence Report: CSCDC-05 Cyber Drill & Crisis Protocol Monitor

## Collection Summary

Collection cycle executed 31 August 2026 (02:00 MYT) for PIR Cluster CSCDC-05 covering OPP-20260725-007 (Cyber Drill) and OPP-20260725-002 (War Room Methodology). Previous cycle: 24 August 2026 (7-day delta). DeerFlow pro dispatch succeeded (thread bd41a0d4, 977 bytes returned) but produced a summary-only output — the full INT record was not captured in the response stream (consistent with prior cycle pattern). Fallback to web_extract on 12 official government sources yielded 11 verified evidence items with full-page extraction.

Three significant findings this cycle: (1) Arahan MKN No.24 status — analytically assessed as likely still active (DeerFlow T3 assessment + corroborating absence of any cancellation notice on NACSA/MKN portals), creating a dual-framework governance period; (2) NACSA published new AISCF (AI Systems Cyber Security Framework) — a new regulatory instrument not present in prior cycle; (3) NCCMP staleness confirmed — NCCMP references 10 CNII domains while current NCII structure has 11 sectors, indicating the crisis management plan has not been updated to match Act 854's expanded framework. NC4 threat level remains LOW (unchanged since 24 Aug). No new NC4 advisories since 24 Jul 2026 (38-day gap).

## PIR Findings

### PIR-OPP007-001: Drill Scope & Objectives
- **Priority:** Critical
- **Previous Status:** Resolved (strengthened)
- **Current Status:** Resolved (strengthened — AISCF addition)
- **Finding:** NACSA has published the AI Systems Cyber Security Framework (AISCF), covering data poisoning, prompt injection, adversarial attacks, model theft, and AI supply chain compromise. This expands the potential drill scope to include AI-driven attack scenarios. NCSS 2026 simulation sessions (Commvault, Cybertronium, ExtraHop) and Locked Shields 2026 integration remain as previously resolved.
- **Source:** https://www.nacsa.gov.my/ai_systems_cyber_security_framework.php (NACSA official — AISCF page, Last Updated 31 Aug 2026)
- **Confidence:** High — official NACSA primary source
- **Analysis:** AISCF introduces AI-specific threat vectors into the cybersecurity framework. Drill scenarios may expand to include AI supply chain compromise and adversarial attack simulations. This is a natural extension of the breach simulation sessions seen at NCSS 2026.

### PIR-OPP007-002: MKN Drill Protocols
- **Priority:** Critical
- **Previous Status:** Partially Resolved — REQUIRES REVALIDATION
- **Current Status:** Partially Resolved — ANALYTICAL FINDING (T3)
- **Finding:** Full text of Arahan MKN No.26 cancellation PDF extracted and analysed. The document (dated 26 Nov 2024, signed by NACSA CE IR. Dr. Megat Zuhairy Megat Tajuddin, ref MKN.600-2/1/6 (S)(53)) specifically and only addresses the cancellation of No.26. Paragraph 6 explicitly states Act 854 "mengambil kira isu-isu penyelarasan termasuk isu tadbir urus yang dihadapi sebelum ini berpandukan kepada Arahan Majlis Keselamatan Negara No. 26" — only No.26 is referenced. **No mention of Arahan MKN No.24 appears anywhere**: not in the cancellation PDF, not on the NACSA homepage (31 Aug 2026), not on the MKN portal, not on the Act 854 page, not on the government circulars page. DeerFlow analytical assessment: No.24 "likely still active (no cancellation mechanism applied)."
- **Source:** https://www.nacsa.gov.my/doc/PEMAKLUMAN%20PEMBATALAN%20ARAHAN%20MAJLIS%20KESELAMATAN%20NEGARA%20NO.26%20...pdf (MKN official cancellation notice, full text extracted), https://www.nacsa.gov.my/ (NACSA homepage, 31 Aug 2026), https://www.mkn.gov.my/ (MKN portal), DeerFlow pro analytical output
- **Confidence:** Medium — [ASSESSMENT] analytical inference based on absence of evidence (no cancellation notice found across 4 government portals)
- **Analysis:** [ASSESSMENT] The absence of any cancellation notice for Arahan MKN No.24 across all publicly accessible government portals, combined with the fact that the No.26 cancellation document specifically references only No.26 (not No.24), strongly suggests No.24 remains active. This creates a **dual-framework period**: X-MAYA drills may still be governed by Arahan MKN No.24 (legacy MKN directive) while Act 854 provides the overarching statutory framework. CSCDC drill protocol positioning must acknowledge both instruments. REQUIRES: HUMINT confirmation via NACSA/MKN contacts.

### PIR-OPP007-003: Participant Organisations
- **Priority:** High
- **Previous Status:** Resolved (strengthened)
- **Current Status:** Resolved (strengthened — state-level expansion)
- **Finding:** NCII sector leads appointed under Section 15(1) Act 854 effective 11 Sep 2024. State-level NCII sector leads (Pejabat SUK Negeri) appointed effective 28 Jan 2025 — this extends Act 854 compliance to state government level. The No.26 cancellation PDF's Senarai Edaran 2 confirms 11 NCII sectors with their sector leads (KSU-level for federal, state-level for SUK).
- **Source:** https://www.nacsa.gov.my/NCII.php (NACSA official — NCII sector lead appointments, 31 Aug 2026), Arahan MKN No.26 cancellation PDF (Senarai Edaran 2)
- **Confidence:** High — official NACSA primary source + MKN official document
- **Analysis:** State-level sector lead appointments (28 Jan 2025) expand the drill participant universe. CSCDC drill design should account for state-level NCII entities, not just federal agencies.

### PIR-OPP007-004: Scenario Types
- **Priority:** High
- **Previous Status:** Resolved (strengthened)
- **Current Status:** Resolved (strengthened — AISCF scenarios)
- **Finding:** AISCF introduces AI-specific attack scenarios: data poisoning, prompt injection, adversarial attacks, model theft, AI supply chain compromise. These complement the existing scenario types (ransomware, breach simulation, SOC 3.0 live attack, encrypted lateral movement detection) from NCSS 2026 and Cyber Games 2025.
- **Source:** https://www.nacsa.gov.my/ai_systems_cyber_security_framework.php
- **Confidence:** High — official NACSA source
- **Analysis:** AI-driven attack scenarios represent the next frontier of drill design. The AISCF framework provides the policy basis for including AI-specific scenarios in future X-MAYA or CSCDC drills.

### PIR-OPP007-005: External Facilitation
- **Priority:** High
- **Previous Status:** Resolved (strengthened)
- **Current Status:** Resolved (strengthened — NACSA CE directive governance)
- **Finding:** NACSA licensing framework (Arahan KE NACSA No. 2) confirms NACSA CE is exercising Section 13 Act 854 directive powers to regulate cybersecurity service providers. This governance model (NACSA CE directives) replaces the old MKN directive model for service provider regulation. Licensing active since 1 Oct 2024 for managed SOC monitoring and penetration testing services.
- **Source:** https://www.nacsa.gov.my/application-licensing.php (NACSA official — licensing page, 31 Aug 2026)
- **Confidence:** High — official NACSA primary source
- **Analysis:** The NACSA CE directive governance model is now operationally confirmed — Arahan KE NACSA No. 2 is a real directive issued under Section 13 powers. This validates the transition from MKN directives to NACSA CE directives as the primary regulatory instrument. External facilitation providers must now be licensed under this framework.

### PIR-OPP007-006: Previous Drills
- **Priority:** Medium
- **Previous Status:** Partially Resolved
- **Current Status:** Partially Resolved (no new data)
- **Finding:** No new drill history data found. X-MAYA (since 2008), Cyber Games 2025 (May 2025), NCSS 2026 simulation sessions (Jul 2026) remain the confirmed exercise portfolio.
- **Source:** https://www.nacsa.gov.my/cyber_games_2025.php (NACSA official — unchanged)
- **Confidence:** Medium — no new data this cycle
- **Analysis:** Exercise portfolio unchanged. No new national drill announcements.

### PIR-OPP007-007: Evaluation Framework
- **Priority:** Medium
- **Previous Status:** Open
- **Current Status:** Open (no new data)
- **Finding:** No publicly documented evaluation framework found. The NACSA government page lists risk assessment guidelines (Pekeliling Am Bil.3/2024) and ICT security assessment guidelines (Pekeliling Am Bil.4/2024) but these are compliance frameworks, not exercise evaluation metrics.
- **Source:** https://www.nacsa.gov.my/government.php (NACSA official — government circulars, 31 Aug 2026)
- **Confidence:** Low — absence of evidence; evaluation framework likely internal (SULIT)
- **Analysis:** Drill evaluation framework remains OSINT-unresolvable.

### PIR-OPP007-008: Timeline
- **Priority:** Medium
- **Previous Status:** Partially Resolved
- **Current Status:** Partially Resolved (no new drill dates)
- **Finding:** No upcoming X-MAYA or national drill dates announced. NCSS 2026 (7-9 Jul 2026) remains the most recent confirmed event. Program Bulan Keselamatan Negara 2026 was launched at NCSS 2026 closing — may include drill activities but not confirmed.
- **Source:** https://cydes.my/ (NCSS 2026 official — unchanged)
- **Confidence:** Medium — no new drill schedule data
- **Analysis:** Drill timeline remains unconfirmed. No future drill dates publicly available.

### PIR-OPP007-009: Budget Adequacy
- **Priority:** Low
- **Previous Status:** Open
- **Current Status:** Open (no new data)
- **Finding:** No public cost disclosure for X-MAYA or Cyber Games 2025. RM 200K allocation (CSCDC Framework v2.0) remains the only budget reference. ePerolehan.gov.my not accessible (DeerFlow reported DNS failure).
- **Source:** CSCDC Framework v2.0 (L2 internal document, prior intelligence)
- **Confidence:** Low — no new OSINT data
- **Analysis:** Budget adequacy remains unassessable via OSINT.

### PIR-OPP007-010: International Observation
- **Priority:** Low
- **Previous Status:** Partially Resolved
- **Current Status:** Partially Resolved (no new data)
- **Finding:** No new international exercise data. Cyber Games 2025 (CoE+INTERPOL, 40 countries), Locked Shields 2026 (41 nations), NCSS 2026 international sponsors remain as previously resolved.
- **Source:** https://www.nacsa.gov.my/cyber_games_2025.php (unchanged)
- **Confidence:** High — prior findings hold
- **Analysis:** International observation portfolio unchanged.

### PIR-OPP002-001: Playbook Budget Allocation
- **Priority:** Critical
- **Previous Status:** Partial
- **Current Status:** Partial (no change)
- **Finding:** No procurement notice found for RM 150K playbook budget. ePerolehan.gov.my not accessible via web_extract (DeerFlow reported DNS failure). No RFP or tender notice on NACSA portal.
- **Source:** No new source found
- **Confidence:** Low — no new OSINT data
- **Analysis:** Playbook budget allocation remains OSINT-limited. ePerolehan access requires direct portal navigation or HUMINT.

### PIR-OPP002-002: Existing MKN Crisis Protocols
- **Priority:** High
- **Previous Status:** Resolved (strengthened)
- **Current Status:** Resolved (updated — NCCMP staleness identified)
- **Finding:** NCCMP page (NACSA official) still references 10 CNII domains using old "CNII" terminology: defence & security; banking & finance; info & comms; energy; transportation; water; health; government services; emergency services; food and agriculture. Current NCII structure (per NCII page) has 11 sectors including "Science, technology and innovation" as the 11th sector — NOT covered by NCCMP. NCCMP has NOT been updated to align with Act 854's 11-sector framework. Pekeliling Am Bil.4/2022 (public sector cyber incident management) and Bil.3-4/2024 (risk management + ICT security assessment) remain the current public sector circulars.
- **Source:** https://www.nacsa.gov.my/nccmp.php (NACSA official — NCCMP page, 31 Aug 2026), https://www.nacsa.gov.my/NCII.php (NACSA official — NCII page, 11 sectors), https://www.nacsa.gov.my/government.php (NACSA official — circulars)
- **Confidence:** High — official NACSA primary sources, direct comparison
- **Analysis:** NCCMP staleness is a significant finding. The national crisis management plan does not cover the 11th NCII sector (Science, technology and innovation) and uses outdated terminology ("CNII" vs "NCII"). This indicates NCCMP has not been updated since Act 854 expanded the NCII framework. CSCDC can flag this as a value-add observation in engagement — the crisis communication playbook should align with the current 11-sector NCII, not the stale 10-domain NCCMP.

### PIR-OPP002-003: War Room Physical Infrastructure
- **Priority:** High
- **Previous Status:** Open
- **Current Status:** Open (no new data)
- **Finding:** No public information on CSCDC physical War Room specifications. NACSA location confirmed: Level LG & G, West Wing, Perdana Putra Building, Putrajaya.
- **Source:** https://www.nacsa.gov.my/ (NACSA address confirmed)
- **Confidence:** Low — War Room infrastructure likely classified/SULIT
- **Analysis:** OSINT-unresolvable.

### PIR-OPP002-004: Technical Liaison Role
- **Priority:** High
- **Previous Status:** Open
- **Current Status:** Open (no new data)
- **Finding:** No publicly named CSCDC technical liaison. NACSA CE (IR. Dr. Megat Zuhairy Megat Tajuddin) confirmed as the directive-issuing authority under Section 13 Act 854.
- **Source:** Arahan MKN No.26 cancellation PDF (signatory confirmation)
- **Confidence:** Low — specific personnel roles likely internal/SULIT
- **Analysis:** OSINT-unresolvable.

### PIR-OPP002-005: Historical Cyber Incidents
- **Priority:** Medium
- **Previous Status:** Resolved (updated)
- **Current Status:** Resolved (no change)
- **Finding:** MyCERT reports 5,774 general incident classifications for 2026 YTD — unchanged from 24 Aug 2026 extraction. NC4 advisories remain at 6 for 2026 (latest: 24 Jul 2026, WordPress wp2shell). 38-day advisory gap since last advisory. NC4 Q3 2026 trends: attribution ▲ upward, vulnerable service ▲ upward.
- **Source:** https://www.mycert.org.my/en/statistics/ (MyCERT, unchanged), https://www.nc4.gov.my/alertAdvisory (NC4, 6 advisories confirmed)
- **Confidence:** High — official MyCERT and NC4 data
- **Analysis:** Incident statistics unchanged. The 38-day NC4 advisory gap (24 Jul to 31 Aug) is notable — either reduced threat activity or reduced advisory publication capacity. The Q3 upward trends in attribution and vulnerable service categories suggest the threat landscape remains active despite LOW overall level.

### PIR-OPP002-006: Holding Statement Bank Scope
- **Priority:** Medium
- **Previous Status:** Partial (strengthened)
- **Current Status:** Partial (no new data)
- **Finding:** No new data on holding statement bank scope. NCSS 2026 NCII resilience session remains the strongest public signal.
- **Source:** https://cydes.my/ (unchanged)
- **Confidence:** Medium — no new data
- **Analysis:** Holding statement bank scope remains partially resolved.

### PIR-OPP002-007: Inter-Agency Crisis Coordination
- **Priority:** High
- **Previous Status:** Resolved (strengthened)
- **Current Status:** Resolved (strengthened — NACSA CE directive model confirmed)
- **Finding:** NACSA CE directive model operationally confirmed via Arahan KE NACSA No. 2 (service provider licensing). This is a NACSA CE directive issued under Section 13 Act 854 — the same power that would govern inter-agency crisis coordination directives. State-level NCII sector leads (Pejabat SUK Negeri, effective 28 Jan 2025) extend coordination to state level.
- **Source:** https://www.nacsa.gov.my/application-licensing.php (Arahan KE NACSA No. 2), https://www.nacsa.gov.my/NCII.php (state-level sector leads)
- **Confidence:** High — official NACSA primary sources
- **Analysis:** Inter-agency coordination governance is now firmly under NACSA CE directive power (Section 13 Act 854). The Arahan KE NACSA directive series replaces the Arahan MKN directive series as the operational instrument.

### PIR-OPP002-008: War Room Activation Threshold
- **Priority:** Medium
- **Previous Status:** Open
- **Current Status:** Open (no new data)
- **Finding:** NC4 threat level remains LOW (31 Aug 2026). 5-level scale (LOW→MODERATE→CAUTION→HIGH→CRITICAL) confirmed. Q3 2026 attribution ▲ and vulnerable service ▲ upward trends noted. Specific War Room activation thresholds remain unpublished.
- **Source:** https://www.nc4.gov.my/ (NC4 portal, 31 Aug 2026)
- **Confidence:** Medium — NC4 threat level scale confirmed; activation criteria not published
- **Analysis:** War Room activation threshold remains OSINT-unresolvable.

### PIR-OPP002-009: Rehearsal & Drill Schedule
- **Priority:** Medium
- **Previous Status:** Partially Resolved
- **Current Status:** Partially Resolved (no new data)
- **Finding:** No new rehearsal or drill schedule data. NCSS 2026 simulation sessions (7-9 Jul 2026) remain the most recent rehearsal activity.
- **Source:** https://cydes.my/ (unchanged)
- **Confidence:** Medium — no new data
- **Analysis:** Rehearsal schedule remains partially resolved.

### PIR-OPP002-010: International Coordination
- **Priority:** Low
- **Previous Status:** Partially Resolved
- **Current Status:** Partially Resolved (no new data)
- **Finding:** No new international coordination data. Multi-channel framework (CoE/INTERPOL, NATO CCDCOE, APCERT/FIRST, OIC-CERT, bilateral MoUs) remains as previously resolved.
- **Source:** https://www.mycert.org.my/en/statistics/ (APCERT, FIRST, APWG, Honeynet, OIC-CERT memberships confirmed)
- **Confidence:** High — prior findings hold
- **Analysis:** International coordination portfolio unchanged.

## Cross-PIR Synthesis

Three major themes emerge this cycle:

1. **Dual-Framework Governance Period (Act 854 + Arahan MKN No.24):** [ASSESSMENT] The analytical finding that Arahan MKN No.24 is likely still active creates a dual-framework governance reality. Act 854 provides the overarching statutory framework, while No.24 may still govern specific X-MAYA drill protocols. The NACSA CE is actively issuing directives under Section 13 (confirmed by Arahan KE NACSA No. 2 for licensing), but the MKN directive system has not been fully wound down — only No.26 has been cancelled. This transition period is a positioning opportunity for CSCDC: show understanding of both instruments and offer to help bridge the gap.

2. **NCCMP Staleness — Crisis Plan Not Aligned with Current NCII:** The NCCMP still references 10 CNII domains using outdated "CNII" terminology, while the current NCII structure (per Act 854 and NACSA's NCII page) has 11 sectors. The 11th sector — Science, technology and innovation — is NOT covered by the national crisis management plan. This is a concrete, verifiable gap that CSCDC can surface in engagement as a value-add observation. It demonstrates deep understanding of the regulatory landscape and positions CSCDC as a partner who can help update the crisis communication framework.

3. **NACSA Institutional Maturation (AISCF + State-Level NCII):** NACSA is expanding its regulatory scope: AISCF adds AI systems security to the framework, and state-level NCII sector leads extend Act 854 compliance to state government. This maturation signals that NACSA is building a comprehensive, multi-layered cybersecurity governance system. CSCDC drill design and crisis communication playbook development should align with this expanding scope — AI-driven scenarios and state-level participation are emerging requirements.

## Intelligence Gaps

1. **Arahan MKN No.24 status** — [ASSESSMENT] Likely still active based on absence of cancellation notice, but unconfirmed. Requires HUMINT.
2. **NCCMP update timeline** — NCCMP is stale (10 vs 11 sectors). When will it be updated?
3. **No procurement data** — ePerolehan.gov.my inaccessible (DNS failure per DeerFlow). RM 150K playbook budget unconfirmed.
4. **No drill evaluation framework** — Internal NACSA/CSM document (PIR-OPP007-007).
5. **No future drill schedule** — No publicly announced X-MAYA or national drill dates (PIR-OPP007-008).
6. **No War Room infrastructure specs** — Classified/SULUT (PIR-OPP002-003).
7. **No technical liaison personnel** — Internal/SULUT (PIR-OPP002-004).
8. **No War Room activation threshold** — Internal NACSA/MKN protocol (PIR-OPP002-008).
9. **AISCF implementation status** — Framework published but integration into drills/playbooks unknown.
10. **NC4 advisory gap** — 38 days since last advisory (24 Jul to 31 Aug). Cause unknown.

## Recommendations

1. **🔴 HIGHEST PRIORITY: Confirm Arahan MKN No.24 status via HUMINT.** Engage NACSA/MKN contacts through classified channels. The dual-framework assessment (Act 854 + likely-active No.24) is the single most important governance finding for CSCDC drill protocol positioning. If No.24 is still active, CSCDC must design drill protocols that comply with both instruments.

2. **🟠 Flag NCCMP staleness as value-add in CSCDC engagement.** The NCCMP (10 domains, "CNII" terminology) is out of alignment with the current NCII structure (11 sectors, "NCII" terminology). The 11th sector (Science, technology and innovation) lacks crisis management coverage. This is a concrete, verifiable observation that demonstrates deep regulatory awareness.

3. **🟠 Prepare drill scenario framework incorporating AISCF threat vectors.** AI-driven attacks (data poisoning, prompt injection, adversarial attacks, model theft, AI supply chain compromise) are now part of NACSA's regulatory framework. CSCDC drill design should include AI-specific scenarios as a differentiator.

4. **🟡 Account for state-level NCII sector leads in drill design.** State-level sector leads (Pejabat SUK Negeri, effective 28 Jan 2025) extend Act 854 compliance to state government. CSCDC drill participant universe should include state-level entities.

5. **🟡 Monitor NC4 advisory pipeline gap.** The 38-day gap since the last advisory (24 Jul 2026) is unusual. Monitor for resumption of advisory publication or any threat level change.

## PIR Resolution Status Table

| PIR ID | Priority | Previous Status | Current Status | Confidence | Change |
|--------|----------|-----------------|----------------|------------|--------|
| PIR-OPP007-001 | Critical | Resolved (strengthened) | Resolved (strengthened — AISCF) | High | AISCF expands scope |
| PIR-OPP007-002 | Critical | Partial — REVALIDATE | Partial — ANALYTICAL (T3) | Medium | [ASSESSMENT] No.24 likely active |
| PIR-OPP007-003 | High | Resolved (strengthened) | Resolved (strengthened — state-level) | High | State-level sector leads |
| PIR-OPP007-004 | High | Resolved (strengthened) | Resolved (strengthened — AISCF) | High | AI scenarios added |
| PIR-OPP007-005 | High | Resolved (strengthened) | Resolved (strengthened — CE directive) | High | NACSA CE directive model confirmed |
| PIR-OPP007-006 | Medium | Partial (NEW) | Partial (no change) | Medium | No new data |
| PIR-OPP007-007 | Medium | Open | Open | Low | No new data |
| PIR-OPP007-008 | Medium | Partial | Partial (no change) | Medium | No new drill dates |
| PIR-OPP007-009 | Low | Open | Open | Low | No new data |
| PIR-OPP007-010 | Low | Partial (NEW) | Partial (no change) | High | No new data |
| PIR-OPP002-001 | Critical | Partial | Partial (no change) | Low | ePerolehan inaccessible |
| PIR-OPP002-002 | High | Resolved (strengthened) | Resolved (updated — NCCMP stale) | High | NCCMP staleness identified |
| PIR-OPP002-003 | High | Open | Open | Low | No new data |
| PIR-OPP002-004 | High | Open | Open | Low | No new data |
| PIR-OPP002-005 | Medium | Resolved (updated) | Resolved (no change) | High | MyCERT unchanged, NC4 gap noted |
| PIR-OPP002-006 | Medium | Partial (strengthened) | Partial (no change) | Medium | No new data |
| PIR-OPP002-007 | High | Resolved (strengthened) | Resolved (strengthened — CE model) | High | NACSA CE directive model confirmed |
| PIR-OPP002-008 | Medium | Open | Open | Medium | NC4 LOW unchanged, trends noted |
| PIR-OPP002-009 | Medium | Partial | Partial (no change) | Medium | No new data |
| PIR-OPP002-010 | Low | Partial (NEW) | Partial (no change) | High | No new data |

**Summary:** 20 PIRs total. 8 Resolved (3 updated/strengthened), 7 Partial (1 analytical finding), 5 Open. 3 significant findings this cycle: (1) Arahan MKN No.24 dual-framework assessment, (2) NCCMP staleness (10 vs 11 sectors), (3) NACSA AISCF publication. 1 T3 analytical finding (PIR-OPP007-002 — No.24 likely active).

## TOP 3 PIR SUGGESTIONS FOR NEXT CYCLE (AUTO-APPROVED)

1. **Suggestion:** Confirm Arahan MKN No.24 status via direct MKN/NACSA enquiry — is it still active, under review, or silently superseded by Act 854?
   **Rationale:** This is the #1 open question for the CSCDC drill workstream. The dual-framework assessment (Act 854 + likely-active No.24) affects drill protocol positioning. If No.24 is still active, X-MAYA governance operates under both statutory and directive frameworks simultaneously.
   **Search Queries:** "Arahan MKN No.24" site:mkn.gov.my, "Arahan MKN" X-MAYA governance 2026, "Arahan MKN No.24" cancellation, site:nacsa.gov.my "Arahan No.24"

2. **Suggestion:** Monitor NCCMP update — has the National Cyber Crisis Management Plan been revised to align with Act 854's 11-sector NCII framework?
   **Rationale:** NCCMP staleness (10 vs 11 sectors) is a verifiable gap. If NCCMP is updated to include the 11th sector (Science, technology and innovation), this signals that the crisis management framework is being aligned with Act 854. If not, the gap persists and CSCDC can flag it.
   **Search Queries:** "NCCMP" update 2026 site:nacsa.gov.my, "National Cyber Crisis Management Plan" revision, NACSA "crisis management plan" 11 sectors, "NCII" "crisis management" Malaysia 2026

3. **Suggestion:** Track AISCF implementation — is NACSA integrating AI systems security into drill scenarios and crisis communication playbooks?
   **Rationale:** AISCF is a new regulatory instrument (not present in prior cycle). If NACSA is integrating AISCF into drill design, CSCDC should prepare AI-specific scenario frameworks (data poisoning, prompt injection, adversarial attacks, model theft, AI supply chain compromise) as a differentiator in engagement.
   **Search Queries:** "AISCF" implementation NACSA 2026, "AI Systems Cyber Security Framework" drill, NACSA AI cybersecurity exercise, "AI supply chain" Malaysia cyber drill

---

---CVS BLOCK---
Claim: Arahan MKN No.24 is likely still active — no cancellation notice found across NACSA homepage, MKN portal, Act 854 page, government circulars page, or the No.26 cancellation PDF
Source: NACSA official homepage (https://www.nacsa.gov.my/), MKN portal (https://www.mkn.gov.my/), Arahan MKN No.26 cancellation PDF (https://www.nacsa.gov.my/doc/PEMAKLUMAN...ARAHAN...NO.26...pdf), NACSA Act 854 page (https://www.nacsa.gov.my/act854.php), NACSA government page (https://www.nacsa.gov.my/government.php) — all accessed 31 Aug 2026
Source Level: L1 (official government portals) + L5 (analytical inference from absence)
Tier: T3 [ASSESSMENT]
Validation Status: Inferred (analytical interpretation based on absence of cancellation evidence across 5 official portals)
Confidence Score: 5 (Authority:2 Traceability:2 Recency:2 Consistency:1 Completeness:0)
Action Required: Human review — HUMINT confirmation via NACSA/MKN classified channel required
---END CVS BLOCK---

---CVS BLOCK---
Claim: NACSA published the AI Systems Cyber Security Framework (AISCF) covering data poisoning, prompt injection, adversarial attacks, model theft, and AI supply chain compromise
Source: NACSA official (https://www.nacsa.gov.my/ai_systems_cyber_security_framework.php — Last Updated 31 Aug 2026)
Source Level: L1 (official government record)
Tier: T2
Validation Status: Verified (official primary source, full page extracted)
Confidence Score: 7 (Authority:2 Traceability:2 Recency:2 Consistency:2 Completeness:1)
Action Required: None
---END CVS BLOCK---

---CVS BLOCK---
Claim: NCCMP references 10 CNII domains using outdated "CNII" terminology while current NCII structure has 11 sectors — the 11th sector (Science, technology and innovation) is NOT covered by NCCMP
Source: NACSA NCCMP page (https://www.nacsa.gov.my/nccmp.php — 10 domains, "CNII" terminology) vs NACSA NCII page (https://www.nacsa.gov.my/NCII.php — 11 sectors, "NCII" terminology) — both accessed 31 Aug 2026
Source Level: L1 (official government records, direct comparison)
Tier: T2
Validation Status: Verified (official primary sources, direct page-to-page comparison)
Confidence Score: 7 (Authority:2 Traceability:2 Recency:2 Consistency:2 Completeness:1)
Action Required: None — flag as value-add observation for CSCDC engagement
---END CVS BLOCK---

---CVS BLOCK---
Claim: NC4 National Cyber Threat Level is LOW as of 31 Aug 2026 with 6 advisories issued in 2026 (latest 24 Jul 2026, WordPress wp2shell) — 38-day advisory gap since last advisory
Source: NC4 Portal (https://www.nc4.gov.my/ — last updated 31 Aug 2026 01 AM) + NC4 Advisory list (https://www.nc4.gov.my/alertAdvisory)
Source Level: L1 (official government operational portal)
Tier: T2
Validation Status: Verified (official primary source, live portal data + advisory list extracted)
Confidence Score: 7 (Authority:2 Traceability:2 Recency:2 Consistency:2 Completeness:1)
Action Required: None — monitor for threat level changes and advisory resumption
---END CVS BLOCK---

---CVS BLOCK---
Claim: MyCERT reports 5,774 general incident classifications for 2026 YTD (unchanged from 24 Aug 2026 extraction)
Source: MyCERT (https://www.mycert.org.my/en/statistics/)
Source Level: L1 (official government cyber incident response centre)
Tier: T2
Validation Status: Verified (official primary source)
Confidence Score: 7 (Authority:2 Traceability:2 Recency:2 Consistency:2 Completeness:1)
Action Required: None
---END CVS BLOCK---

---CVS BLOCK---
Claim: NCII sector leads appointed under Section 15(1) Act 854 effective 11 Sep 2024; state-level sector leads (Pejabat SUK Negeri) appointed effective 28 Jan 2025
Source: NACSA NCII page (https://www.nacsa.gov.my/NCII.php — appointment PDFs linked, 31 Aug 2026)
Source Level: L1 (official government record)
Tier: T2
Validation Status: Verified (official primary source, full page extracted)
Confidence Score: 7 (Authority:2 Traceability:2 Recency:2 Consistency:2 Completeness:1)
Action Required: None
---END CVS BLOCK---

---CVS BLOCK---
Claim: NACSA CE directive model operationally confirmed — Arahan Ketua Eksekutif NACSA No. 2 governs cybersecurity service provider licensing under Section 13 Act 854, active since 1 Oct 2024
Source: NACSA licensing page (https://www.nacsa.gov.my/application-licensing.php — 31 Aug 2026)
Source Level: L1 (official government record)
Tier: T2
Validation Status: Verified (official primary source, full page extracted)
Confidence Score: 7 (Authority:2 Traceability:2 Recency:2 Consistency:2 Completeness:2)
Action Required: None
---END CVS BLOCK---

---CVS BLOCK---
Claim: Arahan MKN No.26 cancellation PDF signed by IR. Dr. Megat Zuhairy Megat Tajuddin (NACSA CE), dated 26 Nov 2024, ref MKN.600-2/1/6 (S)(53), specifically and only cancels No.26 — does not reference No.24
Source: MKN official cancellation notice (https://www.nacsa.gov.my/doc/PEMAKLUMAN%20PEMBATALAN%20ARAHAN%20MAJLIS%20KESELAMATAN%20NEGARA%20NO.26%20...pdf — full text extracted)
Source Level: L1 (official government document, MKN letterhead)
Tier: T2
Validation Status: Verified (official primary source, full document body extracted including all paragraphs and distribution lists)
Confidence Score: 7 (Authority:2 Traceability:2 Recency:1 Consistency:2 Completeness:2)
Action Required: None
---END CVS BLOCK---

---CVS BLOCK---
Claim: DeerFlow pro dispatch succeeded (thread bd41a0d4, 977 bytes) but produced summary-only output — full INT record not captured in response stream
Source: DeerFlow dispatch log + output file (/tmp/pir-CSCDC-05-output.txt)
Source Level: L5 (AI-generated output)
Tier: T3 [ASSESSMENT]
Validation Status: Verified (dispatch confirmed, output size confirmed)
Confidence Score: 7 (Authority:2 Traceability:2 Recency:2 Consistency:2 Completeness:1)
Action Required: None — pattern consistent with prior cycles; web_extract fallback compensates
---END CVS BLOCK---
