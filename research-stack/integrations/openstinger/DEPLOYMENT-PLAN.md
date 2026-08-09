# OpenStinger Deployment Plan

## Executive Summary

**OpenStinger v0.8** is a portable memory and alignment layer for AI agents, exposing **30 MCP tools** across three tiers:
- **Tier 1 (Memory):** 11 tools for bi-temporal episodic memory
- **Tier 2 (Vault):** 11 tools for structured self-knowledge
- **Tier 3 (Gradient):** 8 tools for alignment evaluation

**Deployment Mode:** Alongside → Primary → Exclusive (phased adoption)

**Integration Point:** Research Automation Stack evidence store + skills library

---

## Architecture Overview

```
Research Stack Components:
├── SearXNG (discovery)
├── Firecrawl (acquisition)
├── DeerFlow (orchestration)
└── Evidence Store (PostgreSQL) ← OpenStinger enhances this

OpenStinger Components:
├── FalkorDB (bi-temporal graph + vector search)
├── PostgreSQL (operational audit DB)
├── MCP Server (30 tools on port 8766)
└── Vault (markdown self-knowledge)
```

---

## Deployment Phases

### Phase 1: Install & Configure (Day 1)

**Steps:**

```bash
# 1. Clone OpenStinger
cd /home/p62operator/.openclaw/workspace
git clone https://github.com/srikanthbellary/openstinger.git
cd openstinger

# 2. Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 3. Install
pip install -e "."

# 4. Configure environment
cp .env.example .env
cp config.yaml.example config.yaml
```

**Environment Configuration (.env):**

```bash
# LLM Provider (Anthropic or OpenAI-compatible)
ANTHROPIC_API_KEY=sk-ant-...

# Embeddings (OpenAI-compatible or Ollama for local)
OPENAI_API_KEY=sk-...

# FalkorDB (leave blank for local dev)
FALKORDB_PASSWORD=

# PostgreSQL
POSTGRES_PASSWORD=<secure_password>
```

**Config Updates (config.yaml):**

```yaml
agent_name: research-agent
agent_namespace: research-stack

ingestion:
  sessions_dir: "/home/p62operator/.openclaw/workspace/research-stack/sessions"

falkordb:
  host: localhost
  port: 6379
  password: ""
  vector_dimensions: 1536  # Match embedding model

operational_db:
  provider: postgresql
  postgresql_url: "postgresql+asyncpg://postgres:<password>@localhost:5432/openstinger"

llm:
  provider: anthropic
  model: claude-sonnet-4-6
  fast_model: claude-haiku-4-5-20251001
  embedding_model: text-embedding-3-large
  embedding_provider: openai
```

**Start Services:**

```bash
# Start FalkorDB + PostgreSQL
docker compose up -d

# Verify containers
docker compose ps
```

---

### Phase 2: Memory Harness Integration (Week 1)

**Start Tier 1 MCP Server:**

```bash
cd /home/p62operator/.openclaw/workspace/openstinger
source .venv/bin/activate
python -m openstinger.mcp.server
```

**Configure Research Stack to Use OpenStinger:**

The research stack will use OpenStinger for:
1. **Evidence deduplication** - 3-stage entity matching
2. **Semantic search** - Hybrid BM25 + vector search
3. **Bi-temporal tracking** - `valid_at` vs `recorded_at`

**MCP Configuration:**

```json
{
  "mcpServers": {
    "openstinger": {
      "baseUrl": "http://localhost:8766/sse"
    }
  }
}
```

**Test Memory Tools:**

```bash
# Test memory query
mcporter call openstinger.memory_query \
  --args '{"query": "cyber threat intelligence", "limit": 5}'

# Test memory add
mcporter call openstinger.memory_add \
  --args '{"content": "CVE-2024-1234 affects Apache Log4j", "source": "research-task-001"}'

# Check status
mcporter call openstinger.memory_namespace_status
```

---

### Phase 3: Evidence Store Integration (Week 2)

**Enhance Research Stack Schema:**

Add bi-temporal fields to `research_findings`:

```sql
-- Add bi-temporal tracking
ALTER TABLE research_findings 
ADD COLUMN valid_at TIMESTAMPTZ,
ADD COLUMN recorded_at TIMESTAMPTZ DEFAULT NOW();

-- Add OpenStinger entity references
ALTER TABLE research_findings
ADD COLUMN openstinger_entity_uuid UUID,
ADD COLUMN openstinger_episode_uuid UUID;

-- Create index for temporal queries
CREATE INDEX idx_findings_valid_at ON research_findings(valid_at);
CREATE INDEX idx_findings_recorded_at ON research_findings(recorded_at);
```

