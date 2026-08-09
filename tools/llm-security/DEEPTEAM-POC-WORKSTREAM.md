# DeepTeam POC Workstream

**Workstream ID:** DEEPTEAM-POC-2026-07  
**Created:** 2026-07-07 15:00 UTC  
**Status:** ⏳ Awaiting API Key Configuration  
**Authorized By:** DAF (message_id: 8614, 2026-07-07 14:29 UTC)  
**Owner:** OpenClaw Main Session

---

## Executive Summary

**Objective:** Deploy DeepTeam LLM security testing framework as output guardrails for OpenClaw Brief Generator workflow.

**Current State:** Installation complete, integration wrapper created, configured for OpenClaw vLLM endpoint. Awaiting valid API key to proceed with production testing.

**Risk Level:** LOW (output guardrails only, fail-closed on errors)  
**Estimated Effort:** 2-4 hours remaining (after API key configured)  
**Business Value:** Prevents PII leakage, toxic content, and prompt injection in political briefs

---

## Workstream Timeline

| Date | Milestone | Status | Notes |
|------|-----------|--------|-------|
| 2026-07-07 14:00 | POC Request | ✅ Complete | DAF approved DeepTeam installation |
| 2026-07-07 14:15 | Package Installation | ✅ Complete | DeepTeam 1.0.7 installed in `.venv-deepteam` |
| 2026-07-07 14:30 | Component Validation | ✅ Complete | All imports successful (39 vulns, 30 attacks, 5 frameworks, 5 guardrails) |
| 2026-07-07 14:45 | Integration Wrapper | ✅ Complete | `brief-generator-guardrails.py` created |
| 2026-07-07 15:00 | vLLM Configuration | ✅ Complete | Configured for `https://model.arasintegrasi.ai/v1` (qwen36-27b-unc) |
| 2026-07-07 15:15 | Documentation | ✅ Complete | 4 files created (analytical report, deployment guide, quick start, this workstream) |
| TBD | API Key Configuration | ⏳ Pending | Requires `VLLM_API_KEY` environment variable |
| TBD | Full Test Suite | ⏳ Pending | 6-scenario validation (safe, PII, toxic, injection, illegal, hallucination) |
| TBD | Production Integration | ⏳ Pending | Add guardrails call to Brief Generator workflow |
| TBD | CVS Pipeline Integration | ⏳ Pending | Add monthly DeepTeam scan to HEARTBEAT.md |

---

## Technical Architecture

### Components Deployed

```
┌─────────────────────────────────────────────────────────────┐
│ OpenClaw Brief Generator                                    │
│  └─ DeerFlow Collection → PIR Tagging → Signal Grading     │
│     → Brief Generation → [GUARDRAILS] → Telegram Delivery  │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│ DeepTeam Guardrails (brief-generator-guardrails.py)         │
│  └─ Input Guards: PromptInjectionGuard                      │
│  └─ Output Guards: Toxicity, Privacy, Illegal, Hallucination│
│     └─ Evaluation Model: qwen36-27b-unc (vLLM)             │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│ vLLM Provider (https://model.arasintegrasi.ai/v1)           │
│  └─ LLM-as-a-Judge for safety evaluation                    │
└─────────────────────────────────────────────────────────────┘
```

### Configuration

**Virtual Environment:**
- Location: `/home/p62operator/.openclaw/workspace/.venv-deepteam`
- Python: 3.12
- DeepTeam: 1.0.7
- Dependencies: ~50 packages (isolated from main OpenClaw env)

**Guardrails Configuration:**
```python
GUARDRAILS_CONFIG = {
    "model_name": "qwen36-27b-unc",
    "base_url": "https://model.arasintegrasi.ai/v1",
    "input_guards": ["PromptInjectionGuard"],
    "output_guards": ["ToxicityGuard", "PrivacyGuard", "IllegalGuard"],
    "sample_rate": 1.0,  # 100% coverage
}
```

