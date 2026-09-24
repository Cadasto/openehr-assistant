# openEHR Assistant website

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Material for MkDocs](https://img.shields.io/badge/Material_for_MkDocs-9.7.6-526CFE?logo=materialformkdocs&logoColor=white)](https://squidfunk.github.io/mkdocs-material/)

This repository builds the public website for the openEHR Assistant, published at
**[cadasto.github.io/openehr-assistant](https://cadasto.github.io/openehr-assistant/)**.
It is for contributors who change the site's pages or its build. It holds the
pages in `pages/`, the product's own template override, the MkDocs
configuration, and the checks that assert the published output is complete.

The repository is documentation only and contains no product code. The software
it documents lives in
[openehr-assistant-mcp](https://github.com/cadasto/openehr-assistant-mcp)
(the MCP server) and
[openehr-assistant-plugin](https://github.com/cadasto/openehr-assistant-plugin)
(the Claude Code / Cursor plugin); please open product issues there. Install
instructions and the shared brand layer are not copied here either: the build
fetches them from the repositories that own them (see
[How it stays accurate](#how-it-stays-accurate)).

**Requirements.** Docker; there is no host Python and no MkDocs install to set
up. The build needs network access to fetch the pinned sources and the web
fonts. The optional prose lint needs [Vale](https://vale.sh) on the host.

## Table of contents

- [Building the site](#building-the-site)
- [How it stays accurate](#how-it-stays-accurate)
- [Contributing](#contributing)
- [License](#license)

## Building the site

```bash
make serve   # preview on http://127.0.0.1:8000
make check   # strict build + output checks (CI's verify-site job)
make help    # all targets
```

## How it stays accurate

Install instructions are **not copied** here, and neither is the brand layer:
the CSS, landing template, footer partial, and company mark shared across
Cadasto's sites. The build fetches both, the install prose from the product
repositories and the brand layer from
[docs-theme](https://github.com/Cadasto/docs-theme), each at a ref pinned in
[`sources.json`](sources.json), so there is only ever one authoritative copy.
Bump that source's `ref` when a release should land on this site.

## Contributing

Contributing notes and the site's own conventions are in
[AGENTS.md](AGENTS.md).

## License

[MIT License](LICENSE)
