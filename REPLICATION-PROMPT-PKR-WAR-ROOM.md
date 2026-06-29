# 🎯 REPLICATION PROMPT: PKR War Room Intelligence Automation

**Copy and paste this prompt into OpenClaw to replicate the complete technology stack and workflow.**

---

## 📋 MASTER PROMPT (Copy-Paste Ready)

```
# PKR WAR ROOM INTELLIGENCE REPOSITORY - DEPLOYMENT REQUEST

## Mission Objective
Create a complete, production-ready PKR War Room intelligence repository for electoral campaign use. The repository must include candidate/constituency analysis, vulnerability assessments, campaign strategies, and operational templates—all classified as INTERNAL - WAR ROOM USE ONLY.

## Input Parameters

### Election Context
- **Election Type:** [STATE Election / Parliamentary / By-Election]
- **State/Territory:** [e.g., Johor, Selangor, N15 Kukup]
- **Election Date:** [TBD / Confirmed Date]
- **Party:** PKR (Parti Keadilan Rakyat)

### Scope Selection (Choose One)

**OPTION A: Single Constituency**
- Constituency Name: [e.g., N15 Kukup, P123 Geger]
- Candidate Name: [e.g., Cheah Chee Hong]
- Opponent Name(s): [e.g., Wee Jeck Seng (BN-MCA)]
- Historical Context: [e.g., BN stronghold since 1974]

**OPTION B: State-Level (20+ DUN Seats)**
- Candidate List:
  1. N.01 - [Candidate Name]
  2. N.03 - [Candidate Name]
  3. N.07 - [Candidate Name]
  [Continue for all candidates...]
- Priority Classification:
  - CRITICAL (5): [High-profile candidates, former ministers, AMK chiefs]
  - HIGH (5): [Sitting MPs, state leaders, vulnerable incumbents]
  - STANDARD (10): [First-time candidates, low-profile seats]

## Output Requirements

### Repository Structure (Single Constituency - 13 Files Minimum)

```
repository/
├── README.md (15-20 KB)
│   - Election overview
│   - Repository purpose
│   - Quick start guide
│   - Access instructions
│
├── REPOSITORY-STATUS.md (12-15 KB)
│   - Completion tracking
│   - Update schedule
│   - Version history
│
├── .gitignore (500-700 bytes)
│   - Sensitive file exclusions
│   - Build artifacts
│   - OS files
│
├── docs/
│   ├── candidate-analysis.md (12-16 KB)
│   │   - Candidate biography
│   │   - Political background
│   │   - Public persona
│   │   - Key narratives
│   │
│   ├── constituency-profile.md (14-18 KB)
│   │   - Demographics (ethnicity, age, income)
│   │   - Economic profile
│   │   - Key issues
│   │   - Historical voting patterns
│   │
│   └── polling-district-breakdown.md (18-24 KB)
│       - All PDs listed
│       - 2022 results per PD
│       - Swing analysis
│       - Target PDs identified
│
├── intelligence/
│   └── war-room-brief.md (20-26 KB)
│       - Executive summary
│       - SWOT analysis
│       - Critical vulnerabilities
│       - Offensive opportunities
│       - Resource allocation
│
├── strategy/
│   ├── campaign-strategy.md (24-30 KB)
│   │   - 90-day roadmap
│   │   - Phase 1 (0-30 days): Foundation
│   │   - Phase 2 (31-60 days): Mobilization
│   │   - Phase 3 (61-90 days): GOTV
│   │   - Success metrics
│   │
│   └── messaging-framework.md (24-30 KB)
│       - Core narrative
│       - Key messages (3-5)
│       - Audience segmentation
│       - Attack/defense lines
│
├── historical/
│   ├── 2022-election-results.md (16-20 KB)
│   │   - Full results (all candidates)
│   │   - Vote share by ethnicity
│   │   - Turnout analysis
│   │   - Key takeaways
│   │
│   └── 2018-election-results.md (18-22 KB)
│       - Full results
│       - Comparison with 2022
│       - Swing analysis
│       - Tsunami effect
│
└── sources/
    ├── references.md (22-28 KB)
    │   - 40+ sources listed
    │   - Primary sources (12+)
    │   - Secondary sources (18+)
    │   - Tertiary sources (10+)
    │
    └── fact-check-verification.md (18-24 KB)
        - Verification methodology
        - Claim-by-claim audit
        - Verification rate (target 90%+)
        - Disputed claims flagged
