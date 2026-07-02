<!-- BEGIN AGENTPAL BINDING: codex -->

This directory is bound to AgentPal through a thin project binding.

Read `.agentpal/project.json` and `.agentpal/AGENTPAL.md` for the current binding. The AgentPal workspace remains the central Pal, project-record, and governance source.

Project boundary:

- `active_project_root` is this external user project.
- `agentpal_workspace_root` is only the AgentPal reference workspace.
- `agentpal_project_record` points to `workspace/projects/<project-id>` inside the AgentPal workspace.
- "current project" means `active_project_root` unless the user explicitly says AgentPal itself.
- Project docs, design, requirements, assets, data, and source files are read from `active_project_root` when needed.
- Source maps, derived knowledge, project memory, task packages, reports, governance records, and capability inventory are stored in `agentpal_project_record`, not in project-local `.agentpal/`.

Routing boundary:

- Ordinary messages go to Mira.
- Direct `/pal Name` and `@Name` calls are resolved from central contacts.
- Resolve Pal contacts from `central_pal_contacts` in the AgentPal workspace.
- Owner selection is AI judgement only.
- Keyword routing, `keyword_map`, `domain_map`, and `role_map` are forbidden.

Execution boundary:

- AgentPal is a no-code organization layer, not an execution layer.
- File edits, commands, publishing, or external calls require current host-runtime evidence.

v0.6 Team Pack boundary:

- Natural-language team requests are Team Pack first. When the user asks to form, build, assemble, use, or find a team, inspect existing Team Packs before PalSmith creation planning.
- Discovery checks must compare the user goal with available Team Pack summaries such as `examples/team-packs/marketing-growth-team`, `examples/team-packs/research-team`, `examples/team-packs/fde-business-team`, and validated rehearsal Team Packs such as `evals/team-workflows/r220a-v0.6-closure-rehearsals/simulated-team-packs/after-sales-service-team` when present.
- If a fitting Team Pack exists, output `selected_team`, reuse reason, visible open-role gaps, Workflow Execution Contract, and Closure Gate. Do not hand off to PalSmith to redesign the team.
- PalSmith participates only when no fitting Team Pack exists, the user explicitly asks to create a new durable Team Pack, or an existing Team Pack needs governance, repair, upgrade, or open-role gap planning. If PalSmith participates, state the Team Pack discovery result first.
- For durable Team Pack creation, compound team design, reusable team package creation, team governance / repair, roster design, or workflow package design, PalSmith is the owner after Team Pack discovery shows reuse is insufficient. Mira may intake, discover, hand off, and summarize, but must not write the PalSmith-owned durable asset body herself.
- For team, Team Pack, PalSmith team-creation, or established-team execution, load the minimal relevant AgentPal assets from `agentpal_workspace_root` before answering: central contacts, capability cards, Pal naming protocol, selected Team Pack files, Team Asset Preflight, Workflow Execution Contract, and Closure Gate.
- Team Pack selection is case-specific AI judgement. Mira chooses Team Pack / owner Pal by current task fit, not keyword routing. PalSmith handles durable Pal / Team Pack creation or repair, not routine execution.
- Faye may contribute business process discovery or team setup, then exits before routine established-team execution.
- New Pal proposals require human `display_name`, separate `role_title`, and `contact_label`. Do not create role-title-only Pals such as `Promotion Pal`, `Copywriting Pal`, or `ServiceAgent`.
- `roster.members` may reference only existing registered Pals or user-confirmed Pals.
- Missing durable roles stay as `open_roles` unless a real registered Pal, human owner, or runtime capability is selected with evidence.
- `optional_new_pal_proposals` are proposal-only, not roster members, and require explicit user confirmation before creation or roster insertion.
- A Team label is a selected team anchor, not a person, Pal, participant output, or verifier. Expand the Team into owner, participants, verifier, and open roles, or mark it as anchor-only.
- An `open_role` is an unfilled capability gap, not an assigned contributor, and cannot be credited with output.
- Concrete team tasks need a Workflow Execution Contract and Closure Gate; no planned Step, owner, participant, open role, verifier, Runtime, Skill, plugin, tool, or promised output may disappear from the final report.
- No fake verifier: Quinn is never a fixed verifier. If any verifier is named, record verifier output or a legal skip / block / replan reason.
- Do not present simulated, fixture-based, or single-model reasoning as real multi-Pal execution. Label fixture data and not-run runtime actions honestly.

<!-- END AGENTPAL BINDING: codex -->
