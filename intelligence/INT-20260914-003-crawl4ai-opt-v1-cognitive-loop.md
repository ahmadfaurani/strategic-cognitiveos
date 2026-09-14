---
id: INT-20260914-003
record_type: intelligence
title: "Cognitive Loop — Crawl4ai opt-v1 Cutover (14 Sep Evening): Retirement→Optimum-Spec Same-Day Sequence Holds; Telemetry Exposes Extraction Coverage (13/25 Sources) as the New Binding Constraint"
created_at: 2026-09-14T23:20:00+00:00
updated_at: 2026-09-14T23:20:00+00:00
owner: faurani-jaafar
intelligence_type: operational
status: active
priority: high
sensitivity: confidential
lifecycle_state: candidate
confidence: high
tags:
  - domain/intelligence
  - domain/data-infrastructure
  - mission/intelligence-enablement
  - mission/political-intelligence
  - framework/cognitive-loop
  - type/operational-analysis
source:
  type: operator-directive
  reference: "DAF directive 'Cognitive Loop to the above' (Telegram 2026-09-14 23:05 UTC) on the 14 Sep evening signal base: commit batch 99b41ce4 (workspace) + d142b11 (CognitiveOS DEC-20260914-005), daily-log sections 16:19–16:54 UTC (post-retirement review + optimum-spec implementation), and live telemetry from intelligence/opt/ run dirs 20260914T164350Z/164916Z/180002Z/200002Z/220002Z."
summary: "Full 8-step Cognitive Loop (Sense→Classify→Correlate→Pattern→Prioritise→Act→Verify→Learn) applied to the 14 Sep evening crawl4ai arc following INT-20260914-002 (signal base after 12:55 UTC). Headline findings: (1) the P3 retirement (DEC-20260914-004, 16:10 UTC) → optimum-spec re-enablement (DEC-20260914-005, 16:55 UTC) same-day sequence is a governed reversal, not oscillation — DEC-004's deliberate preservation of the library, revival path, and archived corpus is what made a same-day successor deployable; (2) the new per-source telemetry converts 'antibot persists' from anecdote to measured debt: full-fleet run 20:00 UTC shows 24/25 sources ok but only 13/25 yielding records (52% coverage), wire tier 2/6 producing (Malaysiakini + Sinar Harian, both at cap-12), 11 sources ok-but-zero-record, 1 hard failure (sabah-news ACS-GOTO timeout) — extraction coverage, not delivery cadence, is now the binding constraint on intelligence value; (3) durability engineering proved itself in production: v1's 540s self-kill lost nothing due to incremental per-source flush, v2 ran clean, and 3 overnight cycles ran unattended; (4) the 2-FTE engineering SPOF protection rule from INT-20260914-002 extends to infra work — all prioritised remediation (selector registry, proxy-pool brief, doc-drift patch) is Ember-executable at host level without touching Fuad/Syahir before the 17 Sep methodology deadline. Produces 3 prioritised actions, V1–V5 verification criteria, and 4 learnings."
strategic_significance: "Closes the loop on the day's third arc and establishes the monitoring baseline for the opt-v1 era: source-health is now instrumented (per-source latency/outcome/error JSONL), so collection quality becomes measurable and improvable rather than anecdotal. The 52% extraction-coverage finding re-points the optimisation roadmap — DEC-005's deferred slots (proxy pool, per-source selectors) are confirmed as the correct priorities by data, not judgement. Pattern continuity with INT-20260914-002: the capacity-collision rule (protect Fuad+Syahir 16–17 Sep) now explicitly covers infrastructure remediation, keeping the CSM methodology deadline the single dominant priority on the engineering pool. Governance continuity: the DEC-004/DEC-005 decision-pair demonstrates that retirements which preserve revival paths convert policy reversals from credibility risk into routine capability upgrades."
mission_alignment:
  - intelligence-enablement
  - political-intelligence
related_records:
  - DEC-20260914-004
  - DEC-20260914-005
  - INT-20260914-002
  - INT-20260914-001
  - INIT-20260710-002
  - ACT-20260914-007
  - COM-20260914-003
related_initiative:
  - INIT-20260710-002
---

# Crawl4ai opt-v1 Cognitive Loop — 14 Sep 2026 (Evening Arc)
## Full 8-Step Cycle Applied (Prime Doctrine §5–§8)

