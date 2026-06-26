# Example: With-Memory Export Warning

This is an example only and intentionally uses placeholder scope.

## User Says

`/pal PalSmith 导出 Research Pal，包含记忆`

## PalSmith Questions

- What is the export purpose: personal backup, computer migration, internal team migration, or public release?
- If public release, can this be changed to clean export?
- Which memory sections are allowed: `memory/user`, `memory/project`, collaboration notes, `state/`, `reports/`?
- Do you strongly confirm the private-data risk?

## Plan

- Treat as high-risk private export.
- Refuse public release with private memory unless converted to clean export.
- Include only explicitly approved memory/state/report sections.
- Generate privacy report and restore instructions.

## Runtime Task Package

- `task_name`: With Memory Export Task Package
- `owner_pal`: PalSmith
- `executing_runtime`: current Agent Runtime
- `allowed_read_paths`: target Pal plus explicitly approved memory sections
- `allowed_write_paths`: approved private export location
- `forbidden_write_paths`: public release location
- `required_exclusions`: credentials, tokens, unrelated private memory
- `user_confirmation_required`: yes, strong confirmation

## Handoff To Runtime

After strong confirmation, the current Agent Runtime creates the private export and privacy report.

## PalSmith Acceptance

Accept only if the privacy report exists and public sharing is blocked or converted to clean export.
