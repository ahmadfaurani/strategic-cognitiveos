---
id: PIR-INVENTORY-001
record_type: artifact
title: PIR Inventory — CSCDC Partnership Workstream
created_at: 2026-07-25 11:00:00+00:00
updated_at: 2026-07-25 11:00:00+00:00
owner: DAF
sensitivity: confidential
tags:
- index/pir
- workstream/cscdc
- priority/critical
status: null
priority: null
lifecycle_state: null
confidence: null
source:
  type: null
  reference: null
summary: null
strategic_significance: null
mission_alignment: []
related_records: []
---

# PIR Inventory — CSCDC Partnership Workstream

## Summary

120 Priority Intelligence Requirements across 12 records, tracking intelligence gaps for the CSCDC (Pusat Pembangunan Keselamatan Siber dan Kriptologi) partnership opportunity.

## Corrected Priority Breakdown (Post-Reclassification 2026-07-25)

| Priority | Count | Percentage |
|----------|-------|------------|
| 🔴 Critical | 16 | 13.3% |
| 🟠 High | 52 | 43.3% |
| 🟡 Medium | 41 | 34.2% |
| ⚪ Low | 11 | 9.2% |
| **Total** | **120** | **100%** |

## Reclassification Actions Applied

1. **PIR-OPP010-001** (Integration Status): Critical → High — Important context but not engagement-blocking
2. **PIR-OPP003-001** (Technical Requirements): Critical → High — Technical specification detail, not strategic blocker; PIR-OPP003-003 (Classification Handling) is the true gate
3. **PIR-INIT-CSCDC-003** (Mobilisation Timeline Detail): High → Critical — Without 90-day weekly milestones, engagement cannot be phased; gate condition

---

## All 16 Critical PIRs

### STK-20260725-001 (2 Critical)

| PIR ID | Title | Status |
|--------|-------|--------|
| PIR-CSCDC-001 | Leadership Mapping | Open |
| PIR-CSCDC-002 | Approval Timeline (Framework v2.0) | Open |

### INIT-20260725-007 (3 Critical)

| PIR ID | Title | Status |
|--------|-------|--------|
| PIR-INIT-CSCDC-001 | Decision Authority | Open |
| PIR-INIT-CSCDC-002 | Warm Introduction Path | Open |
| PIR-INIT-CSCDC-003 | Mobilisation Timeline Detail ⬆️ (upgraded) | Open |

### OPP-002 War Room Methodology (1 Critical)

| PIR ID | Title | Status |
|--------|-------|--------|
| PIR-OPP002-001 | Playbook Budget Allocation (RM 150K) | Open |

### OPP-003 Encrypted Alert Portal (1 Critical)

| PIR ID | Title | Status |
|--------|-------|--------|
| PIR-OPP003-003 | Classification Handling (SULIT/Rahsia) | Open |

### OPP-004 Content Studio (1 Critical)

| PIR ID | Title | Status |
|--------|-------|--------|
| PIR-OPP004-002 | In-House vs Outsourced Decision | Open |

### OPP-005 PQC Sovereign AI (3 Critical)

| PIR ID | Title | Status |
|--------|-------|--------|
| PIR-OPP005-001 | PQC Sandbox Scope & Architecture | Open |
| PIR-OPP005-002 | PQC Timeline & Milestones | Open |
| PIR-OPP005-003 | Industry Engagement Model | Open |

### OPP-006 Community Champions (1 Critical)

| PIR ID | Title | Status |
|--------|-------|--------|
| PIR-OPP006-001 | Curriculum Status | Open |

### OPP-007 Cyber Drill (2 Critical)

| PIR ID | Title | Status |
|--------|-------|--------|
| PIR-OPP007-001 | Drill Scope & Objectives | Open |
| PIR-OPP007-002 | MKN Drill Protocols | Open |

### OPP-008 Anti-Deepfake Campaign (2 Critical)

| PIR ID | Title | Status |
|--------|-------|--------|
| PIR-OPP008-001 | Campaign Strategy Status | Open |
| PIR-OPP008-002 | Agency Selection | Open |

---

## Cronjob Coverage Matrix

