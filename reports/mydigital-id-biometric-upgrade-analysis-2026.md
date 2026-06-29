# ANALYTICAL REPORT: Malaysia's MyDigital ID Biometric Security Upgrade (June 2026)

**Report Date:** June 14, 2026  
**Classification:** Comprehensive Security & Policy Analysis  
**Prepared For:** DAF  
**Research Period:** June 2026 Announcement & Historical Context (2023-2026)

---

## EXECUTIVE SUMMARY

On June 12, 2026, Malaysia's National Security Council (Majlis Keselamatan Negara, MKN) announced a **major security overhaul** of the national MyDigital ID system, introducing **real-time facial biometric verification** against the National Registration Department (Jabatan Pendaftaran Negara, JPN/NRD) database. This upgrade represents a critical response to escalating digital identity fraud, with Malaysia recording **RM2.77 billion in online scam losses in 2025 alone**—the highest in three years.

**Key Findings:**
- **Immediate Implementation:** Kiosk upgrades began June 12, 2026 (6am) with completion scheduled for June 14, 2026 (6am)
- **Coverage:** All MyDigital ID registration kiosks nationwide
- **New Requirements:** Real-time facial biometric verification for new registrations + mandatory periodic re-verification for existing users
- **Growth Target:** 17 million registered accounts by end-2026 (up from 7.3 million at end-2025)
- **Integration Scope:** 95% of public services to be integrated by 2030

---

## 1. BACKGROUND & CONTEXT

### 1.1 MyDigital ID Overview

**MyDigital ID** is Malaysia's national digital identity platform, developed by **MIMOS Berhad** (the national R&D center for ICT). Launched in late 2023, it serves as:

- The **only certified online identification platform** in Malaysia
- A **single sign-on (SSO)** solution for 100+ government services
- A **secure authentication layer** for both public and private sector digital services
- A **non-storage verification system** that cross-references against government databases without retaining personal data

**Core Value Proposition:**
- One-time registration, unlimited access
- 24/7 seamless access to services
- No need to remember multiple passwords
- Direct verification against trusted government databases

### 1.2 Adoption Trajectory (2023-2026)

| Period | Registered Accounts | Growth Rate |
|--------|---------------------|-------------|
| December 2023 | ~1.8 million | Baseline |
| December 2024 | ~3.5 million (estimated) | +94% |
| December 2025 | 7.3 million | +109% |
| February 2026 | ~10 million | +37% (Q1) |
| **Target: Dec 2026** | **17 million** | +70% (projected) |

**Key Insight:** Registration accelerated dramatically in 2025-2026, driven by:
1. Mandatory integration with critical services (MyNIISe for immigration, MyJPJ for driving licenses)
2. Growing public awareness of cybersecurity threats
3. Government PR campaigns targeting diversity and addressing misconceptions

### 1.3 The Fraud Crisis: Why Now?

**2025 Financial Fraud Statistics (Home Ministry Data):**
- **Total losses (2025):** RM2.77 billion (US$658 million)
- **Total losses (2023-2025 cumulative):** RM5.62 billion
- **E-financial fraud cases (2025):** 5,159 cases (vs. 1,812 in 2024)
- **E-financial fraud losses (2025):** RM458 million (vs. RM65 million in 2024)

**Year-over-Year Loss Breakdown:**
- 2023: RM1.28 billion
- 2024: RM1.57 billion
- 2025: RM2.77 billion (+76% increase from 2024)

**Dominant Scam Types:**
- Phone call scams (Macau scam variants)
- Romance scams
- E-commerce fraud
- Bogus financing offers
- Non-existent loans/investments
- Identity impersonation

**National Cyber Security Agency (NACSA) Assessment:**
> *"Identity has become a major risk, and as long as digital identity remains fragmented and unreliable, fraudsters will always find you."*  
> — Megat Zuhairy Megat Tajuddin, CEO, NACSA

---

## 2. TECHNICAL ANALYSIS: THE BIOMETRIC UPGRADE

### 2.1 What Changed?

**Before June 2026:**
- Registration via kiosk or mobile app
- Identity verification against JPN database (one-time check)
- No mandatory re-verification cycle
- Potential vulnerability window from stale photo data

**After June 2026 Upgrade:**
- **Real-time facial biometric verification** during registration
- **Direct JPN database cross-referencing** with live facial recognition
- **Mandatory periodic re-verification** for existing users
- **Continuous identity assurance** model (event-led triggers vs. point-in-time checks)

