# Quick Start: Claude Code

## User Flow

```text
cd <your-project>
claude
```

Then paste:

```text
prompts/claude-code/install-agentpal-current-project.md
```

with:

```text
AGENTPAL_HOME = <path-to-AgentPal>
```

Replace `<path-to-AgentPal>` with the real AgentPal Workspace path before pasting, for example `AGENTPAL_HOME = D:/Tools/AgentPal` or `AGENTPAL_HOME = /Users/you/AgentPal`.

## Expected Result

- the current project remains the active project
- `.agentpal/` is created or updated
- `CLAUDE.md` and `AGENTS.md` receive one protected AgentPal block
- `.claude/settings.local.json` receives `permissions.additionalDirectories`
- `.claude/settings.local.json` is treated as local machine configuration and should not be committed
- the final response includes a short `Mira：` welcome

## Not Expected

- AgentPal is not opened as the user project
- all Pal Packs are not copied into the project
- the whole AgentPal Workspace is not imported into project instructions
- `claude --add-dir` is not the default required path; it is only a fallback
