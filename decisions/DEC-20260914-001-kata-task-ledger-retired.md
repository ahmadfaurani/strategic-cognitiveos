---
# === UNIVERSAL BASE ===
id: DEC-20260914-001
record_type: decision
title: "Kata Task Ledger Retired — Total Cleanup (Export Archived, State+Binary Trashed, Heartbeat Sync References Removed; Task Truth Consolidated in CognitiveOS)"
created_at: "2026-09-14T15:45:00+00:00"
updated_at: "2026-09-14T15:45:00+00:00"
owner: faurani-jaafar
status: active
priority: medium
sensitivity: confidential
lifecycle_state: candidate
confidence: high
channel: telegram
decision_date: '2026-09-14'
decision_owner: faurani-jaafar
decision_type: structural
decision_weight: medium
tags:
  - domain/knowledge-management
  - domain/data-infrastructure
  - mission/organisational-capability
  - type/deprecation
source:
  type: telegram
  reference: "DAF directive via Telegram direct, 2026-09-14 within the 13:36-13:45 UTC stack-review window: 'Option 1. Total Kata cleanup.' (response to Kata status brief presenting retire-vs-revive options after the tech stack review flagged the dead daemon)"
summary: "[FACT] DAF decision: the Kata task ledger (agent-native issue-tracker CLI at ~/.local/bin/kata, state in ~/.kata/kata.db) is retired in full. Execution 2026-09-14: full DB export (12.7KB JSONL) + SQLite snapshot (262KB, last touched 21 May 2026) archived to workspace archive/kata-retirement-20260914/ with README and revival path (kata import after reinstall); ~/.kata/ state (284KB) and the 33MB binary trashed via gio (recoverable); the HEARTBEAT.md Kata Task Ledger Sync block and all operational references removed (heartbeat-state.json kata_sync key, critical-delivery-tasks.md scan row, reports/README.md bullet, 00-cdt-discovery README, 11-dpi HEARTBEAT-INTEGRATION.md row); historical mention retained in 09-hoi QUICKREF only. Verification: zero kata references in all six edited files; command -v kata returns nothing. Committed in workspace commit 7020bdb6. Cross-session task continuity is carried solely by CognitiveOS ACT records."
strategic_significance: "Removes a zombie instruction that silently burned heartbeat tokens every cycle against a daemon dead since May 2026, and eliminates a second task-truth source that competed with CognitiveOS canonical records. Closes inventory drift between documented and actual stack surfaced by the 13:36-13:45 tech stack review."
mission_alignment:
  - mission/organisational-capability
related_records:
  - INIT-20260724-001
  - AIP-20260829-002
# === DECISION FIELDS [Structural] ===
context: "Kata is a lightweight agent-native issue tracker — a local CLI backed by a SQLite task ledger with events, cursors, digest, and daemon components. HEARTBEAT.md carried a standing 'Kata Task Ledger Sync' block instructing every heartbeat to run kata health, poll events, append digests to daily memory, and flag blocked tasks. The 13:36-13:45 UTC 14 Sep tech stack review found the daemon not running, the database untouched since 21 May 2026 (~16 weeks), the agent-cursors.json file absent, and no real sync since early June. Its cross-session task-continuity role had been fully absorbed by CognitiveOS ACT records, which doctrine designates as canonical task truth."
decision: "Execute Option 1 — total Kata cleanup: (1) export the ledger (kata export) and snapshot the SQLite DB into archive/kata-retirement-20260914/ with a README documenting removal and the revival path; (2) trash ~/.kata/ state and the ~/.local/bin/kata binary via gio (recoverable, not rm); (3) remove the Kata sync block from HEARTBEAT.md and every operational reference across workspace docs; (4) retain a historical mention in the 09-hoi QUICKREF only."
rationale: "The heartbeat block was a zombie instruction: it consumed tokens every cycle instructing work against a dead daemon, and Kata's purpose (cross-session task continuity) is already served — canonically — by CognitiveOS ACT records. Keeping a dormant second task ledger risks future agents treating stale Kata state as truth. Archiving before deletion preserves the historical issue data at negligible cost."
alternatives_considered:
  - "(a) Revive — restart the daemon, re-baseline cursors, keep Kata as an agent-local task layer beside CognitiveOS — rejected: duplicates the canonical task truth and re-creates the drift the CognitiveOS consolidation was meant to eliminate."
  - "(b) Leave dormant with the heartbeat block intact — rejected: continued silent token burn and ongoing inventory drift."
confirmed_by: faurani-jaafar
confirmed_at: '2026-09-14T13:40:00+00:00'
---

# Context

Kata is a lightweight, agent-native issue tracker — a small CLI (`~/.local/bin/kata`) running a local SQLite task ledger (`~/.kata/kata.db`), with `create/assign/close`, an event stream with cursors, `digest`, and a background `daemon`. HEARTBEAT.md carried a standing "Kata Task Ledger Sync" block: every heartbeat was to run `kata health`, poll new events, append an 8h digest to the daily memory file, and flag blocked tasks. It was positioned as the cross-session task continuity layer before CognitiveOS absorbed that role.

The 14 Sep 2026 tech stack review (13:36-13:45 UTC) found: daemon not running; database last touched 21 May 2026 (~16 weeks stale); cursor file (`agent-cursors.json`) absent; last real sync logged in early June and itself flagged "pending manual run". CognitiveOS ACT records are canonical task truth per doctrine.

# Decision

DAF directed "Option 1. Total Kata cleanup." Executed 14 Sep 2026:

- **Archived** to `archive/kata-retirement-20260914/`: full DB export `kata-export-20260914T134031Z.jsonl` (12.7KB), SQLite snapshot `kata.db.snapshot` (262KB), and a README documenting removal plus the revival path (`kata import` after reinstall).
- **Trashed** (gio, recoverable): `~/.kata/` state (284KB) and the `~/.local/bin/kata` binary (33MB).
- **Operational references removed** from 6 locations: HEARTBEAT.md Kata Sync section, `heartbeat-state.json` `kata_sync` key, critical-delivery-tasks.md scan row, reports/README.md bullet, 00-cdt-discovery README (source table + scan step), 11-dpi HEARTBEAT-INTEGRATION.md row.
- **Historical mention retained** in 09-hoi QUICKREF only.

Verification: zero kata references across all six edited files; `command -v kata` returns nothing. Changes committed in workspace commit 7020bdb6.

# Rationale

The heartbeat block was a zombie instruction — silently burning tokens every cycle against a daemon dead since May. Kata's function is fully superseded by CognitiveOS ACT records, and retaining a dormant second task ledger invites future sessions to treat stale Kata state as authoritative. Archive-before-delete keeps the historical issue data recoverable at negligible cost.

# Alternatives Considered

- Revive (daemon restart + cursor re-baseline) — rejected: duplicates canonical task truth already held by CognitiveOS.
- Leave dormant — rejected: continued token burn and inventory drift.

# Confirmation

DAF, Telegram direct, 14 September 2026, within the 13:36-13:45 UTC stack-review window.
