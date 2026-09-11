---
# === UNIVERSAL BASE ===
id: DOC-20260911-004
record_type: document
title: "CMERP × GovSec Integration — Technical Engineering Paper v1.0 (CSM Acknowledgement Dated 4 Sep 2026)"
created_at: 2026-09-11T06:42:00+00:00
updated_at: 2026-09-11T06:42:00+00:00
owner: faurani-jaafar
status: active
priority: critical
sensitivity: confidential
lifecycle_state: candidate
confidence: high
document_type: specification
version: "1.0"
author: "Aras Integrasi Sdn Bhd (per title page); ARAS signatory Ahmad Fuad Kamarazaman; CSM signatory Fathi Kamil Mohd Zainuddin"
file_path: documents/DOC-20260911-004-cmerp-govsec-technical-engineering-paper.pdf
tags:
  - domain/csm-partnership
  - domain/cybersecurity-productisation
  - domain/technical-integration
  - domain/governance
  - milestone/cyberdsa-2026
  - product/govsec-tip
  - product/cmerp
  - product/lebahnet
source:
  type: document
  reference: "PDF relayed by DAF (Telegram, 11 Sep 2026 06:42 UTC), 21 pages. SHA-256 c7a3109d2c39800afb744da45c7523b4a5b5e6f66aa3902b798c78349c2f09d0. PDF metadata: produced macOS Quartz PDFContext; created 3 Sep 2026 10:30 UTC; modified 4 Sep 2026 07:55 UTC. This is the signed artifact referenced in DAF executive brief 11 Sep (CONV-20260911-006) and recorded as milestone OUT-20260911-001."
summary: "[FACT per source document] CMERP × GovSec Integration Technical Engineering Paper, v1.0 Canonical (Technical), August 2026, classification Confidential/Sulit, 21 pages. Scope: three deliverables — (1) GovSec-hosted signature repository generating ET Pro-compatible signatures for CMERP Suricata ingestion (paper ref COM-20260821-002, owner Fuad); (2) CMERP Sensor Appliance hosted in Aras environment (paper ref COM-20260821-003, Tuan Fatah, PENDING management approval — paper ref RSK-20260821-001, the stated critical-path blocker); (3) Suricata-format TI alert push CMERP → GovSec (paper ref COM-20260821-004; CSM JSON parameter sample in hand). Three data flows: A outbound signatures/IOCs (GovSec→CMERP), B inbound TI/detection alerts (CMERP→GovSec), C inbound LebahNet honeypot indicators (LebahNet→GovSec, STIX/TAXII 2.1, present-state active per Fuad confirmation 22 Aug). Auth state: push ingestion API static API key (only non-JWT endpoint); Flow A delivery auth OPEN (API key vs mTLS to be proposed by Aras, confirmed by CSM). PDPA engine 4-hour PII scan; Malaysian classification levels; immutable audit. Four validation gates with named approvers and dated evidence required (targets 24–27 Aug); ESF DoD §13; 7 open items/contract gaps (§12). PRESENT-STATE vs FUTURE-STATE table (§1.1): GovSec TIP + LebahNet present; CMERP signature feed designed/proposed; sensor appliance pending approval; Suricata alert integration proposed; SiberSUITE/CBOM/Score Card future-state. AUTHORISATION BLOCK (p20–21): CSM — Fathi Kamil Mohd Zainuddin, Head of MyCERT, dated 4/9/2026; ARAS — Ahmad Fuad Kamarazaman, Principal AI Security Architect, dated 26/8/2026. Signature fields are completed form fields (names/dates); the provided PDF contains NO cryptographic signature object (AcroForm only — /ByteRange, /SigFlags absent; Quartz print/export path)."
strategic_significance: "The signed integration artifact itself — converts the 4 Sep milestone (OUT-20260911-001) from summary-attested to artifact-evidenced, closing Cognitive Loop gap #3 (INT-20260911-001) and supplying the first component of the substantiation pack (ACT-20260911-006). Directly feeds Gate 4 co-branding substantiation (DOC-20260822-002) whose 8-artifact minimum evidence package this paper partially satisfies (architecture/flow layers). TWO material discrepancies to govern: (1) CSM signatory is Fathi Kamil (Head of MyCERT, STK-20260804-004 — the CSM integration lead), NOT Hafiz Rahman (SiberSUITE, gate 5) or Zaharudin (gate 6) per the COM-20260827-001 gate schedule — the milestone date reconciles, the signatory does not; the Aug gate chain should be re-reading as 'CSM technical endorsement' delivered via the MyCERT integration lead. (2) The paper's provenance appendix (§15.1) cites a 20260821-series record namespace (INIT-20260821-001, STK-20260821-003, COM-20260821-002/003/004, RSK-20260821-001, ART-20260821-003, CONV-20260821-002/003) that does NOT exist in the canonical strategic-cognitiveos repo — a parallel lineage (possibly another agent's workspace or archived branch) must be reconciled or the references mapped to canonical equivalents. OPEN TECHNICAL QUESTION carried into controlled implementation: sensor-appliance management approval (paper §12 item 2) — status unknown as of 11 Sep; Flow B cannot go live without it."
mission_alignment:
  - domain/cybersecurity-productisation
  - domain/government-partnerships
