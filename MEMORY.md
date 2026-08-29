# Long-Term Memory

_Compact index. Detailed briefs archived to `memory/` subdirectories._
_Full historical memory: `memory/MEMORY.md.bak.20260824` (50K chars, pre-trim)_

---

## 🗳️ Johor PRN 2026 — Seat Index

**Monitoring Period:** Jun–Aug 2026 | **Status:** Active
6 seats monitored (N41 Puteri Wangsa, N16 Sungai Balang, N17 Semerah, N24 Senggarang, N33 Tenggaroh, N32 Endau).
Detail: `memory/johor-prn-2026/` + war-room briefs in `memory/`

---

## 🔧 System & Infrastructure

- **Operational since:** 2026-04-22
- **Model:** vLLM remote API (arasintegrasi.ai), GLM-5.2 permanent default
- **Fallback chain (2026-08-24):** GLM-5.2 → Qwen3.5-397B-A17B → Qwen3.5-27B. Timeout 180s. Watch: keepRecentTokens 293K > Qwen 262K
- **Fallback root cause (2026-08-27 CORRECTED):** Same-provider trap. All 3 fallback models on same `vllm` provider, same endpoint (arasintegrasi.ai), same auth profile. 502 classified as `timeout` → auth profile cooldown blocks ALL same-provider siblings. Bypass only for `rate_limit`/`overloaded`/`unknown` — timeout NOT in bypass list. Fallback chain architecturally useless for provider-level outages. Server architecture: nginx → LiteLLM → vLLM GPU nodes via Tailscale (`balinese-monster.ts.net`). 2 GPU nodes down (bgpu124=Qwen3.8-27B, bgpu125=Kimi-K3). DAF declined cross-provider fallback (codex/GPT), wants server-side fix. Previous Aug 26 diagnosis (retry-loop-same-model) was incomplete — same-provider trap is the deeper issue
- **Context geometry:** GLM-5.2 1M window, keepRecentTokens 293K, reserve 48K, floor 8K, maxTokens 32,768. Compaction: safeguard. Pruning: cache-ttl
- **Context windows:** GLM-5.2 1,048,576; Qwen3.5-397B 262,144; Qwen3.5-27B 262,144
- **Honcho model routing:** GLM-5.2 (session), Qwen3.5-397B (dialectic/dreams), Qwen3.6-27B (deriver/light). Config: `~/.hermes/config.yaml`
- **Memory backend:** QMD v2.5.3. Honcho: PostgreSQL+pgvector+Redis+TEI(bge-m3). All healthy since Aug 19. §9 DoD PASSED (5/5)
- **Scraping:** Crawl4AI 0.9.2 + Firecrawl fallback. 25-source, 100% success
- **CVS:** Master Framework (`03-VERIFICATION/CVS-FRAMEWORK.md`). T1-T6, L1-L5, 5-criteria. DUN Profiling CVS retired
- **Validation architecture:** 3 separate processes by design: Intake SOP (structuring), CVS Evidence Register (verification), Hermes Inline CVS (collection-time)
- **Hermes:** 8 active cron jobs (weekly cron audit added Aug 24, Fri 21:00 MYT)
- **DeerFlow venv:** `/home/p62operator/tools/deer-flow/.venv`
- **Removed:** Ollama (CVE-2026-5757, May 2026)
- **CognitiveOS:** 🟡 Operational with gaps. Doctrine ✅, Memory ✅, CVS ✅, Orchestration 🟡, Portfolio governance 🔴
- **ADEP-001:** Binding 5-step modus operandi. Compliance ~88%
- **Athena SOP compliance:** 4/9 (first measurement Aug 25). Record quality HIGH, procedural compliance LOW. Gaps: daily memory, commit format, confirmation notification. Feedback note drafted for DAF to forward. No direct bridge to Athena (ChatGPT/GitHub stack)
- **Cross-workstream conflation:** 4th instance of quantitative overclaim pattern (Aug 25). Ember padded RISIK timeline with PERJASA+CSM items. DAF corrected. Pattern: Ember inflates quantitative claims to create urgency

---

## 🏢 Commercial & Strategic

