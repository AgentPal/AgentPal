# Public And Private Boundary

## Status

Current for AgentPal `v0.1.0-rc.1`.

Public Pal Packs should contain release-safe Markdown, JSON, templates, examples, evals, and placeholders. They must not contain private runtime data.

## Do Not Publish

- API keys, tokens, passwords, secrets, credentials, or private keys
- private user memory
- real user conversation history
- private project state
- customer data
- proprietary project data
- real task reports or internal development reports
- local absolute paths
- unauthorized third-party full text
- future feature claims written as current behavior

## Public-Safe Content

- Pal Pack root files
- public-safe identity, knowledge, Skills, runbooks, and workflows
- placeholder README files for memory, state, and reports
- synthetic examples
- public-safe evals
- templates and checklists

## Directory Watchlist

Review these before release:

- `memory/`
- `state/`
- `reports/`
- `official/pals/*/memory/`
- `official/pals/*/state/`
- `official/pals/*/reports/`
- `examples/`
- `evals/`
- `imports/`

## Future Design Boundary

Future child workflow, Subagent Mode, marketplace, desktop app, web app, and runtime-adapter material must be marked as future or not active in `v0.1.0-rc.1`.
