# Release Quality Gate Knowledge

## Concept Explanation

Release quality gate is the decision boundary before publishing, exporting, tagging, shipping, or announcing readiness. It asks whether evidence is strong enough for the intended audience and risk.

## Judgement Standards

- Release scope and target audience are clear.
- Acceptance criteria and DoD are met.
- Test/check evidence exists or not-run is justified.
- Privacy, source, license, and no-code boundaries are checked.
- Rollback or recovery path is known.
- User confirmation is recorded for high-risk release steps.

## Examples

- A Pal Pack release needs JSON parse, no-code boundary, registry consistency, clean export safety, and public/private review.
- A software release needs build/test evidence, release notes, version, artifacts, and rollback.

## Counterexamples

- Local files exist, therefore published.
- Not-run release checks hidden in final report.
- Release without rollback notes.

## Scope

Use before AgentPal RC claims, public docs, Pal exports, product deploys, and external sends.

## How This Becomes Skill, Workflow, Or Eval

It supports `release-quality-gate-skill.md`, `release-quality-gate-workflow.md`, `release-candidate-quality-review-runbook.md`, and `quinn-release-quality-gate-eval.md`.

## Common Mistakes

- Confusing local readiness with public release.
- Treating user desire to publish as evidence.
- Ignoring Rhea safety or PalSmith governance findings.

## Source Refs Or Local Notes

Sources: GitLab releases and release evidence docs, Microsoft deployment gates docs, AgentPal no-code release boundary.
