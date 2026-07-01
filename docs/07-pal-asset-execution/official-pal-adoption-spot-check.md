# Official Pal Adoption Spot-Check

Status: R202 maintenance guide.

This guide summarizes how the official bundled Pals currently relate to the Pal
Asset Execution Contract. It is written for maintainers and users who want to
understand the adoption path without reading every audit record.

## Current Conclusion

AgentPal has 10 official bundled Pals. R202 checked their root entries and key
asset directories.

The roster already has strong Pal Pack structure: identities, role boundaries,
knowledge, skills, workflows, memory placeholders, collaboration boundaries,
and quality assets are widely present.

The current gap is explicit Pal Asset Execution adoption. Most official Pals
do not yet expose the R198-R201 entry terms in their sampled root assets:

- Asset Loading Gate;
- Task Asset Packet;
- Asset Use Summary;
- Missing Asset Plan.

PalSmith is currently the clearest adopter because it owns Pal asset governance
and already uses the completeness ladder and Missing Asset Plan language. That
does not mean every other official Pal has completed the same adoption path.

## What This Means For Users

For normal use, users can still call official Pals through Mira or `/pal Name`.
The spot-check does not remove any Pal.

For serious, tool-backed, release, QA, privacy, or customer-sensitive work, the
Pal should be able to explain:

- which Pal assets were needed;
- which assets were loaded;
- which assets were missing;
- why any host tool was used;
- how the output was checked.

If this evidence is missing, the honest result is a limited fallback or a
Missing Asset Plan, not a stronger readiness claim.

## How To Upgrade One Official Pal

Use this sequence for one Pal at a time.

1. Read the Pal's current assets:
   - `PAL.md`
   - `pal.json`
   - `SKILL.md`
   - `README.md`
   - relevant `identity/`, `knowledge/`, `skills/`, `workflows/`, `runtime/`,
     `memory/`, and `evals/` assets when present.
2. Create a Task Asset Packet for a real task family.
3. Add or reference the needed workflow, runtime policy, memory rule, and eval.
4. Run an asset usage regression for that task family.
5. Write an Asset Use Summary and quality review.
6. Raise the completeness level only for the tested scope.

## What Not To Do

- Do not only edit persona and call the Pal executable.
- Do not let a host tool call replace Pal judgement.
- Do not treat tools, models, plugins, MCP servers, shells, browser tools, or
  design generators as Pal assets.
- Do not mark a Pal verified without task-family evidence.
- Do not modify central contacts as part of ordinary adoption work.
- Do not promote draft or user custom Pals into the official roster through
  this guide.

## Suggested Phase Plan

Phase 1: add a short entry note to every official Pal that substantive work must
use the Asset Loading Gate or explicitly stay lightweight.

Phase 2: add Pal-specific Task Asset Packet and Asset Use Summary examples for
high-traffic Pals.

Phase 3: run one representative regression per official Pal task family.

Phase 4: review readiness labels with scope-limited evidence.

## R203 Phase 1 Entry Adoption

R203 completed Phase 1 entry adoption across the 10 official bundled Pals by
adding a concise Pal Asset Execution section to each official Pal `SKILL.md`
and a short adoption note to each official Pal `README.md`.

This means substantive tasks now have an explicit entry rule: use the Asset
Loading Gate and a Task Asset Packet or equivalent plan before
execution-shaped work; treat host tools as execution tools, not Pal assets; and
produce an Asset Use Summary or Missing Asset Plan when needed.

This does not complete per-Pal representative asset usage regression. Current
completeness levels remain unchanged unless a task family has its own evidence.

## R204 Phase 2 High-Priority Pal Examples

R204 added Task Asset Packet and Asset Use Summary examples for five
high-priority official Pals:

- Mira
- PalSmith
- Atlas
- Quinn
- Nova

Each example shows an Asset Loading Gate, Task Asset Packet, expected execution
behavior, tool boundary, Asset Use Summary, Missing Asset Plan handling,
lightweight path, and no-overclaim note.

These examples are adoption guidance. They are not full migration, not a
verified-readiness promotion, and not representative host regression evidence.
Phase 3 should run real or controlled host regressions for the high-priority
examples.

## R205 Representative Host Regressions

R205 ran real Codex host regressions for the same five high-priority official
Pals:

- Mira
- PalSmith
- Atlas
- Quinn
- Nova

