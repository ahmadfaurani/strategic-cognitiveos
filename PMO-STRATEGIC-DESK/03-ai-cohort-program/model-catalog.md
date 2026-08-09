# AI Cohort Model Catalog

**API Endpoint:** `https://model.arasintegrasi.ai/v1`  
**Access:** 90-day validity (renewable)  
**Last Updated:** 2026-07-09

---

## Available Models

### 1. Moonshot AI — Kimi Series

| Model | Context Window | Strengths | Best For |
|-------|----------------|-----------|----------|
| `moonshotai/Kimi-K2.5` | ~128K tokens | Long-context reasoning, document analysis | Policy briefs, stakeholder analysis |
| `moonshotai/Kimi-K2.6` | ~128K tokens | Improved accuracy, faster inference | Real-time query, dashboard integration |

**Use Cases:**
- Strategic briefing (long document synthesis)
- Stakeholder mapping (multi-source analysis)
- Policy comparison (side-by-side evaluation)

---

### 2. Alibaba — Qwen Series

| Model | Context Window | Strengths | Best For |
|-------|----------------|-----------|----------|
| `Qwen/Qwen3.5-397B-A17B` | ~256K tokens | **Current default**, massive scale, multilingual | Complex reasoning, code generation, governance workflows |

**Use Cases:**
- **Current session model** (this is what I'm running on)
- Complex analytical workflows
- Code generation for data pipelines
- Multilingual document processing (BM/EN/ZH)

---

### 3. Google — Gemma Series

| Model | Context Window | Strengths | Best For |
|-------|----------------|-----------|----------|
| `google/gemma-4-31B-it` | ~32K tokens | Lightweight, fast, instruction-tuned | Quick queries, meeting summaries, workflow automation |

**Use Cases:**
- Meeting note summarisation
- Action item extraction
- Quick-turnaround briefs
- Internal workflow automation

---

### 4. Zhipu AI — GLM Series

| Model | Context Window | Strengths | Best For |
|-------|----------------|-----------|----------|
| `zai-org/GLM-5.2` | ~128K tokens | Strong reasoning, Chinese/English bilingual | Socio-economic analysis, cross-border data |

**Use Cases:**
- Socio-economic trend analysis
- Anomaly detection in datasets
- Bilingual report generation
- Public interest profiling

---

## Model Selection Guide

### By Use Case

| Use Case | Recommended Model | Alternative |
|----------|-------------------|-------------|
| **Strategic Briefing** | Kimi-K2.6 | Qwen3.5-397B |
| **Document Intelligence** | Kimi-K2.5 | GLM-5.2 |
| **Natural Language Query** | Gemma-4-31B | Kimi-K2.6 |
| **Meeting Intelligence** | Gemma-4-31B | Kimi-K2.5 |
| **Trend/Anomaly Detection** | GLM-5.2 | Qwen3.5-397B |
| **Report Generation** | Qwen3.5-397B | Kimi-K2.6 |
| **Semantic Search** | Kimi-K2.5 | GLM-5.2 |
| **Code/Data Pipeline** | Qwen3.5-397B | Gemma-4-31B |
| **Governance/Traceability** | Qwen3.5-397B | Kimi-K2.6 |

### By Priority

| Priority | Factor | Recommended Model |
|----------|--------|-------------------|
| **Speed** | Fastest response | Gemma-4-31B |
| **Accuracy** | Highest precision | Qwen3.5-397B |
| **Long Context** | Document synthesis | Qwen3.5-397B (256K) |
| **Multilingual** | BM/EN/ZH support | Qwen3.5-397B, GLM-5.2 |
| **Cost Efficiency** | Token optimization | Gemma-4-31B |

---

## API Usage Examples

### Basic Completion

```bash
curl https://model.arasintegrasi.ai/v1/chat/completions \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "Qwen/Qwen3.5-397B-A17B",
    "messages": [
      {"role": "user", "content": "Summarise this policy document..."}
    ],
    "max_tokens": 2000
  }'
```

### Streaming Response

```bash
curl https://model.arasintegrasi.ai/v1/chat/completions \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "moonshotai/Kimi-K2.5",
    "messages": [{"role": "user", "content": "..."}],
    "stream": true
  }'
```

---

## Key Expiry & Renewal

| Key Holder | Issued Date | Expiry Date | Renewal Status |
|------------|-------------|-------------|----------------|
| nazilah@pmo.gov.my | 2026-07-09 | 2026-10-07 | ⏳ Active |
| hishamuddin@pmo.gov.my | 2026-07-09 | 2026-10-07 | ⏳ Active |
| imran@pmo.gov.my | 2026-07-09 | 2026-10-07 | ⏳ Active |
| azrun@pmo.gov.my | 2026-07-09 | 2026-10-07 | ⏳ Active |
| shahril.shatar@pmo.gov.my | 2026-07-09 | 2026-10-07 | ⏳ Active |

**Renewal Process:** Contact Farul (farul@arasintegrasi.ai) 14 days before expiry.

---

## Performance Benchmarks

*To be populated after pilot testing*

| Model | Avg Response Time | Token/sec | Cost/1K tokens |
|-------|-------------------|-----------|----------------|
| Kimi-K2.5 | TBD | TBD | TBD |
| Kimi-K2.6 | TBD | TBD | TBD |
| Qwen3.5-397B | TBD | TBD | TBD |
| Gemma-4-31B | TBD | TBD | TBD |
| GLM-5.2 | TBD | TBD | TBD |

---

## Support & Documentation

- **API Docs:** [Internal Aras Integrasi Portal]
- **Technical Contact:** Farul Mohd Ghazali (farul@arasintegrasi.ai)
- **Strategic Contact:** DAF (daf@arasintegrasi.ai)

---

*This catalog will be updated as new models are added or performance data becomes available.*
