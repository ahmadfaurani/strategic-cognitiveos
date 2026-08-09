# Harness Research — Batch A (Sources 16–20)

---

## [16] Anthropic — Building Effective Agents

**URL:** https://www.anthropic.com/engineering/building-effective-agents
**Type:** Blog / Engineering guide

### Key Concepts (5 bullets)
- **Workflows vs. Agents distinction:** Workflows are systems where LLMs and tools are orchestrated through predefined code paths; Agents are systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks.
- **Five canonical workflow patterns:** Prompt chaining (sequential steps), Routing (classify → dispatch), Parallelization (sectioning/voting), Orchestrator-workers (dynamic decomposition), Evaluator-optimizer (generate → critique loop). These are composable building blocks, not prescriptive.
- **Augmented LLM as the foundational building block:** Every agentic system starts with an LLM enhanced with retrieval, tools, and memory. The model actively generates search queries, selects tools, and determines what to retain.
- **Simplicity principle:** "Find the simplest solution possible, and only increase complexity when needed." Agentic systems trade latency and cost for better task performance — consider when this tradeoff makes sense.
- **Agent-Computer Interface (ACI) design:** Tool documentation and testing are critical. "Carefully craft your agent-computer interface (ACI) through thorough tool documentation and testing." Frameworks can obscure underlying prompts and responses, making debugging harder.

### Relevance to Harness Design (3 bullets)
- **Directly informs harness architecture:** The workflow patterns (especially orchestrator-workers and evaluator-optimizer) map to harness orchestration strategies for sub-agent coordination and quality loops.
- **ACI design principles apply to tool harness:** The emphasis on clear tool interfaces, good documentation, and testing directly translates to how a harness should expose tools to its agents.
- **Complexity escalation model:** The "start simple, add complexity only when it demonstrably improves outcomes" principle is a governance rule for harness feature accumulation.

### Notable Quotes (2)
> "The most successful implementations weren't using complex frameworks or specialized libraries. Instead, they were building with simple, composable patterns." — Erik S. and Barry Zhang, Anthropic

> "Carefully craft your agent-computer interface (ACI) through thorough tool documentation and testing." — Anthropic, Building Effective Agents

---

## [17] SWE-agent — Agent-Computer Interface Research

**URL:** https://github.com/princeton-nlp/SWE-agent
**Paper:** https://arxiv.org/abs/2405.15793
**Type:** Research repo / Paper (NeurIPS 2024)

### Key Concepts (5 bullets)
- **Agent-Computer Interface (ACI):** The core research contribution — LM agents are a new category of end users with their own needs and abilities, and benefit from specially-built interfaces to software. Interface design directly impacts agent performance.
- **Custom ACI for software engineering:** SWE-agent's interface enhances agents' ability to create/edit code files, navigate repositories, and execute tests/programs — designed specifically for LM agents, not human users.
- **Configurable via single YAML:** The entire agent behavior is governed by one configuration file, making it hackable and research-friendly. "Configurable & fully documented: Governed by a single yaml file."
- **Mini-SWE-agent successor:** The team now recommends mini-SWE-agent, which matches SWE-agent's performance in ~100 lines of Python, demonstrating that the ACI concepts matter more than framework complexity.
- **SWE-bench state-of-the-art:** Achieved SOTA on SWE-bench among open-source projects, validating that interface design (not framework sophistication) drives agent performance.

### Relevance to Harness Design (3 bullets)
- **ACI as first-class harness concern:** The paper formalizes that interface design for agents is a distinct discipline from human UI design. A harness must design its tool interfaces for LM consumption, not human consumption.
- **Minimalism works:** Mini-SWE-agent's 100-line implementation matching full SWE-agent performance suggests harness complexity should be measured against functional outcomes, not feature count.
- **YAML-driven configuration:** Single-file configuration for agent behavior is a pattern a harness can adopt for reproducibility and hackability.

### Notable Quotes (2)
> "LM agents represent a new category of end users with their own needs and abilities, and would benefit from specially-built interfaces to the software they use." — Yang et al., SWE-agent paper (arXiv:2405.15793)

> "Most of our current development effort is on mini-swe-agent, which has superseded SWE-agent. It matches the performance of SWE-agent, while being much simpler." — SWE-agent README

---

## [18] OpenHands — Open-Source Autonomous Agent

**URL:** https://github.com/All-Hands-AI/OpenHands
**Type:** Repo / Platform

### Key Concepts (5 bullets)
- **Agent Canvas as control center:** A self-hosted, always-on developer control center for starting conversations and automating everyday tasks — turns coding agents into a persistent engineering team.
- **Multi-backend architecture:** Agent Canvas connects to multiple "agent backends" (Docker containers, VMs, cloud, local), with the ability to switch between them without losing focus. Agent Server is a REST API for running multiple agents on a single machine.
- **ACP (Agent-Client Protocol) support:** Works with any ACP-compatible agent — OpenHands, Claude Code, Codex, Gemini — enabling agent interoperability rather than lock-in.
- **Automation Server integration:** Paired with an automation server for scheduled/event-triggered agent workflows (Slack, GitHub, Linear, Datadog integrations).
- **Bring your own model:** Works with any LLM, no model lock-in.

