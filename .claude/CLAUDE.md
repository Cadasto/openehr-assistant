# Claude Code Instructions

@../AGENTS.md is the canonical guide for this repository — what it is, the
`make` targets, the layout, and the silent failure modes worth knowing. Follow it.

## Claude-specific notes

- **Docker-only (WSL2 on Windows):** never run `mkdocs` or `python` on the host.
  Everything goes through the `make docs-*` targets, which run the pinned
  `squidfunk/mkdocs-material` image.
- This repository holds **no product code**. A change to a tool, skill or install
  step belongs in `openehr-assistant-mcp` or `openehr-assistant-plugin`.
- Commit with [Conventional Commits](https://www.conventionalcommits.org/) and a
  scope (`docs:`, `feat(site):`, `fix(ci):`).
