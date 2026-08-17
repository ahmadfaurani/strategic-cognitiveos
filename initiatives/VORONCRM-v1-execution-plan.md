---
id: INIT-20260813-001
record_type: initiative
title: VORONCRM v1 Execution Plan
created_at: 2026-08-13 00:00:00+00:00
owner: faurani-jaafar
status: active
portfolio_tier: incubation
readiness_level: concept
summary: Reference document — see body for details.
sensitivity: internal
lifecycle_state: canonical
tags:
- type/reference-document
updated_at: null
priority: null
confidence: null
source:
  type: null
  reference: null
strategic_significance: null
mission_alignment: []
related_records: []
---

# VORONCRM v1 — Analytical Execution Plan
## VoronDRQ GTM CRM Bootstrap

| Field | Value |
|-------|-------|
| **Document ID** | VORONCRM-v1 |
| **Version** | 1.0 |
| **Date** | 8 August 2026 |
| **Author** | Faurani Jaafar, Director — Cyber Security Practice |
| **Classification** | Confidential — Internal |
| **Initiative** | INIT-20260804-001 (GTM Activation), INIT-20260808-002 (Team Mobilisation) |
| **Platform** | HubSpot Sales Hub Professional (14-day trial → paid) |
| **Execution window** | 9–11 August 2026 (3 days) |
| **Owner** | DAF (solo execution) |

---

## 1. Strategic Rationale

### 1.1 The Problem

The VoronDRQ GTM programme requires a CRM to track 193 organisations across 13 market segments through a 7-stage pipeline. The Marketing Operations Specialist who would normally configure this platform has not yet been hired — and cannot be hired until the COO approves the budget. This creates a circular dependency:

```
COO approval → Hire Marketing Ops → Configure CRM → Launch campaign
                    ↑                                      ↓
                    └────── Blocking dependency ───────────┘
```

### 1.2 The Intervention

DAF bootstraps the CRM personally during the 14-day free trial period. This breaks the circular dependency:

```
DAF bootstraps CRM (3 days) → COO sees live system → Approves budget
                                      ↓
                               Hire Marketing Ops → Inherit working CRM → Launch campaign
```

### 1.3 Strategic Outcomes

| Outcome | Mechanism |
|---------|-----------|
| CRM removed from critical path | Configuration no longer waits for hire |
| Working session transformed | Kenny sees a live system, not a proposal |
| Gate 2a accelerated | Shuhada can see account list immediately after import |
| Gate 3 accelerated | Azzatullina can see account structure she's designing campaigns for |
| Purchase decision simplified | "I've already built it — approve the subscription" |
| Zero financial exposure | Free trial → cancel if not approved |

### 1.4 Analytical Assumptions

| # | Assumption | Confidence | Validation |
|---|-----------|------------|------------|
| A1 | HubSpot Sales Hub Professional includes all must-have capabilities | [HIGH] — verified against published feature list |
| A2 | 14-day trial provides full Professional functionality | [HIGH] — HubSpot trial policy |
| A3 | 193 orgs can be imported via CSV in a single operation | [HIGH] — HubSpot supports bulk company import |
| A4 | Parent-child company hierarchy is supported in Sales Hub Professional | [MEDIUM] — available in Professional tier per documentation |
| A5 | Custom properties (Market Segment, Stakeholder Role, etc.) can be created during trial | [HIGH] — standard CRM functionality |
| A6 | Trial can be converted to paid without data loss | [HIGH] — standard SaaS trial conversion |
| A7 | DAF can complete configuration in 2–3 hours per day across 3 days | [MEDIUM] — assumes familiarity with CRM concepts and no import errors |

---

## 2. Data Architecture Specification

### 2.1 Source Data Inventory

| Source File | Records | Key Columns | Purpose |
|------------|---------|-------------|---------|
| `prospect-database-250.csv` | 203 institutions | Tier, Segment, Institution_Name, Type, Est_Revenue_MYR, Employees, RMiT_Urgency | Full database import — company records |
| `prospect-database-7stakeholders.csv` | 203 institutions × 7 roles | Tier, Segment, Institution_Name, CISO, Head of GRC, CFO, CRO, Head of Compliance, CIO, Head of Internal Audit | Stakeholder contact data (mostly empty — to be populated during discovery) |

### 2.2 Market Segment Distribution (Source Data)

| Tier | Count | Segments |
|------|-------|---------|
| 1 | 28 | Licensed Banks |
| 2 | 54 | Investment Banks, Insurers, Takaful |
| 3 | 48 | MSBs, Development FIs |
| 4 | 38 | E-Money, Card Schemes |
| 5 | 24 | GLC-Linked |
| 6 | 20 | Fintech (Sandbox + Registered) |
| **Total** | **203** | **13 sub-segments** |

### 2.3 HubSpot Data Model

#### 2.3.1 Custom Properties (Companies)

| Property Name | Internal Name | Type | Values | Source Column |
|---------------|--------------|------|--------|---------------|
| Market Tier | `market_tier` | Dropdown | Tier 1, Tier 2, Tier 3, Tier 4, Tier 5, Tier 6 | `Tier` |
| Market Segment | `market_segment` | Dropdown | Licensed Banks, Investment Banks, Insurers, Takaful, MSBs, Development FIs, E-Money, Card Schemes, GLC-Linked, Cooperatives, Fintech Sandbox, Fintech Registered, Payment Operators | `Segment` |
| Institution Type | `institution_type` | Dropdown | (dynamic — derive from `Type` column) | `Type` |
| Est. Revenue Band | `est_revenue_band` | Single-line text | — | `Est_Revenue_MYR` |
| Employee Count | `employee_count` | Number | — | `Employees` |
| RMiT Urgency | `rmit_urgency` | Dropdown | Critical, High, Medium, Low | `RMiT_Urgency` |
| Parent Group | `parent_group` | Single-line text | — | Derived (see §2.4) |
| Campaign Tier | `campaign_tier` | Dropdown | Lighthouse, Conversion, Pipeline, Watchlist | Derived (see §2.5) |

