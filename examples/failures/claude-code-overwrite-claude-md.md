# Failure: Claude Code Overwrites CLAUDE.md

## Bad Behavior

The install prompt replaces the whole `CLAUDE.md` file with AgentPal instructions.

## Why This Fails

`CLAUDE.md` may contain important project-specific rules. AgentPal must not delete user-authored project instructions.

## Correct Behavior

Preserve all existing content and replace only:

```text
<!-- BEGIN AGENTPAL BINDING: claude-code -->
...
<!-- END AGENTPAL BINDING: claude-code -->
```

If no block exists, append one lightweight AgentPal block.
