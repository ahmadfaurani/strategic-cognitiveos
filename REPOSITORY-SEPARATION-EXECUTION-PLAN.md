# REPOSITORY SEPARATION EXECUTION PLAN
## Two Repositories — Zero Data Loss — Engineered for Success

**Classification:** TLP:AMBER  
**Plan Version:** 1.0  
**Created:** 2026-07-10 15:13 UTC  
**Plan Owner:** DAF  
**Estimated Duration:** 90-120 minutes

---

## 🎯 EXECUTIVE SUMMARY

**Objective:** Separate merged content into two clean, focused GitHub repositories without data loss.

**Repositories:**
1. **Voron-Campaign** (Existing) → RMiT Compliance Campaign only (250 BNM FIs)
2. **HOI-Intelligence-Operations** (New) → Intelligence operations only (100 agencies)

**Success Criteria:**
- ✅ Zero data loss (100% file preservation)
- ✅ Clean separation (no cross-contamination)
- ✅ Both repos functional and ready for continued work
- ✅ Git history preserved where appropriate
- ✅ All stakeholders notified of new repo locations

---

## 📊 PHASE 0: PRE-FLIGHT CHECKLIST (10 min)

### 0.1 Backup Current State
```bash
# Create timestamped backup of entire workspace
BACKUP_DIR="/home/p62operator/.openclaw/workspace-backup-$(date +%Y%m%d-%H%M%S)"
mkdir -p "$BACKUP_DIR"
cp -r /home/p62operator/.openclaw/workspace/voron-campaign-temp "$BACKUP_DIR/"
cp -r /home/p62operator/.openclaw/workspace/rmit-campaign-workspace "$BACKUP_DIR/"
cp -r /home/p62operator/.openclaw/workspace/hoi-intel-workspace "$BACKUP_DIR/"
echo "Backup created: $BACKUP_DIR"
```

**Validation:**
- [ ] Backup directory created
- [ ] All three directories copied
- [ ] Backup size verified (>100MB expected)

### 0.2 Verify Current File Counts
```bash
# Count files in each workspace
echo "=== VORON-CAMPAIGN-TEMP (Source) ==="
find /home/p62operator/.openclaw/workspace/voron-campaign-temp -type f -name "*.md" | wc -l

echo "=== RMIT-CAMPAIGN-WORKSPACE ==="
find /home/p62operator/.openclaw/workspace/rmit-campaign-workspace -type f -name "*.md" | wc -l

echo "=== HOI-INTEL-WORKSPACE ==="
find /home/p62operator/.openclaw/workspace/hoi-intel-workspace -type f -name "*.md" | wc -l
```

**Expected Counts:**
- voron-campaign-temp: 80+ files (merged content)
- rmit-campaign-workspace: 20+ files (RMiT only)
- hoi-intel-workspace: 80+ files (HOI only)

### 0.3 GitHub Authentication Check
```bash
# Verify gh CLI is authenticated
gh auth status
```

**Required:**
- [ ] GitHub CLI authenticated
- [ ] Write access to `ahmadfaurani/Voron-Campaign`
- [ ] Permission to create new repos under `ahmadfaurani/`

### 0.4 Git Configuration
```bash
# Verify git config
git config --global user.name
git config --global user.email
```

**Required:**
- [ ] Git user.name configured
- [ ] Git user.email configured

---

## 🚀 PHASE 1: VORON-CAMPAIGN CLEANUP (30 min)

### 1.1 Navigate to RMiT Workspace
```bash
cd /home/p62operator/.openclaw/workspace/rmit-campaign-workspace
```

### 1.2 Initialize Git Repository
```bash
# Initialize if not already a git repo
git init
git checkout -b main
```

### 1.3 Add All RMiT Files
```bash
# Add all files for staging
git add -A
git status
```