#### 2.3.2 Custom Properties (Contacts)

| Property Name | Internal Name | Type | Values |
|---------------|--------------|------|--------|
| Stakeholder Role | `stakeholder_role` | Dropdown | CISO, CIO/CTO, Head of GRC, CRO, Head of Compliance, CFO, Head of Internal Audit |
| Engagement Status | `engagement_status` | Dropdown | Not Contacted, Contacted, Responded, Meeting Booked, Meeting Held, Nurturing |
| LinkedIn URL | `linkedin_url` | Single-line text | — |

#### 2.3.3 Custom Properties (Deals)

| Property Name | Internal Name | Type | Values |
|---------------|--------------|------|--------|
| Campaign Tier | `campaign_tier` | Dropdown | Lighthouse, Conversion |
| Stakeholder Count | `stakeholder_count` | Number | — |
| Demo Date | `demo_date` | Date picker | — |
| POC Status | `poc_status` | Dropdown | Not Discussed, Proposed, Scoped, In Progress, Completed, Converted |
| Joint Owner (CSM) | `joint_owner_csm` | Checkbox | — |
| Last Activity Type | `last_activity_type` | Dropdown | Email, LinkedIn, Call, Meeting, Demo, POC Session, None |

### 2.4 Parent-Child Hierarchy Mapping

The 203 institutions map to approximately 40+ parent groups. For the bootstrap, only the 15 pilot groups are mapped. The remainder are linked during programme expansion.

#### 2.4.1 Pilot Group Hierarchy (15 Groups)

**Lighthouse (8 groups → ~24 subsidiary buying centres):**

| # | Parent Group | Subsidiaries to Link | RMiT Urgency |
|---|-------------|---------------------|--------------|
| 1 | Maybank Group | Maybank Berhad, Maybank Islamic, Maybank Investment Bank, Etiqa Life, Etiqa General, Etiqa Takaful, MAE by Maybank | Critical |
| 2 | CIMB Group | CIMB Bank, CIMB Islamic, CIMB Investment Bank, CIMB OctoPay | Critical |
| 3 | RHB Group | RHB Bank, RHB Islamic, RHB Investment Bank, Boost (Axiata+RHB) | Critical |
| 4 | Hong Leong Group | Hong Leong Bank, Hong Leong Islamic, Hong Leong Investment Bank, Hong Leong Assurance | Critical |
| 5 | Public Bank Group | Public Bank, Public Islamic Bank | Critical |
| 6 | Affin Bank Group | Affin Bank, Affin Hwang Investment Bank, Affin Islamic | High |
| 7 | Bank Islam Group (BIMB) | Bank Islam Malaysia, BIMB Investment Bank | Critical |
| 8 | Alliance Bank Group | Alliance Bank, Alliance Islamic, Alliance Investment Bank | High |

**Conversion (7 groups → ~10 subsidiary buying centres):**

| # | Parent Group | Subsidiaries to Link | RMiT Urgency |
|---|-------------|---------------------|--------------|
| 9 | Bank Muamalat | (single entity) | Medium |
| 10 | Kuwait Finance House Malaysia | (single entity) | Medium |
| 11 | MIDF | MIDF Amanah Investment Bank | Medium |
| 12 | Kenanga | Kenanga Investment Bank | Medium |
| 13 | BPMB (Bank Pembangunan) | (single entity) | Medium |
| 14 | EXIM Bank Malaysia | (single entity) | Medium |
| 15 | Etiqa | (if not linked to Maybank Group) | High |

**Analytical note:** The parent-child hierarchy is critical for two reasons:
1. **Campaign targeting:** The CMO Review Package targets 15 group-level buying centres, not 15 individual institutions. The hierarchy must reflect this.
2. **Pipeline tracking:** Each subsidiary is a separate deal in the pipeline, but the executive dashboard rolls up to the parent group level.

### 2.5 Campaign Tier Classification Logic

| Campaign Tier | Criteria | Accounts |
|---------------|---------|---------|
| **Lighthouse** | Tier 1 Licensed Banks with Critical RMiT Urgency and full banking group structure | 8 groups |
| **Conversion** | Tier 2 Investment Banks / DFIs / Takaful with High–Medium RMiT Urgency | 7 groups |
| **Pipeline** | Remaining Tier 1–4 institutions not in pilot | ~170 institutions |
| **Watchlist** | Tier 5–6 (GLC-Linked, Fintech) | ~44 institutions |

### 2.6 Pipeline Stage Architecture

| Stage | Name | Entry Criteria | Exit Criteria | Probability | Owner |
|-------|------|---------------|--------------|-------------|-------|
| 1 | Account Validated | Target confirmed viable: regulatory pressure + installed stack + budget signal | At least 1 stakeholder identified | 5% | DAF |
| 2 | Stakeholder Verified | At least 1 key stakeholder identified and contactable | Discovery call booked or pain confirmed | 10% | Account Owner |
| 3 | Qualified | Discovery call completed — pain confirmed — budget authority verified | Formal discovery session scheduled | 20% | Account Owner |
| 4 | Discovery Session | Formal discovery meeting held — requirements documented | Demo scheduled or POC scope discussed | 35% | Account Owner + DAF |
| 5 | Demonstration | VoronDRQ demo delivered to stakeholder(s) | POC proposed or next steps agreed | 50% | Fuad + Account Owner |
| 6 | POC Definition | POC scope agreed — proposal sent — verbal commitment | POC contract signed or POC initiated | 70% | DAF + Fuad |
| 7 | Commercial Conversion | Contract signed / POC converted to commercial engagement | — | 100% | DAF + Shuhada |