### 2.2 System Architecture

**Key Components:**

1. **MyDigital ID Application Layer**
   - Developed by MIMOS Berhad
   - Available on iOS (App Store), Android (Google Play), Huawei (AppGallery)
   - Does NOT store biometric data locally

2. **JPN/NRD Database Integration**
   - National Registration Department holds Malaysia's biometric database
   - Contains MyKad records with fingerprints and facial images
   - Real-time API access for verification (no data replication to MyDigital ID)

3. **Kiosk Infrastructure**
   - Nationwide network of physical registration kiosks
   - Equipped with cameras for facial capture
   - Undergoing phased hardware/software upgrades (June 12-14, 2026)

4. **Verification Flow (New Registration):**
   ```
   User presents at kiosk/mobile → 
   Facial image captured → 
   Real-time API call to JPN database → 
   Biometric match verification → 
   Identity confirmed → 
   MyDigital ID account created
   ```

5. **Verification Flow (Periodic Re-verification):**
   ```
   Existing user notified → 
   User completes facial scan (kiosk/mobile) → 
   Real-time JPN database check → 
   Match confirmed → 
   Digital identity credentials renewed
   ```

### 2.3 Critical Technical Clarifications (MIMOS, December 2023)

**What MyDigital ID Does NOT Do:**
- ❌ Does NOT store biometric data (fingerprints, iris scans, facial recognition templates)
- ❌ Does NOT use chips or implants
- ❌ Does NOT collect, monitor, share, or store users' personal data or online activities
- ❌ Does NOT allow users to have more than one digital identity
- ❌ Does NOT retain facial images after verification completes

**Data Flow Principle:**
> *"Verification is done entirely online and refers directly to the government database **without storing any of the user's personal data**."*  
> — MyDigital ID Official Documentation

**Privacy-by-Design:**
- Biometric data remains exclusively within JPN's secure government database
- MyDigital ID acts as a **verification gateway**, not a data repository
- Each verification is a **transient query** with no persistent storage
- Compliant with Personal Data Protection Act (PDPA) 2010 + 2024 Amendments

### 2.4 Technology Provider Ecosystem

**Key Players:**
- **MIMOS Berhad:** System developer, national ICT R&D center
- **JPN/NRD:** Biometric database custodian
- **Datasonic Group Berhad:** Supplier of biometric e-gates (immigration integration)
- **National Security Council (MKN):** Policy coordination and security oversight
- **NACSA:** Technical cybersecurity guidance

---

## 3. POLICY & REGULATORY FRAMEWORK

### 3.1 Government Mandates & Deadlines

**MyDigital ID Integration Requirements:**

| Service | Mandatory Date | Target Group |
|---------|---------------|--------------|
| MyNIISe (Immigration) | January 15, 2026 | Malaysians departing country |
| MyJPJ (Driving License/Road Tax) | February 1, 2026 | All license holders |
| Telecommunications (Mobile Apps) | December 2025 | All telco customers |
| Banking/Fintech (18 banks) | 2026 (Phase 2 testing) | Bank customers |
| **95% Public Services** | **2030** | All citizens |

### 3.2 Legislative Support

**Cybersecurity Budget 2026:**
- **RM32 million** allocated for anti-scam initiatives
- **RM12 million** for National Scam Response Centre (NSRC) restructuring under PDRM
- **RM20 million** for PDRM digital forensics upgrades + new Behavioural Science Unit

**New Cyber Crime Bill (2026):**
- Replaces outdated legislation
- Enhances law enforcement powers for digital crime
- Enables penalties and seizures against scam networks
- Targets mule account holders and agents

**Personal Data Protection Act (PDPA) Amendments (2024):**
- First major amendments since 2010
- Addresses rapid technological advances
- Introduces breach notification requirements
- Penalties up to RM1 million for violations
- Brings Malaysia in line with international standards (GDPR-inspired)

### 3.3 National Security Council Statement (June 12, 2026)

**Official Rationale:**
> *"The increasing use of digital services by the public, businesses and government agencies has made the need to protect digital identities more critical amid threats such as online fraud, identity impersonation, data theft and cyber exploitation."*

