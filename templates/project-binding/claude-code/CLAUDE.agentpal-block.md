<!-- BEGIN AGENTPAL WORKGROUP -->

This directory is bound to AgentPal through a thin Claude Code binding.

Read `.agentpal/project.json` and `.agentpal/AGENTPAL.md` for the binding. If Claude needs access to the central AgentPal workspace, use local `.claude/settings.local.json` and keep that file out of git.

The external project remains the active project. AgentPal remains the central Pal, project-record, and governance workspace.

`agentpal_project_record` points to `workspace/projects/<project-id>` inside the AgentPal workspace. Project docs, design, requirements, assets, data, and source files are read from `active_project_root` when needed; source maps, derived knowledge, project memory, task packages, reports, governance records, and capability inventory stay in the central project record.

Owner selection is AI judgement only after reading current central contacts from the AgentPal workspace. Keyword routing, `keyword_map`, `domain_map`, and `role_map` are forbidden.

<!-- END AGENTPAL WORKGROUP -->
