# DeepTeam LLM Security - Quick Start

**Status:** ✅ Installation Complete | ⏳ Awaiting API Key  
**Last Updated:** 2026-07-07

---

## What is DeepTeam?

DeepTeam is an LLM red teaming and guardrails framework that:
- Tests your LLM applications against 50+ vulnerabilities
- Provides runtime guardrails to block harmful content
- Supports OWASP, NIST, MITRE ATLAS, and EU AI Act frameworks
- **Unique:** Only tool with integrated red teaming + production guardrails

---

## Quick Start (3 Steps)

### Step 1: Set API Key

DeepTeam guardrails need an LLM API key for safety evaluation.

**Option A: Use OpenClaw's vLLM (Recommended)**
```bash
export VLLM_API_KEY="sk-your-actual-key"
```

**Option B: Use OpenAI**
```bash
export OPENAI_API_KEY="sk-your-openai-key"
```

### Step 2: Test Guardrails

```bash
cd /home/p62operator/.openclaw/workspace
.venv-deepteam/bin/python tools/llm-security/brief-generator-guardrails.py
```

**Expected Output:**
```
✅ Toxicity Guard: safe
✅ Privacy Guard: safe
✅ Illegal Guard: safe
```

### Step 3: Integrate into Brief Generator

```python
from tools.llm-security.brief-generator-guardrails import guard_brief_output

# Before sending brief to Telegram
result = await guard_brief_output(
    input_prompt="Generate N17 Semerah brief",
    brief_content=brief_text
)

if result['safe_to_deliver']:
    await send_to_telegram(brief_text)
else:
    # Block and alert
    violations = [v['name'] for v in result['verdicts'] if v['breached']]
    print(f"Brief blocked: {violations}")
```

---

## Files in This Directory

| File | Purpose |
|------|---------|
| `deepteam-analytical-report-20260707.md` | Comprehensive 29KB analysis report |
| `brief-generator-guardrails.py` | Production integration wrapper |
| `deepteam-poc-test.py` | Full test suite (6 scenarios) |
| `deepteam-poc-test-simple.py` | Import validation (no API key needed) |
| `DEEPTEAM-POC-RESULTS.md` | Deployment guide & troubleshooting |
| `README-DEEPTEAM.md` | This quick start guide |

---

## Configuration

Edit `brief-generator-guardrails.py` to customize:

```python
GUARDRAILS_CONFIG = {
    "model_name": "qwen36-27b-unc",  # Model for evaluation
    "base_url": "https://model.arasintegrasi.ai/v1",
    "output_guards": [
        "ToxicityGuard",    # Block harmful content
        "PrivacyGuard",     # Block PII leakage
        "IllegalGuard",     # Block illegal activity
    ],
    "sample_rate": 1.0,    # Guard 100% of requests
}
```

---

## Operational Benefits

1. **Blocks PII leakage** - Prevents accidental exposure of contact info, IC numbers, etc.
2. **Prevents toxic content** - Blocks harmful, offensive, or biased outputs
3. **Detects prompt injection** - Stops adversarial attempts to hijack agent behavior
4. **Agentic AI protection** - Unique coverage for multi-agent systems (Goal Theft, Recursive Hijacking, etc.)

**Cost:** ~100-300 tokens per guarded request (depends on model pricing)

---

## Troubleshooting

### "API key is not configured"
```bash
export VLLM_API_KEY="sk-..."
# or
export OPENAI_API_KEY="sk-..."
```

### "ModuleNotFoundError: No module named 'deepteam'"
```bash
# Run from virtual environment
.venv-deepteam/bin/python <script.py>
```

### All guards return "unsafe"
- Check API key is valid
- Verify vLLM endpoint is accessible
- Test with: `curl https://model.arasintegrasi.ai/v1/models -H "Authorization: Bearer $VLLM_API_KEY"`

---

## Documentation

- **Full Deployment Guide:** `DEEPTEAM-POC-RESULTS.md`
- **Analytical Report:** `deepteam-analytical-report-20260707.md`
- **DeepTeam Docs:** https://www.trydeepteam.com/docs

---

## Next Steps

1. **Get API key** from your vLLM provider or OpenAI
2. **Run test suite** to validate guardrails
3. **Integrate** into Brief Generator workflow
4. **Monitor** blocked briefs and adjust configuration

---

*Quick Start Guide - OpenClaw Workspace*  
*2026-07-07*
