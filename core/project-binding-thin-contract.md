# Project Binding Thin Contract

External project binding should be thin.

Canonical project thin binding protocol: `docs/04-runtime-guides/project-thin-binding.md`.

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
3. `core/deliverable-aware-task-judgement-gate.md`
4. `core/main-pal-conductor-gate.md`
5. `core/owner-assignment-integrity-gate.md`
6. `core/pal-asset-preflight-protocol.md`
7. `core/team-asset-preflight-protocol.md`
8. `orchestration/workflow-execution-contract-protocol.md`
9. `orchestration/workflow-closure-gate-protocol.md`
10. `core/runtime-adapter-shared-contract.md`
11. `workspace/organization/contacts/pals.json`
12. `workspace/organization/contacts/PAL_CONTACTS.md`
13. `official/pals/Mira-main/PAL.md`
14. `official/pals/Mira-main/core/output-contract.md`

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
- durable Team Pack creation, compound team design, reusable team package creation, team governance / repair, roster design, and workflow package design require PalSmith ownership after Team Pack discovery shows reuse is insufficient. Mira may intake, discover, hand off, and summarize, but must not write the PalSmith-owned durable asset body.
- a Team label is a selected team anchor, not a participant output. Expand teams into owners, participants, verifiers, and open roles, or mark the team as anchor-only.
- open roles are unfilled capability gaps, not assigned contributors.
- if Quinn or any verifier is named, record verifier output or a legal skip / block / replan reason before Closure Gate can pass.
