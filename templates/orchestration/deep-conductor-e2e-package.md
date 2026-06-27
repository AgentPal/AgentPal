# Deep Conductor E2E Package Template

```yaml
schema: agentpal.deep-conductor-e2e-package.v0.3
package_id: e2e-<short-id>
user_goal: <user goal in the user's language>
project_or_single_task: <project | single_task | mixed | unknown>

memory_used:
  status: <used | missing | not_approved | stale | not_needed>
  sources: []
  privacy_boundary: <what memory must not be shared>
  continuation_notes: <what should continue or not repeat>

capability_inventory_used:
  status: <used | missing | not_needed | blocked>
  profiles_read: []
  profiles_not_read: []
  judgement_note: <profiles inform judgement but do not force selection>

context_budget_plan:
  read_tier: <index_only | summary_first | targeted_full_read | expanded_with_reason>
  allowed_context: []
  forbidden_context: []
  escalation_reasons: []
  stop_conditions: []
  context_usage_report_required: true

workflow_topology:
  selected: <single_owner | owner_verifier | plan_execute_verify | parallel_independent_review | project_conductor | mixed>
  reason: <case-specific fit>
  alternatives_rejected: []
  not_a_fixed_route: true

context_packets:
  - packet_id: cp-<id>
    from_pal: <Pal or owner gap>
    to_pal_candidate: <Pal or owner gap>
    mode: <consult | delegate | handoff | review | owner_transfer>
    can_read: []
    cannot_read: []
    needed_output: <bounded output>
    verification_requirements: []

runtime_skill_aware_packages:
  - package_id: rt-skill-<id>
    host_runtime_candidate: <runtime | unknown>
    runtime_skill_candidates: []
    plugin_candidates: []
    mcp_tool_candidates: []
    availability_check_required: true
    if_unavailable_fallback: <fallback>
    verification_required: true

owner_verifier_plan:
  owner_candidate: <Pal or owner gap>
  verifier_candidate: <Pal or verifier gap>
  owner_evidence_required: []
  verifier_independent_context: []
  possible_results: [pass, fail, blocked]

parallel_review_plan:
  needed: <true | false>
  reviewer_packets: []
  isolation_rule: <reviewers do not read peer drafts before final reports>
  synthesis_owner_candidate: <Pal or owner gap>

plan_execute_verify_plan:
  plan_owner_candidate: <Pal or owner gap>
  runtime_execution_candidate: <host Runtime or unknown>
  execution_evidence_required: []
  verification_owner_candidate: <Pal or owner gap>

runtime_task_packages:
  - package_id: runtime-task-<id>
    goal: <bounded runtime goal>
    allowed_actions: []
    forbidden_actions: []
    evidence_required: []
    final_report_fields: []

verification_plan:
  acceptance_criteria: []
  evidence_required: []
  not_run_reporting: <required>
  blocked_reporting: <required>
  verification_must_not_be_skipped_for_cost: true

context_usage_report_required: true

routing_memory_writeback:
  candidate_needed: <true | false>
  public_safe_fields: []
  private_fields_excluded: []
  next_time_recommendation: <guidance, not a rule>

user_facing_explanation:
  summary: <short explanation>
  scheduling_reason: <why this topology/candidate set fits>
  next_round_recommendation: <next useful action>

no_code_boundary:
  agentpal_executes: false
  host_runtime_executes_only_with_evidence: true
  forbidden: [runtime program, background workflow, automatic routing, automatic skill scan, exact token meter without host evidence]

not_a_fixed_route: true
```
