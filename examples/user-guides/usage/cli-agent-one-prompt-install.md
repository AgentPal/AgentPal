# Generic CLI Agent One-Prompt Install

## User

```text
cd <your-project>
<your-cli-agent>
```

Then paste:

```text
Please connect AgentPal to the current project.
AGENTPAL_HOME = <path-to-AgentPal>
```

Replace `<path-to-AgentPal>` with the real AgentPal Workspace path before pasting.

## Expected Result

- `.agentpal/` is created or updated.
- `AGENTS.md` gets exactly one AgentPal block.
- `CLAUDE.md` is not created unless Claude Code is detected or the user asks.
- No `.claude/settings.local.json` is required.
- AgentPal path is verified before writing binding files.
- AgentPal remains a Pal layer and Simple Pal Mode only.
