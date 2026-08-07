# VORON-C2 — Internal Communication Campaign for Management Engagement

**Document Status:** DRAFT v0.1  
**Date:** 2026-08-06  
**Authority:** DAF  
**Classification:** INTERNAL — RESTRICTED  
**Purpose:** Secure management alignment and approval for sovereign C2 infrastructure initiative

---

## 1. Campaign Objective

**Single sentence:** Secure formal management approval to proceed with Phase 1 (Foundation) of VORON-C2 — a sovereign, open-source C2 infrastructure capability for Aras Integrasi's cybersecurity practice, with future GovSec integration.

**Sub-objectives:**
- Establish strategic urgency (why now)
- Demonstrate operational feasibility (how it works)
- Present financial viability ($0 licensing, resource requirements)
- Build confidence in governance and risk management (how we stay safe and legal)
- Create decision momentum toward Phase 1 kickoff

---

## 2. Audience Analysis

| Audience | Role | What They Care About | Concern To Address |
|----------|------|---------------------|-------------------|
| **CEO / MD** | Strategic direction, revenue, competitive positioning | Does this create market advantage? Is it aligned with business strategy? | Strategic value, differentiation, ROI |
| **CFO / Finance** | Cost, budget, financial risk | What does this cost? What's the return? | Budget clarity, zero-licensing model, revenue potential |
| **COO / Operations** | Delivery capability, operational risk | Can we actually execute this? Do we have the people? | Resource plan, capability build-out, delivery risk |
| **CTO / Technical Lead** | Technical architecture, security | Is the architecture sound? Are we creating exposure? | Technical due diligence, security of the stack, isolation |
| **Legal / Compliance** | Legal exposure, regulatory | Are we legally covered? What if something goes wrong? | Authorization framework, RoE, Computer Crimes Act compliance |
| **GovSec Liaison** (if applicable) | Government alignment | Does this align with national cyber strategy? | National capability narrative, GovSec integration path |

---

## 3. Campaign Architecture — 5 Touchpoints

```
Week 1: Executive Brief (Strategic Vision)
    ↓
Week 2: Technical Deep Dive (Architecture & Feasibility)
    ↓
Week 3: Governance & Risk Review (Legal, Audit, Compliance)
    ↓
Week 4: Financial & Resource Plan (Cost, ROI, Team)
    ↓
Week 5: Decision Session (Approval & Kickoff Authorization)
```

Each touchpoint is a document + a meeting. Documents sent 48 hours before each meeting. Meetings are 30-45 minutes. Decision session is 60 minutes.

---

## 4. Touchpoint 1 — Executive Brief (Strategic Vision)

### Document: "Sovereign C2 — Why Aras Integrasi Needs This Now"

**Format:** 4-page executive brief  
**Audience:** CEO/MD, CFO, COO, CTO  
**Objective:** Create strategic urgency and frame the opportunity

### Document Structure

#### Page 1 — The Strategic Gap

**Opening:**
Malaysia's cybersecurity capability landscape has a structural gap: we depend on foreign-owned or commercial C2 platforms for red team operations, adversarial emulation, and detection validation. This creates three vulnerabilities:

1. **Dependency Risk** — Foreign vendors can revoke access, restrict features, or deny service based on geopolitical pressure. We cannot build a national cyber defense capability on rented ground.

2. **Capability Gap** — Malaysia lacks an indigenous red team / adversarial emulation capability that can operate across government infrastructure without importing foreign operators. Every national cyber exercise relies on foreign tools or foreign personnel.

3. **Detection Deficit** — Malaysian SOC teams cannot train against real adversary tooling without importing foreign operators to generate attack telemetry. Our blue teams are training on simulations, not real C2 traffic.

**The Ask:** Build a sovereign, open-source C2 infrastructure — fully owned, fully controlled, zero licensing cost — as a foundational capability for Aras Integrasi's cybersecurity practice and future national cyber defense operations.

