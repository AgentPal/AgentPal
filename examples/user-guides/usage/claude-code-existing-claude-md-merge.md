# Claude Code Existing CLAUDE.md Merge

## Starting File

```text
# Project Instructions

Keep test fixtures small.

<!-- BEGIN AGENTPAL BINDING: claude-code -->
old AgentPal block
<!-- END AGENTPAL BINDING: claude-code -->

Use the project formatter before release.
```

## Expected Merge

Only the protected AgentPal block is replaced.

The content before and after the block remains unchanged.

Running the install prompt twice must not create duplicate AgentPal blocks.
