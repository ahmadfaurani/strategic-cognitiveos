# Harness Engineering Research Synthesis: 25 Sources → Unified Findings

**Date:** 2026-07-21  
**Author:** Ember  
**Commissioned by:** DAF  
**Sources:** 25 (10 from original report + 15 from batch research)  
**Method:** Sequential prompting — 3 research batches (parallel sub-agents) + disk-based synthesis  

---

## 1. Source Inventory

| # | Source | Type | Key Contribution |
|---|--------|------|-----------------|
| 1 | Lopopolo — Repository Review Playbook | Playbook | Central diagnostic question + 5 warning signs |
| 2 | Lopopolo — Domain Modeling | Thesis | One authoritative owner per concept; repo teaches by structure |
| 3 | Lopopolo — Whole Job | Thesis | Sparse delegation tests environment recoverability |
| 4 | Lopopolo — Just-in-Time Context | Thesis | Route the right slice to the right agent at the right time |
| 5 | Lopopolo — Tool Legibility | Thesis | Discover→select→invoke→interpret→verify→repair cycle |
| 6 | Lopopolo — Authority | Thesis | Broad envelope for reversible, narrow for irreversible |
| 7 | Lopopolo — Proof | Thesis | Claim-matched evidence; verification belongs in the job |
| 8 | Lopopolo — Feedback | Thesis | Failed trajectories → durable infrastructure |
| 9 | OpenAI — Harness Engineering essay | Essay | Million-line product, 0 manual lines, AGENTS.md as TOC |
| 10 | agents.md convention | Standard | 60k+ repos; standardized agent entry point |
| 11 | LangGraph | Framework | Typed channels, checkpoints, HITL as first-class |
| 12 | LangChain Products taxonomy | Docs | Framework vs Runtime vs Harness distinction |
| 13 | AGENTS.md convention (detailed) | Standard | Progressive disclosure, standardized fields |
| 14 | OpenAI Codex PLANS.md | Pattern | Planning as artifact, not mental exercise |
| 15 | ghuntley.com — Everything-as-a-Loop | Philosophy | Loop as primary execution unit; forward/reverse modes |
| 16 | Anthropic — Building Effective Agents | Guide | 5 workflow patterns; ACI design; simplicity principle |
| 17 | SWE-agent — ACI Research | Paper | Agent-Computer Interface as distinct discipline; minimalism works |
| 18 | OpenHands — Autonomous Agent Platform | Repo | Multi-backend, ACP protocol, automation server |
| 19 | Aider — Repo Map Architecture | Tool | Graph-ranked context selection; git-integrated workflow |
| 20 | AutoGen — Multi-Agent Framework | Framework | Event-driven core; tiered abstraction (Studio→AgentChat→Core) |
| 21 | ReAct paper | Paper | Thought→Act→Observe loop; grounding reduces hallucination |
| 22 | MetaGPT | Framework | SOPs as agent contracts; role-based structured outputs |
| 23 | CrewAI | Framework | Flows (state/control) + Crews (execution) two-layer model |
| 24 | Cursor — Cloud Agents & Swarms | Blog | Environment fidelity; Temporal durable execution; tree-based swarm decomposition |
| 25 | Cognition Devin | Product | Long-horizon planning; sandboxed shell+editor+browser; human collaboration |

---

## 2. Thematic Synthesis

### Theme A: Architecture Taxonomy — What Are We Building?

**Sources:** 12 (LangChain taxonomy), 16 (Anthropic), 11 (LangGraph), 20 (AutoGen), 23 (CrewAI)

The research reveals a clear three-tier distinction that our harness design must respect:

- **Framework** (LangChain, CrewAI, AutoGen, MetaGPT) — provides abstractions: agent loops, tool calling, memory primitives. High-level, easy to start, standardizing.
- **Runtime** (LangGraph, Temporal, Inngest) — provides durable execution: streaming, persistence, HITL interrupts, checkpointing. Low-level, production infrastructure.
- **Harness** (Deep Agents SDK, Claude Agent SDK, Manus, OpenClaw) — opinionated, batteries-included: predefined tools, prompts, subagent patterns, file system access, token management, planning.

