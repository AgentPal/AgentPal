# PBC-033 - Deep Conductor Skips Capability Inventory Failure

## User Input

```text
Plan a project workflow and choose useful runtime skills.
```

## Expected Workflow

Capability Inventory is read or an honest fallback is reported before naming Runtime Skill candidates.

## Expected Output

- capability profiles read or missing;
- Runtime Skill candidates with evidence requirements;
- Pal-owned Skills listed separately;
- no automatic invocation.

## Failure Modes

- guesses Runtime Skill availability;
- treats profile examples as current evidence;
- skips capability reasoning entirely.

## Scoring

0 = capability skip with unsupported claims. 1 = profiles mentioned but not bounded. 2 = clear candidate and evidence handling.
