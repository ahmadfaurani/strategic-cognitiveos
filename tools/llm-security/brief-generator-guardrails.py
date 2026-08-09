#!/usr/bin/env python3
"""
DeepTeam Guardrails Integration for OpenClaw Brief Generator

Purpose: Wrap political brief outputs with DeepTeam safety guardrails
before delivery to Telegram/other channels.

Usage:
    from tools.llm-security.brief-generator-guardrails import guard_brief_output
    
    result = await guard_brief_output(input_prompt, brief_content)
    if result.breached:
        # Handle safety violation
        pass

Author: OpenClaw Main Session
Date: 2026-07-07
"""

import asyncio
import os
from typing import Optional, Dict, Any, List
from pathlib import Path

# =============================================================================
# Configuration
# =============================================================================

DEEPTEAM_VENV = Path("/home/p62operator/.openclaw/workspace/.venv-deepteam")

# Use OpenClaw's local vLLM model instead of OpenAI API
# This avoids external API costs and keeps evaluation local
GUARDRAILS_CONFIG = {
    "input_guards": [
        "PromptInjectionGuard"  # Block adversarial inputs
    ],
    "output_guards": [
        "ToxicityGuard",        # Prevent harmful content
        "PrivacyGuard",         # Prevent PII leakage
        "IllegalGuard",         # Prevent illegal activity facilitation
        # "HallucinationGuard"  # Optional: detect fabricated claims (requires fact-checking context)
    ],
    "sample_rate": 1.0,         # Guard 100% of requests (reduce for high-throughput)
    
    # Local vLLM configuration (OpenClaw default model)
    "model_type": "vllm",
    "model_name": "qwen36-27b-unc",  # Match configured model in openclaw.json
    "base_url": "https://model.arasintegrasi.ai/v1",  # OpenClaw vLLM endpoint
    # API key will be loaded from environment or OpenClaw config
    "api_key": os.getenv("VLLM_API_KEY", "sk-placeholder")
}

# =============================================================================
# Lazy Import (only when needed)
# =============================================================================

def _import_deepteam():
    """Import DeepTeam components lazily to avoid overhead when not used."""
    import sys
    sys.path.insert(0, str(DEEPTEAM_VENV / "lib" / "python3.12" / "site-packages"))
    
    from deepteam import Guardrails
    from deepteam.guardrails import (
        PromptInjectionGuard,
        ToxicityGuard,
        PrivacyGuard,
        IllegalGuard,
        HallucinationGuard
    )
    
    return Guardrails, {
        "PromptInjectionGuard": PromptInjectionGuard,
        "ToxicityGuard": ToxicityGuard,
        "PrivacyGuard": PrivacyGuard,
        "IllegalGuard": IllegalGuard,
        "HallucinationGuard": HallucinationGuard
    }

def _get_evaluation_model():
    """Configure local vLLM model for guardrails evaluation."""
    import sys
    import os
    sys.path.insert(0, str(DEEPTEAM_VENV / "lib" / "python3.12" / "site-packages"))
    
    from deepeval.models.llms.openai_model import GPTModel
    
    # Set a dummy API key to satisfy DeepEval's validation
    # The actual authentication is handled by vLLM (which doesn't require auth by default)
    os.environ["OPENAI_API_KEY"] = "vllm-local-key"
    
    # Configure GPTModel to use local vLLM endpoint
    # DeepTeam/DeepEval uses OpenAI-compatible API, which vLLM provides
    model = GPTModel(
        model=GUARDRAILS_CONFIG["model_name"],
        base_url=GUARDRAILS_CONFIG["base_url"],
        api_key="vllm-local-key"
    )
    
    return model

# =============================================================================
# Guardrails Instance (Singleton)
# =============================================================================

_guardrails_instance = None

def get_guardrails():
    """Get or create guardrails instance (singleton pattern)."""
    global _guardrails_instance
    
    if _guardrails_instance is None:
        Guardrails, guards = _import_deepteam()
        
        # Get local vLLM model for evaluation
        evaluation_model = _get_evaluation_model()
        
        # Build input guards
        input_guards = []
        for guard_name in GUARDRAILS_CONFIG["input_guards"]:
            if guard_name in guards:
                # Pass the local model to each guard
                input_guards.append(guards[guard_name](model=evaluation_model))
        
        # Build output guards
        output_guards = []
        for guard_name in GUARDRAILS_CONFIG["output_guards"]:
            if guard_name in guards:
                # Pass the local model to each guard
                output_guards.append(guards[guard_name](model=evaluation_model))
        
        _guardrails_instance = Guardrails(
            input_guards=input_guards,
            output_guards=output_guards,
            sample_rate=GUARDRAILS_CONFIG["sample_rate"]
        )
    
    return _guardrails_instance

# =============================================================================
# Main Guardrails Function
# =============================================================================

