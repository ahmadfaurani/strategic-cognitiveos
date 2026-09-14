---
# === UNIVERSAL BASE ===
id: DEC-20260914-004
record_type: decision
title: "Crawl4ai 25-Source Political Collection Retired (P3) — Crontab Removed After Final Run 16:04Z; 92-Day Corpus Archived to Private Repository political-news-collection"
created_at: "2026-09-14T16:15:00+00:00"
updated_at: "2026-09-14T16:15:00+00:00"
owner: faurani-jaafar
status: active
priority: medium
sensitivity: confidential
lifecycle_state: candidate
confidence: high
channel: telegram
decision_date: '2026-09-14'
decision_owner: faurani-jaafar
decision_type: structural
decision_weight: medium
tags:
  - domain/intelligence
  - domain/knowledge-management
  - mission/political-intelligence
  - mission/organisational-capability
  - type/retirement
source:
  type: telegram
  reference: "DAF directive via Telegram direct, 2026-09-14 16:09 UTC: 'P3' (retire collection) — response to the purpose review of the crawl4ai political-collection cron, which tabled P1 keep-with-consumer / P2 reduce-cadence / P3 retire / P4 keep-as-is"
summary: "[FACT] DAF decision: the crawl4ai 25-source Malaysian political news collection is retired. Purpose review (16:06 UTC) found the sensor layer healthy (4x/day cadence, 25/25 sources) but the consumption chain decayed: PRN-Johor war-room layer last active 20 Jul, curated INTEL-06X brief series stopped 4 Aug, analysis layers dormant, and no systematic consumer remained. Execution 16:10 UTC: all 4 host-crontab lines removed (diff-verified, backup at /tmp/evidence/20260914-crawl4ai-retirement/crontab-before.txt); the 16:00 UTC run had already completed at 16:04:03Z before removal, so the corpus is complete through the final run. The full 92-day corpus (14 Jun - 14 Sep 2026: 3,384 data files + 32 curated briefs + 80 logs + pipeline scripts) was archived the same day to private repository github.com/ahmadfaurani/political-news-collection (initial commit f0548fd, final-run addendum committed post-retirement). Wrapper script carries a RETIRED banner with revival path (restore the 4 crontab lines); collector and generator scripts retained on disk. Extractor-patch (O1) and curated-series (O2) questions become moot. Supersedes the 'pipeline live' preservation note in DEC-20260914-002 with respect to the collection crontab only - the workspace-hoi directory itself remains a static archive."
strategic_significance: "Ends a 4x/day sensor whose readers walked away in July, converting ~108 files/day of unread accumulation into a governed, searchable 92-day corpus in a dedicated private repository. Preserves full revival capability at near-zero cost (4 crontab lines + sync script) should the Johor PRN watch or a new political-intelligence consumer re-activate."
mission_alignment:
  - mission/political-intelligence
related_records:
  - INIT-20260710-002
  - DEC-20260914-002
# === DECISION FIELDS [Structural] ===
context: "The crawl4ai political collection ran 4x/day (08/12/16/23 UTC) from a host crontab wrapper (deer-flow/heartbeat-crawl4ai.sh) into workspace-hoi/intelligence/raw/, collecting 25 Malaysian sources (EN+BM) with bias/reliability scoring, coalition and constituency extraction. Built 14 Jun 2026 (replacing a Firecrawl heartbeat), expanded 7 to 25 sources on 19-20 Jul for the PRN-Johor war-room and Voron campaign era. The 16:06 UTC purpose review found: sensor layer fully operational (final morning runs 25/25 sources), but the consumption chain decayed - PRN-Johor war-room last product 20 Jul, curated INTEL-06X brief series stopped 4 Aug (INTEL-065), entities/sentiment/narrative layers dormant since early August, and no systematic current consumer. The same day, the full corpus was already archived to the private repository political-news-collection at DAF direction."
decision: "Adopt P3 - retire the collection: remove all 4 crawl4ai crontab lines (with pre-change backup and post-change diff verification); treat the 16:04:03Z run as the final capture; designate github.com/ahmadfaurani/political-news-collection as the static corpus of record; mark the wrapper script with a RETIRED banner documenting the revival path; retain collector/generator scripts in place. Drop the dependent open items O1 (constituency extractor patch) and O2 (curated INTEL-06X series revival/retirement) as moot."
rationale: "A sensor nobody reads is spend without product: 108 files/day had been accumulating since the July consumption chain ended, with the only remaining consumers being ad-hoc queries and the archive itself. The 92-day corpus is now preserved in a structured, private, searchable repository, so retirement loses no data. Revival is deliberately cheap - the crontab backup, wrapper banner, and sync script keep reactivation a minutes-level operation - which makes the retirement low-regret even with Johor PRN 2026 still nominally active in the mission index."
alternatives_considered:
  - "(a) P1 - keep 4x/day with a named daily-digest consumer plus extractor fix - rejected for now: no current requirement justifies a new daily deliverable; can be revived under this option if a consumer emerges."
  - "(b) P2 - reduce to 08:00-only daily run - rejected: halves the spend but keeps unread accumulation; the archive already covers the historical need."
  - "(c) P4 - keep as-is with purpose logged - rejected: perpetuates spend without consumption."
