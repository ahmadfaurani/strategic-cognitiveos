---
id: INT-20260904-004
record_type: intelligence
title: "Cohort Portfolio Register Reconciliation — MEISAC × NanoSec × Aras Discovery + PRG-001–005 Status Audit"
created_at: 2026-09-04T03:54:00+00:00
updated_at: 2026-09-04T03:54:00+00:00
owner: faurani-jaafar
intelligence_type: strategic
status: active
priority: high
sensitivity: internal
lifecycle_state: canonical
confidence: high
tags:
  - domain/governance
  - domain/portfolio-governance
  - domain/cognitiveos-operations
  - domain/sovereign-ai
  - domain/cybersecurity-productisation
  - intelligence/operational
  - intelligence/operational
source:
  type: direct-analysis
  reference: "Subagent directive C: CognitiveOS Discovery — Cohort Portfolio Register Reconciliation"
summary: "Full reconciliation of PRG-001 through PRG-005 against actual execution state as of 2026-09-04. MEISAC × NanoSec × Aras cohort programme does NOT exist anywhere in CognitiveOS. NanoSec (ORG-20260904-001) is a pentesting resource, not a cohort partner. Two programmes have passed kill dates (PRG-002, PRG-003). One programme has passed its kill date (PRG-004). PRG-001 workshop dates (Sep 2-3) have passed with no execution evidence ingested. PRG-005 remains design-only."
strategic_significance: "Identifies zombie/stalled programmes, confirms MEISAC non-existence, provides kill-date enforcement recommendations."
mission_alignment:
  - sovereign-ai
  - governance
  - intelligence-enablement
related_records:
  - GOV-PORTFOLIO-REGISTER-001
  - GOV-STRATEGIC-OBJECTIVE-COHORT-PROGRAMME-001
  - ORG-20260904-001
  - INIT-20260813-001
  - INIT-20260804-004
  - INIT-20260803-002
  - INIT-20260611-001
  - INIT-20260808-003
---

# Cohort Portfolio Register Reconciliation

**Date:** 2026-09-04 | **Analyst:** Subagent (Directive C) | **Scope:** Full CognitiveOS repository

---

## 1. MEISAC × NanoSec × Aras Cohort — Discovery Results

### 1.1 MEISAC Search

**Result:** ZERO occurrences of "MEISAC" or "meisac" found anywhere in the CognitiveOS repository.

- Grep across all `.md`, `.csv`, `.yaml`, `.yml` files: **no matches**
- Case-insensitive recursive grep across entire repository: **no matches**
- No initiative, stakeholder, organization, decision, commitment, action, or intelligence record references MEISAC

**Conclusion:** MEISAC does not exist in CognitiveOS. No prior intake, no reference, no context clue. What MEISAC is remains unknown from this repository alone — no expansion, acronym definition, or contextual mention exists.

### 1.2 NanoSec in CognitiveOS

**Result:** NanoSec exists as ORG-20260904-001 (created today, 2026-09-04T02:52 UTC).

- **Identity:** NanoSec Community Team — a cybersecurity community team
- **Purpose:** Pentesting resource for GovSec TIP B1 Security Remediation gate (Sep 15)
- **Relationship:** Replaces the OVERDUE external security assessor
- **Engagement prerequisite:** Hadri must deliver NanoSec Collaboration Email for CyberDSA
- **Related records:** DEC-20260904-002, ACT-20260904-002, ACT-20260904-003, INIT-20260810-003

### 1.3 MEISAC × NanoSec × Aras Cohort — Verdict

**Does a MEISAC × NanoSec × Aras cohort programme exist in CognitiveOS?**

**NO.** Zero evidence. No initiative record, no portfolio register entry, no stakeholder, no conversation, no decision, no commitment, no action, no intelligence record. The term "MEISAC" appears nowhere. NanoSec was only created today as a pentesting resource, not a cohort partner.

**Is it confused with the NanoSec pentesting engagement?**

**Partially — but they are distinct.** NanoSec (ORG-20260904-001) is explicitly a pentesting resource for GovSec TIP B1, not a cohort programme. The DAF directive (2026-09-04 02:52 UTC) correctly identified NanoSec as separate from any cohort. There is no cohort programme involving NanoSec in the Portfolio Register (PRG-001 through PRG-005). The confusion risk is low because the NanoSec record is clearly scoped to pentesting.

