---
id: DOC-20260822-001
record_type: document
title: "Actionable Intelligence Protocol — Honcho Queue Backlog Remediation"
created_at: 2026-08-22T01:05:00+00:00
updated_at: '2026-08-22T01:05:00+00:00'
owner: faurani-jaafar
status: active
priority: high
sensitivity: internal
lifecycle_state: canonical
confidence: high
tags:
  - domain/cognitiveos-operations
  - domain/infrastructure
  - domain/honcho-integration
  - framework/actionable-intelligence-protocol
  - type/actionable-protocol
  - type/execution-protocol
  - type/infrastructure-protocol
source:
  type: synthesis
  reference: "Live API queries to Honcho localhost:8000, Docker container logs (honcho-deriver-1, honcho-api-1, honcho-tei-embeddings-1), honcho-connector logs, IMPLEMENTATION-PLAN.md, AGENTS.md Honcho recall spec"
summary: "Execution protocol for clearing the 526-unit Honcho deriver queue backlog across 4 workspaces (hermes=511, cognitiveos=6, political-intelligence=5, prn-johor-2026=4). Addresses throughput bottleneck (single deriver worker, ~40s per batch), orphaned cognitiveos work units (6 units for sessions with 0 messages), broken recall.sh, and prevention of recurrence."
strategic_significance: "Honcho is the semantic recall layer for CognitiveOS and Hermes operations. A 526-unit backlog means new conversations and CognitiveOS records are not being derived into conclusions — recall queries return stale or empty results. The cognitiveos workspace (Ember's operational memory) has never had a successful recall since deployment. Fixing this unblocks session-start enrichment, ADEP-001 gate compliance logging, and cross-workstream connection discovery."
mission_alignment:
  - cognitiveos-operations
  - infrastructure
  - sovereign-capability
related_records:
  - DOC-20260821-002
  - ACT-20260821-010
  - ACT-20260821-011
  - ACT-20260821-012
---

# Actionable Intelligence Protocol — Honcho Queue Backlog Remediation

**TLP:AMBER | Aras Integrasi | Infrastructure Operations**
**Version:** 1.0
**Reference:** Live system audit Aug 22 01:00 UTC (09:00 MYT)
**Protocol owner:** DAF
**Operator:** Laras (Hermes)
**Protocol status:** ACTIVE — awaiting DAF execution decision

---

## Priority Assessment

**PRIMARY: Hermes queue drain (511 units)** — the blocker. No other workspace queue can be processed until the deriver reaches those sessions. At current throughput (~40s per 2-message batch), ETA ~170 minutes. This is the critical path.

| Metric | Value | Source |
|--------|-------|--------|
| Total pending | 511 | GET /v3/workspaces/hermes/queue/status |
| Completed | 2 | Same |
| Sessions affected | ~90 | Same |
| Largest session | 42 pending (yq0GL1jbDS6QICZlZZBIK) | Same |
| Processing rate | ~40s per 2-msg batch | Docker logs honcho-deriver-1 |
| Deriver uptime | Since Aug 21 05:28 UTC (20h) | ps -p 4181439 |
| Last batch completed | ~01:00 UTC (msgs 2773-2776) | Docker logs |
| Errors | 0 critical, 2 summarizer warnings | Docker logs |

**SECONDARY: CognitiveOS queue drain (6 units)** — blocked behind Hermes. Two sessions with pending work but 0 messages — orphaned work units from the Aug 19 batch ingestion. These will either be processed (no-op, no messages to derive) or discarded by the deriver.

| Session ID | Pending | Messages | Assessment |
|------------|---------|----------|------------|
| anuwN4bFSF9gyZOTwSsC_ | 5 | 0 | Orphaned — work enqueued for empty session |
| rC2ygUH6elUqmxCCzXiDP | 1 | 0 | Orphaned — same |

**TERTIARY: Prevention + connector repair** — recall.sh broken since Aug 19, no session-start enrichment working, deriver throughput is structurally limited to single-worker.

---

## Phase 1 — Immediate Queue Drain (Today, Aug 22)

**Trigger:** DAF authorises execution
**Owner:** Laras (Hermes)
**D-level:** D2 (affects operational infrastructure)

### 1A — Hermes Queue Acceleration (Option A: Scale Workers)

| Step | Action | Owner | Required Input | Required Output | Deadline |
|------|--------|-------|----------------|-----------------|----------|
| 1A.1 | Check current DERIVER_WORKERS setting | Laras | Docker inspect honcho-deriver-1 | Current worker count | 5 min |
| 1A.2 | Scale deriver to 2 workers (restart with DERIVER_WORKERS=2) | Laras | Docker compose override or env injection | Deriver running with 2 workers | 15 min |
| 1A.3 | Monitor queue drain rate for 10 minutes — confirm parallel processing | Laras | GET /v3/workspaces/hermes/queue/status at 2-min intervals | Drain rate doubled (or not) | 25 min |
| 1A.4 | If drain rate improves → let run until clear. If not → revert to 1 worker, proceed to 1B. | Laras | Queue status comparison | Decision: scale or let grind | 30 min |

