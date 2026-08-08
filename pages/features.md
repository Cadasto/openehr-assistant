# Features

Everything the openEHR Assistant ships, in one place. The **server** supplies
knowledge and tools over the Model Context Protocol; the **plugin** turns them
into guided workflows inside Claude Code and Cursor.

## Server

### Tools

Twelve tools, callable from any MCP client.

| Tool | What it does |
|------|--------------|
| `ckm_archetype_search` | Search published CKM archetypes, ranked by relevance, filterable by RM class |
| `ckm_archetype_get` | Fetch one archetype by CKM id or archetype id, in ADL or JSON |
| `ckm_template_search` | Search published CKM templates |
| `ckm_template_get` | Fetch one template, including the archetypes it references |
| `guide_search` | Find implementation guidance across the bundled guide corpus |
| `guide_get` | Retrieve a full guide by category and name |
| `guide_adl_idiom_lookup` | Look up a specific ADL/AQL/OET idiom without loading a whole guide |
| `examples_search` | Find a worked example matching a pattern |
| `examples_get` | Retrieve one curated example |
| `terminology_resolve` | Resolve openEHR terminology codes and groups to their meanings |
| `type_specification_search` | Find an RM/AM/BASE type across the specification components |
| `type_specification_get` | Attributes, functions and invariants for one type, from the BMM schemas |

### Prompts

Guided, multi-step prompts a client can offer as slash commands or presets.

| Group | Prompts |
|-------|---------|
| **Explore** | `ckm_explorer`, `guide_explorer`, `terminology_explorer`, `type_specification_explorer` |
| **Explain** | `explain_archetype`, `explain_template`, `explain_aql`, `explain_simplified_format` |
| **Design or review** | `design_or_review_archetype`, `design_or_review_template`, `design_or_review_aql`, `design_or_review_simplified_format` |
| **Transform** | `fix_adl_syntax`, `translate_archetype_language` |

### Knowledge base

Guides are written for AI context economy: short, scannable, and grounded in the
authoritative specifications rather than model memory.

| Category | Covers |
|----------|--------|
| `archetypes` | ADL syntax and idioms, modelling principles, anti-patterns, structural constraints, terminology, review checklists, and language standards (incl. `nb`, `nl`) |
| `templates` | OET and OPT structure, web templates, serialisation formats, the CGEM categorisation framework, principles and checklists |
| `aql` | Syntax, principles, an idioms cheatsheet, and a review checklist |
| `simplified_formats` | FLAT and STRUCTURED JSON — principles, rules, idioms, checklist |
| `specs` | Digests of every published component: RM, AM (ADL 1.4/2, AOM, OPT2), BASE, QUERY, LANG, SM, PROC, CDS, TERM, CNF and ITS-REST |
| `howto` | Working practices, including the specification-lookup policy the server itself follows |

Curated, runnable examples sit alongside them.

| Kind | Contents |
|------|----------|
| `aql` | Twelve queries — time windows, cohorts, joins across compositions, pagination with totals, terminology value sets, versioning |
| `archetypes` | CKM-published archetypes covering each entry class — OBSERVATION, EVALUATION, INSTRUCTION, ACTION, ADMIN_ENTRY, CLUSTER, COMPOSITION |
| `flat` / `structured` | Simplified-format payloads, including RM attributes, coded text with free text, and the raw escape hatch |

### Resources and completions

Stable `openehr://` URIs let a client read content directly, without a tool call:
`openehr://guides/{category}/{name}`, `openehr://examples/{kind}/{name}`,
`openehr://spec/type/{component}/{name}`, and `openehr://terminology`.

Argument completion is provided for guide names, example names, and
specification components.

## Plugin

### Skills

Skills load automatically when a conversation matches their trigger, so the
right guidance arrives without anyone remembering to ask for it.

| Skill | Purpose |
|-------|---------|
| `openehr-assistant` | Routes any openEHR question that no other skill owns; loads guides before answering |
| `archetype-authoring` | Create, edit, specialise, review, translate an archetype — and fix ADL that will not parse |
| `archetype-lint` | 24 normative lint rules with ERROR/WARNING/INFO severity, in STRICT or PERMISSIVE mode |
| `template-authoring` | Template design and archetype constraint, including the CGEM categorisation framework |
| `composition-builder` | Build and validate compositions in FLAT, STRUCTURED and CANONICAL form |
| `aql-authoring` | Author, review and optimise AQL queries |
| `semantic-diff` | Compare two archetypes or templates and classify the change as patch, minor or major |
| `demographic-modeling` | Model people, organisations, roles and relationships across the PARTY hierarchy |

### Agents

Delegated workers that keep heavy retrieval out of the main conversation.

| Agent | Role |
|-------|------|
| `ckm-scout` | Runs parallel CKM searches across varied phrasings and returns a ranked reuse/specialise/author recommendation |
| `clinical-modeler` | Reads and writes archetype, template and composition files in your workspace |
| `spec-researcher` | Answers precise specification questions using the cheapest-first lookup policy |

### Commands and guardrails

| Command | Use |
|---------|-----|
| `/ckm-search` | Search CKM for archetypes or templates |
| `/openehr-explain` | Explain any openEHR thing — auto-detects archetype, template, RM type or query |
| `/archetype-impact` | Scan the workspace for every reference to an archetype before you change it |

Session hooks load openEHR context at start-up, a lint-on-save hook checks
archetypes as you write them, and an editor rule keeps modelling conventions in
view.

---

Next: see these working in [Use cases](use-cases.md), or [install](install.md)
the server and plugin.
