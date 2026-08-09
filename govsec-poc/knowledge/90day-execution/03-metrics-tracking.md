# KB-90DAY-004: Metrics Tracking — Revenue, POC, Conversion

**Knowledge Unit ID:** KB-90DAY-004  
**Version:** 1.0  
**Classification:** TLP:AMBER (Internal Operational)  
**Created:** 2026-04-25  
**Owner:** DAF (Commercial Lead)  
**Status:** Active — Daily Execution Guidance  

---

## Purpose

**Track revenue, POC deployment, conversion rates, and stakeholder satisfaction across the 90-day execution plan with daily/weekly visibility.**

---

## Revenue Metrics

### Target vs. Actual (Days 1-90)

| Phase | Timeline | Target Revenue | Actual Revenue | Variance | Status |
|-------|----------|----------------|----------------|----------|--------|
| **POC Phase** | Days 1-30 | RM 500K - RM 1M | RM 0 | -RM 500K-1M | 🔲 Not Started |
| **Deployment Phase** | Days 31-60 | RM 2M - RM 5M | RM 0 | -RM 2M-5M | 🔲 Not Started |
| **Scaling Phase** | Days 61-90 | RM 5M - RM 10M | RM 0 | -RM 5M-10M | 🔲 Not Started |
| **Total (Days 1-90)** | 90 days | RM 7.5M - RM 16M | RM 0 | -RM 7.5M-16M | 🔲 Not Started |

### Revenue by Solution Domain (Annual Target)

| Solution | Annual Target | POC Revenue | Deployment Revenue | Scaling Revenue | Total (90-Day) | Status |
|----------|---------------|-------------|--------------------|-----------------|----------------|--------|
| GovSec Threat Intelligence | RM 5M/year | RM 150K | RM 500K | RM 1M | RM 1.65M | 🔲 |
| Digital Risk Quantification GRC | RM 6M/year | RM 150K | RM 750K | RM 1.5M | RM 2.4M | 🔲 |
| Blockchain Intelligence | RM 5M/year | RM 100K | RM 500K | RM 1M | RM 1.6M | 🔲 |
| Unified Intelligence Platform | RM 5M/year | RM 100K | RM 500K | RM 1M | RM 1.6M | 🔲 |
| **Total** | **RM 21M/year** | **RM 500K** | **RM 2.25M** | **RM 4.5M** | **RM 7.25M** | 🔲 |

---

## POC Metrics

### POC Deployment Tracker

| POC # | Account | Solution | Start Date | End Date | Status | Detection Time | FP Rate | Triage Reduction |
|-------|---------|----------|------------|----------|--------|----------------|---------|------------------|
| **POC-001** | CSM | SpankRAT Detection | TBD | TBD | 🔲 Not Started | TBD | TBD | TBD |
| **POC-002** | MINDEF BSEP | LotL C2 Monitoring | TBD | TBD | 🔲 Not Started | TBD | TBD | TBD |
| **POC-003** | UPNM DWI | Training Module | TBD | TBD | 🔲 Not Started | TBD | TBD | TBD |
| **POC-004** | GLC (TBD) | Threat Intel Dashboard | TBD | TBD | 🔲 Not Started | TBD | TBD | TBD |
| **POC-005** | NACSA | CBOM Mapping | TBD | TBD | 🔲 Not Started | TBD | TBD | TBD |

### POC Success Criteria

| Metric | Target | Measurement Method |
|--------|--------|--------------------|
| **Detection Time** | <15 minutes (SpankRAT), <5 minutes (LotL C2) | Time from IOC arrival to alert |
| **False Positive Rate** | <5% | False alerts / Total alerts |
| **SOC Triage Reduction** | ≥30% | Manual triage time before vs. after |
| **Stakeholder Satisfaction** | ≥4/5 | Post-POC survey |
| **Conversion to Production** | ≥30% | POCs converted to paid contracts |

---

## Conversion Metrics

### POC-to-Contract Conversion Tracker

