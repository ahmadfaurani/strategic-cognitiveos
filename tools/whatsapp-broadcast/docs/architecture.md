# WhatsApp Broadcast Architecture

**Version:** 1.0  
**Last Updated:** 2026-07-02  
**Author:** DAF

---

## 🏗️ System Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                         PRESENTATION LAYER                          │
│  ┌─────────────┐  ┌──────────────┐  ┌────────────┐  ┌────────────┐ │
│  │   Web       │  │   Mobile     │  │   Admin    │  │   Public   │ │
│  │  Dashboard  │  │    App       │  │   Portal   │  │   Widgets  │ │
│  └─────────────┘  └──────────────┘  └────────────┘  └────────────┘ │
└─────────────────────────────────────────────────────────────────────┘
                                ↓
┌─────────────────────────────────────────────────────────────────────┐
│                         APPLICATION LAYER                           │
│  ┌────────────────────────────────────────────────────────────────┐ │
│  │                    API Gateway (REST/GraphQL)                  │ │
│  │            • Authentication (OAuth 2.0 / JWT)                  │ │
│  │            • Rate Limiting (Token Bucket)                      │ │
│  │            • Request Validation & Sanitization                 │ │
│  └────────────────────────────────────────────────────────────────┘ │
│                                ↓                                     │
│  ┌─────────────┐  ┌──────────────┐  ┌────────────┐  ┌────────────┐ │
│  │  Campaign   │  │   Template   │  │  Contact   │  │ Analytics  │ │
│  │  Manager    │  │   Manager    │  │  Manager   │  │  Engine    │ │
│  └─────────────┘  └──────────────┘  └────────────┘  └────────────┘ │
│  ┌─────────────┐  ┌──────────────┐  ┌────────────┐  ┌────────────┐ │
│  │   Chatbot   │  │    Inbox     │  │   Segment  │  │   A/B      │ │
│  │   Engine    │  │   (Shared)   │  │   Engine   │  │  Testing   │ │
│  └─────────────┘  └──────────────┘  └────────────┘  └────────────┘ │
└─────────────────────────────────────────────────────────────────────┘
                                ↓
┌─────────────────────────────────────────────────────────────────────┐
│                         INTEGRATION LAYER                           │
│  ┌─────────────┐  ┌──────────────┐  ┌────────────┐  ┌────────────┐ │
│  │   CRM       │  │   eCommerce  │  │  Webhook   │  │   Event    │ │
│  │ Connectors  │  │  Integrations│  │  Manager   │  │   Bus      │ │
│  │ (Salesforce,│  │ (Shopify,    │  │            │  │ (RabbitMQ/ │ │
│  │  HubSpot)   │  │  WooCommerce)│  │            │  │  Kafka)    │ │
│  └─────────────┘  └──────────────┘  └────────────┘  └────────────┘ │
└─────────────────────────────────────────────────────────────────────┘
                                ↓
┌─────────────────────────────────────────────────────────────────────┐
│                      MESSAGING INFRASTRUCTURE                       │
│  ┌────────────────────────────────────────────────────────────────┐ │
│  │              Message Queue (Redis / RabbitMQ)                  │ │
│  │         • Priority Queues (Transactional > Marketing)          │ │
│  │         • Retry Logic (Exponential Backoff)                    │ │
│  │         • Dead Letter Queue (Failed Messages)                  │ │
│  └────────────────────────────────────────────────────────────────┘ │
│                                ↓                                     │
│  ┌────────────────────────────────────────────────────────────────┐ │
│  │              BSP Gateway Adapter Layer                         │ │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────────────┐  │ │
│  │  │  Twilio  │ │  Gupshup │ │ 360dialog│ │   Custom BSP     │  │ │
│  │  │ Adapter  │ │ Adapter  │ │ Adapter  │ │    Adapter       │  │ │
│  │  └──────────┘ └──────────┘ └──────────┘ └──────────────────┘  │ │
│  └────────────────────────────────────────────────────────────────┘ │
│                                ↓                                     │
│  ┌────────────────────────────────────────────────────────────────┐ │
│  │           WhatsApp Business API (Meta Cloud API)               │ │
│  │         • Template Messages (Outbound Broadcast)               │ │
│  │         • Session Messages (24-hour Customer Service)          │ │
│  │         • Media Messages (Images, Videos, PDFs)                │ │
│  │         • Interactive Messages (Buttons, Lists)                │ │
│  └────────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────┘
                                ↓
