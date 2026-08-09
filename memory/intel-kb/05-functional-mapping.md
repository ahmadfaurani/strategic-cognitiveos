# Functional Mapping - PMO BKS Operational Mandate

**Last Updated:** 2026-06-30  
**Status:** ✅ Complete (Core Functions)  
**Classification:** INTERNAL REFERENCE (DAF operational intel)  
**Verification Status:** [HIGH] - Direct from operational source

---

## 1. BLUF (Bottom Line Up Front)

**Operational Mandate:**
The Bahagian Keselamatan Strategik (PMO BKS) protects the **executive branch's decision advantage** by identifying, neutralizing, and pre-empting **Foreign Information Manipulation and Interference (FIMI)**.

**Strategic Context:**
As emphasized during the National Cyber Security Committee meeting (chaired by Prime Minister), the threat landscape has drastically accelerated due to **Frontier AI models** (e.g., Anthropic Mythos class). These models enable adversaries to:
- Automate synthetic narrative generation
- Execute precise micro-targeting campaigns at scale
- Adapt narratives in real-time based on sentiment monitoring

**Operational Philosophy:**
> PMO BKS treats information space **not merely as a public relations theater**, but as a **contested combat domain**.

**Technical Standard:**
BKS uses the **DISARM Framework** mapped directly to **STIX 2.1 data objects** to track and disrupt adversarial campaigns in real-time.

---

## 2. Core Functions by Unit

### 2.1 Unit Ancaman Kognitif (Cognitive Threat Unit)

**Primary Mission:** Counter Foreign Information Manipulation and Interference (FIMI)

**Operational Framework:** Cognitive OODA Disruption Architecture

| Function | Description | Tools/Methods |
|----------|-------------|---------------|
| **FIMI Detection** | Identify foreign-backed information operations targeting Malaysian sovereignty | DISARM Red TTP mapping, OSINT scraping, semantic fingerprinting |
| **Narrative Analysis** | Deconstruct adversarial narratives to identify origin, intent, and target demographics | Stylometric analysis, network graph mapping |
| **Campaign Disruption** | Active counter-measures to degrade adversary operational capacity | MCMC platform hooks, cryptographic verification, exposure operations |
| **Executive Protection** | Ensure PM/PMO communications remain uncompromised by synthetic media | Cryptographic signing, deepfake detection, secure channels |

**Threat Classification:**
| Type | Timeline | Target OODA Phase | Examples |
|------|----------|-------------------|----------|
| **Acute Cognitive Disruption** | Short horizon (minutes to days) | Observe, Act | Deepfaked executive orders, synthetic bank runs, panic-inducing fabrications |
| **Chronic Cognitive Conditioning** | Long horizon (months to years) | Orient, Decide | Cultural/religious fault line exploitation, institutional trust degradation, social cohesion erosion |

---

### 2.2 Unit Risiko Sistemik & Rantaian Bekalan (Systemic Risk & Supply Chain Unit)

**Primary Mission:** Protect critical economic infrastructure from information-enabled attacks

**Operational Focus:**
| Function | Description | Inter-Agency Partners |
|----------|-------------|----------------------|
| **Supply Chain Intelligence** | Monitor information operations targeting food/energy supply chains | Ministry of Agriculture, Ministry of Energy, TNB, PPN |
| **Economic Narrative Defense** | Counter false narratives designed to trigger market panic, capital flight, or currency instability | Bank Negara, Securities Commission, Ministry of Finance |
| **Critical Infrastructure Protection** | Coordinate with CNII owners on information security aspects of physical infrastructure | NACSA, sector regulators, infrastructure operators |
| **Cascade Risk Analysis** | Model how information operations could trigger real-world economic disruption | BKS analysts, economic intelligence units |

**Threat Scenarios:**
- Synthetic rumors of food shortage → panic buying → actual shortage
- Fake central bank announcement → currency volatility → capital flight
- AI-generated "leak" of infrastructure vulnerability → public panic → service disruption

---

### 2.3 Unit Penilaian Polisi & Ketahanan Nasional (Policy Assessment & National Resilience Unit)

**Primary Mission:** Ensure high-impact policies are resistant to foreign influence and information attacks

**Operational Focus:**
| Function | Description | Output Products |
|----------|-------------|-----------------|
| **Policy Security Impact Assessment** | Evaluate proposed policies for vulnerability to information exploitation | Pre-implementation risk briefings |
| **Foreign Influence Detection** | Identify foreign state actors attempting to shape Malaysian policy via information operations | Attribution reports, threat actor profiles |
| **National Resilience Framework** | Develop whole-of-society resilience against cognitive attacks | Public education campaigns, media literacy programs |
| **Strategic Communications Planning** | Coordinate government messaging to pre-empt adversarial narrative exploitation | Pre-bunking campaigns, rapid response protocols |

