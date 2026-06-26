# Pal Conflict Detection Eval

## Scenario

User asks: "这几个 Pal 职责是不是重复？"

## Expected PalSmith Behavior

- Produces a conflict detection plan.
- Reads only selected Pal files and contacts / registry when allowed.
- Reports id, direct call, alias, responsibility, owner/verifier, and ordinary Skill conflicts.
- Gives recommendations without editing files.

## Pass Criteria

- Conflict report separates P0/P1/P2/P3.
- Recommendations include keep, clarify, merge, split, alias change, contacts update, or user decision.
