# Contributing

The openEHR Assistant is built across a few small repositories rather than one
large one. Each is independently useful, and each has its own issues and
releases.

## The repositories

| Repository | What lives there |
|------------|------------------|
| [openehr-assistant-mcp](https://github.com/cadasto/openehr-assistant-mcp) | The MCP server — tools, prompts, resources, and the bundled guide and example corpus |
| [openehr-assistant-plugin](https://github.com/cadasto/openehr-assistant-plugin) | The user-facing plugin — skills, agents, commands, hooks and rules |
| [openehr-assistant](https://github.com/cadasto/openehr-assistant) | This website. Documentation only; no product code |
| [openehr-assistant-dev-plugin](https://github.com/cadasto/openehr-assistant-dev-plugin) | Maintainer tooling — authoring skills for guides, prompts and MCP tools, plus the release workflow |
| [plugin-marketplace](https://github.com/cadasto/plugin-marketplace) | The Cadasto marketplace that serves the plugin |

Start with the server if you want to add domain knowledge — a guide, an example,
a tool. Start with the plugin if you want to change how a workflow is *driven*.

## How the server is specified

The server repository follows a lightweight **Specification-Driven
Development** process. The specification is the source of truth, not a
description written afterwards:

- **Requirements** carry stable `REQ-F#` / `REQ-N#` identifiers and state *what*
  the system must do.
- **Architecture** maps components to those requirements — the *how*.
- **Decision records** capture the *why*, and are immutable once merged; a
  decision is changed by superseding it, never by editing history.
- **Traceability** links requirement ↔ code ↔ test ↔ decision in a machine-
  readable map.

That map is enforced. A `spec-check` gate fails the build on a missing artefact,
a dangling path, or disagreement between the index and the map — so the
documentation cannot quietly rot away from the code. Plans, the only place
checkbox task lists live, are archived once their work lands.

If you add or move a requirement, a capability class, or its test, update the
traceability map in the same change.

## Working on the server

The runtime is **Docker-only** — there is no host PHP or Composer, by decision
rather than by accident, so every maintainer gets the same environment.

```bash
make up-dev      # start the dev containers
make install     # install Composer dependencies inside the container
make ci          # spec-check + PHPStan + PHPUnit
make conformance # the official MCP conformance suite
```

Tests mock external HTTP: the CKM API is never called live, so the suite is
deterministic and works offline.

## Working on the site

This repository is deliberately thin. It holds the pages, the theme, and a build
— nothing that duplicates the product repositories.

```bash
make sync   # pull the products' canonical install docs at their pinned refs
make check  # strict build, then assert the published output is complete
make serve  # preview on http://127.0.0.1:8000
```

Install prose is never copied here. It is fetched at build time from each
product repository at a ref pinned in `sources.json`, so a single source stays
authoritative. Bump the ref there when a release changes its instructions.

## Conventions across the repositories

- [Conventional Commits](https://www.conventionalcommits.org/) with a scope —
  `feat(tools):`, `fix(resources):`, `docs:`.
- Feature branches and pull requests; validation runs on every push.
- Content that describes an openEHR standard is retrieved from the published
  specifications, never written from memory.
- Guides are written for AI consumption: short, scannable, and specific.

## Clinical modelling standards

Contributions touching archetypes, templates or modelling guidance are held to
openEHR's own principles: two-level modelling, single-concept archetypes, no
workflow or UI concerns inside archetypes, and reuse and semantic correctness
ahead of application convenience.
