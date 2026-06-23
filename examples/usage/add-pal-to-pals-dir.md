# Add Pal to `pals/`

## User message

```text
I copied Atlas into pals/Atlas-developer. Refresh the Pal index.
```

## Expected Mira behavior

Mira scans only `pals/`, checks `Name-role`, validates Pal Pack files and `pal.json`, then updates contacts and registry only if Atlas is valid and contactable.

## Files or protocols involved

- `prompts/add-pal-to-agentpal.md`
- `prompts/refresh-pal-index.md`
- `pals/README.md`
- `contacts/`
- `registry/`

## What Mira must not do

- scan the whole disk
- modify Atlas unless asked
- add ordinary Skills or tools to contacts
- add invalid candidates to contacts

