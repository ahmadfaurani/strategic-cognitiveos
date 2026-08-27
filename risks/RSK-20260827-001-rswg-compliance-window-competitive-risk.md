---
id: RSK-20260827-001
record_type: risk
title: "RSWG Compliance Window Creates Competitive Race — First Mover Advantage at Risk if VoronCitadel POC Delays"
created_at: 2026-08-27T02:54:00+00:00
updated_at: 2026-08-27T02:54:00+00:00
owner: faurani-jaafar
status: active
priority: high
sensitivity: confidential
lifecycle_state: candidate
confidence: high
tags:
- domain/risk-management
- domain/commercial-development
- domain/cybersecurity-productisation
- domain/compliance
- risk/timing
- risk/strategic
- sector/financial
source:
  type: external
  reference: "DOC-20260827-001 — RSWG Recommendation Paper (Bursa Malaysia, L1)"
summary: "The RSWG Dec 31, 2026 compliance deadline creates a finite competitive window. Brokers are actively evaluating solutions NOW. If VoronCitadel POC delays beyond Q4 2026, competitors (established security vendors, SI providers, or alternative GRC platforms) will capture the 30-broker pipeline before VoronCitadel has a reference case. The Bursa POC (INIT-20260824-001) is the gating factor — its success or failure determines first mover advantage. Existing RSK-20260824-001 (4-month timeline compression) is amplified by this regulatory deadline."
strategic_significance: "The regulatory deadline that creates the opportunity also creates the risk. Every month of POC delay narrows the competitive window. Competitors with existing GRC/TPRM platforms (ServiceNow, OneTrust, etc.) may position for RSWG compliance without a Bursa-specific reference."
mission_alignment:
- productisation
- commercial-growth
related_records:
- DOC-20260827-001
- INT-20260827-001
- OPP-20260827-001
- INIT-20260824-001
- RSK-20260824-001
- ACT-20260827-001
- ACT-20260827-002
risk_category: timing
probability: medium
impact: high
mitigation_strategy: "1. Accelerate Bursa POC — prioritize RSWG-aligned use cases (TPRM, incident response, vendor oversight). 2. Complete RSWG → VoronCitadel capability mapping (ACT-20260827-001) immediately. 3. Update POC document with explicit RSWG alignment (ACT-20260827-002). 4. Engage CSM channel on competitive intelligence — who else is approaching brokers? 5. Consider parallel pipeline: start engaging Group 2 brokers on RSWG compliance awareness even before POC completes."
mitigation_owner: faurani-jaafar
trigger_conditions: "1. POC timeline slips beyond Q4 2026. 2. Competitor visible at any Bursa broker engagement. 3. Brokers announce vendor selections without VoronCitadel being evaluated. 4. CSM reports competitive activity in the broker ecosystem."
related_initiative: INIT-20260824-001
---

# Risk Description

The RSWG compliance deadline (Dec 31, 2026) creates a finite window. Brokers must select and implement solutions well before the deadline to allow deployment time. If VoronCitadel's Bursa POC is not complete by Q4 2026, the reference case is not established and competitors capture the market.

## Risk Category

Timing + Strategic

## Probability & Impact

- **Probability: Medium** — POC is underway, CSM channel active, but timeline compression risk exists (RSK-20260824-001)
- **Impact: High** — Loss of 30-broker pipeline, first-mover advantage, and Bursa reference account

## Mitigation Strategy

1. **Accelerate POC** — Prioritize RSWG-aligned use cases (§2.6 TPRM, §2.7 Incident Management, §2.1 Access Controls)
2. **Complete capability mapping** (ACT-20260827-001) — Know exactly what VoronCitadel covers natively
3. **Update POC document** (ACT-20260827-002) — Explicit RSWG alignment strengthens the POC business case
4. **Competitive intelligence** — Engage CSM on who else is approaching brokers
5. **Parallel pipeline** — Begin Group 2 broker awareness even before POC completes

## Trigger Conditions

1. POC timeline slips beyond Q4 2026
2. Competitor visible at Bursa broker engagements
3. Brokers announce vendor selections without VoronCitadel evaluation
4. CSM reports competitive activity in broker ecosystem
5. RSWG compliance deadline approaches without VoronCitadel reference case

## Related Records

- **DOC-20260827-001** — RSWG Recommendation Paper
- **INT-20260827-001** — Strategic intelligence assessment
- **OPP-20260827-001** — Commercial opportunity
- **INIT-20260824-001** — Bursa POC
- **RSK-20260824-001** — Existing timeline compression risk (amplified by this)
