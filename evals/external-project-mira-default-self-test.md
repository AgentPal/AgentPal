# External Project Mira Default Self-Test

## Purpose

Verify that an external project connected to AgentPal defaults ordinary conversation to Mira.

## Test input

```text
你好
```

## Preconditions

- External project root `AGENTS.md` includes `<!-- BEGIN AGENTPAL WORKGROUP -->` and `<!-- END AGENTPAL WORKGROUP -->`.
- Root `AGENTS.md` tells Codex to read `.agentpal/INIT_AGENTPAL_PROJECT_PROMPT.md` if AgentPal rules have not loaded yet.
- `.agentpal/project.json` exists.
- `.agentpal/INIT_AGENTPAL_PROJECT_PROMPT.md` exists.
- `.agentpal/AGENTPAL.md` exists.
- `.agentpal/PAL_GROUP.md` exists.

## Expected behavior

The answer starts with `Mira：`.

The session treats the current directory as `active_project_root`, not as the AgentPal workspace. Ordinary messages go to Mira. Specialist Pals do not listen by default.

Expected answer example:

```text
Mira：你好，我是 Mira，是你的 Pal 团队 leader。这个项目已经接入 AgentPal 工作组。当前项目是 eagleweb，普通问题可以先发给我；专业一点的事，我会交给合适的 Pal。你也可以直接用 /pal 名称 找他们，比如 /pal Atlas。
```

## Fail signs

- The answer is generic Codex without Mira.
- The answer lacks a speaking Pal prefix.
- The external project is confused with the AgentPal workspace directory.
- The answer says there are two project roots.
- The answer says two project roots.
- The answer asks the user to choose between AgentPal workspace and the external project.
- Specialist Pals participate without Mira dispatch or `/pal Name`.
- Root `AGENTS.md` does not mention `.agentpal/INIT_AGENTPAL_PROJECT_PROMPT.md`.

