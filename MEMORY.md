# Long-Term Memory

_Compact index. Detailed briefs archived to `memory/` subdirectories._

---

## 🗳️ Johor PRN 2026 — Seat Index

**Monitoring Period:** Jun–Aug 2026 | **Status:** Active

| Seat | Tier | Contest | BN% | Key Dynamic | Archive |
|------|------|---------|-----|-------------|---------|
| N41 Puteri Wangsa | Tier-1 | 5-corner (PH,BN,MUDA,Bersama,Ind) | — | MUDA incumbent not defending; Maszlee vs Rashifa youth battle | `memory/johor-prn-2026/n41-puteri-wangsa.md` |
| N16 Sungai Balang | Tier-2 | 3-corner (BN,PH,PN) | BN-fav | BN defensive; PN disruption risk; PH 2018 near-win | `memory/johor-prn-2026/n16-sungai-balang.md` |
| N17 Semerah | Tier-2 | 3-corner (BN,PH,PN) | BN-lean 60-65% | Turnout-sensitive flip seat; PN split math decisive | `memory/johor-prn-2026/n17-semerah.md` |
| N24 Senggarang | Tier-2 | 3-corner (BN,PH,PN) | BN-lean 60-65% | Live three-way; PN upset moderate (Rashid local figure) | `memory/johor-prn-2026/n24-senggarang.md` |
| N33 Tenggaroh | Tier-2 | 3-corner (BN,PH,PN) | BN-lean 55-60% | FELDA belt; margin collapse trend; PN primary challenger | `memory/johor-prn-2026/n33-tenggaroh.md` |
| N32 Endau | Tier-2 | 4-corner (BN,PH,PN,ASLI) | BN-fav 70-75% | Alwiyah incumbency+party-switch; ASLI OA debut | `memory/johor-prn-2026/n32-endau.md` |

**War room briefs (detailed PD analysis):** `memory/n16-sungai-balang-war-room-brief-20260627.md`, `memory/n17-semerah-war-room-brief-20260627.md`, `memory/n24-senggarang-turnout-scenarios-corrected-20260628.md`, `memory/n33-tenggaroh-war-room-brief-20260627.md`

---

## 🔧 System & Infrastructure Memory

- **Operational since:** 2026-04-22
- **Model backend:** vLLM remote API (arasintegrasi.ai), GLM-5.2 permanent default (set 2026-08-17, changed from Kimi-K3)
- **Context geometry:** GLM-5.2 1M window — keepRecentTokens 293K (~28%), reserve 48K, floor 8K, maxTokens 32,768. Compaction: safeguard. Pruning: cache-ttl. Injection: continuation-skip. Cross-model auto-cap via maxHistoryShare 0.7. (Applied 2026-08-17)
- **Context window corrections:** GLM-5.2 128K→1,048,576; Qwen3.5-397B 128K→262,144; Qwen3.5-27B 128K→262,144 (probed from vLLM, applied 2026-08-17)
- **Removed:** Ollama (CVE-2026-5757, 2026-05-01)
- **Memory backend:** QMD v2.5.3
- **Scraping:** Crawl4AI 0.9.2 (primary) + Firecrawl (fallback). 25-source collection: 100% success, ~5 min, 426 headlines
- **CVS:** Mandatory 2026-06-28. Upgraded to Master Framework 2026-08-17 (`03-VERIFICATION/CVS-FRAMEWORK.md`). T1-T6 tiers, L1-L5 sources, 5-criteria scoring (0-10), Rule 6 (AI cap T2/score 7). DUN Profiling CVS (`tools/truth-validator/`) retired 2026-08-17
- **Validation architecture (2026-08-17):** Three separate validation processes, three operational contexts — by design, not fragmentation:
  1. Intake SOP (9-step) → workstream management & cataloging (structuring)
  2. CVS Evidence Register → core truth validation for OSINT data collection (verification)
  3. Hermes Inline CVS → condensed validation for cronjobs (collection-time tiering)
  - `validate.sh` = narrow pre-delivery linting for political briefs only
  - Lesson: Don't assume unification is design intent. Don't repeat unverified claims from files without checking the source.
