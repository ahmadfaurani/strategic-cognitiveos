# Honcho CognitiveOS Integration — Implementation Plan

**Author:** Ember | **Date:** 2026-08-18 | **Status:** DRAFT

---

## 1. Architecture Overview

### Design Principle

One workspace (`cognitiveos`) for Ember's operational memory. All workstreams live in one workspace so the deriver can cross-pollinate connections. Hermes keeps its own workspaces — `cognitiveos` is Ember's domain.

### Existing State (Do Not Disrupt)

| Workspace | Owner | Sessions | Messages | Status |
|-----------|-------|----------|----------|--------|
| `hermes` | Hermes | 50 | ~1,500+ | Active — leave as-is |
| `political-intelligence` | Hermes | 1 | 5 | Hermes-configured |
| `prn-johor-2026` | Hermes | 1 | 4 | Election intelligence |
| `hiring-2026-cybersecurity` | Hermes | 0 | 0 | Created, unused |
| `default` | — | 0 | 0 | Test only |

### New Workspace: `cognitiveos`

```
cognitiveos (workspace)
├── Peers
│   ├── ember          (agent — observer of all, observed by daf)
│   ├── daf            (operator — observer of ember, observed by ember)
│   ├── csm            (stakeholder — observed by ember)
│   ├── perjasa        (stakeholder — observed by ember)
│   ├── uitm           (stakeholder — observed by ember)
│   ├── nacsa          (stakeholder — observed by ember)
│   ├── mcmc           (stakeholder — observed by ember)
│   ├── pmo            (stakeholder — observed by ember)
│   └── aras-integrasi (institution — observed by ember)
│
├── Sessions (per workstream/topic)
│   ├── sovereign-ai-perjasa     (PERJASA workshop, Sep 2-3)
│   ├── cyberdsa-2026           (CyberDSA war room)
│   ├── risk-uitm               (R.I.S.I.K development)
│   ├── csm-partnership         (CSM × Aras GTM)
│   ├── productisation          (3-flagship productisation freeze)
│   ├── th-rci-watch            (TH RCI parliamentary watch)
│   └── cognitiveos-ops         (CognitiveOS operational management)
│
├── Messages (ingested CognitiveOS records + live exchanges)
├── Conclusions (deriver-produced workstream insights)
└── Dreaming (overnight cross-workstream connection discovery)
```

---

## 2. Peer Model

### Observer/Observed Matrix

In Honcho, `observer_id` is the entity perceiving, `observed_id` is the entity being perceived. The deriver builds representations of observed peers from the observer's perspective.

