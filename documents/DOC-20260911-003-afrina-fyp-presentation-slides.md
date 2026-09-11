---
# === UNIVERSAL BASE ===
id: DOC-20260911-003
record_type: document
title: "FYP Presentation Slides — AI-Based Log Aggregation Techniques for SIEM (Afrina Syuhada, CSP650)"
created_at: 2026-09-11T03:18:00+00:00
updated_at: 2026-09-11T03:18:00+00:00
owner: faurani-jaafar
status: active
priority: low
sensitivity: internal
lifecycle_state: candidate
confidence: high
document_type: presentation
version: "1.0"
author: "Afrina Syuhada binti Jeffri Sem (student ID held in source PDF only)"
file_path: documents/DOC-20260911-003-afrina-fyp-presentation-slides.pdf
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
  reference: "FYP presentation slides PDF relayed by DAF (Telegram, 11 Sep 2026 03:15 UTC), course CSP650. Companion artefact to DOC-20260911-002 (thesis) and DOC-20260911-001 (resume). Stored at documents/DOC-20260911-003-afrina-fyp-presentation-slides.pdf."
summary: "[FACT per source document] Presentation deck for the completed FYP (same work as DOC-20260911-002): background, problem statement, objectives, scope, 5-work literature review (RF-based malicious-URL/NIDS/IoT-ID detection + explainable AI for alert classification), Agile methodology, results, demonstration, conclusion. Metrics beyond/confirming the thesis: train/test split 75,329/18,833 (80/20) of 94,162 events; held-out accuracy 79.81% (79.80% on one slide — rounding), full-dataset scoring agreement 95.60% (90,034/94,162); per-class attack P/R/F1 73.88/74.29/74.09 (support 7,317), normal P/R/F1 83.61/83.31/83.46 (support 11,516), macro-F1 78.77%; ROC-AUC 0.898 ('good'). Feature importance (150 trees): anomaly_score 45.10% dominant, then firewall (TF-IDF) 4.80%, severity_score 4.20%, with TF-IDF words and one-hot categoricals making up the remainder."
strategic_significance: "Companion deck to the thesis — no new capability claims, but two operationally useful disclosures: (1) full-dataset scoring agreement 95.60% shows the deployed scorer is consistent with training-time behaviour (relevant if the artefact is reprised for demo risk-scoring); (2) feature-importance disclosure shows anomaly_score (a pre-computed numeric) carries 45.10% of model weight — meaning the NLP/text pathway is a minority contributor. Honest technical caveat if her work is adapted into product/demo claims: the 'AI' story is partly carried by an existing anomaly score, not purely learned text features. Slide typos noted (test-row count '18,8333'; accuracy 79.80 vs 79.81) — cosmetic, same work. Strengthens the intern capability picture for Fuad's demo-data tasking; no change to placement or scope."
mission_alignment:
  - productisation
  - organisational-capability
related_records:
  - DOC-20260911-002
  - DOC-20260911-001
  - STK-20260911-002
  - DEC-20260911-002
  - STK-20260804-003
---

# DOC-20260911-003 — FYP Presentation Slides: AI-Based Log Aggregation Techniques for SIEM

**Nature:** Intake extraction of Afrina Syuhada's FYP presentation deck (CSP650), relayed by DAF 11 Sep 2026. Companion artefact to the thesis (DOC-20260911-002) — same project, presentation-layer detail. Provenance: academic artefact; author-reported metrics.

## 1. Deck Metadata

| Field | Value |
|-------|-------|
| Course | CSP650 (UiTM FYP presentation) |
| Title | AI-Based Log Aggregation Techniques for SIEM |
| Structure | Background → Problem → Scope/Significance → Literature review → Methodology → Results → Demonstration → Conclusion |

## 2. Metric Detail (slides — confirms + extends thesis figures)

| Metric | Value | Note |
|--------|-------|------|
| Dataset | 94,162 events | 3 sources (firewall, Android, IoT) |
| Split | 75,329 train (80%) / 18,833 test (20%) | Slide typo "18,8333" noted — cosmetic |
| Held-out accuracy | 79.81% | One slide shows 79.80% — rounding |
| ROC-AUC (attack) | 89.76% | Described "good" |
| Attack P/R/F1 | 73.88 / 74.29 / 74.09 | support 7,317 |
| Normal P/R/F1 | 83.61 / 83.31 / 83.46 | support 11,516 |
| Macro-F1 | 78.77% | — |
| Full-dataset scoring agreement | **95.60%** (90,034/94,162) | Deployed-scorer consistency — new vs thesis headline |

## 3. Technical Observation (analysis — matters only if reprised for product/demo claims)

Feature importance across 150 trees: **anomaly_score = 45.10%** (pre-computed numeric) dominates; the top TF-IDF text feature ("firewall") is 4.80%, severity_score 4.20%. Reading: the classifier's discrimination leans primarily on the existing anomaly score, with NLP text features as minority contributors. Not a defect for an FYP — but if her pipeline is adapted into demo risk-scoring or product claims, the "AI-driven" framing should reflect that the learned-text component is complementary, not primary.

## 4. Record Hygiene Notes

- Slide typos (test-row count, accuracy rounding) logged here so they don't propagate into any product/demo material derived from her work
- Student ID present in source PDF only — PII minimisation
