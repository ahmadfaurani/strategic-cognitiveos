---
id: INT-20260907-CSCDC-05-001
record_type: intelligence
title: "PIR Collection: CSCDC-05 Cyber Drill & Crisis Protocol Monitor — 2026-09-07"
created_at: 2026-09-07T01:51:37+08:00
updated_at: 2026-09-07T01:51:37+08:00
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
  reference: "DeerFlow pro dispatch (thread 3dc52be4, 23,986 bytes — full-format output, first since 24 Aug) + orchestrator web_extract on 10 official/secondary URLs + cross-cronjob reference (CSCDC-02, CSCDC-03 same-day records) — 2026-09-07"
summary: "Prasarana ransomware attack 25 Aug 2026 (RansomHub, PDP chain exercised 26-29 Aug) = live national cyber crisis event inside monitoring window; NC4 advisory gap extended to 45 days with threat level LOW since 5 Apr 2024 (29 months); NACSA issued separate 28 Aug cyber attack warning not on NC4 portal (channel duality); NCCMP staleness persists (10 vs 11 sectors, 2nd cycle); no drill dates, no procurement, No.24 still likely active; DeerFlow full-format output returned this cycle with 4 factual errors caught and corrected by orchestrator validation"
strategic_significance: "The Prasarana incident is the closest thing to a live rehearsal of the national cyber crisis architecture in the collection period — the statutory response chain (operator → PDP Commissioner → NACSA+CSM) was exercised end-to-end while the formal drill pipeline (RM 200K National Cyber Drill, RM 150K playbook) shows zero public procurement activity. The crisis communication workstream's value proposition can now be anchored to a real incident, not hypotheticals. Separately, the NC4 public advisory pipeline is dormant (45 days, threat level static 29 months) while NACSA issued a 28 Aug warning through non-NC4 channels — a coordination/signalling gap CSCDC can credibly surface."
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
  - INT-20260831-CSCDC-05-001
  - INT-20260824-CSCDC-05-001
intelligence_type: market
evidence:
  - "Prasarana Malaysia Berhad ransomware attack 25 Aug 2026 attributed to RansomHub; data uploaded to dark web; PDP Commissioner's Office informed 26 Aug and instructed Prasarana to issue Data Breach Notification by 29 Aug, which Prasarana complied with. Full article body extracted. (https://www.securitystudies.info/country/malaysia/reports/malaysia-report-2026-09-04-0640/ — Malaysia Security Report 4 Sep 2026, period 28 Aug-4 Sep)"
  - "Same incident independently recorded by CSCDC-03 same-day collection with additional detail: 316GB data exfiltrated; no disruption to public transport services; sources theedgemalaysia.com, securityonline.info, breach.house. Two independent collection chains agree on all core facts. (INT-20260907-001-cscdc-03-infra-procurement.md, accessed 7 Sep 2026)"
  - "NACSA cyber attack warning issued 28 Aug 2026 — intrusions, DDoS, web defacement, malware infections targeting numerous government and private organisations in Malaysia. NOT present on NC4 advisory portal (45-day silence) and distinct from legacy NACSA 'Heightened Alert' pages (advisory10.php dated 27-10-2023, advisory11.php dated 29-01-2024 — both verified as historical). (SecurityStudies Malaysia Report 4 Sep 2026 + https://www.nacsa.gov.my/advisory10.php + https://www.nacsa.gov.my/advisory11.php, both extracted 7 Sep 2026)"
  - "NC4 advisory gap: latest advisory remains NC4-ALR-2026-000006 (WordPress wp2shell, 24 Jul 2026). 24 Jul → 7 Sep = 45 days. 2026 listing shows 5 advisories (000001, 000002, 000004, 000005, 000006) — ID 000003 absent from public listing; prior cycle's '6 advisories' claim is unconfirmed (only 5 IDs ever listed). (https://www.nc4.gov.my/alertAdvisory, extracted 7 Sep 2026)"
  - "National Cyber Threat Level LOW — widget states 'Last updated: 05 April 2024, 11:46AM' = 29 months static (NOT 17 months as stated by CSCDC-03/DeerFlow this cycle — arithmetic correction: 5 Apr 2024 → 7 Sep 2026 = 29 months). Portal page-level daily refresh (07 Sep 2026, 01 AM) is statistics telemetry, not threat-level status. (https://www.nc4.gov.my/, extracted 7 Sep 2026)"
  - "NC4 dashboard telemetry extracted across 4 reporting periods (7 Sep 2026): Daily — all 6 categories ▼; Monthly (Sep) — all ▼; Q3 (Jul-Sep) — attribution ▲ and vulnerable service ▲, others ▼; Annual 2026 — attribution ▲ (5M vs 12M prior) and vulnerable service ▲ (2M vs 11M prior), others ▼. Dashboard existed in prior cycle (31 Aug) — NOT new; this cycle adds full 4-period extraction. Widget current-vs-delta semantics ambiguous in static extraction; arrows are the reliable qualitative signal. (https://www.nc4.gov.my/)"
  - "MyCERT statistics: 5,774 general incident classifications 2026 YTD — unchanged from 24 Aug and 31 Aug extractions (third consecutive identical reading). 0 Malaysia botnet drones/malware infections. (https://www.mycert.org.my/en/statistics/, extracted 7 Sep 2026)"
  - "NCCMP page re-verified STALE (2nd consecutive cycle): still references 10 CNII domains (defence & security; banking & finance; info & comms; energy; transportation; water; health; government services; emergency services; food & agriculture) with old 'CNII' terminology, vs current 11-sector NCII (11th: Science, technology and innovation). (https://www.nacsa.gov.my/nccmp.php, extracted 7 Sep 2026)"
  - "NACSA homepage (Last Updated: 7 September 2026): Arahan MKN No.26 cancellation notice still displayed; NO cancellation notice for Arahan MKN No.24 anywhere on site. Prior T3 assessment (No.24 likely still active; dual-framework period) carries forward. MyKriptografi Action Plan 2026-2030 (4 pillars, 12 strategies, 32 programmes, 80 activities) confirmed on homepage — but per CSCDC-02 cross-reference it predates this cycle (published 11 Feb 2026, updated 3 Apr 2026) and is CSCDC-02's coverage lane. (https://www.nacsa.gov.my/, extracted 7 Sep 2026)"
  - "NCII page re-verified unchanged: 11 sectors; sector leads appointed under Sec 15(1) Act 854 effective 11 Sep 2024; state-level leads (Pejabat SUK Negeri) effective 28 Jan 2025. (https://www.nacsa.gov.my/NCII.php, extracted 7 Sep 2026)"
  - "cydes.my unchanged: NCSS 2026 (7-9 Jul 2026, PICC Putrajaya) still the featured event; no new drill dates or upcoming exercise announcements. (https://cydes.my/, extracted 7 Sep 2026)"
  - "Cyber Games 2025 page unchanged: 20-23 May 2025, ~120 participants from 40 countries, NACSA + Council of Europe + INTERPOL, opened by Digital Ministry SG Fabian Bigar. (https://www.nacsa.gov.my/cyber_games_2025.php, extracted 7 Sep 2026)"
  - "CSM portal FULLY DOWN this cycle — all service pages return Internal Server Error (CSCDC-03 diagnostic: resolves to IPv6 2001:f40:29:1681:211:24:25:21, HTTP 000). CSM CyberDrill EXCON standing finding NOT re-verifiable this cycle. (INT-20260907-001-cscdc-03-infra-procurement.md, 7 Sep 2026)"
  - "Cyber Security Summit Malaysia 2026 — 10 Sep 2026, InterContinental KL, 150+ CISOs/CIOs/government officials, theme 'Cyber Security Reimagined: Identity, Intelligence & Resilience', NACSA speaker Nuraishah Mokhtar (Senior Principal Assistant Director), organised by Exito Media Concepts. Industry event, 3 days after this cycle. (INT-20260907-001-cscdc-03-infra-procurement.md citing malaysiasun.com/PRNewswire, 7 Sep 2026)"
  - "Budget 2027 to be tabled 9 Oct 2026 (Deputy Finance Minister Liew Chin Tong; The Star 6 Sep 2026) — first fiscal vehicle after the collection period; zero PQC mentions in pre-budget coverage per CSCDC-02; drill/playbook allocation watch item. (INT-20260907T0126-001 CSCDC-02 record, 7 Sep 2026)"
  - "ePerolehan.gov.my unreachable this cycle (curl HTTP 000) — consistent with all prior cycles; RM 200K drill and RM 150K playbook procurement remain unverifiable. (orchestrator network test, 7 Sep 2026)"
  - "QR code scam losses RM28.67M in H1 2026 (5,134 reports); RM80.86M cumulative since Jan 2023 (11,919 cases). Context for crisis communication workload — scam-driven, not drill-driven. (SecurityStudies Malaysia Report 4 Sep 2026, full body extracted)"
  - "Search backend blackout persists for this cycle's own queries (web_search and Firecrawl /v1/search returned empty across 4 attempts 01:47-01:49 MYT) — CSCDC-03 reported 3 successful searches earlier in the same window; recovery is flaky/intermittent. (orchestrator dispatch log + INT-20260907-001-cscdc-03)"
