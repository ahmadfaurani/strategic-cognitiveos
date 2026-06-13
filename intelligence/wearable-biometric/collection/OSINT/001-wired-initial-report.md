# Collection Item: WIRED Initial Report

**Collection ID:** OSINT-2026-001  
**Date Collected:** 2026-06-06  
**Source Type:** News Media (Technology)  
**Reliability:** B (Reliable indirect source)  
**Classification:** TLP:AMBER  

---

## Source Metadata

| Field | Value |
|-------|-------|
| **Publication** | WIRED |
| **Title** | "Meta Has Been Testing Facial Recognition in Its Smart Glasses" |
| **Author** | [To be extracted] |
| **Publication Date** | [To be extracted] |
| **URL** | [To be added] |
| **Archive Link** | [To be added] |
| **Screenshot** | `../artifacts/screenshots/wired-report-[date].png` |

---

## Key Claims

| Claim ID | Statement | Confidence | Source Quote |
|----------|-----------|------------|--------------|
| **C-001** | Meta embedded dormant facial recognition components called "NameTag" in Meta AI app | HIGH | Direct statement |
| **C-002** | Feature is not active for users today | HIGH | Direct statement |
| **C-003** | Core technical components present in shipped app builds as early as January 2026 | HIGH | Direct statement |
| **C-004** | Meta AI app downloaded over 50 million times | MEDIUM | Reported figure |
| **C-005** | EFF researcher described code as "nearly ready to go" | HIGH | Attributed quote |
| **C-006** | Faceprints stored on user's phone, not central database | MEDIUM | Reported architecture |
| **C-007** | Database configured to receive updates from Meta | HIGH | Technical finding |
| **C-008** | Feature would identify people captured by glasses camera | HIGH | Direct statement |

---

## Technical Details Extracted

| Component | Detail | Confidence |
|-----------|--------|------------|
| **Feature Name** | NameTag (internal codename) | HIGH |
| **Product Surface** | Meta AI app for Ray-Ban / Oakley smart glasses | HIGH |
| **Processing Location** | On-device (phone) | MEDIUM |
| **Biometric Type** | Faceprints (numerical embeddings) | HIGH |
| **Match Notification** | Alert wearer when known person recognized | HIGH |
| **Update Mechanism** | Cloud-to-device sync capability | HIGH |

---

## Entities Mentioned

| Entity | Type | Role |
|--------|------|------|
| Meta | Corporation | Feature developer |
| WIRED | Media | Reporting organization |
| EFF | Advocacy | Technical analysis provider |
| Ray-Ban | Brand | Smart glasses manufacturer (Meta partnership) |
| Oakley | Brand | Smart glasses manufacturer (Meta partnership) |
| Meta AI | Product | Companion app platform |

---

## Gaps & Follow-Ups

| Question | Priority | Status | Notes |
|----------|----------|--------|-------|
| Exact publication date? | HIGH | PENDING | Need to verify |
| Author name and credentials? | MEDIUM | PENDING | Assess expertise |
| Technical methodology for code review? | HIGH | PENDING | How was code analyzed? |
| EFF researcher name? | HIGH | PENDING | Follow up with EFF |
| App version containing NameTag? | HIGH | PENDING | Need version number |
| Specific code paths identified? | MEDIUM | PENDING | Feature flags, class names |
| Meta's response to WIRED? | HIGH | PENDING | Official statement needed |

---

## Cross-References

| Related Collection | Relationship |
|-------------------|--------------|
| TECHINT-2026-001 | App binary analysis |
| REGINT-2026-001 | Regulatory response tracking |
| OSINT-2026-002 | Follow-up media coverage |

---

## Analyst Notes

- This is the primary source document for the NameTag disclosure
- Claims are specific and technical, suggesting genuine code review
- EFF attribution adds credibility (technical expertise)
- "Dormant but nearly ready" is a critical framing - not vaporware
- 50M download figure makes this a scale issue, not niche R&D
- Follow up needed: Obtain full article text, screenshots, technical appendix

---

**Collection Timestamp:** 2026-06-06 03:00 UTC  
**Collector:** AI Threat Intelligence Unit  
**Status:** ACTIVE - Requires follow-up
