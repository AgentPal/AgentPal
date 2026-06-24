# Claude Code Prompts

Use these prompts when Claude Code is already running inside the target user project.

## Current Prompts

- `install-agentpal-current-project.md`: project-first AgentPal binding for Claude Code.
- `remove-agentpal-current-project.md`: project-local AgentPal binding removal.
- `verify-agentpal-current-project.md`: project-local verification prompt.

## AgentPal Workspace Path

The install prompt is copy-paste ready. Do not edit it before pasting.

When Claude Code runs the prompt, it asks for the local AgentPal Workspace path unless you already provided a clear path in the current conversation. Enter the path to your AgentPal directory, for example:

```text
<path-to-AgentPal>
```

Claude Code may also need `.claude/settings.local.json` to include the AgentPal Workspace path under `permissions.additionalDirectories`. That file is local machine configuration and should not be committed.

## Boundary

The Claude Code prompt connects an external user project to AgentPal. It does not make AgentPal the project, copy all Pal Packs into the project, activate Subagent Mode, or create a runtime service.
