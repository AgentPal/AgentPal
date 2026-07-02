# Workflow Execution Contract Protocol

Status: v0.6 no-code protocol foundation
Scope: Workflow Plan -> Execution Contract -> Step tracking -> Closure Gate -> Final report -> Memory / Routing writeback

This protocol turns a workflow from advisory planning text into a closeable execution record.

It does not create a background runner, database, CLI, GUI, MCP layer, subagent launcher, or automatic multi-agent execution system. The current host Runtime still performs any real file, command, tool, or publication action. AgentPal records the Pal-layer judgement, assignments, context boundaries, verification decisions, and closure evidence.

## Core Rule

If a Pal, Team, Runtime, Skill, plugin, MCP tool, or verifier is written into a Workflow Execution Contract, that entry must later be one of:

- completed
- verified
- failed
- blocked
- skipped with a reason
- cancelled with a reason
- replanned with a replacement Step or Workflow

No planned participant may disappear silently.

## Workflow Plan vs Execution Contract

| Item | Workflow Plan | Workflow Execution Contract |
| --- | --- | --- |
| Purpose | Describe a possible route. | Track what must close before the final report. |
| Timing | Before execution or as a lightweight planning artifact. | Before multi-step execution, verifier use, or any claim that named participants will act. |
| Assignees | May contain candidates. | Contains assigned participants or explicit pending assignments. |
| Verifiers | May propose verifier candidates. | If `verification_required: true`, verifier output or a closure-status reason is mandatory. |
| Context | May name likely sources. | Each Step references a Context Access List. |
| Status | Not a ledger. | Step state machine ledger. |
| Final report impact | Helpful background. | Closure Gate input; incomplete Steps block a complete final report. |

A plan can remain optional. A contract is binding once used for the current task.

## When Fast Route Is Enough

Use Fast Route instead of a full Workflow Execution Contract when all conditions are true:

- The task has one clear owner Pal by current AI judgement.
- The work is low-risk and does not require staged coordination.
- No verifier is selected or promised.
- No Team, Runtime, Skill, plugin, MCP tool, or child Step needs separate tracking.
- The final answer does not claim independent review or multi-participant execution.

Fast Route may still use a small Task Package or Context Packet when helpful, but it does not need the full Step ledger.

## When Deep Conductor Or Full Contract Is Needed

Create a Workflow Execution Contract when any condition is true:

- Multiple Pals, Teams, Runtimes, Skills, plugins, MCP tools, or stages are named as participants.
- A verifier is selected, promised, or materially needed for false-completion risk.
- The deliverable has dependencies that can leave hidden unfinished work.
- The task is medium or high risk, release-facing, user-data-sensitive, or safety-sensitive.
- A child Step is created because another Pal or execution layer is needed.
- The user asks for a complete workflow, staged report, or auditable collaboration record.
- A Deep Conductor-style plan is used beyond a lightweight explanation.

Deep Conductor remains a no-code mode-decision and workflow protocol unless the current host Runtime provides explicit execution capability.

## Verifier Decision

Verifier selection is always case-by-case. Do not hard-code Quinn, any other Pal, or any task type as the verifier route.

### Verifier Usually Required

The Owner Pal or Mira should consider verification when:

- The task can falsely appear complete.
- The work changes release content, public docs, safety boundaries, or user-visible behavior.
- The user asked for review, validation, acceptance, or release readiness.
- A Runtime, Skill, plugin, MCP tool, or external evidence claim needs checking.
- The selected Workflow topology includes an Owner + Verifier or Plan -> Execute -> Verify stage.
- The owner judgement identifies a material risk that benefits from independent review.

### Verifier May Be Skipped

Verification may be legally skipped when:

- The task is low-risk and single-owner.
- The user requested a quick answer, explanation, or draft only.
- No completion, publication, release, or independent-review claim is made.
- The needed evidence is unavailable and the final report honestly marks the risk or blocker.
- The selected owner judges that verification cost would not improve the outcome, and records why.

Skipping verification requires:

```yaml
verification_required: false
verifier_role: null
verifier_pal: null
skip_reason: "<why verifier was not needed or could not be used>"
```

