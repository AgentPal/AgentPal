<!-- BEGIN AGENTPAL WORKGROUP -->

This directory is bound to AgentPal through a thin project binding.

Read `.agentpal/project.json` and `.agentpal/AGENTPAL.md` for the current binding. The AgentPal workspace remains the central Pal, project-record, and governance source.

Project boundary:

- `active_project_root` is this external user project.
- `agentpal_workspace_root` is only the AgentPal reference workspace.
- `agentpal_project_record` points to `workspace/projects/<project-id>` inside the AgentPal workspace.
- "current project" means `active_project_root` unless the user explicitly says AgentPal itself.
- Project docs, design, requirements, assets, data, and source files are read from `active_project_root` when needed.
- Source maps, derived knowledge, project memory, task packages, reports, governance records, and capability inventory are stored in `agentpal_project_record`, not in project-local `.agentpal/`.

Routing boundary:

- Ordinary messages go to Mira.
- Direct `/pal Name` and `@Name` calls are resolved from central contacts.
- Resolve Pal contacts from `central_pal_contacts` in the AgentPal workspace.
- Owner selection is AI judgement only.
- Keyword routing, `keyword_map`, `domain_map`, and `role_map` are forbidden.

Execution boundary:

- AgentPal is a no-code organization layer, not an execution layer.
- File edits, commands, publishing, or external calls require current host-runtime evidence.

<!-- END AGENTPAL WORKGROUP -->
