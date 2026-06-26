# Example: Clean Export Research Pal

This is an example only. It does not represent a real Pal export.

## User Says

`/pal PalSmith 导出 Research Pal，不含记忆`

## PalSmith Questions

- Which exact Pal directory should be exported?
- Where should the clean export be written?
- Is this for public sharing?
- Should an archive be created, or only an export directory?

## Plan

- Include public-safe root files, identity, core, knowledge, skills, workflows, evals, and README files.
- Exclude `memory/user/`, `memory/project/`, `state/`, `reports/`, logs, cache, credentials, tokens, and executable files.
- Generate `export-manifest.json` and `export-report.md`.

## Runtime Task Package

- `task_name`: Clean Pal Export Task Package
- `owner_pal`: PalSmith
- `executing_runtime`: current Agent Runtime
- `allowed_read_paths`: approved Research Pal public files
- `allowed_write_paths`: approved export location
- `forbidden_write_paths`: source Pal mutation
- `required_exclusions`: memory/user, memory/project, state, reports, credentials, tokens
- `user_confirmation_required`: yes

## Handoff To Runtime

After confirmation, the current Agent Runtime builds the clean export and returns included/excluded file lists.

## PalSmith Acceptance

Accept only if private runtime data is absent and the manifest/report are present.
