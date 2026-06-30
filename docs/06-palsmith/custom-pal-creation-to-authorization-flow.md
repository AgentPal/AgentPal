# PalSmith Custom Pal Creation To Authorization Flow

This guide gives one user-facing path for moving from a Pal idea to a private user custom Pal with optional discovery authorization.

PalSmith remains a no-code Pal asset governor. It prepares plans, evidence, and Runtime Task Packages. The host runtime performs any approved file reads or writes and must report evidence.

## Flow

1. Start with a Pal idea.
   Use [`../../prompts/palsmith/create-composite-pal.md`](../../prompts/palsmith/create-composite-pal.md) when the Pal needs a role, thinking style, voice, job knowledge, Skills, evals, and privacy boundaries.

2. Keep the first result as a draft.
   Draft Pal Packs are review artifacts. They are not official Pals, not central contacts, and not workspace-discoverable by default.

3. Review the draft before installation.
   Check identity, job fit, asset completeness, source permission, privacy class, output contract, and rollback notes.

4. Install only after user confirmation.
   Use [`../../prompts/palsmith/install-draft-as-custom-pal.md`](../../prompts/palsmith/install-draft-as-custom-pal.md) to prepare a bounded installation plan and Runtime Task Package. The target remains under user custom Pal storage, not `official/pals/`.

5. Keep the installed Pal private by default.
   A user custom Pal starts with:

   - `official: false`
   - private or local visibility
   - discovery disabled by default
   - no central contacts write
   - no public Marketplace listing

6. Invoke explicitly before enabling discovery.
   The user may call the custom Pal by explicit path or approved local alias. General Pal discovery must still refuse to surface it until authorization exists.

7. Authorize discovery only as a scoped decision.
   Use [`../../prompts/palsmith/authorize-user-custom-pal-discovery.md`](../../prompts/palsmith/authorize-user-custom-pal-discovery.md). Discovery, invocation, limited delegation, contacts registration, and Marketplace draft work are separate fields. One field does not imply another.

8. Revoke authorization when needed.
   Use [`../../prompts/palsmith/revoke-user-custom-pal-discovery.md`](../../prompts/palsmith/revoke-user-custom-pal-discovery.md). Revocation should preserve audit records, disable the selected scope, and avoid silent deletion.

## Boundaries

- Do not write `workspace/organization/contacts/` unless the user gives a separate governance authorization.
- Do not move a custom Pal into `official/pals/` without official Pal promotion review.
- Do not turn discovery into automatic delegation.
- Do not claim Marketplace publication when only Marketplace draft metadata exists.
- Do not create runtime code, CLI tools, installers, scanners, daemons, connectors, backend services, or app runtime features.
- Do not treat a planning document as execution evidence.

## Evidence Chain

The R190 closeout matrix is recorded in [`../../evals/palbench/v0.5/palsmith/r190-palsmith-custom-pal-creation-authorization-integrated-matrix.md`](../../evals/palbench/v0.5/palsmith/r190-palsmith-custom-pal-creation-authorization-integrated-matrix.md).
