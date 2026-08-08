# Red Team Division — Fullstack National Capability

**Document Status:** DRAFT v0.1  
**Date:** 2026-08-08  
**Authority:** DAF  
**Classification:** INTERNAL — RESTRICTED  
**Context:** Cyber Security Practice expansion — elevating OffSec workstream to standalone division

---

## 1. Strategic Rationale

### Why a Red Team Division?

The Cyber Security Practice currently has Offensive Security as a workstream within the broader BU — 2 roles (Lead Researcher + Security Researcher), RM1.3M revenue target, triggered in Wave 3 of hiring. This is insufficient for what the practice is becoming.

Three drivers force the elevation:

1. **National Capability Mandate** — VORON-C2 architecture, GovSec integration, and NACSA/JDN engagement requirements demand a dedicated division, not a workstream. A national red team capability needs institutional structure, not opportunistic delivery.

2. **Threat Landscape Urgency** — Akira, BumbleBee, AdaptixC2, and AI-generated attack tooling are active in the Malaysian threat landscape. Defensive capability without offensive understanding is blind. The division exists to generate the telemetry that detection engineering depends on.

3. **Commercial Differentiation** — Generic cybersecurity providers sell assessments. A sovereign red team division with dark web intelligence, indigenous C2 infrastructure, and adversary emulation capability sells national resilience. This is a different category of engagement.

### What "Fullstack" Means

| Layer | Capability | Purpose |
|------|------------|---------|
| **Pre-Engagement** | Dark web intelligence, OSINT, threat actor profiling | Understand the adversary before emulating |
| **Initial Access** | Phishing, exploit development, supply chain attacks | Reproduce real attack vectors |
| **C2 Operations** | VORON-C2 (Mythic, Sliver, Havoc, AdaptixC2) | Sustain presence, execute objectives |
| **Post-Exploitation** | Lateral movement, credential harvesting, privilege escalation | Demonstrate full kill chain |
| **Detection Engineering** | Wazuh + ELK, detection rules, purple team exercises | Convert offensive output to defensive value |
| **Reporting** | Structured engagement reports, executive briefings, remediation tracking | Deliver actionable intelligence to stakeholders |

### National Capability Builder Framing

This is not a commercial red team service. It is a **national capability builder** — Aras Integrasi building indigenous Malaysian capacity for adversarial emulation, threat intelligence, and cyber resilience. The division serves:

- **Government** — NACSA, JDN/JDM, CNII sector red teaming, national cyber exercises
- **Defence** — Military red team support, adversary emulation for defence networks
- **Critical Infrastructure** — Energy, finance, telecoms, healthcare red team engagements
- **Commercial** — Enterprise red teaming with national-grade capability (premium positioning)

The sovereign framing matters: Malaysian-controlled infrastructure, Malaysian-operated, no foreign vendor dependency. This aligns with the Cyber Security Act 2024 and national digital sovereignty agenda.

---

## 2. Organisational Structure — 5 FTE

### Design Principle: Compact, High-Leverage, Full Coverage

Five roles. Each covers a critical function. No redundancy, no dead weight. Every role must justify its existence against the capability stack.

### Role 1: Head of Red Team Division (Principal)

| Attribute | Detail |
|-----------|--------|
| **Title** | Head of Red Team Division / Principal Red Team Lead |
| **Level** | Principal / Leadership |
| **Reports to** | Director, Cyber Security Practice (DAF) |
| **Primary Function** | Division leadership, engagement management, national capability stakeholder relationships, strategic development |

**Responsibilities:**
- Division P&L ownership, revenue target, capacity planning
- Lead engagement scoping, rules of engagement (ROE), authorization frameworks
- National capability stakeholder management (NACSA, JDN, CNII sector leads)
- Management committee reporting, budget advocacy, strategic roadmap
- Senior client engagement — briefing C-suite, ministerial level, national cyber exercise design
- Quality assurance on all engagement deliverables
- Talent pipeline development (intern/skunkworks programme oversight)

**Why this role exists:** A division needs a leader who can operate at both the technical and national-strategic level. This person speaks to NACSA directors and writes detection rules. Without this role, the division is a team of operators with no institutional voice.

**Profile:** 8-12 years cybersecurity, 4+ years red team leadership, demonstrated national/government engagement experience, strong written and verbal communication. Must be Malaysian citizen (national capability requirement).

**KPIs:**
- Division revenue vs target
- Engagement delivery quality (client NPS, remediation rate)
- National capability milestones (framework adoption, exercise delivery)
- Stakeholder relationships active (NACSA, JDN, CNII sector)
- Talent pipeline health (intern conversion, skills matrix progression)

**Estimated compensation:** RM 12,000-16,000/month

---

### Role 2: Senior Red Team Operator

| Attribute | Detail |
|-----------|--------|
| **Title** | Senior Red Team Operator |
| **Level** | Senior / Individual Contributor |
| **Reports to** | Head of Red Team Division |
| **Primary Function** | Offensive operations execution, C2 management, attack chain implementation |

**Responsibilities:**
- Execute red team engagements end-to-end (initial access through impact)
- VORON-C2 infrastructure operations — Mythic, Sliver, Havoc, AdaptixC2 deployment, agent management, redirector infrastructure
- Payload development — phishing templates, exploit integration, custom BOFs, agent modifications
- Attack chain reproduction — emulate observed threat actor TTPs (Akira, BumbleBee, ransomware operators)
- Engagement documentation — technical logs, attack chain recording, evidence preservation
- Purple team execution — work alongside Detection Engineer to validate detection coverage
- Tool development — custom scripts, automation, C2 module development
- Skunkworks intern technical supervision

**Why this role exists:** This is the tip of the spear. Without a dedicated operator, the division has theory and infrastructure but no execution capacity. The senior operator runs the C2 stack, delivers engagements, and produces the raw offensive output that everything else depends on.

**Profile:** 5-8 years cybersecurity, 3+ years hands-on red team/pentest, deep C2 framework experience (Cobalt Strike, Sliver, Mythic, or equivalent), OSCP/OSEP/CRTO certification or equivalent demonstrated skill, strong scripting (Python, Go, PowerShell), understanding of Malaysian threat landscape.

