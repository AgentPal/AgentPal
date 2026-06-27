# Central Pal Roster Standard

The central Pal roster source of truth is:

- `workspace/organization/contacts/pals.json`
- `workspace/organization/contacts/PAL_CONTACTS.md`

The roster must state:

- `source_of_truth: true`
- `routing_policy: ai_judgement_only`
- `keyword_routing_allowed: false`
- each Pal status
- each Pal Pack path
- each Pal contact card path
- deprecation and replacement mechanisms

README files may summarize the roster, but they are not the source of truth.

External project bindings must point back to the central roster instead of copying it into the project.
