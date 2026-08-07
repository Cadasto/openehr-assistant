# Install

Two things to install, and you only need the first. The **MCP server** works
with any MCP client on its own; the **plugin** adds guided workflows on top of
it in Claude Code and Cursor.

!!! tip "Just want to try it?"
    Point your client at the hosted endpoint —
    `https://openehr-assistant-mcp.apps.cadasto.com/` — and skip straight to
    [Use cases](use-cases.md). Nothing to run locally.

Everything below is pulled from each product's own install guide when this site
is built, so it cannot fall out of step with the software it describes.

## MCP server

--8<-- "server-install.md"

## Plugin

--8<-- "plugin-install.md"

## Which server does the plugin talk to?

The plugin bundles a `.mcp.json` registering the hosted server under the name
`openehr-assistant`. If you also configure the server by hand, use that same
name — otherwise you end up with two client entries pointing at one endpoint.

Once both are in place, [Features](features.md) lists everything you can now
reach, and [Use cases](use-cases.md) shows it in action.
