# R251 Old Terminology Active Entry Scan

## Scan Terms

- `Simple Pal Mode`
- `simple pal mode`
- `Current active mode`
- `Current v0.1 patterns`
- `Current v0.1 output`
- `v0.1`

## Active Entry Findings

| Path | Finding | Classification |
| --- | --- | --- |
| `core/agentpal-core-gate.md` | `Current active mode: v0.6 no-code Pal / Team orchestration.` | pass |
| `plugins/codex/plugins/agentpal/skills/agentpal-repair/SKILL.md` | Mentions old phrases as examples to clean during repair. | allowed negative/repair example |
| `agentpal.json` | Schema field still says `agentpal.workspace.v0.1`. | schema metadata, not active runtime mode |

## Non-Fresh-Read Residuals

The scan still finds old Simple Pal Mode / v0.1 text in legacy knowledge, examples, research notes, and some non-default Pal core files, especially under `official/pals/Mira-main/`.

Examples:

- `official/pals/Mira-main/templates/task-packages/mira-composite-deliverable-task-package.md`
- `official/pals/Mira-main/core/context-packet-protocol.md`
- `official/pals/Mira-main/knowledge/*`
- `official/pals/Mira-main/examples/*`
- `official/pals/Quinn-quality/research/*`

R251 classification: not a fresh install active entry blocker because the current short load order does not load these files by default. They should be tracked as cleanup debt for a later legacy-content cleanup pass.

## Result

old_terminology_active_entry_scan: pass_with_residual_debt

active_entry_blocker_found: false
