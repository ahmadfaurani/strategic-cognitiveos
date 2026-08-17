---
id: INIT-20260813-005
record_type: initiative
title: Job Description — POC Engineer
created_at: 2026-08-13 00:00:00+00:00
owner: faurani-jaafar
status: active
portfolio_tier: incubation
readiness_level: concept
summary: Reference document — see body for details.
sensitivity: internal
lifecycle_state: canonical
tags:
- type/reference-document
updated_at: null
priority: null
confidence: null
source:
  type: null
  reference: null
strategic_significance: null
mission_alignment: []
related_records: []
---

# Job Description — POC Engineer

**Role Title:** POC Engineer — VoronDRQ
**Department:** Cyber Security Practice / Product Engineering
**Reports To:** Ahmad Fuad (VoronDRQ Product Owner) with matrix reporting to Faurani Jaafar (Practice Director)
**Location:** Level 30, Menara TM, KL (hybrid)
**Employment Type:** Full-time
**Initiative:** INIT-20260808-002 / INIT-20260804-001

---

## Purpose

Own the technical delivery of VoronDRQ Proof-of-Concept engagements — from environment provisioning through client evaluation to commercial conversion handoff. This role exists to eliminate Fuad as the single point of failure across product, demo, and POC delivery. Without this role, concurrent POCs are not possible and the programme's commercial conversion rate is capped by engineering capacity.

## Key Responsibilities

### POC Environment Management
- Provision isolated, secure VoronDRQ instances for each POC client — within 5 business days of POC agreement
- Load client-specific regulatory frameworks (RMiT, SC GTRM, ISO 27001, PDPA, BNM TBS) and configure control structures, evidence templates, and risk register mappings relevant to the institution
- Manage POC environment lifecycle: provisioning, access control, monitoring, and decommissioning after POC conclusion
- Maintain a library of pre-configured POC templates by institution type (bank, insurer, takaful, investment bank) to reduce provisioning time

### POC Delivery
- Serve as day-to-day technical liaison during POC — client's primary technical contact for the evaluation period
- Conduct POC kickoff session: confirm scope, success criteria, timeline, client team, and integration points
- Provide technical guidance to client team during evaluation — how to use VoronDRQ for their specific use cases, how to map their controls, how to interpret findings
- Weekly POC status report: progress against success criteria, client engagement level, blockers, technical issues, next steps
- Escalate product issues or feature requests to Fuad (Product Owner) with full context and reproduction steps

### Integration Scoping
- Work with Hadri (Solutions Architect) to scope integration requirements per POC: API connectors, SSO setup, data import from existing GRC/SIEM tools, export formats
- Document integration architecture and requirements for each POC — this becomes the basis for the commercial implementation proposal if POC converts

### Demo Environment Maintenance
- Maintain the dedicated demo environment — ensure it is stable, up-to-date, and available for client demonstrations
- Keep Malaysian regulatory data current (RMiT updates, SC GTRM revisions, new BNM guidelines)
- Prepare institution-specific demo configurations when requested by Account Owners (2–3 days per institution)

### POC-to-Commercial Handoff
- Prepare the technical implementation proposal for accounts that convert from POC to commercial — environment sizing, integration scope, deployment timeline, ongoing support requirements
- Hand off to Hadri's delivery team for commercial implementation
- Document lessons learned from each POC — what worked, what didn't, what to improve for the next one

## Requirements

### Essential
- 2–4 years experience in technical delivery, solutions engineering, or implementation consulting
- Hands-on experience with GRC, risk management, or compliance platforms — either as a user, implementer, or integrator
- Strong understanding of Malaysian regulatory frameworks: RMiT (Risk Management in Technology), SC GTRM (Guidelines on Technology Risk Management), PDPA, BNM guidelines
- Cloud infrastructure experience — provisioning and managing environments on AWS, Azure, or equivalent
- API integration experience — REST APIs, SSO (SAML/OIDC), data import/export, webhooks
- Ability to explain technical concepts to non-technical stakeholders (CISO, Head of GRC, CRO) without losing accuracy
- Strong documentation discipline — every POC has a defined scope, success criteria, status, and handoff document

### Desirable
- Experience with VoronDRQ or similar GRC platforms
- CISSP, CISA, CRISC, or equivalent certification
- Experience in financial services technology or regulatory technology (RegTech)
- Python or scripting experience for automation of provisioning and data loading
- Experience with SIEM integration (Splunk, QRadar, Elastic) and GRC tool integration

## Success Metrics (First 90 Days)

- POC environment provisioning capability established — can stand up a new POC instance within 5 business days
- Demo environment stable and available 99% of business hours
- Pre-configured POC templates created for at least 3 institution types (bank, insurer, takaful)
- First POC delivered end-to-end with documented success criteria and status reporting
- POC-to-commercial handoff template created and used
- Fuad's POC delivery load reduced by at least 50% — Fuad focuses on product, not POC operations

## Working Relationships

| Internal | External |
|----------|---------|
| Ahmad Fuad (Product Owner — line manager, product escalation) | POC client technical teams |
| Hadri (Solutions Architect — integration scoping, commercial handoff) | POC client stakeholders (CISO, GRC, IT) |
| Account Owners (Sales — POC relationship coordination) | |
| Faurani Jaafar (Practice Director — strategic oversight) | |
| Delivery Owner (programme coordination, status reporting) | |

---

*This role is the bridge between product promise and commercial reality. Every POC is a proof — not just of the technology, but of Aras Integrasi's ability to deliver. You are the person who makes that proof credible.*
