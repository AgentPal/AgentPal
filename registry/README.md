# Registry

`registry/` contains indexes for Pals and other resources.

Only `pal.index.*` is allowed to feed Pal contacts. Skills, tools, knowledge, plugins, models, MCP servers, and non-Pal runtimes are indexed separately and do not become Pals.

`registry/` and `contacts/` are the AgentPal source of truth for Pal discovery. Individual Pal Packs must not maintain local copies of the Pal list or hard-code other Pals as required collaborators.

When adding a Pal, register it in contacts / registry. When removing a Pal, remove it from contacts / registry and public official lists. Existing Pal professional assets should not need broad edits for another Pal's lifecycle change.

Initialization should automatically detect valid Pal Packs under `pals/` and update the Pal index when needed. The current public seed indexes Mira plus the official bundled specialist Pals.

When refreshing Pals, scan only `pals/`. Do not scan the whole disk or unrelated external projects.

Do not put refresh/index maintenance language in Mira's first welcome message.


