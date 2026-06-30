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

## Evidence Files

- [`../../evals/palbench/v0.5/asset-usage/r202-official-pal-asset-execution-adoption-matrix.md`](../../evals/palbench/v0.5/asset-usage/r202-official-pal-asset-execution-adoption-matrix.md)
- [`../../evals/palbench/v0.5/asset-usage/r202-official-pal-adoption-gaps-summary.md`](../../evals/palbench/v0.5/asset-usage/r202-official-pal-adoption-gaps-summary.md)
- [`../../evals/palbench/v0.5/asset-usage/r202-quinn-official-pal-adoption-review.md`](../../evals/palbench/v0.5/asset-usage/r202-quinn-official-pal-adoption-review.md)
