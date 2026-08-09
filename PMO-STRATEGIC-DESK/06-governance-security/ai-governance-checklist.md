# AI Governance Checklist — PMO Operational Context

**Framework:** Perdana Digital AI Cohort with Aras Integrasi  
**Version:** 1.0  
**Last Updated:** 2026-07-09  
**Applicability:** All AI use cases under Bahagian Data Strategik  
**Review Cadence:** Monthly (first Monday of each month)  
**Owner:** DAF (Aras Integrasi) + PMO Legal/Compliance (Joint)

---

## 🛡️ Governance Domains — Operational Procedures

### 1. Access Control & Authentication

**Purpose:** Ensure only authorised personnel can access AI capabilities and data.

#### 1.1 API Key Management

| Requirement | Status | Implementation Steps | Owner | Evidence | Review Date |
|-------------|--------|---------------------|-------|----------|-------------|
| API key-based authentication | ✅ Implemented | 1. Generate unique key per user<br>2. Send via secure email<br>3. Log issuance in registry<br>4. Set 90-day expiry | Farul | `email-registry.md` | Quarterly |
| Key rotation policy | ⏳ Pending | 1. Set calendar reminder 14 days before expiry<br>2. Generate new key<br>3. Notify user<br>4. Revoke old key<br>5. Log rotation | Farul | Key rotation log | 2026-09-09 |
| Key revocation procedure | ⏳ Pending | 1. Identify reason (termination, compromise, etc.)<br>2. Revoke immediately in API gateway<br>3. Notify affected user<br>4. Document in incident log<br>5. Issue replacement if needed | Farul | Revocation log | On-demand |
| Usage monitoring | ⏳ Pending | 1. Enable API gateway logging<br>2. Set up daily usage reports<br>3. Alert on anomalous patterns (>10x normal)<br>4. Review weekly | Aras Integrasi | Usage dashboard | Weekly |

**Operational Procedure: API Key Issuance**
```
1. Request received via email from Puan Nazilah or delegate
2. Verify requester identity (email domain: @pmo.gov.my)
3. Generate key via API gateway admin panel
4. Log in registry: user, email, date, expiry
5. Send key via separate email (not same thread as request)
6. Request acknowledgment of receipt
7. Set expiry reminder (90 days from issuance)
```

**Operational Procedure: Key Revocation**
```
1. Receive revocation request (email/call)
2. Verify authority (Puan Nazilah, IT Security, or HR for terminations)
3. Revoke key immediately in API gateway
4. Log: user, reason, timestamp, revoker
5. Notify user (if not termination)
6. Issue replacement if business continuity requires
7. Document in monthly governance report
```

---

#### 1.2 Role-Based Access Control (RBAC)

| Requirement | Status | Implementation Steps | Owner | Evidence | Review Date |
|-------------|--------|---------------------|-------|----------|-------------|
| Define roles (Viewer, Analyst, Admin, Approver) | ⏳ Pending | 1. Workshop with Bahagian Data Strategik<br>2. Document permissions per role<br>3. Map users to roles<br>4. Implement in API gateway | DAF + PMO IT | RBAC matrix | 2026-07-20 |
| Multi-factor authentication (MFA) | ⏳ Pending | 1. Assess API gateway MFA capability<br>2. Configure for Admin/Approver roles<br>3. Enroll users<br>4. Test failover | PMO IT + Farul | MFA enrollment log | 2026-08-01 |
| Session timeout | ⏳ Pending | 1. Set idle timeout (30 min recommended)<br>2. Configure absolute timeout (8 hours)<br>3. Implement re-authentication flow<br>4. Test user experience | Farul | Config documentation | 2026-07-25 |
| IP whitelisting | ⏳ Pending | 1. Obtain PMO network IP ranges<br>2. Configure API gateway whitelist<br>3. Test from PMO office<br>4. Document exception process | Farul + PMO IT | Whitelist config | 2026-07-25 |

**RBAC Matrix Template:**

