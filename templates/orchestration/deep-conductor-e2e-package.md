# Deep Conductor E2E Package Template

```yaml
schema: agentpal.deep-conductor-e2e-package.v0.3
package_id: e2e-<short-id>
user_goal: <user goal in the user's language>
project_or_single_task: <project | single_task | mixed | unknown>

task_intake:
  user_goal: <original or summarized goal>
  deliverables: []
  constraints: []
  risk_flags: []
  requires_team_discovery: <true | false>
  requires_parallel_work: <true | false>
  requires_verification: <true | false>

team_first_discovery:
  available_team_packs_checked: []
  candidate_teams: []
  selected_team: <team_id | none>
  reuse_reason: <why selected team fits>
  rejected_teams: []
  reason_not_creating_new_team: <why PalSmith creation is not needed>
  open_roles_needed: []
  handoff_to_palsmith_for_team_creation:
    required: <true | false>
    reason: <reason or not_needed>

pal_role_selection:
  selected_participants:
    - pal_name: <display name>
      canonical_id: <pal id>
      role_title: <role>
      why_selected: <case-specific reason>
      capability_card_evidence: []
      team_roster_source: <path or none>
      task_scope: <bounded scope>
      not_responsible_for: []
      participation_required: <true | false>
  rejected_or_not_selected:
    why_not_faye: <reason>
    why_not_palsmith_for_execution: <reason>
    why_not_atlas_if_no_dev_task: <reason>
    why_not_quinn_for_execution: <reason>

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

execution_feasibility:
  status: <pass | partial | unavailable | blocked>
  reason: <why this package can or cannot be followed by the named host Runtime>
  host_runtime_assumptions: []
  unavailable_capabilities: []
  manual_replay_required: true
  fallback_required: <true | false>

runtime_availability_evidence:
  current_runtime: <host Runtime or unknown>
  checked_capabilities: []
  available: []
  unavailable: []
  unknown: []
  evidence_source: <tool output | user statement | package assumption | not_checked>

package_readiness:
  ready_for_host_runtime: <true | false>
  missing_fields: []
  needs_user_confirmation: []
  safe_to_execute_as_no_code_package: <true | false>

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
    host_runtime_requirements:
      can_read_files: <true | false | unknown>
      can_write_files: <true | false | unknown>
      can_run_commands: <true | false | unknown>
      supports_skills: <true | false | unknown>
      supports_subagents: <true | false | unknown>
      supports_external_dirs: <true | false | unknown>
    availability_first:
      required: true
      check_steps: []
      if_unavailable: <fallback or stop condition>
    execution_mode:
      host_runtime_manual_execution: true
      agentpal_auto_execution: false
    allowed_actions: []
    forbidden_actions: []
    evidence_required: []
    final_report_fields: []

workflow_execution_contract:
  template: templates/orchestration/workflow-execution-contract.md
  workflow_id: <id>
  selected_team: <team_id | none>
  owner: <Pal or team role>
  steps: []
  assignment_integrity:
    selected_owner_spoke: <true | false>
    named_participants_closed: <true | false>
    promised_outputs_closed: <true | false>
    verifier_outputs_closed_or_skipped: <true | false>
    open_roles_recorded: <true | false>
    fake_handoff_detected: <true | false>
    missing_records: []

pal_work_plans:
  - pal: <display name>
    assigned_step: <step id>
    what_i_will_do: <bounded work>
    tone_and_voice: <brief style note>
    thinking_basis: []
    knowledge_assets: []
    skill_assets: []
    workflow_assets: []
    memory_assets: []
    team_assets: []
    runtime_or_agent_usage: <none | candidate | used-with-evidence>
    model_choice: <current host | not_selected>
    reasoning_strength: <low | medium | high | host_default>
    expected_output: <output>
    handoff_target: <next step or none>

asset_preflight_records:
  pal_asset_preflight: []
  team_asset_preflight: []

execution_trace:
  - step_id: <step id>
    owner: <Pal or role>
    planned_assets: []
    actual_assets_used: []
    output_path_or_summary: <path or summary>
    status: <done | verified | blocked | skipped | failed | cancelled | replanned>
    deviation_from_plan: <none or description>
    if_deviation_why: <reason or none>

closure_gate_result:
  required_steps_total: <number>
  required_steps_completed: <number>
  skipped_steps: []
  skip_reasons: []
  blocked_steps: []
  block_reasons: []
  verifiers_required: <number>
  verifiers_completed: <number>
  child_steps_returned: <true | false>
  memory_or_asset_writeback: <none | candidate | written | blocked>
  final_delivery_ready: <true | false>

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
  unavailable_must_not_be_reported_as_pass: true
  partial_must_not_be_reported_as_fully_supported: true
  subagent_external_agent_requires_host_runtime_availability: true

not_a_fixed_route: true
```