**What is MEISAC?**

Unknown from CognitiveOS sources. No contextual clues exist. If MEISAC is a real entity DAF intends to partner with, it has not been ingested into CognitiveOS. A dedicated intake event would be required to establish MEISAC as a stakeholder/organization and create the cohort programme in the Portfolio Register.

### 1.4 Trifecta / Third Cohort Search

**Result:** ZERO occurrences of "trifecta" or "third cohort" found anywhere in the repository.

---

## 2. Portfolio Register Reconciliation

### Assessment Date: 2026-09-04 (UTC)

### Current date context: Sep 4, 2026 (UTC). All kill dates assessed against this date.

---

### PRG-001: PERJASA AI Cohort Workshop

| Field | Value |
|-------|-------|
| **Programme** | PERJASA AI Cohort Workshop |
| **Recorded Status** | 🟢 Active |
| **Actual Status** | ⚠️ UNKNOWN — kill date passed, no execution evidence ingested |
| **Owner** | DAF |
| **Next Action** | Logistics execution (venue, materials, team brief) |
| **Deadline** | Aug 29 |
| **Kill Date** | Sep 2 (hard) |
| **Kill Date Passed?** | **YES** — Sep 2 has passed (2 days ago) |
| **Next Action Status** | UNKNOWN — no evidence of logistics completion |
| **Initiative Record** | INIT-20260813-001 (exists, status: active) |
| **Commitment** | COM-20260813-001 (status: active, expected delivery: Sep 3) |
| **Risk** | RSK-20260813-001 — **Resolved** (date confirmed Aug 18) |

**Analysis:**

The workshop was confirmed for Sept 2–3, 2026 (RSK-20260813-001 resolved on Aug 18). The hard kill date was Sep 2. As of Sep 4, the workshop dates have passed. However:

