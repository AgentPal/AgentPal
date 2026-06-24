# Pal Self Test

## Purpose

Check whether `PalName` is a valid Pal Pack.

## Pass Criteria

- `PAL.md` clearly states identity, responsibilities, and boundaries.
- `SKILL.md` explains use cases and read order.
- `pal.json` is valid JSON.
- Replies start with `PalName:`.
- Output follows `core/output-contract.md`.
- The Pal does not fabricate execution results.
- The Pal does not store private data in public directories.
- The Pal does not hard-code other Pals.

## Fail Signs

- The Pal only changes the name but does not use real Pal assets.
- No Pal asset or fallback method is used.
- Tools, Skills, models, or plugins are treated as Pals.
- Other Pals are written as fixed collaborators.
