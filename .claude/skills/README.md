# Vendored skills

Four marketing skills live here so that they load **only in this repository**.
They are copy and SEO tools for the website's prose; every other project would
just have them triggering on unrelated work.

| Skill | Used for |
|-------|----------|
| `copy-editing` | Reviewing and tightening existing page copy |
| `copywriting` | Writing new landing and feature copy |
| `seo-audit` | Technical and on-page checks against the published site |
| `ai-seo` | `llms.txt`, structured data, and being citable by AI search |

## Why they are not committed

`.gitignore` excludes the skill directories, for the same reason `.fetched/` is
excluded: they are somebody else's content, and a second copy in here would
drift from upstream with nothing to detect it. This file is the pointer; the
bodies are fetched.

## Restoring them

Upstream is [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills)
(MIT). The four directories above were taken from tarball `7868cb9`, each with
the upstream `LICENSE` copied alongside it — MIT requires the notice to travel
with the copy.

Only these four are installed. The repository ships 48, and its Claude Code
plugin manifest exposes them as a single all-or-nothing plugin, which is why
they are vendored by hand rather than installed with `/plugin install`.

```bash
gh api repos/coreyhaines31/marketingskills/tarball > /tmp/ms.tar.gz
root=$(tar tzf /tmp/ms.tar.gz | head -1 | cut -d/ -f1)
tar xzf /tmp/ms.tar.gz -C /tmp \
  "$root/skills/copy-editing" "$root/skills/copywriting" \
  "$root/skills/seo-audit"    "$root/skills/ai-seo" "$root/LICENSE"
for s in copy-editing copywriting seo-audit ai-seo; do
  cp -r "/tmp/$root/skills/$s" .claude/skills/
  cp "/tmp/$root/LICENSE" ".claude/skills/$s/LICENSE"
done
```

Drop the pinned ref for `tarball/<ref>` if you want a specific version rather
than the default branch.

## A caution on using them

These skills optimise for conversion. The audience for this site is clinical
modellers and health-IT developers, who tend to distrust growth copy, and
[`AGENTS.md`](../../AGENTS.md) requires that statements about openEHR be grounded
in the published specifications. Treat their output as a critique to accept
selectively, not a rewrite to apply — in particular, they will suggest adding
statistics, testimonials and urgency that this project does not have and should
not invent.
