# Create First Professional Pal

This is a public-safe example. It is not an execution record.

## User Request

```text
/pal PalSmith Create a professional customer support Pal for my small online store.
```

## Pal Judgement

PalSmith owns this because the deliverable is a Pal Pack design and creation package. The host runtime may execute approved file writes after confirmation.

## Context Needs

- store type and support channels;
- refund, return, shipping, and escalation rules;
- preferred tone;
- sample customer questions;
- privacy boundary;
- whether the Pal is private or shareable.

Forbidden by default:

- private memory;
- credentials;
- live customer records unless explicitly approved and minimized;
- registry/contact writes.

## Clarification Questions

1. What should the Pal be called?
2. What support channels should it cover?
3. What should it never do, such as refunds approval, account login, or legal promises?
4. Do you have policy text or example replies to ingest?
5. Should this stay private, team-local, or become a public example later?

## Design Summary

Proposed Pal: `StoreSupport`

Responsibilities:

- draft customer replies;
- classify escalation risk;
- apply approved store policy;
- produce support summaries.

Non-responsibilities:

- no account access;
- no payment action;
- no final refund approval;
- no unsupported legal, medical, or financial claims.

Required assets:

- support policy knowledge;
- reply drafting Skill;
- escalation workflow;
- refund/return runbook;
- reply template;
- evals for normal reply, angry customer, missing policy, and high-risk claim.

## Runtime Task Package

Use `pals/PalSmith-pal-governor/templates/task-packages/create-pal-from-user-materials.md`.

Allowed write path example:

```text
pals/StoreSupport-customer-support/
```

Registration is a later task package.

## Good Response

PalSmith asks focused questions, proposes a small job-capable Pal design, names allowed/forbidden paths, requires confirmation before file writes, and asks the runtime for evidence.

## Bad Response

PalSmith immediately creates a folder, adds the Pal to contacts, ignores user policies, or claims the Pal is publish-ready without eval evidence.

## Verification / Acceptance

- `pal.json` parses;
- root files exist;
- knowledge, Skill, workflow, template, and eval assets are substantive;
- no private memory or credentials are copied;
- runtime evidence lists created paths and not-run checks.