**API Requirements:**
- Environment variable: `VLLM_API_KEY` (required)
- Format: `sk-...` (OpenAI-compatible key format)
- Purpose: Satisfies DeepEval validation, used for vLLM authentication

---

## Files Created

| File | Size | Purpose | Status |
|------|------|---------|--------|
| `tools/llm-security/deepteam-analytical-report-20260707.md` | 29 KB | Comprehensive analysis (50+ vulns, competitive landscape, operational benefits) | ✅ Complete |
| `tools/llm-security/brief-generator-guardrails.py` | 10 KB | Production integration wrapper (async, singleton, lazy import) | ✅ Complete |
| `tools/llm-security/deepteam-poc-test.py` | 9 KB | Full test suite (6 scenarios: safe, PII, toxic, injection, illegal, hallucination) | ✅ Complete |
| `tools/llm-security/deepteam-poc-test-simple.py` | 7 KB | Import validation (no API key needed) | ✅ Complete |
| `tools/llm-security/DEEPTEAM-POC-RESULTS.md` | 10 KB | Deployment guide, troubleshooting, configuration options | ✅ Complete |
| `tools/llm-security/README-DEEPTEAM.md` | 4 KB | Quick start guide (3-step activation) | ✅ Complete |
| `tools/llm-security/DEEPTEAM-POC-WORKSTREAM.md` | - | This workstream document | ✅ Complete |

**Total:** 69 KB of documentation + code

---

## Test Results

### Import Validation (✅ Passed)

```
✅ DeepTeam 1.0.7 imported
✅ 39 vulnerability classes available
✅ 24 single-turn + 6 multi-turn attacks available
✅ 5 safety frameworks (OWASP, NIST, EU AI Act)
✅ 5 guardrails classes importable
```

### Guardrails Execution (⚠️ Partial)

```
Model: qwen36-27b-unc
Base URL: https://model.arasintegrasi.ai/v1
Status: Executing but returning invalid results (API key issue)

Test Case: Safe brief output
Result: All guards returned "unsafe" (false positive)
Root Cause: Invalid/placeholder API key
Resolution: Set valid VLLM_API_KEY environment variable
```

### Expected Test Results (After API Key Configured)

| Test Case | Input | Expected Guard Result | Expected Delivery |
|-----------|-------|----------------------|-------------------|
| Safe Brief | Normal political brief | All guards: safe | ✅ Deliver |
| PII Leak | Brief with IC numbers, phone numbers | PrivacyGuard: unsafe | ❌ Block |
| Toxic Content | Brief with offensive language | ToxicityGuard: unsafe | ❌ Block |
| Prompt Injection | "Ignore previous instructions..." | PromptInjectionGuard: unsafe | ❌ Block |
| Illegal Activity | Brief facilitating illegal acts | IllegalGuard: unsafe | ❌ Block |
| Hallucination | Brief with fabricated claims | HallucinationGuard: uncertain | ⚠️ Review |

---

## Deployment Sequence (DAF-Approved)

### Phase 1: Output Guardrails (P1) - Current Focus
- [ ] Configure `VLLM_API_KEY` environment variable
- [ ] Run full test suite (6 scenarios)
- [ ] Validate results (check false positive/negative rate)
- [ ] Integrate into Brief Generator (output stage)
- [ ] Monitor first 100 guarded briefs
- [ ] Document incidents and adjustments

### Phase 2: Input Guardrails + Monthly Scans (P2)
- [ ] Add input guardrails to DeerFlow collection
- [ ] Configure monthly red team assessment
- [ ] Integrate into HEARTBEAT.md pipeline review
- [ ] Track vulnerability trends over time

### Phase 3: Full Agentic Assessment (P3)
- [ ] Test 11 agentic AI vulnerabilities (Goal Theft, Recursive Hijacking, etc.)
- [ ] Assess multi-agent communication channels
- [ ] Quarterly comprehensive red team assessment
- [ ] Update MEMORY.md with lessons learned

