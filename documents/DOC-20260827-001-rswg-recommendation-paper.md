---
id: DOC-20260827-001
record_type: document
title: "RSWG Recommendation Paper on Regulatory and Cybersecurity Controls for Brokers (2025)"
created_at: 2026-08-27T02:54:00+00:00
updated_at: 2026-08-27T02:54:00+00:00
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
- domain/security-operations
- domain/supply-chain-security
- domain/security-architecture
- domain/incident-response
- domain/commercial-development
- domain/cybersecurity-productisation
- sector/financial
source:
  type: external
  reference: "Bursa Malaysia BERHAD — Regulatory and Security Controls Working Group (RSWG), 2025. Received via DAF (Telegram, Aug 27 2026). Adobe Scan shared document."
summary: "Bursa Malaysia's official Recommendation Paper from the Regulatory and Security Controls Working Group (RSWG), convened June 20, 2025 in response to the April 24, 2025 cyber incident involving unauthorized access and trades through Participating Organisations' systems. Establishes 9 cybersecurity control domains for all Brokers (POs and TPs) with a risk-based 3-group classification framework. Controls cover: (1) Security Access Controls, (2) Threat Detection & Protection, (3) Patch Management, (4) Infrastructure & Operation Resilience, (5) Recovery Planning, (6) Oversight of Technology Service Providers, (7) Incident Management, (8) Training and Awareness, (9) Dedicated Cybersecurity Role (CISO). Compliance timeline: 3 months for people/process/governance items (Recovery Planning + Incident Management), Dec 31, 2026 for system changes. Aligns with GTRM (Securities Commission) and RMiT (BNM) — more stringent applies where overlapping. 30 brokers classified across 3 groups (11 Group 1, 13 Group 2, 6 Group 3)."
strategic_significance: "Directly material to VoronCitadel POC (INIT-20260824-001) and broader cybersecurity productisation strategy. Creates a regulatory-driven compliance market across 30 Malaysian brokers. VoronCitadel's TPRM-first approach directly addresses §2.6 (Oversight of Technology Service Providers). The CISO mandate (§2.9) creates internal champions for cybersecurity spending. 24/7 SOC, SIEM, XDR, compromise assessment, and AASE requirements exceed internal capability for most brokers → outsourcing/commercial opportunity. Document is L1 (Official/System-of-Record) from Bursa Malaysia."
mission_alignment:
- productisation
- commercial-growth
- national-cybersecurity
related_records:
- INIT-20260824-001
- OPP-20260820-001
- ORG-20260820-001
- INT-20260827-001
- OPP-20260827-001
- RSK-20260827-001
- ACT-20260827-001
- ACT-20260827-002
document_type: regulatory-recommendation
file_path: "media/inbound/openclaw-staged-74b87cbe-c842-4be4-bcfc-7293308d8b94/RSWG_Recommendation_Paper_-_2025_-_final.pdf"
version: "Final 2025"
author: "Bursa Malaysia BERHAD — Regulatory and Security Controls Working Group (RSWG)"
---

# Document Type

Regulatory recommendation paper — official output of Bursa Malaysia's RSWG, convened in response to the April 24, 2025 cyber incident.

# File Location

`media/inbound/openclaw-staged-74b87cbe-c842-4be4-bcfc-7293308d8b94/RSWG_Recommendation_Paper_-_2025_-_final.pdf` (28 pages, CONFIDENTIAL)

# Version

Final 2025 (issued after Focus Group Session on July 23, 2025)

# Author

Bursa Malaysia BERHAD — Regulatory and Security Controls Working Group (RSWG), comprising Bursa Malaysia, broking industry representatives, and cybersecurity experts.

# Summary

## Background

- **April 24, 2025:** Cyber incident — unauthorized access and trades executed through Participating Organisations' systems
- **June 11, 2025:** Industry Dialogue with market participants and ASCM
- **June 20, 2025:** RSWG formation announced
- **July 23, 2025:** Focus Group Session with key stakeholders
- **Result:** This Recommendation Paper

## Broker Categorisation (Appendix A)

| Group | Criteria | Count | Examples |
|-------|----------|-------|---------|
| **Group 1** | Top 10 ranking (annual review); online trading + retail clientele; Bank-backed & Investment Bank | 11 | Affin Hwang, AmInvestment, CIMB Securities, Maybank IB, Public IB, RHB IB, Kenanga, Hong Leong, BIMB, CGS International, MBSB |
| **Group 2** | Retail clientele; or operates online trading platform | 13 | Apex, iFast, Moomoo, Phillip Capital, TA Securities, UOB Kay Hian, Mercury, Malacca, SJ Securities, NewParadigm, M&A, Inter-Pacific, FA Securities |
| **Group 3** | Foreign brokers | 6 | Citigroup, CLSA, JPMorgan, Macquarie, Nomura, UBS |

All standalone Trading Participants (derivatives brokers) → Group 2.

## 9 Control Domains

### §2.1 Security Access Controls
- Least privilege, RBAC, MFA (mandatory for critical systems + customer authentication), periodic access review (annual), SoD, PAM with session recording, JIT access (mandatory for privileged accounts), secure session management
- Service accounts: named owners, vaulted secrets, rotation ≤90 days (API keys ≤30 days)
- Logging: all access attempts, 3-year retention, detection use case library (Account Takeover, data exfiltration, lateral movement, unsigned binaries, cloud control-plane abuse)