| POC # | Account | POC End Date | Contract Decision | Contract Value | Conversion Time | Status |
|-------|---------|--------------|-------------------|----------------|-----------------|--------|
| **POC-001** | CSM | TBD | Pending | TBD | TBD | 🔲 Not Started |
| **POC-002** | MINDEF BSEP | TBD | Pending | TBD | TBD | 🔲 Not Started |
| **POC-003** | UPNM DWI | TBD | Pending | TBD | TBD | 🔲 Not Started |
| **POC-004** | GLC (TBD) | TBD | Pending | TBD | TBD | 🔲 Not Started |
| **POC-005** | NACSA | TBD | Pending | TBD | TBD | 🔲 Not Started |

### Conversion Funnel

| Stage | Count | Conversion Rate | Target |
|-------|-------|-----------------|--------|
| **POCs Initiated** | 0 | — | 3-5 |
| **POCs Completed** | 0 | — | ≥3 |
| **Contracts Signed** | 0 | 0% | ≥30% |
| **Revenue Recognized** | RM 0 | — | RM 2M-5M |

---

## Stakeholder Satisfaction Metrics

### CSM Satisfaction Tracker

| Metric | Target | Measurement | Last Score | Trend |
|--------|--------|-------------|------------|-------|
| **Executive Alignment** | ≥4/5 | Post-meeting survey | N/A | ➡️ |
| **Technical Delivery** | ≥4/5 | Post-deployment survey | N/A | ➡️ |
| **Communication Timeliness** | ≥4/5 | Weekly check-in survey | N/A | ➡️ |
| **Overall Satisfaction** | ≥4/5 | 30-day/60-day/90-day review | N/A | ➡️ |

### MINDEF Satisfaction Tracker

| Metric | Target | Measurement | Last Score | Trend |
|--------|--------|-------------|------------|-------|
| **Technical Delivery** | ≥4/5 | Post-deployment survey | N/A | ➡️ |
| **Sovereign Deployment** | ≥4/5 | Air-gap validation | N/A | ➡️ |
| **Overall Satisfaction** | ≥4/5 | 30-day/60-day review | N/A | ➡️ |

---

## Weekly Reporting Cadence

| Day | Report | Audience | Owner |
|-----|--------|----------|-------|
| **Monday** | Week's priorities | Internal team | Hadri |
| **Wednesday** | Mid-week status check | DAF | Fuad |
| **Friday** | Weekly status report | DAF + CSM (Zulfeka) | Hadri |
| **Month-End** | Phase review | DAF + CSM Leadership | DAF |

---

## Dashboard Schema (GitHub / MCP Query)

**Weekly Status Dashboard:**

```json
{
  "week": "Week 1-2",
  "dates": "May 1-10, 2026",
  "revenue": {
    "target": "RM 500K",
    "actual": "RM 0",
    "variance": "-RM 500K"
  },
  "pocs": {
    "initiated": 0,
    "completed": 0,
    "target": 3
  },
  "conversion": {
    "rate": "0%",
    "target": "≥30%",
    "contracts_signed": 0
  },
  "satisfaction": {
    "csm": "N/A",
    "mindef": "N/A",
    "target": "≥4/5"
  },
  "risks": ["R-001", "R-003"],
  "blockers": ["1.1 Joint IP Framework"]
}
```

---

## Query Interface (MCP Tool Access)

```python
# Example: Query current revenue status
revenue = mcp.govsec.kb_query(unit_id="KB-90DAY-004", section="revenue")

# Example: Query POC status
pocs = mcp.govsec.kb_query(unit_id="KB-90DAY-004", section="pocs")

# Example: Query conversion rate
conversion = mcp.govsec.kb_query(unit_id="KB-90DAY-004", section="conversion")

# Example: Generate weekly dashboard
dashboard = mcp.govsec.metrics_dashboard(week="Week 1-2")
```

---

**Last Updated:** 2026-04-25 06:34 UTC  
**Next Review:** 2026-05-01 (Phase 1 Kickoff)  
**Retention Tier:** Operational (Active Daily Use)

#KB90Day
#Metrics
#Revenue
#POC
#Conversion
#GovSec
