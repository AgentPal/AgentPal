# Remove AgentPal Workgroup

## User message

```text
把 AgentPal 工作组从 eagleweb 项目移除
```

## Expected Mira behavior

Mira resolves the target project using Codex project list / `list_projects`, workspace roots, registered projects, or user-provided path.

Before removal:

```text
Mira：
可以移除。这个操作只会删掉这个项目里的 AgentPal 工作组配置，不会动你的项目代码。确认要移除吗？
```

After user confirmation:

- delete target `.agentpal/`
- remove only the `BEGIN AGENTPAL WORKGROUP` / `END AGENTPAL WORKGROUP` block from root `AGENTS.md`
- if root `AGENTS.md` becomes empty or did not exist, write the non-workgroup deactivation marker
- clean AgentPal registered project records
- clear active project state if it points to that project
- archive AgentPal binding memory by default

Completion:

```text
Mira：
已经移除了。这个项目以后不会默认进入 AgentPal 工作组模式了。

注意：如果你还在旧的 Codex 对话线程里继续聊，那个线程可能已经加载过 AgentPal 规则，所以仍可能沿用 Mira。最干净的方式是为这个项目开一个新线程；如果必须继续旧线程，请明确要求 Codex generic answer，不再使用 Pal 模式。
```

## What must not happen

- Delete project source.
- Delete project docs.
- Delete project `.git`.
- Delete package files.
- Delete user-authored `AGENTS.md` content.
- Delete user-authored AGENTS content outside the AgentPal block.
- Delete AgentPal Workspace or AgentPal `pals/`.

