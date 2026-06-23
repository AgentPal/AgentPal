# Rhea Release Candidate Check

This release-safe check summarizes Rhea / System Pal readiness inside the public AgentPal workspace.

## Scope

Object: `pals/Rhea-system`

Goal: confirm Rhea is a valid official bundled Pal Pack and can be published as part of AgentPal without private maintainer data.

## Checklist

- [ ] Root files exist: `README.md`, `LICENSE`, `CHANGELOG.md`, `CONTRIBUTING.md`, `THIRD_PARTY_NOTICES.md`, `SKILL.md`, `PAL.md`, `AGENTS.md`, `pal.json`, `PAL_CONTACTS.md`, `RESOURCE_INDEX.md`.
- [ ] `pal.json` parses and uses `id: rhea-system`.
- [ ] `pal.json.type` is `pal-pack`.
- [ ] Rhea is described as a system/app steward, not a direct installer or system executor.
- [ ] Runbooks require approval for system writes, installs, PATH changes, services, or destructive actions.
- [ ] Contacts contain only valid Pal Packs.
- [ ] No private logs, credentials, system reports, maintainer-local paths, or user machine state are required.

## Expected Result

Rhea can remain in the official bundled Pal set when the checklist passes. Any future standalone release should repeat this check against the standalone repository root.

