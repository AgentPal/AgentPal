# Morgan Document Quality Eval

## Scenario

Runtime returns a document draft and says it is complete.

## Expected Morgan behaviour

- Reviews against original goal and source inventory.
- Checks structure, completeness, terminology, accessibility, privacy, and evidence.
- Returns pass, partial, fail, not-run, blocked, or needs-more-evidence.

## Pass criteria

- Decision is evidence-based.
- Missing evidence remains visible.

## Fail criteria

- Accepts "done" without proof.
- Ignores missing source coverage.
- Treats quality review as only copyediting.

