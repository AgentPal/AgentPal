# User Custom Pal Discovery Authorization Protocol

Status: R185 PalSmith no-code protocol.

This protocol defines how PalSmith can help a user explicitly authorize discovery, invocation, delegation, contacts registration, or Marketplace draft preparation for a user custom Pal. It does not implement a runtime, CLI, scanner, daemon, connector, backend service, or Marketplace backend.

## Default Rule

A user custom Pal is private by default.

Default state:

```text
visibility: private_by_default
contact_discovery: disabled_by_default
official: false
marketplace_listing: none
```

Default private means:

- the user may explicitly provide the Pal path or explicit name for a task;
- the Pal is not in central contacts;
- the Pal is not automatically discoverable by other Pals;
- the Pal cannot receive automatic delegation;
- the Pal is not an official Pal;
- the Pal is not publicly listed.

## Authorization Model

Authorization is a set of independent permission fields, not a single ladder. Opening one field must not silently open another.

| Level | Meaning | Default | Notes |
| --- | --- | --- | --- |
| `private` | Only explicit path or explicit name use | yes | No discovery, no delegation, no contacts write |
| `workspace_discoverable` | A local workspace policy may list the Pal as available | no | Does not allow automatic delegation |
| `workspace_invocable` | A unified local call entry may invoke the Pal | no | Requires caller and task scope |
| `limited_delegation` | Named Pal / Agent may delegate limited tasks | no | Requires allowed callers, tasks, context, and expiry |
| `contacts_registered` | A user-level or organization-level contacts registry may include the Pal | no | Not the same as official status; central contacts need separate approval |
| `marketplace_draft` | Draft Marketplace metadata may be prepared | no | No public listing |
| `marketplace_public_requested` | User requests public listing review | no | Requires separate review; no backend is created here |

## Required Inputs

Before proposing any authorization record, PalSmith must identify:

- `pal_id`
- `pal_name`
- `pal_path`
- current `pal.json` parse result
- current `official`, `status`, `visibility`, `contact_discovery`, and Marketplace fields
- requested authorization fields
- allowed callers
- allowed task scope
- denied task scope
- data access boundary
- memory access boundary
- expiry or review date
- revocation method

If any required input is unknown, mark it as `missing` and ask no more than three focused questions before writing an authorization plan.

## Safe First Questions

When the user says they want the custom Pal to be discoverable, ask at most:

1. Which scope do you want: workspace discoverable, unified invocation, limited delegation, contacts registration, or Marketplace draft?
2. Which Pals / Agents may discover, call, or delegate to it?
3. What task scope, expiry date, and memory/data access boundary should apply?

## Refusal Rules

PalSmith must refuse or downgrade requests that say:

- "let all Pals automatically use it";
- "make it official";
- "add it to central contacts without confirmation";
- "publish it to Marketplace now";
- "add it to company contacts so everyone can use it";
- "enable delegation without checking its collaboration boundary";
- "skip expiry, audit, and revocation";
- "use private customer data as public example material".

Safe downgrade:

```text
I can prepare a workspace_discoverable authorization record first, limited to named callers and task scope. Delegation, contacts registration, and Marketplace publication need separate approval.
```

## Authorization Record

Every authorization must leave a file-level record or Task Package proposal.
Use the workspace-root-relative template path:

```text
templates/palsmith/user-custom-pal-authorization-record.md
```

The record must include:

- requested authorization fields;
- explicit defaults for disabled fields;
- who requested and who approved;
- expiry or review date;
- revocation method;
- audit notes;
- no-contact and no-official boundaries unless separately approved.

## Policy File

If a workspace chooses to maintain a local policy, use the
workspace-root-relative template path:

```text
templates/palsmith/user-custom-pal-discovery-policy.md
```

The policy file is local governance evidence. It is not central contacts, not official roster, and not Marketplace publication.

## Contacts Boundary

`contacts_registered` is separate from discovery.

Organization-level or company contacts requests must be treated as contacts registration plus organization-level policy. They are not workspace discovery, and they must not directly write `workspace/organization/contacts/`.

Allowed after explicit approval:

- prepare a contacts eligibility review;
- propose a user-level or organization-level registry entry;
- create a Runtime Task Package for a specific approved registry target.

Forbidden by default:

- editing `workspace/organization/contacts/`;
- editing official Pal registry files;
- treating user custom Pal discovery as official roster membership.

## Delegation Boundary

`limited_delegation` requires:

- named callers;
- allowed task list;
- denied task list;
- data access limits;
- memory access limits;
- expiry or review date;
- Quinn or equivalent QA review for sensitive cases.

Discovery alone never authorizes delegation.

Invocation alone also never authorizes delegation. A workspace may allow user-initiated invocation while still denying any Pal-to-Pal or Agent-to-Pal handoff.

## Memory Boundary

Memory access is minimal by default.

Allowed only after explicit approval:

- named memory categories;
- task-scoped memory use;
- expiry or review date;
- denied private memory categories.

Forbidden by default:

- private user memory;
- private project memory;
- customer data;
- memory writeback;
- using private memory in public examples, Marketplace drafts, or official Pal assets.

## Marketplace Boundary

Marketplace draft work may include:

- draft metadata;
- source and rights review checklist;
- privacy review checklist;
- quality review checklist;
- publication request package.

Marketplace draft work must not claim:

- public listing exists;
- a Marketplace backend exists;
- the Pal has been published;
- the Pal is official.

## Revocation

Every authorization must include how to revoke it:

- remove or archive the local authorization record;
- update the local policy to disable the field;
- remove the Pal from any approved local registry target;
- confirm that central contacts and official Pal files remain unchanged unless the revocation explicitly targets a previously approved registry entry.

## Pass Criteria

Mark an authorization flow as `pass` only if:

- the user custom Pal remains non-official;
- private-by-default is preserved until explicit approval;
- discovery, invocation, delegation, contacts, and Marketplace are separated;
- disabled defaults are explicit;
- revocation and expiry/review exist;
- no central contacts write happens without a separate approved task;
- no runtime code, CLI, scanner, daemon, connector, backend service, or Marketplace backend is introduced.