### Aras × CSM Partnership
- MOU signed. VoronCitadel technical training delivered Aug 14
- Post-MOU working group (Aug 20): Aisha = CSM coordinator, Amelia introduced to Zulfeka
- Co-branding confirmed (DEC-20260821-006) — CSM × Aras for all 3 products. GovSec primary proof point
- Gate 0: Roshdi executive authorization. **CORRECTED (Aug 27):** Gate 0 NOT a blocker for Gates 3-5. Gate 0 required before Gate 6 (Dr. Megat/NACSA presentation only). Gates 3-5 (Zaharudin→Bala→Wan Roshaimi) = internal CSM coordination, proceed on Azrul's partnership alignment. Gate 0 and Gates 3-5 run in parallel. Deadline ~T-15 (early October). 7-stakeholder chain: Roshdi → Azrul → Zulfeka → Bala → Wan Roshaimi → Zaharudin → Dr. Megat
- Wan Roshaimi protocol v1.2: GovSec-primary, 5-layer engagement, "integration-backed candidate" not "jointly built"
- SiberSUITE × GovSec: telemetry → analytics → CBOM → score card (pre-planning, NOT committed integration)

### Org Structure
DAF (Director, strategic+commercial) + Fuad (Practice Technical Authority) + Hadri (Blockchain Lead+COO) + Syahir (POC Engineer) + Farul (CTO/MTAI) + Amelia Nadia (SSE Lead, DEC-20260820-012)

### TBH Registry
TBH-001: PM — Cyber Security Practice. Blocks CRITICAL actions. 6 JDs exist (5 GTM + 1 PM), 0 candidates. Circular dependency: roles to offload DAF → DAF carries until filled. JD drafted (`94e4ca9`)

### Products (Dev Freeze Aug 11)
- **VoronCitadel:** POC-ready. Bursa Malaysia POC refined to pure ITSS §10 focus (DEC-20260827-001). 19 section files live on github.com/ahmadfaurani/bursa-poc. 17 requirements (§10.1-10.4), 3 use cases, 6 test scenarios, 12 acceptance criteria. 76% Native coverage. 6-9 week timeline (3 phases). ITSS §10 = existing binding law, RSWG §2.6 = forward path. Retail RM368k, early-adopter RM168k
- **GovSec-TIP:** Strategic sovereign platform. Gate 4 technical co-branding. 3-layer assessment: Layer 1 CONDITIONAL, Layer 2 CRITICAL GAP (10 missing), Layer 3 STRONG
- **chain:SENTRY:** 69% implemented, 47% deployed. 3 Critical Phase 0 blockers. Phase 0 (5 days) → 77%. chain:HARVEST new product family

### CyberDSA 2026 (Oct)
- Silver Sponsorship RM50K (deferred to Aug 24, T+2 past deadline)
- Brand narrative: "Built in Malaysia. Integrated for Malaysia. Engineered for Sovereignty."
- 193-org segmentation: 93 A-Target, 35 B-Engage, 44 C-Monitor, 19 D-Watch
- Funnel model: 3 competing versions — **Funnel v3 reconciliation needed** (MQL redefined, downstream never recalculated). Tuesday Aug 25 GTM alignment
- Repo: `cyberdsa-media`

### Teras AI Platform
Farul's 5-layer platform. DEC-20260820-008/009: Teras as infra for all 3 products. VoronCitadel deploys ON Teras. POC timeline 2-3 weeks (was 2-3 months). Target: MCMC, NSRD

### Bursa POC + RSWG Regulatory Tailwind
20-section draft v0.1. 17/22 test cases confirmed. 2 CRITICAL: AI-01/AI-02 (RAG Phase 2), DRM-01 (manual vs automated). Aug 24 meeting introduced 24-entity federation vision (PROPOSED, not committed — architecture validation required). TPRM-first sequencing recommended. RACI exists — needs revision, not recreation
**RSWG Paper (Aug 27):** Bursa Malaysia RSWG Recommendation Paper, 28 pages, CONFIDENTIAL, L1 (Official/System-of-Record). Trigger: April 2025 cyber incident. 30 brokers classified (11 bank-backed, 13 retail, 6 foreign). 9 control domains. Compliance: Dec 31, 2026. **Strongest regulatory tailwind for VoronCitadel** — §2.6 TSP Oversight = VoronCitadel TPRM module. CISO mandate (§2.9) creates named buyer in each broker. Cross-product: §2.3 SBOM → chain:SENTRY CBOM, §2.2.l AASE → Red Team Division. Regulatory-pull (not push-sell). ACT-20260827-001 capability mapping due Aug 29, ACT-20260827-002 POC doc update due Aug 30
**ITSS Directive 5.05-001 (Aug 27):** Existing binding standard (Rule 5.05, introduced May 2013, amended Jan 2017). 12 IT Security Domains, 42 pages. §10 Supplier Management = VoronCitadel TPRM precursor (already law, not recommendation). POC grounded in ITSS §10 (existing obligation), RSWG §2.6 = forward enhancement. Two-layer compliance: ITSS = floor, RSWG = ceiling. DEC-20260827-001: POC focuses on ITSS §10 as primary hook
**Bursa POC Risk Register (Aug 27):** RSK-20260827-002 — 17 risks, 6 categories. Top: B-STR-01 (compliance window, 12), B-OPS-01 (CSM chain, 12), B-OPS-02 (DAF single coordinator, 12), B-TEC-01 (test case gaps, 12). Cognitive Loop INT-20260827-003: competitive window 6-8 weeks (not 4 months), POC must complete before CyberDSA Oct 5-7 for reference case. 3 bottleneck chains: regulatory leverage, Gate 0 stall, single-validator (Fuad)
**Stakeholder Framework V1.1 (Aug 27):** DEC-20260827-002 — dependency chain reordered: Azrul → Zulfeka → Zaharudin (operational, was Gate 5) → Wan Roshaimi (technical, Gate 4) → Bala (marketing, was Gate 3) → Dr. Megat. Operational before technical, marketing after technical. Supersedes V1.0 (DOC-20260819-001). Gates 1 (Azrul) ✅ + 2 (Zulfeka) ✅ completed

