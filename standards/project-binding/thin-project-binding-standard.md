# Thin Project Binding Standard

A thin project binding lets an external project use AgentPal without copying the AgentPal workspace into that project.

The binding must preserve two roots:

- `active_project_root`: the external user project
- `agentpal_workspace_root`: the AgentPal workspace used as Pal and governance reference

Default binding files are limited to `.agentpal/project.json`, `.agentpal/AGENTPAL.md`, and protected instruction blocks in host-runtime instruction files.

The binding may describe how to find the AgentPal workspace, current runtime policy, and project-root separation. It must not include central memory, state, reports, Pal Packs, registries, workflows, or evals.
