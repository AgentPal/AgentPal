# AgentPal Claude Code Thin Binding

This project uses a thin AgentPal binding for Claude Code.

## Active Roots

- `active_project_root`: this external project
- `agentpal_source`: central path, user-configured path, or GitHub source
- `runtime`: `claude-code`
- `default_pal`: `Mira`

## Thin-Binding Boundary

Create and maintain only:

- `.agentpal/project.json`
- `.agentpal/AGENTPAL.md`
- the protected AgentPal block in root `CLAUDE.md`

Do not create by default:

- `.agentpal/memory/`
- `.agentpal/state/`
- `.agentpal/reports/`
- `.agentpal/context/`
- `.agentpal/index/`
- `.agentpal/pals/`
- `.agentpal/workflows/`
- `.agentpal/evals/`

Do not copy into this project:

- full Pal assets
- central contacts or registry bodies
- workflow packs
- report archives
- release assets

## `/pal Name`

`/pal Name` is a semantic protocol.

It does not mean the binder hard-codes a route. After reading the current binding and any accessible AgentPal source, the model should decide owner selection by AI judgement only.

## v0.6 Team Pack Runtime Requirements

Mandatory runtime anchors for the Claude Code binding:

- Pal naming
- open role
- Faye boundary
- Workflow Execution Contract
- Closure Gate
- no fake verifier
- no simulated-as-real result claims

When the user asks Claude Code to create a team, use a team, run a team task,
perform established-team daily execution, or turn a business process into a
team, the response must include:

1. A compact Workflow Execution Contract summary:
   - `workflow_id`
   - `selected_team`
   - `owner`
   - `steps`
   - `assignee` or `open_role`
   - `output_contract`
   - `verification_required`
   - `status`
2. A Closure Gate summary before the final answer:
   - required steps closed?
   - verifier handled?
   - skipped / blocked reason?
   - Faye boundary respected?
   - naming rule respected?
   - memory/writeback decision?

If real execution did not happen, use `not-run`, `blocked`, `skipped`, or
`simulated`. Do not mark unavailable work as done.

When the central AgentPal workspace is accessible, inspect a fitting Team Pack
example before inventing a new team:

- `marketing-growth-team` for AgentPal promotion / content planning.
- `fde-business-team` for from-zero business process discovery.
- `research-team` for source-grounded research.

## Pal Naming And Open Roles

Do not create role-title-only or agent-style Pal display names.

If a new Pal is truly needed, `display_name` must be a human-style name,
`role_title` stores the job, and `contact_label` uses
`HumanName · Role Title`.

If the team only lacks a confirmed person for a responsibility, keep that
responsibility as an `open_role`. Do not create empty shell Pals.

Team Pack roster rules:

- `roster.members` may reference only existing registered Pals or
  user-confirmed Pals.
- Jobs, capabilities, responsibilities, workflow steps, and missing seats are
  roles, not Pals.
- Missing seats must be represented in `open_roles`.
- PalSmith's default Team Pack creation output is: `team_id`, team mission,
  existing member references, `open_roles`, workflow, eval, routing card, and
  optional `new_pal_proposals`.
- `new_pal_proposals` must stay separate from `roster.members`, must be marked
  proposal-only, and require explicit user confirmation before creation or
  roster insertion.
- Do not batch-propose multiple new Pals when the task can be handled by
  existing Pals plus `open_roles`.
- Default `new_pal_proposals` to `[]` for ordinary team creation. Add a new Pal
  proposal only when the user explicitly asks to create new Pals or when one
  durable missing role cannot remain an `open_role`; then propose at most one
  candidate and mark it `requires_user_confirmation`.
- Treat `new_pal_proposals` and `optional_new_pal_proposals` as aliases. Prefer
  the output field `optional_new_pal_proposals`; values under that field are
  not installed, not roster members, and not participants.
- If `optional_new_pal_proposals` is `[]`, do not list candidate human names,
  future Pal ideas, or example proposal tables anywhere else in the response.
- When explaining naming rules without creating a Pal, use placeholders such as
  `<HumanName>` and `<Role Title>`; do not use concrete human-name examples.
- In user-facing scenario results, do not echo the forbidden-name examples from
  this binding. Report naming checks as pass/fail and whether any generated
  member name violated the rule.
- Naming-check output must use a current-output result shape such as
  `generated_display_name_violations: []`. Do not list hypothetical invalid
  display names unless the current answer actually generated them.

## Faye / Quinn / PalSmith Boundaries

- Faye may help with business process discovery, solution framing, workflow
  design, and business-team setup. Do not add Faye to ordinary promotion,
  content, marketing, research, engineering, or established-team tasks unless
  the user is explicitly asking to discover or redesign a business process.
  Creating a promotion/content team is not by itself an FDE business-discovery
  task. Faye exits after handoff and must not be the default executor for
  established-team daily execution.
- Quinn is not a fixed verifier. Use Quinn only when risk or evidence needs
  justify verification; if named, Quinn must review, be skipped with reason, be
  blocked, or be replanned.
- Do not create a fake verifier result. A named verifier must really review,
  be skipped with reason, be blocked, or be replanned.
- PalSmith owns Pal / Team creation, governance, and naming checks. PalSmith is
  not an ordinary business, writing, publishing, or customer-operation executor.

## Repair And Removal

- `repair` may recreate this file when the project is already bound
- `disable` may remove the whole `.agentpal/` directory only when no other runtime binding remains
- neither action should delete the central AgentPal workspace
