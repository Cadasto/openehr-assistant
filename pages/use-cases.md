---
description: >-
  Five things people actually asked the openEHR Assistant to do, each from a
  real prompt, with the tool calls it made on its own — comparing archetypes,
  authoring one, generating code, and writing AQL.
---

# Use cases

Five things people actually asked the assistant to do, and what it did. Each
starts from a real prompt — no scripted demos. The last is lifted verbatim from
a public openEHR forum thread, so the question and the answer can both be
checked against the original.

The tool trails below are the calls the assistant made on its own; nobody named
a tool in the prompt.

## Compare two archetypes that look alike

<!-- Vale is switched off around each quoted question below: the quotes are
     verbatim user prose, so a style finding inside one cannot be acted on. -->
<!-- vale off -->
> *"There are two archetypes on CKM that look quite similar to me:
> `openEHR-EHR-OBSERVATION.progress_note.v1` and
> `openEHR-EHR-EVALUATION.clinical_synopsis.v1`. I don't know the implications
> and why one is OBSERVATION, while the other is EVALUATION. Compare them,
> explain when I should use one or the other."*
<!-- vale on -->

`ckm_archetype_get` ×2 → `ckm_template_search`

The assistant retrieved both archetypes, then searched for published templates
using each one to ground the answer in real usage rather than theory.

The difference is the Reference Model entry class, and it is structural rather
than cosmetic. An `OBSERVATION` carries `HISTORY` → `EVENT` → `ITEM_TREE`, so a
progress note can hold a sequence of timestamped entries: shift after shift,
round after round. An `EVALUATION` carries a plain `ITEM_TREE` — a clinical
synopsis is one persistent statement, with nowhere to put a time series. The
entry class decides what shape the data can take, not merely what it is called.

The answer came back as a comparison table, a structural sketch of both, and a
scenario-by-scenario mapping: shift handover and hourly ICU status to the
progress note; discharge summary and referral letter to the synopsis.

**Why it matters:** entry-class choice is the decision newcomers most often get
wrong, and it is expensive to correct once data exists.

## Understand an unfamiliar archetype

<!-- vale off -->
> *"Explain what this archetype is about, what the concept behind it is, and how
> it aligns to other similar archetypes on CKM. Give examples of how it can be
> used with other archetypes in a template."*
<!-- vale on -->

`ckm_archetype_get` → `ckm_archetype_search` (related concepts) → `ckm_archetype_get` on the candidates

Given `openEHR-EHR-OBSERVATION.four_a_test.v1`, the assistant explained the 4AT
as a validated rapid screening instrument for delirium and cognitive impairment
— four components, about two minutes at the bedside, a total of 0–12 in which
four or more suggests possible delirium.

It then read the modelling back out of the clinical design. The scoring is
deliberately non-linear: alertness and acute change score 0 or 4, never 1 or 2,
because those two carry more weight than the rest. That is why the archetype
models them as ordinals with coded values rather than plain counts. Finally it
placed the 4AT against its neighbours — ACVPU, GCS, NEWS2 — and observed that a
"C" on ACVPU is precisely the trigger for a full 4AT.

**Why it matters:** reading ADL tells you the structure; this tells you the
clinical intent, which is what determines whether you should reuse it.

## Find an archetype — or author one

<!-- vale off -->
> *"What archetype should I use to capture data for the 6-minute walk test? If
> there is no archetype that fits, create one. First analyse published science
> so you can add proper references. Re-use available CLUSTER archetypes through
> slots where CKM already has them."*
<!-- vale on -->

`ckm_archetype_search` (varied phrasings) → `ckm_template_search` → `type_specification_get` → `guide_get`

The honest answer came first: **no published or draft archetype for the 6MWT
exists.** The nearest relative, `openEHR-EHR-OBSERVATION.timed_25_foot_walk.v1`,
uses the opposite paradigm — time over a fixed distance, rather than distance
within a fixed time — so it is not a substitute.

Only then did it author `openEHR-EHR-OBSERVATION.six_minute_walk_test.v0` —
citing the ATS 2002 guideline and the 2014 ERS/ATS technical standard it had
gathered, opening slots onto published CLUSTERs rather than re-inventing them
(`inspired_oxygen.v1` for supplemental oxygen, `device.v1` for the oximeter,
`level_of_exertion.v0` for exertion context), and recommending
`openEHR-EHR-COMPOSITION.encounter.v1` to carry the result.

**Why it matters:** reuse-first is openEHR's most-violated principle. Searching
hard before authoring — and saying plainly when nothing fits — is the whole
game.

## Generate code from a model

<!-- vale off -->
> *"Create a DTO class in PHP that resembles the
> `openEHR-EHR-EVALUATION.precaution.v1` archetype. Adapt the methods published
> on the EVALUATION type where they make sense for a DTO."*
<!-- vale on -->

`ckm_archetype_get` → `type_specification_get` (EVALUATION)

Two sources, deliberately: the archetype for the constraint structure, and the
Reference Model type specification for the class contract. The result mapped
each `at` node to a typed property — mandatory condition with optional
terminology coding, a status enum, evidence as a `0..*` array, optional category
and comment — and kept the CLUSTER slot and protocol extension points open.

**Why it matters:** this is the bridge from clinical model to running software,
and it is where hand-written code and the archetype it claims to implement fall
out of step, with nothing to detect it.

## Write AQL that filters on a link

<!-- vale off -->
> *"When I try to retrieve only medicines that are linked to a particular
> problem using the following aql, I am getting empty response. […] If I remove
> the WHERE clause, both the values are returned. It would be a great help if
> anyone can advise on how to get the aql working."*
<!-- vale on -->

`guide_get` ×3 → `examples_search` → `type_specification_get` (LINK, LOCATABLE)
→ `ckm_archetype_get`

This one is not ours. It was
[asked on the openEHR forum](https://discourse.openehr.org/t/resolved-problem-filtering-on-links-using-where-in-aql-in-ehrbase/16797)
in May 2026: a prescription in which every `medication_item` carries an RM
`LINK` pointing at a problem in another composition, and a query that returns
nothing as soon as it filters on that link. The thread solved it in two hours —
a single character was missing from the URI, so the string never matched.

Put to the assistant, the same question produced the query, the AQL rules a SQL
background gets wrong — `LIKE` matches the *whole* value, and its wildcard is
`*`, not `%` — and the archetype path verified against the published ADL rather
than taken from the question. Then it fetched what `LINK` actually is, and read
back the Reference Model's own words: links *"should be between archetyped
structures only"*, and *"sensible links only exist between whole `ENTRY`s,
`SECTION`s, `COMPOSITION`s and so on"*.

The links in that composition hang on `medication_item` — an `ELEMENT`, an
interior node. The specification says that is the wrong place for them. Nobody
in the thread mentioned it.

**Why it matters:** the typo was found in two hours. The modelling decision
underneath it is the kind that passes review, ships, and turns expensive once
there is data in the system.

---

The first four transcripts live in Cadasto's internal knowledge base; the
archetypes they reference are published on [CKM](https://ckm.openehr.org/ckm/),
except the 6MWT draft, which was authored in the third example. The fifth is a
public thread — question, answer and all — so it can be read at the source.

Ready to try? [Install](install.md) takes a few minutes — or see the full
[feature inventory](features.md) first.
