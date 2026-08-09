# git-005: Clearwing (Lazarus-AI)

**Repository ID:** git-005  
**Name:** Clearwing  
**Organization:** Lazarus-AI  
**URL:** https://github.com/Lazarus-AI/clearwing  
**Classification:** TLP:AMBER (Dual-Use Offensive Security Tool)  
**Registered:** 2026-04-25  
**Status:** Registered — Pending Review  

---

## Executive Summary

**Clearwing** is an autonomous vulnerability scanner and source-code hunter inspired by Anthropic's Glasswing. Built on genai-pyo3 (Rust-backed LLM runtime), it provides dual-mode offensive security capabilities:

1. **Network Pentest Agent** — ReAct-loop agent with 63 bind-tools for live target scanning
2. **Source-Code Hunter** — File-parallel agent-driven pipeline for vulnerability discovery
3. **N-Day Exploit Pipeline** — CVE-based exploit development and validation
4. **Reverse Engineering Pipeline** — Ghidra decompilation + LLM source reconstruction + hybrid validation
5. **Campaign Orchestration** — Multi-repo coordination with shared budget and checkpoint/resume
6. **Responsible Disclosure** — Human-in-the-loop workflow with MITRE/HackerOne templates

**GovSec Relevance:** CRITICAL — Sovereign vulnerability assessment capability for CSM, MINDEF, NACSA operational deployments.

---

## Technical Profile

| Attribute | Value |
|-----------|-------|
| **Language** | Python 3.10+ |
| **Runtime** | genai-pyo3 (Rust-backed, native wheels) |
| **LLM Providers** | Anthropic, OpenAI, OpenRouter, Ollama, LM Studio, Together, Groq, DeepSeek, MiniMax, Gemini, any OpenAI-compatible |
| **Sandboxing** | Docker (Kali container), seccomp, ASan/UBSan |
| **Installation** | `uv sync --all-extras` (recommended) or `pip install` |
| **License** | MIT |
| **Version** | 1.0.0 (tagged release) |

---

## Capabilities Matrix

| Capability | Description | GovSec Application |
|------------|-------------|-------------------|
| **Network Scan** | Port scanning, service detection, vulnerability detection | MINDEF BSEP infrastructure audit |
| **Source Hunt** | File ranking, parallel hunter agents, ASan/UBSan crash validation | CSM threat intel, CBOM vulnerability mapping |
| **N-Day Pipeline** | Build vulnerable version, develop exploits, validate patches | NACSA national vulnerability database |
| **Reverse Engineering** | Ghidra decompilation, LLM source reconstruction, hybrid validation | MINDEF closed-source binary analysis |
| **Campaign Orchestration** | Multi-repo coordination, shared budget, checkpoint/resume | CSM multi-agency vulnerability assessment |
| **Responsible Disclosure** | MITRE/HackerOne templates, SHA-3 commitments, timeline tracking | NACSA coordinated vulnerability disclosure |
| **Benchmarking** | OSS-Fuzz crash severity ladder, A/B testing framework | CSM model evaluation, capability validation |

---

## GovSec Use Case Mapping

| Use Case | Organization | Priority | Timeline | Revenue Potential |
|----------|--------------|----------|----------|-------------------|
| **Sovereign Vulnerability Assessment** | MINDEF BSEP | P1 | May 15-30 | RM 200K-300K |
| **CBOM Vulnerability Mapping** | CSM R&D Labs | P1 | May 20-30 | RM 150K-250K |
| **National Vulnerability Database** | NACSA | P1 | June 1-15 | RM 300K-500K |
| **Closed-Source Binary Analysis** | MINDEF 91 RSD | P2 | June 15-30 | RM 100K-200K |
| **Multi-Agency Campaign** | CSM + NACSA + MINDEF | P2 | July 1-15 | RM 500K-800K |

**Total Pipeline:** RM 1.25M - 2.05M

---

## Integration Assessment

### Athena 5-Vector Score

| Vector | Score (0-10) | Rationale |
|--------|--------------|-----------|
| **Influence** | 9.0 | Positions CSM/MINDEF/NACSA as sovereign vulnerability assessment capability; national-scale impact |
| **Revenue** | 8.5 | RM 1.25M-2.05M pipeline; 4 POC opportunities; high-margin deployment model |
| **Infrastructure** | 9.5 | Self-host capable, air-gapped deployment, no external API dependency (Ollama/vLLM support) |
| **Intelligence** | 9.5 | Autonomous vulnerability discovery, N-day exploit development, reverse engineering pipeline |
| **Optionality** | 8.5 | Multiple deployment modes (network pentest, source hunt, RE, campaign); extensible tool framework |
| **Weighted Total** | **9.0/10** | Priority integration candidate (≥18/25 threshold exceeded) |

