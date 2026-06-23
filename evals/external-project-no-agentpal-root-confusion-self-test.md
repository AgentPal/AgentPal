# External Project No AgentPal Root Confusion Self-Test

## Purpose

Verify that project directory questions do not include the AgentPal workspace unless explicitly requested.

## Test input

```text
你先读取一下项目目录
```

## Expected behavior

- Mira starts with `Mira：`.
- Mira says she will read the current external project directory.
- The execution layer reads only `active_project_root` unless the user asks otherwise.
- AgentPal workspace is not listed as another project root.
- Mira does not say two project roots.

## Explicit AgentPal request

Input:

```text
读取 AgentPal 工作区的 pals 目录
```

Expected:

- Mira may read or route reading of `agentpal_workspace_root/pals`.
- The answer clearly states this is an explicit AgentPal workspace request.

## Fail signs

- Mira says the workspace has two project roots for ordinary project questions.
- Mira lists AgentPal workspace next to the external project when asked to read the project directory.
- Mira refuses to read AgentPal workspace even when the user explicitly asks about AgentPal itself.

