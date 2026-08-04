# CVS Source Register — Master

**Classification:** TLP:AMBER  
**Created:** 2026-08-04  
**Re-assessment:** Monthly (source upgrades/downgrades based on accuracy track record)

---

## Universal Source Hierarchy

### Level 1 — Official / System-of-Record (Highest Trust)

| Source | Domain | Access | Notes |
|--------|--------|--------|-------|
| SPR (Suruhanjaya Pilihan Raya) | Election | Public (spr.gov.my) | Candidate lists, results, election writ |
| Election Commission | Election | Public | Official election data |
| Registrar of Societies | Legal/ROS | Public | Party registration, office bearers |
| Government gazettes | Legal | Public | Official legal notices |
| Parliament records | Legislative | Public | Hansard, official statements |
| PDRM official statements | Law enforcement | Public/press release | Official police positions |
| Regulated filings (SSM, BNM, SC) | Corporate/Finance | Public/paid | Company filings, regulatory submissions |

### Level 2 — Internal Approved / Validated

| Source | Domain | Access | Notes |
|--------|--------|--------|-------|
| Aras internal reports | All | Internal | Approved reports, validated databases |
| Strategic CognitiveOS records | Strategic | Internal | STK/INIT/OPP/INT records, PIR inventory |
| Meeting minutes | All | Internal | Documented meetings, audit logs |
| VoronDRQ canonical database | Commercial | Internal | prospect-database-canonical.csv |
| Malaysia Journalist Registry | Media | Internal | Verified journalist contacts (TLP:AMBER) |

### Level 3 — Direct Stakeholder Confirmation

| Source | Domain | Access | Notes |
|--------|--------|--------|-------|
| Email trails | All | Internal | Direct stakeholder communication |
| Documented interviews | All | Internal | Recorded interviews with attribution |
| Contractor/vendor confirmations | Commercial | Internal | Direct vendor confirmation |

### Level 4 — Secondary Reports / Media

#### Tier B — Major Malaysian Mainstream Media

| Source | Language | URL | Notes |
|--------|----------|-----|-------|
| Sinar Harian | BM | sinarharian.com.my | High circulation, statewide coverage |
| The Star | EN | thestar.com.my | Major English daily |
| NST | EN | nst.com.my | English daily, political coverage |
| Astro Awani | BM/EN | astroawani.com | 24/7 news, TV + online |
| Bernama | BM/EN | bernama.com | National news agency |
| Utusan Malaysia | BM | utusan.com.my | Malay daily |
| Berita Harian | BM | bharian.com.my | Malay daily, high rural penetration |
| Kosmo! | BM | kosmo.com.my | Malay tabloid |
| mStar | BM | mstar.com.my | Malay online portal |

#### Tier C — Independent / Alternative Media

| Source | Language | URL | Notes |
|--------|----------|-----|-------|
| Malaysiakini | EN/BM | malaysiakini.com | Independent, paywall on some content |
| Free Malaysia Today | EN | freemalaysiatoday.com | Independent, free access |
| MalaysiaNow | EN/BM | malaysianow.com | Independent |
| OhBulan | BM | ohbulan.com | Malay political blog/portal |

#### Tier D — Social Media (Verified Accounts)

| Platform | Type | Notes |
|----------|------|-------|
| Verified politician accounts | Twitter/FB/IG | T2 for statements made by the person |
| Party official accounts | FB/IG/Twitter | T2 for announcements |

### Level 5 — Informal / AI-Generated (Not Accepted as Factual Without Validation)

| Source | Domain | Treatment |
|--------|--------|-----------|
| Unverified social media | All | T6 unless corroborated by L4 or above |
| WhatsApp forwards | All | T6 — logged for trend tracking only |
| Anonymous blog posts | All | T6 unless corroborated |
| AI-generated summaries/classifications | All | Max T2, max score 7. Mandatory human review (Rule 6) |
| OSINT aggregates (untraced) | All | T6 unless independently traced to L1-L3 |

---

## Source Attribution Format

Every intelligence product must cite sources using:

```
**Source:** [Source Name], [URL], [Date accessed]
```

Example:
```
**Source:** Sinar Harian, https://www.sinarharian.com.my/article/xxx, 18 Jul 2026
```

For non-URL sources:
```
**Source:** [Source Name], [Document type], [Date]
```

---

## Domain-Specific Source Sections

Each workspace maintains additional domain-specific sources in its local `CVS-SOURCE-REGISTER.md`. See workspace adapter files for details.

---

**Master Document Location:** `/home/p62operator/.openclaw/workspace/03-VERIFICATION/CVS-SOURCE-REGISTER.md`  
**Classification:** TLP:AMBER
