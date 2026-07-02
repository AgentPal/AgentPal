# 02 Setup Claude Code Thin Binding

## Goal

Verify that Claude Code can use AgentPal through a local binder / thin binding.

## Setup

1. Open a test project in Claude Code.
2. Run the AgentPal binder or paste the current Claude Code AgentPal install prompt.
3. Confirm the project has:

```text
.agentpal/project.json
.agentpal/AGENTPAL.md
CLAUDE.md
```

4. Confirm `CLAUDE.md` contains an AgentPal protected block.
5. Confirm repair and disable behavior can be inspected without deleting the central AgentPal workspace.

## Test Prompt

```text
请检查当前项目的 AgentPal Claude Code 绑定状态，并说明它是不是 thin binding。
```

## Expected Result

- The answer reports Claude Code binding status.
- It does not copy full Pal / Team assets into the project.
- It does not claim official Marketplace publication.
- It distinguishes local binder validation from public marketplace release.

## Known Limits

Current validation is local host / binder validation. It is not an official marketplace release.

## Record

In `v06-user-test-result-form.md`, fill:

```text
host_runtime: Claude Code
project_mode:
claude_code_binding_result:
raw_output_paths:
screenshot_paths:
notes:
```
