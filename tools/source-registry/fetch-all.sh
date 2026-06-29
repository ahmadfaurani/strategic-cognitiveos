#!/bin/bash
# Fetch from all Tier 0–1 sources for cross-reference
# Runs parallel fetches, aggregates into single JSONL

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DATE=$(date -u +%Y-%m-%d)

echo "=== Multi-Source Fetch ==="
echo "Date: $DATE"
echo ""

# Fetch from each Tier 0–1 source
echo "[1/5] SPR (Tier 0)..."
bash "$SCRIPT_DIR/fetch-spr.sh"

echo "[2/5] Malaysiakini (Tier 1)..."
bash "$SCRIPT_DIR/fetch-mkini.sh"

echo "[3/5] The Star (Tier 1)..."
# Placeholder: implement fetch-thestar.sh
echo "  ⚠ fetch-thestar.sh not yet implemented"

echo "[4/5] NST (Tier 1)..."
# Placeholder: implement fetch-nst.sh
echo "  ⚠ fetch-nst.sh not yet implemented"

echo "[5/5] FMT (Tier 1)..."
# Placeholder: implement fetch-fmt.sh
echo "  ⚠ fetch-fmt.sh not yet implemented"

echo ""
echo "=== Fetch Complete ==="
echo "Raw data: /home/p62operator/.openclaw/workspace/memory/signals/raw/${DATE}-*.jsonl"
echo ""
echo "Next step: Run crossref.sh to compare claims across sources"
