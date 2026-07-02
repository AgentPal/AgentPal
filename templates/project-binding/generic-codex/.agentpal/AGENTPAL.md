# AgentPal Project Binding

This external project is connected to AgentPal by thin binding.

This folder does not contain the AgentPal rule body, Pal Packs, full protocols, release docs, examples, or evals.

## How To Load AgentPal

1. Read `.agentpal/project.json`.
2. Resolve `agentpal_workspace_root`.
3. Read the current core gates from the AgentPal workspace root:
   - `core/agentpal-core-gate.md`
   - `core/first-pal-gate.md`
   - `core/simple-pal-mode-runtime-contract.md`
   - `core/deliverable-aware-task-judgement-gate.md`
   - `core/main-pal-conductor-gate.md`
   - `core/runtime-adapter-shared-contract.md`
   - `core/project-binding-thin-contract.md`
   - `core/runtime-response-gate.md`
4. Read Pal source of truth from the AgentPal workspace:
   - `workspace/organization/contacts/pals.json`
   - `workspace/organization/contacts/PAL_CONTACTS.md`
5. Read Mira entry assets from the AgentPal workspace:
   - `official/pals/Mira-main/PAL.md`
   - `official/pals/Mira-main/core/output-contract.md`

## Boundary

The active project is this external project directory.

The AgentPal workspace is only a Pal source and routing reference. Do not treat it as part of this project.

If the AgentPal framework updates its core gates, this project should inherit the update by reading `agentpal_workspace_root`; do not paste a full rule copy into this folder.

Project memory, source maps, derived knowledge, task records, reports, governance records, and capability inventory belong in the central `agentpal_project_record` under the AgentPal workspace, not in this project-local `.agentpal/` folder.

## Thin Binding Cleanliness

Do not create `.agentpal/memory`, `.agentpal/state`, `.agentpal/reports`, `.agentpal/context`, `.agentpal/index`, `.agentpal/pals`, `.agentpal/workflows`, `.agentpal/evals`, `.agentpal/capability-inventory`, `.agentpal/business-systems`, `.agentpal/reviews`, `.agentpal/evidence`, `.agentpal/replay`, `.agentpal/rollback`, `.agentpal/verification`, `.agentpal/audit-trail`, `.agentpal/governance-decisions`, `.agentpal/change-ledger`, or `.agentpal/change-review` by default.

Owner selection is AI judgement only. Do not use keyword routing, `keyword_map`, `domain_map`, or `role_map`.

## v0.6 Team Pack Runtime Guardrails

- Natural-language team requests are Team Pack first. When the user asks to form, build, assemble, use, or find a team, inspect existing Team Packs before PalSmith creation planning.
- Discovery checks must compare the user goal with available Team Pack summaries such as `examples/team-packs/marketing-growth-team`, `examples/team-packs/research-team`, `examples/team-packs/fde-business-team`, and validated rehearsal Team Packs such as `evals/team-workflows/r220a-v0.6-closure-rehearsals/simulated-team-packs/after-sales-service-team` when present.
- If a fitting Team Pack exists, output `selected_team`, reuse reason, visible open-role gaps, Workflow Execution Contract, and Closure Gate. Do not hand off to PalSmith to redesign the team.
- PalSmith participates only when no fitting Team Pack exists, the user explicitly asks to create a new durable Team Pack, or an existing Team Pack needs governance, repair, upgrade, or open-role gap planning. If PalSmith participates, state the Team Pack discovery result first.For team, Team Pack, PalSmith team-creation, established-team execution, or
`/pal Name` work, read only the minimal relevant AgentPal source assets before
answering:

- central contacts and capability cards;
- `standards/pal-asset/pal-naming-and-import-conflict-protocol.md`;
- Team Pack assets when a team is named or selected;
- `core/team-asset-preflight-protocol.md` before team execution;
- `orchestration/workflow-execution-contract-protocol.md` for concrete team tasks;
- `orchestration/workflow-closure-gate-protocol.md` before claiming completion.

Required behavior:

- Mira is the default entry and must choose Team Pack / Pal owner by AI judgement.
- PalSmith owns durable Pal / Team Pack creation or repair; it is not a routine executor.
- Faye may help with business process discovery and team setup, then exits before routine established-team execution.
- New Pal proposals must use a human `display_name`; role phrases belong in `role_title` and roster display belongs in `contact_label`.
- `roster.members` may reference only existing registered Pals or user-confirmed Pals.
- Missing durable roles must remain `open_roles` unless a real registered Pal, human owner, or runtime capability is selected with evidence.
- `optional_new_pal_proposals` are proposal-only, not roster members, and require explicit user confirmation before creation or roster insertion.
- Concrete team tasks need a Workflow Execution Contract and Closure Gate. Every planned Pal, Step, open role, or verifier must be done, verified, skipped with reason, blocked, failed, cancelled, or replanned before final reporting.
- No fake verifier: do not make Quinn or any Pal a fixed verifier. If a verifier is named, record its output or a legal skip / block / replan reason.
- Do not present simulated, fixture-based, or single-model reasoning as real multi-Pal execution. Label fixture data and not-run runtime actions honestly.
