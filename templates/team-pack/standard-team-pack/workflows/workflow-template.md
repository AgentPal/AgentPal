# <workflow-id>

## Purpose

Describe the task family this workflow supports.

## Use When

- `<condition>`

## Do Not Use When

- `<condition>`

## Default Roles

- coordinator
- owner
- verifier

## Steps

1. Understand the user goal.
2. Select relevant team assets.
3. Assign roles from `roster.json`.
4. Generate or update a Workflow Execution Contract using `templates/orchestration/workflow-execution-contract.md`.
5. Run Pal Asset Preflight before each assigned Pal Step.
6. Produce the requested output.
7. Review against team evals when verification is required.
8. Run the Closure Gate before the final report.
9. Report completed, skipped, blocked, failed, replanned, and follow-up items.

## Output Contract

- `<required output>`

## Review

Link to `evals/definition-of-done.md`.

## Workflow Execution Contract

Use:

- `orchestration/workflow-execution-contract-protocol.md`
- `templates/orchestration/workflow-execution-contract.md`
- `orchestration/workflow-closure-gate-protocol.md`

Every non-trivial Step should reference a Context Access List.