### Key Decisions
- Co-branding: all 3 products CSM × Aras (DEC-20260821-006). Gate 0 required
- Funnel collision: 78 MQL → 17 POC → 7 sales matches NO canonical model. **Funnel v3 needed before Tuesday**
- IP/revenue: blanket treatment rejected. 3 product-specific frameworks needed (GovSec: joint IP, VoronCitadel: channel, chain:SENTRY: future)
- Ember role boundary (DEC-20260821-007): track/plan/operationalize, NOT execution/closing gates/hiring

### R.I.S.I.K (UiTM × PRISM 2.0)
Collaboration Framework Agreed. RM5M, 12-month, 9-component. Target funder: MCMC. 3 AI use cases. Next: internal review Aug 29, alignment Sep 5
**MCMC Second Track (Aug 26):** INIT-20260826-001 — MCMC as **client** for AI capability development (complementing funder track). 5-area fact-finding. 4-phase path: Discovery → POC → Integration → Advanced. 7-session agenda. DAF × Hadri warm-up Fri Aug 29 11 AM MYT. Convergence risk: MCMC may conflate RISIK platform with social media AI
**PRISM 2.0:** PMO-requested integration. PRISM = Aras's own platform. R.I.S.I.K × PRISM 2.0 = internal product evolution, NOT external integration. KKOM = PRISM 2.0 = PRISM + R.I.S.I.K doctrine. 5 of 6 PRISM AI agents map to R.I.S.I.K layers. Aliran Kerja Stages 1-2 partially complete
**18-Agent Build Plan:** 7 extend PRISM agents (~14.5d), 8 new (~24.5d), 2 doctrine-mandated (reference poisoning, prompt injection guard, ~6d). Total ~45d agents, ~60.5d with infra. Model routing: GLM-5.2 (extract/draft), Qwen-397B (sentiment/analysis), Qwen-27B (embedding)
**Aug 18 Meeting:** Confirmed took place. Outcomes NOT yet ingested — ACT-20260825-007 due Aug 27. CRITICAL missing data
**PRISM URS/SRS:** Pending from Farul — ACT-20260825-008 due Sep 5
**Repo:** `RISIK-Development` (private, 8 dirs, 13 files, `1f1d864`)

### PERJASA Workshop
Confirmed Sep 2-3. 8-page agenda delivered. 4 teams, 4 gates, 100-point framework. Resource collision with CyberDSA window
**PERJASA-Cohort repo (Aug 27):** github.com/ahmadfaurani/PERJASA-Cohort. 21 files, 10 dirs. Workstreams updated: **HRMIS + DOSM** (Hermes→HRMIS rename, MyMesyuarat removed — scope narrowed from 3 to 2). IP co-leads: Razale & **Naim** (new stakeholder, not previously in records)

### Cohort Programme
Governance architecture built. IP framework WIPO-aligned 50:50. Portfolio register 5 programmes with kill dates. SOP-CL-001 Monday 10:30 MYT review
**PRG-003 PMO:** Kill date arrived Aug 25 — Cognitive Loop recommended immediate kill. Decision not yet logged by DAF. First kill-date enforcement test
**PERJASA-Cohort repo:** Created Aug 27. 10-dir structured workspace from Framework V1.1. 21 files, 1,759 lines. Workstreams: Hermes, MyMesyuarat, DOSM. IP co-leads: Razale & Naim (new name — not previously in records)

### Other
- CRC 2026: RM5K sponsorship (Tier 2). Customised package due Aug 28
- UPM Purple Teaming: proposal due Sep 11
- TH-RCI Watch: active, Aug 19 remand expiry
- Project Hearth: vision doc v0.1, needs DAF's voice
- AIRecon: approved, 32x B200 + 12x A100

