# R100-B Official Pal Safe Index File Plan

Date: 2026-06-28

Scope: identify which official Pal index / README additions are safe candidates for a later repair thread. This file is a plan only; it does not create or modify files under `official/pals/**`.

Reference evidence:

- `templates/pal-asset/safe-index-backfill-guide.md`
- `templates/pal-asset/index-templates/`
- `standards/pal-asset/pal-asset-directory-standard.md`
- `standards/pal-asset/pal-skill-vs-agent-skill-standard.md`

## Rules For Future Index / README Additions

Future index additions may only:

- explain the directory purpose.
- list public-safe existing files at a high level.
- use the matching template from `templates/pal-asset/index-templates/` when available.
- state what belongs and what must not belong.
- state privacy, credential, memory, state, and report boundaries.
- preserve `missing`, `unknown`, and `not-run`.

Future index additions must not:

- move assets.
- rename directories.
- delete content.
- change Pal behavior.
- write project-private data.
- write credentials, tokens, secrets, cookies, API keys, customer data, or private memory.
- add route maps or deterministic owner logic.
- claim runtime execution.

## Directory-Level Plan

| Directory index | Current status across official Pals | Safe plan | Human review needed |
| --- | --- | --- | --- |
| `skills/index.md` | present or covered by README for all 9 in current audit | no action by R100-B | no |
| `workflows/index.md` | present or covered by README for all 9 in current audit | no action by R100-B | no |
| `runbooks/index.md` | PalSmith lacks runbooks index/README | add PalSmith `runbooks/README.md` or `runbooks/index.md` later, describing existing runbooks only | yes, to avoid changing PalSmith process semantics |
| `knowledge/index.md` | present or covered by README for all 9 in current audit | no action by R100-B | no |
| `memory/index.md` | missing top-level memory index/README for Atlas, Nova, Vega, Quinn, Morgan, Harper, Rhea; PalSmith lacks `memory/` | add public-safe memory index/README for the 7 Pals with existing `memory/` directories | yes for wording; PalSmith requires policy decision before directory creation |
| `learning/index.md` | present or covered by README where `learning/` exists; PalSmith lacks `learning/` | no direct auto-add for PalSmith until policy says whether learning is required or not-applicable | yes |
| `evals/index.md` | present or covered by README for all 9 in current audit | no action by R100-B | no |
| `examples/index.md` | present or covered by README for all 9 in current audit | no action by R100-B | no |
| `research/index.md` | missing research index/README for all 9 in current audit | prepare cautious public-safe research index template later; content must not promote raw research to knowledge | yes |

## Safe Candidate List

Safe with light human review:

- `official/pals/Atlas-developer/memory/README.md`
- `official/pals/Nova-product/memory/README.md`
- `official/pals/Vega-research/memory/README.md`
- `official/pals/Quinn-quality/memory/README.md`
- `official/pals/Morgan-document/memory/README.md`
- `official/pals/Harper-writing/memory/README.md`
- `official/pals/Rhea-system/memory/README.md`

Safe only after PalSmith policy review:

- `official/pals/PalSmith-pal-governor/runbooks/README.md`

Not safe to auto-create without a policy decision:

- `official/pals/PalSmith-pal-governor/memory/`
- `official/pals/PalSmith-pal-governor/learning/`

Research index candidates require content review before creation:

- `official/pals/Mira-main/research/README.md`
- `official/pals/Atlas-developer/research/README.md`
- `official/pals/Nova-product/research/README.md`
- `official/pals/Vega-research/research/README.md`
- `official/pals/Quinn-quality/research/README.md`
- `official/pals/Morgan-document/research/README.md`
- `official/pals/Harper-writing/research/README.md`
- `official/pals/Rhea-system/research/README.md`
- `official/pals/PalSmith-pal-governor/research/README.md`

## Suggested Memory README Template

Use only after a future repair thread is approved:

```md
# Memory

This directory is for public-safe Pal memory placeholders and approved durable memory summaries.

Do not store credentials, tokens, secrets, private project data, raw logs, customer data, or unapproved user-private memory here.

Reports are not memory until stable lessons are extracted and reviewed. Runtime state belongs in `state/`, not `memory/`.

If no approved memory exists, keep this directory as a boundary placeholder.
```

## Suggested Research README Template

Use only after content review:

```md
# Research

This directory stores source inventories, evidence notes, research drafts, and source-backed analysis for this Pal.

Research is not durable knowledge until reviewed and summarized into `knowledge/`.

Do not store credentials, private source dumps, copyrighted full text, raw private data, or unreviewed claims here.
```

## Suggested PalSmith Runbooks README Template

Use only after PalSmith review:

```md
# Runbooks

This directory contains concrete operation and exception-handling manuals for PalSmith asset governance work.

Runbooks should include symptoms, checks, steps, stop conditions, escalation rules, and verification evidence.

Do not store broad workflows, private memory, credentials, runtime state, or full reports here.
```

## Not-Run Items

R100-B did not:

- create index/README files under `official/pals/**`.
- inspect every file under every candidate directory as content.
- approve PalSmith `memory/` or `learning/` creation.
- generate manifests.