```

**Total Target:** 13 files, 150-250 KB, 90%+ verification rate

---

### Repository Structure (State-Level - 30 Files Minimum)

```
repository/
├── README.md (18-22 KB)
├── EXECUTIVE_SUMMARY.md (20-25 KB)
├── CANDIDATE_INDEX.md (16-20 KB)
├── DEPLOYMENT_SUMMARY.md (18-22 KB)
├── FINAL_DEPLOYMENT_STATUS.md (20-25 KB)
├── .gitignore (500-700 bytes)
│
├── candidate-profiles/ (20 files, 8-10 KB each)
│   ├── N.01-[Constituency]-[Candidate].md
│   ├── N.03-[Constituency]-[Candidate].md
│   [... all 20 candidates ...]
│   └── N.56-[Constituency]-[Candidate].md
│
├── war-room-intel/ (2 files)
│   ├── vulnerability-assessments.md (14-18 KB)
│   │   - Risk matrix (all 20 candidates)
│   │   - CRITICAL/HIGH/MEDIUM/LOW classification
│   │   - Defensive postures
│   │   - Rapid response templates
│   │
│   └── rapid-response-templates.md (16-20 KB)
│       - 10 response templates
│       - Attack scenarios
│       - Escalation protocol
│       - Approval workflow
│
├── digital-strategy/ (1 file)
│   └── platform-strategy.md (14-18 KB)
│       - 5-platform playbook (FB, IG, TikTok, Twitter, WhatsApp)
│       - Content calendar template
│       - Paid ads strategy
│       - Influencer coordination
│
├── templates/ (2 files)
│   ├── biography-template.md (8-10 KB)
│   │   - All formats (short, medium, long)
│   │   - Examples from deployed profiles
│   │   - Customization guide
│   │
│   └── speech-talking-points.md (10-12 KB)
│       - Ceramah structure
│       - Audience adaptations
│       - Attack/defense lines
│       - Closing punchlines
│
└── [Optional: docs/, intelligence/, strategy/, historical/, sources/]
    [Same structure as single constituency, scaled for state-level]
```

**Total Target:** 30 files, 800 KB - 1.2 MB, 90%+ verification rate, 100% candidate coverage

---

## Content Standards

### Classification Headers (Every File)
```markdown
# [Document Title]
**Classification:** INTERNAL - WAR ROOM USE ONLY  
**Election:** [State/Constituency]  
**Date:** [Generation Date]  
**Next Review:** [72-hour cycle / Weekly]  
**Distribution:** PKR State Leadership, Campaign Directors, War Room Staff
```

### Candidate Profile Template (6 Sections)

```markdown
## 1. CANDIDATE OVERVIEW
- Full Name
- Age / Date of Birth
- DUN Seat / Constituency
- Education Background
- Profession
- Party Position
- Profile Type (CRITICAL/HIGH/MEDIUM/LOW)

## 2. PUBLIC PERSONA ANALYSIS
- Core Narrative (1-2 sentences)
- Messaging Themes (3-5 bullet points)
- Unique Selling Points (2-3 bullet points)
- Public Perception (positive/negative/neutral)

## 3. SOCIAL MEDIA FOOTPRINT
| Platform | Status | Followers | Activity Level | Last Post |
|----------|--------|-----------|----------------|-----------|
| Facebook | ✅ Active / ⚠️ Missing / ❌ Emergency | [count] | [High/Med/Low] | [date] |
| Instagram | ✅ / ⚠️ / ❌ | [count] | [High/Med/Low] | [date] |
| TikTok | ✅ / ⚠️ / ❌ | [count] | [High/Med/Low] | [date] |
| Twitter/X | ✅ / ⚠️ / ❌ | [count] | [High/Med/Low] | [date] |
| WhatsApp | ✅ / ⚠️ / ❌ | [N/A] | [Broadcast List] | [N/A] |

## 4. VULNERABILITY ASSESSMENT
### 🔴 CRITICAL Vulnerabilities
- [Specific attack vector with evidence]
- [Defensive posture with rapid response template]

### 🟡 HIGH Vulnerabilities
- [Specific attack vector with evidence]
- [Defensive posture]

### 🟢 MEDIUM/LOW Vulnerabilities
- [Specific attack vector]
- [Monitoring required]

## 5. WAR ROOM RECOMMENDATIONS
### Defensive Posture (Priority 1-3)
1. [Immediate action]
2. [Short-term action]
3. [Ongoing monitoring]

