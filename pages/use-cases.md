# Use cases

Four things people actually asked the assistant to do, and what it did. Each
starts from a real prompt — no scripted demos.

The tool trails below are the calls the assistant made on its own; nobody named
a tool in the prompt.

## Compare two archetypes that look alike

> *"There are two archetypes on CKM that look quite similar to me:
> `openEHR-EHR-OBSERVATION.progress_note.v1` and
> `openEHR-EHR-EVALUATION.clinical_synopsis.v1`. I don't know the implications
> and why one is OBSERVATION, while the other is EVALUATION. Compare them,
> explain when I should use one or the other."*

`ckm_archetype_get` ×2 → `ckm_template_search`

The assistant retrieved both archetypes, then searched for published templates
using each one to ground the answer in real usage rather than theory.

The difference is the Reference Model entry class, and it is semantic rather
than cosmetic: an `OBSERVATION` records what was observed *as it happened*,
while an `EVALUATION` records an *assessment or interpretation* of findings. So
a progress note documenting the course of an encounter is an observation; a
clinical synopsis summarising a patient's situation is an evaluation. The answer
came back as a comparison table plus concrete guidance on which to reach for,
and which templates already combine them.

**Why it matters:** entry-class choice is the decision newcomers most often get
wrong, and it is expensive to correct once data exists.

## Understand an unfamiliar archetype

> *"Explain what this archetype is about, what the concept behind it is, and how
> it aligns to other similar archetypes on CKM. Give examples of how it can be
> used with other archetypes in a template."*

`ckm_archetype_get` → `ckm_archetype_search` (related concepts) → `ckm_archetype_get` on the candidates

Given `openEHR-EHR-OBSERVATION.four_a_test.v1`, the assistant explained the 4AT
as a validated rapid screening instrument for delirium and cognitive impairment
— its four components, why it takes about two minutes at the bedside, and what
its scoring thresholds mean clinically. It then placed it among neighbouring
CKM archetypes and sketched how it composes into a template alongside them.

**Why it matters:** reading ADL tells you the structure; this tells you the
clinical intent, which is what determines whether you should reuse it.

## Find an archetype — or author one

> *"What archetype should I use to capture data for the 6-minute walk test? If
> there is no archetype that fits, create one. First analyse published science
> so you can add proper references. Re-use available CLUSTER archetypes through
> slots where CKM already has them."*

`ckm_archetype_search` (several phrasings) → `ckm_template_search` → `type_specification_get` → `guide_get`

The honest answer came first: **no published or draft archetype for the 6MWT
exists.** The nearest relative, `openEHR-EHR-OBSERVATION.timed_25_foot_walk.v1`,
uses the opposite paradigm — time over a fixed distance, rather than distance
within a fixed time — so it is not a substitute.

Only then did it author `openEHR-EHR-OBSERVATION.six_minute_walk_test.v0`,
citing the literature it had gathered, reusing published CLUSTER archetypes
through slots instead of re-inventing them, and recommending a COMPOSITION
archetype to carry the result.

**Why it matters:** reuse-first is openEHR's most-violated principle. Searching
hard before authoring — and saying plainly when nothing fits — is the whole
game.

## Generate code from a model

> *"Create a DTO class in PHP that resembles the
> `openEHR-EHR-EVALUATION.precaution.v1` archetype. Adapt the methods published
> on the EVALUATION type where they make sense for a DTO."*

`ckm_archetype_get` → `type_specification_get` (EVALUATION)

Two sources, deliberately: the archetype for the constraint structure, and the
Reference Model type specification for the class contract. The result mapped
each `at` node to a typed property — mandatory condition with optional
terminology coding, a status enum, evidence as a `0..*` array, optional category
and comment — and kept the CLUSTER slot and protocol extension points open.

**Why it matters:** this is the bridge from clinical model to running software,
and it is where hand-written code usually drifts from the archetype it claims to
implement.

---

These transcripts live in Cadasto's internal knowledge base; the archetypes they
reference are published on [CKM](https://ckm.openehr.org/ckm/), except the 6MWT
draft, which was authored in the third example.

Ready to try? [Install](install.md) takes a few minutes, or read what the
[Features](features.md) actually are.
