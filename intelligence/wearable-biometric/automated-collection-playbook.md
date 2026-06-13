# Automated Collection Playbook
## Wearable Biometric Intelligence

**Document ID:** AUTO-COLLECT-001  
**Classification:** TLP:AMBER  
**Effective Date:** 2026-06-06  
**Integration:** Heartbeat Sync (every 4-8 hours)

---

## Overview

This playbook defines automated collection workflows that run at every heartbeat cycle. All collection is **read-only** (no external action without approval).

---

## Automated Workflow 1: OSINT Media Monitoring

**Trigger:** Every heartbeat (4-8 hours)

**Query Set:**
```
1. "NameTag" + (Meta OR "smart glasses" OR "facial recognition")
2. "Meta" + "facial recognition" + "smart glasses" + 2026
3. "Ray-Ban Meta" + "biometric" OR "NameTag"
4. "Oakley smart glasses" + "facial recognition"
5. "wearable facial recognition" + (activation OR launch OR privacy)
```

**Sources:**
- Google News
- Twitter/X (advanced search)
- Reddit (r/privacy, r/technology, r/Meta)
- TechCrunch, WIRED, The Verge, Ars Technica
- Privacy advocacy blogs (EFF, ACLU, EPIC)

**Action:**
- If new mention found → Create collection item in `collection/OSINT/`
- Format: `NNN-source-brief-description.md`
- Tag with confidence level and key claims
- Notify analyst via email if >5 mentions in 24h

**Escalation:**
- **CRITICAL:** Major publication confirms activation → Telegram alert
- **HIGH:** Regulatory inquiry announced → Email analyst + legal

---

## Automated Workflow 2: Meta Channel Monitoring

**Trigger:** Every heartbeat (4-8 hours)

**Channels:**
- Meta Newsroom (news.meta.com)
- Mark Zuckerberg posts (Facebook, Twitter/X)
- Andrew Bosworth posts (Twitter/X)
- Meta AI blog
- Meta Developer blog
- SEC EDGAR (Meta filings)

**Action:**
- Check for new posts since last sync
- Search for keywords: "NameTag", "facial recognition", "biometric", "smart glasses", "Ray-Ban"
- If found → Screenshot + archive + create collection item
- Analyze sentiment (defensive, reassuring, silent)

**Escalation:**
- **CRITICAL:** Official announcement of activation → Telegram alert + Flash Alert initiation
- **HIGH:** Acknowledgment of NameTag existence → Email analyst
- **MEDIUM:** General AI wearable statement → Log to Weekly Synthesis

---

## Automated Workflow 3: App Store Monitoring

**Trigger:** Every heartbeat (4-8 hours)

**Targets:**
- Apple App Store: Meta AI app
- Google Play Store: Meta AI app
- APKMirror: Historical versions

**Data Points:**
- Current version number
- Version history (last 10 versions)
- Update notes (keywords: "recognition", "biometric", "identity", "face")
- Permission changes
- Download count (if available)
- User reviews (keywords: "face", "recognition", "privacy", "camera")

**Action:**
- If new version detected → Download APK/IPA for analysis
- Compare version notes to previous
- Flag permission changes
- Create TECHINT collection item if changes detected

**Escalation:**
- **HIGH:** New permissions (camera background, biometric) → Email analyst
- **MEDIUM:** Version update with vague notes → Log to Weekly Synthesis

---

## Automated Workflow 4: Regulatory Filing Monitor

**Trigger:** Every heartbeat (4-8 hours)

**Sources:**
- FTC.gov (press releases, enforcement actions)
- EDPS.europa.eu (statements, opinions)
- ICO.org.uk (guidance, enforcement)
- CNIL.fr (French DPA)
- Garante Privacy (Italian DPA)
- CourtListener (BIPA litigation search)
- PACER (federal court filings)

**Query Set:**
```
1. "Meta" + "facial recognition" + (inquiry OR investigation OR enforcement)
2. "NameTag" + (FTC OR EDPS OR ICO)
3. "BIPA" + "Meta" + (complaint OR lawsuit OR class action)
4. "AI Act" + "facial recognition" + (guidance OR enforcement)
5. "smart glasses" + (privacy OR biometric) + regulator
```

**Action:**
- If filing found → Download PDF + create REGINT collection item
- Extract key dates, deadlines, requirements
- Cross-reference with existing timeline
- Notify legal team

**Escalation:**
- **CRITICAL:** Formal investigation announced → Telegram alert + Policy Brief initiation
- **HIGH:** Warning letter or inquiry → Email analyst + legal
- **MEDIUM:** General guidance mentioning FR → Log to Weekly Synthesis

---

## Automated Workflow 5: Patent Database Monitor

**Trigger:** Daily (09:00 UTC)

**Sources:**
- USPTO.gov (patent applications, grants)
- WIPO.int (PCT applications)
- Google Patents

**Query Set:**
```
1. "Meta" + "facial recognition" + "wearable"
2. "NameTag" + (Meta OR Facebook)
3. "Smart glasses" + "biometric" + (Meta OR Facebook)
4. "Faceprint" + "local storage" + (Meta OR Facebook)
5. "Wearable" + "identity recognition" + (Meta OR Facebook)
```

**Action:**
- If new filing found → Download PDF + add to `artifacts/documents/`
- Extract filing date, inventors, claims
- Analyze technical details
- Update timeline if filing date is significant

**Escalation:**
- **MEDIUM:** New NameTag-specific patent → Email analyst
- **LOW:** General wearable FR patent → Log to Monthly Technical Deep-Dive

---

## Automated Workflow 6: Advocate Statement Monitor

**Trigger:** Every heartbeat (4-8 hours)

