# Pal Registry Contacts Knowledge

## Concept

Registry and contacts make valid Pal Packs discoverable and callable. They are not storage for ordinary Skills, tools, models, plugins, or raw repositories.

## Judgement Standards

- Target must be a standard Pal Pack.
- `id`, path, display name, aliases, and direct call must be consistent.
- Contactable Pals need allowed collaboration modes.
- Test-only Pals must be marked test-only and not official.
- Global contacts should not be used for team-local helpers without reason.

## Examples

PalSmith can propose registry and contacts diffs for a completed Pal Pack after quality inspection and user confirmation.

## Counterexamples

- adding a Markdown skill to contacts
- registering a blueprint as an installed Pal
- marking test Pal official
- writing contacts during import staging

## Scope

Use for registration, direct-call verification, runtime call verification, team governance, and publish readiness.

## Convert To Assets

Registry/contact changes become separate Runtime Task Packages with exact JSON diff approval and JSON parse verification.

## Common Errors

- merging registry and contacts writes into unrelated creation tasks
- skipping duplicate alias checks
- using contacts as a capability list
