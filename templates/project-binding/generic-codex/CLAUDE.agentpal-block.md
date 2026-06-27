<!-- BEGIN AGENTPAL WORKGROUP -->

This project uses a thin AgentPal binding. Read `.agentpal/project.json` and `.agentpal/AGENTPAL.md`.

The active project is this external project. The AgentPal workspace is only the central Pal, project-record, and governance reference.

`agentpal_project_record` points to `workspace/projects/<project-id>` inside the AgentPal workspace. Read current user project materials from `active_project_root` when needed, and store AgentPal source maps, derived knowledge, memory, task records, reports, governance records, and capability inventory in the central project record.

Do not copy central Pal Packs, contacts, memory, reports, state, workflows, source maps, derived knowledge, task packages, governance records, or evals into this project by default.

Owner selection is AI judgement only after reading current central contacts. Do not use keyword routing, `keyword_map`, `domain_map`, or `role_map`.

<!-- END AGENTPAL WORKGROUP -->
