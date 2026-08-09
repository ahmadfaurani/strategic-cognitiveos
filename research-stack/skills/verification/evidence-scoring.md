# Evidence Scoring Framework

## Purpose
Standardized methodology for assessing confidence in research findings based on source quality, corroboration, and verification status.

---

## Confidence Score Components

Confidence is calculated from four weighted factors:

| Factor | Weight | Description |
|--------|--------|-------------|
| **Source Authority** | 30% | How authoritative is the source? |
| **Corroboration** | 30% | How many independent sources confirm? |
| **Recency** | 20% | How current is the information? |
| **Completeness** | 20% | How complete is the evidence? |

---

## Source Authority Scoring (30%)

| Score | Source Type | Examples |
|-------|-------------|----------|
| **1.0** | Primary/Official | NVD, CISA, vendor PSIRT, regulatory bodies, official gazettes |
| **0.8** | Reputable Secondary | Major security blogs, analyst firms, established news |
| **0.6** | Technical Sources | GitHub, Stack Overflow, technical documentation |
| **0.4** | Community Sources | Reddit, forums, social media (verified accounts) |
| **0.2** | Unverified Sources | Anonymous posts, unverified claims, rumors |

**Authority Assessment Questions:**
- Is this the original source or a repost?
- Does the source have subject matter expertise?
- Is the source known for accuracy in this domain?
- Is there editorial oversight or peer review?

---

## Corroboration Scoring (30%)

| Score | Corroboration Level | Criteria |
|-------|---------------------|----------|
| **1.0** | Strong | ≥3 independent sources, including ≥1 official |
| **0.8** | Moderate | 2 independent sources, including ≥1 official |
| **0.6** | Limited | 2 independent sources, no official |
| **0.4** | Weak | Single official source only |
| **0.2** | Unconfirmed | Single non-official source |

**Corroboration Rules:**
- **Independent** = Different organizations/publishers
- **Official** = Government, regulator, vendor, standards body
- **Not independent** = Reposts, syndicated content, same parent company

---

## Recency Scoring (20%)

| Domain | Timeframe | Score |
|--------|-----------|-------|
| **Cyber Threat Intel** | <24 hours | 1.0 |
| | <7 days | 0.8 |
| | <30 days | 0.6 |
| | <90 days | 0.4 |
| | >90 days | 0.2 (stale) |
| **Vendor Due Diligence** | <30 days | 1.0 |
| | <90 days | 0.8 |
| | <6 months | 0.6 |
| | <12 months | 0.4 |
| | >12 months | 0.2 (stale) |
| **Competitive Intel** | <30 days | 1.0 |
| | <90 days | 0.8 |
| | <6 months | 0.6 |
| | <12 months | 0.4 |
| | >12 months | 0.2 (stale) |
| **Regulatory** | <7 days | 1.0 |
| | <30 days | 0.8 |
| | <90 days | 0.6 |
| | <6 months | 0.4 |
| | >6 months | 0.2 (check for updates) |
| **Account Intel** | <30 days | 1.0 |
| | <90 days | 0.8 |
| | <6 months | 0.6 |
| | <12 months | 0.4 |
| | >12 months | 0.2 (verify current) |

**Stale Source Flag:**
- Any source beyond the "stale" threshold must be flagged
- Stale sources can be used for context but not for current-state claims
- Attempt to find updated sources before finalizing

---

## Completeness Scoring (20%)

| Score | Completeness Level | Criteria |
|-------|-------------------|----------|
| **1.0** | Complete | All key fields present, full content accessible |
| **0.8** | Mostly Complete | Most fields present, minor gaps |
| **0.6** | Partial | Key fields present but some gaps |
| **0.4** | Limited | Only basic information available |
| **0.2** | Fragmentary | Snippet only, full content unavailable |

**Completeness Checklist:**
- [ ] Full article/content accessible (not just snippet)
- [ ] Publication date present
- [ ] Author/attribution present
- [ ] Key claims supported with evidence
- [ ] No obvious truncation or paywall blocking

---

## Confidence Score Calculation

```
Confidence Score = (Authority × 0.30) + (Corroboration × 0.30) + (Recency × 0.20) + (Completeness × 0.20)
```

**Confidence Levels:**

| Score Range | Level | Usage |
|-------------|-------|-------|
| **0.80 - 1.00** | High | Use for critical decisions, escalation if high-impact |
| **0.60 - 0.79** | Medium | Use with caveats, note limitations |
| **0.40 - 0.59** | Low | Use for context only, flag for verification |
| **< 0.40** | Very Low | Do not use for findings, informational only |

---

## Verification Status

