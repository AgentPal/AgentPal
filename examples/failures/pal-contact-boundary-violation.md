# Pal Contact Boundary Violation

This is a failure example, not a routing rule.

## Bad user/assistant exchange

User:

```text
把  加进 Pal 通讯录。
```

Assistant:

```text
Mira：好的，我把  作为  旁边的新 Pal contact。
```

## Why it is wrong

 is 's optional tool asset, not a Pal Pack. Tools, Skills, models, plugins, MCP servers, non-Pal runtimes, and raw repositories must not enter Pal contacts.

## Correct behavior

Mira explains that only valid Pal Packs can enter contacts.  remains under `` as 's optional tool asset.

## Related eval

- `evals/pal-contacts-boundary-check.md`
- `evals/pal-contact-boundary-check.md`

## Related protocol

- `contacts/PAL_CONTACTS.md`
- `agentpal.json`


