# VORON-C2 — Intern Project Programme

**Document Status:** DRAFT v0.1  
**Date:** 2026-08-06  
**Authority:** DAF  
**Classification:** INTERNAL — RESTRICTED  
**Purpose:** Structure the VORON-C2 open-source C2 infrastructure build as an intern-led project programme

---

## 1. Programme Concept

**The pitch:** Instead of hiring experienced (and expensive) red team operators to build the C2 infrastructure from scratch, we structure the build-out as a structured intern project programme. Interns get real-world, high-impact cybersecurity engineering experience. Aras Integrasi gets a sovereign C2 capability built at fractional cost.

**Why this works:**
- Open-source C2 deployment is fundamentally an *infrastructure engineering* task — Docker, networking, DNS, reverse proxies, Linux administration. This is exactly what motivated interns can do with proper guidance.
- The frameworks (Mythic, Sliver, Havoc, AdaptixC2) all have documentation and community guides. Interns don't need to invent — they need to deploy, configure, test, and document.
- Interns learn adversary tradecraft by building the tools adversaries use — this is the most effective cybersecurity education model (offense-informed defense).
- The project produces real, auditable, production-grade infrastructure — not a toy lab exercise.
- DAF reviews, validates, and signs off at each milestone. Quality control is built into the programme structure.

**What interns will NOT do:**
- Conduct live red team engagements (requires authorization, experience, legal coverage)
- Make architecture decisions (DAF owns the architecture — interns execute)
- Handle client data or engage with clients directly
- Access production government infrastructure

---

## 2. Programme Structure

### Overview

**Duration:** 12 weeks (one academic semester / one internship cycle)  
**Team Size:** 3-4 interns per cohort  
**Supervision:** 1 senior engineer (part-time mentor) + DAF (weekly review)  
**Output:** Deployed VORON-C2 Phase 1 infrastructure + documentation + detection ruleset  
**Compensation:** Intern stipend (standard rate) + possibility of full-time offer for top performers

### Cohort Roles

| Role | Focus | Headcount | Why |
|------|-------|-----------|-----|
| **Infrastructure Engineer** | Server deployment, Docker, networking, DNS, redirectors | 1-2 | Deploys and configures the C2 core and supporting infrastructure |
| **C2 Operator (Trainee)** | Framework configuration, agent testing, payload compilation, beacon testing | 1 | Gets the frameworks actually working — compiles agents, tests beacons, validates C2 channels |
| **Detection Engineer** | Wazuh/ELK deployment, Sigma rules, ATT&CK mapping, purple team validation | 1 | Builds the defensive telemetry stack that makes the whole thing valuable |

**Cross-training:** All interns participate in all workstreams to some degree — the role is their primary focus, not their only focus.

### Prerequisites

**Required (all interns):**
- Linux command line fundamentals
- Basic networking knowledge (TCP/IP, DNS, HTTP)
- Python scripting ability
- Self-directed learning capability
- Security mindset (understands "do no harm")

**Preferred (per role):**
- Infrastructure Engineer: Docker, Ubuntu/CentOS administration, Nginx/Apache
- C2 Operator: Windows internals basics, malware analysis interest, CTF experience
- Detection Engineer: SIEM concepts, log analysis, YARA/Sigma awareness

---

## 3. 12-Week Project Plan

### Phase A: Foundation (Weeks 1-4)

**Objective:** Environment ready, frameworks deployed, first beacon alive.

#### Week 1 — Environment Setup

**Infrastructure Engineer:**
- [ ] Provision Tier 0 lab server (Ubuntu 22.04/24.04 LTS, 16GB RAM, 4+ cores)
- [ ] Set up isolated network segment (VLAN or separate subnet)
- [ ] Install Docker + Docker Compose on lab server
- [ ] Configure WireGuard VPN for operator access
- [ ] Set up test VMs: 2x Windows 10/11 (with Sysmon), 1x Ubuntu desktop, 1x Windows Server 2022 (AD lab)
- [ ] Document full environment topology with IP map

**C2 Operator:**
- [ ] Clone Mythic repository, read documentation
- [ ] Clone Sliver repository, read documentation
- [ ] Build Sliver server binary from source (`go build`)
- [ ] Generate first Sliver implant (HTTP beacon), test against local VM
- [ ] Document: "Sliver Quick Start" guide for the team