#### Page 2 — The Threat Landscape (Why Now)

**Recent operational intelligence demonstrates urgency:**

- **Akira Ransomware (July 2025):** Threat actors used open-source C2 framework (AdaptixC2) to move from initial access to domain-wide ransomware in 44 hours. This is the threat our clients face today. (Source: The DFIR Report, June 2026)

- **Adversary tool adoption accelerating:** Open-source C2 frameworks (Sliver, Mythic, Havoc, AdaptixC2) are being adopted by ransomware affiliates at scale. Akira alone has compromised 250+ organizations and collected ~$42M in ransoms since March 2023. (Sources: Unit 42, CyberSecurityNews, Silent Push)

- **AI-assisted attacks:** Threat actors are using AI to generate deployment scripts for C2 frameworks — lowering the barrier to entry and accelerating attack timelines. (Source: Unit 42, high confidence assessment)

- **Malaysian context:** Government and CNI infrastructure is a target. National cyber exercises need realistic red team capability. We cannot defend what we cannot emulate.

**The point:** The threat is real, it's here, and it's using open-source tools. We need to understand these tools — which means we need to operate them.

#### Page 3 — The Solution (VORON-C2)

**What:** A 4-framework, 4-layer sovereign C2 infrastructure:

- **4 C2 Frameworks** — Mythic (primary platform), Sliver (workhorse), Havoc (stealth), AdaptixC2 (adversary emulation)
- **4 Infrastructure Layers** — C2 Core, Redirectors + DNS, Operations (payload lab, operator console, engagement logging), Detection Engineering (Wazuh + ELK + Sigma)
- **4-Phase Roadmap** — Foundation (M1-3) → Expansion (M3-6) → Operationalization (M6-12) → GovSec Integration (M12-18)
- **$0 Licensing Cost** — Every component is open-source

**Why this approach:**
- Multiple frameworks = no single point of dependency
- Detection engineering layer = the stack pays for itself in SOC capability
- GovSec integration path = national capability, not just a commercial service
- Phased delivery = low upfront commitment, demonstrable progress

#### Page 4 — The Ask

**Phase 1 commitment (Months 1-3):**
- Provision lab environment (existing infrastructure, minimal incremental cost)
- Deploy Mythic + Sliver (open-source, no licensing)
- Train 2-3 operators (internal team, structured curriculum)
- First internal purple team exercise (lab environment)
- Governance framework + RoE templates (legal compliance)

**Resource requirements:**
- 1 server (existing or incremental) for Tier 0 lab
- 2-3 VPS instances for redirector infrastructure (~RM 200/month)
- 2-3 operator FTE allocation (partial, ramping)
- Legal counsel engagement for RoE framework (~5-10 hours)

**Decision requested:** Approval to proceed with Phase 1, with Phase 2 review at Month 3.

### Meeting Agenda (30 min)

| Time | Topic | Lead |
|------|-------|------|
| 0-5 | Strategic gap presentation | DAF |
| 5-10 | Threat landscape overview | DAF |
| 10-20 | VORON-C2 solution overview | DAF |
| 20-25 | Resource requirements + Phase 1 ask | DAF |
| 25-30 | Discussion + next steps | All |

---

## 5. Touchpoint 2 — Technical Deep Dive (Architecture & Feasibility)

### Document: "VORON-C2 Technical Architecture — How It Works"

**Format:** 8-10 page technical brief + architecture diagram  
**Audience:** CTO/Technical Lead, COO, senior technical staff  
**Objective:** Demonstrate technical feasibility and architectural soundness

### Document Structure

1. **Architecture Overview** — the 4-layer diagram from the architecture document
2. **Framework Selection Rationale** — why 4 frameworks, what each does, comparison matrix
3. **Infrastructure Design** — hosting tiers, redirector architecture, DNS infrastructure
4. **Security of the Stack** — how we protect the C2 infrastructure itself (air-gapped Tier 0, VPN-only access, certificate-based operator auth, audit logging)
5. **Detection Engineering** — how the stack generates defensive value (purple team workflow, ATT&CK mapping, Sigma rule development)
6. **Lab to Production Pipeline** — how we go from lab testing to client engagements (phased, controlled, audited)

