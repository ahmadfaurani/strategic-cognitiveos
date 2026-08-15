# Political Signal Registry — RETIRED

> **⚠️ RETIRED 2026-08-15:** This registry was never operationalized beyond 3 test signals. Canonical signal tracking is now the CVS Evidence Register at `workspace-mlk/03-VERIFICATION/CVS-EVIDENCE-REGISTER.csv` (210 active claims, 20-field validation per claim). This file is retained for historical reference only.

---

**Timestamp:** 2026-06-13 16:45 UTC  
**Classification:** TLP:AMBER  
**Status:** ~~SCHEMA COMPLETE — Implementation starts 2026-06-15~~ → RETIRED

---

## 📋 Schema Summary

**File:** `tools/deer-flow/docs/political-signal-registry-schema.md`  
**Version:** 1.0  
**Fields:** 35 core fields across 9 categories

### Core Categories

| Category | Fields | Purpose |
|----------|--------|---------|
| **Identity** | signal_id, timestamps, TLP, confidence | Unique ID + provenance |
| **Source** | name, tier, category, URL, language | Media outlet metadata |
| **Content** | headline, excerpt, hash, word_count, media_type | What was collected |
| **PIR** | primary, secondary, keywords_matched, relevance_score | Intelligence classification |
| **Sentiment** | polarity, score, archetype, velocity, engagement | Emotional + impact analysis |
| **Alert** | level, threshold_breached, escalation_required | Response trigger |
| **Entities** | person, organization, location, event | Named entity extraction |
| **Processing** | agent, version, timestamp, analyst_reviewed | Audit trail |

---

## 📁 Storage Structure

```
memory/
├── signals/
│   ├── 2026/
│   │   └── 06-june/
│   │       ├── 2026-06-13-signals.jsonl
│   │       └── registry-index.json
├── PIR-005-stability/
│   └── signals-2026-06.jsonl
```

**File Formats:**
- Daily batch: JSONL (one signal per line)
- Registry index: JSON (searchable metadata)
- PIR aggregates: JSONL (monthly by PIR)

---

## 🚨 Alert Levels

| Level | Response | Example Trigger |
|-------|----------|-----------------|
| 🔴 CRITICAL | ≤10 min | Coalition collapse |
| 🟠 HIGH | ≤1 hour | Viral >10K, defection confirmed |
| 🟡 MEDIUM | Daily log | ≥3 autonomy articles/day |
| 🟢 LOW | Weekly log | Routine PIR content |

---

## 🎯 PIR Thresholds (10 PIRs)

| PIR | Focus | Threshold | Level |
|-----|-------|-----------|-------|
| PIR-1 | Cost-of-Living | ≥10 complaints + viral | HIGH |
| PIR-2 | Trust | Post-policy <50% negative | MEDIUM |
| PIR-3 | Regional | ≥3 autonomy articles/day | MEDIUM |
| PIR-4 | Youth | ≥5 anti-system threads/day | MEDIUM |
| PIR-5 | Stability | Snap election speculation | HIGH |
| PIR-6 | Reform | ≥3 reform fatigue mentions | LOW |
| PIR-7 | Digital | Anti-gov viral >10K | HIGH |
| PIR-8 | BERSAMA | Membership drive | LOW |
| PIR-9 | PH Pact | Seat negotiation leak | MEDIUM |
| PIR-10 | Sabah | Defection cascade rumor | HIGH |

---

## 🔄 Heartbeat Integration

**Daily (23:00 UTC):**
1. Collect from 32 sources
2. Classify by PIR + sentiment
3. Write to `signals/YYYY/MM-DD-signals.jsonl`
4. Update `registry-index.json`
5. Check thresholds → alert if breached
6. Generate synthesis (if MEDIUM/HIGH signals)

**Weekly (Sunday 09:00 UTC):**
1. Aggregate 7-day signals
2. Compute PIR trends (WoW change)
3. Identify emerging narratives
4. Update MEMORY.md
5. Archive old signals (optional)

---

## 📅 Implementation Timeline

| Milestone | Deadline | Status |
|-----------|----------|--------|
| Schema design | 2026-06-13 | ✅ Complete |
| DeerFlow integration | 2026-06-15 | ⏳ Pending |
| First daily pulse (test) | 2026-06-16 | ⏳ Pending |
| Registry index populated | 2026-06-17 | ⏳ Pending |
| Threshold alerting live | 2026-06-18 | ⏳ Pending |
| First daily brief | 2026-07-05 | ⏳ Pending |

---

## 🔗 Related Files

- **Schema doc:** `tools/deer-flow/docs/political-signal-registry-schema.md`
- **Config:** `tools/deer-flow/config.yaml` (32 sources, 10 PIRs)
- **Media landscape:** `memory/2026-06-13.md` (100–150 outlet baseline)

---

**Next Action:** Implement DeerFlow signal writer (June 15)  
**Operator Approval:** Not required (internal schema design)
