# Harness Research — Batch C: Sources 11-15

**Extracted from:** `memory/2026-07-21.md` (fetched in prior session)  
**Date:** 2026-07-21  

---

## [11] LangGraph — Agent Orchestration Framework
**URL:** https://langchain.com/langgraph  
**Type:** docs / framework

### Key Concepts
- Low-level orchestration framework for stateful, multi-actor agents — not a high-level agent framework
- Graph-based state machine: nodes = agents/tools, edges = transitions, channels = typed state
- Human-in-the-loop as first-class primitive: interrupts, checkpoints, resume-from-any-state
- Durable execution: agents persist through failures, can run for extended periods
- Reversible execution: roll back to any checkpoint in the graph
- Trusted in production by Klarna, Uber, J.P. Morgan

### Relevance to Harness Design
- **State Layer:** LangGraph's typed channels are the mechanism for "what state flows between agents/sessions" — directly maps to the harness State Layer
- **Authority Layer:** Checkpoint-based rollback provides the "reversible work gets broad envelope" pattern from the authority thesis
- **Loop Layer:** Graph cycles (not just DAGs) enable forward and reverse loops — build→test→deploy and deploy→test→build

### Notable Quotes
> "LangGraph is a low-level orchestration framework and runtime for building, managing, and deploying long-running, stateful agents."

---

## [12] LangGraph — Frameworks, Runtimes, and Harnesses
**URL:** https://docs.langchain.com/oss/python/concepts/products  
**Type:** docs / conceptual

### Key Concepts
- Three-tier distinction: **Framework** (abstractions, integrations) → **Runtime** (durable execution, streaming, HITL, persistence) → **Harness** (predefined tools, prompts, subagents)
- Framework = easy start, standardization. Runtime = production infrastructure. Harness = batteries-included for complex tasks.
- Agent harnesses add: planning capabilities, task delegation, file system access, token management
- Deep Agents SDK builds on LangGraph + adds planning, file systems, subagent spawning, long-term memory
- Deep Agents vs Claude Agent SDK vs Manus — harness-level competition

### Relevance to Harness Design
- **Architecture taxonomy:** The framework/runtime/harness distinction clarifies what we're building — a harness, not a framework
- **Batteries included:** Harness should provide predefined tools, prompts, and subagent patterns — not require the user to build from primitives
- **Deep Agents' virtual filesystem** is directly relevant — pluggable backends, declarative permissions, context offloading to disk

### Notable Quotes
> "Agent harnesses are opinionated, batteries-included frameworks with built-in tools and capabilities for building sophisticated, long-running agents."

---

## [13] AGENTS.md — Open Convention for Guiding Coding Agents
**URL:** https://agents.md  
**Type:** convention / standard

### Key Concepts
- Open format for guiding coding agents — like README but for agents
- Used by 60k+ open-source projects
- Standardized entry point: agents read AGENTS.md first to understand the repo
- Progressive disclosure: AGENTS.md points to deeper docs
- Key fields: name, description, tools, model, instructions
- Becoming a de facto standard — major agent tools support it

### Relevance to Harness Design
- **Entry Point Layer:** AGENTS.md is the canonical entry point for the harness — the table of contents that routes to deeper sources
- **Discoverability:** The convention solves Layer 1 (discovery) — agents know to look for AGENTS.md by convention, not by human instruction
- **Standardization:** Using the convention means compatibility with the broader agent ecosystem (60k+ repos)

### Notable Quotes
> "AGENTS.md is used by 60k+ open-source projects — like README for agents."

---

## [14] OpenAI Codex — Execution Plans (PLANS.md)
**URL:** https://cookbook.openai.com  
**Type:** docs / pattern

### Key Concepts
- PLANS.md: living design documents that agents create and maintain
- Planning as a first-class artifact, not a mental exercise
- Multi-hour problems require decomposition into tracked sub-tasks
- The plan itself becomes part of the harness — reusable across sessions
- PLANS.md evolves: created at task start, updated during execution, consulted for recovery
- Enables sparse delegation: the plan captures the full task, so any agent can pick up from any point

### Relevance to Harness Design
- **State Layer:** PLANS.md is the task-level state artifact — what's done, what's pending, what's blocked
- **Recovery:** After compaction or session restart, PLANS.md is the recovery point — not conversation history
- **Whole Job:** PLANS.md enables the whole-job thesis — delegate the entire task at the highest safe level, track progress in the artifact

### Notable Quotes
> "Planning is a first-class artifact — agents create it, update it, and use it for navigation."

---

## [15] ghuntley.com — Everything-as-a-Loop
**URL:** https://ghuntley.com/loop  
**Type:** blog / philosophy

### Key Concepts
- Everything-as-a-loop: development cycles are the primary execution unit
- Forward loop: build → test → deploy (creation mode)
- Reverse loop: deploy → test → build (debugging/reverse engineering mode)
- Loops have: entry conditions, exit conditions, feedback signals
- The loop IS the harness — the harness IS the loop
- "Ralph loop" concept: continuous integration of feedback into the development cycle
- Loops compose: nested loops, parallel loops, sequential loops

### Relevance to Harness Design
- **Loop Layer:** This is the core execution model — the harness runs loops, not one-shot commands
- **Feedback Layer:** Each loop iteration produces feedback that shapes the next iteration — the feedback thesis in action
- **Proof Layer:** Exit conditions ARE the proof — the loop doesn't terminate until the exit condition (proof) is met
- **Forward/Reverse duality:** The harness must support both creation (build→test→deploy) and investigation (deploy→test→build) — this maps to the agent's need to both build new artifacts and debug existing ones

### Notable Quotes
> "The loop is the harness — the harness is the loop."

---

## Summary: Sources 11-15 Themes

| Theme | Sources | Key Insight |
|-------|---------|-------------|
| State management | LangGraph (11, 12) | Typed channels + checkpoints = durable state |
| Entry point convention | AGENTS.md (13) | Standardized discovery — 60k+ repos |
| Task-level planning | Codex PLANS.md (14) | Plan as artifact, not mental exercise |
| Execution model | ghuntley loop (15) | Loop as primary unit, forward/reverse modes |
| Harness taxonomy | LangChain products (12) | Framework vs Runtime vs Harness — we're building a harness |
