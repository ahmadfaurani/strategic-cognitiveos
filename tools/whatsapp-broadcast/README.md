# WhatsApp Broadcast Workflow (WBS) Workspace

**Purpose:** Centralized repository for WhatsApp Business API broadcast messaging infrastructure, workflows, compliance, and provider management.

**Owner:** DAF  
**Created:** 2026-07-02  
**Last Updated:** 2026-07-02

---

## 📁 Directory Structure

```
tools/whatsapp-broadcast/
├── README.md                    # This file - workspace overview
├── docs/                        # Documentation & guides
│   ├── architecture.md          # System architecture & stack
│   ├── workflow-guide.md        # End-to-end broadcast workflow
│   ├── provider-comparison.md   # BSP comparison matrix
│   ├── api-reference.md         # API endpoints & examples
│   └── troubleshooting.md       # Common issues & solutions
│
├── config/                      # Configuration files
│   ├── providers.yaml           # BSP configurations
│   ├── templates.yaml           # Message template definitions
│   ├── rate-limits.yaml         # Throttling & throughput settings
│   └── webhooks.yaml            # Webhook endpoint configs
│
├── templates/                   # Message templates (Meta-approved)
│   ├── marketing/               # Promotional campaigns
│   ├── transactional/           # OTPs, orders, alerts
│   ├── authentication/          # Login, verification
│   └── utility/                 # Reminders, updates
│
├── scripts/                     # Automation & utility scripts
│   ├── setup.sh                 # Initial BSP onboarding
│   ├── template-submitter.sh    # Bulk template submission
│   ├── broadcast-sender.sh      # Campaign execution
│   ├── analytics-export.sh      # Metrics extraction
│   └── compliance-check.sh      # Pre-send validation
│
├── providers/                   # Provider-specific integrations
│   ├── twilio/                  # Twilio WhatsApp API
│   ├── gupshup/                 # Gupshup BSP
│   ├── 360dialog/               # 360dialog Cloud API
│   ├── messente/                # Messente omnichannel
│   ├── wati/                    # WATI platform
│   └── interakt/                # Interakt eCommerce
│
├── compliance/                  # Regulatory & policy docs
│   ├── meta-policy.md           # WhatsApp Business Policy
│   ├── opt-in-requirements.md   # Consent management
│   ├── template-guidelines.md   # Approval criteria
│   ├── gdpr-compliance.md       # Data protection (EU)
│   └── pdpa-compliance.md       # Data protection (Malaysia)
│
└── examples/                    # Sample implementations
    ├── python/                  # Python SDK examples
    ├── nodejs/                  # Node.js examples
    ├── curl/                    # cURL API examples
    └── postman/                 # Postman collections
```

---

## 🎯 Key Workflows

### 1. **Broadcast Campaign Workflow**
```
1. Audience Segmentation → 2. Template Creation → 3. Meta Approval
       ↓
4. Opt-in Verification → 5. Campaign Scheduling → 6. Message Delivery
       ↓
7. Real-time Tracking → 8. Analytics & Reporting → 9. Compliance Audit
```

### 2. **Template Approval Workflow**
```
Draft Template → Compliance Check → BSP Submission → Meta Review
       ↓
   Approved ✅ / Rejected ❌ → Revision (if needed) → Live Template
```

### 3. **Opt-in Management Workflow**
```
User Consent Collection → Double Opt-in (recommended) → Database Storage
       ↓
   Preference Center → Opt-out Handling → Suppression List Update
```

---

## 📊 Provider Comparison Summary

| Provider | Best For | Setup Time | Pricing Model | Support |
|----------|----------|------------|---------------|---------|
| **Twilio** | Enterprise, custom builds | 2-5 days | Pay-per-conversation + usage | 24/7 developer support |
| **Gupshup** | High-volume, BFSI | 1-3 days | Enterprise contract | Dedicated account manager |
| **360dialog** | Cost-sensitive, API-only | <1 day | $49/month + Meta fees | Email support |
| **Messente** | SMBs, omnichannel | 1-2 days | €0.001/msg + subscription | Account manager |
| **WATI** | Support teams, no-code | <1 day | $49/month tiered | Chat support |
| **Interakt** | D2C, eCommerce | <1 day | $49/month + Meta fees | India-focused support |

---