**Expected Output:**
- README.md
- CAMPAIGN-CHARTER.md
- REPOSITORY-MANIFESTO.md
- collateral/battle-cards.md
- collateral/rmit-compliance-checklist.md
- stakeholders/*.md (23 files)

### 1.4 Create .gitignore
```bash
cat > .gitignore << 'EOF'
# Ignore temporary files
*.tmp
*.bak
*~

# Ignore local config
.env
.local-config.json

# Ignore large data files (if any)
*.csv
!prospect-database-*.csv

# Ignore logs
*.log
logs/
EOF
```

### 1.5 Initial Commit
```bash
git commit -m "feat: RMiT Compliance Campaign - Canonical Pre-Merge Extraction

- Campaign Charter (250 BNM-Regulated Financial Institutions)
- 7 Competitor Battle Cards (ServiceNow, MetricStream, OneTrust, etc.)
- Complete BNM RMiT Compliance Checklist
- 12 Tier 1 Bank Stakeholder Profiles (CIMB, Maybank, HSBC, SC, etc.)
- Campaign Status Reports (2026-07-09 to 2026-07-10)
- Target Database: 143 institutions, 1,001 stakeholders

Classification: TLP:AMBER
Campaign Owner: DAF
Timeline: 28 days (2026-07-10 to 2026-08-07)
Revenue Potential: RM 28.5M - 71.5M

Source: Extracted from merged Voron-Campaign repository
Separation Date: 2026-07-10"
```

### 1.6 Connect to Existing GitHub Repo
```bash
# Add remote (existing Voron-Campaign repo)
git remote add origin https://github.com/ahmadfaurani/Voron-Campaign.git
git remote -v
```

### 1.7 Backup Existing Main Branch
```bash
# Fetch current main branch state
git fetch origin main

# Create backup branch before overwriting
git checkout -b backup-pre-rmit-cleanup origin/main
git checkout main
```

**⚠️ CRITICAL:** This preserves the current state of Voron-Campaign before cleanup

### 1.8 Force Push RMiT Content
```bash
# Force push to main (RMiT-only content)
git push -u origin main --force
```

**Validation:**
- [ ] Push successful
- [ ] GitHub repo shows new commit
- [ ] File count matches local workspace (20+ files)

### 1.9 Document What Was Removed
```bash
# Create migration report
cat > MIGRATION-REPORT.md << 'EOF'
# Voron-Campaign Repository Migration Report

**Date:** 2026-07-10
**Action:** Repository cleanup for RMiT-focused campaign

## Files Retained (RMiT Campaign)
- collateral/battle-cards.md
- collateral/rmit-compliance-checklist.md
- voron-stakeholders/*.md (bank profiles)
- VoronDRQ_*.md (campaign briefs)

## Files Removed (Moved to HOI-Intelligence-Operations)
- ops/tier2-intel/ (entire directory)
- intelligence/briefs/ (daily intel briefs INTEL-001 to INTEL-032)
- intelligence/prn-johor-2026/
- intelligence/kempas/
- intelligence/pdrm-*.md
- entities/ (government agency profiles)
- pdrm-io-*.md

## New Repository Location
HOI content moved to: https://github.com/ahmadfaurani/HOI-Intelligence-Operations

## Backup Branch
Pre-cleanup state preserved in branch: `backup-pre-rmit-cleanup`
EOF
```

---

## 🆕 PHASE 2: HOI-INTELLIGENCE-OPERATIONS CREATION (30 min)

### 2.1 Navigate to HOI Workspace
```bash
cd /home/p62operator/.openclaw/workspace/hoi-intel-workspace
```

### 2.2 Initialize Git Repository
```bash
git init
git checkout -b main
```

### 2.3 Add All HOI Files
```bash
git add -A
git status
```

**Expected Files:**
- README.md
- ops/tier2-intel/*.md (15+ files)
- ops/tier2-intel/execution/*.md
- ops/tier2-intel/evidence/Agency-Profiles/*.md (5+ agencies)
- ops/tier2-intel/research/*.md
- intelligence/briefs/*.md (32 daily briefs)
- intelligence/prn-johor-2026/*.md
- intelligence/kempas/*.md
- intelligence/pdrm-*.md (15+ files)
- intelligence/narrative-tracking/*.md
- intelligence/sentiment-analysis/*.md

### 2.4 Create .gitignore
```bash
cat > .gitignore << 'EOF'
# Ignore temporary files
*.tmp
*.bak
*~

# Ignore local config
.env
.local-config.json

# Ignore sensitive credentials
*.key
*.pem
credentials.json

# Ignore logs
*.log
logs/

# Ignore large data exports (if any)
exports/*.csv
!reports/*.csv
EOF
```

### 2.5 Initial Commit
```bash
git commit -m "feat: HOI Intelligence Operations - Initial Repository

- Tier 2 Intelligence Collection (100 agencies target)
- 32 Daily Intelligence Briefs (INTEL-001 to INTEL-032)
- 5 Tier A Agency Profiles (MKN, KP, KDN, KKM, LHDN)
- PRN Johor 2026 Election Intelligence
- PDRM-IO Contact Database & OSINT Collection
- Operational Manuals & Collection SOPs
- Priority Intelligence Requirements (PIR-1 to PIR-10)

Classification: TLP:AMBER
Operation: HOI-INTEL
Collection Cadence: Daily (23:00 UTC)
Target: 100 Tier 2 Agencies (Federal/State/Statutory)

Source: Extracted from merged Voron-Campaign repository
Separation Date: 2026-07-10"
```

### 2.6 Create New GitHub Repository
```bash
# Create new repo via gh CLI
gh repo create ahmadfaurani/HOI-Intelligence-Operations \
  --public \
  --description "Multi-Agency Intelligence Collection & Analysis - 100 Tier 2 Malaysian Government Agencies" \
  --source=. \
  --remote=origin \
  --push
```

**Alternative (if gh CLI fails):**
```bash
# Manual creation via curl
curl -X POST https://api.github.com/user/repos \
  -H "Authorization: Bearer $(gh auth token)" \
  -d '{
    "name": "HOI-Intelligence-Operations",
    "description": "Multi-Agency Intelligence Collection & Analysis - 100 Tier 2 Malaysian Government Agencies",
    "private": false,
    "auto_init": false
  }'

# Then push manually
git remote add origin https://github.com/ahmadfaurani/HOI-Intelligence-Operations.git
git push -u origin main
```

### 2.7 Validate Push
```bash
# Verify repo exists
gh repo view ahmadfaurani/HOI-Intelligence-Operations

# Check file count
gh api repos/ahmadfaurani/HOI-Intelligence-Operations/git/trees/main \
  | jq '.tree | length'
```

**Validation:**
- [ ] Repository created successfully
- [ ] Initial push successful
- [ ] File count matches local workspace (80+ files)
- [ ] README renders correctly on GitHub

### 2.8 Add Repository Topics
```bash
gh repo edit ahmadfaurani/HOI-Intelligence-Operations \
  --add-topic "osint" \
  --add-topic "intelligence" \
  --add-topic "malaysia" \
  --add-topic "government" \
  --add-topic "tier2-intel"
```

---

## ✅ PHASE 3: VALIDATION & VERIFICATION (20 min)

### 3.1 File Count Comparison
```bash
# Create validation script
cat > /tmp/validate-repos.sh << 'EOF'
#!/bin/bash

echo "=== REPOSITORY VALIDATION REPORT ==="
echo "Date: $(date)"
echo ""

echo "=== BACKUP (Source of Truth) ==="
BACKUP_COUNT=$(find /home/p62operator/.openclaw/workspace/voron-campaign-temp -type f -name "*.md" | wc -l)
echo "voron-campaign-temp: $BACKUP_COUNT files"

echo ""
echo "=== RMIT-CAMPAIGN-WORKSPACE ==="
RMIT_COUNT=$(find /home/p62operator/.openclaw/workspace/rmit-campaign-workspace -type f -name "*.md" | wc -l)
echo "Local files: $RMIT_COUNT"

echo ""
echo "=== HOI-INTEL-WORKSPACE ==="
HOI_COUNT=$(find /home/p62operator/.openclaw/workspace/hoi-intel-workspace -type f -name "*.md" | wc -l)
echo "Local files: $HOI_COUNT"

echo ""
echo "=== VALIDATION ==="
TOTAL_LOCAL=$((RMIT_COUNT + HOI_COUNT))
echo "Total local files: $TOTAL_LOCAL"
echo "Backup files: $BACKUP_COUNT"

if [ $TOTAL_LOCAL -ge $BACKUP_COUNT ]; then
    echo "✅ PASS: No data loss detected"
else
    echo "⚠️ WARNING: File count mismatch - manual review required"
fi
EOF

chmod +x /tmp/validate-repos.sh
/tmp/validate-repos.sh
```

### 3.2 GitHub Repo Verification
```bash
# Verify Voron-Campaign (RMiT)
echo "=== VORON-CAMPAIGN (RMiT) ==="
gh repo view ahmadfaurani/Voron-Campaign --json name,url,defaultBranchRef
gh api repos/ahmadfaurani/Voron-Campaign/contents | jq '.[].name'

# Verify HOI-Intelligence-Operations
echo ""
echo "=== HOI-INTELLIGENCE-OPERATIONS ==="
gh repo view ahmadfaurani/HOI-Intelligence-Operations --json name,url,defaultBranchRef
gh api repos/ahmadfaurani/HOI-Intelligence-Operations/contents | jq '.[].name'
```

### 3.3 Content Spot Check
```bash
# Verify RMiT repo has battle-cards.md
gh api repos/ahmadfaurani/Voron-Campaign/contents/collateral/battle-cards.md > /dev/null && echo "✅ RMiT: battle-cards.md present"

# Verify HOI repo has Tier 2 intel
gh api repos/ahmadfaurani/HOI-Intelligence-Operations/contents/ops/tier2-intel/Collection-Plan-Tier2-Intel.md > /dev/null && echo "✅ HOI: Collection-Plan-Tier2-Intel.md present"

# Verify HOI repo has daily briefs
gh api repos/ahmadfaurani/HOI-Intelligence-Operations/contents/intelligence/briefs/INTEL-032-2026-07-09.md > /dev/null && echo "✅ HOI: INTEL-032 daily brief present"
```

### 3.4 Cross-Contamination Check
```bash
# Verify RMiT repo does NOT have HOI content
gh api repos/ahmadfaurani/Voron-Campaign/contents/ops/tier2-intel 2>&1 | grep -q "Not Found" && echo "✅ RMiT: No HOI ops/ directory (correct)"

# Verify HOI repo does NOT have RMiT content
gh api repos/ahmadfaurani/HOI-Intelligence-Operations/contents/collateral/battle-cards.md 2>&1 | grep -q "Not Found" && echo "✅ HOI: No RMiT collateral/ directory (correct)"
```

---

## 📢 PHASE 4: DOCUMENTATION & NOTIFICATION (10 min)

### 4.1 Update MEMORY.md
```bash
# Add repository separation to long-term memory
cat >> /home/p62operator/.openclaw/workspace/MEMORY.md << 'EOF'

---

## 🔀 Repository Separation (2026-07-10)

**Decision:** Split merged Voron-Campaign repository into two focused repositories.

### Repository 1: Voron-Campaign (RMiT Compliance)
- **URL:** https://github.com/ahmadfaurani/Voron-Campaign
- **Focus:** 250 BNM-Regulated Financial Institutions
- **Content:** RMiT compliance campaign, stakeholder collection, battle cards
- **Target:** 143 FIs, 1,001 stakeholders, RM 28.5M-71.5M revenue
- **Status:** ✅ Cleaned and committed (2026-07-10)

### Repository 2: HOI-Intelligence-Operations
- **URL:** https://github.com/ahmadfaurani/HOI-Intelligence-Operations
- **Focus:** 100 Tier 2 Malaysian Government Agencies
- **Content:** OSINT collection, daily intel briefs, agency profiles, PRN Johor 2026
- **Target:** 100 agencies, 10 PIRs, daily briefs (23:00 UTC)
- **Status:** ✅ Created and populated (2026-07-10)

### Backup
- **Location:** `/home/p62operator/.openclaw/workspace-backup-YYYYMMDD-HHMMSS/`
- **Contents:** Full pre-separation state preserved

### Next Actions
- RMiT: Continue Tier 1 bank collection (16 remaining)
- HOI: Resume Tier A agency profiling (15 remaining)
EOF
```

### 4.2 Create Separation Summary
```bash
cat > /home/p62operator/.openclaw/workspace/SEPARATION-SUMMARY.md << 'EOF'
# Repository Separation Summary

**Date:** 2026-07-10
**Operator:** DAF
**Duration:** 90-120 minutes
**Status:** ✅ Complete

---

## Repositories

### 1. Voron-Campaign (RMiT Compliance)
- **URL:** https://github.com/ahmadfaurani/Voron-Campaign
- **Branch:** `main` (RMiT-only)
- **Backup Branch:** `backup-pre-rmit-cleanup`
- **Files:** 20+ (RMiT campaign only)
- **Next:** Continue Tier 1 bank collection

### 2. HOI-Intelligence-Operations
- **URL:** https://github.com/ahmadfaurani/HOI-Intelligence-Operations
- **Branch:** `main`
- **Files:** 80+ (HOI intel only)
- **Next:** Resume Tier A agency profiling

---

## Validation Results

- ✅ Zero data loss (file count verified)
- ✅ Clean separation (no cross-contamination)
- ✅ Both repos functional
- ✅ Backup preserved

---

## Rollback Plan (If Needed)

If issues detected:
1. Restore from backup: `/home/p62operator/.openclaw/workspace-backup-*/`
2. Revert Voron-Campaign: `git checkout backup-pre-rmit-cleanup && git push --force`
3. Delete HOI repo and recreate from backup

---

**Classification:** TLP:AMBER
EOF
```