┌─────────────────────────────────────────────────────────────────────┐
│                         DATA LAYER                                  │
│  ┌─────────────┐  ┌──────────────┐  ┌────────────┐  ┌────────────┐ │
│  │ PostgreSQL  │  │   MongoDB    │  │   Redis    │  │   S3 /     │ │
│  │ (Structured │  │ (Documents,  │  │  (Cache,   │  │   GCS      │ │
│  │  Data:      │  │  Conversations,│  │  Sessions, │  │ (Media     │ │
│  │  Users,     │  │  Logs)       │  │  Queues)   │  │  Storage)  │ │
│  │  Campaigns) │  │              │  │            │  │            │ │
│  └─────────────┘  └──────────────┘  └────────────┘  └────────────┘ │
└─────────────────────────────────────────────────────────────────────┘
                                ↓
┌─────────────────────────────────────────────────────────────────────┐
│                      COMPLIANCE & SECURITY                          │
│  ┌─────────────┐  ┌──────────────┐  ┌────────────┐  ┌────────────┐ │
│  │  Opt-in     │  │   Template   │  │   Audit    │  │   Data     │ │
│  │  Manager    │  │   Approval   │  │   Logger   │  │  Encryption│ │
│  │             │  │   Workflow   │  │            │  │            │ │
│  └─────────────┘  └──────────────┘  └────────────┘  └────────────┘ │
│  ┌─────────────┐  ┌──────────────┐  ┌────────────┐  ┌────────────┐ │
│  │  Rate       │  │   Quality    │  │   GDPR/    │  │   Access   │ │
│  │  Limiter    │  │   Monitor    │  │   PDPA     │  │   Control  │ │
│  │             │  │              │  │  Compliance│  │            │ │
│  └─────────────┘  └──────────────┘  └────────────┘  └────────────┘ │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 🔧 Technology Stack

### **Backend Services**

| Component | Technology | Purpose |
|-----------|------------|---------|
| **API Server** | Node.js (Express/Fastify) or Python (FastAPI) | REST/GraphQL API endpoints |
| **Message Queue** | Redis Streams / RabbitMQ / Apache Kafka | Asynchronous message processing |
| **Database (Primary)** | PostgreSQL 15+ | User data, campaigns, templates |
| **Database (Documents)** | MongoDB 6+ | Conversation logs, event history |
| **Cache** | Redis 7+ | Session management, rate limiting |
| **Search** | Elasticsearch 8+ | Message search, analytics queries |
| **Media Storage** | AWS S3 / Google Cloud Storage | Template media assets |

### **Frontend**

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Dashboard** | React 18+ / Vue.js 3+ | Admin interface |
| **State Management** | Redux Toolkit / Pinia | Application state |
| **Real-time Updates** | WebSocket (Socket.io) | Live message status |
| **Charts** | Recharts / Chart.js | Analytics visualization |
| **UI Framework** | Tailwind CSS / Material UI | Styling |

### **Infrastructure**

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Containerization** | Docker + Docker Compose | Local development |
| **Orchestration** | Kubernetes (K8s) | Production deployment |
| **CI/CD** | GitHub Actions / GitLab CI | Automated testing & deployment |
| **Monitoring** | Prometheus + Grafana | Metrics & alerting |
| **Logging** | ELK Stack (Elasticsearch, Logstash, Kibana) | Log aggregation |
| **APM** | New Relic / Datadog | Application performance monitoring |

