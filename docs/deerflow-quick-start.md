# 🚀 DeerFlow Constituency Research - Quick Start Guide

**For:** DAF / Campaign Team  
**Purpose:** Get started with automated constituency research in 5 minutes  
**Prerequisites:** DeerFlow installed, GitHub token configured

---

## ⚡ One-Command Research

### Research a Single Constituency

```bash
cd /home/p62operator/tools/deer-flow/scripts
./constituency-research.sh -c N03 -n Pemanis -s Johor
```

**What happens:**
1. ✅ Collects news from 32 media sources (15 min)
2. ✅ Auto-tags by PIR relevance (5 min)
3. ✅ Grades signal quality (5 min)
4. ✅ Checks escalation thresholds (3 min)
5. ✅ Generates daily brief (5 min)
6. ✅ Creates 13-file research repository (10 min)
7. ✅ Pushes to private GitHub repo (5 min)

**Total time:** 48 minutes (fully automated)  
**Your involvement:** 30-45 min for human review + enhancement

---

## 📦 Batch Processing (20 Constituencies)

### Run Overnight Batch

```bash
cd /home/p62operator/tools/deer-flow/scripts
./constituency-research.sh --batch johor-constituencies.txt
```

**What's in the batch:**
- 20 Johor DUN constituencies
- Priority marginal seats first (N03, N09, N15, N17, N19)
- Then strategic seats (N01, N05, N10, N12, N18)
- Finally safe seats (remaining 10)

**Total time:** ~16 hours (overnight run recommended)  
**Output:** 20 private GitHub repositories + daily briefs

---

## 🎯 Recommended Workflow

### Option A: Conservative (Batch of 5)

```bash
# Create batch file for first 5 priority seats
cat > /tmp/priority-5.txt << EOF
N03,Pemanis,Johor
N09,Bukit Batu,Johor
N15,Kukup,Johor
N17,Skudai,Johor
N19,Permas,Johor
EOF

# Run batch (4 hours)
./constituency-research.sh --batch /tmp/priority-5.txt

# Review results next morning
# Enhance with human analysis
# Proceed to next batch
```

**Pros:** Allows human review between batches  
**Cons:** Takes 4 days to complete all 20

---

### Option B: Aggressive (Full Overnight)

```bash
# Start at 23:00 UTC (after daily collection)
./constituency-research.sh --batch johor-constituencies.txt
```

**Pros:** All 20 done by morning  
**Cons:** Requires 8-10 hours human review day

**Recommended start time:** 23:00 UTC (7am MYT next day)

---

## 📊 What You Get

### Per Constituency:

**1. Signal Registry Entry**
```
memory/signals/2026/06/26-escalated.jsonl
→ All collected signals with PIR tags + quality scores
```

**2. Daily Intelligence Brief**
```
memory/briefs/N03-Pemanis-20260626.md
→ Executive summary, key signals, trends, recommendations
```

**3. Research Repository (GitHub Private)**
```
https://github.com/ahmadfaurani/n03-pemanis
→ 13 comprehensive files:
   - README.md (overview)
   - docs/candidate-analysis-*.md (all candidates)
   - docs/constituency-profile.md (demographics)
   - docs/polling-district-breakdown.md (all districts)
   - intelligence/war-room-brief.md
   - strategy/campaign-strategy.md
   - strategy/messaging-framework.md
   - historical/2018-election-results.md
   - historical/2022-election-results.md
   - sources/references.md
   - sources/fact-check-verification.md
   - REPOSITORY-STATUS.md
   - .gitignore
```

---

## 🔍 Human Review Checklist (30-45 min)

After automated pipeline completes:

### 1. Data Quality (10 min)
```bash
# Check signals collected
cat memory/signals/2026/06/26-escalated.jsonl | jq -r '.[] | select(.constituency=="N03")' | head -20

# Review daily brief
cat memory/briefs/N03-Pemanis-20260626.md
```

**Check:**
- [ ] Signals are relevant to constituency
- [ ] PIR tags look accurate
- [ ] Quality scores >0.7
- [ ] No CRITICAL signals missed

---

### 2. Enhance Brief (10 min)

Edit `memory/briefs/N03-Pemanis-20260626.md`:

**Add:**
- Strategic context not captured by automation
- Historical references (2018, 2022 results)
- Demographic insights
- Personal knowledge of local issues

---

### 3. Generate Documents (20 min)

Use OpenClaw to enhance repository:

```bash
cd /tmp/n03-pemanis

# OpenClaw will auto-generate missing files
# Based on DeerFlow brief + existing data
```

**Files to enhance:**
- Candidate profiles (add personal background)
- Constituency profile (add economic data)
- Campaign strategy (add tactical details)
- Messaging framework (add local nuances)

