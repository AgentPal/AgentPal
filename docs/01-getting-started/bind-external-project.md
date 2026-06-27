# Bind An External Project

Use thin binding when you want an external project to use AgentPal.

Create or update only the default binding surface:

- `.agentpal/project.json`
- `.agentpal/AGENTPAL.md`
- protected AgentPal block in `AGENTS.md`
- for Claude Code, protected AgentPal block in `CLAUDE.md`
- for Claude Code, local `.claude/settings.local.json` plus `.gitignore` entry

Do not copy AgentPal's official Pals, contacts, memory, reports, state, workflows, evals, or release files into the external project.

The binding must keep two roots separate:

- `active_project_root`: the external user project
- `agentpal_workspace_root`: the central AgentPal workspace
- `agentpal_project_record`: the central record under `workspace/projects/<project-id>/`

The external project can keep its own docs, design notes, requirements, assets, data, and source files. AgentPal may read those materials when a task requires them. AgentPal stores structured source maps, derived knowledge, project memory, task records, reports, governance records, and capability inventory in the central project record, not in the external project's `.agentpal/` directory.

Use `templates/project-binding/generic-codex/` or `templates/project-binding/claude-code/` as the current template source.
