# Direct Pal Call: Known Pal

## User Message

```text
/pal Name Help me turn this request into a task.
```

## Expected Mira Behavior

Mira resolves `/pal Name`, confirms the Pal is indexed, and prepares a consult-mode Context Packet for the resolved Pal unless the user explicitly asks for delegation or handoff.

## Files or Protocols Involved

- `contacts/mention-aliases.md`
- `contacts/pals.json`
- `registry/pal.index.json`
- `pals/Mira-main/core/direct-pal-call-protocol.md`
- `pals/Mira-main/core/context-packet-protocol.md`

## What Mira Must Not Do

- treat `/pal Name` as a shell command
- route ordinary future messages to that Pal forever
- expose unrelated context to that Pal

