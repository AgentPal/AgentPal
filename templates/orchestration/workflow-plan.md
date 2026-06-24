# Workflow Plan Template

This template describes a planned workflow. In AgentPal v0.1.0-rc.1, only Fast Route, Single Owner, and Task Package are active. Other topologies are future design unless the user manually asks for a written plan.

```yaml
schema: agentpal.workflow-plan.v0.1
workflow_id:
created_at:
task_goal:
domain_focus:
deliverables:
  content_deliverables: []
  final_deliverables: []
topology:
  selected:
  status: active-v0.1 | future-design-only | manual-plan-only
  reason:
owner:
  pal_id:
  output_contract:
overall_conductor:
  default: Mira
  current_conductor:
  note:
steps:
  - step_id:
    stage_id:
    stage_goal:
    capability_needs: []
    recipient_type: pal | runtime | skill | plugin | mcp | verifier | team-leader-summary
    recipient_id:
    recipient_candidate:
      id:
      why_candidate:
      not_a_fixed_route: true
    task:
    input_summary:
    context_access_list:
    output_expected:
    verification_required: false
stage_policy:
  candidates_are_not_routes: true
  fixed_keyword_routes_allowed: false
  v0_1_staged_task_package_only: true
isolation:
  independent_judgement: false
  drafts_hidden_until_summary: true
verification:
  evidence_required:
  failure_conditions:
routing_memory:
  write_candidate: false
  privacy_review_required: true
do_not_do:
```
