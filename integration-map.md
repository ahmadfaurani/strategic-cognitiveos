# Integration Map — Attack Vector Registry

**Classification:** TLP:AMBER  
**Version:** 1.0  
**Created:** 2026-05-21  
**Owner:** GovSec Intelligence Cell

---

## Executive Summary

This document maps integration points between the Attack Vector Registry and existing GovSec systems. Seven (7) primary integration targets are specified with API details, data flows, and implementation status.

**Integration Targets:**
1. Threat Actor Registry
2. HOI Collection Plan (RETIRED 2026-09-14)
3. AIL Framework
4. ChainSentry
5. GovSec TIP
6. Heartbeat System
7. CBO-01 Commercial Operations

---

## Integration Overview

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    Attack Vector Registry                               │
└─────────────────────────────────────────────────────────────────────────┘
         │              │              │              │              │
         │              │              │              │              │
         ▼              ▼              ▼              ▼              ▼
┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐
│   Threat    │ │     HOI     │ │     AIL     │ │  ChainSentry│ │   GovSec    │
│    Actor    │ │ Collection  │ │  Framework  │ │             │ │     TIP     │
│   Registry  │ │    Plan     │ │             │ │             │ │             │
└─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘
         │              │              │              │              │
         │              │              │              │              │
         ▼              ▼              ▼              ▼              ▼
┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐
│  Heartbeat  │ │    CBO-01   │ │  Proxmox VE │ │  ZeroTier   │ │  Telegram   │
│   System    │ │ Commercial  │ │  Sandbox    │ │  Network    │ │  Bot API    │
│             │ │   Ops       │ │             │ │             │ │             │
└─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘
```

---

## 1. Threat Actor Registry Integration

### Integration Type: Actor → CVE Mapping

**Purpose:** Link threat actors to exploited vulnerabilities for attribution and campaign tracking.

### Data Flow

```
Attack Vector Registry          Threat Actor Registry
      │                                │
      │   CVE → Actor Mapping          │
      │───────────────────────────────>│
      │                                │
      │   Actor Profile + TTPs         │
      │<───────────────────────────────│
      │                                │
```

### API Specification

**Endpoint:** `POST /api/v1/actor-cve-mapping`

**Request:**
```json
{
  "cve_id": "CVE-2026-12345",
  "actor_name": "APT40",
  "confidence": "high",
  "evidence": [
    {
      "type": "campaign_observation",
      "source": "Microsoft Threat Intelligence",
      "url": "https://www.microsoft.com/security/blog/apt40"
    }
  ],
  "mitre_mapping": {
    "technique_id": "T1190",
    "procedure": "Exploitation of CVE-2026-12345 in initial access"
  },
  "first_observed": "2026-05-20",
  "tlp": "AMBER"
}
```

**Response:**
```json
{
  "status": "success",
  "mapping_id": "map-001",
  "created_at": "2026-05-21T16:00:00Z"
}
```

### Schema Extension

**Threat Actor Registry Schema Addition:**
```yaml
# actors/[actor-name]/exploited-cves.json
exploited_cves:
  - cve_id: "CVE-2026-12345"
    first_observed: "2026-05-20"
    last_observed: "2026-05-21"
    confidence: "high"
    campaigns:
      - "GraphWorm Deployment 2026"
    mitre_mapping:
      technique_id: "T1190"
      procedure: "Exploitation of Exchange Server vulnerability"
    sources:
      - "Microsoft Threat Intelligence"
    tlp: "AMBER"
```

### Implementation Status: 🟡 Planned

**Dependencies:**
- Threat Actor Registry schema update
- Cross-repository git hooks (atomic commits)
- TLP synchronization

---

## 2. HOI Collection Plan Integration

> ⚠️ **RETIRED 2026-09-14** — HOI agent retired (legacy). This integration is inactive; AVR collection-requirement generation is handled directly in the heartbeat AVR workflow (see HEARTBEAT.md).

### Integration Type: New Collection Requirements

**Purpose:** Automatically generate HOI collection requirements for high-priority CVEs and POCs.

### Data Flow

```
Attack Vector Registry          HOI Collection Plan
      │                                │
      │   New CR Generation            │
      │───────────────────────────────>│
      │   (KEV-listed, POC available)  │
      │                                │
      │   CR Status Updates            │
      │<───────────────────────────────│
      │                                │
```

### Collection Requirement Template

```yaml
# Collection Requirement: CVE-2026-12345 Exploitation

cr_id: "CR-2026-001"
title: "CVE-2026-12345 Exploitation in Malaysian GovSec"
priority: "P1"
status: "OPEN"
created: "2026-05-21T16:00:00Z"
due_date: "2026-05-28T23:59:59Z"

