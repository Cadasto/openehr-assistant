---
# The <title> tag only, not the H1 and not the nav label (mkdocs.yml sets that).
# Without it the homepage title is just the site name, which spends the most
# valuable string on the site saying nothing a searcher would type.
title: openEHR MCP server and Claude Code plugin
description: >-
  Design archetypes, constrain templates and write AQL with an assistant that
  looks the answer up in CKM and the published openEHR specifications: an MCP
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
[View on GitHub](https://github.com/Cadasto/openehr-assistant-mcp){ .md-button }

</div>

<p class="home-reassure" markdown="1">
MIT-licensed and open source. Use Cadasto's hosted endpoint, or
[self-host it](install.md).
</p>

</div>

<h2 class="section-title">What it does</h2>

<div class="features-grid" markdown="1">

<div class="feature-card" markdown="1">

:material-shield-check:

### It looks things up
Archetypes come from CKM, type definitions from the BMM schemas, guidance from a corpus written against the published specifications. The server answers from those sources, not from a model's memory.

</div>

<div class="feature-card" markdown="1">

:material-database-search:

### CKM inside your editor
Search published archetypes and templates by concept, and filter archetypes by RM class. Pull an archetype back as ADL, XML, or a mindmap, and a template as OET or OPT, in the editor you are already modelling in.

</div>

<div class="feature-card" markdown="1">

:material-toolbox:

### Twelve tools, any MCP client
CKM, guides, examples, terminology, and type specifications, reachable from Claude Code, Cursor, Claude Desktop, LibreChat, or any other client that speaks the protocol.

</div>

<div class="feature-card" markdown="1">

:material-book-open-variant:

### The guide loads first
With the plugin, the relevant implementation guide is loaded before the answer is written, so you get the convention and the anti-pattern as well as something that parses.

</div>

<div class="feature-card" markdown="1">

:material-lock-outline:

### Your patient data stays put
A knowledge and authoring server, not a clinical data repository. It reads specifications and published archetypes; it never stores patient data.

</div>

<div class="feature-card" markdown="1">

:material-server-network:

### Managed or self-hosted
Use Cadasto's endpoint, or run your own instance over streamable HTTP or stdio.

</div>

</div>

<h2 class="section-title">The server and the plugin</h2>

<div class="two-products" markdown="1">

<div class="product-card" markdown="1">

:material-server:

### MCP server
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

## Quick start

Point any MCP client at Cadasto's endpoint:

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
