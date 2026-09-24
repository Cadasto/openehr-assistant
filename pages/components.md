---
description: >-
  The openEHR Assistant has two parts: an MCP server that supplies openEHR
  knowledge and tools, and a plugin that decides when to use them. What each one
  is, how they connect, and where their code and documentation live.
---

# Components

The openEHR Assistant has two parts: an **MCP server** that supplies openEHR
knowledge and tools, and a **plugin** that decides when to use them. This page
describes each part, how the two connect, and where their code and
documentation live.

!!! note "Pre-release"
    Expect frequent updates and breaking changes until version 1.0.

## MCP server

The knowledge and tooling layer. It exposes openEHR domain knowledge to AI
assistants over the [Model Context Protocol](https://modelcontextprotocol.io/),
so an agent can discover, explain, design, and review openEHR artefacts.

!!! info "Not a clinical data repository"
    This is a knowledge and authoring-assistance server. It reads
    specifications, published archetypes and its own guide corpus, and it never
    stores patient data.

| | |
|---|---|
| **Hosted endpoint** | `https://openehr-assistant-mcp.apps.cadasto.com/` |
| **Transport** | `streamable-http`, or `stdio` when run locally |
| **Runtime** | PHP 8.4, Docker-only |
| **Works with** | Any MCP client, including Claude Desktop, Claude Code, Cursor, and LibreChat |

It provides tools, guided prompts, readable `openehr://` resources, and argument
completions. [Features](features.md) lists them all.

| | |
|---|---|
| **Repository** | [Cadasto/openehr-assistant-mcp](https://github.com/Cadasto/openehr-assistant-mcp) |
| **Capability reference** | [Available MCP elements](https://github.com/Cadasto/openehr-assistant-mcp#available-mcp-elements) |
| **Contributor docs** | [docs/](https://github.com/Cadasto/openehr-assistant-mcp/tree/main/docs): requirements, architecture, decisions, testing |

## Plugin

The workflow layer, for [Claude Code](https://claude.ai/code) and
[Cursor](https://cursor.com). The server answers questions; the plugin decides
which questions to ask, in what order, and with which guidance loaded.

It adds skills that trigger on intent, subagents for delegated retrieval,
explicit slash commands, and hooks that keep openEHR conventions in view.
[Features](features.md) lists the inventory.

| | |
|---|---|
| **Repository** | [Cadasto/openehr-assistant-plugin](https://github.com/Cadasto/openehr-assistant-plugin) |
| **Install guide** | [docs/install.md](https://github.com/Cadasto/openehr-assistant-plugin/blob/main/docs/install.md): install, update, MCP permissions, Cursor |

## How they fit together

The plugin bundles a `.mcp.json` that registers the hosted server under the name
`openehr-assistant`. Use that same name if you also configure the server by hand,
or you end up with two entries pointing at one endpoint.

To aim the plugin at a local or stdio server instead, follow
[MCP wiring](https://github.com/Cadasto/openehr-assistant-plugin/blob/main/docs/install.md#mcp-wiring)
in the plugin repository; [Install](install.md) has the server URLs and
per-client configuration.

You can use the server on its own with any MCP client. The plugin needs a
server to talk to.

## Maintainer tooling

A third, separate plugin,
[openehr-assistant-dev](https://github.com/Cadasto/openehr-assistant-dev-plugin),
supports building tools, guides, or examples *for* these repositories. It is
for maintainers, not clinical end users; see [Contributing](contributing.md).