implications:
  - "Prasarana incident (25 Aug 2026) is the strongest crisis-protocol engagement hook of the collection period: the statutory chain (operator → PDP Commissioner → NACSA+CSM → public breach notification) ran end-to-end in the real world while the War Room/playbook/drill pipeline shows zero public activity. CSCDC positioning can offer: incident-communication after-action methodology, holding statement banks keyed to transport-sector scenarios, and gap analysis of the PDP-statutory vs War Room-crisis channels."
  - "NC4 public advisory dormancy (45 days) + threat-level stasis (29 months) + a parallel NACSA warning channel (28 Aug) = the national cyber alerting apparatus has a visibility/coordination gap. This is a concrete, verifiable observation CSCDC can surface — the crisis communication playbook should define which channel speaks when, and the 30-minute holding statement KPI currently has no active public advisory pipeline behind it."
  - "NCCMP staleness is now a 2-cycle-confirmed finding: the national crisis management plan covers 10 CNII domains while Act 854's NCII has 11 sectors. The 11th sector (Science, technology and innovation) has no published crisis management coverage. Flag as value-add in CSCDC engagement."
  - "No public drill activity for Q4 2026: no dates, no procurement, no participant announcements, ePerolehan unreachable. Combined with the Prasarana live incident, the national cyber exercise agenda appears dormant while real incidents do the testing — this asymmetry (live-fire vs rehearsal) is itself a strategic observation for drill-design positioning."
  - "CSM portal outage degrades one of the four CERT-ecosystem pillars' public presence during the same window NC4 advisories went quiet — the crisis ecosystem's public-facing layer is thinning even as private-surface incidents (Prasarana, QR scams) rise. Monitor whether this is transient infrastructure failure or structural."
  - "DeerFlow pro returned its first substantial full-format output since 24 Aug (23,986 bytes) but contained 4 factual errors (48→45 days arithmetic error, 17→29 months stale-figure propagation, Q3 metrics row duplicated from monthly, 'dashboard is NEW' false claim) plus 1 fabricated URL (nacsa.gov.my/directive26.php) and 1 unverified date (AISCF 'launched 9 Jul' = NQAIC MoU date conflation). Orchestrator validation against independent L1 extraction remains mandatory; DeerFlow output alone would have shipped a 10% arithmetic error and a false novelty claim."
open_questions:
  - "Arahan MKN No.24 status — T3 assessment (likely active) carries forward a 3rd cycle; no cancellation notice found on NACSA homepage (7 Sep), MKN portal, or No.26 cancellation PDF. Requires HUMINT."
  - "Did the Prasarana incident trigger any War Room / CSCDC crisis activation, or was it handled purely via the PDP statutory channel? No public evidence either way — requires HUMINT or post-incident coverage."
  - "What channel did NACSA's 28 Aug cyber attack warning use, and why is it absent from the NC4 advisory portal? Full text of the warning not located this cycle (search blackout)."
  - "NC4 advisory dormancy cause — resource constraint, strategic quiet, or process change? 45 days and counting."
  - "Prasarana incident volume (316GB) — single-chain attribution (CSCDC-03 citing breach.house/securityonline); SecurityStudies full body does not state volume in extracted portion. Corroborate next cycle."
  - "Drill evaluation framework, War Room activation thresholds, War Room infrastructure specs — all remain SULIT/OSINT-unresolvable (PIR-OPP007-007, PIR-OPP002-003, PIR-OPP002-004, PIR-OPP002-008)."
  - "CSM portal outage — cause, duration, and impact on CSM CyberDrill service delivery unknown while portal is down."
  - "NC4-ALR-2026-000003 — exists but absent from public listing? Prior cycle claimed '6 advisories in 2026' while listing 5 IDs; current listing shows 5. Reconcile."
recommended_actions:
  - "Monitor Cyber Security Summit Malaysia 2026 (10 Sep, InterContinental KL) post-event coverage for CSCDC leadership visibility and any drill/crisis-protocol announcements — 3-day collection window."
  - "Anchor the CSCDC crisis communication positioning to the Prasarana incident: prepare a one-page after-action analysis of the 25 Aug response chain (operator → PDP → NACSA+CSM) mapped against the Framework v2.0 Unit 4 War Room functions, explicitly noting which steps had no public-facing component."
  - "Add NACSA's non-NC4 warning channel to monitoring: the 28 Aug warning was not on the NC4 portal — watch nacsa.gov.my announcements/media statements as a parallel advisory feed; obtain full text of the 28 Aug warning next cycle."
  - "Track Prasarana follow-on signals: PDP enforcement action, NACSA/CSM post-incident statements, transport-sector NCII reviews — each is a live data point on how the crisis architecture actually behaves."
  - "Keep HUMINT priority: Arahan MKN No.24 status confirmation via NACSA/MKN classified channel — 3rd cycle flagged, still the top governance gap for drill protocol positioning."
  - "Flag NCCMP staleness (10 vs 11 sectors) as a value-add observation in CSCDC engagement — now 2-cycle-confirmed against the live NCCMP page."
  - "Watch Budget 2027 (tabled 9 Oct 2026) for drill/playbook allocation signals; ePerolehan remains unreachable so budget documents are the only public funding path."
  - "Retry ePerolehan and CSM portal accessibility next cycle; if CSM outage persists 2+ cycles, note it as an ecosystem fragility data point in CSCDC engagement materials."
