# AgentPal Claude Code Binding

This project uses a thin AgentPal binding for Claude Code.

- `active_project_root` is this external project.
- `agentpal_workspace_root` is the central AgentPal workspace.
- Pal contacts and official Pals stay in the AgentPal workspace.
- Claude-local permission settings may live in `.claude/settings.local.json`; that file should stay uncommitted.

Do not create project-local AgentPal memory, state, reports, context indexes, Pal copies, workflows, or evals by default.