- **Signal Registry:** RETIRED 2026-08-15. CVS Evidence Register canonical (`03-VERIFICATION/CVS-EVIDENCE-REGISTER.csv`)
- **Hermes:** 15 active cron jobs, 3 workstreams. Config: `~/.hermes/config.yaml`
- **DeerFlow venv:** `/home/p62operator/tools/deer-flow/.venv`
- **Memory infrastructure (LIVE 2026-08-19):** TEI (bge-m3, :8082) deployed → 1024-dim embeddings, ~53ms inference. TEI startup flags: `--model-id BAAI/bge-m3 --max-batch-tokens 8192 --max-concurrent-requests 32 --max-batch-requests 64` (added 04:18 UTC — deriver sends batches of 50, TEI default max-batch-requests=32 caused 422 stall). Honcho API (:8000) configured for TEI, healthy. Deriver completed full queue: 833/833 work units across 6 sessions (04:59 UTC). PostgreSQL+pgvector (:5432) column altered vector(1536)→vector(1024), healthy. Redis 8.2 (:6379) healthy. Migration completed via heartbeat cron auto-fix (previous session failed mid-migration; `docker compose up -d --force-recreate` needed, not `docker restart`). (Assessed 2026-08-17, TEI deployed 2026-08-18 23:56, auto-fixed 2026-08-19 02:17, batch fix 04:18, queue complete 04:59)
- **Honcho connector (OPERATIONAL 2026-08-19):** Phase 3 (scripts) + Phase 4 (gates) complete. Scripts: recall.sh (bootstrap recall), query.sh (mid-session search), ingest.sh (write-back), gate.sh (ADEP-001 pre-task/closure gates), audit.sh (daily compliance audit). All tested, fail-open verified. 4 bugs fixed in Phase 3 (bare-list API response, missing observer/observed, wrong peer context direction, ingest ID parse). Duplicates fixed (395 from double ingestion + 134 from dedup guard pagination bug). Dedup guard added to ingest-cognitiveos.py with pagination. AGENTS.md wired: recall.sh at session start, gate.sh for D2+ tasks. HEARTBEAT.md wired: daily audit.sh. 3 compliance records in Honcho. DB clean: csm-partnership 124, cyberdsa-2026 110, cognitiveos-ops 55, risk-uitm 50, sovereign-ai-perjasa 35, productisation 32. (Phase 3 complete 05:28, Phase 4 complete 06:33)
- **CognitiveOS operational review (2026-08-17):** 🟡 OPERATIONAL WITH GAPS. Doctrine ✅, Intake 🟡, Memory ✅, CVS ✅, Collection ✅, OSINT ✅, Orchestration 🟡, Stakeholder tracking 🟡, Portfolio governance 🔴. Key gap: orchestration automation. 90-day roadmap: P1 stabilization, P2 automation, P3 optimization.
- **CognitiveOS taxonomy (expanded 2026-08-18):** 43 namespaces (was 25), 586 controlled values (was ~200). 0 violations (was 500+). Validator: `tools/validate_taxonomy.py`. 72 files normalised (organisation/→org/). 16 schemas synced. DEC-20260818-013.
- **Cognitive Loop as default practice:** DAF now applies the Cognitive Loop to most topics. The loop is the default analytical method, not a special request. SOP-CL-001 codified (Cognitive Loop Review Against Strategic Objective, 7 steps, Monday 10:30 AM UTC+8 via Hermes cron `5bb8217c7f9d`).

### Repositories
- `cognitiveos-workspace` — Technical workspace, skills, memory
- `cbo-01-commercial-ops` — Commercial operations, stakeholder decks
- `Voron-Campaign` — RMiT compliance (143 FIs, 1,001 stakeholders)
- `HOI-Intelligence-Operations` — 100 gov agencies, 10 PIRs, daily briefs
- `th-rci-parliamentary-watch` — TH RCI parliamentary watch (public). Case file + suspect deep dive. RM19.6B losses, 14+ individuals, 3 arrest waves. Critical: Aug 19 remand expiry.
- `strategic-cognitiveos` — CognitiveOS governance, records, indexes. Git author: DAF (rewritten from PKR War Room, 2026-08-17).
- `cohort-programme` — Cohort programme operational workspace: strategic objective, IP framework, portfolio register, participant templates, gate forms, Joint IP Register. Weekly Monday 10:30 AM UTC+8 review via Hermes.
- `cyberdsa-media` — CyberDSA 2026 brand narrative workspace: 13 section directories, templates (press release, social media, one-pager), QC checklist, brand glossary. TLP:AMBER.

