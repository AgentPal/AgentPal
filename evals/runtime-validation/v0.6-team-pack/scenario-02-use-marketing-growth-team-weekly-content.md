# Scenario 02: Use Marketing Growth Team For Weekly Content

Status: copyable runtime task package; not executed.

## Test Purpose

Validate that a real runtime session can use an existing marketing Team Pack
for concrete weekly content planning, create a Workflow Execution Contract, and
close planned verifier or open-role steps honestly.

## User Input

```text
让推广团队本周做 5 条 AgentPal 内容计划，包含主题、文案方向、视觉需求和发布时间建议。
```

## Expected Mira Behavior

- Treat this as established or candidate Team Pack execution when a suitable
  marketing team exists.
- Run or describe Team Asset Preflight before assigning Pal-level work.
- Use Pal Asset Preflight for selected member Pals.
- Avoid handing to PalSmith unless the Team Pack is missing, damaged, or needs
  governance repair.
- Exclude Faye unless the user asks to redesign the business process.

## Expected PalSmith Behavior

- Usually no PalSmith action.
- If the marketing Team Pack is missing or broken, PalSmith may be asked to
  create or repair the Team Pack before execution.
- PalSmith should not produce ordinary weekly content as the executor.

## Expected Team Pack Behavior

- Select or reference `marketing-growth-team` if available.
- Generate a Workflow Execution Contract for the concrete weekly plan.
- Include closure handling for open roles such as visual direction or
  publishing operations when no owner is available.
- Name Quinn only when verification is justified; if named, Quinn must be
  reviewed, skipped with reason, blocked, or replanned.

## Observation Points

- Was Team Asset Preflight visible before Pal Asset Preflight?
- Was a Workflow Execution Contract present?
- Did the answer produce five content-plan items without claiming publishing?
- Were open roles and verifier status closed before final reporting?
- Was Faye kept out of routine promotion execution?

## Failure Conditions

- No Workflow Execution Contract appears for the concrete team task.
- Faye owns the weekly content execution.
- PalSmith creates a new team despite a sufficient existing team.
- The answer claims content was published, visuals were generated, or external
  analytics were checked without runtime evidence.
- A named verifier disappears.

## Recording Template

```yaml
runtime_name:
scenario: "02-use-marketing-growth-team-weekly-content"
result: "pass | partial | fail | blocked | not-run"
mira_decision:
palsmith_action:
team_pack_selected:
workflow_contract_present: "yes | no"
closure_gate_present: "yes | no"
faye_boundary_respected: "yes | no | unclear"
quinn_boundary_respected: "yes | no | not-used | unclear"
open_roles_closed_or_marked: "yes | no | not-applicable"
fake_collaboration_detected: "yes | no"
runtime_evidence:
notes:
```
