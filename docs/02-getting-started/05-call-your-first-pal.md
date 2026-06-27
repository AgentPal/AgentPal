# Call Your First Pal

Use `/pal Name` or `@Name` to call a registered Pal.

Known official calls are resolved from contacts and registry. The list below is a current display, not a separate source of truth:

- `/pal Mira`
- `/pal Atlas`
- `/pal Vega`
- `/pal Rhea`
- `/pal Quinn`
- `/pal Morgan`
- `/pal Harper`
- `/pal Nova`

## Example

```text
/pal Atlas Turn this requirement into an implementation task package.
```

Expected response shape:

```text
Atlas：I will handle it.
```

The selected Pal should then use that Pal's identity, Output Contract, and at least one relevant asset or honest fallback method.

## Unknown Pal

If a Pal name is unknown, the runtime should check `workspace/organization/contacts/pals.json` and `workspace/organization/contacts/PAL_CONTACTS.md`, report that the Pal is missing, and avoid inventing it.

## Boundary

A direct call does not start a separate runtime process. It enters the selected Pal's working mode inside the current runtime.

## Related

- [Simple Pal Mode](../01-concepts/05-simple-pal-mode.md)
- [Official Pals](../99-reference/official-pals.md)
- [Mention protocol](../06-collaboration/02-mention-protocol.md)