Each representative thread recorded Asset Loading Gate evidence, a Task Asset
Packet or equivalent plan, and an Asset Use Summary or equivalent evidence.
Quinn reviewed the five-thread set and returned
`quinn_high_priority_host_regression_pass_with_notes`.

This remains representative task-family evidence. It does not verify all 10
official Pals and does not change contacts, user custom Pals, runtime behavior,
release status, or GitHub publication status.

## R206 Phase 3 Plan

R206 adds the all-official-Pal representative regression coverage matrix and an
R207 execution package for the remaining five official Pals:

- Faye
- Harper
- Morgan
- Rhea
- Vega

This is planning evidence only. It does not run the remaining host regressions
and does not change any Pal completeness label by itself.

## R207 Remaining Official Pal Host Regressions

R207 ran real Codex host regressions for the remaining five official Pals:

- Faye
- Harper
- Morgan
- Rhea
- Vega

Each representative thread recorded Asset Loading Gate or equivalent evidence,
a Task Asset Packet or equivalent plan, and an Asset Use Summary or equivalent
evidence. Quinn reviewed the five-thread set and returned
`quinn_remaining_official_pal_host_regression_pass_with_notes`.

Combined with R205, each of the 10 official bundled Pals now has one scoped
representative task-family host regression. This is not a blanket task-family
certification, not a release-readiness promotion, and not evidence of new
runtime or contacts behavior.

## R208 Scoped Certification Plan

R208 adds a certification plan, checklist, record template, candidate matrix,
and R209 execution package. It keeps R205/R207 as representative task-family
evidence and requires a separate gate before any Pal plus task family can be
marked `scoped_certified`.

The recommended next step is to review the five R205 high-priority task
families first, because those rows already have entry adoption, written
examples, host regressions, and Quinn review evidence.

## R209 High-Priority Scoped Certification Review

R209 reviewed the five R205 high-priority task-family scopes. Each selected
scope received `scoped_certified_with_notes`:

- Mira: release readiness coordination
- PalSmith: existing Pal composite upgrade planning
- Atlas: docs-first development task package
- Quinn: completion report / false completion review
- Nova: product privacy and authorization-boundary decision

These records are task-family scoped. They do not certify the whole official
roster, all task families, or any runtime / contacts / publication behavior.

## Evidence Files

