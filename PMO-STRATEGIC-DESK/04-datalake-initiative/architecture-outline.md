# PMO Strategic Data Lake — Architecture Outline

**Initiative:** Co-Development of PMO Strategic Data Lake  
**Partner:** Bahagian Data Strategik × Aras Integrasi  
**Status:** Conceptual Framework (Pre-Session)  
**Version:** 1.0  
**Date:** 2026-07-09

---

## 🎯 Strategic Context

This architecture supports the **Co-Development of PMO Strategic Data Lake** strategic objective for Bahagian Data Strategik, enabling:

- Data-driven decision-making at PMO leadership level
- AI-assisted strategic analysis and briefing
- Secure, governed access to structured and unstructured data
- Future scalability for cross-agency data integration

---

## 🏗️ High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    PMO Strategic Data Lake                      │
│                   (Bahagian Data Strategik)                     │
└─────────────────────────────────────────────────────────────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
        ▼                     ▼                     ▼
┌───────────────┐   ┌─────────────────┐   ┌───────────────┐
│ Data Sources  │   │ AI Processing   │   │ Consumption   │
│               │   │ Layer           │   │ Layer         │
│ • Policy Docs │   │                 │   │               │
│ • Stakeholder │   │ • LLM Models    │   │ • Dashboards  │
│   Records     │──▶│ • Classification│──▶│ • Briefs      │
│ • Socio-Econ  │   │ • Tagging       │   │ • NL Query    │
│   Data        │   │ • Summarisation │   │ • Reports     │
│ • Meeting     │   │ • NL Query      │   │ • API Access  │
│   Notes       │   │                 │   │               │
└───────────────┘   └─────────────────┘   └───────────────┘
        │                     │                     │
        └─────────────────────┼─────────────────────┘
                              │
                              ▼
                    ┌─────────────────┐
                    │ Governance &    │
                    │ Security Layer  │
                    │                 │
                    │ • Access Control│
                    │ • Audit Logs    │
                    │ • Compliance    │
                    │ • Traceability  │
                    └─────────────────┘
```

---

## 📦 Component Breakdown

### 1. Data Ingestion Layer

**Purpose:** Bring data into the lake from diverse sources

| Component | Description | Technology Options |
|-----------|-------------|-------------------|
| **Batch Ingestion** | Scheduled imports from databases, file shares | Apache NiFi, Airflow |
| **Real-Time Ingestion** | Streaming data from APIs, webhooks | Kafka, Pulsar |
| **Document Ingestion** | PDF, DOCX, PPTX, email archives | Custom parsers, Tika |
| **API Connectors** | External data sources (e.g., DOSM, MAMPU) | REST, GraphQL |
| **Manual Upload** | Ad-hoc file uploads via secure portal | Web interface |

**Data Formats Supported:**
- **Structured:** CSV, JSON, XML, database exports
- **Unstructured:** PDF, DOCX, TXT, email, meeting transcripts
- **Semi-structured:** JSON, YAML, Markdown

---

### 2. Storage Layer

**Purpose:** Secure, scalable storage with appropriate access controls

| Tier | Purpose | Storage Type | Retention |
|------|---------|--------------|-----------|
| **Hot** | Frequently accessed data | SSD/Object Storage | 90 days |
| **Warm** | Periodic access | HDD/Object Storage | 1–2 years |
| **Cold** | Archive/compliance | Tape/Cold Storage | 7+ years |

**Security Features:**
- Encryption at rest (AES-256)
- Encryption in transit (TLS 1.3)
- Role-based access control (RBAC)
- Data classification tagging

---

### 3. AI Processing Layer

**Purpose:** AI-assisted data enrichment, classification, and query

| Capability | Description | Model Options |
|------------|-------------|---------------|
| **Document Classification** | Auto-tag documents by topic, sensitivity, type | Kimi-K2.5, Qwen3.5 |
| **Named Entity Recognition** | Extract people, orgs, locations, dates | Qwen3.5, GLM-5.2 |
| **Summarisation** | Generate executive summaries | Kimi-K2.6, Gemma-4 |
| **Semantic Search** | Vector-based similarity search | Embedding models |
| **Natural Language Query** | Convert NL questions to SQL/API calls | Qwen3.5, Kimi-K2.6 |
| **Anomaly Detection** | Identify outliers in socio-economic data | GLM-5.2, custom ML |
| **Trend Analysis** | Time-series pattern recognition | Custom ML + LLM |

**API Endpoint:** `https://model.arasintegrasi.ai/v1`

---

### 4. Retrieval & Query Layer

**Purpose:** Enable users to access and query data

