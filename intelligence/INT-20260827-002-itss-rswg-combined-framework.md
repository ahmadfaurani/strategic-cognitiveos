---
id: INT-20260827-002
record_type: intelligence
title: "ITSS × RSWG Combined Framework — VoronCitadel Must Position Against Two-Layer Compliance (Existing Floor + New Ceiling)"
created_at: 2026-08-27T03:16:00+00:00
updated_at: 2026-08-27T03:16:00+00:00
owner: faurani-jaafar
status: active
priority: critical
sensitivity: confidential
lifecycle_state: canonical
confidence: high
tags:
- domain/cybersecurity
- domain/compliance
- domain/cybersecurity-productisation
- domain/commercial-development
- domain/supply-chain-security
- domain/security-architecture
- domain/incident-response
- sector/financial
source:
  type: external
  reference: "DOC-20260827-002 — Bursa Malaysia POs ITSS (Directive 5.05-001, L1). DOC-20260827-001 — RSWG Recommendation Paper (L1). Both official Bursa Malaysia documents."
summary: "The ITSS (Directive 5.05-001) is the EXISTING binding standard — 12 domains, 200+ requirements, all 30 POs must already comply. The RSWG paper is the NEW enhancement layer with 9 additional/upgraded control domains. Together they form a two-layer compliance framework: ITSS = floor, RSWG = ceiling. VoronCitadel must position against BOTH layers. Key finding: ITSS §10 Supplier Management is the existing TPRM precursor — VoronCitadel's TPRM module addresses this domain directly, meaning VoronCitadel helps brokers meet EXISTING compliance, not just new RSWG requirements. This doubles the value proposition: VoronCitadel addresses both current obligations (ITSS) and future requirements (RSWG). The ITSS is also likely the source of the '61 Bursa Cybersecurity Controls' already in VoronCitadel's production database (INT-20260821-002), providing a direct lineage from existing platform capability to regulatory compliance."
strategic_significance: "Transforms VoronCitadel's value proposition from 'prepare for upcoming RSWG compliance' to 'address current ITSS compliance AND prepare for RSWG enhancement.' The ITSS is already binding — brokers already need TPRM (§10), incident management (§11), and BCM (§12). VoronCitadel doesn't just address future requirements; it addresses current ones. This eliminates the 'we'll wait for RSWG to be formalized' objection."
mission_alignment:
- productisation
- commercial-growth
- national-cybersecurity
related_initiatives:
- INIT-20260824-001
- INIT-20260804-001
- INIT-20260811-001
related_stakeholders:
- STK-20260813-008
intelligence_type: strategic-regulatory
evidence:
- "DOC-20260827-002 — ITSS Directive 5.05-001, 42 pages, L1 official (Bursa Malaysia Securities Berhad)"
- "DOC-20260827-001 — RSWG Recommendation Paper, 28 pages, L1 official"
- "RSWG §3: 'Where the standards outlined in this paper are also requirements prescribed under the ITSS, Brokers are expected to comply with the said standards in accordance with the applicable rules set out under the ITSS.'"
- "RSWG §3: 'forthcoming updates to the ITSS framework to reflect the standards'"
- "ITSS §10 Supplier Management — existing TPRM requirements: outsourcing risk policy, supplier types, access controls, recovery arrangements, background verification, supplier agreements, audit rights, service delivery monitoring"
- "ITSS §11 Incident Management — existing incident response requirements: monitoring, detection, logging, investigation, resolution, closure, monthly senior management reporting"
- "ITSS §12 BCM — existing business continuity requirements: BCP, BIA, DRP, annual testing"
- "INT-20260821-002 — referenced '61 Bursa Cybersecurity Controls in production database' — likely derived from ITSS"
implications:
- "VoronCitadel's value proposition is strengthened: it addresses BOTH current ITSS compliance AND future RSWG requirements — not just upcoming changes"
- "The 'we'll wait for RSWG formalization' sales objection is eliminated — ITSS §10 Supplier Management is already binding"
- "The '61 Bursa Cybersecurity Controls' in VoronCitadel's database (INT-20260821-002) likely originate from or map to the ITSS 12 domains — this lineage should be verified and documented"
- "ITSS §10 + RSWG §2.6 together form a comprehensive TPRM requirement set — VoronCitadel can position as addressing the full TPRM lifecycle, from current baseline to enhanced oversight"
- "The DRS standards (Appendix 2) add infrastructure resilience requirements that may intersect with VoronCitadel infrastructure monitoring"
- "RSWG will be incorporated into ITSS framework updates — positioning now means VoronCitadel is ready for the updated ITSS when it arrives"
- "Competitive differentiation: vendors who only address RSWG miss the existing ITSS compliance gap; vendors who only address ITSS miss the RSWG enhancement layer"
open_questions:
- "What is the exact relationship between the '61 Bursa Cybersecurity Controls' in VoronCitadel's database and the ITSS 12 domains? Is it a direct mapping?"
- "Has the ITSS already been updated since the RSWG paper was issued? What is the timeline for ITSS updates incorporating RSWG?"
- "Are POs currently audited against ITSS? What does the audit process look like?"
- "How do the 200+ ITSS requirements map to VoronCitadel's existing feature set vs. the 61 controls already in the database?"
recommended_actions:
- "ACT-20260827-003: Extend capability mapping (ACT-20260827-001) to include ITSS 12 domains — create unified ITSS × RSWG × VoronCitadel matrix"
- "Verify the lineage of the 61 Bursa Cybersecurity Controls in VoronCitadel's database against ITSS 12 domains"
- "Update VoronCitadel POC document to reference both ITSS (existing compliance) and RSWG (enhanced compliance)"
- "Sales positioning: 'Address current ITSS compliance AND prepare for RSWG enhancement' — dual value proposition"
- "Assess whether VoronCitadel's existing 61-control database can be extended to cover the full 200+ ITSS requirements"
related_records:
- DOC-20260827-001
- DOC-20260827-002
- INT-20260827-001
- INT-20260821-002
- OPP-20260827-001
- INIT-20260824-001
---