---

### 4. Final QA (5 min)

```bash
# Check for placeholders
grep -r "TODO\|TBD\|FIXME" /tmp/n03-pemanis/

# Verify all files have content
find /tmp/n03-pemanis -name "*.md" -exec wc -l {} \;

# Commit enhancements
git add -A
git commit -m "Human review: Enhanced candidate profiles, added demographic analysis"
git push origin main
```

---

## 🛠️ Common Commands

### Check Pipeline Status

```bash
# View collection logs
tail -f /tmp/n03-collection.log

# View Signal Registry
cat memory/signals/2026/06/26-escalated.jsonl | jq '.' | less

# List generated repos
ls -la /tmp/ | grep -E "n[0-9]+-"
```

---

### Re-run Specific Phase

```bash
# Re-run collection only (skip git)
./constituency-research.sh -c N03 -n Pemanis -s Johor --skip-git

# Re-run without collection (use existing data)
./constituency-research.sh -c N03 -n Pemanis -s Johor --skip-collection

# Dry run (test without executing)
./constituency-research.sh -c N03 -n Pemanis -s Johor --dry-run
```

---

### Access GitHub Repositories

```bash
# List all constituency repos
curl -s -H "Authorization: token $GITHUB_TOKEN" \
  https://api.github.com/user/repos | \
  jq -r '.[] | select(.name | test("^n[0-9]+-")) | "\(.name) - \(.html_url)"'

# Clone specific repo
git clone https://github.com/ahmadfaurani/n03-pemanis
```

---

## 🚨 Troubleshooting

### "No signals collected"

**Cause:** Search queries too narrow  
**Fix:** Broaden keywords in script (line 95-100)

```bash
# Add more query variations
queries=(
  "$code $name election"
  "$code $name candidate"
  "$name $state election 2026"
  "$name by-election"        # ← Add this
  "$candidate_name campaign"  # ← Add this
)
```

---

### "GitHub repo creation failed"

**Cause:** Token expired or insufficient permissions  
**Fix:** Regenerate GitHub PAT with `repo` scope

```bash
# Verify token
echo $GITHUB_TOKEN

# Test token
curl -H "Authorization: token $GITHUB_TOKEN" \
  https://api.github.com/user
```

---

### "Pipeline too slow"

**Cause:** LLM API rate limiting  
**Fix:** Add delay between requests or increase timeout

```bash
# Add to config.yaml
models:
  - name: aras-qwen-397b
    timeout: 120.0  # Increase from 600.0
    max_retries: 3  # Increase from 2
```

---

## 📈 Performance Tracking

### Monitor Pipeline Metrics

Create `pipeline-metrics.md`:

```markdown
# Pipeline Performance Metrics

## Batch 1 (27 Jun 2026)

| Constituency | Start | End | Duration | Signals | Quality |
|--------------|-------|-----|----------|---------|---------|
| N03 Pemanis | 06:00 | 06:48 | 48 min | 12 | 0.89 |
| N09 Bukit Batu | 06:50 | 07:35 | 45 min | 15 | 0.92 |
| N15 Kukup | 07:37 | 08:22 | 45 min | 18 | 0.87 |

## Averages
- Time per constituency: 46 min
- Signals per constituency: 15
- Average quality score: 0.89
```

---

## 🎓 Training Materials

### For New Team Members

1. **Read SOP:** `docs/deerflow-constituency-research-sop.md`
2. **Watch Demo:** Run dry-run on N03 Pemanis
3. **Practice:** Process one safe seat (e.g., N02 Jementah)
4. **Review:** Compare output with manual N03 research
5. **Certify:** Ready for production batches

---

## 📞 Support

**Technical Issues:**
- Check logs: `/tmp/*-collection.log`
- DeerFlow docs: `/home/p62operator/tools/deer-flow/docs/`
- Contact: HOI Intelligence Ops

**Operational Questions:**
- Review SOP: `docs/deerflow-constituency-research-sop.md`
- Check batch status: `ls -la /tmp/ | grep "n[0-9]"`
- Escalate to: Campaign Manager

---

## ✅ Success Criteria

**Pipeline is successful if:**

- ✅ All 20 constituencies processed by 2 July 2026
- ✅ Each repo has 13+ files with substantive content
- ✅ No placeholder files (TODO/TBD)
- ✅ 90%+ factual accuracy (verified against SPR)
- ✅ All repos private on GitHub
- ✅ Human review completed for all constituencies
- ✅ State-wide synthesis report generated

---

**Quick Start Guide v1.0**  
*Last updated: 26 June 2026, 06:35 UTC*  
**Ready for production use** ✅
