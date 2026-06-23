# Pal Discovery Rules

A directory can enter contacts only if it has:

- `PAL.md`
- `SKILL.md`
- `pal.json`
- type `pal-pack`
- display name
- aliases or a clear display-name alias
- discoverable permission
- contactable permission
- at least one collaboration mode

Scan only `pals/` during AgentPal initialization or index refresh. Do not scan the whole disk and do not read unrelated projects unless the user explicitly asks.

## Current Expected Scan

The current Pal list is discovered from valid Pal Pack directories and then written to contacts / registry. This file must not maintain a second list of expected Pal names.

If a directory is missing, invalid, or not present in contacts / registry, do not invent it. Report it as missing or unavailable and leave it out of contacts until a valid Pal Pack exists.

Tools inside external Pal directories are not contacts.