# Summary

[T2 SOURCE-BACKED, Score 9/10 — Two L1 source documents (ITSS + RSWG), both Bura Malaysia official. High authority/traceability/recency/consistency/completeness]

The ITSS (Directive 5.05-001) is the existing binding regulatory standard for all Bursa Malaysia POs. The RSWG Recommendation Paper is the new enhancement layer. Together they create a two-layer compliance framework that VoronCitadel must position against.

## Strategic Significance

This finding transforms VoronCitadel's value proposition. [T3 ASSESSMENT] Previously, the RSWG paper alone positioned VoronCitadel as preparing brokers for upcoming compliance. With the ITSS, VoronCitadel now also addresses **current, existing compliance obligations** — particularly §10 Supplier Management (TPRM), §11 Incident Management, and §12 Business Continuity Management.

**The dual value proposition:**
- **Current:** "VoronCitadel helps you meet existing ITSS §10 Supplier Management requirements today"
- **Future:** "VoronCitadel prepares you for RSWG enhancement layer and forthcoming ITSS updates"

This eliminates the strongest sales objection: "We'll wait for RSWG to be formalized before investing." Brokers already need TPRM under ITSS — the question is not *whether* to invest, but *which platform* to use.

## Evidence

Both sources are L1 (Official/System-of-Record) from Bursa Malaysia:

**ITSS (DOC-20260827-002):**
- §10 Supplier Management: outsourcing risk policy (data centre, network, DR, application hosting, cloud), supplier types, access controls, recovery arrangements, background verification, supplier agreements, audit rights, service delivery monitoring
- §11 Incident Management: monitoring, detection, logging, investigation, resolution, closure, monthly senior management reporting
- §12 BCM: BCP, BIA, DRP, annual testing
- Appendix 2 DRS: 10km separation, separate power/telecom, CDS terminal, trading terminals, annual DR testing

