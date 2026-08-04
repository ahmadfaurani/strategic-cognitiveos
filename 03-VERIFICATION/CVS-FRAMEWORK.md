# Core Validation System (CVS) — Master Framework

**Classification:** TLP:AMBER  
**Status:** UNIVERSAL STANDARD — Institutionalized SOP across all Aras Integrasi workstreams  
**Created:** 2026-08-04  
**Last Updated:** 2026-08-04  
**Authority:** Head of Intelligence, Aras Integrasi  
**Applies to:** ALL intelligence products, reports, dashboards, briefings, compliance submissions, executive communication, and AI-generated outputs across every workspace

---

## 0. Operating Principle

> A claim becomes operationally usable only when its source, evidence, confidence level, and validation status are clearly recorded.

CVS separates verified facts, unverified claims, analytical interpretation, and future assumptions so that decisions are not made on weak, conflicting, or undocumented information. Every factual statement or data point is checked against source evidence before being accepted as reliable.

---

## 1. Core Purpose — Five Validation Questions

| Question | Purpose |
|----------|---------|
| What is being claimed? | Identify the exact data point, statement, or record. |
| Where did it come from? | Trace the original source. |
| Can it be verified? | Check whether supporting evidence exists. |
| Is there any contradiction? | Detect conflicts across sources. |
| How should it be classified? | Assign tier, confidence score, and validation status. |

---

## 2. Claim Classification — 6 Tiers

| Tier | Category | Description | Treatment |
|------|----------|-------------|-----------|
| **T1** | Verified Fact | Confirmed through authoritative or source-traceable evidence. Multiple independent sources agree OR official source. | Safe for formal reports, dashboards, executive briefs. Stated as fact. |
| **T2** | Partially Verified Claim | Supported by some evidence but missing full confirmation. Single credible source or incomplete corroboration. | Use with caution. Label as `[SOURCE-BACKED]`. Tag `[UNVERIFIED]` if not corroborated within 24h. |
| **T3** | Analytical Interpretation | Derived from facts through analysis, calculation, or expert judgment. Not a raw fact — an assessment. | Label as `[ASSESSMENT]`. Never present as fact. Include reasoning chain. |
| **T4** | Assumption / Projection | Based on expectation, forecast, scenario, or incomplete data. | Use only for planning. Label as `[ASSUMPTION]`. Never present as fact in intelligence products. |
| **T5** | Disputed / Conflicting Claim | Sources disagree or evidence is inconsistent. | Escalate for review. Label as `[DISPUTED]`. Do not use as final fact until resolved. |
| **T6** | Rejected Claim | Unsupported, contradicted, outdated, or unreliable. | Exclude from official output. Label as `[EXCLUDED]`. Log in evidence register for audit trail. |

### Tier Transition Rules
- **T2 → T1:** When second independent source corroborates, or official source confirms.
- **T2 → T5:** When a conflicting source emerges.
- **T2 → T6:** When source is retracted, disproven, or found unreliable.
- **T5 → T1:** When conflict resolved by authoritative source.
- **T5 → T6:** When all sources are found unreliable.
- **T3 → T1:** Never. Analysis is always analysis. New facts may be extracted and validated separately.
- **T4 → T1:** Never. Projections are always projections. Actual outcomes may be validated as new facts.

---

## 3. Source Reliability Hierarchy — 5 Levels

| Level | Source Type | Reliability | Treatment |
|-------|------------|-------------|-----------|
| **L1** | Official records, signed documents, system-of-record data, regulated filings, government gazettes | Highest trust | Primary validation layer. Automatic T1 for factual content. |
| **L2** | Internal approved reports, validated databases, meeting minutes, audit logs | Strong trust | Acceptable if traceable and current. T1 if independently verified, T2 otherwise. |
| **L3** | Direct stakeholder confirmation, email trails, documented interviews | Acceptable | T2 with attribution and timestamp. T1 if corroborated. |
| **L4** | Secondary reports, media, third-party references, vendor material | Requires cross-check | T2 if from credible outlet. T5 if conflicting. Never T1 alone. |
| **L5** | Informal notes, verbal claims, assumptions, AI-generated output | Not accepted as factual | T2 at best with explicit validation flag. T6 if uncorroborated. AI output requires mandatory validation (Rule 6). |

### NS Workspace Source Mapping (legacy → universal)
The existing NS A–F source ratings map to the universal hierarchy:
- **A (Official/Government)** → L1
- **B (Major mainstream media)** → L4 (high-quality subset)
- **C (Independent/alternative media)** → L4 (standard subset)
- **D (Social media — verified accounts)** → L4 (low-confidence subset)
- **E (Social media — unverified)** → L5
- **F (OSINT/Aggregate)** → L5 (unless independently traced to L1–L3)

