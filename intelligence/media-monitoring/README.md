# Claw Media Research — Malaysia Media Intelligence

**Classification:** TLP:AMBER — Internal Operational Use  
**Version:** 1.0  
**Created:** 2026-06-14  
**Owner:** HOI Intelligence Operations  
**Repository:** github.com/[ORG]/claw-media-research

---

## Overview

This repository contains comprehensive Malaysia media intelligence for political monitoring, sentiment analysis, and strategic communications planning. Built for the **Johor PRN-16** election monitoring workstream and expandable to national/federal elections (GE16).

---

## Repository Structure

```
claw-media-research/
├── README.md                              # This file
├── MALAYSIA-MEDIA-REGISTRY.md             # Master registry (70+ outlets)
├── MALAYSIA-CONTACTS.md                   # Contact directory
├── POLITICAL-SIGNAL-REGISTRY-EXPANSION.md # Expansion plan (32→70 sources)
├── SABAH-SARAWAK-RSS-FEEDS.md             # East Malaysia RSS discovery
├── OWNERSHIP-MAPPING.md                   # Corporate ownership structures
├── SOURCES/
│   ├── tier1-national.md                  # National mainstream outlets
│   ├── tier2-regional.md                  # Regional/state outlets
│   ├── tier3-digital.md                   # Digital-native outlets
│   └── tier4-community.md                 # Community/niche outlets
├── CONFIG/
│   ├── deerflow-sources.yaml              # DeerFlow integration config
│   ├── political-signal-schema.json       # 35-field signal schema
│   └── alert-thresholds.yaml              # Alert level configurations
├── RSS/
│   ├── working-feeds.md                   # Verified RSS feed URLs
│   └── feed-samples/                      # Sample RSS XML files
└── ARCHIVE/
    └── baseline-2026-06-13.md             # Original media landscape baseline
```

---

## Key Deliverables

### 1. Malaysia Media Registry (Master Document)

**File:** `MALAYSIA-MEDIA-REGISTRY.md`

- **70 total outlets** across 4 tiers
- **Language coverage:** Malay (45), English (25), Chinese (15), Tamil (5), Indigenous (8)
- **Regional coverage:** Peninsular (35), Sabah (12), Sarawak (15), National (25)
- **Ownership mapping:** Government, commercial conglomerates, independents

**Quick Stats:**
| Metric | Count |
|--------|-------|
| Tier 1 (National) | 27 |
| Tier 2 (Regional) | 23 |
| Tier 3 (Digital) | 12 |
| Tier 4 (Community) | 8 |
| **Total** | **70** |

---

### 2. Contact Directory

**File:** `MALAYSIA-CONTACTS.md`

- **35+ verified contacts** (corporate HQs, newsrooms, phone numbers)
- **Key personnel:** Directors, editors-in-chief, CEOs
- **Contact patterns:** Email formats, phone numbers, physical addresses
- **Privacy compliant:** Work emails only, no personal data

**Verified Contacts:**
| Outlet Group | Contacts Verified | Method |
|--------------|-------------------|--------|
| RTM | ✅ Director-General, HQ address | Official site |
| Media Prima | ✅ Contact form, corporate HQ | Official site |
| Astro | ✅ Corporate info, annual reports | Official site |
| Media Chinese Int'l | ✅ HQ addresses (MY + HK) | Official site |
| Malaysiakini | ✅ Address, email pattern | Official site + ContactOut |
| Borneo Post | ✅ Phone (Miri, KK), addresses | Official site |
| Malaysia Nanban | ✅ Phone (03-6251 5981) | Business directory |

---

### 3. Ownership Mapping

**File:** `OWNERSHIP-MAPPING.md`

**Major Ownership Clusters:**

#### Government-Owned
```
Government of Malaysia
└── Ministry of Communications
    ├── RTM (7 TV channels, 34 radio stations)
    ├── Bernama (national news agency)
    └── State Media (TV Sarawak, Borneo.TV, New Sabah Times)
```

