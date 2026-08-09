# Ollama Setup for Embeddings

**Required:** Your external API (arasintegrasi.ai) doesn't provide embedding models, so we need **local embeddings** via Ollama.

---

## Quick Install

### Step 1: Install Ollama

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

This will:
- Download Ollama (~300MB)
- Install to `/usr/local/bin/ollama`
- Start the Ollama service

### Step 2: Pull Embedding Model

```bash
ollama pull nomic-embed-text
```

This downloads the **nomic-embed-text** model (~270MB) which outputs **768-dimensional** vectors.

**Alternative models:**
```bash
# Larger, more accurate (1024 dims)
ollama pull mxbai-embed-large

# Smaller, faster (384 dims)
ollama pull all-minilm
```

### Step 3: Verify Installation

```bash
# Check Ollama is running
ollama list

# Test embedding
ollama run nomic-embed-text "test embedding"
```

---

## Configuration Already Set

Your `config.yaml` is already configured for Ollama:

```yaml
llm:
  # External LLM (arasintegrasi.ai)
  provider: openai
  model: Qwen/Qwen3.5-122B
  fast_model: Qwen/Qwen3.5-27B
  llm_base_url: "https://model.arasintegrasi.ai/v1"
  
  # Local embeddings (Ollama)
  embedding_provider: ollama
  embedding_model: nomic-embed-text
  ollama_host: "http://localhost:11434"

falkordb:
  vector_dimensions: 768  # Matches nomic-embed-text
```

---

## After Installation

### Start OpenStinger

```bash
cd /home/p62operator/.openclaw/workspace/openstinger
source .venv/bin/activate
python -m openstinger.mcp.server
```

### Test Memory Tools

```bash
# Test memory query
mcporter call openstinger.memory_query \
  --args '{"query": "cyber threat intelligence", "limit": 5}'

# Add a test memory
mcporter call openstinger.memory_add \
  --args '{"content": "Test research finding", "source": "test-task"}'
```

---

## Troubleshooting

### Ollama Not Running

```bash
# Start manually
ollama serve

# Or check systemd service
systemctl status ollama
```

### Connection Refused

```
Error: Connection refused to http://localhost:11434
```

**Fix:** Ensure Ollama is running:
```bash
ollama serve &
```

### Model Not Found

```
Error: model 'nomic-embed-text' not found
```

**Fix:** Pull the model:
```bash
ollama pull nomic-embed-text
```

### Wrong Vector Dimensions

```
Error: Embedding dimension mismatch
```

**Fix:** Update `config.yaml`:
```yaml
falkordb:
  vector_dimensions: 768  # nomic-embed-text
  # OR
  vector_dimensions: 1024  # mxbai-embed-large
  # OR
  vector_dimensions: 384   # all-minilm
```

---

## Summary

| Component | Source | Model | Status |
|-----------|--------|-------|--------|
| **LLM** | arasintegrasi.ai | Qwen/Qwen3.5-122B | ✅ Configured |
| **Fast LLM** | arasintegrasi.ai | Qwen/Qwen3.5-27B | ✅ Configured |
| **Embeddings** | Local Ollama | nomic-embed-text | ⏳ Install Ollama |
| **Vector DB** | FalkorDB | 768 dims | ✅ Configured |

---

**Next:** Install Ollama and pull the embedding model, then start the MCP server.
