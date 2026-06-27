# Project Record Standard

AgentPal records external user projects centrally under `workspace/projects/<project-id>/`.

An external project is the bound work target. It is not the AgentPal Workspace and it must not receive copied Pal Packs, copied roster files, internal task reports, project memory, or governance records by default.

## Required Boundary

- External project binding files are thin entrypoints only.
- The central project record lives in the AgentPal Workspace at `workspace/projects/<project-id>/`.
- `active_project_root` points to the user project.
- `agentpal_workspace_root` points to the AgentPal Workspace.
- `agentpal_project_record` points to the central project record directory.

## Record Contents

A central project record may include:

- `PROJECT.md`
- `project.json`
- `binding/`
- `source-map/`
- `derived-knowledge/`
- `memory/`
- `tasks/`
- `reports/`
- `governance/`
- `capability-inventory/`

Real project records are workspace-private by default and should not be committed to the public repository unless explicitly converted into a public-safe example.