### §2.2 Threat Detection & Protection
- NGAV/EDR across all endpoints
- IDPS at network perimeters + critical internal segments
- SIEM with 24/7 behavioural analytics + threat detection; UEBA + automated threat hunting (Group 1 & 2)
- DLP for client data + proprietary trading info
- WAF for public-facing apps, geo-IP blocking
- Compromise Assessments: Group 1 every 12 months, Group 2&3 every 24 months
- Email/web security gateways
- Encryption (data at rest + in transit)
- API security (OAuth 2.0, rate limiting, API inventory, secure error handling)
- Phishing/fake website takedown services
- Vulnerability scanning (weekly external, monthly internal, per release web/API); penetration testing annually for critical systems
- AASE/Red-Teaming: minimum every 3 years, intelligence-led
- Threat intelligence + dark web monitoring
- XDR (where feasible)
- SOC performance: P1 triage ≤15 min, containment ≤2 hours, eradication plan ≤24 hours

### §2.3 Patch Management
- Centralised patch management (automated, real-time inventory, vulnerability scanner integration, audit logging)
- SBOM requirement for Product Owners; CVE monitoring/remediation
- Third-party patching: quarterly vendor attestation
- EOL/EOS tracking + management (board-level reporting)
- Timely deployment: strict timelines, zero-day = immediate, exploited CVE = emergency meeting within 24 hours
- Compensatory controls (virtual patching) when immediate deployment not feasible

### §2.4 Infrastructure & Operation Resilience
- Redundant systems + high availability (no single points of failure, auto-failover drills under load, RTO/RPO verification)
- Network segmentation (tiered/micro-segmentation for critical environments, CIS baseline compliance)
- Regular backups (immutable, encrypted with HSM/KMS-backed keys, air-gapped or immutable storage)
- Climate-risk drills (heat, flood, power) for sites and telecoms
- Monthly KRI pack to board (open critical vulnerabilities, SLA breach, EOL exposure)

### §2.5 Recovery Planning — ⚡ 3-MONTH COMPLIANCE
- BCP + DRP (annual testing, failover scenarios, simulated cyberattacks)
- RTO/RPO defined per critical system, aligned with BIA
- Important Business Services (IBS) identification + impact tolerances
- Annual scenario testing (ransomware, corrupted market data, provider outage, mass Account Takeover)
- Data integrity verification (checksums, hash comparisons)
- Cyber insurance coverage

### §2.6 Oversight of Technology Service Providers
- Cybersecurity risk assessment before engagement + annually thereafter
- Concentration risk evaluation
- Vendor risk-tiering model (low/medium/high)
- Centralised vendor inventory + automated continuous scoring
- Contractual: data protection, incident response, audit rights, Bursa access rights, 3-year log retention, prompt incident updates, secrecy law undertaking, DR/backup arrangements, business continuity on exit
- Cloud: broker control over encryption keys, secure private connections, data location/jurisdiction clarity
- SOC 2 Type 2 audit reports
- Third-party register: service scope, data categories, hosting locations, sub-outsourcing, exit plan, RTO/RPO dependencies
- Critical provider: P1 notification ≤1 hour, full initial report ≤24 hours
- Joint incident response tabletop exercises annually
- Exit strategy per critical provider; exit-execution test every 24-36 months

### §2.7 Incident Management — ⚡ 3-MONTH COMPLIANCE
- Dedicated Incident Response Team (IRT), 24/7 availability
- IRP covering: Detection → Analysis → Containment → Eradication → Recovery → Post-Incident Review
- DFIR process initiated on confirmed incident
- Annual training + tabletop exercises
- Digital forensic capabilities
- **Bursa incident reporting: 15-30 minutes of detection** per BMCert guidelines
- Post-incident review after every significant incident

### §2.8 Training and Awareness
- Regular staff training (phishing, password management, secure data handling, incident reporting, remote work security)
- Role-based: Board/senior management (risk management, governance, strategic oversight); IT/developers (specialised technical)
- Phish-click targets: ≤5% within 12 months, ≤2% thereafter
- Senior management: annual crisis tabletop exercises
- Client/investor awareness: phishing reminders, password management, investor compensation/support policy

### §2.9 Dedicated Cybersecurity Role (CISO)
- CISO or dedicated person with adequate IT knowledge + certification
- Independent from day-to-day technology operations
- Reports to Board on technology risks + cybersecurity matters
- Direct Board access
- Quarterly Board reports (Vulnerability SLAs, logging coverage, ATO rate, TLPT status, vendor concentration)

## Implementation Timeline

| Category | Deadline |
|----------|----------|
| §2.5 Recovery Planning + §2.7 Incident Management (people/process/governance) | 3 months from issuance |
| All other system changes | December 31, 2026 |
| Where overlapping with ITSS | Per ITSS applicable rules |
| Where overlapping with GTRM/RMiT | More stringent requirement applies |

## Regulatory Alignment
- Securities Commission Malaysia — Guidelines on Technology Risk Management (GTRM)
- Bank Negara Malaysia — Risk Management in Technology (RMiT)
- Contact: Secretariat.RSWG@bursamalaysia.com

# Related Records

- **INIT-20260824-001** — Bursa Malaysia VoronCitadel Sectorial POC
- **OPP-20260820-001** — VoronCitadel POC — Bursa Malaysia (CSM-Channel)
- **ORG-20260820-001** — Bursa Malaysia (organization)
- **INT-20260827-001** — Intelligence assessment of RSWG → VoronCitadel strategic impact
- **OPP-20260827-001** — RSWG compliance mandate commercial opportunity
- **RSK-20260827-001** — RSWG compliance window competitive risk
