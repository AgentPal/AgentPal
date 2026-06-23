# Atlas Release Candidate Check

This release-safe check summarizes suitable implementation collaborator readiness inside the public AgentPal workspace.

## Scope

Object: `pals/Atlas-developer`

Goal: confirm Atlas is a valid official bundled Pal Pack and can be published as part of AgentPal without private maintainer data.

## Checklist

- [ ] Root files exist: `README.md`, `LICENSE`, `CHANGELOG.md`, `CONTRIBUTING.md`, `THIRD_PARTY_NOTICES.md`, `SKILL.md`, `PAL.md`, `AGENTS.md`, `pal.json`, `PAL_CONTACTS.md`, `RESOURCE_INDEX.md`.
- [ ] `pal.json` parses and uses `id: atlas-developer`.
- [ ] `pal.json.type` is `pal-pack`.
- [ ] `PAL.md` states Atlas is a suitable implementation collaborator, not an execution Runtime.
- [ ] Skills are documentation/runbook assets, not hidden scripts.
- [ ] Contacts contain only valid Pal Packs.
- [ ] No private user memory, project state, reports, secrets, or maintainer-local paths are required.
- [ ] Examples use public repository-relative paths or placeholders.

## Expected Result

Atlas can remain in the official bundled Pal set when the checklist passes. Any future standalone release should repeat this check against the standalone repository root.

