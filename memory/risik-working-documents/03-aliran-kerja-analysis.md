# R.I.S.I.K Working Document 3 — Analysis & AI Capability Mapping

**Document:** Aliran Kerja — Modul RISIK ke Sistem Penuh (Workflow: RISIK Module → Full System)
**Version:** 1.0 · 15 Ogos 2026 · Dalaman sahaja
**Classification:** SULIT — Dalaman RISIK
**Source:** Received from Prof. Suhaimee / CMIWS via email (Aug 16-17 thread)
**Review date:** Aug 18, 2026

---

## Document Summary

Maps the 7-step journey from doctrinal module to live KKOM (GovComms Command Center) system:

1. **Modul RISIK** — 70+ page doctrinal document by Prof Suhaimee (source of truth)
2. **Static HTML Pages** — ✅ COMPLETED — 8 prototype screens at mock-up-db-kkom-0752.myrisik.duckdns.org
3. **Decision: Upgrade to Full System** — static → live (front-end + back-end + API docs)
4. **Knowledge Transfer Before Building** — doctrine training for developers, paired with internal technical team
5. **Phased Building** — TULIS → BINA → SEMAK → LULUS cycle per stage
6. **Full Integration & UAT** — end-to-end testing on real data
7. **Delivery** — live system + API docs + handbook + ongoing support

## Key Architecture Insights

### Current State (Static Prototype)
- 8 HTML screens with manually typed data
- No database, no back-end, no API
- Reports generated outside the system
- No inter-system connectivity

### Target State (Full System)
- Live data, auto-updating
- Back-end + database
- API + API documentation
- Reports generated from within the system
- Inter-system integration capability

### 5-Stage Build Sequence (Dependency-Ordered)

| Stage | What's Built | RISIK Team Reviews |
|-------|-------------|-------------------|
| 1. Data Foundation | Schema, database, terminology dictionary, codebook | Every field matches module definitions. No developer-invented terms. |
| 2. Back-end + API | Collection & computation engine, API docs | Computation matches doctrine. API docs written WITH code, not after. |
| 3. Front-end | 8 prototype screens upgraded to live data | Screens display what doctrine means, not just look pretty. |
| 4. Reports & Export | Colour PDF, auto-email, archive | Reports generated from system, no manual external work. |
| 5. Full Integration | All components talking to each other | End-to-end tested on real data, not sample data. |

### TULIS → BINA → SEMAK → LULUS Cycle

| Phase | Owner | What Happens |
|-------|-------|-------------|
| TULIS (Write) | Pasukan RISIK (Prof Suhaimee + doctrine team) | Define what to build this stage, boundaries, acceptance criteria |
| BINA (Build) | Developer + internal technical companion | Build together. Companion present throughout, not just at review. |
| SEMAK (Review) | RISIK team + internal technical team | Doctrine-correct? Reviewer tests personally, not via demo. |
| LULUS (Pass) | RISIK team — final say | Written decision with reasons. "Didn't pass" alone is not a decision. |

### Two Types of Return (Critical Distinction)

- **BAIKI (Fix)** — Instructions correct, implementation wrong → developer fixes
- **TULIS SEMULA (Rewrite)** — Instructions themselves wrong → build stops until new instructions ready
- **Don't mix them** — sending work back to developer when the problem is in the instructions wastes everyone's time

### Three Governing Rules

1. No building before writing — every stage starts with written spec and acceptance criteria
2. No approval by demo alone — reviewer tests personally; showing screens is not proof
3. Decisions must be written with reasons — otherwise next stage repeats same errors

### Roles

| Party | Role |
|-------|------|
| Prof Suhaimee & RISIK team | Doctrine owner. Writes what to build, passes/rejects results. Final say on doctrine and measurement accuracy. |
| Internal technical team | Provides training & briefings to developer. Sits beside developer throughout as companion. Reviews technical before it reaches RISIK team. |
| Developer | Builds front-end, back-end, API docs. Asks early when unsure — doesn't guess doctrine. |
| User representative | Tests system per real officer workflow at integration stage. |

### Critical Assumption

"This diagram assumes the 8-screen static prototype is the accepted design reference, and the internal technical team has capacity to companion the developer throughout — not just at review meetings. If companioning capacity doesn't exist, step 4 becomes decoration and the risk of doctrine error returns in full."

---

## AI Capability Mapping (For Alignment Session)

This is where Aras AI development can strengthen the framework:

### Stage 1: Data Foundation
- **AI Opportunity:** Automated terminology extraction from Modul RISIK (70+ pages) → terminology dictionary. NLP-assisted schema mapping from doctrine to database fields.
- **Human Validation:** RISIK team reviews all AI-generated field definitions

