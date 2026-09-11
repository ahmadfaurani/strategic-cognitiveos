---
# === UNIVERSAL BASE ===
id: DOC-20260911-002
record_type: document
title: "FYP Thesis — AI-Based Log Aggregation Techniques for SIEM (Afrina Syuhada, UiTM, July 2026)"
created_at: 2026-09-11T03:15:00+00:00
updated_at: 2026-09-11T03:15:00+00:00
owner: faurani-jaafar
status: active
priority: medium
sensitivity: internal
lifecycle_state: candidate
confidence: high
document_type: report
version: "1.0"
author: "Afrina Syuhada binti Jeffri Sem (UiTM student ID held in source PDF only)"
file_path: documents/DOC-20260911-002-afrina-fyp-thesis.pdf
tags:
  - domain/artificial-intelligence
  - domain/cybersecurity
  - workstream/org-capability
  - workstream/cybersec-products
  - org/aras-integrasi
  - person/afrina-syuhada
  - role/intern
  - lifecycle/active
source:
  type: document
  reference: "Final Year Project thesis PDF relayed by DAF (Telegram, 11 Sep 2026 03:13 UTC). 'AI-Based Log Aggregation Techniques for SIEM', Bachelor of Computer Science (Hons.) Computer Networks, UiTM Shah Alam, submitted July 2026; supervisor Ts. Dr. Mohsen Bin Mohamad Hata. Stored at documents/DOC-20260911-002-afrina-fyp-thesis.pdf. Related: DOC-20260911-001 (resume), DEC-20260911-002 (placement with Fuad)."
summary: "[FACT per source document — formal academic artefact, supervisor-approved] Completed FYP thesis (July 2026): AI-based log aggregation framework for SIEM consolidating three heterogeneous log sources (network firewall, Android endpoint, IoT traffic under DDoS attack) into a unified standardised dataset of 94,162 events. NLP + TF-IDF vectorisation of unstructured log messages, combined with structured numeric/categorical features; supervised Random Forest classifier for attack/normal classification plus continuous per-entry risk score. Held-out test results: 79.81% accuracy, ROC-AUC 89.76%. Includes an interactive SOC dashboard (overview, threat analysis, defense, suggested-response, incident response, per-source monitoring, SOC report, explorer tabs). Agile methodology. Supervisor-approved and submitted — stronger provenance than CV self-report; headline claims remain author-reported pending independent verification."
strategic_significance: "Directly relevant completed work sitting under Fuad's product lanes: the thesis is an end-to-end build of exactly the demo-adjacent capability stack — heterogeneous log normalisation into a unified schema, AI risk scoring, and a SOC dashboard — mapping naturally onto GovSec TIP and chain:SENTRY demo-data preparation and dashboard work ahead of CyberDSA (Oct 5-7). Practical reading: Afrina arrives with a working SIEM log-pipeline + AI-scoring + dashboard artefact she built herself; Fuad can task her to adapt it (or its techniques) for booth demos within the displacing-not-adding supervision constraint. Also a portfolio/CV-substantiation point: the practice gains a demonstrable AI-SIEM skill set at intern cost through 11 Dec. Title-page variant noted: supervisor-approval header reads 'Machine Learning-Based Log Aggregation Framework for SIEM System' vs cover title 'AI-Based Log Aggregation Techniques for SIEM' — same work, internal title inconsistency in the source document."
mission_alignment:
  - productisation
  - organisational-capability
related_records:
  - STK-20260911-002
  - DOC-20260911-001
  - CONV-20260911-004
  - DEC-20260911-002
  - STK-20260804-003
---

# DOC-20260911-002 — FYP Thesis: AI-Based Log Aggregation Techniques for SIEM

**Nature:** Intake extraction of Afrina Syuhada's completed Final Year Project thesis, relayed by DAF. Provenance: formal academic artefact — supervisor-approved (Ts. Dr. Mohsen Bin Mohamad Hata) and submitted to UiTM Faculty of Computer and Mathematical Sciences, July 2026. Stronger provenance than the CV (DOC-20260911-001); headline performance claims remain author-reported — no independent verification performed.

## 1. Thesis Metadata

| Field | Value (per source document) |
|-------|------------------------------|
| Title (cover) | AI-Based Log Aggregation Techniques for SIEM |
| Title (supervisor-approval header) | Machine Learning-Based Log Aggregation Framework for SIEM System — variant noted, same work |
| Author | Afrina Syuhada binti Jeffri Sem |
| Degree | Bachelor of Computer Science (Hons.) Computer Networks, UiTM Shah Alam |
| Submitted | July 2026 |
| Supervisor | Ts. Dr. Mohsen Bin Mohamad Hata |
| Methodology | Agile (requirements → design → development → testing → deployment → review) |

## 2. What Was Built (per abstract + Ch.1/Ch.4)

| Component | Detail |
|-----------|--------|
| Unified dataset | 3 heterogeneous sources — network firewall, Android endpoint, IoT traffic under DDoS attack — normalised to one schema (timestamp, src/dst IP, protocol, severity, event message); **94,162 events** |
| Text feature pipeline | NLP preprocessing + TF-IDF vectorisation of free-text log messages |
| Feature fusion | Text features + structured numeric (severity/anomaly scores) + one-hot categorical (source type, protocol, device type) |
| Model | Supervised Random Forest — binary attack/normal classification + continuous per-entry ML risk score |
| Results (held-out 20% split) | **79.81% accuracy · ROC-AUC 89.76%** (attack class) |
| Deliverable | Interactive SOC dashboard — overview, threat analysis, defense, suggested immediate response actions, incident response, firewall/Android/IoT monitoring tabs, SOC report, explorer, sidebar filters |

## 3. Relevance to Practice Lanes (analysis — placement is Fuad's to task)

1. **GovSec TIP / chain:SENTRY demo data:** the thesis pipeline (heterogeneous log ingestion → unified schema → AI risk scoring) is the same shape of work as preparing credible demo telemetry for the CyberDSA booths
2. **SOC dashboard:** she has already built and tested a multi-tab SOC dashboard — directly reusable skill for demo UI work and ELK-based dashboards
3. **Honest-limitations awareness:** thesis includes limitations + recommendations chapters — useful posture for claims QC discipline (CVS) when adapting the work to product demos
4. **Boundary:** academic prototype (public/simulated datasets, 79.81% accuracy) — not production-grade; treat as a capable junior with relevant hands-on artefacts, not a finished product contribution

## 4. Verification Notes

- Supervisor approval + student declaration present in source PDF → provenance: formal academic submission
- Performance figures (94,162 events; 79.81%; ROC-AUC 89.76%) are author-reported from the thesis — flagged for independent verification only if the work is reprised in product/demo claims
- Personal identifiers (student ID, contacts) held in source PDF only — PII minimisation
