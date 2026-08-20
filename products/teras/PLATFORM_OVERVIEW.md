# Teras AI Platform — Product Overview

> **Classification:** HAK MILIK ARAS INTEGRASI SDN BHD — SULIT [INTERNAL ONLY]
> **Source:** DOC-20260820-003 — Teras AI Platform Presentation
> **Authority:** DAF (2026-08-20)
> **CTO Owner:** Farul (STK-20260803-006)

## What Teras Is

Teras is Aras Integrasi's enterprise AI platform — a unified platform that brings together people, applications, AI services, governance, and infrastructure to deliver trusted AI at enterprise scale.

## 5-Layer Architecture

1. **Sovereign AI Infrastructure** — GPU Compute (NVIDIA RTX PRO 6000 Blackwell), Storage, Network, Backup & DR, Physical Security, Security & Audit
2. **AI Services & Foundation Models** — LLM, RAG, Vision, Speech, OCR, Translation, Sentiment, Model Registry, Fine-tuning, Vector Store
3. **Governed AI Platform** — Identity & Access, API Gateway, AI Guardrails (content safety, bias detection, policy), Observability & Monitoring, Audit & Compliance
4. **Applications** — Akal Suite (Akal Assistant, Akal Coder, Work, Mobile), Developer APIs/SDKs. Integrations with Microsoft 365, Google Workspace, enterprise systems
5. **Users** — Employees, Officers, Developers, Partners

## Performance Benchmarks

| Model | GPUs | 1 User | 4 Users | 8 Users | 16 Users | 32 Users |
|-------|------|--------|---------|---------|----------|----------|
| Qwen3.5-397B | 4× RTX PRO 6000 | 136 tok/s | 342 tok/s | 472 tok/s | 605 tok/s | — |
| Qwen3.6-27B | 2× RTX PRO 6000 | 169 tok/s | 640 tok/s | 1,400 tok/s | 2,200 tok/s | 2,800 tok/s |

Measured at BF16 without quantization on Teras AI Platform deployed on-premise.

## Key Capabilities

- **Optimised Serving Kernel:** 20-25% higher throughput on identical GPUs
- **Tiered Model Serving:** routes each request to the right model
- **Token Usage Attribution:** by user, by application, by division
- **Sovereign Deployment:** all inference, storage, and logging remain within environment
- **Air-Gapped Deployment:** capable
- **Governance:** RBAC, IdP Integration, SIEM, Policy Enforcement, Immutable Audit Logs, Activity Monitoring, Regulatory Alignment
- **Managed Service:** 24/7 operations, SLA-driven, proactive support

## Target Customers

- MCMC (Malaysian Communications and Multimedia Commission)
- NSRD

## Role in CyberSecurity Practice

Teras serves as the **infrastructure layer for ALL three CyberSecurity Practice products** (DEC-20260820-009). Each product deploys as an application ON Teras, like Akal Suite.

### VoronCitadel (GRC & Digital Risk Quantification)
- GPU compute for Sovereign AI Copilot (narrative gen, evidence drafting, coverage suggestion)
- RAG infrastructure for AI Copilot context assembly
- API Gateway, Identity & Access (7 roles, 30 permissions), Audit infrastructure
- Multi-customer deployment isolation (eliminates RLS build)
- Eliminates: RLS build, DevOps hire, API gateway build, governance build, RAG pipeline build

### GovSec-TIP (National Cyber Threat Intelligence Platform)
- GPU compute for AI Analyst (NL queries, case AI, NLP auto-classification)
- RAG infrastructure (replaces in-house context assembly)
- Governance layer maps to Malaysian classification levels (Rahsia/Sensitif/Terhad/Pertidahan/Awam)
- Air-gapped deployment for classified intel platforms
- Multi-agency deployment isolation (each agency = Teras-managed instance)

### ChainSentry (Blockchain Forensics & Investigative Workbench)
- GPU compute for assisted classification (~20s → est. ~5-8s with Teras GPU + optimised kernel)
- OCR and Translation services for evidence processing
- Multi-tenant deployment isolation (resolves known single-tenant gap)
- RAG for dossier assembly with cited assessments
- Air-gapped for sensitive investigations

### Cross-Product Synergies
- Single identity layer across all 3 products
- Shared audit/compliance infrastructure
- Shared GPU pool (Qwen3.5-397B + Qwen3.6-27B serve all 3)
- Unified API gateway for customer integration
- Sovereign AI narrative: one platform, three products

## Related Records

- DOC-20260820-003 — Teras AI Platform Presentation (source PPTX)
- DEC-20260820-007 — Organizational Architecture
- DEC-20260820-008 — Teras as Infrastructure Layer for VoronCitadel POC (predecessor)
- DEC-20260820-009 — Teras as Infrastructure Layer for ALL 3 Products (current)
- INIT-20260820-003 — VoronCitadel POC Mode Activation
- STK-20260803-006 — Farul (CTO, Teras owner)
