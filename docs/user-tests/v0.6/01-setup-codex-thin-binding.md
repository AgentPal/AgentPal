# 01 Setup Codex Thin Binding

## Goal

Verify that a Codex project can use AgentPal through a thin binding without copying the full AgentPal workspace into the user project.

## Setup

1. Open a test project in Codex.
2. Enable AgentPal using the installed AgentPal Codex Skill or the current project binding flow.
3. Confirm the project has:

```text
.agentpal/project.json
.agentpal/AGENTPAL.md
AGENTS.md
```

4. Confirm `AGENTS.md` contains an AgentPal protected block.
5. Confirm `.agentpal/project.json` records a thin binding and the Codex runtime.

## Test Prompt

```text
启用 AgentPal 后，请告诉我当前项目的 AgentPal 绑定状态。不要把 AgentPal 工作区当成当前项目。
```

## Expected Result

- The answer distinguishes the external test project from the AgentPal workspace.
- The binding is thin.
- The full Pal / Team assets are not copied into the project.
- Ordinary AgentPal messages go to Mira.

## Known Limits

- Codex slash-command host surface is not fully verified.
- Project-bound DeepConductor still needs user-side host validation.
- This is not Marketplace installation evidence.

## Record

In `v06-user-test-result-form.md`, fill:

```text
host_runtime: Codex
project_mode:
codex_thin_binding_result:
raw_output_paths:
screenshot_paths:
notes:
```