| Role | Query AI | Generate Briefs | Access Logs | Approve Outputs | Manage Users |
|------|----------|-----------------|-------------|-----------------|--------------|
| **Viewer** | ✅ Read-only | ❌ | ❌ | ❌ | ❌ |
| **Analyst** | ✅ Full | ✅ Draft | Own only | ❌ | ❌ |
| **Admin** | ✅ Full | ✅ Full | ✅ All | ❌ | ✅ |
| **Approver** | ✅ Full | ✅ Full | ✅ All | ✅ | ❌ |

---

### 2. Data Security & Classification

**Purpose:** Protect data based on sensitivity level and comply with government regulations.

#### 2.1 Data Classification Enforcement

| Requirement | Status | Implementation Steps | Owner | Evidence | Review Date |
|-------------|--------|---------------------|-------|----------|-------------|
| Data classification (Public/Internal/Confidential/Restricted) | ⏳ Pending | 1. Review assessment Section 2.1<br>2. Tag all ingested data<br>3. Enforce access rules per classification<br>4. Audit quarterly | Bahagian Data Strategik | Classification log | Quarterly |
| Encryption at rest | ⏳ Pending | 1. Confirm storage encryption (AES-256)<br>2. Verify key management<br>3. Test recovery procedure<br>4. Document in security policy | PMO IT | Encryption cert | 2026-08-01 |
| Encryption in transit | ✅ Standard | 1. TLS 1.3 enforced for API<br>2. Verify certificate validity<br>3. Monitor for downgrade attempts | Farul | TLS config | Monthly |
| Data masking for sensitive fields | ⏳ Pending | 1. Identify PII/confidential fields<br>2. Implement masking in API layer<br>3. Test query results<br>4. Document exceptions | Farul + PMO IT | Masking policy | 2026-08-01 |
| Data minimisation | ⏳ Pending | 1. Define minimum data needed per use case<br>2. Review ingestion requests<br>3. Reject over-collection<br>4. Document justification | DAF + Bahagian Data Strategik | Data request log | Per-use-case |
| Cross-border transfer controls | ✅ Compliant | 1. Confirm all processing in Malaysia<br>2. Verify no data leaves country<br>3. Document in compliance report<br>4. Annual audit | Aras Integrasi | Data flow diagram | Annually |

**Operational Procedure: Data Classification Review**
```
1. Receive dataset for ingestion
2. Review data dictionary/sample records
3. Apply classification:
   - Public: No restrictions, can be shared externally
   - Internal: PMO staff only, no external sharing
   - Confidential: Need-to-know basis, encryption required
   - Restricted: Explicit approval required, highest security
4. Tag dataset in metadata registry
5. Notify data owner of classification
6. Log classification decision
7. Set review date (quarterly for Confidential/Restricted)
```

---

### 3. Audit Trail & Traceability

**Purpose:** Maintain complete records of all AI interactions for compliance and investigation.

#### 3.1 Logging Requirements

| Requirement | Status | Implementation Steps | Owner | Evidence | Review Date |
|-------------|--------|---------------------|-------|----------|-------------|
| API usage logging | ⏳ Pending | 1. Enable logging in API gateway<br>2. Capture: timestamp, user, model, action<br>3. Store in secure log store<br>4. Retain 7 years | Farul | Log samples | Monthly |
| Prompt/output archival | ⏳ Pending | 1. Store prompt hash (not raw content for sensitive data)<br>2. Store output hash<br>3. Link to user/session<br>4. Enable retrieval for audit | Farul | Archive schema | 2026-08-01 |
| Evidence traceability | ⏳ Pending | 1. Link outputs to source documents<br>2. Store document IDs in metadata<br>3. Enable "show sources" feature<br>4. Test traceability end-to-end | DAF + Farul | Traceability demo | 2026-08-01 |
| Human approval logging | ⏳ Pending | 1. Implement approval workflow<br>2. Log: approver, timestamp, decision<br>3. Store approval reason<br>4. Link to output | DAF | Approval log | Per-approval |
| Change tracking | ⏳ Pending | 1. Log model updates<br>2. Log config changes<br>3. Log user permission changes<br>4. Monthly change report | Farul | Change log | Monthly |
| Retention policy | ⏳ Pending | 1. Define retention periods (7 years recommended)<br>2. Implement automated deletion<br>3. Test recovery from backup<br>4. Document in policy | PMO IT + Aras | Retention policy | 2026-08-01 |

