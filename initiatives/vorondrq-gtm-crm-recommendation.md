---
id: INIT-20260813-007
record_type: initiative
title: VoronDRQ GTM CRM Recommendation
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
updated_at: '2026-08-17T17:50:23+00:00'
priority: high
confidence: medium
source:
  type: null
  reference: null
strategic_significance: 'Portfolio: incubation. Readiness: concept.'
mission_alignment: []
related_records: []
---

# CRM Platform Recommendation — VoronDRQ GTM Programme

**Prepared for:** COO Approval (INIT-20260808-002)
**Prepared by:** Faurani Jaafar, Director — Cyber Security Practice
**Date:** 8 August 2026
**Classification:** Confidential — Internal

---

## 1. Requirement

A CRM platform to support the VoronDRQ GTM programme — campaign tracking, pipeline management, email automation, attribution, and executive reporting. The platform is a blocking dependency: the campaign cannot launch without tracking infrastructure.

## 2. Must-Have Capabilities

| Capability | Why It's Required |
|-----------|-------------------|
| Custom pipeline stages (7-stage) | Account Validation → Stakeholder Verification → Qualification → Discovery → Demonstration → POC Definition → Commercial Conversion |
| Email sequence automation | Week 1, 2, 3 cadence with personalisation tokens and stop-on-response rules |
| Contact & account hierarchy | Parent group (e.g. Maybank Group) → subsidiary buying centres (Maybank IB, Maybank Islamic, Etiqa) |
| Campaign attribution tracking | Which channel (email, LinkedIn, roundtable, executive engagement) generated each engagement |
| Custom dashboards | Real-time: accounts activated, stakeholders engaged, sessions booked, demos delivered, POCs in flight |
| LinkedIn Sales Navigator integration | Account targeting, stakeholder identification, connection tracking |
| Role-based access | Sales, Marketing, Practice — different views and permissions |
| Mobile access | Account owners visiting client sites |
| API access | Integration with existing tools and future expansion |

## 3. User Count

| User | Role |
|------|------|
| DAF | Programme Owner — full access |
| Delivery Owner | Programme execution — full access |
| Shuhada | Sales lead — full access |
| Account Owner 1 | Sales — own accounts only |
| Account Owner 2 | Sales — own accounts only |
| Azzatullina | Marketing — campaign and reporting access |
| Marketing Operations Specialist | Marketing — admin/configuration access |
| Fuad | Product — read access to accounts and demos |
| Hadri | Technical — read access to POC stage accounts |

**Total: 9 users** (5 full, 2 restricted, 2 read-only)

## 4. Platform Comparison

### Option A: HubSpot (Sales Hub Professional + Marketing Hub Professional)

**Strengths:**
- All-in-one platform — CRM, email automation, sequences, marketing campaigns, reporting in one system
- Best-in-class email sequence builder with stop-on-response rules, personalisation tokens, A/B testing
- LinkedIn Sales Navigator integration (native)
- Custom pipeline stages and dashboards built-in
- Parent-child account hierarchy supported
- Excellent onboarding and academy resources
- Strong API and integration ecosystem

**Weaknesses:**
- Most expensive option
- Marketing Hub pricing scales with contact database size (1,000+ contacts increases cost)
- Steeper learning curve for non-technical users

**Estimated Cost (approximate — verify at purchase):**
| Component | Monthly Cost (USD) | Monthly Cost (RM ≈ 4.7) |
|-----------|-------------------|------------------------|
| Sales Hub Professional (5 users) | ~$450 ($90/user) | ~RM 2,100 |
| Marketing Hub Professional (1,000 contacts) | ~$800 | ~RM 3,800 |
| Additional Sales users (4 × $90) | ~$360 | ~RM 1,700 |
| **Total monthly** | **~$1,610** | **~RM 7,600** |
| Annual prepayment discount | ~20% | ~RM 6,100/month |

**Time to configure:** 1–2 weeks (Marketing Ops Specialist lead)

---

### Option B: Zoho CRM Enterprise + Zoho Campaigns

**Strengths:**
- Cost-effective — significantly cheaper than HubSpot at equivalent user count
- Enterprise edition includes territory management, journey orchestration, AI assistant, custom functions
- Data centre in Singapore (data residency relevant for Malaysian financial services prospects)
- Zoho Campaigns integrates natively for email automation and sequence building
- Zoho One bundle available if broader toolset needed (email, docs, projects, analytics)
- Strong API and marketplace integrations
- Good LinkedIn integration via Zoho Marketing Plus

