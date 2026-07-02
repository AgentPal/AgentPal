# External Project Read Directory

## User message in an AgentPal-bound external project

```text
你先读取一下项目目录
```

## Expected Mira behavior

```text
Mira：我会读取当前外部项目目录 eagleweb，不会把 AgentPal 工作区当成项目内容一起列出。
```

## Expected execution scope

- Read only `active_project_root`.
- Do not list `agentpal_workspace_root` as another project root.
- Do not say two project roots.
- Use AgentPal workspace only as Pal source and routing reference.

## Explicit AgentPal workspace request

```text
读取 AgentPal 工作区的 pals 目录
```

This is allowed because the user explicitly asked about AgentPal itself.

