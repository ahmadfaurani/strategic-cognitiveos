---
# === UNIVERSAL BASE ===
id: DRAFT-20260908-002
record_type: draft
title: "Change Manifest — CyberDSA T-45 Sales Thread + Invitation List Intake (CognitiveOS, PROPOSE mode)"
created_at: 2026-09-08T14:10:00+00:00
updated_at: 2026-09-08T14:10:00+00:00
owner: faurani-jaafar
status: active
priority: high
sensitivity: confidential
lifecycle_state: candidate
confidence: high
tags:
  - type/documentation
  - domain/stakeholder-engagement
  - domain/commercial-strategy
  - workstream/commercial-dev
  - milestone/cyberdsa-2026
source:
  type: telegram-direct
  reference: "CYBER DSA T-45 thread + invitation xlsx forwarded by DAF, 2026-09-08 13:49–13:53 UTC; CognitiveOS intake directive 13:56 UTC"
summary: "PROPOSE-mode change manifest for the CyberDSA T-45 Sales thread and consolidated invitation list: 11 proposed records (CONV-20260908-003, ORG-20260908-001, STK-20260908-001~008, ART-20260908-002), 4 STK role updates, index syncs. Awaiting DAF validation per AI-PROCESSOR-INSTRUCTIONS v0.2 Step 11."
strategic_significance: "Review instrument for the Sales-side CyberDSA intake — completes the GTM picture: marketing plan (DRAFT-20260908-001 manifest) + sales invitation engine (this manifest) now both captured and cross-linked."
mission_alignment:
  - commercial-growth
related_records:
  - DRAFT-20260908-001
  - CONV-20260908-003
  - ORG-20260908-001
  - ART-20260908-002
draft_type: change-manifest
related_action: ACT-20260908-004
content_summary: >-
  11 new records + 4 STK role updates + 2 index syncs from the CyberDSA T-45
  thread (Aug 9–25) and the consolidated invitation list (21 orgs / 43 reps /
  12 TBA). BSN elevated to lighthouse org record with CFO/CRO named as DAF
  priorities. Validation gate passed 2026-09-08 (commits 44802cc, c9b923d +
  this supplement).
---

# Change Manifest — CyberDSA T-45 Sales Thread + Invitation List Intake

**Source:** Email thread (8 emails, Aug 9–25 2026) + CYBER_DSA_2026 invitation xlsx, forwarded by DAF via Telegram 2026-09-08 13:49–13:53 UTC
**Processing mode:** PROPOSE
**Sensitivity:** confidential (customer names, stakeholder identities, account coverage)
**Directive check:** DAF's "CognitiveOS Intake for the above" (13:56 UTC) = processing instruction from accountable owner via authenticated Telegram channel — valid instruction.

## Proposed Records (already written; states per intake precedent)

1. **CONV-20260908-003** — CyberDSA T-45 Sales×Practice coordination thread (Aug 9–25) — conversation — invitation programme, T-45 phases, enablement directives, BSN prioritisation
2. **ORG-20260908-001** — Bank Simpanan Nasional — organization — Tier 1 lighthouse candidate
3. **STK-20260908-001** — Norhafizah Md Shariff (CFO, BSN) — stakeholder — DAF engagement priority [confidence: medium — name from DAF's database citation, not independently verified]
4. **STK-20260908-002** — Muizz Aiman Farid (SVP/CRO, BSN) — stakeholder — DAF engagement priority [confidence: medium]
5. **STK-20260908-003** — Sujit Guha Thakurta (SVP/CCO, BSN) — stakeholder
6. **STK-20260908-004** — Asrul Kamaruddin (CIO, BSN) — stakeholder
7. **STK-20260908-005** — Mohd Nazri (Aras Sales) — stakeholder
8. **STK-20260908-006** — Hadif Hassan (Aras Sales) — stakeholder
9. **STK-20260908-007** — Nur Edleen Ismail (Aras, role TBD) — stakeholder
10. **STK-20260908-008** — Sirilah Raman (VP/BCM, BSN) — stakeholder — only named BSN invitee (this supplement)
11. **ART-20260908-002** — Invitation list xlsx registered with parsed analysis — artifact — 21 orgs / 43 reps / 12 TBA / BSN gap flagged

## Proposed Updates (written)

1. **STK-20260808-003** (Shuhada) — role: Sales → Sales Director; CyberDSA invitation programme lead; FSI coverage lead
2. **STK-20260811-002/003** (Nik Sarah, Jasila) — role TBD → invitation owners (4 orgs × 3 reps)
3. **STK-20260815-006** (Azirul) — role TBD → invitation owner
4. **Indexes** — organization-index (+ORG-20260908-001), stakeholder-index (+4 BSN prospects, +3 sales contacts, role updates), conversation-index (+CONV-20260908-003, this supplement)

## Validation Gate Results

- [x] Tier 1 claims verified or tagged — list figures from direct file parse (math shown in ART-20260908-002 summary); BSN stakeholder names [SOURCE_ASSERTION] per DAF's database citation, confidence medium
- [x] Epistemic types applied — gaps/inferences tagged (27% TBA, BSN CFO/CRO absent from list)
- [x] Schema validation passed — pre-commit validator green (commits 44802cc, c9b923d); YAML colon fix applied to 3 role strings
- [x] Taxonomy compliance — tags from tags.yaml
- [x] Reference integrity — cross-links CONV↔ORG↔STK↔ART verified
- [x] Contradictory evidence documented — BSN named priorities (DAF) vs invitation list contents (Shu) = discrepancy flagged

## Flagged Items

1. **BSN CFO/CRO gap** — DAF's named priorities absent from invitation list (rows 8–9 TBA); needs Shuhada action; recommended deadline Sep 12
2. **12 TBA placeholders** — Jasila +5 reps, Azirul +1 org/+7 reps outstanding
3. **Data quality** — KPJ spelling dedupe, email-as-name entries (Mh Nazri rows), MCMC Software-Engineer seniority mismatch, RHB "Sr Dev" junior for exec programme
4. **Two-funnel attribution** — ~half the invitation orgs map to GTM database tiers, half are relationship accounts; MQL attribution rule (session Block B) must cover both
5. **Sep 15 session linkage** — invitation list = supply source for the 15 pre-booked meetings; listed as agenda Block C item 13

**Awaiting human validation (Step 11).** Records committed per intake precedent; this manifest + DRAFT-20260908-001 together constitute the approval packet.
