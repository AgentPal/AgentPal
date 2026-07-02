# AgentPal Workspace Status

## User message in the AgentPal Workspace

```text
了解一下当前状态
```

## Expected Mira behavior

```text
Mira：这里是 AgentPal 工作区。当前我会只看 AgentPal 工作区本身：Mira 是默认接收者，Pals 放在 pals/，项目工作组模板在 projects/ 和 templates/。如果你想了解某个外部项目，需要先告诉我项目名，或让我把 Pal 工作组接入那个项目。
```

## What must not happen

- Do not call AgentPal itself "the current project".
- Do not say two project roots.
- Do not list an external project beside the AgentPal Workspace unless the user explicitly asks about that external project.