### Relevance to Harness Design (3 bullets)
- **Multi-backend pattern:** The separation of Agent Canvas (frontend) from Agent Server (backend API) with swappable backends is directly applicable to harness architecture — a harness should abstract its execution environment.
- **Automation integration:** The pattern of pairing agent execution with an automation server for scheduled/event-driven workflows informs how a harness can support both interactive and autonomous modes.
- **Agent interoperability via ACP:** Supporting a protocol for agent interchangeability (ACP) rather than hard-coding to one agent implementation is a design principle for harness portability.

### Notable Quotes (1)
> "The self-hosted developer control center for coding agents and automations. Run OpenHands, Claude Code, Codex, Gemini, or any ACP-compatible agent across local, remote, and cloud backends." — OpenHands README

---

## [19] Aider — AI Pair Programming, Repo Map Architecture

**URL:** https://github.com/Aider-AI/aider
**Repo Map Docs:** https://aider.chat/docs/repomap.html
**Type:** Repo / Tool

### Key Concepts (5 bullets)
- **Repository map (repo map):** Aider constructs a concise map of the entire git repository showing the most important classes, functions, and their call signatures. This gives the LLM context about the codebase structure without needing every file in context.
- **Graph-based relevance ranking:** The repo map is optimized using a graph ranking algorithm where each source file is a node and edges connect files with dependencies. Aider selects the most relevant portions of the map to fit within the active token budget.
- **Dynamic token budget management:** The `--map-tokens` switch (defaults to 1k) controls repo map size. Aider dynamically adjusts the map based on chat state — expanding significantly when no files are added to chat and the LLM needs to understand the whole repo.
- **Git-integrated workflow:** Automatic commits with sensible messages, enabling diff/manage/undo of AI changes using familiar git tools. The LLM works within the existing git workflow rather than alongside it.
- **IDE-agnostic watch mode:** Aider can be used from any IDE by adding comments to code files — aider watches for changes and acts on them, integrating into the developer's existing workflow.

### Relevance to Harness Design (3 bullets)
- **Repo map as context management:** The graph-ranked, token-budgeted repo map is a directly applicable pattern for how a harness should provide codebase context to its agents — not dumping entire repos, but ranking and selecting the most relevant symbols.
- **Dynamic context sizing:** Aider's approach of adjusting context size based on task state (expanding when broad understanding is needed, contracting when specific files are in chat) is a pattern for harness context management.
- **Git as execution substrate:** Using git commits as the atomic unit of AI changes (with automatic messages) provides a natural undo/review/diff mechanism that a harness can adopt for agent action safety.

### Notable Quotes (2)
> "Aider makes a map of your entire codebase, which helps it work well in larger projects." — Aider README

> "Aider solves this problem by sending just the most relevant portions of the repo map. It does this by analyzing the full repo map using a graph ranking algorithm, computed on a graph where each source file is a node and edges connect files which have dependencies." — Aider Repo Map docs

---

## [20] AutoGen — Multi-Agent Conversation Framework

**URL:** https://microsoft.github.io/autogen/
**Type:** Framework / Docs

### Key Concepts (5 bullets)
- **Three-tier architecture:** AutoGen Studio (web UI, no code), AgentChat (Python framework for conversational single/multi-agent apps), Core (event-driven programming framework for scalable multi-agent AI systems). Each tier builds on the one below.
- **Event-driven core:** The Core layer is an event-driven programming framework designed for deterministic and dynamic agentic workflows, multi-agent collaboration research, and distributed agents in multi-language applications.
- **Extensions ecosystem:** Built-in extensions include MCP Workbench (Model-Context Protocol), OpenAIAssistantAgent, DockerCommandLineCodeExecutor (sandboxed code execution), and GrpcWorkerAgentRuntime (distributed agents).
- **Migration from 0.2 to 0.4+:** AutoGen underwent a significant architectural shift from conversation-based to an event-driven model, indicating that the framework's design evolved toward more structured orchestration.
- **AgentChat as the prototyping layer:** The middle tier provides a programming framework for building conversational single and multi-agent applications, requiring only a few lines of code to get started.

### Relevance to Harness Design (3 bullets)
- **Tiered abstraction model:** The Studio → AgentChat → Core progression (no-code → Python prototyping → event-driven framework) is a model for how a harness can expose different complexity levels to different users.
- **Event-driven architecture for multi-agent:** The Core's event-driven design (rather than pure conversation chaining) is relevant for harness designs that need deterministic workflow guarantees alongside agent autonomy.
- **Extension pattern:** The built-in extensions (MCP, Docker execution, gRPC runtime) demonstrate how a harness should expose integration points — as pluggable extensions rather than hardcoded dependencies.

### Notable Quotes (1)
> "An event-driven programming framework for building scalable multi-agent AI systems." — AutoGen Core documentation

---

*Research batch A complete. Sources 16–20 fetched and summarized.*
