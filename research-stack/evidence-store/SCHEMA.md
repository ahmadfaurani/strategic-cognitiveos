# Evidence Store Schema

## Purpose
Standardized schema for storing raw evidence, processed findings, and output artifacts with full auditability and citation chains.

## Core Entities

### Evidence Record
```json
{
  "$schema": "https://research-stack.local/schemas/evidence-v1.json",
  "evidence_id": "uuid-v4",
  "task_id": "uuid-v4",
  "source_url": "https://...",
  "acquisition_timestamp": "2024-06-14T04:30:00Z",
  "source_type": "news|official|technical|social|academic|regulatory",
  "source_credibility": "high|medium|low",
  
  "firecrawl_extract": {
    "markdown": "...",
    "html_snapshot": "...",
    "screenshot_path": "/evidence/screenshots/uuid.png",
    "metadata": {
      "title": "...",
      "author": "...",
      "published_date": "2024-06-14",
      "word_count": 1234,
      "language": "en",
      "extraction_time_ms": 450
    }
  },
  
  "findings": [
    {
      "finding_id": "uuid-v4",
      "type": "fact|claim|statistic|quote|event",
      "content": "...",
      "confidence": "high|medium|low",
      "verified_by": ["agent_id_1", "agent_id_2"],
      "verification_method": "cross_source|official_confirmation|logical_inference",
      "related_findings": ["finding_id_2"],
      "tags": ["cve", "exploit", "vendor_a"]
    }
  ],
  
  "citations": [
    {
      "citation_id": "uuid-v4",
      "citation_text": "...",
      "location": {
        "paragraph": 3,
        "sentence": 2
      },
      "finding_refs": ["finding_id_1"]
    }
  ],
  
  "processing_history": [
    {
      "timestamp": "2024-06-14T04:30:00Z",
      "action": "acquired|analyzed|verified|summarized",
      "agent_id": "deerflow-001",
      "notes": "..."
    }
  ],
  
  "retention": {
    "retention_period_days": 365,
    "delete_after": "2025-06-14",
    "archive_status": "active|archived|deleted"
  }
}
```

### Task Record
```json
{
  "$schema": "https://research-stack.local/schemas/task-v1.json",
  "task_id": "uuid-v4",
  "mode": "cyber_threat_intel|vendor_due_diligence|competitive_intel|regulatory_monitoring",
  "status": "planning|discovery|acquisition|analysis|complete|archived",
  
  "request": {
    "pir": "Priority Intelligence Requirement text",
    "natural_language_request": "...",
    "requester": "user_id",
    "requested_at": "2024-06-14T04:00:00Z",
    "deadline": "2024-06-14T18:00:00Z",
    "priority": "critical|high|medium|low"
  },
  
  "plan": {
    "research_questions": ["...", "..."],
    "search_queries": ["...", "..."],
    "target_sources": ["...", "..."],
    "output_format": "digest|alert|report|brief",
    "confidence_threshold": 0.7
  },
  
  "evidence_refs": ["evidence_id_1", "evidence_id_2"],
  "output_refs": ["output_id_1"],
  
  "metrics": {
    "sources_discovered": 45,
    "sources_acquired": 12,
    "findings_extracted": 23,
    "high_confidence_findings": 15,
    "processing_time_seconds": 180
  },
  
  "created_at": "2024-06-14T04:00:00Z",
  "completed_at": "2024-06-14T04:30:00Z"
}
```

### Output Record
```json
{
  "$schema": "https://research-stack.local/schemas/output-v1.json",
  "output_id": "uuid-v4",
  "task_id": "uuid-v4",
  "type": "digest|alert|report|brief|matrix|tracker",
  "format": "markdown|json|pdf|html",
  
  "content": {
    "markdown": "...",
    "structured_data": {},
    "attachments": ["/outputs/uuid/chart.png"]
  },
  
  "quality": {
    "overall_confidence": "high|medium|low",
    "findings_count": 23,
    "verified_findings_count": 15,
    "citation_count": 12,
    "source_diversity_score": 0.85
  },
  
  "distribution": {
    "delivered_to": ["user_id", "channel_id"],
    "delivered_at": "2024-06-14T04:35:00Z",
    "delivery_method": "telegram|email|slack|api"
  },
  
  "created_at": "2024-06-14T04:30:00Z"
}
```

