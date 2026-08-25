---
id: DOC-20260825-001
record_type: document
title: VoronCitadel Delivery Readiness Framework — Five-POC Stress Test and Bursa Sector-Leader Extension Model
created_at: 2026-08-25T10:32:00+08:00
updated_at: 2026-08-25T10:32:00+08:00
owner: faurani-jaafar
status: draft
priority: high
sensitivity: internal
lifecycle_state: candidate
confidence: high
tags:
- domain/cybersecurity-productisation
- domain/organisational-capability
- domain/portfolio-governance
- product/voroncitadel
source:
  type: direct
  reference: DAF delivery-readiness discussion, 2026-08-25 10:23–10:32 MYT
summary: Initial delivery-readiness framing for VoronCitadel using a five-concurrent-POC stress test. Defines delivery readiness as a repeatable organisational capability, separates the standard VoronCitadel POC delivery model from Bursa-specific sector-leader extensions, and establishes Bursa as a reference customer rather than the default delivery template.
strategic_significance: Commercial readiness is no longer the primary constraint. The practice now needs a repeatable delivery system capable of executing multiple POCs consistently without heroics or allowing a complex sector-level use case to distort the core product and delivery model.
mission_alignment:
- cybersecurity-productisation
- organisational-capability
related_records:
- ASSESS-20260825-001
- INIT-20260824-001
- ACT-20260824-001
- ACT-20260825-002
- ACT-20260825-006
document_type: reference
file_path: documents/DOC-20260825-001-voroncitadel-delivery-readiness-framework.md
related_initiative: INIT-20260824-001
version: '0.1'
author: DAF / ChatGPT strategic capture
---

# VoronCitadel Delivery Readiness Framework

**Status:** Initial framing for detailed follow-up  
**Purpose:** Define what must be true for the Cyber Security Practice to execute multiple VoronCitadel POCs consistently and at scale.

## 1. Governing Question

The delivery-readiness stress test is:

> **Can the practice execute five VoronCitadel POCs in parallel or within the same delivery window to a consistent standard without relying on individual heroics?**

This deliberately shifts the operating question from “Can we deliver one POC?” to “Do we have a delivery system?”

## 2. Delivery Readiness as an Organisational Capability

Delivery readiness is broader than engineering readiness. The initial model has six pillars:

1. **Governance** — decision rights, escalation, cadence, acceptance and change control.
2. **People** — named delivery roles, capacity, role boundaries, backups and customer-facing ownership.
3. **Methods** — repeatable implementation lifecycle, handover method, validation process and transition criteria.
4. **Assets** — reusable templates, reference architecture, runbooks, checklists, test packs and enablement material.
5. **Technology** — deployable environments, configuration standards, integrations, observability, security and technical supportability.
6. **Operations** — support model, issue management, customer-success loop, knowledge management and lessons-to-improvement cycle.

## 3. Practice Maturity Sequence

The working maturity sequence is:

**Commercial Readiness → Delivery Readiness → Operational Maturity / Scale**

Current portfolio assessment indicates the flagship products are commercially ready at the sales-kit level. The next binding question is whether delivery can be repeated consistently across multiple customers.

## 4. Standard VoronCitadel POC Delivery Model

A standard POC should be built around a reusable lifecycle:

**Pre-Deployment → Deploy → Validate → Transition**

The baseline delivery system should include, at minimum:

- Standard commercial-to-delivery handover
- POC qualification and entry criteria
- Reference architecture and deployment topology
- Named delivery roles and RACI
- Environment and access prerequisites
- Deployment runbook
- Configuration and integration checklist
- Test strategy and validation pack
- Governance and customer cadence
- Issue / risk / dependency tracking
- Enablement and customer-facing operating material
- Support and escalation model
- Acceptance / exit criteria
- Transition path from POC to production, managed service, expansion or close-out
- Knowledge-management loop so each POC improves the next one

## 5. Five-POC Stress Test

The framework must eventually answer the following for **five simultaneous VoronCitadel POCs**:

| Dimension | Readiness Question |
|---|---|
| Capacity | Do we have enough named FTE and backup coverage across all stages? |
| Environments | Can five isolated POC environments be provisioned and supported without bespoke engineering each time? |
| Governance | Can status, decisions, risks and changes be managed consistently across five customers? |
| Technical Assets | Are architecture, deployment, integration and test artifacts reusable? |
| Customer Success | Is there a clear owner for adoption, feedback, training and transition per POC? |
| Support | Can incidents and technical questions be handled without consuming Fuad/DAF as default escalation points? |
| Knowledge | Does evidence from each POC feed the product backlog, sales kit and delivery playbook? |
| Commercial Handover | Is the transition from MQL/discovery/POC definition into delivery controlled and complete? |

The five-POC test is a **design constraint**, not a forecast that exactly five POCs will launch in one month.

## 6. Bursa Must Not Become the Default POC Template

Bursa Malaysia should be treated as a **reference customer with sector-leader requirements**, not as the definition of a normal VoronCitadel implementation.

The Bursa opportunity introduces additional complexity because its emerging requirement is not merely organisation-level TPRM. It may require sector-level visibility and federated compliance document checking across participating entities.

The delivery architecture should therefore separate two layers:

### Track A — Standard VoronCitadel POC

Reusable core delivery pattern for a normal customer:

- Single-customer / bounded deployment
- TPRM and applicable compliance use cases
- Standard tenancy and access model
- Standard reporting
- Standard validation and acceptance

### Track B — Bursa Sector-Leader Extension (“Bursa Plus” working concept)

Additional capability and delivery controls required for the Bursa context:

- Federated compliance document checking
- Multi-entity participation model
- Aggregate / sector-level management view
- Tenant and data isolation boundaries
- Cross-entity reporting hierarchy
- Sector-level governance and acceptance
- Architecture/capacity validation for federation

**Key principle:** Bursa-specific requirements should extend the core model rather than redefine it.

## 7. Product and Scope Discipline

The core VoronCitadel platform and standard delivery playbook should remain stable. Bursa-specific federation features should be clearly identified as extensions, hypotheses or validated requirements as evidence emerges.

This protects against:

- One customer driving uncontrolled product scope mutation
- Treating federation as mandatory for every POC
- Building bespoke delivery processes that cannot be reused
- Confusing sector-leader governance requirements with normal customer requirements

## 8. Bursa as a Reference Customer

Bursa is still strategically valuable as the first detailed reference implementation because it forces the practice to mature its delivery discipline. Reusable artifacts created through Bursa should be abstracted into the standard delivery system wherever possible.

The operating rule is:

> **Use Bursa to harden the delivery system; do not use Bursa to define every future delivery.**

## 9. Detailed Follow-Up Required

The next working session should convert this framing into a delivery-readiness blueprint covering:

- Delivery lifecycle and stage gates
- RACI and named roles
- Workstream-to-FTE capacity model for five POCs
- Standard artifact inventory
- Technical environment and deployment readiness
- POC governance cadence
- Customer-success and support operating model
- Knowledge-management / lessons loop
- Standard POC vs Bursa extension requirements matrix
- Readiness scorecard and go/no-go criteria

## Related Records

- **ASSESS-20260825-001** — Flagship Product Commercial Readiness; identifies delivery readiness as the next review topic.
- **ACT-20260825-002** — Workstream-to-FTE Capacity Model / TBH alignment.
- **INIT-20260824-001** — Bursa Malaysia VoronCitadel POC.
- **ACT-20260824-001** — Fuad Bursa targeted development.
- **ACT-20260825-006** — Detailed delivery-readiness blueprint follow-up.