**Minimum Audit Log Fields:**

| Field | Type | Example | Required |
|-------|------|---------|----------|
| Timestamp | ISO 8601 | `2026-07-09T08:15:32Z` | ✅ |
| User ID | String | `nazilah@pmo.gov.my` | ✅ |
| API Key ID | String | `key_abc123` | ✅ |
| Action | Enum | `query`, `brief`, `classify` | ✅ |
| Model | String | `Qwen/Qwen3.5-397B-A17B` | ✅ |
| Input Hash | SHA-256 | `a3f5...8c2e` | ✅ (for sensitive) |
| Output Hash | SHA-256 | `b7d2...1f9a` | ✅ |
| Duration | ms | `1523` | ✅ |
| Status | Enum | `success`, `error`, `blocked` | ✅ |
| IP Address | IPv4/IPv6 | `202.75.123.45` | ✅ |
| Classification | Enum | `Public`, `Internal`, `Confidential` | ✅ (if applicable) |

**Operational Procedure: Audit Log Review**
```
Weekly Review (Aras Integrasi):
1. Export logs for past 7 days
2. Check for anomalies:
   - Unusual volume (>10x normal)
   - Off-hours access (23:00–06:00)
   - Failed authentication attempts (>5)
   - Access from new IP addresses
3. Document findings
4. Escalate suspicious activity to L2 (Farul)

Monthly Review (PMO IT Security):
1. Review aggregated usage patterns
2. Check compliance with access policies
3. Verify retention policy enforcement
4. Generate monthly governance report
5. Present to Puan Nazilah
```

---

### 4. Human-in-the-Loop Controls

**Purpose:** Ensure AI outputs are reviewed and approved by humans before critical decisions.

#### 4.1 Approval Workflows

| Requirement | Status | Implementation Steps | Owner | Evidence | Review Date |
|-------------|--------|---------------------|-------|----------|-------------|
| Human review for strategic briefs | ⏳ Pending | 1. Define "strategic brief" criteria<br>2. Implement review queue<br>3. Assign approver (Puan Nazilah or delegate)<br>4. Log approval/rejection | DAF | Approval workflow | Per-brief |
| Approval workflow for external outputs | ⏳ Pending | 1. Define "external output" criteria<br>2. Require L3/L4 approval<br>3. Document approval chain<br>4. Store approval records | DAF | External output log | Per-output |
| AI output disclaimer | ⏳ Pending | 1. Draft disclaimer text<br>2. Add to all AI-generated outputs<br>3. Test visibility<br>4. Legal review | DAF + PMO Legal | Disclaimer template | 2026-07-20 |
| Override mechanism | ⏳ Pending | 1. Implement "reject output" button<br>2. Require reason for rejection<br>3. Log overrides<br>4. Analyze patterns monthly | Farul | Override log | Monthly |
| Escalation path | ✅ Defined | 1. Document L1–L4 escalation (see README.md)<br>2. Share with all users<br>3. Test escalation procedure<br>4. Update contact list quarterly | DAF | Escalation matrix | Quarterly |

**Approval Workflow Template:**

```
For Strategic Briefs:
1. Analyst generates brief using AI
2. System flags for review (classification: Internal or higher)
3. Brief routed to approver (Puan Nazilah or delegate)
4. Approver reviews:
   - Accuracy check (spot-verify sources)
   - Completeness check (all key points covered)
   - Sensitivity check (appropriate classification)
5. Approver approves or requests revision
6. If approved: brief released to requester
7. If rejected: returned to analyst with feedback
8. Log: brief ID, approver, decision, timestamp
```

