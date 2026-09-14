---
# === UNIVERSAL BASE ===
id: DEC-20260914-002
record_type: decision
title: "HOI Legacy Agent References Retired from Operational Documentation — Active Collection Pipeline, TLP:AMBER Archives, and Hermes Catalog Role Deliberately Preserved"
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
  - domain/intelligence
  - mission/intelligence-enablement
  - mission/organisational-capability
  - type/retirement
source:
  type: telegram
  reference: "DAF directive via Telegram direct, 2026-09-14 within the 13:47-13:55 UTC window: 'HOI ENTRIES REVIEW. HOI is a legacy that have been retired' (directing documentation cleanup after the tech stack review flagged doc drift vs the retired agent)"
summary: "[FACT] DAF decision: HOI — the legacy pre-Ember intelligence agent with no remaining agent config, cron jobs, or systemd units — is formally treated as retired, and all operational documentation presenting HOI as an active component is corrected. Executed 14 Sep across 8 files: HEARTBEAT.md (GitHub sync scoped to CBO-01 only; 'Integration with HOI Agent' replaced by escalation integration via agent-main), critical-delivery-tasks.md (CDT-003 HOI June brief KILLED — deadline 2026-06-30, 3.5 months stale; scan source narrowed), reports/README.md (ownership to Ember), cybersecurity-practice-repo OPERATING-MODEL.md + README.md (workstream row retired, engagements pruned), integration-map.md (§2 HOI Collection Plan retired banner), AVR architecture brief (3 rows marked retired), STRATCOM Master Plan (historical-status note). Deliberately preserved on DAF-record: (1) ~/.openclaw/workspace-hoi/ 1.4GB — ACTIVE data sink for the political-monitoring crawl4ai pipeline (host crontab 08/12/16/23 UTC, ~108 files/day into intelligence/raw); (2) workstreams/09-hoi-intelligence/ + hoi-intel-workspace/ historical TLP:AMBER archives (newest activity 5 Sep); (3) remote hoi-intelligence-ops repo, which still serves as the Hermes-fleet registry catalog pending re-homing (DEC-20260914-003). Both stale local clones of hoi-intelligence-ops trashed 14:53-15:00 UTC after confirming no local-only work (remote held 187 commits local lacked); one untracked script archived first. Committed in workspace commit 7020bdb6."
strategic_significance: "Ends documentation drift that misdirected stack reviews, heartbeat automation, and workstream planning toward a dead agent, while explicitly protecting the still-live collection pipeline that merely carries the legacy name. Establishes the review-time distinction: HOI-the-agent = retired; workspace-hoi-the-pipeline = active; HOI archives = historical TLP:AMBER holdings."
mission_alignment:
  - mission/intelligence-enablement
related_records:
  - INIT-20260710-002
  - DEC-20260710-001
# === DECISION FIELDS [Structural] ===
context: "The 14 Sep 2026 tech stack review found the HOI daemon absent from the live stack while multiple operational documents still referenced HOI as an active integration. Investigation confirmed HOI is a legacy intelligence agent from the pre-Ember era: no agent configuration, no OpenClaw cron jobs, no systemd units reference it. Remaining footprint is documentation drift plus legacy data stores — including an ACTIVE political-monitoring crawl4ai pipeline writing ~108 files/day into ~/.openclaw/workspace-hoi/intelligence/raw on a host crontab (08/12/16/23 UTC), whose name merely carries the legacy label."
decision: "Retire HOI as an operational entity in all documentation: correct 8 files (HEARTBEAT.md, critical-delivery-tasks.md, reports/README.md, cybersecurity-practice-repo OPERATING-MODEL.md + README.md, integration-map.md §2, AVR architecture brief, STRATCOM Master Plan); kill stale CDT-003; reassign GitHub-sync ownership to CBO-01/Ember and escalation integration to agent-main. Deliberately preserve: the live workspace-hoi crawl4ai data sink, the workstreams/09-hoi-intelligence and hoi-intel-workspace TLP:AMBER archives, and the remote hoi-intelligence-ops repository pending full Hermes-catalog re-homing. Trash the two stale local clones of hoi-intelligence-ops."
rationale: "Documentation drift around a retired agent actively misleads automated checks (heartbeat scans, stack reviews) and wastes review cycles re-diagnosing the same ghost. At the same time, the crawl4ai pipeline under the legacy name is a live intelligence source — renaming or dismantling it risks breaking collection for cosmetic reasons, and the archive holdings retain intelligence value under TLP:AMBER handling. The surgical split (docs retired, pipeline preserved, archives retained) removes the drift without touching live capability."
alternatives_considered:
  - "(a) Full teardown including workspace-hoi data sink and pipeline rename — rejected: the pipeline is live (~108 files/day); renaming risks collection breakage for no operational gain, and repository re-homing is a separate Hermes-fleet decision."
  - "(b) Leave documentation as-is — rejected: the drift is what caused this review; it would keep misdirecting every future stack review and heartbeat scan."