### Key Messages

- This is not experimental — all 4 frameworks are in production use globally by legitimate red teams AND threat actors
- The architecture is defensive-first — it exists to serve detection engineering, not offensive operations
- Security of the C2 infrastructure itself is designed-in (air gaps, VPN, cert auth, audit)
- The stack integrates with existing Aras Integrasi capabilities (Wazuh, SIEM, threat intel)

### Meeting Agenda (45 min)

| Time | Topic | Lead |
|------|-------|------|
| 0-5 | Recap from Executive Brief | DAF |
| 5-15 | Architecture walkthrough | DAF / Technical Lead |
| 15-25 | Framework comparison + selection rationale | DAF / Technical Lead |
| 25-35 | Security of the stack + detection engineering | DAF / Technical Lead |
| 35-45 | Q&A + technical concerns | All |

---

## 6. Touchpoint 3 — Governance & Risk Review

### Document: "VORON-C2 Governance Framework — Authorization, Legal, Audit"

**Format:** 6-8 page governance brief  
**Audience:** Legal/Compliance, CTO, COO, CEO/MD  
**Objective:** Address legal exposure, demonstrate governance maturity, secure legal sign-off

### Document Structure

1. **Legal Basis** — Computer Crimes Act 1997 compliance, written authorization requirement, contract terms
2. **Authorization Matrix** — who approves what, at what level, for which engagement type
3. **Rules of Engagement (RoE) Template** — the actual template (targets, prohibited actions, data handling, engagement window)
4. **Audit & Accountability** — session recording, command logging, post-engagement review, segregation of duties, annual external audit
5. **Risk Register** — the 6 risks from the architecture document with mitigations
6. **Data Handling** — what data is collected during engagements, how stored, how destroyed, PDPA 2010 compliance
7. **Incident Response** — what happens if something goes wrong during an engagement (C2 infrastructure compromised, unintended impact on client systems)

### Key Messages

- No engagement proceeds without written authorization — this is non-negotiable
- Every operator action is logged and auditable
- The RoE template is modeled on industry standard (same approach used by Big 4, Mandiant, etc.)
- We engage legal counsel before any client engagement
- The risk register is documented with mitigations for each identified risk

### Meeting Agenda (45 min)

| Time | Topic | Lead |
|------|-------|------|
| 0-5 | Recap from previous sessions | DAF |
| 5-15 | Legal framework + authorization matrix | DAF / Legal |
| 15-25 | RoE template walkthrough | DAF / Legal |
| 25-35 | Risk register + incident response | DAF |
| 35-45 | Q&A + legal sign-off discussion | All |

---

## 7. Touchpoint 4 — Financial & Resource Plan

### Document: "VORON-C2 Phase 1 — Cost, Resources, ROI"

**Format:** 4-5 page financial brief + spreadsheet  
**Audience:** CFO, COO, CEO/MD  
**Objective:** Demonstrate financial viability and resource feasibility

### Document Structure

1. **Cost Breakdown — Phase 1 (Months 1-3)**

| Item | Cost (RM) | Notes |
|------|-----------|-------|
| Lab server (if new) | 8,000-15,000 | One-time. Can use existing infrastructure. |
| VPS (redirectors) | 600/quarter | 2-3 VPS at ~RM 80-100/month each |
| Domain registration | 150/year | 2-3 domains |
| Operator time (partial) | Internal allocation | 2-3 FTE partial, ramping from 20% → 50% |
| Legal counsel | 2,000-5,000 | RoE review, ~5-10 hours |
| Training materials | 0 | All open-source documentation |
| **Total Phase 1** | **~RM 10,000-20,000** | Existing infrastructure → lower end |