async def guard_brief_output(
    input_prompt: str,
    brief_content: str,
    skip_guardrails: bool = False
) -> Dict[str, Any]:
    """
    Guard a political brief output before delivery.
    
    Args:
        input_prompt: The prompt that generated the brief (for context)
        brief_content: The generated brief content to validate
        skip_guardrails: If True, bypass guardrails (for testing/emergency)
    
    Returns:
        Dict with keys:
            - breached: bool (True if any guard failed)
            - safe_to_deliver: bool (True if no breaches)
            - verdicts: List of individual guard results
            - error: str (if an error occurred)
    """
    
    if skip_guardrails:
        return {
            "breached": False,
            "safe_to_deliver": True,
            "verdicts": [],
            "note": "Guardrails skipped (emergency bypass)"
        }
    
    try:
        guardrails = get_guardrails()
        
        result = await guardrails.a_guard_output(
            input=input_prompt,
            output=brief_content
        )
        
        # Parse results
        verdicts = []
        for verdict in result.verdicts:
            verdicts.append({
                "name": verdict.name,
                "safety_level": verdict.safety_level,  # "safe", "uncertain", "unsafe"
                "reason": verdict.reason,
                "breached": verdict.safety_level in ["unsafe", "uncertain"]
            })
        
        return {
            "breached": result.breached,
            "safe_to_deliver": not result.breached,
            "verdicts": verdicts,
            "error": None
        }
        
    except Exception as e:
        # On error, fail open or closed based on your preference
        # Current: fail CLOSED (block delivery on error)
        return {
            "breached": True,
            "safe_to_deliver": False,
            "verdicts": [],
            "error": str(e)
        }

# =============================================================================
# Input Guardrails (for DeerFlow collection, etc.)
# =============================================================================

async def guard_brief_input(
    input_text: str,
    skip_guardrails: bool = False
) -> Dict[str, Any]:
    """
    Guard an input before processing (e.g., DeerFlow collection, user prompts).
    
    Args:
        input_text: The input text to validate
        skip_guardrails: If True, bypass guardrails
    
    Returns:
        Dict with same structure as guard_brief_output
    """
    
    if skip_guardrails:
        return {
            "breached": False,
            "safe_to_deliver": True,
            "verdicts": [],
            "note": "Guardrails skipped (emergency bypass)"
        }
    
    try:
        guardrails = get_guardrails()
        
        result = await guardrails.a_guard_input(input=input_text)
        
        verdicts = []
        for verdict in result.verdicts:
            verdicts.append({
                "name": verdict.name,
                "safety_level": verdict.safety_level,
                "reason": verdict.reason,
                "breached": verdict.safety_level in ["unsafe", "uncertain"]
            })
        
        return {
            "breached": result.breached,
            "safe_to_deliver": not result.breached,
            "verdicts": verdicts,
            "error": None
        }
        
    except Exception as e:
        return {
            "breached": True,
            "safe_to_deliver": False,
            "verdicts": [],
            "error": str(e)
        }

# =============================================================================
# CLI Test Mode
# =============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("DeepTeam Guardrails - Brief Generator Integration Test")
    print("=" * 70)
    print()
    print(f"Model: {GUARDRAILS_CONFIG['model_name']}")
    print(f"Base URL: {GUARDRAILS_CONFIG['base_url']}")
    print(f"Using: Local vLLM (OpenClaw)")
    print()
    
    # Test case: Safe brief
    test_input = "Generate political brief for N17 Semerah"
    test_output = """
## N17 Semerah War Room Brief - 2026-07-07

**BN Retention Probability:** High (60-65%)
**PH Upset Probability:** Low to Moderate (25-30%)

**Key Metrics:**
- Chinese turnout in Kampung Pantai Timor: 75%
- Youth turnout (18-30): 24.7% of electorate

**Assessment:** BN-leaning but operationally competitive.
"""
    
    print("Testing safe brief output...")
    print()
    
    result = asyncio.run(guard_brief_output(test_input, test_output))
    
    print(f"Breached: {result['breached']}")
    print(f"Safe to Deliver: {result['safe_to_deliver']}")
    print()
    
    if result.get("verdicts"):
        print("Verdicts:")
        for v in result["verdicts"]:
            emoji = {"safe": "✅", "uncertain": "⚠️", "unsafe": "❌"}.get(v["safety_level"], "❓")
            print(f"  {emoji} {v['name']}: {v['safety_level']}")
            if v.get("reason"):
                print(f"      {v['reason'][:100]}...")
    
    if result.get("error"):
        print(f"Error: {result['error']}")
    
    print()
    print("=" * 70)
    print("Integration test complete.")
    print()
    print("To use in Brief Generator:")
    print("  from tools.llm-security.brief-generator-guardrails import guard_brief_output")
    print("  result = await guard_brief_output(prompt, brief)")
    print("  if result['safe_to_deliver']:")
    print("      # Send to Telegram")
    print("  else:")
    print("      # Block and alert")
    print("=" * 70)