### Offensive Opportunities
- [Opponent vulnerability to exploit]
- [Messaging angle]
- [Target demographic]

### Digital Strategy
- [Platform-specific recommendations]
- [Content priorities]
- [Resource allocation]

## 6. 72-HOUR ACTION PLAN
### Day 1 (Immediate)
- [Task 1]
- [Task 2]
- [Task 3]

### Day 2-3 (Short-Term)
- [Task 1]
- [Task 2]

### Day 4-7 (First Week)
- [Task 1]
- [Task 2]
- [Task 3]

### Success Metrics
- 30-day targets: [measurable outcomes]
- 90-day targets (election period): [measurable outcomes]
```

---

## Research Protocol

### Step 1: Web Searches (40+ queries minimum)

```
# Candidate Research
"[Candidate Name] + PKR + [State] 2026"
"[Candidate Name] + biography + education"
"[Candidate Name] + social media + Facebook Instagram Twitter"
"[Candidate Name] + news + interview + speech"

# Constituency Research
"[Constituency Name] + election results 2022"
"[Constituency Name] + demographics + ethnicity"
"[Constituency Name] + issues + economy + development"

# Opponent Research
"[Opponent Name] + [Party] + record + controversy"
"[Opponent Name] + voting history + parliamentary attendance"
"[Opponent Name] + assets + declaration + SPRM"

# Historical Context
"[Constituency Name] + GE14 2018 results"
"[Constituency Name] + GE15 2022 results"
"[State] + state election history + swing analysis"
```

### Step 2: Web Fetching (15+ pages minimum)

```
# Social Media Profiles
- Facebook official pages
- Instagram profiles
- Twitter/X accounts
- Wikipedia pages (if available)

# News Articles
- Astro Awani
- The Star
- Malaysiakini
- BHarian
- The Rakyat Post
- CNA
- Malay Mail

# Official Sources
- SPR (Suruhanjaya Pilihan Raya)
- Parliament website
- State assembly website
- Government portals
```

### Step 3: Fact-Checking Protocol

```
For each factual claim:
1. Identify source (primary/secondary/tertiary)
2. Cross-reference with 2+ additional sources
3. Mark verification status:
   - ✅ Verified (2+ primary sources)
   - ⚠️ Partially verified (1 primary + 1 secondary)
   - ❌ Unverified (needs human review)
   - 🔴 Disputed (conflicting sources)

Verification Rate = (Verified Claims / Total Claims) × 100%
Target: 90%+
```

---

## Git Deployment Protocol

### Step 1: Initialize Repository

```bash
# Create directory
mkdir -p /home/p62operator/.openclaw/workspace/[repository-name]
cd /home/p62operator/.openclaw/workspace/[repository-name]

# Initialize Git
git init
git branch -m main

# Create .gitignore
cat > .gitignore << 'EOF'
# Sensitive files
*.env
*.key
*.token
private/
opposition-research/

# Build artifacts
node_modules/
dist/

# OS files
.DS_Store
Thumbs.db
EOF
```

### Step 2: Organize Files

```bash
# Create directory structure
mkdir -p docs/ intelligence/ strategy/ historical/ sources/ candidate-profiles/ war-room-intel/ digital-strategy/ templates/

# Move files to appropriate folders
mv candidate-*.md candidate-profiles/
mv vulnerability-*.md war-room-intel/
mv rapid-response-*.md war-room-intel/
mv platform-*.md digital-strategy/
mv *-template.md templates/
```

### Step 3: Git Commits

```bash
# Initial commit
git add .
git commit -m "Initial commit: [Repository Name] War Room Intelligence

Repository Structure:
- X strategic documents
- Y candidate profiles
- Z intelligence files
- Total: N files, XX KB

Classification: INTERNAL - WAR ROOM USE ONLY
Created: $(date -u +%Y-%m-%d)
Verification Rate: 90%+
"

# Add GitHub remote
git remote add origin https://github.com/ahmadfaurani/[repository-name].git

# Push to GitHub
git push -u origin main
```

### Step 4: GitHub Configuration (Manual via Web Interface)

```
1. Go to: https://github.com/ahmadfaurani/[repository-name]
2. Settings > General > Visibility: Change to PRIVATE
3. Settings > Branches > Add branch protection rule:
   - Branch name pattern: main
   - Require pull request reviews before merging: YES
   - Require status checks to pass before merging: YES
   - Require branches to be up to date before merging: YES