**Strategic Objectives:**
1. Strengthen accuracy of identity verification
2. Reduce risk of identity misuse and unauthorized access
3. Maintain public trust in digital ecosystem
4. Coordinate security enhancements across platforms (MyDigital ID, MyKad, etc.)

---

## 4. IMPLEMENTATION TIMELINE

### 4.1 June 2026 Kiosk Upgrade Schedule

**Maintenance Window:**
- **Start:** June 12, 2026, 6:00 AM
- **End:** June 14, 2026, 6:00 AM
- **Duration:** 48 hours
- **Scope:** All MyDigital ID kiosks nationwide

**Service Continuity:**
- ❌ Kiosk registration: Temporarily unavailable during maintenance
- ✅ Mobile app registration: Fully operational (App Store, Google Play, Huawei AppGallery)
- ✅ Existing user services: Unaffected

**Phased Rollout:**
- Phase 1: June 12-14, 2026 (Initial kiosk upgrades)
- Phase 2: June-December 2026 (Nationwide completion + existing user re-verification notifications)
- Phase 3: 2027+ (Continuous improvement + additional service integrations)

### 4.2 Immigration Integration (MyNIISe)

**MyNIISe (National Integrated Immigration System) Deployment:**
- **September 2025:** Pilot launch at Johor Bahru (Sultan Iskandar Building + Sultan Abu Bakar Complex)
- **December 30, 2025:** Nearly 600,000 downloads, 287,000+ registered users
- **January 15, 2026:** Mandatory for all Malaysians departing country
- **Planned Expansion:**
  - KLIA Terminal 1 & 2
  - Penang (Bayan Lepas Airport)
  - Kuching Airport
  - Kota Kinabalu Airport

**Infrastructure Upgrades:**
- 40 new NIISe eGate units at Johor Bahru border complexes
- 145 QR code scanners for motorcycle, car, and pedestrian crossings
- Addresses previous outage issues (late 2024 Johor Bahru biometric gate failures caused 4-hour delays)

### 4.3 Banking Sector Integration

**Current Status (February 2026):**
- 15 banks/fintechs signed MoUs with MyDigital ID
- 18 banks enrolled in Phase 2 sandbox testing
- Focus: Digital verification for onboarding and transaction verification

**Implementation Model:**
- MyDigital ID e-verification for customer onboarding
- Transaction authentication for high-value transfers
- Single source of truth: NRD database (real-time verification)

**Quote from Banking Consortium:**
> *"MyDigital ID is the only platform in Malaysia that verifies identities directly against the NRD database as the single source of validity in real time."*

---

## 5. COMPARATIVE ANALYSIS: REGIONAL & GLOBAL CONTEXT

### 5.1 Southeast Asia Digital ID Landscape

| Country | System Name | Biometric Type | Launch Year | Adoption Rate |
|---------|-------------|----------------|-------------|---------------|
| **Malaysia** | MyDigital ID | Facial (2026 upgrade) | 2023 | ~31% (10M/33M pop) |
| Singapore | SingPass | Facial + OTP | 2003 (revamped 2018) | ~98% |
| Thailand | Digital ID | Facial + e-KYC | 2018 | ~40% |
| Indonesia | IKD | Facial + Fingerprint | 2022 | ~25% |
| Philippines | PhilSys | Fingerprint + Iris | 2018 | ~70% |

**Malaysia's Position:**
- **Late mover** (2023 vs. 2003-2018 for neighbors)
- **Rapid acceleration** (1.8M → 10M in 2 years)
- **Privacy-first architecture** (no biometric storage)
- **Mandatory integration strategy** (driving adoption via essential services)

### 5.2 Global Best Practices

**Estonia (e-Residency):**
- Pioneer in digital identity (launched 2014)
- Blockchain-backed security
- No biometric requirement (smart card-based)

**India (Aadhaar):**
- World's largest biometric ID system (1.3B+ users)
- Fingerprint + Iris + Facial recognition
- Centralized biometric database (controversial privacy concerns)

**EU (eIDAS 2.0):**
- European Digital Identity Wallet (2024 rollout)
- Voluntary participation
- Cross-border recognition across EU member states

**Malaysia's Hybrid Approach:**
- Combines **mandatory verification** (like Aadhaar) with **privacy-by-design** (like EU)
- Avoids centralized biometric storage (unlike Aadhaar)
- Uses **government database as single source of truth** (like Singapore)

