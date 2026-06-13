# Technical Intelligence: Meta AI App Architecture

**Collection ID:** TECHINT-2026-001  
**Date:** 2026-06-06  
**Analyst:** AI Threat Intelligence Unit  
**Classification:** TLP:AMBER  
**Confidence:** MEDIUM (based on reported findings, not direct analysis)

---

## Target Application

| Property | Value |
|----------|-------|
| **App Name** | Meta AI |
| **Platform** | iOS, Android |
| **Bundle ID (iOS)** | `com.facebook.MetaAI` (TBC) |
| **Package Name (Android)** | `com.facebook.MetaAI` (TBC) |
| **Current Version** | [To be determined] |
| **Version with NameTag** | Reportedly shipped as of January 2026 |
| **Download Count** | 50M+ (reported) |
| **Required For** | Ray-Ban Meta, Oakley smart glasses functionality |

---

## NameTag Pipeline Architecture (Reconstructed)

### High-Level Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                     DATA FLOW DIAGRAM                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  [Smart Glasses]                                                │
│       │                                                         │
│       │ Bluetooth/WiFi                                          │
│       ▼                                                         │
│  [Meta AI App on Phone]                                         │
│       │                                                         │
│       ├──► Face Detection Module                                │
│       │        └─► Face Alignment                               │
│       │                 └─► Embedding Generation                │
│       │                          └─► Faceprint (128-512 dim)    │
│       │                                                         │
│       ├──► Local Database (SQLite/Realm)                        │
│       │        └─► Enrolled Faceprints                          │
│       │                 └─► Metadata (name, relationship)       │
│       │                                                         │
│       ├──► Matching Engine                                      │
│       │        └─► Cosine Similarity                            │
│       │                 └─► Threshold Comparison                │
│       │                          └─► Match Notification         │
│       │                                                         │
│       └──► Cloud Sync (Optional/Configurable)                   │
│                └─► Meta Servers                                 │
│                         └─► Database Updates                    │
│                                  └─► Feature Flags              │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Component Breakdown

| Module | Likely Implementation | Evidence |
|--------|----------------------|----------|
| **Face Detection** | MTCNN, RetinaFace, or proprietary CNN | Industry standard |
| **Face Alignment** | Affine transform based on 5-68 landmarks | Standard pipeline |
| **Embedding Network** | ResNet, ArcFace, or AdaFace architecture | Common in FR systems |
| **Database** | SQLite with encryption, or Realm | Mobile app standard |
| **Matching** | Cosine similarity with configurable threshold | Standard approach |
| **Notification** | iOS: UserNotifications, Android: NotificationManager | Platform APIs |

---

## Reported Code Findings

### Feature Flags (Per WIRED/EFF)

| Flag Name | Purpose | State |
|-----------|---------|-------|
| `nametag_enabled` | Master toggle for NameTag feature | FALSE (dormant) |
| `nametag_cloud_sync` | Enable cloud database sync | Configurable |
| `nametag_threshold` | Matching confidence threshold | Tunable parameter |
| `nametag_ui_strings` | Localized UI text for feature | Present in binaries |

### Class/Method Names (Speculative)

| Component | Expected Naming Pattern |
|-----------|------------------------|
| Face Detection | `FaceDetector`, `FaceDetectionEngine` |
| Embedding | `FaceEmbedder`, `FeatureExtractor` |
| Database | `FaceprintStore`, `BiometricRepository` |
| Matching | `FaceMatcher`, `SimilarityEngine` |
| Notification | `RecognitionNotifier`, `IdentityAlert` |

---

## Network Endpoints (Anticipated)

| Endpoint | Purpose | Risk Level |
|----------|---------|------------|
| `api.meta.ai/biometric/sync` | Faceprint database sync | 🔴 CRITICAL |
| `api.meta.ai/faceprint/update` | Individual faceprint update | 🔴 CRITICAL |
| `api.meta.ai/config/nametag` | Feature flag polling | 🟠 HIGH |
| `api.meta.ai/analytics/recognition` | Usage telemetry | 🟡 MEDIUM |
| `graph.facebook.com/...` | Legacy Meta infrastructure | 🟡 MEDIUM |

**Note:** Actual endpoints require network traffic analysis. Above are educated guesses based on Meta API conventions.

---

## Data Storage Analysis

### Local Database Schema (Speculative)

