# Local Models Setup — Qwen/Kimi

**Status:** Configured for your local models
**Date:** 2026-06-14

---

## Your Available Models

| Model | Purpose | Configured As |
|-------|---------|---------------|
| **Qwen/Qwen3.5-122B** | Primary LLM | `llm.model` |
| **Qwen/Qwen3.5-27B** | Fast LLM | `llm.fast_model` |
| **moonshotai/Kimi-K2.5** | Alternative LLM | Available |
| **Qwen/Qwen3.5-397B-A17B** | Alternative LLM | Available |

---

## Configuration Files Updated

### `.env` (No External API Keys Needed)

```bash
ANTHROPIC_API_KEY=not-needed
OPENAI_API_KEY=not-needed
FALKORDB_HOST=localhost
FALKORDB_PORT=6379
POSTGRES_PASSWORD=research-stack-postgres-secure-password
OPENSTINGER_DB_URL=postgresql+asyncpg://openstinger:research-stack-postgres-secure-password@localhost:5433/openstinger
```

### `config.yaml` (Local Endpoints)

```yaml
llm:
  provider: openai  # OpenAI-compatible
  model: Qwen/Qwen3.5-122B
  fast_model: Qwen/Qwen3.5-27B
  llm_base_url: "http://localhost:8000/v1"  # ← UPDATE THIS
  embedding_provider: openai
  embedding_model: Qwen/Qwen3-embedding-8B  # ← UPDATE THIS
  embedding_base_url: "http://localhost:8000/v1"  # ← UPDATE THIS

falkordb:
  vector_dimensions: 1024  # ← Match your embedding model output
```

---

## ⚠️ Action Required: Update Endpoints

### Step 1: Find Your Model Server Endpoint

**If using vllm:**
```bash
# Check what's running
ps aux | grep vllm
# or
curl http://localhost:8000/v1/models
```

**If using Ollama:**
```bash
ollama list
curl http://localhost:11434/api/tags
```

**If using TGI (Hugging Face):**
```bash
curl http://localhost:8080/info
```

---

### Step 2: Update config.yaml

Replace the placeholder URLs with your actual endpoints:

```yaml
llm:
  # If vllm on port 8000:
  llm_base_url: "http://localhost:8000/v1"
  embedding_base_url: "http://localhost:8000/v1"
  
  # If Ollama:
  # llm_base_url: "http://localhost:11434/v1"
  # embedding_base_url: "http://localhost:11434/v1"
  
  # If different ports for LLM vs embeddings:
  # llm_base_url: "http://localhost:8000/v1"
  # embedding_base_url: "http://localhost:8001/v1"
```

---

### Step 3: Set Vector Dimensions

Match `vector_dimensions` to your embedding model's output:

| Embedding Model | Dimensions | config.yaml Setting |
|-----------------|------------|---------------------|
| Qwen3-embedding-8B | 4096 | `vector_dimensions: 4096` |
| nomic-embed-text | 768 | `vector_dimensions: 768` |
| mxbai-embed-large | 1024 | `vector_dimensions: 1024` |
| all-minilm | 384 | `vector_dimensions: 384` |

---

## Test Your Setup

### Test LLM Endpoint

```bash
curl http://localhost:8000/v1/models \
  -H "Authorization: Bearer not-needed"
```

Expected output:
```json
{
  "data": [
    {"id": "Qwen/Qwen3.5-122B", ...},
    {"id": "Qwen/Qwen3.5-27B", ...}
  ]
}
```

### Test Embedding Endpoint

```bash
curl http://localhost:8000/v1/embeddings \
  -H "Authorization: Bearer not-needed" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "Qwen/Qwen3-embedding-8B",
    "input": "test embedding"
  }'
```

Expected output:
```json
{
  "data": [
    {
      "embedding": [0.1, 0.2, ...],
      "index": 0
    }
  ]
}
```

---

## Start OpenStinger MCP Server

Once endpoints are configured:

```bash
cd /home/p62operator/.openclaw/workspace/openstinger
source .venv/bin/activate
python -m openstinger.mcp.server
```

---

## Troubleshooting

### Connection Refused

```
Error: Connection refused to http://localhost:8000/v1
```

**Fix:** Update `llm_base_url` and `embedding_base_url` to your actual endpoint.

### Vector Dimension Mismatch

```
Error: Embedding dimension 4096 does not match configured 1536
```

**Fix:** Update `falkordb.vector_dimensions` to match your embedding model.

### Model Not Found

```
Error: Model 'Qwen/Qwen3-embedding-8B' not found
```

**Fix:** Either:
1. Load the embedding model in your server
2. Or use a different embedding model you have available
3. Or install Ollama + nomic-embed-text as fallback

---

## Alternative: Use Ollama for Embeddings Only

If you don't have Qwen embeddings locally:

**1. Install Ollama:**
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

**2. Pull embedding model:**
```bash
ollama pull nomic-embed-text
```

**3. Update config.yaml:**
```yaml
llm:
  provider: openai
  model: Qwen/Qwen3.5-122B
  fast_model: Qwen/Qwen3.5-27B
  llm_base_url: "http://localhost:8000/v1"  # Your vllm
  
  embedding_provider: ollama
  embedding_model: nomic-embed-text
  ollama_host: "http://localhost:11434"

falkordb:
  vector_dimensions: 768  # nomic-embed-text output
```

---

## Summary

| Component | Configuration | Status |
|-----------|---------------|--------|
| **LLM** | Qwen/Qwen3.5-122B | ✅ Configured |
| **Fast LLM** | Qwen/Qwen3.5-27B | ✅ Configured |
| **Embeddings** | Qwen3-embedding-8B | ⚠️ Needs endpoint |
| **Vector DB** | FalkorDB (1024 dims) | ⚠️ Match to embedding |
| **API Keys** | None (local) | ✅ Not needed |

---

**Next:** Update `config.yaml` with your actual endpoints, then test with:
```bash
python -m openstinger.mcp.server
```
