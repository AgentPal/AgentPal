# AgentPal Workspace

This directory is the central organization workspace for AgentPal.

It may contain central organization records, project records, shared resources, and runtime-private state placeholders. It is not copied into external user projects by default.

Primary areas:

- `organization/`: central contacts, Pal cards, lifecycle, aliases, and replacement policy.
- `projects/`: private project records, templates, and governance structure.
- `resources/`: central reusable resource references.
- `state/`: workspace-local state placeholders.

External project bindings should point back here through `agentpal_workspace_root`.
