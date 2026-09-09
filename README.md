# openEHR Assistant — website

> **Documentation only.** This repository builds the public website. It contains
> no product code. The software it documents lives in
> [openehr-assistant-mcp](https://github.com/cadasto/openehr-assistant-mcp)
> (the MCP server) and
> [openehr-assistant-plugin](https://github.com/cadasto/openehr-assistant-plugin)
> (the Claude Code / Cursor plugin). Please open product issues there.

**→ [cadasto.github.io/openehr-assistant](https://cadasto.github.io/openehr-assistant/)**

## Build it locally

Docker is the only requirement — no Python, no MkDocs install.

```bash
make serve   # preview on http://127.0.0.1:8000
make check   # strict build + output checks (CI's verify-site job)
make help    # all targets
```

## How it stays accurate

Install instructions are **not copied** here, and neither is the brand layer —
the CSS, landing template, footer partial and company mark shared across
Cadasto's sites. Both are fetched at build time, the install prose from the
product repositories and the brand layer from
[docs-theme](https://github.com/Cadasto/docs-theme), each at a ref pinned in
[`sources.json`](sources.json), so there is only ever one authoritative copy.
Bump that source's `ref` when a release should land on this site.

Contributing notes and the site's own conventions are in
[AGENTS.md](AGENTS.md).

## Licence

MIT — see [LICENSE](LICENSE).
