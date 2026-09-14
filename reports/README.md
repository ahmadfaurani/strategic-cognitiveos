# Reports Directory Structure

## Purpose
Centralized repository for all analytical reports, intelligence briefs, and strategic documents organized by reporting cadence.

## Structure

```
reports/
├── README.md                    # This file
├── daily/                       # Daily operational reports
│   ├── 2026-06/
│   │   ├── 2026-06-10-daily-intel-sync.md
│   │   └── ...
│   └── 2026-05/
├── weekly/                      # Weekly synthesis reports
│   ├── 2026-W24/
│   │   ├── weekly-synthesis-2026-06-14.md
│   │   └── ...
│   └── 2026-W23/
├── monthly/                     # Monthly strategic reports
│   ├── 2026-06/
│   │   ├── monthly-strategic-review-2026-06.md
│   │   └── ...
│   └── 2026-05/
├── ad-hoc/                      # Special analytical reports
│   ├── johor-political/
│   │   ├── onn-hafiz-network-analysis-2026-06-10.md
│   │   └── ...
│   ├── ai-infrastructure/
│   └── threat-intelligence/
└── archives/                    # Historical reports (quarterly+)
    ├── 2026-Q2/
    └── 2026-Q1/
```

## Reporting Cadence

### Daily Reports (`daily/`)
- **When:** Every heartbeat cycle (4-8 hours)
- **Content:**
  - AI infrastructure CVE monitoring
  - GitHub engagement sync
  - Political intelligence updates (PRN-16)
  - Stakeholder registry changes
- **Format:** `YYYY-MM-DD-daily-intel-sync.md`

### Weekly Reports (`weekly/`)
- **When:** Every Sunday 09:00 UTC
- **Content:**
  - Workstream synthesis
  - Intelligence collection summary
  - AVR/Threat Registry updates
  - CVE trend analysis
  - Election monitoring (PRN-16 scenarios)
- **Format:** `weekly-synthesis-YYYY-MM-DD.md` (ISO week directory: `2026-WXX/`)

### Monthly Reports (`monthly/`)
- **When:** Last day of each month
- **Content:**
  - Strategic review
  - Threat landscape assessment
  - Product/portfolio performance
  - Stakeholder engagement summary
  - Resource allocation recommendations
- **Format:** `monthly-strategic-review-YYYY-MM.md`

### Ad-Hoc Reports (`ad-hoc/`)
- **When:** As needed for specific analytical requirements
- **Content:**
  - Network analysis (e.g., Onn Hafiz associates)
  - Threat actor profiles
  - Technology assessments
  - Election risk analysis
- **Format:** `{topic}-{description}-{YYYY-MM-DD}.md`
- **Subdirectories:** Organized by subject matter

### Archives (`archives/`)
- **When:** Quarterly consolidation
- **Content:**
  - Historical reports moved after 90 days
  - Quarterly synthesis documents
  - Year-end strategic reviews
- **Format:** `YYYY-QX/` directories

## Classification Markings

All reports MUST include classification marking in header:

```markdown
**Classification:** TLP:AMBER (or TLP:GREEN/TLP:RED)
**Distribution:** Internal Only / Stakeholder-Specific
```

## Cross-References

- **Source Data:** `/intelligence/` directory
- **Memory Files:** `/memory/YYYY-MM-DD.md`
- **Attack Vector Registry:** `/attack-vector-registry/`
- **Engagements:** `/engagements/`

## Maintenance

- **Daily:** Heartbeat sync creates/updates `daily/` reports
- **Weekly:** Sunday synthesis creates `weekly/` reports
- **Monthly:** Last day of month creates `monthly/` reports
- **Quarterly:** Archive old reports to `archives/`

---

**Owner:** Ember (agent-main)  
**Last Updated:** 2026-09-14  
**Next Review:** 2026-10-14