**KPIs:**
- Engagements delivered per year
- Attack chain completeness (initial access → objective achieved rate)
- C2 infrastructure uptime and operational security
- Detection engineering contribution (TTPs mapped to detections)
- Tool/script output (reusable assets created)

**Estimated compensation:** RM 8,000-12,000/month

---

### Role 3: Dark Web Intelligence Analyst

| Attribute | Detail |
|-----------|--------|
| **Title** | Dark Web Intelligence Analyst |
| **Level** | Senior / Individual Contributor |
| **Reports to** | Head of Red Team Division |
| **Primary Function** | Dark web monitoring, threat actor tracking, underground marketplace intelligence, pre-engagement intelligence preparation |

**Responsibilities:**
- Monitor dark web forums, marketplaces, Telegram channels, and underground communities for:
  - Threat actor TTPs, tool sales, service offerings
  - Leaked credentials, data breaches affecting Malaysian entities
  - Emerging ransomware groups, initial access brokers, affiliate programs
  - Malaysian-targeted attack planning, doxxing, infrastructure exposure
- Threat actor profiling — track groups, affiliations, tooling preferences, target selection patterns
- Credential leak monitoring — alert government and commercial clients when credentials surface
- Pre-engagement intelligence — before any red team operation, build the threat picture: who targets this sector, what tools they use, what TTPs are current
- Intelligence reporting — structured intelligence briefs, IOCs, actor profiles, trend analysis
- OSINT collection and enrichment — Mr.Holmes, manual collection, source validation
- Feed into Threat Intelligence workstream (cross-functional with broader BU intelligence team)
- Dark web infrastructure maintenance — Tor, I2P, VPN, safe collection environment

**Why this role exists:** Red team without intelligence is blind emulation. Dark web intelligence tells you *which* adversaries to emulate, *what* TTPs are current, and *where* the real threats are targeting Malaysian infrastructure. It also provides standalone value — dark web monitoring as a service for government and CNII clients. This role bridges the pre-engagement gap and adds a dedicated intelligence collection capability that no generic red team service provides.

**Profile:** 4-7 years cybersecurity or intelligence analysis, experience with dark web navigation (Tor, I2P, underground forums), OSINT/Wireshark/Maltego or equivalent, threat intelligence platforms (MISP, OpenCTI), structured analytical techniques (STIX/TAXII), strong analytical writing. Malaysian citizen preferred (national capability). Understanding of Malaysian threat landscape and regional cybercrime ecosystem.

**KPIs:**
- Intelligence reports produced per quarter
- Threat actor profiles maintained (active monitoring)
- Pre-engagement intelligence packages delivered
- Credential leak alerts (timeliness, accuracy, client coverage)
- Source network breadth (forums, marketplaces, channels monitored)
- Intelligence integrated into red team engagements (percentage of engagements with intel-driven TTP selection)

**Estimated compensation:** RM 7,000-10,000/month

---

### Role 4: Detection Engineer (Purple Team)

| Attribute | Detail |
|-----------|--------|
| **Title** | Detection Engineer |
| Level | Senior / Individual Contributor |
| **Reports to** | Head of Red Team Division |
| **Primary Function** | Convert offensive output into defensive detection capability, purple team execution, SIEM engineering |

**Responsibilities:**
- Build and maintain detection engineering pipeline — Wazuh + ELK stack
- Write, test, and validate detection rules based on red team engagement output
- Map detections to MITRE ATT&CK framework
- Purple team exercises — real-time detection validation during red team operations
- Detection coverage gap analysis — identify TTPs with no detection coverage
- SIEM engineering — log source onboarding, parser development, correlation rules, alert tuning
- Threat hunting — proactive hunts based on dark web intelligence and red team TTPs
- Client-facing detection engineering — deliver detection packages as engagement deliverables
- Metrics — detection latency, false positive rate, coverage percentage
- Maintain detection rule library (reusable across engagements)

**Why this role exists:** Red team without blue team is just breaking things. The detection engineer is what makes this a *capability builder* rather than a *service provider*. Every engagement produces detection rules that stay with the client. This compounds over time — the division builds a national detection rule library that becomes a strategic asset.

**Profile:** 4-7 years cybersecurity, 2+ years SIEM/detection engineering (Wazuh, Splunk, ELK, or equivalent), MITRE ATT&CK fluency, purple team experience, scripting (Python, Sigma rules), understanding of Windows/Linux internals and attack techniques. OSCP/GCIA/GCIA or equivalent.

**KPIs:**
- Detection rules produced per engagement
- Detection coverage percentage (MITRE ATT&CK techniques covered)
- Purple team exercises completed
- Detection latency (time from TTP execution to alert)
- False positive rate (target <5%)
- Client detection package delivery rate
- National detection rule library size and quality

**Estimated compensation:** RM 7,000-10,000/month

---

### Role 5: Offensive Security Researcher

| Attribute | Detail |
|-----------|--------|
| **Title** | Offensive Security Researcher |
| **Level** | Mid-Senior / Individual Contributor |
| **Reports to** | Head of Red Team Division |
| **Primary Function** | Vulnerability research, exploit development, C2 framework R&D, tool innovation |

**Responsibilities:**
- Vulnerability research — discover, analyze, and validate vulnerabilities in target technologies (software, firmware, protocols)
- Exploit development — write reliable exploits for identified vulnerabilities (internal use only, responsible disclosure where applicable)
- C2 framework R&D — extend VORON-C2 stack with custom modules, agents, BOFs, evasion techniques
- Evasion research — test C2 agents against commercial EDR/AV products, develop bypass techniques
- AI-augmented offensive research — leverage CyberStrike and local LLMs for payload obfuscation, YARA rule generation, attack chain analysis
- Attack surface analysis — research emerging technologies for new attack vectors (cloud, IoT, OT/ICS, AI systems)
- Technical advisory — support Senior Operator with novel exploitation during engagements
- Research publications — produce technical research for external visibility (conference talks, blog posts, advisories) positioning Aras as thought leader
- Tool maintenance and development — maintain division's internal tool library, contribute to open-source where strategic

