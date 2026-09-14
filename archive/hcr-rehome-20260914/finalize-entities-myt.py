#!/usr/bin/env python3
"""Finalize entity extraction output with correct MYT timestamp."""
import json
from pathlib import Path

ENTITIES_DIR = Path("/home/p62operator/.openclaw/workspace-hoi/intelligence/entities")
SRC = ENTITIES_DIR / "2026-07-30T000759Z_entities_extracted.json"

# Actual MYT timestamp from: TZ=Asia/Kuala_Lumpur date '+%Y-%m-%d %H:%M %Z'
MYT_FULL = "2026-07-30 14:00 +08"
MYT_FILE = "20260730-1400"
MYT_DATE = "2026-07-30"

with open(SRC, "r", encoding="utf-8") as f:
    data = json.load(f)

# --- Clean false-positive LOCATION entities (dynamic N\d constituency regex noise) ---
NOISE_LOCATIONS = {
    "N95 and diesel prices up ",
    "N95 dan diesel tanpa subsidi naik ",
    "N97 and diesel will be increased by ",
    "N9 Polls",
}
removed = [l for l in data["entities"]["LOCATION"] if l in NOISE_LOCATIONS]
data["entities"]["LOCATION"] = sorted([l for l in data["entities"]["LOCATION"] if l not in NOISE_LOCATIONS])

entity_counts = {k: len(v) for k, v in data["entities"].items()}
total_entities = sum(entity_counts.values())
data["extraction_summary"]["entity_counts"] = entity_counts
data["extraction_summary"]["total_entities"] = total_entities

data["extraction_timestamp"] = MYT_FULL
data["extraction_timestamp_myt"] = MYT_FULL
data["report_date"] = MYT_DATE
data["timezone"] = "Asia/Kuala_Lumpur (MYT, UTC+8)"
data["cleanup_notes"] = {
    "removed_false_positive_locations": removed,
    "reason": "Dynamic N\\d constituency regex matched diesel-price/mask strings (N95/N97) and an event reference (N9 Polls).",
}

