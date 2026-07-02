# Claude Code One-Prompt Install

## User

```text
cd <your-project>
claude
```

Then paste:

```text
Please connect AgentPal to the current project.
AGENTPAL_HOME = <path-to-AgentPal>
```

Replace `<path-to-AgentPal>` with the real AgentPal Workspace path before pasting.

## Expected Result

- `.agentpal/` is created or updated.
- `CLAUDE.md` gets exactly one AgentPal block.
- `AGENTS.md` gets exactly one AgentPal block.
- `.claude/settings.local.json` includes `permissions.additionalDirectories` with `<path-to-AgentPal>`.
- Existing `CLAUDE.md`, `AGENTS.md`, and Claude Code settings are preserved.
- `.gitignore` contains `.claude/settings.local.json`.
- AgentPal remains Simple Pal Mode only.
- The final install response includes a `Mira：` welcome that introduces Mira as Main Pal / Leader Pal / Conductor, lists Mira, Atlas, Nova, Vega, Rhea, Quinn, Morgan, and Harper, and explains `/pal Name`.
- No Subagent Mode or external Agent orchestration is activated.

## Fallback

If current Claude Code cannot access AgentPal immediately, restart Claude Code or temporarily use:

```text
/add-dir <path-to-AgentPal>
```

This is a fallback, not the default install path.
