# Pal Runtime Call Verification Protocol

Status: PalSmith v0.3 no-code protocol.

This protocol clarifies what it means to verify `/pal Name` calls.

## Verification Levels

| Level | Name | Meaning |
| --- | --- | --- |
| Level 1 | Static Resolution | contacts / registry / `pal.json` / `PAL.md` prove the target can be resolved |
| Level 2 | Runtime Simulation | current Runtime follows the direct call task package, reads target Pal files, and answers as that Pal |
| Level 3 | Native Runtime Call | AgentPal App or a Runtime with native `/pal` support actually executes `/pal Name` |

Current Codex tests usually prove Level 1 and may simulate Level 2. They must not claim Level 3 unless a native runtime call happened.

## Output

`Runtime Call Verification Report`:

- verification level reached
- evidence paths
- direct call tested
- target Pal id
- target `PAL.md`
- whether response used target identity
- why Level 3 was not reached, if applicable
- whether this blocks release
- future upgrade path
