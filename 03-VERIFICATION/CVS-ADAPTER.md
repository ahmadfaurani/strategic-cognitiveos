# CVS Adapter — Strategic CognitiveOS

**Classification:** TLP:AMBER  
**Created:** 2026-08-04  
**Master Framework:** `/home/p62operator/.openclaw/workspace/03-VERIFICATION/CVS-FRAMEWORK.md`

---

## Workstream: CogOS
**Claim ID Format:** `CVS-COG-NNN`

## Domain
Strategic Intelligence — PIR Validation and AI Council Assessment

## Domain-Specific Rules

### PIR-Sourced Claims
Priority Intelligence Requirements (PIR) claims must be validated against the PIR evidence chain. PIR status assessments are **T3 (Analytical Interpretation)** — they represent analytical judgment about collection status, not raw facts.

### AI Council Outputs
- AI Council assessments (Sol, GLM, Claude, Gemini) → **T3 (Analytical Interpretation)** by default
- AI Council outputs with traceable source backing → **T2** with Rule 6 flag (AI output requires validation)
- AI Council outputs without sources → **T6 (Rejected)** per Rule 6

### Strategic Records
- STK (Stakeholder) records → L2 source, T2 unless independently verified
- INIT (Initiative) records → L2 source, T2 for documented initiatives
- OPP (Opportunity) records → L2 source, T2 for documented opportunities
- INT (Intelligence) records → L2-L4 depending on source traceability

### AI Self-Scoring Constraint
All AI-generated PIR assessments and strategic analyses are capped at confidence score 7 until human review (Rule 6). The AI Council cannot self-certify T1.

## Files in This Directory
- `CVS-EVIDENCE-REGISTER.csv` — PIR validation claims register
- `CVS-ADAPTER.md` — This file

---

**Classification:** TLP:AMBER
