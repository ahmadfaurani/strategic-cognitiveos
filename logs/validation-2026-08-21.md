# SOP-AV-001 Validation Report — 2026-08-21

## Scan Summary
- Actions scanned: 95 (draft status)
- Evidence sources: DEC(50), DOC(16), COM(16), OUT(3), ENG(41), RSK(35), INIT(34), daily notes(30), MEMORY.md, indexes(18)

## Results
- CONFIRMED corrections applied: 12
- PROBABLE — needs DAF review: 46
- Genuinely pending (no evidence): 46

## Applied Corrections
- ACT-20260808-010 -> completed (evidence: DEC-20260808-001)
- ACT-20260813-004 -> completed (evidence: COM-20260813-001)
- ACT-20260815-003 -> completed (evidence: 2026-08-20-1110)
- ACT-20260819-003 -> completed (evidence: DEC-20260819-005)
- ACT-20260819-004 -> completed (evidence: DEC-20260819-005)
- ACT-20260819-006 -> completed (evidence: 2026-08-21-0720)
- ACT-20260820-003 -> completed (evidence: COM-20260820-002)
- ACT-20260820-004 -> completed (evidence: 2026-08-20-1723)
- ACT-20260802-006 -> completed (evidence: SOP-CL-001)
- ACT-20260813-001 -> completed (evidence: DOC-20260818-001)
- ACT-20260813-003 -> completed (evidence: ACT-20260813-002)
- ACT-20260807-001 -> completed (evidence: COM-20260807-001)

## Key Findings
1. 12 actions confirmed completed but left in draft status — all corrected
2. 46 actions have probable evidence but need human confirmation
3. 46 actions have no evidence — genuinely pending or abandoned
4. Aug 4 planning spike: 12 of the 46 stale actions came from a single day
5. DEC-20260819-005 (Activation Framework) spawned 8 P0 actions — these are active, not stale

## Rule Effectiveness
- V1 (Decision Supersession): Most powerful — caught 5 of 12 confirmed
- V2 (Document Fulfilment): Caught 2 (agenda doc, SOP-CL-001)
- V3 (Commitment Resolution): Caught 3 (COM references with completion language)
- V9 (Daily Memory Event): Caught 2 (completion terms in daily notes)
- V12 (Owner Drift): Retired from this run — too noisy, needs semantic calibration
- V13 (Deadline Staleness): Effective for identifying genuinely stale actions

## Next Steps
- Phase 2: Build validate-actions.sh script for deterministic rules
- Present 46 PROBABLE items at Tuesday review for DAF adjudication
- Triage 46 genuinely pending: archive stale, assign deadlines to live items
