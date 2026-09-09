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
make sync         # fetch pinned install docs and the docs-theme brand layer
make sync-offline # reuse the cached copies instead of fetching
make build        # strict build → site/
make check        # build + assert the published output is complete (CI's verify-site job)
make serve        # preview on http://127.0.0.1:8000
make clean        # remove site/, .fetched/, fetched brand files and .cache/
```

`build` and `serve` both depend on `sync`, so a plain `make serve` is enough to
get started.

## Layout

| Path | Role |
|------|------|
| `pages/` | The site's `docs_dir` — every published page, `stylesheets/` (fetched brand CSS), `assets/` (product logo plus the fetched company mark), and `llms.txt` / `robots.txt` |
| `overrides/main.html` | Product JSON-LD; stays here. Landing and copyright templates are fetched |
| `scripts/sync_sources.py` | Fetches install docs into `.fetched/` and the brand layer onto live paths |
| `sources.json` | Pinned refs for the product install docs **and** `Cadasto/docs-theme` |
| `mkdocs.yml` | Theme, nav, strict mode and validation |
| `.fetched/`, `site/`, `.cache/` | Generated; all gitignored. Fetched brand files are gitignored too |

## Gotchas

These are the failure modes this site has actually hit. Most are silent.

- **`docs_dir` is `pages/`.** Anything outside it is never published. The product
  logo and the fetched brand CSS / mark live in `pages/stylesheets/` and
  `pages/assets/` for that reason — moving them out builds green and 404s in
  production.
- **Theme colour variables must be scoped to the active scheme's selector
  (`[data-md-color-scheme="slate"]` for dark, `="default"` for light), not
  `:root`.** The theme declares them on `<body>`, and a value on `<body>` beats
  one inherited from `:root`. On `:root` they are silently discarded. The site
  ships both schemes (a header toggle switches them), so the fetched
  `tokens.css` defines the semantic tokens in both blocks; brand-constant
  colours stay on `:root` because nothing on `<body>` shadows those names.
  `--md-text-font-family` is the same class of bug: the theme composes it on
  `body`, so a `:root` value loses to it. The page still renders `Roboto` —
  `tokens.css` sets `--md-text-font` on `:root` and the theme's composition
  reads it — but the brand fallback chain (`Helvetica, Arial, Lucida`) is
  replaced by Material's `-apple-system` path. The fetched `tokens.css`
  therefore re-declares the composed name on `body`; if that ever needs
  changing, change it in `Cadasto/docs-theme`.
- **`strict: true` is set in `mkdocs.yml`, not passed on the command line**, so
  local and CI builds cannot diverge. Any MkDocs warning fails the build.
- **Strict mode cannot see everything.** A missing `extra_css` target or a link
  emitted by a *template* produces no warning at all. That is why `check`
  greps the built output — extend those assertions rather than trusting the
  build's exit code alone.
- **Never edit install prose or the brand layer here.** `pages/install.md`
  includes `.fetched/*.md` via snippets. Brand CSS, `home.html`, the copyright
  partial and the company mark are written by `make sync` from
  `Cadasto/docs-theme`. Change those in their own repositories; bump the
  matching `ref` in `sources.json` to pick up a release.
- **Fetched links are rewritten at fetch time, not by a MkDocs hook** — a hook
  only sees the `--8<--` include line, never the included text.
- **The build needs network access** for the source sync and for the `privacy`
  plugin, which downloads and self-hosts the web fonts. `make sync-offline`
  reuses the cached `.fetched/` and the last fetched brand files instead — but
  only if `make clean` has not run since, because `clean` removes both those
  caches and the fetched brand layer, and the brand files are no longer tracked
  so `git checkout` cannot bring them back.
- **Icons are `:material-xxx:` shortcodes**, rendered as inline SVG from the
  theme's bundled set. No sprite sheet, no third-party request. Verify a name
  exists before using it, or the build fails.

## Conventions

- [Conventional Commits](https://www.conventionalcommits.org/) with a scope —
  `docs:`, `feat(site):`, `fix(ci):`.
- Feature branches and pull requests. `ci.yml` builds and verifies the site on
  every pull request whose base is `main` — that check, `verify-site`, is
  required before merge. `docs-site.yml` builds and deploys on pushes to `main`.
- `ci.yml` also runs `prose`, a [Vale](https://vale.sh) lint of the Markdown that
  gates on errors only and is **not** required before merge; warnings and
  suggestions are a backlog. Vale is the one host binary in an otherwise
  Docker-only toolchain, so there is no `make` target — install it, then run what
  CI runs:

  ```bash
  vale sync
  vale --minAlertLevel=error --glob='!{.fetched,site,styles}/**' .
  ```

  `.vale.ini` documents each rule choice; the vocabulary in
  `styles/config/vocabularies/Cadasto/` is tracked, the packages are not.
- **Do not duplicate product documentation.** Link to it, or fetch it through
  `sources.json`. Two copies of the same prose will drift — that is the reason
  this repository exists separately.
- Statements about openEHR must be grounded in the published specifications or
  in the product repositories, never written from model memory.
- Inventories on `pages/features.md` mirror real repository contents. Verify
  against the source repos before editing counts or names — they rot quickly.
