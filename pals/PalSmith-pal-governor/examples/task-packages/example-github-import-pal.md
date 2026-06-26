# Example: GitHub Import Pal

This is an example only. `https://github.com/example/legal-pal-pack` is a placeholder URL.

## User Says

`/pal PalSmith 从 https://github.com/example/legal-pal-pack 导入 Pal`

## PalSmith Questions

- May the current Agent Runtime access this URL?
- Should the resource be staged only, or staged then considered for install?
- Should any `memory/user` or `memory/project` content be read? Default: no.
- Should contacts/registry updates be proposed only?

## Plan

- Treat source as untrusted.
- Stage into `.agentpal/import-staging/legal-pal-pack/` or another approved staging path.
- Quarantine scripts, credentials, private memory, `state/`, and `reports/`.
- Produce classification and risk report before any install.

## Runtime Task Package

- `task_name`: Pal Import Staging Task Package
- `owner_pal`: PalSmith
- `executing_runtime`: current Agent Runtime
- `allowed_read_paths`: approved GitHub URL
- `allowed_write_paths`: approved staging and quarantine paths
- `forbidden_write_paths`: formal `pals/`, `contacts/`, `registry/`
- `required_exclusions`: script execution, private memory import, automatic install
- `user_confirmation_required`: yes

## Handoff To Runtime

After confirmation, the current Agent Runtime stages the source, lists files, confirms no imported script was executed, and returns a risk report.

## PalSmith Acceptance

Accept staging only if resource type, private data risk, quarantine list, and install recommendation are reported.
