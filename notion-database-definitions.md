# Notion Database Definitions
# Strategic CognitiveOS — Phase 1
# Six operational databases for the Notion command layer.
#
# Each Notion entry must contain:
# - Canonical GitHub record ID
# - Record owner
# - Portfolio tier
# - Status
# - Priority
# - Next action
# - Next review date
# - Link to the authoritative record

---

## Database 1: Executive Portfolio

**Purpose:** Authoritative operating view of all initiatives

| Property | Type | Description |
|----------|------|-------------|
| Record ID | Text | Canonical GitHub identifier (INIT-YYYYMMDD-NNN) |
| Initiative Name | Title | Display name |
| Portfolio Tier | Select | flagship / incubation / watch-list / operational |
| Status | Select | draft / in-progress / active / blocked / deferred / completed / archived |
| Priority | Select | critical / high / medium / low |
| Owner | Text | Accountable owner |
| Sponsor | Text | Executive or institutional sponsor |
| Delivery Owner | Text | Person accountable for execution |
| Commercial Owner | Text | Person accountable for opportunity conversion |
| Readiness Level | Select | concept / framed / prototype / demo-ready / pilot-ready / delivery-ready / commercial-ready / scale-ready |
| Mission Alignment | Multi-select | mission/sovereign-ai, mission/national-cybersecurity, etc. |
| Next Action | Text | What needs to happen next |
| Next Review Date | Date | Required reassessment date |
| GitHub Link | URL | Link to authoritative GitHub record |
| Last Updated | Date | Most recent substantive update |

**Views:**
- **All Initiatives** — Gallery view, grouped by portfolio tier
- **Flagship Dashboard** — Filtered to portfolio/flagship, sorted by priority
- **Blocked Items** — Filtered to status=blocked
- **By Mission** — Grouped by mission alignment
- **Review Queue** — Filtered to next review date ≤ today

---

## Database 2: Strategic Actions

**Purpose:** Actions, owners, deadlines and escalation

| Property | Type | Description |
|----------|------|-------------|
| Record ID | Text | Canonical GitHub identifier (ACT-YYYYMMDD-NNN) |
| Action Title | Title | Clear action statement |
| Owner | Text | Person responsible for execution |
| Related Initiative | Relation | Linked to Executive Portfolio entry |
| Related Stakeholder | Relation | Linked to Stakeholder Intelligence entry |
| Priority | Select | critical / high / medium / low |
| Status | Select | draft / in-progress / blocked / completed / overdue / unresolved |
| Attention Level | Select | owner / approver / consulted / informed / delegated / deferred |
| Deadline | Date | When this action must be completed |
| Dependency | Text | What must happen first |
| Required Output | Text | What the completed action produces |
| GitHub Link | URL | Link to authoritative GitHub record |
| Last Updated | Date | Most recent update |

**Views:**
- **All Actions** — List view, sorted by deadline
- **My Actions** — Filtered by owner
- **Overdue** — Filtered to deadline < today AND status ≠ completed
- **Blocked** — Filtered to status=blocked
- **By Initiative** — Grouped by related initiative
- **Delegation Candidates** — Filtered to attention_level=owner, flagged for review
- **Unresolved** — Filtered to status=unresolved (actions without owners)

---

## Database 3: Stakeholder Intelligence

**Purpose:** Relationships, objectives, commitments and follow-ups

| Property | Type | Description |
|----------|------|-------------|
| Record ID | Text | Canonical GitHub identifier (STK-YYYYMMDD-NNN) |
| Name | Title | Individual or organisation name |
| Stakeholder Type | Select | government / internal / partner / prospect / academic / technical / political / defence / regulatory / industry |
| Organisation | Text | Associated institution |
| Role | Text | Current position or institutional function |
| Influence Level | Select | high / medium / low |
| Interest Level | Select | high / medium / low |
| Relationship Status | Select | new / developing / active / trusted / dormant / at-risk |
| Relationship Owner | Text | Person accountable for this relationship |
| Engagement Objective | Text | Intended relationship outcome |
| Last Engagement | Date | Most recent meaningful interaction |
| Next Engagement | Date | Required follow-up date |
| Related Initiatives | Relation | Linked to Executive Portfolio entries |
| Sensitivity | Select | public / internal / confidential / restricted / controlled |
| GitHub Link | URL | Link to authoritative GitHub record |
| Notes | Text | Additional context |