### Repositories
`strategic-cognitiveos` (governance), `cbo-01-commercial-ops`, `Voron-Campaign`, `HOI-Intelligence-Operations`, `th-rci-parliamentary-watch` (public), `cohort-programme`, `cyberdsa-media`, `MQL-Sales-Kit` (unified GTM workspace), `RISIK-Development` (18-agent build plan, PRISM 2.0), `PERJASA-Cohort` (Cohort Program Management Framework V1.1, Razale alignment)

---

## 📋 Active Workstreams

| Workstream | Status | Next |
|------------|--------|------|
| VoronCitadel | Productisation | A1 ✅ approved. Bursa POC refined to ITSS §10 (19 files live, 17 reqs, 3 use cases). Risk Register + Cognitive Loop built. ACT-001+003 (capability mapping) due Aug 29. ACT-002 (POC doc) due Aug 30. Fuad validation Sep 2. POC finalization Sep 5 |
| GovSec TIP | Dev freeze → CyberDSA | Gate 4 evidence pack (Aug 22-27 critical) |
| chain:SENTRY | Productisation | Phase 0 hardening |
| CSM × Aras GTM | Working group | Gate 0 open but NOT blocking (corrected: due T-15/Oct, parallel to Gates 3-5). Gates 1+2 ✅ done. TBH-001 hiring due Aug 27 — UNKNOWN. Aisha PIC 4.5+ days OVERDUE. A2 has 4 concurrent blockers. CPM undefined |
| CyberDSA 2026 | T-30 countdown (Sep 5) | 6-step gate chain: Aug 31 (Fuad+Hadri) → Sep 2 (Fuad confirms) → Sep 3 (Tuan Fatah CRITICAL) → Sep 4 (Hafiz Rahman CSM validation, DAF-owned) → Sep 5 (Zaharudin baseline). Stakeholder Framework V1.1 (chain reordered). Branding adoption Sep 1 |
| R.I.S.I.K | Framework agreed → PRISM 2.0 | Review Aug 29, alignment Sep 5. Aug 18 outcomes missing (ACT-20260825-007 due Aug 27 — NOW). 18-agent plan ready. PRISM URS/SRS pending from Farul (Sep 5). MCMC second track (capability dev client) — warm-up Aug 29 |
| PERJASA | ✅ Confirmed Sep 2-3 | PERJASA-Cohort repo live + updated (HRMIS + DOSM, Hermes renamed, MyMesyuarat removed). Naim = new IP co-lead. Logistics + Razale alignment pending |
| Cohort | Architecture built → GitHub workspace | PERJASA-Cohort repo live. Workstreams: HRMIS + DOSM (scope narrowed from 3→2). Naim = new stakeholder (IP co-lead). Razale alignment pending |
| CognitiveOS | 🟡 Operational | Orchestration automation = key gap |
| Memory Infra | ✅ FULLY OPERATIONAL | §9 DoD passed (5/5) |

---

## 📝 Daily Memory Index (condensed)

Detailed entries in `memory/YYYY-MM-DD.md`. Full historical: `memory/MEMORY.md.bak.20260824`

