---
# The <title> tag only, not the H1 and not the nav label (mkdocs.yml sets that).
# Without it the homepage title is just the site name, which spends the most
# valuable string on the site saying nothing a searcher would type.
title: openEHR MCP server and Claude Code plugin
description: >-
  Design archetypes, constrain templates and write AQL with an assistant that
  looks the answer up in CKM and the published openEHR specifications — an MCP
  server and a plugin for Claude Code and Cursor.
hide:
  - navigation
  - toc
template: home.html
---

<div class="home-hero" markdown="1">

![](assets/logo.svg){ .home-hero__mark }

# openEHR Assistant

<p class="home-tagline">
Design archetypes, constrain templates and write AQL with an assistant that looks the answer up in CKM and the published specifications.
</p>

<div class="home-cta" markdown="1">

[Get started](install.md){ .md-button .md-button--primary }
[View on GitHub](https://github.com/cadasto/openehr-assistant-mcp){ .md-button }

</div>

</div>

<h2 class="section-title">Why openEHR Assistant?</h2>

<div class="features-grid" markdown="1">

<div class="feature-card" markdown="1">

:material-toolbox:

### MCP-native tools
Search and retrieval for CKM, guides, examples, terminology, and type specifications — ready for any MCP client.

</div>

<div class="feature-card" markdown="1">

:material-book-open-variant:

### Guide-first workflows
Bundled implementation guides ground each answer; task prompts orchestrate multi-step modelling and review.

</div>

<div class="feature-card" markdown="1">

:material-database-search:

### CKM integration
Search and retrieve archetypes and templates from the Clinical Knowledge Manager with relevance scoring.

</div>

<div class="feature-card" markdown="1">

:material-shield-check:

### Spec-aligned content
Type specs, digests, and terminology are grounded in authoritative openEHR sources — not model memory.

</div>

<div class="feature-card" markdown="1">

:material-server-network:

### Managed or self-hosted
Use Cadasto's endpoint, or run your own instance over streamable HTTP or stdio.

</div>

<div class="feature-card" markdown="1">

:material-puzzle:

### Plugin skills layer
Pair the server with the user-facing plugin for skills, commands, and agents that guide clinical modelling.

</div>

</div>

<h2 class="section-title">Two parts, one workflow</h2>

<div class="two-products" markdown="1">

<div class="product-card" markdown="1">

:material-server:

### MCP Server
The knowledge and tooling layer: tools, prompts, resources, and completions. Connect once from Claude Desktop, Cursor, LibreChat, or any MCP client.

[What it provides](features.md){ .md-button }

</div>

<div class="product-card" markdown="1">

:material-toy-brick:

### Plugin
The workflow layer for Claude Code and Cursor: skills, slash commands, and subagents that know when to load guides and call MCP tools.

[What it adds](features.md){ .md-button }

</div>

</div>

<div class="quick-start" markdown="1">

## Quick Start

Point your MCP client at the hosted server:

```json
{
  "mcpServers": {
    "openehr-assistant-mcp": {
      "type": "streamable-http",
      "url": "https://openehr-assistant-mcp.apps.cadasto.com/"
    }
  }
}
```

[Full install options →](install.md) · [See it in action →](use-cases.md)

</div>
