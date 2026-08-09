# Privacy Controls & Personal Data Handling

## Purpose
Ensure compliance with privacy regulations and ethical handling of personal data during research activities.

---

## Personal Data Definition

**Personal Data** includes:
- Names (when combined with other identifiers)
- Contact information (email, phone, address)
- Professional information (title, role, employer)
- Social media profiles and handles
- Photographs/likenesses
- Any identifier that can link to a specific individual

**Special Category Data** (requires extra protection):
- Biometric data
- Political opinions
- Religious beliefs
- Health information
- Sexual orientation
- Ethnic/racial origin

---

## Data Collection Principles

### 1. Data Minimization
**Collect only what is necessary:**
- ✅ Work email addresses for PR outreach
- ✅ Professional titles for stakeholder mapping
- ✅ Public social media handles for contact
- ❌ Personal email addresses
- ❌ Home addresses
- ❌ Family information
- ❌ Private phone numbers

### 2. Purpose Limitation
**Collect only for specified purposes:**
- Account research → Stakeholder identification
- Media registry → PR contact list
- Due diligence → Key personnel assessment
- ❌ No secondary use without consent

### 3. Source Limitation
**Collect only from public, legitimate sources:**
- ✅ Company websites (leadership pages)
- ✅ LinkedIn (public profiles)
- ✅ Publication mastheads
- ✅ Conference speaker lists
- ❌ Hacked/dumped data
- ❌ Private databases without authorization
- ❌ Social media scraping (beyond public profiles)

---

## Mode-Specific Guidelines

### Strategic Account Intelligence

**Permitted:**
- Executive names and titles from company website
- Professional background from LinkedIn
- Public statements/interviews
- Conference appearances

**Prohibited:**
- Personal contact details
- Family information
- Private social media accounts
- Compensation information

**Retention:** 12 months or end of engagement (whichever first)

### Media Registry

**Permitted:**
- Journalist names and titles
- Work email addresses (from publication sites)
- Professional social media handles
- Beat/coverage areas
- Recent bylines

**Prohibited:**
- Personal email addresses
- Personal phone numbers
- Home addresses
- Non-public contact preferences

**Retention:** 90 days with quarterly refresh

### Vendor Due Diligence

**Permitted:**
- Key personnel names and roles
- Professional backgrounds
- Public statements about the company

**Prohibited:**
- Employee personal data
- Compensation details
- Performance reviews

**Retention:** Duration of evaluation + 90 days

### All Other Modes

**General Rule:** Personal data collection should be:
- Incidental to the research objective
- Limited to professional context
- From public sources only
- Retained only as long as necessary

---

## GDPR Compliance (EU Subjects)

### Legal Basis for Processing

**Legitimate Interests** (most common for research):
- Must document legitimate interest
- Must balance against individual rights
- Must allow opt-out

**Consent** (when required):
- Must be explicit, informed, unambiguous
- Must be withdrawable
- Must be documented

### Individual Rights

Research subjects have the right to:
- **Access:** Request what data is held
- **Rectification:** Correct inaccurate data
- **Erasure:** Request deletion ("right to be forgotten")
- **Restriction:** Limit how data is used
- **Portability:** Receive data in portable format
- **Objection:** Object to processing

**Process for Rights Requests:**
1. Log request in tracking system
2. Verify identity of requester
3. Locate all relevant data
4. Respond within 30 days
5. Document action taken

---

## Data Handling Requirements

### Storage

**Requirements:**
- Store in designated evidence store only
- Encrypt at rest
- Access controls (role-based)
- No local downloads without approval
- No personal devices

### Access

**Access Controls:**
- Need-to-know basis
- Named individuals for confidential data
- Access logging enabled
- Regular access reviews

### Transmission

**Secure Transmission:**
- Encrypted email for external
- Secure file transfer for large datasets
- No personal email accounts
- No public file sharing services

### Disposal

**Secure Disposal:**
- Secure delete from all systems
- Confirm deletion from backups (if possible)
- Document disposal date and method
- Certificate of disposal for high-risk data

---

## Retention Schedules

