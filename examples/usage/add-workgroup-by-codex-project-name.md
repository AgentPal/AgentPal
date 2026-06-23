# Add Workgroup By Codex Project Name

## User message

```text
把工作组添加到 eagleweb 项目
```

## Expected Mira behavior

Mira checks Codex `list_projects` first if available, then Codex-known projects / current visible workspace project list / workspace roots.

```text
Mira：我先查 Codex 当前项目列表。已找到 eagleweb：C:/Projects/eagleweb。我会把 AgentPal 工作组加入这个外部项目；写入 .agentpal/，并创建或更新项目根 AGENTS.md。
```

If no `list_projects` interface is available:

```text
Mira：我这里没有可用的 Codex 项目列表接口，所以我只能根据当前可见工作区和已登记项目查找。你也可以直接给我项目路径。
```

## Expected binding semantics

- `active_project_root`: `C:/Projects/eagleweb`
- `agentpal_workspace_root`: the AgentPal workspace path
- `current_project_semantics`: `active_project_root_only`
- `.agentpal/` is created or updated
- root `AGENTS.md` is created or updated

## Fail signs

- Mira asks for a path before checking Codex projects.
- Mira skips `list_projects` when it is available.
- Mira treats the AgentPal workspace as the target project.
- Mira creates only `.agentpal/` and skips root `AGENTS.md`.

