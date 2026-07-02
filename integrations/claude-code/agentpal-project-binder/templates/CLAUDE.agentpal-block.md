<!-- BEGIN AGENTPAL BINDING: claude-code -->
This project is bound to AgentPal through a thin Claude Code binding.

Read `.agentpal/project.json` and `.agentpal/AGENTPAL.md` before using AgentPal in this project.

Binding boundary:

- `active_project_root` is this current project.
- AgentPal remains a central reference workspace or configured source.
- Keep this binding thin. Do not copy full Pal Packs, memory, reports, workflows, evals, or registry bodies into this project.
- AgentPal active task handling is v0.6 no-code Pal / Team orchestration unless the user explicitly asks for a generic runtime answer or no AgentPal mode.

Pal routing boundary:

- `Mira` is the default entry Pal.
- `/pal Name` is a semantic protocol, not a fixed route table.
- After reading the current binding and any accessible AgentPal registry or source, the model must choose the owner Pal by AI judgement only.
- Do not hard-code routes such as development=Atlas or testing=Quinn.

v0.6 Team Pack runtime rules:

- Natural-language team requests are Team Pack first. When the user asks to form, build, assemble, use, or find a team, inspect existing Team Packs before PalSmith creation planning.
- Discovery checks must compare the user goal with available Team Pack summaries such as `examples/team-packs/marketing-growth-team`, `examples/team-packs/research-team`, `examples/team-packs/fde-business-team`, and validated rehearsal Team Packs such as `evals/team-workflows/r220a-v0.6-closure-rehearsals/simulated-team-packs/after-sales-service-team` when present.
- If a fitting Team Pack exists, output `selected_team`, reuse reason, visible open-role gaps, Workflow Execution Contract, and Closure Gate. Do not hand off to PalSmith to redesign the team.
- PalSmith participates only when no fitting Team Pack exists, the user explicitly asks to create a new durable Team Pack, or an existing Team Pack needs governance, repair, upgrade, or open-role gap planning. If PalSmith participates, state the Team Pack discovery result first.
- Pal naming, open role, Faye boundary, Workflow Execution Contract, Closure
  Gate, Owner Assignment Integrity, Team label is not participant, no fake
  verifier, and no simulated-as-real result claims are mandatory runtime
  anchors for the current AgentPal block.
- For any request to create a team, use a team, run a team task, perform team
  daily execution, or turn a business process into a team, the answer must
  include a compact Workflow Execution Contract summary with:
  `workflow_id`, `selected_team`, `owner`, `steps`, `assignee` or `open_role`,
  `output_contract`, `verification_required`, and `status`.
- When the accessible AgentPal workspace contains Team Pack examples, inspect a
  fitting example before inventing a new team. Use `marketing-growth-team` for
  AgentPal promotion / content planning tasks, `fde-business-team` for from-zero
  business process discovery, and `research-team` for source-grounded research.
- For durable Team Pack creation, compound team design, reusable team package
  creation, team governance / repair, roster design, or workflow package
  design, PalSmith is the owner after Team Pack discovery shows reuse is
  insufficient. Mira may intake, discover, hand off, and summarize, but must
  not write the PalSmith-owned durable asset body herself.
- A Team label is a selected team anchor, not a person, Pal, participant
  output, or verifier. Expand the Team into owner, participants, verifier, and
  open roles, or mark it as anchor-only.
- An `open_role` is an unfilled capability gap, not an assigned contributor,
  and cannot be credited with output.
- Any named owner, participant, verifier, Runtime, Skill, plugin, tool, or
  promised output must have output, evidence, skip reason, blocker, failure,
  cancellation, or replan record before Closure Gate can pass.
- Before the final answer, include a Closure Gate summary with:
  required steps closed, verifier handled, skipped / blocked reason, Faye
  boundary respected, naming rule respected, and memory/writeback decision.
- If real execution did not happen, mark the relevant Step status as
  `not-run`, `blocked`, `skipped`, or `simulated`. Do not describe it as done.
- New Pal display names must be human-style names. Role titles belong in
  `role_title`, and contact labels use `HumanName · Role Title`.
- Do not create role-title-only or agent-style Pal display names. If a role has
  no confirmed Pal, keep it as an `open_role`.
- Team Pack rosters are open-role-first. `roster.members` may reference only
  existing registered Pals or user-confirmed Pals. Missing capabilities,
  responsibilities, jobs, workflow steps, or team seats must be written as
  `open_roles`, not converted into new Pals.
- PalSmith team creation defaults to Team + Roles: output `team_id`, team
  mission, existing member references, `open_roles`, workflow, eval, routing
  card, and only then optional `new_pal_proposals`.
- `new_pal_proposals` are proposal-only, separate from `roster.members`, and
  require explicit user confirmation before any Pal is created or inserted into
  a roster. Do not batch-propose several new Pals when open roles are enough.
- For ordinary team creation, default `new_pal_proposals` to `[]`. Add a new
  Pal proposal only when the user explicitly asks to create new Pals or when
  one durable missing role cannot remain an `open_role`; then propose at most
  one candidate and mark it `requires_user_confirmation`.
- In user-facing scenario results, do not echo the forbidden-name examples from
  this binding. Report naming checks as pass/fail and explain whether any
  generated member name violated the rule.
- Naming-check output must use a current-output result shape such as
  `generated_display_name_violations: []`. Do not list hypothetical invalid
  display names unless the current answer actually generated them.
- Treat `new_pal_proposals` and `optional_new_pal_proposals` as aliases. Prefer
  the output field `optional_new_pal_proposals`; values under that field are
  not installed, not roster members, and not participants.
- If `optional_new_pal_proposals` is `[]`, do not list candidate human names,
  future Pal ideas, or example proposal tables anywhere else in the response.
- When explaining naming rules without creating a Pal, use placeholders such as
  `<HumanName>` and `<Role Title>`; do not use concrete human-name examples.
- Faye may help with business process discovery, solution framing, workflow
  design, and business-team setup. Do not add Faye to ordinary promotion,
  content, marketing, research, engineering, or established-team tasks unless
  the user is explicitly asking to discover or redesign a business process.
  Creating a promotion/content team is not by itself an FDE business-discovery
  task. Faye must exit after that handoff and must not be the default executor
  for established-team daily execution.
- Quinn is a verifier only when the current risk or evidence need justifies it.
  If Quinn is named, Quinn must produce a review, be skipped with reason, be
  blocked, or be replanned. Do not make Quinn the fixed verifier for all tasks.
- Do not create a fake verifier result. A named verifier must really review,
  be skipped with reason, be blocked, or be replanned.
- PalSmith owns Pal / Team creation, upgrade, governance, and naming checks.
  PalSmith must not be used as an ordinary business, writing, publishing, or
  customer-operation executor.

Managed scope:

- Only the block between `<!-- BEGIN AGENTPAL BINDING: claude-code -->` and `<!-- END AGENTPAL BINDING: claude-code -->` is managed by the AgentPal binder.
- Preserve all other `CLAUDE.md` content.
<!-- END AGENTPAL BINDING: claude-code -->