**AI Output Disclaimer (Template):**
```
⚠️ AI-ASSISTED OUTPUT

This document was generated with the assistance of artificial intelligence 
and has been reviewed by [Approver Name] on [Date].

While every effort has been made to ensure accuracy, users should verify 
critical information against original sources. This output should not be 
relied upon as the sole basis for decision-making without human oversight.

For questions or concerns, contact: daf@arasintegrasi.ai

Classification: [Public/Internal/Confidential/Restricted]
```

---

### 5. Compliance & Regulatory

**Purpose:** Ensure all AI operations comply with Malaysian laws and government policies.

#### 5.1 Compliance Matrix

| Regulation | Status | Compliance Steps | Owner | Evidence | Review Date |
|------------|--------|------------------|-------|----------|-------------|
| PDPA 2010 (Personal Data Protection Act) | ⏳ Framework Ready | 1. Identify PII in datasets<br>2. Implement consent tracking<br>3. Enable data subject access requests<br>4. Appoint Data Protection Officer<br>5. Annual PDPA audit | PMO Legal + DPO | PDPA compliance report | Annually |
| Official Secrets Act 1972 | ⏳ Framework Ready | 1. Classify all data per OSA<br>2. Restrict access to cleared personnel<br>3. Implement secure storage<br>4. Annual OSA training for users | PMO Security | OSA training records | Annually |
| MAMPU Security Policies | ⏳ Framework Ready | 1. Review MAMPU circulars<br>2. Map controls to AI system<br>3. Implement gap remediation<br>4. Submit compliance declaration | PMO IT + Aras | MAMPU compliance matrix | 2026-09-01 |
| Agency-specific policies | ⏳ Pending Assessment | 1. Request PMO internal policies<br>2. Review AI-specific clauses<br>3. Implement required controls<br>4. Document exceptions | Bahagian Data Strategik | Policy mapping | Post-assessment |
| Data sovereignty | ✅ Compliant | 1. Confirm all processing in Malaysia<br>2. Verify no cross-border transfer<br>3. Document in data flow diagram<br>4. Annual audit | Aras Integrasi | Data flow diagram | Annually |
| Right to explanation | ⏳ Pending | 1. Implement "explain this output" feature<br>2. Document model reasoning<br>3. Enable source citation<br>4. Train users on interpretation | Farul + DAF | Explanation feature | 2026-08-15 |

**Operational Procedure: PDPA Data Subject Request**
```
1. Receive request from data subject (email/form)
2. Verify identity of requester
3. Log request in DPO registry
4. Search all systems for personal data
5. Compile data inventory
6. Review for exemptions (national security, etc.)
7. Respond within 30 days (PDPA requirement)
8. Provide: data held, sources, purposes, corrections
9. Document response
10. Update DPO log
```

---

### 6. Model Governance

**Purpose:** Ensure AI models are monitored, updated, and retired responsibly.

#### 6.1 Model Lifecycle Management

| Requirement | Status | Implementation Steps | Owner | Evidence | Review Date |
|-------------|--------|---------------------|-------|----------|-------------|
| Model version tracking | ⏳ Pending | 1. Log model version per API call<br>2. Maintain version registry<br>3. Enable rollback capability<br>4. Document breaking changes | Farul | Version log | Per-deployment |
| Model performance monitoring | ⏳ Pending | 1. Define KPIs (accuracy, latency, errors)<br>2. Set up monitoring dashboard<br>3. Alert on degradation (>10% drop)<br>4. Monthly performance report | Farul | Performance dashboard | Monthly |
| Bias/fairness assessment | ⏳ Pending | 1. Identify high-risk use cases<br>2. Test for demographic bias<br>3. Document findings<br>4. Remediate if needed | DAF + PMO Legal | Bias assessment | Per-pilot |
| Model update notification | ⏳ Pending | 1. Draft update notification template<br>2. Send 7 days before deployment<br>3. Document user feedback<br>4. Monitor for issues post-update | Farul | Update notifications | Per-update |
| Fallback mechanism | ⏳ Pending | 1. Identify primary/backup models<br>2. Implement automatic failover<br>3. Test failover quarterly<br>4. Document procedure | Farul | Failover test results | Quarterly |
| Model retirement policy | ⏳ Pending | 1. Define retirement criteria<br>2. Plan migration path<br>3. Notify users 30 days in advance<br>4. Archive model artifacts | Farul | Retirement plan | On-demand |

