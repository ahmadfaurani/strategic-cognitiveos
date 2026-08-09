# Batch B — Harness Research Sources 21–25

## [21] ReAct: Synergizing Reasoning and Acting in Language Models
**URL:** https://arxiv.org/abs/2210.03629
**Type:** Paper (ICLR 2023, Yao et al.)

### Key Concepts (5 bullets)
- **Interleaved reasoning + acting:** ReAct generates reasoning traces (Thought) and task-specific actions (Act) in an interleaved manner, creating synergy: reasoning guides action plans, actions gather external info to ground reasoning.
- **Overcomes hallucination & error propagation:** On HotpotQA and FEVER, interacting with a simple Wikipedia API grounds the model, reducing the hallucination and error cascades common in pure chain-of-thought.
- **Outperforms RL/imitation on decision-making:** On ALFWorld and WebShop, ReAct beats imitation and RL methods by +34% and +10% absolute success rate, using only 1–2 in-context examples.
- **Human-interpretable trajectories:** The Thought-Act-Observation loop produces readable task-solving traces, improving trustworthiness and debuggability over black-box methods.
- **Few-shot prompted, no fine-tuning:** ReAct works via in-context prompting, making it model-agnostic and easy to deploy on any capable LLM.

### Relevance to Harness Design (3 bullets)
- **Core loop pattern for agent harnesses:** The Thought → Act → Observe cycle is the foundational control-flow pattern for any agent harness. The harness must manage this loop: dispatch actions, capture observations, feed them back, and maintain the reasoning trace.
- **Grounding via tool interface:** ReAct's Wikipedia API interaction demonstrates that harnesses need a well-defined tool interface layer so the model can query external sources mid-reasoning — directly relevant to tool-use design in the harness.
- **Interpretability as a design requirement:** ReAct's readable trajectories suggest harnesses should expose agent reasoning traces for debugging, audit, and human oversight — a first-class feature, not an afterthought.

### Notable Quotes (2)
> "While large language models have demonstrated impressive capabilities across tasks in language understanding and interactive decision making, their abilities for reasoning and acting have primarily been studied as separate topics." — Yao et al., Abstract

> "ReAct overcomes issues of hallucination and error propagation prevalent in chain-of-thought reasoning by interacting with a simple Wikipedia API, and generates human-like task-solving trajectories that are more interpretable than baselines without reasoning traces." — Yao et al., Abstract

---

## [22] MetaGPT: The Multi-Agent Framework
**URL:** https://github.com/geekan/MetaGPT
**Type:** Repo (MIT License, ICLR 2024 paper)

### Key Concepts (5 bullets)
- **`Code = SOP(Team)`:** MetaGPT's core philosophy — Standard Operating Procedures applied to teams of LLMs. The framework materializes human software-company workflows (product manager → architect → project manager → engineer) as multi-agent SOPs.
- **Role-based multi-agent architecture:** Agents are assigned distinct roles (Product Manager, Architect, Project Manager, Engineer) with structured outputs (user stories, competitive analysis, APIs, data structures, docs).
- **One-line requirement → full project:** Input a single requirement, get structured deliverables including requirements analysis, system design, API specs, and code.
- **Data Interpreter for code execution:** Beyond software generation, MetaGPT includes a Data Interpreter role that writes and executes code for data analysis tasks (e.g., sklearn Iris dataset analysis with plots).
- **AFlow (ICLR 2025 oral, top 1.8%):** Automated agentic workflow generation — the system can auto-generate and optimize its own agent workflow topologies, reducing manual orchestration design.

### Relevance to Harness Design (3 bullets)
- **SOPs as harness contracts:** MetaGPT demonstrates that encoding human workflows as structured SOPs (with defined inputs/outputs per role) gives the harness predictable handoff points between agents — directly applicable to harness design for multi-step pipelines.
- **Role specialization pattern:** The role→output mapping (PM → user stories, architect → API design, engineer → code) shows how a harness should constrain agent outputs to structured deliverables rather than freeform text, improving reliability.
- **Automated workflow generation (AFlow):** The shift from hand-designed to auto-generated workflows suggests harnesses should support pluggable/evolvable orchestration patterns, not hardcode a single topology.

