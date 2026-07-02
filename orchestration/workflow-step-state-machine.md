# Workflow Step State Machine

Status: v0.6 no-code protocol foundation
Applies to: Workflow Execution Contract Steps and child Steps

Every Step in a Workflow Execution Contract must have exactly one current status. Status is an audit field, not a semantic route.

## Status Table

| Status | Meaning | Enters When | Exits When | Final-Closed? | Reason Required? | Allowed Before Complete Final Report? |
| --- | --- | --- | --- | --- | --- | --- |
| `planned` | Step is drafted but not assigned. | The contract lists a needed Step or candidate. | It becomes assigned, skipped, cancelled, or replanned. | No | No, unless skipped/cancelled/replanned next. | No |
| `assigned` | A primary assignee is selected. | Owner or conductor assigns the Step. | Assignee accepts, runs, blocks, skips, cancels, or replans. | No | No | No |
| `accepted` | Assignee acknowledges the Step and scope. | Assignee agrees to own the Step under the given context and output contract. | Work starts, blocks, skips, cancels, or replans. | No | No | No |
| `running` | Step is actively being worked. | Assignee starts producing output or using the execution layer. | Output is done, review is required, fails, blocks, cancels, or replans. | No | No | No |
| `done` | Assignee completed the Step output. | Output contract is satisfied by the assignee. | If verification is required, it enters review_required or verified; otherwise it may close. | Yes only when verification is not required. | Evidence or output summary required. | Yes only when verification is not required. |
| `review_required` | Step output is waiting for verifier review. | Step is done and `verification_required: true`. | Verifier passes, fails, blocks, skips with reason, or replans review. | No | No | No |
| `verified` | Required verification passed. | Verifier produces a result mapped to evidence and criteria. | Terminal unless later reopened by explicit replan. | Yes | Verifier output required. | Yes |
| `failed` | Step output or verification did not satisfy criteria. | Assignee or verifier finds unmet requirements. | Terminal if final report states failure, or replanned to a replacement Step. | Yes with failure report. | Failure reason required. | Yes only if user is told it failed. |
| `blocked` | Step cannot proceed within current constraints. | Required input, permission, runtime, evidence, or decision is unavailable. | Terminal if reported, or replanned when a path exists. | Yes with blocker report. | Blocker reason required. | Yes only if user is told it is blocked. |
| `skipped` | Step is intentionally not executed. | Owner or conductor decides it is unnecessary or unavailable. | Terminal. | Yes | Skip reason required. | Yes |
| `cancelled` | Step is intentionally stopped. | User, owner, or conductor cancels the Step. | Terminal. | Yes | Cancel reason required. | Yes |
| `replanned` | Step is replaced by another Step or Workflow. | Current path is no longer valid. | Terminal only when replacement is identified or impossible replacement is reported. | Yes with replacement or reason. | Replan reason and replacement reference required when available. | Yes |

## Closed Statuses

The Closure Gate treats these as closed when their required evidence fields are present:

- `done` when `verification_required: false`
- `verified`
- `failed`
- `blocked`
- `skipped`
- `cancelled`
- `replanned`

`planned`, `assigned`, `accepted`, `running`, and `review_required` are open statuses and must not remain before a complete final report.

## Required Transition Rules

Allowed common transitions:

- `planned` -> `assigned`
- `planned` -> `skipped`
- `planned` -> `cancelled`
- `planned` -> `replanned`
- `assigned` -> `accepted`
- `assigned` -> `running`
- `assigned` -> `blocked`
- `assigned` -> `skipped`
- `assigned` -> `cancelled`
- `assigned` -> `replanned`
- `accepted` -> `running`
- `accepted` -> `blocked`
- `accepted` -> `skipped`
- `accepted` -> `cancelled`
- `accepted` -> `replanned`
- `running` -> `done`
- `running` -> `failed`
- `running` -> `blocked`
- `running` -> `cancelled`
- `running` -> `replanned`
- `done` -> `review_required`
- `done` -> `verified` only when verifier output is already attached
- `review_required` -> `verified`
- `review_required` -> `failed`
- `review_required` -> `blocked`
- `review_required` -> `skipped`
- `review_required` -> `replanned`

Direct shortcuts are allowed only when the final record still contains the missing evidence. Example: a tiny Step may move from `assigned` to `done` if the assignee output is recorded in the same update.

## Reason And Evidence Fields

These statuses require a written reason:

- `failed`
- `blocked`
- `skipped`
- `cancelled`
- `replanned`

These statuses require output or evidence:

- `done`
- `verified`
- `failed`
- `blocked`

These events require a written reason even if the final status is closed:

- verifier skipped
- verifier changed
- assignee changed after assignment
- child Step cancelled or replanned
- parent Step marked done after a child Step failed, blocked, skipped, or replanned

## Verification Rules

If `verification_required: true`, `done` is not enough for final closure. The Step must become one of:

- `verified` with verifier output
- `failed` with verifier or owner failure reason
- `blocked` with missing evidence or unavailable verifier reason
- `skipped` with an explicit reason that verification was legally skipped
- `replanned` with a replacement verifier Step or Workflow

`verified` is invalid without verifier output. A verifier name in a plan is not verifier participation.

## Child Step Rules

Parent and child Steps each use this same state machine.

- A required child Step in an open status keeps the parent Step open.
- A parent Step may become `done` only after all required child Steps are closed.
- If a child Step closes as `failed`, `blocked`, `skipped`, `cancelled`, or `replanned`, the parent Step must record the effect on its own output.
- Child Step output returns to the parent through the parent Step's allowed context, not through broad draft sharing.

## Final Report Rule

Before a complete final report, no Step may remain in:

- `planned`
- `assigned`
- `accepted`
- `running`
- `review_required`

If any such Step remains, the final report must say the workflow is incomplete or blocked. It may not say the workflow fully completed.
