# 🚀 QUICKSTART GUIDE: War Room Repository Replication
**Classification:** INTERNAL - WAR ROOM USE ONLY  
**Version:** 1.0 (26 June 2026)  
**Time to Deploy:** 2-3 hours (single constituency), 6-8 hours (state-level)

---

## ⚡ FASTEST PATH TO DEPLOYMENT

**Goal:** Create a production-ready War Room intelligence repository in under 3 hours.

**Prerequisites:**
- ✅ OpenClaw installed (`npm install -g openclaw`)
- ✅ GitHub account with repo permissions
- ✅ Git token (repo scope)
- ✅ Internet connection

---

## 📋 STEP-BY-STEP (Single Constituency)

### Step 1: Initialize Repository (5 minutes)

```bash
# Create workspace directory
mkdir -p /home/p62operator/.openclaw/workspace/<constituency-name>
cd /home/p62operator/.openclaw/workspace/<constituency-name>

# Initialize Git
git init
echo "# <Constituency Name> - PKR War Room Intelligence" > README.md
git add README.md
git commit -m "Initial commit"

# Create GitHub repo (via web or CLI)
# gh repo create <constituency-name> --private --source=. --push
```

### Step 2: Request Intelligence Generation (30 minutes)

**User Prompt to OpenClaw:**
```
Create a complete PKR War Room intelligence repository for [CONST Constituency Name].

Requirements:
- 13 standard files (README, candidate analysis, constituency profile, polling districts, war room brief, campaign strategy, messaging framework, historical results 2018+2022, references, fact-check verification, repository status, .gitignore)
- Classification: INTERNAL - WAR ROOM USE ONLY
- Include vulnerability assessments, campaign strategy, messaging framework
- Target size: 150-250 KB
- Verification rate: 90%+

Deploy to GitHub: https://github.com/ahmadfaurani/<constituency-name>
```

**OpenClaw Actions:**
1. Run web searches (constituency, candidates, opponents)
2. Fetch social media profiles
3. Generate structured documents
4. Create Git commits
5. Push to GitHub

### Step 3: Review & Approve (30 minutes)

**Human Reviewer Checklist:**
```markdown
## Quick Audit (30 min)

### File Count
- [ ] 13 required files present
- [ ] No placeholder files
- [ ] Total size: 150+ KB

### Spot-Check (3 files)
- [ ] README.md (overview accurate?)
- [ ] Candidate analysis (vulnerabilities correct?)
- [ ] Campaign strategy (actionable?)

### Security
- [ ] Classification headers applied
- [ ] GitHub repo set to PRIVATE
- [ ] 2FA enabled

### Approval
"I certify this repository is COMPLETE and ready for campaign use."

Signed: _________________
Date: ___________________
```

### Step 4: Deploy to GitHub (10 minutes)

```bash
# Add GitHub remote
git remote add origin https://github.com/ahmadfaurani/<constituency-name>.git

# Push to GitHub
git push -u origin main

# Configure GitHub (via web interface):
1. Settings > General > Visibility: PRIVATE
2. Settings > Branches > Add branch protection rule (main)
3. Settings > Security > Require two-factor authentication: YES
4. Settings > Collaborators > Add team members
```

### Step 5: Team Onboarding (15 minutes)

```bash
# Add War Room staff to GitHub:
1. Settings > Collaborators > Add people
2. Enter GitHub usernames (Election Director, Digital Lead, Intel Chief)
3. Set permission level (write access)
4. Notify team via WhatsApp/Telegram

# Team members must:
1. Accept invitation
2. Enable 2FA
3. Clone repository: git clone https://github.com/ahmadfaurani/<constituency-name>.git
4. Read README.md
```

**Total Time:** 90 minutes (1.5 hours)  
**Manual Equivalent:** 4-5 hours  
**Time Savings:** 68-70%

---

## 📦 STEP-BY-STEP (State-Level, 20 Candidates)

### Step 1: Initialize Repository (10 minutes)

