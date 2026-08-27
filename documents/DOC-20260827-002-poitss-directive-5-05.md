---
id: DOC-20260827-002
record_type: document
title: "Bursa Malaysia POs IT Security Standards & Disaster Recovery Site Standards (Directive 5.05-001)"
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
- domain/risk-management
- domain/security-architecture
- domain/security-operations
- domain/supply-chain-security
- domain/incident-response
- domain/data-protection
- domain/network-security
- sector/financial
source:
  type: external
  reference: "Bursa Malaysia Securities Berhad — Directive No. 5.05-001, Rule 5.05. Introduced 2 May 2013, amended 3 January 2017 vide R/R 7 of 2016. Received via DAF (Telegram, Aug 27 2026)."
summary: "Bursa Malaysia's existing binding IT Security Standards for Participating Organisations (POs), issued under Rule 5.05. This is the CURRENT regulatory standard that all POs must comply with — the RSWG Recommendation Paper (DOC-20260827-001) is an enhancement layer on top of this framework. 12 security domains across 39 pages (Appendix 1) plus Disaster Recovery Site Standards (Appendix 2, 3 pages). Total 42 pages. Domains: (1) Governance of Technology Risks, (2) Organisation of Information Security, (3) Human Resource Security, (4) Asset Management, (5) Access Control, (6) Physical & Environmental Security, (7) Operations Security, (8) Network & Communication Security, (9) System Acquisition/Development/Maintenance, (10) Supplier Management, (11) Information Security Incident Management, (12) Business Continuity Management. DRS Standards mandate: 10km separation from main site, separate power sub-station, separate telecom exchange, 24/7 accessibility, CDS terminal, trading terminals, annual DR testing. The RSWG paper explicitly states: 'Where the standards outlined in this paper are also requirements prescribed under the ITSS, Brokers are expected to comply with the said standards in accordance with the applicable rules set out under the ITSS.' The RSWG paper also notes it supports 'forthcoming updates to the ITSS framework to reflect the standards' — meaning ITSS will be updated to incorporate RSWG requirements."
strategic_significance: "This is the EXISTING binding regulatory standard — the floor that all 30 POs must already meet. The RSWG paper is the enhanced ceiling. Together, ITSS + RSWG form the complete compliance picture for VoronCitadel positioning. ITSS §10 Supplier Management is the existing TPRM precursor — VoronCitadel's TPRM module directly addresses this domain. ITSS §11 Incident Management maps to VoronCitadel incident response. ITSS §12 BCM maps to VoronCitadel resilience monitoring. The DRS standards (Appendix 2) add infrastructure resilience requirements. 200+ individual requirements across 12 domains — likely the source or superset of the '61 Bursa Cybersecurity Controls' already in VoronCitadel's production database (referenced in INT-20260821-002)."
mission_alignment:
- productisation
- commercial-growth
- national-cybersecurity
related_records:
- DOC-20260827-001
- INT-20260827-001
- INT-20260827-002
- INIT-20260824-001
- OPP-20260827-001
- ORG-20260820-001
- ACT-20260827-001
- ACT-20260827-003
document_type: regulatory-directive
file_path: "media/inbound/openclaw-staged-f3af7da0-a502-4da4-b5da-32d350d2c8f2/POs_ITSS---2a80fadd-a234-46b3-a1ba-3663f0418f2b.pdf"
version: "Amended 3 January 2017 (vide R/R 7 of 2016)"
author: "Bursa Malaysia Securities Berhad"
---

# Document Type

Regulatory directive — binding IT security standards for Participating Organisations under Rule 5.05.

# File Location

`media/inbound/openclaw-staged-f3af7da0-a502-4da4-b5da-32d350d2c8f2/POs_ITSS---2a80fadd-a234-46b3-a1ba-3663f0418f2b.pdf` (42 pages, CONFIDENTIAL)

# Version

- Introduced: 2 May 2013
- Amended: 3 January 2017 (vide R/R 7 of 2016)
- POs Circulars: R/R 9 of 1997, G 240 of 1999

# Author

Bursa Malaysia Securities Berhad

# Summary

## Document Structure

| Part | Content | Pages |
|------|---------|-------|
| Directive | Rule 5.05 — requires POs to have adequate security and emergency arrangements | 1 |
| Appendix 1 | POs IT Security Standards (12 domains) | 2–39 |
| Appendix 2 | Disaster Recovery Site Standards (PODRS) | 40–42 |

## 12 IT Security Domains (Appendix 1)

### §1.0 Governance of Technology Risks
- Board of Directors: establish policies, allocate resources, risk framework, awareness programmes
- Technology Risk Management: robust framework, periodic review, risk identification (DoS, internal sabotage, malware), mitigation measures
- Information Security Policies: Board-approved, communicated to all employees, regular review

### §2.0 Organisation of Information Security
- Internal Organisation: defined roles (Data Owners, System Owners, System Users, System Providers, Procedure Owners)
- Security Administration: access control administration, access rights review, security violation monitoring
- Segregation of Duties: application development, technical support, computer operations, QA, internal audit, security administration, user departments

### §3.0 Human Resource Security
- Pre-Employment: background verification, probationary status for IT functions
- Terms & Conditions: confidentiality, reporting weaknesses, IP rights, disciplinary procedures
- During Employment: security briefing, documented roles, training, disciplinary process
- Termination: prompt notification, access revocation

### §4.0 Asset Management
- Inventory: accurate, up-to-date, ownership assigned
- Information Classification: Restricted / Confidential / Public
- Classification policy and labelling procedures

