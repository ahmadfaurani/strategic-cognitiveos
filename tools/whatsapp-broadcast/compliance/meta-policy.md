# WhatsApp Business Policy & Compliance Guide

**Version:** 1.0  
**Last Updated:** 2026-07-02  
**Based on:** Meta WhatsApp Business Policy (2026)  
**Author:** DAF

---

## ⚠️ Important Notice

This document summarizes key compliance requirements for WhatsApp Business API usage. **Always refer to the official Meta documentation for the most current policies:**

- **WhatsApp Business Policy:** https://www.whatsapp.com/legal/business-policy
- **Commerce Policy:** https://www.whatsapp.com/legal/commerce-policy
- **Terms of Service:** https://www.whatsapp.com/legal/terms-of-service

---

## 📋 Table of Contents

1. [Core Principles](#core-principles)
2. [Opt-in Requirements](#opt-in-requirements)
3. [Message Categories](#message-categories)
4. [Template Guidelines](#template-guidelines)
5. [Prohibited Content](#prohibited-content)
6. [Quality Rating System](#quality-rating-system)
7. [Rate Limits & Tiers](#rate-limits--tiers)
8. [Data Protection](#data-protection)
9. [Enforcement & Penalties](#enforcement--penalties)
10. [Compliance Checklist](#compliance-checklist)

---

## 🎯 Core Principles

### **WhatsApp's Three Pillars**

```
┌─────────────────────────────────────────────────────────┐
│                  WhatsApp Business Principles            │
├─────────────────────────────────────────────────────────┤
│  1. USER CONSENT                                        │
│     • No unsolicited messages                           │
│     • Clear opt-in required before first message        │
│     • Easy opt-out mechanism mandatory                  │
├─────────────────────────────────────────────────────────┤
│  2. RELEVANT CONTENT                                    │
│     • Messages must match user expectations             │
│     • Template category must align with content         │
│     • No bait-and-switch tactics                        │
├─────────────────────────────────────────────────────────┤
│  3. QUALITY EXPERIENCE                                  │
│     • High delivery and engagement rates                │
│     • Low block and spam report rates                   │
│     • Respectful frequency and timing                   │
└─────────────────────────────────────────────────────────┘
```

### **Business Responsibilities**

As a WhatsApp Business API user, you must:

1. **Obtain explicit consent** before sending any messages
2. **Provide value** in every interaction
3. **Respect user preferences** (opt-out, frequency, timing)
4. **Protect user data** (encryption, access control, retention limits)
5. **Monitor quality metrics** (delivery, blocks, reports)
6. **Comply with local laws** (GDPR, PDPA, TCPA, etc.)

---

## ✅ Opt-in Requirements

### **What is Opt-in?**

Opt-in is **explicit user consent** to receive messages from your business on WhatsApp. Without valid opt-in, you **cannot legally or compliantly** send messages.

### **Acceptable Opt-in Methods**

#### ✅ **APPROVED METHODS**

| Method | Description | Example | Evidence Required |
|--------|-------------|---------|-------------------|
| **User-initiated message** | Customer messages you first | Clicks wa.me link, sends "Hi" | Conversation history |
| **Website checkbox** | Unchecked checkbox on form | "☐ Send me updates on WhatsApp" | Form submission log, IP, timestamp |
| **Mobile app permission** | In-app consent prompt | Push notification permission flow | App event log, device ID |
| **API import with proof** | Import contacts with consent records | CRM import with timestamps | Consent database records |
| **Click-to-WhatsApp ad** | Facebook/Instagram ad → WhatsApp | "Send Message" button | Ad click log, Meta conversion event |
| **QR code scan** | Physical/digital QR → WhatsApp chat | Restaurant menu QR code | Scan event, session start |
| **In-store signup** | POS system or tablet | Customer enters number at checkout | Transaction log, signed form |
| **Verbal consent** | Phone/in-person with recording | "Can we send order updates via WhatsApp?" | Call recording, transcript |
| **Business card exchange** | With explicit consent note | "Added from business card - consented to WhatsApp updates" | CRM note, context |
| **Loyalty program** | Enrollment with WhatsApp option | "Receive rewards via WhatsApp" | Program enrollment record |

#### ❌ **PROHIBITED METHODS**

| Method | Why Prohibited | Risk |
|--------|----------------|------|
| **Purchased lists** | No consent proof | Immediate ban |
| **Scraped numbers** | No relationship | Ban + legal risk |
| **Pre-checked boxes** | Not explicit consent | Policy violation |
| **Implied consent** | "By using our site..." | Invalid opt-in |
| **Third-party lists** | Consent not transferable | Policy violation |
| **Legacy SMS opt-in** | Channel-specific consent required | Invalid for WhatsApp |

### **Opt-in Record Requirements**

Every opt-in must be **documented and provable**:

```json
{
  "opt_in_record": {
    "contact": {
      "phone_number": "+60123456789",
      "name": "John Doe",
      "contact_id": "UUID-12345"
    },
    "consent": {
      "type": "marketing",  // marketing, utility, authentication, service
      "method": "website_checkbox",
      "timestamp": "2026-07-01T14:30:00Z",
      "ip_address": "203.106.8.123",
      "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)...",
      "language": "en"
    },
    "proof": {
      "form_url": "https://example.com/newsletter-signup",
      "form_version": "v2.1",
      "checkbox_text": "Yes, send me marketing updates on WhatsApp",
      "privacy_policy_url": "https://example.com/privacy",
      "terms_url": "https://example.com/terms",
      "screenshot_url": "https://example.com/consent-proof/12345.png"
    },
    "double_opt_in": {
      "enabled": true,
      "confirmation_sent": true,
      "confirmation_timestamp": "2026-07-01T14:31:00Z",
      "confirmation_message_id": "wamid.HBgNNjAxMjM0NTY3ODkVAgARGBI5QTJCM0Q0RTVGNkc3SDhJAA=="
    }
  }
}
```

### **Opt-in Best Practices**

```markdown
## ✅ DO:
- Use clear, specific language ("WhatsApp" explicitly mentioned)
- Separate consent for different message types (marketing vs transactional)
- Implement double opt-in (recommended for marketing)
- Store opt-in records indefinitely (or per local law)
- Make opt-in easy to find and understand

## ❌ DON'T:
- Use vague language ("We may contact you")
- Bundle WhatsApp consent with general T&Cs
- Assume consent from other channels (SMS, email)
- Share opt-in data with third parties
- Use pre-checked boxes or dark patterns
```

### **Opt-out Requirements**

**Every marketing message must include an opt-out mechanism:**

```
Example Footer for Marketing Templates:
─────────────────────────────────────────
Reply STOP to unsubscribe
Msg & data rates may apply
─────────────────────────────────────────
```

**Opt-out Processing:**

1. **Automatic detection**: Monitor for STOP, UNSUBSCRIBE, CANCEL, END, QUIT
2. **Immediate action**: Suppress within 24 hours (ideally instant)
3. **Confirmation message**: "You've been unsubscribed. Reply START to re-subscribe."
4. **Permanent suppression**: Do not re-add without fresh opt-in
5. **Cross-channel sync**: Update all systems (CRM, ESP, etc.)

---

## 📤 Message Categories

WhatsApp classifies messages into **four categories**, each with distinct rules:

### **1. MARKETING**

**Purpose:** Promotional content, product announcements, sales, offers

**Examples:**
- "Flash Sale: 50% off all items!"
- "New Collection Launch - Shop Now"
- "Exclusive offer for VIP members"
- "Abandoned cart reminder with discount"

**Rules:**
- ✅ Requires explicit marketing opt-in
- ✅ Must include opt-out mechanism
- ✅ Subject to 24-hour messaging window (for free-form)
- ⚠️ Highest conversation fees
- ⚠️ Most scrutinized by Meta review

**Template Approval Tips:**
- Avoid exaggerated claims ("Best ever!", "Guaranteed!")
- Include specific terms and conditions
- Clear value proposition
- Professional tone, no spammy language

---

### **2. UTILITY**

**Purpose:** Transactional messages related to user actions

**Examples:**
- Order confirmations
- Shipping notifications
- Payment receipts
- Appointment reminders
- Account statements
- Billing alerts

**Rules:**
- ✅ Requires transactional relationship (user made purchase, booked service)
- ✅ No promotional content allowed
- ✅ Lower conversation fees than marketing
- ✅ Higher delivery rates expected

**Template Approval Tips:**
- Must be triggered by specific user action
- Include relevant transaction details (order #, date, amount)
- No upselling or cross-selling
- Keep factual and concise

**❌ Common Rejection:**
```
Rejected: "Your order #12345 is shipped! 🎉 Also check out our new collection!"
Reason: Marketing content in utility template
Fix: Remove promotional sentence
```

---

### **3. AUTHENTICATION**

**Purpose:** One-time passwords (OTP), login verification, account security

**Examples:**
- "Your OTP is 123456. Valid for 10 minutes."
- "Verify your email with code: ABCDEF"
- "Login attempt detected. Code: 789012"

**Rules:**
- ✅ No opt-in required (legitimate interest)
- ✅ Lowest conversation fees
- ✅ Must be time-sensitive (typically 30 minutes validity)
- ❌ Cannot include any marketing content
- ❌ Cannot be used for non-authentication purposes

**Template Approval Tips:**
- Keep message short and clear
- Include validity period
- No branding beyond business name
- No links or buttons (security risk)

**Example Template:**
```
Your {{1}} verification code is {{2}}. 
Valid for {{3}} minutes. Do not share this code.
```

---

### **4. SERVICE (User-Initiated)**

**Purpose:** Customer service responses within 24-hour window

**Examples:**
- Responses to customer inquiries
- Support ticket updates
- Follow-up questions
- Issue resolution confirmations

**Rules:**
- ✅ Free-form messages allowed (no template needed)
- ✅ Only within 24 hours of customer's last message
- ✅ No conversation fees for first 1,000 service conversations/month
- ❌ Cannot initiate conversation (must be customer-first)
- ❌ After 24h window, must use template (marketing/utility)

**24-Hour Session Window:**

```
Customer Message → 24-Hour Session Opens → Free-form Replies Allowed
                          ↓
                  24 Hours Elapse
                          ↓
              Session Closes → Template Required for Further Messages
```

**Strategy:** Use service conversations to:
- Resolve issues quickly
- Gather feedback
- Request opt-in for future marketing
- Escalate to human agent if needed

---

## 📝 Template Guidelines

### **Template Structure**

```
┌─────────────────────────────────────────────────────────┐
│                    WhatsApp Template                    │
├─────────────────────────────────────────────────────────┤
│  HEADER (Optional)                                      │
│  • Text (60 chars max) or Image/Video/Document          │
│  • Example: "Order Update" or company logo              │
├─────────────────────────────────────────────────────────┤
│  BODY (Required)                                        │
│  • Main message content (1024 chars max)                │
│  • Variables: {{1}}, {{2}}, {{3}}...                    │
│  • Example: "Hi {{1}}, your order {{2}} has shipped!"   │
├─────────────────────────────────────────────────────────┤
│  FOOTER (Optional)                                      │
│  • Short text (60 chars max)                            │
│  • Example: "Thank you for shopping with us!"           │
├─────────────────────────────────────────────────────────┤
│  BUTTONS (Optional, up to 3)                            │
│  • Quick Reply: "Track Order", "Contact Support"        │
│  • Call-to-Action: Visit URL, Call Phone                │
│  • Example: [Track Order] [Contact Us]                  │
└─────────────────────────────────────────────────────────┘
```

### **Template Approval Process**

```
1. Draft Template
       ↓
2. Internal Review (Compliance + Legal)
       ↓
3. Submit via BSP Dashboard or API
       ↓
4. Meta Review Queue (24-48 hours typical)
       ↓
5. Decision
   ┌──────────────┬─────────────────────────────────────┐
   │   APPROVED   │            REJECTED                 │
   │      ✅      │               ❌                    │
   └──────────────┴─────────────────────────────────────┘
       ↓                        ↓
   Template Active        Review Rejection Reason
       ↓                        ↓
   Ready for Campaign     Revise & Resubmit
```

### **Common Rejection Reasons & Fixes**

| Rejection Reason | Example | Fix |
|------------------|---------|-----|
| **Marketing in Utility** | "Your order shipped! 🎉 Get 20% off next purchase." | Remove promotional content |
| **Incomplete Variables** | "Hi {{}}, your order..." | Provide variable examples in submission |
| **Prohibited Content** | "Bet now on our casino!" | Remove gambling/adult/political content |
| **Broken Media URL** | Image returns 404 | Fix or replace media link |
| **Misleading Claims** | "Guaranteed 100% profit!" | Remove exaggerated claims |
| **Contact Info Missing** | No business name or contact | Add business identification |
| **Wrong Category** | Authentication template for marketing | Select correct category |
| **URL Without Context** | "Click here: https://..." | Use button with descriptive text |

### **Template Examples**

#### ✅ **Approved Marketing Template**

```json
{
  "name": "summer_sale_2026",
  "category": "MARKETING",
  "language": "en",
  "components": [
    {
      "type": "HEADER",
      "format": "IMAGE",
      "image": {
        "link": "https://example.com/images/summer-sale.jpg"
      }
    },
    {
      "type": "BODY",
      "text": "Hi {{1}}! 🌞 Our Summer Sale is here!\n\nGet {{2}}% off on all {{3}}.\n\nUse code: SUMMER{{4}}\nValid until {{5}}.\n\nShop now before items sell out!",
      "variables": [
        {"type": "text", "example": "John"},
        {"type": "text", "example": "50"},
        {"type": "text", "example": "swimwear"},
        {"type": "text", "example": "2026"},
        {"type": "text", "example": "July 31, 2026"}
      ]
    },
    {
      "type": "BUTTONS",
      "buttons": [
        {
          "type": "QUICK_REPLY",
          "text": "Shop Now"
        },
        {
          "type": "QUICK_REPLY",
          "text": "View Catalog"
        }
      ]
    },
    {
      "type": "FOOTER",
      "text": "Reply STOP to unsubscribe"
    }
  ]
}
```

#### ✅ **Approved Utility Template**

```json
{
  "name": "order_shipped",
  "category": "UTILITY",
  "language": "en",
  "components": [
    {
      "type": "HEADER",
      "format": "TEXT",
      "text": "Order Shipped"
    },
    {
      "type": "BODY",
      "text": "Hi {{1}},\n\nGreat news! Your order #{{2}} has been shipped.\n\nEstimated Delivery: {{3}}\nTracking: {{4}}\n\nThank you for your purchase!",
      "variables": [
        {"type": "text", "example": "John"},
        {"type": "text", "example": "ORD-12345"},
        {"type": "text", "example": "July 5, 2026"},
        {"type": "text", "example": "https://track.example.com/12345"}
      ]
    },
    {
      "type": "BUTTONS",
      "buttons": [
        {
          "type": "QUICK_REPLY",
          "text": "Track Order"
        },
        {
          "type": "QUICK_REPLY",
          "text": "Contact Support"
        }
      ]
    }
  ]
}
```

---

## 🚫 Prohibited Content

### **Absolutely Prohibited (Account Ban Risk)**

| Category | Examples | Notes |
|----------|----------|-------|
| **Illegal goods/services** | Drugs, weapons, counterfeit goods | Violates law + policy |
| **Adult content** | Pornography, sexual services, dating (explicit) | Zero tolerance |
| **Gambling** | Casinos, betting, lottery (without license) | Licensed operators may apply |
| **Tobacco/vaping** | Cigarettes, e-cigarettes, accessories | Some regions allow with age-gating |
| **Weapons** | Firearms, ammunition, explosives | Illegal everywhere |
| **Multi-level marketing** | Pyramid schemes, get-rich-quick | High spam risk |
| **Misinformation** | False health claims, election misinformation | Context-dependent |
| **Hate speech** | Racist, sexist, discriminatory content | Zero tolerance |
| **Harassment** | Threats, bullying, doxxing | Zero tolerance |

### **Restricted (Case-by-Case Approval)**

| Category | Requirements | Notes |
|----------|--------------|-------|
| **Alcohol** | Age-gating, licensed retailer, region-compliant | Not allowed in Muslim-majority countries |
| **Dating** | No explicit content, 18+ only | Must comply with local laws |
| **Real money gaming** | Licensed, regulated markets only | Documentation required |
| **Cryptocurrency** | Licensed exchanges, no ICO promotions | High scrutiny |
| **Healthcare** | Licensed providers, no miracle claims | HIPAA/GDPR compliance required |
| **Political** | Varies by region, election period restrictions | Check local laws |
| **Subscription services** | Clear pricing, easy cancellation | No hidden fees |

### **Gray Areas (Use Caution)**

| Content | Risk Level | Guidance |
|---------|------------|----------|
| **Discount codes** | Low | Allowed if not misleading |
| **Testimonials** | Low-Medium | Must be genuine, verifiable |
| **Limited-time offers** | Low | Must have real deadline |
| **Comparative claims** | Medium | Must be substantiated |
| **Before/after images** | Medium-High | Common in beauty/fitness, avoid exaggerated claims |
| **User-generated content** | Medium | Must have permission, moderate content |

---

## ⭐ Quality Rating System

### **What is Quality Rating?**

Meta assigns a **Quality Rating** to each WhatsApp Business phone number based on user feedback and engagement metrics.

### **Rating Levels**

```
┌─────────────────────────────────────────────────────────┐
│                  Quality Rating Scale                    │
├─────────────────────────────────────────────────────────┤
│  HIGH (⭐⭐⭐⭐⭐)                                          │
│  • Excellent user engagement                            │
│  • Very low block/report rate                           │
│  • Full sending limits                                  │
│  • Priority template review                             │
├─────────────────────────────────────────────────────────┤
│  MEDIUM (⭐⭐⭐)                                           │
│  • Moderate engagement                                  │
│  • Some blocks/reports                                  │
│  • Standard sending limits                              │
│  • Normal template review                               │
├─────────────────────────────────────────────────────────┤
│  LOW (⭐)                                                │
│  • Poor engagement                                      │
│  • High block/report rate                               │
│  • Reduced sending limits                               │
│  • Extended template review                             │
│  • Risk of suspension                                   │
├─────────────────────────────────────────────────────────┤
│  UNKNOWN (❓)                                             │
│  • New phone number                                     │
│  • Insufficient data                                    │
│  • Standard limits until rating established             │
└─────────────────────────────────────────────────────────┘
```

### **Factors Affecting Quality Rating**

#### **Positive Signals (Improve Rating)**

```yaml
High Delivery Rate:
  - Target: >95%
  - Indicates: Valid numbers, good list hygiene

High Read Rate:
  - Target: >60%
  - Indicates: Relevant content, good timing

High Engagement:
  - Button clicks, replies, shares
  - Indicates: Valuable content

Low Block Rate:
  - Target: <1%
  - Indicates: Users want your messages

Low Spam Report Rate:
  - Target: <0.1%
  - Indicates: Expected, consented messages

Positive Replies:
  - "Thanks!", "Helpful", "Yes please"
  - Indicates: Good user experience
```

#### **Negative Signals (Degrade Rating)**

```yaml
High Block Rate:
  - Users blocking your number
  - Impact: Severe (major negative signal)
  
High Spam Report Rate:
  - Users clicking "Report as Spam"
  - Impact: Severe (triggers review)
  
Low Read Rate:
  - <20% of messages read
  - Impact: Moderate (content relevance issue)
  
High Opt-out Rate:
  - >5% replying STOP
  - Impact: Moderate (frequency/relevance issue)
  
Invalid Numbers:
  - High bounce rate
  - Impact: Moderate (list quality issue)
  
Policy Violations:
  - Sending without opt-in, prohibited content
  - Impact: Critical (immediate action)
```

### **Quality Rating Monitoring**

**Check Your Rating:**

```bash
# Via Meta Graph API
GET https://graph.facebook.com/v17.0/{PHONE_NUMBER_ID}/quality_rating
Authorization: Bearer {ACCESS_TOKEN}

# Response Example
{
  "quality_rating": "HIGH",  // or MEDIUM, LOW, UNKNOWN
  "last_updated": "2026-07-02T08:00:00Z"
}
```

**Improving Low Rating:**

```markdown
## Immediate Actions (If Rating = LOW)
1. Pause all marketing campaigns
2. Review recent messages for policy violations
3. Clean contact list (remove invalid numbers)
4. Check opt-in records for all recipients
5. Reduce send frequency

## Medium-Term Improvements
1. Improve segmentation (target engaged users only)
2. A/B test content (find what resonates)
3. Optimize send times (when users are active)
4. Add more value (exclusive offers, useful info)
5. Request user feedback (survey, rating)

## Long-Term Strategy
1. Build consent-driven list (quality over quantity)
2. Personalize messages (name, preferences, behavior)
3. Maintain consistent brand voice
4. Monitor metrics weekly (catch issues early)
5. Train team on WhatsApp best practices
```

---

## 📊 Rate Limits & Tiers

### **Phone Number Tiers**

Meta assigns **sending tiers** based on phone number quality and history:

```
┌─────────────────────────────────────────────────────────┐
│              WhatsApp Sending Tiers (2026)               │
├─────────────────────────────────────────────────────────┤
│  Tier 1: 1,000 messages / 24 hours                      │
│  • Default for new phone numbers                        │
│  • Upgrade: Maintain HIGH quality for 7+ days           │
├─────────────────────────────────────────────────────────┤
│  Tier 2: 10,000 messages / 24 hours                     │
│  • Standard for established businesses                  │
│  • Upgrade: Maintain HIGH quality for 14+ days          │
├─────────────────────────────────────────────────────────┤
│  Tier 3: 100,000 messages / 24 hours                    │
│  • High-volume senders                                  │
│  • Upgrade: Request review, demonstrate quality         │
├─────────────────────────────────────────────────────────┤
│  Tier 4: Unlimited                                      │
│  • Enterprise-scale, verified businesses                │
│  • Requires manual approval from Meta                   │
└─────────────────────────────────────────────────────────┘
```

### **Tier Upgrade Process**

```
Tier 1 → Tier 2:
  Requirements:
  - 7+ days of consistent sending
  - Quality rating: HIGH
  - Delivery rate: >95%
  - No policy violations
  Process: Automatic (system evaluates daily)

Tier 2 → Tier 3:
  Requirements:
  - 14+ days at Tier 2
  - Quality rating: HIGH
  - Delivery rate: >95%
  - Block rate: <1%
  Process: Automatic (system evaluates daily)

Tier 3 → Tier 4:
  Requirements:
  - 30+ days at Tier 3
  - Quality rating: HIGH
  - Enterprise verification
  - Use case documentation
  Process: Manual (request via BSP or Meta)
```

### **Rate Limiting Best Practices**

```yaml
Throttling Strategy:
  algorithm: token_bucket
  bucket_size: tier_limit  # 1K, 10K, 100K, or unlimited
  refill_rate: tier_limit / 24  # messages per hour
  burst_limit: tier_limit / 24 / 6  # messages per 10 minutes

Example (Tier 2 - 10K/day):
  - Max per hour: 417 messages
  - Max per minute: 7 messages (sustained)
  - Burst (short): 70 messages (10-minute window)

Priority Queues:
  - Authentication: Highest priority (immediate)
  - Utility: High priority (within 1 hour)
  - Marketing: Normal priority (scheduled delivery)
```

---

## 🔐 Data Protection

### **GDPR (EU) Compliance**

If you send messages to EU residents:

```markdown
## Key Requirements
1. **Lawful Basis**: Explicit consent (opt-in) required
2. **Purpose Limitation**: Only use data for stated purpose
3. **Data Minimization**: Collect only necessary data
4. **Accuracy**: Keep data up-to-date
5. **Storage Limitation**: Delete when no longer needed
6. **Security**: Encrypt data, restrict access
7. **Accountability**: Document compliance measures

## User Rights
- Right to access (request their data)
- Right to rectification (correct inaccuracies)
- Right to erasure ("right to be forgotten")
- Right to restrict processing
- Right to data portability
- Right to object (opt-out)

## Documentation Required
- Privacy policy (clear, accessible)
- Consent records (timestamped, provable)
- Data processing agreements (with vendors)
- Data breach notification procedure
```

### **PDPA (Malaysia) Compliance**

If you send messages to Malaysian residents:

```markdown
## Key Requirements (Personal Data Protection Act 2010)
1. **General Principle**: Consent required for processing
2. **Notice & Choice**: Inform users of data use, offer opt-out
3. **Disclosure**: Only share with consent or legal requirement
4. **Security**: Protect data from unauthorized access
5. **Retention**: Keep only as long as necessary
6. **Data Integrity**: Ensure data accuracy
7. **Access**: Allow users to access/correct their data

## Enforcement
- Commissioner: Personal Data Protection Department (JPDP)
- Penalties: Fines up to RM 500,000 or imprisonment up to 3 years
- Private Right of Action: Users can sue for damages
```

### **Data Retention Guidelines**

```yaml
Opt-in Records:
  - Retention: Indefinite (or 7 years minimum)
  - Reason: Prove consent if challenged
  - Storage: Secure, access-controlled database

Message Logs:
  - Retention: 13 months (Meta default)
  - Reason: Delivery tracking, dispute resolution
  - Storage: Encrypted, anonymized after 90 days

Conversation History:
  - Retention: Per user preference or 24 months
  - Reason: Customer service continuity
  - Storage: Encrypted, user-deletable

Analytics Data:
  - Retention: 24 months (aggregated)
  - Reason: Trend analysis, optimization
  - Storage: Anonymized, no PII after 90 days
```

---

## ⚖️ Enforcement & Penalties

### **Meta Enforcement Actions**

| Violation Severity | Example | Penalty |
|--------------------|---------|---------|
| **Minor** | Template formatting issue | Warning, template rejection |
| **Moderate** | Sending without verified opt-in | Temporary suspension (7-30 days) |
| **Severe** | Prohibited content (gambling, adult) | Permanent ban, business verification revoked |
| **Critical** | Spam, harassment, illegal content | Permanent ban, legal action possible |

### **Warning Signs**

```markdown
## Early Warnings (Take Action Immediately)
- Quality rating dropped from HIGH to MEDIUM
- Delivery rate decreased by >10%
- Opt-out rate increased to >3%
- Template rejection rate >20%

## Critical Warnings (Pause Campaigns)
- Quality rating dropped to LOW
- Receiving warnings from BSP
- Multiple template rejections for same issue
- Spike in spam reports or blocks

## Account at Risk (Immediate Action Required)
- Sending tier reduced (10K → 1K)
- Temporary suspension notice
- BSP threatens termination
- Legal cease-and-desist received
```

### **Appeal Process**

If your account is suspended:

```
1. Review Suspension Notice
   - Identify specific violation
   - Gather evidence (opt-in records, templates)

2. Submit Appeal via BSP
   - Explain what happened
   - Show corrective actions taken
   - Provide evidence of compliance

3. Wait for Review (3-10 business days)
   - Do not create new accounts (policy violation)
   - Continue internal investigation

4. Outcome
   - ✅ Reinstated: Resume with caution
   - ❌ Denied: Request escalation or create new strategy
```

---

## ✅ Compliance Checklist

### **Pre-Campaign Checklist**

```markdown
## Opt-in Verification
- [ ] 100% of recipients have valid opt-in
- [ ] Opt-in records stored and accessible
- [ ] Opt-in method documented (checkbox, API, verbal, etc.)
- [ ] Consent type matches campaign (marketing vs transactional)
- [ ] Double opt-in implemented (recommended for marketing)

## Template Compliance
- [ ] Template approved by Meta (status: APPROVED)
- [ ] Category matches content (MARKETING, UTILITY, AUTH, SERVICE)
- [ ] No prohibited content (adult, gambling, illegal, etc.)
- [ ] Variables tested with sample data
- [ ] Opt-out mechanism included (for marketing)

## List Hygiene
- [ ] Suppression list applied (opted-out users excluded)
- [ ] Invalid numbers removed (hard bounces from previous campaigns)
- [ ] Segmentation applied (relevant audience only)
- [ ] Frequency cap respected (max 4 marketing messages/month)

## Technical Setup
- [ ] Phone number quality rating checked (HIGH or MEDIUM)
- [ ] Sending tier verified (1K, 10K, 100K, unlimited)
- [ ] Rate limiting configured (prevent throttling)
- [ ] Webhook endpoint tested (delivery receipts)
- [ ] Error handling implemented (retry logic, dead letter queue)

## Timing & Frequency
- [ ] Send time respects quiet hours (8 AM - 9 PM local time)
- [ ] No sends during major holidays (unless relevant)
- [ ] Frequency within user expectations (per opt-in)
- [ ] A/B test planned (if applicable)

## Documentation
- [ ] Campaign brief completed
- [ ] Legal review done (if high-risk content)
- [ ] Stakeholder approval obtained
- [ ] Escalation contact identified
- [ ] Rollback plan documented
```

### **Post-Campaign Audit**

```markdown
## Metrics Review
- [ ] Delivery rate >95%
- [ ] Read rate >60%
- [ ] Opt-out rate <2%
- [ ] Block rate <1%
- [ ] Spam reports <0.1%

## Compliance Check
- [ ] No policy violations detected
- [ ] Quality rating maintained or improved
- [ ] All opt-outs processed within 24 hours
- [ ] Suppression list updated
- [ ] Opt-in records archived

## Lessons Learned
- [ ] What worked well?
- [ ] What needs improvement?
- [ ] Any compliance issues to address?
- [ ] Recommendations for next campaign
```

---

## 📚 Additional Resources

### **Official Meta Documentation**

- **WhatsApp Business Policy:** https://www.whatsapp.com/legal/business-policy
- **Commerce Policy:** https://www.whatsapp.com/legal/commerce-policy
- **Template Guidelines:** https://developers.facebook.com/docs/whatsapp/message-templates
- **Quality Rating:** https://developers.facebook.com/docs/whatsapp/overview/quality-rating

### **Regional Regulations**

- **GDPR (EU):** https://gdpr.eu
- **PDPA (Malaysia):** https://www.pdp.gov.my
- **TCPA (USA):** https://www.fcc.gov/consumers/guides/telephone-consumer-protection-act
- **CASL (Canada):** https://fightspam.gc.ca

### **Internal Documents**

- `workflow-guide.md` - End-to-end broadcast workflow
- `templates/` - Approved template library
- `opt-in-requirements.md` - Detailed opt-in guide
- `template-guidelines.md` - Template creation best practices

---

**Last Policy Update Check:** 2026-07-02  
**Next Scheduled Review:** 2026-10-02 (quarterly)

**Document Owner:** DAF  
**Compliance Contact:** [Your compliance team contact]