---

## 🏢 Commercial & Strategic Memory

### Aras × CSM Partnership
- **MOU signed.** Voron Citadel (VoronDRQ) technical training delivered Aug 14 to joint sales teams
- **Aisha** (PA to En. Zulfeka) proposed as CSM-Aras PIC — confirmation expected week of Aug 18
- **SiberSUITE × GovSec integration:** Telemetry → GovSec Analytics → CBOM Agent → Cyber Score Card
- **Three co-branded sovereign tech offerings** for CyberDSA launch
- **NACSA endorsement** in active discussion
- **193-org segmentation (SEG-20260818-001):** 93 A-Target, 35 B-Engage, 44 C-Monitor, 19 D-Watch. Top 15 VIP shortlist. Shuhada execution framework: 2.1 by Aug 20, 2.2 by Aug 21, meeting requests by Aug 22.
- **Stakeholder coverage (TRK-20260818-001):** 94 records, 53 (56.4%) with no recorded contact
- **Internal org structure:** DAF (Director, strategic + commercial) + Fuad (Practice Technical Authority, technical across products, built 2 of 3) + Hadri (Blockchain Lead Architect + COO within practice, operational co-leader + ChainSentry owner), Syahir (POC Engineer, delegated by DAF DEC-20260818-007). Farul = CTO (MTAI, org-level above practice). 3-person leadership team + Syahir as support.
- **Hadri meeting:** Aug 20 (not Aug 19 — first weekly review day). Cross-product support model deferred post-PCD (Aug 28).

### CyberDSA 2026 (Oct)
- **Silver Sponsorship RM50K** — dual approval needed by Aug 22
- **Positioning statement SIGNED OFF** (DEC-20260816-002, commit `2e6fb03`)
- **Brand Narrative (DOC-20260818-002):** 13-section framework, primary reference for all materials. Campaign line: "Built in Malaysia. Integrated for Malaysia. Engineered for Sovereignty." Corporate positioning: "Aras Integrasi — Malaysian Sovereign Technology Integrator." Hierarchy: Sovereign Capability → Integrated Stack → Technology Pillars → Individual Features. Repo: `cyberdsa-media`.
- **193-org segmentation framework (SEG-20260818-001):** 93 A-Target, 35 B-Engage, 44 C-Monitor, 19 D-Watch. Top 15 VIP shortlist. Unblocks 6 CyberDSA criteria.
- **Stakeholder Coverage Tracker (TRK-20260818-001):** 94 records, 53 with no recorded contact (56.4%)
- **4 focus areas:** Partnership, Marketing/Media, Commercial, Post-Launch
- **Actions:** ACT-20260817-001 (Hadri, due Aug 22), -002/-003/-004 (due Aug 29), ACT-20260818-004 (branding team adopt narrative, due Sep 1), -005 (visual/booth design, due Sep 15)
- **Risks:** RSK-20260816-002 ("commercially viable" claim), RSK-20260816-003 ("Malaysia's First" claim → Mitigating via §9 guardrails)
- **ChainSentry assessment:** 6 critical technical gaps, zero pilot agreements, sales kit complete but zero pipeline conversion. Critical path: Hadri PCD Aug 28 → gaps Sep 5 → demo-ready Sep 15 → Oct 5. Zero slack.
- **Key decision needed:** ChainSentry vs GovSec TIP hardening priority (recommendation: ChainSentry first — sovereign blockchain story more differentiated)

### Productisation — Development Freeze (Aug 11)
- **Freeze on all 3 flagships:** VoronCitadel (=VoronDRQ), GovSec TIP, ChainSentry
- No new features. Focus: productisation, commercial readiness, GTM
- 6-category framework per product: MVP Spec, Roadmap, Backlog, Commercial Readiness, GTM Materials, Governance
- **Bottleneck:** Fuad capacity overload (21 deliverables, 1 person)
- GovSec TIP v3.0: Threat Viz, Executive Dashboard, RAG AI Analyst

