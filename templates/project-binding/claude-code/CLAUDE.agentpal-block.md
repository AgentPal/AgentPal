<!-- BEGIN AGENTPAL BINDING: claude-code -->

This directory is bound to AgentPal through a thin Claude Code binding.

Read `.agentpal/project.json` and `.agentpal/AGENTPAL.md` for the binding. If Claude needs access to the central AgentPal workspace, use local `.claude/settings.local.json` and keep that file out of git.

The external project remains the active project. AgentPal remains the central Pal, project-record, and governance workspace.

`agentpal_project_record` points to `workspace/projects/<project-id>` inside the AgentPal workspace. Project docs, design, requirements, assets, data, and source files are read from `active_project_root` when needed; source maps, derived knowledge, project memory, task packages, reports, governance records, and capability inventory stay in the central project record.

Owner selection is AI judgement only after reading current central contacts from the AgentPal workspace. Keyword routing, `keyword_map`, `domain_map`, and `role_map` are forbidden.

v0.6 Team Pack runtime rules for Claude Code:

- Natural-language team requests are Team Pack first. When the user asks to form, build, assemble, use, or find a team, inspect existing Team Packs before PalSmith creation planning.
- Discovery checks must compare the user goal with available Team Pack summaries such as `examples/team-packs/marketing-growth-team`, `examples/team-packs/research-team`, `examples/team-packs/fde-business-team`, and validated rehearsal Team Packs such as `evals/team-workflows/r220a-v0.6-closure-rehearsals/simulated-team-packs/after-sales-service-team` when present.
- If a fitting Team Pack exists, output `selected_team`, reuse reason, visible open-role gaps, Workflow Execution Contract, and Closure Gate. Do not hand off to PalSmith to redesign the team.
- PalSmith participates only when no fitting Team Pack exists, the user explicitly asks to create a new durable Team Pack, or an existing Team Pack needs governance, repair, upgrade, or open-role gap planning. If PalSmith participates, state the Team Pack discovery result first.
- Pal naming, open role, Faye boundary, Workflow Execution Contract, Closure
  Gate, Owner Assignment Integrity, Team label is not participant, no fake
  verifier, and no simulated-as-real result claims are mandatory runtime
  anchors for the current AgentPal block.
- Team creation, team execution, team daily operation, and business-process-to-team requests must include a compact Workflow Execution Contract summary:
  `workflow_id`, `selected_team`, `owner`, `steps`, `assignee` or `open_role`, `output_contract`, `verification_required`, and `status`.
- When accessible examples exist, inspect a fitting Team Pack before inventing a new team: `marketing-growth-team` for AgentPal promotion / content planning, `fde-business-team` for from-zero business process discovery, and `research-team` for source-grounded research.
- For durable Team Pack creation, compound team design, reusable team package creation, team governance / repair, roster design, or workflow package design, PalSmith is the owner after Team Pack discovery shows reuse is insufficient. Mira may intake, discover, hand off, and summarize, but must not write the PalSmith-owned durable asset body herself.
- A Team label is a selected team anchor, not a person, Pal, participant output, or verifier. Expand the Team into owner, participants, verifier, and open roles, or mark it as anchor-only.
- An `open_role` is an unfilled capability gap, not an assigned contributor, and cannot be credited with output.
- Any named owner, participant, verifier, Runtime, Skill, plugin, tool, or promised output must have output, evidence, skip reason, blocker, failure, cancellation, or replan record before Closure Gate can pass.
- Final answers for those tasks must include a Closure Gate summary:
  required steps closed, verifier handled, skipped / blocked reason, Faye boundary respected, naming rule respected, and memory/writeback decision.
- If real execution did not happen, mark Step status as `not-run`, `blocked`, `skipped`, or `simulated`; do not mark it complete.
- New Pal `display_name` values must be human-style names. Store jobs in `role_title`; use `HumanName · Role Title` as `contact_label`.
- Do not create role-title-only or agent-style Pal display names. Use `open_role` when a role has no confirmed Pal.
- Team Pack rosters are open-role-first: `roster.members` may reference only existing registered Pals or user-confirmed Pals. Jobs, capabilities, responsibilities, workflow steps, and missing seats must become `open_roles`, not new Pals.
- PalSmith team creation output should be ordered as `team_id`, team mission, existing member references, `open_roles`, workflow, eval, routing card, then optional `new_pal_proposals`.
- `new_pal_proposals` are proposal-only, separate from `roster.members`, and require explicit user confirmation before creation or roster insertion. Do not batch-propose several new Pals when open roles are enough.
- For ordinary team creation, default `new_pal_proposals` to `[]`. Add a new Pal proposal only when the user explicitly asks to create new Pals or when one durable missing role cannot remain an `open_role`; then propose at most one candidate and mark it `requires_user_confirmation`.
- Treat `new_pal_proposals` and `optional_new_pal_proposals` as aliases. Prefer the output field `optional_new_pal_proposals`; values under that field are not installed, not roster members, and not participants.
- If `optional_new_pal_proposals` is `[]`, do not list candidate human names, future Pal ideas, or example proposal tables anywhere else in the response.
- When explaining naming rules without creating a Pal, use placeholders such as `<HumanName>` and `<Role Title>`; do not use concrete human-name examples.
- In user-facing scenario results, do not echo the forbidden-name examples from this binding. Report naming checks as pass/fail and whether any generated member name violated the rule.
- Naming-check output must use a current-output result shape such as `generated_display_name_violations: []`. Do not list hypothetical invalid display names unless the current answer actually generated them.
- Faye may participate in business discovery, workflow framing, solution design, and business-team setup only. Do not add Faye to ordinary promotion, content, marketing, research, engineering, or established-team tasks unless the user explicitly asks to discover or redesign a business process. Creating a promotion/content team is not by itself an FDE business-discovery task. Faye exits after handoff and must not be default executor for established-team daily execution.
- Quinn is not a fixed verifier. If named, Quinn must output review, be skipped with reason, be blocked, or be replanned.
- Do not create a fake verifier result. A named verifier must really review, be skipped with reason, be blocked, or be replanned.
- PalSmith owns Pal / Team creation, governance, and naming checks; PalSmith is not an ordinary business executor.

<!-- END AGENTPAL BINDING: claude-code -->
