# CVS Dashboard — Master Aggregate

**Classification:** TLP:AMBER  
**Created:** 2026-08-04  
**Purpose:** Cross-workstream validation status aggregate

---

## Dashboard Layers

### 1. Validated Facts (T1 — Ready for Formal Use)
Claims with tier=T1, validation_status=Verified across all workstream evidence registers.

### 2. Pending Validation (T2 — Under Review)
Claims with validation_status=Partially Verified or Pending. Flagged by days pending.

### 3. Disputed Claims (T5 — Requires Resolution)
Claims with tier=T5 or validation_status=Disputed. Escalation queue.

### 4. Source Register
All registered sources across all workstreams. See `CVS-SOURCE-REGISTER.md`.

### 5. Confidence Matrix
Per-claim breakdown of 5 scoring criteria. Filter by workstream, score range, or criteria.

### 6. Action Tracker
Claims with non-empty `action_required` field. Sorted by urgency (disputed > pending > low-score).

### 7. Audit Trail
Validation decisions and reviewer notes. `last_reviewed` and `owner` fields per claim.

---

## Dashboard Query Patterns (CSV)

To extract dashboard views from `CVS-EVIDENCE-REGISTER.csv`:

```bash
# Validated facts (T1)
awk -F',' '$9=="T1" && $10=="Verified"' CVS-EVIDENCE-REGISTER.csv

# Pending validation
awk -F',' '$10=="Partially Verified" || $10=="Pending"' CVS-EVIDENCE-REGISTER.csv

# Disputed claims
awk -F',' '$9=="T5" || $10=="Disputed"' CVS-EVIDENCE-REGISTER.csv

# Low confidence (score 0-4)
awk -F',' '$11<5' CVS-EVIDENCE-REGISTER.csv

# Action required
awk -F',' '$19!="None" && $19!=""' CVS-EVIDENCE-REGISTER.csv
```

---

**Master Document Location:** `/home/p62operator/.openclaw/workspace/03-VERIFICATION/CVS-DASHBOARD.md`  
**Classification:** TLP:AMBER