**Risk:** Multiple deriver workers hitting the same LLM endpoint (model.arasintegrasi.ai) may rate-limit or cause contention. Monitor for LLM call errors in deriver logs.

**Mitigation:** If LLM errors appear, revert to 1 worker immediately. The ~3 hour natural drain is acceptable.

### 1B — Natural Drain (Option B: Let It Run)

| Step | Action | Owner | Required Input | Required Output | Deadline |
|------|--------|-------|----------------|-----------------|----------|
| 1B.1 | Do nothing. Let the deriver process the queue naturally. | — | — | — | — |
| 1B.2 | Monitor queue status every 30 minutes via cronjob or manual check | Laras | Queue API | Status update | Every 30 min |
| 1B.3 | Queue cleared when pending_work_units = 0 for hermes workspace | Laras | Queue API | Confirmation | ~170 min |

**Assessment:** Option B is lower risk. The deriver is healthy, no errors, processing at expected rate. The only cost is time (~3 hours) during which new Hermes messages continue to enqueue but are processed in order. CognitiveOS and other workspaces will drain automatically after Hermes clears.

**Recommendation:** Option B (natural drain) unless DAF needs the queue cleared faster for operational reasons.

### 1C — CognitiveOS Orphaned Work Units

| Step | Action | Owner | Required Input | Required Output | Deadline |
|------|--------|-------|----------------|-----------------|----------|
| 1C.1 | After Hermes queue clears, check if cognitiveos queue drained naturally | Laras | GET /v3/workspaces/cognitiveos/queue/status | Queue status | Post-hermes drain |
| 1C.2 | If 6 units still pending → investigate via DB or API. These are work units for sessions with 0 messages — the deriver should process them as no-ops. | Laras | DB query or API investigation | Root cause of orphaned units | 30 min |
| 1C.3 | If orphans cannot self-resolve → purge via DB (delete queue items for those session IDs). Requires Honcho DB access. | Laras | Docker exec into honcho Postgres | Purged queue items | 15 min |
| 1C.4 | Re-run batch ingestion for the 5 empty CognitiveOS sessions (sovereign-ai-perjasa, productisation, th-rci-watch, risk-uitm, cognitiveos-ops) — the Aug 19 run only populated csm-partnership (74) and cyberdsa-2026 (60) | Laras | ingest-cognitiveos.py with session mapping fix | 5 sessions populated | 1 hour |

**Gate check before proceeding to Phase 2:**
- [ ] Hermes queue: pending_work_units = 0
- [ ] CognitiveOS queue: pending_work_units = 0
- [ ] CognitiveOS sessions have messages in all 7 sessions (not just 2)
- [ ] No deriver errors in Docker logs
- [ ] Conclusions being derived for cognitiveos workspace (check conclusions/list)

**Escalation:** If deriver crashes during drain → restart Docker container `docker restart honcho-deriver-1`, monitor recovery. If LLM endpoint (model.arasintegrasi.ai) is unreachable → deriver will retry with backoff, no action needed.

---

## Phase 2 — Connector Repair (Aug 22-23)

**Trigger:** Phase 1 gate check complete (all queues cleared)
**Owner:** Laras (Hermes)
**D-level:** D2

### 2A — Fix recall.sh

| Step | Action | Owner | Required Input | Required Output | Deadline |
|------|--------|-------|----------------|-----------------|----------|
| 2A.1 | Diagnose recall.sh failure — run manually, capture error output | Laras | recall.sh script, logs/recall.log | Error diagnosis | 15 min |
| 2A.2 | Fix API calls — recall.sh was written for v3 API but may have wrong endpoints or auth. Cross-reference with OpenAPI spec at /openapi.json | Laras | recall.sh, OpenAPI spec | Fixed recall.sh | 30 min |
| 2A.3 | Test recall.sh — run against cognitiveos workspace, verify it returns conclusions and peer context | Laras | cognitiveos workspace with derived conclusions | Successful recall output | 15 min |
| 2A.4 | Verify AGENTS.md session-start recall now works — the startup hook calls recall.sh | Laras | recall.sh exit code 0, non-empty output | Confirmation | 15 min |

