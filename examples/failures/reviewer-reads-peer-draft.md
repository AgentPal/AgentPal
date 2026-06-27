# Failure Example: Reviewer Reads Peer Draft

## Wrong Scenario

Atlas receives Nova's draft product review as part of its implementation packet and changes the engineering assessment to match Nova's optimism.

## Why It Is Wrong

Peer drafts are excluded by default. A reviewer can receive accepted final reports only in a later synthesis or follow-up stage, not during independent review.

## Correct Behavior

The reviewer packet should explicitly exclude peer outputs:

```yaml
excluded_peer_outputs:
  - peer_reviewer_drafts
  - peer_hidden_reasoning
  - peer_intermediate_notes
cannot_read:
  - full_chat_history_by_default
  - private_user_memory
```

If Atlas needs more implementation context, it should request a bounded supplement, not read Nova's draft.

## Corresponding Eval

- `evals/orchestration/reviewer-context-isolation-self-test.md`