### §5.0 Access Control
- Logical Access Policy: business requirements, contractual obligations, SoD enforcement
- User Access Administration: written authorisation, remote access controls, revocation policy
- User Authentication: unique user IDs, password management (case-sensitive, expiry, history, no reuse), cryptography for public network access
- Privileged IDs: restricted, controlled, separate from normal IDs
- Access Review: annual minimum, including unauthorised attempts, privileged activity, third-party access
- Secure Log-on: no system identifiers before login, validation on completion, previous login display, failed attempt details

### §6.0 Physical & Environmental Security
- Secure Areas: identified, documented, security perimeters, visitor controls, regular review
- Equipment: environmental protection, fire detection/suppression, power backup
- Storage Media: restricted access, movement logging, secure disposal
- Emergency Procedures: documented, annual testing, personnel training

### §7.0 Operations Security
- Documented Procedures: startup/shutdown, backups, media handling, maintenance, audit-trail
- Change Management: documented, assessed, approved, tested, logged
- Capacity Management: monitored, annual review, mission-critical plans
- Logical System Segregation: Development / Test / Production environments
- Information Backup: uniquely identified, encryption, retention periods, third-party storage agreements
- Security of Computer Reports: restricted access, secure disposal
- Logging & Monitoring: event logs (User IDs, system activities, access attempts, configuration changes, privilege use, file access, network addresses), 1-year minimum retention, audited, administrator activity protected
- Malware Protection: formal policy, detection software, regular reviews, BCP integration

### §8.0 Network & Communication Security
- Network Controls: management responsibilities, confidentiality/integrity on public networks, availability, logging/monitoring, dial-back controls, configuration authorisation, network user lists
- Network Segregation: internal/external/wireless domains, value-based segregation
- Network Security: firewalls, cryptographic methods for wireless, network diagrams, vulnerability assessment, penetration testing, anti-virus on all critical servers/workstations

### §9.0 System Acquisition, Development & Maintenance
- Security Requirements: access provisioning, asset protection, business process requirements, formal testing
- Source Code Access Control: restricted, centralised storage, audit logs
- Secure Development Policy: development environment security, secure coding guidelines, security checkpoints
- System Change Control: formal procedures, written instructions, approval, version control, audit trail
- Restrictions on Software Package Changes: original retained, designated copy, update management
- System Security Testing: development phase, independent acceptance testing
- System Acceptance Testing: acceptance criteria, security requirement testing
- Test Data Protection: authorisation for operational data use, data masking, erasure after testing, audit trail

### §10.0 Supplier Management — VoronCitadel TPRM Alignment
- Information Security in Supplier Management: outsourcing risk policy (data centre, network, DR, application hosting, cloud), supplier types, access controls, recovery/contingency arrangements
- Engagement of Suppliers: background verification, compliance with ITSS, confidentiality statements
- Supplier Agreements: legal/regulatory obligations, controls, incident management, audit rights, escrow, evidence of testing
- Management of Supplier Service Delivery: performance monitoring, service reports, service continuity plans

### §11.0 Information Security Incident Management
- Responsibilities & Procedures: monitoring, detection, analysis, reporting, logging, response planning, escalation, recovery
- Reporting Events: ineffective controls, breaches, human errors, non-compliance, physical breaches, malfunctions, access violations, misuse
- Incident Logging: centralised, restricted access, structured details (date, description, identification, reporter, extent, priority, actions)
- Investigation & Diagnosis: prompt assignment, impact analysis, classification, escalation
- Resolution & Recovery: timely resolution, root cause analysis, documented actions
- Closure & Evaluation: formal sign-off, regular management review, monthly senior management reporting

### §12.0 Business Continuity Management
- BCP: formalised procedures, business impact analysis, defined responsibilities, third-party services, personnel training, off-site copies, annual review
- Testing: comprehensive testing, documented results, training updates

## Disaster Recovery Site Standards (Appendix 2)

| Requirement | Standard |
|-------------|----------|
| Location | ≥10km from main premise |
| Power | Separate power sub-station |
| Telecom | Separate telecommunication exchange |
| Accessibility | 24 hours |
| Backup system | Clearing & settlement operations |
| Data backup | Latest system/application programs at DRS site |
| CDS terminal | ≥1 maintained at DRS site |
| Trading terminals | Sufficient for disaster trading |
| Trading facilities | Offline except during disaster |
| Network | Fault-tolerant, redundant configuration |
| DR Plan | BIA, roles, decision framework, recovery procedures |
| DR Testing | Annual minimum |
| DR Plan Review | Annual minimum, integrated with BCP |

## Relationship to RSWG Recommendation Paper (DOC-20260827-001)

The RSWG paper explicitly references the ITSS:
- "Where the standards outlined in this paper are also requirements prescribed under the ITSS, Brokers are expected to comply with the said standards in accordance with the applicable rules set out under the ITSS."
- "Early adoption is strongly encouraged to ensure readiness and alignment with forthcoming updates to the ITSS framework to reflect the standards."

This means:
1. ITSS = current binding floor (existing compliance obligation)
2. RSWG = recommended enhancement layer (early adoption encouraged)
3. ITSS will be updated to incorporate RSWG standards (forthcoming)
4. Where overlapping, ITSS rules apply; where RSWG is more stringent, RSWG applies

# Related Records

- **DOC-20260827-001** — RSWG Recommendation Paper (enhancement layer on top of ITSS)
- **INT-20260827-001** — RSWG strategic intelligence
- **INT-20260827-002** — ITSS × RSWG combined regulatory framework intelligence
- **INIT-20260824-001** — Bursa Malaysia VoronCitadel POC
- **OPP-20260827-001** — RSWG compliance mandate commercial opportunity
- **ORG-20260820-001** — Bursa Malaysia
- **ACT-20260827-001** — RSWG capability mapping (should be extended to include ITSS)
- **ACT-20260827-003** — ITSS × RSWG unified capability mapping
