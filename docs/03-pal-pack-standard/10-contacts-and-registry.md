# Contacts And Registry

## Status

Current for AgentPal `v0.1.0-rc.1`.

`contacts/` and `registry/` are the source of truth for Pal discovery.

## Source Files

- `contacts/pals.json`
- `contacts/PAL_CONTACTS.md`
- `contacts/mention-aliases.md`
- `registry/pal.index.json`
- `registry/pal.index.md`

## What They Control

- display name
- aliases
- directory path
- role
- direct call such as `/pal Atlas`
- discoverable / contactable state
- allowed collaboration modes

## What Must Not Enter Contacts

- ordinary Skills
- plugins
- models
- MCP servers
- runtimes
- raw repositories
- knowledge packs
- persona packs

These can support a Pal, but they are not Pals unless packaged as valid Pal Pack directories and intentionally registered.

## Maintenance Rule

Adding, removing, or renaming a Pal should mainly update contacts and registry. Individual Pal Packs should not maintain hard-coded route maps for other Pals.

## Registration Flow

Copying a Pal Pack into `pals/` does not make it discoverable by itself. AgentPal resolves direct calls and Mira routing from contacts / registry, so a copied Pal Pack must be validated and registered.

Recommended prompt:

- [`../../prompts/add-pal-to-agentpal.md`](../../prompts/add-pal-to-agentpal.md) for newly copied Pal Packs
- [`../../prompts/refresh-pal-index.md`](../../prompts/refresh-pal-index.md) when contacts / registry need to be rebuilt after Pal Pack changes

Run these prompts from the AgentPal Workspace:

- Codex: open AgentPal as its own Codex project, then paste the prompt into the AgentPal project conversation.
- Claude Code: `cd <path-to-AgentPal>`, run `claude`, then paste the prompt.
- Generic CLI Agent: `cd <path-to-AgentPal>`, start the CLI agent, then paste the prompt.

If the user normally works from an external project, reinitialize that external project session after registration only if it still shows the old Pal list.