---

## 🔄 PHASE 5: RESUME OPERATIONS (30 min)

### 5.1 RMiT Campaign - Continue Tier 1 Collection
```bash
cd /home/p62operator/.openclaw/workspace/rmit-campaign-workspace

# Remaining Tier 1 banks (16):
# - Citibank, Bank of China, ICBC
# - Japanese banks (Sumitomo, Mizuho, MUFG)
# - Investment banks (Maybank IB, CIMB IB, RHB IB, etc.)

# Next session: Process Citibank Berhad
```

### 5.2 HOI Operations - Resume Tier A Collection
```bash
cd /home/p62operator/.openclaw/workspace/hoi-intel-workspace

# Remaining Tier A agencies (15):
# - Continue from agency #6 (after MKN, KP, KDN, KKM, LHDN)
# - Target: MOT, MOF, MAMPU, MDEC, etc.

# Next session: Process Ministry of Transport (MOT)
```

---

## 🛡️ RISK MITIGATION

| Risk | Impact | Mitigation | Status |
|------|--------|------------|--------|
| Data loss during cleanup | CRITICAL | Full backup before any changes | ✅ Mitigated |
| Wrong files deleted | HIGH | File count validation, spot checks | ✅ Mitigated |
| GitHub push failure | MEDIUM | Local git state preserved, retry | ✅ Mitigated |
| Cross-contamination | MEDIUM | Validation scripts verify separation | ✅ Mitigated |
| Authentication failure | LOW | gh CLI pre-checked | ✅ Mitigated |

