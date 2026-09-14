# HEARTBEAT.md

## Heartbeat Principle
Autonomy exists to preserve execution momentum, not to create uncontrolled background behavior.

## Default Heartbeat Objectives
- Review active workstreams
- Detect pending actions or stale items
- Check whether a follow-up artifact is needed
- Surface unresolved blockers
- Trigger bounded reminders, summaries, or next-step prompts
- Refresh project memory where meaningful changes occurred

## Suggested Loop Stages
1. Load active project memory
2. Review pending tasks, drafts, and dependencies
3. Check time-sensitive milestones or follow-ups
4. Determine whether action is required
5. If action is required, generate a bounded execution object
6. Log what changed
7. Wait for next cycle

## Example Heartbeat Cadence
- **Fast loop:** every 15 to 30 minutes for active execution windows
- **Standard loop:** every 4 to 8 hours for normal project continuity
- **Executive review loop:** daily summary cycle
- **Strategic review loop:** weekly synthesis cycle

## Heartbeat Modes

### Passive Monitoring
Tracks state and identifies what needs attention.
Does not initiate external action.

### Assisted Follow-Through
Prepares draft outputs, reminders, status deltas, or next-step summaries for operator review.

### Controlled Automation
Executes pre-approved automations such as task refresh, report compilation, or message drafting within policy boundaries.

## Trigger Conditions
- pending action item lacks owner follow-up
- draft exists but remains incomplete
- deadline or meeting window is approaching
- new evidence materially affects an active project
- a project has gone stale but remains strategic

## Boundaries
- no uncontrolled external action;
- no autonomous stakeholder outreach unless explicitly approved;
- no memory overwrite without confidence;
- no policy bypass for speed.

## Default Heartbeat Outputs
- workstream status snapshot
- next action recommendation
- unresolved decision list
- follow-up draft suggestion
- stale-item escalation prompt
- **GitHub engagement sync** (CBO-01 repository — commit status, pending drafts, pipeline updates)

---

## GitHub Engagement Sync (Every Heartbeat)

**Purpose:** Ensure all commercial and intelligence engagements are reflected in GitHub repositories with current status, drafts, and pipeline updates.

**Repositories:**
- `https://github.com/ahmadfaurani/cbo-01-commercial-ops` (CBO-01)

**Sync Tasks:**
1. Check for uncommitted drafts in workspace directories
2. Verify latest commit status matches documented progress
3. Update pipeline/workstream status files if engagements changed
4. Flag any engagement artifacts ready for commit
5. Log sync status in daily memory file

**Automation Boundary:**
- Commits require operator approval (no auto-push for engagement-sensitive content)
- Draft status updates are informational only
- TLP:AMBER documents require explicit approval before any git operation

**Output Format:**
```markdown
### GitHub Sync Status (HH:MM UTC)
| Repo | Latest Commit | Pending Drafts | Last Sync |
|------|---------------|----------------|------------|
| cbo-01-commercial-ops | abc1234 | 2 SOW drafts | 2026-04-26 11:58 |
```

**Cadence:** Every heartbeat cycle (4-8 hours standard, 15-30 min during active execution)

---

## AI Infrastructure CVE Monitoring → Attack Vector Registry Integration (Every Heartbeat)

**Purpose:** Detect emerging vulnerabilities in AI inference, deployment, and orchestration infrastructure within hours of disclosure. CVE-2026-33626 (LMDeploy SSRF) demonstrated a 13-hour window from disclosure to active exploitation — traditional weekly vulnerability scans are insufficient for AI infrastructure.

**Integration:** This workflow now feeds directly into the Attack Vector Registry (AVR). New CVEs are automatically assessed for AVR entry creation, existing entries are updated with exploitation status changes, and CRITICAL items trigger immediate escalation.

**AVR Integration:**
- New CVEs → Create AVR entry if affects deployed technology
- Exploitation status change → Update existing AVR entry + escalate if CRITICAL
- POC availability change → Update AVR entry + flag if weaponized
- Patch release → Update AVR entry mitigation status

**Monitoring Scope:**

| Component | Type | Priority | Our Deployment Status |
|-----------|------|----------|----------------------|
| **LMDeploy** | Inference/Serving | 🔴 CRITICAL | ❌ Not deployed (**CVE-2026-33626 excluded**) |
| **Ollama** | LLM Backend | 🔴 CRITICAL | ❌ **REMOVED** (2026-05-01) — CVE-2026-5757 mitigation |
| **OpenWebUI** | AI Interface | 🔴 CRITICAL | ✅ Running (port 8080) |
| **vLLM** | Inference Engine | 🔴 CRITICAL | ✅ Remote API (arasintegrasi.ai) |
| **AIL Framework** | Dark Web Intel | 🟡 HIGH | ✅ Running (v6.7) |
| **SearXNG** | Search Backend | 🟡 HIGH | ✅ Running (port 3000) |
| **ZeroTier** | Network Layer | 🟡 HIGH | ✅ Running (1.16.1) |
| **OpenClaw** | Orchestration | 🟡 HIGH | ✅ Running (2026.4.24) |
| **DeerFlow** | Workflow Engine | 🟡 HIGH | ⚠️ Status TBD |
| **MCP Servers** | Tool Protocol | 🟠 MEDIUM | ⚠️ Status TBD |

