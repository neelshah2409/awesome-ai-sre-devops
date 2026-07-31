#!/usr/bin/env python3
"""
Parses the markdown tables in README.md into docs/data.json, which powers
the searchable/filterable site in docs/index.html.

README.md stays the single source of truth — this script just makes it
consumable by the static site. Runs automatically in CI on every push to
main that touches README.md (see .github/workflows/build-site-data.yml).

Run locally:
    python scripts/generate_site_data.py
"""

import json
import re

README_PATH = "README.md"
OUTPUT_PATH = "docs/data.json"

# Only these ## sections are treated as tool categories (others, like
# "Contents" or "Learning Resources", are skipped or handled separately).
CATEGORY_HEADING_RE = re.compile(r"^## (.+)$")
SKIP_SECTIONS = {
    "Contents",
    "Quick Picks by Use Case",
    "Tool of the Month",
    "How This Stays Updated",
    "Contributing",
    "License",
    "Learning Resources",
}

# Matches: - **[Name](url)** — *Type.* Description text.
# Falls back to a simpler pattern for MCP-server-style entries with no *Type.* tag:
# - [Name](url) — Description text.
ROW_RE = re.compile(
    r"^-\s*\*\*\[([^\]]+)\]\(([^)]+)\)\*\*\s*—\s*\*([^*]+)\.\*\s*(.+)$"
)
ROW_RE_NO_TYPE = re.compile(
    r"^-\s*\*\*\[([^\]]+)\]\(([^)]+)\)\*\*\s*—\s*(.+)$"
)


def parse_readme(text: str):
    lines = text.splitlines()
    categories = []
    current = None

    for line in lines:
        heading_match = CATEGORY_HEADING_RE.match(line)
        if heading_match:
            name = heading_match.group(1).strip()
            if name in SKIP_SECTIONS:
                current = None
                continue
            current = {"name": name, "tools": []}
            categories.append(current)
            continue

        if current is None:
            continue

        stripped = line.strip()
        row_match = ROW_RE.match(stripped)
        if row_match:
            tool_name, url, tool_type, desc = row_match.groups()
            current["tools"].append(
                {
                    "name": tool_name.strip(),
                    "url": url.strip(),
                    "type": tool_type.strip(),
                    "description": desc.strip(),
                }
            )
            continue

        # MCP-server-style entries have no *Type.* tag — infer "Open-source"
        # since virtually all MCP servers are open-source; description text
        # follows the em dash directly.
        fallback_match = ROW_RE_NO_TYPE.match(stripped)
        if fallback_match:
            tool_name, url, desc = fallback_match.groups()
            current["tools"].append(
                {
                    "name": tool_name.strip(),
                    "url": url.strip(),
                    "type": "Open-source",
                    "description": desc.strip(),
                }
            )

    # Drop empty categories (e.g. a table whose header row slipped through).
    categories = [c for c in categories if c["tools"]]
    return categories


def main():
    with open(README_PATH, "r", encoding="utf-8") as f:
        text = f.read()

    categories = parse_readme(text)
    total_tools = sum(len(c["tools"]) for c in categories)

    output = {
        "categories": categories,
        "total_tools": total_tools,
        "total_categories": len(categories),
    }

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2)

    print(f"Wrote {total_tools} tools across {len(categories)} categories to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
