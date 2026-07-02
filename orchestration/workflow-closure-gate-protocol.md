# Workflow Closure Gate Protocol

Status: v0.6 no-code protocol foundation
Runs before: Any final report that claims a Workflow Execution Contract is complete

The Closure Gate checks that the workflow actually closed. It is a gate, not a semantic router.

## Inputs

The gate reads:

- Workflow Execution Contract
- Step state ledger
- child Step state ledger
- Context Access List references and usage summaries
- owner outputs
- verifier outputs
- runtime / skill / plugin / MCP evidence, when used
- blocked, skipped, cancelled, failed, and replanned reasons
- memory writeback decision

## Mandatory Checks

### 1. All Steps Are Closed

Every Step and child Step must be in a closed status:

- `done` when verification was not required
- `verified`
- `failed`
- `blocked`
- `skipped`
- `cancelled`
- `replanned`

Open statuses fail the Closure Gate:

- `planned`
- `assigned`
- `accepted`
- `running`
- `review_required`

### 2. Required Steps Completed Or Terminally Closed

Every required Step must either:

- satisfy its output contract, or
- be terminally closed with `failed`, `blocked`, `skipped`, `cancelled`, or `replanned` and an explicit reason.

The final report must not hide required incomplete work inside "next steps".

### 3. Verifiers Actually Output Review

For every Step with `verification_required: true`, the gate must find one of:

- `verified` plus verifier output
- `failed` plus verifier or owner failure reason
- `blocked` plus missing evidence or unavailable verifier reason
- `skipped` plus legal skip reason
- `replanned` plus replacement verifier Step or Workflow reference

If a named verifier appears in the contract, that verifier cannot disappear. The verifier Step must close through one of the states above.

### 4. Skipped Steps Have Reasons

Every `skipped` Step must include:

- skip reason
- decision owner
- effect on user goal
- whether any replacement Step is needed

Skipped verification must be reported as skipped, not as passed.

### 5. Blocked Steps Are Reported To The User

Every `blocked` Step must include:

- blocker reason
- missing input, permission, runtime, evidence, or decision
- impact on final deliverable
- suggested unblock path, if known

A workflow with blocked required work may still produce a final report, but the report must be marked incomplete or blocked.

### 6. Child Steps Return To Parent

Every child Step must:

- reference `parent_step_id`
- be closed before the parent is marked `done`
- return output, evidence, blocker, skip reason, or replan note to the parent
- be summarized by the parent Step

If a child Step is open, the parent Step is open. If a child Step terminally closes without useful output, the parent Step must say how it handled that result.

### 7. Memory / Routing Writeback Is Decided

The gate must record whether writeback is:

- `none`
- `candidate`
- `written`
- `blocked`

Possible writeback targets:

- Pal Memory
- Team Memory
- Routing Memory
- Runtime Skill usage memory
- Verification memory

Writeback must obey memory privacy and public-release boundaries. The gate may recommend a writeback candidate without performing it.

## Context Boundary Check

For each Step, the gate should confirm:

- the Step references a Context Access List
- reported reads are within the allowed list
- parallel reviewers did not read each other's drafts unless explicitly allowed
- the summary stage read final outputs or allowed summaries, not all drafts by default

If exact read evidence is unavailable, report `not-run`, `unknown`, or `runtime-unavailable`; do not invent proof.

## Final Report Requirements

The final report must state:

- user goal
- selected mode
- team or no-team status
- actual participants
- completed Steps
- skipped Steps
- blocked Steps
- failed Steps
- replanned Steps
- verifier results
- runtime / skill / plugin / MCP usage
- context boundary notes
- memory writeback decision
- remaining risks
- recommended next step

Do not list a Pal, Team, Runtime, Skill, plugin, MCP tool, or verifier as an actual participant unless it produced output, evidence, blocker, skip reason, cancellation, or replan record.

## Gate Outcomes

Use one of these outcomes:

- `pass`: all required work is closed and verification requirements are satisfied or legally skipped.
- `partial`: useful deliverables exist, but one or more optional or non-critical Steps closed as skipped, blocked, failed, cancelled, or replanned.
- `blocked`: required work cannot close without user input, missing evidence, permission, or runtime capability.
- `fail`: required work failed acceptance criteria and no accepted repair or replan is available.

Only `pass` may be described as complete workflow closure.

`partial`, `blocked`, and `fail` must be reported honestly before or inside the final answer.