#### Commercial Conglomerates
| Company | Key Assets | Reach | Ownership |
|---------|------------|-------|-----------|
| **Media Prima** | TV3, 8TV, TV9, NST, BH, Hot FM | National | Public (KLSE: MEDIA) |
| **Astro** | 50+ channels, 10 radio stations | 5.2M homes (64%) | Usaha Tegas Sdn Bhd |
| **Media Chinese Int'l** | Sin Chew, China Press, Nanyang | ~1M daily | Tiong Family (dual-listed) |
| **Star Media Group** | The Star | National | Genting Group (Lim Kok Thay) |
| **Karangkraf** | Sinar Harian | High circulation | Hussamuddin Yaacub |

#### Independent
| Outlet | Ownership Model | Funding |
|--------|-----------------|---------|
| **Malaysiakini** | Founders (60%) + MDIF (29%) + Staff (10%) | Subscriptions + Grants |
| **Free Malaysia Today** | Independent | Advertising |
| **The Vibes** | Independent | Advertising |
| **CodeBlue** | Code Blue Media | Crowdfunding + Grants |

---

### 4. Political Signal Registry Integration

**File:** `POLITICAL-SIGNAL-REGISTRY-EXPANSION.md`

**Current State:** 32 sources configured  
**Expanded Registry:** 70 sources (+38 new)

**10 Priority Intelligence Requirements (PIRs):**

| PIR | Focus | Threshold | Alert Level |
|-----|-------|-----------|-------------|
| PIR-1 | Cost-of-Living | ≥10 complaints + viral | HIGH |
| PIR-2 | Trust/Policy | Post-policy <50% negative | MEDIUM |
| PIR-3 | Regional Autonomy | ≥3 autonomy articles/day | MEDIUM |
| PIR-4 | Youth Sentiment | ≥5 anti-system threads/day | MEDIUM |
| PIR-5 | Stability | Snap election speculation | HIGH |
| PIR-6 | Reform Fatigue | ≥3 reform fatigue mentions | LOW |
| PIR-7 | Digital Sentiment | Anti-gov viral >10K | HIGH |
| PIR-8 | BERSAMA | Membership drive | LOW |
| PIR-9 | PH Pact | Seat negotiation leak | MEDIUM |
| PIR-10 | Sabah Defection | Defection cascade rumor | HIGH |

**Alert Levels:**
- 🔴 **CRITICAL:** ≤10 min response (coalition collapse)
- 🟠 **HIGH:** ≤1 hour response (viral >10K, defection)
- 🟡 **MEDIUM:** Daily log (≥3 autonomy articles/day)
- 🟢 **LOW:** Weekly log (routine PIR content)

---

### 5. East Malaysia RSS Discovery

**File:** `SABAH-SARAWAK-RSS-FEEDS.md`

**Working RSS Feeds (Verified):**

| Outlet | RSS URL | Status | Priority |
|--------|---------|--------|----------|
| **The Borneo Post** | https://www.theborneopost.com/feed/ | ✅ Active | CRITICAL |
| **See Hua Marketing** | https://www.seehuamarketing.com/feed/ | ✅ Active | HIGH |
| **TV Sarawak** | YouTube RSS (channel ID required) | ✅ Active | CRITICAL |

**Non-RSS Outlets (Scraping Required):**

| Outlet | Status | Alternative |
|--------|--------|-------------|
| Daily Express | ❌ 403 Forbidden | Web scrape homepage |
| Utusan Borneo | ❌ Drupal (no RSS) | Web scrape + section feeds |
| Borneo.TV | ❌ Streaming platform | Web scrape + YouTube |
| JohorKini | ❌ WordPress (feed disabled?) | Web scrape |

---

## Integration Status

### DeerFlow Configuration

**Deadline:** 2026-06-15 ✅  
**Config File:** `CONFIG/deerflow-sources.yaml`