**Entity Deduplication Integration:**

When storing sources, use OpenStinger's 3-stage dedup:

```python
# Pseudocode for research stack
def store_source(url, content):
    # Stage 1: Exact match
    existing = openstinger.memory_search(query=url, search_type="entities")
    if existing:
        return existing.uuid
    
    # Stage 2: Fuzzy match (MinHash LSH)
    fuzzy = openstinger.memory_search(query=url, search_type="entities_fuzzy")
    if fuzzy and fuzzy.confidence > 0.85:
        return fuzzy.uuid
    
    # Stage 3: LLM semantic confirmation
    semantic = openstinger.memory_query(query=url, limit=1)
    if semantic and semantic.confidence > 0.90:
        return semantic.uuid
    
    # Create new entity
    return openstinger.memory_add(content=url, source="research-stack")
```

---

### Phase 4: StingerVault for Skills (Week 3)

**Configure Vault for Skills Library:**

The skills library becomes a StingerVault with 5 categories:

| Category | Purpose | Threshold |
|----------|---------|-----------|
| **IDENTITY** | Stack capabilities | 0.92 |
| **DOMAIN** | Research methodologies | 0.85 |
| **METHODOLOGY** | Workflows, patterns | 0.80 |
| **PREFERENCE** | Tool/config preferences | 0.75 |
| **CONSTRAINT** | Governance rules | 0.95 |

**Sync Skills to Vault:**

```bash
# Configure vault directory
# In config.yaml:
vault:
  vault_dir: "/home/p62operator/.openclaw/workspace/research-stack/skills/vault"
  categories:
    - IDENTITY
    - DOMAIN
    - METHODOLOGY
    - PREFERENCE
    - CONSTRAINT

# Start Tier 2
python -m openstinger.scaffold.mcp.server
```

**Test Vault Tools:**

```bash
# List vault notes
mcporter call openstinger.vault_note_list

# Get specific note
mcporter call openstinger.vault_note_get \
  --args '{"category": "DOMAIN", "name": "cyber-threat-intelligence"}'

# Ingest external knowledge
mcporter call openstinger.knowledge_ingest \
  --args '{"url": "https://cisa.gov/known-exploited-vulnerabilities", "category": "DOMAIN"}'
```

---

### Phase 5: Gradient Alignment for Governance (Week 4)

**Configure Gradient for Output Quality:**

Gradient evaluates research outputs against governance controls:

| Dimension | Research Stack Application |
|-----------|---------------------------|
| **Value Coherence** | Alignment with research ethics |
| **Identity Consistency** | Consistent with stack mandate |
| **Constraint Compliance** | Governance controls (privacy, legal) |
| **Content Safety** | No harmful recommendations |

**Start Tier 3 (Observe-Only Mode):**

```bash
# In config.yaml:
gradient:
  observe_only: true  # Start in observe-only
  alignment_threshold: 0.75
  drift_threshold: 0.65

# Start full server
python -m openstinger.gradient.mcp.server
```

**Test Alignment Tools:**

```bash
# Check gradient status
mcporter call openstinger.gradient_status

# Evaluate a research output
mcporter call openstinger.gradient_alignment_score \
  --args '{"response": "[Research finding text]", "context": "cyber-threat-intel"}'

# Check drift
mcporter call openstinger.gradient_drift_status

# Get operational dashboard
mcporter call openstinger.ops_status
```

**After Calibration (2-4 weeks):**

```yaml
# Switch to active mode
gradient:
  observe_only: false
  correction_enabled: true
  max_correction_recursion: 1
```

---

## Integration Points

### 1. Evidence Store Enhancement

**Current Schema:** PostgreSQL with 8 tables

**OpenStinger Adds:**
- Bi-temporal tracking (`valid_at`, `recorded_at`)
- Entity deduplication (3-stage)
- Semantic search (hybrid BM25 + vector)
- Operational audit trail (PostgreSQL)

**Migration Path:**
```sql
-- Keep existing research_stack schema
-- Add OpenStinger references as foreign keys
-- Use OpenStinger for deduplication + search
-- Migrate gradually, no big-bang
```

### 2. Skills Library → StingerVault

**Current:** Markdown files in `skills/`

