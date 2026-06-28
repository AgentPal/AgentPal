# No Stale Pal List In Project Binding Self-Test

## Status

Current for AgentPal `v0.1.0-rc.1`.

## Purpose

Verify that external projects do not store an authoritative copied Pal roster.

## Pass Conditions

- Project binding names `workspace/organization/contacts/pals.json` and `workspace/organization/contacts/PAL_CONTACTS.md` as source of truth.
- Legacy project-local copied roster files are not part of the current thin binding surface.
- Runtime adapters say current official Pals are read from central contacts.
- Adding or removing a Pal in the AgentPal workspace requires central contacts refresh, not external project rule edits.

## Fail Conditions

- A project-local copied roster file contains a long authoritative roster.
- root `AGENTS.md` / `CLAUDE.md` contains a copied Pal list as a rule.
- verification passes by checking a hard-coded count of bundled Pals instead of reading central contacts.