related_records:
  - CONV-20260911-006
  - DEC-20260911-003
  - OUT-20260911-001
  - ACT-20260911-006
  - INT-20260911-001
  - COM-20260827-001
  - INIT-20260804-002
  - DOC-20260822-002
  - STK-20260804-004
  - DOC-20260814-003
---

# DOC-20260911-004 — CMERP × GovSec Technical Engineering Paper (Signed)

**Nature:** Intake of the signed engineering artifact relayed by DAF (Telegram, 11 Sep 2026 06:42 UTC). All content below is **per the source document** unless marked as corpus observation. Classification carried as marked: CONFIDENTIAL / SULIT.

## 1. Document Identity

| Field | Value |
|-------|-------|
| Title | Technical Engineering Paper — CMERP × GovSec Integration |
| Subtitle | Bidirectional interoperability between CMERP (Insight Manager / Sensor Fleet) and the GovSec Threat Intelligence Platform |
| Prepared by / For | Aras Integrasi Sdn Bhd / CyberSecurity Malaysia (CSM) — MyCERT |
| Version | 1.0 (Canonical, Technical), August 2026 |
| Classification | Confidential — Sulit |
| Pages | 21 |
| File | documents/DOC-20260911-004-cmerp-govsec-technical-engineering-paper.pdf |
| SHA-256 | c7a3109d2c39800afb744da45c7523b4a5b5e6f66aa3902b798c78349c2f09d0 |
| PDF metadata | Created 3 Sep 2026 10:30 UTC; modified 4 Sep 2026 07:55 UTC; macOS Quartz PDFContext (print/export); AcroForm present |

## 2. Authorisation Block (p20–21) — SIGNATORY DISCREPANCY vs AUG GATE CHAIN

| Party | Name (per doc) | Title (per doc) | Date (per doc) |
|-------|----------------|-----------------|----------------|
| CyberSecurity Malaysia | Fathi Kamil Mohd Zainuddin | Head of MyCERT | **4/9/2026** |
| Aras Integrasi | Ahmad Fuad Kamarazaman | Principal AI Security Architect, Cyber Security Practice | **26/8/2026** |

**Corpus observation (verification):**
- The authorisation fields are **completed form fields (names + dates), NOT a cryptographic digital signature** — the supplied PDF contains no /ByteRange, /SigFlags, or signature SubFilter objects; it is a Quartz print/export of a signed-or-filled form. "Digitally signed" in DAF's brief should be read as *formally acknowledged and dated in the authorisation block*, not PAdES-verified, **unless an original signed/certified PDF exists elsewhere** (ask Fuad for the signature-variant file if cryptographic evidence is needed for Gate 4).
- **Signatory reconciliation:** COM-20260827-001 scheduled CSM validation via Hafiz Rahman (SiberSUITE, T-32 = 4 Sep) then Zaharudin sign-off/baseline (T-30 = 5 Sep). The artifact's CSM signatory is **Fathi Kamil, Head of MyCERT** (the CSM integration lead per STK-20260804-004), dated 4 Sep. Milestone DATE reconciles with the committed window; signatory identity does NOT match the scheduled gate names. Recorded honestly: the Aug gate-chain mapping in OUT-20260911-001 is amended accordingly.
- ARAS-side signature dated 26 Aug — consistent with the paper's internal 22–27 Aug Gate 4 critical path; CSM countersign 4 Sep completed the pair.

## 3. Deliverables & Flows (per document)