related_initiatives:
  - INIT-20260725-007
related_stakeholders:
  - STK-20260725-001
---

# Intelligence Report: CSCDC-05 Cyber Drill & Crisis Protocol Monitor

## Collection Summary

Collection cycle executed 7 September 2026 (01:46-01:55 MYT) for PIR Cluster CSCDC-05 covering OPP-20260725-007 (Cyber Drill) and OPP-20260725-002 (War Room Methodology). Previous cycle: 31 August 2026 (7-day delta). **DeerFlow pro dispatch SUCCEEDED with a full-format output this cycle** (thread 3dc52be4, 23,986 bytes — first substantial product since 24 Aug; prior cycles returned summary-only 263-977 bytes). Per CVS Rule 6 the DeerFlow output (L5 AI-generated) was validated against independent orchestrator web_extract on 10 official/secondary sources; **4 factual errors were caught and corrected** (advisory gap arithmetic 48→45 days; threat-level staleness 17→29 months; Q3 dashboard metrics row duplicated from monthly; false "live dashboard is NEW" claim), 1 fabricated URL excluded (nacsa.gov.my/directive26.php — the No.26 cancellation is a PDF), and 1 unverified date removed (AISCF "launched 9 Jul 2026" — conflation with the NQAIC MoU date). Cross-cronjob reference applied to same-day CSCDC-02 and CSCDC-03 records.

**Three significant findings this cycle:** (1) **Prasarana Malaysia Berhad ransomware attack, 25 Aug 2026, attributed to RansomHub** — data uploaded to dark web, PDP Commissioner informed 26 Aug, Data Breach Notification issued 29 Aug, NACSA+CSM engaged, no public-transport disruption. This is the first live national-level CNII crisis event inside the collection window and the strongest crisis-protocol engagement hook to date — verified via two independent collection chains (SecurityStudies.info full-body extraction + CSCDC-03 same-day multi-source record). (2) **NC4 public advisory pipeline dormant**: 45-day advisory gap (24 Jul → 7 Sep) and threat level LOW static since 5 Apr 2024 (29 months), while NACSA issued a 28 Aug cyber attack warning through a non-NC4 channel — a verifiable coordination/visibility gap in the national alerting apparatus. (3) **NCCMP staleness confirmed for a 2nd consecutive cycle** (10 CNII domains vs 11 NCII sectors, 7 Sep extraction). No drill dates, no procurement activity, and no Arahan MKN No.24 cancellation found — standing findings unchanged.

## PIR Findings

### PIR-OPP007-001: Drill Scope & Objectives
- **Priority:** Critical
- **Previous Status:** Resolved (strengthened — AISCF)
- **Current Status:** Resolved (no change)
- **Finding:** No new drill scope announcements this cycle. Standing resolution holds: X-MAYA (since 2008) is integrated comms+technical; Locked Shields 2026 integrates comms+legal+decision-making; AISCF (data poisoning, prompt injection, adversarial attacks, model theft, AI supply chain compromise) remains the reference for AI-driven scenario expansion. DeerFlow's "AISCF launched 9 Jul 2026" was **rejected as unverified** — 9 Jul 2026 is the NQAIC MoU date; AISCF launch date is not established in any validated source this cycle.
- **Source:** https://www.nacsa.gov.my/ai_systems_cyber_security_framework.php (NACSA official, unchanged); no new sources found
- **Confidence:** High — standing finding on official sources; no delta
- **Analysis:** Drill scope remains shaped by the standing portfolio; without an announced drill there is nothing to update. AISCF-driven scenario expansion remains the forward-looking differentiator for drill design positioning.

### PIR-OPP007-002: MKN Drill Protocols
- **Priority:** Critical
- **Previous Status:** Partial — ANALYTICAL (T3)
- **Current Status:** Partial — ANALYTICAL (T3, unchanged)
- **Finding:** Arahan MKN No.24 status unchanged: no cancellation notice found on the NACSA homepage (Last Updated 7 Sep 2026), MKN portal, or the No.26 cancellation PDF (which references only No.26). No new NACSA CE directives under Section 13 Act 854 located this cycle. The T3 dual-framework assessment carries forward for a 3rd cycle: Act 854 (statutory) + Arahan MKN No.24 (legacy, likely still active) may simultaneously govern X-MAYA drill protocols.
- **Source:** https://www.nacsa.gov.my/ (7 Sep 2026), https://www.nacsa.gov.my/doc/PEMAKLUMAN PEMBATALAN ARAHAN MAJLIS KESELAMATAN NEGARA NO.26 ....pdf (full text extracted, prior cycle), https://www.mkn.gov.my/
- **Confidence:** Medium — [ASSESSMENT] analytical inference from absence of cancellation evidence across official portals (T3)
- **Analysis:** [ASSESSMENT] The dual-framework governance period persists. This is now the top OSINT-stable, HUMINT-dependent gap in the cluster — 3 consecutive cycles with the same finding. CSCDC drill protocol positioning must acknowledge both instruments until No.24 status is confirmed.

### PIR-OPP007-003: Participant Organisations
- **Priority:** High
- **Previous Status:** Resolved (strengthened — state-level)
- **Current Status:** Resolved (no change)
- **Finding:** NCII page re-verified unchanged (7 Sep 2026): 11 sectors; federal sector leads appointed under Section 15(1) Act 854 effective 11 Sep 2024; state-level sector leads (Pejabat SUK Negeri) effective 28 Jan 2025. No new participant announcements or sector lead changes.
- **Source:** https://www.nacsa.gov.my/NCII.php (NACSA official, 7 Sep 2026)
- **Confidence:** High — official primary source, re-verified this cycle
- **Analysis:** Participant universe stable: X-MAYA joint MKN/CSM, CSM CyberDrill methodology, 11 NCII sectors federal + state. Drill design should still account for state-level NCII entities.

### PIR-OPP007-004: Scenario Types
- **Priority:** High
- **Previous Status:** Resolved (strengthened — AISCF scenarios)
- **Current Status:** Resolved (no change)
- **Finding:** No new scenario types announced. Standing: ransomware on CNII, breach simulation, SOC 3.0 live attack, encrypted lateral movement (NCSS 2026/Cyber Games 2025 baseline) + AISCF AI vectors (data poisoning, prompt injection, adversarial attacks, model theft, AI supply chain compromise). Note: the Prasarana incident (see PIR-OPP002-005) is a real-world data point that ransomware on CNII/transport remains the live scenario class.
- **Source:** https://www.nacsa.gov.my/ai_systems_cyber_security_framework.php; https://cydes.my/ (unchanged)
- **Confidence:** High — official sources, no delta
- **Analysis:** The 25 Aug Prasarana ransomware attack reinforces that ransomware-on-transport-CNII is not hypothetical — drill scenario design should weight real-incident classes observed in 2026 (ransomware, QR-fraud-adjacent social engineering).

