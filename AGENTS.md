# AGENTS.md

## Project Overview

**Documentation only**: the MkDocs site for the openEHR Assistant, published at
<https://cadasto.github.io/openehr-assistant/> (human pitch: [README.md](README.md)).
No product code lives here; the two products it documents are developed elsewhere:

- [Cadasto/openehr-assistant-mcp](https://github.com/Cadasto/openehr-assistant-mcp): the MCP server
- [Cadasto/openehr-assistant-plugin](https://github.com/Cadasto/openehr-assistant-plugin): the Claude Code / Cursor plugin

A change to a tool, a skill or an install step belongs in that product's repository.

## Domain Context

- **Do not duplicate product documentation.** Link to it, or fetch it through
  `sources.json`. Two copies drift; that is why this repository exists separately.
- Statements about openEHR must be grounded in the published specifications or
  in the product repositories, never written from model memory.
- Inventories on `pages/features.md` mirror real repository contents; verify
  counts and names against the source repos before editing them.

## Repository Layout

| Path | Role |
|------|------|
| `pages/` | The site's `docs_dir`: every published page, `stylesheets/` (fetched brand CSS), `assets/` (product logo plus the fetched company mark), and `llms.txt` / `robots.txt` |
| `overrides/main.html` | Product JSON-LD; stays here. `home.html` and `partials/copyright.html` are fetched |
| `scripts/sync_sources.py` | Fetches install docs into `.fetched/` and the brand layer onto live paths |
| `scripts/check_brand_paths.py` | Run by `make check`: asserts `sources.json`, `.gitignore` and `THEME_FETCHED` in the `Makefile` list the same brand paths |
| `sources.json` | Pinned refs for the product install docs **and** `Cadasto/docs-theme` |
| `mkdocs.yml` | Theme, nav, strict mode, validation and the web-font URL |
| `.github/workflows/` | `ci.yml` (PR gate) and `docs-site.yml` (deploy) |
| `.vale.ini`, `styles/config/vocabularies/Cadasto/` | Prose lint config and tracked vocabulary; the rest of `styles/` is downloaded |
| `.fetched/`, `site/`, `.cache/` | Generated; all gitignored. Fetched brand files are gitignored too |

## Development

Docker-only (WSL2 on Windows): never run `mkdocs` or `python` on the host; the
`make` targets run the pinned `squidfunk/mkdocs-material` image.

```bash
make sync         # fetch pinned install docs and the docs-theme brand layer
make sync-offline # reuse the cached copies instead of fetching
make build        # strict build to site/
make check        # build + assert the published output is complete (the CI gate)
make serve        # preview on http://127.0.0.1:8000
make clean        # remove site/, .fetched/, fetched brand files and .cache/
```

`build` and `serve` both depend on `sync`, so a plain `make serve` is enough.

`ci.yml` also runs `prose`, a [Vale](https://vale.sh) lint of the Markdown that
gates on errors only and is **not** required before merge; warnings and
suggestions are a backlog. Vale is the one host binary, so there is no `make`
target. Install it, then run what CI runs (`.vale.ini` documents each rule):

```bash
vale sync
vale --minAlertLevel=error --glob='!{.fetched,site,styles}/**' .
```

### Commit Messages

[Conventional Commits](https://www.conventionalcommits.org/) with a scope:
`docs:`, `feat(site):`, `fix(ci):`.

### Branching

Feature branches and pull requests. `ci.yml` runs `verify-site` (`make check`)
on every pull request whose base is `main`; that check is required before merge.
`docs-site.yml` builds and deploys on pushes to `main` and on a weekly schedule.

## Gotchas

These are the failure modes this site has actually hit. Most are silent.

- **`docs_dir` is `pages/`.** Anything outside it is never published. The product
  logo and the fetched brand CSS / mark live in `pages/stylesheets/` and
  `pages/assets/` for that reason; moving them out builds green and 404s in
  production.
- **Theme colour variables must be scoped to the active scheme's selector
  (`[data-md-color-scheme="slate"]` dark, `="default"` light), not `:root`.**
  The theme declares them on `<body>`, which beats a value inherited from
  `:root`, so on `:root` they are silently discarded. Both schemes ship (a header
  toggle switches them), so the fetched `tokens.css` defines the semantic tokens
  in both blocks; brand-constant colours stay on `:root` because nothing on
  `<body>` shadows them. `--md-text-font-family` is the same bug: the theme
  composes it on `body`. `Roboto` still renders (via `--md-text-font` on
  `:root`), but the brand fallback chain (`Helvetica, Arial, Lucida`) becomes
  Material's `-apple-system` path, so `tokens.css` re-declares it on `body`.
- **`strict: true` is set in `mkdocs.yml`, not passed on the command line**, so
  local and CI builds cannot diverge. Any MkDocs warning fails the build.
- **Strict mode cannot see everything.** A missing `extra_css` target or a link
  emitted by a *template* produces no warning at all. That is why `check` greps
  the built output; extend those assertions rather than trusting the exit code.
- **Never edit install prose or the brand layer here.** `pages/install.md`
  includes `.fetched/*.md` via snippets. Brand CSS, `home.html`, the copyright
  partial and the company mark are written by `make sync` from
  `Cadasto/docs-theme`. Change those in their own repositories; bump the
  matching `ref` in `sources.json` to pick up a release.
- **The docs-theme `ref` is a commit hash, not a tag**, so a moved tag cannot
  change the published site. Resolve a release tag with the command in the
  `sources.json` comment; `ref_tag` is documentation only.
- **The web-font URL in `mkdocs.yml` is a contract with docs-theme.** Its weight
  list must match the weights the fetched CSS uses, so a `theme.ref` bump can
  require a URL change: a dropped weight gets a synthesised face. `check`
  asserts the Fira Sans 500 and 700 faces were localised.
- **Fetched links are rewritten at fetch time, not by a MkDocs hook**: a hook
  only sees the `--8<--` include line, never the included text.
- **The build needs network access** for the source sync and for the `privacy`
  plugin, which downloads and self-hosts the web fonts. `make sync-offline`
  reuses the cached `.fetched/` and last fetched brand files, but only if
  `make clean` has not run since: `clean` removes them, and the brand files are not
  tracked, so `git checkout` cannot bring them back.
- **Icons are `:material-xxx:` shortcodes**, rendered as inline SVG from the
  theme's bundled set. No sprite sheet, no third-party request. Verify a name
  exists before using it, or the build fails.
