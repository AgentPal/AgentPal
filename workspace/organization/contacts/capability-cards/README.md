# Contact Capability Cards

Contact Capability Cards are the structured routing and collaboration summaries
for registered Pals.

They upgrade the central contacts from a short roster into a judgement aid for
Mira and owner Pals. They do not replace full Pal Packs. They do not route by
keywords. They exist so the current AI can judge:

- what a Pal may responsibly own;
- what a Pal must not own;
- what team roles a Pal can or cannot hold;
- when the Pal should hand off;
- what context and verification style the Pal needs.

## Source Of Truth

- Pal roster: `workspace/organization/contacts/pals.json`
- Human-readable roster: `workspace/organization/contacts/PAL_CONTACTS.md`
- Capability cards: `workspace/organization/contacts/capability-cards/*.json`
- Schema: `standards/schemas/contact-capability-card.schema.json`
- Template: `workspace/organization/contacts/templates/pal-capability-card.template.json`
- Routing veto: `workspace/organization/contacts/routing-veto.md`

## Compatibility

Older contact fields remain valid. A missing capability card should be treated
as an upgrade gap, not as permission to invent a route.

When a card exists, Mira or the current owner Pal should read it after selecting
a candidate Pal and before assigning ownership. If the card vetoes the role or
task boundary, the current AI must choose another Pal, create a team/child step,
ask the user, or mark the route blocked.