### **Security**

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Authentication** | OAuth 2.0 + JWT | User authentication |
| **Encryption (Transit)** | TLS 1.3 | API communication |
| **Encryption (Storage)** | AES-256 | Database encryption |
| **Secrets Management** | HashiCorp Vault / AWS Secrets Manager | API keys, credentials |
| **WAF** | Cloudflare / AWS WAF | DDoS protection |

---

## 📡 Message Flow Architecture

### **Outbound Broadcast Flow**

```
1. Campaign Creation
       ↓
   [Dashboard] → API Gateway → Campaign Manager
       ↓
2. Audience Segmentation
       ↓
   Contact Manager → Database Query → Filtered Recipient List
       ↓
3. Template Selection
       ↓
   Template Manager → Verify Approval Status (Meta API)
       ↓
4. Pre-Send Validation
       ↓
   Compliance Check → Opt-in Verification → Suppression List
       ↓
5. Message Queueing
       ↓
   Message Queue (Redis/RabbitMQ) → Priority Assignment
       ↓
6. Rate-Limited Dispatch
       ↓
   Rate Limiter → BSP Adapter → WhatsApp Business API
       ↓
7. Delivery Tracking
       ↓
   Webhook Receiver → Status Update (SENT → DELIVERED → READ)
       ↓
8. Analytics Update
       ↓
   Analytics Engine → Database → Dashboard (Real-time)
```

### **Inbound Message Flow**

```
1. Customer Reply
       ↓
   WhatsApp Business API → Webhook → Inbound Handler
       ↓
2. Session Validation
       ↓
   Check 24-hour Window → Session Message (Free-form allowed)
       ↓
3. Routing Decision
       ↓
   ┌─────────────────┬─────────────────┬──────────────────┐
   │   Chatbot       │    Human        │    Auto-Reply    │
   │   (NLP/ML)      │    Agent        │    (Template)    │
   └─────────────────┴─────────────────┴──────────────────┘
       ↓
4. Response Generation
       ↓
   Response Queue → BSP Adapter → WhatsApp API → Customer
       ↓
5. Conversation Logging
       ↓
   MongoDB (Conversation History) → Analytics Engine
```

---

## 🏢 BSP Integration Patterns

### **Adapter Pattern for Multi-BSP Support**

```typescript
// Abstract BSP Adapter Interface
interface BSPAdapter {
  sendTemplate(message: TemplateMessage): Promise<SendResult>;
  sendSession(message: SessionMessage): Promise<SendResult>;
  getTemplateStatus(templateId: string): Promise<TemplateStatus>;
  submitTemplate(template: Template): Promise<SubmissionResult>;
  getDeliveryStatus(messageId: string): Promise<DeliveryStatus>;
}

// Concrete Implementations
class TwilioAdapter implements BSPAdapter { /* ... */ }
class GupshupAdapter implements BSPAdapter { /* ... */ }
class ThreeSixtyDialogAdapter implements BSPAdapter { /* ... */ }
class MessenteAdapter implements BSPAdapter { /* ... */ }

// Factory Pattern for Runtime Selection
class BSPFactory {
  static getAdapter(provider: string): BSPAdapter {
    switch(provider) {
      case 'twilio': return new TwilioAdapter();
      case 'gupshup': return new GupshupAdapter();
      case '360dialog': return new ThreeSixtyDialogAdapter();
      case 'messente': return new MessenteAdapter();
      default: throw new Error('Unknown provider');
    }
  }
}
```

### **Configuration-Driven Provider Switching**

```yaml
# config/providers.yaml
providers:
  primary: twilio
  fallback: gupshup
  
  twilio:
    enabled: true
    account_sid: "${TWILIO_ACCOUNT_SID}"
    auth_token: "${TWILIO_AUTH_TOKEN}"
    whatsapp_number: "+1234567890"
    rate_limit: 1000  # messages/minute
    retry_attempts: 3
    
  gupshup:
    enabled: true
    api_key: "${GUPSHUP_API_KEY}"
    whatsapp_number: "+9876543210"
    rate_limit: 2000
    retry_attempts: 2
    
  three_sixty_dialog:
    enabled: false
    api_key: "${DIALOG_API_KEY}"
    whatsapp_number: "+1122334455"
    rate_limit: 500
```