```bash
# Create workspace directory
mkdir -p /home/p62operator/.openclaw/workspace/<state>-focus-seat
cd /home/p62operator/.openclaw/workspace/<state>-focus-seat

# Initialize Git
git init

# Create directory structure
mkdir -p candidate-profiles/ war-room-intel/ digital-strategy/ templates/ docs/

# Create README
cat > README.md << 'EOF'
# <State Name> PKR War Room Intelligence

**Classification:** INTERNAL - WAR ROOM USE ONLY  
**Election Date:** [TBD]  
**Candidates:** 20 DUN seats

## Repository Structure
- candidate-profiles/ (20 files)
- war-room-intel/ (vulnerability assessments, rapid response)
- digital-strategy/ (platform playbook)
- templates/ (biographies, speech talking points)
- docs/ (strategic documents)

## Access
Private repository. 2FA required.
EOF

git add .
git commit -m "Initial commit: <State> War Room structure"
```

### Step 2: Request Candidate Intelligence (3-4 hours)

**User Prompt to OpenClaw:**
```
Create complete PKR War Room intelligence repository for [STATE Name] state election.

Candidate List (20 DUN seats):
1. N.01 - [Candidate Name]
2. N.03 - [Candidate Name]
[... all 20 candidates ...]

Requirements:
- 20 candidate profiles (standard template: overview, persona, social media, vulnerabilities, recommendations, 72-hour plan)
- 5 strategic documents (README, Executive Summary, Candidate Index, Deployment Summary, Final Status)
- 2 war room intel files (vulnerability assessments, rapid response templates)
- 1 digital strategy playbook (5-platform: FB, IG, TikTok, Twitter, WhatsApp)
- 2 operational templates (biographies, speech talking points)
- Total: 30 files, 800 KB - 1.2 MB
- Priority: CRITICAL (5) → HIGH (5) → STANDARD (10)
- Verification rate: 90%+

Deploy to GitHub: https://github.com/ahmadfaurani/<state>-focus-seat
```

**OpenClaw Workflow:**
1. Batch research (5 candidates at a time)
2. Generate profiles (prioritized order)
3. Create strategic documents
4. Git commits (logical grouping)
5. Push to GitHub

**Time:** 3-4 hours (automated) + 60 min (human review) = 4-5 hours total

### Step 3: Human Review (60 minutes)

**Two Reviewers Split Workload:**
```bash
# Reviewer 1: Candidate Profiles (1-10)
# Reviewer 2: Candidate Profiles (11-20) + Strategic Docs

## Review Checklist (30 min per reviewer)

### Sample 5 Profiles (20%)
- [ ] Factual accuracy (names, ages, positions correct?)
- [ ] Vulnerability assessments (realistic attack vectors?)
- [ ] Social media audit (links working?)
- [ ] Recommendations (actionable?)

### Strategic Documents
- [ ] Executive Summary (strategic alignment?)
- [ ] Vulnerability Assessments (all 20 candidates covered?)
- [ ] Digital Strategy (platform-specific guidance?)

### Approval
"Repository reviewed and approved for campaign use."

Reviewer 1: _________________  Date: _______
Reviewer 2: _________________  Date: _______
```

### Step 4: Final Deployment (15 minutes)

```bash
# Final commit
git add .
git commit -m "Complete deployment - 20/20 candidate profiles

Repository Statistics:
- 30 files total
- 20 candidate profiles (5 CRITICAL + 5 HIGH + 10 STANDARD)
- 5 strategic documents
- 2 war room intel files
- 1 digital strategy playbook
- 2 operational templates
- Total size: ~1.0 MB
- Verification rate: 90%+

Classification: INTERNAL - WAR ROOM USE ONLY
"

# Push to GitHub
git push -u origin main

# Configure GitHub:
1. Visibility: PRIVATE
2. Branch protection (main)
3. 2FA required
4. Add collaborators (10-15 staff)
```

### Step 5: Team Onboarding (30 minutes)

```bash
# Add War Room staff:
- Election Director (admin access)
- Digital Lead (write access)
- Intel Chief (write access)
- Campaign Managers (write access)
- PD Chiefs (read access)

# Onboarding email/WhatsApp:
"War Room Repository Deployed

URL: https://github.com/ahmadfaurani/<state>-focus-seat
Access: Private (invitation sent)
2FA: Required

Next Steps:
1. Accept GitHub invitation
2. Enable 2FA
3. Clone repository
4. Read README.md
5. Review your assigned candidate profile(s)

First briefing: [Date/Time]
"
```