### R.I.S.I.K (UiTM Collaboration)
- **INIT-20260803-002** — UiTM agreed in principle (Prof. Suhaimee + 5 team members). Readiness: Collaboration Framework Agreed (10/16 checkpoints passed).
- **Cost structure:** RM5.0M, 12-month, 9-component (DEC-20260815-001)
- **Target funder:** MCMC (STK-20260815-002)
- **Four-pillar framework (agreed):** Core IP, Derivative IP, Joint Research, Government Activation
- **Doctrine analysis (2026-08-18):** Five-layer methodology (R→I→S→I→K closed cycle), §2.5 AI rules (AI is NOT a fourth discipline, analyst accountability, source tracing), narrative escalation ladder (5 rungs), source grading A-F
- **KKOM system:** GovComms Command Center, 8-screen prototype live, 7-step pathway, TULIS→BINA→SEMAK→LULUS governance cycle
- **3 AI use cases:** (1) Signal Collection & Grading Engine, (2) Issue Decomposition Assistant, (3) Reference Poisoning Monitor (first-mover)
- **17 questions prepared for CMIWS**
- **§2.5 as self-governance:** AI rules apply to Ember's own work — accountability stays with DAF, AI output is T3 max, declare AI influence, treat monitored content as untrusted
- **Next:** Internal review (ACT-20260818-006, Aug 29), alignment session (ACT-20260818-007, Sep 5), MCMC proposal prep

### PERJASA Government AI Workshop
- **Status:** CONFIRMED Sep 2-3, 2026 (ACT-20260813-002 closed)
- **Agenda:** Delivered and shared with PERJASA (ACT-20260813-006 closed). 8-page final agenda, 12 Aug 2026.
- **Delivery model:** Discover → Design → Build → Validate (2 days, 4 teams, 3 gates)
- **Focus areas:** AI Infrastructure, AI Development, AI Cybersecurity, AI Productivity
- **Evaluation:** 100-point framework, 70 threshold for pilot progression
- **Core nucleus:** 5 named (JDN ×3, MOH ×1, SUK NS ×1)
- **Post-workshop:** 90-day continuation pathway (6 milestones)
- **Risk resolved:** RSK-20260813-001 (first risk to reach resolved status)
- **5 downstream actions unblocked:** ACT-20260813-003 through -007
- **PERJASA review:** Agenda transmitted, review pending on their side (ACT-20260813-001 → pending)
- **Resource collision:** PERJASA Sep 2-3 competes with CyberDSA hardening window for Hadri/Fuad/DAF. No mitigation decision yet.

### Cohort Programme Governance (built 2026-08-18)
- **Strategic Objective (canonical):** Alumni community as primary; co-development & joint IP creation for sovereign technology deployment as major focus
- **Pathway:** Cohort → Alumni Community → Co-Development → Joint IP → Validation → Pilot → Commercialisation → Sovereign Deployment → Enduring Strategic Ecosystem
- **Proposition:** Bring Your IP. Build With Aras. Own What We Create Together.
- **IP Framework:** WIPO-aligned, 6-layer architecture, 50:50 Foreground IP, 7-gate IP governance (MyIPO-aligned), revenue separated by component
- **Portfolio Register:** 5 programmes with kill dates. PMO (Aug 25) and CSM-Aras (Aug 25) kill dates first to enforce.
- **SOP-CL-001:** Cognitive Loop Review Against Strategic Objective — 7-step process, Monday 10:30 AM UTC+8 via Hermes cron `5bb8217c7f9d`. First run Aug 24.
- **Repo separation:** Cohort repo = operational workspace. CognitiveOS repo = governance reference only.
- **Key principle:** DAF sets strategy, Ember builds architecture. The review measures pathway stage progression, not just execution status.

### Skunkworks — AIRecon
- **APPROVED** Option A (Tracks A-E). 32x B200 + 12x A100 available — zero hardware constraint
- Intern research/extension project, not core build. Safe Mode fork (read-only recon)

---

## 📋 Active Workstreams Summary