---

## 📊 Database Schema (Simplified)

### **Core Tables**

```sql
-- Campaigns
CREATE TABLE campaigns (
  id UUID PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  template_id UUID REFERENCES templates(id),
  status VARCHAR(50) DEFAULT 'draft', -- draft, scheduled, active, completed, paused
  scheduled_at TIMESTAMP,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

-- Templates
CREATE TABLE templates (
  id UUID PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  category VARCHAR(50), -- MARKETING, UTILITY, AUTHENTICATION
  language VARCHAR(10) DEFAULT 'en',
  meta_template_id VARCHAR(255), -- Meta's template ID
  meta_status VARCHAR(50), -- APPROVED, REJECTED, PENDING
  content JSONB NOT NULL, -- Template body, variables, buttons
  created_at TIMESTAMP DEFAULT NOW()
);

-- Contacts
CREATE TABLE contacts (
  id UUID PRIMARY KEY,
  phone_number VARCHAR(20) UNIQUE NOT NULL,
  name VARCHAR(255),
  opt_in_status BOOLEAN DEFAULT FALSE,
  opt_in_timestamp TIMESTAMP,
  opt_in_source VARCHAR(100), -- web_form, api, manual, etc.
  suppression_status BOOLEAN DEFAULT FALSE,
  created_at TIMESTAMP DEFAULT NOW()
);

-- Campaign Recipients
CREATE TABLE campaign_recipients (
  id UUID PRIMARY KEY,
  campaign_id UUID REFERENCES campaigns(id),
  contact_id UUID REFERENCES contacts(id),
  message_id VARCHAR(255), -- BSP message ID
  status VARCHAR(50), -- queued, sent, delivered, read, failed
  sent_at TIMESTAMP,
  delivered_at TIMESTAMP,
  read_at TIMESTAMP,
  error_message TEXT
);

-- Opt-in Records
CREATE TABLE opt_in_records (
  id UUID PRIMARY KEY,
  contact_id UUID REFERENCES contacts(id),
  campaign_id UUID REFERENCES campaigns(id),
  consent_type VARCHAR(50), -- marketing, transactional, both
  consent_method VARCHAR(100), -- checkbox, api_import, verbal, etc.
  consent_timestamp TIMESTAMP NOT NULL,
  ip_address INET,
  user_agent TEXT,
  proof_url TEXT -- URL to consent form/screenshot
);
```

---

## 🔐 Security Architecture

### **Data Protection**

```
┌─────────────────────────────────────────────────────────┐
│                    Data Classification                   │
├─────────────────────────────────────────────────────────┤
│  PII (Personal Identifiable Information)                │
│  • Phone numbers (encrypted at rest)                    │
│  • Names, email addresses                               │
│  • Opt-in timestamps & IP addresses                     │
├─────────────────────────────────────────────────────────┤
│  Business Critical                                      │
│  • API credentials (stored in Vault/Secrets Manager)    │
│  • Template content (pre-approval)                      │
│  • Campaign analytics (business intelligence)           │
├─────────────────────────────────────────────────────────┤
│  Compliance Data                                        │
│  • Audit logs (immutable, 7-year retention)             │
│  • Consent records (GDPR/PDPA requirement)              │
│  • Opt-out/suppression lists                            │
└─────────────────────────────────────────────────────────┘
```

### **Access Control Matrix**

