"""Placeholder linter for the discovery + SOW kit.

    python validate.py                   # check every .md under examples/
    python validate.py path/to/my-sow.md # check one file (use this on your drafts)

Flags angle-bracket placeholders like `<client name>`, `<date>`, `<deliverable>`
that you forgot to fill in. Exit code 0 if clean, 1 if any remain — suitable
for a pre-send gate so half-finished SOWs don't reach a client.
"""

from __future__ import annotations

import glob
import re
import sys

PLACEHOLDER = re.compile(r"<[^<>\n]{1,80}>")

# Tags that look like placeholders but aren't (HTML / Mermaid / Markdown).
ALLOW = {
    "<br>", "<br/>", "<br />", "<details>", "</details>",
    "<summary>", "</summary>", "<html>", "</html>",
}


def lint(path: str) -> list[tuple[int, str]]:
    out: list[tuple[int, str]] = []
    with open(path, encoding="utf-8") as fh:
        for ln, line in enumerate(fh, 1):
            for m in PLACEHOLDER.finditer(line):
                text = m.group(0)
                if text.lower() in ALLOW:
                    continue
                if text.startswith("<!--"):
                    continue
                if text.startswith("<https://") or text.startswith("<http://"):
                    continue
                out.append((ln, text))
    return out


def main(argv: list[str]) -> int:
    files = argv if argv else sorted(glob.glob("examples/*.md"))
    if not files:
        print("No files to check (no examples/*.md and no path provided).")
        return 0

    total = 0
    for path in files:
        try:
            issues = lint(path)
        except FileNotFoundError:
            print(f"SKIP {path}: not found")
            continue
        if issues:
            print(f"\n{path}: {len(issues)} unfilled placeholder(s)")
            for ln, text in issues[:15]:
                print(f"  line {ln}: {text}")
            if len(issues) > 15:
                print(f"  ... and {len(issues) - 15} more")
            total += len(issues)
        else:
            print(f"OK   {path}")

    print(f"\n{total} placeholder(s) total.")
    return 0 if total == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
