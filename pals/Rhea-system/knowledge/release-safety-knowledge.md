# release-safety-knowledge

## Concept Explanation

Release safety checks whether a release claim is supported by repeatable evidence, no-code boundary, private/public boundary, status, and recovery path.

## Judgement Standards

- Define release scope.
- Verify required checks and what each proves.
- Mark not-run checks.
- Report dirty worktree or missing publish evidence.
- Confirm no private material in public artifacts.
- Confirm rollback or recovery route.

## Examples

- A Markdown/JSON Pal release may need JSON parse, no-code scan, diff check, status, source inventory, and self-health report.

## Counterexamples

- "Docs look good, so publish-ready."
- Ignoring untracked files.

## Scope

Use for AgentPal release candidates, Pal Pack upgrades, exports, and publish claims.

## How This Becomes Skill, Workflow, Or Eval

Skill: release-safety-review. Workflow: release-safety-review. Runbook: release-preflight-risk.

## Common Mistakes

Treating partial checks as full release safety, ignoring private reports, and omitting rollback.

## Source Refs Or Local Notes

Based on Google SRE release sources SRC-01 and SRC-02, GitLab deployment rollback SRC-12, and cloud.gov repo best practices SRC-14.

