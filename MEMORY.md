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
- **Memory infrastructure (assessed 2026-08-17):** Honcho API (:8000) + Deriver worker running. PostgreSQL+pgvector (:5432) healthy, VECTOR_STORE_MIGRATED=false. Redis 8.2 (:6379) healthy. Model endpoint Qwen3.5-397B configured. All deployed 5+ weeks, all idle — no clients writing. Path: migrate vector store → verify Honcho API → build OpenClaw→Honcho connector → ingest records → wire into session bootstrap.
- **CognitiveOS operational review (2026-08-17):** 🟡 OPERATIONAL WITH GAPS. Doctrine ✅, Intake 🟡, Memory ✅, CVS ✅, Collection ✅, OSINT ✅, Orchestration 🟡, Stakeholder tracking 🟡, Portfolio governance 🔴. Key gap: orchestration automation. 90-day roadmap: P1 stabilization, P2 automation, P3 optimization.

### Repositories
- `cognitiveos-workspace` — Technical workspace, skills, memory
- `cbo-01-commercial-ops` — Commercial operations, stakeholder decks
- `Voron-Campaign` — RMiT compliance (143 FIs, 1,001 stakeholders)
- `HOI-Intelligence-Operations` — 100 gov agencies, 10 PIRs, daily briefs
- `th-rci-parliamentary-watch` — TH RCI parliamentary watch (public). Case file + suspect deep dive. RM19.6B losses, 14+ individuals, 3 arrest waves. Critical: Aug 19 remand expiry.
- `strategic-cognitiveos` — CognitiveOS governance, records, indexes. Git author: DAF (rewritten from PKR War Room, 2026-08-17).

---

## 🏢 Commercial & Strategic Memory

### Aras × CSM Partnership
- **MOU signed.** Voron Citadel (VoronDRQ) technical training delivered Aug 14 to joint sales teams
- **Aisha** (PA to En. Zulfeka) proposed as CSM-Aras PIC — confirmation expected week of Aug 18
- **SiberSUITE × GovSec integration:** Telemetry → GovSec Analytics → CBOM Agent → Cyber Score Card
- **Three co-branded sovereign tech offerings** for CyberDSA launch
- **NACSA endorsement** in active discussion

### CyberDSA 2026 (Oct)
- **Silver Sponsorship RM50K** — dual approval needed by Aug 22
- **Positioning statement SIGNED OFF** (DEC-20260816-002, commit `2e6fb03`)
- **4 focus areas:** Partnership, Marketing/Media, Commercial, Post-Launch
- **Actions:** ACT-20260817-001 (Hadri, due Aug 22), -002/-003/-004 (due Aug 29)
- **Risks:** RSK-20260816-002 ("commercially viable" claim), RSK-20260816-003 ("Malaysia's First" claim)

### Productisation — Development Freeze (Aug 11)
- **Freeze on all 3 flagships:** VoronCitadel (=VoronDRQ), GovSec TIP, ChainSentry
- No new features. Focus: productisation, commercial readiness, GTM
- 6-category framework per product: MVP Spec, Roadmap, Backlog, Commercial Readiness, GTM Materials, Governance
- **Bottleneck:** Fuad capacity overload (21 deliverables, 1 person)
- GovSec TIP v3.0: Threat Viz, Executive Dashboard, RAG AI Analyst

### R.I.S.I.K (UiTM Collaboration)
- **INIT-20260803-002** — UiTM agreed in principle (Prof. Suhaimee + 5 team members)
- **Cost structure:** RM5.0M, 12-month, 9-component (DEC-20260815-001)
- **Target funder:** MCMC (STK-20260815-002)
- **Next:** MCMC proposal prep (ACT-20260815-006), UiTM working session

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

### Skunkworks — AIRecon
- **APPROVED** Option A (Tracks A-E). 32x B200 + 12x A100 available — zero hardware constraint
- Intern research/extension project, not core build. Safe Mode fork (read-only recon)

---

