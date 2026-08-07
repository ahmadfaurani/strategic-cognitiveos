# VORON-C2 — Sovereign Open-Source C2 Infrastructure Architecture

**Document Status:** DRAFT v0.1  
**Date:** 2026-08-06  
**Authority:** DAF  
**Classification:** INTERNAL — RESTRICTED  
**Operational Requirement:** Full open-source C2 stack as national capability, future GovSec integration

---

## 1. Strategic Rationale

### Why a Sovereign C2 Stack?

Malaysia's cybersecurity capability landscape depends on foreign-owned or commercial C2 platforms (Cobalt Strike licenses, third-party red team vendors). This creates three structural vulnerabilities:

1. **Dependency risk** — Foreign vendors can revoke licenses, restrict features, or deny access based on geopolitical pressure
2. **Capability gap** — No indigenous red team / adversarial emulation capability for government-wide exercises
3. **Detection deficit** — Malaysian SOC teams cannot train against real C2 traffic without importing foreign operators

A sovereign, open-source C2 stack addresses all three. It gives Aras Integrasi (and by extension, GovSec) an independent capability to:
- Conduct authorized red team engagements across government infrastructure
- Generate real attack telemetry for SOC detection engineering
- Emulate adversary TTPs observed in Malaysian threat landscape (Akira, BumbleBee, etc.)
- Build national cyber exercise infrastructure (national-level red vs blue)

### Design Principles

| Principle | Meaning |
|-----------|---------|
| **Sovereign** | All infrastructure self-hosted on Malaysian-controlled systems. No foreign cloud dependency for C2 core. |
| **Open-source** | Every component is FOSS. No commercial licensing. Full source code review capability. |
| **Modular** | C2 frameworks as swappable plugins. Add/remove frameworks without rearchitecting. |
| **Auditable** | Every operator action logged. Every engagement traceable. Built-in accountability. |
| **Defensive-first** | The stack exists to serve detection engineering and red team validation — not offensive operations. |
| **GovSec-ready** | Architecture designed for future integration with GovSec TIP and national SOC infrastructure. |

---