**recall.sh failure evidence (from logs):**
```
2026-08-19T05:28:35Z | recall | ERROR | search failed
2026-08-19T05:28:35Z | recall | ERROR | conclusions query failed
2026-08-19T05:28:35Z | recall | ERROR | peer context failed
```

### 2B — Fix audit.sh

| Step | Action | Owner | Required Input | Required Output | Deadline |
|------|--------|-------|----------------|-----------------|----------|
| 2B.1 | Diagnose audit.sh failure — same pattern as recall.sh (Aug 19 errors) | Laras | audit.sh, logs/audit.log | Error diagnosis | 15 min |
| 2B.2 | Fix API calls — same root cause as recall.sh likely | Laras | audit.sh | Fixed audit.sh | 15 min |
| 2B.3 | Test audit.sh — run against cognitiveos workspace | Laras | cognitiveos workspace | Successful audit output | 15 min |

### 2C — Fix Session-Peer Association

| Step | Action | Owner | Required Input | Required Output | Deadline |
|------|--------|-------|----------------|-----------------|----------|
| 2C.1 | Associate peers to sessions — all 7 cognitiveos sessions show peers=0. Use POST /v3/workspaces/cognitiveos/sessions/{id}/peers to add ember + daf to each session. | Laras | Session IDs, peer IDs | 7 sessions with peers configured | 30 min |
| 2C.2 | Verify peer config — GET /v3/workspaces/cognitiveos/sessions/{id}/peers for each session | Laras | API response | Confirmation | 15 min |

**Gate check before proceeding to Phase 3:**
- [ ] recall.sh runs successfully (exit 0, non-empty output)
- [ ] audit.sh runs successfully
- [ ] All 7 cognitiveos sessions have ember + daf as peers
- [ ] gate.sh continues to work (already functional — no action needed)

---

## Phase 3 — Prevention & Scaling (Aug 23-24)

**Trigger:** Phase 2 gate check complete
**Owner:** Laras (Hermes)
**D-level:** D2

### 3A — Throughput Prevention

| Step | Action | Owner | Required Input | Required Output | Deadline |
|------|--------|-------|----------------|-----------------|----------|
| 3A.1 | Assess Hermes message volume — 511 pending across 90 sessions = ~5.7 msgs/session average. Determine if all Hermes conversations need to go to Honcho or if a filter is appropriate. | Laras | Hermes config, Honcho ingestion settings | Volume assessment | 30 min |
| 3A.2 | If volume is excessive → configure Hermes to only ingest significant exchanges (not every tool call) to Honcho. Hermes-native Honcho tools (honcho_profile, honcho_conclude) already handle direct writes. | Laras | Hermes config | Filtered ingestion config | 1 hour |
| 3A.3 | Consider scaling deriver workers permanently — if DERIVER_WORKERS=2 works in Phase 1A, set it as the default in docker-compose.yml | Laras | Docker compose config | Permanent 2-worker config | 15 min |

### 3B — Monitoring Cronjob

| Step | Action | Owner | Required Input | Required Output | Deadline |
|------|--------|-------|----------------|-----------------|----------|
| 3B.1 | Create a Honcho queue monitor cronjob — checks queue status every 30 min, alerts if pending > 100 | Laras | Cronjob creation | Active monitor | 30 min |
| 3B.2 | Alert delivery: send to DAF via Telegram if queue > 100 or deriver not processing (completed_work_units not increasing) | Laras | Telegram delivery config | Alert mechanism | 15 min |

### 3C — CognitiveOS Re-ingestion

| Step | Action | Owner | Required Input | Required Output | Deadline |
|------|--------|-------|----------------|-----------------|----------|
| 3C.1 | Fix ingest-cognitiveos.py session mapping — the script only populated 2 of 7 sessions. Debug the session-to-record mapping logic. | Laras | ingest-cognitiveos.py source | Fixed session mapping | 1 hour |
| 3C.2 | Re-run batch ingestion for all CognitiveOS records across all 7 sessions | Laras | Fixed script, CognitiveOS records | 7 sessions populated (268+ messages) | 1 hour |
| 3C.3 | Verify conclusions are being derived for all 7 sessions within 48h | Laras | conclusions/list API | Conclusions present for all sessions | 48h |

**Gate check for Phase 3 completion:**
- [ ] Hermes message volume assessed and filtered (if needed)
- [ ] Deriver worker count set permanently (1 or 2)
- [ ] Queue monitor cronjob active
- [ ] CognitiveOS ingestion complete (all 7 sessions have messages)
- [ ] Conclusions derived for all 7 sessions within 48h

---

## Decision Points

