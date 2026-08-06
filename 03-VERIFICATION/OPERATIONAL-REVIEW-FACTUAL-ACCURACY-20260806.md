# OPERATIONAL REVIEW — Factual Accuracy Gap Analysis
## CVS Sufficiency Assessment for 100% Operational Accuracy

**Document:** OR-FACT-001
**Created:** 2026-08-06 21:00 MYT
**Classification:** TLP:AMBER
**Authority:** Head of Intelligence, Aras Integrasi
**Trigger:** Intelligence product (commit 1e1d777) contained 5 factual errors requiring user correction

---

## 1. Executive Summary

CVS is necessary but not sufficient for 100% operational accuracy. The framework validates claims in **cronjob outputs** and **workspace documents** — but 3 of 5 errors occurred during **real-time chat responses** and **ad-hoc document generation**, where no CVS enforcement mechanism exists. The gap is structural: CVS is a post-hoc validation layer; what's missing is a pre-output verification gate.

**Verdict:** CVS alone cannot ensure 100% accuracy. Two additional layers are required.

---

## 2. Error Taxonomy

| # | Error Type | Category | CVS Coverage? | Root Cause |
|---|-------|---------|---------------|------------|
| 1 | Former position-holder listed as current | Identity claim — false | ❌ No | Not checked against L1 authoritative registry |
| 2 | Member of one body listed as member of another | Identity claim — false | ❌ No | Not checked against L1 authoritative registry |
| 3 | Contradictory numerical values in same document | Numerical inconsistency | ❌ No | No internal consistency cross-check |
| 4 | Operational trigger stated as fact without source | Unverified claim | ❌ No | Stated without named source or record |
| 5 | Wrong name variant vs official record | Identity claim — unverified | ❌ No | Not checked against L1 authoritative registry |

**All 5 errors are identity/numerical claims that would have been caught by checking against an authoritative source registry.**

---

## 3. CVS Coverage Map — Where It Works and Where It Doesn't

### ✅ CVS COVERS (Working)

| Layer | Mechanism | Status |
|-------|-----------|--------|
| Cronjob outputs (24 LLM jobs) | cvs-validation skill attached to every job | ✅ Active |
| Evidence registers (11 workspaces) | CSV registers with 20-field schema | ✅ Active |
| AI self-scoring (Rule 6) | Max T2/score 7 cap | ✅ Enforced in cronjob prompts |
| Weekly review | Script-only cronjob scans all registers | ✅ Scheduled |
| CVS output blocks | Mandatory in cronjob outputs | ✅ Enforced via skill |

### ❌ CVS DOES NOT COVER (Gaps)

| Layer | Gap | Impact |
|-------|-----|--------|
| **Real-time chat responses** | No validation gate between LLM and user | All 5 errors occurred here |
| **Ad-hoc document generation** | User requests report → LLM writes → commits → no claim extraction or scoring | Errors propagate to git and workspace |
| **Identity verification** | No L1 registry check for entity identity claims | 3 of 5 errors were identity claims |
| **Numerical consistency** | No internal arithmetic cross-check | 1 error was contradictory counts in same document |
| **Source-less claims** | Claims stated as fact without any source attribution | 1 error was an unverified operational trigger |

---

## 4. Root Cause Analysis

### Why CVS Didn't Catch These Errors

CVS is designed as a **post-hoc validation framework**:
1. Claim is made → 2. Claim is extracted → 3. Source is mapped → 4. Evidence is checked → 5. Tier is assigned → 6. Claim is logged

The problem: steps 2-6 happen **after** the claim is already in the output. In real-time chat, there is no post-hoc step — the claim goes directly from LLM to user.

### The Missing Layer: Pre-Output Verification

What's missing is a **pre-output verification gate** that checks factual claims BEFORE they are stated:

```
LLM generates claim → PRE-OUTPUT GATE (verify against L1 registries) → Output to user
                    ↓
                 Claim fails → Suppress or relabel as [ASSESSMENT]
```

This is fundamentally different from CVS's post-hoc model. CVS asks "is this claim valid?" after it's made. The pre-output gate asks "can I verify this claim before I say it?"

---

## 5. Proposed Operational Measures

### Layer 1: Pre-Output Verification Protocol (NEW)

**Applies to:** All real-time chat responses and ad-hoc document generation across all workstreams

**Protocol:**
1. **Identity claims** (who holds a role, belongs to an organisation, holds a position) — must be verifiable against an L1 Reference Registry or at least one L3+ source before stating as fact. If not verified, label as `[UNVERIFIED]` or state as assessment.
2. **Numerical claims** (counts, amounts, dates, statistics) — must be internally consistent. If two different numbers appear in the same output for the same thing, flag and reconcile before output.
3. **Operational triggers** (dates, events, scheduled actions) — must have a named source (individual, court record, official statement, document). If unverified, exclude or label as `[UNCONFIRMED]`.
4. **Source attribution** — every factual claim in ad-hoc documents must include source attribution. No bare facts without sources.