# === Intelligence Requirements ===
requirements:
  - "Identify any Malaysian government agencies affected by CVE-2026-12345"
  - "Determine if exploitation attempts have been observed"
  - "Collect IOCs from any confirmed incidents"
  - "Assess patch status across critical infrastructure"

# === Sources ===
sources:
  - "Agency SOC telemetry"
  - "NACSA incident reports"
  - "CSM threat intel feeds"
  - "AIL Framework dark web monitoring"

# === Distribution ===
distribution:
  - "CSM Intelligence Unit"
  - "NACSA Operations"
  - "MAMPU Security"

# === Automation Trigger ===
automation_trigger:
  kev_listed: true
  poc_available: true
  cvss_score: 9.8
  malaysian_relevance: "HIGH"
```

### API Specification

**Endpoint:** `POST /api/v1/collection-requirements`

**Request:**
```json
{
  "title": "CVE-2026-12345 Exploitation in Malaysian GovSec",
  "priority": "P1",
  "requirements": [
    "Identify affected Malaysian agencies",
    "Determine exploitation status",
    "Collect IOCs"
  ],
  "automation_trigger": {
    "source": "attack-vector-registry",
    "cve_id": "CVE-2026-12345",
    "kev_listed": true,
    "poc_available": true,
    "cvss_score": 9.8
  },
  "due_date": "2026-05-28T23:59:59Z"
}
```

**Response:**
```json
{
  "status": "success",
  "cr_id": "CR-2026-001",
  "created_at": "2026-05-21T16:00:00Z"
}
```

### Implementation Status: 🟡 Planned

**Dependencies:**
- HOI Collection Plan API
- Automation trigger logic (KEV + POC + CVSS threshold)
- Malaysian relevance scoring

---

## 3. AIL Framework Integration

### Integration Type: Dark Web Intel Correlation

**Purpose:** Correlate Attack Vector Registry CVEs with dark web exploit mentions and ransomware claims.

### Data Flow

```
Attack Vector Registry          AIL Framework
      │                                │
      │   CVE Query (hourly)           │
      │───────────────────────────────>│
      │                                │
      │   Dark Web Mentions            │
      │<───────────────────────────────│
      │   (exploit mentions, claims)   │
      │                                │
      │   TLP:RED Intel                │
      │───────────────────────────────>│
      │   (enrich CVE entry)           │
      │                                │
```

### API Specification

**AIL Framework Endpoints:**

```python
# Search for exploit mentions
GET /api/v1/intel/search?q=CVE-2026-12345+exploit

# Get intel by tag
GET /api/v1/intel/tags/exploit

# Get dark web source intel
GET /api/v1/intel/source/darkweb

# Submit new intel (from POC validation)
POST /api/v1/intel
{
  "type": "poc_validation",
  "cve_id": "CVE-2026-12345",
  "validation_status": "working",
  "iocs": [...],
  "tlp": "AMBER"
}
```

### Response Schema

```json
{
  "intel_items": [
    {
      "uuid": "ail-uuid-001",
      "type": "exploit_mention",
      "title": "CVE-2026-12345 exploit for sale",
      "content": "Exploit for CVE-2026-12345 available...",
      "source": "darkweb_forum_x",
      "collected_at": "2026-05-21T15:30:00Z",
      "tags": ["exploit", "cve-2026-12345", "for_sale"],
      "tlp": "RED",
      "confidence": "medium"
    }
  ]
}
```

### Correlation Logic

```python
# /opt/attack-vector-registry/ail-correlator.py

class AILCorrelator:
    def __init__(self):
        self.ail_api = AILFrameworkAPI(base_url="https://192.168.1.102:7000")
    
    async def correlate_cve(self, cve_id):
        """Correlate CVE with AIL Framework intel"""
        
        # Search for CVE mentions
        search_results = await self.ail_api.search(f"{cve_id} exploit")
        
        # Search for exploit tags
        tag_results = await self.ail_api.get_by_tag("exploit")
        
        # Filter and enrich
        relevant_intel = []
        for intel in search_results + tag_results:
            if cve_id.lower() in intel.get('content', '').lower():
                relevant_intel.append({
                    'ail_uuid': intel['uuid'],
                    'type': intel['type'],
                    'source': intel['source'],
                    'collected_at': intel['collected_at'],
                    'tlp': intel['tlp'],
                    'confidence': intel['confidence']
                })
        
        return {
            'cve_id': cve_id,
            'ail_mentions': len(relevant_intel),
            'intel_items': relevant_intel,
            'dark_web_confirmed': any(i['source'].startswith('darkweb') for i in relevant_intel)
        }
