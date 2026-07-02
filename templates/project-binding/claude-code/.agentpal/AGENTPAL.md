# AgentPal Claude Code Binding

This project uses a thin AgentPal binding for Claude Code.

- `active_project_root` is this external project.
- `agentpal_workspace_root` is the central AgentPal workspace.
- Pal contacts and official Pals stay in the AgentPal workspace.
- Claude-local permission settings may live in `.claude/settings.local.json`; that file should stay uncommitted.

Do not create project-local AgentPal memory, state, reports, context indexes, Pal copies, workflows, evals, capability inventory, business-system records, review records, evidence records, replay records, rollback records, verification records, audit trail indexes, governance decision records, or change ledger records by default.

## v0.6 Team Pack Runtime Requirements

- Natural-language team requests are Team Pack first. When the user asks to form, build, assemble, use, or find a team, inspect existing Team Packs before PalSmith creation planning.
- Discovery checks must compare the user goal with available Team Pack summaries such as `examples/team-packs/marketing-growth-team`, `examples/team-packs/research-team`, `examples/team-packs/fde-business-team`, and validated rehearsal Team Packs such as `evals/team-workflows/r220a-v0.6-closure-rehearsals/simulated-team-packs/after-sales-service-team` when present.
- If a fitting Team Pack exists, output `selected_team`, reuse reason, visible open-role gaps, Workflow Execution Contract, and Closure Gate. Do not hand off to PalSmith to redesign the team.
- PalSmith participates only when no fitting Team Pack exists, the user explicitly asks to create a new durable Team Pack, or an existing Team Pack needs governance, repair, upgrade, or open-role gap planning. If PalSmith participates, state the Team Pack discovery result first.Mandatory runtime anchors for the Claude Code binding:

- Pal naming
- open role
- Faye boundary
- Workflow Execution Contract
- Closure Gate
- no fake verifier
- no simulated-as-real result claims

For team creation, team execution, team daily operation, or business-process-to-team requests, Claude Code must include:

- Workflow Execution Contract summary with `workflow_id`, `selected_team`, `owner`, `steps`, `assignee` or `open_role`, `output_contract`, `verification_required`, and `status`.
- Closure Gate summary with required steps closed, verifier handled, skipped / blocked reason, Faye boundary respected, naming rule respected, and memory/writeback decision.

If real execution did not happen, mark work as `not-run`, `blocked`, `skipped`, or `simulated`.

Do not create role-title-only or agent-style Pal display names. Use a human-style `display_name`, separate `role_title`, and `HumanName · Role Title` contact label, or keep the need as an `open_role`.

Team Pack rosters are open-role-first. `roster.members` may reference only existing registered Pals or user-confirmed Pals. Jobs, capabilities, responsibilities, workflow steps, and missing seats must be written as `open_roles`, not new Pals. PalSmith team creation output should be ordered as `team_id`, team mission, existing member references, `open_roles`, workflow, eval, routing card, then optional `new_pal_proposals`. `new_pal_proposals` are proposal-only, separate from `roster.members`, and require explicit user confirmation before creation or roster insertion. Do not batch-propose several new Pals when open roles are enough. For ordinary team creation, default `new_pal_proposals` to `[]`. Add a new Pal proposal only when the user explicitly asks to create new Pals or when one durable missing role cannot remain an `open_role`; then propose at most one candidate and mark it `requires_user_confirmation`. Treat `new_pal_proposals` and `optional_new_pal_proposals` as aliases. Prefer the output field `optional_new_pal_proposals`; values under that field are not installed, not roster members, and not participants. If `optional_new_pal_proposals` is `[]`, do not list candidate human names, future Pal ideas, or example proposal tables anywhere else in the response. When explaining naming rules without creating a Pal, use placeholders such as `<HumanName>` and `<Role Title>`; do not use concrete human-name examples. In user-facing scenario results, do not echo forbidden-name examples. Report naming checks as pass/fail and whether any generated member name violated the rule. Naming-check output must use a current-output result shape such as `generated_display_name_violations: []`. Do not list hypothetical invalid display names unless the current answer actually generated them.

When examples are accessible, inspect a fitting Team Pack before inventing a new one: `marketing-growth-team` for AgentPal promotion / content planning, `fde-business-team` for from-zero business process discovery, and `research-team` for source-grounded research.

Faye is for business discovery / workflow design / business-team setup and must exit after handoff. Do not add Faye to ordinary promotion, content, marketing, research, engineering, or established-team tasks unless the user explicitly asks to discover or redesign a business process. Creating a promotion/content team is not by itself an FDE business-discovery task. Quinn is not a fixed verifier. PalSmith is for Pal / Team creation and governance, not ordinary execution.