**Stage Transition Rules:**
- Stages 1→2: Manual — requires stakeholder contact confirmed
- Stages 2→3: Manual — requires discovery call completed and logged
- Stages 3→4: Manual — requires scheduled session date
- Stages 4→5: Manual — requires Fuad confirmation that demo delivered
- Stages 5→6: Manual — requires POC proposal sent
- Stages 6→7: Manual — requires signed contract or POC conversion

No automation during bootstrap. All stage transitions are manual to maintain data quality.

---

## 3. Execution Plan

### Phase 1: Foundation (Day 1 — 9 August, 2–3 hours)

#### 1.1 Account Provisioning

| Step | Action | Configuration | Validation |
|------|--------|---------------|------------|
| 1.1.1 | Sign up at hubspot.com | Sales Hub Professional trial | Confirmation email received |
| 1.1.2 | Admin email | daf@arasintegrasi.ai | — |
| 1.1.3 | Company name | Aras Integrasi Sdn Bhd | — |
| 1.1.4 | Timezone | UTC+8 (Malaysia) | — |
| 1.1.5 | Currency | MYR (RM) | — |
| 1.1.6 | Fiscal year | January start | — |

#### 1.2 Pipeline Configuration

| Step | Action | Configuration | Validation |
|------|--------|---------------|------------|
| 1.2.1 | Navigate to Sales → Deals → Pipelines | — | — |
| 1.2.2 | Create pipeline: "VoronDRQ GTM Pipeline" | — | Pipeline appears in list |
| 1.2.3 | Add 7 stages per §2.6 | Names and probability weights | All 7 stages visible in kanban view |
| 1.2.4 | Verify stage order | 1→7 sequential | Drag a test deal through all stages |

#### 1.3 Custom Property Creation

| Step | Action | Configuration | Validation |
|------|--------|---------------|------------|
| 1.3.1 | Settings → Properties → Company properties | — | — |
| 1.3.2 | Create `market_tier` (dropdown) | Tier 1–6 | Test by creating a test company |
| 1.3.3 | Create `market_segment` (dropdown) | 13 segments per §2.3.1 | — |
| 1.3.4 | Create `institution_type` (dropdown) | Values from `Type` column: Commercial Bank, Islamic Bank, Investment Bank, Life Insurer, General Insurer, Family Takaful, Development FI, MSB, E-Money Issuer, Bank-issued Wallet, Card Scheme, GLC Financial, Fintech | — |
| 1.3.5 | Create `est_revenue_band` (single-line text) | — | — |
| 1.3.6 | Create `employee_count` (number) | — | — |
| 1.3.7 | Create `rmit_urgency` (dropdown) | Critical, High, Medium, Low | — |
| 1.3.8 | Create `parent_group` (single-line text) | — | — |
| 1.3.9 | Create `campaign_tier` (dropdown) | Lighthouse, Conversion, Pipeline, Watchlist | — |
| 1.3.10 | Settings → Properties → Contact properties | — | — |
| 1.3.11 | Create `stakeholder_role` (dropdown) | CISO, CIO/CTO, Head of GRC, CRO, Head of Compliance, CFO, Head of Internal Audit | — |
| 1.3.12 | Create `engagement_status` (dropdown) | Not Contacted, Contacted, Responded, Meeting Booked, Meeting Held, Nurturing | — |
| 1.3.13 | Create `linkedin_url` (single-line text) | — | — |
| 1.3.14 | Settings → Properties → Deal properties | — | — |
| 1.3.15 | Create `campaign_tier` (dropdown) | Lighthouse, Conversion | — |
| 1.3.16 | Create `stakeholder_count` (number) | — | — |
| 1.3.17 | Create `demo_date` (date picker) | — | — |
| 1.3.18 | Create `poc_status` (dropdown) | Not Discussed, Proposed, Scoped, In Progress, Completed, Converted | — |
| 1.3.19 | Create `joint_owner_csm` (checkbox) | — | — |
| 1.3.20 | Create `last_activity_type` (dropdown) | Email, LinkedIn, Call, Meeting, Demo, POC Session, None | — |

**Validation gate:** All 20 custom properties created. Test by creating a dummy company, contact, and deal — verify all properties are visible and editable.

#### 1.4 Data Import

| Step | Action | Input | Validation |
|------|--------|-------|------------|
| 1.4.1 | Prepare CSV from `prospect-database-250.csv` | Ensure column headers match HubSpot import template | Column count matches |
| 1.4.2 | Navigate to Contacts → Import → Companies | — | — |
| 1.4.3 | Upload CSV | Map columns to company properties per §2.3.1 | Import preview shows correct mapping |
| 1.4.4 | Execute import | — | Import summary: 203 companies created |
| 1.4.5 | Verify import | Search for "Maybank" in companies | Multiple Maybank entities visible |
| 1.4.6 | Spot-check 5 random records | Verify Tier, Segment, Type, Revenue, Employees, RMiT_Urgency mapped correctly | All 5 correct |

**Import mapping reference:**

| CSV Column | HubSpot Property | Notes |
|-----------|-----------------|-------|
| Tier | Market Tier | Dropdown — values must match exactly |
| Segment | Market Segment | Dropdown — values must match exactly |
| Institution_Name | Company Name | HubSpot default field |
| Type | Institution Type | Dropdown — values must match exactly |
| Est_Revenue_MYR | Est. Revenue Band | Single-line text |
| Employees | Employee Count | Number |
| RMiT_Urgency | RMiT Urgency | Dropdown — values must match exactly |

