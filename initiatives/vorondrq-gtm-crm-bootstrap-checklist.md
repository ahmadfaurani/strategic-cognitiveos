---
id: INIT-20260813-006
record_type: initiative
title: "VoronDRQ GTM CRM Bootstrap Checklist"
created_at: 2026-08-13T00:00:00Z
owner: faurani-jaafar
status: active
portfolio_tier: incubation
readiness_level: concept
summary: "Reference document — see body for details."
sensitivity: internal
lifecycle_state: canonical
tags:
  - type/reference-document
---

# VoronDRQ GTM — HubSpot CRM Bootstrap Checklist

**Goal:** Working CRM in 2–3 days, before Marketing Ops Specialist is hired
**Platform:** HubSpot Sales Hub Professional (14-day free trial → paid after approval)
**Owner:** DAF (with support from Ember for data prep)
**Start date:** August 9, 2026 (Saturday)

---

## Pre-Flight (Before You Start)

- [ ] Go to https://www.hubspot.com and sign up for Sales Hub Professional trial (14 days free)
- [ ] Use your Aras Integrasi email (daf@arasintegrasi.ai) as admin account
- [ ] Have the 193-org prospect database ready (the spreadsheet you built)
- [ ] Have the 15-account pilot list ready (8 Lighthouse + 7 Conversion)

---

## Day 1 — Pipeline & Account Foundation (2–3 hours)

### Step 1: Company & Account Setup

- [ ] Set company name: Aras Integrasi Sdn Bhd
- [ ] Set timezone: UTC+8 (Malaysia)
- [ ] Set currency: MYR (RM)
- [ ] Set fiscal year start: January

### Step 2: Configure Custom Pipeline (7-Stage)

Navigate to: Sales → Deals → Pipelines → Create Pipeline
Name it: **VoronDRQ GTM Pipeline**

Create these 7 stages in order:

| Stage # | Name | What It Means |
|---------|------|---------------|
| 1 | Account Validated | Target confirmed as viable (regulatory pressure, installed stack, budget signal) |
| 2 | Stakeholder Verified | At least 1 key stakeholder identified and contactable |
| 3 | Qualified | Discovery call booked or completed — pain confirmed |
| 4 | Discovery Session | Formal discovery meeting held — requirements documented |
| 5 | Demonstration | VoronDRQ demo delivered to stakeholder(s) |
| 6 | POC Definition | POC scope agreed — proposal sent — verbal commitment |
| 7 | Commercial Conversion | Contract signed / POC converted to commercial engagement |

- [ ] Set probability weights for each stage (optional but useful for forecasting):
  - 1-Account Validated: 5%
  - 2-Stakeholder Verified: 10%
  - 3-Qualified: 20%
  - 4-Discovery Session: 35%
  - 5-Demonstration: 50%
  - 6-POC Definition: 70%
  - 7-Commercial Conversion: 100%

### Step 3: Import the 193-Organisation Database

- [ ] Prepare your spreadsheet with these columns (rename if needed):
  - Company Name
  - Parent Group (e.g., Maybank Group, CIMB Group)
  - Market Segment (Tier 1–6)
  - Sub-segment (Bank, Insurance, Islamic Banking, DFI, MSB, Asset Mgmt, E-money, GLC, Fintech)
  - Website
  - HQ City
  - Estimated Employee Count (if available)
  - Regulatory Body (BNM, SC, etc.)
  - Notes

- [ ] Navigate to: Contacts → Import → Import Companies
- [ ] Upload CSV
- [ ] Map columns to HubSpot Company properties
- [ ] Map "Parent Group" to a custom property (create: "Parent Group Name" — single-line text)
- [ ] Map "Market Segment" to a custom property (create: "Market Segment" — dropdown: Tier 1 / Tier 2 / Tier 3 / Tier 4 / Tier 5 / Tier 6)
- [ ] Map "Sub-segment" to a custom property (create: "Sub-segment" — dropdown)
- [ ] Import

### Step 4: Set Up Parent-Child Account Hierarchy (15 Pilot Accounts Only)

For each of the 15 pilot accounts, create the parent-child relationships:

