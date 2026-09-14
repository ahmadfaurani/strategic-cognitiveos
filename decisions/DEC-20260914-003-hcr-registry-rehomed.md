---
# === UNIVERSAL BASE ===
id: DEC-20260914-003
record_type: decision
title: "HCR Registry Rehomed to Dedicated Private Repository (ahmadfaurani/hcr-registry) — Hermes-Created-Repos Catalog Decoupled from HOI Repo"
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
  - mission/intelligence-enablement
  - mission/organisational-capability
  - type/consolidation
source:
  type: telegram
  reference: "DAF directive via Telegram direct, 2026-09-14: 'HCR rehome to its own repo.' (response to the HOI legacy review pending-items list; executed 14:53-15:05 UTC)"
summary: "[FACT] DAF decision: HCR-REGISTRY.md — the 'Hermes Created Repos' catalog (97 entries: 93 actual + 4 phantom, next ID HCR-100), historically maintained inside the hoi-intelligence-ops repository — is rehomed to a dedicated private repository, github.com/ahmadfaurani/hcr-registry. Executed 14 Sep 14:53-15:05 UTC: registry migrated as initial commit 799915c with a canonical README; redirect banner pushed to the old file in hoi-intelligence-ops (commit 70004af) marking it a historical snapshot; stray untracked script finalize-entities-myt.py archived to workspace archive/hcr-rehome-20260914/; both stale local hoi-intelligence-ops clones trashed (DEC-20260914-002). Triggering anomaly resolved: the 13 Sep hoi-intelligence-ops commit ('registry: add HCR-099 sovereign-ai-pir', authored Ember) was fleet registry bookkeeping logging Hermes's new sovereign-ai-pir workspace (HCR-099: sovereign AI x PQC PIR collection & registry, owner DAF, agent Laras/Hermes + CJ-2S collection fleet, 10-PIR registry, 138 collection cycles 26 Jul-13 Sep, 120 CSCDC PIRs, TLP:AMBER) — not a revived HOI process. Standing lesson recorded: the Hermes fleet operates a separate cron plane (cronjob-configs.json: CJ-2S-A 06:45 every-2d PIR-01/02/04/05; CJ-2S-B 07:20 every-2d PIR-03/06/07/10; third job = remainder) invisible to OpenClaw cron; future stack reviews must cross-check Hermes-side cronjob-configs.json exports."
strategic_significance: "Severs the last functional coupling between the retired HOI repository and live Hermes-fleet infrastructure, clearing the path for eventual full disposition of hoi-intelligence-ops without touching fleet bookkeeping. Establishes hcr-registry as the canonical home for Hermes-created-repo tracking going forward and hardens stack-review methodology against the Hermes cron blind spot."
mission_alignment:
  - mission/intelligence-enablement
related_records:
  - INIT-20260710-002
  - DEC-20260914-002
# === DECISION FIELDS [Structural] ===
context: "HCR-REGISTRY.md is the 'Hermes Created Repos' catalog — 97 entries (93 actual repositories + 4 phantom), next ID HCR-100 — maintained by the Hermes fleet inside the hoi-intelligence-ops repository. On 13 Sep 2026 the remote repo received a commit authored Ember ('registry: add HCR-099 sovereign-ai-pir') that no local clone produced, triggering an unexplained-push anomaly during the 14 Sep stack review. The 14:37-14:45 HCR-099 overview resolved the anomaly as routine fleet bookkeeping: HCR-099 is the sovereign-ai-pir workspace (sovereign AI x PQC PIR collection & registry; owner DAF; agent Laras/Hermes with the CJ-2S collection fleet; 10-PIR registry; 138 collection cycles 26 Jul-13 Sep; CSCDC PIR inventory of 120; stakeholder registry of 17 names; TLP:AMBER, CVS-validated). The registry's placement inside the retired HOI repo was the remaining coupling identified by the HOI legacy review."
decision: "Rehome the HCR registry to its own repository: create private repo github.com/ahmadfaurani/hcr-registry; migrate HCR-REGISTRY.md (97 entries, next=HCR-100) as the initial commit (799915c) with a canonical README; push a redirect banner to the old file in hoi-intelligence-ops (commit 70004af) marking it a historical snapshot; archive the stray untracked script finalize-entities-myt.py to workspace archive/hcr-rehome-20260914/. hoi-intelligence-ops no longer carries a canonical registry role."
rationale: "The registry is Hermes-fleet infrastructure, not HOI intelligence content; housing it in a retired repo created a live dependency that blocked clean disposition of hoi-intelligence-ops and confused ownership (the 13 Sep push appeared anomalous precisely because the coupling was undocumented). A dedicated repo gives the fleet an unambiguous canonical home. The same review established that the Hermes fleet runs its own cron plane (cronjob-configs.json) invisible to OpenClaw — stack reviews must cross-check it going forward."
alternatives_considered:
  - "(a) Leave the registry in hoi-intelligence-ops — rejected: preserves the zombie coupling and keeps a retired repo load-bearing for live fleet operations."
  - "(b) Absorb the registry into CognitiveOS — rejected: wrong plane; the catalog tracks Hermes-fleet-created repositories and is maintained by fleet-side agents, not CognitiveOS governance."