**What we're building:** A harness. Not a framework — we don't need to provide general-purpose agent abstractions. Not a runtime — we don't need to build durable execution from scratch. We need an opinionated layer that provides the right tools, the right context, the right prompts, and the right feedback loops for agents to work autonomously in this workspace.

**Key insight from Anthropic (Source 16):** "Find the simplest solution possible, and only increase complexity when needed." The harness should start minimal and grow only when complexity is demonstrably justified.

**Key insight from SWE-agent (Source 17):** Mini-SWE-agent matches full SWE-agent performance in ~100 lines. The ACI concepts matter more than framework complexity. Harness complexity should be measured against functional outcomes, not feature count.

---

### Theme B: The Agent-Computer Interface (ACI) — Tools as First-Class Design

**Sources:** 5 (Lopopolo tool-legibility), 16 (Anthropic ACI), 17 (SWE-agent ACI), 18 (OpenHands ACP), 19 (Aider repo map)

The ACI is a distinct discipline from human UI design. Multiple sources converge on this:

- **Lopopolo (Source 5):** Tools must pass a 6-gate cycle: discover→select→invoke→interpret→verify→repair. If any gate requires a human, the tool doesn't exist for the agent.
- **Anthropic (Source 16):** "Carefully craft your agent-computer interface (ACI) through thorough tool documentation and testing." Tool definitions need as much attention as prompts. Poka-yoke tools — make mistakes harder to make.
- **SWE-agent (Source 17):** LM agents are a new category of end users with their own needs. Interface design directly impacts performance. Mini-SWE-agent's 100-line implementation outperforms complex frameworks — the ACI is what matters.
- **Aider (Source 19):** Graph-ranked repo map provides token-budgeted codebase context. Dynamic sizing based on task state — expand when broad understanding needed, contract when specific files in focus.
- **OpenHands (Source 18):** ACP (Agent-Client Protocol) enables agent interoperability — tools should be protocol-defined, not implementation-locked.

**Harness design implication:** The harness must design tool interfaces for LM consumption, not human consumption. Each tool needs: clear documentation, example usage, edge case handling, error messages that enable repair, and a defined scope that distinguishes it from other tools. The 6-gate cycle is the acceptance criteria.

---

### Theme C: Context Management — Just-in-Time, Not All-at-Once

**Sources:** 4 (Lopopolo JIT context), 9 (OpenAI AGENTS.md as TOC), 14 (Codex PLANS.md), 19 (Aider repo map), 24 (Cursor cloud agents), 12 (Deep Agents virtual filesystem)

Context is the scarcest resource. Every source that addresses it says the same thing: don't dump everything in, route the right slice at the right time.

- **Lopopolo (Source 4):** "Durable knowledge is larger than the working set. The harness routes the right slice to the right agent at the right time."
- **OpenAI (Source 9):** AGENTS.md as encyclopedia fails. AGENTS.md as TOC (~100 lines) + structured docs/ works. Context is a scarce resource — giant instruction files crowd out the task.
- **Aider (Source 19):** Graph-ranked repo map with dynamic token budget. Selects most relevant symbols to fit within active budget.
- **Cursor (Source 24):** Environment fidelity matters — missing deps silently degrade output quality. The agent doesn't crash, it just gets worse.
- **Deep Agents (Source 12):** Virtual filesystem with pluggable backends, declarative permissions, context offloading to disk. Disk as infinite context sink.

**Harness design implication:** The harness must implement progressive disclosure: AGENTS.md → docs/ → specific files. Context budget should be explicit and managed. Disk is the infinite context sink — write intermediate findings, plans, and state to disk rather than holding in context window. This is exactly what the sequential prompting approach demonstrates.

---

### Theme D: State and Planning — Artifacts Over Mental Notes

**Sources:** 11 (LangGraph typed channels), 14 (Codex PLANS.md), 23 (CrewAI Flows), 15 (ghuntley loops), 24 (Cursor Temporal)

State management is not implicit — it's explicit, typed, and persisted.