**Model Performance KPIs:**

| KPI | Target | Measurement | Alert Threshold |
|-----|--------|-------------|-----------------|
| Accuracy | >95% | Human review sample | <90% |
| Latency (p95) | <5 seconds | API gateway metrics | >10 seconds |
| Error rate | <1% | Failed requests / total | >5% |
| Uptime | >99.5% | Availability monitoring | <99% |
| User satisfaction | >80% | Post-interaction survey | <70% |

---

### 7. Risk Management

**Purpose:** Proactively identify, assess, and mitigate risks associated with AI operations.

#### 7.1 Risk Register

| Risk | Likelihood | Impact | Risk Score | Mitigation | Owner | Review Date |
|------|------------|--------|------------|------------|-------|-------------|
| Data leakage | Medium (3) | High (5) | 15 | Encryption, access control, audit logs, DLP | PMO IT + Farul | Monthly |
| Model hallucination | High (4) | Medium (3) | 12 | Human review, evidence traceability, disclaimers | DAF | Per-output |
| Unauthorized access | Medium (3) | High (5) | 15 | MFA, IP whitelisting, key rotation, monitoring | Farul | Weekly |
| Compliance violation | Low (2) | Critical (5) | 10 | Legal review, policy alignment, training | PMO Legal | Quarterly |
| Service disruption | Medium (3) | Medium (3) | 9 | Redundancy, fallback models, SLA monitoring | Farul | Weekly |
| Reputational risk | Medium (3) | High (5) | 15 | Clear disclaimers, human oversight, comms plan | DAF + Puan Nazilah | Per-incident |
| Bias/discrimination | Low (2) | High (5) | 10 | Bias testing, diverse training data, human review | DAF + PMO Legal | Per-pilot |
| Vendor lock-in | Medium (3) | Medium (3) | 9 | Multi-model support, API abstraction, exit plan | Aras Integrasi | Quarterly |

**Risk Score Calculation:**
```
Risk Score = Likelihood (1–5) × Impact (1–5)
- 15–25: Critical (immediate action required)
- 10–14: High (action within 1 week)
- 5–9: Medium (action within 1 month)
- 1–4: Low (monitor, action as needed)
```

**Operational Procedure: Risk Review**
```
Monthly Risk Review (First Monday):
1. Review risk register
2. Update likelihood/impact based on incidents
3. Add new risks identified
4. Close mitigated risks
5. Generate risk report
6. Present to Puan Nazilah
7. Document decisions
```

---

## ✅ Pre-Deployment Checklist

**Use this checklist before any pilot goes live:**

### Phase 1: Development Complete

- [ ] Code reviewed by Farul (CTO)
- [ ] Unit tests passing (>80% coverage)
- [ ] Integration tests passing
- [ ] Performance tests completed (latency <5s p95)
- [ ] Security scan completed (no critical vulnerabilities)

### Phase 2: Governance Review

- [ ] **Access Control:** API keys issued, RBAC defined
- [ ] **Data Classification:** All data sources classified
- [ ] **Encryption:** At rest and in transit verified
- [ ] **Audit Logging:** Enabled and tested
- [ ] **Human Review:** Approval workflow documented
- [ ] **Compliance Review:** Legal/compliance sign-off obtained
- [ ] **Traceability:** Evidence linking implemented
- [ ] **Disclaimer:** AI output disclaimer added
- [ ] **Training:** Users trained on governance requirements
- [ ] **Incident Response:** Escalation path defined
- [ ] **Documentation:** All policies documented and accessible