```sql
-- Enrolled faces table
CREATE TABLE faceprints (
    id INTEGER PRIMARY KEY,
    person_name TEXT,
    faceprint_vector BLOB,      -- 128-512 float values
    enrollment_date TIMESTAMP,
    last_matched TIMESTAMP,
    source_photo_id TEXT,
    metadata JSON               -- Relationship, notes, etc.
);

-- Match history table
CREATE TABLE match_log (
    id INTEGER PRIMARY KEY,
    faceprint_id INTEGER,
    confidence REAL,
    capture_timestamp TIMESTAMP,
    location_lat REAL,
    location_lon REAL,
    capture_image_id TEXT,
    FOREIGN KEY (faceprint_id) REFERENCES faceprints(id)
);

-- Configuration table
CREATE TABLE config (
    key TEXT PRIMARY KEY,
    value TEXT,
    last_updated TIMESTAMP
);
```

### Storage Location

| Platform | Expected Path |
|----------|---------------|
| **iOS** | `/var/mobile/Containers/Data/Application/[UUID]/Library/Application Support/MetaAI/` |
| **Android** | `/data/data/com.facebook.MetaAI/databases/` |

---

## Activation Mechanism Analysis

### Possible Activation Paths

| Method | Description | Detectability |
|--------|-------------|---------------|
| **App Update** | New version enables feature by default | HIGH (version change visible) |
| **Feature Flag** | Remote config toggle enables existing code | LOW (no version change) |
| **A/B Test** | Gradual rollout to user segments | MEDIUM (statistical detection) |
| **Region Unlock** | Enable in specific jurisdictions | MEDIUM (geo-based) |
| **Opt-In Prompt** | User consent dialog enables feature | HIGH (user-visible) |

### Most Likely Scenario

**Assessment:** Feature flag + gradual A/B rollout

**Rationale:**
- Code is already shipped (no app update needed)
- Meta has extensive A/B testing infrastructure
- Gradual rollout reduces scrutiny and backlash
- Can be quickly rolled back if issues arise

---

## Technical Indicators of Activation

| Indicator | Detection Method | Threshold |
|-----------|------------------|-----------|
| Increased camera usage in background | Mobile EDR / App audit | >1 min continuous |
| Network traffic to biometric endpoints | Network monitoring | Any traffic |
| Database size growth (>10MB) | File system inspection | Sudden increase |
| CPU spikes during camera activity | Performance monitoring | Consistent pattern |
| New permission requests | App update review | Camera, location, contacts |

---

## Gaps in Technical Understanding

| Question | Priority | Method to Resolve |
|----------|----------|-------------------|
| Actual app version containing NameTag? | HIGH | App store version history + binary diff |
| Exact feature flag names? | HIGH | Reverse engineering of app binaries |
| Network endpoints used? | HIGH | MITM analysis of app traffic |
| Faceprint storage format? | MEDIUM | Database extraction from rooted device |
| Matching algorithm performance? | MEDIUM | Empirical testing (if activated) |
| Liveness detection present? | HIGH | Code review / empirical testing |
| Encryption method for local DB? | MEDIUM | Database extraction + cryptanalysis |

---

## Recommended Technical Collection

| Activity | Tools Required | Risk | Priority |
|----------|----------------|------|----------|
| **App Binary Download** | APKMirror, iOS IPA archives | LOW | HIGH |
| **Static Analysis** | Ghidra, IDA Pro, Jadx | LOW | HIGH |
| **Dynamic Analysis** | Frida, Objection, rooted device | MEDIUM | HIGH |
| **Network Analysis** | mitmproxy, Charles Proxy | MEDIUM | HIGH |
| **File System Analysis** | Rooted/jailbroken device, ADB | MEDIUM | MEDIUM |
| **Performance Profiling** | Instruments (iOS), Profiler (Android) | LOW | MEDIUM |

---

## Cross-References

| Related Collection | Status |
|-------------------|--------|
| OSINT-2026-001 (WIRED Report) | COMPLETE |
| TECHINT-2026-002 (Patent Analysis) | PENDING |
| TECHINT-2026-003 (Network Traffic Analysis) | PENDING |

---

**Analyst Notes:**
- This assessment is based on reported findings + industry-standard FR architecture
- Direct binary analysis required to confirm specifics
- Meta has not publicly confirmed NameTag existence
- EFF researcher involvement suggests credible technical review

**Next Actions:**
1. Download latest + historical Meta AI app versions
2. Perform static analysis on binaries
3. Set up network monitoring for Meta AI traffic
4. Monitor app update notes for NameTag-related changes

---

**Assessment Date:** 2026-06-06 03:05 UTC  
**Analyst:** AI Threat Intelligence Unit  
**Confidence:** MEDIUM  
**Status:** ACTIVE - Requires technical validation
