# Team Asset Preflight Protocol

Status: v0.6 current protocol draft. Markdown / JSON protocol only; this does not implement a scheduler, background service, scanner, CLI, UI, or automatic multi-Agent runtime.

## Purpose

Team Asset Preflight prepares a team task before individual Pal work begins.

It answers:

- Is this task using a Team Pack?
- Which team assets govern the work?
- Which team workflow, eval, memory, and routing card apply?
- Which member Pals must run their own Pal Asset Preflight?
- What Workflow Execution Contract will be used to close every planned step?

## When To Use

Use Team Asset Preflight when the user explicitly names a team, asks for a stable business workflow, invokes a Team Pack, or the Owner Pal judges that the task is better handled by a known team rather than ad hoc single-Pal work.

If no Team Pack applies, record `team_context: none` and continue with Pal Asset Preflight.

## Team Read Order

When a Team Pack is used, read in this order:

1. User current instruction.
2. Current project constraints and binding context.
3. `TEAM.md`.
4. `team.json`.
5. `roster.json`.
6. Team workflow index and the selected workflow.
7. Team eval / definition-of-done assets.
8. Team knowledge, Skills, and runbooks selected from their indexes.
9. Team memory selected by approved scope.
10. Member Pal root entries and each member's Pal Asset Preflight.

Do not load every team asset by default. Use indexes first and select only assets that shape the current task.

## Required Team Files

For v0.6 planning, a Team Pack may be incomplete, but Team Asset Preflight should look for:

- `TEAM.md`
- `team.json`
- `roster.json`
- `workflows/index.md`
- selected workflow file
- `knowledge/index.md`
- `skills/index.md`
- `runbooks/index.md`
- `memory/README.md` or `memory/index.md`
- `evals/definition-of-done.md`
- routing card or capability card, if present

Missing files are reported as `missing`; they are not silently substituted.

## Workflow Selection

Select a team workflow when:

- it matches the task goal;
- it is within the team's purpose;
- it has compatible roles or member Pals;
- it has clear completion and verification expectations.

If the workflow exists but is incomplete, generate a limited Workflow Execution Contract and mark missing workflow assets.

## Workflow Execution Contract

Team Asset Preflight produces a Workflow Execution Contract before member Pals begin.

Use the canonical contract protocol and template:

- `orchestration/workflow-execution-contract-protocol.md`
- `orchestration/workflow-step-state-machine.md`
- `orchestration/workflow-closure-gate-protocol.md`
- `templates/orchestration/workflow-execution-contract.md`

The Team-specific template at `templates/team/workflow-execution-contract.md`
is only a wrapper that points Team tasks to the canonical orchestration
contract.

The contract records:

- task goal;
- selected team and workflow;
- team assets loaded;
- steps and owners;
- verifier or verification rule;
- required child steps;
- required Pal Asset Preflight per member;
- expected outputs;
- status labels for every step;
- Closure Gate outcome before the final report.

This contract is a no-code task record. It follows the v0.6 Step state machine
and Closure Gate. Planned steps must close as `done`, `verified`, `failed`,
`skipped`, `blocked`, `cancelled`, or `replanned`; open statuses must not remain
before a complete final report.

## Member Pal Preflight

After Team Asset Preflight, each assigned member Pal runs `core/pal-asset-preflight-protocol.md`.

Team assignment does not override Pal boundaries. If a member Pal cannot do the assigned step, the Owner Pal or team conductor must replan.

## Team Memory Boundary

Team memory may shape recurring workflow decisions, but it must be scoped:

- read public-safe or approved project/team memory only;
- do not expose private user memory in public reports;
- do not treat stale memory as current fact;
- do not write memory without the current writeback policy and user approval when needed.

## Required Fields

Use `templates/team/team-asset-preflight.md` for explicit evidence.

Minimum fields:

- `team_id`
- `task_summary`
- `team_pack_used`
- `team_files_checked`
- `selected_workflow`
- `team_assets_required`
- `team_assets_missing`
- `workflow_execution_contract`
- `member_pal_preflights_required`
- `verification_required`

## Failure Cases

Mark the team task as blocked, partial, or needing replan when:

- the task claims to use a team but no Team Pack can be found;
- a workflow is named but not loaded;
- a planned member Pal step has no Pal Asset Preflight;
- a verifier is named but not assigned a real verification step;
- team memory or evals are needed but missing;
- a Pal boundary conflicts with the team assignment.
