# PIR Execution Outsourcing Architecture

**Version:** 1.0
**Authority:** DAF
**Status:** ACTIVE — Canonical architecture for all PIR collection
**Date:** 2026-08-17

---

## 1. Design Principle

All PIR (Priority Intelligence Requirement) execution is outsourced to two external stacks:

1. **DeerFlow Stack** — AI agent platform for research planning, multi-source analysis, and intelligence product generation
2. **OSINT Stack** — Collection infrastructure (Firecrawl, SearXNG, web_extract) for raw intelligence gathering

Hermes cronjobs become **orchestrators** — they dispatch PIR tasks to DeerFlow, which uses OSINT tools to collect, then synthesizes results. Hermes never collects directly for PIR execution.

## 2. Three-Layer Architecture

```
Layer 1: HERMES CRONJOB (Orchestrator)
  │ - Fires on schedule
  │ - Reads PIR definitions from CognitiveOS records
  │ - Constructs DeerFlow research prompt
  │ - Dispatches to DeerFlow API
  │ - Collects result
  │ - Writes intelligence record to CognitiveOS
  │ - Commits to git
  │
Layer 2: DEERFLOW (Research Engine)
  │ - Receives PIR research prompt
  │ - Plans collection strategy (ultra mode: thinking + planning + sub-agents)
  │ - Dispatches sub-agents for parallel collection
  │ - Synthesizes findings
  │ - Returns structured intelligence product
  │
Layer 3: OSINT STACK (Collection Tools)
  │ - Firecrawl: web search, page scraping, structured extraction
  │ - SearXNG: federated search across 7+ engines
  │ - web_extract: direct URL content extraction
  │ - DeerFlow sub-agents use these tools autonomously
```

## 3. Data Flow

```
CognitiveOS PIR Registry
  ↓ (Hermes cronjob reads PIR definitions)
DeerFlow API (/threads → /runs/stream)
  ↓ (DeerFlow plans + dispatches sub-agents)
OSINT Tools (Firecrawl search + SearXNG + web_extract)
  ↓ (Raw intelligence collected)
DeerFlow Synthesis
  ↓ (Structured intelligence product returned)
Hermes Cronjob
  ↓ (Writes INT record to intelligence/)
  ↓ (Updates PIR status in source records)
  ↓ (Git commit + push)
CognitiveOS Repository
```

## 4. PIR Cluster → DeerFlow Mapping

Each cronjob maps to a PIR cluster. The cronjob prompt contains:
- PIR definitions (from CognitiveOS records)
- Collection context (entity backgrounds, known facts)
- Output format specification (INT record structure)
- DeerFlow mode selection (ultra for Critical, pro for High, standard for Medium)

| PIR Cluster | DeerFlow Mode | Schedule | OSINT Tools |
|-------------|--------------|----------|------------|
| Critical PIRs (leadership, authority, timeline) | ultra | every 6h | Firecrawl + SearXNG |
| High PIRs (procurement, technology, competitors) | pro | every 12h | Firecrawl + SearXNG |
| Medium PIRs (context, background) | standard | daily | Firecrawl + web_extract |
| Daily Brief (all PIRs synthesis) | ultra | daily 04:00 MYT | All sources |
| Weekly Deep-Dive (trend analysis) | ultra | weekly Mon 08:00 | All sources |

## 5. DeerFlow API Integration

### Dispatch Pattern

```bash
# 1. Create thread
THREAD_ID=$(curl -s -X POST "$DEERFLOW_LANGGRAPH_URL/threads" \
  -H "Content-Type: application/json" -d '{}' | python3 -c "import sys,json; print(json.load(sys.stdin)['thread_id'])")

# 2. Stream research run (ultra mode for Critical PIRs)
curl -s -N -X POST "$DEERFLOW_LANGGRAPH_URL/threads/$THREAD_ID/runs/stream" \
  -H "Content-Type: application/json" \
  -d '{
    "assistant_id": "lead_agent",
    "input": {
      "messages": [{
        "type": "human",
        "content": [{"type": "text", "text": "PIR_RESEARCH_PROMPT"}]
      }]
    },
    "stream_mode": ["values"],
    "config": {"recursion_limit": 1000},
    "context": {
      "thinking_enabled": true,
      "is_plan_mode": true,
      "subagent_enabled": true,
      "thread_id": "THREAD_ID"
    }
  }'
```

### Response Parsing

The SSE stream returns `values` events. The last `values` event contains the complete `messages` array. The final AI message's `content` field is the intelligence product.

## 6. Hermes Cronjob Prompt Template

Each PIR cronjob prompt follows this structure:

```
You are a PIR Collection Orchestrator for Strategic CognitiveOS.

## MISSION
Execute PIR cluster [CLUSTER_NAME] via DeerFlow research engine.

## PIR DEFINITIONS
[Extracted from CognitiveOS records — PIR ID, requirement, priority, status]

## COLLECTION CONTEXT
[Entity backgrounds, known facts, previous findings]

## EXECUTION
1. Read the PIR definitions above
2. Construct a DeerFlow research prompt using the template at osint-stack/templates/deerflow-pir-prompt.md
3. Dispatch to DeerFlow API:
   - Create thread: POST $DEERFLOW_LANGGRAPH_URL/threads
   - Stream run: POST $DEERFLOW_LANGGRAPH_URL/threads/<id>/runs/stream
   - Mode: [ultra for Critical, pro for High, standard for Medium]
4. Collect the final AI response from the SSE stream
5. Parse the intelligence product
6. Write an INT record to intelligence/cron-output/ using the CognitiveOS INT template
7. Update PIR status in source records if resolved
8. Git commit + push

## OUTPUT FORMAT
Save to: intelligence/cron-output/cjN-name-[TIMESTAMP].md
Format: CognitiveOS INT record (YAML frontmatter + markdown body)

## DEERFLOW CONFIG
DEERFLOW_URL=http://localhost:2026
DEERFLOW_GATEWAY_URL=http://localhost:2026
DEERFLOW_LANGGRAPH_URL=http://localhost:2026/api/langgraph
```

## 7. OSINT Stack Health Check

Before each cronjob run, verify OSINT stack:
- Firecrawl: `curl -s http://localhost:3002/health`
- SearXNG: `curl -s http://127.0.0.1:8080/search?q=test&format=json`
- DeerFlow: `curl -s http://localhost:2026/health`

If any service is down, fall back to Hermes native web_search/web_extract (record fallback in output).

## 8. Fallback Hierarchy

```
Primary: DeerFlow (ultra/pro/standard mode) → OSINT stack
  ↓ if DeerFlow unavailable
Secondary: Hermes web_search + Firecrawl MCP + web_extract (inline collection)
  ↓ if Firecrawl unavailable
Tertiary: Hermes web_search + SearXNG direct + web_extract
  ↓ if all external tools fail
Quaternary: Skip cycle, log failure, retry next schedule
```
