# WhatsApp Broadcast Cost Analysis: 10,000 Messages
## Detailed Cost Breakdown for Cognitive Operation Unit

**Version:** 1.0  
**Analysis Date:** 2026-07-02  
**Author:** DAF  
**Scenario:** 10,000 WhatsApp broadcasts/month (Malaysia focus)

---

## 📊 Executive Summary

### **Total Monthly Cost Range: RM 470 - RM 1,200 ($100 - $255)**

| Provider Tier | Monthly Cost (MYR) | Monthly Cost (USD) | Best For |
|---------------|-------------------|-------------------|----------|
| **Budget** | RM 470 - 600 | $100 - 128 | Startups, testing, low-margin ops |
| **Mid-Market** | RM 700 - 900 | $149 - 191 | Growing businesses, AI features |
| **Enterprise** | RM 1,000 - 1,200+ | $213 - 255+ | Compliance, SLA, omnichannel |

**Recommended:** **Hyperleap AI (RM 788/month)** or **Interakt (RM 716/month)**

---

## 💰 Cost Component Breakdown

### **Two-Part Pricing Structure**

```
┌─────────────────────────────────────────────────────────────┐
│  Total WhatsApp Cost = Meta Fees + BSP Provider Fees       │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│  1. META FEES (Mandatory, Non-Negotiable)                  │
│     - Charged by Meta per 24-hour conversation             │
│     - Varies by country and conversation category          │
│     - Same rate regardless of BSP choice                   │
│                                                             │
│  2. BSP FEES (Variable, Negotiable)                        │
│     - Charged by Business Solution Provider                │
│     - Platform subscription OR per-message markup          │
│     - Can be $0 to $500+/month depending on provider      │
└─────────────────────────────────────────────────────────────┘
```

---

## 📋 Meta Conversation Fees (The Fixed Cost)

### **Understanding the 24-Hour Conversation Window**

```
Customer receives broadcast → Opens 24-hour window → Unlimited replies FREE
                              within this window

Example:
09:00 - You send broadcast template (1 conversation charged)
09:15 - Customer replies "Interested" (FREE - within 24h window)
10:30 - You send follow-up with pricing (FREE - within 24h window)
14:00 - Customer asks question (FREE - within 24h window)
18:00 - You send closing message (FREE - within 24h window)
                              ↓
         All messages in 24h = 1 conversation charged
```

### **4 Conversation Categories**

| Category | Definition | Malaysia Rate | US Rate | India Rate |
|----------|------------|---------------|---------|------------|
| **Marketing** | Promotions, offers, announcements | RM 0.10 | $0.025 | $0.007 |
| **Utility** | Order updates, appointments, reminders | RM 0.06 | $0.015 | $0.002 |
| **Authentication** | OTP, verification codes | RM 0.02 | $0.005 | $0.001 |
| **Service** | Customer-initiated conversations | RM 0.00 | $0.00 | $0.00 |

**Key Insight:** Service conversations (customer-initiated) are **FREE** from Meta

---

## 🧮 Cost Calculation: 10,000 Broadcasts

### **Scenario A: 100% Marketing Broadcast**

```
Meta Fees (Malaysia):
10,000 conversations × RM 0.10 = RM 1,000/month

This is the MAXIMUM you would pay for Meta fees.
```

### **Scenario B: Mixed Campaign (Recommended)**

```
Assumption: 10,000 broadcasts trigger conversations

Breakdown:
- 5,000 Marketing (promotional broadcasts) × RM 0.10 = RM 500
- 3,000 Utility (order updates triggered by broadcast) × RM 0.06 = RM 180
- 2,000 Service (customer replies within 24h window) × RM 0.00 = RM 0

Meta Total: RM 680/month

Savings vs Scenario A: RM 320/month (32% reduction)
```

### **Scenario C: Optimized with 24-Hour Window**

```
Strategy: Send 1 template, continue conversation within 24h

Instead of:
- Day 1: Broadcast (10,000 conversations)
- Day 2: Follow-up (10,000 conversations)
- Day 3: Reminder (10,000 conversations)
Total: 30,000 conversations charged

Do this:
- Day 1: Broadcast template (10,000 conversations)
- Day 1-2: All follow-ups within 24h window (FREE)
Total: 10,000 conversations charged

Savings: 20,000 conversations × RM 0.10 = RM 2,000/month
```

---

## 🏢 BSP Provider Fees (The Variable Cost)

### **7 Provider Options Compared**

#### **1. Interakt (Budget Choice)**
```
Platform Fee: $12/month = RM 56
Meta Markup: 10% on conversation fees

Calculation (Scenario B - RM 680 Meta fees):
- Platform: RM 56
- Meta Fees: RM 680
- Markup (10%): RM 68
- Total: RM 804/month (~$171)

Pros: Cheapest, Malaysia-friendly, same-day setup
Cons: Basic AI, India-timezone support
```