confirmed_by: faurani-jaafar
confirmed_at: '2026-09-14T14:50:00+00:00'
---

# Context

HCR-REGISTRY.md — the "Hermes Created Repos" catalog (97 entries: 93 actual + 4 phantom; next ID HCR-100) — has been maintained by the Hermes fleet inside the hoi-intelligence-ops repository. On 13 Sep 2026 the remote repo received a commit authored Ember ("registry: add HCR-099 sovereign-ai-pir") that no local clone produced; the 14 Sep stack review flagged this as an unexplained push. The 14:37-14:45 HCR-099 overview resolved it: the commit was fleet registry bookkeeping logging HCR-099, the sovereign-ai-pir workspace (sovereign AI x PQC PIR collection & registry; owner DAF; agent Laras/Hermes + CJ-2S collection fleet; 10-PIR registry; 138 collection cycles 26 Jul-13 Sep; 120 CSCDC PIRs; 17-name stakeholder registry; TLP:AMBER, CVS-validated). With HOI retired as an operational entity (DEC-20260914-002), the registry was the last live dependency inside the HOI repo.

# Decision

DAF directed: "HCR rehome to its own repo." Executed 14 Sep 2026, 14:53-15:05 UTC:

- **Created** private repository `github.com/ahmadfaurani/hcr-registry`.
- **Migrated** HCR-REGISTRY.md (97 entries, next=HCR-100) as initial commit `799915c` with a canonical README.
- **Redirect banner** pushed to the old file in hoi-intelligence-ops (commit `70004af`): "REHOMED 2026-09-14 — canonical registry moved to hcr-registry; this file is a historical snapshot."
- **Archived** the stray untracked script `finalize-entities-myt.py` to `archive/hcr-rehome-20260914/`.
- **Local clone coupling severed** — both stale local hoi-intelligence-ops clones trashed in the same batch (disposition recorded under DEC-20260914-002).

# Rationale

The registry is Hermes-fleet infrastructure, not HOI content. Housing it in a retired repository created a live dependency that (a) blocks clean future disposition of hoi-intelligence-ops and (b) produced a false-positive security anomaly — the 13 Sep push looked unexplained only because the coupling was undocumented. A dedicated private repo gives the fleet an unambiguous canonical home and decouples two systems that have different owners, cadences, and lifecycles. Standing lesson recorded for stack reviews: the Hermes fleet operates a separate cron plane (cronjob-configs.json — CJ-2S-A 06:45 every-2d PIR-01/02/04/05; CJ-2S-B 07:20 every-2d PIR-03/06/07/10; third job = remainder) invisible to OpenClaw cron; future reviews must cross-check Hermes-side cronjob-configs.json exports.

# Alternatives Considered

- Leave registry in hoi-intelligence-ops — rejected: keeps a retired repo load-bearing for live fleet operations.
- Absorb into CognitiveOS — rejected: wrong plane; fleet-maintained asset catalog, not CognitiveOS governance content.

# Confirmation

DAF, Telegram direct, 14 September 2026 ("HCR rehome to its own repo."), executed 14:53-15:05 UTC.
