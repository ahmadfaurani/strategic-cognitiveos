#!/usr/bin/env python3
"""
CognitiveOS ID Resolver (D8 precondition — DEC-20260909-005)
============================================================
Resolves an identifier to a canonical record path, with canonical/alias
resolution parity:

  - canonical id  → record file (primary key, direct)
  - alias handle  → the single record declaring it (single hop; aliases never
                    resolve to other aliases — no chains)

Usage:
  python3 tools/resolve_id.py <identifier>              # resolve one id
  python3 tools/resolve_id.py --parity                  # verify every declared
                                                        # alias resolves to exactly
                                                        # one record (parity proof)
  python3 tools/resolve_id.py --parity --quiet          # machine mode
Exit 0 = resolved / parity holds · exit 1 = unresolved / parity violated.
"""
import os
import re
import sys
from pathlib import Path

DEFAULT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RECORD_DIRS = ("actions", "assessments", "briefings", "commitments", "decisions",
               "documents", "drafts", "engagements", "initiatives", "intelligence",
               "lessons", "opportunities", "organizations", "outcomes", "risks",
               "stakeholders", "artifacts")


def _fm_field(fm_lines, key):
    for i, l in enumerate(fm_lines):
        if l.startswith(f"{key}:"):
            v = l.split(":", 1)[1].strip()
            if v.startswith("["):
                return [x.strip().strip("\"'") for x in v.strip("[]").split(",") if x.strip()]
            if v:
                return v
            vals = []
            for l2 in fm_lines[i + 1:]:
                mt = re.match(r"^\s*-\s(.*)$", l2)
                if mt:
                    vals.append(mt.group(1).strip().strip("\"'"))
                else:
                    break
            return vals
    return None


def build_index(root):
    """canonical id → path · alias → path (single-hop only). Raises on unreadable files (no silent skips)."""
    canonical, alias = {}, {}
    for d in RECORD_DIRS:
        base = Path(root) / d
        if not base.is_dir():
            continue
        for p in sorted(base.glob("*.md")):
            try:
                txt = p.read_text(encoding="utf-8")
            except Exception as e:
                raise RuntimeError(f"unreadable record {p}: {e}")  # no silent skips — parity must be honest
            if not txt.startswith("---"):
                continue
            lines = txt.split("\n")
            try:
                end = lines[1:].index("---") + 1
            except ValueError:
                continue
            fm = lines[1:end]
            rid = _fm_field(fm, "id")
            if not rid or rid in canonical:
                continue
            rel = str(p.relative_to(root))
            canonical[rid] = rel
            al = _fm_field(fm, "aliases")
            if isinstance(al, list):
                for a in al:
                    if isinstance(a, str) and a and a != rid:
                        alias.setdefault(a, []).append(rel)
    return canonical, alias


def resolve(identifier, canonical, alias):
    """Return (path, resolution_kind) or (None, None). Aliases are single-hop."""
    if identifier in canonical:
        return canonical[identifier], "canonical"
    hits = alias.get(identifier, [])
    if len(hits) == 1:
        return hits[0], "alias"
    if len(hits) > 1:
        return hits, "ambiguous"
    return None, None


def main():
    root = Path(sys.argv[sys.argv.index("--root") + 1]) if "--root" in sys.argv else Path(DEFAULT_ROOT)
    canonical, alias = build_index(root)
    quiet = "--quiet" in sys.argv

    if "--parity" in sys.argv:
        bad = []
        for a, owners in sorted(alias.items()):
            if len(owners) != 1:
                bad.append((a, owners))
            elif owners[0] not in canonical.values():
                bad.append((a, f"unresolved target {owners[0]}"))
        if bad:
            print("❌ PARITY VIOLATIONS:", len(bad))
            for a, o in bad:
                print(f"   alias `{a}` → {o}")
            sys.exit(1)
        if not quiet:
            print(f"✅ Resolution parity: {len(alias)} alias handle(s), each resolving to exactly one canonical record; "
                  f"{len(canonical)} canonical ids indexed")
        sys.exit(0)

    ident = sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith("--") else None
    if not ident:
        print(__doc__)
        sys.exit(2)
    path, kind = resolve(ident, canonical, alias)
    if path is None:
        print(f"❌ UNRESOLVED: {ident}")
        sys.exit(1)
    if kind == "alias" or kind == "canonical":
        print(f"{kind}: {ident} → {path}")
        sys.exit(0)
    print(f"❌ AMBIGUOUS: {ident} → {path}")
    sys.exit(1)


if __name__ == "__main__":
    main()