**RSWG (DOC-20260827-001):**
- §3: "Where the standards outlined in this paper are also requirements prescribed under the ITSS, Brokers are expected to comply with the said standards in accordance with the applicable rules set out under the ITSS."
- §3: "forthcoming updates to the ITSS framework to reflect the standards"
- §2.6: Enhanced TSP Oversight (builds on ITSS §10)
- §2.7: Enhanced Incident Management (builds on ITSS §11)
- §2.5: Enhanced Recovery Planning (builds on ITSS §12)

**Existing VoronCitadel capability (INT-20260821-002):**
- "61 Bursa Cybersecurity Controls in production database" — likely derived from or mapped to ITSS 12 domains

## Implications

**VoronCitadel positioning [T3 ASSESSMENT]:**
1. **Dual-layer compliance:** VoronCitadel addresses both ITSS (current) and RSWG (future) — not just one layer
2. **Current compliance gap:** Many brokers may not be fully compliant with ITSS §10 Supplier Management — VoronCitadel fills this gap today
3. **Competitive differentiation:** Vendors addressing only RSWG miss existing ITSS gaps; vendors addressing only ITSS miss RSWG enhancement
4. **61-control lineage:** The 61 Bura Cybersecurity Controls in VoronCitadel's database likely originate from ITSS — this lineage should be verified and documented as a compliance credential
5. **ITSS update readiness:** RSWG will be incorporated into ITSS updates — VoronCitadel positioned now is ready for the updated ITSS when it arrives

**Cross-product synergies [T3 ASSESSMENT]:**
- ITSS §10 + RSWG §2.6 = comprehensive TPRM lifecycle (current + enhanced)
- ITSS §11 + RSWG §2.7 = comprehensive incident management (current + enhanced)
- ITSS §12 + RSWG §2.5 = comprehensive BCM/DR (current + enhanced)
- ITSS §8 Network Security + RSWG §2.2 = comprehensive threat detection
- ITSS DRS Appendix 2 = infrastructure resilience (VoronCitadel monitoring)

**Sales objection handling [T3 ASSESSMENT]:**
| Objection | Response with ITSS + RSWG |
|-----------|---------------------------|
| "We'll wait for RSWG to be formalized" | "ITSS §10 Supplier Management is already binding — you need TPRM today" |
| "RSWG is just a recommendation" | "RSWG will be incorporated into ITSS updates — early adoption ensures readiness" |
| "We already have ITSS compliance" | "RSWG enhancement layer adds 24/7 SOC, SIEM/UEBA, compromise assessments, AASE — do you have these?" |
| "We use an existing GRC platform" | "Does it address both ITSS current requirements AND RSWG enhancement layer?" |

## Open Questions

1. **61-control lineage:** What is the exact relationship between the 61 Bursa Cybersecurity Controls in VoronCitadel's database and the ITSS 12 domains?
2. **ITSS update timeline:** When will ITSS be updated to incorporate RSWG? What is Bursa's publication process?
3. **Audit process:** How are POs currently audited against ITSS? Self-attestation, third-party audit, or Bursa-led?
4. **Compliance gap data:** What percentage of POs are currently non-compliant with ITSS §10 Supplier Management?
5. **ITSS control count:** Are there exactly 61 top-level controls in ITSS, or is the 61 figure from a different grouping?

## Recommended Actions

1. **ACT-20260827-003:** Extend capability mapping to include ITSS 12 domains — unified ITSS × RSWG × VoronCitadel matrix
2. Verify 61-control lineage against ITSS 12 domains
3. Update POC document to reference both ITSS (existing) and RSWG (enhanced)
4. Sales positioning: dual value proposition (current + future compliance)
5. Assess extending VoronCitadel's 61-control database to full 200+ ITSS requirements

## Related Records

- **DOC-20260827-001** — RSWG Recommendation Paper
- **DOC-20260827-002** — ITSS Directive 5.05-001
- **INT-20260827-001** — RSWG strategic intelligence
- **INT-20260821-002** — VoronCitadel POC Bursa Success Trigger Assessment (references 61 controls)
- **OPP-20260827-001** — RSWG compliance mandate commercial opportunity
- **INIT-20260824-001** — Bursa Malaysia VoronCitadel POC