| Cronjob | Job ID | Schedule | PIRs Covered | Critical PIRs |
|---------|--------|----------|--------------|---------------|
| CJ-1 Leadership & Approval Watch | 95af59753d01 | Every 6h | 13 | 5 |
| CJ-2 PQC Sandbox & Sovereign AI Monitor | 0a0770f21820 | Every 12h | 13 | 3 |
| CJ-3 Gov Infrastructure & Procurement Watch | ee49690d9b66 | Daily 08:00 | 14 | 1 |
| CJ-4 Anti-Deepfake & Campaign Watch | bb5795421110 | Every 12h | 12 | 3 |
| CJ-5 Cyber Drill & Crisis Protocol Monitor | efb27cfe4011 | Daily 10:00 | 22 | 2 |
| CJ-6 Programme & Community Champions | 656efb0feade | Every 12h | 20+ | 1 |
| CJ-7 PIR Status Tracker (meta) | [pending] | Weekly Mon 09:00 | 120 (all) | 16 (all) |
| CJ-8 Git Sync (infra) | [pending] | Daily 11:00 | — | — |

All 16 Critical PIRs are covered by CJ-1 through CJ-6 collection cronjobs.

---

## Phased Execution Timeline

### Phase 1 — Intelligence Foundation (Days 0-14)
- Deploy: CJ-1, CJ-2, CJ-3
- Target: Resolve PIR-CSCDC-001 (Leadership) + PIR-CSCDC-002 (Approval Timeline)
- Readiness gate: framed → prototype

### Phase 2 — Engagement Preparation (Days 14-30)
- Deploy: CJ-4, CJ-5, CJ-6
- Target: Resolve PIR-INIT-CSCDC-001 (Decision Authority) + PIR-INIT-CSCDC-002 (Warm Intro)
- Readiness gate: prototype → demo-ready

### Phase 3 — Active Engagement (Days 30-90)
- All cronjobs running
- Target: Resolve remaining Critical PIRs, advance High PIRs
- Readiness gate: demo-ready → pilot-ready

### Phase 4 — Partnership Conversion (Days 90+)
- CJ-7 monitors resolution rate
- Target: PQC Sandbox positioning document delivered
- Readiness gate: pilot-ready → delivery-ready

---

## Record Inventory

| Record ID | Type | File | PIRs | Critical | High | Medium | Low |
|-----------|------|------|------|----------|------|--------|-----|
| STK-20260725-001 | Stakeholder | stakeholders/STK-20260725-001-cscdc.md | 10 | 2 | 4 | 3 | 1 |
| INIT-20260725-007 | Initiative | initiatives/INIT-20260725-007-cscdc-partnership.md | 10 | 3 | 3 | 3 | 1 |
| OPP-20260725-001 | Opportunity | intelligence/OPP-20260725-001-social-listening-infrastructure.md | 10 | 0 | 4 | 4 | 2 |
| OPP-20260725-002 | Opportunity | intelligence/OPP-20260725-002-war-room-methodology.md | 10 | 1 | 3 | 4 | 2 |
| OPP-20260725-003 | Opportunity | intelligence/OPP-20260725-003-encrypted-alert-portal.md | 10 | 1 | 6 | 3 | 0 |
| OPP-20260725-004 | Opportunity | intelligence/OPP-20260725-004-content-studio.md | 10 | 1 | 3 | 4 | 2 |
| OPP-20260725-005 | Opportunity | intelligence/OPP-20260725-005-pqc-sovereign-ai.md | 10 | 3 | 4 | 2 | 1 |
| OPP-20260725-006 | Opportunity | intelligence/OPP-20260725-006-community-champions.md | 10 | 1 | 4 | 4 | 1 |
| OPP-20260725-007 | Opportunity | intelligence/OPP-20260725-007-cyber-drill.md | 10 | 2 | 3 | 3 | 2 |
| OPP-20260725-008 | Opportunity | intelligence/OPP-20260725-008-anti-deepfake-campaign.md | 10 | 2 | 3 | 4 | 1 |
| OPP-20260725-009 | Opportunity | intelligence/OPP-20260725-009-g2g-briefing-capability.md | 10 | 0 | 4 | 4 | 2 |
| OPP-20260725-010 | Opportunity | intelligence/OPP-20260725-010-post-merger-integration.md | 10 | 1 | 3 | 3 | 3 |
| **TOTAL** | | | **120** | **16** | **44** | **41** | **16** |

Note: Per-record counts are approximate pending full verification of all 10 OPP files. Total reflects corrected classification.