| Observer | Observed | Purpose |
|----------|----------|---------|
| `ember` | `daf` | Ember's model of DAF — preferences, patterns, decision history |
| `ember` | `csm` | Ember's model of CSM — partnership state, key contacts |
| `ember` | `perjasa` | Ember's model of PERJASA — workshop status, requirements |
| `ember` | `uitm` | Ember's model of UiTM — R.I.S.I.K collaboration state |
| `ember` | `nacsa` | Ember's model of NACSA — endorsement discussions |
| `ember` | `mcmc` | Ember's model of MCMC — R.I.S.I.K funder |
| `ember` | `pmo` | Ember's model of PMO — Data Lake, strategic alignment |
| `ember` | `aras-integrasi` | Ember's model of Aras — CyberDSA, commercial |
| `daf` | `ember` | DAF's model of Ember — useful for DAF to see how the agent is perceived |
| `daf` | `daf` | Self-model (deriver builds DAF's representation from his own messages) |

### Session Peer Configuration

Each session has peer config:
- `ember`: `observe_me: true, observe_others: true` (full observation)
- `daf`: `observe_me: true, observe_others: false` (DAF is observed but doesn't observe others in this context)

---

## 3. Ingestion Plan

### 3.1 CognitiveOS Records → Messages

268 records across 6 workstreams. Each record becomes a message in the appropriate session:

| Record Type | Honcho Mapping | Speaker (`peer_id`) | Session Target |
|-------------|---------------|---------------------|----------------|
| INIT (initiatives) | message with metadata `{type: "INIT", record_id, status, ...}` | `daf` | Matching workstream session |
| CONV (conversations) | message with metadata `{type: "CONV", record_id, parties, ...}` | `daf` | Matching workstream session |
| DEC (decisions) | message with metadata `{type: "DEC", record_id, authority, ...}` | `daf` | Matching workstream session |
| ACT (actions) | message with metadata `{type: "ACT", record_id, assignee, due, status, ...}` | `daf` | Matching workstream session |
| RSK (risks) | message with metadata `{type: "RSK", record_id, severity, status, ...}` | `daf` | Matching workstream session |
| STK (stakeholders) | message with metadata `{type: "STK", record_id, entity, role, ...}` | `ember` | `cognitiveos-ops` session |
| INT (intelligence) | message with metadata `{type: "INT", record_id, source, classification, ...}` | `ember` | Matching workstream session |
| OUT (outcomes) | message with metadata `{type: "OUT", record_id, linked_act, ...}` | `daf` | Matching workstream session |

### 3.2 Message Content Format

Each message content is a structured string that the deriver can process:

```
[INIT-20260803-002] R.I.S.I.K (UiTM Collaboration)
Type: Initiative
Status: Collaboration Framework Agreed
Authority: DAF
Created: 2026-08-03
Context: UiTM agreed in principle (Prof. Suhaimee + 5 team members)
Cost: RM5.0M, 12-month, 9-component (DEC-20260815-001)
Funder: MCMC (STK-20260815-002)
Next: MCMC proposal prep (ACT-20260815-006), UiTM working session
Links: DEC-20260815-001, STK-20260815-002, ACT-20260815-006
```

### 3.3 Session Mapping

| CognitiveOS Workstream Cluster | Honcho Session |
|--------------------------------|----------------|
| A. Sovereign AI & Government AI | `sovereign-ai-perjasa` |
| B. Cybersecurity Productisation | `productisation` |
| C. Government & Institutional Partnerships | `csm-partnership` |
| D. Political & Strategic Intelligence | (stays in Hermes `political-intelligence`) |
| E. Commercial & Market Development | `cyberdsa-2026` |
| F. Organisational Capability Building | `cognitiveos-ops` |
| R.I.S.I.K | `risk-uitm` |
| TH-RCI Watch | `th-rci-watch` |

### 3.4 Ingestion Phases

**Phase A: Batch ingest existing records** (one-time)
1. Parse all 268 records from CognitiveOS GitHub repos
2. Map each to the correct session
3. Batch upload via `POST /v3/workspaces/cognitiveos/sessions/{session_id}/messages` (MessageBatchCreate)
4. Mark each message with `created_at` = original record date (preserves timeline)

**Phase B: Live ingestion** (ongoing)
- At key moments during a session (decision made, action assigned, risk identified), write to Honcho
- Triggered by explicit markers in conversation or by Ember judgment

---

## 4. Connector Design

### 4.1 Bootstrap Hook (Session Start)

Script: `tools/honcho-connector/recall.sh`

```
Input: query string (derived from session type or first user message)
Process:
  1. POST /v3/workspaces/cognitiveos/search — semantic search for relevant messages
  2. POST /v3/workspaces/cognitiveos/conclusions/query — search conclusions
  3. GET /v3/workspaces/cognitiveos/peers/daf/context — get DAF peer context
  4. Format results as context injection text
Output: relevant context from Honcho (messages, conclusions, peer representations)
```

### 4.2 Write-Back Hook (During Session)

Script: `tools/honcho-connector/ingest.sh`

```
Input: message content, peer_id, session_id, metadata
Process:
  1. POST /v3/workspaces/cognitiveos/sessions/{session_id}/messages
  2. Message enters deriver queue for processing
Output: message_id confirmation
```

### 4.3 Batch Ingestion Script

Script: `tools/honcho-connector/ingest-cognitiveos.py`

```
Input: CognitiveOS records (parsed from GitHub repos)
Process:
  1. Parse records from strategic-cognitiveos repo
  2. Map to sessions based on workstream cluster
  3. Batch upload with original timestamps
  4. Create peer associations for each session
Output: ingestion report (records loaded, sessions updated, errors)
```

### 4.4 Context Query Script (Mid-Session)

Script: `tools/honcho-connector/query.sh`

```
Input: natural language query
Process:
  1. Search workspace for relevant messages
  2. Search conclusions for distilled insights
  3. Return formatted results
Output: relevant context for current processing
```

---

## 5. Implementation Phases

### Phase 1: Foundation (Day 1)
- [ ] Create `cognitiveos` workspace
- [ ] Create all peers (ember, daf, stakeholders)
- [ ] Create sessions (7 workstream sessions)
- [ ] Configure session peer associations (who observes whom)
- **Deliverable:** Empty workspace ready for data

### Phase 2: Batch Ingestion (Day 1-2)
- [ ] Write `ingest-cognitiveos.py` parser
- [ ] Parse 268 records from `strategic-cognitiveos` repo
- [ ] Map records to sessions
- [ ] Batch upload with original timestamps
- [ ] Verify ingestion (message count, embedding count)
- **Deliverable:** 268 records in Honcho, deriver processing queue

### Phase 3: Connector (Day 2-3)
- [ ] Write `recall.sh` (bootstrap query)
- [ ] Write `ingest.sh` (write-back)
- [ ] Write `query.sh` (mid-session query)
- [ ] Test each against live Honcho API
- **Deliverable:** Three scripts, tested and working

### Phase 4: OpenClaw Integration (Day 3-4)
- [ ] Wire `recall.sh` into OpenClaw session bootstrap
- [ ] Wire `ingest.sh` into session end / key exchange moments
- [ ] Test end-to-end: new session → recall → process → write-back → next session recall
- **Deliverable:** Closed cognitive loop

### Phase 5: Advanced Features (Day 5+)
- [ ] Activate conclusions (configure deriver to produce workstream-level conclusions)
- [ ] Schedule dreaming (overnight cross-workstream discovery)
- [ ] Wire conclusions query into recall.sh
- [ ] Monitor deriver queue and representation quality
- **Deliverable:** Deriver producing insights, dreaming active

---

## 6. API Call Sequence

### Phase 1: Foundation

```bash
# 1. Create workspace
POST /v3/workspaces
  {"id": "cognitiveos", "metadata": {"description": "CognitiveOS operational memory — Ember's semantic recall layer", "created_by": "ember", "version": "1.0"}}

# 2. Create peers (idempotent — Get or Create)
POST /v3/workspaces/cognitiveos/peers
  {"id": "ember", "metadata": {"type": "agent", "role": "observer"}}
POST /v3/workspaces/cognitiveos/peers
  {"id": "daf", "metadata": {"type": "operator", "role": "authority"}}
POST /v3/workspaces/cognitiveos/peers
  {"id": "csm", "metadata": {"type": "stakeholder", "entity": "CSM"}}
# ... repeat for each stakeholder

# 3. Create sessions
POST /v3/workspaces/cognitiveos/sessions
  {"id": "sovereign-ai-perjasa", "metadata": {"workstream": "A", "topic": "PERJASA Workshop Sep 2-3"}, "peers": {"ember": {"observe_me": true, "observe_others": true}, "daf": {"observe_me": true, "observe_others": false}}}
# ... repeat for each session
```

### Phase 2: Batch Ingestion

```python
# For each CognitiveOS record:
POST /v3/workspaces/cognitiveos/sessions/{session_id}/messages
  {
    "messages": [
      {
        "content": "[INIT-20260803-002] R.I.S.I.K (UiTM Collaboration)\n...",
        "peer_id": "daf",
        "created_at": "2026-08-03T00:00:00Z",
        "metadata": {"type": "INIT", "record_id": "INIT-20260803-002", "workstream": "F"}
      }
    ]
  }
```

### Phase 3-4: Connector

```bash
# Bootstrap recall
POST /v3/workspaces/cognitiveos/search
  {"query": "R.I.S.I.K funding MCMC", "limit": 10}

POST /v3/workspaces/cognitiveos/conclusions/query
  {"query": "R.I.S.I.K collaboration status", "top_k": 5}

GET /v3/workspaces/cognitiveos/peers/daf/context?target=ember

# Write-back
POST /v3/workspaces/cognitiveos/sessions/{session_id}/messages
  {"messages": [{"content": "Decision: ...", "peer_id": "daf", "metadata": {"type": "DEC", "live": true}}]}
```

### Phase 5: Advanced

```bash
# Schedule dream
POST /v3/workspaces/cognitiveos/schedule_dream
  {"types": ["omni"]}

# Query conclusions
POST /v3/workspaces/cognitiveos/conclusions/query
  {"query": "cross-workstream dependencies", "top_k": 10}
```

---

## 7. Data Flow Summary

```
COGNITIVEOS REPOS (268 records)
    ↓ ingest-cognitiveos.py
HONCHO cognitiveos WORKSPACE
    ↓ deriver processes
    ↓ → peer representations (DAF, stakeholders)
    ↓ → conclusions (workstream insights)
    ↓ → dreaming (cross-workstream connections)
    ↓
OPENCLAW SESSION START
    ↓ recall.sh queries Honcho
    ↓ relevant context injected into working memory
    ↓
EMBER PROCESSES + RESPONDS
    ↓ ingest.sh writes significant exchanges back
    ↓ deriver processes new messages
    ↓ representations and conclusions updated
    ↓
NEXT SESSION: enriched recall
```

---

## 8. Risk Assessment

| Risk | Severity | Mitigation |
|------|----------|------------|
| Ingestion corrupts existing Hermes data | Critical | `cognitiveos` is a new workspace — no overlap with `hermes` workspace |
| Deriver overwhelmed by batch ingestion | Medium | Batch in groups of 50, monitor queue status, deriver has backoff built in |
| Embedding API rate limits | Low | Already proven at 1,596 embeddings; sovereign infrastructure, no external limits |
| Connector adds latency to session start | Medium | recall.sh has timeout (default 5s), fail-open if Honcho unavailable |
| Stale conclusions mislead recall | Low | Conclusions are timestamped; recall can filter by recency |
| CognitiveOS records out of sync with Honcho | Medium | Batch ingestion is one-time; live ingestion handles new records; periodic re-sync script for reconciliation |

---

## 9. Success Criteria

| Criterion | Measurement | Target |
|-----------|------------|--------|
| Workspace created | `cognitiveos` workspace exists | ✅ |
| Peers created | 10 peers in workspace | 10 |
| Sessions created | 7 workstream sessions | 7 |
| Records ingested | Message count ≥ 268 | 268+ |
| Embeddings generated | message_embeddings count matches messages | 100% |
| Deriver processing | Queue shows work units processed | > 0 |
| Bootstrap recall working | recall.sh returns relevant context on test query | ✅ |
| Write-back working | ingest.sh creates message in Honcho | ✅ |
| End-to-end loop | New session gets enriched context from previous session's write-back | ✅ |
| Conclusions produced | At least 1 conclusion within 48h of ingestion | ≥ 1 |

---

## 10. File Structure

```
tools/honcho-connector/
├── IMPLEMENTATION-PLAN.md      ← this document
├── recall.sh                   ← bootstrap recall script
├── ingest.sh                   ← write-back script
├── query.sh                    ← mid-session query script
├── ingest-cognitiveos.py       ← batch ingestion script
├── config.sh                   ← shared config (URL, workspace, defaults)
├── lib/
│   └── honcho-client.sh        ← shared API client functions
└── logs/
    └── ingestion-report.json    ← batch ingestion results
```

---

*Plan status: DRAFT — ready for DAF review and execution.*
