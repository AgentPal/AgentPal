# Asset Execution Example

## Status

phase: phase_2_task_asset_packet_example
verified_executable_pal: false
full_asset_usage_regression: not_yet

This example shows how Atlas should prepare a development Runtime Task Package.
It is not a completed development task and not a representative host
regression.

## Example Task

User says:

```text
给 AgentPal 增加一个文档索引检查脚本，帮我写开发提示词给 Codex。
```

## Asset Loading Gate

target_pal: Atlas

task_type: development task package / no-code boundary review

required_assets:

- `official/pals/Atlas-developer/PAL.md`
- `official/pals/Atlas-developer/pal.json`
- `official/pals/Atlas-developer/SKILL.md`
- `official/pals/Atlas-developer/core/output-contract.md`
- `official/pals/Atlas-developer/skills/runtime-task-package-writing-skill.md`
- `official/pals/Atlas-developer/workflows/implementation-task-package-workflow.md`
- `core/pal-asset-execution-contract.md`
- `core/asset-loading-gate.md`
- current AgentPal no-code boundary instructions

go_no_go_decision: `go_asset_grounded`

reasoning_summary: The user asks for a development prompt, not direct code
implementation. Atlas must preserve AgentPal's no-code boundary and produce a
bounded Codex task package with forbidden changes and evidence requirements.

## Task Asset Packet

task_id: atlas-doc-index-check-task-package-example

target_pal: Atlas

task_type: development Runtime Task Package

user_goal: write a Codex task prompt for a document index check script

execution_mode: no-code development planning and handoff prompt

required_identity_assets:

- Atlas root identity and boundary

required_knowledge_assets:

- developer role and no-code AgentPal boundary

required_skill_assets:

- `skills/runtime-task-package-writing-skill.md`

required_workflows:

- `workflows/implementation-task-package-workflow.md`

required_runtime_policy:

- Codex is execution runtime; Atlas does not write or run code directly

required_memory_scope:

- no private project memory in public prompt

required_eval_assets:

- acceptance criteria and not-run reporting requirements

optional_tools:

- none for the prompt-only phase

loaded_assets:

- Atlas root entry assets
- output contract
- runtime task package writing skill
- implementation task package workflow
- Pal Asset Execution Contract
- Asset Loading Gate

missing_assets:

- user confirmation if the request changes from prompt writing to actual code
  writing

allowed_tool_calls:

- none required for the example

blocked_tool_calls:

- adding runtime code without explicit user confirmation
- installing dependencies
- broad repository rewrites
- release or remote Git actions

go_no_go_decision: `go_asset_grounded`

## Expected Execution

Atlas should output a Codex-ready task prompt with:

- goal and non-goals;
- files to read;
- files allowed to edit;
- forbidden files and forbidden behavior;
- acceptance criteria;
- verification commands or manual evidence;
- final report format;
- stop conditions if the task conflicts with AgentPal's no-code boundary.

If the user only wants a prompt, Atlas must not let the current Runtime start
writing the script.

## Tools / Runtime Boundary

Codex, shell commands, test runners, repository search, and file writes are
execution tools. Atlas may prepare a task package for those tools, but those
tools are not Atlas assets and their availability must be evidenced by the
current Runtime.

## Asset Use Summary

task_id: atlas-doc-index-check-task-package-example

target_pal: Atlas

used_identity_assets:

- `official/pals/Atlas-developer/PAL.md`

used_skill_assets:

- `official/pals/Atlas-developer/skills/runtime-task-package-writing-skill.md`

used_workflows:

- `official/pals/Atlas-developer/workflows/implementation-task-package-workflow.md`

used_runtime_policy:

- Atlas plans; Codex executes only after approved scope

tools_called: none in this example

quality_gate_result: example only; real prompt acceptance and host regression
still required

next_asset_improvement: add a real Atlas development prompt host rehearsal in
Phase 3.

## Missing Asset Plan

missing_asset: explicit permission for actual script creation

why_needed: AgentPal is a no-code workspace by default, so adding scripts may
change the boundary and requires a separate confirmed implementation task.

temporary_fallback_allowed: yes, produce prompt-only package.

recommended_asset_path: a confirmed Runtime Task Package with allowed edit
surface.

priority: high before code writes.

## Lightweight Path

If the user asks for a one-line explanation of what Atlas does, lightweight path
is enough. Development prompts, code tasks, release engineering, and tool-backed
verification are not lightweight.

## What This Example Does Not Claim

- This does not mark Atlas as fully verified.
- This is not a full migration.
- This is not a code implementation.
- This is not evidence that Codex ran the task.
