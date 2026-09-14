# Heartbeat Integration: DPI LLM Profiling

**Version:** 1.0  
**Date:** 2026-05-26  
**Related:** `HEARTBEAT.md`, `workstreams/09-hoi-intelligence/agents/README.md`

---

## Purpose

Integrate DPI LLM Profiling alerts into the HOI Intelligence heartbeat cycle for continuous monitoring, automated analysis, and stakeholder reporting.

---

## Heartbeat Cadence

| Check Type | Cadence | Priority | Agent |
|------------|---------|----------|-------|
| **DPI Alert Scan** | Every heartbeat (4-8 hours) | HIGH | AVR Collector |
| **New Case Detection** | Every heartbeat | HIGH | Intel Analyst |
| **Traffic Profile Analysis** | On new case detected | HIGH | Intel Analyst |
| **Report Generation** | Daily (23:00 UTC) | MEDIUM | Report Generator |
| **Stakeholder Sync** | Daily (23:00 UTC) | MEDIUM | GitHub Sync |

---

## Agent Roles

### AVR Collector

**Task:** Scan for new DPI alerts + CVE correlation

**Input:**
- SIEM alert feed (Elasticsearch/Splunk query)
- Detection rule triggers (`periodic_beaconing`, `abnormal_egress`, etc.)

**Output:**
- New case files (`endpoints/<entity-id>.md`)
- IOC extraction (`iocs/indicators.md`)
- CVE correlation (if malware detected)

**Query Example:**
```json
GET /zeek-logs-*/_search
{
  "query": {
    "bool": {
      "must": [
        { "term": { "detection_rule": "periodic_beaconing" }},
        { "range": { "@timestamp": { "gte": "now-8h" }}}
      ]
    }
  },
  "size": 100
}
```

**Confidence Threshold:** ≥0.6 for case creation

---

### Intel Analyst

**Task:** Behavioral profiling + threat hypothesis generation

**Input:**
- New case files from AVR Collector
- Flow metadata (session count, egress ratio, interval, etc.)
- Threat intel feeds (OTX, VirusTotal, MISP)

**Output:**
- Traffic profile analysis (`analysis/<entity-id>.md`)
- Threat hypothesis ranking (H1-H5)
- Destination reputation report

**Analysis Steps:**
1. Extract behavioral IOCs (interval, ratio, volume)
2. Query reputation APIs (VT, OTX)
3. Generate hypothesis table (confidence-scored)
4. Recommend next actions (isolate, forensics, interview)

**Confidence Threshold:** ≥0.7 for intel attribution

---

### Report Generator

**Task:** Draft TLP-classified stakeholder reports

**Input:**
- Case files (`endpoints/*.md`)
- Analysis reports (`analysis/*.md`)
- IOC files (`iocs/indicators.md`)

**Output:**
- Initial assessment (`reports/initial-assessment-<id>.md`)
- Daily summary (TLP:AMBER brief)
- Escalation alerts (if CRITICAL)

**Report Types:**

| Report | Audience | Classification | Frequency |
|--------|----------|----------------|-----------|
| **Initial Assessment** | SOC Lead, Intel | TLP:AMBER | Per case |
| **Daily Summary** | CSM, SOC | TLP:AMBER | Daily (23:00 UTC) |
| **Escalation Alert** | CISO, Executive | TLP:AMBER/RED | Immediate (CRITICAL only) |
| **Weekly Synthesis** | Stakeholders | TLP:AMBER | Weekly (Sunday 09:00 UTC) |

---

### GitHub Sync

**Task:** Sync case status to GitHub repository

**Repository:** `https://github.com/ahmadfaurani/hoi-intelligence-ops`

**Sync Tasks:**
1. Create GitHub Issue for new CRITICAL/HIGH cases
2. Update issue status (Analysis → Contained → Closed)
3. Attach reports (PDF/Markdown)
4. Comment with IOC updates

**Automation Boundary:**
- No auto-close (requires analyst approval)
- No TLP:RED content (manual review required)
- Commit messages sanitized (no sensitive details)

---

## Escalation Logic

### Confidence-Based Escalation

| Confidence | Severity | Action | SLA |
|------------|----------|--------|-----|
| **≥0.8** | CRITICAL | Immediate Telegram alert + endpoint isolation | <15 min |
| **0.6-0.79** | HIGH | Email alert + analyst review | <1 hour |
| **0.4-0.59** | MEDIUM | Daily brief | <24 hours |
| **<0.4** | LOW | Log only | Weekly review |

### Rule-Based Escalation

| Detection Rule | Default Severity | Escalation Trigger |
|----------------|------------------|--------------------|
| `periodic_beaconing` | HIGH | +1 if session count >500 |
| `abnormal_egress` | HIGH | +1 if ratio >100:1 |
| `rare_destination` | MEDIUM | +1 if VT score ≥5/100 |
| `llm_api_endpoint` | CRITICAL | Immediate (no escalation needed) |

### Multi-Endpoint Escalation

**If same destination/domain detected on 5+ endpoints:**
- Escalate to CRITICAL (regardless of individual confidence)
- Activate enterprise-wide threat hunt
- Notify CISO + stakeholder brief

---

## Heartbeat Workflow