```

### Implementation Status: 🟢 Ready

**Configuration:**
- AIL Framework API token: Available (see TOOLS.md)
- Base URL: `https://192.168.1.102:7000`
- Polling interval: Hourly

---

## 4. ChainSentry Integration

### Integration Type: POC Validation Input

**Purpose:** Provide validated POCs to ChainSentry for exploit chaining analysis via pentest-ai-agents.

### Data Flow

```
Attack Vector Registry          ChainSentry
      │                                │
      │   Validated POCs               │
      │───────────────────────────────>│
      │   (working POCs only)          │
      │                                │
      │   Exploit Chain Analysis       │
      │<───────────────────────────────│
      │   (chain validation results)   │
      │                                │
```

### API Specification

**Endpoint:** `POST /api/v1/poc-ingestion`

**Request:**
```json
{
  "poc_id": "poc-001",
  "cve_id": "CVE-2026-12345",
  "validation_status": "working",
  "poc_location": "/opt/poc-sandbox/pocs/20260521/poc-e3b0c44.py",
  "target_platform": "Windows",
  "target_product": "Microsoft Exchange Server",
  "iocs": {
    "file_hashes": ["e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"],
    "network": ["192.168.1.100"],
    "behavioral": ["process_spawn", "network_connection"]
  },
  "tlp": "AMBER",
  "sandbox_artifacts": {
    "sysmon_log": "/opt/poc-sandbox/artifacts/20260521/vm-100/sysmon.xml",
    "network_capture": "/opt/poc-sandbox/artifacts/20260521/vm-100/capture.pcap"
  }
}
```

**Response:**
```json
{
  "status": "accepted",
  "chainsentry_id": "cs-poc-001",
  "analysis_queue_position": 3,
  "estimated_analysis_time": "15 minutes"
}
```

### ChainSentry Analysis Output

```json
{
  "chainsentry_id": "cs-poc-001",
  "analysis_status": "completed",
  "exploit_chains": [
    {
      "chain_id": "chain-001",
      "poc_sequence": ["poc-001", "poc-002"],
      "combined_impact": "CRITICAL",
      "feasibility": "high",
      "description": "CVE-2026-12345 RCE + privilege escalation chain"
    }
  ],
  "recommendations": [
    "Prioritize patching for CVE-2026-12345",
    "Deploy detection rules for POC-001 behavioral indicators"
  ]
}
```

### Implementation Status: 🟡 Planned

**Dependencies:**
- ChainSentry API development
- POC artifact sharing mechanism (secure file transfer)
- TLP governance for POC distribution

---

## 5. GovSec TIP Integration

### Integration Type: STIX/TAXII Ingestion

**Purpose:** Automated intelligence sharing with CSM/NACSA via STIX/TAXII protocol.

### Data Flow

```
Attack Vector Registry          GovSec TIP
      │                                │
      │   STIX Bundles                 │
      │───────────────────────────────>│
      │   (CVEs, POCs, IOCs)           │
      │                                │
      │   TAXII Collection             │
      │<───────────────────────────────│
      │   (external intel feeds)       │
      │                                │
```

### STIX 2.1 Bundle Schema

```json
{
  "type": "bundle",
  "id": "bundle--attack-vector-registry-2026-05-21",
  "objects": [
    {
      "type": "identity",
      "id": "identity--govsec-intel-cell",
      "name": "GovSec Intelligence Cell",
      "identity_class": "government"
    },
    {
      "type": "vulnerability",
      "id": "vulnerability--CVE-2026-12345",
      "name": "CVE-2026-12345",
      "description": "Microsoft Exchange Server Elevation of Privilege Vulnerability",
      "external_references": [
        {
          "source_name": "NVD",
          "url": "https://nvd.nist.gov/vuln/detail/CVE-2026-12345"
        }
      ],
      "created": "2026-05-21T10:00:00Z"
    },
    {
      "type": "indicator",
      "id": "indicator--poc-001",
      "indicator_types": ["malicious-activity"],
      "pattern": "[file:hashes.'SHA-256' = 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855']",
      "pattern_type": "stix",
      "valid_from": "2026-05-21T16:00:00Z"
    },
    {
      "type": "relationship",
      "id": "relationship--001",
      "relationship_type": "exploits",
      "source_ref": "indicator--poc-001",
      "target_ref": "vulnerability--CVE-2026-12345"
    }
  ]
}
```

### TAXII 2.1 Configuration

