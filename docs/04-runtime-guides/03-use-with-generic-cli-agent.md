# Use With Generic CLI Agent

This guide covers the generic compatibility path for AgentPal v0.5.

## When This Path Fits

Use this path when your CLI agent can:

- read directories and local files
- follow Markdown / JSON instructions
- keep project context stable across the task
- report what it really executed

AgentPal does not promise that every CLI agent has been validated. This is a generic compatibility guide.

## Quick Start

```text
cd <your-project>
<your-cli-agent>
```

Then paste the one-prompt project connection prompt from `prompts/generic-cli-agent/install-agentpal-current-project.md`.

The install prompt is copy-paste ready. Do not edit the prompt before pasting.

When the CLI agent runs the prompt, it asks for your local AgentPal Workspace path unless you already provided a clear path in the current conversation. Enter the path to your AgentPal directory, for example:

```text
<path-to-AgentPal>
```

Do not ask the CLI Agent to scan the whole disk for AgentPal.

## What This Path Creates

- `.agentpal/` project binding files
- `AGENTS.md` workgroup block for the current project

It does not require Claude Code local settings, and it should not create runtime-specific files unless the current project already uses them or the user asks.

## Important Boundary

- The current project stays the active task context.
- The AgentPal Workspace is a reference workspace, not the user project.
- AgentPal is a Pal layer, not an Agent runtime or execution layer.
- The simple Mira-to-owner path is available for clear tasks.
- Deep Conductor is available as a no-code collaboration and mode-decision protocol, not automatic runtime execution.
- Subagent execution, external Agent execution, MCP/plugin calls, and Runtime Skill execution require current host evidence or explicit user authorization.

## Related

- [Runtime Compatibility](00-runtime-compatibility.md)
- [Project-First Connection](04-project-first-connection.md)
