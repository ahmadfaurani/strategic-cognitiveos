---
id: GOV-PROCESS-MATURITY-REGISTER-001
record_type: document
title: Process Maturity Register
created_at: 2026-08-04 00:00:00+00:00
updated_at: 2026-08-19 16:00:00+00:00
owner: DAF
status: active
priority: high
sensitivity: internal
lifecycle_state: canonical
confidence: high
tags:
  - doctrine/adep-001
  - doctrine/cognitiveos-prime
  - domain/cognitiveos-operations
  - domain/development-governance
  - domain/governance
  - domain/quality-assurance
  - framework/actionable-intelligence-protocol
  - framework/cognitive-loop
  - framework/engineered-success
  - method/cross-doctrinal-analysis
  - method/engineered-success
  - method/triangulation
source:
  type: direct
  reference: DAF authority
summary: Governance reference document for Process Maturity Register.
strategic_significance: Governs CognitiveOS operational standards and procedures.
mission_alignment:
- sovereign-ai
- intelligence-enablement
related_records:
- GOV-INTAKE-SOP-001
document_type: reference
file_path: governance/process-maturity-register.md
version: '1.0'
author: DAF
---

# Process Maturity Register

**Created:** 2026-08-16  
**Owner:** Ember  
**Authority:** DAF  
**Governing Framework:** ADEP-001 §3 (Four States of Process Maturity)  
**Review Cycle:** Quarterly + at each checkpoint (CP1, CP2, etc.)

---

## Purpose

Track all CognitiveOS governance artifacts across the Four States of Process Maturity (ADEP-001 §3). No artifact may be declared "operational" (State 4) without passing the 13-Point Operationalisation Gate (§33).

---

## The Four States

| State | Definition | Evidence Required |
|-------|-----------|-------------------|
| **1. Expressed** | Idea/request articulated | Record of request (message, conversation, DEC) |
| **2. Codified** | Written as document/SOP/schema | File exists in repository, version controlled |
| **3. Institutionalised** | Integrated into governance mechanisms | Pre-commit hook, validator, index, mandatory reference |
| **4. Operationalised** | Actually used in practice with measurable outcomes | Execution logs, adoption evidence, outcome verification |

**Key rule (ADEP §4):** State 3 ≠ State 4. An SOP in the repository is NOT operational. Operational means: people/agents are using it, outputs are measurably better, and the process has survived at least one real execution cycle.

---

## Register

### Governance Documents

| Artifact | State 1 | State 2 | State 3 | State 4 | Evidence | Last Reviewed | Next Review |
|----------|:-:|:-:|:-:|:-:|----------|--------------|-------------|
| **CognitiveOS Prime Doctrine** (§1-§51) | ✅ | ✅ | ✅ | ⚠️ Partial | §5-§10: INT-006/007/008/009. §11-§20: NOT deployed. §21-§49: partial. §50: 1 pilot cycle. §51: just added. | 2026-08-16 | CP1 (Aug 22) |
| **ADEP-001** (47 sections) | ✅ | ✅ | ✅ | ❌ | Stored, DEC-20260816-001, pre-commit hook. No execution cycle yet. | 2026-08-16 | CP1 (Aug 22) |
| **Intake SOP** (9 steps) | ✅ | ✅ | ✅ | ⚠️ Partial | Steps 1-7 consistent. Step 8 (MEMORY.md update) inconsistent. Step 9 (notification format) sometimes skipped. | 2026-08-16 | CP1 (Aug 22) |
| **Template Discipline SOP** (10 sections) | ✅ | ✅ | ✅ | ⚠️ Partial | Validator runs on every commit. Template REQ markers exist. But template compliance not audited for completeness. | 2026-08-16 | CP1 (Aug 22) |
| **Cross-Doctrinal Analysis SOP** (12 sections) | ✅ | ✅ | ✅ | ❌ | 1 pilot cycle (INT-006/007/008/009). No second execution. | 2026-08-16 | CP1 (Aug 22) |
| **Contribution Standard** | ✅ | ✅ | ✅ | ⚠️ Partial | Referenced in templates. But contribution compliance not systematically checked. | 2026-08-16 | CP2 (Sep 5) |

### Schemas & Templates

| Artifact | State 1 | State 2 | State 3 | State 4 | Evidence | Last Reviewed | Next Review |
|----------|:-:|:-:|:-:|:-:|----------|--------------|-------------|
| **11 JSON Schemas** | ✅ | ✅ | ✅ | ✅ | Validator runs on every commit. 338/338 pass. | 2026-08-16 | CP1 (Aug 22) |
| **12 Templates** | ✅ | ✅ | ✅ | ⚠️ Partial | Templates exist with REQ markers. But not all templates aligned to canonical schema (commitment, conversation, decision, event, initiative, outcome need alignment). | 2026-08-16 | CP2 (Sep 5) |
| **Organization schema + template** | ✅ | ✅ | ✅ | ✅ | 17 ORG records created. Validator supports type. | 2026-08-16 | CP1 (Aug 22) |

### Operational Mechanisms

