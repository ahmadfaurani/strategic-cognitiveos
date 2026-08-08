# JOB DESCRIPTION — Senior Red Team Operator

**Position:** Senior Red Team Operator  
**Division:** Red Team Division, Cyber Security Practice  
**Company:** Aras Integrasi Sdn Bhd  
**Reports to:** Head of Red Team Division  
**Location:** Kuala Lumpur, Malaysia (hybrid)  
**Employment type:** Full-time, permanent  
**Date:** August 2026

---

## Position Summary

The Senior Red Team Operator is the primary execution role in the Red Team Division. You run the C2 stack, deliver attack chains from initial access through objective achievement, and produce the raw offensive output that the detection engineer converts into defensive capability. You are the tip of the spear.

This role operates VORON-C2 — a sovereign, open-source C2 infrastructure built on four frameworks (Mythic, Sliver, Havoc, AdaptixC2). You will deploy, manage, and operate this stack across government, defence, critical infrastructure, and commercial engagements.

This is a hands-on technical role. You will write payloads, configure C2 infrastructure, execute phishing campaigns, exploit vulnerabilities, move laterally, harvest credentials, and document every step. You will also mentor interns and contribute to the division's tool library.

---

## Key Responsibilities

### C2 Infrastructure Operations (25%)

- Deploy, configure, and maintain VORON-C2 infrastructure across engagements:
  - **Mythic** — primary C2 platform, Docker-based, custom agent development
  - **Sliver** — workhorse implant, Go-based, cross-platform compilation
  - **Havoc** — stealth operations, C/C++ agents, evasion-focused
  - **AdaptixC2** — adversary emulation, BOF support, multi-agent operations
- Manage redirector infrastructure (Apache/Nginx), DNS configurations, domain fronting
- Maintain C2 OPSEC — beacon configurations, sleep/jitter tuning, kill dates, working hours
- Rotate infrastructure between engagements (fresh domains, new VPS, clean certificates)
- Monitor C2 infrastructure health and operational security (detection by target blue team)

### Engagement Execution (35%)

- Execute red team engagements end-to-end following division SOPs:
  1. **Reconnaissance** — internal network mapping, domain enumeration, asset discovery
  2. **Initial Access** — phishing campaigns, exploit delivery, supply chain attacks, physical access (where authorised)
  3. **Execution** — payload deployment, DLL side-loading, process injection, living-off-the-land
  4. **Persistence** — scheduled tasks, services, registry run keys, WMI subscriptions, account creation
  5. **Privilege Escalation** — token impersonation, UAC bypass, kernel exploits, AD exploitation
  6. **Defense Evasion** — AV/EDR bypass, obfuscation, LOLBins, BYOVD, timestomping
  7. **Credential Access** — LSASS dumping, NTDS extraction, DPAPI, Kerberoasting, AS-REP roasting
  8. **Lateral Movement** — Pass-the-Hash, Pass-the-Ticket, WMI, PsExec, RDP, SMB relay
  9. **Collection** — data staging, credential harvesting, sensitive file identification
  10. **Exfiltration** — covert channels, DNS exfiltration, HTTPS tunnelling (simulated)
  11. **Impact** — ransomware simulation, data destruction simulation (controlled, authorised)
- Produce detailed engagement logs — timestamps, commands, outputs, screenshots, network captures
- Maintain chain of custody for all engagement evidence
- Adapt TTPs based on pre-engagement intelligence (dark web analyst input)
- Emulate specific threat actors when requested (Akira, BumbleBee, Fog, etc.)

### Payload Development (15%)

- Develop custom payloads for engagements:
  - Phishing templates (email, landing pages, attachments)
  - Macro-enabled documents, LNK files, ISO/IMG containers
  - DLL loaders, shellcode runners, process injection modules
  - Custom BOFs (Beacon Object Files) for AdaptixC2/Mythic
  - PowerShell/C#/.NET assemblies for post-exploitation
  - Go-based Sliver extensions and Mythic agents
- Test payloads against commercial EDR/AV products in the division's lab
- Develop evasion techniques — signature bypass, behavioural evasion, AMSI bypass, ETW patching

### Purple Team Operations (10%)

- Work alongside Detection Engineer during purple team exercises:
  - Execute TTPs while Detection Engineer monitors for alerts
  - Validate detection coverage in real-time
  - Identify detection gaps and provide TTP details for rule writing
  - Tune TTPs to test edge cases in detection logic
- Contribute to detection rule library with TTP metadata and test data

### Tool Development & Maintenance (10%)

