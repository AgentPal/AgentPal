# User Custom Pal Discovery Authorization

User custom Pals are private by default. Installing or copying a user custom Pal does not make it official, does not add it to central contacts, and does not let other Pals automatically discover or delegate to it.

Use this guide when a user wants to make a user custom Pal easier to find or call inside a workspace.

## Core Rule

The user must explicitly authorize every permission.

Discovery, invocation, delegation, contacts registration, and Marketplace draft work are separate. Enabling one does not enable the others.

## Authorization Levels

| Authorization | Meaning | Default |
| --- | --- | --- |
| `private` | Explicit path or explicit name use only | enabled |
| `workspace_discoverable` | The workspace may list the Pal as available | disabled |
| `workspace_invocable` | A local unified call entry may invoke the Pal | disabled |
| `limited_delegation` | Named Pals / Agents may delegate limited tasks | disabled |
| `contacts_registered` | A specific user-level or organization-level contacts registry may include it | disabled |
| `marketplace_draft` | Draft Marketplace metadata may be prepared | disabled |
| `marketplace_public_requested` | Public listing review is requested | disabled |

These are permission fields, not a linear ladder. A Pal can be workspace-discoverable but still not delegable. A Pal can have Marketplace draft metadata but still not be publicly listed.

## Required Authorization Record

Use this template:

```text
templates/palsmith/user-custom-pal-authorization-record.md
```

The record must state:

- target Pal id, name, and path;
- requested permissions;
- allowed callers;
- allowed and denied task scope;
- data and memory access boundary;
- approval identity;
- expiry or review date;
- revocation steps;
- audit notes.

Default values must remain conservative:

- delegation: `false`
- contacts registration: `false`
- Marketplace: `none` or `draft_only`
- public listing: `false`
- official status: `false`

## Safe Flow

1. Read the target user custom Pal `pal.json`.
2. Confirm it is `status: user_custom_pal` and `official: false`.
3. Ask no more than three focused questions about scope, callers, and expiry/data boundaries.
4. Generate an authorization record or Task Package proposal.
5. Ask for explicit approval before any local policy or registry file write.
6. Keep central contacts unchanged unless a separate contacts governance task is approved.
7. Keep official Pal files unchanged.
8. Record revocation instructions.

Memory access is minimal by default. Private user memory, private project memory, customer data, and memory writeback stay disabled unless a separate explicit approval names the allowed memory category, task scope, expiry or review date, and denied memory categories.

## Example Safe Response

If the user says:

```text
I want this custom Pal to be discoverable in the workspace.
```

PalSmith should ask:

```text
Which scope do you want: workspace discoverable, unified invocation, limited delegation, contacts registration, or Marketplace draft?

Which Pals / Agents may discover or call it?

What task scope, expiry date, and data or memory boundary should apply?
```

If the user says:

```text
Let all Pals automatically use it.
```

PalSmith should refuse the full request and offer:

```text
I can prepare a workspace_discoverable authorization record first, limited to named callers and task scope. Delegation, contacts registration, and Marketplace publication need separate approval.
```

If the user says:

```text
Add it to company contacts so everyone can use it.
```

PalSmith should separate:

- workspace discovery;
- workspace invocation;
- contacts registration;
- organization-level policy;
- limited delegation.

It must not directly modify `workspace/organization/contacts/` from that request.

## Marketplace Boundary

Marketplace work is also split:

- `marketplace_draft`: prepare metadata only;
- `marketplace_public_requested`: prepare a publication request and review checklist;
- public listing: not available from this protocol.

This protocol does not create a Marketplace backend, public listing, payment flow, connector, scanner, daemon, CLI, or runtime implementation.

## Next Reading

- [PalSmith index](README.md)
- [Full authorization protocol](user-custom-pal-discovery-authorization-protocol.md)
- [Draft to user custom Pal installation](../../prompts/palsmith/install-draft-as-custom-pal.md)
- [Authorization prompt](../../prompts/palsmith/authorize-user-custom-pal-discovery.md)
- [Revocation prompt](../../prompts/palsmith/revoke-user-custom-pal-discovery.md)
- [Authorization record template](../../templates/palsmith/user-custom-pal-authorization-record.md)
- [Discovery policy template](../../templates/palsmith/user-custom-pal-discovery-policy.md)
