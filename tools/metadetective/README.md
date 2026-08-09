# MetaDetective - Metadata Extraction Tool

**Purpose:** OSINT and pentesting metadata extraction from documents, images, emails, and websites.

**GitHub:** https://github.com/franckferman/MetaDetective

**Added:** 2026-07-05

---

## Overview

MetaDetective is a single-file Python 3 tool for metadata extraction and web scraping, built for OSINT and pentesting workflows. Designed as a Metagoofil replacement.

**Key Advantage:** No Python dependencies beyond `exiftool`. One curl and you're operational.

---

## What It Extracts

- **Identities:** Authors, creators, last-modified-by
- **Software:** Application versions, tools used to create documents
- **Location:** GPS coordinates with reverse geocoding (OpenStreetMap)
- **Timestamps:** Creation, modification, access dates
- **Infrastructure:** Internal hostnames, serial numbers
- **Media:** Camera models, hyperlinks, email addresses

---

## Supported File Types

**Documents:** PDF, DOCX, ODT, XLS, XLSX, PPTX, ODP, RTF, CSV, XML

**Images:** JPEG, PNG, TIFF, BMP, GIF, SVG, PSD, HEIC, HEIF

**Email:** EML, MSG, PST, OST

**Video:** MP4, MOV

---

## Installation

### Prerequisites

```bash
# Debian / Ubuntu / Kali
sudo apt install libimage-exiftool-perl

# Arch
sudo pacman -S perl-image-exiftool

# Gentoo
sudo emerge -av media-libs/exiftool

# macOS
brew install exiftool

# Windows
winget install OliverBetz.ExifTool
```

### Install MetaDetective

```bash
# Option 1: Direct download (recommended)
curl -O https://raw.githubusercontent.com/franckferman/MetaDetective/stable/src/MetaDetective/MetaDetective.py
python3 MetaDetective.py -h

# Option 2: pip
pip install MetaDetective
metadetective -h

# Option 3: Git clone
git clone https://github.com/franckferman/MetaDetective.git
cd MetaDetective
python3 src/MetaDetective/MetaDetective.py -h

# Option 4: Docker
docker pull franckferman/metadetective
docker run --rm franckferman/metadetective -h
```

---

## Quick Start

```bash
# Analyze a directory (default: singular/deduplicated view)
python3 MetaDetective.py ./loot/

# Analyze a single file
python3 MetaDetective.py report.pdf

# Scrape website and download files
python3 MetaDetective.py https://target.com/

# Quick summary stats
python3 MetaDetective.py -d ./loot/ --summary
```

---

## Core Usage Patterns

### File/Directory Analysis

```bash
# Analyze directory with deduplicated view
python3 MetaDetective.py -d ./loot/

# Filter by file types
python3 MetaDetective.py -d ./loot/ -t pdf docx

# Ignore noise patterns (regex supported)
python3 MetaDetective.py -d ./loot/ -i admin anonymous

# Per-file display (forensic mode)
python3 MetaDetective.py -d ./loot/ --display all

# Formatted output (vertical list with markers)
python3 MetaDetective.py -d ./loot/ --format formatted

# Single file
python3 MetaDetective.py -f report.pdf

# Multiple files
python3 MetaDetective.py -f report.pdf photo.heic
```

### Summary & Timeline Views

```bash
# Quick stats: identities, emails, GPS exposure, tools, date range
python3 MetaDetective.py -d ./loot/ --summary

# Chronological view of document creation/modification
python3 MetaDetective.py -d ./loot/ --timeline

# Both together
python3 MetaDetective.py -d ./loot/ --summary --timeline

# Scripting mode (no banner)
python3 MetaDetective.py -d ./loot/ --summary --no-banner
```

### Selective Field Extraction

```bash
# Extract only Author and Creator fields
python3 MetaDetective.py -d ./loot/ --parse-only Author Creator

# Extract GPS data only from iPhone photos
python3 MetaDetective.py -d ./photos/ -t heic heif --parse-only 'GPS Position' 'Map Link'
```