### PIR-OPP007-005: External Facilitation
- **Priority:** High
- **Previous Status:** Resolved (strengthened — NACSA CE directive governance)
- **Current Status:** Resolved (standing — NOT re-verifiable this cycle)
- **Finding:** Standing resolution holds (CSM CyberDrill as EXCON methodology provider; Arahan KE NACSA No. 2 licensing directive since 1 Oct 2024). **CSM portal is FULLY DOWN this cycle** — all service pages return Internal Server Error (CSCDC-03 diagnostic: IPv6 resolution, HTTP 000), so the CSM CyberDrill service page could not be re-verified. No new facilitator appointments or licensing updates found.
- **Source:** https://www.nacsa.gov.my/application-licensing.php (unchanged); CSM outage per INT-20260907-001-cscdc-03-infra-procurement.md (diagnostic detail)
- **Confidence:** Medium — standing finding valid from cached intelligence; live re-verification blocked by CSM outage
- **Analysis:** CSM's public-facing infrastructure being fully down during the same window NC4 advisories went quiet is a coincident signal worth watching — if both persist, the crisis ecosystem's public-facing layer is structurally thinning.

### PIR-OPP007-006: Previous Drills
- **Priority:** Medium
- **Previous Status:** Partial
- **Current Status:** Partial (no change)
- **Finding:** No after-action reports or lessons-learned publications found. Exercise portfolio unchanged: X-MAYA (since 2008), Cyber Games 2025 (20-23 May 2025, ~120 participants, 40 countries, CoE+INTERPOL — page re-verified unchanged), NCSS 2026 simulation sessions (7-9 Jul 2026). No NCSS 2026 after-action publication.
- **Source:** https://www.nacsa.gov.my/cyber_games_2025.php (re-verified 7 Sep 2026), https://cydes.my/ (unchanged)
- **Confidence:** Medium — no new data
- **Analysis:** The after-action gap is itself the finding: Malaysia's exercise portfolio has no public lessons-learned pipeline, which is exactly the artefact a drill-design engagement would produce.

### PIR-OPP007-007: Evaluation Framework
- **Priority:** Medium
- **Previous Status:** Open
- **Current Status:** Open (no change)
- **Finding:** No published evaluation framework or after-action methodology found. Likely internal NACSA/CSM SULIT document; CSM outage removes even indirect signals this cycle.
- **Source:** No new source found
- **Confidence:** Low — absence of evidence; OSINT-unresolvable
- **Analysis:** Remains OSINT-unresolvable. HUMINT or partnership access required.

### PIR-OPP007-008: Timeline
- **Priority:** Medium
- **Previous Status:** Partial
- **Current Status:** Partial (no new drill dates)
- **Finding:** No X-MAYA 2026/2027 dates or national drill announcements. cydes.my unchanged (NCSS 2026 remains featured). New context: **Cyber Security Summit Malaysia 2026 on 10 Sep 2026** (InterContinental KL; NACSA speaker Nuraishah Mokhtar, Senior Principal Assistant Director) — an industry event, not a drill, but the nearest-term public forum where NACSA/crisis-protocol signals may surface.
- **Source:** https://cydes.my/ (7 Sep 2026); INT-20260907-001-cscdc-03-infra-procurement.md (summit detail, PRNewswire/malaysiasun)
- **Confidence:** Medium — no drill schedule data; summit detail single-source via CSCDC-03 chain
- **Analysis:** Q4 2026 drill planning shows no public footprint. If the RM 200K drill proceeds, it is operating entirely outside public channels — or deferred to 2027.

### PIR-OPP007-009: Budget Adequacy
- **Priority:** Low
- **Previous Status:** Open
- **Current Status:** Open (no change)
- **Finding:** No procurement data. ePerolehan.gov.my unreachable this cycle (curl HTTP 000 — consistent with all prior attempts). RM 200K allocation (CSCDC Framework v2.0, L2) remains the only budget reference. Budget 2027 (tabled 9 Oct 2026, per CSCDC-02/The Star) is the next public funding event that could surface drill allocations.
- **Source:** Network test (curl HTTP 000, 7 Sep 2026); INT-20260907T0126-001 (Budget 2027 date)
- **Confidence:** Low — no new OSINT data
- **Analysis:** Budget adequacy remains unassessable via OSINT. The 9 Oct Budget 2027 tabling is the next observable funding checkpoint.

### PIR-OPP007-010: International Observation
- **Priority:** Low
- **Previous Status:** Partial
- **Current Status:** Partial (no change)
- **Finding:** No new international exercise announcements. Standing: Cyber Games 2025 (40 countries), Locked Shields 2026 (41 nations), NCSS 2026 international sponsors, memberships in APCERT/FIRST/OIC-CERT. SecurityStudies reports Malaysia's participation in military exercises (Keris Strike 31/2026, 2,800 personnel; Pacific Partnership 2026, 9 nations) — defence-domain, not cyber-drill, but sustains the multinational exercise relationship pattern.
- **Source:** https://www.nacsa.gov.my/cyber_games_2025.php (unchanged); SecurityStudies Malaysia Report 4 Sep 2026
- **Confidence:** Medium — no new cyber-exercise data
- **Analysis:** International cyber exercise portfolio unchanged; multinational military exercise activity (non-cyber) continues in parallel.

### PIR-OPP002-001: Playbook Budget Allocation
- **Priority:** Critical
- **Previous Status:** Partial
- **Current Status:** Partial (no change)
- **Finding:** No tender/RFP found for the RM 150K Cyber Crisis Communication Playbook. ePerolehan unreachable (HTTP 000). No RFP notice on NACSA portal. Budget 2027 (9 Oct) is the next funding-cycle observation point.
- **Source:** No new source found
- **Confidence:** Low — no new OSINT data
- **Analysis:** Procurement status remains OSINT-limited. Third cycle without ePerolehan access; alternative tender aggregators have yielded nothing across cycles.

### PIR-OPP002-002: Existing MKN Crisis Protocols
- **Priority:** High
- **Previous Status:** Resolved (updated — NCCMP staleness identified)
- **Current Status:** Resolved (staleness CONFIRMED — 2nd cycle)
- **Finding:** NCCMP page re-extracted 7 Sep 2026: still references 10 CNII domains ("defence and security; banking and finance; information and communications; energy; transportation; water; health; government services; emergency services; and food and agriculture") using old "CNII" terminology — vs the current 11-sector NCII (11th: Science, technology and innovation). No revision, no update notice. Pekeliling Am Bil.4/2022, Bil.3/2024, Bil.4/2024 remain the current public-sector circulars (per NACSA government page, unchanged).
- **Source:** https://www.nacsa.gov.my/nccmp.php (7 Sep 2026) vs https://www.nacsa.gov.my/NCII.php (7 Sep 2026)
- **Confidence:** High — official primary sources, direct page-to-page comparison, now replicated across 2 cycles
- **Analysis:** The staleness is stable, verifiable, and engagement-ready: the national crisis management plan does not cover the 11th NCII sector and uses pre-Act-854 terminology. This remains the strongest concrete value-add observation for CSCDC playbook positioning.

