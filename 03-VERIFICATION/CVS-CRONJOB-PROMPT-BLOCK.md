# CVS Cronjob Integration — AI Self-Scoring Prompt Block

**Classification:** TLP:AMBER  
**Created:** 2026-08-04  
**Purpose:** Standard prompt block to append to ALL LLM-driven cronjob prompts for CVS compliance

---

## How to Use

Append the following block to the end of every LLM-driven cronjob prompt. This instructs the AI to self-score its output using the full 5-criteria CVS rubric.

---

## Standard CVS Prompt Block (copy below this line)

```
---CVS INSTRUCTIONS---
You must apply the Core Validation System (CVS) to every factual claim in your output. For each claim, provide a CVS validation block.

CVS TIER CLASSIFICATION:
- T1 (Verified Fact): Confirmed by authoritative/source-traceable evidence. Multiple independent sources agree OR official source.
- T2 (Partially Verified): Supported by some evidence but missing full confirmation. Single credible source.
- T3 (Analytical Interpretation): Derived from facts through analysis, calculation, or expert judgment. NOT a raw fact.
- T4 (Assumption/Projection): Based on expectation, forecast, scenario, or incomplete data.
- T5 (Disputed/Conflicting): Sources disagree or evidence is inconsistent.
- T6 (Rejected): Unsupported, contradicted, outdated, or unreliable.

SOURCE LEVELS:
- L1: Official records, government gazettes, regulated filings (highest trust)
- L2: Internal approved reports, validated databases, meeting minutes
- L3: Direct stakeholder confirmation, email trails, documented interviews
- L4: Secondary reports, media, third-party references
- L5: Informal notes, verbal claims, AI-generated output (not accepted as factual without validation)

CONFIDENCE SCORING (0-2 per criterion, total 0-10):
- Authority: 0=unknown source, 1=secondary (L4), 2=official/authoritative (L1-L2)
- Traceability: 0=no trace, 1=general reference, 2=specific document/URL
- Recency: 0=outdated (>30 days), 1=possibly current (7-30 days), 2=confirmed current (<7 days)
- Consistency: 0=contradicted, 1=partially aligned, 2=fully aligned or single authoritative source
- Completeness: 0=major gaps, 1=minor gaps, 2=complete context

CONFIDENCE RATING:
- 8-10: High — accept as verified (T1 eligible)
- 5-7: Medium — use with caveat (T2)
- 3-4: Low — keep under review (T2 flagged)
- 0-2: Very Low — do not use as fact (T6)

AI SELF-SCORING CONSTRAINTS (Rule 6):
- You CANNOT self-certify T1. Maximum self-assigned tier = T2.
- Your maximum initial confidence score = 7. Human review required to exceed 7.
- Claims without traceable source = T6 (Rejected).
- Analytical assessments = T3 with [ASSESSMENT] tag.
- Projections/forecasts = T4 with [ASSUMPTION] tag.
- Conflicting sources detected = T5 with [DISPUTED] tag.

OUTPUT FORMAT — Append a CVS block after each factual claim:
---CVS BLOCK---
Claim: [exact factual claim]
Source: [source name + URL if available]
Source Level: [L1-L5]
Tier: [T1-T6]
Validation Status: [Verified/Partially Verified/Pending/Disputed/Inferred/Rejected]
Confidence Score: [0-10] (Authority:[0-2] Traceability:[0-2] Recency:[0-2] Consistency:[0-2] Completeness:[0-2])
Action Required: [None/Human review needed/Corroboration needed/Escalation]
---END CVS BLOCK---
---END CVS INSTRUCTIONS---
```

---

## Notes

1. This block is mandatory for all LLM-driven cronjobs producing intelligence products.
2. Script-only cronjobs (no_agent=True) do not need this block — they produce raw data, not claims.
3. The AI's self-assigned scores are preliminary. Human review upgrades T2→T1 and adjusts scores above 7.
4. Self-scored claims should be entered into the workspace's `CVS-EVIDENCE-REGISTER.csv` after human review.
5. The block adds approximately 300 tokens to each cronjob prompt — negligible overhead for the validation discipline gained.

---

**Master Document Location:** `/home/p62operator/.openclaw/workspace/03-VERIFICATION/CVS-CRONJOB-PROMPT-BLOCK.md`  
**Classification:** TLP:AMBER
