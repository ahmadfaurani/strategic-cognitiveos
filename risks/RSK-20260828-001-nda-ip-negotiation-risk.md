---
id: RSK-20260828-001
record_type: risk
title: "NDA IP Terms Negotiation Risk — 4 Critical Provisions May Require Reconciliation"
created_at: 2026-08-28T08:58:00+00:00
updated_at: 2026-08-28T08:58:00+00:00
owner: faurani-jaafar
status: identified
priority: high
sensitivity: confidential
lifecycle_state: canonical
confidence: high
tags:
  - domain/csm-partnership
  - domain/legal
  - domain/legal
  - domain/risk-management
  - domain/pilot-design
  - workstream/cybersec-products
source:
  type: email
  reference: "CONV-20260828-001 — DAF → Azrul, Aug 28, 2026"
summary: "The NDA Framework contains 4 commercially sensitive IP provisions that may require negotiation or counter-proposals from CSM: (1) Foreground IP ownership (Bursa), (2) Background IP licensing (Aras → CSM perpetual/irrevocable/royalty-free), (3) Bursa sublicensing rights (CSM → Bursa), (4) Non-reuse restrictions (Aras). CSM may seek broader usage rights, different licensing terms, or modifications to non-reuse scope. Extended negotiation could delay POC technical discovery and compress the competitive window (6-8 weeks per INT-20260827-003)."
strategic_significance: "NDA is prerequisite for exchanging restricted Bursa information. If IP terms negotiation extends beyond 1-2 weeks, it creates a bottleneck that compresses the POC timeline and risks missing the CyberDSA reference case window (Oct 5-7)."
mission_alignment:
  - csm-partnership
  - commercial-strategy
  - risk-management
related_records:
  - CONV-20260828-001
  - DEC-20260828-001
  - ACT-20260828-001
  - INIT-20260824-001
  - INT-20260827-003
  - RSK-20260827-001
# === RISK FIELDS [Tactical] ===
risk_type: legal-negotiation
risk_category: governance
related_initiative: INIT-20260824-001
probability: medium
likelihood: medium
impact: high
priority: high
mitigation: "DAF has pre-emptively framed 4 provisions for targeted review rather than opening entire document for debate. Working-level alignment before legal review reduces legal iteration cycles."
escalation_trigger: "No response from Azrul within 7 days (Sep 4)"
---

# Risk

The NDA Framework's 4 critical IP provisions may require negotiation or counter-proposals from CSM, potentially delaying the POC technical discovery phase.

## 4 Critical Provisions at Risk of Negotiation

1. **Foreground IP ownership (Bursa)** — CSM may question whether all Bursa-specific outputs should be Bursa property or if some shared ownership is appropriate
2. **Background IP licensing (Aras → CSM)** — CSM may seek broader usage rights beyond the POC scope, or challenge the perpetual/irrevocable/royalty-free structure
3. **Bursa sublicensing rights (CSM → Bursa)** — Scope of sublicensing may need definition (usage vs modification vs redistribution)
4. **Non-reuse provisions (Aras)** — Aras may resist overly broad non-reuse restrictions if they limit legitimate product development

## Likelihood

Medium — CSM has been collaborative but IP terms are commercially sensitive and this is the first formal legal instrument

## Impact

High — NDA is prerequisite for restricted Bursa information exchange. Delay compresses POC timeline and competitive window (6-8 weeks per INT-20260827-003).

## Mitigation

- DAF has pre-emptively flagged 4 specific provisions for review rather than opening the entire document
- Working-level alignment before legal review reduces legal iteration cycles
- DAF's framing positions NDA as enabling framework, not restrictive
- Principles are structured to be mutually beneficial (Aras keeps Background IP, Bursa gets Foreground IP, CSM gets sublicensing)

## Escalation Trigger

No response from Azrul within 7 days (Sep 4, 2026) — DAF to follow up directly.

## Related Records

- **CONV-20260828-001** — Source email
- **DEC-20260828-001** — 11 NDA principles
- **ACT-20260828-001** — Azrul's review action
- **INIT-20260824-001** — Bursa POC initiative
- **INT-20260827-003** — Cognitive Loop (competitive window 6-8 weeks)
- **RSK-20260827-001** — RSWG compliance window competitive risk