**Sources:**
- EFF.org (Deep Links blog, press releases)
- ACLU.org (press releases, blog)
- EPIC.org (alerts, filings)
- PrivacyInternational.org
- AccessNow.org

**Query Set:**
```
1. "Meta" + "NameTag" + (statement OR response OR analysis)
2. "smart glasses" + "facial recognition" + (EFF OR ACLU OR EPIC)
3. "wearable biometric" + (advocacy OR campaign)
```

**Action:**
- If statement found → Screenshot + archive + create OSINT collection item
- Extract key arguments, recommendations, calls to action
- Cross-reference with regulatory filings (amicus briefs, etc.)
- Track advocate coalition growth

**Escalation:**
- **HIGH:** Formal complaint filed by advocate group → Email analyst + legal
- **MEDIUM:** Public statement or blog post → Log to Weekly Synthesis
- **LOW:** Social media mention → Log to collection item

---

## Automated Workflow 7: Technical Indicator Collection

**Trigger:** Every heartbeat (4-8 hours)

**Indicators to Monitor:**
- Meta AI app network traffic (new endpoints)
- GitHub repositories (Meta open-source FR projects)
- Security researcher blogs (technical analysis)
- Conference presentations (CVPR, ICCV, USENIX Security)
- Academic papers (arXiv, IEEE, ACM)

**Action:**
- If new IOC found → Create TECHINT collection item
- Update IOCs in `collection/TECHINT/`
- Cross-reference with existing architecture analysis
- Flag for detection rule development

**Escalation:**
- **HIGH:** New cloud sync endpoint discovered → Email analyst + security
- **MEDIUM:** Researcher publishes technical analysis → Log to Weekly Synthesis
- **LOW:** Academic paper on wearable FR → Log to Monthly Technical Deep-Dive

---

## Automated Workflow 8: Abuse Incident Tracker

**Trigger:** Every heartbeat (4-8 hours)

**Sources:**
- News media (local + national)
- Social media (Twitter/X, Reddit)
- Law enforcement press releases
- Privacy advocacy incident reports
- Court filings (restraining orders, criminal cases)

**Query Set:**
```
1. "smart glasses" + (stalking OR harassment OR "facial recognition")
2. "Ray-Ban Meta" + (abuse OR misuse OR "privacy violation")
3. "wearable camera" + (arrest OR complaint OR lawsuit)
4. "facial recognition" + (stalking OR doxxing) + 2026
```

**Action:**
- If incident found → Create OSINT collection item
- Extract: date, location, perpetrator, victim, outcome
- Assess if NameTag-specific or general smart glasses abuse
- Track incident count over time

**Escalation:**
- **CRITICAL:** NameTag-specific abuse confirmed → Telegram alert + Technical Advisory
- **HIGH:** Smart glasses abuse with FR element → Email analyst
- **MEDIUM:** General smart glasses privacy complaint → Log to Weekly Synthesis

---

## Collection Item Creation Standard

All automated collection items must follow this format:

```markdown
# Collection Item: [Brief Title]

**Collection ID:** [DISCIPLINE]-2026-[NNN]
**Date Collected:** [YYYY-MM-DD HH:MM UTC]
**Source Type:** [News / Social Media / Regulatory / Technical / etc.]
**Reliability:** [A/B/C/D/F]
**Classification:** TLP:AMBER
**Automated:** Yes ([Workflow Name])

---

## Source Metadata
- **Publication/Platform:** [Name]
- **Author:** [If available]
- **URL:** [Link]
- **Archive Link:** [Archive.is / Wayback Machine]
- **Screenshot:** `../artifacts/screenshots/[filename].png`

---

## Summary
[2-3 paragraph summary of key content]

---

## Key Claims
| Claim | Confidence | Quote/Evidence |
|-------|------------|----------------|
| [Claim 1] | [HIGH/MED/LOW] | "[Direct quote]" |

---

## Relevance to NameTag
[Explain how this relates to NameTag threat landscape]

---

## Follow-Up Required
- [ ] Analyst review
- [ ] Technical validation
- [ ] Legal assessment
- [ ] Cross-reference with [related item]

---

**Collector:** Automated (Heartbeat Sync)  
**Reviewer:** [Pending]  
**Status:** ACTIVE
```

---

## Heartbeat Integration Checklist

At each heartbeat cycle:

- [ ] Run OSINT Media Monitoring (Workflow 1)
- [ ] Run Meta Channel Monitoring (Workflow 2)
- [ ] Run App Store Monitoring (Workflow 3)
- [ ] Run Regulatory Filing Monitor (Workflow 4)
- [ ] Run Advocate Statement Monitor (Workflow 6)
- [ ] Run Technical Indicator Collection (Workflow 7)
- [ ] Run Abuse Incident Tracker (Workflow 8)
- [ ] Patent Monitor (Workflow 5) — if daily 09:00 UTC cycle
- [ ] Update heartbeat sync template in daily memory
- [ ] Flag any escalations required
- [ ] Log completion timestamp

---

## Error Handling

| Error Type | Response |
|------------|----------|
| **Source unavailable** | Log error, retry next cycle, notify if >3 cycles |
| **Rate limit hit** | Back off 1 hour, log, continue other workflows |
| **False positive** | Mark collection item as "Low relevance", continue |
| **Duplicate detection** | Skip, log as "Previously collected" |
| **Escalation channel down** | Fallback to email, log error |

---

## Performance Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| **Collection Coverage** | 100% of workflows per heartbeat | Heartbeat sync log |
| **False Positive Rate** | <20% of collection items | Analyst review |
| **Escalation Timeliness** | 100% within SLA | Timestamp comparison |
| **Source Uptime** | >95% availability | Error log |

---

**Document Owner:** AI Threat Intelligence Unit  
**Next Review:** 2026-07-06 (Monthly)  
**Classification:** TLP:AMBER