---

## Risk Assessment

| Risk | Severity | Mitigation |
|------|----------|------------|
| **Dual-Use Liability** | HIGH | Authorized use only; scope documentation; legal authorization required; human-in-the-loop exploit gating |
| **Operational Security** | MEDIUM | Audit trails, behavior monitoring, seccomp sandboxing, credential isolation |
| **Learning Curve** | MEDIUM | Comprehensive docs (quickstart, providers, architecture, CLI); interactive setup wizard; `clearwing doctor` validation |
| **Resource Requirements** | LOW | Prebuilt wheels (no Rust toolchain needed); Docker optional for sandboxing; scalable concurrency |
| **Vendor Dependency** | LOW | Supports 10+ LLM providers; self-host capable (Ollama, vLLM, LM Studio); provider routing per task |

---

## Integration Recommendation

**Priority:** P1 — **ESCALATE TO DAF** (Athena score 9.0/10, exceeds 18/25 threshold)

**Recommended Path:**
1. **Week 1 (May 1-7):** Clone, install, run `clearwing doctor`, test with Ollama/vLLM
2. **Week 2 (May 8-14):** Source hunt test repo (e.g., FFmpeg), validate findings, benchmark models
3. **Week 3 (May 15-21):** CSM POC scoping (SpankRAT codebase or internal target)
4. **Week 4 (May 22-30):** MINDEF BSEP infrastructure scan (authorized scope)

**Deployment Model:**
- **CSM:** Self-host with Ollama (air-gapped capable)
- **MINDEF:** Self-host with vLLM (sovereign LLM runtime)
- **NACSA:** Hybrid (local + OpenRouter for non-sensitive targets)

**MCP Tool Integration Candidate:**
- `clearwing_scan_target` — Network pentest orchestration
- `clearwing_sourcehunt` — Source code vulnerability hunting
- `clearwing_nday_exploit` — N-day exploit pipeline
- `clearwing_reveng` — Reverse engineering pipeline

---

## Installation & Testing Plan

```bash
# Week 1: Installation & Setup
git clone https://github.com/Lazarus-AI/clearwing.git
cd clearwing
uv sync --all-extras
source .venv/bin/activate
clearwing doctor  # Environment validation
clearwing setup   # Interactive provider configuration

# Week 2: Test Source Hunt (small repo)
clearwing sourcehunt https://github.com/example/small-project --depth standard

# Week 3: Test Network Scan (authorized target)
clearwing scan 192.168.1.10 -p 22,80,443 --detect-services

# Week 4: CSM POC Scoping
clearwing campaign run csm-poc-campaign.yaml
```

---

## GovSec Deployment Considerations

| Consideration | Recommendation |
|---------------|----------------|
| **Legal Authorization** | Written scope required for all network scans; CSM/MINDEF/NACSA legal review mandatory |
| **Data Residency** | All findings stored locally; knowledge graph on-premises; no cloud telemetry |
| **Air-Gapped Deployment** | Use Ollama/vLLM for LLM; no external API calls; offline model downloads |
| **Human-in-the-Loop** | Exploit attempts gated through approval workflow; disclosure requires manual review |
| **Audit Trails** | Enable event bus logging; retain all findings with evidence levels; SHA-3 commitments for priority |
| **Integration with OC-CIL** | Feed findings into OC-CIL knowledge base (Phase 2); correlate with AIL Framework threat intel |

---

## Next Actions

| Action | Owner | Due Date | Status |
|--------|-------|----------|--------|
| **Review Clearwing capability** | DAF, Hadri, Fuad | Apr 26 | 🔲 Pending |
| **Decision: Integrate vs. Reference** | DAF | Apr 28 | 🔲 Pending |
| **If INTEGRATE: Clone & test** | Fuad | May 1-7 | 🔲 Pending |
| **If INTEGRATE: CSM POC scoping** | DAF + Zulfeka | May 10-15 | 🔲 Pending |
| **If REFERENCE: Document as external capability** | Second | Apr 26 | 🔲 Pending |

---

## Registry Metadata

- **Registry Version:** 1.2 (updated 2026-04-25)
- **Total Repositories:** 5
- **P1 Priority:** 5/5 (100%)
- **Sovereign Capable:** 5/5 (100%)
- **Air-Gapped Capable:** 5/5 (100%)
- **Integration Recommended:** 4/5 (80%), 1/5 pending review

---

**Last Updated:** 2026-04-25 07:43 UTC  
**Reviewer:** Second (Git Capability Registry Advisor)  
**Status:** Registered — Pending DAF Review  

#git-005
#Clearwing
#LazarusAI
#VulnerabilityAssessment
#OffensiveSecurity
#GovSec
#CSM
#MINDEF
#NACSA
#P1Priority