- [`../../evals/palbench/v0.5/asset-usage/r202-official-pal-asset-execution-adoption-matrix.md`](../../evals/palbench/v0.5/asset-usage/r202-official-pal-asset-execution-adoption-matrix.md)
- [`../../evals/palbench/v0.5/asset-usage/r202-official-pal-adoption-gaps-summary.md`](../../evals/palbench/v0.5/asset-usage/r202-official-pal-adoption-gaps-summary.md)
- [`../../evals/palbench/v0.5/asset-usage/r202-quinn-official-pal-adoption-review.md`](../../evals/palbench/v0.5/asset-usage/r202-quinn-official-pal-adoption-review.md)
- [`../../evals/palbench/v0.5/asset-usage/r203-official-pal-entry-adoption-matrix.md`](../../evals/palbench/v0.5/asset-usage/r203-official-pal-entry-adoption-matrix.md)
- [`../../evals/palbench/v0.5/asset-usage/r203-official-pal-entry-adoption-before-after.md`](../../evals/palbench/v0.5/asset-usage/r203-official-pal-entry-adoption-before-after.md)
- [`../../evals/palbench/v0.5/asset-usage/r203-quinn-official-pal-entry-adoption-review.md`](../../evals/palbench/v0.5/asset-usage/r203-quinn-official-pal-entry-adoption-review.md)
- [`../../evals/palbench/v0.5/asset-usage/r204-high-priority-pal-task-asset-packet-examples-matrix.md`](../../evals/palbench/v0.5/asset-usage/r204-high-priority-pal-task-asset-packet-examples-matrix.md)
- [`../../evals/palbench/v0.5/asset-usage/r204-task-asset-packet-example-quality-review.md`](../../evals/palbench/v0.5/asset-usage/r204-task-asset-packet-example-quality-review.md)
- [`../../evals/palbench/v0.5/asset-usage/r204-quinn-phase-2-example-review.md`](../../evals/palbench/v0.5/asset-usage/r204-quinn-phase-2-example-review.md)
- [`../../evals/palbench/v0.5/asset-usage/r205-high-priority-host-regression-summary.md`](../../evals/palbench/v0.5/asset-usage/r205-high-priority-host-regression-summary.md)
- [`../../evals/palbench/v0.5/asset-usage/r205-quinn-high-priority-host-regression-review.md`](../../evals/palbench/v0.5/asset-usage/r205-quinn-high-priority-host-regression-review.md)
- [`phase-3-official-pal-regression-plan.md`](phase-3-official-pal-regression-plan.md)
- [`../../evals/palbench/v0.5/asset-usage/r206-official-pal-representative-regression-coverage-matrix.md`](../../evals/palbench/v0.5/asset-usage/r206-official-pal-representative-regression-coverage-matrix.md)
- [`../../evals/palbench/v0.5/asset-usage/r206-remaining-official-pal-regression-plan.md`](../../evals/palbench/v0.5/asset-usage/r206-remaining-official-pal-regression-plan.md)
- [`../../evals/palbench/v0.5/asset-usage/r206-r207-execution-package.md`](../../evals/palbench/v0.5/asset-usage/r206-r207-execution-package.md)
- [`../../evals/palbench/v0.5/asset-usage/r206-quinn-phase-3-plan-review.md`](../../evals/palbench/v0.5/asset-usage/r206-quinn-phase-3-plan-review.md)
- [`../../evals/palbench/v0.5/asset-usage/r207-faye-delivery-host-regression.md`](../../evals/palbench/v0.5/asset-usage/r207-faye-delivery-host-regression.md)
- [`../../evals/palbench/v0.5/asset-usage/r207-harper-writing-host-regression.md`](../../evals/palbench/v0.5/asset-usage/r207-harper-writing-host-regression.md)
- [`../../evals/palbench/v0.5/asset-usage/r207-morgan-document-host-regression.md`](../../evals/palbench/v0.5/asset-usage/r207-morgan-document-host-regression.md)
- [`../../evals/palbench/v0.5/asset-usage/r207-rhea-system-boundary-host-regression.md`](../../evals/palbench/v0.5/asset-usage/r207-rhea-system-boundary-host-regression.md)
- [`../../evals/palbench/v0.5/asset-usage/r207-vega-research-host-regression.md`](../../evals/palbench/v0.5/asset-usage/r207-vega-research-host-regression.md)
- [`../../evals/palbench/v0.5/asset-usage/r207-quinn-remaining-official-pal-host-regression-review.md`](../../evals/palbench/v0.5/asset-usage/r207-quinn-remaining-official-pal-host-regression-review.md)
- [`../../evals/palbench/v0.5/asset-usage/r207-remaining-official-pal-host-regression-summary.md`](../../evals/palbench/v0.5/asset-usage/r207-remaining-official-pal-host-regression-summary.md)
- [`../../evals/palbench/v0.5/asset-usage/r207-official-pal-representative-regression-coverage-matrix.md`](../../evals/palbench/v0.5/asset-usage/r207-official-pal-representative-regression-coverage-matrix.md)
- [`scoped-certification-plan.md`](scoped-certification-plan.md)
- [`scoped-certification-checklist.md`](scoped-certification-checklist.md)
- [`../../templates/pal/scoped-certification-record.md`](../../templates/pal/scoped-certification-record.md)
- [`../../evals/palbench/v0.5/asset-usage/r208-scoped-certification-candidate-matrix.md`](../../evals/palbench/v0.5/asset-usage/r208-scoped-certification-candidate-matrix.md)
- [`../../evals/palbench/v0.5/asset-usage/r208-r209-scoped-certification-execution-package.md`](../../evals/palbench/v0.5/asset-usage/r208-r209-scoped-certification-execution-package.md)
- [`../../evals/palbench/v0.5/asset-usage/r208-quinn-scoped-certification-plan-review.md`](../../evals/palbench/v0.5/asset-usage/r208-quinn-scoped-certification-plan-review.md)
- [`../../evals/palbench/v0.5/asset-usage/r209-scoped-certification-review-matrix.md`](../../evals/palbench/v0.5/asset-usage/r209-scoped-certification-review-matrix.md)
- [`../../evals/palbench/v0.5/asset-usage/r209-quinn-scoped-certification-review.md`](../../evals/palbench/v0.5/asset-usage/r209-quinn-scoped-certification-review.md)
