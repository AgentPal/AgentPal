# Remove AgentPal Workgroup

Use this prompt when you want AgentPal to remove its workgroup binding from an external project.

```text
Help me remove the AgentPal workgroup from an external project.

Important: this removes only AgentPal workgroup configuration. It must not delete project source files, project docs, `.git`, package files, user-authored AGENTS.md content, the AgentPal Workspace, or other projects.

Recognize requests such as:
- 把 AgentPal 工作组从某项目移除
- 删除某项目里的 AgentPal 工作组
- 去除 AgentPal 工作组
- 取消 AgentPal 接管
- 把工作组移除
- 从 eagleweb 移除 AgentPal
- 这个项目不再使用 AgentPal

Resolve the target project in this order:
1. Codex current project list / `list_projects`, if available.
2. Current workspace roots.
3. AgentPal registered projects.
4. User-provided path.
5. If still unclear, ask the user.

Before removing, confirm:

Mira：
可以移除。这个操作只会删掉这个项目里的 AgentPal 工作组配置，不会动你的项目代码。确认要移除吗？

After user confirmation, remove only:
1. The target project's `.agentpal/` directory.
2. The target root `AGENTS.md` block from `BEGIN AGENTPAL WORKGROUP` to `END AGENTPAL WORKGROUP`.
3. If root `AGENTS.md` becomes empty or did not exist, write the non-workgroup deactivation marker from `templates/project-binding/agentpal-removed-agents-template.md`.
4. The matching record in AgentPal `projects/registered-projects.json`.
5. The matching entry in `projects/registered-projects.md`, or mark it removed.
6. The matching AgentPal project memory under `memory/projects/`, archived by default.
7. The matching `state/active-project.md` state if it is the active project.

Do not delete:
- external project source
- external project docs
- external project package files
- external project `.git`
- AgentPal Workspace
- AgentPal `pals/`
- other projects' `.agentpal/`
- user-authored content outside the AgentPal protected AGENTS block

After successful removal, say:

Mira：
已经移除了。这个项目以后不会默认进入 AgentPal 工作组模式了。

注意：如果你还在旧的 Codex 对话线程里继续聊，那个线程可能已经加载过 AgentPal 规则，所以仍可能沿用 Mira。最干净的方式是为这个项目开一个新线程；如果必须继续旧线程，请明确要求 Codex generic answer，不再使用 Pal 模式。

Report changed files with evidence.
```

