# No Two Projects Context Self-Test

## Purpose

Verify that AgentPal chooses one active context and does not answer project questions by listing both AgentPal Workspace and an external project.

## AgentPal Workspace Mode

Input:

```text
了解一下当前状态
```

Expected:

- Mira says this is the AgentPal Workspace / AgentPal 工作区.
- Mira does not call it the current project.
- Mira does not list an external project as a second project.

## External Project Bound Mode

Input:

```text
了解一下这个项目，是什么状态
```

Expected:

- Mira answers only about `active_project_root`.
- AgentPal workspace is only a Pal source.
- 当前上下文只能有一个。

## Fail signs

- "我看到两个项目目录"
- "我看到两个根目录"
- "two project roots"
- Lists AgentPal Workspace and external project as two current projects.
- Asks the user to choose between the two roots for an ordinary project question.

