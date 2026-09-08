---
id: LSN-20260907-001
record_type: lesson
title: "Filename convention violation + BRE alternation misuse + unguarded head pipe — cascading exec failure on RISIK intake"
created_at: 2026-09-07T01:31:00+00:00
updated_at: 2026-09-07T01:31:00+00:00
owner: faurani-jaafar
status: active
priority: medium
sensitivity: internal
lifecycle_state: canonical
confidence: high
tags:
  - domain/cognitiveos-operations
  - domain/execution-management
  - type/operator-error
  - type/naming-convention
  - type/shell-quoting
  - type/silent-pipe-failure
source:
  type: incident
  reference: "Exec failure card 2026-09-07 01:21 UTC during CONV-20260907-001 intake processing (MCMC RISIK invitation)"
summary: "Three-part failure chain during intake processing: (1) grep invoked with alternation pattern 'RISIK-AI-PLATFORM|RM5|RM 5' WITHOUT -E — in default BRE mode '|' is a literal character, so the pattern matched nothing and exited 1; (2) head was piped into the terminal instead of redirected from a file (head -60 of /dev/null), producing no output with exit 0 — masking the upstream grep failure; (3) organizations/ORG-20260815-004.md was referenced by bare-ID guess but the canonical filename is ORG-20260815-004-mcmc.md (suffixed). The exec error card surfaced all three to the operator. Root causes: filename guessed from record ID instead of resolved via find; BRE/ERE alternation semantics misapplied; unguarded pipes into terminal with no file-existence check."
strategic_significance: "CognitiveOS holds 520+ records where ~85% of action/decision/stakeholder files are bare-ID but organizations are 83% suffixed — bare-ID guessing is structurally unreliable and every failed read burns operator attention and pollutes the session with error cards. Silent pipe failures (exit 0 on empty input) can fabricate 'no data' conclusions from broken queries — an evidence-integrity risk for an intelligence practice. Codified rule: resolve IDs with find before any read; always use grep -E for alternation; guard every head/cat with a file test."
mission_alignment:
  - organizational-capability-building
related_records:
  - CONV-20260907-001
  - ACT-20260907-001
---

# LSN-20260907-001 — Exec Failure RCA: RISIK Intake Processing

## Incident Chain (3 failures, 1 command block)

| # | Failure | Mechanism | Effect |
|---|---------|-----------|--------|
| 1 | grep returned nothing (exit 1) | `'RISIK-AI-PLATFORM\|RM5\|RM 5'` in BRE mode → `\|` treated as literal, not alternation | Search appeared to find no RISIK pricing references |
| 2 | head output empty (exit 0) | `head -60 of 2>/dev/null` — piped into terminal instead of redirected from file | Masked failure #1; looked like "no content" |
| 3 | head: No such file or directory | `organizations/ORG-20260815-004.md` guessed from record ID; canonical file is `ORG-20260815-004-mcmc.md` | Read aborted (exit 1) → error card to operator |

## Root Causes

1. **Filename guessed from record ID.** The CognitiveOS convention is inconsistent by design era: ~85% of actions/decisions/stakeholders/risks use bare-ID filenames (`ACT-20260907-001.md`), but organizations are 83% suffixed (`ORG-20260815-004-mcmc.md`). ID → filename mapping must be resolved, never assumed.
2. **BRE/ERE confusion.** In grep's default mode, `\|` is a literal pipe. Alternation requires `-E` (or `\|` only in GNU BRE extension contexts — never rely on it).
3. **Unguarded pipes.** `head`/`cat` into the terminal with no `[ -s file ]` check converts a broken query into a silent "no data" — the worst failure mode for evidence-driven work.

## Codified Rules (standing)

1. **Resolve before read:** `find . -name "<ID>*.md"` before any `head`/`read` of a record.
2. **Always `-E` for alternation:** `grep -rniE "a|b|c"`.
3. **Guard every read:** `[ -s "$f" ] && head -N "$f" || echo "EMPTY/MISSING: $f"`.
4. **Redirect, don't pipe:** file reads use redirection; pipes only into `wc`/`grep -c` counters.

## Remediation Applied (2026-09-07 01:31 UTC)

- ORG-20260815-004 read completed via resolved path; key_contacts updated (added STK-20260828-001 Aravind, STK-20260907-001 Azim); Current Position updated with 10 Sep session.
- CONV-20260907-001 related_records completed (added ORG-20260815-004).
- All three intake records verified: every referenced ID resolves to an existing file.
