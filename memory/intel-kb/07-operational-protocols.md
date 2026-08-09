# Operational Protocols - Reporting, Response & Coordination

**Last Updated:** 2026-06-30  
**Status:** In Progress (75% complete)  
**Classification:** INTERNAL REFERENCE (open-source + DAF intel)

---

## 1. Intelligence Reporting Flow (Field → PM)

### Standard Reporting Chain

```
┌─────────────────────────────────────────────────────────────┐
│  LEVEL 1: PERINGKAT AKAR UMBI (Field Level)                 │
│  - PDRM field reports                                       │
│  - APMM patrol logs                                         │
│  - ATM border incident reports                              │
│  - NACSA cyber incident alerts                              │
│  - State/District Security Council reports                  │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  LEVEL 2: SEKTOR KESELAMATAN STRATEGIK (MKN)                │
│  - Tactical filtering & validation                          │
│  - Operational assessment                                   │
│  - Multi-agency deconfliction                               │
│  - Initial response coordination (if needed)                │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  LEVEL 3: BAHAGIAN KESELAMATAN STRATEGIK (PMO)              │
│  - Political-implication assessment                         │
│  - Policy impact analysis                                   │
│  - Strategic risk evaluation                                │
│  - Cabinet communication prep (if needed)                   │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  LEVEL 4: PERDANA MENTERI                                   │
│  - Executive Summary (Dual-Perspective Format):             │
│    • Impak Operasi (from MKN)                               │
│    • Implikasi Strategik (from PMO)                         │
│  - Decision point: approve, escalate, or delegate           │
└─────────────────────────────────────────────────────────────┘
```

---

## 2. Report Classification & Escalation Thresholds

### Classification Levels (per Section 37, Act 776)

| Classification | Handling | Distribution |
|---------------|----------|--------------|
| **TOP SECRET (RAHSIA BESAR)** | Highest protection | PM, DPMs, KP MKN, Pengarah BKS |
| **SECRET (RAHSIA)** | Secure channels | Senior officials, agency heads |
| **CONFIDENTIAL (SULIT)** | Controlled access | Mid-level management |
| **RESTRICTED (TERHAD)** | Limited distribution | Operational staff |

**Note:** All MKN matters are TOP SECRET by law (Section 37, Act 776).

---

### Escalation Thresholds (ESC Codes)

**Integrated with Political Signal Registry escalation framework:**

| ESC Code | Threshold | Response Time | Recipients |
|----------|-----------|---------------|------------|
| **ESC-001 (CRITICAL)** | Imminent threat to national security, sovereignty, or public order | Immediate (<15 min) | PM, DPMs, KP MKN, relevant agency heads |
| **ESC-002 (HIGH)** | Significant security incident with political implications | <1 hour | PM, KP MKN, Pengarah BKS |
| **ESC-003 (MEDIUM)** | Developing situation requiring monitoring | <4 hours | KP MKN, Pengarah BKS |
| **ESC-004 (LOW)** | Routine intelligence, no immediate action | <24 hours | MKN duty officer |
| **ESC-005 (INFO)** | Background intelligence, trend data | Weekly digest | BKS analysts |
| **ESC-006 (ADMIN)** | Administrative, procedural updates | As needed | Relevant staff |

---

## 3. Dual-Perspective Executive Summary Format

**Standard briefing format for Prime Minister:**

```markdown
# KERTAS KERJA: [Title]

## 1. RINGKASAN EKSEKUTIF

### A. Impak Operasi (MKN Assessment)
- Status ancaman: [Current situation]
- Kapasiti respons: [Available resources]
- Garis masa krisis: [Timeline projection]
- Agensi terlibat: [List of involved agencies]

### B. Implikasi Strategik (PMO Assessment)
- Kesan politik: [Domestic political impact]
- Risiko geopolitik: [International implications]
- Naratif awam: [Public perception risk]
- Pilihan dasar: [Policy options]

## 2. SITUASI SEMASA
[Detailed operational update]

## 3. PENILAIAN RISIKO
| Risiko | Kebarangkalian | Impak | Mitigasi |
|--------|----------------|-------|----------|
| [Risk 1] | [High/Med/Low] | [High/Med/Low] | [Mitigation] |

## 4. CADANGAN TINDAKAN
### Pilihan A: [Option name]
- Tindakan: [Description]
- Kelebihan: [Pros]
- Kekurangan: [Cons]

### Pilihan B: [Option name]
- Tindakan: [Description]
- Kelebihan: [Pros]
- Kekurangan: [Cons]

## 5. KEPUTUSAN DIPERLUKAN
[Clear ask for PM decision]

---
**Disediakan oleh:** [BKS-PMO + SKS-MKN]
**Tarikh:** [Date]
**Klasifikasi:** RAHSIA BESAR
```