| Interface | Description | Users |
|-----------|-------------|-------|
| **Natural Language Query** | Ask questions in plain language | All users |
| **Semantic Search** | Search by meaning, not keywords | Analysts |
| **SQL Interface** | Direct database queries (for technical users) | Data team |
| **API Access** | Programmatic access for integrations | Developers |
| **Dashboard UI** | Visual exploration and filtering | Leadership |

---

### 5. Consumption Layer

**Purpose:** Deliver insights to end users

| Output Type | Description | Example Use Cases |
|-------------|-------------|-------------------|
| **Strategic Briefs** | AI-generated policy/stakeholder briefs | Leadership meetings |
| **Dashboards** | Interactive visualisations | Operational monitoring |
| **Reports** | Automated periodic reports | Weekly/monthly updates |
| **Alerts** | Anomaly/threshold notifications | Risk monitoring |
| **API Responses** | Structured data for downstream systems | Integration workflows |

---

### 6. Governance & Security Layer

**Purpose:** Ensure compliance, security, and traceability

| Component | Description | Implementation |
|-----------|-------------|----------------|
| **Access Control** | RBAC, MFA, API key auth | Azure AD / Custom |
| **Audit Logging** | All queries and access logged | ELK Stack / Splunk |
| **Data Classification** | Public/Internal/Confidential/Restricted | Auto-tagging + manual |
| **Compliance** | PDPA, Official Secrets Act, MAMPU | Policy engine |
| **Traceability** | Link outputs to source documents | Metadata tracking |
| **Human Approval** | Workflow for sensitive outputs | Approval queue |

---

## 🔐 Security Architecture

### Network Security

```
┌─────────────────────────────────────────────────────┐
│              PMO Network (Secure Zone)              │
│                                                     │
│  ┌─────────────┐      ┌─────────────────────────┐  │
│  │   Users     │─────▶│   API Gateway           │  │
│  │ (PMO Staff) │      │   (Authentication)      │  │
│  └─────────────┘      └───────────┬─────────────┘  │
│                                   │                │
│                                   ▼                │
│                        ┌──────────────────────┐   │
│                        │   Aras Integrasi     │   │
│                        │   AI Endpoint        │   │
│                        │   (External, TLS)    │   │
│                        └──────────────────────┘   │
│                                   │                │
│                                   ▼                │
│                        ┌──────────────────────┐   │
│                        │   Data Lake Storage  │   │
│                        │   (PMO Internal)     │   │
│                        └──────────────────────┘   │
└─────────────────────────────────────────────────────┘
```

### Access Control Model

| Role | Permissions | Example Users |
|------|-------------|---------------|
| **Viewer** | Read-only access to public/internal data | General staff |
| **Analyst** | Query, classify, generate briefs | Data strategists |
| **Admin** | Manage users, configure pipelines | IT team |
| **Approver** | Review/approve sensitive outputs | Leadership |

---

## 🚀 Implementation Phases

### Phase 1: Foundation (Months 1–2)

- [ ] Set up storage infrastructure
- [ ] Implement basic access control
- [ ] Ingest priority data sources (2–3)
- [ ] Deploy AI classification/tagging
- [ ] Pilot 1–2 use cases

### Phase 2: Expansion (Months 3–4)

- [ ] Expand data ingestion (5–10 sources)
- [ ] Implement natural language query
- [ ] Deploy dashboard UI
- [ ] Integrate audit logging
- [ ] Scale to 10–20 users

### Phase 3: Optimization (Months 5–6)

- [ ] Advanced analytics (trend/anomaly detection)
- [ ] Automated report generation
- [ ] Cross-agency API integrations
- [ ] Full governance framework operational
- [ ] Training and change management

---

## 📊 Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| **Data Sources Ingested** | 10+ sources by Month 6 | Count |
| **Active Users** | 20+ by Month 6 | Monthly active users |
| **Query Response Time** | <5 seconds (95th percentile) | Performance monitoring |
| **Brief Generation Time** | <10 minutes per brief | Time tracking |
| **User Satisfaction** | >80% positive feedback | Survey |
| **Governance Compliance** | 100% audit pass rate | Compliance review |

---

## 🔗 Related Documents

- `readiness-assessment.md` — Current state assessment
- `integration-roadmap.md` — Detailed implementation plan
- `../06-governance-security/ai-governance-checklist.md` — Governance requirements
- `../03-ai-cohort-program/pilot-tracking.md` — Pilot use cases

---

*This architecture is a conceptual framework. Final design will be refined based on the Data Lake Readiness Assessment and working session outcomes.*

**Next Review:** Post-session (after Bahagian Data Strategik assessment completed)