```yaml
# config/taxii.yaml

taxii_server:
  url: "https://tip.govsec.my/taxii2/"
  api_root: "govsec-intel"
  auth:
    type: "basic"
    username: "attack-vector-registry"
    password_env: "TAXII_PASSWORD"

collections:
  - id: "attack-vectors"
    title: "Attack Vector Intelligence"
    description: "CVEs, POCs, and IOCs from Attack Vector Registry"
    can_read: true
    can_write: true
  
  - id: "kev-alerts"
    title: "CISA KEV Alerts"
    description: "KEV-listed vulnerabilities with Malaysian relevance"
    can_read: true
    can_write: true
```

### Distribution Triggers

| Trigger | TLP | Distribution |
|---------|-----|--------------|
| CVE + KEV listed | GREEN | Full STIX bundle to TIP |
| CVE + POC validated (working) | AMBER | STIX bundle (IOC subset) |
| CVE + Malaysian targeting | AMBER | Targeted distribution (CSM/NACSA only) |
| POC + RED TLP | RED | No automated distribution (manual only) |

### Implementation Status: 🟡 Planned

**Dependencies:**
- GovSec TIP TAXII 2.1 server deployment
- STIX 2.1 schema mapping
- TLP-governed distribution logic

---

## 6. Heartbeat System Integration

### Integration Type: Daily CVE Summary

**Purpose:** Provide executive awareness of high-priority CVEs via heartbeat system.

### Data Flow

```
Attack Vector Registry          Heartbeat System
      │                                │
      │   Daily CVE Summary            │
      │───────────────────────────────>│
      │   (KEV + POC + Critical)       │
      │                                │
      │   Heartbeat Poll               │
      │<───────────────────────────────│
      │   (Telegram message)           │
      │                                │
```

### Daily Summary Template

```markdown
🔴 **Attack Vector Registry — Daily Summary**
**Date:** 2026-05-21
**Period:** Last 24 hours

---

### 📊 Metrics

| Metric | Count | Change |
|--------|-------|--------|
| **New CVEs** | 45 | +12 |
| **KEV Listed** | 3 | +1 |
| **POC Available** | 15 | +5 |
| **POC Validated** | 8 | +3 |
| **Critical (CVSS ≥9.0)** | 5 | +2 |

---

### 🚨 High-Priority CVEs

#### CVE-2026-12345 (CRITICAL)
- **CVSS:** 9.8
- **KEV Listed:** ✅
- **POC Available:** ✅ (Working)
- **Affected:** Microsoft Exchange Server
- **Malaysian Relevance:** HIGH

#### CVE-2026-12346 (HIGH)
- **CVSS:** 8.5
- **KEV Listed:** ❌
- **POC Available:** ✅ (Not Tested)
- **Affected:** Cisco ASA
- **Malaysian Relevance:** MEDIUM

---

### 📈 Trends

- **Exploitation Activity:** Elevated (3 KEV additions)
- **POC Development:** Active (5 new POCs)
- **Vendor Response:** On track (80% patched within 7 days)

---

**Next Heartbeat:** 2026-05-22 08:00 UTC
```

### Heartbeat Configuration

```yaml
# config/heartbeat.yaml

heartbeat:
  schedule: "0 8 * * *"  # Daily at 08:00 UTC
  channel: "telegram"
  recipient_user_id: 640442208
  
  filters:
    min_cvss_score: 7.0
    include_kev: true
    include_poc: true
    malaysian_relevance: ["HIGH", "MEDIUM"]
  
  template: "daily-cve-summary.md"
```

### Implementation Status: 🟢 Ready

**Dependencies:**
- Heartbeat system (existing)
- Telegram bot API (@Dafclawbot)
- Summary template

---

## 7. CBO-01 Commercial Operations Integration

### Integration Type: Commercial SKU Positioning

**Purpose:** Enable "Automated Threat Intel" SKU for VoronDRQ commercial offering.

### Data Flow

```
Attack Vector Registry          CBO-01 Commercial Ops
      │                                │
      │   Capability Metrics           │
      │───────────────────────────────>│
      │   (for GTM positioning)        │
      │                                │
      │   Revenue Attribution          │
      │<───────────────────────────────│
      │   (POC-to-revenue mapping)     │
      │                                │
```

### Commercial SKU Definition

