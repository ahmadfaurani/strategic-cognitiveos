# Memory Harness — Loop Engineering Infrastructure

**Purpose:** Provide the feedback loop infrastructure for continuous truth validation improvement.

**Status:** ✅ Built (embedding-independent)

---

## 📁 Components

| Script | Purpose | Loop | Embedding Required? |
|--------|---------|------|---------------------|
| `indexer.sh` | Index memory files into QMD | Loop 1 | ❌ No |
| `retriever.sh` | Keyword search across memory | Loop 2 | ❌ No |
| `archiver.sh` | Archive old memory files | Maintenance | ❌ No |
| `feedback-capture.sh` | Capture human corrections | **Loop 3** | ❌ No |
| `calibration-check.sh` | Track confidence accuracy | **Loop 4** | ❌ No |

---

## 🚀 Quick Start

### 1. Index Memory Files

```bash
./tools/memory-harness/indexer.sh
```

**What it does:**
- Scans `MEMORY.md` and `memory/*.md`
- Indexes `sources/war-room` and `sources/technical-runbooks`
- Triggers QMD reindex (if gateway is running)

---

### 2. Search Memory

```bash
# Keyword search
./tools/memory-harness/retriever.sh "N17 Semerah"

# Limit results
./tools/memory-harness/retriever.sh "turnout analysis" -n 5

# Filter by date
./tools/memory-harness/retriever.sh "BN candidate" -d 2026-06-27

# JSON output
./tools/memory-harness/retriever.sh "validation" -j
```

---

### 3. Archive Old Files

```bash
# Dry run (see what would be archived)
./tools/memory-harness/archiver.sh -d 30 -n

# Archive files >30 days old (keep 10 most recent)
./tools/memory-harness/archiver.sh -d 30 -k 10

# List archivable files
./tools/memory-harness/archiver.sh -l
```

**Why:** Reduces bootstrap load (MEMORY.md was 28% truncated per `openclaw doctor`)

---

### 4. Capture Feedback (Loop 3)

```bash
# Add factual correction
./tools/memory-harness/feedback-capture.sh add \
  -f memory/n17-brief.md \
  -c "BN won by 4,041 votes" \
  -t factual \
  -o "4,041" \
  -n "4,042" \
  -s "SPR official data"

# Add confidence correction
./tools/memory-harness/feedback-capture.sh add \
  -f memory/n17-brief.md \
  -c "Turnout >80% favors PH" \
  -t confidence \
  -o "HIGH" \
  -n "MEDIUM" \
  -m "Historical pattern, not verified data"

# List recent feedback
./tools/memory-harness/feedback-capture.sh list -n 10

# Show statistics
./tools/memory-harness/feedback-capture.sh stats
```

**Output:** `memory/validation-feedback.jsonl`

---

### 5. Analyze Calibration (Loop 4)

```bash
# Analyze feedback and update calibration
./tools/memory-harness/calibration-check.sh analyze

# Generate calibration report
./tools/memory-harness/calibration-check.sh report

# Show source accuracy (placeholder)
./tools/memory-harness/calibration-check.sh source
```

**Output:** `memory/confidence-calibration.json`, `memory/source-accuracy.json`

---

## 📊 Data Files

| File | Purpose | Format |
|------|---------|--------|
| `memory/validation-feedback.jsonl` | Human corrections (Loop 3) | JSONL (one entry per correction) |
| `memory/confidence-calibration.json` | Tag accuracy tracking | JSON |
| `memory/source-accuracy.json` | Source reliability over time | JSON |

### Feedback Entry Schema

```json
{
  "id": "uuid-or-timestamp",
  "timestamp": "2026-06-28T10:30:00Z",
  "file": "memory/n17-brief.md",
  "claim": "BN won by 4,041 votes",
  "type": "factual|confidence|source|citation",
  "original": "4,041",
  "corrected": "4,042",
  "source": "SPR official data",
  "note": "Optional context"
}
```

---

## 🔄 Integration with Truth Validator

### Validation Gate Workflow

```bash
# Generate brief
./generate-brief.sh > memory/draft-brief.md

# Validate (exit code 1 = failed, blocks delivery)
./tools/truth-validator/validate.sh memory/draft-brief.md || exit 1

# If validation fails, fix and re-validate
# If validation passes, deliver

# If human later finds error, capture feedback
./tools/memory-harness/feedback-capture.sh add -f memory/draft-brief.md ...

# Monthly: analyze calibration
./tools/memory-harness/calibration-check.sh analyze
```

---

## 🎯 Success Metrics

| Metric | Target | Current |
|--------|--------|---------|
| Validation gate coverage | 100% of briefs | ✅ Implemented |
| Feedback capture time | <2 min per correction | ✅ Script ready |
| Calibration accuracy (HIGH tag) | >90% | ⏳ Awaiting data |
| Archive bootstrap load | <10KB MEMORY.md | ⏳ Pending first archive |

---

## 🛠️ Maintenance

### Daily (Automated via Heartbeat)
- Index new memory files
- Capture any feedback from corrections

### Weekly
- Review feedback statistics
- Identify patterns in corrections

### Monthly (Loop 4)
```bash
./tools/memory-harness/calibration-check.sh analyze
./tools/memory-harness/calibration-check.sh report
./tools/truth-validator/monthly-review.sh
```

---

## 📝 Examples

### Example 1: Capture Factual Error

```bash
# Human notices wrong vote count in brief
./tools/memory-harness/feedback-capture.sh add \
  -f memory/n33-tenggaroh-brief.md \
  -c "PN received 9,172 votes" \
  -t factual \
  -o "9,172" \
  -n "9,173" \
  -s "SPR official results" \
  -m "Off by 1 vote"
```

### Example 2: Capture Confidence Miscalibration

```bash
# Human notices HIGH confidence was wrong
./tools/memory-harness/feedback-capture.sh add \
  -f memory/n41-puteri-wangsa-brief.md \
  -c "MUDA will retain seat" \
  -t confidence \
  -o "HIGH" \
  -n "MEDIUM" \
  -m "Incumbent not defending, race too close"
```

### Example 3: Analyze Monthly Trends

```bash
# See which confidence tags are most accurate
./tools/memory-harness/calibration-check.sh report

# Output example:
# Confidence Accuracy:
#   HIGH:   45/50 (90%)
#   MEDIUM: 12/20 (60%)
#   LOW:    3/5 (60%)
#
# Recommendation: MEDIUM and LOW tags need calibration
```

---

## 🔜 Future Enhancements (Requires Embedding API)

- [ ] Semantic search (currently keyword-only)
- [ ] Auto-suggest relevant prior briefs during validation
- [ ] Dreaming cycle synthesis (3 AM UTC pattern detection)
- [ ] Auto-cluster feedback by topic
- [ ] Source reliability scoring from feedback patterns

---

**Related:**
- Truth Validator: `tools/truth-validator/README.md`
- Source Registry: `tools/source-registry/README.md`
- Quick Start: `tools/truth-validator/QUICKSTART.md`
