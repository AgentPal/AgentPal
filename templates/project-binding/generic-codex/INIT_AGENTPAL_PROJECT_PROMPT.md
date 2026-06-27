# Initialize AgentPal Thin Binding

Use the files in this template to bind the current external project to AgentPal.

Create or update only:

- `.agentpal/project.json`
- `.agentpal/AGENTPAL.md`
- the protected AgentPal block in `AGENTS.md`

Do not create `.agentpal/memory`, `.agentpal/state`, `.agentpal/reports`, `.agentpal/context`, `.agentpal/index`, `.agentpal/pals`, `.agentpal/workflows`, or `.agentpal/evals` by default.

The generated `.agentpal/project.json` should include `binding_mode: thin`, `central_pal_contacts`, and `agentpal_project_record`.

Use `workspace/projects/<project-id>/` inside the AgentPal workspace for source maps, derived knowledge, project memory, task records, reports, governance records, and capability inventory.