2. **Revenue Model — Phase 2+ (Months 3-12)**

| Service | Price Range (RM) | Target Volume | Annual Revenue Potential |
|---------|-----------------|--------------|------------------------|
| Red Team Engagement (per engagement) | 50,000-150,000 | 4-6/year | 200,000-900,000 |
| Purple Team Engagement (per engagement) | 30,000-80,000 | 6-8/year | 180,000-640,000 |
| Detection Engineering Service (retainer) | 10,000-25,000/month | 2-3 clients | 240,000-900,000 |
| National Cyber Exercise (government) | 200,000-500,000 | 1-2/year | 200,000-1,000,000 |
| Training & Certification | 5,000-15,000/person | 20-30 people | 100,000-450,000 |

**Conservative Year 1-2 estimate:** RM 500,000-1,500,000 revenue from services built on VORON-C2.

3. **ROI Analysis**

| Metric | Value |
|--------|-------|
| Phase 1 Investment | RM 10,000-20,000 |
| Year 1-2 Revenue (conservative) | RM 500,000-1,500,000 |
| ROI (Year 1) | 25x-75x |
| Breakeven | First paying engagement |

4. **Resource Plan**

| Role | Phase 1 | Phase 2 | Phase 3 |
|------|---------|---------|---------|
| Red Team Lead | DAF (partial) | DAF + 1 FTE | DAF + 2 FTE |
| Red Team Operator | 1-2 (partial, internal) | 2 FTE | 3 FTE |
| Detection Engineer | 1 (partial, internal) | 1 FTE | 2 FTE |
| Legal Counsel | External (as needed) | External | External |

5. **Strategic Value (Non-Financial)**

- National capability — positioning Aras Integrasi as the Malaysian authority on sovereign red team
- GovSec partnership — gateway to national cyber exercise infrastructure
- Competitive differentiation — no other Malaysian firm has indigenous C2 capability
- Talent magnet — red team capability attracts top cybersecurity talent

### Meeting Agenda (30 min)

| Time | Topic | Lead |
|------|-------|------|
| 0-5 | Recap from previous sessions | DAF |
| 5-15 | Cost breakdown + ROI | DAF |
| 15-20 | Resource plan | DAF |
| 20-30 | Discussion + budget alignment | All |

---

## 8. Touchpoint 5 — Decision Session

### Document: "VORON-C2 — Decision Summary"

**Format:** 2-page decision memo  
**Audience:** Full management committee  
**Objective:** Secure formal approval to proceed with Phase 1

### Decision Memo Structure

#### Page 1 — Summary

**The Initiative:** Build VORON-C2 — a sovereign, open-source C2 infrastructure as a national capability for red team operations, adversarial emulation, and detection engineering.

**The Gap:** Malaysia lacks indigenous red team capability. We depend on foreign tools and operators. Our SOC teams train on simulations, not real threats.

**The Solution:** 4-framework, 4-layer architecture. Open-source. $0 licensing. Phased delivery over 18 months. GovSec integration path.

**The Cost:** Phase 1: RM 10,000-20,000 + internal resource allocation. Phase 2+: funded by first client engagements.

**The Risk:** Managed through governance framework, written authorization, audit trail, legal compliance.

**The Return:** Conservative RM 500,000-1,500,000 Year 1-2. Strategic positioning as national capability. GovSec partnership gateway.

#### Page 2 — Decision Requested

**Approval sought:**

1. ✅ Proceed with Phase 1 (Months 1-3) — lab setup, Mythic + Sliver deployment, operator training, governance framework
2. ✅ Allocate 2-3 operator FTE (partial, Phase 1) for training and infrastructure deployment
3. ✅ Authorize VPS + domain budget (~RM 600/quarter)
4. ✅ Engage legal counsel for RoE framework (~RM 2,000-5,000)
5. ✅ Schedule Phase 2 review at Month 3 (go/no-go decision for client engagements)

**No further commitment requested at this stage.** Phase 2 is a separate decision point.