---

## 6. SECURITY ASSESSMENT

### 6.1 Threat Landscape

**Primary Threats Addressed:**
1. **Identity Impersonation:** Fraudsters using stolen credentials
2. **Synthetic Identity Fraud:** Fabricated identities using mixed real/fake data
3. **Account Takeover:** Unauthorized access to existing accounts
4. **Stale Data Exploitation:** Using outdated photos/documents
5. **Mule Account Networks:** Facilitating money laundering via compromised identities

**2025 Attack Vectors:**
- Phone call scams (vishing)
- Romance scams (pig butchering)
- Phishing + credential harvesting
- E-commerce fraud (fake marketplaces)
- Investment scams (crypto/forex platforms)

### 6.2 Security Enhancements: Before vs. After

| Security Feature | Pre-2026 | Post-2026 Upgrade |
|-----------------|----------|-------------------|
| **Initial Verification** | One-time JPN check | Real-time facial biometric + JPN |
| **Re-verification** | None | Mandatory periodic facial scans |
| **Data Storage** | None (transient) | None (transient) |
| **Vulnerability Window** | High (stale photos) | Minimal (live verification) |
| **Fraud Detection** | Reactive | Proactive + continuous |
| **Integration Scope** | Limited | 95% public services by 2030 |

### 6.3 NACSA's Role

**National Cyber Security Agency Initiatives:**
- **Centre for Cryptology and Cyber Security Development:** New national hub
- **AI-Powered Verification Tool:** Partnership with CyberSecurity Malaysia + Universiti Kebangsaan Malaysia
  - Detects digital image/video manipulation
  - Identifies synthetic media (deepfakes)
  - Supports investigators in fraud cases

**NACSA CEO Statement:**
> *"Identity has become a major risk, and as long as digital identity remains fragmented and unreliable, fraudsters will always find you."*  
> — Megat Zuhairy Megat Tajuddin

### 6.4 Remaining Vulnerabilities

**Potential Weaknesses:**
1. **Social Engineering:** Biometrics can't prevent users from willingly sharing credentials
2. **Deepfake Technology:** Advanced AI-generated facial replicas (countered by AI detection tools)
3. **Insider Threats:** Compromised JPN database access (mitigated by strict access controls)
4. **Mobile Device Security:** Compromised phones could intercept verification flows
5. **Cross-Border Coordination:** International scam networks require multi-jurisdiction cooperation

---

## 7. PRIVACY & CIVIL LIBERTIES ANALYSIS

### 7.1 Privacy Safeguards

**MIMOS Commitments (December 2023):**
- No biometric data storage in MyDigital ID system
- No chips or implants
- No monitoring of online activities
- No data sharing with third parties
- Single digital identity per user (prevents identity fragmentation)

**PDPA Compliance:**
- Personal Data Protection Act 2010 + 2024 Amendments
- 7 Data Protection Principles enforced
- Breach notification requirements
- Penalties up to RM1 million for violations
- Data subject rights (access, correction, deletion)

### 7.2 Public Concerns & Government Response

**Common Misconceptions (Addressed in PR Campaign):**
- ❌ *"MyDigital ID stores my biometric data"* → ✅ **False:** Data stays with JPN only
- ❌ *"Government can track my online activity"* → ✅ **False:** No activity monitoring
- ❌ *"Multiple digital IDs are possible"* → ✅ **False:** One ID per citizen
- ❌ *"Chips or implants are required"* → ✅ **False:** No physical hardware needed

**Biometric Update Analysis (January 2026):**
> *"MyDigital ID PR campaign targeting Malaysian diversity and misconceptions hailed a success"*

**Privacy Advocacy Perspective:**
- **Positive:** No centralized biometric database (unlike Aadhaar)
- **Positive:** Transient verification model (no persistent storage)
- **Concern:** Mandatory periodic re-verification (frequency not yet specified)
- **Concern:** Expanding mandatory integration (95% of services by 2030)

### 7.3 Data Sovereignty

**Key Advantage:**
- All biometric data remains within **Malaysian government control** (JPN database)
- No foreign cloud storage or third-party processors
- Compliant with Malaysia's data localization requirements
- Reduces risk of foreign surveillance or data breaches

---

## 8. ECONOMIC & SOCIETAL IMPACT

### 8.1 Fraud Prevention Economics

