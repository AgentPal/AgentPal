# Use With Claude Code

This is the recommended Claude Code path for AgentPal v0.3.0-rc.1.

## Project-First Path

Start from the real user project:

```text
cd <your-project>
claude
```

Then paste the one-prompt AgentPal connection prompt from `prompts/claude-code/install-agentpal-current-project.md`.

The install prompt is copy-paste ready. Do not edit the prompt before pasting.

When Claude Code runs the prompt, it asks for your local AgentPal Workspace path unless you already provided a clear path in the current conversation. Enter the path to your AgentPal directory, for example:

```text
<path-to-AgentPal>
```

Do not ask Claude Code to scan the whole disk for AgentPal. Provide the path yourself when prompted.

## What This Path Does

- keeps the current user project as the active task context
- connects the project to the AgentPal Workspace through `.agentpal/`
- updates `CLAUDE.md` and `AGENTS.md` with a lightweight AgentPal workgroup block
- updates `.claude/settings.local.json` so Claude Code can read the AgentPal Workspace path

## Important Boundary

- `.claude/settings.local.json` is local machine configuration and should not be committed.
- This is not a deep Claude Code plugin.
- This is not an automatic installer outside the current project.
- AgentPal must not mistake its own workspace directory for the user's project.
- Project questions should resolve to the current user project directory first.

## If Access Does Not Apply Immediately

If the current Claude Code session still cannot read the AgentPal path after the local settings update:

- restart Claude Code in the project
- or temporarily use `/add-dir <path-to-AgentPal>`
- or restart with `claude --add-dir <path-to-AgentPal>`

These are fallback options, not the default setup path.

## Current Runtime Boundary

- AgentPal is a Pal layer, not an Agent runtime.
- The active path is `Simple Pal Mode only`.
- Deep Conductor is a no-code protocol foundation, not automatic runtime execution.
- Subagent Mode and external Agent orchestration are not active in this release.

## Related

- [Project-First Connection](04-project-first-connection.md)
- [Runtime Compatibility](00-runtime-compatibility.md)
