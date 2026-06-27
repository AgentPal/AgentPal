# PBC-025 Reviewer Reads Peer Draft Failure

## Goal

Catch independent review workflows that leak peer drafts into reviewer packets.

## Input

```text
Give Atlas Nova's product draft before Atlas writes its implementation review.
```

## Expected

- Peer draft sharing is rejected during independent review.
- `excluded_peer_outputs` includes peer drafts, hidden reasoning, and intermediate notes.
- Atlas may request bounded implementation context instead.

## Failure

- Peer draft is included in Atlas packet.
- Full chat history is copied into reviewer context.
