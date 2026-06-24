# Generic CLI Agent Prompts

Use these prompts when a Markdown/JSON-capable CLI Agent is already running inside the target user project.

## Current Prompts

- `install-agentpal-current-project.md`: project-first AgentPal binding for generic CLI Agents.
- `remove-agentpal-current-project.md`: project-local AgentPal binding removal.

## AgentPal Workspace Path

The install prompt is copy-paste ready. Do not edit it before pasting.

When the CLI agent runs the prompt, it asks for the local AgentPal Workspace path unless you already provided a clear path in the current conversation. Enter the path to your AgentPal directory, for example:

```text
<path-to-AgentPal>
```

The path is used only to connect the current project to the AgentPal Workspace. Do not commit private local paths in public repository files.

## Boundary

This path is for CLI agents that can read directories, follow Markdown / JSON instructions, maintain task context, and report execution evidence. AgentPal does not claim every CLI agent has been validated.

Do not create Claude Code-specific files unless the runtime is Claude Code or the user explicitly asks.