**How in HubSpot:**
- [ ] Open a child company (e.g., Maybank Investment Bank)
- [ ] In the right sidebar, find "Parent Company" association
- [ ] Link to parent (e.g., Maybank Group)
- [ ] Repeat for all subsidiaries under each parent

**The 15 pilot groups and their buying centres:**

**Lighthouse (8):**

1. **Maybank Group**
   - Maybank Investment Bank
   - Maybank Islamic
   - Etiqa Insurance
   - (add others as relevant)

2. **CIMB Group**
   - CIMB Investment Bank
   - CIMB Islamic
   - Sun Life Malaysia Takaful

3. **RHB Group**
   - RHB Investment Bank
   - RHB Islamic

4. **Hong Leong Group**
   - Hong Leong Investment Bank
   - Hong Leong Islamic Banking

5. **Public Bank Group**
   - Public Islamic Bank
   - (add subsidiaries)

6. **Affin Bank Group**
   - Affin Hwang Investment Bank
   - Affin Islamic

7. **Bank Islam Group (BIMB)**
   - (subsidiaries as relevant)

8. **Alliance Bank Group**
   - (subsidiaries as relevant)

**Conversion (7):**

9. **Bank Muamalat**
10. **Kuwait Finance House Malaysia**
11. **MIDF**
12. **Kenanga Investment Bank**
13. **BPMB (Bank Pembangunan)**
14. **EXIM Bank Malaysia**
15. **Etiqa** (if separate from Maybank Group — otherwise linked as child)

- [ ] For single-entity groups (Bank Muamalat, KFH Malaysia, etc.), just create the company record — no parent needed

---

## Day 2 — Dashboard, Users & Shortlist (2–3 hours)

### Step 5: Create Executive Dashboard

Navigate to: Reports → Dashboards → Create Dashboard
Name it: **VoronDRQ GTM — Executive View**

Add these report cards:

- [ ] **Pipeline Overview** — Deal count and value by stage (bar chart)
- [ ] **Accounts Activated** — Count of companies in Stages 1–7 (single number)
- [ ] **Stakeholders Engaged** — Count of contacts associated with deals (single number)
- [ ] **Discovery Sessions Booked** — Deals in Stage 4 (single number)
- [ ] **Demos Delivered** — Deals in Stage 5 (single number)
- [ ] **POCs in Flight** — Deals in Stage 6 (single number)
- [ ] **Conversion Rate** — Stage 7 count / Stage 1 count (calculated)
- [ ] **By Market Segment** — Deal count grouped by Market Segment (bar chart)

- [ ] Set dashboard visibility: Share with team (all users)

### Step 6: Create the 15-Account Shortlist Deal Records

For each of the 15 pilot accounts:

- [ ] Create a Deal named: "[Group Name] — VoronDRQ GTM"
- [ ] Set pipeline: VoronDRQ GTM Pipeline
- [ ] Set stage: Account Validated (Stage 1)
- [ ] Link to the parent company record
- [ ] Set Deal value: leave blank for now (or set nominal RM 50,000 placeholder for tracking)
- [ ] Set close date: 31 December 2026 (placeholder — will refine as POCs define)

This gives you 15 deals in Stage 1 — the starting position for the working session.

### Step 7: Invite Users

Navigate to: Settings → Users & Teams → Invite Users

