#!/bin/bash
# Fetch latest election/politics news from Malaysiakini
# Output: Structured JSONL for ingestion

set -e

OUTPUT_DIR="/home/p62operator/.openclaw/workspace/memory/signals/raw"
mkdir -p "$OUTPUT_DIR"

DATE=$(date -u +%Y-%m-%d)
OUTPUT_FILE="$OUTPUT_DIR/${DATE}-mkini.jsonl"

echo "Fetching Malaysiakini (Tier 1)..."

# Fetch RSS feed
RSS_URL="https://www.malaysiakini.com/en/rss/news"
TEMP_FILE=$(mktemp)

curl -s "$RSS_URL" -o "$TEMP_FILE"

# Extract items (title, link, pubDate, description)
# Simple XML parsing with grep/sed (production would use xmlstarlet)
grep -E '<item>|<title>|<link>|<pubDate>|<description>' "$TEMP_FILE" | \
while read -r line; do
    # Parse and output as JSONL
    # Simplified for demo; production needs proper XML parser
    echo "$line"
done > "$OUTPUT_FILE"

rm -f "$TEMP_FILE"

echo "✓ Fetched Malaysiakini → $OUTPUT_FILE"
