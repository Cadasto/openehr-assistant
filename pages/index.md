---
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

<p class="home-reassure">
MIT-licensed and open source. Nothing to install to try it — point any MCP client at the hosted endpoint.
</p>

</div>

<h2 class="section-title">Why openEHR Assistant?</h2>

<div class="features-grid" markdown="1">

<div class="feature-card" markdown="1">

:material-shield-check:

### It looks things up
Archetypes come from CKM, type definitions from the BMM schemas, guidance from a corpus written against the published specifications. Nothing is recalled from training.

</div>

<div class="feature-card" markdown="1">

:material-database-search:

### CKM, without the tab-switching
Search published archetypes and templates by concept, filter by RM class, and pull one back as ADL or JSON — in the editor you are already modelling in.

</div>

<div class="feature-card" markdown="1">

:material-toolbox:

### Twelve tools, any MCP client
CKM, guides, examples, terminology and type specifications, reachable from Claude Code, Cursor, Claude Desktop, LibreChat or anything else that speaks the protocol.

</div>

<div class="feature-card" markdown="1">

:material-book-open-variant:

### The guide loads first
The relevant implementation guide is read before the answer is written, so you get the convention and the anti-pattern — not just something that parses.

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
