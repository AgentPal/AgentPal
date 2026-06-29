# Runtime Compatibility

AgentPal v0.5 is a Pal layer, not an execution layer. Compatibility depends on whether a runtime can read structured workspace files, follow Markdown / JSON instructions, preserve context, and report execution evidence honestly.

## Current Quick-Start Paths

- Codex
- Claude Code
- generic CLI agents

These are the three user-facing paths documented for the current release candidate.

## Codex

Codex can open the AgentPal Workspace directly and initialize from `prompts/codex/initialize-agentpal-workspace.md`. Mira becomes the default entry Pal, and `/pal Name` can call a specialist.

See [Use With Codex](01-use-with-codex.md).

## Claude Code

Claude Code should usually use the project-first path:

```text
cd <your-project>
claude
```

Then paste the one-prompt AgentPal connection prompt. The current project remains the task context. AgentPal must not become the user project by mistake.

See [Use With Claude Code](02-use-with-claude-code.md).

## Generic CLI Agent

A generic CLI agent can use AgentPal if it can:

- read directories and local files
- follow Markdown / JSON instructions
- maintain working context
- report execution evidence

This is a compatibility guide, not a promise that every CLI agent has been validated.

See [Use With Generic CLI Agent](03-use-with-generic-cli-agent.md).

## Common Boundary

- AgentPal is not a runtime adapter that guarantees identical behavior everywhere.
- AgentPal is not a deep plugin for Codex or Claude Code.
- Deep Conductor, Subagent Mode, parallel child workflows, and external Agent orchestration are not active runtime paths in this release.

## Related

- [Project-First Connection](04-project-first-connection.md)
- [Current Status](../00-overview/01-current-status.md)