---

## 4. Inter-Agency Coordination Mechanisms

### COMSEC Framework (Comprehensive Security)

**Objective:** Eliminate communication silos between:
- Military agencies (ATM, APMM)
- Civil intelligence (MKN, BKS)
- Domestic security (PDRM, APM)

### Coordination Structures

#### A. Joint Operations Centre (JOC)
| Feature | Description |
|---------|-------------|
| **Purpose** | Real-time multi-agency crisis coordination |
| **Location** | MKN Headquarters, Putrajaya |
| **Activation** | ESC-001, ESC-002 incidents |
| **Participants** | Liaison officers from PDRM, ATM, APMM, NACSA, etc. |
| **Communication** | Encrypted channels, secure video conferencing |

#### B. National Security Committee (Kabinet)
| Feature | Description |
|---------|-------------|
| **Purpose** | Cabinet-level security policy decisions |
| **Chair** | Prime Minister |
| **Members** | DPMs, Menteri Pertahanan, Menteri Dalam Negeri, KP MKN |
| **Meeting Frequency** | As needed (typically monthly or during crises) |

#### C. Technical Working Groups
| Working Group | Lead Agency | Focus |
|---------------|-------------|-------|
| **Cyber Security WG** | NACSA | CNII protection, cyber incident response |
| **Maritime Security WG** | APMM | ZMM patrol coordination, SCS issues |
| **Border Security WG** | MCBA (when formed) | Land border management |
| **Counter-Terrorism WG** | PDRM (D88) | Domestic CT operations |
| **Disaster Management WG** | NADMA | Emergency response coordination |

---

## 5. Crisis Response Protocols

### Standard Operating Procedure (Generic)

```
PHASE 1: DETECTION & REPORTING
│
├─ Field agency detects incident
├─ Initial report to MKN duty officer (within 30 min)
├─ MKN assigns ESC code
└─ Notify relevant agencies (if multi-agency response needed)
│
▼
PHASE 2: ASSESSMENT & COORDINATION
│
├─ SKS-MKN conducts tactical assessment
├─ BKS-PMO conducts strategic assessment
├─ JOC activated (if ESC-001/002)
└─ Inter-agency coordination call convened
│
▼
PHASE 3: RESPONSE EXECUTION
│
├─ Lead agency executes operational response
├─ MKN coordinates resource allocation
├─ BKS prepares PM briefing
└─ Public communications (if needed) - coordinated message
│
▼
PHASE 4: RESOLUTION & RECOVERY
│
├─ Incident contained/resolved
├─ JOC stands down
├─ After-action review scheduled
└─ Lessons learned documented
│
▼
PHASE 5: POST-INCIDENT ANALYSIS
│
├─ SKS-MKN: Operational after-action report
├─ BKS-PMO: Strategic lessons learned
├─ Arahan MKN updates (if gaps identified)
└─ PM briefed on outcomes
```

---

## 6. Mega-Event Security Protocol

**Applicable to:** Sidang Kemuncak ASEAN 2026, Commonwealth Heads of Government Meeting, etc.

### Pre-Event Phase (6-12 months prior)
- [ ] SKS-MKN leads security planning
- [ ] BKS-PMO assesses geopolitical risk context
- [ ] Multi-agency threat assessment conducted
- [ ] Security perimeter design approved
- [ ] Contingency plans developed (various scenarios)