#### **2. Hyperleap AI (AI-First Choice)** ⭐
```
Platform Fee: $40/month = RM 188
Meta Markup: 0% (passed at cost)

Calculation (Scenario B - RM 680 Meta fees):
- Platform: RM 188
- Meta Fees: RM 680
- Markup: RM 0
- Total: RM 868/month (~$185)

Pros: RAG-based AI, multi-channel, doc-grounded responses
Cons: Higher platform fee, no human inbox focus
```

#### **3. 360dialog (Developer Choice)**
```
Platform Fee: €49/month = RM 245
Meta Markup: 0% (passed at cost)

Calculation (Scenario B - RM 680 Meta fees):
- Platform: RM 245
- Meta Fees: RM 680
- Markup: RM 0
- Total: RM 925/month (~$197)

+ Development Cost: RM 3,000-5,000 (one-time)

Pros: Raw API, EU-hosted, cheapest long-term at scale
Cons: Requires developer, no UI, custom build needed
```

#### **4. Twilio (CPaaS Choice)**
```
Platform Fee: $0
Meta Markup: 20% on conversation fees

Calculation (Scenario B - RM 680 Meta fees):
- Platform: RM 0
- Meta Fees: RM 680
- Markup (20%): RM 136
- Total: RM 816/month (~$174)

Pros: No platform fee, global infrastructure, developer-friendly
Cons: 20% markup at scale, requires dev work
```

#### **5. Wati (Support Team Choice)**
```
Platform Fee: $49/month = RM 230
Meta Markup: 0% (passed at cost)

Calculation (Scenario B - RM 680 Meta fees):
- Platform: RM 230
- Meta Fees: RM 680
- Markup: RM 0
- Total: RM 910/month (~$194)

Pros: Shared inbox, collision detection, Shopify integration
Cons: WhatsApp-only, AI is add-on
```

#### **6. AiSensy (Marketing Choice)**
```
Platform Fee: $14/month = RM 66
Meta Markup: 15% on conversation fees

Calculation (Scenario B - RM 680 Meta fees):
- Platform: RM 66
- Meta Fees: RM 680
- Markup (15%): RM 102
- Total: RM 848/month (~$180)

Pros: Broadcast-focused, Click-to-WhatsApp ads, D2C optimized
Cons: Markup on Meta fees, limited AI
```

#### **7. Infobip (Enterprise Choice)**
```
Platform Fee: Custom (~$500/month minimum) = RM 2,350
Meta Markup: Bundled/negotiated

Calculation (Scenario B - RM 680 Meta fees):
- Platform: RM 2,350
- Meta Fees: RM 680 (may be bundled)
- Setup Fee: RM 2,800 (one-time, ~$600)
- Total Month 1: RM 5,830
- Total Month 2+: RM 3,030/month (~$645)

Pros: Enterprise SLA, compliance, omnichannel, 24/7 support
Cons: Expensive for 10K volume, 12-month contract typical
```

---

## 📊 Complete Cost Comparison Table

### **10,000 Broadcasts/Month (Malaysia, Mixed Category)**

| Provider | Platform (MYR) | Meta Fees (MYR) | Markup (MYR) | **Total/Month** | **Total/Year** | Setup Fee |
|----------|---------------|-----------------|--------------|-----------------|----------------|-----------|
| **Interakt** | RM 56 | RM 680 | RM 68 | **RM 804** | RM 9,648 | RM 0 |
| **Twilio** | RM 0 | RM 680 | RM 136 | **RM 816** | RM 9,792 | RM 0 |
| **AiSensy** | RM 66 | RM 680 | RM 102 | **RM 848** | RM 10,176 | RM 0 |
| **Hyperleap AI** | RM 188 | RM 680 | RM 0 | **RM 868** | RM 10,416 | RM 0 |
| **Wati** | RM 230 | RM 680 | RM 0 | **RM 910** | RM 10,920 | RM 0 |
| **360dialog** | RM 245 | RM 680 | RM 0 | **RM 925** | RM 11,100 | RM 0 |
| **Infobip** | RM 2,350 | RM 680 | (bundled) | **RM 3,030** | RM 36,360 | RM 2,800 |

**Note:** 360dialog requires RM 3,000-5,000 one-time development cost

---

## 🎯 Cost Optimization Strategies

### **Strategy 1: Optimize Message Category** ⭐⭐⭐

```
Before (All Marketing):
10,000 × RM 0.10 = RM 1,000 Meta fees

After (Mixed Categories):
- 5,000 Marketing × RM 0.10 = RM 500
- 3,000 Utility × RM 0.06 = RM 180
- 2,000 Service × RM 0.00 = RM 0
Total: RM 680 Meta fees

Savings: RM 320/month (RM 3,840/year)
```

