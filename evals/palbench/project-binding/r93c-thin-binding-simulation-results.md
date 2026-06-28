# R93-C Thin Binding Simulation Results

## Test date

2026-06-28 17:09:20 +08:00

## Scope

This record covers a local public-safe simulation of the current thin binding templates under `templates/project-binding/`.

No temp project was created inside this repository. No template source file was modified.

## Temp dirs

Sanitized base path:

`%TEMP%/agentpal-r93c-20260628-170851`

Simulated projects:

- Generic Codex: `%TEMP%/agentpal-r93c-20260628-170851/agentpal-r93c-generic-project`
- Claude Code: `%TEMP%/agentpal-r93c-20260628-170851/agentpal-r93c-claude-project`

## Generic Codex result

Result: Pass.

Created files:

- `.agentpal/AGENTPAL.md`
- `.agentpal/project.json`
- `AGENTS.md`

Checks:

- JSON parse result: pass
- `binding_mode`: `thin`
- `agentpal_workspace_root`: present
- `central_pal_contacts` / Pal source reference: present
- `agentpal_project_record`: present
- `keyword_routing_allowed`: `false`
- forbidden dirs count: `0`
- copied `official/pals`: no
- copied `workspace/organization/contacts/pals.json`: no
- copied `.agentpal/memory`, `.agentpal/reports`, or `.agentpal/evals`: no

## Claude Code result

Result: Pass.

Created files:

- `.agentpal/AGENTPAL.md`
- `.agentpal/project.json`
- `.claude/settings.local.json`
- `.gitignore`
- `CLAUDE.md`

Checks:

- JSON parse result: pass
- `binding_style`: `thin-binding`
- `agentpal_workspace_root`: present
- `central_contacts` / Pal source reference: present
- `agentpal_project_record`: present
- `keyword_routing_allowed`: `false`
- forbidden dirs count: `0`
- copied `official/pals`: no
- copied `workspace/organization/contacts/pals.json`: no
- copied `.agentpal/memory`, `.agentpal/reports`, or `.agentpal/evals`: no
- `.gitignore` contains `.claude/settings.local.json`

## Forbidden dirs check

Result: Pass.

The following default-forbidden project-local directories were absent in both temp projects:

- `.agentpal/memory`
- `.agentpal/state`
- `.agentpal/reports`
- `.agentpal/context`
- `.agentpal/index`
- `.agentpal/pals`
- `.agentpal/workflows`
- `.agentpal/evals`
- `.agentpal/capability-inventory`
- `.agentpal/business-systems`
- `.agentpal/reviews`
- `.agentpal/evidence`
- `.agentpal/replay`
- `.agentpal/rollback`
- `.agentpal/verification`
- `.agentpal/audit-trail`
- `.agentpal/governance-decisions`
- `.agentpal/change-ledger`
- `.agentpal/change-review`

## Central contacts path check

Result: Pass.

The generated bindings reference central contacts in the AgentPal workspace and do not copy `workspace/organization/contacts/pals.json` into the temp projects.

## No keyword routing check

Result: Pass.

Search terms checked:

- `keyword_map`
- `domain_map`
- `role_map`

Observed matches were prohibition text only:

- Generic `AGENTS.md`: states keyword routing and route maps are forbidden.
- Generic `.agentpal/AGENTPAL.md`: states keyword routing and route maps must not be used.
- Claude `CLAUDE.md`: states keyword routing and route maps are forbidden.

No generated JSON route map field was present.

## No copied Pal packs

Result: Pass.

No `official/pals` tree was copied into either temp project.

## No copied memory/reports/evals

Result: Pass.

No `.agentpal/memory`, `.agentpal/reports`, or `.agentpal/evals` directory was created in either temp project.

## Credentials and secrets check

Result: Pass.

The generated temp files had no hits for credential-like placeholders such as API key, secret, token, password, credential, or private key.

## Template source mutation check

Result: Pass.

`templates/project-binding/`, `standards/project-binding/`, `docs/01-getting-started/bind-external-project.md`, and `workspace/organization/contacts/pals.json` had no current diff from this simulation.

## Conclusion

Pass. The current thin binding templates can generate the expected minimal external project binding surface for Generic Codex and Claude Code simulations without copying AgentPal Pal Packs, central contacts, memory, reports, evals, or forbidden project-local AgentPal directories.
