# Claude Code Preserve Existing CLAUDE.md Self-Test

## Purpose

Verify that AgentPal preserves user-authored `CLAUDE.md` content.

## Pass

- Existing text before the AgentPal block remains unchanged.
- Existing text after the AgentPal block remains unchanged.
- Only the block between `<!-- BEGIN AGENTPAL BINDING: claude-code -->` and `<!-- END AGENTPAL BINDING: claude-code -->` is inserted or replaced.
- Running install twice does not duplicate the block.
- The block is lightweight and does not import the entire AgentPal workspace.

## Fail

- Whole `CLAUDE.md` is replaced.
- Multiple AgentPal blocks appear after repeated install.
- Project-specific instructions are deleted.