#### 1.5 Parent-Child Hierarchy Setup

| Step | Action | Validation |
|------|--------|------------|
| 1.5.1 | Open Maybank Islamic Berhad | — |
| 1.5.2 | Set Parent Company → search "Maybank Group" (create parent company record if not imported) | Hierarchy link confirmed |
| 1.5.3 | Repeat for all Maybank Group subsidiaries | 7 children linked to Maybank Group |
| 1.5.4 | Repeat for CIMB Group (4 children) | 4 children linked |
| 1.5.5 | Repeat for RHB Group (4 children) | 4 children linked |
| 1.5.6 | Repeat for Hong Leong Group (4 children) | 4 children linked |
| 1.5.7 | Repeat for Public Bank Group (2 children) | 2 children linked |
| 1.5.8 | Repeat for Affin Bank Group (3 children) | 3 children linked |
| 1.5.9 | Repeat for Bank Islam Group (2 children) | 2 children linked |
| 1.5.10 | Repeat for Alliance Bank Group (3 children) | 3 children linked |
| 1.5.11 | Etiqa: link to Maybank Group if applicable, otherwise create standalone | — |
| 1.5.12 | For Conversion groups (7): create parent records where needed, link children | — |

**Validation gate:** All 15 pilot groups have parent records with linked children. Open Maybank Group → see all subsidiaries in the "Child Companies" section.

**Day 1 exit criteria:**
- [ ] Pipeline created with 7 stages
- [ ] 20 custom properties created (10 company, 3 contact, 7 deal)
- [ ] 203 companies imported
- [ ] 15 pilot groups have parent-child hierarchy established

---

### Phase 2: Operational Layer (Day 2 — 10 August, 2–3 hours)

#### 2.1 Executive Dashboard Construction

| Step | Report Card | Type | Data Source | Filter |
|------|-------------|------|-------------|--------|
| 2.1.1 | Pipeline Overview | Bar chart | Deals | Pipeline = VoronDRQ GTM |
| 2.1.2 | Accounts Activated | Single number | Companies | Campaign Tier = Lighthouse OR Conversion |
| 2.1.3 | Stakeholders Engaged | Single number | Contacts | Associated with VoronDRQ GTM deals |
| 2.1.4 | Discovery Sessions Booked | Single number | Deals | Stage = 4 (Discovery Session) |
| 2.1.5 | Demos Delivered | Single number | Deals | Stage = 5 (Demonstration) |
| 2.1.6 | POCs in Flight | Single number | Deals | Stage = 6 (POC Definition) |
| 2.1.7 | Conversion Rate | Calculated | Deals | Stage 7 count ÷ Stage 1 count |
| 2.1.8 | Pipeline by Market Segment | Bar chart | Deals | Grouped by Market Segment |

| Step | Action | Validation |
|------|--------|------------|
| 2.1.9 | Create dashboard: "VoronDRQ GTM — Executive View" | — |
| 2.1.10 | Add all 8 report cards | All cards render with data |
| 2.1.11 | Set visibility: Share with team | All invited users can view |
| 2.1.12 | Test on desktop browser | Dashboard loads in <5 seconds |
| 2.1.13 | Test on mobile app | Dashboard renders correctly |

#### 2.2 Deal Record Creation (15 Pilot Accounts)

| Step | Action | Validation |
|------|--------|------------|
| 2.2.1 | Create Deal: "Maybank Group — VoronDRQ GTM" | — |
| 2.2.2 | Pipeline: VoronDRQ GTM, Stage: Account Validated | Deal appears in Stage 1 |
| 2.2.3 | Link to parent company: Maybank Group | Company association visible |
| 2.2.4 | Set Campaign Tier: Lighthouse | — |
| 2.2.5 | Set close date: 31 December 2026 (placeholder) | — |
| 2.2.6 | Repeat for all 15 pilot groups | 15 deals in Stage 1 |

**Deal naming convention:** `[Parent Group Name] — VoronDRQ GTM`

| # | Deal Name | Campaign Tier | Linked Company |
|---|-----------|---------------|----------------|
| 1 | Maybank Group — VoronDRQ GTM | Lighthouse | Maybank Group |
| 2 | CIMB Group — VoronDRQ GTM | Lighthouse | CIMB Group |
| 3 | RHB Group — VoronDRQ GTM | Lighthouse | RHB Group |
| 4 | Hong Leong Group — VoronDRQ GTM | Lighthouse | Hong Leong Group |
| 5 | Public Bank Group — VoronDRQ GTM | Lighthouse | Public Bank Group |
| 6 | Affin Bank Group — VoronDRQ GTM | Lighthouse | Affin Bank Group |
| 7 | Bank Islam Group — VoronDRQ GTM | Lighthouse | Bank Islam Group |
| 8 | Alliance Bank Group — VoronDRQ GTM | Lighthouse | Alliance Bank Group |
| 9 | Bank Muamalat — VoronDRQ GTM | Conversion | Bank Muamalat |
| 10 | KFH Malaysia — VoronDRQ GTM | Conversion | Kuwait Finance House Malaysia |
| 11 | MIDF — VoronDRQ GTM | Conversion | MIDF |
| 12 | Kenanga — VoronDRQ GTM | Conversion | Kenanga Investment Bank |
| 13 | BPMB — VoronDRQ GTM | Conversion | Bank Pembangunan |
| 14 | EXIM Bank — VoronDRQ GTM | Conversion | EXIM Bank Malaysia |
| 15 | Etiqa — VoronDRQ GTM | Conversion | Etiqa (standalone or Maybank child) |

#### 2.3 User Provisioning

