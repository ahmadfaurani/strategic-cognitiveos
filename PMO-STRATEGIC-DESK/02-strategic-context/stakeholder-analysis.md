# PERSADA PMO Stakeholder Map

**Date:** 2026-07-13  
**Classification:** TLP:AMBER  
**Owner:** DAF (Aras Integrasi)  
**Document Reference:** PERSADA — 3 Vendors Segmentation (inbound PDF)  
**Cross-Ref:** `memory/struktur-keselamatan-strategik-jpm-2026.md`, `memory/pmo-email-registry.md`, `reports/2026-06-25-persada-requirements-analysis.md`

---

## Executive Summary

PERSADA is a **Strategic Requirement of PMO** comprising three AI-driven vendor segments for social media messaging, area-based profiling, and multi-source data integration. This document maps all stakeholders across the PMO, MKN, inter-agency network, and vendor ecosystem, identifying their influence, interest, alignment to PERSADA segments, and engagement status.

**Key Finding:** Aras Integrasi's Loop Engineering pipeline currently satisfies **70-75%** of PERSADA requirements. The primary engagement gap is the ** Bahagian Keselamatan Strategik (BKS)** — the likely end-user consumer of PERSADA intelligence products — which has no direct relationship with Aras Integrasi yet. The existing relationship is with **Bahagian Data Strategik / Perdana Digital**, which is the data infrastructure counterpart, not the intelligence consumer.

---

## 1. PERSADA Overview — Three Vendor Segments

| Segment | Title | Core Mandate | Deliverable Cadence |
|---------|-------|-------------|---------------------|
| **S1** | AI-Driven Social Media Messaging Strategy | Sentiment analysis, narrative suggestion/avoidance, linguistic analysis, counter-narrative | 2x daily (9am/3pm), weekly, quarterly |
| **S2** | AI-Driven Area Based Profiling | Hyper-local sentiment, 100 areas of interest, pre/post-visit analysis | Daily (9am), per-visit, quarterly |
| **S3** | AI-Driven Multi-Source Multiformat Data Integration | Data fusion, 7-domain SME validation, predictive/prescriptive analysis | Daily (5pm), 24/7 support, quarterly |

**SME Validation Domains (S3 Req 3):**
1. Political Security Analysis
2. Party Institution & Electoral Strategy
3. Social-Media Analysis
4. PSY-OP / PSY-WAR Analysis
5. National Security Analysis
6. Socio-Economic Analysis
7. Specific Social & Political Institution

---

## 2. Stakeholder Tiers

### Tier 1 — Executive Authority

| Stakeholder | Role | Influence | Interest | PERSADA Link |
|------------|------|-----------|----------|--------------|
| **PM Anwar Ibrahim** | Chairman, Majlis Keselamatan Negara (MKN) | **SUPREME** | High | Ultimate consumer of PERSADA intelligence products; receives dual-perspective briefs (operational from MKN, strategic from BKS) |
| **Cabinet** | Policy approval body | HIGH | Medium | Approves funding and scope for PERSADA implementation |

### Tier 2 — Procuring Entity: Perdana Digital / Bahagian Data Strategik

This is the team Aras Integrasi has an **active relationship with** via the AI Cohort.

| Name | Email | Role | Engagement Level | Status |
|------|-------|------|-----------------|--------|
| **Puan Nazilah** | nazilah@pmo.gov.my | Primary Decision Maker [Role TBD] | **PRIMARY** — All correspondence routed through her | ✅ API Key Issued, ⏳ Awaiting session date |
| Encik Hishamuddin | hishamuddin@pmo.gov.my | [Role TBD] | API Key Holder | ✅ API Key Issued |
| Encik Imran | imran@pmo.gov.my | [Role TBD] | API Key Holder | ✅ API Key Issued |
| Encik Azrun | azrun@pmo.gov.my | [Role TBD] | API Key Holder | ✅ API Key Issued |
| Encik Shahril Shatar | shahril.shatar@pmo.gov.my | [Role TBD] | API Key Holder | ✅ API Key Issued |