confirmed_by: faurani-jaafar
confirmed_at: '2026-09-14T13:50:00+00:00'
---

# Context

The 14 Sep 2026 tech stack review surfaced drift between the documented and actual stack: HOI appeared in operational documents as an active integration, but no HOI agent config, OpenClaw cron job, or systemd unit exists. HOI is a legacy intelligence agent from the pre-Ember era. Its remaining footprint divides into (a) documentation drift, (b) an ACTIVE political-monitoring crawl4ai pipeline writing ~108 files/day into `~/.openclaw/workspace-hoi/intelligence/raw` on a host crontab (08/12/16/23 UTC) — the legacy name is incidental, the pipeline is live — and (c) historical intel archives (TLP:AMBER, newest activity 5 Sep). A 13 Sep commit to the remote hoi-intelligence-ops repo was separately resolved as Ember's registry bookkeeping for HCR-099 (see DEC-20260914-003), not a revived HOI process.

# Decision

DAF directed: "HOI ENTRIES REVIEW. HOI is a legacy that have been retired." Executed 14 Sep 2026:

- **Doc cleanup (8 files):** HEARTBEAT.md (GitHub sync → CBO-01 only; "Integration with HOI Agent" → escalation integration via agent-main); critical-delivery-tasks.md (CDT-003 HOI June brief KILLED — deadline was 2026-06-30, 3.5 months stale; scan source narrowed); reports/README.md (owner → Ember); cybersecurity-practice-repo OPERATING-MODEL.md + README.md (workstream row retired, engagements list pruned); integration-map.md (§2 HOI Collection Plan retired banner); AVR architecture brief (3 rows marked retired); STRATCOM Master Plan (historical-status note at header).
- **Deliberately preserved (pending separate decisions):** (1) `~/.openclaw/workspace-hoi/` 1.4GB — active crawl4ai collection sink; (2) `workstreams/09-hoi-intelligence/` + `hoi-intel-workspace/` historical TLP:AMBER archives; (3) the remote hoi-intelligence-ops repo, which still serves as the Hermes-fleet registry catalog until re-homing completes (DEC-20260914-003).
- **Local clones trashed (14:53-15:00 UTC batch):** both stale local clones of hoi-intelligence-ops via gio after verifying no local-only work (remote held 187 commits the local clone lacked); one untracked script (`finalize-entities-myt.py`) archived to `archive/hcr-rehome-20260914/` first.

Changes committed in workspace commit 7020bdb6.

# Rationale

A retired agent lingering in operational docs misdirects every automated and manual check that trusts documentation — heartbeat scans, stack reviews, workstream planning. Correcting the record restores trust in the docs as ground truth. The live crawl4ai pipeline is retained untouched because it is a producing intelligence source; the legacy directory name is not worth collection risk. Archives are retained for intelligence value under TLP:AMBER handling.

# Alternatives Considered

- Full teardown including the workspace-hoi data sink and pipeline rename — rejected: live collection source; cosmetic rename risks operational breakage; repo re-homing is a separate Hermes-fleet decision.
- No documentation change — rejected: the drift itself caused this review and would recur.

# Confirmation

DAF, Telegram direct, 14 September 2026, within the 13:47-13:55 UTC window.