| Artifact | State 1 | State 2 | State 3 | State 4 | Evidence | Last Reviewed | Next Review |
|----------|:-:|:-:|:-:|:-:|----------|--------------|-------------|
| **Pre-commit hook** | ✅ | ✅ | ✅ | ⚠️ Partial | Governance integrity check works (6 files). Record validation path issue (validator not found from git CWD). | 2026-08-16 | CP1 (Aug 22) |
| **Validator (validate.py)** | ✅ | ✅ | ✅ | ✅ | 338/338 records pass. Runs manually + via hook (when path resolves). | 2026-08-16 | CP1 (Aug 22) |
| **Process Maturity Register** (this document) | ✅ | ✅ | ✅ | ⚠️ | Just created. First use = first review at CP1. | 2026-08-16 | CP1 (Aug 22) |
| **Closure Gate Checklist** | ✅ | ✅ | ❌ | ❌ | Created but not yet in pre-commit hook or mandatory process. | 2026-08-16 | CP1 (Aug 22) |
| **Reporting Standard Template** | ✅ | ✅ | ❌ | ❌ | Created. Not yet mandated for all updates. | 2026-08-16 | CP1 (Aug 22) |

### Analytical Products

| Artifact | State 1 | State 2 | State 3 | State 4 | Evidence | Last Reviewed | Next Review |
|----------|:-:|:-:|:-:|:-:|----------|--------------|-------------|
| **Cognitive Loop** (§5, 8 steps) | ✅ | ✅ | ✅ | ⚠️ Partial | 1 full cycle (INT-006). Template established. Not yet recurring. | 2026-08-16 | CP1 (Aug 22) |
| **Actionable Intelligence Standard** (§7) | ✅ | ✅ | ✅ | ⚠️ Partial | Applied once (INT-007). Not yet embedded in all intelligence production. | 2026-08-16 | CP1 (Aug 22) |
| **Prioritisation Engine** (§8) | ✅ | ✅ | ✅ | ⚠️ Partial | Applied once (INT-007). Not yet standard for all action scoring. | 2026-08-16 | CP1 (Aug 22) |
| **Engineered Success Framework** (§9) | ✅ | ✅ | ✅ | ⚠️ Partial | Applied once (INT-008). Not yet standard for all initiative assessment. | 2026-08-16 | CP1 (Aug 22) |
| **Objective Decomposition** (§10) | ✅ | ✅ | ✅ | ⚠️ Partial | Applied within INT-008. Not yet standard for all initiative planning. | 2026-08-16 | CP1 (Aug 22) |
| **Cross-Doctrinal Analysis** (§50) | ✅ | ✅ | ✅ | ❌ | 1 synthesis (INT-009). SOP codified. Not yet recurring cycle. | 2026-08-16 | CP1 (Aug 22) |

---

## 13-Point Operationalisation Gate (ADEP §33)

Applied before promoting any artifact from State 3 → State 4.

| # | Gate Point | Description |
|---|-----------|-------------|
| 1 | Owner assigned | A named owner is responsible for the artifact |
| 2 | Workflow defined | The process is documented step-by-step |
| 3 | Users identified | Who/what will use this is known |
| 4 | Resources available | Time, tools, access required are available |
| 5 | Access configured | Users can access the artifact and supporting systems |
| 6 | Procedures accessible | Documentation is findable and readable |
| 7 | Inputs available | Required inputs (data, triggers, events) are available |
| 8 | Integrations functioning | Connected systems work correctly |
| 9 | Monitoring available | Can detect when the process runs or fails |
| 10 | Exception handling | Known failure modes have handling procedures |
| 11 | Reporting established | Output/status is communicated to stakeholders |
| 12 | Users capable of executing | Users have the skills/tools to execute the process |
| 13 | First real execution | At least one non-pilot execution has completed successfully |

**Pass criteria:** All 13 points must be ✅. Any ❌ or ⚠️ blocks State 4 promotion.

---

## State Transitions

### Promotion (State N → State N+1)

1. Artifact meets all criteria for current state
2. Apply gate for next state (for 3→4: 13-Point Operationalisation Gate)
3. Record transition in this register with date and evidence
4. Commit to Git

### Demotion (State N → State N-1)

Triggered by:
- Artifact found stale or unused for >90 days
- Process failure causing material impact
- Dependencies removed (e.g., tool offline)
- DAF directive

Record demotion with reason and remediation plan.

---

## Review Cadence

| Review Type | Frequency | Scope |
|------------|-----------|-------|
| Checkpoint review | At each CP (CP1, CP2, etc.) | All artifacts tagged for that CP |
| Quarterly review | Every 3 months | Full register |
| Triggered review | On material change | Affected artifacts only |
| Annual review | Yearly | Full register + process assessment |

---

## Summary Statistics

| State | Count |
|-------|-------|
| State 4 (Operationalised) | 3 (schemas, validator, organization schema) |
| State 4 Partial | 9 (doctrine, SOPs, analytical products) |
| State 3 (Institutionalised) | 2 (closure gate checklist, reporting template — just created) |
| State 2 (Codified) | 0 |
| State 1 (Expressed) | 0 |

**Assessment:** The system is heavily concentrated in "State 3 + Partial 4" — meaning most artifacts are codified and institutionalised but not fully operationalised. The path to State 4 requires real execution cycles, which CP1 (Aug 22) will provide for several artifacts simultaneously.
