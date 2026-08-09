# WhatsApp Broadcast - Quick Start Guide

**Get your first campaign running in 30 minutes**

---

## 🚀 Option 1: Use a BSP Platform (Recommended for First-Time Users)

**Best for:** Non-developers, marketing teams, quick setup

### **Step 1: Choose a Provider (5 minutes)**

| Provider | Best For | Setup Time | Starting Price |
|----------|----------|------------|----------------|
| **WATI** | Support teams, no-code | <15 min | $49/month |
| **Interakt** | eCommerce, D2C | <15 min | $49/month |
| **AiSensy** | Marketing automation | <20 min | Custom |
| **Messente** | Global + SMS fallback | <20 min | Pay-per-use |

**Recommendation for Malaysia:** Start with **Interakt** or **AiSensy** (India/Malaysia focus, good support)

---

### **Step 2: Sign Up & Verify Business (15 minutes)**

1. **Go to provider website** (e.g., https://www.interakt.app)
2. **Click "Get Started" / "Sign Up"**
3. **Enter business details:**
   - Business name (as registered)
   - Business registration number
   - Website URL
   - Business category
4. **Upload documents:**
   - Business registration certificate
   - Website with privacy policy
   - Logo (square, minimum 192x192px)
5. **Wait for verification** (typically 1-2 hours, max 48 hours)

---

### **Step 3: Connect Facebook Business Manager (5 minutes)**

1. **Create Facebook Business Manager** (if you don't have one):
   - Go to https://business.facebook.com
   - Click "Create Account"
   - Follow prompts

2. **Connect to BSP:**
   - In BSP dashboard, click "Connect Facebook"
   - Log in to Facebook
   - Grant permissions to your Business Manager

3. **Create WhatsApp Business Account (WABA):**
   - BSP will create WABA automatically
   - Or select existing WABA if you have one

---

### **Step 4: Add & Verify Phone Number (5 minutes)**

1. **Choose phone number:**
   - New number (recommended for dedicated broadcast)
   - Existing business number (will lose personal WhatsApp)

2. **Verify number:**
   - Enter phone number in BSP dashboard
   - Receive 6-digit code via SMS or call
   - Enter code to verify

3. **Set up business profile:**
   - Business name
   - Business hours
   - Address
   - Email
   - Website
   - Logo
   - Description

---

### **Step 5: Create First Template (10 minutes)**

**Example: Welcome Message**

1. **Go to Templates → Create Template**
2. **Fill in details:**
   ```
   Template Name: welcome_message
   Category: UTILITY
   Language: English
   
   Header: Welcome to [Your Business]!
   Body: Hi {{1}}! Thanks for joining us on WhatsApp. 
         We'll send you order updates and exclusive offers here.
         Reply HELP for assistance or STOP to unsubscribe.
   
   Buttons: 
   - Quick Reply: "View Products"
   - Quick Reply: "Contact Support"
   ```
3. **Submit for approval** (24-48 hours typical)

**Pro tip:** Create 2-3 templates while waiting:
- Welcome message (UTILITY)
- Order confirmation (UTILITY)
- Promotional offer (MARKETING)

---

### **Step 6: Upload Contacts (5 minutes)**

**CSV Format:**
```csv
phone_number,name,email,opt_in_date
+60123456789,Ahmad Ali,ahmad@example.com,2026-07-01
+60198765432,Siti Nurhaliza,siti@example.com,2026-07-01
+60177654321,Tan Ah Kow,tank@example.com,2026-07-01
```

**Important:**
- Phone numbers must include country code (+60 for Malaysia)
- **Only upload contacts with valid opt-in**
- Include opt-in date for compliance

---

### **Step 7: Send First Campaign (5 minutes)**

1. **Go to Broadcasts → Create Campaign**
2. **Select template** (e.g., welcome_message)
3. **Choose audience** (all contacts or segment)
4. **Personalize variables** (e.g., {{1}} = customer name)
5. **Preview message** on your own number
6. **Schedule or send immediately**

---

## 🛠️ Option 2: Direct API Integration (Developers)

**Best for:** Custom workflows, existing tech stack, high volume

### **Step 1: Set Up Meta Developer Account (10 minutes)**

1. Go to https://developers.facebook.com
2. Create developer account
3. Create new app → Business type
4. Add WhatsApp product to app

### **Step 2: Configure Cloud API (10 minutes)**

```bash
# Install Meta CLI (optional)
npm install -g @whatsapp-business/cloud-api-sdk

# Or use REST API directly
# Get access token from Meta Developer Dashboard
export WHATSAPP_TOKEN="EAAG..."
export PHONE_NUMBER_ID="123456789"
export BUSINESS_ACCOUNT_ID="987654321"
```

### **Step 3: Test with Sandbox (5 minutes)**

```bash
# Send test message
curl -X POST "https://graph.facebook.com/v17.0/${PHONE_NUMBER_ID}/messages" \
  -H "Authorization: Bearer ${WHATSAPP_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{
    "messaging_product": "whatsapp",
    "to": "+60123456789",
    "type": "template",
    "template": {
      "name": "hello_world",
      "language": { "code": "en" }
    }
  }'
```

### **Step 4: Build Integration (Variable)**

**Use our provided scripts:**
```bash
cd tools/whatsapp-broadcast/

# Configure provider
cp config/providers.yaml.example config/providers.yaml
# Edit with your credentials

# Send first broadcast
./scripts/broadcast-sender.sh \
  --template welcome_message \
  --list contacts.csv \
  --dry-run  # Test without sending
```

**Or use SDKs:**
- **Node.js:** `npm install whatsapp-cloud-api`
- **Python:** `pip install whatsapp-business-python`
- **PHP:** `composer require whatsapp-business/php`

---

## ✅ Pre-Launch Checklist

Before sending your first campaign:

```markdown
## Compliance
- [ ] All contacts have valid opt-in (documented)
- [ ] Privacy policy published on website
- [ ] Template approved by Meta (status: APPROVED)
- [ ] Opt-out mechanism included (STOP keyword)

## Technical
- [ ] Phone number verified
- [ ] Business profile complete
- [ ] Webhook configured (for delivery receipts)
- [ ] Test message sent successfully

## Content
- [ ] Template content reviewed (no policy violations)
- [ ] Personalization variables tested
- [ ] Message preview looks good on mobile
- [ ] Links tested and working

## Operations
- [ ] Team trained on WhatsApp Best Practices
- [ ] Response time SLA defined (<24 hours for customer messages)
- [ ] Escalation process documented
- [ ] Analytics dashboard set up
```

---

## 📊 Expected Timeline

| Phase | Duration | Milestone |
|-------|----------|-----------|
| **Provider Selection** | 1 day | Contract signed |
| **Business Verification** | 1-2 days | Account approved |
| **Phone Number Setup** | 1 day | Number verified |
| **Template Creation** | 1 day | Templates submitted |
| **Template Approval** | 1-3 days | First template approved |
| **Contact Upload** | 1 day | List imported |
| **Test Campaign** | 1 day | Internal test sent |
| **First Live Campaign** | Day 7-10 | First broadcast to customers |

**Total: 7-10 days from start to first live campaign**

---

## 💰 Cost Breakdown (Example: 10,000 Messages/Month)

### **Malaysia Rates (2026)**

```
Meta Conversation Fees (Marketing Category):
- 10,000 messages × €0.0072 = €72.00 (~RM 340)

BSP Service Fees:
- Interakt Starter: $49/month (~RM 230)
- OR
- Messente: 10,000 × €0.001 = €10 (~RM 47)

Total Monthly Cost:
- Interakt: RM 340 + RM 230 = RM 570
- Messente: RM 340 + RM 47 = RM 387

Cost per Message:
- RM 0.057 (Interakt)
- RM 0.039 (Messente)
```

**Note:** First 1,000 **service** conversations per month are **FREE** (marketing messages not included)

---

## 🆘 Common Issues & Solutions

### **Issue 1: Template Rejected**

**Reason:** Marketing content in utility template

**Solution:**
- Separate marketing and utility templates
- Remove promotional language from utility templates
- Resubmit with correct category

---

### **Issue 2: Phone Number Banned**

**Reason:** Sending without opt-in or spam reports

**Solution:**
- Pause all campaigns immediately
- Review opt-in records for all contacts
- Remove contacts without proof of consent
- Appeal to Meta via BSP (if wrongful ban)
- Start fresh with new number (if appeal denied)

---

### **Issue 3: Low Delivery Rate (<80%)**

**Reason:** Invalid numbers or blocked by recipients

**Solution:**
- Clean contact list (remove invalid formats)
- Implement double opt-in
- Reduce send frequency
- Improve content relevance

---

### **Issue 4: High Opt-out Rate (>5%)**

**Reason:** Too frequent or irrelevant messages

**Solution:**
- Survey customers for preferences
- Segment by engagement level
- Reduce frequency for low-engagement segment
- A/B test content and timing

---

## 📚 Next Steps

After completing setup:

1. **Read Full Documentation:**
   - `docs/architecture.md` - System design
   - `docs/workflow-guide.md` - End-to-end workflow
   - `compliance/meta-policy.md` - Policy compliance

2. **Set Up Analytics:**
   - Track delivery rate, read rate, CTR
   - Set up alerts for quality rating drops
   - Weekly performance review

3. **Optimize Campaigns:**
   - A/B test templates
   - Segment audience by behavior
   - Personalize content

4. **Scale Gradually:**
   - Start with 100-500 recipients
   - Monitor quality metrics
   - Increase volume as quality rating improves

---

## 📞 Support Resources

### **Provider Support**

- **Interakt:** support@interakt.app | +91-80-4718-5888
- **WATI:** support@wati.io | Live chat in dashboard
- **Messente:** support@messente.com | +372-6-340-100
- **Twilio:** support@twilio.com | https://support.twilio.com

### **Meta Support**

- **Business Help Center:** https://business.whatsapp.com/resources
- **Developer Docs:** https://developers.facebook.com/docs/whatsapp
- **Policy Questions:** https://www.facebook.com/business/help/whatsapp

### **Internal Contacts**

- **Workspace Owner:** DAF
- **Compliance Team:** [Your contact]
- **Technical Lead:** [Your contact]

---

## 🎯 Success Metrics (First 30 Days)

| Metric | Target | Status |
|--------|--------|--------|
| Templates Approved | 3+ | ⬜ |
| First Campaign Sent | Day 10 | ⬜ |
| Delivery Rate | >95% | ⬜ |
| Read Rate | >60% | ⬜ |
| Opt-out Rate | <2% | ⬜ |
| Quality Rating | HIGH | ⬜ |

---

**Ready to start?** Pick your provider and begin with Step 1!

**Questions?** Reply to this message or check the full documentation in `docs/` and `compliance/` folders.