**Detection Engineer:**
- [ ] Install Wazuh manager + Wazuh agent on test VMs
- [ ] Install Elasticsearch + Kibana (or Wazuh's built-in ELK)
- [ ] Configure Sysmon on Windows test VMs with SwiftOnSecurity config
- [ ] Verify logs flowing from endpoints → Wazuh → ELK
- [ ] Document: "Detection Stack Setup" guide

**All Interns:**
- [ ] Complete: Read VORON-C2 Architecture document (the full thing)
- [ ] Complete: Read DFIR Report on BumbleBee → AdaptixC2 → Akira attack chain
- [ ] Complete: MITRE ATT&CK Enterprise Matrix walkthrough (identify which techniques each C2 framework covers)

**Week 1 Deliverables:**
- Lab environment operational (documented topology)
- Sliver server running, first beacon tested
- Wazuh + ELK receiving logs from test VMs
- Three "Quick Start" guides drafted

**Milestone Review (Friday Week 1):** DAF reviews environment, validates first Sliver beacon, checks log flow.

---

#### Week 2 — Mythic Deployment

**Infrastructure Engineer:**
- [ ] Deploy Mythic via `mythic-cli` and Docker Compose
- [ ] Configure Mythic server: operator accounts, certificates, network binding
- [ ] Install C2 profiles: HTTP, WebSocket, SMB
- [ ] Install agent types: Apollo (Windows), Poseidon (Linux)
- [ ] Configure Mythic to bind to internal interface only (no direct internet exposure)
- [ ] Set up Mythic PostgreSQL database backup schedule

**C2 Operator:**
- [ ] Create first Mythic Apollo agent (Windows HTTP beacon)
- [ ] Deploy agent to Windows test VM
- [ ] Test basic commands: ls, cd, pwd, cat, download, upload
- [ ] Test advanced commands: screenshot, process list, shell
- [ ] Test SMB beacon — deploy via HTTP beacon, establish peer-to-peer C2
- [ ] Document: "Mythic Operator Guide" with screenshots

**Detection Engineer:**
- [ ] Write first Sigma rule: detect Mythic HTTP beacon traffic (URL patterns, UA strings, beacon timing)
- [ ] Write Sigma rule: detect Sliver HTTP beacon traffic
- [ ] Test rules against live beacon traffic in Wazuh — do they fire?
- [ ] Document: "First Detection Rules — Validation Report"
- [ ] Map each detected activity to MITRE ATT&CK technique ID

**All Interns:**
- [ ] Weekly knowledge share: 15-min presentation by each intern on what they learned

**Week 2 Deliverables:**
- Mythic server operational with Apollo + Poseidon agents
- Apollo agent deployed and tested on Windows VM
- SMB beacon tested (peer-to-peer C2)
- First 5+ Sigma detection rules written and validated
- MITRE ATT&CK mapping document started

**Milestone Review (Friday Week 2):** DAF reviews Mythic deployment, tests agent commands, validates detection rules.

---

#### Week 3 — Sliver Deep Dive + Redirector Infrastructure

**Infrastructure Engineer:**
- [ ] Deploy redirector VPS (Ubuntu, 2-3 VPS instances)
- [ ] Configure Apache/Nginx reverse proxy on each redirector
- [ ] Write mod_rewrite / proxy_pass rules to forward C2 traffic to Mythic server
- [ ] Configure legitimate-looking web server on redirectors (decoy site)
- [ ] Test: agent → redirector → C2 server chain works end-to-end
- [ ] Write auto-deploy script for redirector spin-up (bash/Ansible)
- [ ] Write teardown script (for post-engagement cleanup)

**C2 Operator:**
- [ ] Sliver: Generate mTLS beacon, test against Linux VM
- [ ] Sliver: Generate WireGuard beacon, test against Windows VM (encrypted UDP C2)
- [ ] Sliver: Generate DNS beacon, test against Windows VM
- [ ] Sliver: Test implant formats — EXE, DLL, shellcode
- [ ] Sliver: Test process migration and impersonation commands
- [ ] Document: "Sliver C2 Channels — Testing Report" (what worked, what didn't, detection surface for each channel)
- [ ] Configure Sliver to use redirectors (C2 traffic through redirector chain)

**Detection Engineer:**
- [ ] Write Sigma rules for Sliver mTLS, WireGuard, and DNS beacons
- [ ] Write YARA rule for Sliver implant binary signatures
- [ ] Test: Can Wazuh detect C2 traffic through redirectors?
- [ ] Write network detection rules (Zeek/Suricata if available, else Wazuh network rules)
- [ ] Document: "Redirector Detection — Can We See Through It?"

**All Interns:**
- [ ] Weekly knowledge share presentations
- [ ] Begin drafting the "VORON-C2 Operations Manual" (collaborative document)

**Week 3 Deliverables:**
- 3 redirector VPS deployed and tested
- C2 traffic flowing through redirector chain
- Sliver fully tested across all C2 channels (mTLS, WG, DNS, HTTP)
- YARA + Sigma rules for Sliver and Mythic agents
- Redirector detection report
- Operations Manual draft started

**Milestone Review (Friday Week 3):** DAF reviews redirector chain, tests traffic flow, validates detection rules through redirectors.

---

#### Week 4 — DNS Infrastructure + Phase A Integration Test

**Infrastructure Engineer:**
- [ ] Deploy authoritative DNS server (PowerDNS or BIND9) on lab infrastructure
- [ ] Register 2-3 domains for C2 infrastructure (operational domains, not production client domains)
- [ ] Configure DNS records: A, CNAME, TXT for C2 infrastructure
- [ ] Configure DNS for beacon domains (subdomains for DNS beaconing)
- [ ] Test DNS resolution from test VMs through the C2 DNS infrastructure
- [ ] Document: "DNS Infrastructure Setup Guide"

**C2 Operator:**
- [ ] Configure Sliver DNS beacon to use authoritative DNS infrastructure
- [ ] Configure Mythic DNS C2 profile (if available) or document limitation
- [ ] Test DNS beaconing end-to-end: agent → DNS server → C2 server → response
- [ ] Test DNS beacon through redirector chain
- [ ] Full integration test: Deploy agent via redirector → beacon via DNS → execute commands → results returned
- [ ] Document: "End-to-End C2 Integration Test Report"

**Detection Engineer:**
- [ ] Write DNS detection rules: anomalous DNS queries, TXT record beaconing, high-frequency DNS to single domain
- [ ] Full purple team test: Red (C2 Operator) deploys beacon → Blue (Detection Engineer) attempts detection
- [ ] Document: "Purple Team Exercise #1 — Results and Gaps"
- [ ] Update ATT&CK mapping with all techniques tested in Phase A
- [ ] Compile all detection rules into a structured rule pack

**All Interns:**
- [ ] Complete "VORON-C2 Operations Manual" v1.0 (Phase A content)
- [ ] Prepare Phase A presentation for DAF review

**Week 4 Deliverables:**
- Authoritative DNS infrastructure operational
- DNS beaconing tested end-to-end
- Full integration test passed (agent → redirector → DNS → C2 → command → result)
- Purple Team Exercise #1 completed with documented results
- Complete detection rule pack (15-20+ rules)
- VORON-C2 Operations Manual v1.0 (Phase A)
- ATT&CK coverage matrix (Phase A)

**Phase A Milestone Review (Friday Week 4):** Full DAF review. End-to-end demonstration. Go/no-go for Phase B.

---

### Phase B: Advanced Frameworks (Weeks 5-8)

**Objective:** Havoc + AdaptixC2 deployed, evasion testing, advanced detection engineering.

#### Week 5 — Havoc Framework Deployment

**Infrastructure Engineer:**
- [ ] Deploy Havoc server (Go) on separate Docker container or VM
- [ ] Configure Havoc team server — operator accounts, listener configuration
- [ ] Build Havoc agent from source (C/C++ — requires MinGW cross-compilation on Linux)
- [ ] Configure Havoc to use existing redirector infrastructure
- [ ] Test agent deployment to Windows test VM

**C2 Operator:**
- [ ] Deploy Havoc agent on Windows VM via Mythic/Sliver (staged deployment)
- [ ] Test Havoc commands: shell, file operations, process management
- [ ] Test Havoc sleep obfuscation (ekko/zilean) — verify memory scanning evasion
- [ ] Test Havoc process injection modules
- [ ] Compare Havoc footprint vs Mythic Apollo vs Sliver (file size, process footprint, network artifacts)
- [ ] Document: "Havoc Framework — Deployment and Testing Report"

**Detection Engineer:**
- [ ] Analyze Havoc agent memory footprint — can Wazuh/Sysmon detect sleep obfuscation?
- [ ] Write Sigma rules for Havoc process injection patterns
- [ ] Write YARA rules for Havoc agent binary
- [ ] Test: Does Havoc evade existing detection rules? If yes, what new rules are needed?
- [ ] Document: "Havoc Detection Engineering Report"

**All Interns:**
- [ ] Weekly knowledge share
- [ ] Update Operations Manual with Havoc chapter

**Week 5 Deliverables:**
- Havoc server deployed, agent compiled, tested on Windows VM
- Havoc sleep obfuscation tested and documented
- Havoc detection rules written (where possible — evasion is expected)
- Comparative analysis: Mythic vs Sliver vs Havoc (detection surface, capabilities, footprint)

---

#### Week 6 — AdaptixC2 Deployment + Adversary Emulation Lab

**Infrastructure Engineer:**
- [ ] Deploy AdaptixC2 server (Go) on lab infrastructure
- [ ] Build AdaptixC2 Qt client on operator workstation (or lab machine)
- [ ] Configure AdaptixC2 agent types: HTTP/HTTPS, SMB, DNS/DoH
- [ ] Configure AdaptixC2 to use redirector infrastructure

**C2 Operator:**
- [ ] Generate AdaptixC2 HTTP beacon, deploy to Windows test VM
- [ ] Test AdaptixC2 commands and capabilities
- [ ] Test BOF execution (if available)
- [ ] Replicate the BumbleBee → AdaptixC2 attack chain (lab only): DLL side-loading → AdaptixC2 beacon → credential harvesting commands
- [ ] Document: "AdaptixC2 Adversary Emulation — Akira Attack Chain Reproduction"

**Detection Engineer:**
- [ ] Write detection rules for AdaptixC2 default headers (`Server: AdaptixC2`, `Adaptix-Version`)
- [ ] Build AdaptixC2 RC4 config extractor (Python script — key is appended to payload)
- [ ] Write Sigma rules for AdaptixC2 beacon patterns
- [ ] Test: Can we detect the replicated Akira attack chain at each stage?
- [ ] Document: "AdaptixC2 Detection Engineering — From Default to Custom"

**All Interns:**
- [ ] Weekly knowledge share
- [ ] Update Operations Manual with AdaptixC2 chapter

**Week 6 Deliverables:**
- AdaptixC2 deployed, all agent types tested
- Akira attack chain reproduced in lab (documented step-by-step)
- AdaptixC2 RC4 config extractor tool built
- Detection rules for each stage of the Akira attack chain
- AdaptixC2 detection report

---

#### Week 7 — Evasion Testing + OPSEC Hardening

**All Interns (joint exercise):**

This is a cross-role week. All interns work together on a structured evasion testing exercise.

- [ ] Take existing detection rule pack (all rules from Phase A + B so far)
- [ ] Red team challenge: Modify C2 configurations to evade as many rules as possible
  - Change default User-Agent strings
  - Modify beacon timing/jitter
  - Use non-standard C2 ports
  - Domain fronting via CDN
  - Process injection into legitimate processes
  - Sleep obfuscation
  - DLL side-loading techniques
- [ ] Blue team response: For each evasion, attempt to write new detection rules
- [ ] Document: "Evasion vs Detection — Cat and Mouse Report"
- [ ] Document which evasions are detectable and which are not (gap analysis)
- [ ] Update ATT&CK coverage matrix with evasion techniques
- [ ] Hardening recommendations: What should be changed in C2 deployments for OPSEC?

**Week 7 Deliverables:**
- Evasion testing report (what evasions worked, what was detected, what gaps remain)
- Updated detection rule pack with evasion-resistant rules
- OPSEC hardening guide for C2 deployments
- ATT&CK coverage matrix updated

---

#### Week 8 — Purple Team Exercise #2 + Phase B Review

**All Interns (joint exercise):**

Full-scale purple team exercise — the capstone of Phase B.

- [ ] **Red team (C2 Operator + Infrastructure Engineer):**
  - Deploy agent via redirector chain (realistic deployment, not lab-direct)
  - Use the framework best suited for evasion (based on Week 7 findings)
  - Execute full attack chain: initial beacon → privilege escalation → lateral movement → credential access → data staging
  - Attempt to evade all detection rules
- [ ] **Blue team (Detection Engineer):**
  - Monitor Wazuh/ELK in real-time during the exercise
  - Attempt to detect each stage of the attack
  - Document detections and gaps in real-time
- [ ] **Joint:**
  - Post-exercise review: What was detected? What was missed? Why?
  - Write new detection rules for any gaps identified
  - Document: "Purple Team Exercise #2 — Full Report"
  - Update Operations Manual with Phase B content
  - Prepare Phase B presentation

**Week 8 Deliverables:**
- Purple Team Exercise #2 full report
- Updated detection rule pack (30+ rules)
- Updated ATT&CK coverage matrix
- VORON-C2 Operations Manual v2.0 (Phase A + B)
- Phase B milestone presentation

**Phase B Milestone Review (Friday Week 8):** Full DAF review. Purple team exercise replay. Go/no-go for Phase C.

---

### Phase C: Productionization (Weeks 9-12)

**Objective:** Documentation finalization, automation, deployment scripts, handoff package.

#### Week 9 — Deployment Automation

**Infrastructure Engineer:**
- [ ] Write Ansible playbook for full VORON-C2 deployment from scratch:
  - Mythic server setup (Docker Compose, C2 profiles, agent types)
  - Sliver server setup (Go build, configuration)
  - Redirector setup (Apache/Nginx, SSL, mod_rewrite rules)
  - DNS server setup (PowerDNS/BIND9, zone files)
  - Wazuh + ELK setup (Docker Compose, agent enrollment)
- [ ] Write deployment scripts for rapid redirector spin-up/teardown
- [ ] Write backup and restore scripts for C2 infrastructure
- [ ] Test: Deploy full stack from scratch on fresh server using only the Ansible playbook
- [ ] Document: "VORON-C2 Automated Deployment Guide"

**C2 Operator:**
- [ ] Write operator onboarding guide (how to connect, authenticate, deploy first agent)
- [ ] Create standard agent configuration templates (per engagement type)
- [ ] Create payload compilation pipeline script (automated agent build with custom configs)
- [ ] Document: "VORON-C2 Operator Handbook"

**Detection Engineer:**
- [ ] Package all detection rules into a deployable rule pack
- [ ] Write Wazuh + Sigma rule deployment script
- [ ] Create detection testing pipeline (automated test: deploy agent → check if rules fire)
- [ ] Document: "VORON-C2 Detection Rule Pack — Installation and Usage"

**Week 9 Deliverables:**
- Full Ansible deployment playbook (tested on fresh server)
- Operator onboarding guide + agent config templates
- Detection rule pack (deployable, scripted)
- Automated payload compilation pipeline

---

#### Week 10 — Documentation Finalization

**All Interns (joint week):**

- [ ] Finalize VORON-C2 Operations Manual v3.0 (all chapters)
- [ ] Write "VORON-C2 Infrastructure Architecture" — clean, finalized version (this becomes the reference document for future operators)
- [ ] Write "VORON-C2 Detection Engineering Guide" — all rules documented, mapped to ATT&CK, with testing methodology
- [ ] Write "VORON-C2 Adversary Emulation Playbook" — step-by-step guides for emulating: Akira ransomware chain, generic ransomware operator, APT lateral movement
- [ ] Write "VORON-C2 Governance Document" — authorization matrix, RoE template, audit procedures
- [ ] Write "VORON-C2 Intern Handoff Guide" — so the next cohort can pick up where this one left off
- [ ] Review all documentation for accuracy, completeness, and clarity
- [ ] DAF reviews each document — iterative feedback cycle

**Week 10 Deliverables:**
- Complete documentation set (6 documents)
- All documents reviewed by DAF
- Documentation repository structure established

---

#### Week 11 — Final Integration Test + Gap Analysis

**All Interns (joint exercise):**

- [ ] Full deployment from scratch on fresh infrastructure using only the Ansible playbook and documentation
  - No manual steps, no "tribal knowledge" — can someone follow the docs and deploy?
- [ ] Full purple team exercise #3 — the final exam:
  - Red team deploys using only the documented procedures
  - Blue team detects using only the deployed rule pack
  - Full attack chain test: deployment → beacon → escalation → lateral movement → collection → exfiltration (simulated)
- [ ] Gap analysis:
  - What works?
  - What doesn't?
  - What's missing from the documentation?
  - What's missing from the detection rules?
  - What should the next cohort focus on?
- [ ] Write: "VORON-C2 Phase 1 — Final Integration Test and Gap Analysis Report"
- [ ] Write: "VORON-C2 Phase 2 Recommendations" (what should happen next, what capabilities to add)

**Week 11 Deliverables:**
- Clean-room deployment test results
- Purple Team Exercise #3 report (final capstone)
- Gap analysis document
- Phase 2 recommendations document

---

#### Week 12 — Presentation + Handoff

**All Interns:**

- [ ] Prepare final presentation for DAF and management committee
  - Architecture overview
  - Live demonstration (end-to-end C2 deployment + detection)
  - Results and metrics (rules written, ATT&CK coverage, deployment time)
  - Lessons learned
  - Recommendations for Phase 2
- [ ] Present to DAF (45-60 min presentation + Q&A)
- [ ] Handoff session: Walk DAF through all infrastructure, documentation, and code
- [ ] Knowledge transfer: Ensure DAF (or designated operator) can independently operate the stack
- [ ] Intern evaluations: Each intern receives written feedback and performance review
- [ ] Top performer consideration: Identify candidates for full-time offer

**Week 12 Deliverables:**
- Final presentation deck
- Live demonstration (recorded)
- Complete handoff (infrastructure + documentation + code)
- Intern performance reviews
- Phase 2 kickoff plan

**Phase C Milestone Review (Friday Week 12):** Full DAF + management review. Final sign-off.

---

## 4. Deliverables Summary

### By Phase

| Phase | Duration | Key Deliverables |
|-------|----------|-----------------|
| **Phase A: Foundation** | Weeks 1-4 | Lab environment, Mythic + Sliver deployed, redirectors, DNS, first detection rules, Purple Team #1 |
| **Phase B: Advanced** | Weeks 5-8 | Havoc + AdaptixC2 deployed, Akira attack chain reproduced, evasion testing, Purple Team #2 |
| **Phase C: Productionization** | Weeks 9-12 | Automation (Ansible), full documentation, final integration test, Purple Team #3, handoff |

### Complete Output (All 12 Weeks)

**Infrastructure:**
- ✅ Tier 0 lab environment (server, network, VPN, test VMs)
- ✅ Mythic server (Docker, 2+ agent types, 2+ C2 profiles)
- ✅ Sliver server (all C2 channels tested)
- ✅ Havoc server (agent compiled, tested)
- ✅ AdaptixC2 server (adversary emulation lab)
- ✅ 3 redirector VPS (auto-deploy/teardown)
- ✅ Authoritative DNS infrastructure
- ✅ Wazuh + ELK detection stack
- ✅ Full Ansible deployment playbook

**Detection Engineering:**
- ✅ 30-50+ Sigma/YARA detection rules
- ✅ ATT&CK coverage matrix
- ✅ AdaptixC2 RC4 config extractor tool
- ✅ Purple team exercise reports (3 exercises)
- ✅ Evasion testing report
- ✅ Detection rule pack (deployable)

**Documentation:**
- ✅ VORON-C2 Operations Manual v3.0
- ✅ Automated Deployment Guide
- ✅ Operator Handbook
- ✅ Detection Engineering Guide
- ✅ Adversary Emulation Playbook
- ✅ Governance Document (RoE template, authorization matrix)
- ✅ Intern Handoff Guide
- ✅ Final Integration Test + Gap Analysis Report
- ✅ Phase 2 Recommendations

**Code:**
- ✅ Ansible deployment playbook
- ✅ Redirector auto-deploy/teardown scripts
- ✅ Payload compilation pipeline
- ✅ Detection rule deployment scripts
- ✅ AdaptixC2 config extractor (Python)
- ✅ All code in Git repository

---

## 5. Mentorship & Supervision

### Structure

| Role | Responsibility | Time Commitment |
|------|---------------|-----------------|
| **DAF** | Architecture authority, weekly milestone reviews, final sign-off, strategic direction | 2-3 hours/week |
| **Senior Engineer (Mentor)** | Daily guidance, technical troubleshooting, code review, quality assurance | 5-10 hours/week |
| **Intern Cohort** | Execution, documentation, testing, learning | Full-time (40 hours/week) |

### Weekly Rhythm

| Day | Activity |
|-----|----------|
| Monday | Week kickoff — task assignment, goals review (30 min, all hands) |
| Tuesday-Thursday | Independent work + mentor availability for questions |
| Wednesday | Mid-week check-in (15 min, mentor + interns) |
| Friday | Milestone review — demo to DAF, feedback, next-week planning (60 min) |

### Escalation Path

```
Intern question → Mentor (same day)
Technical blocker → Mentor + DAF (within 24h)
Architecture question → DAF directly
Security concern → DAF immediately (any time)
```

---

## 6. Evaluation Criteria

### Intern Performance Assessment

| Criterion | Weight | Measurement |
|-----------|--------|-------------|
| **Technical Execution** | 30% | Did the infrastructure work? Did the detection rules fire? Quality of deployment. |
| **Documentation Quality** | 25% | Can someone else follow the docs and reproduce the work? Clarity, completeness, accuracy. |
| **Problem Solving** | 20% | When something broke, did they debug and fix it? Did they research solutions? |
| **Learning Velocity** | 15% | How much did they grow from Week 1 to Week 12? Did they go beyond their assigned role? |
| **Teamwork & Communication** | 10% | Weekly knowledge shares, helping other interns, clear communication in docs and presentations. |

### Grading

| Grade | Description | Action |
|-------|-------------|--------|
| **A (Excellent)** | Exceeded expectations, produced production-quality work, grew significantly | Full-time offer consideration |
| **B (Good)** | Met expectations, produced usable work, grew adequately | Strong reference, possible contract extension |
| **C (Satisfactory)** | Met minimum requirements, produced functional work | Standard reference |
| **D (Needs Improvement)** | Below expectations, work required significant mentor intervention | Constructive feedback, no continued engagement |

---

## 7. Learning Outcomes

By the end of the 12-week programme, interns will have:

**Technical Skills:**
- Deployed and operated 4 open-source C2 frameworks (Mythic, Sliver, Havoc, AdaptixC2)
- Built redirector infrastructure with Apache/Nginx reverse proxies
- Deployed authoritative DNS infrastructure for C2 support
- Deployed and configured Wazuh + ELK SIEM stack
- Written 30+ detection rules (Sigma + YARA)
- Conducted 3 purple team exercises
- Built automation with Ansible and Python
- Reproduced a real-world ransomware attack chain (Akira)

**Security Knowledge:**
- MITRE ATT&CK framework — practical application, not just theory
- C2 infrastructure architecture and operational security
- Detection engineering methodology
- Adversary tradecraft (through building and testing the tools)
- Red team / purple team engagement workflow
- Legal and governance framework for security testing

**Professional Skills:**
- Technical documentation (produced 9+ documents)
- Presentation skills (weekly knowledge shares + final presentation)
- Collaborative work (cross-role exercises)
- Problem-solving under pressure (evasion testing, purple team exercises)

**Portfolio Output:**
Each intern leaves with a portfolio of:
- Deployed infrastructure (documented, reproducible)
- Detection rules they personally wrote (with validation evidence)
- Documentation they authored (published internally)
- Purple team exercise reports they contributed to
- A real-world attack chain reproduction (Akira/BumbleBee/AdaptixC2)

This is not a toy project for a resume. This is real capability infrastructure that will be used by Aras Integrasi for real engagements.

---

## 8. Recruitment & Selection

### Sourcing

| Channel | Target |
|---------|--------|
| University career offices (UM, UTM, USM, UNITEN, MMU) | Final-year CS/Cybersecurity students |
| LinkedIn internship postings | Early-career professionals seeking pivot to cybersecurity |
| Cybersecurity student clubs / CTF communities | Self-motivated learners with hands-on interest |
| Aras Integrasi website | Direct applicants |

### Selection Process

| Stage | Format | Duration | Assesses |
|-------|--------|----------|----------|
| **Application** | CV + cover letter (why this project?) | Rolling | Basic fit, motivation |
| **Technical Screen** | 30-min interview: Linux CLI, networking basics, Python | 30 min | Technical fundamentals |
| **Practical Exercise** | 2-hour lab: Deploy a simple Docker container, write a Python script to parse a log file, explain a DNS lookup | 2 hours | Hands-on ability |
| **Cultural Fit** | 30-min conversation with DAF or mentor | 30 min | Attitude, learning mindset, team fit |

### Ideal Candidate Profile

- Self-directed learner (proven by CTF participation, personal projects, or self-study)
- Linux comfort (not expert, but not afraid of the terminal)
- Networking fundamentals (understands DNS, HTTP, TCP)
- Python scripting (can write a script, not just copy-paste)
- Security curiosity (reads about threats, follows security news)
- Documentation discipline (can write clear instructions)
- Team player (wants to build something real, not just pad a resume)

---

## 9. Budget

### Per Cohort (12 weeks, 3-4 interns)

| Item | Cost (RM) | Notes |
|------|-----------|-------|
| Intern stipends (3-4 × 12 weeks) | 14,400-19,200 | RM 300-400/week per intern |
| Lab server (if not existing) | 8,000-15,000 | One-time, reusable across cohorts |
| VPS (redirectors, 3 instances × 12 weeks) | 1,800 | RM 50/month × 3 × 3 months |
| Domain registration (3 domains) | 150 | Annual |
| Mentor time (senior engineer, partial) | Internal cost | ~5-10 hours/week |
| DAF time (reviews, oversight) | Internal cost | ~2-3 hours/week |
| **Total per cohort** | **~25,000-37,000** | First cohort (includes server) |
| **Total per cohort (subsequent)** | **~17,000-21,000** | Server already exists |

### ROI Comparison

| Approach | Cost | Output |
|----------|------|--------|
| Hire senior red team operator (6 months) | RM 60,000-90,000 salary | Built infrastructure + operational capability |
| Intern cohort (12 weeks) | RM 25,000-37,000 | Built infrastructure + documentation + trained potential hires |
| External consultancy (build C2 infra) | RM 50,000-150,000 | Built infrastructure, no knowledge transfer |

The intern programme produces the same infrastructure output at lower cost, with documentation, knowledge transfer, and a talent pipeline as bonus.

---

## 10. Risk Management

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|-----------|
| Interns lack skills to complete tasks | Medium | High | Clear prerequisites, practical exercise in selection, mentor support, phased complexity |
| Intern leaves mid-programme | Medium | Medium | Documentation discipline from Day 1 (no tribal knowledge), cross-training, 3-4 interns for redundancy |
| Infrastructure deployed insecurely | Medium | High | DAF reviews at each milestone, mentor code review, air-gapped Tier 0, no production access |
| Intern does something unsafe (deploys agent outside lab) | Low | Critical | Clear rules: lab environment only, no external deployment, signed acceptable use policy, mentor supervision |
| Quality of detection rules is poor | Medium | Medium | DAF reviews rules at each milestone, purple team exercises validate rules, iterative improvement |
| Documentation incomplete at handoff | Medium | Medium | Documentation is a weekly deliverable, not a Week 12 rush. DAF reviews docs at each milestone. |

### Acceptable Use Policy (Intern Sign-On)

All interns must sign before starting:

1. I will only deploy C2 agents in the designated lab environment
2. I will not deploy any agent, beacon, or payload outside the lab network
3. I will not access, scan, or probe any system outside the lab environment
4. I will not remove any data, code, or configuration from the lab environment without authorization
5. I will not discuss the project details outside the team
6. I will document all my work in the shared repository
7. I will report any security concern or mistake immediately to the mentor or DAF
8. I understand that violating these terms may result in immediate termination

---

## 11. Scaling Model

### Cohort 1 (Current Plan)
- 3-4 interns, 12 weeks, Phase 1 build-out
- Output: Deployed infrastructure + documentation + detection rules

### Cohort 2 (Next Cycle)
- 3-4 new interns, 12 weeks, Phase 2 build-out
- Builds on Cohort 1 infrastructure
- Focus: Advanced evasion research, custom agent development, GovSec API integration, expanded detection rules
- Cohort 1 top performer returns as junior mentor

### Cohort 3+ (Ongoing)
- Continuous intern programme
- Each cohort advances the capability
- Builds talent pipeline for Aras Integrasi
- Creates a training programme that becomes a product itself (certified red team operators trained on sovereign C2)

### Long-Term Vision

The intern programme becomes Aras Integrasi's **national cybersecurity talent development pipeline**:

```
Intern Cohort → Trained Operator → Full-time Hire → Senior Operator → National Capability
     ↓                ↓                    ↓                  ↓                    ↓
  12 weeks        6 months            12 months         24 months          Sovereign C2
                     trained            leading            directing           operational
                     engagements         engagements        the programme        for GovSec
```

Each cohort produces:
- Infrastructure improvements
- Detection rule expansions
- Documentation updates
- Trained cybersecurity professionals
- Potential full-time hires

The programme becomes self-sustaining: Cohort 1 top performers mentor Cohort 2, Cohort 2 mentors Cohort 3, etc.

---

## 12. Immediate Next Steps

1. **Approve intern programme concept** — DAF reviews and approves this document
2. **Identify mentor** — Who is the senior engineer who will provide daily guidance?
3. **Open recruitment** — University outreach, LinkedIn posting, CTF community
4. **Provision lab server** — Before Cohort 1 starts (can be done by mentor or DAF)
5. **Prepare onboarding materials** — Reading list, environment access, acceptable use policy
6. **Set start date** — Target: Next academic semester intake or immediate hiring

---

*This programme turns a capability build into a talent development engine. The infrastructure gets built. The interns get trained. The company gets a talent pipeline. The nation gets a sovereign capability. Everyone wins.*
