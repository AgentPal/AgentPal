# No Code AgentPal Boundary Knowledge

## Concept explanation

AgentPal v0.1 is a Markdown / JSON / protocol workspace. Atlas can improve development-facing Pal assets, but must not turn AgentPal into a code app, CLI, scanner, validator, installer, exporter, importer, daemon, or UI.

## Judgement standards

- Allowed release assets are Markdown, JSON, JSONL examples, README files, templates, workflows, runbooks, evals, and public-safe docs.
- Disallowed additions include `.py`, `.js`, `.ts`, `.rs`, `.ps1`, `.sh`, `.bat`, `.cmd`, package manifests, requirements, Cargo manifests, executable tools, and tool directories.
- Runtime may run commands for evidence, but AgentPal must not ship those commands as built-in tools.
- Private memory, state, and reports must not become public release content.

## Examples

- Good: Add a Runtime Task Package template as Markdown.
- Good: Add a manual eval checklist.
- Good: Report that Playwright verification was not run instead of adding a test runner.

## Counterexamples

- Bad: Add `validator.py` to check Pal Packs.
- Bad: Add a CLI installer.
- Bad: Write private user memory into public examples.

## Scope

Use for all AgentPal workspace development and default Pal deepening.

## How it becomes skill / workflow / eval

Use with risk, release, file boundary, and self-health checks.

## Common mistakes

- Adding a tool to make validation easier.
- Treating no-code as "no validation".
- Forgetting ignored private report directories.

## Source references or local notes

Local: AgentPal root AGENTS and release no-code boundary. External: A02 as runtime distinction context.
