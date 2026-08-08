# AI Guidelines: openEHR Assistant website

This repository is **documentation only**. It builds the public website for the
openEHR Assistant at <https://cadasto.github.io/openehr-assistant/>.

No product code lives here. The two things the site documents are developed
elsewhere:

- [cadasto/openehr-assistant-mcp](https://github.com/cadasto/openehr-assistant-mcp) — the MCP server
- [cadasto/openehr-assistant-plugin](https://github.com/cadasto/openehr-assistant-plugin) — the Claude Code / Cursor plugin

If a change belongs to a product — a tool, a skill, an install step — make it in
that product's repository, not here.

## Commands

Docker-only; no host Python, and no MkDocs install needed.

```bash
make sync    # fetch the product repos' canonical docs (refs pinned in sources.json)
make build   # strict build → site/
make check   # build + assert the published output is complete (what CI runs)
make serve   # preview on http://127.0.0.1:8000
make clean   # remove site/, .fetched/ and .cache/
```

`build` and `serve` both depend on `sync`, so a plain `make serve` is enough to
get started.

## Layout

| Path | Role |
|------|------|
| `pages/` | The site's `docs_dir` — every published page, plus `stylesheets/` and `assets/` |
| `overrides/home.html` | Landing-page template; strips the theme chrome for a full-bleed page |
| `scripts/sync_sources.py` | Fetches and rewrites the product repos' docs into `.fetched/` |
| `sources.json` | Which document is pulled from which repo, **at which pinned ref** |
| `mkdocs.yml` | Theme, nav, strict mode and validation |
| `.fetched/`, `site/`, `.cache/` | Generated; all gitignored |

## Gotchas

These are the failure modes this site has actually hit. Most are silent.

- **`docs_dir` is `pages/`.** Anything outside it is never published. The brand
  stylesheet and logo live in `pages/stylesheets/` and `pages/assets/` for that
  reason — moving them out builds green and 404s in production.
- **Theme colour variables must be scoped to `[data-md-color-scheme="slate"]`,
  not `:root`.** The theme declares them on `<body>`, and a value on `<body>`
  beats one inherited from `:root`. On `:root` they are silently discarded.
- **`strict: true` is set in `mkdocs.yml`, not passed on the command line**, so
  local and CI builds cannot diverge. Any MkDocs warning fails the build.
- **Strict mode cannot see everything.** A missing `extra_css` target or a link
  emitted by a *template* produces no warning at all. That is why `check`
  greps the built output — extend those assertions rather than trusting the
  build's exit code alone.
- **Never edit install prose here.** `pages/install.md` includes
  `.fetched/*.md` via snippets. To change that text, change it in the product
  repository; to pick up a change, bump the `ref` in `sources.json`.
- **Fetched links are rewritten at fetch time, not by a MkDocs hook** — a hook
  only sees the `--8<--` include line, never the included text.
- **The build needs network access** for the source sync and for the `privacy`
  plugin, which downloads and self-hosts the web fonts. Use
  `python3 scripts/sync_sources.py --offline` to build from a cached `.fetched/`.
- **Icons are `:material-xxx:` shortcodes**, rendered as inline SVG from the
  theme's bundled set. No sprite sheet, no third-party request. Verify a name
  exists before using it, or the build fails.

## Conventions

- [Conventional Commits](https://www.conventionalcommits.org/) with a scope —
  `docs:`, `feat(site):`, `fix(ci):`.
- Feature branches and pull requests. `ci.yml` builds and verifies the site on
  every pull request whose base is `main` — that check, `verify-site`, is
  required before merge. `docs-site.yml` builds and deploys on pushes to `main`.
- **Do not duplicate product documentation.** Link to it, or fetch it through
  `sources.json`. Two copies of the same prose will drift — that is the reason
  this repository exists separately.
- Statements about openEHR must be grounded in the published specifications or
  in the product repositories, never written from model memory.
- Inventories on `pages/features.md` mirror real repository contents. Verify
  against the source repos before editing counts or names — they rot quickly.