**Action:** Review all templates, categorize correctly (Utility vs Marketing)

---

### **Strategy 2: Maximize 24-Hour Window** ⭐⭐⭐

```
Before (Multiple broadcasts):
- Day 1: Promo broadcast (10,000 conversations)
- Day 2: Follow-up broadcast (10,000 conversations)
- Day 3: Last chance broadcast (10,000 conversations)
Total: 30,000 conversations = RM 3,000 Meta fees

After (Single broadcast + 24h follow-ups):
- Day 1: Promo broadcast (10,000 conversations)
- Day 1-2: All follow-ups within 24h window (FREE)
Total: 10,000 conversations = RM 1,000 Meta fees

Savings: RM 2,000/month (RM 24,000/year)
```

**Action:** Consolidate messages into single template + conversation flow

---

### **Strategy 3: Drive Customer-Initiated Conversations** ⭐⭐

```
Tactic: Use Click-to-WhatsApp ads, opt-in prompts

Before (All outbound):
10,000 outbound × RM 0.10 = RM 1,000 Meta fees

After (50% customer-initiated):
- 5,000 outbound × RM 0.10 = RM 500
- 5,000 customer-initiated × RM 0.00 = RM 0
Total: RM 500 Meta fees

Savings: RM 500/month (RM 6,000/year)
```

**Action:** Add "Message us on WhatsApp" CTAs, use wa.me links

---

### **Strategy 4: Choose No-Markup Provider** ⭐⭐

```
Before (10% markup provider):
RM 680 Meta fees + RM 68 markup = RM 748

After (0% markup provider):
RM 680 Meta fees + RM 0 markup = RM 680

Savings: RM 68/month (RM 816/year)
```

**Action:** Switch to Hyperleap AI, 360dialog, or Wati (no markup)

---

### **Strategy 5: Volume Tier Negotiation** ⭐

```
At 10,000 conversations/month, you're in mid-market tier

Negotiation points:
- Commit to 12-month contract → 10-15% platform fee discount
- Pre-pay quarterly → 5-10% discount
- Multi-number deployment → Bundle pricing

Potential savings: RM 50-100/month (RM 600-1,200/year)
```

**Action:** Request custom quote, mention competitor pricing

---

## 📈 Total Cost of Ownership (TCO) Analysis

### **Year 1 Total Cost (Including Setup)**

| Provider | Monthly | Setup | **Year 1 Total** | **Effective Monthly** |
|----------|---------|-------|-----------------|----------------------|
| Interakt | RM 804 | RM 0 | **RM 9,648** | RM 804 |
| Twilio | RM 816 | RM 0 | **RM 9,792** | RM 816 |
| AiSensy | RM 848 | RM 0 | **RM 10,176** | RM 848 |
| Hyperleap AI | RM 868 | RM 0 | **RM 10,416** | RM 868 |
| Wati | RM 910 | RM 0 | **RM 10,920** | RM 910 |
| 360dialog | RM 925 | RM 4,000 | **RM 15,100** | RM 1,258 |
| Infobip | RM 3,030 | RM 2,800 | **RM 39,160** | RM 3,263 |

**Note:** 360dialog includes RM 4,000 estimated development cost

---

### **Year 3 Total Cost (Scale to 50,000 conversations)**

| Provider | Monthly (50K) | **Year 3 Total** | Notes |
|----------|---------------|-----------------|-------|
| Interakt | RM 3,500 | **RM 42,000** | 10% markup scales with volume |
| Twilio | RM 3,600 | **RM 43,200** | 20% markup scales with volume |
| Hyperleap AI | RM 3,188 | **RM 38,256** | No markup, platform fee same |
| 360dialog | RM 3,125 | **RM 37,500** | Cheapest at scale (no markup) |
| Infobip | RM 8,000 | **RM 96,000** | Enterprise pricing, negotiated |

**Key Insight:** At 50K conversations, **360dialog** and **Hyperleap AI** become cheapest (no markup)

---

## 💡 Recommended Cost Structure for Your Unit

### **Phase 1: Launch (Months 1-3)**
```
Provider: Interakt
Volume: 10,000 conversations/month
Category Mix: 50% Marketing, 30% Utility, 20% Service

Monthly Cost:
- Platform: RM 56
- Meta Fees: RM 680
- Markup (10%): RM 68
- Total: RM 804/month

Why: Lowest commitment, same-day setup, test viability
```

### **Phase 2: Optimization (Months 4-12)**
```
Provider: Hyperleap AI
Volume: 15,000 conversations/month
Category Mix: 40% Marketing, 40% Utility, 20% Service

Monthly Cost:
- Platform: RM 188
- Meta Fees: RM 840
- Markup (0%): RM 0
- Total: RM 1,028/month

Why: AI capabilities, no markup, multi-channel, better ROI
```

