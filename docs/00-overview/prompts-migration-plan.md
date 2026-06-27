# Prompts Migration Plan

R77 leaves root `prompts/` in place because many user-facing docs and runtime setup flows still point to copyable prompts there.

## Current Prompt Families

| current family | role | future home |
| --- | --- | --- |
| `prompts/codex/` | Codex workspace initialization and removal prompts | stay at root until runtime docs are migrated |
| `prompts/claude-code/` | Claude Code project-first install/remove/verify prompts | stay at root until runtime docs are migrated |
| `prompts/generic-cli-agent/` | generic CLI install/remove prompts | stay at root until runtime docs are migrated |
| `prompts/project-workgroup/` | project workgroup prompt pointers | `templates/prompts/project-workgroup/` or archive |
| maintenance prompts | maintainer operations | `templates/prompts/maintenance/` if reusable; archive if historical |

## Target Split

- Runtime entry prompts may remain under root `prompts/` while docs use them as direct copy targets.
- Reusable prompt templates should move to `templates/prompts/`.
- Historical prompts should move to `archive/migration-from-v0.3/root-legacy/prompts/`.
- Internal development prompts must not be committed to the public workspace.

## Migration Rounds

1. R79: inventory all docs and README references to `prompts/`.
2. R79: move reusable non-entry prompts to `templates/prompts/` with compatibility links.
3. R80: decide whether runtime entry prompts remain at root permanently or move after docs are updated.
4. R80: archive obsolete prompts and update removal/checklist docs.

## Boundaries

- Prompts are Markdown instructions, not installers or scripts.
- Do not add CLI, web app, desktop app, scanner, validator, daemon, database, auto sync, or auto execution.
- Project binding prompts must continue to install thin binding only.