- [ ] Invite Shuhada (shuhada@arasintegrasi.ai) — Sales access (full deals, contacts)
- [ ] Invite Fuad (fuad's email) — Read-only or Sales access (needs to see demo-stage deals)
- [ ] Invite Hadri (hadri@arasintegrasi.ai) — Read-only (needs to see POC-stage deals)
- [ ] Set up user roles:
  - DAF: Super Admin
  - Shuhada: Sales Manager (full access to deals, contacts, companies)
  - Fuad: Sales Agent (own deals visible) or Read-Only if preferred
  - Hadri: Read-Only

Note: Don't invite Kenny, Azzatullina, or Account Owners yet. Invite them after the working session — you want the CRM to show progress first, not an empty system.

---

## Day 3 — Refinement & Working Session Prep (1–2 hours)

### Step 8: Create Stakeholder Contact Records (For 3 Pilot Accounts)

You don't need all 15 accounts' stakeholders loaded — just 3 to demonstrate the structure at the working session.

Pick 3 accounts where you already know stakeholder names:
- [ ] Account 1: Add 2–3 stakeholder contacts (CISO, CIO/CTO, Head of GRC)
- [ ] Account 2: Add 2–3 stakeholder contacts
- [ ] Account 3: Add 2–3 stakeholder contacts

For each contact:
- [ ] Name, title, email, LinkedIn profile URL
- [ ] Associate with the company record
- [ ] Tag with custom property: "Stakeholder Role" (dropdown: CISO / CIO-CTO / Head of GRC / CRO / Head of Compliance / CFO / Head of Internal Audit)

### Step 9: Create a "Working Session Demo" View

- [ ] Create a custom Deal view: "Pilot Accounts — Working Session View"
- [ ] Filter: Pipeline = VoronDRQ GTM Pipeline, Stage = Account Validated
- [ ] Columns: Deal Name, Company, Market Segment, Parent Group, Stakeholder Count, Last Activity
- [ ] This is what you'll show Kenny on screen — 15 named accounts, structured, ready

### Step 10: Test Mobile Access

- [ ] Download HubSpot mobile app
- [ ] Log in
- [ ] Verify you can see the pipeline and deals on phone
- [ ] This is what Account Owners will use during client visits

---

## What You're NOT Doing During Bootstrap

These are deferred to the Marketing Ops Specialist:

| Capability | Why It Can Wait |
|-----------|---------------|
| Email sequence automation | No campaign launching until Fuad validates + Azzatullina co-designs |
| Campaign attribution tracking | Need campaign structure defined first |
| LinkedIn Sales Navigator integration | Need LN SN licenses purchased (Kenny approval) |
| A/B testing | No campaigns to test yet |
| Advanced reporting / attribution models | Basic dashboard is enough for working session |
| Marketing email templates | Azzatullina owns messaging — not our call |
| Workflow automation | Manual is fine for 15 accounts |
| Custom properties beyond basics | Add as needed during campaign build |

---

## Cost During Bootstrap

| Period | Cost |
|--------|------|
| Days 1–14 (free trial) | RM 0 |
| After trial (if approved) | ~RM 6,100/month (annual) or ~RM 7,600/month (monthly) |
| Before Kenny approves | Cancel trial if not approved — no financial commitment |

---

## Working Session Presentation (What You Show)

When you sit down with Kenny, Azzatullina, and Shuhada:

1. **Open HubSpot on screen** — live CRM, not a slide deck
2. **Show the 15-account pipeline** — all in Stage 1, named, structured
3. **Drill into one account** — show parent-child hierarchy (e.g., Maybank Group → 3 buying centres)
4. **Show stakeholder contacts** — 3 accounts loaded with named stakeholders, tagged by role
5. **Show the executive dashboard** — accounts activated, pipeline by stage, by segment
6. **Show mobile app** — "this is what your Account Owners will carry into client meetings"
7. **Say:** "The CRM is live. The team structure is defined. The 15 accounts are loaded. What I need from this meeting is your approval on hires and budget so we can start outreach by September 1."

---

## Success Criteria for Bootstrap

| Criterion | How to Verify |
|-----------|--------------|
| CRM is live and accessible | Log in, see dashboard |
| 193 orgs imported as company records | Companies → search "bank" → see results |
| 15 pilot accounts have deals in Stage 1 | Pipeline view → 15 deals visible |
| Parent-child hierarchy for 8 Lighthouse groups | Open Maybank Group → see child companies |
| 3 accounts have stakeholder contacts loaded | Open deal → see associated contacts |
| Executive dashboard renders | Reports → Dashboard → all cards populated |
| Shuhada, Fuad, Hadri invited | Settings → Users → 4 users listed |
| Mobile app works | Open app → see pipeline |

---

*This checklist is designed to be completed solo by DAF in 2–3 focused sessions. Ember can assist with data preparation (CSV formatting, account list refinement) but cannot access HubSpot directly.*