## 2. Architecture Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                    VORON-C2 INFRASTRUCTURE                        │
│                                                                  │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐              │
│  │  C2 CORE    │  │  REDIRECTORS │  │  DNS INFRA   │              │
│  │  (Layer 1)  │  │  (Layer 2)   │  │  (Layer 2)   │              │
│  │             │  │              │  │              │              │
│  │  Mythic     │  │  Apache/Nginx│  │  Authoritative│              │
│  │  Sliver     │  │  reverse     │  │  DNS servers  │              │
│  │  Havoc      │  │  proxies     │  │  Domain       │              │
│  │  AdaptixC2  │  │              │  │  management   │              │
│  └──────┬──────┘  └──────┬───────┘  └──────┬───────┘              │
│         │                │                  │                      │
│         └────────────────┴──────────────────┘                      │
│                          │                                       │
│  ┌───────────────────────────────────────────┐                    │
│  │           OPERATIONS LAYER (Layer 3)       │                    │
│  │                                           │                    │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐   │                    │
│  │  │ Payload  │ │ Operator │ │ Engage-  │   │                    │
│  │  │ Dev Lab  │ │ Console  │ │ ment Log │   │                    │
│  │  └──────────┘ └──────────┘ └──────────┘   │                    │
│  └───────────────────────────────────────────┘                    │
│                          │                                       │
│  ┌───────────────────────────────────────────┐                    │
│  │       DETECTION ENGINEERING (Layer 4)      │                    │
│  │                                           │                    │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐   │                    │
│  │  │  Wazuh   │ │  ELK     │ │ ATT&CK   │   │                    │
│  │  │  (SIEM)  │ │  Stack   │ │ Mapper   │   │                    │
│  │  └──────────┘ └──────────┘ └──────────┘   │                    │
│  └───────────────────────────────────────────┘                    │
│                          │                                       │
│  ┌───────────────────────────────────────────┐                    │
│  │     GOVSEC INTEGRATION PATH (Future)       │                    │
│  │                                           │                    │
│  │  GovSec TIP ← → VORON-C2 API ← → National  │                    │
│  │  Threat Intel   Engagements    SOC Grid    │                    │
│  └───────────────────────────────────────────┘                    │
└─────────────────────────────────────────────────────────────────┘
```

---

## 3. Layer 1 — C2 Core (Framework Selection)

### Framework Matrix

| Framework | Language | License | Maturity | Strength | Role in Stack |
|-----------|----------|---------|----------|----------|---------------|
| **Mythic** | Go/Python/Docker | BSD 3-Clause | High | Multi-agent, extensible, web UI, API-first | **Primary platform** — team operations, multi-agent engagements, API automation |
| **Sliver** | Go | BSD 3-Clause | High | Mature, reliable, per-binary encryption, WG support | **Rapid deployment** — quick engagements, training, single-operator |
| **Havoc** | C/C++ | MIT | Medium | Stealthy, modern evasion, C++ agents | **High-stealth tier** — advanced engagements requiring evasion |
| **AdaptixC2** | Go/C++ | MIT | Emerging | Modular plugin architecture, BOF support, OpSec features | **Adversary emulation** — replicate real threat actor TTPs (Akira, BumbleBee) |

### Why Four Frameworks?

Each serves a distinct operational purpose. A national capability stack needs depth:

- **Mythic** = the operations platform (multi-operator, multi-agent, API-driven)
- **Sliver** = the workhorse (reliable, well-documented, easy to train on)
- **Havoc** = the stealth option (when engagements require high evasion)
- **AdaptixC2** = the adversary emulation engine (replicates what we're seeing in the wild)

### Mythic — Deep Dive (Primary Platform)

**Architecture:**
- Docker-based — each component (server, agent, C2 profile) runs as a container
- Web UI — collaborative, browser-based operator console
- API-first — REST/WebSocket API for automation and integration
- Multi-agent — supports Apollo (Windows), Poseidon (Linux), Athena (Windows .NET), and community agents
- C2 Profiles — HTTP, WebSocket, SMB, TCP, custom profiles as plugins

**Why it's the primary:**
- Best for team operations (multiplayer, role-based access)
- Most extensible (agents and C2 profiles are Docker plugins — swap without touching core)
- API enables GovSec integration and automation
- Docker architecture = easy sovereign deployment
- Active community, ongoing development

**Deployment:**
```
mythic-server/
├── docker-compose.yml
├── mythic-cli/
├── Payload_Type/
│   ├── apollo/          # Windows agent
│   ├── poseidon/        # Linux agent
│   └── athena/          # .NET agent
├── C2_Profiles/
│   ├── http/
│   ├── websocket/
│   └── smb/
└── Documentation/
```

### Sliver — Deep Dive (Workhorse)

**Key features:**
- Per-binary asymmetric encryption (each implant has unique keypair)
- C2 protocols: mTLS, WireGuard, HTTP(S), DNS
- Dynamic compilation — implants compiled on-demand with unique configs
- Implant formats: EXE, DLL, shellcode
- BOF support
- WireGuard C2 — encrypted, fast, hard to detect (uses UDP, blends with VPN traffic)

**Why it's the workhorse:**
- Most mature open-source C2
- Best documentation — ideal for training new operators
- BishopFox (reputable security company) maintains it
- Reliable across diverse environments
- Sliver GUI + CLI — flexible operator experience

### Havoc — Deep Dive (Stealth Tier)

**Key features:**
- C/C++ agents — smaller footprint, fewer .NET artifacts
- Python extender system — runtime extensibility
- Sleep obfuscation — ekko/zilean sleep techniques
- Process injection modules
- Debug/Release builds for engagement flexibility

**Why it's the stealth option:**
- C/C++ agents avoid .NET/PowerShell detection surface
- Sleep obfuscation evades memory scanning
- More modern evasion features out of the box
- Used by real threat actors (WIRTE/Hamas-linked) — proves stealth value

**Caveat:** Less actively maintained than Sliver/Mythic. Requires more operational testing before deployment in sensitive engagements.

### AdaptixC2 — Deep Dive (Adversary Emulation)

**Why include it:**
- We just saw it used in a real Akira ransomware deployment (DFIR Report)
- Modular plugin architecture = easy to customize for specific adversary emulation scenarios
- BOF & Async BOF support
- Built-in OpSec features (KillDate, WorkingTime)
- Weak default config (RC4 key in payload) = good for teaching detection engineering

**Role in stack:**
- Adversary emulation lab — replicate real intrusion chains for SOC training
- Detection engineering — generate telemetry matching real-world TTPs
- NOT for live engagements initially — too new, reputation concerns

---

## 4. Layer 2 — Infrastructure Components

### 4.1 Redirector Infrastructure

**Purpose:** Obsfuscate C2 server location. Traffic flows through redirectors before hitting C2 core.

**Design:**
```
Target ← → Redirector 1 ← → C2 Core
        ↘ Redirector 2 ↗
        ↘ Redirector 3 ↗