### Notable Quotes (2)
> "Assign different roles to GPTs to form a collaborative entity for complex tasks." — MetaGPT README tagline

> "MetaGPT takes a one line requirement as input and outputs user stories / competitive analysis / requirements / data structures / APIs / documents, etc." — MetaGPT README

---

## [23] CrewAI: Role-Based Multi-Agent Orchestration
**URL:** https://docs.crewai.com/introduction
**Type:** Docs (Open-source framework, 100k+ certified developers)

### Key Concepts (5 bullets)
- **Flows + Crews architecture:** Flows are the "backbone" (state management, event-driven execution, control flow with branching/loops). Crews are the "intelligence" (role-playing agents with specific goals and tools that collaborate autonomously).
- **Flows manage state and control; Crews do the work:** A Flow triggers events, manages state, delegates complex tasks to a Crew, receives results, and continues — clear separation of orchestration from execution.
- **Role-Playing Agents:** Each agent has a defined role, goal, and set of tools, enabling specialization and natural task delegation patterns.
- **Production-grade design:** Built for reliability and scalability — stateful workflows that handle long-running processes, with enterprise security and compliance focus.
- **When to use Crews vs Flows:** Simple automation = single Flow with Python tasks. Complex research = Flow managing state → Crew performing research. Application backend = Flow handling API → Crew generating content → Flow saving to DB.

### Relevance to Harness Design (3 bullets)
- **Two-layer orchestration model:** The Flow/Crew split is a clean architectural pattern for harnesses — a deterministic orchestration layer (Flow) managing state and routing, with an autonomous execution layer (Crew) for creative/collaborative work. This maps well to a harness that needs both predictable control flow and flexible agent execution.
- **State management as a first-class concern:** CrewAI Flows persist state across steps and executions. A harness must treat conversation state, task state, and agent state as managed resources — not implicit context that drifts.
- **Event-driven execution for long-running tasks:** The event-driven model (trigger actions based on events/inputs) is critical for harnesses that handle async work, webhooks, or multi-turn conversations where the next step depends on external signals.

### Notable Quotes (2)
> "CrewAI is the leading open-source framework for orchestrating autonomous AI agents and building complex workflows." — CrewAI Docs, Introduction

> "For any production-ready application, start with a Flow. Use a Flow to define the overall structure, state, and logic of your application. Use a Crew within a Flow step when you need a team of agents to perform a specific, complex task that requires autonomy." — CrewAI Docs

---

## [24] Cursor: AI Code Editor — Cloud Agents & Swarm Architecture
**URL:** https://cursor.com/blog (specific posts: /blog/cloud-agent-lessons, /blog/agent-swarm-model-economics)
**Type:** Blog (Engineering posts from Cursor team)

### Key Concepts (5 bullets)
- **The development environment IS the product:** Cloud agent quality is dominated by environment fidelity. Subtle environment degradation (missing deps, no network access) silently degrades output quality — the agent doesn't crash, it just gets worse. Rebuilding a full dev environment in the cloud requires VM checkpointing, forking, secret redaction, and credential management — "enterprise IT for agents."
- **Durable execution via Temporal:** Cloud agents migrated from a work-stealing architecture (one 9 of reliability) to Temporal workflows (two 9s+), surviving inference outages, pod hibernation, and multi-day runs. Now 50M+ actions/day across 7M+ workflows; 40%+ of internal PRs from cloud agents.
- **Decouple agent loop, machine state, and conversation state:** The agent loop lives in Temporal (not the VM), enabling independent pod lifecycle management, prewarmed/readonly VMs, and an append-only streaming layer that handles retries (rewind + replay on step failure).
- **Tree-based swarm decomposition:** Planner agents (smart models) split goals into subtrees; worker agents (fast/cheap models) execute leaves. Context efficiency comes from specialization — planners never fill context with low-level detail, workers never hold the big picture. This generalizes to browsers, math, GPU kernels.
- **Custom VCS for 1,000 commits/sec:** Git/Cargo coarse locks break at swarm scale. Cursor built a custom version control system handling 1,000 commits/sec (vs 1,000/hr with Git), with coordination mechanisms: split-brain detection, design-doc-backed decision propagation, third-party merge-conflict resolution agents, megafile decomposition, and "licensed breakage" for core changes.