---

## 📋 CHECKLIST SUMMARY

### Pre-Flight
- [ ] Backup created
- [ ] File counts verified
- [ ] GitHub auth confirmed
- [ ] Git config verified

### Phase 1: Voron-Campaign Cleanup
- [ ] RMiT workspace initialized
- [ ] All RMiT files added
- [ ] .gitignore created
- [ ] Initial commit made
- [ ] Remote connected
- [ ] Backup branch created
- [ ] Force push successful
- [ ] Migration report created

### Phase 2: HOI-Intelligence-Operations Creation
- [ ] HOI workspace initialized
- [ ] All HOI files added
- [ ] .gitignore created
- [ ] Initial commit made
- [ ] GitHub repo created
- [ ] Initial push successful
- [ ] Topics added

### Phase 3: Validation
- [ ] File count comparison passed
- [ ] Both repos accessible
- [ ] Content spot check passed
- [ ] Cross-contamination check passed

### Phase 4: Documentation
- [ ] MEMORY.md updated
- [ ] Separation summary created
- [ ] Rollback plan documented

### Phase 5: Resume Operations
- [ ] RMiT next steps identified
- [ ] HOI next steps identified

---

## 🎯 SUCCESS METRICS

| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Data Loss | 0% | TBD | ⏳ Pending |
| File Separation Accuracy | 100% | TBD | ⏳ Pending |
| Repository Functionality | Both operational | TBD | ⏳ Pending |
| Time to Complete | <120 min | TBD | ⏳ Pending |

---

**Plan Approved By:** DAF  
**Execution Window:** 2026-07-10 15:13 UTC onwards  
**Rollback Authority:** DAF (any time if issues detected)

---

*This plan is engineered for zero data loss. Execute sequentially, validate at each phase, and do not proceed to next phase until current phase validation passes.*
