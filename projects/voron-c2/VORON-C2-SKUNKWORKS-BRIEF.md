# VORON-C2 Skunkworks — Intern Brief

**Project:** VORON-C2 Skunkworks  
**Type:** Intern skunkworks project  
**Duration:** 5 weeks  
**Supervisor:** DAF  
**Classification:** INTERNAL — RESTRICTED  
**Date:** 2026-08-06

---

## The Brief

You're getting a box and a goal. The box is a server. The goal is to deploy an open-source C2 framework, get a beacon calling back to it, and write detections for your own traffic.

But before you touch the box, you need approval. That's the project.

## Why This Exists

In cybersecurity — especially national capability work — the hardest part isn't deploying the tool. It's getting authorization to deploy the tool. Anyone can follow a GitHub README. Almost no junior person knows how to write a proposal that survives a risk-averse review committee.

This project teaches both. The approval process comes first. The technical build is the reward for getting it right.

---

## Phase 1 — The Ask (Weeks 1-2)

Before any hardware is touched, any software installed, any command run — you write the case for why this should be allowed to happen.

### Deliverables

**1. Project Proposal**
- What you want to build (scope, objectives, justification)
- Which open-source frameworks you plan to use and why
- What infrastructure you need (the box, network access, test VMs)
- What the risks are and how you'll mitigate them
- What success looks like

**2. Authorization Memo**
- Who needs to approve this and why
- What authorities are required (internal, legal if applicable)
- What the rules of engagement are for the lab environment
- What happens if something goes wrong (incident response for your own lab)

**3. Risk Assessment**
- What could go wrong
- What data is at risk
- What network exposure exists
- How you prevent the lab from touching anything outside the lab

**4. The Pitch**
- 15-minute presentation to DAF (acting as management committee)
- You present. DAF questions. You defend.
- Expect to be told to revise. That's not failure — that's the process.

### Rules

- DAF reviews and can reject any deliverable. Revise and resubmit.
- No work on the box until written approval is granted.
- If your proposal is vague, hand-wavy, or missing a risk section, it gets bounced immediately.
- If you can't articulate why this is safe, you're not ready to do it.

### Learning Objective

You learn that in this field, the paperwork comes before the payload. A proposal that doesn't survive a friendly review won't survive a hostile one. Learn here, where the worst outcome is a revision cycle.

---

## Phase 2 — The Build (Weeks 3-4)

Approval granted. Now you build.

### The Box

You get one server. It has Linux, Docker, and internet access. That's it. Everything else, you figure out.

### The Goal

1. Deploy one open-source C2 framework (suggested: Sliver — best documentation, most reliable)
2. Deploy a detection stack (suggested: Wazuh + Sysmon on a Windows test VM)
3. Get a beacon calling back from a test VM to your C2 server
4. Execute basic commands through the beacon
5. Write detection rules that catch your own beacon traffic
6. Test: can you evade your own detection rules? What does that teach you?

### Suggested Approach

- **Week 3:** Deploy Sliver server. Spin up a Windows test VM. Generate an implant. Get it calling back. Confirm you can run commands.
- **Week 4:** Deploy Wazuh. Install Sysmon on the test VM. Watch the beacon traffic. Write Sigma rules. Test them. Try to evade them.

### Constraints

- Lab environment only. No deploying agents outside the lab network.
- No scanning, probing, or touching any system outside the lab.
- All activity logged. All configurations documented.
- If you break something, report it immediately. Hiding it is the only real failure.

### Learning Objective

You learn by doing. You deployed the tool, so you understand how it works. You wrote the detections, so you understand what defenders can and can't see. You tried to evade them, so you understand the gap between "deployed" and "undetected."

---

## Phase 3 — The Report (Week 5)

### Deliverables

**1. Technical Report**
- What you deployed and how
- What detections you wrote and whether they work
- What evasions you tried and what worked
- Architecture diagram of your lab
- MITRE ATT&CK techniques you touched (map them)

**2. Process Retrospective**
- What was the approval process like?
- How many revision cycles did you go through?
- What did you get wrong in your first proposal?
- What would you do differently next time?
- What did you learn about how decisions get made in a security organization?

**3. Presentation**
- 30 minutes to DAF
- Show the working lab (live demo)
- Present the detections
- Present the process retrospective
- Be honest about what worked and what didn't

### Learning Objective

The report is not a victory lap. It's an honest accounting. The best operators are the ones who can say "here's what I built, here's where it's weak, and here's what I'd do differently." If your report says everything went perfectly, you weren't paying attention.

---

## What You Actually Learn

| Skill | How You Learn It |
|-------|-----------------|
| Writing security proposals | Phase 1 — write, get rejected, revise |
| Risk assessment | Phase 1 — identify what could go wrong before it does |
| Authorization and governance | Phase 1 — navigate the approval process |
| C2 framework deployment | Phase 2 — deploy Sliver from scratch |
| Detection engineering | Phase 2 — write rules that catch your own traffic |
| Evasion and gap analysis | Phase 2 — test what your rules miss |
| Technical documentation | Phase 3 — document what you built and what you learned |
| Honest self-assessment | Phase 3 — retrospective on both process and technical work |

---

## What You Don't Do

- Conduct red team engagements against real targets
- Deploy agents outside the lab
- Access client data or systems
- Make architecture decisions (DAF owns the architecture — you execute within it)
- Skip the approval process because "it's just a lab"

The last one is the most important. "It's just a lab" is how bad habits start. Practice the discipline here so it's automatic when it matters.

---

## Reading List

Read these before Phase 1:

1. **VORON-C2 Architecture document** — `strategic-cognitiveos/projects/voron-c2/VORON-C2-ARCHITECTURE.md`
2. **DFIR Report: BumbleBee → AdaptixC2 → Akira** — https://thedfirreport.com/2026/06/29/from-bing-search-to-ransomware-bumblebee-and-adaptixc2-deliver-akira-3/
3. **MITRE ATT&CK Enterprise Matrix** — https://attack.mitre.org/matrices/enterprise/
4. **Sliver documentation** — https://github.com/BishopFox/sliver/wiki
5. **Wazuh documentation** — https://documentation.wazuh.com/current/getting-started/

That's it. No course. No bootcamp. No hand-holding. Read, understand, propose, build, report.

---

## The One-Liner

*Deploy a C2 lab. But first, convince someone it's safe to let you.*

---

*This is a skunkworks project. The point isn't to build production infrastructure. The point is to learn that in cybersecurity, the hardest part isn't the technology — it's the authorization to use it.*