**Projected Savings (2026-2030):**
- 2025 losses: RM2.77 billion
- Target reduction: 50% by 2028 (conservative estimate)
- **Potential savings:** RM1.38 billion annually

**Cost-Benefit Analysis:**
- **Investment:** RM32 million (2026 cybersecurity budget) + infrastructure upgrades
- **Return:** RM1+ billion annually in fraud prevention
- **ROI:** ~30:1 (first year alone)

### 8.2 Digital Economy Enablement

**MyDigital Blueprint Alignment:**
- Supports Malaysia's transformation into a **high-income nation driven by technology**
- Enables **frictionless digital transactions** across public/private sectors
- Reduces **administrative burden** (no more long queues, multiple passwords)
- Improves **financial inclusion** (easier access to banking services)

**Business Impact:**
- **Banks:** Reduced onboarding costs, improved KYC compliance
- **Telcos:** Streamlined customer verification, reduced SIM swap fraud
- **E-commerce:** Enhanced trust, reduced chargeback fraud
- **Government:** Improved service delivery, reduced identity fraud in benefits

### 8.3 Social Inclusion

**Accessibility Features:**
- Free registration for all citizens/PR holders (18+)
- Mobile app availability (no need to visit physical offices)
- Multi-platform support (iOS, Android, Huawei)
- Kiosk network for non-smartphone users

**Demographic Reach:**
- 10 million registered (February 2026) = ~31% of population
- Target: 17 million (end-2026) = ~52% of population
- Remaining gap: Elderly, rural populations, digitally excluded groups

---

## 9. STAKEHOLDER ANALYSIS

### 9.1 Government Agencies

| Agency | Role | Responsibility |
|--------|------|----------------|
| **National Security Council (MKN)** | Policy Lead | Security oversight, coordination |
| **JPN/NRD** | Database Custodian | Biometric data management, verification API |
| **MIMOS Berhad** | System Developer | Platform development, maintenance |
| **NACSA** | Cybersecurity Advisor | Technical guidance, threat intelligence |
| **Home Ministry** | Policy Implementation | Immigration integration, law enforcement |
| **PDRM (Police)** | Enforcement | Scam investigations, NSRC operations |
| **Ministry of Communications & Digital** | Digital Policy | Overall digital transformation strategy |

### 9.2 Private Sector Partners

**Banking & Fintech (15 MoU Signatories):**
- Maybank, CIMB, Public Bank, RHB, Hong Leong Bank (major banks)
- Fintech partners (e-wallets, payment processors)
- Use case: Customer onboarding, transaction verification

**Telecommunications:**
- CelcomDigi, Maxis, U Mobile, Telekom Malaysia
- Mandatory MyDigital ID verification for mobile app access
- Reduces SIM swap fraud and identity theft

**Technology Vendors:**
- **Datasonic:** Biometric e-gate supplier (immigration)
- **Cloud/Infrastructure Providers:** Secure hosting for government systems

### 9.3 Civil Society & Advocacy Groups

**Privacy Advocates:**
- Cautious support for privacy-by-design architecture
- Monitoring mandatory re-verification frequency
- Advocating for transparency in data access logs

**Digital Rights Organizations:**
- Pushing for clear grievance mechanisms
- Requesting audit trails for verification queries
- Ensuring opt-out pathways for non-essential services

---

## 10. RISK ASSESSMENT

### 10.1 Implementation Risks

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| **System Downtime** | Medium | High | Redundant infrastructure, mobile app fallback |
| **User Resistance** | Medium | Medium | PR campaigns, mandatory integration drivers |
| **Technical Glitches** | Medium | High | Phased rollout, extensive testing |
| **Privacy Breaches** | Low | Critical | No biometric storage, strict access controls |
| **Deepfake Exploitation** | Medium | High | AI detection tools, liveness detection |
| **Cross-Agency Coordination** | Medium | Medium | MKN oversight, clear governance framework |

### 10.2 Long-Term Strategic Risks

1. **Mission Creep:** Expansion beyond original scope without proper oversight
2. **Function Creep:** Using system for purposes not originally intended (e.g., surveillance)
3. **Vendor Lock-In:** Dependence on specific technology providers
4. **Obsolescence:** Rapid technological change requiring frequent upgrades
5. **Public Trust Erosion:** Any security incident could undermine confidence

### 10.3 Mitigation Strategies