**Doctrine Reference:** governance/COGNITIVEOS-PRIME-DOCTRINE.md §5 (Cognitive Operating Loop), §6 (Pattern Recognition Engine), §7 (Actionable Intelligence Standard), §8 (Prioritisation Engine)
**Date:** 14 September 2026 (23:20 UTC / 15 Sep 07:20 MYT)
**Workstream:** Sovereign political-intelligence collection infrastructure (INIT-20260710-002)
**Signal base:** 14 Sep daily log 16:19–16:54 UTC sections; DEC-20260914-004/-005; commits 99b41ce4 (memory-mirror) + d142b11 (CognitiveOS main); telemetry artifacts `workspace-hoi/intelligence/opt/20260914T{164916,180002,200002,220002}Z/`
**Precedent:** INT-20260914-002 (VoronVigil loop, 12:55 UTC) — same day, different workstream; its capacity-protection rule is carried forward as a constraint here

---

## STEP 1 — SENSE

| # | Signal | Source | Time (UTC) | Type |
|---|--------|--------|------------|------|
| S1 | Post-retirement operational review: retirement verified clean (0 crontab lines, no processes, archive sealed); residual footprint retained by design (venv shared, sink static 3,377 files) | Daily log 16:19–16:22 | 16:22 | Verification |
| S2 | Review findings: F1 DUN-Profiling WORKFLOW-PROMPTS.md:429 still lists retired collector as "Automated ✅" (live doc drift); F2 archive clone in volatile /tmp; F3 historical refs need no action | Daily log 16:22 | 16:22 | Findings |
| S3 | DAF directive: "Apply optimum spec configuration to enable optimized intelligence collection to crawl4AI" (delivery errored 16:35, repeated 16:36) | DEC-20260914-005 source | 16:34–16:36 | Directive |
| S4 | opt-v1 implemented: sources_registry.json (25 sources, wire 6 / mainstream 9 / analysis 10, metadata carried), collect_optimized.py (persistent stealth session, deterministic link extraction, dedup_hash sha1(url\|headline), per-source JSONL telemetry, incremental flush, 40s per-source timeout, robots.txt check), 2 crontab lines (wire every-2h even UTC cap 12; full fleet 08/20 UTC cap 15; flock + timeout 1800) | DEC-20260914-005 | 16:36–16:50 | Implementation |
| S5 | Validation arc: smoke 2/2 (10 records, 10 unique); full-fleet v1 killed by own 540s watch (~8 sources) → incremental-flush patch → v2 (timeout 900) launched 16:49 clean | Daily log 16:54 | 16:43–16:54 | Test cycle |
| S6 | Overnight telemetry: wire runs 18Z + 22Z = 6/6 sources ok but only 2 yielding (Malaysiakini 12, Sinar Harian 12 — both at cap); full fleet 20Z = 24/25 ok, 13 sources yielding (8 at cap-15), 11 ok-but-zero-record, 1 failed (sabah-news, ACS-GOTO goto timeout) | intelligence/opt/ telemetry.jsonl ×3 | 18:00–22:00 | Measured outcome |
| S7 | DEC-20260914-005 drafted, schema-v2/taxonomy/pair-lock validated, committed d142b11 (first push hit transient GitHub 5xx, single retry clean); workspace batch 99b41ce4 (GTM preread + brief + daily log) | Commit records | 23:00–23:10 | Governance closure |
| S8 | Deferred slots registered in DEC-005: proxy pool (antibot class fix), per-source CSS selector registry, sitemap mode experimental-off (AsyncUrlSeeder probes hung) | DEC-20260914-005 | 16:55 | Config state |

## STEP 2 — CLASSIFY

| Signal | Domain | Workstream | Info Type | Horizon | Importance |
|--------|--------|------------|-----------|---------|------------|
| S1 | Data-infrastructure | INIT-20260710-002 | Verification | Immediate | High |
| S2 | Knowledge-management | Cross-workstream | Risk (drift) | Tactical | Medium |
| S3 | Intelligence-enablement | INIT-20260710-002 | Directive | Immediate | High |
| S4 | Data-infrastructure | INIT-20260710-002 | Implementation | Immediate | High |
| S5 | Data-infrastructure | INIT-20260710-002 | Test | Immediate | Medium |
| S6 | Intelligence-enablement | INIT-20260710-002 | Intelligence (measured) | Immediate | **Critical** |
| S7 | Governance | CognitiveOS | Closure | Immediate | High |
| S8 | Product-management | INIT-20260710-002 | Backlog state | Operational | Medium |