**Weaknesses:**
- Email automation is split across Zoho CRM (sequences/cadences) and Zoho Campaigns (bulk email) — slightly less unified than HubSpot
- Reporting and dashboards capable but less polished than HubSpot
- Smaller integration ecosystem than HubSpot
- Learning curve for configuration (Zoho's interface is powerful but less intuitive)

**Estimated Cost (approximate — verify at purchase):**
| Component | Monthly Cost (USD) | Monthly Cost (RM ≈ 4.7) |
|-----------|-------------------|------------------------|
| Zoho CRM Enterprise (9 users) | ~$315 ($35/user) | ~RM 1,500 |
| Zoho Campaigns (10,000 contacts) | ~$150 | ~RM 700 |
| Zoho Analytics (reporting) | ~$300 | ~RM 1,400 |
| **Total monthly** | **~$765** | **~RM 3,600** |
| Annual prepayment discount | ~34% | ~RM 2,400/month |

**Time to configure:** 2–3 weeks (Marketing Ops Specialist lead, slightly more complex setup)

---

### Option C: Pipedrive + Separate Email Tool

**Strengths:**
- Simplest interface — sales-focused, fast to deploy
- Custom pipeline stages are easy to configure
- Good for small teams with straightforward sales process
- Lowest cost option

**Weaknesses:**
- No built-in email automation or sequence builder — requires separate tool (Mailchimp, ActiveCampaign, or similar)
- No marketing campaign management — purely a sales CRM
- Limited reporting and dashboard capabilities
- No parent-child account hierarchy (critical for buying centre mapping)
- Attribution tracking would need manual workarounds
- Two systems to manage (CRM + email tool) = data sync risk

**Estimated Cost (approximate — verify at purchase):**
| Component | Monthly Cost (USD) | Monthly Cost (RM ≈ 4.7) |
|-----------|-------------------|------------------------|
| Pipedrive Professional (9 users) | ~$441 ($49/user) | ~RM 2,100 |
| ActiveCampaign (1,000 contacts) | ~$150 | ~RM 700 |
| **Total monthly** | **~$591** | **~RM 2,800** |
| Annual prepayment | ~20% | ~RM 2,200/month |

**Time to configure:** 1–2 weeks (but integration between two systems adds complexity)

---

## 5. Recommendation

### Primary Recommendation: HubSpot (Option A)

**Why:**
1. **All-in-one** — CRM, email sequences, marketing campaigns, reporting, attribution in a single platform. The Marketing Operations Specialist doesn't need to integrate two systems.
2. **Stop-on-response rules** are native and reliable — critical for the campaign guardrail "stop automated follow-ups after substantive response"
3. **Parent-child account hierarchy** is native — essential for mapping 15 group-level buying centres to their subsidiaries
4. **Best-in-class reporting** — the executive dashboard for Kenny and the weekly review for the Marketing-Sales meeting need to be production-quality
5. **LinkedIn Sales Navigator integration** is native and well-documented
6. **Scalability** — if the programme expands beyond the pilot to the full 193-organisation database, HubSpot scales without platform change
7. **Onboarding support** — HubSpot Academy and onboarding team reduce time-to-competency for the Marketing Ops Specialist

**Cost concern:** At ~RM 7,600/month (annual billing), it's the most expensive option. However, the cost difference versus Zoho (~RM 3,600/month) is ~RM 4,000/month — less than the cost of one bad month of campaign data gaps or attribution errors. For a programme targeting RM millions in pipeline, the instrumentation cost is justified.

### Budget Backup: Zoho (Option B)

If the COO requires a lower-cost option, Zoho CRM Enterprise + Zoho Campaigns is a credible alternative at ~RM 2,400/month (annual billing). The trade-off is more configuration effort, slightly less polished reporting, and split email automation across two Zoho products. The Singapore data centre is a bonus for data residency conversations with financial services prospects.

### Not Recommended: Pipedrive (Option C)

Pipedrive lacks parent-child account hierarchy, built-in email automation, and attribution tracking. The VoronDRQ GTM programme needs these capabilities on day one. Adding a second tool to fill the gaps creates data sync risk and operational complexity that the Marketing Ops Specialist shouldn't have to manage.

## 6. Cost Summary

| Option | Monthly (RM, monthly billing) | Monthly (RM, annual billing) | Annual (RM) |
|--------|------------------------------|-------------------------------|-------------|
| HubSpot (recommended) | ~7,600 | ~6,100 | ~73,000 |
| Zoho (backup) | ~3,600 | ~2,400 | ~29,000 |
| Pipedrive + email tool (not recommended) | ~2,800 | ~2,200 | ~26,000 |

*All prices are approximate, based on published rates as of mid-2025. Verify current pricing at time of purchase. Exchange rate assumed at USD 1 = RM 4.70.*

## 7. Decision Required

| # | Decision | Options |
|---|---------|---------|
| 1 | CRM platform selection | HubSpot (recommended) / Zoho (backup) / Pipedrive (not recommended) |
| 2 | Billing cycle | Monthly / Annual (20–34% saving) |
| 3 | Marketing Ops Specialist to lead configuration | Confirm assignment |
| 4 | Budget approval | Monthly operating cost from programme budget |
| 5 | Purchase timeline | Target: CRM live by Sep 1 (campaign launch readiness) |

---

*If HubSpot is approved, the Marketing Operations Specialist can begin configuration immediately upon hire. A 14-day free trial is available for initial exploration before commitment.*