- **LangGraph (Source 11):** Typed channels define what state flows between agents. Checkpoints enable rollback. State is the core of orchestration.
- **Codex PLANS.md (Source 14):** Planning as a first-class artifact. Created at task start, updated during execution, consulted for recovery. The plan IS the harness — reusable across sessions.
- **CrewAI (Source 23):** Flows manage state and control; Crews do the work. State is a first-class managed resource, not implicit context that drifts.
- **Cursor (Source 24):** Decouple agent loop, machine state, and conversation state. Agent loop lives in Temporal (not the VM). Append-only streaming layer handles retries.
- **ghuntley (Source 15):** Loops have entry conditions, exit conditions, feedback signals. The loop IS the harness.

**Harness design implication:** The harness needs three state artifacts:
1. **PLANS.md** — task-level state (what's done, pending, blocked)
2. **Typed state channels** — session-level state (what context is active, what tools are available)
3. **Loop state** — execution-level state (entry/exit conditions, feedback signals)

All three must be disk-persisted and recoverable after compaction or session restart.

---

### Theme E: Execution Models — Loops, Workflows, and Swarms

**Sources:** 15 (ghuntley loops), 16 (Anthropic workflows), 21 (ReAct), 22 (MetaGPT SOPs), 24 (Cursor swarms), 20 (AutoGen event-driven)

The execution model is not one pattern — it's a spectrum from simple loops to complex swarms.

- **ReAct (Source 21):** Thought→Act→Observe is the foundational loop. Grounding via tools reduces hallucination. Readable trajectories improve trustworthiness.
- **Anthropic (Source 16):** Five workflow patterns: prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer. Composable building blocks.
- **ghuntley (Source 15):** Forward loop (build→test→deploy) and reverse loop (deploy→test→build). Loops compose: nested, parallel, sequential.
- **MetaGPT (Source 22):** SOPs as agent contracts. Role→output mapping. AFlow: auto-generated workflow topologies.
- **Cursor (Source 24):** Tree-based swarm decomposition. Planner agents (smart models) split goals into subtrees; worker agents (fast/cheap models) execute leaves. Context efficiency through specialization.
- **AutoGen (Source 20):** Event-driven core for deterministic and dynamic workflows. Migration from conversation-based to event-driven model.

**Harness design implication:** The harness should support multiple execution modes:
1. **Single-agent ReAct loop** — for simple tasks (Thought→Act→Observe)
2. **Orchestrator-workers** — for complex tasks requiring decomposition
3. **Evaluator-optimizer** — for quality-sensitive tasks requiring iteration
4. **Forward/reverse loops** — for both creation and investigation modes

The default should be the simplest mode that works (Anthropic's simplicity principle). Escalate to more complex patterns only when justified.

---

### Theme F: Authority, Safety, and Human-in-the-Loop

**Sources:** 6 (Lopopolo authority), 11 (LangGraph HITL), 16 (Anthropic), 18 (OpenHands), 25 (Devin), 24 (Cursor)

Authority is not binary — it's a spectrum from full autonomy to full human control.

- **Lopopolo (Source 6):** Broad envelope for reversible work (agent can try, fail, rollback). Narrow envelope for irreversible work (agent must escalate). "Sparse delegation tests whether the environment has made the real requirements recoverable."
- **LangGraph (Source 11):** HITL as first-class interrupt primitive, not afterthought. Checkpoints enable human review at any point.
- **Anthropic (Source 16):** Agents begin with human command, operate independently, return to human for judgment. Human review remains crucial even with automated testing.
- **Devin (Source 25):** Active collaboration — reports progress, accepts feedback, surfaces decision points. Not fire-and-forget but teammate.
- **Cursor (Source 24):** "Licensed breakage" for core changes — agents can break things in controlled ways if the system can detect and repair.

**Harness design implication:** Authority boundaries must be encoded in the harness, not in human heads. The harness defines:
- What's reversible (broad envelope — agent acts autonomously)
- What's irreversible (narrow envelope — agent escalates)
- Where human touchpoints are (structured decision points, not every step)
- How rollback works (checkpoint-based, like LangGraph)

---

### Theme G: Verification and Proof — Claim-Matched Evidence

**Sources:** 7 (Lopopolo proof), 9 (OpenAI), 16 (Anthropic evaluator-optimizer), 17 (SWE-agent SWE-bench)

Verification is not afterthought — it's part of the job.

- **Lopopolo (Source 7):** "Green tests ≠ working system." Claim-matched evidence: "I deployed" ≠ "deployment is healthy." Define success where experienced.
- **OpenAI (Source 9):** Codex wired Chrome DevTools Protocol, LogQL, PromQL into agent runtime. Real verification, not mocked tests.
- **Anthropic (Source 16):** Evaluator-optimizer workflow — one LLM generates, another evaluates, loop until quality threshold met. Automated testing helps verify functionality; human review ensures alignment.
- **SWE-agent (Source 17):** SWE-bench as real-world verification. 13.86% (Devin) vs 1.96% (previous) — the gap between synthetic and real-world verification is enormous.

**Harness design implication:** Every task in the harness must include its own verification. "Build X" means "build X AND prove X works in the real environment." The proof must match the claim — unit tests for unit behavior, integration tests for integration, deployment checks for deployment. The harness should reject claims that aren't proven.

---

### Theme H: Feedback as Infrastructure — Failed Trajectories Become Durable

**Sources:** 8 (Lopopolo feedback), 9 (OpenAI doc-gardening), 15 (ghuntley loops), 24 (Cursor progressive autonomy)

Feedback is not "we fixed it" — it's "the system now prevents it."

- **Lopopolo (Source 8):** "Recurring corrections become infrastructure that shapes the next run." Failed trajectories should become durable types, APIs, lints, tests, runbooks.
- **OpenAI (Source 9):** "Doc-gardening" agent scans for deviations and opens cleanup PRs. Golden principles as mechanical rules. Codex replicates existing patterns — even bad ones — so the repository must be kept clean.
- **ghuntley (Source 15):** Each loop iteration produces feedback that shapes the next iteration. The loop doesn't terminate until the exit condition (proof) is met.
- **Cursor (Source 24):** "Progressive autonomy — move logic from harness to agent tools." As models improve, hardcoded harness behavior migrates to agent-controllable tools. The harness's role shifts from controlling to providing.

**Harness design implication:** The harness must have a feedback mechanism: failed agent runs produce lints, checks, or documentation that prevents the same failure in future runs. This is the "doc-gardening" pattern — a maintenance loop that keeps the repository teachable. The harness should also evolve: hardcoded behavior migrates to agent-controllable tools as the model's capabilities grow.

---

## 3. Cross-Source Pattern Matrix

| Pattern | Sources Supporting | Harness Application |
|---------|-------------------|---------------------|
| Progressive disclosure of context | 4, 9, 13, 19, 12 | AGENTS.md as TOC → docs/ → files |
| Loop as primary execution unit | 15, 21, 16, 24 | ReAct loop default; escalate to swarms |
| State as disk-persisted artifact | 11, 14, 23, 24 | PLANS.md + typed state + checkpoint files |
| ACI design as distinct discipline | 5, 16, 17, 18, 19 | 6-gate acceptance for every tool |
| Authority spectrum (reversible/irreversible) | 6, 11, 16, 25 | Encoded in harness, not human head |
| Claim-matched verification | 7, 9, 16, 17 | Proof belongs in the job, not after |
| Feedback → durable infrastructure | 8, 9, 15, 24 | Failed runs produce lints/checks/docs |
| Simplicity first, escalate complexity | 16, 17, 12 | Start minimal; grow when justified |
| Environment fidelity is non-negotiable | 17, 24, 25, 9 | Full dev environment; detect gaps |
| Tree-based decomposition for complex tasks | 16, 22, 24, 20 | Planner (smart) → workers (fast) |

---

## 4. The 7-Layer Harness Architecture (Emerging from Research)

Based on 25 sources, the harness design has 7 layers:

### Layer 1: Entry Point (Discovery)
- AGENTS.md as TOC (~100 lines) — standardized convention, 60k+ repos
- Structured docs/ directory for deep knowledge
- PLANS.md for task-specific navigation
- **Sources:** 9, 10, 13, 4

### Layer 2: State (Persistence)
- PLANS.md — task-level state (done/pending/blocked)
- Typed state channels — session-level state (active context, available tools)
- Disk-based state files — execution-level state (checkpoints, loop state)
- **Sources:** 11, 14, 23, 24

### Layer 3: Loop (Execution)
- Default: ReAct loop (Thought→Act→Observe)
- Forward loop: build→test→deploy (creation)
- Reverse loop: deploy→test→build (investigation)
- Escalation: orchestrator-workers, evaluator-optimizer
- **Sources:** 15, 16, 21, 24

### Layer 4: Tool (ACI)
- 6-gate acceptance: discover→select→invoke→interpret→verify→repair
- Token-budgeted context (graph-ranked, like Aider repo map)
- Poka-yoke design (make mistakes harder)
- Protocol-defined (ACP-style for interoperability)
- **Sources:** 5, 16, 17, 18, 19

### Layer 5: Authority (Safety)
- Reversible work → broad envelope (agent acts, can rollback)
- Irreversible work → narrow envelope (agent escalates)
- HITL interrupts at structured decision points
- Checkpoint-based rollback
- **Sources:** 6, 11, 16, 25

### Layer 6: Proof (Verification)
- Claim-matched evidence (proof matches the claim)
- Real environment verification (not mocked)
- Exit conditions = proof (loop doesn't terminate until proven)
- Human review for alignment (even with automated tests)
- **Sources:** 7, 9, 16, 17

### Layer 7: Feedback (Evolution)
- Failed trajectories → durable infrastructure (lints, types, checks)
- Doc-gardening agent for entropy management
- Golden principles as mechanical rules
- Progressive autonomy: harness logic → agent tools as models improve
- **Sources:** 8, 9, 15, 24

---

## 5. Key Tensions and Design Decisions

The research reveals several tensions that the harness design must resolve:

### Tension 1: Simplicity vs. Capability
- Anthropic (Source 16): "Find the simplest solution possible"
- Cursor (Source 24): Built custom VCS for 1,000 commits/sec
- **Resolution:** Start simple. Add complexity only when it's demonstrably justified by functional outcomes. The harness should make adding complexity a deliberate, documented decision.

### Tension 2: Standardization vs. Customization
- AGENTS.md (Source 10): Use the standard (60k+ repos)
- SWE-agent (Source 17): Custom ACI for domain-specific tasks
- **Resolution:** Use standards for entry points (AGENTS.md) and protocols (ACP). Customize for domain-specific tool interfaces. Standardize the interface, customize the implementation.

### Tension 3: Autonomy vs. Oversight
- Lopopolo (Source 6): Maximize autonomy inside explicit authority
- Devin (Source 25): Active collaboration with humans
- **Resolution:** Authority is a spectrum, not binary. The harness defines the spectrum: fully autonomous for reversible work, human escalation for irreversible work, structured touchpoints for meaningful decisions.

### Tension 4: Context Abundance vs. Context Scarcity
- Lopopolo (Source 4): Route the right slice at the right time
- Aider (Source 19): Graph-ranked selection within token budget
- **Resolution:** Context is always scarce. The harness must actively manage the context budget: progressive disclosure, disk offloading, dynamic sizing based on task state.

---

## 6. What This Means for Our Workspace

The 7-layer architecture maps directly to our existing workspace:

| Layer | Current State | Gap |
|-------|--------------|-----|
| Entry Point | AGENTS.md exists but is large (not ~100-line TOC) | Needs restructuring to TOC pattern |
| State | MEMORY.md + daily notes exist, but no PLANS.md | No task-level state artifact |
| Loop | Heartbeat exists but is periodic, not task-driven | No ReAct loop for task execution |
| Tool | Tools exist (DeerFlow, truth-validator, etc.) but no 6-gate validation | Tools not validated for agent legibility |
| Authority | AGENTS.md has red lines but not structured as authority spectrum | No reversible/irreversible classification |
| Proof | Truth validator exists but not integrated into every task | Verification is opt-in, not mandatory |
| Feedback | Memory system exists but no doc-gardening loop | No automatic entropy management |

---

## 7. Next Steps

1. **Step 5:** Evaluate current workspace against the 6-test diagnostic framework (from original report)
2. **Step 6:** Design the harness architecture with implementation plan
3. **Implementation:** Build the harness layers incrementally, starting with Entry Point and State

---

*Synthesis complete. 25 sources integrated across 8 themes, producing a 7-layer harness architecture with 4 key design tensions and a workspace gap analysis.*
