# Pal Contact Source Of Truth

This is a non-binding example. It demonstrates the contact source-of-truth rule, not a fixed route.

## Principle

AgentPal discovers Pals from contacts / registry:

- `contacts/pals.json`
- `contacts/PAL_CONTACTS.md`
- `contacts/mention-aliases.md`
- `registry/pal.index.json`
- `registry/pal.index.md`
- `registry/pal-subagent-map.json`
- `registry/pal-subagent-map.md`

Individual Pal Packs do not keep their own list of other Pals.

## Collaboration Example

When a Pal needs help outside its own domain, it should not name a fixed collaborator in its professional files.

It should say:

```text
Resolve a suitable collaborator from the current AgentPal contacts / registry, then prepare a Context Packet for the selected Pal.
```

The current AI / Mira / Brain then judges case-by-case from the current request, available Pal pool, risk, assets, and output need.

## Add / Remove Behavior

When a Pal is added:

- register it in contacts / registry
- do not edit every existing Pal's knowledge files

When a Pal is removed:

- remove it from contacts / registry and public official lists
- do not leave direct-call examples or default usage docs for the removed Pal

Examples may still mention specific Pals when the example explicitly says it is non-binding. Evals may mention specific Pals as test fixtures.
