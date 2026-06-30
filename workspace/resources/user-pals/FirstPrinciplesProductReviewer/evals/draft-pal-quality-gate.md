# Draft Pal Quality Gate

This is a user custom Pal test artifact created from a PalSmith draft. It is not an official Pal.

## Required Checks

- `pal.json` parses as JSON.
- `official` is `false`.
- `status` is `user_custom_pal`.
- README, PAL, SKILL, role, source boundary, knowledge, workflow, Skill/Agent mapping, memory, eval, and publication boundary files exist.
- No central contacts file is modified.
- Official Pal directory count remains unchanged.
- No runtime code, CLI, scanner, daemon, connector, backend service, or Marketplace backend is added.
- No real-person representation or protected-source copying claim appears.

## Review Result Labels

Use `pass`, `partial`, `fail`, or `blocked`.

Passing this gate means the user custom Pal test artifact preserves the source draft's quality and boundary evidence. It does not mean the Pal is official or public-ready.
