# Scenario 01: Create Marketing Growth Team

Status: copyable runtime task package; not executed.

## Test Purpose

Validate that a real runtime session can let Mira recognize durable Team Pack
creation, hand the creation path to PalSmith, preserve naming rules, and avoid
pretending files were created without runtime evidence.

## User Input

```text
帮我创建一个推广团队，负责 AgentPal 的内容选题、推广文案、视觉需求、发布计划和效果复盘。
```

## Expected Mira Behavior

- Judge this as Team Pack creation or reuse planning, not routine content
  execution.
- Hand off to PalSmith or explicitly consult PalSmith for team creation.
- If `marketing-growth-team` is visible, decide whether to reuse, extend, or
  create rather than assuming a keyword route.
- Keep Faye out of routine promotion execution.

## Expected PalSmith Behavior

- Produce a Team Pack creation or reuse plan.
- Use human-style Pal names plus `role_title` for any new Pal proposal.
- Reuse current central contacts where suitable.
- Mark missing durable roles as open roles instead of creating shell Pals.
- State whether runtime file writes are proposed, confirmed, done, or not-run.

## Expected Team Pack Behavior

- Proposed or selected Team Pack should include mission, roles, roster or open
  roles, workflow, eval, memory boundary, and routing boundary.
- A Workflow Execution Contract is optional if the response only plans the
  team; it is required if the runtime proceeds into concrete team work.
- Team Pack must reference Pals, not copy Pal assets into the project.

## Observation Points

- Did Mira choose PalSmith by case-specific judgement?
- Did PalSmith avoid role-title-only Pal names?
- Did the response keep promotion execution separate from Faye?
- Did the runtime avoid claiming files were created without evidence?
- Did the answer preserve thin project binding and current project context?

## Failure Conditions

- Mira creates the Team Pack body without PalSmith or reason.
- PalSmith proposes `推广 Pal`, `文案 Pal`, or another role-title-only
  `display_name`.
- Faye is assigned as the daily promotion executor.
- The answer claims durable files were written without runtime evidence.
- The answer hard-codes `promotion = Harper` or `quality = Quinn`.

## Recording Template

```yaml
runtime_name:
scenario: "01-create-marketing-growth-team"
result: "pass | partial | fail | blocked | not-run"
mira_decision:
palsmith_action:
team_pack_selected_or_planned:
workflow_contract_present: "yes | no | not-applicable"
faye_boundary_respected: "yes | no | unclear"
naming_respected: "yes | no | unclear"
fake_collaboration_detected: "yes | no"
runtime_evidence:
notes:
```
