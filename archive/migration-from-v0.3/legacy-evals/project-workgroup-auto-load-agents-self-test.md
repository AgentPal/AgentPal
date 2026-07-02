# Project Workgroup Auto Load AGENTS Self-Test

Legacy archive note: this file documents the old pre-runtime-qualified marker format for migration history only. New bindings must use runtime-qualified markers.

## Purpose

Verify that external project binding tells Codex how to enter AgentPal project-bound mode.

Keyword: project workgroup auto-load.
Keyword: read root AGENTS.md.

## Test input

```text
把 AgentPal 工作组加入 eagleweb 项目
```

## Expected behavior

- Binding creates or updates `.agentpal/`.
- Binding creates or updates root `AGENTS.md`.
- Root `AGENTS.md` includes `<!-- BEGIN AGENTPAL WORKGROUP -->` and `<!-- END AGENTPAL WORKGROUP -->`.
- Root `AGENTS.md` tells Codex to read `.agentpal/INIT_AGENTPAL_PROJECT_PROMPT.md` if AgentPal rules have not loaded yet.
- Join completion reply includes:

```text
请读取当前项目根 AGENTS.md，以及 .agentpal/INIT_AGENTPAL_PROJECT_PROMPT.md，进入 AgentPal project-bound mode。普通消息默认交给 Mira，当前项目只以本项目目录为准。
```

## Fail signs

- Only `.agentpal/` is created.
- Root `AGENTS.md` is missing.
- Join completion does not tell the user how to make the external project load AgentPal rules.