### Export Formats

```bash
# HTML report (default) - dark theme, stats bar, responsive
python3 MetaDetective.py -d ./loot/ -e html

# HTML per-file view
python3 MetaDetective.py -d ./loot/ --display all -e html

# Plain text
python3 MetaDetective.py -d ./loot/ -e txt

# JSON (structured, pipe into jq)
python3 MetaDetective.py -d ./loot/ -e json

# JSON per-file
python3 MetaDetective.py -d ./loot/ --display all -e json

# Custom output directory and filename suffix
python3 MetaDetective.py -d ./loot/ -e json -c pentest-corp -o ~/results/
```

**JSON Output Structure:**
```json
{
  "tool": "MetaDetective",
  "generated": "2026-03-21T...",
  "unique": {
    "Author": ["Alice Martin", "Bob Dupont"],
    "Creator Tool": ["Microsoft Word 16.0"]
  }
}
```

**Query with jq:**
```bash
jq '.unique.Author' MetaDetective_Export-*.json
```

---

## Web Scraping Mode

MetaDetective can crawl target websites, discover downloadable files, and download them for local metadata analysis.

### Scraping Modes

**Download (primary):** Downloads files to local directory for analysis

**Scan (preview):** Lists discovered files and stats without downloading

### Depth Control

| Depth | Behavior |
|-------|----------|
| 0 | Only the target URL (single page) |
| 1 (default) | Target URL + all pages linked from it |
| 2+ | Follows links N levels deep |

### Download Examples

```bash
# Standard download with depth 1 (recommended)
python3 MetaDetective.py --scraping --url https://target.com/ \
  --download-dir ~/loot/ --depth 1

# Target specific file types
python3 MetaDetective.py --scraping --url https://target.com/ \
  --download-dir ~/loot/ --depth 2 --extensions pdf docx xlsx pptx

# Parallel download (8 threads, 10 req/s)
python3 MetaDetective.py --scraping --url https://target.com/ \
  --download-dir ~/loot/ --depth 2 --threads 8 --rate 10

# Follow external links (CDN, subdomain, partner sites)
python3 MetaDetective.py --scraping --url https://target.com/ \
  --download-dir ~/loot/ --depth 1 --follow-extern

# Stealth mode (realistic User-Agent + low rate)
python3 MetaDetective.py --scraping --url https://target.com/ \
  --download-dir ~/loot/ --depth 2 --user-agent stealth --rate 2
```

### Scan (Preview) Examples

```bash
# Quick preview: how many files are reachable?
python3 MetaDetective.py --scraping --scan --url https://target.com/ --depth 1

# Filter preview by extension
python3 MetaDetective.py --scraping --scan --url https://target.com/ \
  --depth 2 --extensions pdf docx
```

### Full Pipeline (Scrape + Analyze + Export)

```bash
# Step 1: Download files
python3 MetaDetective.py --scraping --url https://target.com/ \
  --download-dir ~/loot/ --depth 2 --extensions pdf docx xlsx

# Step 2: Analyze and export
python3 MetaDetective.py -d ~/loot/ -e html -o ~/results/
```

### Scraping Flags

| Flag | Default | Description |
|------|---------|-------------|
| `--url` | required | Target URL |
| `--download-dir` | `./loot/` | Download destination (created if missing) |
| `--scan` | - | Preview mode (no download) |
| `--depth` | 1 | Link depth to follow (0 = single page, 2+ = deeper) |
| `--extensions` | all supported | Filter by file type |
| `--threads` | 4 | Concurrent download threads (1-100) |
| `--rate` | 5 | Max requests per second (1-1000) |
| `--follow-extern` | off | Follow links to external domains |
| `--user-agent` | `MetaDetective/<ver>` | Custom or preset UA string |

### User-Agent Presets

