# JOB DESCRIPTION — Detection Engineer (Purple Team)

**Position:** Detection Engineer (Purple Team)  
**Division:** Red Team Division, Cyber Security Practice  
**Company:** Aras Integrasi Sdn Bhd  
**Reports to:** Head of Red Team Division  
**Location:** Kuala Lumpur, Malaysia (hybrid)  
**Employment type:** Full-time, permanent  
**Date:** August 2026

---

## Position Summary

The Detection Engineer is what makes this a national capability builder rather than a red team service provider. Every red team engagement produces attack telemetry. Your job is to convert that telemetry into reusable detection rules that stay with the client. Over time, you build a national detection rule library that becomes a strategic asset for Malaysian cyber resilience.

You operate on the blue side of the purple team — working in real-time alongside the red team operator during engagements, monitoring SIEM alerts, identifying detection gaps, and writing rules that close them. After engagements, you package detections for client delivery and add them to the division's growing library.

This is a hands-on engineering role. You will build and maintain the Wazuh + ELK detection stack, write Sigma rules, map coverage to MITRE ATT&CK, tune alerts to reduce false positives, and hunt for threats based on dark web intelligence. You are the bridge between offensive output and defensive value.

---

## Key Responsibilities

### Detection Engineering Pipeline (30%)

- Build and maintain the division's detection engineering infrastructure:
  - **Wazuh SIEM** — deployment, configuration, agent management, rule management
  - **Elasticsearch + Kibana** — log storage, indexing, dashboards, visualisations
  - **Log shipping** — Filebeat/Winlogbeat configuration, log source onboarding
  - **Sigma rule library** — write, test, version, and maintain detection rules
- Convert red team engagement output into detection rules:
  - Parse engagement logs to identify detectable behaviours
  - Write Sigma rules for each detectable TTP
  - Test rules against recorded engagement telemetry
  - Tune rules to reduce false positives (target <5% FP rate)
  - Document rules with detection logic, TTP mapping, and response guidance
- Maintain detection rule lifecycle:
  - Version control (Git), peer review, automated testing
  - Periodic rule review for relevance and accuracy
  - Rule retirement when TTPs become obsolete
  - Rule portability (Sigma → Wazuh, Splunk, Sentinel formats)

### Purple Team Execution (25%)

- Participate in all purple team exercises as the blue team lead:
  - **Pre-exercise** — deploy SIEM, onboard log sources, configure alerts, establish baseline
  - **During exercise** — monitor SIEM in real-time, track alerts, identify gaps, document detection latency
  - **Post-exercise** — analyze gaps, write new rules, tune existing rules, produce purple team report
- Work with Senior Red Team Operator to:
  - Design purple team exercise scenarios covering specific MITRE ATT&CK techniques
  - Identify which TTPs to test per exercise (gap-driven, not coverage-driven)
  - Validate detection coverage in real-time during TTP execution
  - Iterate: red team adjusts TTP → you adjust detection → re-test
- Produce purple team exercise reports for clients:
  - Detection coverage matrix (what was detected, what was missed)
  - Detection latency metrics (time from TTP execution to alert)
  - Gap analysis with prioritised remediation recommendations
  - Delivered detection rules package

### SIEM Engineering & Operations (20%)

- Design, deploy, and maintain Wazuh + ELK stack for division operations:
  - Architecture: Wazuh manager, Wazuh indexer, Wazuh dashboard, Elasticsearch cluster, Kibana
  - Sizing and scaling for engagement requirements (single-engagement vs national exercise)
  - High availability for operational deployments
- Onboard and configure log sources:
  - Windows — Security event logs, Sysmon, PowerShell logs, WMI activity
  - Linux — auth logs, auditd, syslog, journald
  - Network — Zeek, Suricata, firewall logs, proxy logs
  - Cloud — AWS CloudTrail, Azure AD, GCP Audit logs (where applicable)
  - Application — web server logs, database logs, custom application logs
- Develop and maintain parsers, decoders, and rules:
  - Wazuh decoders for custom log formats
  - Wazuh rules mapped to MITRE ATT&CK
  - Correlation rules for multi-stage attack detection
  - Alert tuning — threshold adjustments, noise reduction, whitelist management
- Deploy and manage Wazuh agents across engagement environments:
  - Windows, Linux, macOS agent deployment
  - Agent configuration and policy management
  - Agent health monitoring and troubleshooting

