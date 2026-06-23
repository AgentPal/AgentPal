# AgentPal Workspace Vs Project Semantics Self-Test

## Purpose

Verify naming and context semantics.

## Required terms

- AgentPal itself: AgentPal Workspace / AgentPal 工作区
- External project directory: project / 当前项目 / 外部项目
- AgentPal joined to external project: Project-bound AgentPal Workgroup
- Current project root: `active_project_root`
- AgentPal source directory: `agentpal_workspace_root`

## Test input in AgentPal Workspace

```text
了解一下当前状态
```

Expected:

- Mira says "AgentPal 工作区".
- Mira does not say "AgentPal 项目".
- Mira does not call it the current project.

## Test input in external project

```text
读取项目目录
```

Expected:

- Mira treats only `active_project_root` as the current project.
- Mira does not list `agentpal_workspace_root`.

