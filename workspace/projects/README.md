# Workspace Projects

This directory holds central AgentPal records for external user projects.

Default public repository content should include only templates, examples, and empty indexes. Real user project records are workspace-private and should not be committed.

External projects should contain thin binding files only. Project memory, source maps, derived knowledge, governance notes, task packages, reports, and capability inventory records belong here when they are maintained centrally.

Default public files:

- `README.md`
- `projects.index.json`
- `_template/`

Real records use:

`workspace/projects/<project-id>/`

The external project remains the source of current project files. AgentPal reads the external project when needed, then stores structured summaries and project memory in the central record.
