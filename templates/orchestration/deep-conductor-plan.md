# Deep Conductor Plan

Use this template when Mira or the current owner Pal applies the Deep Conductor Master Loop.

```yaml
schema: agentpal.deep_conductor_plan.v0.1
user_goal: ""
task_kind: "" # ordinary | composite | project_level | verification | continuation
project_or_single_task: "" # project | single_task
e2e_package:
  applies: false
  package_id: ""
  template: "templates/orchestration/deep-conductor-e2e-package.md"
  synthesis_template: "templates/orchestration/deep-conductor-e2e-synthesis-report.md"
  complete_output_shape_required: false
  no_auto_execution: true
memory_used:
  used: false
  sources: []
  pal_project_memory_snapshot: ""
  routing_memory_summary: []
  runtime_skill_usage_memory_summary: []
  verification_memory_summary: []
  freshness_or_risk_notes: []
cross_runtime_continuation:
  applies: false
  previous_runtime: ""
  current_runtime_candidate: ""
  current_runtime_evidence_required: true
capabilities_read:
  profile_read_count: 0
  profiles: []
topology_selected: ""
topology_reason: ""
alternatives_rejected:
  - topology: ""
    reason: ""
context_budget:
  context_budget_plan: ""
  read_tier:
    initial: 1
    max: 4
    current: 1
  cost_sensitivity: ""
  quality_target: ""
  prompt_shaping_notes: []
  model_or_reasoning_candidate:
    model: ""
    reasoning: ""
    reason: ""
  index_only_sources: []
  summary_sources: []
  full_text_sources: []
  cannot_read: []
  verification_cost_reason: ""
  context_usage_report_required: true
task_packages:
  - package_id: ""
    owner_pal_candidate: ""
    runtime_candidate: ""
    runtime_skill_candidates: []
    template: ""
memory_writeback_candidates:
  pal_project_memory_snapshot: false
  routing_memory_record: false
  runtime_skill_usage_memory_record: false
  verification_memory: false
  decision_memory: false
verification_plan:
  verifier_candidates: []
  evidence_required: []
  result_record: ""
routing_memory_writeback:
  write_candidate: false
  decision_record_candidate: ""
  result_record_candidate: ""
  not_a_fixed_route: true
user_explanation: ""
```

## Rules

- `topology_selected` is a current judgement, not a permanent route.
- `runtime_skill_candidates` require current host Runtime evidence.
- `memory_used` must not expose private content.
- `cross_runtime_continuation` does not make the current Runtime a fixed route.
- Memory summaries are judgement inputs, not proof of current Runtime capability.
- `context_budget` must reference a Context Budget Plan when token / cost awareness matters.
- `read_tier` is qualitative and is not an exact token count.
- `context_budget` must not reduce verification quality.
- `verification_cost_reason` explains necessary evidence cost; it must not be used to skip verification.
- `context_usage_report_required` should stay true for complex or cross-runtime work.
- `user_explanation` must say when no execution has happened.
- `e2e_package` applies when the user goal needs the full loop from memory through next-round recommendation.
- E2E package use does not create automatic execution or background orchestration.