Source reliability is re-assessed every 7 days. Sources demonstrating consistent accuracy are upgraded; sources with repeated errors are downgraded.

---

## 4. Validation Workflow — 5 Steps

### Step 1 — Claim Extraction
Break the document, dataset, or briefing into individual claims. Each claim is validated separately.

**Example:**
- Raw: "The project will launch in October with three agencies involved."
- Claim 1: Project launch target is October.
- Claim 2: Three agencies are involved.

### Step 2 — Source Mapping
For each claim, record:

| Field | Description |
|-------|-------------|
| Claim ID | Unique reference (format: `CVS-[WORKSPACE]-[NNN]`) |
| Claim Statement | Exact factual claim |
| Source Name | Document, person, database, system, or email |
| Source Type | Official, internal, external, verbal, inferred |
| Source Date | When the evidence was created or received |
| Source URL | Direct link to source (where applicable) |
| Owner | Person responsible for validation |

### Step 3 — Evidence Check
Assess whether the claim is supported by evidence using 5 tests:

| Evidence Test | Question |
|---------------|----------|
| Traceability | Can the claim be traced to a specific source? |
| Authority | Is the source qualified or authoritative? |
| Currency | Is the information still current? |
| Consistency | Does it match other available sources? |
| Completeness | Is any important context missing? |

### Step 4 — Conflict Detection
If two or more sources disagree, the claim must be flagged as T5 (Disputed).

| Conflict Type | Example |
|---------------|---------|
| Date conflict | One source says September; another says October. |
| Quantity conflict | One report says 50 users; another says 75. |
| Ownership conflict | Different parties claim responsibility for the same deliverable. |
| Status conflict | One document says completed; another says pending. |
| Scope conflict | One source includes 3 workstreams; another includes 2. |

Conflicted claims must not be used as final facts until resolved.

### Step 5 — Validation Decision
Each claim receives a final validation status:

| Status | Meaning | Usage Rule |
|--------|---------|------------|
| **Verified** | Evidence is strong and consistent (score 8-10) | Safe for formal use. |
| **Partially Verified** | Some support exists, gaps remain (score 5-7) | Use with caveat. |
| **Pending Validation** | Evidence not yet reviewed (no score) | Do not use as confirmed fact. |
| **Disputed** | Sources conflict (any score — conflict overrides) | Escalate. |
| **Inferred** | Derived from analysis, not directly stated | Label clearly as [ASSESSMENT]. |
| **Rejected** | Unsupported or contradicted (score 0-2) | Remove from output. |

---

## 5. Confidence Score — 5-Criteria Model

Each validated claim receives a confidence score. This is applied by the validating analyst or, in automated workflows, by the AI agent generating the claim (subject to Rule 6 — AI output requires validation).

| Criteria | Score 0 | Score 1 | Score 2 |
|----------|---------|---------|---------|
| **Source Authority** | Unknown source | Secondary source (L4) | Official / authoritative source (L1-L2) |
| **Source Traceability** | No trace | General reference | Specific document / record / URL |
| **Recency** | Outdated (>30 days or undated) | Possibly current (7-30 days) | Confirmed current (<7 days or official) |
| **Cross-Source Consistency** | Contradicted by other sources | Partially aligned | Fully aligned or single authoritative source |
| **Completeness** | Major context gaps | Minor gaps | Complete context |

### Confidence Rating

| Total Score | Confidence Level | Treatment |
|------------|------------------|-----------|
| **8–10** | High | Accept as verified. T1 eligible. |
| **5–7** | Medium | Use with caveat. T2. |
| **3–4** | Low | Keep under review. T2 with flag. |
| **0–2** | Very Low | Do not use as fact. T6 or T4 if assumption. |

### Scoring Override Rules
- **Conflict detected → automatic T5** regardless of score. Score is recorded for reference but does not override dispute status.
- **AI-generated claim → max initial score 7** (cannot self-certify as High confidence). Human review required to exceed 7.
- **Official source (L1) → minimum score 6** for factual content (authority=2, traceability=2, recency=2 baseline).

---

## 6. Evidence Register — CSV Format

The evidence register is maintained as a CSV file in each workspace's `03-VERIFICATION/` directory. The master register aggregates all workstream registers.

**File:** `CVS-EVIDENCE-REGISTER.csv`  
**Header row (15 fields):**

```
claim_id,workstream,claim,source_name,source_type,source_url,source_date,evidence_type,tier,validation_status,confidence_score,authority,traceability,recency,consistency,completeness,issue_gap,owner,action_required,last_reviewed
```

