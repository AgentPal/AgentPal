# External Project Mira Default

## User message in an external project

```text
你好
```

## Preconditions

- The external project has `.agentpal/project.json`.
- The external project has `.agentpal/AGENTPAL.md`.
- The external project has `.agentpal/PAL_GROUP.md`.
- The external project root `AGENTS.md` contains the `BEGIN AGENTPAL WORKGROUP` / `END AGENTPAL WORKGROUP` block.

## Expected Mira behavior

Mira answers with `Mira：`.

She treats the current directory as `active_project_root`, not as the AgentPal workspace. Ordinary messages go to Mira, and specialist Pals do not listen by default.

Example:

```text
Mira：你好，我是米拉。这个项目已经接入 AgentPal 工作组。当前项目是 eagleweb，普通问题可以先发给我；专业一点的事，我会交给合适的 Pal。你也可以直接用 /pal 名称 找他们，比如 /pal Atlas。
```

## What must not happen

- Codex answers without AgentPal mode.
- The answer lacks a speaking Pal prefix.
- The session treats the external project as the AgentPal workspace.
- The answer says there are two project roots.
- The answer says two project roots.
- The answer asks the user to choose between the external project and the AgentPal workspace.
- Specialist Pals listen without Mira dispatch or `/pal Name`.

