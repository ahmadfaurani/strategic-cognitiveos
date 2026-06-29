# Browser-Harness Controlled Deployment Runbook

**Classification:** High-Autonomy Subagent  
**Status:** Ready for Deployment  
**Last Updated:** 2026-06-14

---

## Executive Summary

Browser-Harness is a self-extending browser agent runtime that connects directly to Chrome via CDP. Unlike OpenClaw's browser tool (gateway-mediated, policy-enforced), Browser-Harness gives the agent direct browser control with persistent learning capabilities.

**Deploy as:** Isolated subagent for browser-only workflows  
**Do not deploy as:** Replacement for OpenClaw browser tool

---

## 1. Installation

### 1.1 Prerequisites

- `uv` package manager installed
- Chrome or Chromium browser available
- Dedicated workspace directory (not `/tmp`)

### 1.2 Install Steps

```bash
# 1. Clone to durable location
git clone https://github.com/browser-use/browser-harness ~/Developer/browser-harness
cd ~/Developer/browser-harness

# 2. Editable install (global command, local checkout)
uv tool install -e .

# 3. Verify installation
command -v browser-harness
browser-harness --doctor
```

### 1.3 Register Skill with Agent

**Claude Code:**
```bash
# Add to ~/.claude/CLAUDE.md:
@~/Developer/browser-harness/SKILL.md
```

**Codex:**
```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills/browser-harness"
ln -sf ~/Developer/browser-harness/SKILL.md \
       "${CODEX_HOME:-$HOME/.codex}/skills/browser-harness/SKILL.md"
```

---

## 2. Isolation Strategy

### 2.1 Browser Profiles

| Method | Profile Type | Use Case |
|--------|-------------|----------|
| **Way 1** | User's real Chrome | Logged-in sessions you trust agent with |
| **Way 2** | Isolated profile | Automation, scraping, no popup interruptions |
| **Cloud** | Remote browser | Headless servers, parallel sub-agents |

### 2.2 Way 2: Isolated Profile Setup (Recommended Default)

```bash
# Create dedicated automation profile directory
mkdir -p ~/.chrome-automation-profile

# Launch Chrome with remote debugging (no popup interruptions)
google-chrome \
  --remote-debugging-port=9222 \
  --user-data-dir=~/.chrome-automation-profile

# Set environment variable for harness
export BU_CDP_URL=http://127.0.0.1:9222
```

**Critical:** The `--user-data-dir` must NOT be Chrome's default profile location:
- ❌ `~/.config/google-chrome` (Linux default - silently ignored)
- ❌ `~/Library/Application Support/Google/Chrome` (macOS default)
- ❌ `%LOCALAPPDATA%\Google\Chrome\User Data` (Windows default)

### 2.3 OS-Level Isolation

```bash
# Create dedicated low-privilege user (optional, high-security)
sudo useradd -r -s /bin/false browser-agent
sudo chown -R browser-agent:browser-agent /path/to/browser-harness

# Run harness under separate user
sudo -u browser-agent browser-harness <<'PY'
# agent code here
PY
```

---

## 3. Port & Network Configuration

### 3.1 Default Ports

| Component | Port | Binding | Notes |
|-----------|------|---------|-------|
| CDP (Way 2) | 9222 | localhost | Configurable via `--remote-debugging-port` |
| Daemon IPC | Unix socket | `/tmp/bu-<NAME>.sock` | Namespaced by `BU_NAME` |
| Cloud API | HTTPS | browser-use.com | Requires `BROWSER_USE_API_KEY` |

### 3.2 Environment Variables

```bash
# Local browser connection
export BU_CDP_URL=http://127.0.0.1:9222

# Namespace daemon (for parallel sub-agents)
export BU_NAME=work

# Remote browser (cloud)
export BROWSER_USE_API_KEY=your-key-here
export BU_CDP_WS=wss://...  # Set by start_remote_daemon()

# Domain skills (opt-in)
export BH_DOMAIN_SKILLS=0  # Default OFF until reviewed
```

