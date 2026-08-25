---
description: >-
  Everything the openEHR Assistant ships — twelve MCP tools for CKM, guides,
  examples, terminology and type specifications, plus the plugin's skills,
  agents and commands for clinical modelling.
---

# Features

The openEHR Assistant comes in two halves. The **MCP server** supplies knowledge
and tools over the [Model Context Protocol](https://modelcontextprotocol.io/),
and works with any client that speaks it. The **plugin** turns those tools into
guided workflows, and runs in Claude Code and Cursor only.

Use the server on its own to search CKM, read specifications and resolve
terminology from whatever client you already have. Add the plugin when you want
the modelling workflow around it: the relevant guide loaded before an answer,
and lint, diff and impact checks over the files in your workspace.
[Use cases](use-cases.md) shows both at work, with the tool calls each one made.

!!! note "Pre-release"
    Expect breaking changes until version 1.0 — see [Components](components.md).
    The counts and names below were checked against the hosted server and plugin
    v0.9.2 on 26 August 2026.

## MCP server

Everything here is reachable from any MCP client. Every tool is a read — search,
fetch, resolve — so nothing writes back to CKM.

### Tools

Twelve tools, callable from any MCP client.

| Tool | What it does |
|------|--------------|
| `ckm_archetype_search` | Search published CKM archetypes, ranked by relevance, filterable by RM class |
| `ckm_archetype_get` | Fetch one archetype by CKM id or archetype id, as ADL, XML or a mindmap |
| `ckm_template_search` | Search published CKM templates |
| `ckm_template_get` | Fetch one template as OET (design-time source) or OPT (flattened, with every archetype constraint inlined) |
| `guide_search` | Find implementation guidance across the bundled guide corpus |
| `guide_get` | Retrieve a full guide by category and name |
| `guide_adl_idiom_lookup` | Look up a specific ADL/AQL/OET idiom without loading a whole guide |
| `examples_search` | Find a worked example matching a pattern |
| `examples_get` | Retrieve one curated example |
| `terminology_resolve` | Resolve openEHR terminology codes to their rubrics, across groups and codesets |
| `type_specification_search` | Find an RM/AM/BASE type across the specification components |
| `type_specification_get` | Attributes, functions and invariants for one type, from the BMM schemas |

### Prompts

Fourteen prompts that walk a client through a multi-step workflow. The protocol
treats prompts as optional, so whether they surface — as slash commands, as
presets, or not at all — is the client's choice.

| Group | Prompts |
|-------|---------|
| **Explore** | `ckm_explorer`, `guide_explorer`, `terminology_explorer`, `type_specification_explorer` |
| **Explain** | `explain_archetype`, `explain_template`, `explain_aql`, `explain_simplified_format` |
| **Design or review** | `design_or_review_archetype`, `design_or_review_template`, `design_or_review_aql`, `design_or_review_simplified_format` |
| **Transform** | `fix_adl_syntax`, `translate_archetype_language` |

### Guides and examples

Sixty-six guides ship with the server, reachable through `guide_search` and
`guide_get`. The spec digests run 250–900 words each and link the canonical
specification page they summarise, so a claim can be followed to its source.
They track the specifications' `development` branch rather than a numbered
release.

| Category | Guides | Covers |
|----------|-------:|--------|
| `archetypes` | 12 | ADL syntax and idioms, modelling principles, anti-patterns, structural constraints, terminology, a review checklist, and language standards (incl. `nb`, `nl`) |
| `templates` | 9 | OET and OPT structure, web templates, serialisation formats, the CGEM categorisation framework, principles and a checklist |
| `aql` | 4 | Syntax, principles, an idioms cheatsheet, and a review checklist |
| `simplified_formats` | 4 | FLAT and STRUCTURED JSON — principles, rules, idioms, checklist |
| `specs` | 36 | Digests of the published components: RM, AM (ADL 1.4/2, AOM, OPT2), BASE, QUERY, LANG, SM, PROC, CDS, TERM, CNF and ITS-REST |
| `howto` | 1 | The specification-lookup policy the server itself follows |

Twenty-four curated examples sit alongside them, reachable through
`examples_search` and `examples_get`.

| Kind | Examples | Contents |
|------|---------:|----------|
| `aql` | 12 | Time windows, cohorts, joins across compositions, pagination with totals, terminology value sets and audit trails, among others |
| `archetypes` | 7 | CKM-published archetypes, one per top-level content class — the five `ENTRY` subtypes (OBSERVATION, EVALUATION, INSTRUCTION, ACTION, ADMIN_ENTRY), plus CLUSTER and COMPOSITION |
| `flat` | 4 | FLAT payloads, including optional RM attributes, coded text with free text, and the raw escape hatch |
| `structured` | 1 | The vital-signs payload again, in STRUCTURED form, so the two can be read side by side |

### Resources and completions

Documented `openehr://` URIs let a client read content directly, without a tool
call: `openehr://guides/{category}/{name}`, `openehr://examples/{kind}/{name}`,
`openehr://spec/type/{component}/{name}`, and `openehr://terminology`.

The server completes guide names by category, example names by kind, and
specification components.

## Plugin

The workflow layer for Claude Code and Cursor. It needs a host and a reachable
MCP server: without one, the guide-first workflows have nothing to load — the
`clinical-modeler` agent falls back to the reference material bundled in the
plugin, and `ckm-scout` and `spec-researcher` stop and say so.

### Skills

Skills are model-invoked: the host reads a skill's trigger description and loads
the one that matches, so the guidance arrives without anyone naming it. Seven are
also slash commands you can call directly; `openehr-assistant` only routes.

| Skill | Purpose |
|-------|---------|
| `openehr-assistant` | Routes any openEHR question that no other skill owns; loads guides before answering |
| `archetype-authoring` | Create, edit, specialise, review, translate an archetype — and fix ADL that will not parse |
| `archetype-lint` | 24 lint checks with ERROR/WARNING/INFO severity, in STRICT or PERMISSIVE mode, indexed against the server's `archetypes/rules` guide |
| `template-authoring` | Template design and archetype constraint, including the CGEM categorisation framework |
| `composition-builder` | Build compositions in FLAT, STRUCTURED and CANONICAL form, and guide validation against a target template — no automated validator ships |
| `aql-authoring` | Author, review and optimise AQL queries |
| `semantic-diff` | Compare two archetypes or templates and classify the change as patch, minor or major |
| `demographic-modeling` | Model people, organisations, roles and relationships across the PARTY hierarchy |

### Agents

Subagents the main conversation delegates to, so heavy retrieval stays out of its
context.

| Agent | Role |
|-------|------|
| `ckm-scout` | Runs parallel CKM searches across varied phrasings and returns a ranked reuse/specialise/author recommendation |
| `clinical-modeler` | Reads and writes archetype, template and composition files in your workspace |
| `spec-researcher` | Answers precise specification questions using the cheapest-first lookup policy |

### Commands

Three slash commands, alongside the seven skills that are invocable the same way.

| Command | Use |
|---------|-----|
| `/ckm-search` | Search CKM for archetypes or templates |
| `/openehr-explain` | Explain any openEHR thing — auto-detects archetype, template, RM type or query |
| `/archetype-impact` | Scan the workspace for every reference to an archetype before you change it |

### Hooks and editor rule

A session-start hook loads openEHR context in both hosts. In Claude Code, a
second hook notices when the assistant writes an `.adl` file and suggests an
`/archetype-lint` run — it prompts, it does not lint. The editor rule applies
when openEHR files are in context (`.adl`, `.oet`, `.opt`, `.aql` and their
variants), keeping modelling conventions in view.

---

Next: see these working in [Use cases](use-cases.md), or [install](install.md)
the server and plugin.