| Step | User | Email | Role | Access Level |
|------|------|-------|------|--------------|
| 2.3.1 | Shuhada M. Halimi | shuhada@arasintegrasi.ai | Sales Manager | Full: deals, contacts, companies |
| 2.3.2 | Ahmad Fuad | (confirm email) | Sales Agent | View: all deals (needs demo-stage visibility) |
| 2.3.3 | Hadri | hadri@arasintegrasi.ai | Read-Only | View: POC-stage deals only |

| Step | Action | Validation |
|------|--------|------------|
| 2.3.4 | Settings → Users & Teams → Invite each user | Invitation emails sent |
| 2.3.5 | Configure role permissions per table above | Each user sees correct scope |
| 2.3.6 | Do NOT invite Kenny, Azzatullina, or Account Owners | Post-working-session only |

**Rationale for delayed invitations:** The CRM must show progress (15 deals, structured hierarchy, dashboard) before non-execution stakeholders see it. First impression matters.

**Day 2 exit criteria:**
- [ ] Executive dashboard live with 8 report cards
- [ ] 15 deal records created in Stage 1
- [ ] 3 users invited (Shuhada, Fuad, Hadri)
- [ ] Dashboard renders on desktop and mobile

---

### Phase 3: Working Session Preparation (Day 3 — 11 August, 1–2 hours)

#### 3.1 Stakeholder Contact Loading (3 Pilot Accounts)

Select 3 accounts where DAF already knows stakeholder names. For each:

| Step | Action | Validation |
|------|--------|------------|
| 3.1.1 | Create contact: Name, Title, Email, LinkedIn URL | Contact record created |
| 3.1.2 | Associate with company record | Company link visible |
| 3.1.3 | Set Stakeholder Role (dropdown) | Role tagged |
| 3.1.4 | Set Engagement Status: "Not Contacted" | — |
| 3.1.5 | Repeat for 2–3 stakeholders per account | 6–9 contacts total |
| 3.1.6 | Update Deal: set Stakeholder Count property | Number matches contacts |

**Recommended accounts for stakeholder loading:**
1. An account where DAF has direct relationships (likely Maybank or CIMB)
2. An account from the Conversion tier (demonstrates breadth)
3. A third account to show the pattern is repeatable

#### 3.2 Working Session Demo View

| Step | Action | Configuration |
|------|--------|---------------|
| 3.2.1 | Create custom Deal view: "Pilot Accounts — Working Session" | — |
| 3.2.2 | Filter: Pipeline = VoronDRQ GTM, Campaign Tier = Lighthouse OR Conversion | 15 deals visible |
| 3.2.3 | Columns: Deal Name, Company, Campaign Tier, Market Segment, Stakeholder Count, Last Activity | — |
| 3.2.4 | Save view | — |
| 3.2.5 | Test: open this view first when sharing screen | Clean, professional, 15 rows |

#### 3.3 Mobile Validation

| Step | Action | Validation |
|------|--------|------------|
| 3.3.1 | Download HubSpot mobile app (iOS/Android) | — |
| 3.3.2 | Log in with admin credentials | — |
| 3.3.3 | Verify pipeline view visible | 7 stages, 15 deals |
| 3.3.4 | Verify dashboard renders | All 8 cards visible |
| 3.3.5 | Verify contact records accessible | Can open stakeholder contacts |
| 3.3.6 | Verify deal editing on mobile | Can update a deal stage |

#### 3.4 Data Quality Audit

| Check | Method | Pass Criteria |
|-------|--------|---------------|
| No duplicate companies | Search for "Maybank" — verify one record per legal entity | 0 duplicates |
| All 15 pilot deals in Stage 1 | Pipeline view → count deals | 15 deals |
| Parent-child links correct | Open 3 random parents → verify children | All 3 correct |
| Custom properties populated | Open 5 random companies → verify Tier, Segment, Type, Urgency | All 5 populated |
| No orphan contacts | Open 3 contacts → verify company association | All 3 associated |
| Dashboard cards render | Open dashboard → all 8 cards show data | All 8 render |

**Day 3 exit criteria:**
- [ ] 3 accounts have stakeholder contacts loaded (6–9 contacts)
- [ ] Working Session demo view created and tested
- [ ] Mobile app validated
- [ ] Data quality audit passed (6/6 checks)

---

## 4. Working Session Presentation Script

### 4.1 Sequence (7 minutes)

| Minute | Action | Screen | Narrative |
|--------|--------|--------|-----------|
| 1 | Open HubSpot → Pipeline view | VoronDRQ GTM Pipeline kanban | "This is live. 15 accounts loaded, all in Stage 1." |
| 2 | Click Maybank Group deal → show company record | Parent-child hierarchy | "Maybank Group maps to 7 subsidiary buying centres. Each is a separate engagement." |
| 3 | Click a subsidiary → show stakeholder contacts | 2–3 named contacts with roles | "Stakeholders are tagged by role — CISO, Head of GRC, CRO. This is what the Account Owners will build out." |
| 4 | Navigate to Executive Dashboard | 8 report cards | "Real-time visibility: accounts activated, sessions booked, demos delivered, POCs in flight. This is what weekly reviews look like." |
| 5 | Show pipeline by market segment | Bar chart | "The 193-org database is fully imported. We're starting with 15. The remaining 170 are in the system, ready for Wave 2." |
| 6 | Open mobile app on phone | Pipeline on mobile | "Account Owners carry this into client meetings. Demo notes, stakeholder updates, stage changes — all on-site." |
| 7 | Close laptop. Look at Kenny. | — | "The CRM is live. The team structure is defined. The 15 accounts are loaded. What I need from this meeting is your approval on hires and budget so we can start outreach by September 1." |

### 4.2 Anticipated Questions