**OpenStinger Adds:**
- Autonomous categorization
- Self-updating based on evidence
- Semantic search across skills
- Confidence thresholds per category

**Migration Path:**
```
skills/
├── search/           → Vault: DOMAIN
├── verification/     → Vault: METHODOLOGY
├── reporting/        → Vault: METHODOLOGY
├── governance/       → Vault: CONSTRAINT
└── vault/            ← OpenStinger manages this
```

### 3. Governance Controls → Gradient

**Current:** Manual checklist + human review

**OpenStinger Adds:**
- Pre-delivery alignment scoring
- Drift detection (rolling window)
- Automatic correction (soft flags)
- Audit trail for all evaluations

**Integration:**
```yaml
# Before delivering research output:
alignment_check:
  enabled: true
  min_score: 0.75
  dimensions:
    - value_coherence
    - identity_consistency
    - constraint_compliance
    - content_safety
```

---

## Testing Plan

### Week 1: Memory Tools
- [ ] Ingest sample research sessions
- [ ] Test memory_query with various queries
- [ ] Verify entity deduplication
- [ ] Test temporal filtering

### Week 2: Evidence Store
- [ ] Migrate sample findings to bi-temporal
- [ ] Test semantic search vs keyword
- [ ] Verify audit trail in PostgreSQL
- [ ] Test FalkorDB browser UI

### Week 3: Vault
- [ ] Sync skills library to vault
- [ ] Test autonomous categorization
- [ ] Verify knowledge_ingest from URLs
- [ ] Test vault_note_get for skill retrieval

### Week 4: Gradient
- [ ] Run in observe-only mode
- [ ] Collect alignment scores
- [ ] Tune thresholds
- [ ] Enable correction engine

### Week 5: Full Integration
- [ ] End-to-end research task
- [ ] Verify all 30 tools accessible
- [ ] Performance benchmarking
- [ ] Documentation update

---

## Operational Runbook

### Daily Operations

```bash
# Check OpenStinger health
mcporter call openstinger.ops_status

# Check memory ingestion
mcporter call openstinger.memory_job_status

# Check gradient alignment
mcporter call openstinger.gradient_status
```

### Weekly Maintenance

```bash
# Trigger vault sync
mcporter call openstinger.vault_sync_now

# Check drift status
mcporter call openstinger.gradient_drift_status

# Review alignment log
mcporter call openstinger.gradient_alignment_log --args '{"limit": 100}'
```

### Monthly Tasks

```bash
# Archive old namespaces
mcporter call openstinger.namespace_archive --args '{"namespace": "old-task"}'

# Review vault notes
mcporter call openstinger.vault_note_list

# Check for stale notes
# (notes not updated in 90+ days)
```

---

## Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Memory query latency | <500ms | Benchmark tests |
| Entity dedup accuracy | >95% | Manual audit |
| Vault categorization accuracy | >90% | Human review |
| Gradient alignment pass rate | >85% | ops_status |
| Drift alerts | <1/month | gradient_alert |

---

## Rollback Plan

If issues arise:

1. **Disable OpenStinger MCP:**
   ```bash
   # Stop OpenStinger server
   # Remove MCP config from research stack
   # Revert to native evidence store
   ```

2. **Preserve Data:**
   ```bash
   # Export FalkorDB data
   docker compose exec falkordb redis-cli SAVE
   
   # Export PostgreSQL
   pg_dump openstinger > backup.sql
   ```

3. **Resume Native Operations:**
   ```yaml
   # Revert to original research stack config
   # No data loss - OpenStinger is additive
   ```

---

## Next Steps

1. **Immediate:** Clone and install OpenStinger
2. **Day 1:** Configure environment and start Docker services
3. **Week 1:** Test Tier 1 memory tools with sample data
4. **Week 2:** Integrate with evidence store schema
5. **Week 3:** Configure StingerVault for skills
6. **Week 4:** Enable Gradient alignment (observe-only)
7. **Week 5:** Full integration testing
8. **Week 6:** Production deployment

---

## Contacts & Resources

| Resource | URL |
|----------|-----|
| GitHub Repo | https://github.com/srikanthbellary/openstinger |
| Integration Guides | `/integrations/` folder |
| FalkorDB Docs | https://falkordb.com/docs |
| MCP Protocol | https://modelcontextprotocol.io |

---

**Deployment Status:** Ready to begin
**Estimated Timeline:** 6 weeks
**Risk Level:** Low (additive, non-breaking)
