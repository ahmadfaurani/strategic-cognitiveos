# CVS Adapter Guide — Workstream Deployment

**Classification:** TLP:AMBER  
**Created:** 2026-08-04

---

## Purpose

This guide defines how each workspace adapts the master CVS framework to its domain. Each workspace maintains a `03-VERIFICATION/` directory with three files:

1. `CVS-EVIDENCE-REGISTER.csv` — Local claims register (CSV, 20-field schema per master)
2. `CVS-SOURCE-REGISTER.md` — Local source hierarchy (domain-specific sources added to master)
3. `CVS-ADAPTER.md` — Domain-specific rules, overrides, and special cases

---

## Standard Deployment Checklist

For each workspace, the following must be completed:

- [ ] Create `03-VERIFICATION/` directory
- [ ] Create `CVS-EVIDENCE-REGISTER.csv` with header row only (or seed with existing claims)
- [ ] Create `CVS-SOURCE-REGISTER.md` with domain-specific sources
- [ ] Create `CVS-ADAPTER.md` with domain-specific rules
- [ ] Update any existing verification documents to reference master framework
- [ ] Ensure cronjob prompts include CVS output block (see master framework §10)

---

## Domain-Specific Adapter Rules

### Election Intelligence (NS, MLK)

**Special Rules:**
- SPR/EC official data → automatic T1, minimum score 8 (L1 source override)
- Party Sec-Gen/President statements → T1 for fact statement was made, T2 for content claims
- Verified politician social media → T2 for statements made
- Unverified social media → T6 (excluded), logged for trend tracking only
- WhatsApp forwards → T6 (excluded), logged for trend tracking only

**Claim ID Format:** `CVS-NS-NNN`, `CVS-MLK-NNN`

### Strategic CognitiveOS

**Special Rules:**
- PIR-sourced claims → validated against PIR evidence chain
- AI Council outputs (Sol/GLM/Claude/Gemini) → T3 (assessment) by default
- AI Council outputs with source backing → T2
- Strategic records (STK/INIT/OPP/INT) → L2 source, T2 unless independently verified
- PIR status assessments → T3 (analytical interpretation)

**Claim ID Format:** `CVS-COG-NNN`

### HOI Intelligence Operations

**Special Rules:**
- Multi-domain: covers hoi-intelligence-ops, cyber-intel, gov-intel, pdrm-io
- Cross-referenced claims across sub-workstreams get compound IDs
- Human intelligence (HUMINT) → L3 with attribution and timestamp
- Open source intelligence (OSINT) → L4-L5 depending on traceability

**Claim ID Format:** `CVS-HOI-NNN`

### PDRM Info Ops

**Special Rules:**
- Official PDRM statements → L1, T1 for fact of statement
- Policing publications → L2, T2 unless independently verified
- PDRM official social media → L4, T2 for announcements
- Unverified policing claims → T6

**Claim ID Format:** `CVS-PDRM-NNN`

### Weststar-RTI

**Special Rules:**
- RTI response documents → L1 (official government response)
- RTI application correspondence → L2
- Media coverage of RTI matters → L4

**Claim ID Format:** `CVS-RTI-NNN`

### Cybersecurity Practice

**Special Rules:**
- Vendor threat reports → L4, requires cross-check
- Government cyber advisories (CERT, NACSA) → L1
- Internal penetration test results → L2
- AI-generated vulnerability assessments → T3 (assessment), Rule 6 applies

**Claim ID Format:** `CVS-CYB-NNN`

### CBO-01 Commercial Operations

**Special Rules:**
- VoronDRQ canonical database → L2, T2 for prospect data
- Vendor confirmations → L3 with timestamp
- Market projections → T4 (assumption)
- Sales pipeline data → L2, T2 unless contractually confirmed

**Claim ID Format:** `CVS-CBO-NNN`

### AZW

**Special Rules:**
- To be defined based on workstream activation

**Claim ID Format:** `CVS-AZW-NNN`

### TH-RCI (Tabung Haji RCI)

**Special Rules:**
- Official TH statements → L1
- Audit findings → L1 (if from official audit body)
- Media coverage → L4
- Historical records → L2 if from validated archive

**Claim ID Format:** `CVS-TH-NNN`

---

## CSV Register Schema (All Workspaces)

Identical 20-field schema across all workstreams:

```
claim_id,workstream,claim,source_name,source_type,source_url,source_date,evidence_type,tier,validation_status,confidence_score,authority,traceability,recency,consistency,completeness,issue_gap,owner,action_required,last_reviewed
```

See master framework §6 for field definitions.

---

## Upgrade Procedure (NS — 3-Tier to 6-Tier)

The existing NS workspace uses a 3-tier system (T1/T2/T3). The upgrade procedure:

1. **T1 (Confirmed) → T1 (Verified Fact):** Direct mapping. Add confidence scores to existing T1 claims.
2. **T2 (Medium-Confidence) → T2 (Partially Verified):** Direct mapping. Add confidence scores. Claims that were analytical assessments → reclassify as T3.
3. **T3 (Excluded) → T6 (Rejected):** Direct mapping. Conflicting claims that were logged as T3 → reclassify as T5 if they represent source disagreement.
4. **New tiers populated:** T3 (Analytical Interpretation) and T4 (Assumption/Projection) — extract from existing T2 claims that were actually analysis or projections.
5. **Migration:** Existing `verification-status.md` entries → migrated to `CVS-EVIDENCE-REGISTER.csv`.
6. **Legacy files retained** for audit trail, marked as superseded.

---

**Master Document Location:** `/home/p62operator/.openclaw/workspace/03-VERIFICATION/CVS-ADAPTER-GUIDE.md`  
**Classification:** TLP:AMBER
