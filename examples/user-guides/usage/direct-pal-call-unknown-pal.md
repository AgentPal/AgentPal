# Direct Pal Call: Unknown Pal

## User Message

```text
/pal Echo Please review this launch plan.
```

## Expected Mira Behavior

Mira checks `contacts/pals.json` and `registry/pal.index.json`, reports that Echo is not indexed, and suggests copying a valid Echo Pal Pack into `pals/Echo-role/` before refreshing the Pal index.

## Files or Protocols Involved

- `pals/Mira-main/core/direct-pal-call-protocol.md`
- `contacts/pals.json`
- `registry/pal.index.json`

## What Mira Must Not Do

- invent Echo
- roleplay Echo
- add Echo to contacts without a valid Pal Pack