### **Phase 3: Scale (Year 2+)**
```
Provider: 360dialog (with custom build) OR Hyperleap AI
Volume: 50,000+ conversations/month
Category Mix: 30% Marketing, 50% Utility, 20% Service

Monthly Cost:
- Platform: RM 245 (360dialog)
- Meta Fees: RM 1,900
- Markup (0%): RM 0
- Total: RM 2,145/month

Why: Lowest cost at scale, full control, API flexibility
```

---

## 🚨 Hidden Costs to Watch

### **1. Template Rejection Costs**
```
Risk: Template rejected after campaign scheduled
Impact: Campaign delay, redesign time, potential revenue loss
Mitigation: Submit templates 48h before campaign, have backup templates
```

### **2. Quality Rating Degradation**
```
Risk: High block rate → lower sending tier → rate limits
Impact: Cannot send 10K broadcasts, must reduce volume
Mitigation: Only send to verified opt-in, monitor block rate (<1%)
```

### **3. Number Porting Downtime**
```
Risk: Switching providers → 4-24h downtime
Impact: Missed customer messages, lost conversations
Mitigation: Schedule porting during low-traffic, notify customers
```

### **4. Development Costs (API Providers)**
```
Risk: Underestimated dev time for 360dialog/Twilio
Impact: RM 5,000-15,000 one-time cost, 2-4 weeks dev time
Mitigation: Get quotes upfront, use existing templates/scripts
```

### **5. Overage Charges**
```
Risk: Exceed conversation limit in flat-fee plans
Impact: RM 0.10-0.15 per extra conversation (higher than base rate)
Mitigation: Monitor usage, set alerts at 80% of limit
```

---

## 📋 Pre-Signup Cost Checklist

```markdown
## Pricing Verification
- [ ] Confirm Meta fee markup % (get in writing)
- [ ] Verify platform fee includes all features
- [ ] Check for overage charges beyond plan limits
- [ ] Ask about volume discounts at 25K, 50K, 100K
- [ ] Confirm billing currency (USD vs MYR vs EUR)

## Contract Terms
- [ ] Contract length (monthly vs annual)
- [ ] Cancellation policy (30 days notice?)
- [ ] Setup fee (negotiate waiver if >$0)
- [ ] Payment terms (credit card vs invoice)
- [ ] Price lock guarantee (12-24 months)

## Hidden Fees
- [ ] Phone number porting fee
- [ ] Template submission fee
- [ ] Additional user/agent fees
- [ ] API call limits/throttling
- [ ] Premium support charges
```

---

## 🎯 Final Recommendation

### **For 10,000 Broadcasts/Month (Malaysia)**

| Priority | Provider | Monthly Cost | Why |
|----------|----------|--------------|-----|
| **Budget** | Interakt | RM 804 | Cheapest, Malaysia-friendly |
| **Value** | Hyperleap AI | RM 868 | AI features, no markup, multi-channel |
| **Control** | 360dialog | RM 925 + dev | API access, cheapest at scale |
| **Avoid** | Infobip | RM 3,030 | Overkill for 10K volume |

### **My Recommendation: Hyperleap AI**

```
Total Cost: RM 868/month (~$185)

Breakdown:
- Platform: RM 188 (22%)
- Meta Fees: RM 680 (78%)
- Markup: RM 0 (0%)

Value Proposition:
✅ RAG-based AI chatbot (cognitive ops capability)
✅ Multi-channel (Web + WA + IG + FB)
✅ No Meta fee markup
✅ 7-day free trial
✅ Monthly contract (no lock-in)
✅ 3-5 day setup time

ROI Calculation:
- If AI handles 30% of inbound queries automatically
- Saves 30 hours/month human agent time
- At RM 20/hour = RM 600/month savings
- Net cost: RM 868 - RM 600 = RM 268/month

Effective cost for 10K broadcasts: RM 0.027 per message
```

---

## 📞 Next Actions

1. **Start Hyperleap AI 7-day trial** - https://hyperleap.ai/pricing
2. **Prepare 3-5 message templates** - Use `compliance/meta-policy.md` for guidelines
3. **Clean contact list** - Ensure 100% opt-in compliance
4. **Run pilot (500 contacts)** - Test delivery, engagement, costs
5. **Scale to 10K** - Monitor quality rating, adjust category mix

**Questions?** Review full provider comparison: `docs/provider-options-2026.md`

---

**Last Updated:** 2026-07-02  
**Next Review:** After first month of actual usage (compare projected vs actual)

**Document Owner:** DAF  
**Budget Approval:** [Pending]
