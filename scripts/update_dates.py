#!/usr/bin/env python3
"""
Update "Last Updated" badges for each project entry in README.md.

For each ## [Name](url) entry, finds the GitHub repo URL and fetches
the latest push date via the GitHub API, then inserts/updates a
shields.io badge on the entry's tagline line.

Usage:
    python scripts/update_dates.py [--readme README.md] [--dry-run] [--token TOKEN]
"""

import argparse
import os
import re
import sys
import time
from datetime import datetime, timezone

import requests

# --- Patterns ---
ENTRY_HEADING = re.compile(r'^(## \[.+?\]\((.+?)\))\s*$', re.MULTILINE)
GITHUB_URL = re.compile(r'https://github\.com/([a-zA-Z0-9._-]+/[a-zA-Z0-9._-]+)')
GITHUB_LINK = re.compile(r'-\s*\[GitHub\]\((https://github\.com/[^\)]+)\)')
BADGE_PATTERN = re.compile(r'\s*!\[Last Updated\]\(https://img\.shields\.io/badge/Last%20Updated-[^)]+\)')


def extract_github_repo(heading_url: str, details_block: str) -> str | None:
    """Extract owner/repo from heading URL or details block GitHub link."""
    # Prefer heading URL if it's a GitHub URL
    m = GITHUB_URL.match(heading_url.rstrip('/'))
    if m:
        parts = m.group(1).split('/')
        return f"{parts[0]}/{parts[1]}"

    # Fall back to GitHub link inside details
    m = GITHUB_LINK.search(details_block)
    if m:
        gm = GITHUB_URL.match(m.group(1).rstrip('/'))
        if gm:
            parts = gm.group(1).split('/')
            return f"{parts[0]}/{parts[1]}"

    return None


def get_pushed_at(owner_repo: str, token: str | None, retried: bool = False) -> str | None:
    """Fetch pushed_at for a GitHub repo. Returns ISO 8601 string or None."""
    headers = {"Accept": "application/vnd.github+json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"

    try:
        resp = requests.get(
            f"https://api.github.com/repos/{owner_repo}",
            headers=headers,
            timeout=15,
        )
    except requests.RequestException as e:
        print(f"  WARNING: network error for {owner_repo}: {e}", file=sys.stderr)
        return None

    if resp.status_code == 200:
        return resp.json().get("pushed_at")
    elif resp.status_code == 404:
        print(f"  WARNING: {owner_repo} not found (deleted/private)", file=sys.stderr)
        return None
    elif resp.status_code == 403 and not retried:
        reset = int(resp.headers.get("X-RateLimit-Reset", time.time() + 60))
        wait = max(reset - int(time.time()), 1)
        print(f"  Rate limited. Sleeping {wait}s...", file=sys.stderr)
        time.sleep(wait)
        return get_pushed_at(owner_repo, token, retried=True)
    else:
        print(f"  WARNING: unexpected status {resp.status_code} for {owner_repo}", file=sys.stderr)
        return None


def make_badge(date_str: str) -> str:
    encoded = date_str.replace(" ", "%20")
    return f"![Last Updated](https://img.shields.io/badge/Last%20Updated-{encoded}-blue)"


def format_date(pushed_at: str) -> str:
    dt = datetime.fromisoformat(pushed_at.replace("Z", "+00:00"))
    return dt.strftime("%b %Y")


def find_tagline_line(lines: list[str], start: int) -> int | None:
    """Find index of tagline line: first non-empty, non-details line after heading."""
    i = start + 1
    while i < len(lines):
        line = lines[i].strip()
        if line and not line.startswith('<details') and not line.startswith('##'):
            return i
        if line.startswith('##'):
            return None  # next entry started, no tagline
        i += 1
    return None


def process_readme(content: str, token: str | None, dry_run: bool) -> str:
    lines = content.splitlines(keepends=True)

    # Find all entry headings: (line_index, heading_url)
    entries = []
    for i, line in enumerate(lines):
        m = ENTRY_HEADING.match(line.rstrip('\n'))
        if m:
            entries.append((i, m.group(2)))

    total = len(entries)
    updated = 0
    skipped_no_url = 0
    errors = 0

    for idx, (line_idx, heading_url) in enumerate(entries):
        # Collect details block: lines between this heading and next
        next_line = entries[idx + 1][0] if idx + 1 < len(entries) else len(lines)
        details_block = ''.join(lines[line_idx + 1:next_line])

        owner_repo = extract_github_repo(heading_url, details_block)
        if not owner_repo:
            skipped_no_url += 1
            continue

        print(f"[{idx+1}/{total}] {owner_repo}", end=" ... ", flush=True)
        pushed_at = get_pushed_at(owner_repo, token)

        if pushed_at is None:
            errors += 1
            print("skipped")
            continue

        date_str = format_date(pushed_at)
        badge = make_badge(date_str)

        tagline_idx = find_tagline_line(lines, line_idx)
        if tagline_idx is None:
            errors += 1
            print("no tagline found")
            continue

        tagline = lines[tagline_idx].rstrip('\n')
        # Remove existing badge if present
        tagline_clean = BADGE_PATTERN.sub('', tagline)
        new_tagline = f"{tagline_clean} {badge}\n"

        if dry_run:
            if lines[tagline_idx] != new_tagline:
                print(f"WOULD UPDATE:\n  - {lines[tagline_idx].rstrip()}\n  + {new_tagline.rstrip()}")
            else:
                print("no change")
        else:
            lines[tagline_idx] = new_tagline
            print(date_str)

        updated += 1

    print(f"\nDone. Updated: {updated}/{total} | No GitHub URL: {skipped_no_url} | Errors: {errors}")
    return ''.join(lines)


def main():
    parser = argparse.ArgumentParser(description="Update last-updated badges in README.md")
    parser.add_argument("--readme", default="README.md", help="Path to README.md")
    parser.add_argument("--dry-run", action="store_true", help="Print changes without writing")
    parser.add_argument("--token", default=os.environ.get("GITHUB_TOKEN"), help="GitHub API token")
    args = parser.parse_args()

    if not args.token:
        print("WARNING: No GITHUB_TOKEN set. Unauthenticated rate limit is 60 req/hr.", file=sys.stderr)

    with open(args.readme, encoding="utf-8") as f:
        content = f.read()

    new_content = process_readme(content, args.token, args.dry_run)

    if not args.dry_run:
        with open(args.readme, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Wrote {args.readme}")


if __name__ == "__main__":
    main()
