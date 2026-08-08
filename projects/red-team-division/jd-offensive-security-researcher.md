# JOB DESCRIPTION — Offensive Security Researcher

**Position:** Offensive Security Researcher  
**Division:** Red Team Division, Cyber Security Practice  
**Company:** Aras Integrasi Sdn Bhd  
**Reports to:** Head of Red Team Division  
**Location:** Kuala Lumpur, Malaysia (hybrid)  
**Employment type:** Full-time, permanent  
**Date:** August 2026

---

## Position Summary

The Offensive Security Researcher is what makes the division genuinely different from every other red team provider in Malaysia. A red team that only uses existing tools is a commodity. This role produces custom exploits, novel evasion techniques, and indigenous tool development that can't be bought off the shelf.

You research vulnerabilities, write exploits, extend the VORON-C2 stack with custom modules, test agents against commercial EDR products, and explore AI-augmented offensive techniques using CyberStrike and local LLMs. Your work feeds directly into engagements — when the Senior Operator hits a wall, you build the tool that gets through.

This is a hands-on research and development role. You will reverse engineer binaries, fuzz software for vulnerabilities, write reliable exploits, develop C2 extensions, and publish research that positions Aras Integrasi as a thought leader. You also mentor interns and contribute to the skunkworks programme with technical challenges.

---

## Key Responsibilities

### Vulnerability Research (30%)

- Conduct vulnerability research across target technologies:
  - **Software** — enterprise applications, web frameworks, middleware, operating system components
  - **Firmware** — IoT devices, network appliances, embedded systems relevant to Malaysian infrastructure
  - **Protocols** — authentication protocols, network protocols, custom protocols in critical infrastructure
  - **Cloud** — misconfigurations, IAM exploitation, container escape, serverless attack vectors
  - **AI Systems** — LLM attacks, model inversion, adversarial examples, prompt injection at scale
- Vulnerability research methodology:
  - Static analysis (Ghidra, IDA Pro, radare2, Binary Ninja)
  - Dynamic analysis (debugging, fuzzing, instrumentation)
  - Protocol analysis (Wireshark, mitmproxy, custom protocol fuzzers)
  - Code auditing (source code review where available, decompilation where not)
- Responsible disclosure:
  - Report vulnerabilities to vendors with coordinated disclosure timelines
  - Maintain CVE records for discovered vulnerabilities
  - Publish technical write-ups after vendor patch release
  - Build relationships with vendor PSIRT teams for coordinated response

### Exploit Development (20%)

- Develop reliable exploits for identified vulnerabilities:
  - **Memory corruption** — stack/heap overflows, use-after-free, type confusion, race conditions
  - **Logic bugs** — authentication bypass, privilege escalation, business logic exploitation
  - **Injection** — SQLi, XSS, SSRF, command injection, template injection
  - **Deserialisation** — Java, .NET, Python pickle exploitation
  - **Cloud** — IAM privilege escalation, container escape, metadata service exploitation
- Exploit development standards:
  - Reliability — exploits must work consistently, not crash targets
  - Portability — exploits should work across target versions where possible
  - OPSEC — exploits should minimise target impact and detection surface
  - Documentation — full exploit documentation with vulnerability details and reproduction steps
- Maintain exploit development lab:
  - Isolated environment with target software versions for testing
  - Snapshot/rollback capability for repeated exploit testing
  - Network isolation to prevent accidental impact

### C2 Framework R&D (15%)