**Why this role exists:** A red team division that only uses existing tools is a commodity. The researcher is what makes the division genuinely different — custom exploits, novel evasion techniques, and indigenous tool development. This role also feeds the talent pipeline — researchers mentor interns and produce the technical content that builds the division's reputation.

**Profile:** 3-6 years cybersecurity, demonstrated vulnerability research (CVEs, write-ups, bug bounties), exploit development experience (Python, C, assembly), reverse engineering (Ghidra, IDA, radare2), C2 framework internals knowledge, familiarity with EDR/AV bypass techniques. OSEE/OSED/CRTO-II or equivalent demonstrated skill.

**KPIs:**
- Vulnerability research outputs (findings, write-ups, advisories)
- Exploit development (working exploits produced)
- C2 tool contributions (modules, agents, BOFs, evasion techniques)
- EDR/AV bypass research (techniques developed, tested, documented)
- Research publications (conference talks, blog posts, community contributions)
- Engagement support (novel exploitation delivered)

**Estimated compensation:** RM 7,000-11,000/month

---

## 3. Capability Stack

### Division Solution Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                   RED TEAM DIVISION                              │
│                                                                  │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────────┐   │
│  │  INTELLIGENCE │  │  OFFENSIVE    │  │  DETECTION           │   │
│  │  COLLECTION   │  │  OPERATIONS   │  │  ENGINEERING         │   │
│  │               │  │               │  │                      │   │
│  │  Dark Web Mon │  │  VORON-C2     │  │  Wazuh + ELK         │   │
│  │  OSINT (Mr.H) │  │  Mythic      │  │  Sigma Rules         │   │
│  │  Actor Profiling│ │  Sliver      │  │  Purple Team        │   │
│  │  Cred Leaks   │  │  Havoc       │  │  MITRE ATT&CK       │   │
│  │  Pre-Eng Intel│  │  AdaptixC2   │  │  Threat Hunting     │   │
│  └──────┬───────┘  └──────┬───────┘  └──────────┬───────────┘   │
│         │                  │                      │               │
│         └──────────────────┼──────────────────────┘               │
│                            │                                      │
│                   ┌────────▼────────┐                             │
│                   │   RESEARCH &    │                             │
│                   │   DEVELOPMENT   │                             │
│                   │                 │                             │
│                   │  Vulnerability  │                             │
│                   │  Research      │                              │
│                   │  Exploit Dev    │                             │
│                   │  C2 R&D        │                              │
│                   │  Evasion       │                              │
│                   │  CyberStrike   │                              │
│                   └─────────────────┘                             │
└─────────────────────────────────────────────────────────────────┘
```

### Technology Stack

| Layer | Technology | Status | Notes |
|-------|-----------|--------|-------|
| **C2 Core** | Mythic (primary) | Architecture complete | Docker-based, extensible, multiplayer |
| | Sliver (workhorse) | Architecture complete | Go-based, cross-platform implants |
| | Havoc (stealth) | Architecture complete | C/C++ agents, evasion focus |
| | AdaptixC2 (emulation) | Architecture complete | Adversary emulation, BOF support |
| **Infrastructure** | Apache/Nginx redirectors | Architecture complete | Traffic distribution, OPSEC |
| | DNS infrastructure | Architecture complete | DNS beacons, domain fronting |
| | Cloud VPS fleet | To be provisioned | Malaysian-hosted, sovereign |
| **Detection** | Wazuh SIEM | Architecture complete | Open-source, ARM64 compatible |
| | Elasticsearch + Kibana | Architecture complete | Log storage, analytics, visualization |
| | Sigma rule library | To be built | Reusable detection rules |
| **Intelligence** | Mr.Holmes OSINT | Deployed | Username, phone, domain, email OSINT |
| | Dark web monitoring stack | To be built | Tor, forum scrapers, alert system |
| | MISP / OpenCTI | To be evaluated | Threat intelligence platform |
| **R&D** | CyberStrike integration | Conceptual | AI-augmented offensive ops |
| | Local LLM (DGX Spark) | Available | Payload obfuscation, YARA gen, analysis |
| | Exploit dev lab | To be built | Isolated environment for safe research |
| **Reporting** | Engagement report templates | To be built | Standardised deliverables |
| | Executive briefing templates | To be built | National-level presentation format |

---

## 4. Revenue Model

### Revenue Streams

| Stream | Model | Year 1 Target | Year 2 Target | Notes |
|--------|-------|---------------|---------------|-------|
| **Government Red Team Engagements** | Project-based, national exercise | RM 500K | RM 1.0M | NACSA, JDN, CNII sector |
| **Commercial Red Team Engagements** | Project-based, tiered pricing | RM 400K | RM 800K | Enterprise, financial sector |
| **Dark Web Intelligence Service** | Subscription retainer | RM 300K | RM 600K | Continuous monitoring for clients |
| **Purple Team / Detection Engineering** | Project + retainer | RM 200K | RM 500K | Detection package + ongoing tuning |
| **National Cyber Exercise** | Annual contract | RM 200K | RM 400K | National-level red vs blue exercise |
| **Training & Certification** | Per-seat, cohort-based | RM 100K | RM 300K | Intern programme → external training |
| **Vulnerability Research / Advisories** | Subscription or per-report | RM 50K | RM 200K | Technical research, responsible disclosure |
| **Total** | | **RM 1.75M** | **RM 3.8M** | Conservative |

### Cost Structure

| Item | Year 1 Cost | Notes |
|------|-------------|-------|
| **Personnel (5 FTE)** | RM 552K-828K | Range across role compensation |
| **Infrastructure** | RM 30K-50K | VPS, domains, DNS, dark web access |
| **Tooling & Lab** | RM 10K-20K | Exploit dev lab, testing environments |
| **Training & Cert** | RM 20K-30K | Team skill development |
| **Total** | RM 612K-928K | |

### ROI

| Metric | Year 1 | Year 2 |
|--------|--------|--------|
| Revenue | RM 1.75M | RM 3.8M |
| Cost | RM 750K (mid) | RM 850K (salary growth) |
| **Gross Margin** | RM 1.0M | RM 2.95M |
| **ROI** | 2.3x | 4.5x |
| **Break-even** | 2-3 engagements | First quarter |

---

## 5. Phased Build-Out

### Phase 1: Foundation (Months 1-3)

**Objective:** Division established, core capability operational, first engagement delivered.

| Milestone | Target | Owner |
|-----------|--------|-------|
| Head of Division hired | Month 1 | DAF |
| VORON-C2 infrastructure deployed (Mythic + Sliver) | Month 2 | Senior Operator |
| Dark web monitoring stack operational | Month 2 | Dark Web Analyst |
| Detection engineering pipeline (Wazuh + ELK) | Month 2 | Detection Engineer |
| First engagement scope defined | Month 2 | Head of Division |
| Team fully hired (all 5 FTE) | Month 3 | DAF + Head |
| First red team engagement delivered | Month 3 | Full team |
| First dark web intelligence report delivered | Month 3 | Dark Web Analyst |

### Phase 2: Operationalization (Months 4-6)

**Objective:** Routine engagement delivery, purple team capability active, national stakeholder engagement.

| Milestone | Target | Owner |
|-----------|--------|-------|
| VORON-C2 full stack (Havoc + AdaptixC2 added) | Month 4 | Senior Operator |
| First purple team exercise delivered | Month 4 | Detection Engineer + Operator |
| NACSA engagement scoped | Month 4 | Head of Division |
| Detection rule library (30+ rules) | Month 5 | Detection Engineer |
| First government engagement delivered | Month 5 | Full team |
| Threat actor profile library (5+ actors) | Month 5 | Dark Web Analyst |
| First CVE / vulnerability research published | Month 6 | OffSec Researcher |
| Skunkworks Cohort 1 onboarded | Month 6 | Head of Division |

### Phase 3: National Capability (Months 7-12)

**Objective:** National recognition, routine government engagement, cyber exercise delivery, revenue target achieved.

| Milestone | Target | Owner |
|-----------|--------|-------|
| National cyber exercise designed and pitched | Month 8 | Head of Division |
| Dark web intelligence service (3+ clients on retainer) | Month 8 | Dark Web Analyst |
| GovSec Red integration scoped | Month 9 | Head + GovSec TPM |
| Detection rule library (100+ rules) | Month 9 | Detection Engineer |
| First national cyber exercise delivered | Month 10 | Full team |
| Research publication (conference talk) | Month 10 | OffSec Researcher |
| Revenue target RM 1.75M achieved | Month 12 | Head of Division |
| Skunkworks Cohort 2 onboarded | Month 12 | Head of Division |

### Phase 4: GovSec Integration & Scaling (Months 13-18)

**Objective:** Division integrated into GovSec TIP, national capability institutionalized, scaling toward RM 3.8M.

| Milestone | Target | Owner |
|-----------|--------|-------|
| GovSec Red module operational | Month 14 | Head + GovSec TPM |
| CyberStrike integration (AI-augmented ops) | Month 15 | OffSec Researcher |
| National detection rule library (500+ rules) | Month 16 | Detection Engineer |
| Annual national cyber exercise (recurring) | Month 18 | Head of Division |
| Revenue target RM 3.8M trajectory | Month 18 | Head of Division |

---

## 6. Dark Web Intelligence — Deep Dive

### Why It's Part of the Red Team Division (Not Separate)

Dark web intelligence serves three functions within the division:

1. **Pre-Engagement Intelligence** — Before any red team operation, the dark web analyst builds the threat picture: Which actors target this sector? What tools are they selling? What TTPs are current? What credentials are already leaked for the target? This makes red team engagements *threat-driven*, not generic. Without this, you're running standard pentest playbooks against a live threat landscape you haven't studied.

2. **Standalone Service** — Dark web monitoring as a subscription for government and CNII clients. "We watch the dark web for your leaked credentials, your brand mentions, your infrastructure exposure." This is immediately commercializable without waiting for red team engagement infrastructure to mature. Revenue from Month 3.

3. **Threat Intelligence Feed** — Feeds into the broader BU threat intelligence workstream and GovSec TIP. Dark web findings become IOCs, actor profiles, and trend analysis that enrich the entire practice's intelligence picture.

### Capability Architecture

```
┌─────────────────────────────────────────────┐
│         DARK WEB INTELLIGENCE STACK          │
│                                              │
│  ┌─────────────┐  ┌──────────────────────┐  │
│  │ COLLECTION   │  │  ANALYSIS            │  │
│  │              │  │                      │  │
│  │ Tor/I2P      │  │ Actor profiling     │  │
│  │ Forum scrape │  │ TTP extraction      │  │
│  │ Market mon   │  │ Credential analysis │  │
│  │ Telegram mon │  │ Trend analysis      │  │
│  │ IRC monitor  │  │ Risk scoring        │  │
│  └──────┬──────┘  └──────────┬───────────┘  │
│         │                     │               │
│         └─────────────────────┘               │
│                     │                        │
│              ┌──────▼───────┐                │
│              │  DELIVERY     │                │
│              │              │                │
│              │ Intel briefs  │                │
│              │ IOC feeds     │                │
│              │ Cred alerts   │                │
│              │ Actor reports │                │
│              │ Pre-eng packs │                │
│              └──────────────┘                │
└─────────────────────────────────────────────┘
```

### Monitoring Targets

| Target Type | Specifics | Method |
|-------------|-----------|--------|
| **Underground forums** | Ransomware leak sites, carding forums, exploit marketplaces | Tor access, monitored accounts, scrape pipeline |
| **Telegram channels** | Cybercrime channels, initial access broker channels, Malaysian/SEA-focused threat groups | Telegram API, keyword monitoring |
| **Marketplaces** | Credential markets, tool sales, access sales | Periodic manual + automated monitoring |
| **Leak sites** | Ransomware victim posting sites (Akira, Fog, etc.) | RSS/scrape monitoring, alert on Malaysian entities |
| **Code repositories** | GitHub, GitLab for leaked credentials, exposed API keys, internal code | Automated scanning (Mr.Holmes + manual) |
| **Surface web OSINT** | LinkedIn, job postings, tech forums for infrastructure exposure | Mr.Holmes, manual collection |

### Deliverable Types

| Deliverable | Audience | Frequency | Revenue Link |
|------------|----------|-----------|-------------|
| **Pre-Engagement Intelligence Package** | Red team division (internal) | Per engagement | Embedded in engagement cost |
| **Dark Web Monitoring Report** | Client (government/commercial) | Monthly (subscription) | RM 3K-8K/month per client |
| **Credential Leak Alert** | Client (real-time) | Event-driven | Included in monitoring subscription |
| **Threat Actor Profile** | Client + internal | Quarterly | Embedded in retainer or standalone |
| **Dark Web Trend Brief** | Client executive | Quarterly | Premium retainer add-on |
| **IOC Feed** | GovSec TIP / client SIEM | Continuous | Integration into GovSec subscription |

---

## 7. Relationship to Existing Practice

### BU Integration Points

| Existing Workstream | Red Team Division Relationship |
|--------------------|------------------------------|
| **GovSec TIP** | Division feeds IOCs, threat actor data, and detection rules into GovSec. Phase 4: GovSec Red module operational. |
| **VORON/VoronDRQ** | Division provides adversary emulation data that validates VORON compliance assessments. Purple team outputs prove detection gaps. |
| **Threat Intelligence** | Dark web analyst feeds into broader TI workstream. Cross-functional intelligence sharing. |
| **Professional Services** | Division delivers red team engagements as premium PS engagements. PS engineers can shadow for skill transfer. |
| **Blockchain Intelligence** | Division researches blockchain-based dark web marketplaces. Cross-pollination on crypto crime tracking. |
| **DevSecOps** | Division tests client DevSecOps pipelines (CI/CD attacks, supply chain). Detection engineer validates security controls. |

### Governance

| Attribute | Detail |
|-----------|--------|
| **Division Head reports to** | Director, Cyber Security Practice (DAF) |
| **Engagement authorization** | Head of Division + DAF co-sign for government engagements; Head alone for commercial |
| **Rules of Engagement (ROE)** | Standardized ROE template per engagement type (government, commercial, internal) |
| **Legal framework** | Cyber Security Act 2024 compliance, Computer Crimes Act, client authorization letters |
| **Audit trail** | All C2 activity logged, engagement evidence preserved, reportable to client and regulators |
| **Insurance** | Professional indemnity + cyber liability insurance for engagement delivery |

---

## 8. Talent Pipeline

### Skunkworks → Division Flow

The VORON-C2 Skunkworks Programme (already designed) becomes the division's talent pipeline:

```
Skunkworks Cohort (3-4 interns, 5 weeks)
    ↓
