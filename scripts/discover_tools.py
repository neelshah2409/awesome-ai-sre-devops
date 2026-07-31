#!/usr/bin/env python3
"""
Weekly discovery script for the Awesome AI SRE & DevOps list.

What it does:
1. Queries the GitHub Search API for repos matching a set of topic/keyword
   queries relevant to AI + DevOps/SRE (e.g. topic:ai-sre, "kubernetes ai agent").
2. Sorts by recently-updated + stars to surface things gaining traction.
3. Skips anything whose repo URL already appears in README.md.
4. Writes the remaining candidates to CANDIDATES.md for human review.

This script never edits README.md directly and never merges anything —
it only proposes. A maintainer reviews CANDIDATES.md in the PR the
discover-tools.yml workflow opens, and folds the good ones into README.md
by hand (or with an editor's one-line description).

Run locally:
    GITHUB_TOKEN=ghp_xxx python scripts/discover_tools.py
"""

import os
import re
import sys
import time
from datetime import datetime, timedelta

import requests

README_PATH = "README.md"
OUTPUT_PATH = "CANDIDATES.md"

# Search queries — tune these over time as the space evolves.
SEARCH_QUERIES = [
    "topic:ai-sre",
    "topic:ai-devops",
    "topic:llmops",
    "topic:aiops",
    "topic:mcp-server devops",
    "kubernetes ai agent in:name,description",
    "ai incident response in:description",
    "ai root cause analysis in:description",
]

MIN_STARS = 20
LOOKBACK_DAYS = 180  # only consider repos pushed to within this window


def get_headers():
    token = os.environ.get("GITHUB_TOKEN")
    headers = {"Accept": "application/vnd.github+json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers


def already_listed(repo_url: str, readme_text: str) -> bool:
    # Normalize trailing slash / case for a simple substring check.
    return repo_url.rstrip("/").lower() in readme_text.lower()


def search_github(query: str, headers: dict) -> list:
    url = "https://api.github.com/search/repositories"
    params = {
        "q": f"{query} stars:>={MIN_STARS}",
        "sort": "updated",
        "order": "desc",
        "per_page": 15,
    }
    resp = requests.get(url, headers=headers, params=params, timeout=30)
    if resp.status_code == 403:
        print(f"Rate limited on query '{query}', skipping.", file=sys.stderr)
        return []
    resp.raise_for_status()
    return resp.json().get("items", [])


def main():
    headers = get_headers()

    if not os.path.exists(README_PATH):
        print("README.md not found — run this from the repo root.", file=sys.stderr)
        sys.exit(1)

    with open(README_PATH, "r", encoding="utf-8") as f:
        readme_text = f.read()

    cutoff = datetime.utcnow() - timedelta(days=LOOKBACK_DAYS)
    seen_repos = set()
    candidates = []

    for query in SEARCH_QUERIES:
        items = search_github(query, headers)
        time.sleep(2)  # be polite to the API / avoid secondary rate limits

        for repo in items:
            html_url = repo["html_url"]
            if html_url in seen_repos:
                continue
            seen_repos.add(html_url)

            if already_listed(html_url, readme_text):
                continue

            pushed_at = datetime.strptime(repo["pushed_at"], "%Y-%m-%dT%H:%M:%SZ")
            if pushed_at < cutoff:
                continue

            candidates.append(
                {
                    "name": repo["full_name"],
                    "url": html_url,
                    "description": (repo.get("description") or "").strip(),
                    "stars": repo["stargazers_count"],
                    "matched_query": query,
                    "pushed_at": repo["pushed_at"][:10],
                }
            )

    # Sort by stars descending for easier triage.
    candidates.sort(key=lambda c: c["stars"], reverse=True)

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write("# Candidate tools — weekly discovery run\n\n")
        f.write(
            f"Generated {datetime.utcnow().strftime('%Y-%m-%d')}. "
            f"{len(candidates)} candidates not yet in README.md.\n\n"
        )
        f.write(
            "Review each one: does it fit an existing category? Is it "
            "actively maintained and genuinely relevant (not just star-farming)? "
            "Move the keepers into README.md with a one-line description in "
            "your own words, then delete this file.\n\n"
        )
        f.write("| Repo | Stars | Last push | Matched query | Description |\n")
        f.write("|---|---|---|---|---|\n")
        for c in candidates:
            desc = c["description"].replace("|", "-")[:140]
            f.write(
                f"| [{c['name']}]({c['url']}) | {c['stars']} | {c['pushed_at']} "
                f"| `{c['matched_query']}` | {desc} |\n"
            )

    print(f"Wrote {len(candidates)} candidates to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