**Field definitions:**

| Field | Description | Example |
|-------|-------------|---------|
| claim_id | Unique ID: `CVS-[WS]-[NNN]` | CVS-NS-001 |
| workstream | Source workspace | NS, MLK, CogOS, HOI, PDRM, RTI |
| claim | Exact factual claim text | "103 candidates across 36 DUNs" |
| source_name | Document/outlet/system | SPR official candidate list |
| source_type | L1-L5 source level | L1 |
| source_url | Direct link | https://www.spr.gov.my/... |
| source_date | Evidence date (YYYY-MM-DD) | 2026-07-18 |
| evidence_type | Document, database, interview, media, social | Official document |
| tier | T1-T6 | T1 |
| validation_status | Verified, Partially Verified, Pending, Disputed, Inferred, Rejected | Verified |
| confidence_score | 0-10 total | 10 |
| authority | 0-2 | 2 |
| traceability | 0-2 | 2 |
| recency | 0-2 | 2 |
| consistency | 0-2 | 2 |
| completeness | 0-2 | 2 |
| issue_gap | Note any gap or issue | None |
| owner | Responsible person | DAF |
| action_required | Next action | None |
| last_reviewed | Date last reviewed (YYYY-MM-DD) | 2026-08-04 |

---

## 7. Governance Rules

### Rule 1 — No Source, No Fact
Any claim without a source must be treated as unverified. Minimum required: source name + source date. URL required where source is online.

### Rule 2 — Analysis Is Not Fact
Calculated, interpreted, or modelled outputs must be labelled as analysis (T3). Analytical findings derive from validated facts but are not themselves facts.

### Rule 3 — Projection Is Not Evidence
Forecasts, assumptions, estimates, and scenarios cannot validate factual claims. Projections are T4 and used for planning only.

### Rule 4 — Latest Is Not Always Correct
A newer document may still contain copied, outdated, or incomplete information. Recency is one scoring criterion, not a validation override.

### Rule 5 — Contradiction Requires Escalation
Conflicting evidence must be reviewed before the claim is used in a formal output. Conflicted claims are T5 until resolved.

### Rule 6 — AI Output Requires Validation
All AI-generated summaries, classifications, extracted claims, scores, and analytical outputs must be checked against primary sources before use. AI-generated claims are capped at confidence score 7 until human review. This applies to:
- All cronjob-generated intelligence products
- All LLM-extracted entity data
- All AI-assisted analysis and assessments
- All automated scoring outputs

AI output without a traceable source is T6 (Rejected) by default.

---

## 8. CVS Dashboard Structure

| Dashboard Layer | Purpose | Source |
|-----------------|---------|--------|
| **Validated Facts** | Confirmed T1 data points ready for formal use | Evidence register (tier=T1, status=Verified) |
| **Pending Validation** | T2 claims awaiting source review or corroboration | Evidence register (status=Partially Verified or Pending) |
| **Disputed Claims** | T5 conflicting or unresolved data points | Evidence register (tier=T5 or status=Disputed) |
| **Source Register** | All documents, systems, and people used as evidence | CVS-SOURCE-REGISTER.md |
| **Confidence Matrix** | Claim-level confidence score breakdown | Evidence register (score columns) |
| **Action Tracker** | Follow-up tasks to resolve gaps | Evidence register (action_required field) |
| **Audit Trail** | Record of validation decisions and reviewer notes | Evidence register (last_reviewed, owner fields) |

---

## 9. Output Labels

Every intelligence product, brief, report, or dashboard output must clearly mark the status of information:

| Label | Meaning | Tag |
|-------|---------|-----|
| Verified Fact | Confirmed by reliable source evidence (T1) | `[CONFIRMED]` |
| Source-Backed Claim | Supported by evidence, not yet fully validated (T2) | `[SOURCE-BACKED]` |
| Analytical Finding | Derived from validated facts through analysis (T3) | `[ASSESSMENT]` |
| Working Assumption | Used for planning only, not fact (T4) | `[ASSUMPTION]` |
| Unresolved Conflict | Sources disagree, requires clarification (T5) | `[DISPUTED]` |
| Excluded Claim | Rejected due to lack of evidence or contradiction (T6) | `[EXCLUDED]` |

All claims must include: `[SOURCE: URL]` or `[SOURCE: source name, date]`

---

## 10. Cronjob Integration — Full AI Self-Scoring

All LLM-driven cronjobs must include CVS tagging in their output. The AI agent applies the full 5-criteria scoring rubric to its own claims. This is mandatory.

