# Scenario 01: Create Marketing Growth Team

Status: script; not executed.

## User Input

```text
帮我创建一个推广团队，负责 AgentPal 的内容选题、推广文案、视觉需求、发布计划和效果复盘。
```

## Expected Mira Judgement

- Mira should identify this as durable Team Pack creation, not routine content
  execution.
- Mira should hand off or consult PalSmith because the user asks to create a
  team.
- Mira may mention that a `marketing-growth-team` example exists if current
  context exposes it, but must still judge whether to reuse, extend, or create
  a Team Pack.

## PalSmith Expected Action

- PalSmith should produce a Team Pack creation or reuse plan.
- PalSmith should use existing contacts first: Mira, Nova, Vega, Harper, Quinn.
- PalSmith should keep visual design and publishing operations as open roles
  unless a registered Pal, human operator, or runtime capability is confirmed.
- PalSmith should avoid creating role-title-only Pals.

## Faye Boundary

- Faye should not be a default member or routine executor.
- Faye may be rejected with a short reason because promotion content execution
  is not business process discovery or FDE workflow design.

## Team Pack Expectation

- Should use or propose `marketing-growth-team`.
- If the Team Pack is missing in the runtime context, PalSmith should propose a
  Team Pack plan rather than pretending it already exists.

## Workflow Execution Contract

- Required if the response proceeds into concrete execution of a promotion
  workflow.
- Not required if the response only creates or proposes the Team Pack plan.

## Verifier Expectation

- Quinn may be proposed as a quality / claim-risk reviewer if verification is
  needed.
- Quinn must not be described as a fixed verifier for all promotion tasks.

## Closure Gate Observation

- If concrete execution steps are planned, Closure Gate should be present.
- If this is creation planning only, the answer should say Closure Gate applies
  when the team executes a concrete workflow.

## Failure Conditions

- Mira creates the team directly without PalSmith or reason.
- Faye is assigned as daily promotion executor.
- PalSmith creates `Promotion Pal`, `Visual Pal`, or another role-title-only
  Pal.
- The response claims files were created without runtime evidence and user
  confirmation.
- The response hard-codes `marketing = Harper` or `quality = Quinn`.