### MITRE ATT&CK Coverage Management (10%)

- Maintain division detection coverage matrix:
  - Map all detection rules to specific MITRE ATT&CK techniques and sub-techniques
  - Track coverage percentage across tactics and techniques
  - Identify high-priority gaps (critical techniques with no detection)
  - Prioritise rule development based on gap analysis and threat relevance
- Use MITRE ATT&CK Navigator for visualisation and planning
- Align coverage with Malaysian threat landscape (prioritise techniques used by Akira, BumbleBee, regional APTs)
- Contribute to ATT&CK evaluation and mapping for national cyber exercise design

### Threat Hunting (10%)

- Conduct proactive threat hunts based on:
  - Dark web intelligence (actor TTPs, emerging tool usage)
  - Red team engagement findings (TTPs that might exist in client environment)
  - Emerging threat intelligence (new TTPs, new attack tools)
  - Hypothesis-driven hunting ("if this TTP is present, what would it look like in logs?")
- Develop hunt playbooks for repeatable proactive detection
- Document hunt findings with detection opportunities for rule development
- Use ELK/Kibana for interactive hunting (KQL, Lucene, ES|QL queries)

### Client Delivery & National Library (5%)

- Package detection rules for client delivery after engagements:
  - Sigma rules (portable, vendor-neutral format)
  - Wazuh rules (ready to deploy)
  - Splunk SPL (for clients using Splunk)
  - Microsoft Sentinel KQL (for clients using Sentinel)
  - Documentation per rule — detection logic, TTP mapping, response playbook
- Maintain and grow the national detection rule library:
  - All rules version-controlled, tagged by sector, technique, and maturity
  - Library becomes strategic asset — grows with each engagement
  - Target: 100+ rules by Month 9, 500+ by Month 16
  - Library access can be offered as subscription product (future revenue)

---

## Requirements

### Essential Qualifications

- Malaysian citizen or PR (national capability preference)
- Bachelor's degree in Computer Science, Information Security, Cybersecurity, or equivalent demonstrated experience
- 4–7 years cybersecurity experience
- 2+ years SIEM engineering or detection engineering experience
- Demonstrated experience writing detection rules (Sigma, YARA, Wazuh, Splunk SPL, or equivalent)

### Essential Technical Skills

**SIEM Engineering:**
- Wazuh — deployment, configuration, agent management, rule writing, decoder development
- Elasticsearch + Kibana — indexing, querying (KQL, Lucene), dashboards, visualisations
- Splunk — SPL queries, dashboards, alerts (for client compatibility)
- Microsoft Sentinel — KQL queries, analytics rules (for client compatibility)
- Log shipping — Filebeat, Winlogbeat, auditbeat, Logstash

**Detection Rule Writing:**
- Sigma rules — fluent in Sigma syntax, rule structure, rule modifiers
- YARA — for malware detection and classification
- Wazuh rules — rule syntax, decoders, local rule overrides
- Rule testing methodology — false positive testing, true positive validation, edge case testing
- Rule lifecycle — development, testing, deployment, tuning, retirement

**MITRE ATT&CK:**
- Fluent in ATT&CK framework — tactics, techniques, sub-techniques
- ATT&CK mapping — map detections to techniques, map adversary behaviour to techniques
- ATT&CK Navigator — coverage visualisation and gap analysis
- ATT&CK Evaluations — understanding of vendor detection results

**Operating Systems & Internals:**
- Windows internals — event logs, Sysmon, PowerShell logging, WMI, registry, services
- Linux internals — syslog, auditd, journald, file system monitoring, process monitoring
- Network protocols — SMB, Kerberos, NTLM, LDAP, DNS, HTTP/HTTPS
- Understanding of attack techniques at OS level (what logs they generate)

**Threat Hunting:**
- Hypothesis-driven hunting methodology
- KQL, Lucene, or SPL for interactive hunting
- Understanding of behavioural analytics vs signature-based detection
- Baseline anomaly detection (what's normal, what's suspicious)

**Purple Team:**
- Experience working alongside red team operators
- Real-time detection monitoring during active attacks
- Gap analysis and rapid rule development
- Purple team reporting and client delivery

### Essential Certifications (one or more)

