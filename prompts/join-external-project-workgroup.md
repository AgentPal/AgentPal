# Join External Project Workgroup

Use this inside the AgentPal Workspace when the user asks to add AgentPal to an external project.

This prompt creates a thin project binding. It must not copy the full AgentPal rule body into the external project.

```text
Add AgentPal to the requested external project as a thin project binding.

Resolve the external project:
1. If the runtime provides a project list, inspect it first.
2. If the user provided a path, use that path.
3. If unclear, ask for the project path.

Do not bind AgentPal to the AgentPal workspace itself unless the user explicitly says they are developing AgentPal itself.

Create or update only:
- `.agentpal/project.json`
- `.agentpal/AGENTPAL.md`
- root `AGENTS.md` protected AgentPal block
- root `CLAUDE.md` protected AgentPal block only for Claude Code
- `.claude/settings.local.json` only for Claude Code

Use the AgentPal workspace templates:
- `projects/project-workgroup-template/agentpal/project.json`
- `projects/project-workgroup-template/agentpal/AGENTPAL.md`
- `projects/project-workgroup-template/agentpal/INIT_AGENTPAL_PROJECT_PROMPT.md`
- `templates/project-binding/root-agents-agentpal-block-template.md`

Do not copy optional `.agentpal/state`, `.agentpal/memory`, `.agentpal/reports`, `.agentpal/context`, or `.agentpal/index` folders by default.

Do not copy:
- full Pal list
- full Mira assets
- full orchestration protocols
- full docs
- examples
- evals
- release notes
- PalBench reports

The root `AGENTS.md` / `CLAUDE.md` block must point the runtime to current core gates in the AgentPal workspace:
1. core/agentpal-core-gate.md
2. core/first-pal-gate.md
3. core/simple-pal-mode-runtime-contract.md
4. core/deliverable-aware-task-judgement-gate.md
5. core/main-pal-conductor-gate.md
6. core/runtime-adapter-shared-contract.md
7. core/project-binding-thin-contract.md
8. core/runtime-response-gate.md

Pal source of truth remains:
- contacts/pals.json
- registry/pal.index.json

Mira entry remains:
- pals/Mira-main/PAL.md
- pals/Mira-main/core/output-contract.md

The root `AGENTS.md` / `CLAUDE.md` block must also explicitly tell a fresh session to enter AgentPal project-bound mode when loaded, start ordinary messages with Mira, start every AgentPal-mode natural-language reply with the current speaking Pal prefix, apply First Pal Gate before substantive work, and require a visible Pal-prefixed owner judgement before any Runtime tool call, Bash / shell command, MCP call, file write, project inspection, or system inspection. If the selected owner is not the current speaking Pal, that owner Pal must speak with its own prefix before the tool call. Composite deliverable tasks name selected or provisional stage owner Pals through AI judgement and current contacts / registry before broad clarification, handoff, or execution. Implementation-shaped final deliverables require AI owner judgement before Runtime execution; Atlas is only a possible candidate from current contacts / registry, not an automatic route from words such as HTML, page, frontend, code, or repository. For tasks the AI judges to involve local system/app state, permission or safety boundaries, runtime/environment readiness, command failure recovery, system-impact risk, or execution-layer diagnostic evidence, the block should require a system-owner judgement before any command or inspection. Rhea is a case-specific candidate from the current registry, not a keyword route or fixed task-domain map.

For Claude Code, create or merge `.claude/settings.local.json` so `permissions.additionalDirectories` contains the AgentPal workspace root. Add `.claude/settings.local.json` to `.gitignore`.

After binding, report:
- active project root
- AgentPal workspace root
- runtime hint
- files created or updated
- whether Claude Code local settings were updated
- that project binding is thin and reads AgentPal core gates from the workspace
- that official Pals are read from contacts / registry
- that v0.1 uses Simple Pal Mode only

If the target runtime has an already-open session, recommend reloading the project instructions or restarting the session.
```
