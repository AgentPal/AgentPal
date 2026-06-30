# Phase 3 Official Pal Regression Plan

Status: R206 maintainer guide.

Phase 3 is the representative host regression stage for official Pals. Its job
is to check whether a Pal can use its own assets during a real task, not merely
whether the Pal has a name, persona, or entry file.

## Adoption Levels

| Level | Meaning |
| --- | --- |
| Entry adoption | The Pal entry files tell the Pal to use the Asset Loading Gate and Task Asset Packet for substantive work. |
| Example | The Pal has a written example of a Task Asset Packet and Asset Use Summary. |
| Representative host regression | A real host thread shows the Pal using assets for one representative task family. |
| Certification candidate | Multiple task families, missing-asset handling, tool boundary, and verifier review are covered enough to discuss a scoped completeness label. |

R203 completed entry adoption for all 10 official Pals.

R204 added examples for Mira, PalSmith, Atlas, Quinn, and Nova.

R205 ran representative Codex host regressions for Mira, PalSmith, Atlas,
Quinn, and Nova.

R206 plans the remaining representative host regressions for Faye, Harper,
Morgan, Rhea, and Vega.

R207 executed those remaining representative host regressions in real Codex
local project threads and recorded the results as scoped evidence.

## Why R206 Exists

The official Pal roster has 10 Pals. R205 covered five high-priority task
families, but the remaining five official Pals still need real host evidence
before maintainers can say the official roster has broad representative
coverage.

R206 creates:

- the 10-Pal coverage matrix;
- the remaining five-Pal regression plan;
- the R207 execution package;
- the Quinn plan review.

## Remaining Phase 3 Targets

| Pal | Planned task family |
| --- | --- |
| Faye | delivery / handoff / user-facing delivery summary |
| Harper | README-oriented writing / style / revision |
| Morgan | document structure / release notes / document package |
| Rhea | system boundary / no-code boundary / risk review |
| Vega | research / source policy / external Skill-to-Pal evaluation |

## What R207 Should Prove

For each remaining Pal, R207 should prove that a real host thread can:

- resolve the Pal correctly;
- use Asset Loading Gate or equivalent judgement;
- form a Task Asset Packet or equivalent plan;
- load task-relevant Pal assets;
- preserve tool and Runtime boundaries;
- output Asset Use Summary or equivalent evidence;
- record missing assets honestly.

## What R207 Still Will Not Prove

Even if R207 succeeds, the result is still representative task-family coverage.
It is not a blanket completeness label for every task the Pal might handle.

R207 should not:

- alter central contacts;
- promote user custom Pals;
- create official Pals;
- add runtime code or scanners;
- publish releases;
- create remote tags;
- claim every task family is covered.

## R207 Result

R207 completed representative host regressions for the remaining five official
Pals:

| Pal | Representative task family | Result |
| --- | --- | --- |
| Faye | delivery / handoff / user-facing delivery summary | pass_with_notes |
| Harper | README-oriented writing / style / revision | pass_with_notes |
| Morgan | document structure / release notes / document package | pass_with_notes |
| Rhea | system boundary / no-code boundary / risk review | pass_with_notes |
| Vega | research / source policy / external Skill-to-Pal evaluation | pass_with_notes |

Quinn reviewed the five-thread set and returned
`quinn_remaining_official_pal_host_regression_pass_with_notes`.

Combined with R205, the official bundled Pal roster now has one representative
task-family host regression per Pal. This is still scoped evidence. It is not a
claim that every task family is covered, and it does not add runtime,
publication, contacts, or backend behavior.

## Phase 4 / Certification Preconditions

Phase 4 can only consider scoped completeness labels when:

- every official Pal has at least one representative host regression;
- each regression has Quinn or equivalent QA review;
- each Pal has clear missing-asset behavior;
- tool / Runtime boundaries were pressure-tested for the relevant task family;
- coverage is labelled by task family, not by Pal name alone;
- no private user data or customer material is embedded in public examples.

## Evidence

- [`../../evals/palbench/v0.5/asset-usage/r206-official-pal-representative-regression-coverage-matrix.md`](../../evals/palbench/v0.5/asset-usage/r206-official-pal-representative-regression-coverage-matrix.md)
- [`../../evals/palbench/v0.5/asset-usage/r206-remaining-official-pal-regression-plan.md`](../../evals/palbench/v0.5/asset-usage/r206-remaining-official-pal-regression-plan.md)
- [`../../evals/palbench/v0.5/asset-usage/r206-r207-execution-package.md`](../../evals/palbench/v0.5/asset-usage/r206-r207-execution-package.md)
- [`../../evals/palbench/v0.5/asset-usage/r206-quinn-phase-3-plan-review.md`](../../evals/palbench/v0.5/asset-usage/r206-quinn-phase-3-plan-review.md)
- [`../../evals/palbench/v0.5/asset-usage/r207-remaining-official-pal-host-regression-summary.md`](../../evals/palbench/v0.5/asset-usage/r207-remaining-official-pal-host-regression-summary.md)
- [`../../evals/palbench/v0.5/asset-usage/r207-official-pal-representative-regression-coverage-matrix.md`](../../evals/palbench/v0.5/asset-usage/r207-official-pal-representative-regression-coverage-matrix.md)
- [`../../evals/palbench/v0.5/asset-usage/r207-quinn-remaining-official-pal-host-regression-review.md`](../../evals/palbench/v0.5/asset-usage/r207-quinn-remaining-official-pal-host-regression-review.md)