```bash
# Use preset
python3 MetaDetective.py --scraping --scan --url https://target.com/ --user-agent stealth

# Available presets:
# stealth, chrome-win, chrome-mac, chrome-linux,
# firefox-win, firefox-mac, firefox-linux,
# safari-mac, edge-win, android, iphone, googlebot

# Custom string
python3 MetaDetective.py --scraping --scan --url https://target.com/ \
  --user-agent 'Mozilla/5.0 (compatible; MyScanner/1.0)'
```

---

## GPS & Geocoding

When files expose GPS coordinates, MetaDetective resolves them to human-readable addresses via OpenStreetMap's Nominatim service.

**Note:** This sends coordinates to a third party. Requests are rate-limited to 1/second (per Nominatim policy) and cached.

```bash
# OPSEC: Disable geocoding entirely (raw GPS only, no third-party request)
python3 MetaDetective.py -d ./loot/ --no-geocode

# Use self-hosted Nominatim server
python3 MetaDetective.py -d ./loot/ --nominatim-url https://nominatim.example.com
```

| Flag | Default | Description |
|------|---------|-------------|
| `--no-geocode` | off (geocoding on) | Disable reverse geocoding |
| `--nominatim-url` | public OSM server | Base URL of custom Nominatim server |

---

## Display Modes

### Singular (Default)

Aggregates all unique values per field across every file. Best for OSINT: "who touched these documents?"

```bash
# Default: deduplicated singular view
python3 MetaDetective.py -d ./loot/

# With formatted style (vertical list with markers)
python3 MetaDetective.py -d ./loot/ --format formatted

# With concise style (comma-separated on one line)
python3 MetaDetective.py -d ./loot/ --format concise
```

### All (Per-File)

One block per file with individual metadata. Best for forensic analysis.

```bash
python3 MetaDetective.py -d ./loot/ --display all
```

**Note:** `--format` only works with `--display singular`. Using `--format` with `--display all` produces an error.

---

## Use Cases for Political Monitoring

### Campaign Document Analysis
- Extract authorship from leaked opposition documents
- Identify software/tools used by campaign teams
- Track document creation timelines

### Social Media Intelligence
- Extract GPS data from campaign photos
- Verify location claims from polling station images
- Map event locations from supporter uploads

### Website Reconnaissance
- Scrape opposition party websites for downloadable materials
- Download and analyze PDFs, brochures, manifestos
- Build identity profiles from document metadata

### Email Leak Analysis
- Extract sender/recipient data from EML/MSG files
- Identify internal hostnames and infrastructure
- Map organizational relationships

---

## Practice Lab

Test MetaDetective on the project's own site (hosts metadata-rich sample documents):

```bash
# Scrape and download
python3 MetaDetective.py https://franckferman.github.io/MetaDetective/

# Analyze results
python3 MetaDetective.py ./loot/ --summary
```

You'll recover planted identities, emails, tools, and GPS coordinates.

---

## Security Notes

- **HTML Export:** All metadata values are HTML-escaped. Malicious metadata cannot inject scripts into reports.
- **OPSEC:** Use `--no-geocode` to prevent GPS coordinates from leaving your machine.
- **Rate Limiting:** Web scraping includes configurable rate limits and thread controls.
- **Legal:** Provided for educational and authorized security testing. Ensure compliance with applicable laws.

---

## License

AGPL-3.0

---

## Contact

- **Author:** Franck Ferman
- **Email:** contact@franckferman.fr
- **LinkedIn:** https://www.linkedin.com/in/franckferman
- **Twitter:** https://www.twitter.com/franckferman

---

## Quick Reference Card

```bash
# Install
curl -O https://raw.githubusercontent.com/franckferman/MetaDetective/stable/src/MetaDetective/MetaDetective.py

# Basic analysis
python3 MetaDetective.py ./loot/

# Summary stats
python3 MetaDetective.py -d ./loot/ --summary

# Scrape website
python3 MetaDetective.py https://target.com/

# Export to HTML
python3 MetaDetective.py -d ./loot/ -e html

# GPS-only extraction (no geocoding)
python3 MetaDetective.py -d ./photos/ -t heic --parse-only 'GPS Position' --no-geocode
```