| Question | Answer |
|----------|--------|
| "How much does this cost?" | ~RM 6,100/month on annual billing. Trial is free. No commitment until you approve. |
| "Can we use a cheaper option?" | Zoho is ~RM 2,400/month — credible backup. I recommend HubSpot because the email automation and reporting are stronger, and it scales to 193 accounts without platform change. |
| "Who maintains this?" | The Marketing Operations Specialist — one of the 4 hires in the JD package. I'm bootstrapping it so they inherit a working system, not a blank slate. |
| "What about data security?" | HubSpot is SOC 2 Type II certified, ISO 27001 certified. Data stored in AWS cloud. No Malaysian data residency requirement for CRM pipeline data — this is sales tracking, not customer financial data. |
| "What if Fuad hasn't validated by the working session?" | The CRM is a tracking tool, not a product claims document. The pipeline stages track engagement progress. Fuad's validation gates what we *say* in outreach, not whether the CRM exists. |
| "Can Azzatullina see this?" | Yes — I'll invite her after this session. She can see the account structure and stakeholder roles, which is exactly what she needs to design the campaign messaging. |

---

## 5. Risk Analysis

### 5.1 Execution Risks (Bootstrap Phase)

| ID | Risk | Probability | Impact | Mitigation |
|----|------|------------|--------|------------|
| R1 | CSV import fails or maps incorrectly | Medium | High | Spot-check 5 records immediately after import. If >5% error rate, re-import with corrected mapping. |
| R2 | Parent-child hierarchy not available in trial tier | Low | High | Verify during Day 1 Step 1.2 before proceeding to import. If unavailable, use "Parent Group" custom property as text field workaround. |
| R3 | Custom property creation limited in trial | Low | Medium | Verify during Day 1 Step 1.3. If limited, prioritise Market Tier, Market Segment, and Campaign Tier — defer the rest to Marketing Ops Specialist. |
| R4 | DAF time displaced by urgent operational issue | Medium | Medium | Block calendar for 3 sessions. If interrupted, extend to 4 days. The trial is 14 days — buffer is sufficient. |
| R5 | Stakeholder data (7-stakeholder CSV) is mostly empty | High | Low | Expected — stakeholder loading is a discovery-phase activity, not bootstrap. Load only 3 accounts' known contacts for demo. |
| R6 | HubSpot trial expires before working session | Low | Critical | Trial is 14 days. Working session target is Aug 22 (Day 14). If session slips, convert to paid and cancel if not approved. |
| R7 | HubSpot UX changes since research | Low | Low | HubSpot interface is stable. If changed, adapt — core concepts (pipelines, deals, contacts, companies) are unchanged. |

### 5.2 Strategic Risks (Post-Bootstrap)

| ID | Risk | Probability | Impact | Mitigation |
|----|------|------------|--------|------------|
| S1 | Kenny sees bootstrap as overstepping authority | Low | High | Frame as "I wanted to show you something real, not a proposal." Decision is still his — approval for hires and budget. CRM is free trial, no financial commitment. |
| S2 | Azzatullina feels bypassed by CRM configuration | Medium | Medium | Frame CRM as infrastructure, not campaign design. Azzatullina owns messaging, content, outreach sequencing — CRM is the tracking layer beneath her work. Invite her after working session, walk her through personally. |
| S3 | Fuad's product validation contradicts CRM stage assumptions | Low | Medium | CRM stages track engagement, not product claims. If Fuad's validation changes the outreach narrative, update deal descriptions — not pipeline structure. |
| S4 | Zoho turns out to be better fit post-evaluation | Low | Medium | Data export from HubSpot is straightforward (CSV export of all records). Migration cost is ~1 day of Marketing Ops time. Not a lock-in risk. |
| S5 | Marketing Ops Specialist prefers different platform | Low | Low | Platform decision is made. Specialist inherits the system. If they make a compelling case for Zoho, migration is possible but requires COO approval. |

### 5.3 Risk Heat Map

```
         Low Impact    Medium Impact    High Impact    Critical
High     R5            —                R1, R2        R6
Medium   R7            R3, R4, S2       —             —
Low     —             S1, S3, S4, S5   R7             —
```

**No Critical/High-probability risks identified.** The bootstrap is low-risk: the primary failure mode is time (R4), which is manageable with calendar blocking.

---

## 6. Success Metrics

### 6.1 Bootstrap Completion Metrics (Hard Gates)

| ID | Metric | Target | Measurement | Gate |
|----|--------|--------|------------|------|
| M1 | CRM live and accessible | Admin can log in, see dashboard | Manual | Day 1 |
| M2 | Companies imported | 203 records | Company count in HubSpot | Day 1 |
| M3 | Pilot pipeline populated | 15 deals in Stage 1 | Deal count in pipeline | Day 2 |
| M4 | Parent-child hierarchy | 15 groups with linked children | Spot-check 3 groups | Day 1 |
| M5 | Executive dashboard | 8 report cards rendering | Dashboard visual check | Day 2 |
| M6 | Users invited | 3 users (Shuhada, Fuad, Hadri) | User list | Day 2 |
| M7 | Stakeholder contacts | 6–9 contacts across 3 accounts | Contact count | Day 3 |
| M8 | Mobile app functional | Pipeline visible on mobile | App visual check | Day 3 |
| M9 | Data quality audit | 6/6 checks passed | Audit checklist | Day 3 |

### 6.2 Working Session Success Metrics

| ID | Metric | Target | Measurement |
|----|--------|--------|------------|
| W1 | Kenny sees live CRM | Screen shared, CRM visible | Session observation |
| W2 | Kenny approves budget | Verbal or written confirmation | Session outcome |
| W3 | Kenny approves 4 hires | Verbal or written confirmation | Session outcome |
| W4 | Working session date scheduled | Calendar invite sent | Calendar confirmation |
| W5 | Azzatullina engaged post-session | CRM invite accepted + login within 48h | User activity log |