Skipping verification must not be described as passed verification.

### Verifier Change

If a verifier changes after being written into the contract:

- The original verifier Step becomes `replanned`, `blocked`, `cancelled`, or `skipped`.
- `replan_reason` or `skip_reason` records why.
- The replacement verifier receives a new Step ID or replacement workflow reference.
- The final report states both the original and replacement verification path.

## Step Assignment

Each Step has exactly one primary assignee. The assignee can be a Pal, Team, Runtime, Skill, plugin, MCP tool, coordinator role, or human role.

Allowed `assignee_type` values:

- `pal`
- `team`
- `runtime`
- `skill`
- `plugin`
- `mcp`
- `coordinator`
- `human`
- `role`

Runtime, Skill, plugin, and MCP assignees are execution layers or capabilities, not Pal owners. When they produce implementation-shaped or evidence-shaped output, the contract should still record the Pal-layer owner who requested and interprets that output.

Assignment must be a current AI judgement using current contacts, available evidence, and task context. Capability notes and memory may inform judgement, but they are not fixed routes.

## Context Access List Linkage

Every non-trivial Step must reference a Context Access List ID.

Rules:

- A Step may read only the files, summaries, previous outputs, and memory explicitly allowed by its Context Access List.
- Parallel reviewers default to isolation and should not read each other's drafts unless the contract grants access.
- The summary stage reads final reports or designated outputs, not every private draft by default.
- Child Steps inherit only the parent context that is explicitly passed into the child Context Access List.
- Runtime output does not expand context access for later Steps unless the contract updates the relevant Context Access List.

This protocol supplements `context-access-list-protocol.md`; it does not replace Context Slicing or Context Packet rules.

## Child Steps

A child Step is required when a current Step discovers that another Pal, Team, Runtime, Skill, plugin, MCP tool, or verifier must produce separate output.

Do not say "let X handle it" without creating or referencing a child Step in the contract.

Child Step requirements:

- `parent_step_id` points to the parent.
- The child has its own `step_id`, `assignee_type`, `assignee_id`, status, Context Access List, and output contract.
- The child inherits only the parent context explicitly listed in the child Context Access List.
- The child returns an output summary, evidence, blocker, or replan note to the parent.
- The parent Step cannot become `done` while required child Steps are still open.
- If the child is skipped, blocked, cancelled, failed, or replanned, the parent must record how that affects its own output.

## Replanning

Use `replanned` when the current Step should no longer be executed as written.

Required fields:

```yaml
status: replanned
replan_reason: "<why the old step is no longer the right path>"
replacement_step_id: "<new step id>"
replacement_workflow_id: "<new workflow id, if applicable>"
```

A replanned Step is closed only when it points to a replacement Step or Workflow, or when the final report states that no replacement is possible and why.

## Runtime And Skill Output

When a Runtime, Skill, plugin, MCP tool, or command is used:

- The Step records the execution layer and evidence available to the current host.
- The Pal-layer owner remains responsible for interpreting whether the output satisfies the user goal.
- The contract must not claim execution that the current host did not perform or observe.
- If execution is unavailable, the Step becomes `blocked`, `skipped`, or `replanned`; it must not be silently omitted.

## Writeback

After Closure Gate, the final report may propose or perform memory writeback according to existing memory boundaries.

Possible writeback targets:

- Pal Memory
- Team Memory
- Routing Memory
- Runtime Skill usage memory
- Verification memory

Writeback is not automatic. The final report must state:

- `none`: no writeback needed.
- `candidate`: writeback is recommended but not performed.
- `written`: writeback was performed with evidence and allowed scope.
- `blocked`: writeback could not be performed and why.

Do not write private user memory, secrets, unverified facts, or temporary development notes into public release files.

## Required Closure

Before any final report that claims the workflow is complete, run the Closure Gate defined in `workflow-closure-gate-protocol.md`.

If Closure Gate fails, the response may still be useful, but it must be labeled as incomplete, blocked, partially complete, or requiring user decision. It must not claim complete workflow closure.
