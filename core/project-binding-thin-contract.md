# Project Binding Thin Contract

External project binding should be thin.

The external project is the active user project. The AgentPal workspace is only a Pal source and routing reference.

## Required Files

Required in an external project:

- `.agentpal/project.json`
- `.agentpal/AGENTPAL.md`
- root `AGENTS.md` protected AgentPal block

Required for Claude Code projects:

- root `CLAUDE.md` protected AgentPal block
- `.claude/settings.local.json` with `permissions.additionalDirectories` including the AgentPal workspace root

## Optional / Lazy-Created

Create only when needed:

- `.agentpal/state/`
- `.agentpal/memory/`
- `.agentpal/reports/`
- `.agentpal/context/`
- `.agentpal/index/`

## Do Not Copy Into Project Binding

- full Pal list as source of truth
- full Mira assets
- full orchestration protocols
- full docs
- full examples
- full evals
- release notes
- PalBench reports

## Read From AgentPal Workspace

Before responding as AgentPal, the runtime should use `.agentpal/project.json` to locate `agentpal_workspace_root`, then read:

1. `core/agentpal-core-gate.md`
2. `core/first-pal-gate.md`
3. `core/simple-pal-mode-runtime-contract.md`
4. `core/deliverable-aware-task-judgement-gate.md`
5. `core/main-pal-conductor-gate.md`
6. `core/runtime-adapter-shared-contract.md`
7. `workspace/organization/contacts/pals.json`
8. `workspace/organization/contacts/PAL_CONTACTS.md`
9. `official/pals/Mira-main/PAL.md`
10. `official/pals/Mira-main/core/output-contract.md`

The project binding is a pointer and state holder, not a copy of AgentPal.

## Fresh Session Activation

The root `AGENTS.md` / `CLAUDE.md` protected block must explicitly tell a fresh session to enter AgentPal project-bound mode when the file is loaded.

At minimum, the block should say:

- ordinary messages start with Mira
- every AgentPal-mode natural-language reply starts with the current speaking Pal prefix
- generic runtime answers are used only when the user explicitly asks for generic runtime / no AgentPal / no Pal mode
- substantive tasks run the First Pal Gate before work begins
- composite deliverable tasks name selected or provisional stage owner Pals through AI judgement and current contacts / registry before broad clarification, handoff, or execution
- implementation-shaped final deliverables require AI owner judgement before Runtime execution. Atlas is only a possible candidate from current contacts / registry, not an automatic route from words such as HTML, page, frontend, code, or repository.
- tasks the AI judges to involve local system/app state, permission or safety boundaries, runtime/environment readiness, command failure recovery, system-impact risk, or execution-layer diagnostic evidence should receive a system-owner judgement before any command or inspection. Rhea is a case-specific candidate from the current registry, not a keyword route or fixed task-domain map.
