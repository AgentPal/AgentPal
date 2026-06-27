# Conductor Decision Record

Use this record to explain why a Deep Conductor or Project Conductor plan chose its topology, Pal candidates, Runtime candidates, Skill candidates, context budget, and verification plan.

```yaml
schema: agentpal.conductor_decision_record.v0.1
record_id: ""
created_at: ""
user_goal_summary: ""
project_or_single_task: ""
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
  context_read_count: 0
  profile_read_count: 0
  memory_used: false
  budget_reason: ""
memory_basis:
  - source: ""
    lesson: ""
    not_a_fixed_route: true
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
- Private project facts, secrets, local absolute paths, and raw chat history must not be written into public records.
