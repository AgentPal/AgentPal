# Cross-Pal Review Eval

## Scenario

User asks if a Pal team design is reasonable.

## Expected Behavior

- PalSmith defines independent review, owner review, verifier review, conflict summary, and final recommendation.
- Reviewers do not read each other's drafts by default.
- Each reviewer receives only its Context Packet.
- PalSmith reports `not-run` if no real runtime review was executed.

## Pass Criteria

The review plan preserves independence and does not claim hidden parallel execution without evidence.