### Event Phase (during event)
- [ ] JOC activated 24/7
- [ ] Real-time intelligence fusion
- [ ] Rapid response teams on standby
- [ ] PM receives twice-daily briefings (morning/evening)

### Post-Event Phase
- [ ] After-action review (within 30 days)
- [ ] Best practices documented
- [ ] Arahan MKN updates (if needed)

---

## 7. Communication Protocols

### Secure Communication Channels

| Channel | Purpose | Users |
|---------|---------|-------|
| **MKN Secure Network** | Classified document sharing | MKN staff, agency liaisons |
| **Encrypted Voice** | Crisis coordination calls | KP MKN, agency heads |
| **Secure Video Conferencing** | JOC meetings, Cabinet security briefings | Senior leadership |
| **Courier Service** | Physical document transfer (TOP SECRET) | MKN ↔ PMO, agencies |

### Public Communications (During Crises)

| Scenario | Lead Agency | Coordination Required |
|----------|-------------|----------------------|
| **Domestic security incident** | PDRM | MKN approval for public statement |
| **Maritime incursion** | APMM + ATM | MKN + Wisma Putra coordination |
| **Cyber attack on CNII** | NACSA | MKN + sector regulator approval |
| **Natural disaster** | NADMA | MKN coordination, state government liaison |
| **Cross-border incident** | ATM + Wisma Putra | MKN + PMO strategic comms approval |

**Key Principle:** Single coordinated message to avoid confusion.

---

## 8. Simulation & Exercise Framework

### National Security Exercise Cycle

| Exercise Type | Frequency | Scale | Lead |
|---------------|-----------|-------|------|
| **Tabletop Exercise (TTX)** | Quarterly | Agency-specific | SKS-MKN |
| **Command Post Exercise (CPX)** | Annual | Multi-agency | MKN |
| **Field Exercise (FIELDEX)** | Biennial | Full-scale operational | Lead agency + MKN |
| **Mega-Event Rehearsal** | Pre-event | Event-specific | SKS-MKN + host agency |

### Example: Cyber Crisis Simulation (Arahan MKN No. 24)
- **Scenario:** Coordinated ransomware attack on multiple CNII sectors
- **Participants:** NACSA, MKN, sector regulators, affected operators
- **Objectives:** Test reporting thresholds, inter-agency coordination, public communications
- **Output:** After-action report → Arahan MKN No. 24 revision (if gaps found)

---

## 9. Compliance Monitoring

### MKN Audit Powers

| Audit Type | Frequency | Target |
|------------|-----------|--------|
| **Compliance Audit** | Annual | All ministries (Arahan MKN implementation) |
| **Readiness Assessment** | Biennial | State/District Security Councils |
| **CNII Security Audit** | Annual | Critical infrastructure operators |
| **Special Inquiry** | As needed | Specific incidents or failures |

### Reporting Requirements

| Report Type | Frequency | Recipient |
|-------------|-----------|-----------|
| **Monthly Security Report** | Monthly | KP MKN |
| **Quarterly Threat Assessment** | Quarterly | PM, Cabinet Security Committee |
| **Annual Security Review** | Annual | PM, Parliament (classified annex) |

---

## 10. Gaps / To Verify

- [ ] Exact reporting timelines for each ESC level
- [ ] Specific templates used for PM briefings
- [ ] Full list of JOC participating agencies
- [ ] Details of secure communication infrastructure
- [ ] Historical after-action reports (for pattern analysis)

---

**Cross-References:**
- `01-command-architecture.md` - Reporting chain authority
- `04-directives-library.md` - Arahan MKN compliance requirements
- `06-threat-landscape.md` - Threat-specific response protocols
- `08-relationship-network.md` - Inter-agency coordination details

---

## Notes for Future Updates

1. **Integration with Signal Registry:** Map ESC codes to Political Signal Registry thresholds
2. **Template Library:** Collect actual briefing templates (if available via open sources)
3. **Case Studies:** Document historical crisis responses for lessons learned
4. **Contact Directory:** Build detailed liaison officer contact list (if publicly available)
