# Codex Project List First Self-Test

## Purpose

Verify that Mira checks Codex `list_projects` first if available, then Codex-known projects and workspace roots before asking for a manual path.

## Test input

```text
把工作组添加到 eagleweb 项目
```

## Preconditions

- Codex-visible projects or workspace roots include `C:/Projects/eagleweb`.

## Expected behavior

- Mira starts with `Mira：`.
- Mira checks Codex `list_projects` first if the current environment provides it.
- Mira checks Codex project list / visible workspace project list before AgentPal registered projects.
- Mira checks workspace roots before asking for a manual path.
- Mira resolves `eagleweb` to `C:/Projects/eagleweb` or asks the user to confirm that matched path.
- Mira does not ask the user to manually provide a path before checking visible projects.
- Binding still creates or updates both `.agentpal/` and the external project root `AGENTS.md`.

If no `list_projects` interface is available, Mira says:

```text
Mira：我这里没有可用的 Codex 项目列表接口，所以我只能根据当前可见工作区和已登记项目查找。你也可以直接给我项目路径。
```

## Fail signs

- Mira immediately asks the user to provide a path.
- Mira skips `list_projects` when available.
- Mira only searches AgentPal registration records.
- Mira creates `.agentpal/` but does not update root `AGENTS.md`.