### PIR-OPP002-003: War Room Physical Infrastructure
- **Priority:** High
- **Previous Status:** Open
- **Current Status:** Open (no change)
- **Finding:** No public information on CSCDC/NACSA War Room specifications; no facility tenders found. Likely SULIT.
- **Source:** No new source found
- **Confidence:** Low — OSINT-unresolvable
- **Analysis:** Remains unresolvable without internal access.

### PIR-OPP002-004: Technical Liaison Role
- **Priority:** High
- **Previous Status:** Open
- **Current Status:** Open (no change)
- **Finding:** No publicly named CSCDC technical liaison. NACSA CE (IR. Dr. Megat Zuhairy Megat Tajuddin) remains the only publicly named directive-issuing authority (Section 13 Act 854).
- **Source:** No new source found
- **Confidence:** Low — internal/SULIT
- **Analysis:** OSINT-unresolvable.

### PIR-OPP002-005: Historical Cyber Incidents
- **Priority:** Medium
- **Previous Status:** Resolved (no change as of 31 Aug)
- **Current Status:** Resolved (UPDATED — SIGNIFICANT NEW INCIDENT DATA)
- **Finding:** **NEW #1 — Prasarana ransomware attack (25 Aug 2026):** Prasarana Malaysia Berhad (transport CNII operator) hit by ransomware attributed to RansomHub; data uploaded to dark web; PDP Commissioner's Office informed 26 Aug and instructed Prasarana to issue a Data Breach Notification by 29 Aug, which Prasarana complied with; Prasarana worked with NACSA and CSM; no disruption to public transport services. Volume of 316GB exfiltrated is single-chain (CSCDC-03 citing breach.house/securityonline). This is a SECOND Prasarana ransomware incident — the first (RansomHub, 2024) is in the standing baseline. Verified via SecurityStudies.info Malaysia Report (4 Sep 2026) full-body extraction + CSCDC-03 same-day record (theedgemalaysia.com, securityonline.info, breach.house chains).
  **NEW #2 — NACSA cyber attack warning (28 Aug 2026):** NACSA issued an alert on intrusions, DDoS, web defacement, and malware targeting numerous government and private organisations. NOT on the NC4 advisory portal; distinct from NACSA's legacy "Heightened Alert" pages (advisory10.php dated 27-10-2023; advisory11.php dated 29-01-2024 — both extracted and confirmed historical). Full text of the 28 Aug warning not located this cycle (search blackout).
  **UPDATE — NC4 advisory gap:** latest advisory remains NC4-ALR-2026-000006 (24 Jul, WordPress wp2shell). Gap = 45 days (24 Jul → 7 Sep; corrected from DeerFlow's 48 and CSCDC-03's 44 — both arithmetic errors). 2026 listing shows 5 advisories (000001, 000002, 000004, 000005, 000006); ID 000003 absent from the public listing — prior cycle's "6 advisories" claim is unconfirmed.
  **UPDATE — Threat level:** LOW, widget states "Last updated: 05 April 2024, 11:46AM" = 29 months static (corrected from "17 months" in DeerFlow and CSCDC-03 — stale figure propagation). The portal's daily "07 Sep 2026, 01 AM" stamp is statistics refresh, not threat-level status.
  **UPDATE — MyCERT:** 5,774 general incident classifications 2026 YTD — unchanged for a 3rd consecutive reading (24 Aug, 31 Aug, 7 Sep). 0 botnet drones. (DeerFlow failed to extract this; orchestrator extraction confirms.)
  **UPDATE — NC4 dashboard telemetry (full 4-period extraction):** Daily (7 Sep): all 6 categories ▼. Monthly (Sep): all ▼. Q3 (Jul-Sep): attribution ▲, vulnerable service ▲, others ▼. Annual 2026: attribution ▲, vulnerable service ▲, others ▼. Trend arrows are consistent with the prior cycle's Q3 reading; widget numeric semantics (current vs delta) are ambiguous in static extraction, so arrows are treated as the reliable qualitative signal. **Correction to DeerFlow:** the dashboard is NOT new — it existed in the 31 Aug cycle; this cycle adds the full 4-period extraction.
- **Source:** https://www.securitystudies.info/country/malaysia/reports/malaysia-report-2026-09-04-0640/ (full body extracted); INT-20260907-001-cscdc-03-infra-procurement.md (multi-source chain); https://www.nc4.gov.my/ + https://www.nc4.gov.my/alertAdvisory (7 Sep 2026); https://www.nacsa.gov.my/advisory10.php + advisory11.php (7 Sep 2026); https://www.mycert.org.my/en/statistics/ (7 Sep 2026)
- **Confidence:** High for NC4/MyCERT official data (L1); Medium for Prasarana incident (2 independent chains but aggregator-grade; direct outlet re-extraction blocked by search blackout); Medium for the 28 Aug NACSA warning (single secondary source, full text pending)
- **Analysis:** The Prasarana incident is the single most valuable crisis-protocol data point of the collection period: it exercised the statutory chain end-to-end (operator → PDP → public notification within 4 days of detection) with NACSA+CSM engaged — while no drill, playbook, or War Room activity is publicly visible. The national system is being tested by live fire, not rehearsal. The 45-day NC4 advisory silence, alongside a 28 Aug NACSA warning on a separate channel, shows the public alerting layer is fragmented — a concrete playbook-design gap.

### PIR-OPP002-006: Holding Statement Bank Scope
- **Priority:** Medium
- **Previous Status:** Partial
- **Current Status:** Partial (no change)
- **Finding:** No new holding statement bank details. NCSS 2026 Session 12 ("Malaysia's National Cyber Crisis Playbook: Are We Ready for a Major Cyber Attack?") remains the strongest public signal. The Prasarana Data Breach Notification (29 Aug) is a real-world artefact of crisis communication output — but no holding statement bank content is public.
- **Source:** https://cydes.my/ (unchanged); SecurityStudies Malaysia Report (notification timeline)
- **Confidence:** Medium — no new bank data
- **Analysis:** The incident's 26→29 Aug notification sequence (3 days from PDP report to public breach notification) offers a concrete timeline for calibrating holding statement assumptions in transport-sector scenarios.

