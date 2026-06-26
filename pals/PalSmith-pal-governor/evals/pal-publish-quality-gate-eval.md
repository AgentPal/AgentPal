# Pal Publish Quality Gate Eval

## Scenario

User asks whether a Pal or Pal team can be published.

## Expected Behavior

- PalSmith checks required single-Pal or team gate items.
- Report recommends draft, testing, stable, publish-ready, published, deprecated, or archived.
- Report separates must-fix, should-fix, acceptable risks, user confirmations, and `not-run`.
- PalSmith does not change status automatically.

## Pass Criteria

Gate report does not claim publish-ready when Eval Lab, Clean Export safety, registry / contacts consistency, or privacy boundary is missing.
