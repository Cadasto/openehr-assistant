#!/usr/bin/env python3
"""Fetch pinned install docs and the Cadasto brand layer.

Install prose from the product repositories lands in `.fetched/`. Brand files
from `Cadasto/docs-theme` land on their live paths (`extra_css`, `custom_dir`,
`docs_dir/assets`). Copying either here would guarantee drift, so both are
pulled at build time from a pinned ref — `sources.json` is the single place a
version is named.

Rewriting of install Markdown happens here rather than in a MkDocs hook on
purpose: a hook sees the `--8<--` include line, not the included text, so it
could never fix links inside fetched content. Doing it at fetch time is also
deterministic and testable.

Usage:
    python3 scripts/sync_sources.py            # fetch, fail if unreachable
    python3 scripts/sync_sources.py --offline  # reuse cached copies
"""

from __future__ import annotations

import argparse
import json
import posixpath
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG = ROOT / "sources.json"
OUT_DIR = ROOT / ".fetched"

RAW = "https://raw.githubusercontent.com/{repo}/{ref}/{path}"
BLOB = "https://github.com/{repo}/blob/{ref}/{path}"

#: A relative Markdown link: not absolute, not an anchor, not a mail link.
RELATIVE_LINK = re.compile(
    r"\]\("
    r"(?!https?:|mailto:|#|/)"
    r"([^)\s#]+)"
    r"(#[^)\s]*)?"
    r"\)"
)

HEADING = re.compile(r"^(#{1,6})(\s+)", re.MULTILINE)
FENCE = re.compile(r"^(```|~~~)")


def fetch_bytes(url: str, timeout: int = 20) -> bytes:
    with urllib.request.urlopen(url, timeout=timeout) as response:
        if response.status != 200:
            raise RuntimeError(f"{url} returned HTTP {response.status}")
        return response.read()


def fetch(url: str, timeout: int = 20) -> str:
    return fetch_bytes(url, timeout=timeout).decode("utf-8")


def _fail_fetch(url: str, error: Exception, offline: bool) -> int:
    print(f"sync: cannot fetch {url}\n      {error}", file=sys.stderr)
    if not offline:
        print(
            "      re-run with --offline to build from a cached copy.",
            file=sys.stderr,
        )
    return 1


def sync_theme(theme: dict, offline: bool) -> int:
    """Write each brand file onto the path MkDocs actually reads."""
    repo, ref = theme["repo"], theme["ref"]
    for item in theme["files"]:
        dest_rel = Path(item["dest"])
        if dest_rel.is_absolute() or ".." in dest_rel.parts:
            raise SystemExit(
                f"sync: theme dest {item['dest']!r} must be a relative path "
                f"under the repository root."
            )
        dest = ROOT / dest_rel
        url = RAW.format(repo=repo, ref=ref, path=item["path"])
        try:
            data = fetch_bytes(url)
        except (urllib.error.URLError, RuntimeError, TimeoutError) as error:
            if offline and dest.exists():
                print(f"  ! theme/{item['path']}: unreachable, reusing cached copy ({error})")
                continue
            return _fail_fetch(url, error, offline)
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(data)
        print(f"  ✓ theme/{item['path']}  ←  {repo}@{ref}:{item['path']}")
    return 0


def absolutise_links(text: str, repo: str, ref: str, doc_path: str) -> str:
    """Point every relative link at the source repository on GitHub.

    Relative targets resolve against the document's own directory in that repo,
    not against this site, so they must be rewritten or they 404 once published.
    """
    doc_dir = posixpath.dirname(doc_path)

    def rewrite(match: re.Match) -> str:
        target, anchor = match.group(1), match.group(2) or ""
        resolved = posixpath.normpath(posixpath.join(doc_dir, target))
        if resolved.startswith(".."):
            raise SystemExit(
                f"sync: {repo}:{doc_path} links to {target!r}, which escapes the "
                f"repository root — cannot rewrite to a GitHub URL."
            )
        return "](" + BLOB.format(repo=repo, ref=ref, path=resolved) + anchor + ")"

    return RELATIVE_LINK.sub(rewrite, text)


def shift_headings(text: str, levels: int) -> str:
    """Demote headings so fetched content nests under this site's own sections.

    Fenced code is skipped — a `#` comment inside a shell block is not a heading.
    """
    if levels <= 0:
        return text
    out, in_fence = [], False
    for line in text.splitlines(keepends=True):
        if FENCE.match(line):
            in_fence = not in_fence
        if not in_fence:
            line = HEADING.sub(
                lambda m: "#" * min(len(m.group(1)) + levels, 6) + m.group(2), line
            )
        out.append(line)
    return "".join(out)


def drop_leading_heading(text: str) -> str:
    """Remove the source document's own title; this site supplies the framing."""
    lines = text.splitlines(keepends=True)
    for i, line in enumerate(lines):
        if line.strip():
            if line.lstrip().startswith("#"):
                return "".join(lines[i + 1 :]).lstrip("\n")
            break
    return text


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--offline",
        action="store_true",
        help="reuse an existing .fetched/ copy instead of failing when offline",
    )
    args = parser.parse_args()

    config = json.loads(CONFIG.read_text())
    OUT_DIR.mkdir(exist_ok=True)

    for source in config["sources"]:
        name, repo, ref, path = (
            source["name"], source["repo"], source["ref"], source["path"],
        )
        destination = OUT_DIR / f"{name}.md"
        url = RAW.format(repo=repo, ref=ref, path=path)

        try:
            text = fetch(url)
        except (urllib.error.URLError, RuntimeError, TimeoutError) as error:
            if args.offline and destination.exists():
                print(f"  ! {name}: unreachable, reusing cached copy ({error})")
                continue
            return _fail_fetch(url, error, args.offline)

        if source.get("drop_first_heading"):
            text = drop_leading_heading(text)
        text = absolutise_links(text, repo, ref, path)
        text = shift_headings(text, source.get("heading_shift", 0))

        destination.write_text(
            f"<!-- Fetched from {repo}@{ref}:{path} by scripts/sync_sources.py."
            f" Do not edit; edit it in that repository. -->\n\n{text}"
        )
        print(f"  ✓ {name}  ←  {repo}@{ref}:{path}")

    theme = config.get("theme")
    if theme:
        result = sync_theme(theme, args.offline)
        if result != 0:
            return result

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