**Enforcement:** Self-enforced by the LLM before output. No external script needed — this is a cognitive protocol, not a software gate.

### Layer 2: L1 Reference Registry System (NEW)

**Concept:** Maintain local authoritative source registries for any domain where the workstream frequently makes identity claims about a class of entities.

**Current registries:**
- `03-VERIFICATION/L1-PARLIAMENT-MEMBERS.csv` — 222 sitting Dewan Rakyat MPs (code, constituency, name, party, coalition)

**Adding new registries:** When a workstream frequently makes identity claims about a class of entities (companies, officials, organisations, products), create an L1 Reference CSV in `03-VERIFICATION/` with the authoritative fields for that domain. Update on a cadence appropriate to the domain (monthly, quarterly, or event-driven).

**Every identity claim must be cross-referenced against the relevant L1 Reference Registry before stating as fact.** This is the single highest-impact measure. 3 of 5 errors would have been caught by registry cross-reference alone.

### Layer 3: Ad-Hoc Document CVS Gate (NEW)

**Applies to:** Any document written at user request and committed to git

**Protocol:**
1. Before committing any ad-hoc document, run `validate.sh` to extract numerical claims and named entities
2. Cross-reference extracted names against relevant L1 Reference Registries
3. Flag any name not found in the registry as `[UNVERIFIED]`
4. Commit only after all flagged claims are resolved or labeled

**This extends CVS from cronjob-only to all outputs.**

---

## 6. Implementation Plan

### Immediate (This Session)

| # | Action | Status | Impact |
|---|--------|--------|--------|
| 1 | Create first L1 Reference Registry (Parliament members) | ✅ Done | Catches identity errors for that domain |
| 2 | Patch CVS skill with general pre-output verification protocol | ✅ Done | Extends CVS to chat responses |
| 3 | Write this operational review | ✅ Done | Documents the gap and solution |

### Short-Term (Next 7 Days)

| # | Action | Impact |
|---|--------|--------|
| 4 | Identify other domains needing L1 registries (companies? officials? organisations?) | Expands coverage |
| 5 | Run validate.sh on existing workspace documents | Retroactive error catch |
| 6 | Add internal consistency check to validate.sh (detect contradictory numbers) | Catches arithmetic errors |

### Ongoing

| # | Action | Impact |
|---|--------|--------|
| 7 | Update L1 registries on domain-appropriate cadence | Keeps references current |
| 8 | Quarterly CVS audit includes ad-hoc document review | Catches unvalidated documents |

---

## 7. Revised Accuracy Architecture

```
┌─────────────────────────────────────────────────────┐
│ LAYER 0: L1 Reference Registries (NEW)               │
│ • Domain-specific authoritative source CSVs          │
│ • One per class of entity (Parliament, companies...) │
│ Cross-reference before ANY identity claim           │
├─────────────────────────────────────────────────────┤
│ LAYER 1: Pre-Output Verification Gate (NEW)          │
│ • Identity claims → check L1 registry                │
│ • Numerical claims → internal consistency check      │
│ • Operational triggers → require named source        │
│ • Unverifiable → label [UNVERIFIED] or suppress      │
├─────────────────────────────────────────────────────┤
│ LAYER 2: CVS Post-Hoc Validation (EXISTING)          │
│ • 6-tier classification                               │
│ • 5-criteria scoring                                  │
│ • Evidence registers                                  │
│ • Cronjob CVS blocks                                  │
├─────────────────────────────────────────────────────┤
│ LAYER 3: Weekly Review & Audit (EXISTING)            │
│ • CVS weekly review cronjob                           │
│ • T2 escalation flags                                 │
│ • T5 dispute tracking                                  │
└─────────────────────────────────────────────────────┘
```

---

## 8. Bottom Line

CVS ensures that cronjob outputs are validated, scored, and logged. It does not prevent the LLM from making factual errors in real-time chat or ad-hoc documents. The 5 errors in this incident all occurred in the gap between "LLM generates claim" and "claim reaches user."

**Three measures close this gap:**
1. **L1 Reference Registry system** — authoritative source-of-truth files for any domain with frequent identity claims
2. **Pre-output verification protocol** — cognitive gate before any factual claim is stated
3. **Ad-hoc document CVS gate** — extend validation from cronjob-only to all outputs

With these three layers, CVS moves from "post-hoc validation" to "end-to-end accuracy assurance." Without them, the same class of errors will recur in every chat-level intelligence product.

The protocol is domain-agnostic. The Parliament member registry is the first instance; additional registries should be created whenever a workstream frequently makes identity claims about a class of entities.
