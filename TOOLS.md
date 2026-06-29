# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

Add whatever helps you do your job. This is your cheat sheet.

---

## 📄 Git-to-Drive (PDF Automation)

**Location:** `tools/git-to-drive/`

**Purpose:** Generate professional PDFs from Git repos → Auto-upload to Google Drive

### Quick Commands

```bash
# Setup (one-time)
cd tools/git-to-drive
./setup.sh
rclone config

# Generate & upload PDF
./git-to-drive.sh https://github.com/user/repo
./git-to-drive.sh https://github.com/user/repo my-documentation
./git-to-drive.sh ./local-repo report-2026 "/Shared/Docs"
```

### Configuration

- **rclone remote:** `drive`
- **Default Drive folder:** `/Git-PDFs`
- **Template:** Eisvogel (LaTeX)
- **Syntax highlighting:** Monokai

### Credentials

- **Config file:** `~/.config/rclone/rclone.conf`
- **Service account:** `~/.config/rclone/gdrive-service-account.json`
- **Setup guide:** `tools/git-to-drive/CREDENTIALS_SETUP.md`

### GitHub Actions

For CI/CD automation, use workflow in `tools/git-to-drive/github-workflow.yml`

Required secrets:
- `GDRIVE_SERVICE_ACCOUNT` — Service account JSON
- `GDRIVE_FOLDER_ID` — Target Drive folder ID

---

## 🔍 Truth Validation Protocol

**Purpose:** Prevent hallucination, factual drift, and conflation of inference with fact in long-form outputs.

**Mandatory for:** Any output containing numerical claims, named entities, historical data, or analytical assessments.

### Claim Tiers

#### Tier 1: Factual Claims (Must verify before output)
- Numbers: vote counts, percentages, dates, margins, electorate sizes
- Names: candidates, positions, titles, party affiliations
- Locations: constituencies, polling districts, geographic references
- Historical results: past election outcomes, majorities, turnout figures

**Validation method:** Cross-reference against source file + line number. If source is external (news, official data), fetch and cite URL.

**Output requirement:** Every Tier 1 claim must include `Source: <file#line>` or `Source: <URL>`

---

#### Tier 2: Analytical Claims (Must label confidence)
- Vote split calculations
- Turnout sensitivity analysis
- Demographic inferences
- Strategic assessments
- Mathematical derivations

**Validation method:** Show the math explicitly. Tag confidence:
- `[HIGH]` — Derived from verified Tier 1 data, straightforward calculation
- `[MEDIUM]` — Reasonable inference from multiple data points
- `[LOW]` — Speculative, depends on unverified assumptions

**Output requirement:** Confidence tag + brief justification

---

#### Tier 3: Predictive/Speculative Claims (Must flag as such)
- Future scenarios
- Emerging narratives
- Risk assessments
- "What-if" modelling

**Validation method:** Explicitly mark as `SPECULATION:` or `SCENARIO:` — never present as fact.

**Output requirement:** Clear demarcation + underlying assumptions stated

---

### Pre-Output Checklist

Before any long-form analysis leaves the queue:

```
[ ] All Tier 1 numbers verified against source?
[ ] All names double-checked (spelling, position, party)?
[ ] All citations include file#line or URL?
[ ] Confidence tags applied to Tier 2 claims?
[ ] Tier 3 speculation clearly demarcated?
[ ] Any contradictory evidence considered?
[ ] Math shown explicitly for analytical claims?
```

---

### Structured Output Format

For complex analysis, use tabular format:

```markdown
## Claim | Source | Confidence | Notes
--------|--------|--------------|------
"BN won 2022 by 4,041 votes" | MEMORY.md#L142 | HIGH | Verified from SPR data
"PN could exceed 2022 base" | Inference | MEDIUM | Depends on Malay sentiment shift
"Turnout >80% favors PH" | Historical pattern | MEDIUM | Based on 2018 vs 2022 delta
```

---

### Automated Validation Tools

**Location:** `tools/truth-validator/`

```bash
# Validate claims against source files
./tools/truth-validator/validate.sh memory/n17-semerah-war-room-brief-20260627.md

# Extract and verify all numerical claims
./tools/truth-validator/extract-numbers.sh < input.md

# Cross-reference candidate names with official registry
./tools/truth-validator/verify-names.sh < input.md
```

**Integration:** Run validator before any political brief is delivered.

---

## Related

- [Agent workspace](/concepts/agent-workspace)
- [Git-to-Drive Docs](tools/git-to-drive/README.md)
