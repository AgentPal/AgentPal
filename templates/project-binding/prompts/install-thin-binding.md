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
- `.agentpal/capability-inventory/`
- `.agentpal/business-systems/`
- `.agentpal/reviews/`
- `.agentpal/evidence/`
- `.agentpal/replay/`
- `.agentpal/rollback/`
- `.agentpal/verification/`
- `.agentpal/audit-trail/`
- `.agentpal/governance-decisions/`
- `.agentpal/change-ledger/`
- `.agentpal/change-review/`

Keep `active_project_root` and `agentpal_workspace_root` separate.

The binding metadata should include:

- `schema_version: agentpal.project_binding.v1`
- `binding_version`
- `binding_type: thin`
- `runtime`
- `agentpal_source` as a structured object
- `enabled_runtimes`
- `last_runtime`
- `central_pal_contacts`
- `agentpal_project_record`
- `workspace/projects/<project-id>` as the central record location

Read user project materials from the external project when needed. Write AgentPal source maps, derived knowledge, project memory, task packages, reports, governance records, and capability inventory to the central project record, not to the external project's `.agentpal/` directory.