### 3.3 Network Security

- **Default:** CDP binds to localhost only
- **Never:** Expose CDP port to external network without authentication
- **Cloud:** Use Browser Use Cloud proxy for remote browsers (handles auth)

---

## 4. Workspace Structure

```
~/Developer/browser-harness/
├── SKILL.md                    # Agent instructions (register with agent)
├── install.md                  # Setup guide
├── agent-workspace/
│   ├── agent_helpers.py        # Task-specific helpers (agent edits)
│   └── domain-skills/          # Site-specific playbooks (opt-in)
│       ├── github/
│       ├── linkedin/
│       └── amazon/
└── src/browser_harness/        # Core package (protected)
```

### 4.1 Version Control

```bash
# Initialize repo for audit trail
cd ~/Developer/browser-harness
git init

# Track helper changes
git add agent-workspace/
git commit -m "Initial browser-harness deployment"

# Review before merging skill contributions
git diff agent-workspace/agent_helpers.py
```

### 4.2 What Agent Can Modify

| Path | Modifiable | Review Required |
|------|------------|-----------------|
| `agent-workspace/agent_helpers.py` | ✅ Yes | Before production use |
| `agent-workspace/domain-skills/` | ✅ Yes (if enabled) | Before enabling |
| `src/browser_harness/` | ❌ No | N/A |

---

## 5. Approval Boundaries

### 5.1 Allowed Without Approval

| Task Type | Examples |
|-----------|----------|
| Public page scraping | Documentation, blogs, public APIs |
| Dashboard extraction | Metrics, status pages (read-only) |
| Form automation | Search forms, filters, non-destructive |
| Browser QA | Visual regression, layout checks |
| Site exploration | Mapping structure, finding endpoints |

### 5.2 Require OpenClaw + Human Approval

| Task Type | Reason |
|-----------|--------|
| Login/authentication | Credential exposure risk |
| Email sending | External communication |
| Payments/transactions | Financial risk |
| Data exports | PII/sensitive data handling |
| Destructive actions | Delete, modify, publish |
| Government/customer systems | Compliance requirements |

### 5.3 Approval Gate Pattern

```python
# In agent code - detect sensitive operations
if action_requires_approval():
    # Return to OpenClaw for human decision
    return "APPROVAL_REQUIRED: {reason}"
    
# OpenClaw routes to human for approval
# On approval, agent continues with documented action
```

---

## 6. Rollback Procedures

### 6.1 Daemon Issues

```bash
# Check status
browser-harness --doctor

# Restart daemon
browser-harness <<'PY'
restart_daemon()
PY

# Nuclear option: kill all and restart
pkill -f browser_harness
pkill -f "chrome.*remote-debugging"
rm -f /tmp/bu-*.sock /tmp/bu-*.pid
```

### 6.2 Helper Code Rollback

```bash
# View changes
git diff agent-workspace/agent_helpers.py

# Revert to last known good
git checkout HEAD -- agent-workspace/agent_helpers.py

# Or reset to clean state
git clean -fd agent-workspace/
```

### 6.3 Profile Corruption

```bash
# Way 2: Delete and recreate profile
rm -rf ~/.chrome-automation-profile
mkdir -p ~/.chrome-automation-profile
# Relaunch Chrome with fresh profile

# Cloud: Stop and recreate browser
browser-harness <<'PY'
# Cloud browser auto-stops on daemon shutdown
PY
```

---

## 7. OpenClaw Delegation Rules

### 7.1 Tiered Architecture

```
┌─────────────────────────────────────────┐
│         User / OpenClaw Gateway         │
└─────────────────┬───────────────────────┘
                  │
         ┌────────▼────────┐
         │  Decision Point │
         └────────┬────────┘
                  │
    ┌─────────────┼─────────────┐
    │             │             │
    ▼             ▼             ▼
┌────────┐  ┌──────────┐  ┌──────────┐
│ Tier 1 │  │  Tier 2  │  │  Tier 3  │
│General │  │ Browser- │  │Sensitive │
│Tools   │  │ Only     │  │Actions   │
└────────┘  └──────────┘  └──────────┘
    │             │             │
    ▼             ▼             ▼
OpenClaw     Browser-      OpenClaw +
Native       Harness       Approval
Tools        Subagent      or Manual
```

