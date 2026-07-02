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
- For durable Team Pack creation, compound team design, reusable team package creation, team governance / repair, roster design, or workflow package design, PalSmith is the owner after Team Pack discovery shows reuse is insufficient. Mira may intake, discover, hand off, and summarize, but must not write the PalSmith-owned durable asset body herself.
- A Team label is a selected team anchor, not a person, Pal, participant output, or verifier. Expand the Team into owner, participants, verifier, and open roles, or mark it as anchor-only.
- An `open_role` is an unfilled capability gap, not an assigned contributor, and cannot be credited with output.
- Any named owner, participant, verifier, Runtime, Skill, plugin, tool, or promised output must have output, evidence, skip reason, blocker, failure, cancellation, or replan record before Closure Gate can pass.

<!-- END AGENTPAL BINDING: claude-code -->