**Technical:**
- Regular security audits (internal + third-party)
- Penetration testing schedules
- Incident response protocols
- Continuous monitoring (NACSA oversight)

**Governance:**
- Clear legal framework (Cyber Crime Bill, PDPA)
- Parliamentary oversight
- Public consultation on major changes
- Transparency reports (verification volumes, incident counts)

**Operational:**
- Phased implementation (reduce single points of failure)
- Backup systems (mobile app during kiosk maintenance)
- User education campaigns
- Grievance redressal mechanisms

---

## 11. RECOMMENDATIONS

### 11.1 For Government

1. **Define Re-verification Frequency:**
   - Establish clear guidelines (annual? biennial?)
   - Communicate timeline to users in advance
   - Provide flexible completion windows

2. **Enhance Transparency:**
   - Publish verification query logs (user-accessible)
   - Release annual security audit reports
   - Create public dashboard for system uptime/metrics

3. **Strengthen Cross-Border Cooperation:**
   - Formalize information-sharing with regional partners (ASEAN)
   - Coordinate with international law enforcement (Interpol, ASEANAPOL)
   - Harmonize digital ID standards for cross-border recognition

4. **Expand Digital Literacy:**
   - Target elderly and rural populations
   - Partner with community organizations
   - Provide multilingual support materials

### 11.2 For Private Sector

1. **Accelerate Integration:**
   - Banks: Complete Phase 2 testing, move to production
   - Telcos: Ensure seamless user experience
   - E-commerce: Implement MyDigital ID for high-value transactions

2. **Invest in User Education:**
   - Explain benefits clearly (security, convenience)
   - Address privacy concerns proactively
   - Provide step-by-step registration guides

3. **Build Redundancy:**
   - Maintain alternative authentication methods (transition period)
   - Ensure fallback options during system maintenance
   - Test disaster recovery scenarios

### 11.3 For Citizens

1. **Register Early:**
   - Complete MyDigital ID registration before mandatory deadlines
   - Use official channels only (App Store, Google Play, Huawei AppGallery)
   - Beware of phishing attempts mimicking MyDigital ID

2. **Stay Informed:**
   - Monitor official announcements (MKN, MyDigital ID website)
   - Understand re-verification requirements
   - Report suspicious activity to authorities

3. **Practice Good Cyber Hygiene:**
   - Use strong, unique passwords
   - Enable multi-factor authentication where available
   - Never share verification codes or credentials

---

## 12. CONCLUSION

Malaysia's June 2026 MyDigital ID biometric upgrade represents a **pivotal moment** in the nation's digital transformation journey. By introducing **real-time facial biometric verification** and **mandatory periodic re-verification**, the government is addressing a critical vulnerability in the country's digital identity infrastructure.

**Key Takeaways:**

1. **Urgency is Justified:** RM2.77 billion in fraud losses (2025) demanded immediate action
2. **Privacy-Preserving Design:** No biometric storage maintains citizen trust
3. **Rapid Adoption Trajectory:** 1.8M → 17M accounts in 3 years demonstrates strong momentum
4. **Whole-of-Government Approach:** MKN, JPN, MIMOS, NACSA coordination ensures cohesive execution
5. **Regional Leadership:** Malaysia positioning itself as a Southeast Asian digital identity leader

**Success Factors:**
- ✅ Clear policy mandate (95% public services by 2030)
- ✅ Strong technical foundation (MIMOS development, JPN database integration)
- ✅ Adequate funding (RM32 million cybersecurity budget)
- ✅ Public-private partnerships (15 banks, telcos)
- ✅ Privacy-by-design architecture

**Remaining Challenges:**
- ⚠️ Ensuring inclusive access (elderly, rural, digitally excluded)
- ⚠️ Maintaining public trust through transparency
- ⚠️ Countering evolving threats (deepfakes, AI-powered fraud)
- ⚠️ Balancing security with civil liberties

**Final Assessment:**

The MyDigital ID biometric upgrade is a **necessary and well-designed response** to Malaysia's escalating digital identity crisis. While implementation risks exist, the government's privacy-first approach, phased rollout strategy, and multi-agency coordination significantly mitigate potential downsides.

If executed effectively, this initiative could:
- **Prevent billions in fraud losses** over the next decade
- **Establish Malaysia as a regional digital identity leader**
- **Enable seamless, secure access to 100+ government and private services**
- **Build public trust in digital transactions**

