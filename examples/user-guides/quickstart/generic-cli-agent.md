# Quick Start: Generic CLI Agent

## User Flow

```text
cd <your-project>
<your-cli-agent>
```

Then paste:

```text
prompts/generic-cli-agent/install-agentpal-current-project.md
```

with:

```text
AGENTPAL_HOME = <path-to-AgentPal>
```

Replace `<path-to-AgentPal>` with the real AgentPal Workspace path before pasting, for example `AGENTPAL_HOME = D:/Tools/AgentPal` or `AGENTPAL_HOME = /Users/you/AgentPal`.

## Expected Result

- the current project remains the active project
- `.agentpal/` is created or updated
- `AGENTS.md` receives one protected AgentPal block
- no Claude Code local settings are required
- AgentPal remains a Pal layer using `Simple Pal Mode only`

## Compatibility Boundary

This path is for CLI agents that can read directories, follow Markdown / JSON instructions, maintain context, and report execution evidence. It is a conservative compatibility path, not a claim that every CLI agent has been validated.