out_json = ENTITIES_DIR / (MYT_FILE + "_entities.json")
with open(out_json, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

type_order = ["PERSON", "ORGANIZATION", "LOCATION", "EVENT", "CONCEPT"]
sb = data["source_breakdown"]
pir_defs = data["pir_keywords_loaded"]
pir_matches = data["pir_analysis"]

# --- Build report ---
lines = []
def A(s=""):
    lines.append(s)

A("# Entity Extraction Report — HOI Political Intelligence")
A("")
A("**Classification:** TLP:AMBER")
A("")
A("| Field | Value |")
A("|---|---|")
A("| Generated | " + MYT_FULL + " (MYT) |")
A("| Report Date | " + MYT_DATE + " |")
A("| Brief ID | ENT-" + MYT_FILE + " |")
A("| Collection Cycle | " + data["source_timestamp"] + " |")
A("| Source Collection | `" + data["source_collection"] + "` |")
A("| Skill Used | " + data["skill_used"] + " |")
A("| PIR Source | `" + data["pir_source"] + "` |")
A("| PIRs Defined | 10 (PIR-1 … PIR-10) |")
A("")
A("---")
A("")
A("## 1. Executive Summary")
A("")
A("Entity extraction was run against the previous collection cycle "
  "(`" + data["source_timestamp"] + "`, 25-source OPERATIONAL collection) using the "
  "**entity-extraction** skill methodology: pre-collected entity fields "
  "(coalitions / politicians / candidates / constituencies / events / hot_seats), "
  "knowledge-base pattern matching, and dynamic regex extraction (titled names, "
  "constituency N## codes, event patterns). Extracted entities were matched against "
  "the 10 Priority Intelligence Requirements (PIRs) defined in "
  "`/home/p62operator/tools/deer-flow/backend/config.yaml`.")
A("")
cs = data["extraction_summary"]["collection_stats"]
A("- **Sources processed:** " + str(cs["total_sources"]) + " (" + str(cs["successful"]) + " success / " + str(cs["failed"]) + " failed)")
A("- **Total entities extracted:** " + str(total_entities))
pc = data["extraction_summary"]["pir_coverage"]
A("- **PIR coverage:** " + str(pc["pirs_with_matches"]) + "/10 (" + str(pc["coverage_percentage"]) + "%)")
A("")
A("### Entity Counts by Category")
A("")
A("| Category | Count |")
A("|---|---|")
for t in type_order:
    A("| " + t + " | " + str(entity_counts[t]) + " |")
A("| **TOTAL** | **" + str(total_entities) + "** |")
A("")
A("> Cleanup note: " + str(len(removed)) + " false-positive LOCATION entries removed "
  "(dynamic `N\\d` constituency regex matched diesel-price/mask strings). Removed: "
  + ", ".join(repr(x) for x in removed) + ".")
A("")
A("---")
A("")
A("## 2. Extracted Entities")
A("")
for t in type_order:
    ents = data["entities"][t]
    A("### " + t + " (" + str(len(ents)) + ")")
    A("")
    A("```")
    for e in ents:
        A("- " + e)
    A("```")
    A("")
A("---")
A("")
A("## 3. PIR Matching Analysis")
A("")
A("Each PIR's keywords were searched (word-boundary, case-insensitive) across the full content + headlines of all 25 sources. The table below shows which PIRs registered keyword hits this cycle.")
A("")
A("| PIR | Keywords (from config.yaml) | Matched Keywords | Status |")
A("|---|---|---|---|")
for pir_id in sorted(pir_defs.keys()):
    kws = pir_defs[pir_id]
    matched = pir_matches.get(pir_id, [])
    status = "ACTIVE" if matched else "DORMANT"
    mk = ", ".join(matched) if matched else "—"
    A("| " + pir_id + " | " + ", ".join(kws) + " | " + mk + " | " + status + " |")
A("")
A("### PIRs with Matches (Active)")
A("")
if pir_matches:
    for pir_id in sorted(pir_matches.keys()):
        A("**" + pir_id + "** — matched: " + ", ".join(pir_matches[pir_id]))
        A("")
else:
    A("No PIRs registered matches this cycle.")
    A("")
A("### Interpretation")
A("")
A("- **PIR-2 (BERSAMA / third force):** ACTIVE — `BERSAMA` detected. The new coalition/party signal remains present in coverage (MalaysiaGazette).")
A("- **PIR-4 (BN Johor / UMNO / opposition):** ACTIVE — `UMNO` detected across multiple sources (Sinar Harian, Utusan Malaysia, Free Malaysia Today).")
A("- **PIR-7 (Onn Hafiz / 56 seats / solo bid):** ACTIVE — `Onn Hafiz` detected (CodeBlue). The Johor MB-centric signal persists.")
A("- **PIR-1, PIR-3, PIR-5, PIR-6, PIR-8, PIR-9, PIR-10: DORMANT** this cycle — no keyword hits. Notable absences: no `defection`, `Rafizi`, `INVOKE`, `seat negotiation`, `Sabah PKR`, `GRB` signal in this collection window.")
A("")
A("---")
A("")
A("## 4. Source Breakdown (by entity yield)")
A("")
A("| Source | Entities | Intel Score | Pol. Headlines | PIRs Hit |")
A("|---|---|---|---|---|")
for s in sorted(sb, key=lambda x: sum(x["entities_found"].values()), reverse=True):
    tot = sum(s["entities_found"].values())
    pirhit = ", ".join(s.get("pir_matches", {}).keys()) if s.get("pir_matches") else "—"
    A("| " + str(s["source"]) + " | " + str(tot) + " | " + str(s.get("intelligence_score", "—")) + " | " + str(s.get("political_headlines_count", "—")) + " | " + pirhit + " |")
A("")
A("---")
A("")
A("## 5. Deliverables")
A("")
A("- Entities JSON: `" + out_json.name + "`")
A("- Raw extraction (UTC, collection-timestamped): `" + SRC.name + "`")
A("- This report: `" + MYT_FILE + "_entities_report.md`")
A("")
A("---")
A("")
A("*Generated by Hermes Agent cron job using the entity-extraction skill. Timestamp: " + MYT_FULL + " (Asia/Kuala_Lumpur, MYT/UTC+8).*")

report_path = ENTITIES_DIR / (MYT_FILE + "_entities_report.md")
with open(report_path, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print("=== FINALIZATION COMPLETE ===")
print("Entities JSON: " + str(out_json))
print("Report MD:    " + str(report_path))
print("Cleaned locations removed: " + str(len(removed)))
print("Final counts: " + str(entity_counts) + "  (total " + str(total_entities) + ")")