```yaml
# SKU: Automated Threat Intel Module

sku_id: "VORON-AVT-001"
name: "VoronDRQ — Automated Threat Intel Module"
category: "Threat Intelligence"
pricing_model: "subscription"

# === Capabilities ===
capabilities:
  - "Automated CVE ingestion (9 sources)"
  - "POC validation sandbox"
  - "TLP-governed distribution"
  - "STIX/TAXII integration"
  - "Executive CVE summaries"

# === Metrics ===
metrics:
  - "CVEs ingested per day"
  - "POCs validated per week"
  - "Time-to-intel (publication → registry)"
  - "KEV coverage (100%)"

# === Target Customers ===
target_customers:
  - "Malaysian government agencies"
  - "Critical infrastructure operators"
  - "Financial services"
  - "Healthcare"

# === Pricing ===
pricing:
  base_price_myr: 50000
  billing_cycle: "annual"
  includes:
    - "Attack Vector Registry access"
    - "Daily CVE summaries"
    - "POC validation reports"
    - "STIX/TAXII feed"
```

### Revenue Attribution

```python
# /opt/cbo-01/revenue-attribution.py

class RevenueAttribution:
    def __init__(self):
        self.sku_pricing = {
            'VORON-AVT-001': 50000  # MYR annual
        }
    
    def attribute_revenue(self, customer_id, subscription_start, subscription_end):
        """Attribute revenue to Attack Vector Registry capability"""
        
        sku = 'VORON-AVT-001'
        base_price = self.sku_pricing[sku]
        
        # Prorate by subscription period
        days = (subscription_end - subscription_start).days
        daily_rate = base_price / 365
        attributed_revenue = daily_rate * days
        
        return {
            'customer_id': customer_id,
            'sku': sku,
            'capability': 'Attack Vector Registry',
            'attributed_revenue_myr': attributed_revenue,
            'period_days': days
        }
```

### GTM Positioning

**Value Proposition:**
> "Sovereign attack vector intelligence with automated POC validation — no commercial feed dependency."

**Differentiation:**
- ✅ 24/7 automated collection (9 sources)
- ✅ POC validation sandbox (working/non-working classification)
- ✅ TLP-governed distribution (CISA/NACSA compliant)
- ✅ Malaysian relevance scoring
- ✅ Integration with existing GovSec TIP

**Target Early Adopters:**
1. CyberSecurity Malaysia (CSM) — Intel Unit
2. NACSA — Operations
3. MAMPU — Security Division
4. Bank Negara Malaysia — Cybersecurity

### Implementation Status: 🟡 Planned

**Dependencies:**
- CBO-01 commercial ops framework
- SKU definition and pricing
- Customer onboarding workflow

---

## Integration Summary

| # | System | Integration Type | Status | Priority |
|---|--------|------------------|--------|----------|
| 1 | Threat Actor Registry | Actor → CVE mapping | 🟡 Planned | P1 |
| 2 | HOI Collection Plan | New CR generation | 🟡 Planned | P1 |
| 3 | AIL Framework | Dark web correlation | 🟢 Ready | P1 |
| 4 | ChainSentry | POC validation input | 🟡 Planned | P2 |
| 5 | GovSec TIP | STIX/TAXII ingestion | 🟡 Planned | P1 |
| 6 | Heartbeat System | Daily CVE summary | 🟢 Ready | P2 |
| 7 | CBO-01 Commercial Ops | SKU positioning | 🟡 Planned | P3 |

---

## API Authentication Summary

| System | Auth Type | Credential Location |
|--------|-----------|---------------------|
| **AIL Framework** | API Token | `AIL_API_TOKEN` (TOOLS.md) |
| **GitHub** | Personal Access Token | `GH_TOKEN` (env) |
| **NVD** | API Key (optional) | `NVD_API_KEY` (env) |
| **Twitter** | Bearer Token | `TWITTER_BEARER_TOKEN` (env) |
| **GovSec TIP** | Basic Auth | `TAXII_PASSWORD` (env) |
| **Telegram** | Bot Token | `TELEGRAM_BOT_TOKEN` (env) |

---

## Implementation Priorities

### Phase 1 (Week 1-2): Core Integrations
- [ ] AIL Framework integration (🟢 Ready)
- [ ] Heartbeat System integration (🟢 Ready)
- [ ] Threat Actor Registry schema update

### Phase 2 (Week 3-4): Intelligence Sharing
- [ ] GovSec TIP STIX/TAXII integration
- [ ] HOI Collection Plan automation
- [ ] ChainSentry POC ingestion

### Phase 3 (Week 5): Commercial
- [ ] CBO-01 SKU definition
- [ ] GTM positioning
- [ ] Early adopter outreach

---

**Classification:** TLP:AMBER  
**Version:** 1.0  
**Created:** 2026-05-21  
**Owner:** GovSec Intelligence Cell