### Phase 3: Go-Live Approval

- [ ] Pilot scope document approved (Puan Nazilah)
- [ ] Success metrics defined and baselined
- [ ] Rollback plan tested
- [ ] Support contacts distributed
- [ ] Monitoring dashboard live
- [ ] First week check-in scheduled

**Sign-off:**

| Role | Name | Signature | Date |
|------|------|-----------|------|
| **Aras Integrasi (Technical)** | Farul Mohd Ghazali | | |
| **Aras Integrasi (Strategic)** | DAF (Faurani Jaafar) | | |
| **PMO (Business Owner)** | Puan Nazilah | | |
| **PMO (IT Security)** | [TBD] | | |
| **PMO (Legal/Compliance)** | [TBD] | | |

---

## 📋 Audit Requirements

### Audit Schedule

| Audit Type | Frequency | Auditor | Scope | Report To |
|------------|-----------|---------|-------|-----------|
| Operational logs | Weekly | Aras Integrasi | API usage, errors, anomalies | Farul |
| Access patterns | Monthly | PMO IT Security | User access, RBAC compliance | Puan Nazilah |
| Compliance audit | Quarterly | PMO Legal/Compliance | PDPA, OSA, MAMPU | PMO Leadership |
| Full governance review | Annually | External auditor | All domains | PMO DG + Aras CEO |

### Minimum Audit Log Fields

| Field | Description | Retention |
|-------|-------------|-----------|
| Timestamp | ISO 8601 format | 7 years |
| User ID | API key holder | 7 years |
| Action | API call type (query, brief, etc.) | 7 years |
| Model | Model identifier | 7 years |
| Input Hash | Hash of prompt (not raw content for sensitive) | 7 years |
| Output Hash | Hash of response | 7 years |
| Duration | Processing time (ms) | 7 years |
| Status | Success/failure | 7 years |
| IP Address | Request origin | 7 years |
| Classification | Data sensitivity level | 7 years |

---

## 📞 Governance Contacts

| Role | Name | Email | Phone | Availability |
|------|------|-------|-------|--------------|
| **Aras Integrasi — Governance Lead** | DAF (Faurani Jaafar) | daf@arasintegrasi.ai | +6019 434 2727 | 24/7 (urgent) |
| **Aras Integrasi — Technical Lead** | Farul Mohd Ghazali | farul@arasintegrasi.ai | +6017 218 9748 | 24/7 (urgent) |
| **PMO — Data Owner** | [TBD] | [TBD] | [TBD] | Business hours |
| **PMO — IT Security** | [TBD] | [TBD] | [TBD] | 24/7 (PMO SOC) |
| **PMO — Legal/Compliance** | [TBD] | [TBD] | [TBD] | Business hours |
| **PMO — Data Protection Officer** | [TBD] | [TBD] | [TBD] | Business hours |

---

## 📚 Related Documents

| Document | Purpose | Link |
|----------|---------|------|
| Readiness Assessment | Section 2: Data Sensitivity & Governance | `memory/pmo-datalake-readiness-assessment.md` |
| Access Control Policy | RBAC implementation details | `06-governance-security/access-control-policy.md` |
| Audit Trail Requirements | Logging specifications | `06-governance-security/audit-trail-requirements.md` |
| Compliance Matrix | Detailed compliance mapping | `06-governance-security/compliance-matrix.md` |
| Action Items | Governance action items | `01-engagement-tracker/action-items.md` |

---

*This checklist is a living document. Update as governance requirements evolve or new compliance obligations emerge.*

**Next Review Date:** 2026-08-09 (30 days from creation)  
**Owner:** DAF (daf@arasintegrasi.ai) + PMO Legal/Compliance (Joint)  
**Version:** 1.0