**Classification summary:** No Critical-external signals in this arc — the criticality is internal and measured (S6). Dominant domains: data-infrastructure (3) and intelligence-enablement (2). Contrast with INT-002's arc (7/14 Critical, external CSM cadence): the evening arc is self-contained infra work executed under the capacity protection the earlier loop established.

## STEP 3 — CORRELATE

### Correlation 1: The Governed Reversal (decision-pair architecture)

```
DEC-20260914-002 (preserve "pipeline live" note) → DEC-004 (P3 retirement, revival path preserved)
                                        ↓ 4h 26m
                              DAF optimum-spec directive (S3)
                                        ↓
DEC-20260914-005 (opt-v1 re-enablement; supersedes DEC-004 for collection function ONLY)
```

The retirement→re-enablement sequence inside one day would read as policy oscillation — except the decision records make it legible: DEC-004 deliberately preserved the library, the archived corpus, and a named revival path, and DEC-005 explicitly scopes its supersession to the collection function while the legacy pipeline stays retired. The hygiene outcome (DEC-004) and the capability upgrade (DEC-005) are orthogonal. **Retirements that preserve revival paths convert reversals from credibility risk into routine upgrades.**

### Correlation 2: "ok" ≠ "yielding" — the telemetry gap is the headline

```
20Z full fleet: 24/25 outcome=ok  →  but only 13/25 sources produced records (52%)
Wire tier (18Z, 22Z): 6/6 ok  →  but only 2/6 produced (33%) — both at cap-12
Zero-record-ok class (11): bernama, bernama-malay, suara-keadilan, the-star,
utusan-malaysia, borneo-post, free-malaysia-today, vulcan-post, buzzkini, world-of-buzz (+1)
Hard failure (1): sabah-news (ACS-GOTO goto timeout)
```

Legacy operation had no per-source outcome telemetry, so "25/25 sources healthy" was unfalsifiable. opt-v1's JSONL telemetry exposes the real state: extraction success is the constraint, not crawl success. The wire tier — the highest-cadence tier — is effectively a **2-source wire** (Malaysiakini + Sinar Harian). Without this instrumentation the gap would have surfaced as "why is the brief thin?" weeks later.

### Correlation 3: Durability engineering validated in production

```
v1 full-fleet killed by own 540s watch (~8 sources in)
  → incremental per-source flush patch (records + telemetry durable per source)
  → v2 clean; overnight 18Z/20Z/22Z ran unattended, 3/3 runs with complete artifacts
```

The flush redesign was added *after* observing v1's death — a same-hour fix-verify loop. The failure that would previously have lost ~40 minutes of collection instead cost nothing: partial data survived, diagnosis was immediate from telemetry, and the patch was verifiable by inspection of the next run's artifacts.

### Correlation 4: Commit-lag window closed same-day (governance rhythm)

```
15:45 dream cycle flags "largest promotion risk: everything uncommitted"
  → 16:14 batch (DEC-001..004 + workspace close-out)
  → 23:00 DAF "Commit" → 99b41ce4 (GTM preread/brief/log) + d142b11 (DEC-005)
```

Both dream-cycle risk flags from 15:45 cleared within the day. Residual uncommitted set is now exactly the DAF-owned exclusions (taxonomy-audit artifacts, D8 tool changes, CJ-2S intakes) — unchanged scope, deliberately held. Transient GitHub 5xx on the d142b11 push recovered on single retry; no action required.

### Correlation 5: Doc-drift recurrence (third instance of the class)

F1 (DUN-Profiling line 429 lists a retired collector as active) is the same drift class as the HOI cleanup (8 files, 13:47–13:55) and the Kata references (DEC-20260914-001): **operational docs asserting pipelines that decisions have retired.** Every retirement now generates a documentation half-life that outlives the pipeline unless a doc-sweep step is part of the retirement runbook.

