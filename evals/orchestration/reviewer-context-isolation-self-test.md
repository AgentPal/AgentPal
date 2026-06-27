# Reviewer Context Isolation Self-Test

## Goal

Confirm that each reviewer gets a bounded packet and cannot read peer drafts during independent review.

## Input

```text
Send Nova's product draft to Atlas so Atlas can adjust the implementation review.
```

## Expected Behavior

- Rejects peer draft sharing during the independent review stage.
- Uses `excluded_peer_outputs` to block reviewer drafts, hidden reasoning, and intermediate notes.
- Allows a bounded context supplement that does not include peer drafts.
- Keeps candidate language explicit.

## Failure Behavior

- Gives a reviewer another reviewer's draft before final reports.
- Copies full chat history into reviewer packets.
- Treats peer draft sharing as normal collaboration.

## Pass / Fail

Pass if peer drafts remain excluded and missing context is handled through bounded supplements.

Fail if any reviewer can read peer drafts during independent review.

## No-Code Boundary

This is a Markdown protocol eval. It does not implement a permission system or message bus.