### 6.3 Post-Bootstrap Programme Metrics (Tracked in CRM)

| ID | Metric | Target (30 days) | Target (90 days) |
|----|--------|-----------------|------------------|
| P1 | Accounts in Stage 2+ | 5 | 10 |
| P2 | Discovery sessions booked | 3 | 5+ |
| P3 | Demos delivered | 2 | 5–6 |
| P4 | POC candidates | 1 | 2–3 |
| P5 | Pipeline value (estimated) | RM 250K | RM 1M+ |
| P6 | Stakeholder contacts per account | 1.5 avg | 3+ avg |

---

## 7. Dependency Map

### 7.1 Bootstrap Dependencies

```
                    ┌─────────────────┐
                    │  HubSpot Trial   │
                    │  Activation      │
                    └────────┬────────┘
                             │
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
     ┌────────────┐  ┌──────────────┐  ┌──────────────┐
     │ Pipeline   │  │ Custom       │  │ CSV Import   │
     │ Config     │  │ Properties   │  │ (203 orgs)   │
     │ (7 stages) │  │ (20 fields)  │  │              │
     └────────┬───┘  └──────────────┘  └──────┬───────┘
              │                                │
              └──────────────┬─────────────────┘
                             ▼
                   ┌─────────────────┐
                   │  Parent-Child   │
                   │  Hierarchy Setup │
                   │  (15 groups)     │
                   └────────┬────────┘
                             │
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
     ┌────────────┐  ┌──────────────┐  ┌──────────────┐
     │ Dashboard  │  │ 15 Deal      │  │ User Invites │
     │ (8 cards)  │  │ Records      │  │ (3 users)    │
     └────────────┘  └──────────────┘  └──────────────┘
                             │
                             ▼
                   ┌─────────────────┐
                   │  Stakeholder    │
                   │  Loading (3     │
                   │  accounts)     │
                   └────────┬────────┘
                             │
                             ▼
                   ┌─────────────────┐
                   │  Working Session │
                   │  Demo View      │
                   └────────┬────────┘
                             │
                             ▼
                   ┌─────────────────┐
                   │  Data Quality   │
                   │  Audit (6/6)    │
                   └─────────────────┘
```

### 7.2 Programme Dependencies (Post-Bootstrap)

```
  CRM Bootstrap ──────┐
                     │
  Fuad Validation ───┤
                     │
  Shuhada Alignment ─┤──→ Working Session ──→ Kenny Approval ──→ Hire 4 Roles
                     │                                                        │
  Hadri Capacity ────┤                                                        ▼
                     │                                               Marketing Ops Inherits
  Azzatullina Co-Design┘                                             CRM + Campaign Launch
```

### 7.3 Critical Path

| Step | Duration | Predecessor | Successor |
|------|----------|------------|-----------|
| CRM Bootstrap | 3 days (Aug 9–11) | None | Working Session |
| Fuad Validation | 2–5 days (response time) | Email sent Aug 8 | Azzatullina Co-Design |
| Shuhada Alignment | 1–3 days (conversation) | DAF initiates | Working Session |
| Hadri Capacity Check | 1–3 days (conversation) | DAF initiates | Working Session |
| Azzatullina Co-Design | 3–5 days | Fuad Validation | Working Session |
| Working Session | 1 day | All above | Kenny Approval |
| Kenny Approval | 1 day | Working Session | Recruitment Initiation |
| Recruitment | 2–4 weeks | Kenny Approval | Campaign Launch |
| Campaign Launch | — | Recruitment + CRM + CMO Package | Sep 1 target |

**Critical path duration:** ~3–4 weeks from Aug 9 to Campaign Launch (Sep 1–22).

---

## 8. Post-Bootstrap Transition Plan

### 8.1 Marketing Ops Specialist Handover

When the Marketing Ops Specialist is hired, they inherit a working CRM with:
- 203 company records, fully classified
- 15 pilot deals in Stage 1
- Parent-child hierarchy for 15 groups
- 3 stakeholder-loaded accounts (demo data)
- Executive dashboard live
- 3 active users (Shuhada, Fuad, Hadri)
- Mobile app validated

**Handover checklist (Day 1 for Marketing Ops Specialist):**

| Step | Action | Time |
|------|--------|------|
| 1 | Walkthrough: pipeline structure, custom properties, dashboard | 1 hour |
| 2 | Review: 15 pilot deals and parent-child hierarchy | 30 min |
| 3 | Review: data quality audit results | 15 min |
| 4 | Access: confirm user role (Marketing — admin) | 15 min |
| 5 | Handover document: this execution plan + bootstrap checklist | 30 min |
| 6 | First task: email sequence configuration (Week 1/2/3 cadence) | Begin Day 2 |

### 8.2 Platform Decision Finalisation

| Trigger | Action |
|---------|--------|
| Kenny approves budget | Convert HubSpot trial to paid (Sales Hub Professional + Marketing Hub Professional) |
| Kenny requires lower cost | Export all data from HubSpot → Import to Zoho CRM Enterprise. Estimated migration: 1 day. |
| Kenny defers decision | Continue on trial. If trial expires before decision, extend with monthly billing (cancel anytime). |

### 8.3 Data Expansion Plan

| Phase | What's Added | When |
|-------|-------------|------|
| Bootstrap (VORONCRM v1) | 203 orgs, 15 deals, 3 stakeholder accounts | Aug 9–11 |
| Working Session | Azzatullina's campaign messaging mapped to stakeholder roles | Aug 22+ |
| Campaign Launch | Email sequences, attribution tracking, LinkedIn integration | Sep 1+ |
| Wave 2 | Remaining 170 orgs promoted from Pipeline to active deals | Oct+ |
| CSM Joint Accounts | CSM-identified accounts added with Joint Owner flag | Post-CSM alignment |