| Status | Definition | Action |
|--------|------------|--------|
| **Verified** | Confirmed by ≥2 sources including official | Use in findings |
| **Pending** | Single source or awaiting confirmation | Flag for follow-up |
| **Contradicted** | Conflicting information across sources | Escalate for review |
| **Unverifiable** | No way to confirm (anonymous, no evidence) | Do not use as finding |

---

## Special Handling Rules

### High-Impact Findings
**Definition:** Findings that could result in:
- Security incidents if acted upon incorrectly
- Financial/reputational damage
- Regulatory non-compliance
- Strategic missteps

**Requirements:**
- Minimum confidence score: 0.70
- Must have official source confirmation
- Must be verified (not pending)
- Requires human review before action

### Contradiction Handling

When sources contradict:

1. **Assess source authority** - Which source is more authoritative?
2. **Check recency** - Is one source more current?
3. **Look for resolution** - Is there a third source that resolves the contradiction?
4. **Flag explicitly** - Mark the contradiction in findings
5. **Escalate** - Send for human review if high-impact

**Contradiction Documentation:**
```yaml
contradiction:
  claim: "[What is disputed]"
  source_a:
    url: "..."
    claim: "[Version A]"
    authority: 0.8
  source_b:
    url: "..."
    claim: "[Version B]"
    authority: 0.6
  assessment: "[Which is more credible and why]"
  resolution: "[If resolved, how]"
  escalation: true/false
```

### Stale Source Handling

When sources are stale (>threshold age):

1. **Flag as stale** - Mark in metadata
2. **Search for updates** - Attempt to find current information
3. **Use with caveats** - If no update found, use for context only
4. **Note in findings** - Explicitly state information age

**Stale Source Documentation:**
```yaml
stale_source:
  url: "..."
  original_date: "2023-01-15"
  retrieval_date: "2024-06-14"
  age_days: 516
  update_search_attempted: true
  update_found: false
  usage: "context_only"
```

---

## Fact vs. Inference vs. Recommendation

**Critical distinction in all findings:**

| Type | Definition | Label |
|------|------------|-------|
| **Fact** | Directly stated in source, verifiable | `[FACT]` |
| **Inference** | Derived from facts, logical conclusion | `[INFERENCE]` |
| **Recommendation** | Suggested action based on analysis | `[RECOMMENDATION]` |

**Examples:**

❌ Wrong: "The vendor has a weak security posture"

✅ Right: 
- `[FACT]` "The vendor's security page lists no certifications"
- `[INFERENCE]` "This suggests limited security program maturity"
- `[RECOMMENDATION]` "Request security questionnaire before proceeding"

---

## Evidence Chain Requirements

Every finding must maintain:

1. **Source URL** - Exact URL where evidence was found
2. **Supporting Excerpt** - Direct quote from source
3. **Relevance Statement** - Why this evidence supports the finding
4. **Timestamps** - Publication date AND retrieval date
5. **Confidence Score** - Calculated per this framework
6. **Verification Status** - Verified/pending/contradicted

**Evidence Chain Template:**
```yaml
evidence_chain:
  - source_url: "https://..."
    supporting_excerpt: "[Direct quote]"
    relevance: "[Why this supports the finding]"
    publication_date: "2024-06-13"
    retrieval_date: "2024-06-14"
    authority_score: 0.8
  - source_url: "https://..."
    supporting_excerpt: "[Direct quote]"
    relevance: "[Why this supports the finding]"
    publication_date: "2024-06-13"
    retrieval_date: "2024-06-14"
    authority_score: 0.6
    
confidence_score: 0.82
confidence_level: "high"
verification_status: "verified"
```

---

## Human Review Triggers

**Automatically escalate to human review when:**

| Trigger | Reason |
|---------|--------|
| Confidence < 0.70 on high-impact finding | Insufficient certainty for critical decision |
| Contradiction across sources | Requires judgment to resolve |
| Official source contradicts secondary | Authority assessment needed |
| Stale source is only evidence | Currency verification needed |
| Finding implies security vulnerability | Accuracy critical |
| Finding implies regulatory requirement | Compliance risk |
| Finding implies financial impact | Business risk |
| Personal data involved | Privacy review needed |

---

## Quality Assurance Checks

Before finalizing findings:

- [ ] Confidence score calculated correctly
- [ ] All evidence has supporting excerpts
- [ ] Publication and retrieval dates recorded
- [ ] Source authority assessed accurately
- [ ] Corroboration count is correct (independent sources)
- [ ] Recency threshold appropriate for domain
- [ ] Fact/inference/recommendation clearly distinguished
- [ ] Contradictions flagged
- [ ] Stale sources identified
- [ ] Human review triggered where required

---

## Skill Maintenance

**Update this skill when:**
- New source types emerge
- Domain-specific thresholds need adjustment
- Scoring formula is refined
- New verification methods are adopted

**Review frequency:** Quarterly