**Engagement Status:** AI Cohort kickoff (Thread #001, 6 Jul), API keys issued (Thread #002, 9 Jul), working session proposed (Thread #003, 9 Jul) — **awaiting session confirmation**.

**Critical Gap:** Roles of all 5 contacts remain TBD. Must be clarified during working session to map to PERSADA decision-making structure.

### Tier 3 — Intelligence Consumer: Bahagian Keselamatan Strategik (BKS-PMO)

This is the likely **end-user** of PERSADA intelligence products. **No direct relationship with Aras Integrasi exists yet.**

| Stakeholder | Role | Influence | Interest | PERSADA Link |
|------------|------|-----------|----------|--------------|
| **Khairil Hilmi** | Pengarah (Director), BKS-PMO | **CRITICAL** | Very High | Primary consumer of S1 (narrative/counter-narrative), S2 (area profiling), S3 (SME-validated intelligence) |
| **Unit Ancaman Kognitif** | Cognitive Threat Unit — countering foreign information manipulation, disinformation campaigns | HIGH | Very High | Direct consumer of S1 Req 5/6 (narrative/counter-narrative), S1 Req 9 (pre-emptive narrative framework) |
| **Unit Risiko Sistemik** | Systemic Risk Unit — economic vulnerability, supply chain, strategic economic security | HIGH | High | Consumer of S3 Req 2 (socio-economic segment), S2 Req 7 (socio-political issues) |
| **Unit Penilaian Polisi** | Policy Assessment & National Resilience Unit | HIGH | High | Consumer of S3 Req 5 (prescriptive analysis), S1 Req 10 (socio-political campaign messaging) |

**Source:** `memory/struktur-keselamatan-strategik-jpm-2026.md` (documented 2026-06-30)  
**Note:** Khairil Hilmi was hospitalized in ICU (Jan 2026, Bernama/malaysiakini). Current health status unknown — may affect engagement timeline.

**Engagement Strategy:** BKS should be identified as a key stakeholder during the working session with Bahagian Data Strategik. Aras Integrasi should request an introduction or briefing opportunity with BKS to understand their operational requirements firsthand.

### Tier 4 — Operational Coordination: Sektor Keselamatan Strategik (SKS-MKN)

MKN translates national security policy into inter-agency operations. BKS-PMO advises; SKS-MKN executes.

| Stakeholder | Role | Influence | Interest | PERSADA Link |
|------------|------|-----------|----------|--------------|
| **Datuk Raja Nurshirwan Zainal Abidin** | Ketua Pengarah MKN | HIGH | Medium | Oversees SKS which may consume PERSADA threat assessments |
| **Timbalan Ketua Pengarah (Strategik)** | Deputy Director-General (Strategic) | HIGH | Medium | Direct overseer of SKS sectors |
| **Sektor Siber & Teknologi Kritikal** | Cyber & Critical Tech — CNII protection, national cyber crisis | MEDIUM | Medium | Potential consumer of S3 (national security SME domain) |
| **Sektor Maritim, Udara & Sempadan** | Maritime/Air/Border — ZMM monitoring, border security | MEDIUM | Low | Indirect — peripheral to PERSADA's social media/area profiling focus |
| **Sektor Geostrategi & Isu Antarabangsa** | Geostrategy & International — South China Sea, ASEAN stability | MEDIUM | Medium | Potential consumer of S1 (narrative framing on geopolitical issues) |
| **Sektor Pengurusan Krisis & Kesiapsiagaan** | Crisis Management — national crisis simulation, mega event security (ASEAN Summit 2026) | MEDIUM | High | Consumer of S2 (pre/post-visit analysis for event security), S3 (24/7 decision support) |

**Reporting Flow:** Root-level intelligence → SKS-MKN (tactical screening) → BKS-PMO (political-policy assessment) → PM (dual-perspective executive summary).

### Tier 5 — Vendor / Solution Provider: Aras Integrasi

| Name | Role | Contact | PERSADA Position |
|------|------|---------|-----------------|
| **Faurani Jaafar (DAF)** | Director, Cyber Security Practice | daf@arasintegrasi.ai / +6019 434 2727 | Lead strategist; positioned as solution provider for S1-S3 |
| **Farul Mohd Ghazali** | Chief Technology Officer | farul@arasintegrasi.ai / +6017 218 9748 | Technical implementation; API infrastructure owner |

**Solution:** Loop Engineering Political Monitoring Pipeline — 4-Loop framework with PIR classification, 6-level escalation, 32-source DeerFlow collection. 70-75% PERSADA coverage (9/23 fully covered, 6/23 partial, 8/23 missing).

**Competitive Advantages:** Transparency (full audit trail), Modularity (independent skills), Human-in-Loop (SME validation), Continuous Improvement (Loop 4), Cost Efficiency (open-source stack).

### Tier 6 — Competing Vendors (3 Segments)

PERSADA is structured as 3 separate vendor segments. Aras Integrasi may bid for one, multiple, or all segments.

| Segment | Competitive Landscape | Aras Integrasi Position | Strategy |
|---------|----------------------|------------------------|----------|
| **S1: Social Media Messaging** | Unknown — likely established PR/social media analytics firms | Strong (70% coverage) | Position Loop Engineering + counter-narrative capability as differentiator |
| **S2: Area Based Profiling** | Unknown — likely GIS/data analytics firms | Moderate (gap in hyper-local) | Leverage PRN Johor constituency profiling experience as proof-of-concept |
| **S3: Multi-Source Data Integration** | Unknown — likely system integrators / defense contractors | Strong (DeerFlow 32-source fusion) | Highlight human-in-loop SME validation as key differentiator vs pure AI vendors |

**Action Required:** Research competing vendors for each segment. Identify if PERSADA is an open tender, restricted tender, or direct negotiation.

---

## 3. Power-Interest Grid

```
                    HIGH INFLUENCE
                         │
    ┌────────────────────┼────────────────────┐
    │  MANAGE CLOSELY    │  MANAGE CLOSELY     │
    │                    │                      │
    │  • Puan Nazilah    │  • PM Anwar Ibrahim  │
    │    (Perdana Digital)│  • Khairil Hilmi    │
    │  • BKS Unit Heads  │    (BKS-PMO)         │
    │  • Ketua PG MKN    │  • Cabinet           │
    │                    │                      │
 LOW ├────────────────────┼────────────────────┤ HIGH
INTER│  KEEP INFORMED     │  KEEP SATISFIED     │ INTER
EST  │                    │                      │ EST
    │  • API Key Holders │  • SKS Sector Heads │
    │    (Hishamuddin,   │  • Inter-Agency      │
    │     Imran, Azrun,  │    Partners          │
    │     Shahril)       │  • Competing Vendors │
    │  • MKN Deputies    │                      │
    │                    │                      │
    └────────────────────┼────────────────────┘
                         │
                    LOW INFLUENCE
```

---

## 4. Stakeholder-to-PERSADA Segment Mapping

| Stakeholder | S1: Social Media | S2: Area Profiling | S3: Data Integration |
|------------|:-:|:-:|:-:|
| **PM** | Consumer (executive brief) | Consumer (executive brief) | Consumer (executive brief) |
| **Puan Nazilah / Perdana Digital** | Procurement decision | Procurement decision | Procurement decision + data infrastructure |
| **Khairil Hilmi / BKS** | **Primary consumer** (narrative, counter-narrative, cognitive threat) | **Primary consumer** (area profiling, pre/post-visit) | **Primary consumer** (SME validation, strategic briefs) |
| **Unit Ancaman Kognitif** | **Direct user** (S1 Req 5,6,9) | Indirect | SME domain (Social-Media Analysis) |
| **Unit Risiko Sistemik** | Indirect | Indirect | SME domain (Socio-Economic Analysis) |
| **Unit Penilaian Polisi** | Consumer (S1 Req 10) | Consumer (S2 Req 7) | SME domain (Political Security Analysis) |
| **SKS-MKN** | Consumer (narrative framing) | Consumer (event security profiling) | Consumer (24/7 decision support, national security SME) |
| **Aras Integrasi** | Solution provider | Solution provider | Solution provider |

---

## 5. SME Domain Stakeholder Mapping (S3 Req 3)

PERSADA S3 requires 7 SME validation domains. Each domain maps to specific stakeholders:

| SME Domain | Likely SME Source | Aras Integrasi Capability | Gap |
|------------|-------------------|--------------------------|-----|
| Political Security Analysis | BKS Unit Penilaian Polisi | PIR-1 (Gov Stability), PIR-5 (Corruption) | ⚠️ No dedicated SME |
| Party Institution & Electoral Strategy | External (political analysts) | PIR-7 (Electoral Politics), PRN Johor experience | ⚠️ Requires recruitment |
| Social-Media Analysis | BKS Unit Ancaman Kognitif | Signal quality grader, DeerFlow | ✅ Covered (partially) |
| PSY-OP / PSY-WAR Analysis | BKS / Military Intelligence | Not implemented | ❌ Critical gap |
| National Security Analysis | SKS-MKN / MKN deputies | PIR-4 (Security & Defense) | ⚠️ No dedicated SME |
| Socio-Economic Analysis | BKS Unit Risiko Sistemik | PIR-2 (Economic Policy), PIR-9 (Corporate) | ⚠️ No dedicated SME |
| Specific Social & Political Institution | TBD during session | PIR-3, PIR-8 | ❌ Undefined |

**Key Insight:** BKS units are natural SME sources for at least 4 of 7 domains. Access to BKS would simultaneously solve the SME validation requirement AND establish the intelligence consumer relationship.

---

## 6. Inter-Agency Network

Stakeholders connected to PERSADA through MKN's COMSEC (Tactical Integration) framework:

```
ATM ──┬── APMM ──┬── PDRM ──┬── APM
      │          │          │
      ▼          ▼          ▼
      [ SKS-MKN ] ←──→ [ BKS-PMO ]
               │
               ▼
          [ Perdana Menteri ]
               │
               ▼
     [ Perdana Digital / BDS ]
          (data infrastructure)
               │
               ▼
     [ Aras Integrasi ]
          (vendor / AI Cohort)
```

| Agency | PERSADA Relevance | Engagement Status |
|--------|-------------------|------------------|
| NACSA | S3 (cyber security SME domain), potential data source | No direct contact |
| PDRM | S2 (area profiling for domestic security), S3 (national security SME) | Contact directory exists: `hoi-intel-workspace/intelligence/pdrm-contacts-directory.md` |
| ATM | S3 (national security SME), peripheral | No direct contact |
| APMM | Peripheral (maritime border) | No direct contact |
| Wisma Putra | S1 (geopolitical narrative framing) | No direct contact |

---

## 7. Engagement Status Summary

| Stakeholder Group | Relationship | Status | Next Action |
|-------------------|-------------|--------|-------------|
| **Perdana Digital / BDS** | Active (AI Cohort) | ⏳ Awaiting session date | Follow up 2026-07-13 if no response |
| **BKS-PMO (Khairil Hilmi)** | None — identified only | ❌ Not engaged | Request introduction via Puan Nazilah |
| **SKS-MKN** | None — mapped structurally | ❌ Not engaged | Defer until BKS relationship established |
| **Inter-Agency (NACSA, PDRM, etc.)** | PDRM: contacts exist; others: none | ⚠️ Partial | Leverage existing PDRM contacts if area profiling expands |
| **Competing Vendors** | Unknown | ❌ Not researched | Research tender/procurement process |
| **Aras Integrasi Internal** | Active | ✅ Operational | Continue Loop Engineering development |

---

## 8. Engagement Strategy

### 8.1 Short-Term (Before Working Session)

1. **Clarify Puan Nazilah's role** — Is she in Bahagian Data Strategik, BKS, or a coordinating role? This determines the procurement path for PERSADA.

2. **Request BKS introduction** — During working session, ask: "Does BKS-PMO have visibility into the PERSADA requirements? Would a briefing session with Pengarah BKS be appropriate?"

3. **Research PERSADA procurement mechanism** — Is this an open tender (RFP published), restricted tender (invited vendors only), or direct negotiation? This affects competitive strategy.

4. **Identify Khairil Hilmi's current status** — Verify health/recovery status and current operational capacity (was in ICU Jan 2026).

### 8.2 Medium-Term (During/After Working Session)

5. **Map roles to PERSADA segments** — Once Perdana Digital team roles are clarified, map each individual to their PERSADA segment interest.

6. **Position Loop Engineering as S1-S3 solution** — Present the 70-75% coverage analysis and the MVP roadmap (Phases 1-4, 4 weeks).

7. **Propose BKS SME partnership** — Suggest BKS units as SME validators for S3 Req 3, creating a direct operational relationship.

### 8.3 Long-Term (Post-Pilot)

8. **Establish BKS operational liaison** — Dedicated point of contact in BKS for daily PERSADA deliverables (9am/3pm/5pm reports).

9. **Integrate MKN reporting flow** — Ensure PERSADA outputs align with the existing BKS→PM dual-perspective briefing structure.

10. **Expand to inter-agency data sharing** — If PERSADA S3 requires multi-source data, establish feeds from PDRM, NACSA, and other agencies.

---

## 9. Risk Assessment

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|-----------|
| BKS inaccessible — no direct relationship | HIGH | HIGH | Request introduction via Perdana Digital; position AI Cohort as bridge |
| Khairil Hilmi health/availability | MEDIUM | HIGH | Identify alternate BKS contacts; engage at unit head level |
| Competing vendors with existing PMO relationships | MEDIUM | HIGH | Research competitive landscape; emphasize transparency + human-in-loop differentiation |
| PERSADA scope change during engagement | MEDIUM | MEDIUM | Modular architecture allows adaptation; maintain flexibility in pilot scope |
| Procurement process favors large SI/defense contractor | MEDIUM | HIGH | Position as specialist/niche provider; offer pilot POC to demonstrate capability |
| Roles of Perdana Digital contacts remain TBD | HIGH | MEDIUM | Make role clarification a #1 priority for working session |
| PERSADA is classified (rahsia besar per MKN Sec 37) | MEDIUM | HIGH | Ensure all Aras Integrasi personnel have appropriate clearance; implement TLP controls |

---

## 10. Document Cross-References

| Document | Location | Relevance |
|----------|----------|-----------|
| PERSADA Vendor Segmentation PDF | `.openclaw/media/inbound/PERSADA_-_3_Vendors_Segmentation*.pdf` | Source document — 3 segments, 23 requirements |
| PERSADA Requirements Analysis | `reports/2026-06-25-persada-requirements-analysis.md` | Gap analysis vs Loop Engineering pipeline |
| BKS Structure | `memory/struktur-keselamatan-strategik-jpm-2026.md` | Organizational structure of BKS-PMO and SKS-MKN |
| PMO Email Registry | `memory/pmo-email-registry.md` | Communication log with Perdana Digital |
| Data Lake Readiness Assessment | `memory/pmo-datalake-readiness-assessment.md` | Pre-session assessment template |
| Action Items Tracker | `PMO-STRATEGIC-DESK/01-engagement-tracker/action-items.md` | 18 tracked actions, 61% complete |
| BDS Mandate | `PMO-STRATEGIC-DESK/02-strategic-context/bahagian-data-strategik-mandate.md` | Organizational context of counterpart |
| PDRM Contacts | `hoi-intel-workspace/intelligence/pdrm-contacts-directory.md` | Existing PDRM inter-agency contacts |

---

## 11. Confidence Tags

| Claim | Confidence | Justification |
|-------|-----------|---------------|
| PERSADA is a PMO strategic requirement | [HIGH] | Direct from source PDF (inbound, titled "PERSADA REQUIREMENTS-FUNCTIONS-DELIVERABLES") |
| BKS is the likely intelligence consumer | [MEDIUM] | Inferred from BKS mandate (cognitive threats, policy assessment) + PERSADA content (narrative, counter-narrative, area profiling) |
| Khairil Hilmi is Director of BKS | [HIGH] | Confirmed by Bernama + Malaysiakini (Jan 2026) + internal structure document |
| Aras Integrasi covers 70-75% of PERSADA | [MEDIUM] | Based on internal gap analysis (self-assessed, not independently validated) |
| Perdana Digital roles are TBD | [HIGH] | Documented in BDS mandate file and email registry |
| MKN Section 37 (rahsia besar) applies | [HIGH] | From Akta MKN 2016, documented in BKS structure file |
| PERSADA procurement mechanism unknown | [HIGH] | No procurement documentation found in workspace |

---

*This stakeholder map is a living document. Update after each engagement milestone, role clarification, or new intelligence.*

**Last Updated:** 2026-07-13  
**Next Review:** After working session with Bahagian Data Strategik  
**Owner:** DAF (daf@arasintegrasi.ai)