### PIR-OPP002-007: Inter-Agency Crisis Coordination
- **Priority:** High
- **Previous Status:** Resolved (strengthened — NACSA CE directive model)
- **Current Status:** Resolved (strengthened — live incident evidence)
- **Finding:** The Prasarana response provides the first live observation of the inter-agency chain inside the collection period: operator → PDP Commissioner (26 Aug) → statutory Data Breach Notification (29 Aug) → NACSA + CSM engagement. The NC4-led 4-pillar CERT ecosystem and NACSA CE directive model stand. New wrinkle: the 28 Aug NACSA cyber attack warning circulated outside the NC4 advisory portal — the coordination architecture's public signalling is not channel-coherent.
- **Source:** SecurityStudies Malaysia Report (full body); INT-20260907-001-cscdc-03 record; https://www.nc4.gov.my/alertAdvisory (45-day silence)
- **Confidence:** Medium-High — official ecosystem structure (L1) + incident chain via 2 secondary chains (L4/L2)
- **Analysis:** Coordination worked through statutory/data-protection channels in the Prasarana case. What is NOT visible: whether the War Room Communication (Unit 4) function activated at all. That gap — statutory compliance vs crisis communication activation — is precisely the technical-to-communication interface gap (Gap #1 in the original framework analysis) made concrete.

### PIR-OPP002-008: War Room Activation Threshold
- **Priority:** Medium
- **Previous Status:** Open
- **Current Status:** Open (no change — reinforced by stasis evidence)
- **Finding:** Activation criteria remain unpublished. Reinforcing context: the National Cyber Threat Level has been LOW and static since 5 Apr 2024 (29 months) even through a live CNII ransomware incident (25 Aug) and an active NACSA warning (28 Aug) — i.e., the public threat-level instrument did not move during a real incident, suggesting it is not wired to incident response, or its update process is dormant. NC4 5-level scale (LOW→MODERATE→CAUTION→HIGH→CRITICAL) confirmed on the live portal.
- **Source:** https://www.nc4.gov.my/ (7 Sep 2026); SecurityStudies Malaysia Report
- **Confidence:** Medium — scale confirmed; criteria unpublished; non-movement during a live incident is an observable (T3 inference)
- **Analysis:** [ASSESSMENT] The static threat level through a live CNII incident is itself intelligence: the public escalation instrument and the incident response chain appear disconnected. A crisis communication playbook that keys off the national threat level would not have activated for Prasarana. This materially strengthens the case for defining War Room activation thresholds independent of the public threat level.

### PIR-OPP002-009: Rehearsal & Drill Schedule
- **Priority:** Medium
- **Previous Status:** Partial
- **Current Status:** Partial (no change)
- **Finding:** No rehearsal schedule announcements. NCSS 2026 simulation sessions remain the most recent public rehearsal activity. The RM 200K National Cyber Drill's status as primary War Room rehearsal vehicle remains unconfirmed.
- **Source:** https://cydes.my/ (unchanged)
- **Confidence:** Medium — no new data
- **Analysis:** Unchanged; Prasarana did the live testing instead.

### PIR-OPP002-010: International Coordination
- **Priority:** Low
- **Previous Status:** Partial
- **Current Status:** Partial (no change)
- **Finding:** No new international cyber crisis coordination agreements. Standing: CoE/INTERPOL (Cyber Games 2025), NATO CCDCOE (Locked Shields 2026), APCERT/FIRST/OIC-CERT memberships, bilateral MoUs.
- **Source:** https://www.mycert.org.my/en/statistics/ (memberships confirmed, 7 Sep 2026)
- **Confidence:** High — prior findings hold on official source
- **Analysis:** Unchanged.

## Cross-PIR Synthesis

Four themes this cycle:

1. **Live fire replaced rehearsal.** The Prasarana incident (25 Aug 2026) exercised the national cyber crisis chain end-to-end — operator reporting, PDP statutory notification, public breach disclosure within 4 days, NACSA+CSM engagement — while the formal rehearsal pipeline (RM 200K drill, RM 150K playbook, War Room) shows zero public activity: no dates, no procurement, no announcements, ePerolehan unreachable. The asymmetry is the message: Malaysia's crisis system is currently validated by incidents, not exercises. For CSCDC positioning, the after-action methodology that exists in war-room practice (scenario reconstruction, timeline analysis, communication audit) applies directly to Prasarana-type incidents, and a drill designed from the 2026 real-incident classes (transport-sector ransomware first) is a stronger pitch than a generic scenario catalogue.

2. **The public alerting layer is fragmented and dormant.** Three channels, three behaviours: NC4 advisory portal silent 45 days (and the threat level static 29 months — it did not move during the Prasarana incident); NACSA issuing a 28 Aug warning through a non-NC4 channel (full text still unlocated); legacy NACSA "Heightened Alert" pages (Oct 2023, Jan 2024) still occupying the homepage announcement block. A national crisis communication playbook must specify which channel speaks, when, and with what authority — today's observable is three channels with no visible coordination logic. This is a verifiable, citation-ready gap CSCDC can put on the table.

3. **Structural staleness is compounding.** NCCMP (10 CNII domains vs 11 NCII sectors, 2-cycle-confirmed), the static threat level (29 months), the 45-day advisory silence, and the CSM portal outage (all service pages down) are individually minor; together they describe an ecosystem whose public-facing governance layer is not being actively maintained even as the incident surface (Prasarana, QR-fraud losses RM28.67M H1) grows. This is the environment in which Unit 4's 30-minute holding statement KPI would have to operate.

4. **Collection infrastructure:** DeerFlow pro returned its first full-format output since 24 Aug, but with 4 factual errors and 1 fabricated URL — every load-bearing number in this record comes from orchestrator L1 extraction, with DeerFlow used as scaffold only. Search backends remain mostly blacked out (CSCDC-03 got intermittent successes earlier in the same window; this cycle's own queries all failed). Direct URL extraction remains the reliable primary path.

## Intelligence Gaps

1. **Arahan MKN No.24 status** — 3rd cycle of the same T3 assessment; requires HUMINT. (Critical, ongoing)
2. **War Room activation during Prasarana** — did Unit 4/War Room activate, or was the response purely statutory? No public evidence. (Critical, new)
3. **28 Aug NACSA warning full text + channel** — why is it absent from NC4's advisory portal? (High, new)
4. **NC4 advisory dormancy cause** — 45 days; resource, strategy, or process failure? (High, ongoing)
5. **Prasarana 316GB figure** — single-chain; corroborate against The Edge/securityonline directly next cycle. (Medium, new)
6. **Procurement (RM 200K + RM 150K)** — ePerolehan unreachable in every attempt; Budget 2027 (9 Oct) is the next public funding window. (High, ongoing)
7. **Drill dates/evaluation framework/activation thresholds/War Room specs** — all SULIT or unpublished. (Ongoing)
8. **CSM outage** — cause/duration unknown; blocks EXCON re-verification. (Medium, new)
9. **NC4-ALR-2026-000003** — absent from public listing; reconcile prior cycle's "6 advisories" claim. (Low, bookkeeping)
10. **AISCF launch date** — not established in any validated source (DeerFlow's "9 Jul" rejected); fix in next cycle's collection. (Low, metadata)

## Recommendations

1. **🔴 HIGHEST PRIORITY — Anchor CSCDC crisis-protocol positioning to the Prasarana incident.** Prepare a one-page after-action reconstruction of the 25-29 Aug chain (detection → PDP notification → public disclosure → NACSA/CSM engagement) mapped against Unit 4's War Room functions, explicitly noting which steps had no public-facing communication component. This converts a hypothetical pitch ("when the War Room activates...") into a live case study that already happened.

2. **🟠 Exploit the 10 Sep Cyber Security Summit (3 days away).** NACSA speaker confirmed (Nuraishah Mokhtar). Monitor post-event coverage for drill, playbook, or CSCDC signals; the summit is the nearest-term public NACSA forum.

3. **🟠 Surface the alerting-channel gap in engagement.** Three verifiable facts: NC4 advisory silence (45 days), static threat level (29 months, unmoved through a live CNII incident), and a NACSA warning outside the NC4 channel (28 Aug). The playbook design conversation should start here — this is Gap #1 (technical-to-communication interface) made visible in the public domain.

4. **🟡 Keep NCCMP staleness as the standing value-add observation** — 2-cycle-confirmed against the live page (10 domains vs 11 sectors; "CNII" vs "NCII" terminology).

5. **🟡 HUMINT queue unchanged:** Arahan MKN No.24 status (3rd cycle flagged); Prasarana War Room activation question (new, high value).

6. **🟡 Budget 2027 (9 Oct) watch** — drill/playbook allocations may surface in the budget debate coverage; ePerolehan remains the hard blocker for procurement-level visibility.

7. **🟢 Infrastructure hygiene:** re-test CSM portal and ePerolehan next cycle; obtain full text of the 28 Aug NACSA warning; corroborate the 316GB figure; establish AISCF launch date. Maintain orchestrator-validation of DeerFlow output as a hard gate — this cycle it caught a 10% arithmetic error, a stale figure, a duplicated metrics row, a false novelty claim, and a fabricated URL.

## PIR Resolution Status Table

| PIR ID | Priority | Previous Status | Current Status | Confidence | Change |
|--------|----------|-----------------|----------------|------------|--------|
| PIR-OPP007-001 | Critical | Resolved (strengthened) | Resolved (no change) | High | No delta |
| PIR-OPP007-002 | Critical | Partial — T3 | Partial — T3 (unchanged) | Medium | No.24 still unconfirmed; 3rd cycle |
| PIR-OPP007-003 | High | Resolved (strengthened) | Resolved (re-verified) | High | NCII page re-verified |
| PIR-OPP007-004 | High | Resolved (strengthened) | Resolved (no change) | High | Prasarana reinforces ransomware scenario class |
| PIR-OPP007-005 | High | Resolved (strengthened) | Resolved (not re-verifiable — CSM down) | Medium | CSM portal outage blocks refresh |
| PIR-OPP007-006 | Medium | Partial | Partial (no change) | Medium | No after-action publications |
| PIR-OPP007-007 | Medium | Open | Open | Low | No new data |
| PIR-OPP007-008 | Medium | Partial | Partial (no change) | Medium | Summit 10 Sep = new monitoring point |
| PIR-OPP007-009 | Low | Open | Open | Low | ePerolehan still unreachable |
| PIR-OPP007-010 | Low | Partial | Partial (no change) | Medium | No new cyber-exercise data |
| PIR-OPP002-001 | Critical | Partial | Partial (no change) | Low | No procurement data |
| PIR-OPP002-002 | High | Resolved (stale) | Resolved (stale — 2nd cycle confirmed) | High | Staleness replicated |
| PIR-OPP002-003 | High | Open | Open | Low | No new data |
| PIR-OPP002-004 | High | Open | Open | Low | No new data |
| **PIR-OPP002-005** | **Medium** | **Resolved** | **Resolved (UPDATED — Prasarana 25 Aug, 28 Aug warning, 45-day gap)** | **Medium-High** | **Significant new incident data** |
| PIR-OPP002-006 | Medium | Partial | Partial (no change) | Medium | Prasarana timeline = calibration data |
| **PIR-OPP002-007** | **High** | **Resolved (strengthened)** | **Resolved (strengthened — live chain evidence)** | **Medium-High** | Prasarana chain observed live; channel incoherence |
| **PIR-OPP002-008** | **Medium** | **Open** | **Open (stasis evidence added)** | **Medium** | Threat level unmoved through live incident [T3] |
| PIR-OPP002-009 | Medium | Partial | Partial (no change) | Medium | No new data |
| PIR-OPP002-010 | Low | Partial | Partial (no change) | High | No new data |

**Summary:** 20 PIRs. 8 Resolved (3 with updated evidence), 7 Partial, 5 Open. No status regressions. Cycle signature: live incident (Prasarana) + alerting-layer dormancy (NC4 45 days / 29-month threat level) + structural staleness replication (NCCMP 2nd cycle). DeerFlow pro full-format output achieved with orchestrator corrections; no fabricated content shipped.

## TOP 3 PIR SUGGESTIONS FOR NEXT CYCLE (AUTO-APPROVED)

1. **Suggestion:** Prasarana incident follow-through — obtain direct outlet coverage (The Edge Malaysia, securityonline.info), confirm the 316GB figure, and scan for NACSA/CSM/PDP follow-on signals (enforcement, transport-sector advisories, post-incident statements).
   **Rationale:** The incident is the cycle's highest-value engagement hook and is currently sourced via two secondary chains; direct outlet extraction plus any after-action signals would upgrade it toward T1-grade and may reveal War Room behaviour.
   **Search Queries:** "Prasarana" ransomware site:theedgemalaysia.com, "Prasarana" "RansomHub" 2026, "Prasarana" "data breach notification" August 2026, NACSA CSM Prasarana incident response

2. **Suggestion:** Obtain the full text of NACSA's 28 Aug 2026 cyber attack warning and map the NACSA-vs-NC4 advisory channel relationship.
   **Rationale:** A national-level warning outside the NC4 advisory pipeline during a 45-day NC4 silence is a concrete alerting-coordination gap — directly relevant to the playbook's channel-authority design and citable in CSCDC engagement.
   **Search Queries:** NACSA "cyber attack" warning "28 August 2026", site:nacsa.gov.my kenyataan media Ogos 2026, NACSA media statement intrusion DDoS defacement 2026, "NACSA" alert government private organisations August 2026

3. **Suggestion:** Post-event coverage of Cyber Security Summit Malaysia 2026 (10 Sep, InterContinental KL) for drill/crisis-protocol signals and NACSA leadership visibility.
   **Rationale:** Nearest-term public NACSA forum; 150+ CISOs/officials; any drill, playbook, or War Room announcements would surface here first. Time-boxed to 10-12 Sep.
   **Search Queries:** "Cyber Security Summit Malaysia 2026" NACSA, "Cyber Security Summit" InterContinental September 2026, Nuraishah Mokhtar NACSA 2026, "cyber security reimagined" Malaysia summit coverage

---

---CVS BLOCK---
Claim: Prasarana Malaysia Berhad suffered a ransomware attack on 25 Aug 2026 attributed to RansomHub; PDP Commissioner's Office informed 26 Aug; Data Breach Notification issued by 29 Aug as instructed; NACSA and CSM engaged; no public transport disruption
Source: SecurityStudies.info Malaysia Security Report 4 Sep 2026 (https://www.securitystudies.info/country/malaysia/reports/malaysia-report-2026-09-04-0640/ — full article body extracted) + CSCDC-03 same-day record INT-20260907-001 (citing theedgemalaysia.com, securityonline.info, breach.house)
Source Level: L4 (secondary report, full body) + L2 (internal validated cron record, multi-source)
Tier: T2
Validation Status: Partially Verified — 2 independent chains agree on all core facts (dates, actor, notification chain); direct outlet re-extraction blocked by search blackout; 316GB volume single-chain
Confidence Score: 6 (Authority:1 Traceability:2 Recency:2 Consistency:2 Completeness:1)
Action Required: Corroboration — direct outlet extraction next cycle to confirm 316GB and upgrade
---END CVS BLOCK---

---CVS BLOCK---
Claim: NC4 latest advisory remains NC4-ALR-2026-000006 (24 Jul 2026) — 45-day advisory gap as of 7 Sep 2026; 2026 listing shows 5 advisories with ID 000003 absent from the public listing
Source: NC4 Advisory portal (https://www.nc4.gov.my/alertAdvisory — extracted 7 Sep 2026)
Source Level: L1 (official government portal)
Tier: T2
Validation Status: Verified (official primary source, live extraction; arithmetic stated: 24 Jul → 7 Sep = 45 days; corrects DeerFlow's 48 and CSCDC-03's 44)
Confidence Score: 7 (Authority:2 Traceability:2 Recency:2 Consistency:2 Completeness:1)
Action Required: None — prior cycle's "6 advisories" count flagged as unconfirmed (only 5 IDs ever listed)
---END CVS BLOCK---

---CVS BLOCK---
Claim: National Cyber Threat Level is LOW, widget last updated 05 April 2024 — 29 months static as of 7 Sep 2026; the level did not change through the 25 Aug Prasarana CNII incident or the 28 Aug NACSA warning
Source: NC4 Portal (https://www.nc4.gov.my/ — "Last updated: 05 April 2024, 11:46AM" on threat level widget; page-level daily refresh 07 Sep 2026 01 AM)
Source Level: L1 (official government portal)
Tier: T2
Validation Status: Verified (official primary source; 29-month figure computed: 5 Apr 2024 → 7 Sep 2026; corrects "17 months" in DeerFlow and CSCDC-03 — stale-figure propagation)
Confidence Score: 7 (Authority:2 Traceability:2 Recency:2 Consistency:2 Completeness:1)
Action Required: None — cross-workspace inconsistency (17 vs 29 months) flagged to CSCDC-03 record owner for correction
---END CVS BLOCK---

---CVS BLOCK---
Claim: NCCMP still references 10 CNII domains using "CNII" terminology while the current NCII structure has 11 sectors — staleness confirmed for a 2nd consecutive cycle (7 Sep 2026)
Source: NACSA NCCMP page (https://www.nacsa.gov.my/nccmp.php) vs NACSA NCII page (https://www.nacsa.gov.my/NCII.php) — both extracted 7 Sep 2026; prior comparison 31 Aug 2026
Source Level: L1 (official government records, direct page-to-page comparison, replicated across 2 cycles)
Tier: T2
Validation Status: Verified (official primary sources, direct comparison)
Confidence Score: 7 (Authority:2 Traceability:2 Recency:2 Consistency:2 Completeness:1)
Action Required: None — standing value-add observation for CSCDC engagement
---END CVS BLOCK---

---CVS BLOCK---
Claim: MyCERT reports 5,774 general incident classifications for 2026 YTD — unchanged across 3 consecutive readings (24 Aug, 31 Aug, 7 Sep 2026); 0 botnet drones
Source: MyCERT (https://www.mycert.org.my/en/statistics/ — extracted 7 Sep 2026)
Source Level: L1 (official government CERT)
Tier: T2
Validation Status: Verified (official primary source; DeerFlow failed to extract this — orchestrator extraction used)
Confidence Score: 7 (Authority:2 Traceability:2 Recency:2 Consistency:2 Completeness:1)
Action Required: None
---END CVS BLOCK---

---CVS BLOCK---
Claim: Arahan MKN No.24 is likely still active — no cancellation notice found across NACSA homepage (7 Sep), MKN portal, and the No.26 cancellation PDF (which references only No.26); dual-framework period assessment carries forward
Source: NACSA homepage (https://www.nacsa.gov.my/ — Last Updated 7 Sep 2026), MKN portal (https://www.mkn.gov.my/), No.26 cancellation PDF (full text extracted, prior cycle)
Source Level: L1 (official portals) + L5 (analytical inference from absence)
Tier: T3 [ASSESSMENT]
Validation Status: Inferred (analytical interpretation from absence of evidence; 3rd cycle of same finding)
Confidence Score: 5 (Authority:2 Traceability:2 Recency:2 Consistency:1 Completeness:0)
Action Required: Human review — HUMINT confirmation via NACSA/MKN classified channel remains the top governance gap
---END CVS BLOCK---

---CVS BLOCK---
Claim: NACSA issued a cyber attack warning on 28 Aug 2026 (intrusions, DDoS, web defacement, malware targeting government and private organisations) that is NOT present on the NC4 advisory portal; NACSA homepage "Heightened Alert" pages are legacy items dated 27-10-2023 and 29-01-2024
Source: SecurityStudies.info Malaysia Report 4 Sep 2026 (full body extracted) + NACSA advisory10.php and advisory11.php (both extracted 7 Sep 2026, dates confirmed from page bodies)
Source Level: L4 (secondary, full body) + L1 (official legacy pages for the negative finding)
Tier: T2
Validation Status: Partially Verified — warning existence corroborated by one secondary source; full text and issuing channel not located (search blackout)
Confidence Score: 5 (Authority:1 Traceability:2 Recency:2 Consistency:1 Completeness:1)
Action Required: Corroboration — obtain full text and channel of the 28 Aug warning next cycle
---END CVS BLOCK---

---CVS BLOCK---
Claim: DeerFlow pro dispatch succeeded this cycle (thread 3dc52be4, 23,986 bytes, full-format output — first since 24 Aug) but contained 4 factual errors (48→45 days; 17→29 months; Q3 metrics duplicated from monthly; "dashboard is NEW" false), 1 fabricated URL (nacsa.gov.my/directive26.php), and 1 unverified date (AISCF "9 Jul 2026" = NQAIC MoU date conflation) — all caught and corrected by orchestrator validation against independent L1 extractions
Source: DeerFlow output file /tmp/pir-CSCDC-05-output.txt + orchestrator extractions (this record's CVS blocks)
Source Level: L5 (AI-generated output) validated against L1
Tier: T3 [ASSESSMENT]
Validation Status: Verified (dispatch confirmed; error inventory compiled line-by-line)
Confidence Score: 7 (Authority:2 Traceability:2 Recency:2 Consistency:2 Completeness:1)
Action Required: None — DeerFlow output remains a scaffold-only input; hard orchestrator validation gate confirmed necessary
---END CVS BLOCK---

---CVS BLOCK---
Claim: Cyber Security Summit Malaysia 2026 scheduled 10 Sep 2026 (InterContinental KL, NACSA speaker Nuraishah Mokhtar); Budget 2027 to be tabled 9 Oct 2026 — two near-term monitoring windows for drill/crisis funding signals
Source: INT-20260907-001-cscdc-03-infra-procurement.md (citing malaysiasun.com/PRNewswire) + INT-20260907T0126-001 CSCDC-02 record (citing The Star, 6 Sep 2026)
Source Level: L2 (internal validated records with named secondary sources)
Tier: T2
Validation Status: Partially Verified — internal single-chain per item, outlets named
Confidence Score: 6 (Authority:1 Traceability:2 Recency:2 Consistency:2 Completeness:1)
Action Required: Corroboration — verify via event page / pre-budget coverage next cycle
---END CVS BLOCK---