### Stage 2: Back-end + API
- **AI Opportunity:** AI-assisted computation engine — implement doctrinal calculation logic as code. Automated API documentation generation.
- **Human Validation:** RISIK team verifies computation matches doctrine at each step

### Stage 3: Front-end
- **AI Opportunity:** Dynamic data binding from live back-end to existing 8 prototype screens. AI-assisted UI adaptation based on doctrine requirements.
- **Human Validation:** RISIK team confirms screens represent doctrine meaning

### Stage 4: Reports & Export
- **AI Opportunity:** AI-generated report templates based on doctrinal output requirements. Automated report population from live system data. Intelligent report formatting (colour PDF, structured email).
- **Human Validation:** RISIK team reviews report content for doctrinal accuracy

### Stage 5: Full Integration
- **AI Opportunity:** AI-assisted UAT — automated test generation from doctrine. Anomaly detection on real data vs doctrinal expectations.
- **Human Validation:** User representative tests per real workflow

### Cross-Stage AI Opportunities
- **Doctrine parsing & extraction** — NLP/LLM to extract structured requirements from the 70+ page Modul RISIK
- **TULIS assistant** — AI to help RISIK team write stage specifications (draft from doctrine, human edits)
- **SEMAK assistant** — AI to pre-check builds against doctrine before human review (reduces review burden)
- **Decision support** — AI to flag potential doctrine compliance issues during BINA phase

### Key Principle: AI Strengthens, Humans Validate
The document's core concern is doctrine integrity. AI should reduce the burden on the RISIK team (who are the bottleneck — they must write, review, and approve every stage), NOT replace their authority. The TULIS → BINA → SEMAK → LULUS cycle has human gates by design. AI makes the humans at those gates faster and more accurate.

---

## Initial Use Case Candidates (For Alignment Session)

### Use Case 1: Doctrine-to-Schema Extraction
**Scope:** Use NLP/LLM to extract structured data fields, terminology, and calculation logic from the 70+ page Modul RISIK. Output: structured schema + terminology dictionary + codebook ready for Stage 1 database build.
**Why first:** Everything depends on data foundation. This is the highest-leverage AI application — turning 70 pages of doctrine into structured data.
**Validation:** RISIK team reviews every extracted field against source doctrine.

### Use Case 2: SEMAK Pre-Check Engine
**Scope:** AI system that reviews developer builds against doctrine at each stage, before human review. Flags potential doctrine compliance issues, missing fields, calculation mismatches.
**Why second:** The RISIK team is the bottleneck — they must personally review every stage. AI pre-checking reduces their burden and catches low-level issues before they spend time on high-level review.
**Validation:** RISIK team reviews AI flags and makes final determination.

---

## Strategic Observations

1. **Prototype already exists** — 8 screens at mock-up-db-kkom-0752.myrisik.duckdns.org. This is not zero-base — there's a working design reference.
2. **The document is about governance, not technology** — the 7 steps are really about maintaining doctrine integrity through a build process. AI must serve this governance model.
3. **The "companion" role is critical** — the internal technical team must sit with the developer throughout. This maps to Hadri/Fuad's role in the Aras context.
4. **The staged approach prevents expensive doctrine errors** — the document explicitly warns that doctrine errors found late (after real data) are the most expensive to fix. This validates the phased approach.
5. **The document is marked SULIT** — Dalaman RISIK only. Handle with appropriate sensitivity.
6. **KKOM = GovComms Command Center** — this is the target system name. RISIK is the doctrine, KKOM is the system.
7. **Version 1.0, dated Aug 15** — this was prepared just before the email exchange, likely for the weekend meeting.

---

## Questions for CMIWS (For Alignment Session)

1. Who is the "developer" in the current plan — internal to UiTM, external contractor, or Aras?
2. What technology stack is the static prototype built on? (HTML/CSS/JS? Any framework?)
3. What is the intended tech stack for the full system?
4. What database is being considered for Stage 1?
5. Is there an existing API specification, or will it be defined during Stage 2?
6. What is the timeline expectation for the full 7-step process?
7. Is there a budget allocated for development, or is this part of the RM5M MCMC proposal?
8. Who are the "user representatives" for UAT at Stage 6?
9. Is the prototype URL (mock-up-db-kkom-0752.myrisik.duckdns.org) accessible to Aras team for review?
10. What is the relationship between KKOM (this system) and the broader RISIK framework?

---

*Analysis by Ember (Aras Integrasi) — Aug 18, 2026*
*Internal review per ACT-20260818-006*
*Document 3 of 3 received from CMIWS*