```

**Implementation:**
- Apache/Nginx reverse proxy with mod_rewrite / proxy_pass
- Each redirector on separate VPS (different providers, different geographies — but all Malaysian-controlled or neutral)
- Domain fronting via legitimate CDN (where authorized)
- Auto-deploy scripts for rapid redirector spin-up/teardown
- Redirector logs shipped to central logging (for engagement audit trail)

**Redirection rules (Apache example):**
```apache
<VirtualHost *:443>
    ServerName legitimate-looking-domain.my
    SSLEngine on
    SSLCertificateFile /etc/ssl/cert.pem
    SSLCertificateKeyFile /etc/ssl/key.pem
    
    # Only forward requests matching C2 profile
    RewriteEngine On
    RewriteCond %{REQUEST_URI} ^/api/v1/update [OR]
    RewriteCond %{HTTP_USER_AGENT} ^Mozilla/5.0.*Custom$
    RewriteRule ^(.*)$ https://c2-core.internal:8443$1 [P]
    
    # Everything else → legitimate-looking site
    ProxyPass / http://127.0.0.1:8080/
    ProxyPassReverse / http://127.0.0.1:8080/
</VirtualHost>
```

### 4.2 DNS Infrastructure

**Purpose:** Support DNS beaconing, domain management, infrastructure resilience.

**Components:**
- Authoritative DNS servers (BIND9/PowerDNS) — self-hosted
- Domain registration — Malaysian .my domains + international domains for redirectors
- DNS categorization management — ensure domains don't get blacklisted
- DGA (Domain Generation Algorithm) capability — for adversary emulation (research/lab use only)

**DNS beaconing support:**
- Sliver DNS C2 — text/TXT/A record beaconing
- Mythic DNS C2 profile — configurable DNS beacon channels
- AdaptixC2 DNS/DoH beacon — DNS-over-HTTPS for encrypted DNS channels

### 4.3 Hosting Strategy

**Sovereign hosting tiers:**

| Tier | Location | Purpose | Security |
|------|----------|---------|----------|
| Tier 0 | On-premise (air-gapped lab) | C2 core, payload dev, sensitive engagements | Physical isolation, no internet |
| Tier 1 | Malaysian datacenter (controlled) | Staging, training, redirector management | VPC isolation, VPN access only |
| Tier 2 | Malaysian VPS providers | Redirectors, DNS infrastructure | Separate IPs, rapid deploy/teardown |

**No foreign cloud for C2 core.** Redirectors may use foreign VPS when operationally necessary, but C2 command infrastructure stays sovereign.

---

## 5. Layer 3 — Operations Layer

### 5.1 Payload Development Lab

**Environment:**
- Isolated network segment (VLAN or air-gapped)
- Compilation environment: Go, C/C++, C#, Rust, Python
- Testing environment: Windows/Linux VMs with Sysmon + EDR for self-detection
- Payload repository: version-controlled, audited builds

**Capabilities:**
- Implant compilation (Sliver, Mythic agents, Havoc, AdaptixC2)
- Payload obfuscation testing (AMSI bypass, ETW patch, sleep techniques)
- YARA rule testing (ensure payloads don't trip own detection rules)
- Staged payload development → testing → validation pipeline

### 5.2 Operator Console

**Primary:** Mythic Web UI (browser-based, multi-operator)
**Secondary:** Sliver CLI/GUI (single-operator, rapid deployment)
**Tertiary:** Havoc UI (stealth engagements)
**Quaternary:** AdaptixC2 Qt client (adversary emulation lab)

**Operator authentication:**
- Certificate-based operator identity (no shared credentials)
- Role-based access: Lead Operator, Operator, Observer
- All operator actions logged to immutable audit trail
- Session recording for post-engagement review

### 5.3 Engagement Logging

**Every engagement produces:**
- Operator action log (commands executed, by whom, when)
- Agent/beacon log (C2 communications, tasking, results)
- Network capture (redirector traffic — for validation)
- MITRE ATT&CK technique mapping (what techniques were used)
- Engagement timeline (chronological event log)

**Storage:** Encrypted at rest, access-controlled, retention per engagement agreement. Logs are the property of the client, not the operator.

---

## 6. Layer 4 — Detection Engineering (Purple Team)

This is where the C2 stack pays for itself. Every engagement generates real attack telemetry that feeds detection engineering.

### 6.1 SIEM Stack

| Component | Role |
|-----------|------|
| **Wazuh** | Open-source SIEM/XDR — agent-based endpoint detection, log collection, rule engine |
| **Elasticsearch/Kibana** | Log storage, search, visualization — SIEM backend |
| **Sigma rules** | Generic detection rule format — portable, shareable |
| **YARA** | File-based detection — payload signatures, malware family identification |

### 6.2 Purple Team Workflow

```
1. Red Team deploys C2 agent against lab/client environment
2. SIEM/EDR captures telemetry (process creation, network, file, registry)
3. Detection engineer reviews telemetry → writes Sigma/YARA rules
4. Rules tested against C2 traffic (does it catch the beacon?)
5. Rules refined → false positive testing against legitimate traffic
6. Validated rules deployed to client SIEM/EDR
7. Red Team modifies TTPs → detection engineer adapts rules
8. Cycle repeats (continuous improvement)
```

### 6.3 ATT&CK Mapping

Every C2 capability maps to MITRE ATT&CK techniques:

| C2 Activity | ATT&CK Technique |
|-------------|-----------------|
| HTTP beacon | T1071.001 (Web Protocols) |
| DNS beacon | T1071.004 (DNS) |
| SMB named pipe | T1570 (Lateral Tool Transfer) |
| Process injection | T1055 (Process Injection) |
| BOF execution | T1055 (Process Injection) |
| WMI execution | T1047 (Windows Management Instrumentation) |
| Sleep obfuscation | T1497.003 (Time Based Evasion) |
| DLL side-loading | T1574.002 (DLL Side-Loading) |
| SOCKS proxy | T1090.003 (Proxy Chains) |
| KillDate/WorkingTime | T1497 (Virtualization/Sandbox Evasion) |

This mapping provides:
- Engagement coverage reporting (which ATT&CK techniques were tested)
- Detection coverage reporting (which techniques have working detection rules)
- Gap analysis (techniques tested but not detected = detection gap)
- Executive reporting (visual ATT&CK matrix coverage)

---

## 7. Governance & Legal Framework

### 7.1 Authorization Matrix

| Activity | Required Authorization |
|----------|----------------------|
| Lab testing (internal) | DAF approval |
| Client red team engagement | Written client authorization + Rules of Engagement (RoE) |
| Government engagement | Contracting agency authorization + RoE + Legal clearance |
| Adversary emulation (lab) | DAF approval + documented scenario |

### 7.2 Rules of Engagement (RoE) Template

Every engagement must have a signed RoE specifying:
- Authorized targets (IP ranges, systems, accounts)
- Prohibited actions (data destruction, DoS, accessing non-target systems)
- Communication plan (emergency contacts, notification protocol)
- Engagement window (start/end dates, working hours)
- Data handling (what data is collected, how stored, how destroyed post-engagement)
- Legal basis (Computer Crimes Act 1997, client contract terms)

### 7.3 Audit & Accountability

- All operator sessions recorded
- All C2 commands logged with operator ID, timestamp, target
- Post-engagement audit review (mandatory)
- Segregation of duties: red team operator ≠ audit reviewer
- Annual external audit of C2 infrastructure security

### 7.4 Legal Compliance

- **Computer Crimes Act 1997** — unauthorized access is a crime. Written authorization is mandatory.
- **PDPA 2010** — personal data encountered during engagements must be handled per law
- **Client contracts** — engagement scope defined by contract terms
- **Evidence law** — engagement logs may be used in legal proceedings; chain of custody required

---

## 8. GovSec Integration Path (Future)

### Phase 1: Standalone (Now)
- VORON-C2 operates as standalone Aras Integrasi capability
- Internal training, lab exercises, pilot client engagements

### Phase 2: GovSec TIP Integration
- C2 engagement data feeds into GovSec Threat Intelligence Platform
- Red team findings → threat intel → detection rules for national SOC
- ATT&CK coverage data shared with GovSec dashboard

### Phase 3: National Exercise Infrastructure
- VORON-C2 serves as red team platform for national cyber exercises
- Integrates with national SOC grid for real-time detection validation
- Provides red team capability for CNI/NACSA exercises

### Phase 4: Sovereign Capability Export
- Offer red team / purple team services to ASEAN partners
- Become regional hub for open-source C2 capability development
- Training and certification program for Malaysian red team operators

---

## 9. Development Roadmap

### Phase 1: Foundation (Months 1-3)

**Objective:** Stand up core infrastructure, train operators, first lab exercise

- [ ] Provision Tier 0 lab environment (air-gapped network, VMs, compilation environment)
- [ ] Deploy Mythic server (Docker-based, internal network only)
- [ ] Deploy Sliver server (standalone, for training)
- [ ] Configure Wazuh + ELK stack for detection engineering
- [ ] Develop operator training curriculum (Mythic + Sliver basics)
- [ ] First internal purple team exercise (lab environment)
- [ ] Develop RoE templates and governance documentation

**Deliverables:**
- Operational Mythic + Sliver deployment
- 2-3 trained operators
- First detection rule set validated against C2 traffic
- Governance framework document

### Phase 2: Capability Expansion (Months 3-6)

**Objective:** Add stealth and emulation tiers, redirector infrastructure, first client engagement

- [ ] Deploy Havoc framework in lab
- [ ] Deploy AdaptixC2 for adversary emulation lab
- [ ] Build redirector deployment automation (Apache/Nginx auto-config scripts)
- [ ] Set up DNS infrastructure (authoritative DNS, domain management)
- [ ] Develop payload testing pipeline (compile → test → validate → deploy)
- [ ] First authorized client engagement (pilot)
- [ ] Sigma rule library development (based on engagement telemetry)

**Deliverables:**
- Full 4-framework C2 stack operational
- Redirector infrastructure with rapid deploy/teardown
- Sigma rule library (initial 50+ rules)
- First client engagement report
- ATT&CK coverage matrix from pilot engagement

### Phase 3: Operationalization (Months 6-12)

**Objective:** Production-ready capability, team built out, GovSec integration prep

- [ ] Hire/train dedicated red team operators (2-3 FTE)
- [ ] Standardize engagement methodology (SOPs for each engagement type)
- [ ] Develop client-facing reporting templates (executive + technical)
- [ ] Build GovSec TIP API integration prototype
- [ ] Conduct first government-sector engagement (if authorized)
- [ ] National cyber exercise participation (red team role)
- [ ] Develop ASEAN engagement capability (regional service offering)

**Deliverables:**
- Production team (2-3 operators)
- Standardized engagement methodology
- GovSec TIP integration prototype
- Government engagement (if authorized)
- National exercise participation
- Service offering documentation

### Phase 4: GovSec Integration (Months 12-18)

**Objective:** Full GovSec integration, national capability

- [ ] GovSec TIP API integration (bi-directional)
- [ ] National SOC grid integration (detection rule distribution)
- [ ] National cyber exercise infrastructure
- [ ] Operator certification program
- [ ] Regional (ASEAN) engagement capability
- [ ] Research & development (custom agents, evasion research, detection research)

**Deliverables:**
- GovSec-integrated C2 capability
- National exercise infrastructure
- Certified operator program
- Regional service offering

---

## 10. Technology Stack Summary

| Layer | Component | Technology | License |
|-------|-----------|------------|---------|
| C2 Core | Primary platform | Mythic | BSD 3-Clause |
| C2 Core | Workhorse | Sliver | BSD 3-Clause |
| C2 Core | Stealth tier | Havoc | MIT |
| C2 Core | Adversary emulation | AdaptixC2 | MIT |
| Redirectors | Reverse proxy | Apache/Nginx | Apache 2.0 / BSD |
| DNS | Authoritative DNS | PowerDNS / BIND9 | GPL / MPL |
| Detection | SIEM/XDR | Wazuh | GPLv2 |
| Detection | Log backend | Elasticsearch + Kibana | Elastic License (free tier) |
| Detection | Rule format | Sigma | MIT |
| Detection | File signatures | YARA | BSD |
| Payload Dev | Compilation | Go, GCC, MinGW, .NET | Open |
| Lab | Virtualization | Proxmox / KVM / VirtualBox | GPLv3 / GPLv2 / GPL |
| Comms | Operator VPN | WireGuard | GPLv2 |
| Comms | Operator access | OpenVPN | GPLv2 |
| Monitoring | Infrastructure monitoring | Prometheus + Grafana | Apache 2.0 |
| Audit | Log management | rsyslog + Elasticsearch | GPLv3 / Elastic |

**Total licensing cost: $0**

---

## 11. Risk Register

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|-----------|
| Framework abandonment (maintainer stops) | Medium | High | Use 4 frameworks — no single point of dependency. Fork capability if needed. |
| Operator skill gap | High | High | Structured training program. Start with Sliver (easiest to learn). Partner with experienced operators initially. |
| Legal exposure | Low | Critical | Written authorization mandatory. Legal review of RoE for every engagement. |
| Infrastructure compromise | Medium | Critical | Air-gapped Tier 0. VPN-only access. Certificate-based operator auth. Regular security audits. |
| Detection by client EDR (red team caught too early) | Medium | Medium | Proper payload testing against common EDR before engagement. EDR evasion research program. |
| Scope creep (GovSec integration delays) | Medium | Medium | Phased approach. Standalone capability first, integration later. |

---

## 12. Next Actions

1. **Decision required:** Confirm framework selection (Mythic primary, Sliver workhorse, Havoc stealth, AdaptixC2 emulation)
2. **Resource allocation:** Identify lab hardware (servers for Tier 0, VPS budget for redirectors)
3. **Team identification:** Who will be the first operators? Internal team or hire?
4. **Legal framework:** Engage legal counsel for RoE template and authorization framework
5. **Phase 1 kickoff:** Provision lab environment, deploy Mythic + Sliver

---

*This document is a living architecture. It evolves as the capability develops and operational experience informs design decisions.*
