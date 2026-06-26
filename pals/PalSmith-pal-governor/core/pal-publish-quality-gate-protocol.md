# Pal Publish Quality Gate Protocol

Status: PalSmith v0.3 no-code protocol.

The publish quality gate decides whether a Pal or Pal team should remain draft, move to testing, become stable, or be considered publish-ready.

## Status Values

- draft
- testing
- stable
- publish-ready
- published
- deprecated
- archived

## Single Pal Gate

Check:

- `PAL.md`
- `SKILL.md`
- `AGENTS.md`
- `pal.json`
- identity files
- `skills/index.md`
- `knowledge/index.md`
- `workflows/index.md`
- `evals/definition-of-done.md`
- `README.md`
- no private memory
- no runtime state or private reports
- registry / contacts consistency
- current `no_runtime_code` standard
- Clean Export safety
- With Memory Export strong confirmation
- ordinary Skill not in contacts

## Pal Team Gate

Check:

- `TEAM.md`
- `team.json`
- unique team Pal ids
- owner present
- verifier present
- consultants present
- Context Packet rules
- team capability map
- conflict detection result
- team eval plan
- team-local / global contacts boundary

## Output

`Publish Quality Gate Report`:

- recommended status
- must-fix items
- should-fix items
- acceptable risks
- user confirmation questions
- `done`, `missing`, and `not-run`

## Boundary

The gate recommends status. Version or status changes require a separate confirmed Runtime Task Package.
