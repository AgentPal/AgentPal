# Team Asset Preflight Template

Status: v0.6 template. Use before team tasks that rely on a Team Pack.

## Team Context

- team_id:
- team_name:
- task_summary:
- team_pack_used: unknown
- team_request_type: create-new-team / use-existing-team / redesign-workflow / unknown
- current_project_constraints:
- user_instruction_priority_note:

## Team Files Checked

- `TEAM.md`: not-run
- `team.json`: not-run
- `roster.json`: not-run
- `workflows/index.md`: not-run
- selected_workflow:
- `knowledge/index.md`: not-run
- `skills/index.md`: not-run
- `runbooks/index.md`: not-run
- `memory/README.md` or `memory/index.md`: not-run
- `evals/definition-of-done.md`: not-run
- routing_or_capability_card: not-run

## Team Assets

- team_assets_required:
- team_assets_loaded:
- team_assets_missing:
- team_memory_scope:
- team_eval_required:

## Workflow Execution Contract

- workflow_id:
- selected_workflow:
- workflow_status: draft
- canonical_template: `templates/orchestration/workflow-execution-contract.md`
- closure_gate_protocol: `orchestration/workflow-closure-gate-protocol.md`
- steps:
  - step_id:
    parent_step_id:
    owner_role:
    owner_pal:
    context_access_list:
    required_team_assets:
    pal_asset_preflight_required: true
    expected_output:
    verifier:
    status:
- closure_rule: every step must follow `orchestration/workflow-step-state-machine.md` and close before a complete final report.

## Member Pal Preflights

- member_pal_preflights_required:
- member_pal_preflight_status:
- boundary_conflicts:
- routing_veto_checks:
  - candidate_pal:
    proposed_role:
    veto_triggered:
    veto_reason:
    next_action:
- faye_boundary_check: not-applicable / discovery-stage / routine-execution-vetoed / redesign-consult
- replan_required:

## Decision

- go_no_go_label:
- verification_required:
- blocked_reason:
- next_action:

## Notes

- This is a no-code protocol template, not a workflow state machine implementation.
- Team assignment cannot override a Pal responsibility boundary.