- **Jun 11:** MiroFish bug fixed, DeerFlow operational, Phase 1 approved
- **Jun 28:** CVS mandated. Memory harness built. QMD active
- **Jul 5-10:** Security tooling expansion. Repo separation. Crawl4AI integrated
- **Jul 24-25:** PI-OS spec received. ChatGPT+GitHub integration viable
- **Aug 2:** Background dossier PERMANENTLY DELETED per DAF directive
- **Aug 4-7:** R.I.S.I.K doctrine expanded. UiTM collaboration accepted
- **Aug 9-11:** AIRecon approved. Dev freeze on all 3 flagships
- **Aug 15-16:** R.I.S.I.K RM5M. CyberDSA positioning signed off. Kimi K3 analysis
- **Aug 17:** CSM alignment email. CognitiveOS review (🟡). Git author rewritten. Three-validation doctrine. Model stack changed to GLM-5.2
- **Aug 18:** Cohort programme built. 193-org segmentation. CyberDSA narrative. Taxonomy 43 namespaces. R.I.S.I.K deep analysis. chain:SENTRY Cognitive Loop
- **Aug 19:** Honcho Phases 1-4 complete. §5→§7→§9 cascade fixes. Model routing 3-tier. Hiddify analysis. TEI Alternative Review scheduled
- **Aug 20:** CRC RM5K. CSM working group. Bursa POC first named. chain:SENTRY v4.1. Amelia=SSE Lead. WIP Protocol. TBH Registry. Teras platform. VoronCitadel POC Mode. "That's it" SOP v1.2
- **Aug 21:** Dual-review convergence. Co-branding decision. Wan Roshaimi protocol. Ember role boundary. SOP-AV-001. ADEP-001 binding. Naming alignment. Bursa validation. Gateway fix. Repos private. ~30 records
- **Aug 22:** Gate 4 governing principle. VoronCitadel GTM Strategy from WIG. CSM email trail ingested. DAF conversion model. Project Hearth. GovSec 3-layer (Layer 1 downgraded). Gate 4 review (9-state classification). ESF. GTM quantifiable outcomes. Funnel reconciliation. Document index audit
- **Aug 23:** TBH-001 fact-check (quantitative overclaim pattern). Wan Roshaimi v1.2 (5 corrections). RCA+Remediation (6 root causes, gateway clean). Azrul review + NACSA playbook. TBH-001 JD. SOP-AV-001 validation (V2 false positives, 66% orphan). Zulfeka Gate 2 protocol. Product conflation error. 4 consecutive dreaming successes
- **Aug 24:** Model fallback configured (GLM→Qwen→Qwen). Timeout 180s. Zombie tei-health-check deleted (5.3 days, ~11,500 wasted LLM calls). Rate limit resolved. Weekly Cron Audit created (Fri 21:00 MYT). MEMORY.md trimmed (50K→9.8K, 80.6%). Social engineering framework: 3-week timeline (17 moves, 3 meetings), influence matrix (13 stakeholders), "meetings are the last 20%". AIP Gate A1 ✅ APPROVED (Track A unblocked). A2 next bottleneck (Aug 28, Aisha PIC overdue). MQL Sales Kit built (38 files, new repo). Gate 0 (Roshdi) still UNVERIFIED — highest risk. TBH-001 hiring approach due Aug 27. 5 consecutive dreaming successes
- **Aug 25:** R.I.S.I.K dominated day (5/8 sessions). PRISM 2.0 = internal product evolution (PMO-requested). 18-agent build plan (~45d agents, ~60.5d total). RISIK-Development repo created. PRISM system overview + URS/SRS analyzed. Cognitive Loop: Gate 0 + CPM = single largest gap. PRG-003 PMO kill date arrived. Athena SOP audit 4/9 (first external agent measurement). DAF corrected cross-workstream conflation (PERJASA+CSM not in RISIK). Fallback chain root cause: retry-loop-same-model. `--max-old-space-size` RETRACTED. GLM empty-response = third failure mode. 6 consecutive dreaming successes
- **Aug 26:** MCMC second track created (INIT-20260826-001, MCMC as client for AI capability dev, 4-phase path). T-40 CyberDSA engineering closure directive (6-action sequential gate chain, Fattah Hafiz = new stakeholder, RSK-20260826-001). AIP deadline check: 3 convergent deadlines in 36h (TBH-001 Aug 27, A2 Aug 28, Gate 0 Aug 28). A2 has 4 concurrent blockers. Gate 0 = 4th cycle flagging. DeerFlow cron fix (`.venv/bin/bash` → `/bin/bash`, 6 days silent failure). Heartbeat note: DO NOT RUN GATEWAY HEALTH CHECKS (Hermes watchdog handles it). 7 consecutive dreaming successes
- **Aug 27:** RSWG Paper + ITSS Directive 5.05-001 intake (L1 sources). POC refined to ITSS §10 focus (19 section files, 17 requirements, 3 use cases). Hadri T-30 closure commitment (6-step gate chain, Aug 31→Sep 5, Hafiz Rahman new stakeholder). Gate 0 dependency corrected (parallel track, due T-15 Oct not Aug 28). Stakeholder Framework V1.1 (chain reordered). 502 root cause: same-provider trap + GPU nodes down (bgpu124/bgpu125). Bursa POC Risk Register (17 risks) + Cognitive Loop (competitive window 6-8 weeks). 8 consecutive dreaming successes

---

## 🎯 DAF Operating Directives (Active)

1. **Auto-draft generation:** Proceed with draft generation whenever a need is identified — do not ask permission
2. **Draft delivery:** All drafts output to Telegram + sync to GitHub as artifacts
3. **UTC+8 canonical:** All times in UTC+8 (Malaysia) unless explicitly stated
4. **CVS mandatory:** All outputs pass CVS Master Framework validation (`03-VERIFICATION/CVS-FRAMEWORK.md`)
5. **CognitiveOS intake:** All incoming data follows 9-step SOP automatically
