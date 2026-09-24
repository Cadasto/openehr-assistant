---
description: >-
  Install the openEHR Assistant MCP server (Cadasto's endpoint, Docker, or
  stdio) and the plugin for Claude Code and Cursor. Instructions come straight
  from each product's own repository.
---

# Install

This page covers installing both parts of the openEHR Assistant, and you only
need the first. The **MCP server** works with any MCP client on its own; the
**plugin** adds guided workflows on top of it in Claude Code and Cursor.

!!! tip "Want to try it first?"
    Point your client at the hosted endpoint,
    `https://openehr-assistant-mcp.apps.cadasto.com/`, and skip straight to
    [Use cases](use-cases.md). Nothing runs locally.

Everything below is fetched from each product's own install guide when this
site is built, at the version the site pins, so the steps here match that
release of the software.

## MCP server

--8<-- "server-install.md"

## Plugin

--8<-- "plugin-install.md"

## Using the plugin and the server together

The plugin registers the hosted server for you. If you also configure the
server by hand, use the same name the plugin uses; [How they fit
together](components.md#how-they-fit-together) gives the name and how to aim the
plugin at another server.

Once both are in place, [Features](features.md) lists everything you can now
reach, and [Use cases](use-cases.md) shows it in action.
