# Workflow Execution Contract Template

Use this template when a Workflow Plan becomes an auditable execution record.

Candidates are not fixed routes. Only participants written into `steps` become closure obligations.

```yaml
schema: agentpal.workflow-execution-contract.v0.6
workflow_id: ""
created_at: ""
updated_at: ""
mode: fast_route | single_owner | owner_verifier | plan_execute_verify | deep_conductor | custom
team_id: null
team_source: null
owner_pal:
  pal_id: ""
  selection_reason: ""
  not_a_fixed_route: true
user_goal: ""
risk_level: low | medium | high
source_docs:
  - path: ""
    reason: ""
context_access_lists:
  - cal_id: ""
    template: "templates/orchestration/context-access-list.md"
    allowed_summary: ""
steps:
  - step_id: "S1"
    parent_step_id: null
    title: ""
    required: true
    assignee_type: pal | team | runtime | skill | plugin | mcp | coordinator | human | role
    assignee_id: ""
    assignee_selection_reason: ""
    role: owner | contributor | verifier | executor | reviewer | coordinator | summarizer
    status: planned | assigned | accepted | running | done | review_required | verified | failed | blocked | skipped | cancelled | replanned
    depends_on: []
    context_access_list: ""
    output_contract:
      expected_output: ""
      evidence_required: []
      failure_conditions: []
    verification_required: false
    verifier_role: null
    verifier_pal: null
    verifier_selection_reason: null
    verification_result_ref: null
    skip_reason: null
    block_reason: null
    failure_reason: null
    cancel_reason: null
    replan_reason: null
    replacement_step_id: null
    replacement_workflow_id: null
    child_steps: []
    returned_to_parent: false
    output_summary: ""
    evidence:
      - ref: ""
        note: ""
dependencies:
  - from_step_id: ""
    to_step_id: ""
    dependency_type: context | output | verification | decision | runtime
verification_required: false
verification_policy:
  required_reason: null
  skip_reason: null
  verifier_candidates: []
  no_hardcoded_verifier: true
closure_gate:
  protocol: "orchestration/workflow-closure-gate-protocol.md"
  outcome: not_run | pass | partial | blocked | fail
  open_steps: []
  skipped_steps_without_reason: []
  verifier_outputs_missing: []
  child_steps_not_returned: []
  blocked_steps_reported_to_user: false
  final_report_ref: null
memory_writeback:
  pal_memory: none | candidate | written | blocked
  team_memory: none | candidate | written | blocked
  routing_memory: none | candidate | written | blocked
  runtime_skill_usage_memory: none | candidate | written | blocked
  verification_memory: none | candidate | written | blocked
  privacy_review_required: true
  writeback_notes: ""
```

## Step Use Notes

- `planned`, `assigned`, `accepted`, `running`, and `review_required` must not remain before a complete final report.
- `verified` requires verifier output, not just a verifier name.
- `skipped`, `blocked`, `failed`, `cancelled`, and `replanned` require reasons.
- `replanned` must point to a replacement Step or Workflow when one exists.
- A parent Step cannot close as `done` while required child Steps are still open.
- Runtime, Skill, plugin, and MCP Steps must record host evidence or an honest unavailable status.
