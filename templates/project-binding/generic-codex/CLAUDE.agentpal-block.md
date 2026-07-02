<!-- BEGIN AGENTPAL BINDING: claude-code -->

This project uses a thin AgentPal binding. Read `.agentpal/project.json` and `.agentpal/AGENTPAL.md`.

The active project is this external project. The AgentPal workspace is only the central Pal, project-record, and governance reference.

`agentpal_project_record` points to `workspace/projects/<project-id>` inside the AgentPal workspace. Read current user project materials from `active_project_root` when needed, and store AgentPal source maps, derived knowledge, memory, task records, reports, governance records, and capability inventory in the central project record.

Do not copy central Pal Packs, contacts, memory, reports, state, workflows, source maps, derived knowledge, task packages, governance records, or evals into this project by default.

Owner selection is AI judgement only after reading current central contacts. Do not use keyword routing, `keyword_map`, `domain_map`, or `role_map`.

- Natural-language team requests are Team Pack first. When the user asks to form, build, assemble, use, or find a team, inspect existing Team Packs before PalSmith creation planning.
- Discovery checks must compare the user goal with available Team Pack summaries such as `examples/team-packs/marketing-growth-team`, `examples/team-packs/research-team`, `examples/team-packs/fde-business-team`, and validated rehearsal Team Packs such as `evals/team-workflows/r220a-v0.6-closure-rehearsals/simulated-team-packs/after-sales-service-team` when present.
- If a fitting Team Pack exists, output `selected_team`, reuse reason, visible open-role gaps, Workflow Execution Contract, and Closure Gate. Do not hand off to PalSmith to redesign the team.
- PalSmith participates only when no fitting Team Pack exists, the user explicitly asks to create a new durable Team Pack, or an existing Team Pack needs governance, repair, upgrade, or open-role gap planning. If PalSmith participates, state the Team Pack discovery result first.

<!-- END AGENTPAL BINDING: claude-code -->
