# AgentPal External Project Binding

This project uses a thin AgentPal binding.

- `active_project_root` is this external project.
- `agentpal_workspace_root` is the central AgentPal workspace.
- `agentpal_project_record` points to the central project record under `workspace/projects/<project-id>/`.
- Ordinary messages go to Mira unless the user directly calls a Pal with `/pal Name` or `@Name`.
- Pal contacts, Pal Packs, governance, memory, reports, workflows, source maps, derived knowledge, and task records stay in the AgentPal workspace.
- This `.agentpal/` directory is not a Pal asset store, memory store, state database, report archive, project index, source map, or derived-knowledge store.

When answering about "this project" or "current project", use only the active external project unless the user explicitly asks about AgentPal itself.

AgentPal may read this project's docs, design notes, requirements, source files, assets, and data when the task requires them. Structured summaries, derived knowledge, project memory, task packages, reports, governance records, and capability inventory should be written to the central `agentpal_project_record`, not into this external project's `.agentpal/` directory.
