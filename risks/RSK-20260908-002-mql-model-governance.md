---
# === UNIVERSAL BASE ===
id: RSK-20260908-002
record_type: risk
title: "78-MQL target governed by unresolved conversion model — 413×19% vs 1,300×20%→260×30%; enrichment is single point of reconciliation"
created_at: 2026-09-08T13:40:00+00:00
updated_at: 2026-09-08T13:40:00+00:00
owner: faurani-jaafar
status: active
priority: high
sensitivity: internal
lifecycle_state: canonical
confidence: high
tags:
  - domain/commercial-strategy
  - domain/risk-management
  - workstream/commercial-dev
source:
  type: analysis
  reference: "Plan review 2026-09-08 (workspace memory/2026-09-08.md). Plan: 78 MQLs from 413 named individuals = 19% vs approved GTM framework 6% of ~1,300 universe. DAF Aug-21 email: 1,300×20%=260 engaged → 30% → 78 meetings → 23 POC → 7 sales → RM1.176M. Plan contact data internally inconsistent: 413 distinct vs 513 tier-table sum vs 493 wave sum."
summary: "[FACT] The plan's 78 MQLs assume 19% conversion of 413 named individuals — 3× the 6% rate in the approved GTM framework — justified by enrichment expansion toward 900–1,000 real inboxes. [FACT] DAF's own Aug-21 matrix reaches 78 via a different chain (1,300 universe × 20% engagement × 30% meeting). [DISPUTED] Which model governs the 78 — and therefore what Sales is promised and what enrichment must deliver — is not stated in the plan. Additionally the contact-basis numbers (413/513/493) do not reconcile, so the 19% denominator itself is ambiguous."
strategic_significance: "If the 413×19% model governs and enrichment slips, 78 is unachievable and the November/December concentration (two-thirds of MQLs) collapses. If the 1,300 model governs, Wave coverage assumptions (493 named people across 3 waves) are undersized. The Sep 15 session must declare one canonical model; the enrichment line (RM10k inside RM30k) is the mechanism that makes either model executable."
mission_alignment:
  - commercial-growth
related_records:
  - INIT-20260908-001
  - CONV-20260908-002
  - RSK-20260908-001
# === RISK FIELDS [Operational + Tactical] ===
risk_category: planning/conversion-assumption
probability: high
impact: medium
mitigation_strategy: "At Sep 15 session: declare canonical model (recommend 413-base with enrichment-adjusted denominator restated in writing), fix contact-basis discrepancies (413/513/493), and bind Wave targets to the canonical denominator. Treat 78 as enrichment-conditional, not base case."
mitigation_owner: faurani-jaafar
trigger_conditions: "Enrichment brief not approved Sep 15; or wave lists built without re-stated denominators; or weekly MQL handover shows <2/week cumulative pace by Oct 10."
related_initiative:
  - INIT-20260908-001
---
