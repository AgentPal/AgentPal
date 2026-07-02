# 07 Test Workflow Execution Contract

## Goal

Verify that work assigned to Pals or roles is recorded in a Workflow Execution Contract.

## Prompt

```text
请用已有推广团队帮我设计下周 5 条 AgentPal 内容计划。请输出 Workflow Execution Contract，列出每个 step 的 owner、输出、verification_required、状态和 skip/replan 记录。
```

## Expected Result

The output should include:

```text
workflow_id:
selected_team:
owner:
steps:
  - id:
    name:
    assignee:
    output_contract:
    verification_required:
    status:
    skip_reason:
    replan_note:
```

## Required Behavior

- Every step has an owner or `open_role`.
- Selected Pals have visible output or an explicit skipped / blocked reason.
- Verifier has verification output when verification is required.
- Replan is recorded when ownership or scope changes.
- Daily team execution does not default to Faye.

## Fail Signals

- Steps have no owner.
- Pal is assigned but no output appears.
- Verifier is named but disappears.
- Skipped work has no reason.
- The answer says completed while required steps are missing.
