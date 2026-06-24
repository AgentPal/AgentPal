# Contacts

`contacts/` contains the AgentPal Pal contacts.

Only valid Pal Packs can enter contacts. Ordinary Skills, tools, models, MCP servers, plugins, non-Pal runtimes, raw repositories, knowledge packs, and persona packs must not be added here.

Contacts are the source of truth for Pal discovery together with `registry/`. Individual Pal Packs must not maintain their own hard-coded lists of other Pals.

When adding a Pal, register it here and in the Pal registry. When removing a Pal, remove it here and from the Pal registry. Existing Pal professional knowledge, skills, workflows, and runbooks should not need broad edits just because another Pal was added, removed, or renamed.

Normal initialization reads the current contacts / registry files. Copying a Pal Pack into `pals/` does not register it by itself; use `prompts/add-pal-to-agentpal.md` or `prompts/refresh-pal-index.md` from the AgentPal Workspace when contacts need to be updated. The current public seed includes Mira plus the official bundled specialist Pals.

Do not expose contact/index maintenance in Mira's first welcome message. Users only need to hear about add/refresh steps when they ask how to add a new Pal or when a Pal cannot be found.

## Unknown or invalid directories

Directories that look like Pals but fail validation belong in `contacts/discovered-candidates.md`, not in `contacts/pals.json`.

Do not promote a candidate until it has valid Pal Pack files and collaboration permissions.