4. Settings > Security > Require two-factor authentication: YES
5. Settings > Collaborators > Add people:
   - Election Director (admin access)
   - Digital Lead (write access)
   - Intel Chief (write access)
   - Campaign Managers (write access)
   - PD Chiefs (read access)
```

---

## Quality Assurance Checklist

### File Count Audit
- [ ] Single constituency: 13 files minimum
- [ ] State-level: 30 files minimum
- [ ] No placeholder files (all substantive content)
- [ ] Total size meets target (150+ KB single, 800+ KB bulk)

### Content Quality Audit
- [ ] Factual accuracy (90%+ claims verified)
- [ ] Source diversity (40+ sources, 12+ primary)
- [ ] Internal consistency (no conflicting claims)
- [ ] Actionability (clear campaign guidance)
- [ ] Classification headers applied to all files

### Security Audit
- [ ] GitHub visibility: PRIVATE
- [ ] 2FA required for collaborators
- [ ] Branch protection enabled (main)
- [ ] Access control documented
- [ ] Leak response protocol included

### Documentation Audit
- [ ] README.md complete (overview, quick start)
- [ ] REPOSITORY-STATUS.md tracking update schedule
- [ ] Sources/references.md (40+ sources listed)
- [ ] Fact-check-verification.md (verification methodology)

---

## Performance Targets

| Metric | Single Constituency | State-Level (20) |
|--------|---------------------|------------------|
| **Time to Deploy** | <4 hours | <8 hours |
| **File Count** | 13+ | 30+ |
| **Total Size** | 150-250 KB | 800 KB - 1.2 MB |
| **Verification Rate** | 90%+ | 90%+ |
| **Source Count** | 40+ | 60+ |
| **Candidate Coverage** | N/A | 100% (20/20) |
| **Time Savings** | 68%+ | 71%+ |

---

## Security & Classification

### Classification Levels

| Level | Definition | Access | Storage |
|-------|------------|--------|---------|
| **INTERNAL** | Campaign strategy, candidate profiles | All campaign staff | Private GitHub |
| **RESTRICTED** | Opposition research, vulnerability intel | War Room leads only | Separate private repo |
| **CONFIDENTIAL** | Personal data, financial info | Campaign Director only | Encrypted, offline |

### Access Control Protocol

```
1. Access Request:
   - Email Campaign Director with justification
   - Director approves/rejects within 24 hours

2. If Approved:
   - Add to GitHub collaborator list
   - User enables 2FA immediately
   - Access logged in TOOLS.md

3. Access Revocation:
   - Campaign ends OR
   - Security concern OR
   - Role change
   - Immediate removal from GitHub
```

### Leak Response Protocol

```
IMMEDIATE (0-1 hour):
- Notify War Room Chief via WhatsApp "[REPO]-ALERT"
- Emergency meeting (all leads)
- Assess leak scope (what files, how far)

SHORT-TERM (1-4 hours):
- Damage assessment
- Identify leak source (if possible)
- Prepare public response (if necessary)

MEDIUM-TERM (4-24 hours):
- Public response (if leak is public)
- Security audit (access logs, collaborator review)
- Update access controls (revoke suspicious access)

LONG-TERM (24-72 hours):
- Full security audit
- Update protocols (lessons learned)
- Rebuild repository (if compromised)
```

---

## Update Cycle

### 72-Hour Refresh (Every 3 Days)

```
1. Review candidate profiles (new developments?)
2. Update vulnerability assessments (new attacks?)
3. Refresh social media audit (new posts? follower changes?)
4. Check opponent news (controversies? gaffes?)
5. Update REPOSITORY-STATUS.md with changes
6. Git commit: "Refresh [date] - [summary of changes]"
```

### Weekly Review (Every Sunday, 10:00 UTC)

```
1. Full repository audit (file count, verification rate)
2. Archive old signals (move to memory/signals/archive/)
3. Plan next week's priorities
4. Team briefing (War Room leads)
5. Git commit: "Weekly review [date] - [summary]"
```

### Monthly Review (1st of Month)

```
1. Complete repository rebuild (if needed)
2. Technology stack updates (version upgrades)
3. Review time savings metrics
4. Identify bottlenecks
5. Implement process improvements
6. Update playbooks (if needed)
```

---

## Success Criteria

### Repository is COMPLETE when:

✅ **File Count:** 13+ (single) or 30+ (bulk)  
✅ **Size:** 150+ KB (single) or 800+ KB (bulk)  
✅ **Verification Rate:** 90%+  
✅ **No Placeholder Files:** All substantive content  
✅ **Classification Headers:** Applied to all files  
✅ **GitHub Visibility:** PRIVATE  
✅ **2FA Required:** For all collaborators  
✅ **Branch Protection:** Enabled on main  
✅ **Update Schedule:** Established (72-hour + weekly)  
✅ **Sources Documented:** 40+ sources listed  

### Repository is PRODUCTION-READY when:

✅ All COMPLETE criteria met  
✅ Human review completed (30 min single, 60 min bulk)  
✅ War Room Chief sign-off obtained  
✅ Team onboarding completed  
✅ First update cycle scheduled  

---

## Execution Command

**To begin deployment, respond with:**

```
"Deploy PKR War Room Intelligence Repository