---

## Operational Metrics (Baseline)

**Performance:**
- Latency per guard: ~100-500ms (LLM evaluation time)
- Total overhead (3 guards): ~300-1500ms per brief
- Token consumption: ~100-300 tokens per guard evaluation
- Cost estimate: Depends on vLLM provider pricing

**Coverage:**
- Sample rate: 100% (all briefs guarded)
- Guard types: 3 output guards (Toxicity, Privacy, Illegal)
- Input guards: 1 (Prompt Injection) - optional activation

**Safety:**
- Failure mode: Fail-closed (block on error)
- False positive handling: Manual review queue
- False negative handling: Monthly red team scans

---

## Risks & Mitigations

| Risk | Impact | Probability | Mitigation |
|------|--------|-------------|------------|
| Invalid API key | High | ✅ Current | Obtain valid key from vLLM provider admin |
| High false positive rate | Medium | Medium | Tune guard strictness, add human review queue |
| Latency impact on brief delivery | Low | Medium | Use async execution, reduce sample rate if needed |
| vLLM endpoint unavailable | Medium | Low | Fallback to OpenAI API (configure secondary provider) |
| Guardrails bypass (adversarial) | High | Low | Monthly red team scans, update vulnerability coverage |

---

## Open Decisions

| Decision | Options | Recommendation | Status |
|----------|---------|----------------|--------|
| API Key Source | vLLM vs OpenAI | vLLM (already configured in OpenClaw) | ✅ Decided |
| Sample Rate | 100% vs 10% | 100% for POC, adjust based on false positive rate | ⏳ Pending |
| Hallucination Guard | Enable vs Disable | Disable initially (requires fact-checking context) | ✅ Decided |
| Failure Mode | Fail-closed vs Fail-open | Fail-closed (safer for political content) | ✅ Decided |
| Human Review Queue | Required vs Optional | Optional for POC, required if false positives >5% | ⏳ Pending |

---

## Next Actions (Awaiting Resumption)

### Immediate (When API Key Available)

1. **Set Environment Variable**
   ```bash
   export VLLM_API_KEY="sk-you…-key"
   ```

2. **Run Full Test Suite**
   ```bash
   cd /home/p62operator/.openclaw/workspace
   .venv-deepteam/bin/python tools/llm-security/deepteam-poc-test.py
   ```

3. **Validate Results**
   - Expected: Safe brief passes, PII/toxic/illegal briefs blocked
   - Review false positives/negatives
   - Adjust guard configuration if needed

4. **Production Integration**
   - Add guardrails call to Brief Generator workflow
   - Start with 100% sample rate
   - Monitor first 100 briefs

### Short-Term (1-2 Weeks After Activation)

1. **Performance Monitoring**
   - Track latency impact on brief delivery
   - Measure token consumption per guard evaluation
   - Calculate actual cost per day/week/month

2. **Incident Review**
   - Log all blocked briefs
   - Categorize by guard type (Toxicity, Privacy, Illegal)
   - Identify patterns (false positives vs legitimate blocks)

3. **Configuration Tuning**
   - Adjust sample rate if latency/cost too high
   - Add/remove guards based on incident patterns
   - Consider adding HallucinationGuard if fact-checking context available

### Medium-Term (1 Month After Activation)

1. **CVS Pipeline Integration**
   - Add monthly DeepTeam scan to HEARTBEAT.md
   - Track vulnerability trends over time
   - Update MEMORY.md with key insights

2. **Input Guardrails**
   - Deploy PromptInjectionGuard on DeerFlow collection
   - Block adversarial content at ingestion stage
   - Reduce downstream processing of malicious inputs

3. **Quarterly Red Team Assessment**
   - Run full 50+ vulnerability scan
   - Compare results quarter-over-quarter
   - Identify emerging risks and mitigation strategies

