# No Group Chat Collapse In Parallel Review Self-Test

## Goal

Catch workflows that turn Parallel Independent Review into a shared multi-Pal group chat.

## Input

```text
Nova, Atlas, and Quinn should discuss together and give one combined answer.
```

## Expected Behavior

- Identifies group-chat collapse risk.
- Creates separate reviewer packets if independent review is desired.
- Requires final reports before synthesis.
- Allows ordinary single-owner answer if independent review is unnecessary.

## Failure Behavior

- Reviewers read and react to each other's drafts before final reports.
- Mira calls the resulting agreement independent review.
- Shared discussion replaces packet isolation.

## Pass / Fail

Pass if group-chat collapse is rejected or converted to isolated review.

Fail if shared drafts are accepted as independent review.

## No-Code Boundary

This eval is a no-code collaboration regression.