- Maintain and extend division's internal tool library:
  - C2 modules, agents, and extensions
  - Post-exploitation scripts (Python, Go, PowerShell, C#)
  - Automation scripts for repetitive engagement tasks
  - Infrastructure deployment scripts (Ansible, Docker Compose)
- Contribute to open-source security tools where strategically valuable (division visibility)
- Document all tools with usage instructions, requirements, and examples

### Mentorship & Knowledge Transfer (5%)

- Supervise skunkworks interns during technical phases (Phase 2: The Build)
- Pair with interns on infrastructure deployment tasks
- Review intern technical work and provide feedback
- Deliver internal technical training sessions (brown bag, hands-on labs)
- Maintain engagement runbooks for knowledge transfer

---

## Requirements

### Essential Qualifications

- Malaysian citizen or PR (national capability preference; security clearance may be required for government engagements)
- Bachelor's degree in Computer Science, Information Security, or equivalent demonstrated experience
- 5–8 years cybersecurity experience
- 3+ years hands-on red team, penetration testing, or offensive security operations
- Demonstrated experience with C2 frameworks in real engagements (not just lab environments)

### Essential Technical Skills

**C2 Frameworks:**
- Hands-on operational experience with at least 2 of: Cobalt Strike, Sliver, Mythic, Havoc, AdaptixC2
- Understanding of C2 architecture — beacons, listeners, redirectors, DNS infrastructure
- Agent deployment, configuration, and management across Windows/Linux environments

**Attack Chain Execution:**
- Active Directory exploitation (BloodHound, PowerView, Rubeus, SharpHound)
- Windows internals — process injection, token manipulation, UAC bypass
- Network protocols — SMB, Kerberos, NTLM, LDAP, WMI
- Lateral movement techniques across Windows and Linux environments
- Credential theft and manipulation (LSASS, NTDS, DPAPI, credential dumping)

**Payload Development:**
- Proficient in Python and PowerShell for offensive scripting
- Understanding of C/C++ for shellcode and BOF development
- .NET/C# for post-exploitation assemblies (SharpTools, Rubeus, etc.)
- Assembly (x86/x64) understanding for exploit development
- Experience with macro, LNK, ISO payload delivery mechanisms

**Infrastructure:**
- Docker and Docker Compose for C2 deployment
- Linux server administration (Ubuntu/Debian)
- Apache/Nginx configuration for redirectors
- DNS configuration and management
- Basic cloud (AWS/Azure/GCP) for VPS provisioning

**OPSEC:**
- Understanding of operational security in offensive operations
- EDR/AV evasion techniques (AMSI bypass, ETW patching, direct syscalls, unhooking)
- Network OPSEC — traffic encryption, domain fronting, DNS tunnelling
- Infrastructure rotation and hygiene practices

### Essential Certifications (one or more)

- OSCP (Offensive Security Certified Professional)
- OSEP (Offensive Security Experienced Penetration Tester)
- CRTO (Certified Red Team Operator)
- PNPT (Practical Network Penetration Tester) + demonstrated experience
- Or equivalent demonstrated capability through engagement portfolio

### Preferred

- OSED (Offensive Security Exploit Developer) or OSEE
- CRTO-II
- Experience emulating specific threat actors (Akira, Conti, FIN7, etc.)
- Published security research or tools (GitHub, blog, conference)
- Experience with national cyber exercises
- Active CTF participation (national or international)

### Language

- English (fluent — required for technical work)
- Bahasa Malaysia (conversational minimum — preferred for government engagement)

---

## What You'll Be Working With

### Daily Tools

| Category | Tools |
|----------|-------|
| C2 | Mythic, Sliver, Havoc, AdaptixC2 |
| Recon | Nmap, BloodHound, SharpHound, CrackMapExec, NetExec |
| Exploitation | Metasploit, Empire, custom payloads |
| Post-Exploitation | Rubeus, SharpTools, Mimikatz, lsassy, Impacket |
| Payload Dev | Python, Go, C/C++, C#/.NET, PowerShell, NASM |
| Infrastructure | Docker, Ansible, Apache/Nginx, DNS, VPS fleet |
| Lab | Isolated testing environment with commercial EDR/AV for payload testing |
| OS | Kali Linux, Windows 10/11, Windows Server, Ubuntu Server |

### Engagement Workflow

```
1. Intake — Head of Division scopes engagement, provides ROE and objectives
2. Intelligence — Dark Web Analyst provides pre-engagement intelligence package
3. Planning — You design attack plan, select TTPs, prepare infrastructure
4. Deployment — Stand up C2 infrastructure, redirectors, payload hosting
5. Execution — Run attack chain per engagement plan, adapt as needed
6. Detection — Detection Engineer monitors for your TTPs (purple team)
7. Reporting — You provide engagement logs, timeline, technical findings
8. Review — Post-engagement review, lessons learned, detection gaps
```

---

## Performance Expectations

### First 90 Days

- VORON-C2 infrastructure deployed: Mythic + Sliver operational with redirectors
- First internal capability exercise completed (internal target, full attack chain)
- 10+ custom payloads developed and tested against lab EDR
- Detection rules contributed to division library (working with Detection Engineer)

### Year 1

- 4–6 red team engagements delivered as primary operator
- VORON-C2 full stack operational (all 4 frameworks)
- 20+ custom tools/payloads in division library
- 50+ detection rules validated through purple team exercises
- Skunkworks Cohort 1 technical phase supervised

---

## Compensation

| Component | Range |
|-----------|-------|
| Monthly salary | RM 8,000 – RM 12,000 |
| Annual bonus | Performance-linked, up to 2 months |
| Benefits | EPF, SOCSO, medical, dental, optical |
| Training budget | RM 8,000/year (certifications, conferences) |
| Conference attendance | Minimum 1 international + 2 local per year |

---

## Why This Role

You won't be running generic pentest checklists. You'll be operating a sovereign C2 stack with four frameworks, emulating real threat actors observed in the Malaysian threat landscape, and producing attack telemetry that directly feeds national detection engineering capability. The division is building something that doesn't exist in Malaysia yet — indigenous offensive security capacity — and you'll be the person at the keyboard.

---

**To apply:** Send CV, cover letter, and technical portfolio (GitHub, write-ups, CVEs, tool contributions, or redacted engagement summaries) to [HR contact to be inserted].

**Classification:** INTERNAL — for HR firm distribution