**Total Time:** 5-6 hours  
**Manual Equivalent:** 15-20 hours  
**Time Savings:** 68-70%

---

## 🎯 SUCCESS CRITERIA

### Repository Must Have:

**File Count:**
- ✅ Single constituency: 13 files minimum
- ✅ State-level: 30 files minimum

**Size:**
- ✅ Single constituency: 150+ KB
- ✅ State-level: 800 KB - 1.2 MB

**Quality:**
- ✅ Verification rate: 90%+
- ✅ No placeholder files
- ✅ All claims sourced (40+ sources)
- ✅ Internal consistency (no conflicts)

**Security:**
- ✅ GitHub visibility: PRIVATE
- ✅ 2FA required
- ✅ Classification headers applied
- ✅ Access control documented

**Actionability:**
- ✅ Clear campaign guidance
- ✅ Vulnerability assessments (all candidates)
- ✅ Rapid response templates
- ✅ 72-hour action plans
- ✅ Success metrics (30-day, 90-day)

---

## 🚨 COMMON PITFALLS

### ❌ Mistake 1: Skipping Human Review
**Problem:** LLM generates inaccurate claims  
**Solution:** Mandatory 30-min human review (spot-check 20% of content)

### ❌ Mistake 2: Public Repository
**Problem:** Sensitive intel exposed  
**Solution:** Double-check GitHub visibility (Settings > General > Visibility)

### ❌ Mistake 3: No 2FA
**Problem:** Account compromise risk  
**Solution:** Require 2FA for all collaborators (Settings > Security)

### ❌ Mistake 4: Incomplete Source Documentation
**Problem:** Can't verify claims  
**Solution:** Include sources/references.md (40+ sources minimum)

### ❌ Mistake 5: No Update Schedule
**Problem:** Intelligence goes stale  
**Solution:** Establish 72-hour update cycle (weekly reviews)

---

## 📞 SUPPORT

**If You Get Stuck:**

1. **Git Issues:** Check Git token permissions (repo scope required)
2. **Web Search Fails:** Refine query (add "PKR", "election", "Malaysia")
3. **Facebook Fetch Fails:** Use alternative source (Instagram, Twitter)
4. **LLM Quality Issues:** Increase verification threshold (90% → 95%)

**Emergency Contact:**
- WhatsApp: "WAR-ROOM-HELP"
- Email: [TBD]
- GitHub Issues: https://github.com/ahmadfaurani/prn-johor-focus-seat/issues

---

## 📚 REFERENCE REPOSITORIES

**Production Examples:**
1. **PRN Johor Focus Seat** (20 candidates, 30 files, 1.0 MB)
   - URL: https://github.com/ahmadfaurani/prn-johor-focus-seat
   - Status: ✅ COMPLETE (100% candidate coverage)

2. **N15 Kukup** (BN stronghold, 13 files, 220 KB)
   - URL: https://github.com/ahmadfaurani/n15-kukup
   - Status: ✅ COMPLETE (90.4% verification rate)

**Study These Repositories:**
- File structure
- Classification headers
- Vulnerability assessment format
- Campaign strategy templates
- Source documentation style

---

## ✅ DEPLOYMENT CHECKLIST

### Pre-Deployment
- [ ] OpenClaw installed
- [ ] GitHub account ready
- [ ] Git token generated (repo scope)
- [ ] Candidate/constituency list prepared

### During Deployment
- [ ] Repository initialized
- [ ] Intelligence generated
- [ ] Files organized (correct folders)
- [ ] Git commits logical
- [ ] Pushed to GitHub

### Post-Deployment
- [ ] Visibility: PRIVATE
- [ ] 2FA required
- [ ] Branch protection enabled
- [ ] Collaborators added
- [ ] Team notified
- [ ] First review scheduled (72-hour cycle)

### Quality Assurance
- [ ] File count meets target
- [ ] Size meets target
- [ ] Verification rate 90%+
- [ ] No placeholder files
- [ ] Classification headers applied
- [ ] Update schedule established

---

**Document Classification:** INTERNAL - WAR ROOM USE ONLY  
**Distribution:** PKR State Leadership, Campaign Directors, War Room Staff  
**Created:** 26 June 2026  
**Next Review:** 3 July 2026  

**Prepared by:** DeerFlow + OpenClaw Hybrid Research Pipeline