- GCIA (GIAC Certified Intrusion Analyst)
- GCIH (GIAC Certified Incident Handler)
- GREM (GIAC Reverse Engineering Malware) — for malware detection focus
- SANS SEC599 (Defeating Advanced Adversaries) or equivalent
- Or equivalent demonstrated capability through detection rule portfolio

### Preferred

- GCFA (GIAC Certified Forensic Analyst)
- OSCP or equivalent red team certification (understand the attack side)
- Experience with Wazuh specifically (not just Splunk/Sentinel)
- Experience in national cyber exercise context
- Published detection engineering content (Sigma rules, blog posts, GitHub)
- Active in detection engineering community (Sigma HQ, Detection Engineering Summit)

### Language

- English (fluent — required for technical work and rule documentation)
- Bahasa Malaysia (conversational minimum — preferred for client delivery)

---

## What You'll Be Working With

### Daily Tools

| Category | Tools |
|----------|-------|
| SIEM | Wazuh (manager, indexer, dashboard), Elasticsearch, Kibana |
| Log Shipping | Filebeat, Winlogbeat, auditbeat, Logstash |
| Detection | Sigma rules, YARA, Wazuh rules |
| Frameworks | MITRE ATT&CK, ATT&CK Navigator, D3FEND |
| Hunting | KQL, Lucene, ES\|QL, Sigma |
| Development | Python (rule automation, testing), Git (version control) |
| Lab | Isolated Wazuh + ELK environment for rule testing |
| OS | Ubuntu Server (SIEM), Windows (agent testing), Linux (agent testing) |

### Purple Team Exercise Workflow

```
1. Pre-Exercise Planning (Week Before)
   - Red team proposes TTPs to test
   - You identify which TTPs have existing detections
   - You identify gaps (TTPs with no detection)
   - Deploy/verify SIEM and log sources at target environment
   - Configure alerts and dashboards for exercise

2. Exercise Execution (Live)
   - Red team executes TTPs
   - You monitor SIEM in real-time
   - Document: which TTPs generated alerts, which didn't
   - Measure detection latency (TTP execution → alert fired)
   - Identify false positives and noise

3. Post-Exercise (Days After)
   - Analyse detection gaps
   - Write new Sigma rules for missed TTPs
   - Tune existing rules for false positives
   - Test rules against recorded telemetry
   - Produce purple team report for client
   - Add validated rules to national detection library
```

---

## Performance Expectations

### First 90 Days

- Wazuh + ELK stack deployed and operational in division lab
- First purple team exercise completed (internal, with Senior Operator)
- 15+ detection rules written and tested
- Detection coverage baseline established (MITRE ATT&CK mapping)
- Log source onboarding runbooks created

### Year 1

- 4–6 purple team exercises delivered (one per red team engagement)
- 100+ detection rules in national library
- Detection coverage: 60%+ of priority MITRE ATT&CK techniques
- Detection latency: <5 minutes for 80% of tested TTPs
- False positive rate: <5% across all rules
- Client detection packages delivered for all engagements
- Threat hunts conducted: 12+ (one per month)

---

## Compensation

| Component | Range |
|-----------|-------|
| Monthly salary | RM 7,000 – RM 10,000 |
| Annual bonus | Performance-linked, up to 2 months |
| Benefits | EPF, SOCSO, medical, dental, optical |
| Training budget | RM 6,000/year (certifications, conferences) |
| Conference attendance | Minimum 1 international + 2 local per year |

---

## Why This Role

Detection engineers in most organisations sit in a SOC, writing alerts for things that already happened. This role is different. You're embedded in a red team division, working in real-time with the operator who's executing the attack. You see the attack happen, you see what the SIEM catches, and you see what it misses. Then you write the rule that closes the gap. Every engagement makes the national detection library stronger. Every rule you write is a piece of Malaysian cyber resilience infrastructure.

The library you build doesn't disappear when a project ends. It compounds. By Year 2, you'll have 500+ rules covering the Malaysian threat landscape — a strategic asset no other Malaysian cybersecurity provider has.

---

**To apply:** Send CV, cover letter, and detection engineering portfolio (Sigma rules, Wazuh rules, blog posts, GitHub contributions, or purple team reports with sensitive details redacted) to [HR contact to be inserted].

**Classification:** INTERNAL — for HR firm distribution