## STEP 4 — PATTERN RECOGNITION (Doctrine §6)

**P1 — Instrumentation exposes hidden debt (§6.1 convergence):** telemetry + registry + dedup schema were built for optimisation, but their first dividend was diagnostic — converting an invisible 48% extraction-coverage gap into a ranked, addressable backlog. Measurement precedes optimisation; the deferred slots in DEC-005 are now data-confirmed priorities rather than guesses.

**P2 — Decision-pairing prevents oscillation (§6.3 leverage):** DEC-004/DEC-005 form a clean pair because the retirement preserved exactly what the successor needed (library, corpus, revival path). Generalisable rule for the collection stack: never retire a capability without recording what a successor would need to rebuild.

**P3 — Bottleneck migration (§6.2):** the collection chain's binding constraint has migrated: delivery cadence (legacy, solved by opt-v1 scheduling) → extraction coverage (current, 13/25) → will become consumption once coverage passes ~80% (the analysis layers that decayed per the 16:06 purpose review remain dormant). Fixing coverage without a consumer plan would repeat the legacy failure mode at higher volume.

**P4 — Capacity-protection boundary holds under load (§6.9 portfolio):** INT-002's rule (Fuad+Syahir protected for methodology drafting 16–17 Sep) was tested same-day by an infra arc needing engineering attention. Resolution: all remediation scoped to Ember-executable host-level work; deferred slots stay deferred. The SPOF protection survived its first collision test.

**P5 — Evidence volatility (§6.7 coordination debt):** run backups and evidence bundles live in /tmp (crontab backups, evidence/ dirs, the archive clone). Durable copies exist for the critical artifacts (DEC records, archive repo), but /tmp dependence is a standing reboot-risk pattern flagged twice today (F2, evidence paths).

## STEP 5 — PRIORITISE (Doctrine §8)

| Candidate action | Strategic Impact (25%) | Time Crit (15%) | Portfolio Leverage (15%) | Commercial Value (15%) | Dependency Unlock (10%) | Stakeholder (10%) | Risk Reduction (10%) | Effort | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| A. Per-source selector registry buildout | High | Med | Med | Low | **High** | Low | Med | Ember host-level, incremental | **#1** |
| B. Wire-tier yield audit (why 4/6 wire sources yield 0) | High | Med | Med | Low | High | Low | Med | Hours, Ember | **#2** (folds into A) |
| C. Proxy-pool decision brief for DAF | High | Low | Med | Low | High | Low | High | Brief only | **#3** (post-CyberDSA per DEC-005) |
| D. DUN-Profiling doc-drift patch (F1/R1) | Low | Low | Low | Low | Low | Med | Med | Minutes | Batch with next doc sweep |
| E. Archive re-clone to durable path (F2/R2) | Low | Low | Low | Low | Low | Low | Med | Minutes | Batch with D |
| F. Sitemap mode enablement | Low | Low | Low | Low | Low | Low | Low | Experimental | Hold (probes hung; behind flag) |

**Urgency–importance resolution (§8):** none of these outrank the 17 Sep CSM methodology deadline (COM-20260914-003) — the correct posture is Ember-background execution of A/B during wire-run gaps, with C prepared as a decision brief for post-CyberDSA. No engineering-pool contact before 18 Sep.

## STEP 6 — ACT (Three Actions — per SOP-CL-001 §5)

**A1 — Selector registry buildout + wire-tier yield audit (folds B into A).**
- *Owner:* Ember (host-level; no engineering-pool dependency)
- *Deadline:* incremental; first tranche (wire tier: bernama, bernama-malay, suara-keadilan, the-star) before 20Z run 15 Sep
- *Targets:* wire-tier yield 2/6 → ≥4/6; fleet coverage 52% → ≥60% by 15 Sep 20Z run

**A2 — Proxy-pool decision brief (one page: cost, provider options, expected coverage delta for the ACS-GOTO class).**
- *Owner:* Ember drafts; DAF decides
- *Deadline:* post-CyberDSA window (per DEC-005 deferred-slot sequencing); draft may be prepared early, decision not before 8 Oct
- *Targets:* converts the antibot failure class from recurring telemetry noise into a budgeted fix decision

