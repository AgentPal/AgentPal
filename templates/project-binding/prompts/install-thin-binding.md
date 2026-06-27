# Install Thin AgentPal Binding

Install AgentPal into the current external project as a thin binding.

Allowed default writes:

- `.agentpal/project.json`
- `.agentpal/AGENTPAL.md`
- protected AgentPal block in `AGENTS.md` or `CLAUDE.md`
- `.claude/settings.local.json` and `.gitignore` entry only for Claude Code permission needs

Forbidden default writes:

- `.agentpal/memory/`
- `.agentpal/state/`
- `.agentpal/reports/`
- `.agentpal/context/`
- `.agentpal/index/`
- `.agentpal/pals/`
- `.agentpal/workflows/`
- `.agentpal/evals/`

Keep `active_project_root` and `agentpal_workspace_root` separate.

The binding metadata should include:

- `binding_mode: thin`
- `central_pal_contacts`
- `agentpal_project_record`
- `workspace/projects/<project-id>` as the central record location

Read user project materials from the external project when needed. Write AgentPal source maps, derived knowledge, project memory, task packages, reports, governance records, and capability inventory to the central project record, not to the external project's `.agentpal/` directory.