- **No execution evidence ingested.** No post-workshop report, no outcome record, no daily memory entry for Sep 2-3 has been found in CognitiveOS. The most recent daily memory is `memory/2026-09-03.md` which covers the MAPO intake and C1/C2 directives — no mention of PERJASA workshop outcomes.
- **No status update to COM-20260813-001** — still shows "Active" with expected delivery Sep 3.
- **No completion evidence** — the commitment requires "Workshop executed on confirmed dates" as completion evidence. None logged.
- **Two scenarios:** (a) Workshop happened but outcomes not yet ingested (likely if DAF was physically at the workshop Sep 2-3 and hasn't had time to ingest), or (b) Workshop did not happen or was delayed (possible given no pre-workshop logistics confirmation evidence).

**Verdict:** KILL DATE PASSED. Status requires immediate update. If workshop was executed, intake the evidence and mark COM-20260813-001 as delivered. If not executed, mark PRG-001 as 💀 Killed and archive.

**Recommendation:** DAF to confirm workshop status IMMEDIATELY. Update COM-20260813-001 and INIT-20260813-001. If executed, trigger 90-day post-workshop continuation (COM-20260813-003).

---

### PRG-002: CSM × Aras GTM Partnership

| Field | Value |
|-------|-------|
| **Programme** | CSM × Aras GTM Partnership |
| **Recorded Status** | 🟡 Stalled |
| **Actual Status** | 💀 KILLED — kill date passed 13 days ago |
| **Owner** | DAF |
| **Next Action** | Confirm Aisha PIC + POC scope with En. Zulfeka |
| **Deadline** | Aug 22 |
| **Kill Date** | Aug 22 |
| **Kill Date Passed?** | **YES** — Aug 22 passed 13 days ago |
| **Next Action Status** | UNKNOWN — no evidence of Aisha PIC confirmation or POC scope agreement |
| **Initiative Record** | INIT-20260804-001 (CSM × Aras VoronCitadel Joint GTM Activation) |

**Analysis:**

The kill criteria are explicit: "If Aisha PIC not confirmed + POC scope not agreed by Aug 22, CyberDSA silver sponsorship (RM50K) is at risk. Kill = withdraw sponsorship + pause GTM." The kill date passed on Aug 22 with no evidence in CognitiveOS that:

- Aisha was confirmed as PIC (RSK-20260815-001 mentions Aisha was "proposed" as PIC but no confirmation record found)
- POC scope was agreed with Zulfeka
- The kill decision was formally logged

However, CSM partnership activity continues extensively across other workstreams — INIT-20260804-004 (Co-Design Lab Cohort 01), multiple stakeholders (STK-20260812-001 through 017), DEC-20260812-001 (MyCERT accepts Cohort 01), CONV-20260817-002 (Hadri's MyCERT onboarding), etc. The CSM relationship is alive; the specific GTM partnership gate (Aisha PIC + POC scope) appears to have been bypassed rather than formally killed.

**Verdict:** KILL DATE PASSED. No formal kill decision logged. This is a **zombie gate** — the specific next action (Aisha PIC + POC scope) was not completed by Aug 22, but no kill was enforced. The broader CSM partnership continues through other channels, creating ambiguity about whether PRG-002 is alive or dead.

**Recommendation:** Formally update PRG-002 status. Either: (a) Mark as 💀 Killed — the GTM partnership gate failed, withdraw sponsorship, pause GTM track; or (b) If the GTM was absorbed into the broader CSM Joint Operating Model (INIT-20260813-005) and is no longer a separate programme, mark as "Merged" and update the register. Do not leave it as 🟡 Stalled — that's a zombie.

---

### PRG-003: PMO AI Cohort Initiative

| Field | Value |
|-------|-------|
| **Programme** | PMO AI Cohort Initiative |
| **Recorded Status** | 🔴 Stalled |
| **Actual Status** | 💀 KILLED — kill date passed 10 days ago |
| **Owner** | DAF |
| **Next Action** | Send re-engagement email — "connect by Aug 25 or pause" |
| **Deadline** | Aug 25 |
| **Kill Date** | Aug 25 |
| **Kill Date Passed?** | **YES** — Aug 25 passed 10 days ago |
| **Next Action Status** | NO EVIDENCE — no re-engagement email sent (no conversation record found) |
| **Initiative Record** | No dedicated INIT record found for "PMO AI Cohort Initiative" |

**Analysis:**

The kill criteria are explicit: "If no response by Aug 25, formally park. Send: 'We'll pause this initiative and revisit when timing aligns.' Free the cognitive slot. No zombie programmes."

The Strategic Objective document (GOV-STRATEGIC-OBJECTIVE-COHORT-PROGRAMME-001) explicitly labels PRG-003 as "Status: Zombie. Kill Aug 25." Yet the Portfolio Register still shows it as 🔴 Stalled, not ⛔ Parked or 💀 Killed.

The ESF-20260829-001 DAF Strategic Leader Profile (Aug 29) identifies this as a known gap: "PRG-003 passed kill date with no decision logged" and lists "Enforce PRG-003 kill decision — first kill-date enforcement test" as a DoD-1 action with Sep 7 deadline.

No initiative record, no stakeholder record, no conversation record, no commitment, and no action record exists for a "PMO AI Cohort Initiative." This programme appears to have never been formally ingested beyond the Portfolio Register entry itself.

**Verdict:** KILL DATE PASSED. This is the **first documented zombie programme** in the register. The kill criteria were defined but never enforced. The ESF profile flagged it on Aug 29 but as of Sep 4 it remains unenforced.

**Recommendation:** IMMEDIATE enforcement. Update PRG-003 to ⛔ Parked (formal pause, cognitive slot freed). Log the decision. This is the first kill-date enforcement test — failing it sets a precedent that kill dates are advisory, not binding.

---

### PRG-004: R.I.S.I.K × UiTM Collaboration

| Field | Value |
|-------|-------|
| **Programme** | R.I.S.I.K × UiTM Collaboration |
| **Recorded Status** | 🟡 Planned |
| **Actual Status** | ⚠️ KILL DATE PASSED — Phase 0 deliverables not confirmed built |
| **Owner** | DAF |
| **Next Action** | Build Phase 0 deliverables (daily collection + claim register + sample brief) |
| **Deadline** | Sep 3 |
| **Kill Date** | Sep 3 (push UiTM session if not ready) |
| **Kill Date Passed?** | **YES** — Sep 3 passed 1 day ago |
| **Next Action Status** | UNKNOWN — no evidence Phase 0 deliverables are complete |
| **Initiative Record** | INIT-20260803-002 (exists, status: active, readiness: collaboration-framework-agreed) |

**Analysis:**

The kill criteria state: "If Phase 0 deliverables (daily collection script, claim register, sample brief) not built by Sep 3, push UiTM session to Sep 20. Do not walk in with concepts only."

The STRAT-20260807-001 RISIK Operational Development Plan shows Phase 0 deliverables were planned with W1 (Week 1) deadlines including "Daily collection operational on schedule" and "Claim register live and populated." The strategy document references these as not yet built ("❌ Does not exist" for claim register).

However, DeerFlow (INIT-20260611-001) has been operational since July 2026 with 100% success rate on 25-source collection. The daily collection capability exists as infrastructure. Whether the claim register and sample brief were built specifically for RISIK Phase 0 by Sep 3 is unclear — no completion evidence was found.

The initiative record (INIT-20260803-002) shows significant progress on framework and doctrine (collaboration framework agreed, cost structure formalised, PRISM 2.0 integration context established) but Phase 0 operational deliverables are not marked as complete. The "Operational Development Alignment Session conducted" is marked as ❓ (unknown).

**Verdict:** KILL DATE PASSED (1 day ago). The contingency action is clear: push UiTM session to Sep 20. This is not a kill — it's a slip. The programme has substantial momentum (RM5M cost structure, MCMC funding pathway, PRISM 2.0 integration, academic validation).

**Recommendation:** Update PRG-004 status to reflect Sep 3 kill date triggered. Execute the contingency: push UiTM working session to Sep 20. Confirm whether Phase 0 deliverables exist (DeerFlow collection is operational; claim register and sample brief need verification). Update next action to "Complete Phase 0 deliverables by Sep 20 — UiTM session rescheduled."

---

### PRG-005: VORON-C2 Internship Programme

| Field | Value |
|-------|-------|
| **Programme** | VORON-C2 Internship Programme |
| **Recorded Status** | ⚪ Design-only |
| **Actual Status** | ⚪ Design-only — confirmed accurate |
| **Owner** | DAF |
| **Next Action** | Launch decision review |
| **Deadline** | Oct 1 |
| **Kill Date** | Oct 1 |
| **Kill Date Passed?** | NO — 27 days remaining |
| **Next Action Status** | No launch decision evidence |
| **Initiative Record** | INIT-20260808-003 (Red Team Division — VORON-C2 is a sub-component) |

**Analysis:**

The VORON-C2 Intern Programme document (projects/voron-c2/VORON-C2-INTERN-PROGRAMME.md) is a comprehensive 12-week programme design with 3 phases, 3-4 interns per cohort, detailed weekly plans, budget (RM 25K-37K per cohort), evaluation criteria, and scaling model. It is design-complete but has not launched.

The Red Team Division (INIT-20260808-003, projects/red-team-division/) references the VORON-C2 skunkworks intern programme as a component:
- "Skunkworks Cohort 1 onboarded" is listed as a Month 6 milestone
- "Skunkworks Cohort 2 onboarded" at Month 12
- JD for Head of Red Team Division references overseeing "VORON-C2 Skunkworks intern programme — approval process, mentorship, cohort selection"

The Red Team Division itself is a Draft v0.1 structure (Aug 8, 2026) — it has not been launched either. The VORON-C2 intern programme is correctly classified as Design-only. Kill date (Oct 1) has not passed.

**Is this a cohort programme?** YES — it uses cohort terminology explicitly (3-4 interns per cohort, Cohort 1/2/3+, cohort roles, cross-training). However, it is a cybersecurity infrastructure build programme, not a sovereign AI cohort programme in the sense of the Strategic Objective. It feeds talent into the Red Team Division, not into the Alumni Community described in GOV-STRATEGIC-OBJECTIVE-COHORT-PROGRAMME-001.

**Verdict:** Status accurate. No action needed until Oct 1 kill date.

**Recommendation:** No immediate action. Monitor for Oct 1 launch decision review. If Red Team Division has not launched by Oct 1, archive VORON-C2 design docs and revisit post-CyberDSA as specified.

---

## 3. Additional Cohort References Found

### Programmes NOT in the Portfolio Register

The following cohort-related programmes exist in CognitiveOS but are NOT registered in the Portfolio Register:

1. **AI Systems Co-Design Lab (Cohort 01) — CSM Partnership** (INIT-20260804-004)
   - Status: Active — Prototype
   - 23 MyCERT personnel onboarded (Aug 12-17)
   - This is the CSM/MyCERT track of the Co-Design Lab
   - **Should this be in the Portfolio Register?** It fits the cohort programme definition and has more active momentum than PRG-002 or PRG-003. Currently tracked through INIT-20260804-004 and COM-20260812-001.

2. **R.I.S.I.K Cohort Programme** (referenced in DEC-20260818-012, COM-20260818-001)
   - Mentioned as "practitioner/SME development platform" and "long-term pathway"
   - This is the RISIK equivalent of the PERJASA alumni model
   - Currently tracked under INIT-20260803-002 (same as PRG-004)

3. **Perdana Digital AI Cohort** (referenced in INIT-20260725-001)
   - Listed as "active, JDN stakeholder, pilot stage"
   - No dedicated INIT record found
   - Not in the Portfolio Register

### PQC Sandbox Cohorts (Intelligence Only)

Multiple references to PQC Sandbox 2025/2026 cohorts appear in intelligence cron-output files. These are intelligence monitoring subjects, not Aras programmes. Correctly excluded from the Portfolio Register.

### Red Team Division Skunkworks Cohorts

The Red Team Division structure references "Skunkworks Cohort 1" (Month 6) and "Skunkworks Cohort 2" (Month 12). These are the VORON-C2 intern cohorts. Correctly tracked under PRG-005.

---

## 4. Reconciliation Summary Table

```
PRG-ID  | Programme                  | Recorded | Actual              | Kill Date | Passed? | Next Action Status    | Recommendation
--------|---------------------------|----------|---------------------|-----------|---------|-----------------------|----------------------------------------------
PRG-001 | PERJASA AI Cohort Workshop| 🟢 Active| ⚠️ UNKNOWN          | Sep 2     | YES     | UNKNOWN (no evidence)  | DAF confirm workshop status IMMEDIATELY
PRG-002 | CSM × Aras GTM Partnership| 🟡 Stalled| 💀 KILLED (zombie) | Aug 22    | YES     | NOT completed          | Formally kill or merge into CSM JOM (INIT-20260813-005)
PRG-003 | PMO AI Cohort Initiative  | 🔴 Stalled| 💀 KILLED (zombie) | Aug 25    | YES     | NOT completed          | IMMEDIATE park — first kill-date enforcement test
PRG-004 | R.I.S.I.K × UiTM         | 🟡 Planned| ⚠️ KILL DATE PASSED| Sep 3     | YES     | UNKNOWN                | Push UiTM session to Sep 20 (contingency)
PRG-005 | VORON-C2 Internship       | ⚪ Design | ⚪ Design (accurate)| Oct 1     | NO      | Not yet triggered       | No action — monitor for Oct 1
```

---

## 5. Key Findings

### 5.1 MEISAC × NanoSec × Aras Cohort

**Does not exist.** Zero evidence in CognitiveOS. MEISAC is not mentioned anywhere. NanoSec is a pentesting resource (ORG-20260904-001), not a cohort partner. If DAF intends to create this cohort, it requires:
1. MEISAC intake (organization record + stakeholder records)
2. New PRG-006 entry in Portfolio Register
3. Initiative record for the cohort programme
4. Kill date and next action definition

### 5.2 Zombie Programmes

**Two confirmed zombies:**
- **PRG-002** (CSM × Aras GTM) — kill date Aug 22, passed 13 days ago, no kill logged
- **PRG-003** (PMO AI Cohort) — kill date Aug 25, passed 10 days ago, no kill logged

**One day-past kill date:**
- **PRG-004** (RISIK × UiTM) — kill date Sep 3, passed 1 day ago, contingency action (push to Sep 20) not yet triggered

**One past kill date with unknown status:**
- **PRG-001** (PERJASA Workshop) — hard kill date Sep 2, passed 2 days ago, workshop may have happened but no evidence ingested

### 5.3 Kill-Date Enforcement Failure

The Portfolio Register explicitly states: "No programme without a kill date" and "Parked programmes free cognitive capacity. Zombies drain it." Yet 3 of 5 programmes have passed kill dates with no enforcement action logged. The ESF-20260829-001 profile flagged PRG-003 as the "first kill-date enforcement test" with a Sep 7 deadline. As of Sep 4, this test has not been executed.

**This is a systemic governance failure.** The register's own rules are being violated. The pattern the register was designed to prevent ("the five-programme pattern from repeating on the next five") is actively repeating.

### 5.4 Unregistered Cohort Programmes

The CSM Co-Design Lab Cohort 01 (INIT-20260804-004) is a active cohort programme with 23 personnel onboarded but is NOT in the Portfolio Register. This violates Rule 5: "New programmes must enter the register before work begins. No shadow portfolios."

### 5.5 NanoSec Conflation Check

NanoSec (ORG-20260904-001) is correctly scoped as a pentesting resource. There is no conflation with cohort programmes. The DAF directive correctly identified them as separate. No remediation needed on conflation risk.

---

## 6. Recommendations

### Immediate (Sep 4-7)

1. **PRG-001:** DAF confirms whether PERJASA workshop was executed Sep 2-3. If yes → ingest evidence, update COM-20260813-001 to delivered, trigger 90-day continuation. If no → mark 💀 Killed and reschedule or archive.
2. **PRG-002:** Formally update status. Either kill (withdraw sponsorship + pause GTM) or merge into CSM JOM (INIT-20260813-005) and close the PRG-002 slot.
3. **PRG-003:** IMMEDIATE formal park. Log the decision. This is the first kill-date enforcement test — passing it validates the register's authority; failing it renders the register advisory.
4. **PRG-004:** Trigger contingency — push UiTM session to Sep 20. Verify Phase 0 deliverable status (DeerFlow collection exists; claim register and sample brief need confirmation).

### Short-Term (Sep 7-14)

5. **Register PRG-006:** If the CSM Co-Design Lab Cohort 01 (INIT-20260804-004) is a continuing programme, add it to the Portfolio Register with a kill date and next action. No shadow portfolios.
6. **MEISAC Intake:** If DAF has a MEISAC × NanoSec × Aras cohort concept, it requires a full intake event — organization record for MEISAC, stakeholder records, initiative record, and PRG-007 entry.
7. **Weekly Review Cadence:** The register specifies Monday 09:00 UTC+8 weekly review. The last review evidence is unclear — enforce the cadence.

### Structural

8. **Kill-Date Enforcement Protocol:** The register needs an automated enforcement mechanism. The Cognitive Loop review (SOP-COGNITIVE-LOOP-REVIEW.md) references the `ahmadfaurani/cohort-programme` repo and Hermes cron, but the loop has not been running consistently. The ESF profile (Aug 29) notes the first automated run was Aug 24 — 20 days after institutionalisation.
9. **Register Completeness:** The register has 5 entries but at least 6 cohort programmes exist in CognitiveOS (adding CSM Co-Design Lab). Audit all cohort programmes and ensure register completeness.

---

## 7. Source References

| Record | Role |
|--------|------|
| governance/PORTFOLIO-REGISTER.md | The register itself |
| governance/STRATEGIC-OBJECTIVE-COHORT-PROGRAMME.md | Canonical strategic objective |
| governance/COHORT-IP-FRAMEWORK.md | IP framework for cohort programmes |
| governance/SOP-COGNITIVE-LOOP-REVIEW.md | Review SOP (repo: ahmadfaurani/cohort-programme) |
| initiatives/INIT-20260813-001.md | PERJASA × Aras Co-Design Lab (PRG-001) |
| initiatives/INIT-20260804-004.md | CSM Co-Design Lab Cohort 01 (unregistered) |
| initiatives/INIT-20260803-002.md | RISIK × UiTM (PRG-004) |
| initiatives/INIT-20260611-001.md | DeerFlow (not a cohort, infrastructure) |
| initiatives/INIT-20260808-003.md | Red Team Division (contains VORON-C2) |
| projects/voron-c2/VORON-C2-INTERN-PROGRAMME.md | VORON-C2 intern programme (PRG-005) |
| organizations/ORG-20260904-001-nanosec.md | NanoSec (pentesting, not cohort) |
| commitments/COM-20260813-001.md | PERJASA workshop delivery commitment |
| risks/RSK-20260813-001.md | PERJASA workshop date confirmation risk (resolved) |
| artifacts/ESF-20260829-001-DAF-Strategic-Leader-Profile.md | DAF profile (flags PRG-003 enforcement) |
| decisions/DEC-20260818-012.md | RISIK four-pillar framework (references cohort programme) |
| decisions/DEC-20260812-001.md | CSM/MyCERT accepts Cohort 01 |