### Meeting Agenda (60 min)

| Time | Topic | Lead |
|------|-------|------|
| 0-10 | Full summary presentation | DAF |
| 10-25 | Open discussion — concerns, questions, modifications | All |
| 25-40 | Risk + governance + legal discussion | Legal / CTO / DAF |
| 40-50 | Financial + resource discussion | CFO / COO / DAF |
| 50-60 | Decision + next steps | CEO/MD |

---

## 9. Supporting Materials

### Pre-Campaign Preparation

- [ ] VORON-C2 Architecture document finalized (✅ drafted)
- [ ] 1-page summary version of architecture for non-technical readers
- [ ] ROI spreadsheet built (interactive model)
- [ ] RoE template reviewed by legal counsel (before Touchpoint 3)
- [ ] Risk register reviewed by CTO (before Touchpoint 3)
- [ ] Demo prepared for Touchpoint 2 — basic Mythic + Sliver deployment in lab showing C2 beacon, task execution, and SIEM detection

### Campaign Schedule Template

| Week | Touchpoint | Document Sent | Meeting Date | Attendees |
|------|-----------|---------------|---------------|-----------|
| 1 | Executive Brief | Monday | Thursday | CEO, CFO, COO, CTO |
| 2 | Technical Deep Dive | Monday | Thursday | CTO, COO, Tech Lead |
| 3 | Governance & Risk | Monday | Thursday | Legal, CTO, COO, CEO |
| 4 | Financial & Resource | Monday | Thursday | CFO, COO, CEO |
| 5 | Decision Session | Monday | Thursday | Full committee |

---

## 10. Communication Style Guidance

For DAF specifically — aligned to your established communication pattern:

**Structure:** Acknowledge context → Confirm strategic alignment → Present opportunity → Identify requirements → Propose action → Reinforce commitment

**Tone:** Professional, confident, evidence-backed. Not selling — informing and recommending. Let the architecture and the threat landscape make the case.

**Key phrases that resonate with your leadership style:**
- "This is a capability gap we can close"
- "Sovereign capability, not rented dependency"
- "Defensive-first — we operate these tools to build detection, not to attack"
- "Phased approach — low initial commitment, demonstrable progress"
- "National capability with commercial application"
- "Zero licensing cost — the entire stack is open-source"

**Anticipated objections + responses:**

| Objection | Response |
|-----------|----------|
| "Is this legal?" | Written authorization mandatory. Computer Crimes Act compliant. Legal counsel engaged. No engagement without RoE. |
| "Do we have the people?" | Phase 1 is training-focused. We build the team as we build the capability. Start with internal allocation. |
| "What if the C2 infrastructure gets compromised?" | Air-gapped Tier 0. VPN-only access. Certificate-based auth. The same security standards we apply to client environments. |
| "Why not just buy Cobalt Strike?" | RM 150,000+/year licensing. Foreign vendor dependency. No sovereign control. Open-source stack = $0 + full control + customization. |
| "Is this just for red teaming?" | No. The detection engineering layer is where the sustained value is — every engagement generates telemetry that improves client SOC capability. |
| "Why now?" | Threat actors are already using these tools against Malaysian targets. Every month we wait is a month our clients defend against tools we don't understand. |

---

## 11. Post-Campaign Actions

If approved:
1. Formal kickoff memo (Phase 1 start date, resource allocation confirmed)
2. Lab provisioning initiated
3. Operator training schedule published
4. Legal counsel engagement for RoE framework
5. Monthly progress report to management committee
6. Phase 2 review scheduled at Month 3

If not approved:
1. Document concerns raised
2. Adjust architecture/plan based on feedback
3. Reschedule decision session with revised proposal
4. Consider phased pilot (even smaller — Sliver only, single operator, lab only)

---

*This campaign is designed to build alignment through evidence, not persuasion. Each touchpoint adds a layer of confidence. The goal is informed decision-making — not approval pressure.*
