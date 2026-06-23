# Vega Release Candidate Check

This release-safe check summarizes Vega / Research Pal readiness inside the public AgentPal workspace.

## Scope

Object: `pals/Vega-research`

Goal: confirm Vega is a valid official bundled Pal Pack and can be published as part of AgentPal without private maintainer data.

## Checklist

- [ ] Root files exist: `README.md`, `LICENSE`, `CHANGELOG.md`, `CONTRIBUTING.md`, `THIRD_PARTY_NOTICES.md`, `SKILL.md`, `PAL.md`, `AGENTS.md`, `pal.json`, `PAL_CONTACTS.md`, `RESOURCE_INDEX.md`.
- [ ] `pal.json` parses and uses `id: vega-research`.
- [ ] `pal.json.type` is `pal-pack`.
- [ ] Vega does not claim to be a browser, crawler, search engine, or final fact authority.
- [ ] Research examples separate facts, inferences, recommendations, uncertainty, and source status.
- [ ] Research cards are reference cards, not copied third-party packages.
- [ ] Contacts contain only valid Pal Packs.
- [ ] No private user memory, project state, reports, secrets, or maintainer-local paths are required.

## Expected Result

Vega can remain in the official bundled Pal set when the checklist passes. Any future standalone release should repeat this check against the standalone repository root.