| Deliverable (paper ref) | Direction | Owner (per doc) | Status (per doc) |
|--------------------------|-----------|-----------------|------------------|
| Signature repository, ET Pro-compatible (COM-20260821-002*) | GovSec → CMERP | Ahmad Fuad | Agreed — no external dependency |
| CMERP Sensor Appliance (COM-20260821-003*) | Hosted in Aras env | Tuan Fatah | **PENDING management approval (RSK-20260821-001*) — critical-path blocker** |
| Suricata / TI alert integration (COM-20260821-004*) | CMERP → GovSec | Tuan Fatah (MyCERT CTRC) | Agreed — JSON param sample in hand |

*20260821-series refs are per the paper's provenance appendix; not present in canonical repo (see §6).

| Flow | Path | Format | Auth | State |
|------|------|--------|------|-------|
| A | GovSec → CMERP signatures/IOCs | ET Pro-compatible | Push delivery credentials — **TBD (§6.3 open)** | Designed/proposed |
| B | CMERP sensors → GovSec alerts | Suricata/JSON (CSM sample authoritative) | Push ingestion API, static API key, TLS, 10 MB cap | Proposed — gated on sensor deployment |
| C | LebahNet → GovSec indicators | STIX/TAXII 2.1 | Push ingestion API, static API key | **Present-state ACTIVE** (Fuad-confirmed 22 Aug) |

## 4. Present-State vs Future-State (§1.1, verbatim classification)

| Component | State |
|-----------|-------|
| GovSec TIP | Present-state (MVP) |
| LebahNet honeypot network | Present-state (Active) |
| CMERP signature feed | Designed / Proposed |
| CMERP sensor appliance | Pending approval |
| Suricata alert integration | Proposed |
| SiberSUITE | Future-state |
| CBOM | Future-state |
| Score Card | Future-state |

Consistent with DEC-20260911-003 and the DEC-20260822-001 doctrine — no present-state/future-state conflation inside the signed paper itself.

## 5. Governance & Validation Skeleton (per document)

- **Validation gates (§9.2, §13.1):** Gate 1 Flow A contract (Fuad, 24 Aug) · Gate 2 Flow B JSON-sample ingestion (Fuad, 25 Aug) · Gate 3 sensor appliance live (Tuan Fatah, 26 Aug, management approval on file) · Gate 4 end-to-end loop (Fuad + Tuan Fatah joint, 27 Aug). Named-approver sign-off + dated evidence required; unsigned gates do not count.
- **Open items (§12):** (1) Flow A delivery auth — Aras proposes API key/mTLS, CSM confirms; (2) sensor-appliance management approval; (3) consolidation meeting slot (Aug 18/19/20 lapsed, re-propose); (4) alert SLA push→indexed; (5) confirm CSM JSON sample authoritative; (6) external government IOC feed contributors/format; (7) API key rotation process.
- **Security posture (§6, §9.3):** TLS only; RBAC + classification at route layer; ingestion-only push channel; PDPA 4h PII scan with redaction + access logging; OWASP Web + LLM Top 10 baseline; immutable append-only audit.

## 6. Corpus Observations — Provenance Namespace Divergence (flagged)

The paper's §15.1 provenance appendix cites the following record IDs, which are **NOT present in the canonical strategic-cognitiveos repo** (searched 11 Sep): INIT-20260821-001, STK-20260821-003, RSK-20260821-001, ART-20260821-003, COM-20260821-002/003/004, CONV-20260821-002/003, ACT-20260820-009/010. Canonical records exist for adjacent 20260804/20260826/20260827-series records (INIT-20260804-002, COM-20260827-001) covering the same integration. The 20260821 series likely lives in a parallel lineage (another agent's workspace, cohort-programme repo, or an archived branch). **Action:** map paper refs → canonical equivalents (COM-20260827-001 chain) or ingest the 20260821 series; unresolved cross-namespace references weaken the substantiation pack if left dangling.

## 7. Intake Checklist

| Check | Result |
|-------|--------|
| PDF opens, 21 pages, text extractable | ✅ |
| SHA-256 recorded | ✅ c7a3109d…f09d0 |
| Authorisation block read from page images + text | ✅ names/dates captured |
| Cryptographic signature present | ❌ none (AcroForm fields only) — flagged |
| Signatory vs gate chain reconciled | ⚠️ date ✅ / signatory ≠ Hafiz Rahman/Zaharudin — flagged |
| PDF tracked into repo (private, precedent: Afrina docs) | ✅ |
| PII scan | No personal data beyond signatory names/titles (public-role info) |