### Relevance to Harness Design (3 bullets)
- **Environment fidelity is non-negotiable:** A harness must ensure the agent's execution environment (tools, deps, network, secrets) is complete and verified — not just "no crash" but "full capability." The harness should detect and report environment gaps to the agent for self-healing.
- **Durable execution primitives are essential:** Long-running agents need retry, checkpointing, state persistence across failures, and decoupled lifecycle management. Temporal-style durable execution is the proven pattern — a harness that can't survive infrastructure blips will fail in production.
- **Progressive autonomy — move logic from harness to agent tools:** As models improve, hardcoded harness behavior (commit, push, CI autofix logic) should migrate to agent-controllable tools. The harness's role shifts from "controlling the agent" to "providing tools the agent can choose to use." This is the key insight for harness evolution over time.

### Notable Quotes (2)
> "The single biggest factor in cloud agent output quality is ensuring it has a full development environment, like a developer has... Instead of a crash or an error message, often the only indication is a subtle degradation in output quality." — Josh Ma, Cursor Blog

> "We think this is why the design generalizes to tasks as diverse as building a browser, solving math problems, and optimizing GPU kernels... a planner never implements, so its context never fills with low-level detail, and a worker never plans, so it can spend all its context on one narrow piece of work." — Wilson Lin, Cursor Blog

---

## [25] Cognition Devin: The First AI Software Engineer
**URL:** https://www.cognition.ai/blog/introducing-devin
**Type:** Blog (Product announcement, Cognition Labs)

### Key Concepts (5 bullets)
- **Long-term reasoning & planning:** Devin's core differentiator is long-horizon reasoning — planning and executing tasks requiring thousands of decisions, recalling relevant context at every step, learning over time, and fixing mistakes autonomously.
- **Full sandboxed dev environment:** Equipped with shell, code editor, and browser within a sandboxed compute environment — "everything a human would need to do their work." This mirrors Cursor's finding that environment fidelity is the determining factor.
- **Active collaboration with humans:** Devin reports progress in real-time, accepts feedback, and collaborates on design choices — not a fire-and-forget system but a teammate that surfaces decision points.
- **SWE-bench performance:** 13.86% end-to-end resolution on SWE-bench (real-world GitHub issues), vs. 1.96% previous SOTA. Even assisted models (told which files to edit) only reached 4.80%. Devin was unassisted.
- **Capability breadth:** Learning unfamiliar tech (reading blog posts → running ControlNet), building/deploying apps end-to-end (Game of Life → Netlify), autonomous bug fixing, fine-tuning AI models, addressing GitHub issues, contributing to mature production repos (sympy).

### Relevance to Harness Design (3 bullets)
- **Long-horizon planning as a harness concern:** Devin's "thousands of decisions" implies the harness must support long-running sessions with persistent context, plan tracking, and the ability to recover from mistakes mid-plan — not just single-turn tool calls.
- **Sandboxed environment as standard:** The shell + editor + browser triad in a sandbox is the emerging standard agent environment. A harness should provision and manage this environment, including network access control, secret management, and cleanup.
- **Human-in-the-loop touchpoints:** Devin's real-time progress reporting and feedback acceptance suggests harnesses should define structured interaction points where agents surface decisions to humans — not every step, but at meaningful choice points, balancing autonomy with oversight.

### Notable Quotes (2)
> "With our advances in long-term reasoning and planning, Devin can plan and execute complex engineering tasks requiring thousands of decisions. Devin can recall relevant context at every step, learn over time, and fix mistakes." — Cognition AI Blog

> "We are an applied AI lab focused on reasoning. We're building AI teammates with capabilities far beyond today's existing AI tools. By solving reasoning, we can unlock new possibilities in a wide range of disciplines—code is just the beginning." — Cognition AI Blog