confirmed_by: faurani-jaafar
confirmed_at: '2026-09-14T16:09:00+00:00'
---

# Context

The crawl4ai 25-source Malaysian political news collection ran 4x/day (08:00/12:00/16:00/23:00 UTC) via host crontab wrapper `deer-flow/heartbeat-crawl4ai.sh`, writing per-source JSON captures, collection/source manifests, and auto intelligence briefs to `workspace-hoi/intelligence/raw/` (3,350 files, 195MB at review time). Built 14 Jun 2026 to replace a Firecrawl heartbeat; expanded 7 to 25 sources on 19-20 Jul during the PRN-Johor war-room / Voron campaign era.

The 16:06 UTC purpose review found the sensor layer healthy but the consumption chain decayed: PRN-Johor war-room products stopped 20 Jul, curated INTEL-06X brief series stopped 4 Aug, downstream analysis layers dormant, no systematic consumer. Earlier the same day (15:54 UTC), DAF directed the full corpus be archived to a structured external GitHub repository, which was completed as `ahmadfaurani/political-news-collection` (private, commit f0548fd).

# Decision

DAF directed "P3" (retire collection). Executed 16:10 UTC:

- **Crontab:** all 4 crawl4ai lines removed; backup saved to `/tmp/evidence/20260914-crawl4ai-retirement/crontab-before.txt`; post-change diff verified clean (only crawl4ai lines removed, 7 unrelated lines remain).
- **Final run captured:** the 16:00 UTC scheduled run had completed at 16:04:03Z before removal - corpus complete through `2026-09-14T160403Z` (27 files, added to the archive repo post-retirement).
- **Corpus of record:** `github.com/ahmadfaurani/political-news-collection` (private) - 92 days, 14 Jun - 14 Sep 2026; README updated to mark the repository static with revival instructions.
- **Wrapper:** RETIRED banner added citing this decision, final-run timestamp, and the crontab backup path. Collector and brief-generator scripts retained on disk.
- **Moot items closed:** O1 (constituency extractor patch) and O2 (curated INTEL-06X series disposition) - both were consumption-layer concerns under a live pipeline.

# Rationale

The purpose review established that the pipeline's declared mission (political intelligence for the PRN war-room and campaign work) lost its consumers in July, leaving a healthy sensor feeding nobody. With the corpus fully archived at DAF direction the same day, retirement preserves all data while ending the accumulation of unread output. The revival path (restore 4 crontab lines; sync script ready) keeps the decision low-regret if the Johor PRN watch or another political-intelligence consumer re-activates.

# Alternatives Considered

- P1 (keep 4x/day + named daily-digest consumer + extractor fix) - rejected for now: no current requirement justifies a new daily deliverable.
- P2 (reduce to 08:00-only) - rejected: halves spend but keeps unread accumulation.
- P4 (keep as-is, log purpose) - rejected: perpetuates spend without consumption.

# Confirmation

DAF, Telegram direct, 14 September 2026 16:09 UTC ("P3").