```yaml
sources:
  # Tier 1 - National
  - name: "RTM News"
    url: "https://www.rtm.gov.my/contents/siaran-media"
    type: "scrape"
    language: "ms"
    tier: 1
    
  - name: "Media Prima"
    url: "https://www.mediaprima.com.my/"
    type: "scrape"
    language: "ms,en"
    tier: 1
    
  # Tier 2 - East Malaysia (RSS)
  - name: "The Borneo Post"
    url: "https://www.theborneopost.com/feed/"
    type: "rss"
    language: "en"
    region: "Sarawak,Sabah"
    tier: 2
    
  - name: "See Hua Marketing"
    url: "https://www.seehuamarketing.com/feed/"
    type: "rss"
    language: "zh"
    region: "Sarawak,Sabah,Brunei,Labuan"
    tier: 2
```

---

### Political Signal Schema

**Schema File:** `CONFIG/political-signal-schema.json`

**35 Core Fields across 9 categories:**

| Category | Fields | Purpose |
|----------|--------|---------|
| Identity | signal_id, timestamps, TLP, confidence | Unique ID + provenance |
| Source | name, tier, category, URL, language | Media outlet metadata |
| Content | headline, excerpt, hash, word_count | What was collected |
| PIR | primary, secondary, keywords_matched, relevance | Intelligence classification |
| Sentiment | polarity, score, archetype, velocity, engagement | Emotional analysis |
| Alert | level, threshold_breached, escalation_required | Response trigger |
| Entities | person, organization, location, event | Named entity extraction |
| Processing | agent, version, timestamp, analyst_reviewed | Audit trail |
| Metadata | language_detected, region, election_relevance | Additional context |

---

## Usage Guidelines

### For Intelligence Analysts

1. **Daily Monitoring:**
   - Check `SOURCES/tier1-national.md` for national sentiment
   - Review `SOURCES/tier2-regional.md` for East Malaysia developments
   - Monitor alert thresholds in `CONFIG/alert-thresholds.yaml`

2. **Weekly Synthesis:**
   - Aggregate signals from `memory/signals/` directory
   - Update PIR trends (WoW change)
   - Generate weekly brief for stakeholders

3. **Event-Driven Analysis:**
   - Escalate per alert thresholds (CRITICAL ≤10 min, HIGH ≤1 hour)
   - Cross-reference 3+ sources before escalation
   - Document in analyst notes

### For Engineers

1. **DeerFlow Integration:**
   - Use `CONFIG/deerflow-sources.yaml` for source configuration
   - Implement schema from `CONFIG/political-signal-schema.json`
   - Output to `memory/signals/YYYY/MM-DD-signals.jsonl`

2. **RSS Collection:**
   - Prioritize working feeds in `RSS/working-feeds.md`
   - Implement scraping for non-RSS outlets
   - Validate feed freshness daily

3. **Alert System:**
   - Configure thresholds per `CONFIG/alert-thresholds.yaml`
   - Route alerts to Telegram channel
   - Log all escalations for audit

---

## Classification & Handling

**TLP:AMBER** — Internal Operational Use

- ✅ **Permitted:** Internal team sharing, operational planning, stakeholder briefings
- ❌ **Prohibited:** External distribution, public posting, social media sharing

**Personal Data Handling:**
- ✅ Work emails, professional titles, public social handles
- ❌ Personal emails, private phones, home addresses, family info

**Retention:**
- Review and update quarterly
- Purge outdated contact information every 90 days
- Archive historical signals after 12 months

---

## Related Projects

- **Johor Political Monitoring:** `intelligence/johor-political/` (monitoring dashboard, sentiment tracker)
- **Political Signal Registry:** `memory/2026-06-13-political-signal-registry.md` (35-field schema)
- **Research Stack Media Registry:** `research-stack/modes/media-registry/` (workflow, runbook)
- **DeerFlow Assessment:** `workstreams/political-monitoring/02-analysis/deerflow-deployment-assessment.md`

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | 2026-06-14 | Initial repository creation | HOI Intelligence |
| 1.1 | 2026-06-15 | DeerFlow integration, RSS discovery | HOI Intelligence |

---

## Contact

**Repository Owner:** HOI Intelligence Operations  
**Classification:** TLP:AMBER  
**Last Updated:** 2026-06-15