- Extend VORON-C2 stack with custom capabilities:
  - **Mythic** — custom agent development (Python, Go, C#), custom C2 profiles, task modules
  - **Sliver** — extensions, custom beacon behaviours, Sliver wire protocol extensions
  - **Havoc** — C/C++ agent modifications, evasion modules, custom injection techniques
  - **AdaptixC2** — BOF development, custom plugins, AxScript extensions
- Develop custom BOFs (Beacon Object Files):
  - Reconnaissance BOFs (domain enumeration, session enumeration, share discovery)
  - Lateral movement BOFs (WMI execution, PsExec alternatives, SMB relay)
  - Credential BOFs (LSASS dumping alternatives, DPAPI operations, Kerberos ticket operations)
  - Evasion BOFs (EDR unhooking, AMSI bypass, ETW patching, syscall proxying)
- Develop custom post-exploitation tools:
  - Memory-only loaders, reflective DLL injection, process hollowing alternatives
  - In-memory .NET assembly execution (avoiding disk artefacts)
  - Custom shellcode runners and encoders
  - Encrypted payload delivery systems

### Evasion Research (15%)

- Test C2 agents against commercial EDR/AV products:
  - Maintain lab with commercial EDR products (CrowdStrike, SentinelOne, Microsoft Defender for Endpoint, etc.)
  - Test agent behaviours — beaconing patterns, process injection, file operations
  - Identify detection triggers — what the EDR sees and alerts on
  - Develop bypass techniques for identified triggers
  - Document evasion techniques with detection-avoidance rationale
- Evasion technique research areas:
  - **EDR bypass** — unhooking, direct syscalls, NTAPI callback removal, kernel callbacks
  - **AMSI bypass** — patching, hardware breakpoint, provider removal
  - **ETW bypass** — patching, session disabling, provider removal
  - **Behavioural evasion** — sleep mask, memory encryption, thread stack spoofing
  - **Network evasion** — domain fronting, DNS over HTTPS, encrypted channels, traffic shaping
  - **File system evasion** — in-memory execution, fileless persistence, NTFS alternate data streams
- Maintain evasion knowledge base:
  - Catalogue techniques by effectiveness, detection rate, and target EDR product
  - Track EDR vendor updates and re-test techniques after updates
  - Maintain "what works today" matrix for the division's operators

### AI-Augmented Offensive Research (10%)

- Leverage CyberStrike and local LLMs for offensive research:
  - **Payload obfuscation** — use LLMs to generate variant code that evades signature detection
  - **YARA rule generation** — auto-generate YARA rules from malware samples for detection engineering
  - **Attack chain analysis** — use LLMs to analyse and optimise attack paths
  - **Vulnerability triage** — AI-assisted prioritisation of vulnerability research targets
  - **Exploit variant generation** — generate multiple exploit variants to test against patched systems
- Maintain local LLM infrastructure:
  - DGX Spark or equivalent for local model inference
  - Model selection and fine-tuning for offensive security tasks
  - Prompt engineering for offensive use cases
  - Integration with C2 framework (MCP-based orchestration where applicable)
- Research AI attack vectors:
  - LLM prompt injection at scale
  - Model inversion and extraction attacks
  - Adversarial examples for ML-based security products
  - AI-generated phishing and social engineering content
  - Supply chain attacks on ML pipelines

### Research Publication & Thought Leadership (5%)

- Produce external research outputs:
  - Conference talks (DEF CON, Black Hat, Hack in the Box, TalkSec, local Malaysian cons)
  - Blog posts and technical write-ups (Aras Integrasi blog, personal, industry publications)
  - CVE submissions and advisories
  - Open-source tool releases (where strategically beneficial for division visibility)
- Maintain research publication calendar:
  - Minimum 2 conference submissions per year
  - Minimum 4 blog posts / technical write-ups per year
  - Minimum 1 CVE or vulnerability advisory per year
- Review all publications for OPSEC — no division capabilities, client data, or sensitive techniques disclosed

### Engagement Support & Mentorship (5%)

- Support Senior Red Team Operator during engagements:
  - Provide novel exploitation when standard techniques fail
  - Develop custom payloads for specific target environments
  - Advising on EDR evasion strategy based on research findings
  - On-call for difficult exploitation problems during active engagements
- Mentor skunkworks interns:
  - Design technical challenges for skunkworks programme
  - Review intern research projects
  - Pair with interns on vulnerability research tasks
  - Deliver internal training on exploit development, reverse engineering

---

## Requirements

### Essential Qualifications

- Malaysian citizen or PR (national capability preference)
- Bachelor's degree in Computer Science, Information Security, or equivalent demonstrated experience
- 3–6 years cybersecurity experience with demonstrated vulnerability research output
- Demonstrated exploit development capability (CVEs, write-ups, bug bounties, CTF wins)

### Essential Technical Skills

**Reverse Engineering:**
- Ghidra, IDA Pro, radare2, Binary Ninja — decompilation, disassembly, analysis
- Assembly (x86/x64, ARM where applicable) — reading and writing
- Debugging — x64dbg, WinDbg, GDB, Frida
- Binary analysis — PE format, ELF format, Mach-O (for cross-platform research)
- Packer/crypter identification and unpacking

**Exploit Development:**
- Memory corruption exploitation — stack overflow, heap overflow, use-after-free, ROP chains
- Windows exploitation — DEP/ASLR bypass, CFG bypass, HGS bypass
- Linux exploitation — ASLR bypass, stack protections, heap exploitation
- Fuzzing — AFL, libFuzzer, honggfuzz, custom fuzzers
- Exploit mitigations understanding and bypass techniques

**Programming:**
- Python — proficient for research automation, exploit scripting, tool development
- C/C++ — proficient for exploit development, BOF writing, agent modification
- Assembly (x86/x64) — reading and writing for shellcode and exploits
- Go — for Sliver extensions, Mythic agents, tool development
- C#/.NET — for post-exploitation assembly development
- PowerShell — for offensive scripting and payload development

**C2 Framework Internals:**
- Understanding of C2 architecture internals (not just usage)
- Mythic — agent development, C2 profile development, task module development
- Sliver — extension development, beacon internals, wire protocol
- Havoc — C/C++ agent source code, modification, custom modules
- AdaptixC2 — plugin development, BOF integration, AxScript

**EDR/AV Evasion:**
- Understanding of EDR architecture — kernel callbacks, ETW, AMSI, sensor pipelines
- EDR bypass techniques — unhooking, direct syscalls, callback removal, memory manipulation
- AV bypass — signature evasion, behavioural evasion, packer development
- Sand-box evasion — environment detection, timing-based, hardware-based

**AI/ML for Offensive Security:**
- Understanding of LLM capabilities and limitations
- Prompt engineering for offensive use cases
- Local LLM deployment (Ollama, vLLM, or equivalent)
- Understanding of AI attack vectors (prompt injection, model inversion, adversarial examples)

### Essential Certifications (one or more)

- OSEE (Offensive Security Exploit Expert)
- OSED (Offensive Security Exploit Developer)
- GREM (GIAC Reverse Engineering Malware)
- Or equivalent demonstrated capability through CVE portfolio, exploit write-ups, and tool releases

### Preferred

- Published CVEs in real-world software
- Conference talks at recognised security conferences (DEF CON, Black Hat, HITB, etc.)
- Bug bounty track record (HackerOne, Bugcrowd, or private programs)
- Active CTF participant (national or international, top-tier finishes)
- Open-source security tool contributions (GitHub with meaningful stars/usage)
- Postgraduate degree in security, CS, or related field
- Experience with OT/ICS security research (for critical infrastructure engagements)

### Language

- English (fluent — required for research publication and technical work)
- Bahasa Malaysia (conversational — preferred but not essential for this role)

---

## What You'll Be Working With

### Daily Tools

| Category | Tools |
|----------|-------|
| Reverse Engineering | Ghidra, IDA Pro, radare2, Binary Ninja |
| Debugging | x64dbg, WinDbg, GDB, Frida, Time Travel Debugging |
| Fuzzing | AFL++, libFuzzer, honggfuzz, custom fuzzers |
| Exploit Dev | Python, C/C++, x86/x64 assembly, pwntools, ropper |
| C2 R&D | Mythic (agent dev), Sliver (extensions), Havoc (C/C++ mods), AdaptixC2 (BOFs, plugins) |
| Evasion | Lab EDR products (CrowdStrike, SentinelOne, Defender for Endpoint), custom bypass tools |
| AI/ML | CyberStrike, local LLM (DGX Spark), Ollama/vLLM, prompt engineering |
| Development | Python, Go, C/C++, C#/.NET, PowerShell, NASM |
| Lab | Isolated exploit dev environment, target software snapshots, EDR test licenses |

### Research Workflow

```
1. Target Selection
   - Based on threat relevance (used by actors targeting Malaysia)
   - Based on client engagement needs (specific software in client environment)
   - Based on national capability requirements (critical infrastructure components)

2. Reconnaissance
   - Identify target software versions, architecture, attack surface
   - Source code review (if available) or binary analysis
   - Identify input vectors, trust boundaries, security controls

3. Vulnerability Discovery
   - Code auditing, fuzzing, protocol analysis, architectural review
   - Document potential vulnerabilities with reproduction steps

4. Vulnerability Confirmation
   - Develop proof-of-concept (PoC) exploit
   - Confirm reliability and impact
   - Assess exploitability constraints (mitigations, environment requirements)

5. Exploit Development
   - Develop reliable, documented exploit
   - Test across target versions
   - Minimise detection surface (OPSEC-aware exploit)

6. Integration
   - Package exploit for division use (module, BOF, script)
   - Document for operator usage
   - Add to division exploit library

7. Responsible Disclosure (where applicable)
   - Report to vendor with coordinated disclosure timeline
   - Maintain CVE record
   - Publish write-up after vendor patch

8. Publication
   - Conference talk or blog post (post-disclosure, OPSEC-reviewed)
   - Position Aras Integrasi as thought leader
```

---

## Performance Expectations

### First 90 Days

- Exploit development lab operational with 2+ EDR products for testing
- First vulnerability research target selected and research begun
- 5+ custom BOFs developed for division's C2 stack
- First evasion technique tested and documented against lab EDR
- CyberStrike integration assessment completed

### Year 1

- 1+ CVE or vulnerability advisory published
- 2+ conference talk submissions
- 4+ blog posts / technical write-ups published
- 10+ custom C2 modules/BOFs in division library
- 5+ evasion techniques documented in "what works today" matrix
- 1+ AI-augmented offensive capability prototyped (CyberStrike or local LLM)
- Engagement support: novel exploitation delivered for 2+ engagements

---

## Compensation

| Component | Range |
|-----------|-------|
| Monthly salary | RM 7,000 – RM 11,000 |
| Annual bonus | Performance-linked, up to 2 months |
| Benefits | EPF, SOCSO, medical, dental, optical |
| Training budget | RM 10,000/year (certifications, conferences) |
| Conference attendance | Minimum 1 international + 2 local per year (preference for research conferences — DEF CON, Black Hat, HITB) |
| Research time | Protected research time — minimum 20% of work hours |

---

## Why This Role

Security researchers in most organisations are siloed — they research, they publish, and their work rarely touches operations. This role is different. Your research directly feeds the division's operators. You find the vulnerability, you write the exploit, the operator uses it in an engagement next week. Your evasion research means the difference between the C2 beacon getting caught and getting through. Your BOFs extend the division's capability every week.

The 20% protected research time is real — this isn't a role where research gets squeezed out by billable hours. Your research output IS the product. And the publication path means you get the recognition — CVEs, conference talks, and your name on the research that positions Aras Integrasi as the Malaysian offensive security thought leader.

---

**To apply:** Send CV, cover letter, and research portfolio (CVEs, exploit write-ups, GitHub tool contributions, conference talks, blog posts) to [HR contact to be inserted].

**Classification:** INTERNAL — for HR firm distribution