### 7.2 Delegation Decision Matrix

| Criteria | OpenClaw | Browser-Harness |
|----------|----------|-----------------|
| Multi-tool workflow | ✅ | ❌ |
| Approval gates needed | ✅ | ❌ |
| Browser-only task | ❌ | ✅ |
| Persistent learning | ❌ | ✅ |
| Repetitive scraping | ❌ | ✅ |
| Authenticated session | ⚠️ Case-by-case | ⚠️ Case-by-case |
| Audit trail required | ✅ | ⚠️ Manual setup |

### 7.3 Spawn Pattern

```bash
# From OpenClaw, delegate browser-heavy work
openclaw sessions_spawn \
  --task="Use browser-harness to scrape X, Y, Z" \
  --runtime=subagent \
  --label="browser-scraper" \
  --mode=run
```

### 7.4 Return Protocol

Browser-Harness subagent should:
1. Complete task or hit blocker
2. Return structured result to OpenClaw
3. Flag any sensitive data encountered
4. Clean up browser state (close tabs, stop daemon if remote)

---

## 8. Monitoring & Logging

### 8.1 What to Log

```bash
# Capture to audit log
- Commands executed
- URLs visited
- Helper file diffs
- Screenshots taken
- Errors encountered
- Approval requests
```

### 8.2 Daemon Logs

```bash
# Log location (default namespace)
cat /tmp/bu-default.log

# Custom namespace
cat /tmp/bu-${BU_NAME}.log
```

### 8.3 Health Checks

```bash
# Daily check
browser-harness --doctor

# Check for updates (printed once/day)
# When banner appears: [browser-harness] update available: X -> Y
browser-harness --update -y
```

---

## 9. Quick Reference

### 9.1 Common Commands

```bash
# Test connection
browser-harness <<'PY'
print(page_info())
PY

# Screenshot current page
browser-harness <<'PY'
capture_screenshot()
PY

# Navigate safely (new tab, don't clobber user's work)
browser-harness <<'PY'
new_tab("https://example.com")
wait_for_load()
PY

# Check for stale tabs
browser-harness <<'PY'
ensure_real_tab()
PY
```

### 9.2 Troubleshooting

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| `chrome FAIL` | No Chrome running | Launch Chrome (Way 1 or 2) |
| `daemon FAIL` | Remote debugging not enabled | Tick checkbox or use Way 2 |
| Popup appears | Chrome 144+ first attach | Click Allow |
| Stale refs | Tab closed/navigated | `ensure_real_tab()` |
| Update banner | New version available | `browser-harness --update -y` |

---

## 10. Compliance Checklist

Before deploying Browser-Harness:

- [ ] Dedicated Chrome profile created (not user's daily driver)
- [ ] Workspace under version control
- [ ] `BH_DOMAIN_SKILLS=0` (default)
- [ ] Approval boundaries documented
- [ ] Rollback procedure tested
- [ ] Logging enabled
- [ ] Network binding verified (localhost only)
- [ ] No secrets in helper files
- [ ] OpenClaw delegation rules understood

---

## Appendix A: Security Warnings

From OpenClaw security documentation:

> **Browser-control exposure** is a common footgun. Agents with direct browser access can:
> - Exfiltrate session cookies
> - Access logged-in services
> - Perform actions on behalf of user
> - Navigate to malicious sites
>
> **Mitigation:** Use isolated profiles, audit helper code, enforce approval gates for sensitive operations.

---

## Appendix B: Related Documents

- `install.md` - Full installation guide
- `SKILL.md` - Day-to-day usage patterns
- `interaction-skills/` - UI mechanics helpers
- OpenClaw `browser-automation` skill - For comparison
