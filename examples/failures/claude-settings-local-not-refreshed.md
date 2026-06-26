# Failure Example: Claude Settings Local Not Refreshed

## Wrong Scenario

`.claude/settings.local.json` includes the AgentPal Workspace path, but the current Claude Code session still cannot read AgentPal files.

## Consequence

The binding appears correct on disk, but Claude Code cannot load core gates, contacts, registry, or Mira entry files in the running session.

## Correct Check

- Confirm `.claude/settings.local.json` is valid JSON.
- Confirm `permissions.additionalDirectories` contains the AgentPal Workspace path exactly once.
- Try reading the required AgentPal Workspace files through the recorded path.
- If the file is correct but the session still cannot read, treat it as a session refresh issue.

## Correct Fix

Restart Claude Code from the project directory or use `/add-dir <path-to-AgentPal>` for the current session, then rerun verification.

## Wrong Fixes

- Add duplicate directory entries repeatedly.
- Move AgentPal files into the project.
- Replace unrelated Claude Code settings.