### Parallel Execution (Every Heartbeat)

```
┌─────────────────────────────────────────────────────────────┐
│                    HEARTBEAT TRIGGER                        │
└─────────────────────────────────────────────────────────────┘
                            │
            ┌───────────────┼───────────────┐
            │               │               │
            ▼               ▼               ▼
    ┌───────────────┐ ┌───────────────┐ ┌───────────────┐
    │ AVR Collector │ │ Intel Analyst │ │ GitHub Sync   │
    │ (Scan SIEM)   │ │ (Profile New) │ │ (Sync Cases)  │
    └───────┬───────┘ └───────┬───────┘ └───────┬───────┘
            │               │               │
            └───────────────┼───────────────┘
                            │
                            ▼
                  ┌───────────────────┐
                  │ Report Generator  │
                  │ (Daily Summary)   │
                  └─────────┬─────────┘
                            │
                            ▼
                  ┌───────────────────┐
                  │ Memory Update     │
                  │ (YYYY-MM-DD.md)   │
                  └───────────────────┘
```

**Expected Duration:** 5-10 minutes (parallel execution)

---

## Output Artifacts

### Daily Memory Update

**Location:** `memory/YYYY-MM-DD.md`

**Format:**
```markdown
### DPI LLM Profiling (HH:MM UTC)
| Metric | Value |
|--------|-------|
| New Cases (24h) | N |
| Active Cases | N |
| Closed Cases (24h) | N |
| CRITICAL Alerts | N |
| HIGH Alerts | N |

**New Cases:** <list>
**Escalations:** <list>
**Pending Actions:** <list>
```

### GitHub Issue Template

```markdown
## [DPI-XXX] <Brief Description>

**Severity:** HIGH/CRITICAL  
**Endpoint:** <IP/hostname>  
**Destination:** <domain/IP>  
**Detection Rules:** <list>  
**Status:** Analysis/Contained/Closed  

### Summary
<2-3 sentence overview>

### IOCs
- <IOC 1>
- <IOC 2>

### Actions Taken
- [ ] <Action 1>
- [ ] <Action 2>

### Classification
TLP:AMBER
```

### Telegram Alert (CRITICAL Only)

```
🚨 [CRITICAL] DPI LLM Profiling Alert

Case: DPI-XXX
Endpoint: <IP>
Destination: <domain>
Confidence: 0.XX
Action: <Isolation/Analysis/etc.>

Details: <1-sentence summary>
Report: <GitHub link>
```

---

## Governance Boundaries

| Boundary | Rule | Enforcement |
|----------|------|-------------|
| **TLP Classification** | No auto-push for TLP:AMBER+ | Human review required |
| **Endpoint Isolation** | Requires SOC Lead approval | Manual action |
| **Stakeholder Outreach** | No auto-contact (CSM/executives) | Human approval |
| **Confidence Thresholds** | ≥0.6 AVR, ≥0.7 intel, ≥0.8 POC | Agent logic enforced |
| **Data Retention** | 90 days raw, 1 year metadata | Automated lifecycle |

---

## Integration with Existing Heartbeat

### Current Heartbeat Agents (from `HEARTBEAT.md`)

| Agent | Current Task | DPI Integration |
|-------|--------------|-----------------|
| **GitHub Sync** | cbo-01 + hoi-intelligence-ops | Add DPI case sync |
| **AVR Collector** | CVE monitoring | Add DPI alert scan |
| **Stakeholder Logger** | Contact registry | Add DPI stakeholder notifications |
| **CDT Discovery** | Critical Delivery Tasks | Add DPI-related CDTs |

### New Agent: DPI Scanner

**Purpose:** Dedicated DPI alert monitoring

**Tasks:**
1. Query SIEM for new DPI alerts
2. Extract metadata (endpoint, destination, metrics)
3. Create case file if confidence ≥0.6
4. Trigger Intel Analyst for profiling

**Status:** 🟡 Pending (to be added to heartbeat roster)

---

## Metrics & KPIs

| Metric | Target | Measurement |
|--------|--------|-------------|
| **Detection Latency** | <15 minutes (CRITICAL) | Alert → Case creation |
| **Analysis SLA** | <4 hours (HIGH) | Case → Initial assessment |
| **False Positive Rate** | <10% | Closed cases / Total cases |
| **Escalation Accuracy** | ≥95% | Correct severity assignment |
| **Heartbeat Coverage** | 100% (no missed cycles) | Successful heartbeat / Total |

---

## Testing & Validation

### Test Scenarios

| Scenario | Expected Outcome |
|----------|------------------|
| **Simulated beaconing** (lab) | Case created, confidence ≥0.8 |
| **Known LLM domain** | Immediate CRITICAL escalation |
| **False positive** (legitimate backup) | Classified LOW, whitelisted |
| **Multi-endpoint detection** | Enterprise hunt triggered |

### Validation Cadence

- **Weekly:** Review false positives, tune detection rules
- **Monthly:** Test heartbeat agents (simulate alerts)
- **Quarterly:** Full tabletop exercise (CRITICAL scenario)

---

**Owner:** Rook  
**Next Review:** 2026-06-09 (bi-weekly cycle)  
**Approval:** SOC Lead (pending)
