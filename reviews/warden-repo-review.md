# Warden — Structured Analytical & Canonical Overview

**Repository:** `domdoss/Warden` — [github.com/domdoss/Warden](https://github.com/domdoss/Warden)
**Review Date:** 2026-08-15
**Reviewer:** Ember (at request of DAF)

---

## 1. Repository Identity

| Field | Value |
|-------|-------|
| **Name** | Warden |
| **Owner** | `domdoss` (Dominic) |
| **Visibility** | Public |
| **Created** | 2026-07-09 |
| **Last Push** | 2026-08-14 |
| **Default Branch** | `main` |
| **Stars** | 154 |
| **Forks** | 46 |
| **Watchers** | 154 |
| **Subscribers** | 5 |
| **Open Issues** | 0 |
| **Repo Size** | ~10.4 MB |
| **Homepage** | [aionsystems.ca](https://aionsystems.ca) |
| **Topics** | `agent`, `agentic-ai`, `ai`, `llm`, `llm-tools` |
| **Description** | "This is a fork of the https://dockbox.dev project I made" |

**Origin:** Warden is a fork/derivative of the **Dockbox** project (`dockbox.dev`), rebranded and extended by Dominic. The `package.json` still carries `"name": "dockbox"` and `"description": "Personal Claude assistant. Lightweight, secure, customizable."` — confirming the lineage.

---

## 2. License

**Type:** Custom **"Warden Personal-Use License"** (NOASSERTION on SPDX)

- Copyright (c) 2026 Dominic
- **Personal, non-commercial use only** — download, run, modify, study
- **No commercial use** — no selling, licensing, leasing, offering as paid service, or internal business revenue generation
- **Copyleft-style inheritance** — forks and derivatives must carry the same license, no relicensing to more permissive terms, no commercialization of forks
- **No warranty** — standard AS-IS disclaimer

**Assessment [HIGH]:** This is one of the more restrictive "personal use" licenses seen in the AI agent space. It effectively prevents any organizational or commercial deployment. The copyleft-style clause on forks is unusual for non-commercial licenses and closes the "relicense and commercialize" loophole. This is a deliberate choice — the author wants Warden to remain a personal, individual tool.

---

## 3. Language Composition

| Language | Bytes | % (of total) | Role |
|----------|-------|-------------|------|
| **TypeScript** | 1,750,073 | 31.2% | Core server, agent orchestration, channels, tools |
| **JavaScript** | 1,276,997 | 22.8% | Dashboard UI, build scripts, agent-runner |
| **Python** | 856,644 | 15.3% | Eyes/Ears subsystem (vision, voice, STT/TTS) |
| **HTML** | 767,431 | 13.7% | Dashboard panels, hologram UI |
| **CSS** | 243,033 | 4.3% | Dashboard styling |
| **Shell** | 121,307 | 2.2% | Install scripts, deployment |
| **Dart** | 55,050 | 1.0% | (Likely a companion mobile app or Flutter component) |
| **PowerShell** | 7,292 | 0.1% | Windows install support |
| **Inno Setup** | 3,321 | 0.06% | Windows installer |
| **Kotlin** | 127 | <0.01% | (Minimal — possibly a stub or config) |

**Total:** ~5.6 MB of source code across 10 languages.

**Assessment [HIGH]:** TypeScript dominates the core, with Python handling the perceptual subsystem (camera/vision/voice). The JavaScript footprint is significant — the dashboard is a first-class component, not an afterthought. Dart and Inno Setup suggest cross-platform ambitions (mobile companion + Windows installer).

---

## 4. Technology Stack

### Runtime & Build

| Layer | Technology |
|-------|-----------|
| **Runtime** | Node.js ≥ 20 |
| **Language** | TypeScript (strict mode, ES2022, NodeNext modules) |
| **Module System** | ES Modules (`"type": "module"`) |
| **Build** | `tsc` + `tsx` for dev |
| **Package Manager** | npm (with `--ignore-scripts` safety) |
| **Testing** | Vitest |
| **Formatting** | Prettier |
| **Git Hooks** | Husky |
| **Database** | SQLite via `better-sqlite3` (synchronous, embedded) |
| **Browser Automation** | Playwright Core |
| **Terminal Emulation** | `node-pty` (real PTY allocation) |

### Key Dependencies

| Package | Purpose | Significance |
|---------|---------|-------------|
| `@modelcontextprotocol/sdk` | MCP server/client | First-class MCP support — extensible tool ecosystem |
| `@whiskeysockets/baileys` | WhatsApp Web protocol | WhatsApp channel without official API |
| `grammy` | Telegram Bot API | Telegram channel |
| `better-sqlite3` | SQLite driver | All state — conversations, tasks, memory, audit |
| `node-pty` | Pseudo-terminal | Shell command execution with real PTY |
| `playwright-core` | Browser automation | DOM-level browser control (not screenshots) |
| `nodemailer` + `imapflow` | Email send/receive | Full email integration |
| `sharp` | Image processing | Vision pipeline, image handling |
| `zod` | Schema validation | Structured outputs, config validation |
| `ws` | WebSocket | Real-time dashboard communication |
| `cron-parser` | Cron scheduling | Heartbeat, scheduled tasks |
| `http-proxy` | HTTP proxy | Credential proxy layer |
| `yaml` | YAML parsing | Config, driving-forces, skills |
| `yt-search` | YouTube search | Media/tool integration |
| `qrcode` / `qrcode-terminal` | QR codes | WhatsApp pairing, mobile linking |
| `mammoth` | DOCX parsing | Document processing |
| `basic-ftp` | FTP client | File transfer capability |
| `glob` | File globbing | File search |
| `pino` / `pino-pretty` | Structured logging | Production-grade logging |

### Python Subsystem (eyes_ears/)

| Component | Purpose |
|-----------|---------|
| **RF-DETR** | Object detection (real-time, webcam) |
| **InsightFace** | Face recognition |
| **OpenCV** | Computer vision |
| **ONNX Runtime** | Model inference |
| **Supervision** | Detection visualization/annotation |
| **Whisper** | Speech-to-text |
| **TTS** | Text-to-speech |
| **ImageHash** | Perceptual image hashing |

---

## 5. Project Structure

```
Warden/
├── .env.example              # Configuration template
├── .gitignore
├── LICENSE                  # Personal-Use Non-Commercial
├── MANIFEST.txt             # File manifest
├── README.md                # 75 KB — extremely detailed
├── install-deps.sh          # Linux dependency installer
├── install-macos.sh         # macOS dependency installer
├── package.json             # Node project (name: "dockbox")
├── tsconfig.json            # Strict TS, ES2022, NodeNext
│
├── src/                     # Core TypeScript source
│   ├── agent-session-store.ts      # Agent session persistence
│   ├── agent-spawn.ts              # Sub-agent spawning (39 KB — core orchestration)
│   ├── anthropic-translate.ts      # Anthropic API translation layer
│   ├── backup.ts                  # Backup system
│   ├── calendar-sync.ts           # Calendar synchronization
│   ├── capture.ts                 # Screen/camera capture
│   ├── channels/                  # Messaging channel adapters
│   │   ├── index.ts
│   │   ├── registry.ts
│   │   ├── slack.ts               # Slack integration
│   │   ├── telegram.ts            # Telegram integration (16 KB)
│   │   ├── web.ts                 # Web/dashboard channel
│   │   └── whatsapp.ts            # WhatsApp integration (11 KB)
│   ├── config.ts                  # Configuration management
│   ├── container-runtime.ts       # Container/agent runtime
│   ├── context-compressor.ts      # Context window compression
│   ├── credential-proxy.ts        # API key/credential proxy
│   ├── db.ts                      # SQLite database layer (103 KB — largest file)
│   ├── desktop-control.ts         # Mouse/keyboard control
│   ├── desktop-plasma.ts          # KDE Plasma integration
│   ├── digest-notes.ts            # Note digesting
│   ├── email.ts                   # Email send/receive
│   ├── encryption.ts              # Encryption utilities
│   └── ... (more files)
│
├── container/               # Agent runner container
│   └── agent-runner/        # Sandboxed agent execution
│
├── data/                    # Runtime data
│   ├── driving-forces/      # Expert role presets (markdown)
│   └── skills/              # Skill definitions
│
├── docs/                    # Documentation
│
├── eyes_ears/               # Perception subsystem (Python)
│   ├── eyes/                # Vision (RF-DETR, face recognition)
│   ├── ears/                # Voice (STT/TTS/UI)
│   ├── ui/                  # Hologram + panels
│   ├── config/              # Settings
│   └── core/                # Shared Python core
│
├── Notes/                   # Developer notes
└── voice/                   # (Legacy — merged into eyes_ears/)
```

**Key observation:** `db.ts` at 103 KB is the single largest TypeScript file — this is the entire data layer (schema, queries, migrations) in one file. This is a monolithic pattern common in early-stage projects where the schema is still evolving rapidly.

---

## 6. Architecture — The Orchestrator-Specialist Pattern

### 6.1 Core Design Philosophy

Warden's architecture is built on a **counterintuitive premise: the cheapest model supervises the most expensive ones.** A small orchestrator model (runs locally on Ollama, e.g. `gemma4:latest` at 4B params, or a 31B cloud model) handles only routing, classification, and composition — never generation. Frontier models do the expensive work; the small model babysits them.

```
User → Orchestrator (small; e4b local / 31B cloud)
         ↓
    ┌────┴────────────────────────────────────────┐
    │   Atlas      (large, cloud) — execution      │
    │   Vulkan     (large, cloud) — coding         │
    │   Iris       (local rec.)  — email/calendar  │
    │   Dexter     (local rec.)  — scheduling      │
    │   Byte       (local rec.)  — project mgmt    │
    │   Mercury    (local rec.)  — memory/RAG      │
    │   Artemis    (large, cloud) — audit/review    │
    │   Oculus     (local, light) — security        │
    │   The Council (3×, any)    — deliberation      │
    └──────────────────────────────────────────────┘
         ↓
    Orchestrator → User (only voice in chat)
```

### 6.2 The Orchestrator

- **Never touches the internet directly** — no browsing, no search, no URL fetching
- **Never prescribes HOW** — only WHAT (no URLs, no search queries, no step-by-step)
- **Rewrites user messages** into clean, self-contained briefs for specialists
- **Supervises on a 30-second tick** — checks each running job's status, kills drifters, re-briefs failures
- **Silent supervision** — progress lives in the dashboard, not chat bubbles
- **Drains an inbox** at end of each turn — digests results, chains follow-ups
- **Auto-retries failed tasks** — re-delegates with corrected briefs; only surfaces to user after 2 same-cause failures

### 6.3 Sub-Agents

| Agent | Model | Tools | Role |
|-------|-------|-------|------|
| **Atlas** | Large, cloud | Shell, browser (DOM), desktop, files, web search/fetch, documents | General execution — internet + commands |
| **Vulkan** | Large, cloud | Read, Edit, Grep, Glob, Bash, build & test | Coding, scripting, refactoring, builds |
| **Iris** | Local recommended | Email, calendar, contacts, todos | Personal information management |
| **Dexter** | Local recommended | Calendar CRUD + scheduled tasks (cron/interval/once) | Scheduling — never executes scheduled tasks |
| **Byte** | Local recommended | Projects, deliverables, blockers, time tracking | Work management |
| **Mercury** | Local recommended | Memory summarization + RAG injection | Distills conversations into context window |
| **Artemis** | Large, cloud | Read-only file access | Critical review / audit |
| **Oculus** | Local, vision-optional | awareness_log, security_log, webcam_capture, arm/disarm | Security + situational awareness via webcam |
| **The Council** | 3×, any | Read-only file access | Three seats: **Skeptic**, **Pragmatist**, **Synthesist** — deliberate in parallel on high-stakes decisions |

### 6.4 Key Design Principles

1. **One conversation, one voice** — user only talks to the orchestrator; specialists are invisible
2. **Brief composition, not micromanagement** — orchestrator can't see specialist tools, so it can't prescribe execution steps
3. **Async delegation with supervision** — jobs run in background, orchestrator stays free for next message
4. **Inbox-based result routing** — finished jobs drop output in an inbox; orchestrator drains and digests
5. **Context isolation** — each sub-agent gets a self-contained brief, no shared context
6. **Model right-sizing** — orchestrator is smallest (routing only); generation lives in specialists

---

## 7. Feature Analysis

### 7.1 Communication Channels

| Channel | Library | Status |
|---------|---------|--------|
| **Telegram** | grammy | Full integration (16 KB module) |
| **WhatsApp** | baileys (WhatsApp Web protocol) | Full integration (11 KB) |
| **Slack** | Slack Bot API | Full integration (7 KB) |
| **Web/Dashboard** | WebSocket + HTTP | Built-in dashboard on port 3200 |

### 7.2 Desktop Control

- **Mouse/keyboard** — full control via `desktop-control.ts`
- **KDE Plasma** — specific integration via `desktop-plasma.ts`
- **Browser** — Playwright DOM-level control (not screenshots — actual element manipulation with real logged-in sessions)
- **Terminal** — `node-pty` for real PTY allocation; shell commands execute as the user

### 7.3 Email & Calendar

- **Email** — full IMAP receive + SMTP send via `imapflow` + `nodemailer`
- **Calendar** — calendar synchronization via `calendar-sync.ts`
- **Scheduling** — Dexter handles calendar CRUD + scheduled tasks (cron, interval, one-shot)
- **Contacts** — managed by Iris

### 7.4 Memory System

- **MEMORY.md** — orchestrator writes directly; loaded into context every turn
- **JOURNAL.md** — auto-distilled conversation summaries (fire-and-forget writeback)
- **MERCURY_MEMORY.md** — Mercury agent's RAG-injected memory
- **HEARTBEAT.md** — standing instructions for autonomous behavior on schedule
- **TODO.md** — task tracking
- **Auto-writeback** — after every conversation, a local model reads last ~30 messages, distills durable facts, appends to MEMORY.md + JOURNAL.md
- **Auto-compaction** — MEMORY.md is compacted when it grows too large
- **Throttled** — fire-and-forget, max once per chat per 15 minutes

### 7.5 Security & Awareness

- **Oculus agent** — background security via webcam + structured AWARENESS events
- **RF-DETR** — real-time object detection
- **InsightFace** — face recognition
- **Arming/disarming** — Oculus owns security state
- **Security log** — persistent audit trail
- **Alert system** — captioned frames + red alert UI for security events
- **Eyes/Ears merged subsystem** — vision + voice combined into one venv, one config, one run script

### 7.6 Intelligence Augmentation

- **258 Fabric expert prompt patterns** — keyword-extracted top 5 injected per turn
- **Driving Forces** — expert role presets (e.g. `paranoid-reviewer`, `staff-engineer`) as markdown files in `data/driving-forces/`
- **The Council** — 3-seat parallel deliberation (Skeptic, Pragmatist, Synthesist) for high-stakes decisions
- **Tool relevance ranking** — not all 30+ tools go into every prompt; keyword-ranked, core routing tools always included
- **MCP support** — `@modelcontextprotocol/sdk` for external tool servers
- **Skills system** — extensible skill files in `data/skills/`

### 7.7 Tool Loop Safety

| Circuit Breaker | Function |
|-----------------|----------|
| Intent-without-action detection | Nudges model after saying "I'll do X" without calling tools (max 2) |
| Circling detection | Forces a no-tools round after consecutive useless loops |
| Degenerate output filter | Detects and suppresses word-mash/garbled output |
| Verifier sub-agent | Post-execution verification of file writes/edits |

### 7.8 Dashboard

- **Port 3200** by default
- WebSocket-based real-time updates
- Live Activity panel (grouped, collapsible) — streaming job status
- Memory/Heartbeat/Driving Forces editors
- Model configuration per agent
- No auth gate — single-user, loads directly

### 7.9 Configuration Model

```env
ASSISTANT_NAME=Mirific         # Default assistant name
ADMIN_PASSWORD=mirific         # Dashboard password
DEFAULT_MODEL_MODE=            # "" | "local" | "hybrid"
OLLAMA_CHAT_MODEL=llama3.2:latest  # Local chat model
LOCAL_ASSISTANT_NAME=Kimi      # Bot name in local mode
MAX_CONCURRENT_CONTAINERS=8    # Parallel agent limit
IDLE_TIMEOUT=1800000           # 30 min container idle
```

---

## 8. Commit History & Development Activity

### Timeline

| Date | Activity |
|------|----------|
| **2026-07-09** | Repository created |
| **2026-08-14** | Latest commit (merge security + voice into eyes_ears, UI-only mode) |

**Active development period:** ~5 weeks
**Commit cadence:** Multiple commits per day (based on visible samples)
**Sole author:** Dominic (`dominic@dockbox.dev`)

### Recent Commit Themes

1. **Architectural merge** — combining `security/` and `voice/` into unified `eyes_ears/` directory
2. **Install robustness** — `--ignore-scripts` to prevent partial installs, native addon rebuilds
3. **Documentation** — removing fictional login page from README, correcting dashboard description
4. **Naming consistency** — Sentry → Oculus rename across codebase, DockboxClient → WardenClient
5. **Path normalization** — `/home/dominic/Projects/Warden` → `/opt/warden` for deploy host

**Assessment [MEDIUM]:** This is a solo project in active, rapid development. The commit messages are detailed and follow conventional commits format (`feat:`, `fix:`, `docs:`). The author is clearly experienced — the install fixes show production-deployment awareness. The Sentry→Oculus rename and the eyes_ears merge indicate the architecture is still evolving significantly at week 5.

---

## 9. Security Posture

### Risk Model

The README opens with one of the most candid security warnings in any AI agent project:

> *"Warden is an AI agent with the same access as your user account. It executes shell commands, moves your mouse and types on your keyboard, drives your real browser with your real logged-in sessions and saved passwords, reads and sends your email, and can edit and restart its own source code. There is no sandbox and no container."*

**There is no sandbox. There is no container. The agent IS the user.**

### Attack Surfaces

| Surface | Risk |
|---------|------|
| Shell execution | Full user-level command execution via `node-pty` |
| Browser control | Real logged-in sessions, saved passwords, DOM manipulation |
| Email | Read + send as the user |
| Desktop | Mouse, keyboard, screen capture |
| Webcam | Oculus has webcam capture capability |
| Self-modification | Can edit and restart its own source code |
| Prompt injection | Agent visits web pages and reads emails — both are injection vectors |

### Mitigations Present

- **Credential proxy** — API keys proxied, not directly exposed to agents
- **Encryption module** — exists (`encryption.ts`)
- **Oculus security agent** — monitors via webcam, logs security events
- **Artemis audit agent** — read-only critical review of conversations/decisions
- **The Council** — three-seat deliberation for high-stakes decisions
- **Tool relevance gating** — not all tools exposed in every turn
- **Verifier sub-agent** — post-execution verification
- **Circuit breakers** — loop detection prevents runaway actions

### Mitigations Absent

- No sandboxing or containerization
- No rate limiting on shell commands
- No file-system path restrictions
- No network egress filtering
- No human-in-the-loop approval for destructive actions
- No audit trail of shell commands executed (beyond logging)

**Assessment [HIGH]:** Warden's security model is "trust the LLM + supervise with another LLM." This is a philosophical choice, not an oversight — the author explicitly states they run it on their own laptop and desktop "rawdogging the system." The mitigations are all *internal* (agent supervising agent), none are *external* (OS-level containment). This is the opposite of projects like OpenClaw which operate within a sandboxed gateway. For a personal-use tool controlled by a technically sophisticated user who accepts the risk, this is a defensible position. For any other context, it's dangerous.

---

## 10. Architecture Assessment

### Strengths

1. **Orchestrator-specialist separation is genuinely novel.** Most agent frameworks use one model for everything or hardcode routing. Warden's "small model supervises frontier model" pattern, with the orchestrator physically unable to see specialist tools (preventing micromanagement), is an elegant constraint-based design.

2. **Async supervision loop is well-engineered.** The 30-second tick, silent progress, inbox-based result routing, and automatic failure recovery with re-briefing create a robust autonomous execution model. The "fail twice same way → escalate to user" rule prevents infinite retry loops.

3. **Model right-sizing is pragmatic.** Local models for routine tasks (Iris, Dexter, Byte, Mercury, Oculus), cloud models for heavy generation (Atlas, Vulkan, Artemis). The orchestrator is deliberately the cheapest model. This keeps per-turn costs near zero for routing while reserving cloud spend for actual generation.

4. **Channel abstraction is clean.** Four channels (Telegram, WhatsApp, Slack, Web) with a registry pattern — adding new channels is straightforward.

5. **MCP integration future-proofs the tool surface.** External tools can be added as MCP servers without touching core code.

6. **Memory system is sophisticated.** Auto-writeback with local model distillation, fire-and-forget throttling, auto-compaction, and the separation of MEMORY.md (loaded context) vs JOURNAL.md (append-only log) vs MERCURY_MEMORY.md (RAG) is a well-thought-out tiered memory architecture.

7. **The Council pattern is interesting.** Three independent seats with different biases (Skeptic, Pragmatist, Synthesist) running in parallel on high-stakes decisions is a lightweight form of ensemble reasoning.

### Weaknesses & Risks

1. **`db.ts` at 103 KB is a monolith.** This single file contains the entire data layer. It should be split into schema, migrations, queries, and repository modules. This will become a maintenance bottleneck.

2. **No tests visible in the repository.** Vitest is configured as a dev dependency, and a `test` script exists, but no test files were found in the visible directory listing. For a system with this level of autonomy (shell execution, email sending, browser control), the absence of automated tests is a significant risk.

3. **No sandbox = no second chance.** A single prompt injection from a visited web page or read email can compromise the entire system. The mitigations are all agent-level (LLM supervising LLM), none are OS-level. If the supervising LLM fails (and the README acknowledges e4b orchestrators can be fooled by non-results), there is no backstop.

4. **Single maintainer.** All commits are from Dominic. Bus factor = 1. The personal-use license further limits community contribution potential.

5. **README is 75 KB.** This is extraordinarily large — essentially a manual. While thorough, it suggests the project's complexity exceeds what can be documented concisely. A 75 KB README is also a maintenance burden.

6. **Package name mismatch.** `package.json` still says `"name": "dockbox"` — the rename to Warden is incomplete in the codebase. This can cause confusion in npm tooling and logs.

7. **No CI/CD.** No GitHub Actions workflows were visible. All builds and tests are manual.

8. **No release tags.** The repository has no tagged releases — only `main` branch commits. Versioning is implicit (`1.2.14` in package.json).

---

## 11. Comparative Positioning

| Dimension | Warden | OpenClaw | Open Interpreter | SWE-Agent |
|-----------|--------|----------|-----------------|----------|
| **Execution model** | Direct user-level (no sandbox) | Sandboxed gateway | Direct (local) | Docker container |
| **Orchestration** | Small model supervises large | Gateway-mediated | Single model | Single model |
| **Channels** | Telegram, WhatsApp, Slack, Web | Telegram, Discord, Signal, Web | CLI | API/CLI |
| **Memory** | Auto-distill + RAG + files | Memory files + wiki + search | None (stateless) | Repo context |
| **MCP support** | Yes | Yes | No | No |
| **Browser** | Playwright (DOM) | Browser tool | Playwright | None |
| **Desktop control** | Yes (mouse/keyboard) | No | Yes | No |
| **Email** | Full IMAP/SMTP | Configurable | No | No |
| **Vision** | RF-DETR + face recognition | No | No | No |
| **Voice** | Whisper STT/TTS | Configurable | No | No |
| **License** | Personal non-commercial | MIT | MIT | MIT |
| **Multi-agent** | Yes (9 specialists + Council) | Yes (sub-agents) | No | No |

**Assessment [MEDIUM]:** Warden occupies a unique niche — it's the most *integrated* personal AI agent in this comparison (desktop control + email + vision + voice + browser + multi-agent), but also the most *risky* (no sandbox, personal-use license, single maintainer). It trades safety for capability. OpenClaw trades capability for safety. For a technically sophisticated individual who wants maximum integration and accepts the risk, Warden is more powerful. For any institutional or team context, OpenClaw's sandboxed model is more appropriate.

---

## 12. Canonical Summary

**Warden is a personal AI assistant that runs on your desktop with the same access as your user account — no sandbox, no container, no apologies.** It is a fork of the Dockbox project, rebranded and extended by Dominic (domdoss), with a custom non-commercial personal-use license.

**Architecture:** An orchestrator-specialist pattern where a small local model (Ollama, e4b–31B) routes and supervises nine specialist sub-agents running on larger cloud models. The orchestrator never touches the internet directly — it only classifies intent, composes briefs, and babysits execution. Specialists handle execution (Atlas), coding (Vulkan), email/calendar (Iris), scheduling (Dexter), project management (Byte), memory (Mercury), audit (Artemis), security (Oculus), and high-stakes deliberation (The Council).

**Capabilities:** Shell commands, browser DOM control, mouse/keyboard, email read/send, calendar, webcam-based security with face recognition, voice STT/TTS, self-editing source code, MCP tool servers, 258 Fabric expert patterns, driving-force role presets, multi-channel messaging (Telegram, WhatsApp, Slack, Web dashboard), tiered auto-distilling memory, scheduled autonomous behavior via heartbeat.

**Maturity:** 5 weeks old, solo-developed, active daily commits, no releases, no tests, no CI/CD. The 75 KB README is effectively the manual. Architecture is still evolving (security/voice merge, agent renames).

**Risk profile:** Maximum capability, minimum containment. A model mistake, prompt injection, or degenerate loop has full user-level access. All mitigations are agent-internal (LLM supervising LLM); none are OS-level. The author acknowledges this and runs it on personal machines.

**Bottom line:** Warden is an ambitious, well-architected, genuinely innovative personal AI agent project that is also genuinely dangerous to run. It is the most integrated desktop AI agent stack I've seen. The orchestrator-specialist pattern is a real contribution to agent design. The non-commercial license and no-sandbox model limit it to personal use by technically sophisticated individuals. For research, it's a fascinating reference architecture. For production deployment, it needs a sandbox layer, automated tests, CI/CD, and a release management process.
