# Contact Capability Card Migration

Status: v0.6 incremental upgrade.

This migration keeps the old central contacts roster intact and adds structured
capability cards beside it.

## Old Contact Shape

Existing contacts may include:

- `id`
- `display_name`
- `status`
- `pack_path`
- `role`
- `aliases`
- `direct_call`
- `contact_card`

These fields remain valid.

## New Enhancement

Each registered Pal may now include:

- `capability_card`

The value points to a JSON file under
`workspace/organization/contacts/capability-cards/`.

## Upgrade Steps

1. Confirm the target is a valid Pal Pack with `PAL.md` and `pal.json`.
2. Confirm `discoverable`, `contactable`, and collaboration permissions are on.
3. Create a capability card from
   `workspace/organization/contacts/templates/pal-capability-card.template.json`.
4. Fill both positive capability fields and negative boundary fields.
5. Add the `capability_card` path to the Pal entry in `pals.json`.
6. Do not add ordinary Skills, tools, models, plugins, knowledge packs, persona
   packs, raw repositories, or runtime adapters to contacts.

## Routing Compatibility

The capability card is not a semantic route table. It is used after AI judgement
selects a candidate Pal, to confirm the Pal is allowed to own or participate in
the current task.
