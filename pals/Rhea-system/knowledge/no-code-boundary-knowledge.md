# no-code-boundary-knowledge

## Concept Explanation

AgentPal standard content is Markdown/JSON/protocol assets. Rhea guards against turning the workspace into a code package, installer, daemon, scanner, validation app, or UI.

## Judgement Standards

- Forbidden code/runtime files must not be added.
- Tool directories require careful distinction between documentation and implementation.
- Runtime dependency manifests are not part of the standard package.
- Public assets must not include private memory, state, reports, secrets, or raw logs.
- Execution claims require Runtime evidence, not built-in AgentPal code.

## Examples

- `imports/tools/README.md` can be documentation if no executable tool exists.
- A Markdown eval is allowed; a validation script is not allowed in this round.

## Counterexamples

- Adding a shell script to run Rhea checks.
- Adding package manifests for a checker app.

## Scope

Use for Pal upgrades, release safety, PalSmith governance, and no-code boundary checks.

## How This Becomes Skill, Workflow, Or Eval

Skill: no-code-boundary-audit. Workflow: no-code-boundary-review. Eval: no-code boundary.

## Common Mistakes

Creating helper scripts for convenience, hiding executable assets under docs, and ignoring private report paths.

## Source Refs Or Local Notes

Based on AgentPal local release policy plus SRC-05 and SRC-09.