---

## 9. Configuration Audit Trail

### 9.1 All Custom Properties Created (Reference for Marketing Ops Specialist)

**Company Properties (10):**
1. `market_tier` — Dropdown: Tier 1, Tier 2, Tier 3, Tier 4, Tier 5, Tier 6
2. `market_segment` — Dropdown: 13 values (Licensed Banks, Investment Banks, Insurers, Takaful, MSBs, Development FIs, E-Money, Card Schemes, GLC-Linked, Cooperatives, Fintech Sandbox, Fintech Registered, Payment Operators)
3. `institution_type` — Dropdown: Commercial Bank, Islamic Bank, Investment Bank, Life Insurer, General Insurer, Family Takaful, Development FI, MSB, E-Money Issuer, Bank-issued Wallet, Card Scheme, GLC Financial, Fintech
4. `est_revenue_band` — Single-line text
5. `employee_count` — Number
6. `rmit_urgency` — Dropdown: Critical, High, Medium, Low
7. `parent_group` — Single-line text
8. `campaign_tier` — Dropdown: Lighthouse, Conversion, Pipeline, Watchlist

**Contact Properties (3):**
9. `stakeholder_role` — Dropdown: CISO, CIO/CTO, Head of GRC, CRO, Head of Compliance, CFO, Head of Internal Audit
10. `engagement_status` — Dropdown: Not Contacted, Contacted, Responded, Meeting Booked, Meeting Held, Nurturing
11. `linkedin_url` — Single-line text

**Deal Properties (7):**
12. `campaign_tier` — Dropdown: Lighthouse, Conversion
13. `stakeholder_count` — Number
14. `demo_date` — Date picker
15. `poc_status` — Dropdown: Not Discussed, Proposed, Scoped, In Progress, Completed, Converted
16. `joint_owner_csm` — Checkbox
17. `last_activity_type` — Dropdown: Email, LinkedIn, Call, Meeting, Demo, POC Session, None
18. `close_date` — Date picker (HubSpot default, used with 31 Dec 2026 placeholder)

### 9.2 Pipeline Configuration (Reference)

| Stage # | Name | Probability | Description |
|---------|------|-------------|-------------|
| 1 | Account Validated | 5% | Target confirmed as viable |
| 2 | Stakeholder Verified | 10% | At least 1 key stakeholder identified |
| 3 | Qualified | 20% | Discovery call completed, pain confirmed |
| 4 | Discovery Session | 35% | Formal discovery meeting held |
| 5 | Demonstration | 50% | VoronDRQ demo delivered |
| 6 | POC Definition | 70% | POC scope agreed, proposal sent |
| 7 | Commercial Conversion | 100% | Contract signed |

---

## 10. Decision Log

| # | Decision | Rationale | Date | Decided By |
|---|---------|-----------|------|------------|
| D1 | Platform: HubSpot | All-in-one, native hierarchy, best reporting, scales to 193 | Aug 8 | DAF |
| D2 | Bootstrap before hire | Removes blocking dependency on critical path | Aug 8 | DAF |
| D3 | Free trial first | Zero financial exposure before COO approval | Aug 8 | DAF |
| D4 | 15 pilot deals only | Working session demo, not full campaign | Aug 8 | DAF |
| D5 | 3 stakeholder accounts only | Demo pattern, not full data entry | Aug 8 | DAF |
| D6 | Invite Shuhada/Fuad/Hadri only | Execution team; Kenny/Azzatullina post-session | Aug 8 | DAF |
| D7 | Manual stage transitions only | Data quality over speed during bootstrap | Aug 8 | DAF |
| D8 | Defer email automation to Marketing Ops | Requires campaign structure from Azzatullina | Aug 8 | DAF |

---

## 11. Glossary

| Term | Definition |
|------|-----------|
| **Bootstrap** | Self-configuration of CRM by DAF before Marketing Ops Specialist is hired |
| **Buying Centre** | A subsidiary or business unit within a parent group that has independent procurement authority |
| **Campaign Tier** | Classification of accounts: Lighthouse (8 pilot groups), Conversion (7 pilot groups), Pipeline (~170 remaining), Watchlist (~44 Tier 5–6) |
| **Lighthouse** | 8 pilot accounts with Critical RMiT Urgency and full banking group structure |
| **Conversion** | 7 pilot accounts with High–Medium RMiT Urgency |
| **RMiT** | Risk Management in Technology — Bank Negara Malaysia policy document governing technology risk management |
| **RMiT Urgency** | Analytical assessment of how urgently an institution needs continuous assurance (driven by RMiT compliance pressure) |
| **Parent-Child Hierarchy** | HubSpot company association linking subsidiary buying centres to their parent group |
| **Pipeline Stage** | One of 7 defined stages in the VoronDRQ GTM Pipeline |
| **Stakeholder Role** | One of 7 functional roles mapped per account (CISO, CIO/CTO, Head of GRC, CRO, Head of Compliance, CFO, Head of Internal Audit) |
| **VoronDRQ** | Aras Integrasi's continuous assurance platform — the product being brought to market |
| **Working Session** | Meeting with Kenny (COO), Azzatullina (CMO), Shuhada (Sales) to present the COO Approval Package and secure approval |

---

*End of VORONCRM v1 — Analytical Execution Plan*

*Next version (v2) will be maintained by the Marketing Operations Specialist post-hire, covering email automation, campaign attribution, LinkedIn integration, and advanced reporting configuration.*
