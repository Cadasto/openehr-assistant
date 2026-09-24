---
description: >-
  How the openEHR Assistant is built across several small repositories, which
  one owns what, and where to open an issue or a pull request for each.
---

# Contributing

This page is for anyone who wants to change the openEHR Assistant: which
repository owns what, how the server is specified and built, and how this
website is built. The assistant is spread across a few small repositories
rather than one large one. Each is independently useful, and each has its own
issues and releases.

## The repositories

| Repository | What lives there |
|------------|------------------|
| [openehr-assistant-mcp](https://github.com/Cadasto/openehr-assistant-mcp) | The MCP server: tools, prompts, resources, and the bundled guide and example corpus |
| [openehr-assistant-plugin](https://github.com/Cadasto/openehr-assistant-plugin) | The user-facing plugin: skills, agents, commands, hooks, and rules |
| [openehr-assistant](https://github.com/Cadasto/openehr-assistant) | This website. Documentation only; no product code |
| [openehr-assistant-dev-plugin](https://github.com/Cadasto/openehr-assistant-dev-plugin) | Maintainer tooling: authoring skills for guides, prompts, and MCP tools, plus the release workflow |
| [plugin-marketplace](https://github.com/Cadasto/plugin-marketplace) | The Cadasto marketplace that serves the plugin |
| [docs-theme](https://github.com/Cadasto/docs-theme) | The brand layer this site fetches: CSS, landing template, footer partial, and company mark |

Start with the server if you want to add domain knowledge, such as a guide, an
example, or a tool. Start with the plugin if you want to change how a workflow is *driven*.

## How the server is specified

The server repository follows a lightweight **Specification-Driven
Development** process. The specification is the source of truth, and the code
is checked against it:

- **Requirements** carry stable `REQ-F#` / `REQ-N#` identifiers and state *what*
  the system must do.
- **Architecture** maps components to those requirements: the *how*.
- **Decision records** capture the *why*, and are immutable once merged; a
  decision is changed by superseding it, never by editing history.
- **Traceability** links requirement ↔ code ↔ test ↔ decision in a
  machine-readable map.

That map is enforced. A `spec-check` gate fails the build on a missing artefact,
a dangling path, or disagreement between the index and the map, so drift
between the map and the tree stops the build. Plans, the only place
checkbox task lists live, are archived once their work lands.

If you add or move a requirement, a capability class, or its test, update the
traceability map in the same change.

## Working on the server

The runtime is **Docker-only**: there is no host PHP or Composer, a choice
recorded in the server's
[ADR-0004](https://github.com/Cadasto/openehr-assistant-mcp/blob/main/docs/decisions/0004-docker-only-runtime.md),
so every maintainer gets the same environment.

```bash
make up-dev      # start the dev containers
make install     # install Composer dependencies inside the container
make ci          # spec-check + PHPStan + PHPUnit
make conformance # the official MCP conformance suite
```

Tests mock external HTTP: the CKM API is never called live, so the suite is
deterministic and works offline.

## Working on the site

This repository is deliberately thin. It holds the pages, the product's own
template override, and a build. The shared brand layer (the CSS, landing
template, footer partial, and company mark used across Cadasto's sites) lives in
[docs-theme](https://github.com/Cadasto/docs-theme) and is fetched, never
edited here.

```bash
make sync   # pull install docs and the brand layer at their pinned refs
make check  # strict build, then assert the published output is complete
make serve  # preview on http://127.0.0.1:8000
```

Install prose is not copied here either. It is fetched at build time from each
product repository at a ref pinned in `sources.json`, so a single source stays
authoritative. Bump the ref there when a release changes its instructions.

The brand CSS, the landing template, the footer partial, and the company mark
are fetched the same way, at the commit pinned in `theme.ref`. That one is a
commit rather than a tag because two of those files are templates the build
executes, so a moved tag could change the published site with nothing here
recording it.

## Conventions across the repositories

- [Conventional Commits](https://www.conventionalcommits.org/) with a scope,
  such as `feat(tools):`, `fix(resources):`, or `docs:`.
- Feature branches and pull requests; every pull request is validated before it
  can be merged.
- Content that describes an openEHR standard is retrieved from the published
  specifications, never written from memory.
- Guides are written for AI consumption: short, scannable, and specific.

## Clinical modelling standards

Contributions touching archetypes, templates, or modelling guidance are held to
openEHR's own principles: two-level modelling, single-concept archetypes, no
workflow or UI concerns inside archetypes, and reuse and semantic correctness
ahead of application convenience.