---

## Stakeholder Communications

### DAF Briefing Points

**What was delivered:**
- DeepTeam installation complete (v1.0.7)
- Integration wrapper configured for OpenClaw vLLM
- 69 KB of documentation (analytical report, deployment guide, quick start)
- Test suite ready for execution

**What's blocked:**
- Valid `VLLM_API_KEY` required for production testing
- Guardrails execute but return invalid results with placeholder key

**What's needed:**
- Obtain vLLM API key from provider administrator
- OR authorize use of OpenAI API (separate cost center)

**Timeline:**
- API key configuration: 15 minutes (once key available)
- Full test suite: 10-15 minutes
- Production integration: 1-2 hours
- Total remaining effort: 2-4 hours

**Business Value:**
- Prevents PII leakage in political briefs
- Blocks toxic/harmful content before Telegram delivery
- Detects prompt injection attempts from compromised sources
- Protects agent workflows from agentic AI vulnerabilities (unique to DeepTeam)

---

## Appendix: Command Reference

### Quick Commands

```bash
# Test guardrails (after API key configured)
cd /home/p62operator/.openclaw/workspace
.venv-deepteam/bin/python tools/llm-security/brief-generator-guardrails.py

# Run full test suite
.venv-deepteam/bin/python tools/llm-security/deepteam-poc-test.py

# Validate imports only (no API key needed)
.venv-deepteam/bin/python tools/llm-security/deepteam-poc-test-simple.py

# Check vLLM endpoint
curl https://model.arasintegrasi.ai/v1/models -H "Authorization: Bearer $VLLM_API_KEY"
```

### Environment Setup

```bash
# Set API key (persistent)
echo 'export VLLM_API_KEY="sk-..." ' >> ~/.bashrc
source ~/.bashrc

# Set API key (current session only)
export VLLM_API_KEY="sk-..."

# Verify key is set
echo $VLLM_API_KEY
```

### Integration Code Snippet

```python
from tools.llm-security.brief-generator-guardrails import guard_brief_output

async def generate_and_send_brief():
    # Generate brief (existing code)
    brief = await generate_political_brief()
    
    # Guard before delivery
    result = await guard_brief_output(
        input_prompt="Generate N17 Semerah brief",
        brief_content=brief
    )
    
    if result['safe_to_deliver']:
        await send_to_telegram(brief)
    else:
        violations = [v['name'] for v in result['verdicts'] if v['breached']]
        await alert_admin(f"Brief blocked: {', '.join(violations)}")
```

---

## References

### Internal Documentation
- Analytical Report: `tools/llm-security/deepteam-analytical-report-20260707.md`
- Deployment Guide: `tools/llm-security/DEEPTEAM-POC-RESULTS.md`
- Quick Start: `tools/llm-security/README-DEEPTEAM.md`
- Integration Wrapper: `tools/llm-security/brief-generator-guardrails.py`

### External Resources
- DeepTeam Documentation: https://www.trydeepteam.com/docs
- DeepTeam GitHub: https://github.com/confident-ai/deepteam
- DeepTeam Discord: https://discord.gg/3SEyvpgu2f
- OWASP Top 10 for LLM: https://owasp.org/www-project-top-10-for-large-language-model-applications/

### OpenClaw Configuration
- Gateway Config: `~/.openclaw/openclaw.json`
- vLLM Provider: `https://model.arasintegrasi.ai/v1`
- Model: `qwen36-27b-unc`
- Context Window: 128K tokens

---

**Workstream Status:** ⏳ Awaiting API Key Configuration  
**Next Review:** Upon DAF request or API key availability  
**Contact:** OpenClaw Main Session (this workspace)

---

*Workstream document created by OpenClaw Main Session*  
*Date: 2026-07-07 15:15 UTC*  
*Classification: Internal Technical Documentation*  
*Retention: Until POC complete + 90 days*
