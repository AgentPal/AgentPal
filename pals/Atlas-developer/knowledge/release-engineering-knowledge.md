# Release Engineering Knowledge

## Concept explanation

Release engineering prepares software changes for reliable delivery. It values repeatable checks, traceable artifacts, release notes, version state, rollback planning, and clear evidence.

## Judgement standards

- Release readiness is the lowest state proven by evidence.
- Build/test/check evidence must be tied to the target release scope.
- Version, artifacts, docs, changelog, and rollback notes should be checked when relevant.
- Publishing, tagging, pushing, or deploying requires explicit user confirmation.

## Examples

- Good: "Ready for local RC review; remote release not proven."
- Good: "No publish claim because no tag or release artifact evidence exists."
- Good: "Quinn should review quality gate before release decision."

## Counterexamples

- Bad: Docs consistency alone means release-ready.
- Bad: Tagging or pushing from a planning request.
- Bad: Hiding dirty worktree or not-run checks.

## Scope

Use for release candidate checks, package readiness, merge readiness, publish planning, and rollout reports.

## How it becomes skill / workflow / eval

Use with `release-engineering-skill.md`, `release-readiness-workflow.md`, `release-candidate-review-runbook.md`, and `atlas-release-readiness-eval.md`.

## Common mistakes

- Overclaiming publish state.
- Missing rollback.
- Forgetting environment owner or quality owner.
- Treating local validation as remote proof.

## Source references or local notes

External: A11 and A12. Local: AgentPal release boundary instructions.
