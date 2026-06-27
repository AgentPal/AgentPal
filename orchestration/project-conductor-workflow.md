# Project Conductor Workflow

Project Conductor is a no-code workflow for project-level continuing goals.

It helps Mira or the current owner Pal convert a broad project goal into a task map, next-round Runtime packages, progress reports, verification plans, and routing memory candidates.

Project Conductor does not execute project tasks. It does not create a background task system, database, CLI, scanner, validator, daemon, service, desktop app, web app, or automation runtime.

## When To Use

Use Project Conductor when the user asks AgentPal to move a project toward a continuing outcome, such as release readiness, research-to-artifact delivery, Pal team creation, migration, documentation overhaul, or cross-runtime continuation.

Do not use it for a simple one-shot question that one owner Pal can answer directly.

## Workflow

1. Project Goal Identification
   - Capture the project goal, target outcome, constraints, and completion target.
   - Decide whether this is project-level work or a single task.
2. Current Project State Summary
   - Read bounded project state, previous reports, Pal memory, and Routing Memory candidates when available.
   - Separate known state from assumptions.
3. Phase Roadmap
   - Split the goal into phases with deliverables and acceptance checks.
   - Keep phases as planning structure, not automatic execution.
4. Task Pool
   - Create project tasks with priority, complexity, risk, expected output, and status.
5. Task Priority
   - Prioritize by user value, blocker status, risk, dependency, verification need, and cost.
6. Owner Pal Candidates
   - Name owner Pal candidates by case-specific AI judgement from contacts / registry.
   - Do not use task-domain or keyword routes.
7. Runtime Candidates
   - Name host Runtime candidates only when current evidence or profile context supports the suggestion.
   - Runtime is execution layer, not Pal-layer owner.
8. Runtime Skill Candidates
   - Name Runtime-installed Skill / Plugin / MCP candidates separately from Pal-owned Skills.
   - Require current host Runtime evidence before claiming use.
9. Verification Requirements
   - Define evidence, verifier candidate, result record, not-run handling, and repair path.
10. Context Budget
   - Use index-only, full-text, summarize-first, memory reuse, and profile reads deliberately.
   - Record `context_read_count`, `profile_read_count`, and `memory_used`.
11. Next-Round Package
   - Convert the next actionable slice into `templates/orchestration/next-round-runtime-task-package.md`.
   - Keep forbidden context explicit.
12. Progress Report
   - Report completed, in-progress, blocked, not-run, risks, and decisions needed.
13. Routing Memory Update
   - Prepare Routing Memory writeback candidates after outcome or verification evidence exists.
   - Do not auto-write private memory into public files.

## Typical Artifacts

- `templates/orchestration/project-conductor-task-map.md`
- `templates/orchestration/deep-conductor-plan.md`
- `templates/orchestration/context-budget-plan.md`
- `templates/orchestration/runtime-skill-aware-task-package.md`
- `templates/orchestration/next-round-runtime-task-package.md`
- `templates/orchestration/conductor-decision-record.md`

## Cross-Runtime Continuity

Project Conductor can help the same Pal continue the same project across Codex, Claude Code, OpenCode, OpenHands, Gemini CLI, or another host Runtime.

Runtime can change, Pal memory must not break. Current Runtime capability still needs fresh evidence.

## Boundary

Project Conductor generates no-code project maps and task packages. The host Runtime executes the approved next-round task package and reports evidence.
