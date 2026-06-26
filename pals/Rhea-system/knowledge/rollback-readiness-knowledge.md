# rollback-readiness-knowledge

## Concept Explanation

Rollback readiness checks whether a change can be reversed or recovered from and whether the recovery path has enough evidence to trust.

## Judgement Standards

- Identify previous known-good state.
- Identify tracked, untracked, ignored, generated, and external state.
- Identify who can perform rollback.
- Identify backup or archive.
- Identify rollback test or post-rollback evidence.
- Mark missing or untested rollback as risk.

## Examples

- Tracked Markdown edit: git diff can show rollback target.
- Untracked new files: need explicit cleanup or archive plan.
- Deployment: use known previous successful deployment where available.

## Counterexamples

- "Git can undo it" when files are untracked.
- Rollback plan depends on unavailable artifacts.

## Scope

Use for releases, Pal Pack changes, dependency changes, system configuration, and file operations.

## How This Becomes Skill, Workflow, Or Eval

Skill: rollback-readiness-review. Runbook: rollback-readiness. Eval: release safety.

## Common Mistakes

Ignoring untracked files, assuming backup is tested, and not naming rollback authority.

## Source Refs Or Local Notes

Based on Google canary and GitLab deployment/rollback sources SRC-01, SRC-12, and SRC-13.

