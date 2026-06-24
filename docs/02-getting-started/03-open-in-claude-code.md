# Use With Claude Code

## Purpose

This document explains the basic Claude Code path for AgentPal v0.1.0-rc.1.

## Recommended Project Path

For real project work, open Claude Code in the user project, not in the AgentPal directory:

```text
cd <your-project>
claude
```

Then paste `prompts/claude-code/install-agentpal-current-project.md`.

The install prompt is copy-paste ready. Do not edit it before pasting. Claude Code asks for the local AgentPal Workspace path during installation unless you already provided a clear path in the conversation. Enter the path to your AgentPal directory, for example:

```text
<path-to-AgentPal>
```

The prompt creates or updates `.agentpal/`, `CLAUDE.md`, `AGENTS.md`, and `.claude/settings.local.json`.

`settings.local.json` is local machine configuration. It can store `permissions.additionalDirectories` for the AgentPal workspace path and should not be committed.

`--add-dir` and `/add-dir` are fallback options if the current Claude Code session does not immediately pick up the new local settings.

## AgentPal Workspace Path

Opening the AgentPal directory directly is still useful for maintaining AgentPal itself or initializing Mira in the AgentPal Workspace. It is not the recommended way to work on an external user project.

## Related

- [Quick start](00-quick-start.md)
- [Initialize AgentPal](04-initialize-agentpal.md)
- [Runtime compatibility](../04-runtime-guides/00-runtime-compatibility.md)
- [Claude Code project install](../10-using-agentpal-with-claude-code.md)
