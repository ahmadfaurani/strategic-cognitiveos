# DUN Profiling V1 — Configuration Guide

**Version:** 1.0  
**Status:** ✅ Production  
**Last Updated:** 2026-07-01  
**Maintainer:** Political Intelligence Team

---

## 📋 Overview

This document covers configuration options, environment variables, and deployment settings for the DUN Profiling V1 workflow.

---

## 🔧 Environment Variables

### Required Variables

| Variable | Description | Example | Source |
|----------|-------------|---------|--------|
| `SPR_DATA_PATH` | Path to SPR Electoral Roll XLSX files | `/home/p62operator/data/spr/` | Local filesystem |
| `ELECTIONDATA_API_KEY` | ElectionData.MY API key | `edmy_xxxxxxxxxxxx` | https://electiondata.my/console |
| `GITHUB_TOKEN` | GitHub PAT with `repo` scope | `ghp_xxxxxxxxxxxx` | GitHub Settings → Developer Settings |
| `MEMORY_PATH` | Path to memory/ directory for brief storage | `/home/p62operator/memory/` | Local filesystem |

### Optional Variables

| Variable | Description | Default | Example |
|----------|-------------|---------|---------|
| `GITHUB_ORG` | GitHub organization (if not personal) | (user's personal org) | `johor-war-room` |
| `REPO_VISIBILITY` | Default repository visibility | `private` | `private` or `public` |
| `TLP_MARKING` | Default TLP classification | `TLP:AMBER` | `TLP:AMBER`, `TLP:RED`, `TLP:GREEN` |
| `WAR_ROOM_TEAM` | Comma-separated GitHub usernames | (empty) | `user1,user2,user3` |
| `ENABLE_CVS_VALIDATION` | Enable truth validation gate | `true` | `true` or `false` |
| `VALIDATOR_PATH` | Path to truth validator script | `./tools/truth-validator/validate.sh` | Custom path |

---

## 📁 Configuration Files

### 1. Workflow Config (`config.yaml`)

**Location:** `workflows/dun-profiling/config.yaml`

```yaml
# DUN Profiling V1 Configuration

workflow:
  name: "DUN Profiling V1"
  version: "1.0"
  status: "production"

# Input Data Sources
data_sources:
  spr:
    path: "${SPR_DATA_PATH}"
    format: "xlsx"
    filename_pattern: "{code}_{constituency}_as_of_{date}.xlsx"
  
  electiondata:
    api_key: "${ELECTIONDATA_API_KEY}"
    base_url: "https://api.electiondata.my/v1"
    timeout_seconds: 30

# Output Configuration
output:
  memory_path: "${MEMORY_PATH}"
  file_naming: "{code}-{constituency}-{type}-{date}.md"
  date_format: "YYYYMMDD"
  
  github:
    token: "${GITHUB_TOKEN}"
    org: "${GITHUB_ORG}"
    visibility: "${REPO_VISIBILITY}"
    naming_pattern: "analytical-dun-profiling-n{code}-{constituency}"
    collaborators: "${WAR_ROOM_TEAM}"

# CVS Validation
cvs:
  enabled: "${ENABLE_CVS_VALIDATION}"
  validator_path: "${VALIDATOR_PATH}"
  fail_on_error: true
  warn_on_unverified: true

# TLP Classification
tlp:
  default_marking: "${TLP_MARKING}"
  enforce_distribution: true

# Logging
logging:
  level: "INFO"
  format: "json"
  output: "workflows/dun-profiling/logs/"
```

---

### 2. Constituency Registry (`constituencies.yaml`)

**Location:** `workflows/dun-profiling/constituencies.yaml`

```yaml
# Johor DUN Constituencies Registry

state: Johor
total_seats: 56
workflow_version: "1.0"

constituencies:
  # N16 Sungai Balang (P146 Muar)
  - code: N16
    name: Sungai Balang
    parliament: P146
    parliament_name: Muar
    status: "completed"
    completed_date: "2026-06-27"
    github_repo: "analytical-dun-profiling-n16-sungai-balang"
    
  # N17 Semerah (P147 Parit Sulong)
  - code: N17
    name: Semerah
    parliament: P147
    parliament_name: Parit Sulong
    status: "completed"
    completed_date: "2026-06-27"
    github_repo: "analytical-dun-profiling-n17-semerah"
    
  # N27 Layang-Layang (P149 Layang-Layang)
  - code: N27
    name: Layang-Layang
    parliament: P149
    parliament_name: Layang-Layang
    status: "completed"
    completed_date: "2026-07-01"
    github_repo: "analytical-dun-profiling-n27-layang-layang"
    
  # N32 Endau (P154 Mersing)
  - code: N32
    name: Endau
    parliament: P154
    parliament_name: Mersing
    status: "completed"
    completed_date: "2026-06-29"
    github_repo: "pending"
    
  # N41 Puteri Wangsa (P158 Tebrau)
  - code: N41
    name: Puteri Wangsa
    parliament: P158
    parliament_name: Tebrau
    status: "pending"
    priority: "high"
    notes: "Tier-1 urban battleground, MUDA incumbent not defending"
    
  # Add remaining 51 constituencies...
```

---

### 3. Source Registry (`source-registry.yaml`)

**Location:** `workflows/dun-profiling/source-registry.yaml`

```yaml
# Media & Data Source Registry for DUN Profiling

# Tier 1: Official Primary Sources (Highest Trust)
tier1_sources:
  - name: "SPR Electoral Roll"
    type: "xlsx"
    trust_level: "primary"
    url_pattern: "https://www.spr.gov.my/index.php/component/content/article/80-undian/2081-daftar-pemilih"
    update_frequency: "monthly"
    cvs_status: "Primary source - no cross-reference needed"
    
  - name: "ElectionData.MY"
    type: "api"
    trust_level: "primary"
    url: "https://api.electiondata.my/v1"
    api_key_required: true
    cvs_status: "Primary source - verified against SPR"

# Tier 2: Official Secondary Sources (High Trust)
tier2_sources:
  - name: "Wikipedia Malaysia Elections"
    type: "web"
    trust_level: "secondary"
    url_pattern: "https://ms.wikipedia.org/wiki/Pilihan_raya"
    cvs_status: "Cross-reference required"
    
  - name: "Bernama"
    type: "news"
    trust_level: "secondary"
    url: "https://www.bernama.com"
    cvs_status: "Official news agency - high reliability"

# Tier 3: Party & Candidate Sources (Medium Trust)
tier3_sources:
  - name: "UMNO Online"
    type: "party"
    trust_level: "medium"
    url: "https://umno-online.my"
    cvs_status: "Party announcement - verify with news"
    
  - name: "PKR Official"
    type: "party"
    trust_level: "medium"
    url: "https://pkrr.com.my"
    cvs_status: "Party announcement - verify with news"
    
  - name: "PAS Official"
    type: "party"
    trust_level: "medium"
    url: "https://pas.org.my"
    cvs_status: "Party announcement - verify with news"
    
  - name: "MUDA Official"
    type: "party"
    trust_level: "medium"
    url: "https://muda.org.my"
    cvs_status: "Party announcement - verify with news"

# Tier 4: News Media (Variable Trust)
tier4_sources:
  - name: "Sinar Harian"
    type: "news"
    trust_level: "medium"
    url: "https://www.sinarharian.com.my"
    cvs_status: "Verify with second source"
    
  - name: "The Star"
    type: "news"
    trust_level: "medium"
    url: "https://www.thestar.com.my"
    cvs_status: "Verify with second source"
    
  - name: "New Straits Times"
    type: "news"
    trust_level: "medium"
    url: "https://www.nst.com.my"
    cvs_status: "Verify with second source"
    
  - name: "Malaysiakini"
    type: "news"
    trust_level: "medium"
    url: "https://www.malaysiakini.com"
    cvs_status: "Verify with second source"
    
  - name: "Free Malaysia Today"
    type: "news"
    trust_level: "medium"
    url: "https://www.freemalaysiatoday.com"
    cvs_status: "Verify with second source"
```

---

## 🚀 Execution Modes

### Mode 1: Manual (Current Production)

**Description:** Human operator executes each step via OpenClaw agent session.

**Commands:**
```bash
# Step 1: Demographics
openclaw skill run dun-profiling-step1 \
  --spr-xlsx /home/p62operator/data/spr/8_N16_SUNGAI_BALANG_as_of_190626.xlsx \
  --code N16 \
  --name "Sungai Balang"

# Step 2: Candidates
openclaw skill run dun-profiling-step2 \
  --code N16 \
  --name "Sungai Balang" \
  --news-sources "https://..."

# Step 3: Historical
openclaw skill run dun-profiling-step3 \
  --code N16 \
  --api-key ${ELECTIONDATA_API_KEY}

# Step 4: Synthesis
openclaw skill run dun-profiling-step4 \
  --demographic-brief /home/p62operator/memory/n16-demographic-brief.md \
  --candidate-brief /home/p62operator/memory/n16-candidate-brief.md \
  --historical-brief /home/p62operator/memory/n16-historical-brief.md

# Step 5: GitHub Upload
openclaw skill run dun-profiling-step5 \
  --brief-files /home/p62operator/memory/n16-*.md \
  --github-token ${GITHUB_TOKEN} \
  --visibility private
```

**Pros:**
- Full human oversight at each step
- CVS validation enforced manually
- Flexible adjustments per constituency

**Cons:**
- ~2 hours per constituency
- Not scalable to 40+ seats
- Operator fatigue risk

---

### Mode 2: Semi-Automated (Planned)

**Description:** Steps 1-3 automated via Python scripts, Steps 4-5 manual review.

**Commands:**
```bash
# Run automated pipeline for single constituency
python tools/dun-profiling/run-single.py \
  --code N16 \
  --spr-xlsx /home/p62operator/data/spr/8_N16_SUNGAI_BALANG_as_of_190626.xlsx \
  --api-key ${ELECTIONDATA_API_KEY} \
  --output-dir /home/p62operator/memory/

# Review generated briefs
code /home/p62operator/memory/n16-*.md

# Manual CVS validation
./tools/truth-validator/validate.sh /home/p62operator/memory/n16-*.md

# Manual Step 4-5 (synthesis + GitHub upload)
openclaw skill run dun-profiling-step4 ...
openclaw skill run dun-profiling-step5 ...
```

**Pros:**
- ~45 minutes per constituency
- Consistent output format
- Human review retained for synthesis

**Cons:**
- Still requires manual intervention
- Two separate toolchains (Python + OpenClaw)

---

### Mode 3: Fully Automated (Future)

**Description:** All 5 steps automated, single command for batch processing.

**Commands:**
```bash
# Process single constituency
python tools/dun-profiling/run-full.py \
  --code N16 \
  --spr-xlsx /home/p62operator/data/spr/ \
  --api-key ${ELECTIONDATA_API_KEY} \
  --github-token ${GITHUB_TOKEN} \
  --visibility private

# Batch process all constituencies
python tools/dun-profiling/run-batch.py \
  --spr-xlsx /home/p62operator/data/spr/ \
  --api-key ${ELECTIONDATA_API_KEY} \
  --github-token ${GITHUB_TOKEN} \
  --constituencies N16,N17,N27,N32,N41 \
  --parallel 3
```

**Pros:**
- ~25 minutes per constituency (parallel: ~10 min effective)
- Consistent CVS validation
- Scalable to 40+ seats

**Cons:**
- Less human oversight
- Requires robust error handling
- API rate limits (ElectionData.MY, GitHub)

---

## 🔐 Security Configuration

### GitHub Token Permissions

**Required Scopes:**
- `repo` (Full control of private repositories)
- `read:user` (Read user profile for collaborator invites)
- `user:email` (Read email addresses for notifications)

**Token Creation:**
1. Go to GitHub Settings → Developer Settings → Personal Access Tokens
2. Generate new token (classic)
3. Select scopes: `repo`, `read:user`, `user:email`
4. Copy token and store in secure location
5. Add to environment: `export GITHUB_TOKEN=ghp_xxxxxxxxxxxx`

**Security Best Practices:**
- Never commit tokens to Git
- Use environment variables or secret manager
- Rotate tokens every 90 days
- Use separate tokens for development vs production

---

### ElectionData.MY API Key

**Obtain API Key:**
1. Visit https://electiondata.my/console
2. Register for free account
3. Generate API key in dashboard
4. Add to environment: `export ELECTIONDATA_API_KEY=edmy_xxxxxxxxxxxx`

**Rate Limits:**
- Free tier: 100 requests/hour
- Paid tier: 1000 requests/hour
- Batch processing: Use caching to minimize API calls

---

### TLP Classification Enforcement

**TLP Markings:**
- **TLP:RED** — Not for disclosure, restricted to named recipients only
- **TLP:AMBER** — Limited disclosure, war room team only (default)
- **TLP:GREEN** — Limited disclosure, community within organization
- **TLP:CLEAR** — Unlimited disclosure, public

**Enforcement Rules:**
```yaml
tlp_enforcement:
  TLP:RED:
    github_visibility: private
    collaborators_max: 3
    telegram_delivery: false
    email_delivery: encrypted_only
    
  TLP:AMBER:
    github_visibility: private
    collaborators_max: 20
    telegram_delivery: true
    email_delivery: internal_only
    
  TLP:GREEN:
    github_visibility: private
    collaborators_max: 100
    telegram_delivery: true
    email_delivery: true
    
  TLP:CLEAR:
    github_visibility: public
    collaborators_max: unlimited
    telegram_delivery: true
    email_delivery: true
```

---

## 📊 Logging & Monitoring

### Log Configuration

```yaml
logging:
  level: "INFO"  # DEBUG, INFO, WARNING, ERROR, CRITICAL
  format: "json"
  output_dir: "workflows/dun-profiling/logs/"
  rotation:
    max_size_mb: 100
    max_files: 10
    compress: true
    
  fields:
    - timestamp
    - level
    - constituency_code
    - step
    - duration_seconds
    - cvs_status
    - error_code
```

### Example Log Entry

```json
{
  "timestamp": "2026-07-01T07:30:00Z",
  "level": "INFO",
  "constituency_code": "N16",
  "step": "step1_demographics",
  "duration_seconds": 45,
  "cvs_status": "passed",
  "output_file": "/home/p62operator/memory/n16-demographic-brief-20260701.md",
  "message": "Demographic brief generated successfully"
}
```

---

## 🐛 Troubleshooting

### Common Issues

**Issue:** SPR XLSX parsing fails  
**Error:** `ERR-SPX-002: XLSX format changed`  
**Resolution:**
```bash
# Check XLSX structure
python tools/dun-profiling/inspect-xlsx.py \
  --file /home/p62operator/data/spr/8_N16_SUNGAI_BALANG_as_of_190626.xlsx

# Update parser if column names changed
edit tools/dun-profiling/spr-xlsx-parser.py
# Update column mappings
```

**Issue:** ElectionData.MY API rate limited  
**Error:** `429 Too Many Requests`  
**Resolution:**
```bash
# Enable caching
export ELECTIONDATA_CACHE_ENABLED=true
export ELECTIONDATA_CACHE_TTL=3600

# Or upgrade to paid tier
# https://electiondata.my/pricing
```

**Issue:** GitHub repo creation fails  
**Error:** `ERR-GH-001: Token permissions insufficient`  
**Resolution:**
```bash
# Verify token scopes
curl -H "Authorization: token ${GITHUB_TOKEN}" \
  https://api.github.com/user

# Regenerate token with repo scope
# GitHub Settings → Developer Settings → Personal Access Tokens
```

**Issue:** CVS validation fails  
**Error:** `ERR-CVS-001: Missing source citation`  
**Resolution:**
```bash
# Run validator with verbose output
./tools/truth-validator/validate.sh \
  /home/p62operator/memory/n16-demographic-brief.md \
  --verbose

# Edit brief to add missing citations
edit /home/p62operator/memory/n16-demographic-brief.md
```

---

## 📈 Performance Optimization

### Batch Processing Strategy

**For 40 constituencies:**

| Strategy | Time per Seat | Total Time | Parallelization |
|----------|---------------|------------|-----------------|
| Manual (current) | 2 hours | 80 hours | None |
| Semi-automated | 45 min | 30 hours | None |
| Fully automated (serial) | 25 min | 16.7 hours | None |
| Fully automated (parallel x3) | 25 min | 5.6 hours | 3 concurrent |
| Fully automated (parallel x5) | 25 min | 3.3 hours | 5 concurrent |

**Recommended:** Parallel x3 (balance between speed and API rate limits)

---

### Caching Strategy

```yaml
caching:
  enabled: true
  backend: "sqlite"
  database: "/home/p62operator/.cache/dun-profiling/cache.db"
  
  ttl_seconds:
    spr_xlsx_parsing: 86400  # 24 hours
    electiondata_api: 3600   # 1 hour
    candidate_research: 7200 # 2 hours
    historical_analysis: 86400 # 24 hours
    
  invalidation:
    on_spr_update: true
    on_nomination_day: true
    manual_trigger: true
```

---

**Document Control:**
- Version: 1.0
- Status: Production
- Next Review: 2026-07-15
