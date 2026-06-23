# External Project Active Root Self-Test

## Purpose

Verify that an AgentPal-bound external project treats only `active_project_root` as the current project.

## Preconditions

- External project root `AGENTS.md` includes `BEGIN AGENTPAL WORKGROUP` and `END AGENTPAL WORKGROUP`.
- `.agentpal/project.json` contains `active_project_root` and `agentpal_workspace_root`.
- `current_project_semantics` is `active_project_root_only`.

## Test input

```text
你好
```

## Expected behavior

- Mira starts with `Mira：`.
- Mira identifies the external project as the current project.
- Mira treats AgentPal workspace as only a Pal source and routing reference.
- 当前上下文只能有一个。

## Fail signs

- The answer says there are two current project roots.
- The answer says two project roots.
- The answer asks the user to choose between the external project and AgentPal workspace.
- The answer treats AgentPal workspace as part of the business project.