| Question | Options | Risk | Recommendation |
|----------|---------|------|----------------|
| Natural drain vs scale workers? | A: Let it run (~3h). B: Scale to 2 workers (risky — LLM contention). | B has LLM rate-limit risk. A has time cost only. | **A — natural drain.** Deriver is healthy, no errors. 3 hours is acceptable. |
| Purge orphaned cognitiveos work units? | A: Let deriver process as no-ops. B: Purge via DB. | A may take time. B requires DB access. | **A first, B as fallback.** Let the deriver handle it — it should skip empty sessions. |
| Filter Hermes message ingestion? | A: Ingest all. B: Filter to significant exchanges only. | B loses context. A causes recurring backlog. | **Assess in Phase 3.** Need data on what Hermes sends vs what the deriver actually uses. |
| Re-ingest CognitiveOS now or after Hermes drains? | A: Now (adds to backlog). B: After Hermes clears. | A adds ~268 messages to an already 511-unit backlog. | **B — after Hermes drains.** Don't compound the backlog. |

---

## Monitoring & Escalation Protocol

### Queue Status Check (every 30 min during Phase 1)

| Check | Green | Amber | Red |
|-------|-------|-------|-----|
| Hermes pending units | < 50 | 50-200 | > 200 or increasing |
| CognitiveOS pending units | 0 | 1-5 | > 5 or not draining |
| Deriver processing | completed_work_units increasing | Stalled for > 15 min | Deriver process dead |
| LLM call success rate | No errors in logs | Occasional retries | Continuous failures |
| TEI embeddings | Healthy | Slow responses > 5s | Container down |

### Escalation Paths

| Situation | Action | Timeline |
|-----------|--------|----------|
| Deriver crashes during drain | `docker restart honcho-deriver-1`, monitor recovery | Immediate |
| LLM endpoint (model.arasintegrasi.ai) unreachable | Deriver will retry with backoff. Wait. Check if other services using the endpoint are also affected. | 15 min assessment |
| Queue not draining after 4 hours | Check deriver logs for stuck sessions. Consider purging the largest session queue (42 units). | 4h after start |
| CognitiveOS orphans survive Hermes drain | DB-level purge of queue items for the 2 orphaned session IDs | Post-hermes drain |
| recall.sh fix reveals deeper API issue | Cross-reference with Honcho CLAUDE.md and OpenAPI spec. May need Honcho version check. | 1h diagnosis |

---

## Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Hermes queue cleared | pending_work_units = 0 | GET /v3/workspaces/hermes/queue/status |
| CognitiveOS queue cleared | pending_work_units = 0 | GET /v3/workspaces/cognitiveos/queue/status |
| All workspaces queue cleared | pending = 0 across all 7 workspaces | Queue status for each |
| recall.sh functional | Exit 0, non-empty output | Manual run + log check |
| audit.sh functional | Exit 0, non-empty output | Manual run + log check |
| All 7 cognitiveos sessions have peers | peers ≥ 2 (ember + daf) | GET session peers |
| All 7 cognitiveos sessions have messages | message_count > 0 | POST messages/list |
| Conclusions derived for all sessions | ≥ 1 conclusion per session within 48h | POST conclusions/list |
| Queue monitor cronjob active | Running every 30 min | Cronjob list |
| No recurrence within 7 days | Queue stays < 50 | Monitor check |

---

## Protocol Rules

1. **Do not compound the backlog.** No new batch ingestion until Hermes queue is cleared.
2. **Natural drain is the default.** Scaling workers is opt-in, not default. The deriver is healthy — time is the only cost.
3. **Orphaned work units are low priority.** The deriver should handle them as no-ops. Only purge via DB if they persist after the Hermes queue clears.
4. **Fix connectors after queue drain, not during.** recall.sh and audit.sh fixes require the deriver to be processing cognitiveos messages to test — can't verify fixes while queue is backed up.
5. **Session-peer association is a prerequisite for conclusions.** Without peers associated to sessions, the deriver cannot build per-peer representations. This must be fixed before re-ingestion.
6. **Monitor, don't babysit.** Set up the cronjob monitor and let it alert. Don't manually poll every 5 minutes.
7. **One change at a time.** Don't scale workers AND fix recall.sh AND re-ingest in the same window. Each change needs verification before the next.

---

## Document Control

| Field | Value |
|-------|-------|
| Protocol owner | DAF |
| Operator | Laras (Hermes) |
| Created | Aug 22, 2026 09:05 MYT |
| v1.0 | Aug 22, 2026 — initial protocol from live system audit |
| Status | ACTIVE — awaiting DAF execution decision |
| Next review | Aug 23 (post-Phase 1 gate check) |
| Key source | Live API queries to localhost:8000, Docker logs, honcho-connector logs |

---

*Author: Laras | Source: Live system audit Aug 22 2026 01:00 UTC | Classification: TLP:AMBER*
