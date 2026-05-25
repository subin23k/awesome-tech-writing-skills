#!/usr/bin/env python3
"""Validate readme.md conventions for awesome-tech-writing-skills."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import urldefrag


ENTRY_RE = re.compile(r"^- \[([^\]]+)\]\(([^)]+)\): (.+)$")
HEADING_RE = re.compile(r"^## (.+)$")

EXPECTED_SECTIONS = [
    "Agent & LLM Skills",
    "AI Prompt Libraries",
    "Best Practices",
    "Tools",
]


def normalize_name(name: str) -> str:
    return re.sub(r"\s+", " ", name).casefold()


def main() -> int:
    path = Path(sys.argv[1] if len(sys.argv) > 1 else "readme.md")
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    errors: list[str] = []

    sections: dict[str, list[tuple[int, str, str]]] = {
        section: [] for section in EXPECTED_SECTIONS
    }
    current: str | None = None
    urls: dict[str, int] = {}

    for idx, line in enumerate(lines, start=1):
        heading = HEADING_RE.match(line)
        if heading:
            current = heading.group(1)
            continue

        if not line.startswith("- "):
            continue

        if current == "Contents":
            continue

        if current not in sections:
            continue

        match = ENTRY_RE.match(line)
        if not match:
            errors.append(f"Line {idx}: entry must match '- [Name](URL): Description'.")
            continue

        name, url, description = match.groups()
        clean_url = urldefrag(url.strip())[0]

        sections[current].append((idx, name, url))

        if clean_url in urls:
            errors.append(f"Line {idx}: duplicate URL also appears on line {urls[clean_url]}.")
        else:
            urls[clean_url] = idx

        if not description.strip():
            errors.append(f"Line {idx}: description is empty.")
        if any(word in description.casefold() for word in ["ultimate", "best-in-class", "revolutionary"]):
            errors.append(f"Line {idx}: description appears promotional.")

    for section in EXPECTED_SECTIONS:
        if f"## {section}" not in text:
            errors.append(f"Missing section: {section}")
            continue

        entries = sections[section]
        names = [name for _, name, _ in entries]
        sorted_names = sorted(names, key=normalize_name)
        if names != sorted_names:
            expected = ", ".join(sorted_names)
            actual = ", ".join(names)
            errors.append(
                f"Section '{section}' is not alphabetized. "
                f"Actual: {actual}. Expected: {expected}."
            )

    if errors:
        print("README validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"{path} passed README validation.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