| Data Type | Retention Period | Disposal Method |
|-----------|------------------|-----------------|
| **Account Intel (personal)** | 12 months or engagement end | Secure delete |
| **Media contacts** | 90 days with quarterly refresh | Update or delete |
| **Vendor personnel** | Evaluation + 90 days | Secure delete |
| **General research** | Per task retention policy | Archive or delete |
| **Special category** | Do not collect | N/A |

---

## Human Review Triggers

**Automatically escalate to privacy review when:**

| Trigger | Action |
|---------|--------|
| Special category data encountered | Stop collection, escalate |
| Request for personal email/phone | Review before collection |
| EU subject data for media outreach | Verify legal basis |
| Data subject access request | Forward to privacy officer |
| Potential data breach | Follow incident response |
| Large-scale personal data collection | Privacy impact assessment |

---

## Privacy Impact Assessment (PIA)

**Required when:**
- Systematic collection of personal data
- Large-scale processing
- Sensitive data involved
- New technology/methods used
- High risk to individuals

**PIA Template:**
```yaml
privacy_impact_assessment:
  task_id: "[ID]"
  data_types: "[What personal data]"
  data_subjects: "[Who is affected]"
  data_volume: "[Approximate count]"
  sources: "[Where collected from]"
  purpose: "[Why collecting]"
  legal_basis: "[GDPR legal basis]"
  retention: "[How long keeping]"
  risks: "[Privacy risks identified]"
  mitigations: "[How risks addressed]"
  approval: "[Privacy officer sign-off]"
```

---

## Consent Management

**When Consent is Required:**
- Non-public contact information
- Secondary use of data
- Marketing communications
- Special category data (if ever applicable)

**Consent Record Requirements:**
- Who consented
- What they consented to
- When consent was given
- How consent was obtained
- Evidence of consent

**Withdrawal Process:**
1. Log withdrawal request
2. Cease processing immediately
3. Delete data (unless legal requirement to retain)
4. Confirm deletion to individual
5. Update suppression list

---

## Cross-Border Transfers

**Restrictions:**
- EU personal data cannot leave EU/EEA without safeguards
- Use Standard Contractual Clauses (SCCs) if needed
- Document all transfers
- Verify recipient country adequacy

**Approved Transfer Mechanisms:**
- Adequacy decisions (list of approved countries)
- Standard Contractual Clauses
- Binding Corporate Rules (for intra-company)

---

## Breach Response

**Data Breach Definition:**
- Unauthorized access to personal data
- Accidental or unlawful destruction
- Loss, alteration, or disclosure

**Response Steps:**
1. **Contain:** Stop the breach
2. **Assess:** What data, how many individuals, risk level
3. **Notify:** Internal (privacy officer), external (if required)
4. **Remediate:** Fix the cause
5. **Document:** Record all actions

**Notification Timelines:**
- **Internal:** Immediately upon discovery
- **Regulator:** Within 72 hours (GDPR)
- **Affected Individuals:** Without undue delay (high risk)

---

## Training Requirements

**All researchers must complete:**
- Privacy fundamentals training (annual)
- Role-specific data handling (onboarding)
- Breach response training (annual)
- GDPR/privacy law updates (as applicable)

**Documentation:**
- Training completion records
- Acknowledgment of privacy policy
- Signed confidentiality agreements

---

## Audit & Compliance

**Regular Audits:**
- Quarterly: Access logs review
- Semi-annual: Retention compliance
- Annual: Full privacy audit
- Ad hoc: Upon complaint or incident

**Audit Checklist:**
- [ ] Personal data inventory current
- [ ] Retention schedules followed
- [ ] Access controls working
- [ ] Consent records complete
- [ ] Breach log reviewed
- [ ] Training up to date

---

## Contacts

**Privacy Officer:** [Name, contact]
**Data Protection Officer (if required):** [Name, contact]
**Legal Counsel:** [Name, contact]

---

## Skill Maintenance

**Update this skill when:**
- Privacy laws change
- New data types are encountered
- Processing methods change
- Incidents reveal gaps

**Review frequency:** Quarterly or upon regulatory change