---

## 3. DISARM Framework Operationalization

### Overview

**DISARM** (Disinformation, Misinformation, and Malinformation) Framework provides standardized taxonomy for tracking information operations.

**BKS Implementation:**
- **DISARM Red:** Dissect attacker Tactics, Techniques, and Procedures (TTPs)
- **DISARM Blue:** Deploy precise counter-measures
- **STIX 2.1 Mapping:** Machine-readable intelligence for tactical network integration

---

### Threat Mapping & Mitigation Matrix

| DISARM Red Tactic (Attacker) | Observed Technique Signature | PMO BKS Blue Countermeasure | Target OODA Layer |
|------------------------------|------------------------------|------------------------------|-------------------|
| **TA14: Develop Narratives** | AI-generated "fake research" documents, skewed whitepapers designed to alter policy perception | **Inoculation / Pre-bunking:** Deploy authoritative data arrays to verified nodes prior to campaign maturation | Orient |
| **TA15: Establish Social Assets** | Coordinated Inauthentic Behavior (CIB) using high-fidelity persona bots running localized dialects | **Asset Isolation & Takedown:** Trigger expedited legal/technical removal via MCMC/SKMM platform hooks | Observe |
| **TA07: Select Channels & Affordances** | Cross-platform coordinate pivoting (e.g., seed on closed Telegram, amplify via TikTok algorithm exploits) | **Network Graph Interdiction:** Map structural topology of propagation path to block amplification bots before trend-saturation | Decide |
| **TA02: Objective Planning** | "Sharp Power" projections engineered to destabilize specific regional bilateral relations | **Expose Actor Signatures:** Attribute behavioral signatures to known state-sponsored threat groups publicly | All Layers |

---

### DISARM TTP Library (BKS Catalog)

**Tactics Tracked:**
- TA01: Establish Strategic Intent
- TA02: Objective Planning
- TA03: Target Analysis
- TA04: Develop Content
- TA05: Create Delivery Mechanisms
- TA06: Establish Infrastructure
- TA07: Select Channels & Affordances
- TA08: Drive Discovery
- TA09: Maximize Exposure
- TA10: Influence Target Audience
- TA11: Measure Effectiveness
- TA12: Adapt & Evolve
- TA13: Sustain Operations
- TA14: Develop Narratives
- TA15: Establish Social Assets
- TA16: Build Audience
- TA17: Deliver Content

**Note:** Full DISARM framework documentation at disarmframework.org

---

## 4. Frontier AI & Synthetic Narrative Defense

### The Threat Shift

**Pre-Frontier AI Era:**
- Rigid content scripts
- Manual narrative adjustment
- Limited scale, slower adaptation

**Post-Frontier AI Era (Anthropic Mythos Class+):**
- Real-time LLM-driven agents
- Dynamic narrative adjustment based on sentiment monitoring
- Automated micro-targeting at population scale
- Synthetic media (deepfakes, AI-generated "evidence")

---

### BKS Defensive Pipelines

#### 4.1 Semantic & Stylometric Fingerprinting

**Method:**
- Automated scraping engines analyze high-velocity text patterns across known echo chambers
- While content varies, underlying semantic architecture often betrays machine-generated origin
- Stylometric markers (sentence structure, vocabulary patterns, rhetorical devices) create unique "fingerprints"

**Detection Signatures:**
| Marker | Human-Generated | AI-Generated |
|--------|-----------------|--------------|
| Sentence variance | High | Low (optimized for clarity) |
| Emotional inconsistency | Natural | Often flat or exaggerated |
| Citation patterns | Variable | Often hallucinated or generic |
| Temporal awareness | Contextual | May show training cutoff artifacts |
| Dialect consistency | Native | May show training data bias |

**Tools:**
- Custom NLP pipelines
- Open-source stylometry libraries
- Proprietary BKS classification models

---

#### 4.2 Cryptographic Verification Anchors

**Policy Basis:** National directives on cryptology and post-quantum preparedness

**Implementation:**
- All official executive communications and policy updates are **cryptographically signed at source**
- Distribution platforms (government websites, official social media, press agencies) verify signatures before publishing
- Any altered variant or deepfake can be **instantly programmatically identified** as illegitimate by automated scrapers

**Technical Stack:**
- Digital signatures (RSA/ECC, transitioning to post-quantum algorithms)
- Blockchain-based timestamping (for public verification)
- API integration with major platforms (Meta, TikTok, X, Telegram)

**Example Flow:**
```
1. PMO issues policy statement
2. Document cryptographically signed (private key, BKS HSM)
3. Signature + document hash published to verification ledger
4. Platforms scrape + verify before amplifying
5. Unsigned/modified variants flagged + deprioritized
```

