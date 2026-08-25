# Claude Code Instructions

@../AGENTS.md is the canonical guide for this repository — what it is, the
`make` targets, the layout, and the silent failure modes worth knowing. Follow it.

## Claude-specific notes

- **Docker-only (WSL2 on Windows):** never run `mkdocs` or `python` on the host.
  Everything goes through the `make` targets (`sync`, `build`, `check`, `serve`,
  `clean`), which run the pinned `squidfunk/mkdocs-material` image.
- This repository holds **no product code**. A change to a tool, skill or install
  step belongs in `openehr-assistant-mcp` or `openehr-assistant-plugin`.
- **Copy and SEO work comes from the `docs-editing` plugin**, installed from the
  Cadasto marketplace — `/copy-editing`, `/marketing-copy`, `/seo-audit` and
  `/ai-seo`. Nothing is vendored into `.claude/skills/` any more; there is
  nothing to fetch. Its claims rule (no invented statistics, testimonials or
  superlatives — describe the mechanism instead) and `AGENTS.md`'s grounding
  rule point the same way, and `AGENTS.md` wins where they differ.
- Commit with [Conventional Commits](https://www.conventionalcommits.org/) and a
  scope (`docs:`, `feat(site):`, `fix(ci):`).