Top performers offered Associate roles (future expansion)
    ↓
Associate → Senior progression within division
    ↓
Senior → Principal (future Head of Division candidate)
```

**Cohort 1** (Month 6): First intern cohort onboarded, runs 5-week skunkworks
**Cohort 2** (Month 12): Second cohort, Cohort 1 survivors mentor
**Year 2**: Cohort 3-4, division becomes self-sustaining talent engine

### Skills Matrix (Division Internal)

| Skill | Head | Operator | Dark Web Analyst | Detection Eng | Researcher |
|-------|------|----------|------------------|---------------|------------|
| C2 Operations | ●●●○○ | ●●●●● | ●○○○○ | ●●○○○ | ●●●○○ |
| Exploit Dev | ●●○○○ | ●●●○○ | ●○○○○ | ●○○○○ | ●●●●● |
| Detection Engineering | ●●○○○ | ●●○○○ | ●○○○○ | ●●●●● | ●●○○○ |
| Dark Web / OSINT | ●●○○○ | ●○○○○ | ●●●●● | ●○○○○ | ●●○○○ |
| Threat Intelligence | ●●●○○ | ●●○○○ | ●●●●○ | ●●○○○ | ●●○○○ |
| Engagement Mgmt | ●●●●● | ●●○○○ | ●○○○○ | ●○○○○ | ●○○○○ |
| Stakeholder Mgmt | ●●●●● | ●○○○○ | ●○○○○ | ●○○○○ | ●○○○○ |
| Reporting | ●●●●○ | ●●●○○ | ●●●○○ | ●●●○○ | ●●●●○ |
| Research | ●●○○○ | ●●○○○ | ●●○○○ | ●●○○○ | ●●●●● |
| Tool Development | ●○○○○ | ●●●○○ | ●○○○○ | ●●○○○ | ●●●●○ |

---

## 9. Management Summary

### The Ask

| Item | Detail |
|------|--------|
| **Headcount** | 5 FTE (new division) |
| **Annual personnel cost** | RM 552K-828K |
| **Total Year 1 cost (incl. infra)** | RM 612K-928K |
| **Year 1 revenue target** | RM 1.75M |
| **Year 2 revenue target** | RM 3.8M |
| **ROI Year 1** | 2.3x |
| **Break-even** | 2-3 paid engagements |
| **National capability** | Sovereign red team, dark web intelligence, detection engineering |
| **Government stakeholder** | NACSA, JDN/JDM, CNII sector |
| **Existing investment leveraged** | VORON-C2 architecture (RM 0 licensing), Mr.Holmes, Wazuh/ELK, CyberStrike integration path |

### Why Approve

1. **National capability** — Builds Malaysian sovereign offensive security capacity. No foreign dependency.
2. **Revenue-positive from Year 1** — 2.3x ROI, break-even at 2-3 engagements
3. **Zero licensing cost** — Full open-source stack already architected
4. **Feeds GovSec** — Division output enriches GovSec TIP, increasing platform value
5. **Dark web intelligence** — Immediately commercializable, revenue from Month 3
6. **Talent pipeline** — Skunkworks programme already designed, feeds division growth
7. **Differentiation** — No Malaysian competitor offers sovereign red team + dark web intel + detection engineering as integrated capability
8. **Threat relevance** — Directly responds to Akira, AdaptixC2, and AI-augmented threat landscape

### Risk Mitigation

| Risk | Mitigation |
|------|------------|
| Head of Division hiring difficulty | DAF interim leadership, skunkworks pipeline, competitive comp |
| Government engagement cycle slow | Commercial engagements bridge revenue gap |
| Dark web access operational risk | Legal framework, VPN/Tor hygiene, documented collection methodology |
| C2 infrastructure compromise | Segregated infrastructure, OPSEC protocols, regular rotation |
| Talent retention | Clear progression path, research time allocation, conference budget |
| Legal/regulatory compliance | Cyber Security Act 2024 alignment, ROE templates, legal review per engagement |

---

## 10. Next Actions

| # | Action | Owner | Deadline |
|---|--------|-------|----------|
| 1 | Review and approve division structure | DAF | Immediate |
| 2 | Draft Head of Division job description and open recruitment | DAF + HR | Week 1 |
| 3 | Interim: DAF appoints acting Head from existing team or self | DAF | Week 1 |
| 4 | Open remaining 4 role recruitments | HR | Week 2 |
| 5 | Provision VORON-C2 infrastructure (Phase 1: Mythic + Sliver) | Senior Operator (on hire) | Month 2 |
| 6 | Stand up dark web monitoring stack | Dark Web Analyst (on hire) | Month 2 |
| 7 | First management committee presentation (this document) | DAF | Week 2-3 |
| 8 | Identify first engagement target (commercial or government) | DAF + Head | Month 2 |
| 9 | Schedule NACSA introductory engagement | DAF | Month 3 |
| 10 | Launch Skunkworks Cohort 1 recruitment | Head of Division | Month 4 |

---

---

## 11. Engagement Lifecycle (Operational SOP)

### Standard Engagement Workflow

Every red team engagement follows a structured 7-phase lifecycle. No engagement begins without Phase 1–2 completion and signed authorisation.

### Phase 1: Scoping & Authorization (Weeks –2 to 0)

| Step | Owner | Output |
|------|-------|--------|
| Client intake meeting | Head of Division | Engagement objectives, target environment overview |
| Pre-engagement intelligence package | Dark Web Analyst | Threat landscape, actor recommendations, TTP priorities, OSINT summary |
| Scope definition document | Head of Division | In-scope assets, out-of-scope assets, rules of engagement, timeline |
| Rules of Engagement (ROE) | Head of Division + Client | Authorisation letter, scope confirmation, emergency contacts, stop conditions |
| Legal review | Head of Division (with legal counsel if required) | Cyber Security Act 2024 compliance, Computer Crimes Act compliance, client authorisation verified |
| Go/No-go decision | Head of Division (Director co-sign for government) | Signed authorisation, engagement scheduled |

**Deliverables:** Signed ROE, scope document, engagement schedule
**Duration:** 1–2 weeks
**Gate criteria:** Signed authorisation, clear objectives, no legal blockers

### Phase 2: Planning & Preparation (Week 0)

| Step | Owner | Output |
|------|-------|--------|
| Attack plan development | Senior Operator + Head | TTP selection based on intelligence package, attack chain design |
| Infrastructure deployment | Senior Operator | C2 servers, redirectors, payload hosting, DNS configured and tested |
| Payload preparation | Senior Operator + Researcher | Phishing templates, exploit payloads, custom BOFs built and tested |
| Detection stack deployment | Detection Engineer | Wazuh deployed at client environment (if purple team), log sources onboarded, baseline established |
| Team briefing | Head of Division | All team members briefed on scope, ROE, objectives, roles |

**Deliverables:** Attack plan, deployed infrastructure, prepared payloads, team briefing
**Duration:** 1 week
**Gate criteria:** Infrastructure operational, payloads tested, team briefed

### Phase 3: Initial Access (Week 1)

| Step | Owner | Output |
|------|-------|--------|
| Phishing campaign execution | Senior Operator | Emails sent, landing pages deployed, payload delivery |
| Exploit delivery (if network-accessible) | Senior Operator | Direct exploitation of exposed services |
| Initial beacon check-in | Senior Operator | First C2 sessions established, agent connectivity confirmed |
| Initial access report | Senior Operator | Methods attempted, success rate, initial foothold documentation |

**Deliverables:** Initial access achieved, C2 beacons calling back, engagement log started
**Duration:** 1–5 days
**Gate criteria:** At least one initial access vector successful

### Phase 4: Post-Exploitation & Objective Achievement (Weeks 2–3)

| Step | Owner | Output |
|------|-------|--------|
| Internal reconnaissance | Senior Operator | Network map, domain enumeration, high-value target identification |
| Privilege escalation | Senior Operator | Domain admin or equivalent achieved, access to target objectives |
| Lateral movement | Senior Operator | Access to in-scope systems, objective targets reached |
| Credential harvesting | Senior Operator | Credentials collected, validated, stored securely |
| Objective execution | Senior Operator | Data access demonstrated, impact simulation (controlled) |
| Purple team monitoring | Detection Engineer | Real-time detection monitoring, gap documentation, alert validation |

**Deliverables:** Full attack chain documented, objectives achieved, purple team data collected
**Duration:** 1–2 weeks
**Gate criteria:** Engagement objectives met or timebox expired

### Phase 5: Reporting & Delivery (Week 4)

| Step | Owner | Output |
|------|-------|--------|
| Technical engagement report | Senior Operator + Head | Full attack chain, timeline, TTPs used, findings, evidence |
| Detection coverage report | Detection Engineer | Coverage matrix, detection gaps, latency metrics, new rules written |
| Executive briefing | Head of Division | C-suite presentation, business impact, strategic recommendations |
| Detection package delivery | Detection Engineer | Sigma rules, Wazuh rules, deployment instructions for client SIEM |
| Remediation recommendations | Head of Division | Prioritised remediation list with effort and impact ratings |

**Deliverables:** Technical report, executive briefing, detection package, remediation plan
**Duration:** 1 week
**Gate criteria:** Client accepts delivery, signs engagement completion

### Phase 6: Post-Engagement Review (Week 5)

| Step | Owner | Output |
|------|-------|--------|
| Internal post-mortem | Head of Division | What worked, what didn't, process improvements |
| Detection library update | Detection Engineer | New rules added to national library, tagged with sector and technique |
| Lessons learned documentation | Full team | Runbook updates, tool improvements, SOP revisions |
| Client feedback collection | Head of Division | Client NPS, satisfaction survey, improvement suggestions |
| Engagement evidence archival | Senior Operator | Evidence packaged, encrypted, stored per retention policy |

**Deliverables:** Post-mortem report, updated runbooks, archived evidence
**Duration:** 2–3 days
**Gate criteria:** Post-mortem complete, evidence archived

### Phase 7: Remediation Tracking (Ongoing)

| Step | Owner | Output |
|------|-------|--------|
| Client remediation tracking | Head of Division | Periodic check-ins, remediation status, verification testing |
| Re-test (if contracted) | Senior Operator | Verify remediation effectiveness, re-test fixed vulnerabilities |
| Final closure | Head of Division | Engagement formally closed, final report amendment if needed |

**Deliverables:** Remediation status reports, re-test results (if applicable)
**Duration:** Per contract (typically 30–90 days post-engagement)

---

## 12. Division Daily Operations

### Daily Rhythm

| Time (MYT, UTC+8) | Activity | Owner |
|---------------------|----------|-------|
| 08:00–09:00 | Dark web monitoring sweep, overnight alert review | Dark Web Analyst |
| 09:00–09:15 | Division stand-up (15 min) — yesterday's progress, today's plan, blockers | All (Head chairs) |
| 09:15–12:00 | Engagement execution / infrastructure work / research | All |
| 12:00–13:00 | Lunch | All |
| 13:00–17:00 | Engagement execution / tool development / detection engineering | All |
| 15:00–15:15 | Afternoon check-in (if active engagement) — status sync, risk check | Operator + Head |
| 17:00–17:30 | Daily log update, evidence organisation, day's work documented | All |
| 17:30–18:00 | End-of-day dark web sweep, alert queue clearance | Dark Web Analyst |

### Weekly Cadence

| Day | Meeting | Duration | Attendees |
|-----|---------|----------|----------|
| Monday | Division operations meeting — pipeline review, engagement status, week's priorities | 30 min | All |
| Tuesday | Intelligence brief — dark web findings, threat landscape update, actor tracking | 30 min | All (Analyst leads) |
| Wednesday | Detection engineering review — new rules, coverage gaps, library status | 30 min | Operator + Detection Eng + Researcher |
| Thursday | Research review — vulnerability research progress, tool development, publications | 30 min | Researcher leads, all attend |
| Friday | Division retrospective — what worked, what didn't, improvements for next week | 30 min | All |

### Monthly Cadence

| Activity | Owner | Output |
|----------|-------|--------|
| Monthly division report to Director | Head of Division | Revenue, engagement status, pipeline, risks, milestones |
| Dark web monitoring report (for clients) | Dark Web Analyst | Monthly intelligence product |
| Detection library audit | Detection Engineer | Rule count, coverage percentage, FP rate, retirements |
| Threat actor profile updates | Dark Web Analyst | Updated profiles, new actors added |
| Skills matrix review | Head of Division | Individual development progress, training needs |
| Infrastructure health check | Senior Operator | C2 infrastructure status, rotation schedule, OPSEC review |

### Engagement vs Non-Engagement Time Allocation

When no active engagement is running, the division focuses on capability building:

| Role | Engagement Time | Non-Engagement Time |
|------|----------------|---------------------|
| Head of Division | 30% engagement mgmt, 70% stakeholder/strategy | Stakeholder engagement, pipeline, national capability, strategy |
| Senior Operator | 80% engagement, 20% capability | Infrastructure improvement, tool development, training, lab exercises |
| Dark Web Analyst | 20% engagement support, 80% continuous monitoring | Source expansion, collection automation, profile depth, reporting quality |
| Detection Engineer | 40% engagement (purple team), 60% capability | Rule library expansion, SIEM engineering, threat hunting, lab improvements |
| Offensive Security Researcher | 20% engagement support, 80% research | Vulnerability research, exploit development, evasion research, publications |

---

## 13. Operational Security (OPSEC) Standards

### Division OPSEC Rules (Non-Negotiable)

1. **No engagement infrastructure used for personal activity** — C2 servers, redirectors, payload hosting are engagement-only. No browsing, no personal projects, no testing from engagement infrastructure.

2. **Infrastructure rotation between engagements** — Fresh domains, new VPS, clean certificates for every engagement. No infrastructure reuse across clients.

3. **Engagement evidence encryption** — All engagement logs, screenshots, captured credentials, and attack artefacts encrypted at rest. Encryption keys managed by Head of Division.

4. **Dark web access isolation** — Dark web collection performed only from designated collection infrastructure. No dark web access from personal devices, corporate network, or engagement infrastructure.

5. **Persona separation** — Collection personas maintained separately from personal identity. No cross-contamination. Persona credentials stored in dedicated password manager.

6. **No client data in research publications** — All publications reviewed by Head of Division before release. No client names, engagement details, or sensitive TTPs disclosed.

7. **C2 traffic encryption** — All C2 traffic encrypted. No plaintext C2 protocols. HTTPS/DNS over HTTPS mandatory.

8. **Evidence retention policy** — Engagement evidence retained per client contract terms. Default: 90 days post-engagement closure. Secure deletion after retention period.

9. **Incident reporting** — Any infrastructure compromise, access loss, or OPSEC failure reported to Head of Division within 1 hour. No exceptions.

10. **Travel OPSEC** — No engagement data on personal devices during travel. Encrypted laptop only. No C2 infrastructure access from untrusted networks.

### Government Engagement Additional Controls

- Security clearance verification for all team members before engagement briefing
- Engagement evidence stored on government-approved infrastructure (or air-gapped if required)
- No foreign nationals on government engagement teams without explicit authorisation
- All reports classified per government classification guidelines
- Post-engagement evidence handled per government retention requirements

---

## 14. Division Governance Framework

### Decision Rights

| Decision | Authority |
|----------|----------|
| Engagement go/no-go (commercial) | Head of Division |
| Engagement go/no-go (government) | Head of Division + Director (co-sign) |
| Engagement pricing | Head of Division (within approved rate card) |
| Engagement pricing (below rate card) | Director approval required |
| New tool purchase (< RM 5,000) | Head of Division |
| New tool purchase (> RM 5,000) | Director approval |
| Hiring decision | Head of Division + Director + HR |
| Research publication (pre-release review) | Head of Division |
| Research publication (sensitive/government-adjacent) | Director review |
| Infrastructure provisioning | Senior Operator (within approved budget) |
| ROE modification during engagement | Head of Division + Client (documented) |
| Emergency engagement stop | Any team member (safety first, document later) |

### Escalation Paths

| Situation | Escalate To | Timeline |
|------------|-------------|----------|
| OPSEC failure (infrastructure compromise) | Head of Division → Director | Within 1 hour |
| Legal issue during engagement | Head of Division → Legal Counsel → Director | Within 2 hours |
| Client requests scope expansion | Head of Division (document, price, re-authorize) | Same day |
| Emergency stop condition triggered | Head of Division → Director + Client | Immediate |
| Personnel issue (team conflict, performance) | Head of Division → HR if needed | Within 24 hours |
| Security clearance concern | Head of Division → Director | Immediate |
| Media inquiry about division or engagements | Director only | Immediate, no team member responds |

### Quality Standards

| Standard | Requirement |
|----------|------------|
| Engagement reports | Peer-reviewed by Head of Division before delivery |
| Detection rules | Tested against recorded telemetry, false positive rate < 5% |
| Intelligence products | Source-verified, confidence-tagged, reviewed by Head |
| Research publications | OPSEC-reviewed, no client data, factual accuracy verified |
| Client communication | Professional, documented, timely (24-hour response SLA) |
| Evidence handling | Chain of custody maintained, encrypted, access-controlled |

---

## 15. Onboarding Plan (First 90 Days for New Division Hires)

### Week 1: Orientation

- Company orientation, cybersecurity practice overview, division mission briefing (Head of Division)
- Security clearance initiation (if required for government engagements)
- Access provisioning: division infrastructure, lab, tools, documentation
- Reading assignment: VORON-C2 architecture document, division SOPs, OPSEC standards
- Meet the team: 1-on-1 with each division member

### Weeks 2–4: Technical Onboarding

| Role | Onboarding Focus |
|------|------------------|
| Senior Operator | VORON-C2 infrastructure deployment (lab), first beacon check-in, payload testing against lab EDR |
| Dark Web Analyst | Collection infrastructure setup, source identification, first monitoring sweep, first intelligence brief draft |
| Detection Engineer | Wazuh + ELK deployment in lab, first rules written, first purple team exercise (internal, with Operator) |
| Offensive Security Researcher | Lab setup, first vulnerability research target selected, first BOF development, first evasion test |
| Head of Division | Stakeholder mapping (NACSA, JDN, CNII), first engagement scoping, division operations rhythm established |

### Weeks 5–8: Integration

- Participate in first internal capability exercise (full attack chain, internal target)
- Purple team exercise #1 (internal) — Operator attacks, Detection Engineer defends, Researcher provides custom tools
- Dark Web Analyst produces first pre-engagement intelligence package (hypothetical engagement)
- Researcher presents first research finding at weekly research review
- All team members complete OPSEC certification (internal, Head of Division administered)

### Weeks 9–12: First Engagement

- First client engagement scoped and scheduled
- Team executes first engagement under Head of Division supervision
- Full engagement lifecycle (Phases 1–6) completed
- Post-engagement review conducted, lessons documented
- 90-day performance review with Head of Division

---

## 16. Tooling & Infrastructure Budget

### Year 1 Infrastructure Costs

| Item | Purpose | Cost (RM) | Frequency |
|------|---------|-----------|----------|
| VPS fleet (8–12 servers) | C2 servers, redirectors, payload hosting, dark web collection | 300–500/month | Monthly |
| Domain names (20–30) | C2 redirector domains, phishing infrastructure | 200–300/year | Annual |
| Cloud storage | Evidence archival, encrypted backups | 100–200/month | Monthly |
| EDR lab licenses | 2–3 commercial EDR products for evasion testing | 2,000–4,000/year | Annual |
| Exploit dev lab hardware | Isolated testing environment (if physical) | 5,000–8,000 (one-time) | One-time |
| Dark web access tools | VPN, residential proxies, forum access fees | 200–500/month | Monthly |
| Threat intel platform | MISP (self-hosted, free) or OpenCTI (self-hosted, free) | 0 | — |
| Development tools | GitHub, CI/CD, testing tools | 0–200/month | Monthly |
| Conference & training | Per role training budget | 6,000–10,000/person | Annual |
| **Total Year 1** | | **RM 30,000–50,000** | |

### Free / Open-Source Stack (RM 0 Licensing)

| Tool | Function | Cost |
|-----|----------|------|
| Mythic | C2 framework | Free (self-hosted) |
| Sliver | C2 framework | Free (self-hosted) |
| Havoc | C2 framework | Free (self-hosted) |
| AdaptixC2 | C2 framework | Free (self-hosted) |
| Wazuh | SIEM | Free (self-hosted) |
| Elasticsearch + Kibana | Log storage & analytics | Free (self-hosted, basic tier) |
| MISP | Threat intelligence platform | Free (self-hosted) |
| Mr.Holmes | OSINT tool | Free (already deployed) |
| Ghidra | Reverse engineering | Free |
| radare2 | Reverse engineering | Free |
| Sigma | Detection rule format | Free (open standard) |
| MITRE ATT&CK | Framework | Free (open framework) |
| CyberStrike | AI-augmented offensive ops | Free (open-source) |
| Docker | Container platform | Free (community edition) |

---

**Document end.**

*This document is designed for management committee presentation and HR firm distribution. It wraps organisational structure, capability architecture, revenue model, operational SOPs, governance, and onboarding around the existing VORON-C2 technical work. The technical architecture is already complete — this is the institutional shell that makes it a division. Individual job descriptions are available as separate files for HR firm distribution.*