| Workstream | Status | Next Action |
|------------|--------|-------------|
| GovSec TIP | Dev freeze → CyberDSA launch | Hardening + demo flow |
| VoronCitadel/DRQ | Productisation | Naming transition + GTM |
| ChainSentry | Productisation — 6 critical gaps | Decide hardening priority (ChainSentry vs GovSec) by Aug 20 |
| CSM × Aras GTM | Active | Aisha PIC confirmation (week of Aug 18) |
| CyberDSA 2026 | War-room | Silver sponsorship approval (Aug 22); branding team adoption (Sep 1) |
| R.I.S.I.K | Collaboration Framework Agreed | Internal review (Aug 29) + alignment session (Sep 5) |
| PERJASA Workshop | ✅ Confirmed Sep 2-3 | Logistics execution (5 downstream actions unblocked) |
| Cohort Programme | Governance architecture built | First automated review Aug 24 (SOP-CL-001) |
| UPM Purple Teaming | Proposal Stage | UPM proposal due Sep 11; Aras evaluation framework prep |
| TH-RCI Watch | Active | Aug 19 remand expiry monitoring |
| CognitiveOS | 🟡 Operational with gaps | Taxonomy expanded (43 namespaces, 0 violations). Memory infra LIVE. |
| Memory Infrastructure | ✅ LIVE (TEI→Honcho→pgvector) | Build OpenClaw→Honcho connector (step 3 of 5) |

## Action Pipeline Status (as of 2026-08-18 02:42 UTC)

| Metric | Value |
|--------|-------|
| Actions completed | 9 (8.3%) |
| Actions in draft | 60 |
| Risks resolved | 1 |
| Top 10 addressed | 6 of 10 |

**Remaining Tuesday review items (stale — 2 cycles no movement):**
1. CSM-Aras AI Token session (DAF calendar block, 2 hrs)
2. GTM programme mechanism (DAF 2-hour drafting session)
3. Tech docs handover (confirm Fuad capacity)
4. CyberDSA launch checklist (confirm Hadri acknowledgment)
5. **NEW:** Decide ChainSentry vs GovSec TIP hardening priority for CyberDSA (by Aug 20)
6. **NEW:** Hadri meeting (Aug 20, not Aug 19 — COO role, CyberDSA readiness, ChainSentry PCD)
7. **NEW:** Shuhada meeting (Aug 20 — account ownership model, 193-org framework handoff)

---

## 📝 Key Promoted Memories (Condensed)