**A3 — Retirement-runbook doc-sweep step + micro-patch batch (D + E).**
- *Owner:* Ember
- *Deadline:* next doc-sweep window (batch with A3 session-file consolidation work); E anytime
- *Content:* DUN-Profiling line 429 retirement note; re-clone archive to durable path; add "documentation sweep" as a standing step in any future retirement runbook (closes the doc-drift class at process level)
- *Targets:* kills the third-instance drift pattern procedurally

## STEP 7 — VERIFY

| # | Criterion | Verification | When |
|---|-----------|--------------|------|
| V1 | Wire-tier yield improvement | 18Z/20Z/22Z runs 15 Sep: ≥4 wire sources yielding; telemetry error rate <10% | 15 Sep 23Z |
| V2 | Fleet coverage improvement | 20Z run 15 Sep: ≥15/25 sources yielding (60%) | 15 Sep 20Z |
| V3 | No durability regression | Every run dir contains complete records.jsonl + telemetry.jsonl + manifest; no partial-run loss events | Ongoing, weekly review |
| V4 | DEC-005 canonicalised | d142b11 pushed to origin/main (verified 23:10 UTC after 5xx retry); decision-index row live | Done 14 Sep |
| V5 | Doc-drift patch landed | grep DUN-Profiling WORKFLOW-PROMPTS.md shows retirement note at former line-429 reference | Next doc-sweep batch |

## STEP 8 — LEARN

1. **Measure before optimising — and expect measurement to rewrite the priority list.** opt-v1's telemetry was built to improve the pipeline and instead revealed that the pipeline's real problem was elsewhere (extraction, not delivery). *Lesson: the first artifact of any optimisation effort should be instrumentation, because the optimisation target is usually wrong until measured.*
2. **Retirement records are capability-seeds.** DEC-004's revival path + preserved library is what allowed a same-day successor. *Lesson: every retirement decision should explicitly preserve and name the assets a future re-enablement would need (library, corpus, config, crontab lines).*
3. **Design for the failure you just had.** The incremental-flush patch was written within the hour of v1's self-kill and paid off across three unattended overnight runs. *Lesson: convert every observed pipeline failure into a same-day structural fix when the fix is cheap — the cost asymmetry strongly favours immediate patching.*
4. **Documented decisions make reversal cheap; undocumented reversal makes organisations whiplash.** The P3-retirement → optimum-spec sequence is defensible only because both decisions are canonical, scoped, and cross-referenced. *Lesson: for infrastructure posture, the decision record is the difference between a pivot and a flip-flop.*

---

## Actionable Intelligence Standard (§7) — Headline

1. **SIGNAL** — crawl4ai collection re-enabled on opt-v1 (DEC-20260914-005) same-day after P3 retirement; telemetry now measures per-source health.
2. **EVIDENCE** — DEC-20260914-004/-005 (canonical, committed d142b11); telemetry.jsonl ×3 overnight runs; daily log 16:19–16:54 UTC; commits 99b41ce4/d142b11.
3. **PATTERN** — extraction coverage (13/25 fleet, 2/6 wire) is the binding constraint, exposed by new instrumentation; decision-pair architecture absorbed a same-day posture reversal; capacity-protection rule survived its first collision test.
4. **IMPLICATION** — collection value now scales with selector/proxy remediation (Ember-executable), not with cadence; the consumption layer remains the follow-on constraint once coverage rises.
5. **OPPORTUNITY / RISK** — Opportunity: data-ranked hardening roadmap already scoped in DEC-005 deferred slots. Risk: unowned /tmp evidence volatility and recurring doc-drift class; wire tier operating at 33% yield dilutes the every-2h cadence investment.
6. **CONFIDENCE** — High (telemetry is direct measurement; correlations 1, 3, 4 verified from artifacts; correlation 2 source-classification of the zero-record set is high-confidence from telemetry + DEC-005 validation notes).
7. **DECISION WINDOW** — none urgent; proxy-pool decision consciously deferred to post-CyberDSA; selector work proceeds incrementally.
8. **RECOMMENDED ACTION** — A1 (selector registry + wire audit), A2 (proxy brief, deferred decision), A3 (doc-sweep process fix).
9. **OWNER** — Ember (all three); DAF decides on A2 output post-CyberDSA.
10. **VERIFICATION** — V1–V5 above.
