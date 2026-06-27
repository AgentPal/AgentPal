# PBC-032 - Deep Conductor Token Budget Failure

## User Input

```text
This project has many docs and Pal assets. Make a conductor plan without overloading context.
```

## Expected Workflow

The conductor uses Context Budget Plan and avoids broad reads.

## Expected Output

- index-only, full-text, summarize-first, and memory source categories;
- `context_read_count`, `profile_read_count`, and `memory_used`;
- `cannot_read` boundaries;
- verification quality preserved.

## Failure Modes

- reads all Pal Packs, all project files, or all memory by default;
- forwards full chat history;
- skips verification to save tokens.

## Scoring

0 = context overload. 1 = partial budget. 2 = bounded budget with verification protection.
