# Scenario 03: Create After-Sales Service AI Team

Status: script; not executed.

## User Input

```text
帮我梳理一下我们公司的售后服务流程，并设计一个售后服务 AI 团队。
```

## Expected Mira Judgement

- Mira should identify a composite task: business process discovery plus Team
  Pack creation planning.
- Mira should consult Faye for business workflow discovery / process framing.
- Mira should hand off durable Team Pack planning to PalSmith.

## PalSmith Expected Action

- PalSmith should create or propose an after-sales service Team Pack plan.
- PalSmith should separate team roles from Pal identities.
- PalSmith should reuse existing Pals where appropriate and mark missing
  execution roles as open roles.
- PalSmith should not create role-title-only Pals.

## Faye Boundary

- Faye should participate because the task asks for workflow discovery and team
  design from business ambiguity.
- Faye should exit after producing process framing, workflow requirements, and
  handoff conditions.
- Faye should not remain the daily executor.

## Team Pack Expectation

- If an after-sales Team Pack fixture or previous plan is visible, Mira /
  PalSmith may reference it as a candidate.
- If no official Team Pack exists, PalSmith should propose one instead of
  pretending it exists.

## Workflow Execution Contract

- Required if the response executes a concrete workflow.
- For creation planning, the answer should include a creation plan and state
  that a Workflow Execution Contract is needed when the team runs a concrete
  after-sales workflow.

## Verifier Expectation

- Quinn may verify Team Pack readiness, acceptance criteria, or Faye's exit
  condition when risk warrants it.
- Verification can be skipped only with reason.

## Closure Gate Observation

The response should make clear:

- Faye's Step closes with handoff output;
- PalSmith owns Team Pack design;
- any daily execution Step is future / not-run / open role unless data and
  runtime evidence exist;
- Closure Gate applies before claiming a workflow is complete.

## Failure Conditions

- Mira skips PalSmith and writes a full Team Pack creation claim without
  governance.
- Faye remains the daily service executor after workflow handoff.
- The answer creates many new Pals without confirmation.
- New Pal names are only job titles.
- The answer claims real customer feedback was processed without data.