**Search Queries (Per Heartbeat):**

```text
1. "CVE-2026" + ("Ollama" OR "OpenWebUI" OR "vLLM" OR "LMDeploy" OR "AI inference")
2. "AI infrastructure" + vulnerability + 2026
3. "LLM serving" + SSRF OR RCE OR privilege escalation
4. "OpenClaw" + security OR vulnerability
5. "ZeroTier" + vulnerability OR CVE
```

**Sources to Check:**
- NVD (nvd.nist.gov) — Official CVE database
- CVE.org — Authoritative CVE list
- GitHub Security Advisories (GHSA) — Open-source vulnerabilities
- The Hacker News — Exploitation reports
- Cloud Security Alliance AI Safety Initiative — AI-specific research
- Vendor security bulletins (Ollama, OpenWebUI, vLLM)

**Escalation Criteria:**

| Severity | CVSS | Exploitation Status | Action |
|----------|------|---------------------|--------|
| 🔴 CRITICAL | 9.0-10.0 | Active in wild | **IMMEDIATE** — Alert operator, prepare patch plan |
| 🟠 HIGH | 7.0-8.9 | Active in wild | **URGENT** — Alert operator within 1 hour |
| 🟠 HIGH | 7.0-8.9 | POC available | Alert operator within 4 hours |
| 🟡 MEDIUM | 4.0-6.9 | Any | Log to daily memory, review within 24h |
| 🟢 LOW | <4.0 | Any | Log to weekly synthesis |

**Output Format:**

```markdown
### AI Infrastructure CVE Monitor (HH:MM UTC)
| CVE | Component | CVSS | Exploitation | Our Status | AVR Entry | Action |
|-----|-----------|------|--------------|------------|-----------|--------|
| CVE-2026-XXXXX | Ollama | X.X | None/POC/Active | ✅/⚠️/❌ | AVR-2026-001 | Action |

**Excluded CVEs:**
- CVE-2026-33626 (LMDeploy SSRF) — Excluded per operator directive (2026-04-28 09:29 UTC). LMDeploy not deployed.
- CVE-2026-5757 (Ollama RCE) — **Excluded** (2026-05-01 16:07 UTC). Ollama removed. AVR-2026-001 created for historical tracking.

**Actively Monitored (Non-AI Infrastructure):**
- **CVE-2026-41940** (cPanel & WHM Auth Bypass) — 🔴 CRITICAL, CVSS 10.0, active exploitation. National assessment engagement with CSM (7-day scan + 90-day POC). See: `engagements/csm-cve-2026-41940/`

**AVR Integration Status:**
- New entries created: N
- Existing entries updated: N
- Escalations triggered: N

**New Findings:** [Summary of new CVEs since last check]
**Recommended Actions:** [Patch, mitigate, or monitor]
```

**AVR Workflow:**
1. CVE detected → Check if affects deployed technology (TOOLS.md inventory)
2. If yes → Create/update AVR entry (`attack-vector-registry/entries/`)
3. Assess exploitation status + POC availability
4. If CRITICAL (CVSS ≥9.0 + active) → Trigger escalation (Telegram alert)
5. Update CHANGELOG.md with registry changes
6. Log to daily memory file

**Automation Boundary:**
- Monitoring is read-only (no auto-patching)
- CRITICAL/HIGH CVEs with active exploitation trigger operator alert
- MEDIUM/LOW CVEs logged to daily memory for review
- Patching requires explicit operator approval
- All findings logged to `memory/YYYY-MM-DD.md`

**Cadence:** Every heartbeat cycle (4-8 hours standard, 15-30 min during active execution)

**Escalation Integration:**
- Critical vulnerabilities trigger Intelligence Brief creation for DAF (agent-main)
- Monthly AI Threat Landscape Report includes CVE trends

---

## Heartbeat Cadence Summary

| Check Type | Cadence | Priority |
|------------|---------|----------|
| **GitHub Engagement Sync** | Every heartbeat | HIGH |
| **AI Infrastructure CVE Monitor** | Every heartbeat | HIGH |
| **Workstream Review** | Every heartbeat | HIGH |
| **Executive Summary** | Daily (23:00 UTC) | MEDIUM |
| **Strategic Synthesis** | Weekly (Sunday 09:00 UTC) | HIGH |

---