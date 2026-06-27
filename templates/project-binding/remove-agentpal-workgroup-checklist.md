# Remove AgentPal Workgroup Checklist

Use this checklist before removing AgentPal from an external project.

## Confirm target

- [ ] Resolve target through Codex project list / `list_projects`, workspace roots, registered projects, or user-provided path.
- [ ] Confirm the target is an external user project, not the AgentPal Workspace.
- [ ] Ask the user to confirm removal.

Confirmation text:

```text
Mira：
可以移除。这个操作只会删掉这个项目里的 AgentPal 工作组配置，不会动你的项目代码。确认要移除吗？
```

## Remove only AgentPal-managed content

- [ ] Delete target `.agentpal/`.
- [ ] Remove only the `<!-- BEGIN AGENTPAL WORKGROUP -->` / `<!-- END AGENTPAL WORKGROUP -->` block from root `AGENTS.md`.
- [ ] Remove the same block from root `CLAUDE.md` when present.
- [ ] Support legacy `BEGIN AGENTPAL WORKGROUP` / `END AGENTPAL WORKGROUP` removal only for old bindings.
- [ ] Preserve all user-authored `AGENTS.md` content outside the block.
- [ ] If root `AGENTS.md` becomes empty or whitespace-only, replace it with the non-workgroup deactivation marker from `templates/project-binding/agentpal-removed-agents-template.md`.
- [ ] If root `AGENTS.md` did not exist, create the same non-workgroup deactivation marker.
- [ ] Remove matching `projects/registered-projects.json` record.
- [ ] Remove or mark removed in `projects/registered-projects.md`.
- [ ] Archive matching `memory/projects/` binding memory by default.
- [ ] Clear `state/active-project.md` if it points to the target.

Keyword rules:

- delete .agentpal
- remove AGENTS.md AgentPal block
- leave deactivation marker if AGENTS.md would otherwise be empty or missing
- do not delete user AGENTS content
- cleanup registered projects
- warn that old Codex threads may still retain loaded AgentPal context

## Do not delete

- [ ] Project source files.
- [ ] Project docs.
- [ ] Project package files.
- [ ] Project `.git`.
- [ ] AgentPal Workspace.
- [ ] AgentPal `official/pals/` or central workspace assets.
- [ ] Other projects' `.agentpal/`.

## Completion

```text
Mira：
已经移除了。这个项目以后不会默认进入 AgentPal 工作组模式了。

注意：如果你还在旧的 Codex 对话线程里继续聊，那个线程可能已经加载过 AgentPal 规则，所以仍可能沿用 Mira。最干净的方式是为这个项目开一个新线程；如果必须继续旧线程，请明确要求 Codex generic answer，不再使用 Pal 模式。
```

