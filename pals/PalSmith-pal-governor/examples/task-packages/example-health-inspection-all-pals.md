# Example: Health Inspection For All Pals

This is an example only. It is not a completed inspection report.

## User Says

`/pal PalSmith 体检所有 Pal`

## PalSmith Questions

- Should the scope be all registered Pals or all directories under `pals/`?
- May the current Agent Runtime read `contacts/pals.json` and `registry/pal.index.json`?
- Should the result be written to a report file or returned inline?
- Should repair tasks be suggestions only?

## Plan

- Inspect required root files, `pal.json`, collaboration flags, contacts/registry consistency, and public/private boundary.
- Do not read private memory content.
- Report `missing` and `not-run` honestly.

## Runtime Task Package

- `task_name`: Pal Health Inspection Task Package
- `owner_pal`: PalSmith
- `executing_runtime`: current Agent Runtime
- `allowed_read_paths`: `pals/`, `contacts/pals.json`, `registry/pal.index.json`, `agentpal.json`
- `allowed_write_paths`: approved report path only
- `forbidden_write_paths`: Pal source files, contacts, registry
- `required_exclusions`: private memory content from public report
- `user_confirmation_required`: yes if writing report

## Handoff To Runtime

The current Agent Runtime reads only approved files, parses JSON, and returns health evidence.

## PalSmith Acceptance

Accept only if content-read paths, missing items, JSON parse results, and not-run checks are clear.
