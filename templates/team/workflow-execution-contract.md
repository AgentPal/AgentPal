# Team Workflow Execution Contract Wrapper

Status: v0.6 wrapper template. This is not a scheduler, runtime executor, or
separate Team-specific state machine.

Use the canonical Workflow Execution Contract template for the actual task
record:

- `templates/orchestration/workflow-execution-contract.md`

Use these protocols for status and closure:

- `orchestration/workflow-execution-contract-protocol.md`
- `orchestration/workflow-step-state-machine.md`
- `orchestration/workflow-closure-gate-protocol.md`

## Team Required Bindings

When a Team Pack governs the work, the canonical contract must include:

- `workflow_id`
- `mode`
- `team_id`
- `owner_pal`
- `user_goal`
- `risk_level`
- `source_docs`
- `context_access_lists`
- `steps`
- `dependencies`
- `verification_required`
- `closure_gate`
- `memory_writeback`

Each Team Step should also include:

- `step_id`
- `parent_step_id` when it is a child Step
- `title`
- `required`
- `assignee_type`
- `assignee_id`
- `role`
- `status`
- `depends_on`
- `context_access_list`
- `output_contract`
- `verification_required`
- `verifier_role`
- `verifier_pal`
- `skip_reason`
- `block_reason`
- `failure_reason`
- `cancel_reason`
- `replan_reason`
- `replacement_step_id`
- `child_steps`
- `output_summary`
- `evidence`

## Team Asset Links

The contract should reference:

- Team Asset Preflight result: `templates/team/team-asset-preflight.md`
- Selected Team workflow file
- Team eval / Definition of Done
- Member Pal Asset Preflight result for each assigned member Step
- Context Access List for every non-trivial Step

## Closure Rule

Final reports must run the Closure Gate. They must not leave Steps in
`planned`, `assigned`, `accepted`, `running`, or `review_required`.