| Role | Campaigns | Templates | Contacts | Analytics | Billing |
|------|-----------|-----------|----------|-----------|---------|
| **Admin** | CRUD | CRUD | CRUD | Read | Read/Write |
| **Campaign Manager** | CRUD | Read/Write | Read | Read | No Access |
| **Agent** | Read | Read | Read (own chats) | No Access | No Access |
| **Analyst** | Read | Read | Aggregated Only | Read | No Access |
| **Billing** | No Access | No Access | No Access | Aggregated | Read/Write |

---

## 📈 Scalability Considerations

### **Horizontal Scaling Strategy**

```
┌──────────────────────────────────────────────────────────┐
│              Load Balancer (Nginx/HAProxy)               │
└──────────────────────────────────────────────────────────┘
              ↓              ↓              ↓
    ┌─────────────┐ ┌─────────────┐ ┌─────────────┐
    │  API Server │ │  API Server │ │  API Server │
    │   (Node 1)  │ │   (Node 2)  │ │   (Node N)  │
    └─────────────┘ └─────────────┘ └─────────────┘
              ↓              ↓              ↓
    ┌─────────────────────────────────────────────────┐
    │           Message Queue (Redis Cluster)          │
    └─────────────────────────────────────────────────┘
              ↓              ↓              ↓
    ┌─────────────┐ ┌─────────────┐ ┌─────────────┐
    │   Worker    │ │   Worker    │ │   Worker    │
    │   (Send)    │ │   (Send)    │ │   (Send)    │
    └─────────────┘ └─────────────┘ └─────────────┘
              ↓              ↓              ↓
    ┌─────────────────────────────────────────────────┐
    │         BSP Adapters (Connection Pooling)        │
    └─────────────────────────────────────────────────┘
```

### **Throughput Optimization**

| Technique | Implementation | Impact |
|-----------|----------------|--------|
| **Connection Pooling** | Reuse BSP HTTP connections | Reduces latency by 40-60% |
| **Batch Sending** | Group messages (100-500/batch) | API call reduction |
| **Priority Queues** | Transactional > Marketing | Critical messages first |
| **Rate Limiting** | Token bucket per BSP | Prevents throttling |
| **Caching** | Template/content cache (Redis) | Reduces DB load |
| **Async Processing** | Non-blocking I/O | Higher concurrency |

---

## 🚨 Monitoring & Alerting

### **Key Metrics**

```yaml
# Infrastructure Metrics
- api_response_time_p95: < 200ms
- api_error_rate: < 0.1%
- queue_depth: < 10,000 messages
- worker_utilization: 60-80%
- database_connections: < 80% of pool

# Business Metrics
- message_delivery_rate: > 95%
- message_read_rate: > 60%
- opt_out_rate: < 2%
- quality_rating: HIGH (Meta)
- template_rejection_rate: < 10%

# Compliance Metrics
- opt_in_verification_rate: 100%
- suppression_list_hit_rate: Track trends
- template_approval_time: < 48 hours
```

### **Alert Thresholds**

| Metric | Warning | Critical | Action |
|--------|---------|----------|--------|
| Delivery Rate | < 90% | < 80% | Investigate BSP issues |
| API Error Rate | > 1% | > 5% | Check logs, rollback if needed |
| Queue Depth | > 50K | > 100K | Scale workers |
| Quality Rating | MEDIUM | LOW | Pause campaigns, review content |
| Opt-out Rate | > 3% | > 5% | Review targeting & frequency |

---

## 📝 Next Steps

1. **Select BSP Provider** → See `docs/provider-comparison.md`
2. **Design Database Schema** → Adapt to specific needs
3. **Build MVP** → Start with single BSP (Twilio/360dialog)
4. **Implement Compliance** → Opt-in management, audit logging
5. **Test & Iterate** → Load testing, template approval workflow
6. **Scale** → Multi-BSP support, advanced analytics

---

**Related Documents:**
- `workflow-guide.md` - End-to-end broadcast process
- `provider-comparison.md` - BSP evaluation matrix
- `api-reference.md` - API endpoint documentation
- `../compliance/meta-policy.md` - WhatsApp Business Policy
