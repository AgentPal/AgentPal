# Conductor Decision Record

Use this record to explain why a Deep Conductor or Project Conductor plan chose its topology, Pal candidates, Runtime candidates, Skill candidates, context budget, and verification plan.

```yaml
schema: agentpal.conductor_decision_record.v0.1
record_id: ""
created_at: ""
user_goal_summary: ""
project_or_single_task: ""
e2e_package:
  applies: false
  package_id: ""
  complete_output_shape_required: false
  no_auto_execution: true
topology_selected: ""
topology_reason:
  - ""
pal_candidates:
  - pal: ""
    role: ""
    reason: ""
runtime_candidates:
  - runtime: ""
    reason: ""
    current_evidence: ""
runtime_skill_candidates:
  - skill_or_tool: ""
    type: ""
    reason: ""
    current_evidence: ""
pal_owned_skills_used:
  - pal: ""
    skill_or_method: ""
    purpose: ""
alternatives_rejected:
  - alternative: ""
    reason: ""
token_cost_considerations:
  context_budget_plan: ""
  read_tier:
    initial: 1
    max: 4
    used: []
  prompt_shaping_notes: []
  model_or_reasoning_candidate:
    model: ""
    reasoning: ""
    reason: ""
  cost_sensitivity: ""
  quality_target: ""
  context_read_count: 0
  profile_read_count: 0
  memory_used: false
  budget_reason: ""
  verification_cost_reason: ""
  context_usage_report_required: true
memory_basis:
  - source: ""
    lesson: ""
    not_a_fixed_route: true
cross_runtime_memory:
  previous_runtime: ""
  current_runtime_candidate: ""
  pal_project_memory_snapshot_used: ""
  routing_memory_used: []
  runtime_skill_usage_memory_used: []
  verification_memory_used: []
  current_runtime_evidence_required: true
memory_writeback_candidates:
  pal_project_memory_snapshot: false
  routing_memory_record: false
  runtime_skill_usage_memory_record: false
  verification_memory: false
  decision_memory: false
risks:
  - ""
verification_plan:
  evidence_required: []
  verifier_candidates: []
next_time_suggestion:
  summary: ""
  not_a_fixed_route: true
privacy_review:
  public_safe: true
  sensitive_context_excluded: true
```

## Rules

- The record is a judgement trace, not a route table.
- Current Runtime evidence must be separated from memory.
- Cross-runtime memory preserves continuity but does not prove the current Runtime has the same tools, Skills, or permissions.
- Runtime Skill Usage Memory records host Runtime experience. It must not be recorded as a Pal-owned Skill.
- Token / cost notes are qualitative unless the host Runtime provides exact metering.
- Model and reasoning candidates are not automatic selectors.
- Verification cost is necessary quality cost; missing evidence must remain visible.
- Private project facts, secrets, local absolute paths, and raw chat history must not be written into public records.
- When `e2e_package.applies` is true, the decision record must show how memory, Capability Inventory, Context Budget, topology, Runtime Skill-aware packages, verification, and Routing Memory were considered together.
