# Pal Group Pointer

Default Main Pal: Mira.

This file is a legacy thin project-local pointer, not the Pal roster source of truth. New thin bindings can omit it.

The current Pal roster must be read from the AgentPal workspace root:

- `workspace/organization/contacts/pals.json`
- `workspace/organization/contacts/PAL_CONTACTS.md`

Do not use a copied Pal list in this project as an authoritative roster. If Pals are added, removed, renamed, deprecated, or replaced in AgentPal, reload the central contacts from `agentpal_workspace_root`.

Specialist Pals are loaded lazily after direct `/pal Name` calls or case-by-case owner judgement.
