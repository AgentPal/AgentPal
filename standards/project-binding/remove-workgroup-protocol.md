# Remove Workgroup Protocol

Use this protocol when the user asks to remove an AgentPal workgroup from an external project.

## Trigger phrases

Mira should recognize:

- 把 AgentPal 工作组从某项目移除
- 删除某项目里的 AgentPal 工作组
- 去除 AgentPal 工作组
- 取消 AgentPal 接管
- 把工作组移除
- 从 eagleweb 移除 AgentPal
- 这个项目不再使用 AgentPal

## Target lookup

Resolve the target external project in this order:

1. Codex current project list / `list_projects`, if available.
2. Current workspace roots.
3. AgentPal registered projects.
4. User-provided path.
5. If still unclear, ask the user.

Do not target the AgentPal Workspace unless the user explicitly says they are modifying AgentPal itself.

## Confirmation

Before removal, Mira must ask:

```text
Mira：
可以移除。这个操作只会删掉这个项目里的 AgentPal 工作组配置，不会动你的项目代码。确认要移除吗？
```

Do not remove anything until the user confirms.

## Removal actions

After confirmation:

1. Identify the runtime binding being removed: `codex`, `claude-code`, or full project disconnection.
2. For Codex removal, remove only the target root `AGENTS.md` block between `<!-- BEGIN AGENTPAL BINDING: codex -->` and `<!-- END AGENTPAL BINDING: codex -->`.
3. For Claude Code removal, remove only the root `CLAUDE.md` block between `<!-- BEGIN AGENTPAL BINDING: claude-code -->` and `<!-- END AGENTPAL BINDING: claude-code -->`.
4. Legacy bindings may use `<!-- AGENTPAL:BEGIN -->` / `<!-- AGENTPAL:END -->` or `<!-- BEGIN AGENTPAL WORKGROUP -->` / `<!-- END AGENTPAL WORKGROUP -->`; remove that legacy block only from the current runtime's instruction file during migration or cleanup.
5. Remove the current runtime from `.agentpal/project.json` `enabled_runtimes` and update `last_runtime`, `runtime`, `updated_at`, and `status`.
6. Delete the target project's `.agentpal/` directory only when `enabled_runtimes` is empty.
7. If another runtime remains enabled, preserve `.agentpal/project.json` and `.agentpal/AGENTPAL.md`.
8. If `AGENTS.md` is empty or blank after removing the Codex block in a full project disconnection, replace it with the non-workgroup deactivation marker from `templates/project-binding/agentpal-removed-agents-template.md`.
9. If root `AGENTS.md` did not exist and this is a full project disconnection, create that same non-workgroup deactivation marker.
10. For Claude Code, remove the AgentPal workspace path from `.claude/settings.local.json` `permissions.additionalDirectories`, preserving all other settings.
11. Remove or mark removed the matching central project record under `workspace/projects/<project-id>/` and `workspace/projects/projects.index.json` only when such a public/approved record exists and the user asked for full project disconnection.
12. If a legacy registry entry exists under `archive/migration-from-v0.3/root-legacy/projects/registered-projects.json` or `.md`, mark it as historical rather than treating it as current truth.
13. Archive matching AgentPal binding memory under `workspace/organization/memory/projects/` or the selected central project record by default only for full project disconnection.
14. Clear ignored local runtime state under `.agentpal/local/state/` only if it points to the removed project.
15. Generate a concise removal summary that warns about old runtime thread context.

Keyword rules:

- delete `.agentpal/` only when no runtime binding remains
- remove only the current runtime's AGENTS.md or CLAUDE.md AgentPal block
- remove only AgentPal path from Claude Code additionalDirectories when present
- leave deactivation marker if AGENTS.md would otherwise be empty or missing
- do not delete user AGENTS content
- cleanup central project records
- warn that old Codex threads may still retain loaded AgentPal context

## Boundaries

Remove AgentPal workgroup does not delete:

- external project source
- external project docs
- external project package files
- external project `.git`
- AgentPal Workspace
- AgentPal `pals/`
- other projects' `.agentpal/`
- user-authored `AGENTS.md` content outside the AgentPal protected block
- user-authored `CLAUDE.md` content outside the AgentPal protected block
- other `.claude/settings.local.json` settings

Only delete:

- target project `.agentpal/` only when `enabled_runtimes` is empty
- target project `AGENTS.md` Codex AgentPal block when removing Codex
- target project `CLAUDE.md` Claude Code AgentPal block when removing Claude Code
- target project `.claude/settings.local.json` AgentPal additionalDirectories entry when present
- AgentPal central project record for that target, when present and approved for cleanup
- AgentPal ignored local active project state for that target

## Completion message

```text
Mira：
已经移除了。这个项目以后不会默认进入 AgentPal 工作组模式了。

注意：如果你还在旧的 Codex 对话线程里继续聊，那个线程可能已经加载过 AgentPal 规则，所以仍可能沿用 Mira。最干净的方式是为这个项目开一个新线程；如果必须继续旧线程，请明确要求 Codex generic answer，不再使用 Pal 模式。
```

