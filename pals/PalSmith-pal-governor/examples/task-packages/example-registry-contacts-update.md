# Example: Registry And Contacts Update

This is an example only. It does not update real JSON.

## User Says

`/pal PalSmith 把这个 Pal 加入通讯录`

## PalSmith Questions

- Which Pal directory is the target?
- Is it a standard Pal Pack with `PAL.md`, `SKILL.md`, `AGENTS.md`, `pal.json`, and `core/output-contract.md`?
- Is it discoverable and contactable?
- Do you approve a registry diff, a contacts diff, or suggestions only?

## Plan

- Inspect target Pal root files.
- If it is an ordinary Skill, explain it cannot enter contacts.
- Prepare separate registry and contacts diffs.
- Require exact user confirmation before writing JSON.

## Runtime Task Package

- `task_name`: registry update task package and contacts update task package
- `owner_pal`: PalSmith
- `executing_runtime`: current Agent Runtime
- `allowed_read_paths`: target Pal, `registry/pal.index.json`, `contacts/pals.json`
- `allowed_write_paths`: approved JSON files after exact confirmation
- `forbidden_write_paths`: unrelated Pal files
- `required_exclusions`: Skills, tools, models, raw repositories, private memory
- `user_confirmation_required`: yes

## Handoff To Runtime

After exact diff approval, the current Agent Runtime snapshots JSON, applies the diff, parses JSON, and reports evidence.

## PalSmith Acceptance

Accept only when the target is a valid contactable Pal Pack and parse evidence is present.
