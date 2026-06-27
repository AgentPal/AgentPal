# Thin Project Binding

Thin binding lets an external user project use AgentPal without becoming an AgentPal workspace.

Default files added to the external project:

- `.agentpal/project.json`
- `.agentpal/AGENTPAL.md`
- protected AgentPal block in `AGENTS.md`
- protected AgentPal block in `CLAUDE.md`, when Claude Code is used
- `.claude/settings.local.json`, when Claude Code needs local access to the AgentPal workspace
- `.gitignore` entry for `.claude/settings.local.json`

Default files not added:

- `.agentpal/memory/`
- `.agentpal/state/`
- `.agentpal/reports/`
- `.agentpal/context/`
- `.agentpal/index/`
- `.agentpal/pals/`
- `.agentpal/workflows/`
- `.agentpal/evals/`

The external project remains the active project. AgentPal remains the central Pal and governance workspace.

The binding file should also point to a central project record:

- `agentpal_project_record`: `workspace/projects/<project-id>/`

Project docs, requirements, design files, assets, data, and source files stay in the external project. AgentPal reads them when needed and writes its structured source map, derived knowledge, project memory, task packages, reports, governance records, and capability inventory to the central project record.

Thin binding must not turn `.agentpal/` into a project memory store, Pal Pack store, workflow store, or report archive.
