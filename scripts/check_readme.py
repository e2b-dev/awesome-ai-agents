#!/usr/bin/env python3
"""Check structural integrity of the Awesome AI Agents README."""

from __future__ import annotations

import re
import sys
from pathlib import Path

PROJECT_HEADING = re.compile(
    r"^## \[(?P<name>[^\]]+)\]\((?P<url>https?://.+)\)\s*$"
)
MALFORMED_MARKDOWN_URL = re.compile(r"\]\(https?:(?!//)[^)]+\)", re.IGNORECASE)
EMPTY_LIST_ITEM = re.compile(r"^\s*[-*+]\s*$")
CATEGORY_HEADING = re.compile(r"^### Category\s*$")
DETAILS_TAG = re.compile(r"</?details\b[^>]*>", re.IGNORECASE)


def _without_html_comments(text: str) -> str:
    """Blank HTML comments while preserving source line numbers."""
    return re.sub(
        r"<!--.*?-->",
        lambda match: "".join("\n" if char == "\n" else " " for char in match.group()),
        text,
        flags=re.DOTALL,
    )


def _project_headings(lines: list[str]) -> list[tuple[int, str, str]]:
    headings = []
    for line_number, line in enumerate(lines, start=1):
        match = PROJECT_HEADING.match(line)
        if match:
            headings.append(
                (line_number, match.group("name").strip(), match.group("url").strip())
            )
    return headings


def validate_readme_text(text: str) -> list[str]:
    """Return structural README issues; an empty list means the checks pass."""
    visible_text = _without_html_comments(text)
    lines = visible_text.splitlines()
    issues: list[str] = []

    for line_number, line in enumerate(lines, start=1):
        if EMPTY_LIST_ITEM.match(line):
            issues.append(f"line {line_number}: empty list item")
        if MALFORMED_MARKDOWN_URL.search(line):
            issues.append(f"line {line_number}: Markdown URL is missing // after its scheme")

    headings = _project_headings(lines)
    names: dict[str, int] = {}
    urls: dict[str, int] = {}
    for line_number, name, url in headings:
        normalized_name = name.casefold()
        normalized_url = url.rstrip("/").casefold()
        if normalized_name in names:
            issues.append(
                f"line {line_number}: duplicate project name {name!r} "
                f"(first listed on line {names[normalized_name]})"
            )
        else:
            names[normalized_name] = line_number
        if normalized_url in urls:
            issues.append(
                f"line {line_number}: duplicate project URL {url!r} "
                f"(first listed on line {urls[normalized_url]})"
            )
        else:
            urls[normalized_url] = line_number

    for index, (line_number, name, _url) in enumerate(headings):
        end = headings[index + 1][0] - 1 if index + 1 < len(headings) else len(lines)
        category_lines = [
            candidate
            for candidate in range(line_number, end + 1)
            if CATEGORY_HEADING.match(lines[candidate - 1])
        ]
        if len(category_lines) > 1:
            issues.append(
                f"line {category_lines[1]}: project {name!r} repeats its Category section "
                f"(first on line {category_lines[0]})"
            )

    stack: list[int] = []
    fence: tuple[str, int] | None = None
    for line_number, line in enumerate(lines, start=1):
        fence_match = re.match(r"^\s*(`{3,}|~{3,})", line)
        if fence is None and fence_match:
            marker = fence_match.group(1)
            fence = (marker[0], len(marker))
            continue
        if fence is not None:
            marker, minimum_length = fence
            closing_fence = re.match(
                rf"^\s*{re.escape(marker)}{{{minimum_length},}}\s*$", line
            )
            if closing_fence:
                fence = None
            continue
        for tag in DETAILS_TAG.finditer(line):
            if tag.group().startswith("</"):
                if stack:
                    stack.pop()
                else:
                    issues.append(f"line {line_number}: unmatched </details> tag")
            else:
                stack.append(line_number)
    for line_number in stack:
        issues.append(f"line {line_number}: <details> tag is not closed")

    return issues


def main() -> int:
    readme_path = Path(__file__).resolve().parents[1] / "README.md"
    issues = validate_readme_text(readme_path.read_text(encoding="utf-8"))
    if issues:
        print("README integrity check failed:")
        for issue in issues:
            print(f"- {issue}")
        return 1

    visible_text = _without_html_comments(readme_path.read_text(encoding="utf-8"))
    entry_count = len(_project_headings(visible_text.splitlines()))
    print(f"README integrity check passed ({entry_count} project entries).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