## 📋 Active Workstreams Summary

| Workstream | Status | Next Action |
|------------|--------|-------------|
| GovSec TIP | Dev freeze → CyberDSA launch | Hardening + demo flow |
| VoronCitadel/DRQ | Productisation | Naming transition + GTM |
| ChainSentry | Productisation | Regulator use-case deck |
| CSM × Aras GTM | Active | Aisha PIC confirmation (Aug 18) |
| CyberDSA 2026 | War-room | Silver sponsorship approval (Aug 22) + Brand narrative framework adopted (DEC-20260818-011) |
| R.I.S.I.K | Cost-structured | MCMC proposal + UiTM session |
| PERJASA Workshop | ✅ Confirmed Sep 2-3 | Logistics execution (5 downstream actions unblocked) |
| UPM Purple Teaming | Proposal Stage | UPM proposal due Sep 11; Aras evaluation framework prep |
| TH-RCI Watch | Active | Aug 19 remand expiry monitoring |
| CognitiveOS | 🟡 Operational with gaps | 268 records, 551 fixes. Orchestration automation gap. |

## Action Pipeline Status (as of 2026-08-18 02:42 UTC)

| Metric | Value |
|--------|-------|
| Actions completed | 9 (8.3%) |
| Actions in draft | 60 |
| Risks resolved | 1 |
| Top 10 addressed | 6 of 10 |

**Remaining Tuesday review items:**
1. CSM-Aras AI Token session (DAF calendar block, 2 hrs)
2. GTM programme mechanism (DAF 2-hour drafting session)
3. Tech docs handover (confirm Fuad capacity)
4. CyberDSA launch checklist (confirm Hadri acknowledgment)

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
- **2026-08-18:** PERJASA workshop confirmed Sep 2-3. Agenda delivered and shared. ACT-20260813-006 + ACT-20260813-002 closed. RSK-20260813-001 resolved (first risk to reach resolved). 5 downstream PERJASA actions unblocked. Action pipeline: 9 completed (8.3%), 60 in draft, 1 risk resolved. Top 10: 6 addressed, 4 remaining for Tuesday review (CSM-Aras token session, GTM mechanism, tech docs handover, CyberDSA launch checklist). TH-RCI parliamentary watch repo made public — case file + suspect deep dive (14+ individuals, 3 arrest waves, 2 fugitives, RM19.6B losses). Critical date: Aug 19 remand expiry. CSM formal letter (Suraya Hani → Dr. Azree, UPM) requesting 6-component technical proposal for Autonomous AI Cyber Security Purple Teaming by Sep 11. Aras formally designated as infrastructure funder — first written acknowledgement. INIT-20260813-004 upgraded Concept → Proposal Stage. 7 new records, 4 indexes updated. CyberDSA 2026 Key Media & Brand Narrative delivered by DAF — complete 13-section framework directing branding team to frame story as Malaysian sovereign technology capability (not products). Campaign line: "Built in Malaysia. Integrated for Malaysia. Engineered for Sovereignty." Corporate positioning: "Aras Integrasi — Malaysian Sovereign Technology Integrator." Branding hierarchy: Sovereign Capability → Integrated Stack → Technology Pillars → Individual Features. RSK-20260816-003 ("Malaysia's First" claim risk) upgraded to Mitigating via §9 messaging guardrails. 5 new records, 3 indexes updated.

---

## 🎯 DAF Operating Directives (Active)

1. **Auto-draft generation:** Proceed with draft generation whenever a need is identified — do not ask permission
2. **Draft delivery:** All drafts output to Telegram + sync to GitHub as artifacts
3. **UTC+8 canonical:** All times in UTC+8 (Malaysia) unless explicitly stated
4. **CVS mandatory:** All outputs pass CVS Master Framework validation (`03-VERIFICATION/CVS-FRAMEWORK.md`). DUN Profiling CVS retired 2026-08-17
5. **CognitiveOS intake:** All incoming data follows 9-step SOP automatically
