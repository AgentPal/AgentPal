# Release Readiness Workflow

## Trigger

User asks whether work is ready to release, merge, tag, package, publish, or deploy.

## Inputs

- Release scope.
- Changed files and artifacts.
- Test/build/check evidence.
- Documentation and changelog state.
- Version, tag, package, or deployment expectations.
- Rollback and risk notes.

## Steps

1. Identify release target and non-goals.
2. Check implementation evidence.
3. Check test and regression evidence.
4. Check docs, changelog, version, artifacts, and rollback notes when relevant.
5. Consult Quinn for quality gate when needed.
6. Consult Rhea for environment/deployment risk when needed.
7. Report lowest proven readiness state.

## Decision points

- Is this local readiness, merge readiness, release candidate, or publish readiness?
- Are remote state, tag, artifact, or deployment evidence required?
- Are any checks not-run?
- Is user confirmation required for release action?

## Outputs

Release readiness report, blocker list, not-run list, and next task package.

## Quality checks

- No publish claim without publish evidence.
- Dirty worktree and missing artifacts are visible.
- Quality and environment owners are considered.
- Rollback path is present where relevant.

## Required user confirmation

Required before staging, commit, tag, push, publish, deploy, version bump, or release artifact modification.

## Evidence to return

Return commands/checks, artifacts, docs links, version/tag state, Git status, not-run checks, and risks.