## 🔐 Compliance Checklist

Before any broadcast:

- [ ] **Opt-in verified** for all recipients (timestamped consent)
- [ ] **Template approved** by Meta (status: APPROVED)
- [ ] **Category match**: Template category aligns with use case
- [ ] **Rate limit check**: Within daily tier limit (1K/10K/100K/unlimited)
- [ ] **Quality rating**: Phone number quality = HIGH or MEDIUM
- [ ] **Suppression list**: Opted-out users excluded
- [ ] **Timezone compliance**: Messages sent within allowed hours (local time)
- [ ] **Content policy**: No prohibited content (adult, political, gambling, etc.)

---

## 📈 Key Metrics to Track

| Metric | Definition | Target |
|--------|------------|--------|
| **Delivery Rate** | % messages successfully delivered | >95% |
| **Read Rate** | % messages opened/read | >60% |
| **Reply Rate** | % recipients who respond | >15% |
| **Opt-out Rate** | % users who unsubscribe | <2% |
| **Block Rate** | % users who block number | <1% |
| **Quality Rating** | Meta's sender score | HIGH |
| **Cost per Conversation** | Average cost per 24h session | <€0.05 |

---

## 🚀 Quick Start

### Option A: BSP Platform (Recommended for non-developers)
```bash
# 1. Choose provider (e.g., WATI, Interakt)
# 2. Sign up and complete business verification
# 3. Connect Facebook Business Manager
# 4. Request phone number verification
# 5. Create and submit message templates
# 6. Upload contact list (with opt-in proof)
# 7. Schedule and launch campaign
```

### Option B: Direct Cloud API (Developers)
```bash
# 1. Create Meta Business Account
# 2. Set up WhatsApp Business Platform (Cloud API)
# 3. Generate access token
# 4. Register phone number
# 5. Configure webhook endpoint
# 6. Submit templates via API
# 7. Build/send via REST API or SDK
```

### Option C: CPaaS (Twilio, Gupshup)
```bash
# 1. Sign up with BSP (e.g., Twilio)
# 2. Purchase/verify phone number
# 3. Configure API credentials
# 4. Create templates in dashboard
# 5. Integrate via SDK (Node.js, Python, etc.)
# 6. Test in sandbox environment
# 7. Go live with production number
```

---

## 📚 Related Documentation

- **Architecture Deep Dive:** `docs/architecture.md`
- **API Reference:** `docs/api-reference.md`
- **Compliance Guide:** `compliance/meta-policy.md`
- **Provider Setup:** `providers/<provider-name>/README.md`
- **Template Library:** `templates/`

---

## 🛠️ Tools & Scripts

| Script | Purpose | Usage |
|--------|---------|-------|
| `scripts/setup.sh` | Initial BSP onboarding | `./setup.sh --provider twilio` |
| `scripts/template-submitter.sh` | Bulk template submission | `./template-submitter.sh templates/marketing/` |
| `scripts/broadcast-sender.sh` | Campaign execution | `./broadcast-sender.sh --template promo_june --list customers.csv` |
| `scripts/analytics-export.sh` | Metrics extraction | `./analytics-export.sh --from 2026-07-01 --to 2026-07-07` |
| `scripts/compliance-check.sh` | Pre-send validation | `./compliance-check.sh --campaign campaign_id` |

---

## ⚠️ Important Warnings

1. **No "Blasting"**: Use "broadcast" or "campaign" terminology. "Blasting" implies spam.
2. **Opt-in is mandatory**: Messaging without consent = account ban.
3. **Template approval required**: 24-48 hours typical review time.
4. **24-hour session rule**: Free-form replies only within 24h of customer message.
5. **Quality rating matters**: High block/report rates = tier downgrade or ban.

---

## 📞 Support & Resources

- **Meta Business Help:** https://business.whatsapp.com/resources
- **API Documentation:** https://developers.facebook.com/docs/whatsapp
- **Policy Guidelines:** https://www.whatsapp.com/legal/business-policy
- **Internal Contacts:** DAF (workspace owner)

---

**Next Steps:**
1. [ ] Select BSP provider based on requirements
2. [ ] Complete business verification
3. [ ] Create first message template
4. [ ] Build opt-in collection mechanism
5. [ ] Test broadcast with small segment
6. [ ] Scale to full campaign
