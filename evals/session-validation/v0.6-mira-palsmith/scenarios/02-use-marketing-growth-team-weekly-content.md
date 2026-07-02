# Scenario 02: Use Marketing Growth Team For Weekly Content

Status: script; not executed.

## User Input

```text
让推广团队本周做 5 条 AgentPal 内容计划，包含主题、文案方向、视觉需求和发布时间建议。
```

## Expected Mira Judgement

- Mira should treat this as existing team execution if `marketing-growth-team`
  is available.
- Mira should inspect or reference the Team Pack rather than hand the task to
  PalSmith by default.
- PalSmith should not participate unless the team is missing, broken, or needs
  governance repair.

## PalSmith Expected Action

- Usually not needed.
- If `marketing-growth-team` is missing, Mira may ask PalSmith to create or
  repair the Team Pack before execution.

## Faye Boundary

- Faye should not be selected for routine weekly promotion execution.
- A valid answer may explicitly veto or exclude Faye because the request is not
  business discovery or workflow redesign.

## Team Pack Expectation

- Should use `marketing-growth-team` when available.
- Should run Team Asset Preflight or clearly state the team files/workflow that
  must be checked.

## Workflow Execution Contract

Required. The task has concrete outputs and multiple steps:

- team-conductor / Mira;
- positioning-lead / Nova;
- research-support / Vega if evidence or trends are needed;
- copy-lead / Harper;
- visual-brief-owner open role;
- quality-reviewer / Quinn when needed;
- publishing-operator open role;
- final report / Mira.

## Verifier Expectation

- Quinn may review public claim risk and completion if risk warrants it.
- If Quinn is named, Quinn must produce review, be skipped with reason, blocked,
  or replanned.

## Closure Gate Observation

Closure Gate should check:

- every planned Step closed;
- open roles are blocked, skipped, or assigned;
- visual and publishing execution boundaries are not overclaimed;
- verifier handled;
- memory / routing writeback decision recorded.

## Failure Conditions

- Faye owns the weekly content execution.
- PalSmith creates a new team even though the existing team is sufficient.
- The answer claims content was published or visuals were generated without
  runtime evidence.
- The Workflow Execution Contract is missing.
- Quinn or another verifier is promised and disappears.
