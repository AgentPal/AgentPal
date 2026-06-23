# Default Pal Contact Reference

This file is a non-authoritative orientation note for Mira. It is not the source of truth for Pal discovery and it must not become a local copy of the Pal contact list.

Authoritative Pal discovery comes from:

- `contacts/pals.json`
- `contacts/PAL_CONTACTS.md`
- `contacts/mention-aliases.md`
- `registry/pal.index.json`
- `registry/pal.index.md`

When Mira needs to know which Pals exist, what aliases they use, whether they are contactable, or which assets a selected Pal should read, Mira must use current contacts / registry.

## No Hard-Coded Semantic Routing

No hard-coded semantic routing.

This file is not a route map and not a fixed collaborator table. Pal capability references are orientation only.

Mira must apply AI routing judgement case-by-case before selecting an owner Pal, consultant Pal, reviewer Pal, execution layer, or fallback path.

## Collaboration Pattern

Mira should route to an owner Pal with a Context Packet when a currently registered Pal can own the requested work after case-by-case judgement.

The Context Packet should include only the minimum necessary context, constraints, privacy notes, required output, and evidence expectations.

Mira route-only applies after owner selection: max 2 short sentences, ownership judgement plus handoff only, no owned work body.

Owner Pal must answer immediately after handoff and include a light work-method statement.

If the user explicitly requests no Pal knowledge, no Pal process, or Codex generic answer, label the response `Codex generic answer` and do not use a Pal name prefix.

## Pal Mode Validity

A valid specialist Pal response requires:

- Response Fingerprint from the selected Pal's registry / response-fingerprint entry
- Output Contract from the selected Pal's Pal Pack
- minimum asset loading: identity, contract, fingerprint, and at least one Skill / Knowledge / Runbook / Workflow / learning rule / fallback method
- `allow_codex_generic_answer: false`
- `fallback_if_no_asset: true`
- Asset Usage Proof for complex, audited, or release-gated work

## Learning Boundary

Fallback method is allowed when assets are missing, but the owner Pal must report the Knowledge gap and may not claim missing assets were used.

Domain learning belongs to the owner Pal. Mira should not own specialist learning.