Scope: [Single Constituency / State-Level]
Election: [State/Constituency Name]
Candidates: [List or "See attached"]
Priority: [CRITICAL first / Standard order]
GitHub Repo: [repository-name]

Proceed with 4-phase workflow:
1. Intelligence Collection (48 min)
2. Content Synthesis (35 min)
3. Git Repository Creation (15 min)
4. Quality Assurance (30 min)

Classification: INTERNAL - WAR ROOM USE ONLY
Verification Target: 90%+
Time Target: <4 hours (single) / <8 hours (bulk)
"
```

---

## Reference Repositories

**Study These Before Deployment:**

1. **PRN Johor Focus Seat** (State-Level, 20 Candidates)
   - URL: https://github.com/ahmadfaurani/prn-johor-focus-seat
   - Files: 30 | Size: 1.0 MB | Verification: 92%
   - Status: ✅ COMPLETE (100% candidate coverage)

2. **N15 Kukup** (Single Constituency, BN Stronghold)
   - URL: https://github.com/ahmadfaurani/n15-kukup
   - Files: 13 | Size: 220 KB | Verification: 90.4%
   - Status: ✅ COMPLETE (90.4% verified)

3. **War Room Playbooks** (Documentation)
   - URL: https://github.com/ahmadfaurani/pkr-war-room-playbooks (pending)
   - Files: 2 | Size: 33 KB
   - Contents: Operational Playbook + Quickstart Guide

---

## Support & Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| Web search returns irrelevant content | Refine query (add "PKR", "election", "Malaysia"), use domain_filter |
| Facebook fetch fails (DNS) | Retry with different DNS, use Instagram/Twitter alternative |
| Git authentication fails | Verify token permissions (repo scope), regenerate token |
| LLM generates inaccurate claims | Increase verification threshold (90% → 95%), add primary sources |
| Files in wrong folders | Use standardized directory structure (see above) |
| Repository accidentally public | Settings > General > Visibility > PRIVATE |

### Emergency Contact

- **WhatsApp:** "WAR-ROOM-HELP"
- **GitHub Issues:** https://github.com/ahmadfaurani/prn-johor-focus-seat/issues
- **Documentation:** /home/p62operator/.openclaw/workspace/OPERATIONAL_PLAYBOOK-PKR-WAR-ROOM-AUTOMATION.md

---

**Document Classification:** INTERNAL - WAR ROOM USE ONLY  
**Version:** 1.0 (26 June 2026)  
**Based On:** PRN Johor Focus Seat + N15 Kukup deployments  
**Time Savings:** 68-71% vs manual research  
**Verification Rate:** 90%+  
**Ready for:** Immediate deployment
```

---

## 📎 QUICK REFERENCE CARD

**For rapid deployment, use this condensed version:**

```
Deploy PKR War Room Repository

Scope: [Single/State]
Election: [Name]
Candidates: [List]
GitHub: [repo-name]

Standards:
- Classification: INTERNAL - WAR ROOM USE ONLY
- Files: 13+ (single) / 30+ (bulk)
- Size: 150+ KB / 800+ KB
- Verification: 90%+
- Sources: 40+ / 60+
- Security: PRIVATE, 2FA, branch protection
- Update: 72-hour + weekly cycle

Proceed with 4-phase workflow.
```

---

**This prompt is copy-paste ready for immediate operational replication.**

**Location:** `/home/p62operator/.openclaw/workspace/REPLICATION-PROMPT-PKR-WAR-ROOM.md`  
**Size:** 28 KB  
**Status:** ✅ Production-ready