---

## 5. Cross-Agency Operational Pipeline

### Intelligence Flow Architecture

```
┌─────────────────────────────────────────────────────────────┐
│              MULTI-VECTOR INPUT STREAMS                     │
├─────────────────────────────────────────────────────────────┤
│  • OSINT Scrapers (Web, Social Media, Alternative Platforms)│
│  • MCMC/SKMM Telemetry (Bot Amplification & Platform Exploits)│
│  • Military/SIGINT Feeds (State-sponsored Infrastructure Activity)│
│  • Partner Agency Intel (PDRM D88, NACSA, ATM J2)          │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│              PMO BKS FUSION CENTER                          │
├─────────────────────────────────────────────────────────────┤
│  • TTP Mapping via DISARM Framework                         │
│  • Impact Triage (Acute vs. Chronic Assessment)             │
│  • Attribution Analysis (State vs. Non-State)               │
│  • Confidence Scoring (CVS Tier 1-3 Verification)           │
└─────────────────────────────────────────────────────────────┘
                              │
              ┌───────────────┴───────────────┐
              ▼                               ▼
┌───────────────────────────┐   ┌───────────────────────────┐
│    STRATEGIC OUTPUT       │   │   TACTICAL EXECUTION      │
│                           │   │         HOOKS             │
│ • Policy Directives for   │   │ • MCMC (Platform          │
│   Prime Minister          │   │   Enforcements)           │
│ • Cabinet Briefings       │   │ • Wisma Putra (Diplomatic │
│ • Threat Actor Profiles   │   │   Attributions)           │
│ • Campaign Assessments    │   │ • Joint Cyber Commands    │
│                           │   │   (Defensive Actions)     │
└───────────────────────────┘   └───────────────────────────┘
```

---

### Partner Agency Integration

| Agency | Data Contribution | Action Authority |
|--------|-------------------|------------------|
| **MCMC/SKMM** | Platform telemetry, bot detection, content removal requests | Platform enforcement, ISP-level blocking |
| **NACSA** | CNII threat intel, cyber incident correlation | CNII protection directives |
| **PDRM (D88)** | Domestic CT intel, CIB investigation | Law enforcement, arrests |
| **ATM (J2)** | SIGINT, state actor infrastructure tracking | Defense coordination |
| **Wisma Putra** | Diplomatic cables, foreign policy context | Diplomatic attributions, expulsions |
| **NADMA** | Disaster-related misinformation tracking | Public warning systems |

---

## 6. Operational Metrics & KPIs

### Detection Metrics
| Metric | Target | Measurement |
|--------|--------|-------------|
| **FIMI Campaign Detection Time** | <4 hours from inception | Time from first artifact to BKS identification |
| **Attribution Confidence** | ≥80% for state-sponsored | DISARM TTP match + SIGINT correlation |
| **Synthetic Media Detection Rate** | ≥95% | Deepfake/AI-content identification accuracy |

### Response Metrics
| Metric | Target | Measurement |
|--------|--------|-------------|
| **Platform Takedown Time** | <2 hours (ESC-001) | Time from request to platform action |
| **Pre-bunking Deployment** | <6 hours (acute threats) | Time from threat ID to counter-narrative launch |
| **Executive Briefing Time** | <30 min (ESC-001) | Time from detection to PM notification |

### Impact Metrics
| Metric | Target | Measurement |
|--------|--------|-------------|
| **Narrative Containment** | <10% penetration | Adversarial narrative reach vs. target population |
| **Public Trust Index** | Stable/improving | Longitudinal polling on institutional trust |
| **Decision Advantage Preservation** | 100% | Zero successful FIMI-influenced policy decisions |

---

## 7. Gaps / To Verify

- [ ] Full list of BKS software tools (proprietary vs. commercial)
- [ ] Specific MCMC/SKMM API endpoints for platform enforcement
- [ ] Cryptographic signature algorithm specifications
- [ ] Complete DISARM TTP catalog as implemented by BKS
- [ ] Historical campaign case studies (sanitized for knowledgebase)

---

**Cross-References:**
- `01-command-architecture.md` - BKS organizational position
- `02-entity-registry.md` - Partner agency details
- `06-threat-landscape.md` - Threat taxonomy (to be created)
- `07-operational-protocols.md` - ESC codes, reporting flows
- `08-relationship-network.md` - Inter-agency data sharing (to be created)

---

## Notes for Future Updates

1. **Case Study Library:** Document anonymized FIMI campaign takedowns
2. **Tool Inventory:** Catalog BKS technical stack (if information becomes available)
3. **Training Pipeline:** Document analyst certification requirements
4. **International Partnerships:** Map Five Eyes, ASEAN-NACSA, bilateral intel sharing