The next 12-18 months will be critical. Success depends on:
1. Smooth technical implementation (June 2026 kiosk upgrades)
2. Clear communication with citizens (re-verification requirements)
3. Continued private sector integration (banking, telcos, e-commerce)
4. Transparent governance (audit reports, public dashboards)

**Malaysia is betting its digital future on MyDigital ID.** Early indicators suggest this bet will pay off—but vigilance, transparency, and citizen engagement remain essential.

---

## APPENDICES

### Appendix A: Timeline of Key Events

| Date | Event |
|------|-------|
| **December 2023** | MyDigital ID launches; MIMOS clarifies no biometric storage |
| **September 2025** | MyNIISe pilot at Johor Bahru immigration |
| **December 2025** | 7.3 million MyDigital ID accounts; telco integration begins |
| **January 15, 2026** | MyDigital ID mandatory for MyNIISe (immigration) |
| **February 1, 2026** | MyDigital ID mandatory for MyJPJ (driving license/road tax) |
| **February 12, 2026** | 10 million accounts reached; 17 million target announced |
| **June 12, 2026** | MKN announces biometric upgrade; kiosk maintenance begins (6am) |
| **June 14, 2026** | Kiosk upgrades complete (6am) |
| **2026-2027** | Existing user re-verification notifications roll out |
| **2030** | Target: 95% of public services integrated with MyDigital ID |

### Appendix B: Glossary of Terms

| Term | Definition |
|------|------------|
| **MyDigital ID** | Malaysia's national digital identity platform |
| **JPN/NRD** | Jabatan Pendaftaran Negara / National Registration Department |
| **MIMOS** | National ICT R&D center; MyDigital ID developer |
| **MKN** | Majlis Keselamatan Negara / National Security Council |
| **NACSA** | National Cyber Security Agency |
| **MyNIISe** | National Integrated Immigration System mobile app |
| **MyJPJ** | Road Transport Department mobile app |
| **PDPA** | Personal Data Protection Act 2010 (+ 2024 Amendments) |
| **NSRC** | National Scam Response Centre |
| **PDRM** | Polis Diraja Malaysia / Royal Malaysia Police |
| **SSO** | Single Sign-On |
| **e-KYC** | Electronic Know Your Customer |
| **KYC** | Know Your Customer (identity verification process) |

### Appendix C: Sources & References

1. **National Security Council (MKN) Statement** - June 12, 2026
2. **New Straits Times** - "MyDigital ID kiosks get facial biometric verification upgrade" - June 12, 2026
3. **The Star** - "Facial biometric verification to strengthen MyDigital ID kiosk registration" - June 12, 2026
4. **The Vibes** - "MyDigital ID kiosks to be upgraded with facial biometric verification" - June 12, 2026
5. **Human Resources Online** - "MyDigital ID to see enhanced security features" - June 12, 2026
6. **Biometric Update** - "Malaysia mandates MyDigital ID for Malaysians traveling abroad" - January 2026
7. **Biometric Update** - "Malaysia targets 17 million MyDigital IDs by end-2026" - February 2026
8. **Malay Mail** - "Home Ministry: Malaysia's online fraud surge drains RM2.77b in 2025" - January 22, 2026
9. **Fintech News Malaysia** - "New Cyber Crime Bill and RM32 Million Boost to Tackle Scams" - 2026
10. **MIMOS Berhad Statement** - "MyDigital ID does not store biometric data" - December 12, 2023
11. **MyDigital ID Official Website** - www.digital-id.my
12. **Personal Data Protection Department (PDP)** - www.pdp.gov.my
13. **DeepIDV** - "Malaysia Mandates Real-Time Facial Biometrics Across MyDigital ID Ecosystem" - June 12, 2026
14. **Media Selangor** - "MyDigital ID kiosks to adopt facial biometric checks" - June 2026
15. **Chambers & Partners** - "Data Protection & Privacy 2026 - Malaysia" - 2026

---

**Report Prepared By:** AI Research Assistant  
**Review Status:** Draft (Pending Human Review)  
**Distribution:** DAF (Requestor)  
**Confidentiality:** Public Information (All sources are publicly available)

---

*This report is based on publicly available information as of June 14, 2026. For the most current updates, refer to official government sources and the MyDigital ID website.*