### Skill Record
```json
{
  "$schema": "https://research-stack.local/schemas/skill-v1.json",
  "skill_id": "uuid-v4",
  "name": "cyber/cve-monitoring",
  "category": "cyber_threat_intel|vendor_due_diligence|competitive_intel|regulatory_monitoring",
  "description": "...",
  
  "workflow": {
    "trigger_patterns": ["Monitor CVEs for...", "CVE tracking..."],
    "steps": [
      {
        "step_id": 1,
        "action": "generate_queries",
        "tool": "deerflow",
        "parameters": {}
      },
      {
        "step_id": 2,
        "action": "search",
        "tool": "searxng",
        "parameters": {
          "engines": ["google", "bing", "duckduckgo"]
        }
      }
    ]
  },
  
  "templates": {
    "output_template": "markdown/daily-digest.md",
    "evidence_schema": "evidence-v1"
  },
  
  "metrics": {
    "times_executed": 45,
    "avg_processing_time_seconds": 120,
    "avg_confidence_score": 0.82,
    "user_satisfaction": 4.5
  },
  
  "created_at": "2024-06-14T00:00:00Z",
  "updated_at": "2024-06-14T00:00:00Z"
}
```

## Storage Structure

```
evidence-store/
├── tasks/
│   └── {task_id}.json
├── evidence/
│   ├── {evidence_id}.json
│   └── screenshots/
│       └── {evidence_id}.png
├── outputs/
│   └── {output_id}.{md|json|pdf}
├── skills/
│   └── {skill_id}.json
└── indexes/
    ├── by_url.json
    ├── by_finding.json
    └── by_task.json
```

## Indexes

### URL Index
```json
{
  "https://example.com/article": [
    {
      "evidence_id": "uuid",
      "task_id": "uuid",
      "acquired_at": "2024-06-14T04:30:00Z"
    }
  ]
}
```

### Finding Index
```json
{
  "CVE-2024-1234": [
    {
      "finding_id": "uuid",
      "evidence_id": "uuid",
      "task_id": "uuid",
      "confidence": "high"
    }
  ]
}
```

### Task Index
```json
{
  "by_mode": {
    "cyber_threat_intel": ["task_id_1", "task_id_2"],
    "vendor_due_diligence": ["task_id_3"]
  },
  "by_status": {
    "complete": ["task_id_1"],
    "in_progress": ["task_id_2"]
  },
  "by_requester": {
    "user_123": ["task_id_1", "task_id_3"]
  }
}
```

## Retention Policy

| Evidence Type | Retention Period | Archive After | Notes |
|---------------|------------------|---------------|-------|
| Raw web content | 365 days | 90 days | Screenshots included |
| Processed findings | 730 days | 365 days | High-confidence only |
| Output reports | 730 days | 365 days | All formats |
| Skill definitions | Indefinite | N/A | Versioned |
| Task metadata | 730 days | 365 days | For analytics |

## Audit Trail

All evidence records must maintain:
1. **Acquisition timestamp** - When content was scraped
2. **Processing history** - Each transformation step
3. **Verification chain** - Which agents verified which findings
4. **Citation links** - Trace findings back to source text
5. **Access log** - Who accessed the evidence when

## Query Patterns

### Find all evidence for a task
```
GET /evidence?task_id={task_id}
```

### Find evidence by URL
```
GET /evidence?url={encoded_url}
```

### Find findings by tag
```
GET /findings?tag=cve&confidence=high
```

### Find tasks by mode and date range
```
GET /tasks?mode=cyber_threat_intel&from=2024-06-01&to=2024-06-14
```

### Find skills by category
```
GET /skills?category=vendor_due_diligence
```

## Backup & Recovery

- **Daily incremental backups** of evidence-store
- **Weekly full backups** retained for 90 days
- **Cross-region replication** for critical evidence
- **Recovery point objective (RPO):** 24 hours
- **Recovery time objective (RTO):** 4 hours
