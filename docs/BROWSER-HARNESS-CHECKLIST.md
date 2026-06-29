# Browser-Harness Deployment Checklist

**Use this checklist before each deployment or major task.**

---

## Pre-Installation

- [ ] `uv` package manager installed and working
- [ ] Chrome/Chromium browser available on system
- [ ] Dedicated workspace path selected (not `/tmp`)
- [ ] OpenClaw gateway status verified

---

## Installation

- [ ] Cloned to `~/Developer/browser-harness` (or similar durable path)
- [ ] Ran `uv tool install -e .`
- [ ] Verified with `command -v browser-harness`
- [ ] Ran `browser-harness --doctor` successfully
- [ ] Registered `SKILL.md` with agent environment

---

## Isolation Setup

- [ ] **Browser Profile Method Selected:**
  - [ ] Way 1 (chrome://inspect) - for trusted logged-in sessions
  - [ ] Way 2 (isolated profile) - **RECOMMENDED DEFAULT**
  - [ ] Cloud (remote browser) - for headless/parallel

- [ ] **If Way 2:**
  - [ ] Created dedicated profile directory
  - [ ] Launched Chrome with `--remote-debugging-port=9222`
  - [ ] Set `BU_CDP_URL=http://127.0.0.1:9222`
  - [ ] Verified profile dir is NOT Chrome's default location

- [ ] **If OS Isolation:**
  - [ ] Created dedicated low-privilege user
  - [ ] Set file permissions correctly

---

## Workspace & Version Control

- [ ] Initialized git repo in browser-harness directory
- [ ] Committed initial state
- [ ] Verified `agent-workspace/` is tracked
- [ ] Confirmed `src/browser_harness/` is protected (not editable by agent)

---

## Security Hardening

- [ ] `BH_DOMAIN_SKILLS=0` (default, not enabled)
- [ ] CDP binding verified as localhost only
- [ ] No credentials stored in workspace
- [ ] Approval boundaries documented for this task
- [ ] Network exposure reviewed (no external CDP access)

---

## Task Classification

**What type of task is this?**

- [ ] Public page scraping → ✅ Proceed
- [ ] Dashboard extraction (read-only) → ✅ Proceed
- [ ] Form automation (non-destructive) → ✅ Proceed
- [ ] Browser QA / visual regression → ✅ Proceed
- [ ] Site exploration → ✅ Proceed

**Requires Approval Gate:**

- [ ] Login/authentication needed → 🛑 STOP - Get approval
- [ ] Email sending → 🛑 STOP - Get approval
- [ ] Payments/transactions → 🛑 STOP - Get approval
- [ ] Data exports (PII/sensitive) → 🛑 STOP - Get approval
- [ ] Destructive actions → 🛑 STOP - Get approval
- [ ] Government/customer systems → 🛑 STOP - Get approval

---

## Pre-Flight Tests

- [ ] Connection test passed:
  ```bash
  browser-harness <<'PY'
  print(page_info())
  PY
  ```

- [ ] Navigation test passed:
  ```bash
  browser-harness <<'PY'
  new_tab("https://example.com")
  wait_for_load()
  PY
  ```

- [ ] Screenshot capability verified

---

## During Execution

- [ ] Monitoring daemon logs (`/tmp/bu-*.log`)
- [ ] Tracking URLs visited
- [ ] Reviewing helper file changes (if any)
- [ ] Capturing screenshots for audit
- [ ] Ready to intervene if blocker hit

---

## Post-Execution

- [ ] Task completed or blocker documented
- [ ] Results returned to OpenClaw
- [ ] Browser state cleaned (tabs closed)
- [ ] Remote daemon stopped (if cloud browser used)
- [ ] Helper file diffs reviewed and committed
- [ ] Any sensitive data encountered flagged

---

## Rollback Ready

- [ ] Know how to restart daemon: `browser-harness <<'PY'` → `restart_daemon()`
- [ ] Know how to revert helpers: `git checkout HEAD -- agent-workspace/`
- [ ] Know how to kill all: `pkill -f browser_harness`
- [ ] Profile recreation path documented (if needed)

---

## Sign-Off

**Deployer:** _________________  
**Date:** _________________  
**Task Description:** _________________  
**Approval Required:** Yes / No  
**Approved By (if applicable):** _________________  

---

## Quick Status Commands

```bash
# Check daemon and Chrome status
browser-harness --doctor

# View logs
cat /tmp/bu-default.log  # or /tmp/bu-${BU_NAME}.log

# Check for updates
browser-harness <<'PY'
# Update banner prints once per day if available
PY

# Restart if stale
browser-harness <<'PY'
restart_daemon()
PY
```
