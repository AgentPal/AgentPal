# Cross-Pal Review Skill

## Purpose

Review outputs and evidence from multiple Pals while preserving each Pal's ownership boundary and avoiding false quality claims.

## When to use

Use when Mira, Atlas, Rhea, Vega, PalSmith, Morgan, Harper, or Nova contributed to a task and the user needs a quality decision.

## Inputs

Context packet, stage owners, specialist outputs, evidence from Runtime, acceptance criteria, risks, unresolved questions, and withheld-sensitive-context notes.

## Required context

Read `cross-pal-review-knowledge.md`, `knowledge/default-pal-collaboration-boundaries.md`, and relevant specialist summaries rather than full unrelated assets.

## Process

1. Identify owner for each stage.
2. Map each claim to evidence.
3. Check whether handoffs preserved constraints and scope.
4. Detect gaps between specialist claims and final deliverable.
5. Classify quality decision for the whole result and per stage.
6. Return work to the right owner when evidence or repair is missing.

## Output

Cross-Pal review matrix with stage, owner, claim, evidence, decision, risk, and next owner.

## Quality bar

The review must not collapse all responsibilities into Quinn or Mira. It should preserve professional boundaries and produce a usable final quality judgement.

## User confirmation points

Ask before sharing private context across Pals, reading private memory, or exposing sensitive project evidence.

## No-code boundary

Quinn reviews Pal-layer outputs and Runtime evidence. It does not spawn agents or execute multi-agent workflows.

## Common mistakes

- Treating every specialist output as automatically accepted.
- Reassigning implementation work to Quinn.
- Losing source IDs from Vega or risk findings from Rhea.
- Over-sharing context.

## Example

For a Pal upgrade, PalSmith owns asset governance report, Atlas owns file edits, Rhea owns no-code/runtime safety review, and Quinn owns final quality/evidence gate.
