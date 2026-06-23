# Join Project Workgroup

Flow:

1. Identify external project name or path.
2. Check Codex `list_projects` if the current environment provides it.
3. Inspect Codex-known projects / current Codex project list / current-session visible projects / workspace roots.
4. Inspect AgentPal registered external projects.
5. Inspect recent project records.
6. Use an explicit user-provided path if present.
7. If still unresolved, ask the user for the path.
8. Confirm the exact path before writing.
9. Use the `.agentpal/` template.
10. Set `active_project_root` to the external user project.
11. Set `agentpal_workspace_root` to the AgentPal workspace.
12. Set `current_project_semantics` to `active_project_root_only`.
13. Create or update the external project root `AGENTS.md`.
14. Set default listener to Mira.
15. Keep specialist Pals lazy.
16. Explain that direct calls use `/pal Name`.
17. Do not copy all Pal Packs into the external project.

If no `list_projects` interface is available, say:

```text
Mira：我这里没有可用的 Codex 项目列表接口，所以我只能根据当前可见工作区和已登记项目查找。你也可以直接给我项目路径。
```

Do not ask for a manual path before checking Codex project list / `list_projects` and workspace roots.

## Remove workgroup

If the user asks to remove, cancel, delete, or undo the AgentPal workgroup binding, switch to remove flow instead of join flow.

Removal requires confirmation and removes only:

- target `.agentpal/`
- target `AGENTS.md` AgentPal protected block
- AgentPal registered project record
- AgentPal active project state for that target

Do not delete project source or user-authored AGENTS content.