**Views:**
- **All Stakeholders** — Gallery view, grouped by stakeholder type
- **Active Relationships** — Filtered to relationship_status = active or trusted
- **Follow-Up Required** — Filtered to next engagement ≤ today
- **At Risk** — Filtered to relationship_status = at-risk
- **By Initiative** — Grouped by related initiatives
- **Influence Map** — Board view, grouped by influence level

---

## Database 4: Decision Register

**Purpose:** Approved decisions and implementation status

| Property | Type | Description |
|----------|------|-------------|
| Record ID | Text | Canonical GitHub identifier (DEC-YYYYMMDD-NNN) |
| Decision Title | Title | Clear decision statement |
| Decision Date | Date | When the decision was made |
| Decision Owner | Text | Person with authority |
| Status | Select | draft / validated / approved / active / superseded / archived |
| Portfolio Tier | Select | flagship / incubation / watch-list / operational |
| Decision Category | Multi-select | investment / partnership / product-architecture / commercial-model / governance / etc. |
| Implementation Owner | Text | Person responsible for implementation |
| Implementation Status | Select | not-started / in-progress / completed / blocked |
| Review Trigger | Text | Conditions for revisiting this decision |
| Supersedes | Text | Earlier decision replaced |
| Superseded By | Text | Later decision that replaces |
| GitHub Link | URL | Link to authoritative GitHub record |
| Decision Date | Date | When decided |
| Last Updated | Date | Most recent update |

**Views:**
- **All Decisions** — List view, sorted by decision date descending
- **Active Decisions** — Filtered to status=active
- **Pending Approval** — Filtered to status=draft or validated
- **By Category** — Grouped by decision category
- **Superseded** — Filtered to status=superseded (historical reference)
- **Implementation Tracker** — Filtered to implementation_status ≠ completed

---

## Database 5: Product Readiness

**Purpose:** Readiness levels, gaps, owners and external-positioning status

| Property | Type | Description |
|----------|------|-------------|
| Product Name | Title | Product or platform name |
| Related Initiative | Relation | Linked to Executive Portfolio entry |
| Current Readiness | Select | concept / framed / prototype / demo-ready / pilot-ready / delivery-ready / commercial-ready / scale-ready |
| Target Readiness | Select | Next target readiness level |
| Owner | Text | Person accountable for readiness progression |
| Gaps | Text | What's preventing advancement to next level |
| External Commitments | Text | Current external commitments (must not exceed readiness) |
| Overcommitment Flag | Checkbox | Auto-flagged if external commitments exceed readiness |
| Last Assessed | Date | When readiness was last verified |
| Next Assessment | Date | When readiness should be reassessed |
| GitHub Link | URL | Link to authoritative GitHub record |

**Views:**
- **All Products** — Board view, grouped by current readiness
- **Advancement Queue** — Filtered to gaps not empty
- **Overcommitment Risk** — Filtered to overcommitment_flag = true
- **External-Ready** — Filtered to readiness ≥ delivery-ready
- **Assessment Due** — Filtered to next assessment ≤ today

---

## Database 6: Risks and Blockers

**Purpose:** Strategic, commercial, technical and delivery constraints

| Property | Type | Description |
|----------|------|-------------|
| Record ID | Text | Canonical GitHub identifier (RSK-YYYYMMDD-NNN) |
| Risk Title | Title | Clear risk description |
| Risk Category | Select | delivery-capacity / sponsor-gap / product-maturity / commercial-viability / stakeholder-alignment / technical-debt / governance / resource-constraint / timing / dependency |
| Related Initiative | Relation | Linked to Executive Portfolio entry |
| Probability | Select | high / medium / low |
| Impact | Select | high / medium / low |
| Risk Score | Formula | Probability × Impact composite |
| Status | Select | identified / mitigating / monitoring / realised / closed |
| Mitigation Strategy | Text | What can reduce probability or impact |
| Mitigation Owner | Text | Person responsible |
| Trigger Conditions | Text | What indicates the risk is materialising |
| Priority | Select | critical / high / medium / low |
| GitHub Link | URL | Link to authoritative GitHub record |
| Last Updated | Date | Most recent update |

**Views:**
- **All Risks** — Board view, grouped by status
- **High Priority** — Filtered to priority = critical or high
- **By Initiative** — Grouped by related initiative
- **Realised** — Filtered to status=realised (active incidents)
- **Mitigation Tracking** — Filtered to status=mitigating
- **Risk Matrix** — Board view grouped by probability, sub-grouped by impact