- **2026-06-11:** MiroFish Twitter bug fixed. DeerFlow operational. Phase 1 approved.
- **2026-06-28:** CVS mandated system-wide. Memory harness built (5 scripts). QMD backend active.
- **2026-07-05:** Offensive security tooling expansion 5→16 repos. pentest-ai-agents (31 subagents) integrated.
- **2026-07-10:** Repository separation: Voron-Campaign + HOI-Intelligence-Operations. Zero data loss.
- **2026-07-19:** Crawl4AI 0.9.2 integrated. 100% collection success rate.
- **2026-07-24:** PI-OS specification received from DAF. PI-OS is format, not platform.
- **2026-07-25:** ChatGPT+GitHub integration makes PI-OS AI Layer achievable without custom scripting.
- **2026-08-02:** Personal background dossier PERMANENTLY DELETED per DAF directive.
- **2026-08-04:** R.I.S.I.K operating doctrine expanded (23 sections, 4-layer architecture).
- **2026-08-07:** UiTM R.I.S.I.K collaboration accepted in principle. 5 named team members.
- **2026-08-09:** AIRecon approved (Option A). 32x B200 + 12x A100 — no hardware limit.
- **2026-08-10:** GovSec dev freeze declared. SiberSUITE integration session. CyberDSA launch readiness.
- **2026-08-11:** Freeze expanded to all 3 flagships. 6-category productisation framework.
- **2026-08-15:** R.I.S.I.K cost structure RM5M formalised. MCMC target funder.
- **2026-08-16:** CyberDSA positioning signed off. Kimi K3 compatibility analysis (conditional). Silver sponsorship RM50K submitted. Two new DAF directives: (1) auto-draft on identified need, (2) drafts to Telegram + sync to GitHub.
- **2026-08-17:** CSM partnership alignment email sent (4 actions). Azrul stakeholder assessment completed. Weekly workplan Aug 17-21: 13 deadlines, 7 overdue. CognitiveOS operational review completed (🟡 operational with gaps). Three-validation-architecture doctrine clarified by DAF (separate by design). Memory infrastructure assessed (Honcho+pgvector+Redis idle). Git author identity rewritten (PKR War Room → DAF, 107 commits).
- **2026-08-18:** Cohort programme governance architecture built in one session (portfolio register, strategic objective, IP framework, participant artefacts, SOP-CL-001, repo, Hermes cron). 193-org segmentation framework delivered (72hrs late, 93 A-Target, 35 B-Engage). Stakeholder coverage tracker created (94 records, 56.4% no contact). CyberDSA Key Media & Brand Narrative delivered by DAF — 13-section framework, campaign line "Built in Malaysia. Integrated for Malaysia. Engineered for Sovereignty." `cyberdsa-media` repo created. RSK-20260816-003 upgraded to Mitigating. CSM formal letter (Suraya Hani → Dr. Azree, UPM) requesting 6-component Purple Teaming proposal by Sep 11. Aras formally designated infrastructure funder. INIT-20260813-004 → Proposal Stage. CognitiveOS taxonomy expanded: 25→43 namespaces, 500+→0 violations, validator built. 72 files normalised. R.I.S.I.K deep analysis: doctrine (five-layer, §2.5 AI rules), KKOM system discovery (TULIS→BINA→SEMAK→LULUS), 3 AI use cases (Signal Collection, Issue Decomposition, Reference Poisoning Monitor), 17 questions for CMIWS. 10 new records across 2 commits. ChainSentry Cognitive Loop: 6 critical gaps, zero pilot agreements, sales kit complete but zero pipeline conversion. Hadri = COO within practice (corrected). Cross-product support model deferred post-PCD (Aug 28). Hadri meeting scheduled Aug 20. Shuhada meeting designed (Meeting 3). 3 actions closed (ACT-20260802-001, -002, ACT-20260816-001). Product repo deadline extended to Aug 28. Hadri org structure updated (STK-20260803-007, commit `d5f771e`).
- **2026-08-19:** TEI (bge-m3) deployed → Honcho configured → pgvector column altered → embeddings generating. Memory infrastructure transitioned from "deployed but idle" to LIVE. Previous session (23:56 UTC) failed mid-migration; heartbeat cron auto-detected and auto-fixed at 02:17 UTC. Root cause: `docker restart` doesn't pick up new `.env` values — needed `docker compose up -d --force-recreate`. TEI batch fix at 04:18 (added `--max-batch-requests 64` — deriver sends batches of 50, TEI default 32 caused 422 stall). Deriver queue complete 833/833 at 04:59. Phase 3 connector scripts built and tested (recall.sh, query.sh, ingest.sh — 4 bugs fixed). Phase 4 operational gates built (gate.sh, audit.sh — ADEP-001 enforcement wired into AGENTS.md + HEARTBEAT.md). Duplicates fixed (395 from double ingestion + 134 from dedup guard pagination bug). Dedup guard added with pagination fix. AGENTS.md wired: recall.sh at session start, gate.sh for D2+ tasks. All containers healthy: TEI (:8082, 1024-dim, 53ms), Honcho API (:8000), Deriver, PostgreSQL (:5432), Redis (:6379). DB clean: 406 messages across 6 sessions. Memory infrastructure FULLY OPERATIONAL.

---

## 🎯 DAF Operating Directives (Active)

1. **Auto-draft generation:** Proceed with draft generation whenever a need is identified — do not ask permission
2. **Draft delivery:** All drafts output to Telegram + sync to GitHub as artifacts
3. **UTC+8 canonical:** All times in UTC+8 (Malaysia) unless explicitly stated
4. **CVS mandatory:** All outputs pass CVS Master Framework validation (`03-VERIFICATION/CVS-FRAMEWORK.md`). DUN Profiling CVS retired 2026-08-17
5. **CognitiveOS intake:** All incoming data follows 9-step SOP automatically