### CVS Output Block (appended to every cronjob intelligence product)

```
---CVS VALIDATION BLOCK---
Claim: [exact factual claim]
Source: [source name + URL if available]
Source Level: [L1-L5]
Tier: [T1-T6]
Validation Status: [Verified/Partially Verified/Pending/Disputed/Inferred/Rejected]
Confidence Score: [0-10]
  Authority: [0-2] | Traceability: [0-2] | Recency: [0-2] | Consistency: [0-2] | Completeness: [0-2]
Action Required: [None / Human review needed / Corroboration needed / Escalation]
---END CVS BLOCK---
```

### AI Self-Scoring Constraints (Rule 6 Enforcement)
- AI-generated claims: max initial confidence score = 7
- AI cannot self-certify T1 — max self-assigned tier = T2
- T1 requires human review and upgrade confirmation
- Claims without traceable source: auto-T6
- AI analytical assessments: auto-T3 with [ASSESSMENT] tag
- AI projections/forecasts: auto-T4 with [ASSUMPTION] tag
- Conflicting sources detected by AI: auto-T5 with [DISPUTED] tag

### Human Review Workflow
1. Cronjob generates intelligence product with CVS blocks
2. Product saved to workspace `01-DAILY-INTELLIGENCE/`
3. Human reviews CVS blocks — validates, upgrades tiers, resolves disputes
4. Human-validated claims entered into `CVS-EVIDENCE-REGISTER.csv`
5. Weekly audit: all T2 claims >5 days pending reviewed for re-assessment

---

## 11. Workstream Adapters

Each workspace maintains its own `03-VERIFICATION/` directory containing:
- `CVS-EVIDENCE-REGISTER.csv` — local claims register
- `CVS-SOURCE-REGISTER.md` — local source hierarchy (domain-specific sources)
- `CVS-ADAPTER.md` — domain-specific rules and overrides (where applicable)

### Active Workstreams

| Workspace | Directory | Domain | Status |
|-----------|-----------|--------|--------|
| Main (CogOS) | `workspace/03-VERIFICATION/` | Strategic intelligence, PIR validation | Master framework |
| PRN NS | `workspace-ns/03-VERIFICATION/` | Election intelligence | Upgrade from 3-tier |
| PRN MLK | `workspace-mlk/03-VERIFICATION/` | Election intelligence | New deployment |
| HOI | `workspace-hoi/03-VERIFICATION/` | Multi-domain intel ops | New deployment |
| PDRM | `workspace-pdrm/03-VERIFICATION/` | Info ops, policing | New deployment |
| Weststar-RTI | `workspace-weststar-rti/03-VERIFICATION/` | RTI response | New deployment |
| Cybersecurity | `workspace-cybersecurity-practice/03-VERIFICATION/` | Cyber intel | New deployment |
| CBO-01 | `workspace-cbo-01/03-VERIFICATION/` | Commercial ops | New deployment |
| AZW | `workspace-azw/03-VERIFICATION/` | TBD | New deployment |
| TH-RCI | `workspace-th-rci/03-VERIFICATION/` | Tabung Haji RCI | New deployment |

### Domain-Specific Override Examples

**Election Intelligence (NS, MLK):**
- SPR/EC official data → automatic T1, score ≥8 (L1 source)
- Party Sec-Gen statements → T1 for fact statement was made, T2 for content
- WhatsApp forwards → T6 (excluded), logged for trend tracking only

**Strategic CognitiveOS:**
- PIR-sourced claims → validated against PIR evidence chain
- AI Council outputs (Sol/GLM/Claude) → T3 (assessment) by default, T2 if source-backed

**PDRM Info Ops:**
- Official PDRM statements → L1, T1 for fact of statement
- Policing publications → L2, T2 unless independently verified

---

## 12. Re-Assessment Cadence

| Cadence | Action |
|---------|--------|
| **Weekly** | All T2 claims reviewed. Pending >5 days flagged for re-evaluation. |
| **Event-driven** | T2 claims immediately re-assessed when new information arrives. |
| **Phase transition** | All claims re-assessed at operational phase transitions (nomination day, campaign period, polling day, project milestones). |
| **Monthly** | Source register re-assessed. Sources upgraded/downgraded based on accuracy track record. |
| **Quarterly** | Full CVS audit — all registers reviewed for completeness, stale claims archived. |

---

**Master Document Location:** `/home/p62operator/.openclaw/workspace/03-VERIFICATION/CVS-FRAMEWORK.md`  
**Classification:** TLP:AMBER  
**Authority:** Head of Intelligence, Aras Integrasi
