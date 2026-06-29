# Embedding API Access Request

**Date:** 2026-06-28  
**Requestor:** DAF  
**System:** OpenClaw Truth Validation Pipeline  
**Priority:** Medium (enables trust/verification infrastructure)

---

## 🎯 Purpose

Enable **semantic memory search** for the truth validation system. This allows:

1. **Automated fact-checking** — Cross-reference claims against prior briefs, source data, and corrections
2. **Citation trail** — Every output claim traceable to source (`Source: <file#line>` or `Source: <URL>`)
3. **Feedback loop** — Human corrections captured and synthesized to improve system accuracy over time
4. **Hallucination prevention** — Multi-source verification before output generation

**Business Impact:** Reduces manual verification burden, increases trust in AI-generated analysis, creates audit trail for political intelligence briefs.

---

## 🔧 Technical Requirements

### Embedding Provider

| Field | Value |
|-------|-------|
| **API Type** | OpenAI-compatible |
| **Model** | `text-embedding-3-small` or equivalent (768+ dimensions) |
| **Endpoint** | `<YOUR_BASE_URL>/v1/embeddings` |
| **Auth** | Bearer token (API key) |
| **Rate Limit** | ~500 requests/day (initial indexing), ~50 requests/day (steady state) |

### Current Configuration

```json
{
  "agents.defaults.memorySearch": {
    "enabled": true,
    "provider": "openai",
    "remote": {
      "baseUrl": "<TO_BE_PROVIDED>",
      "apiKey": "<TO_BE_PROVIDED>"
    }
  }
}
```

---

## 🔐 Security & Governance

### Data Sent to Embedding API

| Data Type | Sensitivity | Volume |
|-----------|-------------|--------|
| Memory file content (MEMORY.md, memory/*.md) | Internal analysis notes | ~20KB/day |
| Political brief drafts | Pre-publication analysis | ~10KB/brief |
| Source registry metadata | Public source URLs | ~1KB/day |
| **NOT sent:** PII, credentials, classified data | — | — |

### Retention

- Embeddings stored locally in `~/.openclaw/memory-vectors/`
- No persistent storage on embedding provider side (stateless API calls)
- Can disable/flush embeddings at any time

### Access Control

- API key scoped to embedding-only (no chat/completions access)
- Rate-limited to prevent cost overruns
- Logged for audit trail

---

## 📊 Cost Estimate

**Assumptions:**
- `text-embedding-3-small`: $0.02 / 1M tokens
- Average embedding: ~500 tokens per memory file
- Daily volume: 40 files × 500 tokens = 20K tokens/day

**Monthly Cost:**
```
20K tokens/day × 30 days = 600K tokens/month
600K tokens × $0.02 / 1M = $0.012/month
```

**Estimated cost: < $0.05/month** (negligible)

---

## 🚀 Implementation Plan

### Phase 1: Access Provisioning (1-2 days)
- [ ] CTO approves request
- [ ] API key generated (embedding-only scope)
- [ ] Base URL provided
- [ ] Rate limit configured

### Phase 2: Configuration (same day)
```bash
openclaw config set agents.defaults.memorySearch.provider openai
openclaw config set agents.defaults.memorySearch.remote.baseUrl <URL>
openclaw config set agents.defaults.memorySearch.remote.apiKey <KEY>
openclaw gateway restart
```

### Phase 3: Validation (1 day)
- [ ] Memory search functional (`memory_search` tool works)
- [ ] Initial indexing complete (war-room + runbooks collections)
- [ ] Truth validator gate tested end-to-end

### Phase 4: Production (ongoing)
- [ ] Dreaming cycle enabled (3 AM UTC synthesis)
- [ ] First feedback loop captured
- [ ] Monthly review scheduled

---

## ⚠️ Impact if Denied

| Capability | Status Without Embeddings |
|------------|---------------------------|
| Truth validation gate | ✅ Works (manual source lookup) |
| Multi-source verification | ✅ Works (script-based) |
| Citation generation | ✅ Works (file-based) |
| **Semantic memory search** | ❌ **Disabled** |
| **Automated cross-reference** | ❌ **Disabled** |
| **Dreaming cycle synthesis** | ❌ **Limited** (keyword-only) |
| **Feedback loop automation** | ⚠️ Manual capture required |

**Bottom line:** Core validation works, but system cannot self-improve or auto-retrieve relevant prior analysis.

---

## 📞 Contact

**Technical Questions:** DAF (OpenClaw operator)  
**System Owner:** DAF  
**Escalation:** CTO office

---

## ✅ Approval

- [ ] Approved — API key + base URL provided
- [ ] Approved with conditions: _______________
- [ ] Denied — Reason: _______________

**Approved by:** _______________  
**Date:** _______________
