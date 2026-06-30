# Draft Pal Quality Gate

This is a PalSmith draft Pal Pack test artifact, not an official Pal.

## Required Checks

- `pal.json` parses as JSON.
- `official` is `false`.
- `status` is `draft_test_artifact`.
- README, PAL, SKILL, role, source boundary, knowledge, workflow, Skill/Agent mapping, memory, eval, and publication boundary files exist.
- No central contacts file is modified.
- Official Pal directory count remains unchanged.
- No runtime code, CLI, scanner, daemon, connector, backend service, or Marketplace backend is added.
- No real-person representation or protected-source copying claim appears.

## Review Result Labels

Use `pass`, `partial`, `fail`, or `blocked`.

Passing this gate means the draft is useful as R174 evidence. It does not mean the draft is official or public-ready.
