# PalSmith v0.5 User Flow

This is the shortest user path for PalSmith v0.5.

PalSmith is a no-code Pal asset governor. It helps design Pals, Pal Teams, draft Pal Packs, user custom Pals, authorization records, and review evidence. It does not execute file changes by itself. Codex, Claude Code, OpenCode, OpenHands, or another host runtime performs approved file operations and must report evidence.

## 1. Start With A Pal Idea

Use:

```text
/pal PalSmith I want to create a Pal that helps with <job>.
```

You can describe:

- the job or responsibility;
- the thinking style;
- the voice or personality;
- the knowledge it should use;
- the Skills, Agents, workflows, memory, contacts, or Marketplace metadata it may need;
- the privacy and publication boundary.

For a copyable prompt, use [`../../prompts/palsmith/create-composite-pal.md`](../../prompts/palsmith/create-composite-pal.md).

## 2. Keep The First Result As A Draft

A draft Pal Pack is a review artifact. It is not official, not central contacts, and not discoverable by default.

PalSmith should create a plan first, then a bounded Runtime Task Package if files need to be written.

## 3. Install A Reviewed Draft As A User Custom Pal

Use [`../../prompts/palsmith/install-draft-as-custom-pal.md`](../../prompts/palsmith/install-draft-as-custom-pal.md).

A user custom Pal should stay:

- `official: false`
- private by default
- outside central contacts
- outside `official/pals/`
- not publicly listed

The host runtime may copy approved files only after explicit user confirmation.

## 4. Use A User Custom Pal Explicitly

The user may explicitly call a user custom Pal by name, path, or approved local alias.

This does not mean other Pals may automatically discover or delegate to it.

## 5. Authorize Discovery Carefully

Use [`../../prompts/palsmith/authorize-user-custom-pal-discovery.md`](../../prompts/palsmith/authorize-user-custom-pal-discovery.md).

Keep these fields separate:

- workspace discovery;
- workspace invocation;
- limited delegation;
- contacts registration;
- Marketplace draft metadata;
- public Marketplace listing request.

Discovery does not imply delegation. Contacts registration is not default behavior. Marketplace draft metadata is not public listing.

## 6. Revoke Or Reduce Authorization

Use [`../../prompts/palsmith/revoke-user-custom-pal-discovery.md`](../../prompts/palsmith/revoke-user-custom-pal-discovery.md).

Revocation should:

- preserve audit history;
- disable only the selected scope;
- keep unrelated fields unchanged;
- keep memory access minimal unless explicitly approved;
- avoid contacts and official Pal writes unless a separate governance task authorizes them.

## 7. Review And Improve Pals

PalSmith can review job fit, missing assets, knowledge quality, output contracts, privacy boundaries, and release readiness.

Quinn or another QA owner can review the evidence before the result is treated as ready.

For asset execution readiness, use:

- [`../07-pal-asset-execution/README.md`](../07-pal-asset-execution/README.md)
- [`palsmith-pal-completeness-guide.md`](palsmith-pal-completeness-guide.md)
- [`existing-pal-upgrade-asset-execution-guide.md`](existing-pal-upgrade-asset-execution-guide.md)

PalSmith should not call a Pal executable only because it has a persona or can
use a host tool. It should check assets, output a Missing Asset Plan when
needed, and ask for confirmation before controlled writes.

## What PalSmith Does Not Do

PalSmith v0.5 does not provide:

- a runtime backend;
- CLI or installer;
- daemon;
- scanner;
- connector backend;
- Marketplace backend;
- automatic central contacts writes;
- automatic public listing;
- automatic push, tag, or release.

Remote GitHub sync, tags, and releases require separate user authorization.
