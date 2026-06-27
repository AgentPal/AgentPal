# Deep Conductor Plan

Use this template when Mira or the current owner Pal applies the Deep Conductor Master Loop.

```yaml
schema: agentpal.deep_conductor_plan.v0.1
user_goal: ""
task_kind: "" # ordinary | composite | project_level | verification | continuation
project_or_single_task: "" # project | single_task
memory_used:
  used: false
  sources: []
  freshness_or_risk_notes: []
capabilities_read:
  profile_read_count: 0
  profiles: []
topology_selected: ""
topology_reason: ""
alternatives_rejected:
  - topology: ""
    reason: ""
context_budget:
  context_read_count: 0
  index_only_sources: []
  full_text_sources: []
  summarize_first_sources: []
  cannot_read: []
task_packages:
  - package_id: ""
    owner_pal_candidate: ""
    runtime_candidate: ""
    runtime_skill_candidates: []
    template: ""
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
- `context_budget` must not reduce verification quality.
- `user_explanation` must say when no execution has happened.
